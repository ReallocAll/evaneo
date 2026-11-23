<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:248"],"source_type":"public","date":"2025-08-17","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-248-bug-itemstack-constructor-prevents-items-from-being-moved-within-the-inventory"></a>
# EndstoneMC/endstone #248: [bug] ItemStack constructor prevents items from being moved within the inventory {#endstonemc-endstone-248-bug-itemstack-constructor-prevents-items-from-being-moved-within-the-inventory}

Source: https://github.com/EndstoneMC/endstone/issues/248

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat bundles three ItemStack defects: new stacks cannot move in hotbar/main inventory, aux data produces water rather than the intended potion, and setting amount deletes an existing stack. Wu links two fixes, then deliberately reopens because movement is still unresolved; later attributes movement to 242's sync fix and reopens that issue. Full patches inspected: ffe337efbf0b8df886fb1f0b667d13102e2ea384 preserves getData in native stack conversion; c8392d2a45fb2e087c583760bf1470c0805e76ed changes an inverted setNull condition from !isNull to !*this. Neither patch addresses movement synchronization. Reporter celebration is not evidence that all three were fixed; the correction is essential.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/248
- https://github.com/EndstoneMC/endstone/issues/248#issuecomment-3197481424
- https://github.com/EndstoneMC/endstone/issues/248#issuecomment-3202355555
- https://github.com/EndstoneMC/endstone/issues/248#issuecomment-3227693636
- https://github.com/EndstoneMC/endstone/issues/248#issuecomment-3228074824
- https://github.com/EndstoneMC/endstone/issues/248#issuecomment-3228105161
- https://github.com/EndstoneMC/endstone/issues/248#issuecomment-3228117635
- https://github.com/EndstoneMC/endstone/issues/248#issuecomment-3228122230
- https://github.com/EndstoneMC/endstone/issues/248#issuecomment-3263968992
- https://github.com/EndstoneMC/endstone/commit/ffe337efbf0b8df886fb1f0b667d13102e2ea384
- https://github.com/EndstoneMC/endstone/commit/c8392d2a45fb2e087c583760bf1470c0805e76ed
