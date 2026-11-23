<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:182"],"source_type":"public","date":"2025-05-18","topics":["lifetime","concurrency","testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-182-bug-crash-when-retrieving-offline-player-objects"></a>
# EndstoneMC/endstone #182: [bug] Crash when retrieving offline player objects {#endstonemc-endstone-182-bug-crash-when-retrieving-offline-player-objects}

Source: https://github.com/EndstoneMC/endstone/issues/182

## Review scope and state {#review-scope-and-state}

- Thread author: pgrd1; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

pgrd1 caches an online Player wrapper and calls methods after disconnect. Wu explains that Python bindings do not extend the native C++ player's lifetime: retain uuid/name and reacquire, or check is_valid before using a stored reference. Reporter accepts. A follow-up about get_player for a nonexistent name is separate; Wu says tests exist and believes the prior temporary stop is no longer an issue, without linking or running those tests. Thus lifetime guidance is firm historical API advice while the missing-player fix remains a qualified maintainer belief. A check is not a general concurrency lifetime guarantee; use must still respect server-thread/lifecycle boundaries.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/182
- https://github.com/EndstoneMC/endstone/issues/182#issuecomment-2889044915
- https://github.com/EndstoneMC/endstone/issues/182#issuecomment-2889046671
- https://github.com/EndstoneMC/endstone/issues/182#issuecomment-2889050090
- https://github.com/EndstoneMC/endstone/issues/182#issuecomment-2889051472
- https://github.com/EndstoneMC/endstone/issues/182#issuecomment-2889052024
