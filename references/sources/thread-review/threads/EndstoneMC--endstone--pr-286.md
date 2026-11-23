<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:286"],"source_type":"public","date":"2025-10-28","topics":["concurrency","ffi","testing","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-286-feat-add-support-for-1-21-120"></a>
# EndstoneMC/endstone #286: feat: add support for 1.21.120 {#endstonemc-endstone-286-feat-add-support-for-1-21-120}

Source: https://github.com/EndstoneMC/endstone/pull/286

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (497 additions, 202 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu authored and merged this version-support PR. Its primary body and all comments/review components are empty; all technical conclusions below derive from the exact patch, with no invented design conversation or testing claim.

### Complete patch inspection {#complete-patch-inspection}

The full 37-file patch targets Minecraft 1.21.120, protocol 859 and Endstone patch version 0.10.8. It pins endstone-bstats from a broad <1.0.0 constraint to exactly 0.1.0, but the empty thread supplies no dependency-regression rationale. Both symbol tables are refreshed/reordered; MapDataManager::_loadMapData receives addresses on Windows and Linux. An address entry alone is not a newly implemented or tested map API.

Packet's fixed server-bound maximum becomes virtual getMaxSize(), preserving the default 0xA00000 (10 MiB) and strict greater-than rejection. checkSize now includes numeric packet type and actual size in its error. Client-bound calls remain outside that limit check. New packet IDs and the inserted virtual slot must track the native ABI. NetworkSystem adds a session-summary publisher, EntityRegistry adds pre/post invocation callbacks, ServerInstance removes its command queue field, and pack settings gain value/default pairs and a last-used field. These layout changes are substantive even where implementation remains native.

Block-change operations replace bare actor-source arguments with BlockChangeContext, a variant distinguishing environment position, actor and script/command causes. The exposed constructors provide position/actor conversions, but most query/default constructors remain declarations; the patch does not establish complete behavior of all context alternatives. BlockSource changes set/remove signatures, adds extra-block/event operations and removes validity-update interfaces. Level changes destroyBlock, dimension-factory argument type and camera virtual order. Block direct data adds a 16-bit registry handle and six directional handles, raising declared Block sizes from 304/312 to 320/328. BlockOcclusionType deletes ThinConnects2D and renumbers subsequent values, so persisted/native numeric identity cannot be assumed stable across versions.

New DenseEnumMap and RegistryHandle provide native-compatible storage declarations. Most methods have no implementation here; DenseEnumMap.asSpan is declared as span<int> even for non-int TValue, a genericity caveat if used rather than mere layout reconstruction. Function-wrapper specializations now cover copyable/move-only, const/nonconst signatures and forward the argument pack into function_base_impl, whereas the old specialization omitted it. DerivedDimensionArguments uses the new move_only_function to construct TaskGroups.

Player::setPermissions is renamed setCommandPermissions and Endstone's setOp call is migrated without changing its Admin/Any choice. PlayerUseNameTagEvent now contains named entity, previous/redactable new names instead of an ItemStack; a sleep-state event changes the gameplay variant's alternative order. Item virtuals gain swing duration and rename in-use game-event emission, with the caller updated. Unbreakable NBT uses a shared constant with the same literal, and UWP/Win32 device labels both become Windows. No tests or human review are present. Reusable lesson: version ports require tracing enum values, virtual order, variant order and storage layouts in addition to changing version constants; declarations and symbol refreshes are evidence of intended adaptation, not runtime verification.

Exact inspected base/head: 909a36d8e2819c3add421d53883e5c3a2c4d3a85…8f61392d2bbe65ca6088b0ddd6af0285d774549d. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/286
