<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:189"],"source_type":"public","date":"2025-05-26","topics":["lifetime","ffi","testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-189-feat-new-itemtype-api"></a>
# EndstoneMC/endstone #189: [feat] New ItemType API {#endstonemc-endstone-189-feat-new-itemtype-api}

Source: https://github.com/EndstoneMC/endstone/pull/189

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (464 additions, 56 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu proposes an immutable ItemType API, comparing its role with Bukkit Material, and explicitly calls out ItemStack.type changing from a string to an object: use item.type.id for the prior identifier. One Codecov comment and no substantive reviews are captured. The 24-file patch was fully read; usage examples are author-provided examples rather than independent test results.

### Complete patch inspection {#complete-patch-inspection}

ItemType is an immutable-facing view of a native item definition, exposing identifier/key, translation key, maximum stack size and durability. Equality compares identifiers and retains string comparisons as migration convenience. Server creates its item registry when the level is set; native lookup still uses ItemRegistryManager, and ItemType objects retain const references to native definitions. Immutability of the API does not establish lifetime safety across registry reload or availability before level initialization.

ItemStack now holds a reference_wrapper to ItemType, defaulting through lookup of minecraft:air. String constructors resolve names; the checked create factories reject unknown names and amounts outside 1..255. Python construction uses those factories and raises on their Result errors. In contrast, direct C++ construction with an unknown string leaves an air/zero stack, and setAmount remains unchecked. The 1..255 factory limit is a storage bound, not the item's natural maximum stack size. ItemFactory/meta applicability methods migrate from strings to ItemType.

There is a notable overload inconsistency in this exact patch: EndstoneItemStack::setType(string) delegates to ItemStack::setType(string), which changes only the base reference, while its getType reads the native handle. The ItemType overload does replace that handle. Therefore string and object assignment need separate behavior tests. Python's string setter also ignores the returned failure Result, unlike construction, so an invalid string need not raise. Static lookup may return null, despite a non-optional stub annotation, and native wrapper conversion dereferences it without a guard. These observations relate to later item-lifetime/custom-item diagnosis, but do not establish those later crashes' cause by themselves.

Only a mock interface method is added under tests; the diamond-sword assertions in the body were not executed here. No automated migration, invalid-input or registry-lifetime tests accompany the change.

Exact inspected base/head: 1dcbc0eddf2ecb95c15c107d6fe86e815b9a0ec6…1b7265155b10f1324e3fd1e758a4b4a55bb0af25. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/189
- https://github.com/EndstoneMC/endstone/pull/189#issuecomment-2912051380
