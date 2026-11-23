<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2026-07-26","topics":["testing","maintainability","complexity","review","concurrency","lifetime","counterexample"],"limitations":"Static review of linked primary sources and bundled historical analyses; upstream tests were not executed. Historical claims and code changes are distinguished from proven runtime outcomes."} -->
# Endstone #436: real async unload risks justify a dedicated regression suite {#case}

## Necessity rather than minimalism {#changes}

In [PR #436](https://github.com/EndstoneMC/endstone/pull/436), initially authored by ReallocAll and revised by maintainer wu-vincent, queued/running asynchronous scheduler callbacks could outlive a C++ plugin's loaded module. The PR revised draining before unload, cancellation cleanup, worker-thread scheduling and executor enqueue failures. Its final diff comprised 13 paths, **+334/−38 lines**, including new `test_scheduler.cpp` and `test_thread_pool_executor.cpp` regression coverage. Review identified real failure paths, including exceptions escaping a tick loop or being silently swallowed.

## Counterexample to 'fewer tests' {#reading}

Removing these tests solely to reduce code volume would leave high-risk ownership and concurrency contracts unprotected. When the failure can crash a process or execute callbacks after unloading code, a focused deterministic test with explicit scheduling or lifecycle barriers is justified even if it requires more setup than an ordinary function test. Integration checks remain necessary where a real module unload boundary cannot be simulated faithfully.

## Limit {#limits}

The PR includes many revisions and did not monotonically shrink. This is **not** a positive example of line-count reduction; it is a necessary-complexity counterexample. Passing the added tests is a submitter/PR claim, not independent execution here.
