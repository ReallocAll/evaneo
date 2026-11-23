<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:96"],"source_type":"public","date":"2024-11-28","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-96-second-name-for-player"></a>
# EndstoneMC/endstone #96: second name for player {#endstonemc-endstone-96-second-name-for-player}

Source: https://github.com/EndstoneMC/endstone/issues/96

## Review scope and state {#review-scope-and-state}

- Thread author: Mih4n; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Mih4n distinguishes immutable player name from mutable display name tag. Wu links d3979e1b4f143c634277380743b4683eb6e32889 and Actor.name_tag as completion. This reuses the actor-level property rather than a separate player identity; no implementation or persistence semantics are supplied in the thread.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/96
- https://github.com/EndstoneMC/endstone/issues/96#issuecomment-2558709805
- https://github.com/EndstoneMC/endstone/commit/d3979e1b4f143c634277380743b4683eb6e32889
