<!-- retrieval: {"source_ids":["public:commit:0b41fe71d2921b915480e5cefd607d56204ae313","public:commit:1608ef01e8c8a89abddf3151d39ccbc39e032801","public:commit:2597eeca495d0d4d94f0e600974aca1b1d84b3ad","public:commit:32860a1c09628326b28812bb6fe0d134f84f6a49","public:commit:38b262298ac192ba1a81250d4f39737e88cb50d8","public:commit:39ce1ba35ea97ff336b9eff838e2dde6e5d84c7e","public:commit:3e81975a9b69da1870039c5b10a568f4f940fe34","public:commit:400184c491022c25f53cdd563989dbb0f06d7d08","public:commit:42f5b9d1196591139d33345e555c68397d71d0e6","public:commit:4524abbb91e61b00af509e7d1c2daa782f718458","public:commit:4816aef277f86290cef18daf14aeee2d0904bca4","public:commit:5aa11cc6a93c9f8c78813b00335dcf19af066b41","public:commit:70cfe379eacc9214c29737b082acdd121ddeb505","public:commit:7f01cf0102ede5d1d780277078e7f8fd0387453e","public:commit:b16ec4a30715f6c40c2b886ea520c9fd96e96d12","public:commit:f66147f0c00e7575ca573d819131e7a7ade8a37d"],"source_type":"public","date":"2025-11-24..2025-11-25","topics":["lifetime","ffi","testing","build","api","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# API error and ownership migration {#api-error-and-ownership-migration}

## A deliberate change in failure surface {#a-deliberate-change-in-failure-surface}

Main's November 25 sequence replaces many Result wrappers with direct values/void and exceptions. Preconditions initially carries source-location formatting; the public helper soon removes that extra parameter. Argument violations use invalid_argument, state failures use runtime_error. Boss bar, health, distance, block/state, inventory, player experience/flight and server factories migrate in small commits. Mock signatures and one identifier test follow API changes, but there are no new behavioral assertions for the changed exception paths in this slice.

The migration is not uniformly “exceptions everywhere.” Permission attachment removal returns bool for expected absence; objective display slot/order use optional for a valid undisplayed state. setSortOrder ceases to report an error after successful mutation and becomes a no-op when undisplayed. These choices distinguish absence, invalid arguments and invalid state without evidence for a universal preference outside this project.

Color is a semantic exception: C++ component factories drop bounds checks and narrow to uint8_t; packed RGB ignores high bits. Python still converts components through uint8_t first. Thus changing Result<Color> to Color also changes accepted input behavior, and language-boundary contracts must be compared separately.

## Ownership and registry contracts {#ownership-and-registry-contracts}

ItemStack.type now returns const ItemType& instead of an ID/string. A temporary borrowed Identifier member is repaired to owned std::string in 1338. Registry-returned references still depend on registry lifetime; reload replaces registries in inherited code. Generic Python get_registry explicitly uses reference policy; the newly added unused registry_getter with reference_internal is not evidence that the live path retains the server.

Objective replaces a native reference and name-based registry check with NonOwnerPointer. This tracks native object invalidation rather than merely existence of an equal name, but the local pointer implementation has sharp edges: reset throws when its control is invalid, and its destructor calls reset. It also declares dereference noexcept while the underlying access can throw. Objective state checks improve one boundary without proving complete destruction safety. The scoreboard itself remains borrowed.

## Counterexamples retained at main1352 {#counterexamples-retained-at-main1352}

- addObjective uses checkState(objective == nullptr), then dereferences objective. A successful native add throws after mutation; a null result passes the condition and is dereferenced. This exact predicate persists at main1352.
- The three-argument addObjective overload still forwards name instead of display_name, and render_type is unused.
- Native ItemStackBase::reinit(string_view,...) is empty; changing setType's return/error surface does not complete it.
- setMaxHealth writes maximum and marks dirty without an explicit current-health clamp, although public prose promises clamping.
- distanceSquared's helper-call formatting arguments are evaluated eagerly, including dimension-name access even when pointer equality passes.

These are historical static findings, not executed failures. They constrain claims of behavior-preserving refactoring. The separate December stable port does not descend from main1352 and therefore cannot be credited as fixing these main changes.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1332"></a>
## Commit 1332 {#commit-1332}

4816aef277f86290cef18daf14aeee2d0904bca4 · 2025-11-24T21:57:49Z

[refactor: rename AttributeModifier operations](https://github.com/EndstoneMC/endstone/commit/4816aef277f86290cef18daf14aeee2d0904bca4)

**Change and causal context.** Renames attribute operations AddNumber/AddScalar/MultiplyScalar1 to Add/MultiplyBase/Multiply, updating Python enum names and explaining sum-of-modifiers versus product-of-modifiers behavior.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Numeric ordering is retained, but source/Python names break compatibility. Stub update follows in 1333; no arithmetic implementation changes here.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1333"></a>
## Commit 1333 {#commit-1333}

42f5b9d1196591139d33345e555c68397d71d0e6 · 2025-11-24T22:11:32Z

[refactor: update `ItemStack.type` property return type to `ItemType`](https://github.com/EndstoneMC/endstone/commit/42f5b9d1196591139d33345e555c68397d71d0e6)

**Change and causal context.** Changes ItemStack.type/getType from ID/string to registry-backed const ItemType&, renames ItemId to ItemTypeId throughout public/core factory and metadata APIs, and updates Python stubs plus the identifier test. Public getType falls back to air; native getType dereferences registry lookup for a nonempty native item. NBT damage explicitly narrows to short.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** At this stage ItemStack stores borrowed Identifier rather than owned text, introducing a lifetime risk repaired by 1338. Native getType assumes registry lookup succeeds; the public air fallback also assumes air exists. Registry reload can invalidate returned references. No new ownership test is added.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1334"></a>
## Commit 1334 {#commit-1334}

7f01cf0102ede5d1d780277078e7f8fd0387453e · 2025-11-24T22:31:30Z

[feat: add setter for `Mob.max_health` property](https://github.com/EndstoneMC/endstone/commit/7f01cf0102ede5d1d780277078e7f8fd0387453e)

**Change and causal context.** Adds Mob.max_health setter to C++ and Python/stubs, validates health > 0, and writes the mutable health attribute maximum with dirty-context propagation. AttributeInstance gains direct min/max setters.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Public docs promise current health clamping when lowered, but the shown setMaxValue only changes maximum and marks dirty. Any later native clamping is not proven. Setter initially returns Result, then migrates to exceptions in 1345.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1338"></a>
## Commit 1338 {#commit-1338}

5aa11cc6a93c9f8c78813b00335dcf19af066b41 · 2025-11-25T17:09:40Z

[refactor: update `ItemStack` and enchantment handling logic for type and ID consistency](https://github.com/EndstoneMC/endstone/commit/5aa11cc6a93c9f8c78813b00335dcf19af066b41)

**Change and causal context.** Restores public ItemStack.type_ to std::string and copies getType().getId(), fixing the borrowed Identifier storage introduced in 1333. Enchantment metadata stores native string IDs directly and strips the namespace via EnchantmentId(...).getKey() for native name lookup.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** The latter relies on the native lookup using the key component and may conflate namespaces if custom registry entries use equal keys. No new round-trip tests accompany this patch.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1339"></a>
## Commit 1339 {#commit-1339}

2597eeca495d0d4d94f0e600974aca1b1d84b3ad · 2025-11-25T17:29:19Z

[refactor: simplify registry binding logic with `type_list`](https://github.com/EndstoneMC/endstone/commit/2597eeca495d0d4d94f0e600974aca1b1d84b3ad)

**Change and causal context.** Centralizes registry binding over type_list<Enchantment,ItemType>, using a fold for declarations and dispatch. Public get_registry uses py::return_value_policy::reference and unknown types return None. A separate registry_getter with reference_internal is added but not the called path.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** The presence of unused reference_internal code is not proof that returned registries retain server ownership. Existing server reload replaces registries; reference-lifetime concern remains. Per-registry prose is dropped by generic binding.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1340"></a>
## Commit 1340 {#commit-1340}

4524abbb91e61b00af509e7d1c2daa782f718458 · 2025-11-25T18:37:54Z

[refactor: replace `Result<void>` with `void` in `setProgress` and add `Preconditions` utility](https://github.com/EndstoneMC/endstone/commit/4524abbb91e61b00af509e7d1c2daa782f718458)

**Change and causal context.** BossBar::setProgress becomes void and range failure throws invalid_argument through new Preconditions::checkArgument. This starts a broad Result-to-exception migration; progress broadcast logic stays the same.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Initial helper places source_location after a variadic pack, complicating formatted-argument deduction; later 1343 removes it and moves helper public. No tests/build run establishes compiler acceptance.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1343"></a>
## Commit 1343 {#commit-1343}

3e81975a9b69da1870039c5b10a568f4f940fe34 · 2025-11-25T19:30:08Z

[refactor: replace `Result<Color>` with `Color`](https://github.com/EndstoneMC/endstone/commit/3e81975a9b69da1870039c5b10a568f4f940fe34)

**Change and causal context.** Moves Preconditions to public check.h and removes source-location formatting. Color factories/setters return Color directly and remove range/high-bit validation: component inputs narrow to uint8_t and packed RGB ignores excess high bits. Map canvas color returns simplify; cursor direction still validates by throwing; Python color caster removes Result unwrapping but still casts input elements to uint8_t.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** This is not purely transport of errors: C++ color acceptance changes to truncation/wrapping. Python conversion can still reject out-of-range values before the factory. A generic claim that all Result conversions preserve validation would be false.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1344"></a>
## Commit 1344 {#commit-1344}

b16ec4a30715f6c40c2b886ea520c9fd96e96d12 · 2025-11-25T19:41:12Z

[refactor: update `remove_attachment` method to return a boolean](https://github.com/EndstoneMC/endstone/commit/b16ec4a30715f6c40c2b886ea520c9fd96e96d12)

**Change and causal context.** Permission removal returns bool rather than Result. Missing attachment becomes false; successful callback, erase and permission recomputation return true. Changes wrappers/core/player/stub, simplifies PermissionAttachment::remove and deletes obsolete permissible forwarding macro.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Callback still runs before erase and can reenter mutation; this patch does not add reentrancy protection. Returning false models expected absence without an exception, a counterexample to universal exception preference.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1345"></a>
## Commit 1345 {#commit-1345}

400184c491022c25f53cdd563989dbb0f06d7d08 · 2025-11-25T19:50:55Z

[refactor: replace `Result<void>` with `void` in `setHealth` and `setMaxHealth`, add `Preconditions` validation](https://github.com/EndstoneMC/endstone/commit/400184c491022c25f53cdd563989dbb0f06d7d08)

**Change and causal context.** Mob health/max-health setters become void and use Preconditions for the same numeric constraints before mutable attribute updates.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Existing max-health clamp documentation remains stronger than the shown direct maximum write. [[nodiscard]] remains on implementation void methods. No new behavioral coverage.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1346"></a>
## Commit 1346 {#commit-1346}

70cfe379eacc9214c29737b082acdd121ddeb505 · 2025-11-25T19:52:12Z

[refactor: replace `Result<float>` with `float` in `distanceSquared`, add `Preconditions` validation](https://github.com/EndstoneMC/endstone/commit/70cfe379eacc9214c29737b082acdd121ddeb505)

**Change and causal context.** Location::distanceSquared returns float and throws invalid_argument on different dimension pointers instead of returning an error Result.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** The formatting arguments dimension_->getName() and other.dimension_->getName() are now eagerly evaluated even when the condition is true, unlike the old failure macro. Null/default-location behavior needs care; no new null guard is added.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1347"></a>
## Commit 1347 {#commit-1347}

0b41fe71d2921b915480e5cefd607d56204ae313 · 2025-11-25T19:52:36Z

[refactor: replace `Result<float>` with `float` in `distance`](https://github.com/EndstoneMC/endstone/commit/0b41fe71d2921b915480e5cefd607d56204ae313)

**Change and causal context.** Location::distance directly takes sqrt(distanceSquared(other)); removes Result propagation/unwrapping.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Different-dimension failures now propagate exceptions from 1346. Numeric calculation unchanged; no new geometric validation.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1348"></a>
## Commit 1348 {#commit-1348}

f66147f0c00e7575ca573d819131e7a7ade8a37d · 2025-11-25T20:32:35Z

[refactor: replace `Result<T>` with `T` in `Objective` and `Score`, add `Preconditions` validation](https://github.com/EndstoneMC/endstone/commit/f66147f0c00e7575ca573d819131e7a7ade8a37d)

**Change and causal context.** Objective/Score APIs return values, references, unique_ptr or optional, and mutation failures throw. Undisplayed slot/order become nullopt; setSortOrder on an undisplayed objective becomes a no-op instead of always returning an error even after successful mutation. Objective replaces a native reference plus name lookup with NonOwnerPointer and control-block validity checks; Score keeps a copied objective wrapper. Python wrappers simplify and default set_display order becomes the enum value.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Board itself remains borrowed. Local NonOwnerPointer reset throws for invalid controls and its destructor calls reset, so native invalidation can still lead to termination during destruction; validity checks do not prove complete safe ownership. Explicit None for Python order is no longer accepted by the typed parameter.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1349"></a>
## Commit 1349 {#commit-1349}

1608ef01e8c8a89abddf3151d39ccbc39e032801 · 2025-11-25T21:20:21Z

[refactor: replace `Result<Objective>` with `Objective`, add `Preconditions` validation](https://github.com/EndstoneMC/endstone/commit/1608ef01e8c8a89abddf3151d39ccbc39e032801)

**Change and causal context.** Scoreboard addObjective returns unique_ptr and uses Preconditions. Criteria absence throws; native add result is checked with objective == nullptr, then dereferenced to construct wrapper. Visitor reformatting retains existing null checks and concrete actor casts.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** The new predicate is inverted: successful nonnull creation throws, potentially after native mutation; null passes then is dereferenced. Three-argument overload still forwards name instead of display_name and render_type remains unused. These static facts persist at main1352; no runtime reproduction claimed.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1350"></a>
## Commit 1350 {#commit-1350}

32860a1c09628326b28812bb6fe0d134f84f6a49 · 2025-11-25T23:28:07Z

[refactor: replace `Result` with `Preconditions` validation](https://github.com/EndstoneMC/endstone/commit/32860a1c09628326b28812bb6fe0d134f84f6a49)

**Change and causal context.** Migrates Block setType/setData, Player experience/flight and Server max-players/block-data factory to void/value plus exceptions. Existing bounds remain, absent block descriptor becomes invalid_argument, and mocks update signatures. Block setType directly delegates through createBlockData.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Block::setData still static-casts implementation data and ignores native setBlock success; migration does not add transactional semantics or type validation. Mock updates maintain interface compatibility, not behavioral test coverage.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1351"></a>
## Commit 1351 {#commit-1351}

38b262298ac192ba1a81250d4f39737e88cb50d8 · 2025-11-25T23:34:47Z

[refactor: replace `Result` with `Preconditions` validation](https://github.com/EndstoneMC/endstone/commit/38b262298ac192ba1a81250d4f39737e88cb50d8)

**Change and causal context.** Migrates inventory setContents, item type/amount setters and selected hotbar slot to void with Preconditions. Inventory size and amount/slot constraints remain; setContents updates sequentially and clears omitted slots. Native setType calls reinit after successful registry validation.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Native ItemStackBase::reinit(string_view,...) remains empty at main1352, so changing the error surface does not fill its implementation. Partial inventory mutation on a later failure is not rolled back.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1352"></a>
## Commit 1352 {#commit-1352}

39ce1ba35ea97ff336b9eff838e2dde6e5d84c7e · 2025-11-25T23:38:56Z

[refactor: replace `Result` with `Preconditions` validation](https://github.com/EndstoneMC/endstone/commit/39ce1ba35ea97ff336b9eff838e2dde6e5d84c7e)

**Change and causal context.** BlockState setType/setData become void, preserving unknown-type validation via invalid_argument and direct assignment from concrete EndstoneBlockData. This is the maximal assigned main tip.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** State remains a borrowed native block representation; no new type/lifetime protection. December stable changes are not descendants of this main endpoint.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.
