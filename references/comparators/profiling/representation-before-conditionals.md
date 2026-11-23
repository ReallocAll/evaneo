<!-- retrieval: {"source_ids":["public:comparator-source:profiling:L01","public:comparator-source:profiling:L02"],"source_type":"public","date":"2026-10-20","topics":["profiling","design","validation"],"limitations":"External comparator at pinned samples; transfer guidance is independent analysis. No upstream or target implementation runtime tests were executed."} -->
# Remove exceptional states in the model, then count the real costs {#case}
## Context and actual choice {#section-01}

Linux v6.17 uses a circular intrusive doubly linked list: the head has the same link structure as the embedded nodes, and an empty head links to itself. The documentation explicitly explains that embedding links lets generic operations work with different payload types. It also cautions that linked lists often lose to simple arrays because of poor locality. [L01: rationale and caution](https://github.com/torvalds/linux/blob/e5f0a698b34ed76002dc5cff3804a61c80233a7a/Documentation/core-api/list.rst#L14-L70)

The corresponding code initializes the head, inserts between two adjacent links, and removes an entry by reconnecting its neighbors. Ordinary deletion poisons the removed node's links; `list_del_init` instead restores a self-linked state. Hardening checks can validate adjacency. The implementation therefore distinguishes a removed-invalid node from a reinitialized reusable node rather than pretending they have identical semantics. [L02: initialization and operations](https://github.com/torvalds/linux/blob/e5f0a698b34ed76002dc5cff3804a61c80233a7a/include/linux/list.h#L23-L232), [reinitialization](https://github.com/torvalds/linux/blob/e5f0a698b34ed76002dc5cff3804a61c80233a7a/include/linux/list.h#L282-L289)

**Evidence quality:** the payload-generic rationale and locality warning are explicitly documented; the reduction in endpoint-specific mutation logic follows from the inspected representation.

## What actually becomes simpler {#section-02}

The following is analysis of that invariant:

With a null-terminated representation, deleting a known node may require separate head and tail repair. With a permanent circular head, the first payload node's predecessor and the last payload node's successor are ordinary link objects. The same neighbor-reconnection relation applies to first, middle, and last payload nodes, including the only payload node. The structure absorbs those endpoint cases.

This does not remove the distinction between payload and head during traversal. Nor does it grant permission to delete the head, use an uninitialized node, insert a node twice, or free an object still visible to another reader. A shorter mutation primitive is valuable because its preconditions are clearer, not because every conditional is undesirable.

## Alternatives and tradeoffs {#section-03}

These comparisons are our recommendations, not upstream performance claims:

- **Contiguous array/vector:** often the lowest-maintenance baseline for append, batch processing, and traversal. Erasing or moving elements can invalidate references or cost linear work.
- **Null-ended linked structure:** familiar and sufficient for many small structures; explicit endpoint cases may be clearer than introducing an intrusive abstraction.
- **Circular intrusive structure:** useful when stable object identity and frequent known-node insertion/removal justify it. It adds link storage, lifetime coupling, and invariants about membership and movement.
- **Wrapper/generic container framework:** may standardize repeated real needs, but can merely move complexity into templates, allocators, and adapters. One local use is weak evidence that a reusable framework is required.

Circularity does not improve cache locality, and an intrusive node is not an owning pointer. Copying or moving self-referential objects deserves explicit semantics. Kernel synchronization and compiler conventions are also not a license to paste the header into portable C++.

## Applying the lesson to Spark {#section-04}

The target is not “replace Spark queues or trees with Linux lists.” It is **find a representation that states the actual invariant once**.

Original design questions motivated by [Spark: profiler lifecycle](../../sources/commit-review/plugin-api-evolution/cases/spark-profiler-lifecycle.md) and [Spark: measurement and export](../../sources/commit-review/plugin-api-evolution/cases/spark-measurement-and-export.md):

1. **Run ownership:** could all state whose meaning starts at capture start live in one per-run object? This may eliminate reset omissions more reliably than adding another list of fields to clear. Persistent plugin services can remain outside it.
2. **Metric meaning:** could a value carry availability/provenance explicitly, so a failed `/proc` read is not accidentally indistinguishable from a measured zero? Do not add wrappers everywhere; apply them at the boundary where that ambiguity affects consumers.
3. **Tick completeness:** could one tick record retain both duration and pending samples until the contract says it is complete? A single mixed event queue is not automatically a solution: independent producers can enqueue in an order different from event time. Completion still needs a producer acknowledgement, watermark, or another justified ordering rule.
4. **Export intent:** could the run own an explicit effective destination mode, rather than resolving potentially different start/stop flags through scattered defaults? Keep the user's chosen local/remote behavior visible at the boundary that performs delivery.

These are candidates to compare, not a prescribed Spark rewrite. A small explicit check is preferable when it expresses a genuine external difference, such as unsupported Windows functionality or a viewer compatibility rule. Hiding such differences behind a uniform interface can make the model less truthful.

## Benefits, costs, and failure boundaries {#section-05}

Better representation can reduce the number of states every caller must remember, and concentrate validation at construction/transition boundaries. Its cost is migration work and learning a new invariant. Require the proposal to name which invalid state becomes unrepresentable or which repeated proof becomes local.

If all that changes is fewer lines, more indirection, or an impressive template signature, the benefit has not been established. Do not delete compatibility handling merely because it looks ugly; first separate required external semantics from accidental internal state.

## Verification implications {#section-06}

Unexecuted specifications:

- Exercise empty, singleton, first/middle/last removal, clear, and reuse against a simple reference sequence. Compare contents and order after every operation; “it traversed” is insufficient.
- For any intrusive or pointer-stable proposal, test the declared copy/move policy and invalid membership operations. Reject a mutant that leaves the old object's address in a copied head.
- For a per-run redesign, generate two runs with overlapping window numbers but distinct run IDs; reject any merge across them.
- For metric availability, send measured zero, measured nonzero, unavailable, and malformed input through export. Reject an implementation that collapses all four into a numeric default.
- For tick ordering, deliberately reverse arrival of closure and a same-tick sample. Verify the chosen completeness contract, not an assumption that a different queue topology magically creates time order.

A design claim must survive its counterexamples. The smallest design is the one with the smallest complete proof under the real constraints, not necessarily the fewest branches.

## Applicability and review limits {#review-limits}

This is a supporting design example. Suggested tests remain unexecuted.

Applicability: A repeated special state might be removed by a clearer representation

- Supporting design example only; not a recommendation to replace Spark structures with Linux lists.
- Fewer conditionals alone does not establish lower maintenance cost.
