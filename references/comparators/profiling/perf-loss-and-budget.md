<!-- retrieval: {"source_ids":["public:comparator-source:profiling:P01","public:comparator-source:profiling:P03","public:comparator-source:profiling:P02"],"source_type":"public","date":"2026-10-20","topics":["profiling","design","validation"],"limitations":"External comparator at pinned samples; transfer guidance is independent analysis. No upstream or target implementation runtime tests were executed."} -->
<a id="case"></a>
# A profiler's missing data and observer cost are part of its result {#case}
## Context and actual choice {#section-01}

Linux perf moves event data from kernel producers to a userspace consumer. Its v6.17 documentation describes two distinct contracts: forward non-overwrite buffers preserve unread records and report losses when later space permits; backward overwrite buffers retain newer data and do not emit the same loss records. The documented head/tail protocol also requires publication and consumption ordering. These are operational contracts, not interchangeable ring-buffer variants. [P01: pinned documentation](https://github.com/torvalds/linux/blob/e5f0a698b34ed76002dc5cff3804a61c80233a7a/Documentation/userspace-api/perf_ring_buffer.rst#L438-L585)

In the corresponding producer code, insufficient non-overwrite space increments both a pending loss count and an event counter, then returns an error. A later reservation includes room for the pending loss record before exchanging that count to zero. Separately, `perf_sample_event_took` uses a decaying history of sample-handler duration and reduces the configured sample-rate ceiling when its allowed-duration threshold is exceeded. The code includes the reason in its diagnostic: sampling interrupts have taken too long. [P02: loss path](https://github.com/torvalds/linux/blob/e5f0a698b34ed76002dc5cff3804a61c80233a7a/kernel/events/ring_buffer.c#L152-L270), [P03: duration control](https://github.com/torvalds/linux/blob/e5f0a698b34ed76002dc5cff3804a61c80233a7a/kernel/events/core.c#L600-L664)

**Evidence boundary:** these are directly inspected implementations and documented semantics. They do not prove a particular deployment's actual loss, overhead, or statistical bias. The report does not claim a public historical review established every original design motive.

## Alternatives and why this choice matters {#section-02}

The following comparison is engineering analysis, not a quotation of perf's authors:

- **Unbounded backlog:** avoids an immediate full-buffer decision but transfers the failure to memory use and teardown time. It cannot promise finite memory when production persistently outruns consumption.
- **Block the producer:** can preserve delivery in ordinary worker pipelines. In a sampling path it risks perturbing precisely the thread being measured, and may be impossible in interrupt/signal contexts.
- **Drop new records:** caps resource use and preserves the existing prefix; the missing tail must be visible to readers.
- **Overwrite old records:** serves a recent-history/flight-recorder objective; it destroys earlier evidence, which is a different product contract.

Perf's actual choices make these tradeoffs explicit. The transferable principle is to choose a loss policy from the diagnostic question before optimizing queue internals. A rate ceiling limits some sampling work; it is not a whole-application overhead guarantee. Export, unwinding, symbolization, and contention may have different costs.

## Applying this to Spark without importing perf's implementation {#section-03}

The existing [Spark: profiler lifecycle](../../sources/commit-review/plugin-api-evolution/cases/spark-profiler-lifecycle.md) describes signal-based single-thread capture and separate aggregation. [Spark: measurement and export](../../sources/commit-review/plugin-api-evolution/cases/spark-measurement-and-export.md) identifies configured-interval time estimates without separately exported capture failures. Those observations motivate the following **proposals**, not verified Spark behavior changes:

1. Define separate concepts for requested cadence, actual attempt times, completed captures, rejected/failed attempts, queue admission, and intentional filtering. A truncated stack can still be an admitted sample, so do not force every diagnostic into one misleading sum.
2. For a terminal run, make accounting identities explicit where the categories really are disjoint. For example, captures offered to a queue equal admitted plus rejected, if there is no third outcome; admitted captures equal consumed plus explicitly discarded at termination, after pending work is resolved. These equations do not estimate unobserved scheduled opportunities.
3. Publish the final loss/quality summary independently of a queue that might be permanently full. A loss marker that can only be queued later cannot alone guarantee a truthful final report after abrupt termination.
4. Retain timestamps and the statistical meaning of any count-to-time conversion. A narrow counter makes missing evidence visible; it does not reconstruct missing stacks or remove workload-correlated bias.
5. Prefer an existing, suitable queue with documented ownership and memory ordering. Kernel `READ_ONCE` and barriers are not drop-in ISO C++ atomics. Signal-safety, producer count, and reclamation constraints must match the chosen abstraction.

An external perf-backed capture mode could be worth evaluating on supported Linux deployments; it is not automatically simpler for a cross-platform, unloadable, in-process plugin. Permissions, target-thread identity, native stack recovery, packaging, and operating-system parity remain separate acceptance questions.

## Benefits, costs, and failure boundaries {#section-04}

A bounded queue plus explicit quality counters constrains one resource and prevents a superficially complete report from silently meaning “whatever survived.” Costs include accounting work, exposing uncertainty in the output, and choosing a useful default budget. Avoid atomic counter updates in a signal handler unless their suitability there has been established for the supported platform and implementation.

Finite queue capacity does not bound the call-tree size, intern table, pending tick buckets, symbol cache, or export buffer. Account for those separately. Loss accounting also does not cure stale-buffer writes after a timeout. Do not let measurement improvements substitute for the lifetime proof in the [Tracy lifetime and delivery case](tracy-lifetime-and-delivery.md#case).

## Verification implications: tests that could reject the proposal {#section-05}

These are unexecuted test specifications for a future implementation:

- **Consumer stall:** fill a deliberately tiny queue while consumption is gated. Verify exactly the selected drop/overwrite policy, the admitted/rejected counts, and the memory bound. Reject the mutant that silently drops but reports all attempts as samples.
- **No recovery before stop:** finish with a full queue and pending losses. Verify the final summary still exposes them. Reject the mutant whose only loss report needs another successful enqueue.
- **Cadence distortion:** use a controllable clock/capture stub whose work lasts longer than the requested interval. Verify timestamps and labels reflect the actual attempts; reject blindly reporting requested duration as measured CPU time.
- **Boundary wrap:** exercise capacity minus one, capacity, capacity plus one, and repeated wraparound while preserving unique IDs. Do not treat “no crash” as an ordering oracle.
- **Real overhead experiment:** compare profiler-disabled and profiler-enabled builds under repeated, comparable workloads; record compiler flags, CPU, workload, interval, stack depth, throughput/tick latency, memory, and losses. Evaluate distributions and variance. This is distinct from deterministic stub tests and must be done before claiming low perturbation.

Reuse the mature contract, not an unmeasured performance reputation.

## Applicability and review limits {#review-limits}

This is a conditional problem match. Suggested tests remain unexecuted.

Applicability: A profiler must expose missing evidence and observer cost under a finite resource budget

- Counters cannot reconstruct lost stacks or eliminate sampling bias.
- Kernel memory barriers are not portable C++ atomic recipes.
- No real profiler overhead was measured.
