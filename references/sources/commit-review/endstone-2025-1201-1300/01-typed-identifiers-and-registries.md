<!-- retrieval: {"source_ids":["public:commit:0e5d525323e56574ef7f984af6801e9c76e00ff8","public:commit:0fe098ffc5499997105e765f84c87016c3bbb080","public:commit:14df5d638bcdc1f3af85292b1dfb2c7764073978","public:commit:2601786032d80d330aaf4211c4eb664ad613b005","public:commit:261cc36e1234edd81f333da75d8254a0883e0201","public:commit:30e36f99b56e0d64bb9656448be41de2039dc491","public:commit:3eee3292306bf159c88fc4278d8946c3d8ec7a94","public:commit:43429578ee49a17f5682569a0a97c36e33d73a75","public:commit:4aed1e3e788ef52a349612246149cad53165910f","public:commit:581d1721133deaf594d55bb3f8889c7ded873b3d","public:commit:5be76ecfd519ed3d83c759f6b08c68498638a0a9","public:commit:673125ba82c7536e3b471ace91db75cfde540d1f","public:commit:737b46d8a84dda6def7cdabaf549dd4aa91af51d","public:commit:84502e70d3df057ab44275f23563ca8dadd269e0","public:commit:8f1a3c1d3587a77d392636662e5019bab0aafdd7","public:commit:97a8689ca19742c750b86acf1ed2bf152afa7850","public:commit:9a7f5d82115bea4060c70c3e0f3e97e65c74e783","public:commit:b6a674cffde88cf0fd91b9d241f2f5cbc1bb2b29","public:commit:c17a457efffb3ee04502127d0709dcf79c90685b","public:commit:c8d5319ee2fb87b269696a20444e4a814e1735f2","public:commit:cb1e7b2b270255f9d47b9cb8fbf307e5b94088db","public:commit:d0f9a479755fd76872c211202576d2ce5d3c91b1","public:commit:d6e9f54fcb7aa2770da4d890fb36207b3c332ee4","public:commit:e9bb88512792ce018c80fbf2e5d9cb88f93171c7","public:commit:ed4bdb1bbeb5f50e681658ca33021c1f8e685f46","public:commit:ffd9af31d557f4548466705dff089b66036fe257"],"source_type":"public","date":"2025-11-06..2025-11-11","topics":["lifetime","ffi","testing","build","api","documentation","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Typed identifiers and registries {#typed-identifiers-and-registries}

## Evolution and reasons {#evolution-and-reasons}

The main branch first exposes string constants for attributes, potions, enchantments and effects (1207–1226), passing through an X-macro, explicit names, constexpr views and owning namespaced strings. These are actual reversals, not one timeless preference. The initial extra macro argument and uninitialized constexpr potion declarations are staged source inconsistencies repaired in following commits. No compiler or generator was run in this review.

The generic Registry transition (1221–1227) replaces separate server entry points with a type-name keyed internal registry map and a templated C++ facade. Python initially compares a class name and then changes to exact bound-type identity, which rejects an unrelated same-name class. The Python stub still advertises a nonoptional Registry although unsupported types return None; the C++ reference facade assumes the internal registry exists. AttributeInstance exposes a contract and modifier operations but this slice does not supply a concrete actor attribute adapter. Constants and interfaces should not be presented as implemented effect application.

1250–1256 consolidate the families into Identifier<T>. The type parameter prevents mixing unrelated identifier families at C++ API boundaries; namespace and key remain borrowed string_views. Parsing uses the last colon and defaults to minecraft. Static constants are lifetime-safe literals, while the std::string constructor does not retain a temporary or caller-owned string. Five authored tests and constexpr assertions cover literal parsing, equality and string conversion, not that dynamic-storage boundary. This is an observed type-safety/lifetime tradeoff; no explicit rationale for all reversals was given.

The Python caster revision is important:1259 first leaves views into a local owning std::string, and1260 switches to string_view conversion backed by normal Python string storage. That removes the immediate local-string problem for ordinary arguments but does not make the C++ identifier owning.1260 also restores Python ItemStack amount checks after1258 temporarily removed them. The final stack API returns ItemId (Python str), reversing its short-lived ItemType-reference result.

## Limits and attribution {#limits-and-attribution}

The target commits are authored by Vincent. Imported changes retain their original authorship in prior-target-reuse.json. Enchantment native lookup deliberately receives only id.getKey in the registry, so the namespace is not enforced there. The metadata serializer instead supplies the full normalized string to an exact HashedString comparator; these routes differ, but native table contents were not inspected at runtime. Python enchantment objects gain equality without an explicit hash binding while becoming dictionary keys; this is a binding-contract risk requiring runtime verification, not a reported executed failure. Fortune is present among41 C++ constants and absent among40 Python constants at the boundary.

## Where this helps {#where-this-helps}

Use this chain when changing cross-language registries or deciding whether an identifier should own storage. Audit the entire route: storage lifetime, cache key ownership, namespace normalization, unknown lookup behavior, stub optionality and export completeness. Read tests as evidence of the chosen contract and its coverage limits, rather than evidence that a native integration passed.

## Per-commit decisions and revisions {#per-commit-decisions-and-revisions}

<a id="commit-1207"></a>
### Commit 1207 {#commit-1207}

[0fe098ffc549](https://github.com/EndstoneMC/endstone/commit/0fe098ffc5499997105e765f84c87016c3bbb080) · 2025-11-06T22:37:59Z · feat: define attributes in `attribute.def`

Introduces16 attribute constants through three-argument X-macro; movement row has extra GENERIC argument, repaired1209. Initial staged implementation.

<a id="commit-1209"></a>
### Commit 1209 {#commit-1209}

[14df5d638bcd](https://github.com/EndstoneMC/endstone/commit/14df5d638bcdc1f3af85292b1dfb2c7764073978) · 2025-11-06T23:03:59Z · feat(python): add attribute module

Attribute public class, sixteen string constants, Python native bindings/lazy facade/stubs/build integration. Removes extra movement macro argument.

<a id="commit-1210"></a>
### Commit 1210 {#commit-1210}

[e9bb88512792](https://github.com/EndstoneMC/endstone/commit/e9bb88512792ce018c80fbf2e5d9cb88f93171c7) · 2025-11-06T23:42:07Z · feat(attribute): implement `AttributeModifier` and expose relevant methods in `MutableAttributeWithContext`

Native AttributeModifier operation/operand/UUID/serialization layout and forwarder method declarations; bodies not implemented by this commit despite title.

<a id="commit-1211"></a>
### Commit 1211 {#commit-1211}

[9a7f5d82115b](https://github.com/EndstoneMC/endstone/commit/9a7f5d82115bea4060c70c3e0f3e97e65c74e783) · 2025-11-06T23:57:42Z · feat: add `AttributeInstance` and its python bindings

Abstract AttributeInstance base/current/min/max contract and Python properties. No concrete instance adapter or actor retrieval supplied here; modifier TODO.

<a id="commit-1212"></a>
### Commit 1212 {#commit-1212}

[d0f9a479755f](https://github.com/EndstoneMC/endstone/commit/d0f9a479755fd76872c211202576d2ce5d3c91b1) · 2025-11-07T00:38:47Z · feat: add `AttributeModifier` and its python bindings

Public modifier value class exposes name/amount/operation/operand/UUID and abstract instance modifier operations; Python enums and stubs. Default UUID bytes now zero-initialized, so no random uniqueness claim. Exported native-enum aliases lose duplicate docstrings globally, including Criteria.DUMMY.

<a id="commit-1213"></a>
### Commit 1213 {#commit-1213}

[cb1e7b2b2702](https://github.com/EndstoneMC/endstone/commit/cb1e7b2b270255f9d47b9cb8fbf307e5b94088db) · 2025-11-07T00:40:55Z · fix: update module exports

Adds AttributeModifier to lazy facade exports, repairing1212's omission.

<a id="commit-1215"></a>
### Commit 1215 {#commit-1215}

[2601786032d8](https://github.com/EndstoneMC/endstone/commit/2601786032d80d330aaf4211c4eb664ad613b005) · 2025-11-07T15:33:09Z · refactor: replace `attribute.def` with explicit definitions

Replaces X-macro attribute constants with explicit CamelCase C++ definitions and repeated Python bindings; clang-tidy ClassConstantCase changes globally. Same sixteen values; no author rationale beyond refactor title.

<a id="commit-1216"></a>
### Commit 1216 {#commit-1216}

[ffd9af31d557](https://github.com/EndstoneMC/endstone/commit/ffd9af31d557f4548466705dff089b66036fe257) · 2025-11-07T17:22:46Z · feat: add `PotionType`

PotionType scaffold includes initialized water plus many uninitialized constexpr auto declarations; incomplete staging repaired1217.

<a id="commit-1217"></a>
### Commit 1217 {#commit-1217}

[30e36f99b56e](https://github.com/EndstoneMC/endstone/commit/30e36f99b56e0d64bb9656448be41de2039dc491) · 2025-11-08T00:54:49Z · feat(potion): add `PotionType` constants and python bindings

Completes46 potion string IDs including strong slowness, long slow falling and four newer potions; wires native module, lazy facade, stubs and build. Constants identify potion types, no effect-application implementation.

<a id="commit-1218"></a>
### Commit 1218 {#commit-1218}

[581d1721133d](https://github.com/EndstoneMC/endstone/commit/581d1721133deaf594d55bb3f8889c7ded873b3d) · 2025-11-08T01:14:39Z · refactor: use `std::string_view` for `PotionType` and `Attribute` constants

Attribute and potion constants use constexpr string_view; static literal lifetime, type-only change verified across full families.

<a id="commit-1219"></a>
### Commit 1219 {#commit-1219}

[43429578ee49](https://github.com/EndstoneMC/endstone/commit/43429578ee49a17f5682569a0a97c36e33d73a75) · 2025-11-08T17:35:16Z · refactor: use `NamespacedKey` for `PotionType` and `Attribute` constants

Returns constants to owning strings constructed by new NamespacedKey::minecraft helper. Prefix helper preserves minecraft: inputs but prepends others, and potion namespaces include potion_type. No validation here.

<a id="commit-1220"></a>
### Commit 1220 {#commit-1220}

[673125ba82c7](https://github.com/EndstoneMC/endstone/commit/673125ba82c7536e3b471ace91db75cfde540d1f) · 2025-11-08T18:19:04Z · feat: add `Enchantment` constants and corresponding Python bindings

Adds41 C++ enchantment constants and40 Python constants (Fortune absent Python); NamespacedKey splits at last colon. Native enchant registry strips namespaces on lookup and prefixes keys, so arbitrary namespace is not enforced. All values/docs read.

<a id="commit-1221"></a>
### Commit 1221 {#commit-1221}

[3eee3292306b](https://github.com/EndstoneMC/endstone/commit/3eee3292306bf159c88fc4278d8946c3d8ec7a94) · 2025-11-08T21:06:59Z · refactor: simplify `Server::getRegistry`

Replaces separate server registries with IRegistry map and type-name macro, templated getRegistry dereferences cast result. _getRegistry returns null for unknown type, while template reference assumes present. Python initially dispatches by class name; mocks and registry wrappers updated.

<a id="commit-1222"></a>
### Commit 1222 {#commit-1222}

[261cc36e1234](https://github.com/EndstoneMC/endstone/commit/261cc36e1234edd81f333da75d8254a0883e0201) · 2025-11-08T21:13:38Z · refactor: add generic type `Registry`

Hand-authored generic Registry[T] stub hides concrete registry classes and models get as optional. Server.get_registry still annotated nonoptional although runtime unsupported type returnsNone.

<a id="commit-1223"></a>
### Commit 1223 {#commit-1223}

[0e5d525323e5](https://github.com/EndstoneMC/endstone/commit/0e5d525323e56574ef7f984af6801e9c76e00ff8) · 2025-11-08T21:29:43Z · feat: add generic type support to stubgen

Stub generator injects generic type variable/Registry and Server.get_registry signature from package; removes concrete *Registry exports. Generator not run.

<a id="commit-1224"></a>
### Commit 1224 {#commit-1224}

[ed4bdb1bbeb5](https://github.com/EndstoneMC/endstone/commit/ed4bdb1bbeb5f50e681658ca33021c1f8e685f46) · 2025-11-08T21:30:28Z · refactor: update docstring for `get_registry` method in stub

Corrects get_registry stub documentation from enchantment-specific to arbitrary given type.

<a id="commit-1225"></a>
### Commit 1225 {#commit-1225}

[5be76ecfd519](https://github.com/EndstoneMC/endstone/commit/5be76ecfd519ed3d83c759f6b08c68498638a0a9) · 2025-11-08T21:37:06Z · feat: add new Python doc reference pages for `Attribute`, `Map`, and `Potion`

Adds attribute/map/potion reference pages and navigation; miscellaneous page switches to genericRegistry. Documentation plumbing, no runtime test.

<a id="commit-1226"></a>
### Commit 1226 {#commit-1226}

[737b46d8a84d](https://github.com/EndstoneMC/endstone/commit/737b46d8a84dda6def7cdabaf549dd4aa91af51d) · 2025-11-08T22:16:28Z · feat(effect): add `EffectType` constants and Python bindings

Adds36 effect ID constants with C++ descriptions, Python module/bindings/lazy facade/stubs/build registration. No effect application implementation; authored descriptions are not external fact validation.

<a id="commit-1227"></a>
### Commit 1227 {#commit-1227}

[4aed1e3e788e](https://github.com/EndstoneMC/endstone/commit/4aed1e3e788ef52a349612246149cad53165910f) · 2025-11-08T23:06:32Z · refactor: simplify Python `get_registry` method implementation

Python registry dispatch now compares exact pybind type identity rather than __name__, preventing same-name impostors; unsupported types stillNone and registry lifetime assumption remains.

<a id="commit-1250"></a>
### Commit 1250 {#commit-1250}

[c8d5319ee2fb](https://github.com/EndstoneMC/endstone/commit/c8d5319ee2fb87b269696a20444e4a814e1735f2) · 2025-11-11T17:23:51Z · refactor: replace `NamespacedKey` with `Identifier` and update usages

Introduces typed Identifier<T> with borrowed namespace/key string_views, last-colon parsing/defaultMinecraft namespace, equality and string conversion. Replaces all attribute/effect/enchantment/potion constants preserving literals and potion_type namespace. Enchantment adapter returns view over owned ID; arbitrary runtime input lifetimes remain caller obligation.

<a id="commit-1251"></a>
### Commit 1251 {#commit-1251}

[b6a674cffde8](https://github.com/EndstoneMC/endstone/commit/b6a674cffde88cf0fd91b9d241f2f5cbc1bb2b29) · 2025-11-11T18:05:03Z · feat: add string-based constructor for `Identifier`

Adds std::string constructor delegating to string_view and fmt formatter; constructor borrows rather than owns supplied string.

<a id="commit-1252"></a>
### Commit 1252 {#commit-1252}

[8f1a3c1d3587](https://github.com/EndstoneMC/endstone/commit/8f1a3c1d3587a77d392636662e5019bab0aafdd7) · 2025-11-11T18:09:12Z · refactor: replace key-based lookups with identifier-based API across Registry classes

Registry APIs become typed identifiers; server factories simplified, native item names normalized through typed IDs, caches retain owning string keys. Enchantment backend still ignores namespace. Python get/item lookup now const with KeyError, temporary argument label typo repaired1259.

<a id="commit-1253"></a>
### Commit 1253 {#commit-1253}

[84502e70d3df](https://github.com/EndstoneMC/endstone/commit/84502e70d3df057ab44275f23563ca8dadd269e0) · 2025-11-11T18:13:57Z · feat: add string_view comparison operators to `Identifier`

Adds explicit string_view comparison overloads by parsing other; later1254 removes in favor implicit identifier construction.

<a id="commit-1254"></a>
### Commit 1254 {#commit-1254}

[97a8689ca197](https://github.com/EndstoneMC/endstone/commit/97a8689ca19742c750b86acf1ed2bf152afa7850) · 2025-11-11T18:28:14Z · feat: add unit tests for `Identifier`

Adds5Identifier tests plus constexpr assertions for literal/default namespace/equality/string conversion; switches to const char* constructor, removes explicit comparisons. Does not test dynamic temporary string lifetime or malformed names.

<a id="commit-1255"></a>
### Commit 1255 {#commit-1255}

[d6e9f54fcb7a](https://github.com/EndstoneMC/endstone/commit/d6e9f54fcb7aa2770da4d890fb36207b3c332ee4) · 2025-11-11T18:40:40Z · refactor: rename test cases in `IdentifierTest` for consistency

Renames test suite consistently to IdentifierTest, expectations unchanged.

<a id="commit-1256"></a>
### Commit 1256 {#commit-1256}

[c17a457efffb](https://github.com/EndstoneMC/endstone/commit/c17a457efffb3ee04502127d0709dcf79c90685b) · 2025-11-11T18:45:38Z · feat: add std::string-based constructor to `Identifier`

Restores constexpr std::string constructor alongside char*; still a borrowed view.
