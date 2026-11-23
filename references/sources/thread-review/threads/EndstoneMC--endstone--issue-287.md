<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:287"],"source_type":"public","date":"2025-10-29","topics":["concurrency","testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-287-bug-crash-when-using-status"></a>
# EndstoneMC/endstone #287: [bug] Crash when using /status {#endstonemc-endstone-287-bug-crash-when-using-status}

Source: https://github.com/EndstoneMC/endstone/issues/287

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat's0.10.8 Windows /status stack faults in EndstoneDimension::getLoadedChunks. Wu promises a hotfix that night, without linked patch or reporter confirmation. The shared method connects it to 289's loaded_chunks regression, but this thread alone supplies only stack localization and a promise, not an implemented fix.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/287
- https://github.com/EndstoneMC/endstone/issues/287#issuecomment-3462650402
