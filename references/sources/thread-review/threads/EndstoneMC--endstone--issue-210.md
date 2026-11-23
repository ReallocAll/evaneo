<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:210"],"source_type":"public","date":"2025-06-29","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-210-feature-itemuse-event"></a>
# EndstoneMC/endstone #210: [feature] ItemUse Event {#endstonemc-endstone-210-feature-itemuse-event}

Source: https://github.com/EndstoneMC/endstone/issues/210

## Review scope and state {#review-scope-and-state}

- Thread author: DayOfMagic; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

DayOfMagic wants non-consumable item-use callbacks for menus/tools, distinguishing them from PlayerItemConsumeEvent. Wu points to b38fb6684cb1f0fa5a4276e8ad8a9c3be6c521ad and the next release. Full linked patch inspected: ItemUseEvent converts ItemInstance to ItemStack and emits PlayerInteractEvent with RightClickAir, null block, no clicked position, and an existing player wrapper; cancellation returns BypassListeners/Cancel. The block path now explicitly uses RightClickBlock. The solution extends an existing interaction event rather than adding a separate public item-use class. Consumers must branch on action before assuming block/position exists; no guarantee that every arbitrary client gesture creates native ItemUseEvent is established.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/210
- https://github.com/EndstoneMC/endstone/issues/210#issuecomment-3039354189
- https://github.com/EndstoneMC/endstone/commit/b38fb6684cb1f0fa5a4276e8ad8a9c3be6c521ad
