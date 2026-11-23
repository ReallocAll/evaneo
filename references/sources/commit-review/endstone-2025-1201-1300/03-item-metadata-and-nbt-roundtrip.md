<!-- retrieval: {"source_ids":["public:commit:09a6c2c00f39b4d6265f84943ca8945c44d88e45","public:commit:1060cef1e57fc69c1d1ff0efb5b4e8d8f0f7c39c","public:commit:1a528588a194b217bb3c377468cb6bfbfadba64d","public:commit:326ac3b5c38f3ef4e53ce1990f52180083746aac","public:commit:4939fd4bf31a705f59c757f7ab15d8205069a8af","public:commit:6cfcdc8630f151a599bd4059b2bd1c5f4c8afa65","public:commit:73725113aa7b2f10618201f4d71770ddda57bc43","public:commit:8a887da9505bb35bb87496edc858f329cd980a90","public:commit:92a4535846fd58c065e43290c52ea155cf29b134","public:commit:93438eec2fb946d9d08535e0f9eb289fd7a90583","public:commit:add1092a85b7b1b44af7ff1378eb1b33e5b1ecb2","public:commit:c6ad0b40be3edb4ab0aae368e9722436dc166569","public:commit:e8ab74f465de4c267eda8640be7ef1a76aef2183","public:commit:e99cc6d4e845523d10683dfcf19b2b304765c20e","public:commit:f273867ae87a2404f511dbc3fe1f58cbb16e4f60","public:commit:f68fe6c88174a9009c018d11085a71be483c85b4"],"source_type":"public","date":"2025-11-09..2025-11-14","topics":["lifetime","ffi","testing","build","api","diagnosis","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Item metadata and NBT round-trip {#item-metadata-and-nbt-round-trip}

## Design reversal and implementation {#design-reversal-and-implementation}

1243–1247 reverse the earlier public value-metadata design: ItemMeta and MapMeta become abstract interfaces, with concrete templated EndstoneItemMetaBase implementations plus a separate ItemMetaExtras contract. Native serialization details move behind these interfaces. Map-specific notUncommon comparison is restored after the earlier value design had omitted it. The staged const mutator, private remnants and stale include are repaired in1246. The rationale beyond the refactor labels is not stated.

The concrete factory nevertheless casts arbitrary ItemMeta objects to EndstoneItemMeta, while EndstoneMapMeta is a sibling specialization of EndstoneItemMetaBase<MapMeta>. The templated copy/equality paths similarly cast to the current specialization. That is a stronger assumption than the abstract API guarantees. The evidence is a static type-hierarchy contradiction, not an observed crash.

The complete setItemMeta function matters: an initial equals(meta,nullptr) branch clears user data for null or genuinely empty metadata. The later nonempty-only application does not establish that empty input leaves old fields intact. Nonempty adaptation clones existing native NBT before replacing recognized fields, preserving unrelated tags; conversion to a specialized type that becomes empty can reach the later skip. This corrects a concern raised by reading only the changed hunk.

1258–1263 adopt typed ItemId and EnchantmentId. Plain ItemStack construction accepts unknown types by leaving air and loses C++ constructor amount validation; the Python constructor restores1..255 checking in1260. Owned native ItemInstance storage survives the NBT factory's local temporary:1288 copies it into EndstoneItemStack rather than retaining a reference. This does not validate native reinit or inventory synchronization.

1285–1288 build recursive conversion between public variant NBT and native tags, then add toNbt/fromNbt. Plain ItemStack writes Name/Count/Damage and interpreted metadata. The native wrapper additionally preserves arbitrary user data, serialized block state, pickup state and CanPlaceOn/CanDestroy lists. Serialized names strip a raw .tile suffix. The factory calls native ItemInstance::fromTag and always returns a wrapper; its documented nullptr-on-invalid contract is not implemented by a local validity check. Native setUserData is reimplemented locally to maintain the charged-item cache. Native offsets and binary behavior are unvalidated.

1291 adds written/writable book and crossbow interfaces only. The concrete adapters and Python exports are absent at1300. Variadic page helpers take addresses of arguments when forming vector<string>; setTitle is void while its comment describes a success result. These staged contracts should not be claimed as completed working features.

## Tests and usage {#tests-and-usage}

NBT container tests are substantial, but no native item round-trip test is added here. Use this chain when preserving unknown serialization fields, separating API interfaces from native backing, or auditing ownership across a factory return. Check concrete casts and validity contracts alongside value storage; a copied native handle does not prove every conversion and specialized metadata operation is safe.

## Per-commit decisions and revisions {#per-commit-decisions-and-revisions}

<a id="commit-1243"></a>
### Commit 1243 {#commit-1243}

[73725113aa7b](https://github.com/EndstoneMC/endstone/commit/73725113aa7b2f10618201f4d71770ddda57bc43) · 2025-11-09T23:12:30Z · refactor: make `ItemMeta` and `MapMeta` pure abstract interfaces

ItemMeta/MapMeta switch public value classes to abstract interfaces; removes public isEmpty and implementation/constructors, adds conflict query and tagged downcast macro. Intermediate private data remnants and const mutator repaired1246. This reverses earlier1070 public-value design.

<a id="commit-1246"></a>
### Commit 1246 {#commit-1246}

[e99cc6d4e845](https://github.com/EndstoneMC/endstone/commit/e99cc6d4e845523d10683dfcf19b2b304765c20e) · 2025-11-10T23:21:27Z · refactor: revamp `ItemMeta` with a full redesign

Concrete templated metadata classes move native serialization behind abstract interfaces plus ItemMetaExtras. Restores map-specific notUncommon equality, clones concrete values, removes const addEnchant. Factory and copy/equality implementations static_cast ItemMeta to EndstoneItemMeta or current template specialization; MapMeta is a sibling specialization, so this assumption needs endpoint qualification. Applying nonempty meta clones unknown native NBT. Endpoint full-function check corrects the partial-diff concern: the initial equals(meta,nullptr) branch clears user data for genuinely empty metadata as well as null. Only metadata that becomes empty during type adaptation reaches the later skip. No runtime tests.

<a id="commit-1247"></a>
### Commit 1247 {#commit-1247}

[6cfcdc8630f1](https://github.com/EndstoneMC/endstone/commit/6cfcdc8630f151a599bd4059b2bd1c5f4c8afa65) · 2025-11-10T23:24:02Z · refactor: adjust polymorphic_type_hook

Polymorphic ItemMeta hook explicit Item case falls through to base type, Map remains specialized; no ownership policy change.

<a id="commit-1257"></a>
### Commit 1257 {#commit-1257}

[add1092a85b7](https://github.com/EndstoneMC/endstone/commit/add1092a85b7b1b44af7ff1378eb1b33e5b1ecb2) · 2025-11-11T19:20:23Z · feat: add `Air` constant to `ItemType` and update comparison operators to use `ItemId`

ItemType gains Air typed constant and Identifier comparison, avoiding plain string comparison signature.

<a id="commit-1258"></a>
### Commit 1258 {#commit-1258}

[f68fe6c88174](https://github.com/EndstoneMC/endstone/commit/f68fe6c88174a9009c018d11085a71be483c85b4) · 2025-11-11T19:59:58Z · refactor: replace `std::string` with `ItemId` in `ItemStack` and related APIs

ItemStack accepts ItemId constructor, removes Result create factory and its amount validation, temporarily returns ItemType reference with air fallback; unknown C++type silently leaves emptyair. Python validates known type but amount bound temporarily lost. Factory/meta APIs typed and native reinit uses owning conversion.1260 restores Python amount checks; C++constructor remains unchecked.

<a id="commit-1259"></a>
### Commit 1259 {#commit-1259}

[f273867ae87a](https://github.com/EndstoneMC/endstone/commit/f273867ae87a2404f511dbc3fe1f58cbb16e4f60) · 2025-11-11T20:30:43Z · feat: add pybind11 type_caster for `endstone::Identifier`

Identifier Python caster initially stores views into local std::string caster, lifetime ends on load return;1260 changes to Python-backed string_view. Empty key converts to empty string while formatter still namespace:key. Repairs registry argument name; updates interim ItemType stub.

<a id="commit-1260"></a>
### Commit 1260 {#commit-1260}

[4939fd4bf31a](https://github.com/EndstoneMC/endstone/commit/4939fd4bf31a705f59c757f7ab15d8205069a8af) · 2025-11-11T20:55:50Z · refactor: use `std::string_view` in type_caster and improve `ItemStack` validation logic

Python ItemStack constructor restores1..255bound and Unknown item type wording. Identifier caster uses string_view instead of local owning string, avoiding immediate temporary-storage loss for normal Python strings; cross-call retention still borrowed.

<a id="commit-1261"></a>
### Commit 1261 {#commit-1261}

[09a6c2c00f39](https://github.com/EndstoneMC/endstone/commit/09a6c2c00f39b4d6265f84943ca8945c44d88e45) · 2025-11-11T21:08:48Z · refactor: rename generic type `T` to `_T`

Generic stub variable T renamed_T in Registry and generator; Server.get_registry signature is not updated in this patch and still refersT until later stub refresh.

<a id="commit-1262"></a>
### Commit 1262 {#commit-1262}

[326ac3b5c38f](https://github.com/EndstoneMC/endstone/commit/326ac3b5c38f3ef4e53ce1990f52180083746aac) · 2025-11-11T21:28:06Z · refactor: replace `ItemType` with `ItemId` in `ItemStack::getType`

Reverses temporary ItemType-returning stack API to ItemId; Python returnsstr again. Translation/maxsize use private registry-backed helper with air fallback, type storage remains owningstd::string.

<a id="commit-1263"></a>
### Commit 1263 {#commit-1263}

[92a4535846fd](https://github.com/EndstoneMC/endstone/commit/92a4535846fd58c065e43290c52ea155cf29b134) · 2025-11-11T21:39:01Z · refactor: replace `std::string` with `EnchantmentId` in enchantment-related APIs

Enchantment lookup/mutation APIs accept typed IDs; loading native tags normalizes IDs into owningstring map. Serialization now passes full namespaced string to native getEnchantFromName, while registry path strips key; endpoint native implementation compares HashedString IDs exactly and performs no normalization. The two caller forms are observably inconsistent; the external enchantment table contents were not observed, so actual lost-enchantment behavior is unvalidated.

<a id="commit-1269"></a>
### Commit 1269 {#commit-1269}

[c6ad0b40be3e](https://github.com/EndstoneMC/endstone/commit/c6ad0b40be3edb4ab0aae368e9722436dc166569) · 2025-11-12T12:33:57Z · refactor: update `ItemMeta::getEnchants` to use `Enchantment` as key type

getEnchants now returns Enchantment-pointer-keyed maps resolved through registry without null filtering; adds C++/Python equality and Python string conversion. No explicit Python hash binding accompanies equality; mapping-key behavior requires runtime verification.

<a id="commit-1284"></a>
### Commit 1284 {#commit-1284}

[1a528588a194](https://github.com/EndstoneMC/endstone/commit/1a528588a194b217bb3c377468cb6bfbfadba64d) · 2025-11-13T19:00:54Z · refactor(item_stack): mark `getItemType` method as `[[nodiscard]]`

Adds nodiscard to private ItemStack type-registry helper. No behavior change beyond compiler diagnostics.

<a id="commit-1286"></a>
### Commit 1286 {#commit-1286}

[1060cef1e57f](https://github.com/EndstoneMC/endstone/commit/1060cef1e57fc69c1d1ff0efb5b4e8d8f0f7c39c) · 2025-11-14T15:40:16Z · feat(nbt): add `ItemStack::toNbt`

Adds public and native ItemStack::toNbt, plus ItemMeta::toNbt. Public stack serializes Name/Count/Damage and interpreted metadata; native stack preserves complete user data through recursive conversion. Qualifies native NBT names after public aliases are added and fixes1285 header linkage declarations.

<a id="commit-1287"></a>
### Commit 1287 {#commit-1287}

[8a887da9505b](https://github.com/EndstoneMC/endstone/commit/8a887da9505bb35bb87496edc858f329cd980a90) · 2025-11-14T19:08:51Z · feat(nbt): extend `ItemStack::toNbt` with additional fields

Native item serialization uses namespace plus raw name with .tile suffix stripped, and includes WasPickedUp, block serialization, CanPlaceOn/CanDestroy and user data. Plain public stack serialization remains a smaller schema; no equality-of-all-native-state promise.

<a id="commit-1288"></a>
### Commit 1288 {#commit-1288}

[e8ab74f465de](https://github.com/EndstoneMC/endstone/commit/e8ab74f465de4c267eda8640be7ef1a76aef2183) · 2025-11-14T20:06:20Z · feat(nbt): add `ItemStack::fromNbt`

Adds ItemStack::fromNbt via server ItemFactory and native ItemInstance::fromTag; returned EndstoneItemStack owns copied native state. Factory always returns wrapper even though API docs promise nullptr for invalid input. setUserData now locally updates charged-item cache rather than calling native symbol. Also updates BDS1.21.123 tables and adds fromTag/removes setUserData symbols; no runtime ABI/roundtrip test.

<a id="commit-1291"></a>
### Commit 1291 {#commit-1291}

[93438eec2fb9](https://github.com/EndstoneMC/endstone/commit/93438eec2fb946d9d08535e0f9eb289fd7a90583) · 2025-11-14T21:16:54Z · feat(meta): add `BookMeta`, `WritableBookMeta`, and `CrossbowMeta`

Adds abstract BookMeta/WritableBookMeta/CrossbowMeta contracts and enum tags/umbrella includes; no concrete adapters or Python exports yet. Variadic page helpers construct vector<string> from &pages rather than forwarded values; title docs claim boolean result but setter is void, page limits differ by operation. These are staged API/source contradictions.
