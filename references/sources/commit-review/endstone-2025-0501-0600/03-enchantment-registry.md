<!-- retrieval: {"source_ids":["public:commit:168002abdb356be27442bfc5d8ac3ef54a4098bc","public:commit:191a978ffc7c92e7f0846b75182b75d0af7dd627","public:commit:1c9fbde1a399096bde37be6fae7c720bb700732b","public:commit:24b6179b4b737abffcb432c5e417aa52487d209b","public:commit:2c44952c2b57b450449ba66e8455e7b92c3d64eb","public:commit:2cf1cd2bcc5b461a542f907ee10f87418ccbd732","public:commit:44084b7fc3d53398a6972d6d6a2b96cb3540cf85","public:commit:47ea0cc640cbd208c0197a88cfa6924a612523b2","public:commit:625b13d38be0d5707b2926e6236e69d639f2a600","public:commit:6b69fa09a24282caeeeda5a9b9b43dbb2ee5c4f4","public:commit:7141737306e92b1f29f1f63a416dd9c3778071a9","public:commit:9460cba64d86ca3d28efa8ec9609e67ac2d2dddd","public:commit:a03600a9660c5d28e12e6b0789769e33bad2546a","public:commit:a2ae5683b8a0a39d337a5c898e0e29405c63192b","public:commit:be074c3ceac2a3958fcc2874dc63a5e20e9aa476","public:commit:cea8c55244b0808f03ec10d2eecf1f2d5105d6db","public:commit:de35b1fcf4b4f9048ddca3dfb65dc5a67d07d418","public:commit:e7a314799c30c651c4c6ff6ff732382f561d43e8","public:commit:ec57508defb1e955e04c992ce0c54dc7ebd8b203","public:commit:f3239f396d4301ecac646d2e63d509570fd2bc44","public:thread:EndstoneMC/endstone:103","public:thread:EndstoneMC/endstone:177"],"source_type":"public","date":"2024-12-06..2025-05-07","topics":["lifetime","ffi","testing","build","api","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Enchantment contribution, API redesign and unfinished registry {#enchantment-contribution-api-redesign-and-unfinished-registry}

<a id="problem-people-and-revisions"></a>
## Problem, people and revisions {#problem-people-and-revisions}

Issue103 by xXLarryTFVWXx asks for names/levels of enchantments to experiment with damage calculations and suggests get/set methods returning a list or dictionary. Vincent promises future work in December2024. killcerr's May2025 branch supplies41 numeric constants, optional numeric enchantment map, NBT short getters and serialization, then Python bindings. Its early optional assignment leaves the optional disengaged; a follow-up constructs it explicitly. Further fixes clear stale tags, handle the INFINITY macro and repair iteration after getEnchants becomes optional. These13 contextual patches (including form/dependency context) are separately preserved, not counted as100 new target commits.

smartcmd explicitly requests pyi regeneration in PR177; killcerr confirms updating it. Two parallel stub edits merge with nullable dictionary preserved but has_enchants stub removed; Vincent581 later supplies the redesigned string-based stub. Vincent565 replaces numeric constants with an abstract enchantment interface;563/566/567 add Registry/server access/lazy native wrapping;568–571 connect native schemas and correct conflictsWith polarity. Metadata580/581 chooses owned string keys, readonly Python dictionary copies and explicit mutation methods. The final merge585 says completes103, while586 removes unnecessary namespace normalization from the codec.

## What the source establishes {#what-the-source-establishes}

The native-slot eligibility helper569 is narrower than a complete enchant policy: permissive mode bypasses, NONE rejects, otherwise slot masks decide. It does not enforce levels/conflicts. EndstoneItemMeta::addEnchant still contains a level-limit TODO through600 and ignores force; invalid IDs can be accepted and later omitted during serialization. Repeated level0 can be reported as changed. Do not turn the interface description into tested policy guarantees.

The Windows-native table adapter579 incorrectly pre-sizes a pointer vector then appends pointers, creating null entries;582 replaces it with native vector access and584 changes a noncopyable unique_ptr-vector return to const reference. Endpoint getEnchant checks > NumEnchantments rather than >=, so sentinel41 can reach at(41). Neither malformed-ID behavior nor null entries in native storage were executed here.

Registry is incomplete at endpoint600. Server owns a default-null unique_ptr, setLevel still says TODO(init registries), and getter dereferences it. The generic adapter's overridden custom iterators do not match base unordered_map iterators, iterator keys refer to a temporary vector, const lookup calls nonconst helpers, and converter expects reference but receives pointer. The template is not instantiated in the endpoint source. These are bounded source observations, not a claim that a particular compiler or released binary crashed. Borrowed string_view keys, borrowed native Enchant references and noexcept allocation impose additional lifetime/exception constraints.

## Tests and cost {#tests-and-cost}

Commit573 temporarily uses concrete EndstoneServer in mocks to reduce duplication.574 instead centralizes abstract mock methods, uses NiceMock and stack/member fixtures, and removes an incidental exact logger call count while retaining behavioral plugin/scheduler assertions. This can reduce brittle maintenance cost. No tests were run, and compile-fix titles are not treated as successful build results. Metadata test removal597/599 is separately scoped in the next dossier.

## Reuse guidance {#reuse-guidance}

Use the contribution/revision chain to preserve collaborator credit, see how a raw-storage feature becomes a public API, and identify integration checkpoints. Do not derive a universal preference for registries or abstractions: the concrete registry remains unused/uninitialized here, while the simpler item enchant map is the actual functional path intended by the feature.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-563"></a>
### Commit 563 {#commit-563}

f3239f396d4301ecac646d2e63d509570fd2bc44 · 2025-05-02T08:31:21Z

[feat: add registry base class](https://github.com/EndstoneMC/endstone/commit/f3239f396d4301ecac646d2e63d509570fd2bc44)

**Observed change.** Adds Keyed concept and abstract Registry lookup, throwing lookup and iteration, initially storing T values under borrowed string_view keys.

**Causal interpretation.** Establishes a public lookup abstraction before concrete native backing; abstract Enchantment storage later requires unique_ptr574.

**Limits.** Borrowed key lifetime and concrete iterator representation remain API constraints; no registry tests.

<a id="commit-564"></a>
### Commit 564 {#commit-564}

625b13d38be0d5707b2926e6236e69d639f2a600 · 2025-05-02T08:41:44Z

[Merge remote-tracking branch 'origin/main' into fork/killcerr/test-local](https://github.com/EndstoneMC/endstone/commit/625b13d38be0d5707b2926e6236e69d639f2a600)

**Observed change.** Merges new Registry API into killcerr's enchantment branch; two changed files exactly equal imported parent.

**Causal interpretation.** Preserves contributor work while integrating the shared abstraction.

**Limits.** No independent implementation credit for merge repetition.

<a id="commit-565"></a>
### Commit 565 {#commit-565}

a03600a9660c5d28e12e6b0789769e33bad2546a · 2025-05-02T08:47:14Z

[refactor: rework the Enchantment interface](https://github.com/EndstoneMC/endstone/commit/a03600a9660c5d28e12e6b0789769e33bad2546a)

**Observed change.** Replaces killcerr's41 static numeric enchantment constants with an abstract key/max-level/conflicts/item-applicability interface.

**Causal interpretation.** Moves API consumers toward descriptive identifiers and native behavior rather than raw protocol numbers.

**Limits.** Public API redesign by Vincent builds on killcerr's feature; not blanket Vincent authorship of the branch.

<a id="commit-566"></a>
### Commit 566 {#commit-566}

191a978ffc7c92e7f0846b75182b75d0af7dd627 · 2025-05-02T08:51:07Z

[feat: add `Server::getEnchantmentRegistry`](https://github.com/EndstoneMC/endstone/commit/191a978ffc7c92e7f0846b75182b75d0af7dd627)

**Observed change.** Adds Server::getEnchantmentRegistry reference accessor and corresponding mock method.

**Causal interpretation.** Exposes registry through server ownership rather than constructing it in plugins.

**Limits.** Interface alone does not initialize storage; endpoint still has TODO.

<a id="commit-567"></a>
### Commit 567 {#commit-567}

be074c3ceac2a3958fcc2874dc63a5e20e9aa476 · 2025-05-02T17:01:49Z

[feat: add `endstone::core::EndstoneRegistry` implementation](https://github.com/EndstoneMC/endstone/commit/be074c3ceac2a3958fcc2874dc63a5e20e9aa476)

**Observed change.** Adds lazy EndstoneRegistry adapter/cache plus custom iterators and conversion callback.

**Causal interpretation.** Attempts on-demand wrapping of native registry entries. Inspection finds custom iterator return types incompatible with base iterator aliases, keys() temporary iterator lifetime, pointer/reference callback mismatch and constness issues.

**Limits.** Template is not instantiated in reviewed endpoint; these are source-level incomplete-design conditions, not observed compiler/runtime failures. noexcept allocation can terminate.

<a id="commit-568"></a>
### Commit 568 {#commit-568}

7141737306e92b1f29f1f63a416dd9c3778071a9 · 2025-05-03T16:07:25Z

[feat: add `Enchant` class](https://github.com/EndstoneMC/endstone/commit/7141737306e92b1f29f1f63a416dd9c3778071a9)

**Observed change.** Models native Enchant vtable/enums/slot masks/fields with168/144-byte assertions.

**Causal interpretation.** Introduces backing native schema needed for public wrapper operations.

**Limits.** Native implementation remains proprietary/external; no layout validation.

<a id="commit-569"></a>
### Commit 569 {#commit-569}

cea8c55244b0808f03ec10d2eecf1f2d5105d6db · 2025-05-03T19:24:00Z

[feat: implement `Enchant::canEnchant`](https://github.com/EndstoneMC/endstone/commit/cea8c55244b0808f03ec10d2eecf1f2d5105d6db)

**Observed change.** Implements native canEnchant: allow_non_vanilla accepts all; NONE slot rejects; otherwise primary/secondary bitmask intersection accepts.

**Causal interpretation.** Keeps permissive bypass separate from normal slot eligibility.

**Limits.** Does not by itself enforce conflicts, level bounds or disabled state. No gameplay test.

<a id="commit-570"></a>
### Commit 570 {#commit-570}

2cf1cd2bcc5b461a542f907ee10f87418ccbd732 · 2025-05-03T19:24:15Z

[feat: add `endstone::core::EndstoneEnchantment` implementation](https://github.com/EndstoneMC/endstone/commit/2cf1cd2bcc5b461a542f907ee10f87418ccbd732)

**Observed change.** Adds EndstoneEnchantment with owned key and borrowed native Enchant reference; forwards max level and checks native item slot; initial conflictsWith returns compatibility directly.

**Causal interpretation.** Connects public interface to native schema but initially inverts the documented conflict meaning.

**Limits.** 571 corrects negation. Item conversion/invalid-item dereference and borrowed native lifetime are not tested.

<a id="commit-571"></a>
### Commit 571 {#commit-571}

de35b1fcf4b4f9048ddca3dfb65dc5a67d07d418 · 2025-05-03T19:25:28Z

[fix: correct logic in enchantment conflict check](https://github.com/EndstoneMC/endstone/commit/de35b1fcf4b4f9048ddca3dfb65dc5a67d07d418)

**Observed change.** Negates native isCompatibleWith result in conflictsWith.

**Causal interpretation.** Corrects semantic polarity immediately after570.

**Limits.** No conflict-matrix tests.

<a id="commit-572"></a>
### Commit 572 {#commit-572}

1c9fbde1a399096bde37be6fae7c720bb700732b · 2025-05-03T19:27:26Z

[refactor: rename `TAG_ENCH` to `TAG_ENCHANTS`](https://github.com/EndstoneMC/endstone/commit/1c9fbde1a399096bde37be6fae7c720bb700732b)

**Observed change.** Renames native TAG_ENCH constant to TAG_ENCHANTS at declarations/definitions/uses while keeping literal ench.

**Causal interpretation.** Naming consistency without persistence-format migration.

**Limits.** Mechanical identifier change verified in full diff.

<a id="commit-573"></a>
### Commit 573 {#commit-573}

47ea0cc640cbd208c0197a88cfa6924a612523b2 · 2025-05-05T10:24:30Z

[test: simplify test mocks with direct inheritance from `EndstoneServer`](https://github.com/EndstoneMC/endstone/commit/47ea0cc640cbd208c0197a88cfa6924a612523b2)

**Observed change.** Temporarily derives test mocks from EndstoneServer, removing repeated pure-interface mock declarations; loader keeps logger override and scheduler mock is empty.

**Causal interpretation.** Attempts lower boilerplate during Server API growth; concrete-server coupling cost becomes relevant.

**Limits.** 574 replaces this approach with shared abstract mocks. No tests run.

<a id="commit-574"></a>
### Commit 574 {#commit-574}

a2ae5683b8a0a39d337a5c898e0e29405c63192b · 2025-05-05T11:19:18Z

[fix: compilation errors](https://github.com/EndstoneMC/endstone/commit/a2ae5683b8a0a39d337a5c898e0e29405c63192b)

**Observed change.** Changes Registry stored value to unique_ptr and cache alias, adds server registry member/getter but leaves initialization TODO. Replaces temporary concrete mocks with shared mocks.h using abstract Server; loader uses NiceMock/member ownership and drops exact logger Times(2) expectation.

**Causal interpretation.** Reduces duplicated test scaffolding and a brittle incidental call-count expectation while retaining plugin/scheduler behavior assertions; this is a maintainability/coverage tradeoff, not automatically defective test removal.

**Limits.** No actual compile success verified despite title. Registry is still not initialized and custom adapter defects remain.

<a id="commit-578"></a>
### Commit 578 {#commit-578}

e7a314799c30c651c4c6ff6ff732382f561d43e8 · 2025-05-07T15:40:14Z

[Merge remote-tracking branch 'origin' into fork/killcerr/test-local](https://github.com/EndstoneMC/endstone/commit/e7a314799c30c651c4c6ff6ff732382f561d43e8)

**Observed change.** Merges current main into enchantment branch;56 of57 entries exactly equal imported parent. Mixed server.cpp retains registry TODO/getter while adding real pack-provider construction.

**Causal interpretation.** Combines independent feature ownership and ABI work explicitly in the only mixed file.

**Limits.** Both-parent residuals read; no repeated semantic credit for imported work.

<a id="commit-579"></a>
### Commit 579 {#commit-579}

ec57508defb1e955e04c992ce0c54dc7ebd8b203 · 2025-05-07T15:57:01Z

[feat: add methods to retrieve all vanilla enchants](https://github.com/EndstoneMC/endstone/commit/ec57508defb1e955e04c992ce0c54dc7ebd8b203)

**Observed change.** Adds Windows native Enchant::mEnchants symbol/access. Initial getEnchants allocates result with native size then appends each pointer, creating leading null entries; name lookup dereferences entries.

**Causal interpretation.** A concrete adapter defect introduced during feature wiring, later replaced582; preserve revision rather than only final code.

**Limits.** No crash observed. Linux symbol support follows582.

<a id="commit-580"></a>
### Commit 580 {#commit-580}

9460cba64d86ca3d28efa8ec9609e67ac2d2dddd · 2025-05-07T16:29:17Z

[refactor: improve enchantment handling in `ItemMeta`](https://github.com/EndstoneMC/endstone/commit/9460cba64d86ca3d28efa8ec9609e67ac2d2dddd)

**Observed change.** ItemMeta enchantments become string→int map, included in isEmpty; display name/lore normalize empty to absent; add/get/remove methods replace numeric optional map. addEnchant ignores force/level validation TODO.

**Causal interpretation.** Refines killcerr's raw numeric API to descriptive identifiers and simpler empty-state representation.

**Limits.** Unknown IDs/levels remain accepted; return old==0 || old!=level can report change for repeated level0. No validation tests.

<a id="commit-581"></a>
### Commit 581 {#commit-581}

6b69fa09a24282caeeeda5a9b9b43dbb2ee5c4f4 · 2025-05-07T16:58:56Z

[feat: update python bindings](https://github.com/EndstoneMC/endstone/commit/6b69fa09a24282caeeeda5a9b9b43dbb2ee5c4f4)

**Observed change.** Publishes Python string-key enchant APIs, readonly copied enchants dictionary, methods and force defaultfalse; removes direct property setter.

**Causal interpretation.** Aligns Python surface with redesigned C++ metadata while keeping mutation through explicit methods.

**Limits.** No binding/import tests; API compatibility changes must be visible to users.

<a id="commit-582"></a>
### Commit 582 {#commit-582}

24b6179b4b737abffcb432c5e417aa52487d209b · 2025-05-07T17:57:13Z

[feat: add Enchant::getEnchant](https://github.com/EndstoneMC/endstone/commit/24b6179b4b737abffcb432c5e417aa52487d209b)

**Observed change.** Adds Linux Enchant table symbol, replaces579's null-prefilled pointer vector with native unique_ptr vector access, and adds enum lookup guard.

**Causal interpretation.** Fixes the intermediate null-vector construction by borrowing native storage, but initially returns unique_ptr vector by value.

**Limits.** 584 fixes return to const reference. Guard uses > NumEnchantments, permitting sentinel41 to reach at(41); malformed signed IDs cast to small enum can wrap.

<a id="commit-583"></a>
### Commit 583 {#commit-583}

168002abdb356be27442bfc5d8ac3ef54a4098bc · 2025-05-07T18:14:22Z

[feat: add `NamespacedKey`](https://github.com/EndstoneMC/endstone/commit/168002abdb356be27442bfc5d8ac3ef54a4098bc)

**Observed change.** Adds NamespacedKey parsing/validation/lowercasing, string rendering and hash combination.

**Causal interpretation.** Separates namespace/key syntax for registry-facing identifiers. Unqualified uppercase is rejected before create whereas qualified uppercase gets normalized.

**Limits.** No parser tests; tolower on signed non-ASCII and noexcept allocating toString deserve bounded scrutiny. Later586 stops applying this normalizer to enchant codec.

<a id="commit-584"></a>
### Commit 584 {#commit-584}

44084b7fc3d53398a6972d6d6a2b96cb3540cf85 · 2025-05-07T18:34:21Z

[feat: improving the codec of enchantment tags](https://github.com/EndstoneMC/endstone/commit/44084b7fc3d53398a6972d6d6a2b96cb3540cf85)

**Observed change.** Defines native string-ID/type getters, returns enchant vector by const reference, and validates NBT id/lvl short tags before conversion. Codec normalizes namespaced keys but serializes using only key portion.

**Causal interpretation.** Repairs move-only vector copying and rejects wrong-tag shapes before native lookup; maps serialized short IDs to API strings.

**Limits.** Enum sentinel boundary remains; namespace is discarded in serialization lookup; force/level limits still TODO.

<a id="commit-585"></a>
### Commit 585 {#commit-585}

2c44952c2b57b450449ba66e8455e7b92c3d64eb · 2025-05-07T18:41:30Z

[feat(enchant): add basic enchant api (#177)](https://github.com/EndstoneMC/endstone/commit/2c44952c2b57b450449ba66e8455e7b92c3d64eb)

**Observed change.** Merges basic enchant API PR177;26 changed entries exactly equal reviewed branch parent. Commit says completes issue103.

**Causal interpretation.** Preserves killcerr's initial feature, smartcmd's pyi request, Vincent's extensive wrapper/registry/API revisions and exact merge provenance. Issue103 requested names/levels for damage calculations.

**Limits.** Completed feature statement does not imply all registry paths work: endpoint initialization and adapter concerns are separately recorded.
