<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:543"],"source_type":"public","date":"2026-10-06","topics":["lifetime","concurrency","testing","performance","recovery","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-543-perf-python-reuse-the-primary-thread-state"></a>
# EndstoneMC/endstone #543: perf(python): reuse the primary thread state {#endstonemc-endstone-543-perf-python-reuse-the-primary-thread-state}

Source: https://github.com/EndstoneMC/endstone/pull/543

## Evidence and attribution {#evidence-and-attribution}

Primary author: ReallocAll. Created 2026-10-06T10:36:44Z; recorded state closed; merged True.

## Persistent Python state: benchmark and test claims were corrected {#persistent-python-state-benchmark-and-test-claims-were-corrected}
ReallocAll uses nested long-lived gil_scoped_acquire then gil_scoped_release on the server thread: the GIL remains released between callbacks, while the thread state remains alive. Reverse destruction restores GIL before releasing the state; server/plugin Python-facing objects die first, interpreter later. Worker threads unchanged. PyTorch is cited as lifetime precedent.
Live Spark captures across different loads show old lifecycle/syscall hotspots disappear, but do not measure aggregate A/B MSPT. Wu explicitly refuses that causal comparison and benchmarks alternating20k no-op callbacks×7 rounds on one worker: Windows2.4µs→66ns, Linux5.3–5.9µs→~60ns. Linux2,000 calls reduce mmap2056→57, munmap2007→8, affinity2001→2. Same-world DLL-swap2000-callback batches give5.5/8.7ms baseline→0.21ms, one persistent state and999/999 thread-local survival. Native start/stop callbacks were verified on the same thread.
A critical test failure: deleting the proposed RAII members still passes pointer-equality reuse tests because the allocator recycles addresses. Between-callback PyGILState_GetThisThreadState or threading.local survival tests identify the mechanism. Persistence is observably semantic: threading.local/contextvars no longer reset per callback. Wu's bfb6efe replaces wrapper class/header with two optional guards directly on lifecycle listener, removes test files/embed linkage, folds changelog and reports live shutdown/reuse checks still pass. No-wrapper means no bespoke unit tests retained; preserve that coverage tradeoff instead of quoting initial test list as final suite.

## Direct patch findings {#direct-patch-findings}

Final bfb6efe diff has optional acquire/release members on lifecycle listener, emplaces acquire then release, disables plugins/resets server before release.reset then acquire.reset, and documents thread-local/context persistence. No test files or wrapper remain.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (2198 characters; SHA-256 992ca6585a9bbef4ec85b677e66311f9e9b121e19291efb35f6c82847b01c95e), head bfb6efee62276426d129e36c22ec286f8542c0a6. This covers the supplied PR patch, not unrelated commits or historical intermediate revisions. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/543
- https://github.com/EndstoneMC/endstone/pull/543#issuecomment-6019240987
- https://github.com/EndstoneMC/endstone/pull/543#issuecomment-6019522675
