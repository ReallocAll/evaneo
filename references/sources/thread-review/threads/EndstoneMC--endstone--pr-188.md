<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:188"],"source_type":"public","date":"2025-05-24","topics":["ffi","testing","documentation","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-188-feat-add-playeritemconsumeevent"></a>
# EndstoneMC/endstone #188: feat: add PlayerItemConsumeEvent {#endstonemc-endstone-188-feat-add-playeritemconsumeevent}

Source: https://github.com/EndstoneMC/endstone/pull/188

## Review scope and state {#review-scope-and-state}

- Thread author: killcerr; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (522 additions, 130 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

killcerr authors this merged 39-file PR. Wu's four inline notes ask for ItemStack references instead of nullable pointers, correct a Windows completeUsingItem address, and reuse getEndstoneActor rather than constructing a fresh player wrapper. All four review bodies and inline contexts were read. These support nullability, offset accuracy and wrapper-identity concerns; further motivation is not invented. The final code differs from the early food/name-filter proposal, as detailed below.

### Complete patch inspection {#complete-patch-inspection}

Final code adopts the non-null reference constructor/storage, uses getEndstoneActor to preserve the existing player wrapper, and includes corrected completeUsingItem symbols for both platforms. Unlike the early inline proposal, the final hook does not filter a named food/potion/milk list: it observes every native completeUsingItem invocation. It derives hand from the selected inventory container, converts the current native item to an Endstone snapshot, dispatches synchronously, then either clears USINGITEM and both item-use components on cancellation or calls the original native method. Its observable coverage and off-hand identification require native runtime validation; the callback name alone is not proof that every consumable path reaches it.

The event exposes only a cloned ItemStack getter and a hand getter. It has no setItem. Consequently comments promising changed-item effects and documentation saying get-or-set are ahead of implementation; mutating the returned clone cannot replace the consumed item. The reference member points to a local snapshot alive through synchronous dispatch, so retaining the event beyond that scope is unsupported. ItemStack gains copy/clone semantics, and the native wrapper overrides clone to preserve its handle/metadata instead of slicing it.

Supporting changes move item-use duration into an ECS component, add component removal and a trident movement marker, and support WeakPtr conversion via shared control-block reinterpretation without a type constraint. This general conversion is broader than the immediate const-item use and should not be treated as a universally safe pointer cast. There are also unrelated documentation/import reorders and scoreboard integer parsing switched to from_chars; it checks error code but not full input consumption, retaining acceptance of numeric prefixes. ItemStackBase::set is largely relocated with its existing nulling logic, not a newly demonstrated inventory fix. No new tests are included.

Exact inspected base/head: 09680b318cdd675aeeaf05bafae617c30d88b30b…f0a60dc3bc48256449ff72e38ea8c12a9062f754. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/188
- https://github.com/EndstoneMC/endstone/pull/188#discussion_r2105860832
- https://github.com/EndstoneMC/endstone/pull/188#discussion_r2105860856
- https://github.com/EndstoneMC/endstone/pull/188#discussion_r2105860903
- https://github.com/EndstoneMC/endstone/pull/188#discussion_r2105861479
- https://github.com/EndstoneMC/endstone/pull/188#pullrequestreview-2866363186
- https://github.com/EndstoneMC/endstone/pull/188#pullrequestreview-2866363203
- https://github.com/EndstoneMC/endstone/pull/188#pullrequestreview-2866363264
- https://github.com/EndstoneMC/endstone/pull/188#pullrequestreview-2866363812
