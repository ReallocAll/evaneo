<!-- retrieval: {"source_ids":["public:commit:0bc48f0851cdb51318d7de52a2841fd7b7a86309","public:commit:1093250547f3c9af64d164bac38d7d22c6e8123f","public:commit:1506cbf7e7e5915e1aa9ea9fdf8b5592c1ad4b23","public:commit:198993e0462970907c24fa154ea3b900ab6d72fa","public:commit:1e921d85bf7090d66d9c34eb92cb573124096fc5","public:commit:2460fc28ff33200b3a6fe062194c003d7a2078ee","public:commit:27bced163dc91c6266a189f6a3e8439846741bf8","public:commit:2d2834dbf5c3cf3878d5d825bbb4a86dfadc5529","public:commit:3203d872694fe55179f650fa8d3c4d36c3ad0c5a","public:commit:3669991268ed4939747498c881ee184eb3959b48","public:commit:37a3459dcb51122d917457953eaf5544bf581e29","public:commit:3dcde3c8475100fbbec6d87f25dfceb7e148220b","public:commit:3fb444c11efb6ffcd6ad262c5f17afefc18d4438","public:commit:499369dbde0a46077dcb66153a233db76cc49d44","public:commit:7287010f44b4ead4f4ec5ad3b79073ae194a26d9","public:commit:734e6ce1baa128d4e56158766e079f3425d20bcd","public:commit:85ac189f24d4993abd7fd39b578a468af1f38499","public:commit:8fb1e32f6d5f8a4dac7fe6a227c89b38ab580fb4","public:commit:90a778c940a8e0fd52f86ce9ada699fe63dfb420","public:commit:9cdb0113943e815726de00c4464a5625fab5f555","public:commit:a9e8ddfedbed404ac4d5752cbc417576a6a9e5bf","public:commit:b6daee8f3d3081cff58cfe0237d7e122d5ba3098","public:commit:ba6e3edca190bdb075809e75f256d4f7de1c4f64","public:commit:bd3cf022b572bc4452ef84e7b9f4df769529cfe4","public:commit:c4bfdbfaed1cd5ba392536c95301fb987d7af956","public:commit:c598c7ef0ad4dd52183a549bbb2aac325fc59697","public:commit:c6f334451a9e51525fa354d1973ab558038508b2","public:commit:e1cc60cf78ead1d667467557ef554ee03850843a","public:commit:f9d6830a33d912619c886f39c38aa15d69bd1060"],"source_type":"public","date":"2024-06-24..2024-07-01","topics":["lifetime","concurrency","ffi","testing","build","api","diagnosis","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native block and item registry models {#native-block-and-item-registry-models}

## Declarations are part of executable behavior here {#declarations-are-part-of-executable-behavior-here}

The large run of Block, BlockLegacy, BlockPalette, CachedComponentData, Material, ItemRegistry and Item declarations is not treated as meaningless header bulk. This project calls into an external host through modeled memory/vtables. Field ordering, platform padding, parameter types and virtual slot order govern the later viewer's reads. Conversely, hundreds of native declarations do not establish hundreds of independent personal design preferences: they are constrained interoperability work.

Block foundations arrive in 1231–1238. An opaque region becomes CachedComponentData at 1256–1257, followed by material and property views at 1263–1266. Unknown fields and incomplete tails remain explicit. At 1275 the permutation list has Linux offsets marked TODO; 1295–1297 extend/refine the tail and repair a platform branch. The commit titled member renaming (1296) also changes types, and the precision-titled 1307 initializes Packet fields. Reading actual changes prevents both undercounting semantics and attributing intent from labels alone.

## Choosing the right enumeration source {#choosing-the-right-enumeration-source}

The original viewer's palette is a network/runtime-oriented collection. Native BlockTypeRegistry forwarding at 1276, combined with non-null permutation traversal at 1275, enables the later switch to type/permutation enumeration at [1277](04-devtools-data-evolution.md#commit-1277). The message explicitly aims for all states. That is evidence for correcting the domain model of discovery, not a measured proof that every possible state was emitted. The local bool callback result is ignored by the permutation helper, so callers cannot infer early termination semantics from its type.

Block material/serialization getters return borrowed references, keeping the host as owner. The registry itself and per-item pointer model have separate lifetimes: the registry wrapper uses std::weak_ptr, while entries use custom SharedPtr/WeakPtr (1280–1281). The custom ownership implementation and later reversal are examined in [the ownership dossier](05-ownership-scheduler-boundaries.md). These names must not be flattened into an assumption that standard-library weak promotion guarantees apply everywhere.

## Field reads become virtual calls, with visible transition costs {#field-reads-become-virtual-calls-with-visible-transition-costs}

Item starts as a scaffold and direct field model (1282–1283). The expanded vtable at 1290 changes maximum-damage access and adds an ItemDescriptor argument to stack-size lookup. The caller temporarily drops maximum-stack output at 1291, then a minimal default descriptor restores it at 1293. This is a concrete change in the host-call contract and a staged compatibility repair. It is not evidence that the descriptor path was tested against every item.

Creative enumeration follows in 1308, getters at 1310 and consumers in 1311–1312. The naming path is revised after an explicit crash comment, but the unit does not establish whether the cause was native signature/layout, thread affinity, pointer lifetime or another condition. The final scheduler relocation is a separate observed response. For recipes, a CraftingDataPacket factory hook at 1315 is removed at 1319 and replaced by a direct Recipes reference/TODO at 1320. The final capability remains absent despite feature titles.

## Evidence and appropriate reuse {#evidence-and-appropriate-reuse}

Use this material for choosing host discovery boundaries, keeping ABI models modest, recording platform corrections and recognizing transient breakage during multi-commit construction. Static assertions, comments, enums and forwarding bodies are evidence of the declared model only. No native binary introspection, compiler build, size-test execution or data census was performed. Reuse exact version-specific addresses through the manifest audit, never as timeless constants. Native schema knowledge and third-party types are distinct from the commit author's own API/design decisions.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1231"></a>
### 1231: feat: add Block class {#commit-1231}

Source: [c598c7ef0ad4dd52183a549bbb2aac325fc59697](https://github.com/EndstoneMC/endstone/commit/c598c7ef0ad4dd52183a549bbb2aac325fc59697), 2024-06-24T21:40:36Z; git author Vincent. Disposition: native_model.

Adds native Block's 208-byte model, ComponentStorage's vector/flags/vtable shape and the initial BlockLegacy destructor scaffold. This is host-layout groundwork for inspection, not a public block-editing API. Size assertions constrain the local declarations but are not evidence that all fields or live server versions have been validated.

<a id="commit-1232"></a>
### 1232: feat: add BlockLegacy class {#commit-1232}

Source: [bd3cf022b572bc4452ef84e7b9f4df769529cfe4](https://github.com/EndstoneMC/endstone/commit/bd3cf022b572bc4452ef84e7b9f4df769529cfe4), 2024-06-25T09:20:23Z; git author Vincent. Disposition: native_model.

Expands BlockLegacy with material, rendering, light and identifier fields, documented platform offsets and an explicitly partial tail. Subsequent accessors and data export depend on these offsets. The partial model is an intentional boundary of known structure; avoid presenting it as a complete reconstruction of the native class.

<a id="commit-1233"></a>
### 1233: refactor: remove Common::getGameVersionString to file bedrock/common/game_version.h {#commit-1233}

Source: [0bc48f0851cdb51318d7de52a2841fd7b7a86309](https://github.com/EndstoneMC/endstone/commit/0bc48f0851cdb51318d7de52a2841fd7b7a86309), 2024-06-25T09:20:44Z; git author Vincent. Disposition: verified_relocation.

Moves Common::getGameVersionString into bedrock/common/game_version.h, updates consumers and adds forward declarations for block enum/material types. This separates a common utility from its prior host header. The next commit has the same subject but a distinct cleanup patch; identities are not deduplicated by title.

<a id="commit-1234"></a>
### 1234: refactor: remove Common::getGameVersionString to file bedrock/common/game_version.h {#commit-1234}

Source: [1506cbf7e7e5915e1aa9ea9fdf8b5592c1ad4b23](https://github.com/EndstoneMC/endstone/commit/1506cbf7e7e5915e1aa9ea9fdf8b5592c1ad4b23), 2024-06-25T09:26:47Z; git author Vincent. Disposition: mechanical.

Completes the preceding include cleanup with cstdint, Color and server include adjustments and a newline repair. Its subject repeats 1233, but the actual files/hunks differ. No new game-version behavior or independent architecture decision is supported.

<a id="commit-1235"></a>
### 1235: feat: add BlockPalette {#commit-1235}

Source: [3dcde3c8475100fbbec6d87f25dfceb7e148220b](https://github.com/EndstoneMC/endstone/commit/3dcde3c8475100fbbec6d87f25dfceb7e148220b), 2024-06-25T09:52:13Z; git author Vincent. Disposition: native_model.

Introduces BlockPalette's native mutex, name/runtime mappings, block vector and level relationship, with a Threading mutex alias. This enables later palette access rather than constructing or owning a new registry. Platform-sensitive standard-library layout remains an external host-ABI assumption.

<a id="commit-1237"></a>
### 1237: feat: expand BlockPalette class with new methods {#commit-1237}

Source: [c6f334451a9e51525fa354d1973ab558038508b2](https://github.com/EndstoneMC/endstone/commit/c6f334451a9e51525fa354d1973ab558038508b2), 2024-06-25T10:13:14Z; git author Vincent. Disposition: native_model.

Extends BlockPalette's virtual interface with network-ID assignment and get/append operations, plus a size getter. In this native declaration the ordering is part of the call contract. It does not by itself populate the palette or prove that enumerating it yields every possible block state.

<a id="commit-1238"></a>
### 1238: feat: expand Block class with new methods {#commit-1238}

Source: [198993e0462970907c24fa154ea3b900ab6d72fa](https://github.com/EndstoneMC/endstone/commit/198993e0462970907c24fa154ea3b900ab6d72fa), 2024-06-25T10:47:50Z; git author Vincent. Disposition: substantive.

Adds borrowed serialization-ID and runtime-ID getters to native Block, exposing existing host data for the forthcoming viewer. The serialization compound remains host-owned. There is no copy, persistence or mutation guarantee attached to this const-reference accessor.

<a id="commit-1256"></a>
### 1256: feat: add CachedComponentData {#commit-1256}

Source: [7287010f44b4ead4f4ec5ad3b79073ae194a26d9](https://github.com/EndstoneMC/endstone/commit/7287010f44b4ead4f4ec5ad3b79073ae194a26d9), 2024-06-27T09:18:25Z; git author Vincent. Disposition: native_model.

Introduces CachedComponentData for previously opaque block state, including light, flammability, friction and destruction properties. This improves the meaning of native fields without defining independent game rules. The subsequent getters use these values; correspondence to the live host remains a layout assumption.

<a id="commit-1257"></a>
### 1257: feat: add getters to Block class {#commit-1257}

Source: [8fb1e32f6d5f8a4dac7fe6a227c89b38ab580fb4](https://github.com/EndstoneMC/endstone/commit/8fb1e32f6d5f8a4dac7fe6a227c89b38ab580fb4), 2024-06-27T09:18:54Z; git author Vincent. Disposition: substantive.

Replaces an opaque 80-byte block region with the modeled 76-byte CachedComponentData and adds property/thickness getters. Alignment accounts for the next vector's position rather than requiring the replacement field itself to be 80 bytes. Getter code is read, but no compiled size or live value comparison was executed.

<a id="commit-1263"></a>
### 1263: feat: add Material class {#commit-1263}

Source: [90a778c940a8e0fd52f86ce9ada699fe63dfb420](https://github.com/EndstoneMC/endstone/commit/90a778c940a8e0fd52f86ce9ada699fe63dfb420), 2024-06-27T11:40:08Z; git author Vincent. Disposition: native_model.

Models native Material as a 16-byte set of type/physical flags and exposes borrowed const references from Block/BlockLegacy. The view avoids taking ownership of the host material. Later export schema changes do not alter that ownership contract or turn the flags into independently computed physics.

<a id="commit-1265"></a>
### 1265: feat: add BlockProperty {#commit-1265}

Source: [1e921d85bf7090d66d9c34eb92cb573124096fc5](https://github.com/EndstoneMC/endstone/commit/1e921d85bf7090d66d9c34eb92cb573124096fc5), 2024-06-27T13:21:05Z; git author Vincent. Disposition: native_model.

Adds a 64-bit BlockProperty mask with named values through bit 48, retaining an unknown/commented bit 39 and the entt bitmask marker. These declarations encode observed native flags; an enum name is not proof of the corresponding behavior. No broad public block-property API is implemented here.

<a id="commit-1266"></a>
### 1266: feat: extend BlockLegacy with virtual methods {#commit-1266}

Source: [f9d6830a33d912619c886f39c38aa15d69bd1060](https://github.com/EndstoneMC/endstone/commit/f9d6830a33d912619c886f39c38aa15d69bd1060), 2024-06-27T13:21:47Z; git author Vincent. Disposition: native_model.

Extends BlockLegacy's ordered virtual interface through canContainLiquid and adds a borrowed legacy accessor on Block. Forward declarations support the large native signatures. Although most lines are declarations, slot order is behaviorally important for host calls; no native method body or public implementation is being imported.

<a id="commit-1272"></a>
### 1272: feat: add Block::getTags {#commit-1272}

Source: [27bced163dc91c6266a189f6a3e8439846741bf8](https://github.com/EndstoneMC/endstone/commit/27bced163dc91c6266a189f6a3e8439846741bf8), 2024-06-28T10:55:32Z; git author Vincent. Disposition: substantive.

Adds Block tags with fallback to BlockLegacy when its own tag set is empty, expands version structures/native legacy tail, and exports tags per state. The fallback is a concrete data-access policy; it is later superseded in the dumper by type-level registry traversal, not evidence that every native tag source is identical.

<a id="commit-1275"></a>
### 1275: fix: add BlockLegacy::forEachBlockPermutation {#commit-1275}

Source: [85ac189f24d4993abd7fd39b578a468af1f38499](https://github.com/EndstoneMC/endstone/commit/85ac189f24d4993abd7fd39b578a468af1f38499), 2024-06-28T14:07:28Z; git author Vincent. Disposition: substantive.

Adds BlockLegacy's permutation vector/native tail and a forEachBlockPermutation helper over non-null entries. Its callback has a bool result but the loop ignores it, so callers cannot rely on short-circuiting. Linux offsets are still marked TODO at this point. This prepares broader state discovery than the network palette alone.

<a id="commit-1276"></a>
### 1276: fix: add BlockTypeRegistry::forEachBlock {#commit-1276}

Source: [734e6ce1baa128d4e56158766e079f3425d20bcd](https://github.com/EndstoneMC/endstone/commit/734e6ce1baa128d4e56158766e079f3425d20bcd), 2024-06-28T14:15:43Z; git author Vincent. Disposition: substantive.

Adds native BlockTypeRegistry::forEachBlock forwarding and two platform symbol addresses, with only timestamp change to the rest of the manifest. Corrects the HashedString include. It is a host enumeration hook, not proof that callback order or host registry completeness is stable across versions.

<a id="commit-1280"></a>
### 1280: feat: add ItemRegistry {#commit-1280}

Source: [c4bfdbfaed1cd5ba392536c95301fb987d7af956](https://github.com/EndstoneMC/endstone/commit/c4bfdbfaed1cd5ba392536c95301fb987d7af956), 2024-06-28T15:33:55Z; git author Vincent. Disposition: staging.

Introduces ItemRegistry and a registry-reference wrapper using std::weak_ptr, with necessary complete includes. This establishes host registry access but is distinct from the custom SharedPtr/WeakPtr used for contained item entries. The two lifetime mechanisms must not be conflated in subsequent ownership analysis.

<a id="commit-1281"></a>
### 1281: feat: add ItemRegistry members {#commit-1281}

Source: [1093250547f3c9af64d164bac38d7d22c6e8123f](https://github.com/EndstoneMC/endstone/commit/1093250547f3c9af64d164bac38d7d22c6e8123f), 2024-06-28T15:55:25Z; git author Vincent. Disposition: native_model.

Models ItemRegistry's vector of custom SharedPtr items and name/ID maps of custom WeakPtr entries, plus count/name-map getters. Introduces the single-control-block pointer shapes later implemented at 1286/1287. Layout scaffolding is not yet a verified standard shared_ptr replacement or a fully safe ownership implementation.

<a id="commit-1282"></a>
### 1282: feat: add Item class {#commit-1282}

Source: [37a3459dcb51122d917457953eaf5544bf581e29](https://github.com/EndstoneMC/endstone/commit/37a3459dcb51122d917457953eaf5544bf581e29), 2024-06-28T16:09:37Z; git author Vincent. Disposition: staging.

Adds Item's initial virtual/texture structure and a GUI list of names from weak registry entries via lock(). The caller does not check the locked result before dereference. This demonstrates the first item-inspection path and its native-model dependence, not a robust arbitrary-expiration contract.

<a id="commit-1283"></a>
### 1283: feat: expand Item class {#commit-1283}

Source: [499369dbde0a46077dcb66153a233db76cc49d44](https://github.com/EndstoneMC/endstone/commit/499369dbde0a46077dcb66153a233db76cc49d44), 2024-06-28T16:29:23Z; git author Vincent. Disposition: native_model.

Expands the Windows Item layout with identifier, maximum-damage/stack fields and getters, plus ItemTag scaffolding. Direct field access is later revised to native virtual methods at 1290. The evolution is important: initial field meaning/layout confidence was not the final access strategy.

<a id="commit-1290"></a>
### 1290: feat: expand Item class with virtual methods {#commit-1290}

Source: [3203d872694fe55179f650fa8d3c4d36c3ad0c5a](https://github.com/EndstoneMC/endstone/commit/3203d872694fe55179f650fa8d3c4d36c3ad0c5a), 2024-06-29T22:17:24Z; git author Vincent. Disposition: native_model.

Expands Item's ordered native virtual interface, replaces direct maximum-damage access with a virtual getter and changes maximum-stack access to require an ItemDescriptor. This temporarily invalidates the earlier no-argument caller; 1291 disables that output until 1293 supplies a descriptor. Declaration-only native patches can therefore affect real call behavior and build continuity.

<a id="commit-1293"></a>
### 1293: feat: add maxStackSize to item data in DevTools {#commit-1293}

Source: [3fb444c11efb6ffcd6ad262c5f17afefc18d4438](https://github.com/EndstoneMC/endstone/commit/3fb444c11efb6ffcd6ad262c5f17afefc18d4438), 2024-06-30T11:21:18Z; git author Vincent. Disposition: substantive.

Adds the minimal ItemDescriptor unique-implementation shape and restores maximum-stack export via getMaxStackSize({}). This resolves the specific call-signature gap from 1290/1291. The native host's acceptance of a default descriptor is assumed by the caller and is not independently runtime-verified here.

<a id="commit-1295"></a>
### 1295: feat: add canDropWithAnyTool to block data in DevTools {#commit-1295}

Source: [ba6e3edca190bdb075809e75f256d4f7de1c4f64](https://github.com/EndstoneMC/endstone/commit/ba6e3edca190bdb075809e75f256d4f7de1c4f64), 2024-06-30T12:06:27Z; git author Vincent. Disposition: native_model.

Adds Block::canDropWithAnyTool by forwarding the legacy flag, and expands the BlockLegacy tail including the Linux shared_timed_mutex region. The extra following 64-bit field is initially present on Linux too; 1297 corrects that branch. These platform-layout changes deserve semantic coverage despite their mostly declarative form.

<a id="commit-1296"></a>
### 1296: refactor: rename members in BlockLegacy class {#commit-1296}

Source: [9cdb0113943e815726de00c4464a5625fab5f555](https://github.com/EndstoneMC/endstone/commit/9cdb0113943e815726de00c4464a5625fab5f555), 2024-06-30T14:00:48Z; git author Vincent. Disposition: mixed_change.

The rename title also refines native field types: a data-driven flag changes from int to bool and the experience-drop representation from int64 to IntRange. Offset comments/names improve along with the type model. Alignment preservation is an assumption expressed by the declaration layout, not a compiled or live-memory result in this review.

<a id="commit-1297"></a>
### 1297: fix: size of BlockLegacy on Linux {#commit-1297}

Source: [e1cc60cf78ead1d667467557ef554ee03850843a](https://github.com/EndstoneMC/endstone/commit/e1cc60cf78ead1d667467557ef554ee03850843a), 2024-06-30T14:14:47Z; git author Vincent. Disposition: corrective.

Places the extra 64-bit field after the mutex in the Windows branch only, removing it from Linux and completing corresponding offset comments. The message identifies Linux BlockLegacy size as the problem. This closes 1295's local layout mistake; no complete cross-platform class-size test was executed.

<a id="commit-1307"></a>
### 1307: fix: float point precision for material translucency {#commit-1307}

Source: [2d2834dbf5c3cf3878d5d825bbb4a86dfadc5529](https://github.com/EndstoneMC/endstone/commit/2d2834dbf5c3cf3878d5d825bbb4a86dfadc5529), 2024-07-01T00:10:55Z; git author Vincent. Disposition: mixed_change.

Rounds exported material translucency, but also initializes native Packet priority, reliability, subclient ID, handled/time/handler/compressibility fields. Those defaults are a real packet-model change hidden by the floating-precision title. The patch still contains commented virtual declarations; it is not proof of a complete packet ABI reconstruction.

<a id="commit-1308"></a>
### 1308: feat: add CreativeItemRegistry::forEachCreativeItemInstance {#commit-1308}

Source: [b6daee8f3d3081cff58cfe0237d7e122d5ba3098](https://github.com/EndstoneMC/endstone/commit/b6daee8f3d3081cff58cfe0237d7e122d5ba3098), 2024-07-01T08:22:14Z; git author Vincent. Disposition: substantive.

Adds CreativeItemRegistry::forEachCreativeItemInstance forwarding, the derived ItemInstance model and two platform manifest entries. Other offsets are unchanged, with a timestamp update. This creates a native enumeration route; the following getters/dumper determine which creative item details are actually exported.

<a id="commit-1310"></a>
### 1310: feat: expand ItemStackBase class with property getters {#commit-1310}

Source: [a9e8ddfedbed404ac4d5752cbc417576a6a9e5bf](https://github.com/EndstoneMC/endstone/commit/a9e8ddfedbed404ac4d5752cbc417576a6a9e5bf), 2024-07-01T08:42:43Z; git author Vincent. Disposition: substantive.

Adds ItemStackBase custom-display-name and auxiliary-value getters, with 0x7fff/block-data fallback behavior, and getName that checks item expiration before calling the native virtual display-name path. Native Block friendship supports the access. A later crash comment is attached to getName; the method must not be treated as validated by its initial guard.

<a id="commit-1315"></a>
### 1315: feat: add CraftingDataPacket::prepareFromRecipes {#commit-1315}

Source: [3669991268ed4939747498c881ee184eb3959b48](https://github.com/EndstoneMC/endstone/commit/3669991268ed4939747498c881ee184eb3959b48), 2024-07-01T10:49:11Z; git author Vincent. Disposition: staging.

Adds CraftingDataPacket::prepareFromRecipes with return-value/unique_ptr hook handling and two manifest entries, preparing a possible recipe-dump route. No recipe JSON serializer is added. The entire route is removed at 1319; treat it as a short trial rather than a completed export capability.

<a id="commit-1319"></a>
### 1319: refactor: remove CraftingDataPacket {#commit-1319}

Source: [2460fc28ff33200b3a6fe062194c003d7a2078ee](https://github.com/EndstoneMC/endstone/commit/2460fc28ff33200b3a6fe062194c003d7a2078ee), 2024-07-01T14:18:52Z; git author Vincent. Disposition: reversal.

Deletes CraftingDataPacket's declaration, implementation and two manifest entries after the 1315 trial. Existing symbol values remain unchanged. The dumper still references the removed factory until the immediate 1320 repair, so this intermediate commit is not claimed independently buildable. No external reason for abandoning the packet-based route is supplied.
