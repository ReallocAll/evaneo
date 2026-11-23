<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:242"],"source_type":"public","date":"2025-08-08","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-242-bug-inventory-setitem-does-not-update-the-client-properly"></a>
# EndstoneMC/endstone #242: [bug] Inventory.setItem does not update the client properly. {#endstonemc-endstone-242-bug-inventory-setitem-does-not-update-the-client-properly}

Source: https://github.com/EndstoneMC/endstone/issues/242

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat proposes batched update_inventory after metadata changes. Wu initially says inventory.set_item should update a slot; the reporter provides the full get-meta/add-enchant/set-meta/set-slot sequence, disproving the assumption that set_item was omitted. Wu agrees immediate visibility is intended and links a test build, without a reporter validation. Later 248 identifies immovable newly created stacks as a regression from this fix and reopens 242, so the attempted client-sync repair is not an uncomplicated success. Explicit batch-flush API remains only the reporter's proposal.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/242
- https://github.com/EndstoneMC/endstone/issues/242#issuecomment-3169020008
- https://github.com/EndstoneMC/endstone/issues/242#issuecomment-3169052573
- https://github.com/EndstoneMC/endstone/issues/242#issuecomment-3169056214
- https://github.com/EndstoneMC/endstone/issues/242#issuecomment-3176964863
