<!-- retrieval: {"source_ids":["public:commit:0d69b01fce362717573502c8210fad29bfb347be","public:commit:0dc5a4c5584114afbee7b911ed0b7bec28a538fa","public:commit:20c197b68d81b48e7ce67f577d99a63398260bc7","public:commit:2d7f46cf10984d19c821d84e0281f6e2273dfa1c","public:commit:2ed5de22a3818c3084f57de87d10e693efc99097","public:commit:463bf5e2a240751cfeecab91ee1856f376ccd113","public:commit:51232b3a5b4583b7559967df854f14c2e3fc9175","public:commit:5fd09d41521d129792c09ce8a1ff23c58884ed7e","public:commit:9af01367734fe733d37032c3472d1a695d9706f7","public:commit:a0b251d19afd2479732b62fd409f9d28118078d4","public:commit:a334f69a7d0e7c87021ba700e0f53578a5dfc470","public:commit:c22a2d15d48e77d2ca6603d675cb96aa13b9bfbe","public:commit:ca74c33ef7d542194b3cae6bb2ddbf4840c7f8a3","public:commit:ccad4736303dc5f44fa8b4d00aa51721527d3beb","public:commit:ebb300c45795150b1532a104f72eec5c96ae1437","public:commit:ee55bd94526969cfee06c64d82280cfccd548fa2","public:commit:fed2ccb9545e5a31e1c04f9394811034387dc71a"],"source_type":"public","date":"2025-03-27..2025-05-08","topics":["ffi","testing","build","recovery","api","diagnosis","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Runtime-owned item metadata and coverage tradeoffs {#runtime-owned-item-metadata-and-coverage-tradeoffs}

## From values to runtime interfaces {#from-values-to-runtime-interfaces}

Damage512 fixes an unrelated-lore early return and updates empty-state semantics. Later589–600 converts ItemFactory/ItemMeta from inline concrete value helpers into runtime-owned interfaces. Plain ItemStack now resolves Server through a platform module lookup and C export, then asks its ItemFactory to create/compare/convert metadata. The earlier sibling456 removal of cached exported getServer makes this a concrete reversal, not evidence that one design was always preferred.596 fixes the undefined class-static pointer by using a local static;600 adds the export and excludes it from detour scanning.

The export returns the current entt locator value, but the header caches a raw Server pointer after first lookup. Linux dlopen handles are not closed, assignment after static initialization is not synchronized, and no cache invalidation follows locator reset. These are source lifecycle constraints, not observed reload failures. At exact600, the new virtual Server::getItemFactory is declared without an implementation or EndstoneServer override in the searched include/src/tests tree. The slice ends during integration.

## Semantics and persistence {#semantics-and-persistence}

Applicability gate592 initially rejects applicable metadata;598 corrects its polarity. Plain hasItemMeta593 returns equality-to-empty without negation and remains so at600; native stack uses the correct negation. Factory equality treats null and empty as equivalent; air construction returns null. Setter contracts assume metadata originates in core and use unchecked static_casts to EndstoneItemMeta.

Native setter593 constructs a new CompoundTag and serializes represented fields, unlike the earlier in-place update of existing userData. EndstoneItemMeta595 reads only display name/lore/enchantments/damage, so unknown NBT fields are not retained by this path. It computes a converted item_meta but applies original meta. MapMeta becomes an abstract empty interface; map-specific concrete loading is commented out and factory notes TODO. These are explicit capability/round-trip limits.

The new enchant parser595 removes prior id/lvl type checks and masks lvl with0xffff, so negative shorts become unsigned-range values. Getter defaults and the native enum boundary remain relevant for malformed data. Serialization narrows int to short and skips unknown IDs. No NBT round-trip, malformed-data or client validation was run.

## Test-removal interpretation {#test-removal-interpretation}

597 first removes ItemStack tests from the CMake target;599 deletes exactly three tests: setting lore, clearing lore with an empty vector, and clearing metadata with null. Those tests assumed standalone construction before runtime-factory coupling. Removing outdated test infrastructure can be a reasonable cost decision, particularly when low-value mocks would merely reproduce implementation. The source does not state that rationale, and this dossier does not infer a permanent personal preference. It records the actual tradeoff: less standalone scaffolding, and those explicit assertions no longer present in this target; no replacement integration tests appear in the bounded slice. No claim is made that removal is automatically defective or that more tests would necessarily be worth the cost.

## Other API boundary change {#other-api-boundary-change}

Plugin event registration588 replaces static_cast with reinterpret_cast in both handler overloads. This removes compile-time downcast constraints and pointer adjustment, so runtime event-name/type agreement and object layout become more important. No rationale or proof of safety is supplied by the title. Keep it as a bounded compatibility change, not a reusable casting recommendation.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-512"></a>
### Commit 512 {#commit-512}

ccad4736303dc5f44fa8b4d00aa51721527d3beb · 2025-03-27T21:43:08Z

[feat: add damage to `ItemMeta`](https://github.com/EndstoneMC/endstone/commit/ccad4736303dc5f44fa8b4d00aa51721527d3beb)

**Observed change.** Adds integer ItemMeta damage, hasDamage > 0 and Python bindings/stubs. isEmpty now includes name/lore/damage. NBT loading no longer returns early when lore is absent, so damage is still read; writes positive damage or removes tag.

**Causal interpretation.** A later metadata field must not be hidden behind an unrelated optional-field early return. Empty-state semantics are updated alongside the API.

**Limits.** Negative damage is accepted by setter but treated absent by hasDamage. No NBT round-trip tests.

<a id="commit-513"></a>
### Commit 513 {#commit-513}

0d69b01fce362717573502c8210fad29bfb347be · 2025-03-28T12:42:11Z

[feat: add `BlockData::getRuntimeId`](https://github.com/EndstoneMC/endstone/commit/0d69b01fce362717573502c8210fad29bfb347be)

**Observed change.** Exposes BlockData runtime ID as uint32_t across API, native implementation, Python binding and stub.

**Causal interpretation.** Supplies the network-facing native identifier without forcing plugins through private wrappers.

**Limits.** No guarantee that runtime IDs persist across versions/world sessions; no packet interop test.

<a id="commit-586"></a>
### Commit 586 {#commit-586}

ee55bd94526969cfee06c64d82280cfccd548fa2 · 2025-05-07T18:56:04Z

[refactor: simplify enchantment key handling](https://github.com/EndstoneMC/endstone/commit/ee55bd94526969cfee06c64d82280cfccd548fa2)

**Observed change.** Removes NamespacedKey normalization around native enchant IDs; codec uses getStringId directly for read/write lookup.

**Causal interpretation.** Avoids adding/dropping namespace components when native IDs already define the lookup representation.

**Limits.** No migration or round-trip test; NamespacedKey remains public but no longer mediates this codec.

<a id="commit-587"></a>
### Commit 587 {#commit-587}

2ed5de22a3818c3084f57de87d10e693efc99097 · 2025-05-08T10:10:42Z

[refactor: improve MSVC debug mode check](https://github.com/EndstoneMC/endstone/commit/2ed5de22a3818c3084f57de87d10e693efc99097)

**Observed change.** Includes vector before a conditional MSVC _ITERATOR_DEBUG_LEVEL assertion; shortens diagnostic and reorders one include.

**Causal interpretation.** Defends release-native C++ standard-library ABI against debug iterator layout when macro is defined.

**Limits.** No MSVC build; assertion coverage depends on include/macro configuration.

<a id="commit-588"></a>
### Commit 588 {#commit-588}

a334f69a7d0e7c87021ba700e0f53578a5dfc470 · 2025-05-08T10:11:02Z

[fix: use `reinterpret_cast` instead of `static_cast` for event handlers](https://github.com/EndstoneMC/endstone/commit/a334f69a7d0e7c87021ba700e0f53578a5dfc470)

**Observed change.** Changes plugin event-handler casts from static_cast to reinterpret_cast in both registration overloads.

**Causal interpretation.** Relaxes compile-time base-conversion constraints but removes pointer-adjustment/type guarantees. Event dispatch still trusts matching event-name/type.

**Limits.** No rationale beyond title, and no runtime event-layout proof; unsafe to generalize as preferred casting practice.

<a id="commit-589"></a>
### Commit 589 {#commit-589}

c22a2d15d48e77d2ca6603d675cb96aa13b9bfbe · 2025-05-08T11:16:12Z

[feat: add `Endstone::getServer` for internal usage](https://github.com/EndstoneMC/endstone/commit/c22a2d15d48e77d2ca6603d675cb96aa13b9bfbe)

**Observed change.** Adds internal Endstone::getServer that loads/finds runtime module and endstone_get_server symbol, invokes it and caches Server*. Initial static data member lacks definition.

**Causal interpretation.** Allows header-side API objects to reach runtime-owned factory/services; introduces explicit runtime dependency and failure exceptions.

**Limits.** Linux dlopen handle not closed, cache invalidation/reload/thread safety not supplied.596 fixes storage definition;600 supplies export.

<a id="commit-590"></a>
### Commit 590 {#commit-590}

ca74c33ef7d542194b3cae6bb2ddbf4840c7f8a3 · 2025-05-08T11:16:27Z

[refactor: make `ItemFactory` an interface](https://github.com/EndstoneMC/endstone/commit/ca74c33ef7d542194b3cae6bb2ddbf4840c7f8a3)

**Observed change.** Converts ItemFactory's static inline constructors into virtual interface with getItemMeta/asMetaFor contracts.

**Causal interpretation.** Moves concrete metadata construction behind server/runtime ownership, preparing pure ItemMeta interface.

**Limits.** Intermediate callers remain staged; no build.

<a id="commit-591"></a>
### Commit 591 {#commit-591}

2d7f46cf10984d19c821d84e0281f6e2273dfa1c · 2025-05-08T11:16:43Z

[refactor: clean up includes](https://github.com/EndstoneMC/endstone/commit/2d7f46cf10984d19c821d84e0281f6e2273dfa1c)

**Observed change.** Replaces Inventory's ItemStack include with forward declaration and adjusts ItemStack includes to runtime accessor/factory.

**Causal interpretation.** Reduces an include dependency while enabling new factory access.

**Limits.** Header completeness and ABI compilation untested.

<a id="commit-592"></a>
### Commit 592 {#commit-592}

5fd09d41521d129792c09ce8a1ff23c58884ed7e · 2025-05-08T11:24:31Z

[refactor: use `ItemFactory` for creating `ItemMeta` in `ItemStack` class](https://github.com/EndstoneMC/endstone/commit/5fd09d41521d129792c09ce8a1ff23c58884ed7e)

**Observed change.** Routes plain ItemStack metadata creation/conversion through server ItemFactory; adds isApplicable API and Server getter. Initial setItemMeta rejects when applicability is true.

**Causal interpretation.** Introduces validity gate but with inverted condition, later corrected598. Existing meta is cloned; null clears without factory.

**Limits.** Server getter is declared nonpure without definition/EndstoneServer override in endpoint600. No linkage/runtime test.

<a id="commit-593"></a>
### Commit 593 {#commit-593}

0dc5a4c5584114afbee7b911ed0b7bec28a538fa · 2025-05-08T12:43:45Z

[refactor: clean up logics for modifying item meta](https://github.com/EndstoneMC/endstone/commit/0dc5a4c5584114afbee7b911ed0b7bec28a538fa)

**Observed change.** Adds factory equals semantics and changes plain hasItemMeta to equals(meta,nullptr), missing negation. Native stack uses correct negation, enforces applicability and replaces userData with newly constructed CompoundTag.

**Causal interpretation.** Empty-state comparison centralizes behavior but plain/native paths diverge. Rebuilding only represented fields changes unknown-tag preservation; native setter computes converted meta but applies original pointer.

**Limits.** No runtime validation; plain predicate remains inverted600, arbitrary third-party ItemMeta is unchecked static_cast, unknown NBT fields can be lost.

<a id="commit-594"></a>
### Commit 594 {#commit-594}

20c197b68d81b48e7ce67f577d99a63398260bc7 · 2025-05-08T12:54:11Z

[refactor: convert `ItemMeta` into a pure interface](https://github.com/EndstoneMC/endstone/commit/20c197b68d81b48e7ce67f577d99a63398260bc7)

**Observed change.** Makes ItemMeta pure interface and removes EMPTY/global inline storage and method implementations.

**Causal interpretation.** Moves representation and persistence behavior out of public API headers into core implementation.

**Limits.** ABI/source break and staged implementation; not yet usable on its own.

<a id="commit-595"></a>
### Commit 595 {#commit-595}

463bf5e2a240751cfeecab91ee1856f376ccd113 · 2025-05-08T13:29:39Z

[refactor: move implementations to `EndstoneItemMeta`](https://github.com/EndstoneMC/endstone/commit/463bf5e2a240751cfeecab91ee1856f376ccd113)

**Observed change.** Moves metadata implementation/codec into EndstoneItemMeta source/header; factory implementation temporarily empty. Reads name/lore/enchant/damage, writes only represented nonempty fields to a fresh tag.

**Causal interpretation.** Centralizes native persistence with runtime-owned metadata. New enchant parser drops prior explicit short-type checks and masks level with0xffff, changing negative-short interpretation.

**Limits.** Unknown NBT not preserved by constructor; level/force validation still TODO. Native sentinel lookup boundary remains. No round-trip tests.

<a id="commit-596"></a>
### Commit 596 {#commit-596}

fed2ccb9545e5a31e1c04f9394811034387dc71a · 2025-05-08T13:30:09Z

[refactor: code clean up](https://github.com/EndstoneMC/endstone/commit/fed2ccb9545e5a31e1c04f9394811034387dc71a)

**Observed change.** Uses function-local static Server* instead of undefined class static member, registers item_meta.cpp in build, makes MapMeta empty abstract interface and temporarily disables native map-specific metadata creation.

**Causal interpretation.** Completes storage/build wiring but explicitly defers map behavior.

**Limits.** Lazy pointer assignment after static initialization is not synchronized; cached pointer does not track locator reset. No build/run.

<a id="commit-597"></a>
### Commit 597 {#commit-597}

ebb300c45795150b1532a104f72eec5c96ae1437 · 2025-05-08T14:16:56Z

[test: remove tests for `ItemStack`](https://github.com/EndstoneMC/endstone/commit/ebb300c45795150b1532a104f72eec5c96ae1437)

**Observed change.** Removes ItemStack API test file from test target without deleting source yet.

**Causal interpretation.** Tests that assumed standalone header-only metadata now depend on a live runtime factory. Removing obsolete harness cost can be rational; no stated author rationale beyond title.

**Limits.** Coverage narrows until replacement/integration tests are supplied; do not label removal inherently defective.599 deletes exact three tests.

<a id="commit-598"></a>
### Commit 598 {#commit-598}

51232b3a5b4583b7559967df854f14c2e3fc9175 · 2025-05-08T14:17:21Z

[feat: implements `EndstoneItemFactory`](https://github.com/EndstoneMC/endstone/commit/51232b3a5b4583b7559967df854f14c2e3fc9175)

**Observed change.** Implements singleton EndstoneItemFactory, null/empty equality, applicability delegation, clone/conversion and air→null; fixes592's inverted applicability gate.

**Causal interpretation.** Centralizes construction and empty semantics with explicit air handling.

**Limits.** Static casts assume core-created metadata; MapMeta remains TODO. Plain hasItemMeta inversion from593 persists.

<a id="commit-599"></a>
### Commit 599 {#commit-599}

a0b251d19afd2479732b62fd409f9d28118078d4 · 2025-05-08T14:17:37Z

[feat: implements `EndstoneItemMeta`](https://github.com/EndstoneMC/endstone/commit/a0b251d19afd2479732b62fd409f9d28118078d4)

**Observed change.** Adds EndstoneItemMeta copy-from-pointer constructor, non-air applicability and common-field equality; notUncommon always true. Deletes three standalone tests: lore set, lore removal and null clear.

**Causal interpretation.** Completes common metadata comparison and removes obsolete test fixture after runtime coupling. Cost saved and specific lost coverage are both recorded without extrapolating author preference.

**Limits.** Does not add enchant validation despite broad implementation title; force/limits TODO persists. No replacement tests in this patch.

<a id="commit-600"></a>
### Commit 600 {#commit-600}

9af01367734fe733d37032c3472d1a695d9706f7 · 2025-05-08T14:17:59Z

[feat: add `endstone_get_server` export](https://github.com/EndstoneMC/endstone/commit/9af01367734fe733d37032c3472d1a695d9706f7)

**Observed change.** Exports C endstone_get_server returning entt locator server; removes that export from both platforms' detour maps.

**Causal interpretation.** Makes header/runtime service lookup possible while preventing a service export from being mistaken for a native hook target.

**Limits.** Requires initialized locator; no ABI/link/load validation. Endpoint remains mid-refactor with missing Server getter implementation, inverted plain metadata predicate and uninitialized enchant registry.
