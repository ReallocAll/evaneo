<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:108"],"source_type":"public","date":"2024-12-12","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-108-bug-player-inventory-clear-method-does-not-update-the-inventory-on-client-side-instantly"></a>
# EndstoneMC/endstone #108: [bug] Player inventory clear() method does not update the Inventory on client side instantly {#endstonemc-endstone-108-bug-player-inventory-clear-method-does-not-update-the-inventory-on-client-side-instantly}

Source: https://github.com/EndstoneMC/endstone/issues/108

## Review scope and state {#review-scope-and-state}

- Thread author: AcquaticLegend; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

AcquaticLegend reports clear() changes inventory server-side but client display updates only after interaction; setting slot 0 to air triggers the expected refresh. Wu confirms a bug and says recent commits fix it for the next release. This distinguishes data mutation from client synchronization. No exact commit is given, so the mechanism or client refresh packet cannot be asserted.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/108
- https://github.com/EndstoneMC/endstone/issues/108#issuecomment-2546005387
