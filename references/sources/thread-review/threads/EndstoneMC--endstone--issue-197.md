<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:197"],"source_type":"public","date":"2025-06-14","topics":["concurrency","api","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-197-bug-playerjoinevent-delayed"></a>
# EndstoneMC/endstone #197: [bug] PlayerJoinEvent delayed {#endstonemc-endstone-197-bug-playerjoinevent-delayed}

Source: https://github.com/EndstoneMC/endstone/issues/197

## Review scope and state {#review-scope-and-state}

- Thread author: DayOfMagic; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

DayOfMagic dislikes seeing the old spawn location briefly before a PlayerJoinEvent teleport. Wu explains the deliberate timing tradeoff: earlier join callbacks preceded client readiness, so forms silently failed and ability changes could prevent block breaking (106). Moving join later makes player-side API behavior reliable at the cost of a visible initial location. Reporter continues to find the visual effect undesirable; no alternative pre-spawn API is promised. This is a lifecycle/API-readiness choice with a documented UX cost, not a dismissed reproducibility problem.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/197
- https://github.com/EndstoneMC/endstone/issues/197#issuecomment-2993562642
- https://github.com/EndstoneMC/endstone/issues/197#issuecomment-2993604396
