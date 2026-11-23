<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:59"],"source_type":"public","date":"2024-09-22","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-59-bug-event-block-type-conversion-error-in-blockplaceevent"></a>
# EndstoneMC/endstone #59: [bug] event.block.type conversion error in blockplaceevent {#endstonemc-endstone-59-bug-event-block-type-conversion-error-in-blockplaceevent}

Source: https://github.com/EndstoneMC/endstone/issues/59

## Review scope and state {#review-scope-and-state}

- Thread author: pgrd1; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

pgrd1 expects BlockPlaceEvent.block.type to identify the new block but observes air. Wu explains the event occurs before placement: block denotes the existing block being replaced, while block_placed_state denotes the proposed future state, applied only if not cancelled. This is a temporal API contract: a not-yet-existing world object cannot be returned as an already placed instance. The distinction supports explicit before/current/proposed state modeling.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/59
- https://github.com/EndstoneMC/endstone/issues/59#issuecomment-2366860097
