<!-- retrieval: {"source_ids":["public:comparator-source:profiling:T01","public:comparator-source:profiling:T02"],"source_type":"public","date":"2026-10-20","topics":["profiling","design","validation"],"limitations":"External comparator at pinned samples; transfer guidance is independent analysis. No upstream or target implementation runtime tests were executed."} -->
<a id="case"></a>
# Shutdown is a delivery and ownership contract {#case}
## Context and actual choice {#section-01}

Tracy v0.11.1 exposes a deliberate short-lived-program mode: `TRACY_NO_EXIT` can keep a finished application alive until a profiler connection arrives. Its default non-on-demand recording retains events before connection; the manual warns about substantial memory growth. On-demand mode changes collection timing and adds bookkeeping costs. For multi-library integration, delayed initialization and manual lifetime functions let an integrator choose initialization/destruction points. The manual separately warns that profiling inside unloaded modules requires respecting data lifetime, and that calling `exit()` inside an unfinished zone can leave termination waiting for the zone. [T01: lifetime and collection policy](https://github.com/wolfpld/tracy/blob/5d542dc09f3d9378d005092a4ad446bd405f819a/manual/tracy.tex#L519-L573), [data lifetime](https://github.com/wolfpld/tracy/blob/5d542dc09f3d9378d005092a4ad446bd405f819a/manual/tracy.tex#L1005-L1023), [zone exit](https://github.com/wolfpld/tracy/blob/5d542dc09f3d9378d005092a4ad446bd405f819a/manual/tracy.tex#L1394-L1398)

The pinned client code checks shutdown while waiting for a connection unless no-exit behavior is selected. Its connected termination path drains queues, sends termination, and continues servicing remaining queries. This is a multi-phase protocol; the inspected loop does not establish a global finite shutdown deadline. The explicit startup/shutdown functions manage profiler data lifetime. [T02: connection policy](https://github.com/wolfpld/tracy/blob/5d542dc09f3d9378d005092a4ad446bd405f819a/public/client/TracyProfiler.cpp#L1790-L1812), [drain/query phase](https://github.com/wolfpld/tracy/blob/5d542dc09f3d9378d005092a4ad446bd405f819a/public/client/TracyProfiler.cpp#L2047-L2133), [manual lifetime](https://github.com/wolfpld/tracy/blob/5d542dc09f3d9378d005092a4ad446bd405f819a/public/client/TracyProfiler.cpp#L1192-L1223)

**Evidence quality:** the short-lived-capture purpose and warnings are explicit upstream documentation. The absence of a global deadline is bounded source inspection, not proof of every Tracy exit path or a reproduced hang. This case is a tradeoff example, not an allegation that Tracy should satisfy an unrelated plugin contract.

## Alternatives and rationale {#section-02}

Tracy's documented no-exit mode prioritizes obtaining evidence from a program that might finish before the collector attaches. The option is sensible for an explicitly controlled diagnostic run. A long-running host unloading one plugin has a different priority: the profiler must not hold the host's lifecycle hostage to a remote endpoint.

The following options and recommendations are **our analysis**:

- **Wait for delivery:** offers the strongest opportunity to preserve data while the peer cooperates, but the peer and network can control latency.
- **Discard on stop:** minimizes delivery work, but must communicate that the result was abandoned; it still requires capture workers to stop safely.
- **Snapshot locally, export separately:** separates acquisition lifetime from delivery and may allow retry; it costs storage, an owned artifact, and explicit retention/privacy policy.
- **Finite best-effort delivery:** bounds waiting only if all underlying blocking operations and callbacks participate in cancellation/deadline handling. A timeout around a join is not a safe implementation.

Do not add all four modes preemptively. First state which one the application actually needs, then implement the smallest lifecycle that can satisfy it.

## Applying this to Spark {#section-03}

[Spark: profiler lifecycle](../../sources/commit-review/plugin-api-evolution/cases/spark-profiler-lifecycle.md) identifies two distinct local concerns: a capture timeout does not acknowledge completion by a handler that already acquired a buffer, and plugin disable joins an export thread whose network operation has no timeout. Tracy does not validate Spark's signal protocol; it helps frame the choices that protocol and export must expose.

Before coding, write these ownership obligations:

1. **Close admission:** identify who can still create samples, tick events, callbacks, and export jobs. Define when each producer observes closure.
2. **Establish quiescence:** identify the acknowledgement that no capture handler or worker can still touch run-owned memory. A cancellation flag, cleared pointer, or generation number alone is not that acknowledgement. Generation numbers can reject stale completions; they cannot make freed memory safe for a late writer.
3. **Resolve accepted work:** drain or discard under the declared policy, producing a terminal status. “Stop requested” and “stopped safely” must not be aliases.
4. **Release owners:** remove callbacks and free memory only when their possible executors no longer depend on them. If asynchronous delivery is retained, it needs ownership independent of the unloaded plugin and a callback policy that cannot jump into unloaded code.
5. **Start afresh:** a subsequent run receives fresh state or a completely specified reset. Do not let run identity leak through persistent call-tree or timestamp storage.

The sequence is a design obligation, not a claim that five new classes or a generic state-machine framework are necessary. One run object and a small explicit state enum may be enough; existing host facilities may remove some phases entirely.

## Benefits, costs, and failure boundaries {#section-04}

Explicit lifecycle phases make it possible to reason about stop/restart, partial export, and cleanup after initialization failure. They also expose the uncomfortable case: if a platform cannot establish quiescence within a desired time, immediate unload and safe reclamation cannot both be promised. The correct response is a supported host policy or a different capture mechanism, not detaching a writer and freeing its state.

A local artifact can decouple export from capture but must not be silently created, uploaded, or retained outside the operator's chosen mode. A network timeout should include connect, transfer, subprocess, and callback hops relevant to the actual implementation. Adding a timeout only to the outermost operation leaves hidden waits intact.

## Verification implications {#section-05}

Unexecuted specifications, using deterministic gates rather than random sleeps where possible:

- **Late capture:** pause a handler immediately after it acquires the buffer, request stop, then resume it. Verify reclamation occurs only after the permitted writer finishes. Reject clearing the global pointer as sufficient cancellation.
- **Stop during blocked export:** hold the fake exporter indefinitely. Verify the documented terminal status and deadline policy without requiring network access. Reject a worker detach that merely lets disable return while retaining plugin pointers.
- **Callback after disable:** queue completion, disable the plugin before dispatch, then dispatch under a controlled scheduler. Verify no plugin-owned callback executes after its lifetime ends.
- **Partial startup:** fail each resource acquisition in turn and check exactly-once cleanup and safe retry. Include acquisition of process-global facilities where applicable.
- **Run A then B:** give the runs disjoint frame/tick IDs. B's counters, windows, configuration, and tree must contain only B's data.

Real operating-system signal, unwind, and unload tests remain necessary. A stub proves the intended state machine, not its low-level implementation.

## Applicability and review limits {#review-limits}

This is a conditional problem match. Suggested tests remain unexecuted.

Applicability: Stop/unload and export have a declared ownership and delivery contract

- No global-deadline proof was established for all Tracy paths.
- Manual lifetime functions do not by themselves protect module string literals, callbacks or code.
- Generation numbers or cleared pointers are not late-writer reclamation proofs.
