<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:289"],"source_type":"public","date":"2025-10-30","topics":["concurrency","testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-289-crash-on-iterating-through-loadedchunks"></a>
# EndstoneMC/endstone #289: Crash on iterating through loaded_chunks {#endstonemc-endstone-289-crash-on-iterating-through-loadedchunks}

Source: https://github.com/EndstoneMC/endstone/issues/289

## Review scope and state {#review-scope-and-state}

- Thread author: DayOfMagic; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

DayOfMagic reports loaded_chunks crashes breaking random teleport. Wu asks for 0.10.10 verification and a minimal reproducer; the supplied complex plugin function includes a temporary early return, delayed server tasks, chunk search and async waits, so it is not itself a clean runnable reproduction. The later stack specifically faults in weak_ptr<LevelChunk>::expired under getLoadedChunks during a main-thread scheduler callback and identifies 0.10.8. Wu catches that stale version evidence and requests a matching current crash; reporter then confirms it works. This supports the 0.10.10 resolution for this case while avoiding a false claim that it still crashes in the fixed version or that asyncio alone caused it.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/289
- https://github.com/EndstoneMC/endstone/issues/289#issuecomment-3477934218
- https://github.com/EndstoneMC/endstone/issues/289#issuecomment-3478714349
- https://github.com/EndstoneMC/endstone/issues/289#issuecomment-3479752321
- https://github.com/EndstoneMC/endstone/issues/289#issuecomment-3481411397
- https://github.com/EndstoneMC/endstone/issues/289#issuecomment-3481440057
- https://github.com/EndstoneMC/endstone/issues/289#issuecomment-3481569834
