<!-- retrieval: {"source_ids":["public:commit:1fbb4027a611d86cf6d4245714455ea58b2e6ace","public:commit:2b1603b50712fffa44ef38b7128628ef72f8a40e","public:commit:48438406c23e824df4f7f4c14fafc20db77a3a42","public:commit:547d2e1b79a91ff4c734b8440030ca406bdd7fef","public:commit:5fd30889963e2921bb0de8ff0b36a36a761c12de","public:commit:63463a8b657b3656e026a681e328983dde4629c6","public:commit:8d47aa53dc956c0be493a250597dd82e79007f8c","public:commit:9596f813d0b984f07fb64d75f371c859aa6bd4fe","public:commit:b3e495be412c7f8f36af57d2ee0f35c9adc989d2","public:commit:b5eead2d5b1d2534a98d81f7a0f1aea6218a40ad","public:commit:bc5758adf89c7d60e11cf89fa3794d7219ace9dc","public:commit:c0a6c78bade07da32cd25964c6fd3707fad289f3","public:commit:e02945aef92f61e349e25bbdfdb1b44db8ad0aea","public:commit:e5d440049595fd7e123b17c3175f33bd18030835"],"source_type":"public","date":"2025-05-08..2025-05-11","topics":["lifetime","ffi","testing","performance","recovery","api","diagnosis","documentation","review","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Metadata, errors and registry ownership {#metadata-errors-and-registry-ownership}


## Result and causal boundary {#result-and-causal-boundary}

Commits601–614 close three unfinished contracts inherited from the completed501–600 review: the server factory accessor acquires a concrete override, plain ItemStack metadata presence stops reporting the inverse of emptiness, and the enchantment registry acquires actual native lookup/enumeration and initialization. These repairs are visible in source; no native test was run. The chain then adds repair cost and unbreakability, simplifies Result failures, and connects those APIs to Python.

The distinction between metadata *being represented* and the game *honoring* it matters. Repair cost is present only when positive. An unrestricted integer setter can retain a negative number in memory while serialization and presence-aware equality ignore it. Unbreakable serializes a true byte and omits false. The native item adapter must serialize the factory-adapted metadata rather than the original input;602 repairs that conversion boundary. Enchantment force bypasses level bounds, but607 still rejects an unknown enchantment. None of this proves durability behavior or native NBT round trips.

## API and diagnostic costs {#api-and-diagnostic-costs}

The609 message states simplification, not a measured performance goal. Replacing the structured error carrying a stack trace with a string removes automatic trace construction, requiring callers and logging interfaces to change. This plausibly reduces allocation/trace cost and loses diagnostic richness, but no benchmark supports a numerical claim. The error-shape migration also changes failure delivery: registerEvent now logs and returns void; addAttachment logs and returns a nullable pointer. Consumers can no longer inspect the previous Result through those signatures.

The diff is not mechanically uniform. Flight disabling becomes legal without flight permission, a native max-player ceiling disappears, and positive conjunction checks reject NaN where older out-of-range comparisons did not. Treat the refactor label as intent, then inspect each behavioral boundary.613 repairs the template wrappers that still expected a Result and adds a test-plugin member-handler instantiation; that fixture is compile/integration coverage, not an assertion that death events fire correctly.

## Registry and language boundary {#registry-and-language-boundary}

The registry replaces the unfinished keyed-iterator abstraction with callback enumeration and a lazy cache of uniquely owned wrappers. Native definitions remain borrowed. Range-for over the returned key vector avoids the earlier iterator-over-temporary construction, but cache allocation occurs in noexcept get, no synchronization or invalidation is added, and native enchant lookup uses only the key component while the cache uses the full NamespacedKey. Those are explicit snapshot limits, not evidence of a reported production failure.

NamespacedKey parsing becomes Result-based and gains plugin/default namespaces. Its create implementation computes a lowercase key but validates the original key, so the source does not establish case-insensitive keys. Comments still describing optional/nullopt lag the implementation. Python binding order is deliberately staged with class shells before cross-type signatures. Nullable C++ results remain incompletely reflected in stubs.

At700 the generic registry binding still returns a list from __iter__, which does not fulfill Python's iterator-return contract. Several accessors also lack an explicit borrowed return policy while the registry owns their objects. This review identifies a protocol mismatch and an ownership-validation requirement, without claiming an executed crash. The later ItemType registry inherits these same choices; see06.

## Evidence and applicability {#evidence-and-applicability}

Primary evidence is the per-commit full parent patches, especially608–614. The historical registry endpoint snapshots, blob/range proofs and preceding bounded review are not included in this bundle; inspect the linked public commits to recheck the source-level claims. Use this case when migrating error APIs, adding factory adapters, binding nullable registries, or separating representation tests from game behavior. Do not infer a universal preference for strings over richer errors from one explicitly scoped simplification.

## Per-commit decisions and revisions {#per-commit-decisions-and-revisions}

<a id="commit-601"></a>
### Commit 601 {#commit-601}

[5fd30889963e](https://github.com/EndstoneMC/endstone/commit/5fd30889963e2921bb0de8ff0b36a36a761c12de) · 2025-05-08T14:18:11Z · feat: add `Server::getItemFactory`

Completes the prior600 missing getItemFactory: Server accessor becomes const pure virtual; EndstoneServer returns singleton factory and mock gains override. This is an API contract correction, not a separately tested implementation.


<a id="commit-602"></a>
### Commit 602 {#commit-602}

[1fbb4027a611](https://github.com/EndstoneMC/endstone/commit/1fbb4027a611d86cf6d4245714455ea58b2e6ace) · 2025-05-08T14:53:38Z · fix: correct `hasItemMeta` logic

Negates factory equality-to-empty in plain ItemStack::hasItemMeta, repairing600's inversion. Native setItemMeta now applies the adapted item_meta rather than original input, preserving factory conversion semantics; equals0 uses references. No tests added.


<a id="commit-603"></a>
### Commit 603 {#commit-603}

[b3e495be412c](https://github.com/EndstoneMC/endstone/commit/b3e495be412c7f8f36af57d2ee0f35c9adc989d2) · 2025-05-08T15:08:31Z · feat: add methods for getting/setting repair cost for items

RepairCost added across public metadata/native tag/read/write/equality/emptiness. Presence means cost>0; setter accepts any int, so zero/negative values are stored in memory but excluded from persistence/equality presence. Explicit feature intent only; native round-trip untested.


<a id="commit-604"></a>
### Commit 604 {#commit-604}

[c0a6c78bade0](https://github.com/EndstoneMC/endstone/commit/c0a6c78bade07da32cd25964c6fd3707fad289f3) · 2025-05-08T15:13:11Z · feat: update python bindings

Python repair_cost read/write and has_repair_cost read-only properties plus stub expose603 without separate validation or tests.


<a id="commit-605"></a>
### Commit 605 {#commit-605}

[48438406c23e](https://github.com/EndstoneMC/endstone/commit/48438406c23e824df4f7f4c14fafc20db77a3a42) · 2025-05-08T16:50:44Z · docs: update README.md

README roadmap marks Player/Actor and Block APIs complete at0.6.0; this is author release-status documentation, not independent completeness evidence.


<a id="commit-606"></a>
### Commit 606 {#commit-606}

[2b1603b50712](https://github.com/EndstoneMC/endstone/commit/2b1603b50712fffa44ef38b7128628ef72f8a40e) · 2025-05-08T20:38:39Z · feat: add `ItemMeta::setUnbreakable` and `ItemMeta::isUnbreakable`

Unbreakable field spans public virtuals, Python/stub, NBT byte/boolean getters, metadata load/apply/equality/emptiness. Missing or wrong-type Byte returns0; true serializes, false omitted. Domain contract says unbreakable prevents durability loss; no native behavior test accompanies it.


<a id="commit-607"></a>
### Commit 607 {#commit-607}

[8d47aa53dc95](https://github.com/EndstoneMC/endstone/commit/8d47aa53dc956c0be493a250597dd82e79007f8c) · 2025-05-08T21:09:31Z · feat: improve enchantment logic

addEnchant rejects unknown native enchant IDs and enforces min/max unless force; only changed/new level returns true. Force bypasses level limits, not unknown-name rejection. Conflict/applicability checks remain separate; no rationale beyond improve logic.


<a id="commit-608"></a>
### Commit 608 {#commit-608}

[547d2e1b79a9](https://github.com/EndstoneMC/endstone/commit/547d2e1b79a91ff4c734b8440030ca406bdd7fef) · 2025-05-08T22:20:55Z · feat: implement `Server::getEnchantmentRegistry`

Replaces unfinished keyed iterator/storage abstraction with NamespacedKey and callback forEach, lazy unique-owned wrapper cache and native Enchant specializations. setLevel creates enchantment registry, eliminating prior TODO. Adapter now dereferences native pointer for factory and iterates a stable temporary vector through range-for, avoiding prior iterator-over-temporary design. Native enchant lookup uses key component only, ignoring namespace; cache still keys full NamespacedKey. get is noexcept despite allocation. Handles remain borrowed native references; lifecycle/concurrency unproven.


<a id="commit-609"></a>
### Commit 609 {#commit-609}

[bc5758adf89c](https://github.com/EndstoneMC/endstone/commit/bc5758adf89c7d60e11cf89fa3794d7219ace9dc) · 2025-05-08T23:40:58Z · refactor: simplify error handling

Result error payload changes Error(message,stacktrace) to string; removes per-error cpptrace generation/logger Error overload, adds CHECK/CHECKF macros and migrates callers/Python exceptions/ban tests. Event registration becomes void/log-and-return; attachment add becomes nullable pointer/log-and-return, losing structured caller failure. Not purely mechanical: setFlying(false) allowed without flight permission; max-player native hard ceiling check removed; positive-conjunction float checks reject NaN unlike old range comparison. Detours gitlink moves b2bf32a to ea6c4ae, contents not included/reviewed. Explicit simplification intent, inferred diagnostics/cost tradeoff, no measured performance.


<a id="commit-610"></a>
### Commit 610 {#commit-610}

[9596f813d0b9](https://github.com/EndstoneMC/endstone/commit/9596f813d0b984f07fb64d75f371c859aa6bd4fe) · 2025-05-08T23:46:33Z · feat: add python binding for `NamespacedKey`

NamespacedKey creation now plugin-scoped Result; fromString accepts explicit valid namespace or defaults to plugin/minecraft, rejects empty/multiple colon/invalid syntax with errors. Normalizes plugin name; create computes lowercased key but validates original key, so uppercase remains rejected. Adds formatter and Python constructor/from_string/string/repr/properties/export; no Python equality/hash bindings. Form export formatting unrelated. Comments still describe optional/nullopt despite Result migration.


<a id="commit-611"></a>
### Commit 611 {#commit-611}

[e02945aef92f](https://github.com/EndstoneMC/endstone/commit/e02945aef92f61e349e25bbdfdb1b44db8ad0aea) · 2025-05-09T00:12:34Z · feat: add python binding for registries

Adds generic Python registry get/get_or_throw, indexing, contains and __iter__, plus server factory/enchantment access. String contains treats invalid syntax as false; indexing throws. __iter__ returns a list rather than its iterator, a static protocol mismatch; get pointer uses default binding policy and registry owns wrappers, requiring ownership validation. Stubs temporarily have ellipses before class bindings exist.


<a id="commit-612"></a>
### Commit 612 {#commit-612}

[b5eead2d5b1d](https://github.com/EndstoneMC/endstone/commit/b5eead2d5b1d2534a98d81f7a0f1aea6218a40ad) · 2025-05-11T18:55:29Z · feat: add python binding for `ItemFactory`

ItemFactory binding exposes metadata creation, applicability, equality and conversion; exported in inventory and typed stub replaces placeholder. Nullable native inputs/results are not fully reflected in stub. No separate tests.


<a id="commit-613"></a>
### Commit 613 {#commit-613}

[63463a8b657b](https://github.com/EndstoneMC/endstone/commit/63463a8b657b3656e026a681e328983dde4629c6) · 2025-05-11T18:58:46Z · fix: correct the template function `Plugin::registerEvent`

Repairs Plugin::registerEvent templates after609 void return: removes obsolete result/error branch. Test plugin onEnable now instantiates member handler for const PlayerDeathEvent and logs player, adding compile/integration fixture coverage rather than an event assertion.


<a id="commit-614"></a>
### Commit 614 {#commit-614}

[e5d440049595](https://github.com/EndstoneMC/endstone/commit/e5d440049595fd7e123b17c3175f33bd18030835) · 2025-05-11T19:29:10Z · feat: add python binding for `Enchantment`

Enchantment binding exposes key/level/conflict/applicability and shared_ptr holder; adds docs facade/navigation and stub generation helper. Registers ItemStack/NamespacedKey class shells before method binding so cross-type signatures resolve. Registry stub placeholders become Enchantment, but get remains nonoptional despite native null. Helper invokes stubgen only when run; not executed here.

