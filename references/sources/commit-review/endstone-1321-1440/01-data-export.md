<!-- retrieval: {"source_ids":["public:commit:1e63b0883ebcbba31ee09a48b87ee637c04beec5","public:commit:2de7402f7780317effac97e5a32e572cc7553841","public:commit:30648befccab302522808d56178aba50f6b96e06","public:commit:3d911853dfcb4cf12d2a13d242d5092800634299","public:commit:4a5824894fd3cbdb726f470b6d970628370a19cf","public:commit:4b41220d1fc0653e2e2e6852fe32532e6ff3b8b3","public:commit:4f4c6f35df007efb57b6c298a4dc32da183aca76","public:commit:511841de1ada0867519e37375441b50c004d705b","public:commit:517f7a5c45900aeb91252cd664baf79c70e738cb","public:commit:522511640641b3bd8cc5333b441b2375809a01e9","public:commit:6063407c70daabbc11e478d738950744d008f1c8","public:commit:6d07a30492afdf547f8e7c7a55e83842d800e97e","public:commit:7f5cba0326249334ec45671b3e13ba8a3bf3884a","public:commit:849f896461f37165871d668d79af700ed0f9372a","public:commit:9d8752cabd604c2b8d55f11110bde1f4088f84ac","public:commit:b0949667f3d66c82573d1264b7b2ddbc35438a96","public:commit:cc65f77cde5edcaf048ebe181b7ee9a196011ba3","public:commit:d49df1b8ea6aca76a8eb1e8ab031a6dad0d7b6d6","public:commit:d865a8d38b7ebdd4a4a6b4068f869a7b74d611b5","public:commit:dc7ff6a26f081c076a16ed0b0e040986f7b0930f","public:commit:e08087b0f66209dd4c9ba0975ce7bd1b5ccb6d6e","public:commit:eb85787c5a723f69f79b76814eee6a7bc2a775b1","public:commit:ecbc376254c4bdb482d362c7fcfe66cef55865e4","public:commit:f7d6f43474929c805602c47ee8f8934ddb2d3c5f"],"source_type":"public","date":"2024-07-01..2024-07-06","topics":["lifetime","concurrency","ffi","api","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Data export: ownership, schemas and snapshot publication {#data-export-ownership-schemas-and-snapshot-publication}


## Decision chain and supported purpose {#decision-chain-and-supported-purpose}

The unit begins directly after 1320's recipe TODO, on the same parent chain. Changelog 1343 explicitly says DevTools should help community projects obtain BDS data. That purpose explains why the work combines native layout access, a JSON viewer, and portable NBT/JSON artifacts. It does not establish a universal preference for extracting engine internals. The exact source identities below distinguish scaffolds, schema repairs and the eventual implementations.

NBT export develops through byte sinks (1321), list construction (1323), a borrowed palette payload (1324), binary output (1325), gzip integration (1326–1327), and owned compound/list payloads (1328–1330). Owning export data is a supported local choice: native serialization compounds are deep-copied before they are retained. The editor's JSON projection remains a different representation from typed NBT. Recipe result NBT is separately encoded as Base64 at 1352, avoiding loss of tag types inside the JSON schema. No file round-trip or consumer compatibility test was run.

## Reversals and invariants {#reversals-and-invariants}

The native recipe packet factory was introduced at 1315, removed at 1319 and restored at 1331; the runtime factory file is exactly the original blob. That is an observed return to a previously tried mechanism, not evidence of an explained rejection/acceptance debate. ABI scaffolds subsequently become typed entry vectors, modeled Recipe virtuals, lazily resolved descriptors and ten category routes. Readiness varies at each step: 1336 has null placeholders even though all enum cases are enumerated. 1340 has substantive serializers, while 1341 and 1349 repair tag/shape/schema distinctions. Deduplicating shaped ingredients by a name string still loses differences when metadata or count distinguishes two occurrences. The correct lesson is to inspect the identity key, not to infer complete fidelity from a field-preserving patch.

The thread protocol also changes causally. Prior 1318 schedules extraction on the server thread and constructs a local value. 1324 publishes the moved value before a sequentially consistent atomic ready store; a UI load that observes ready has the corresponding publication ordering. However multiple scheduled producers could still replace the locator. 1341 adds a should_run flag checked around enqueueing, adequate to suppress repeated calls from the single rendering path, but not a compare-exchange reservation for arbitrary concurrent callers. Neither scheduler enqueue failure nor extraction exceptions reset it. A fixed initial snapshot, server/level lifetime and successful completion remain assumptions. Do not carry the earlier unsynchronized-publication criticism forward unchanged, or promote the new gate into general concurrent/restart safety.

## Attribution, evidence and use {#attribution-evidence-and-use}

Vincent is the Git author/committer for these commits; native declarations adapt BDS interfaces and dependency integration is not authorship of zstr or engine algorithms. Only commit messages, code comments and changelog statements establish motives here. There are no reviewed PR objections in this unit and no invented alternative discussion. Alternative representations are visible in the actual transitions: borrowed versus owned compound, JSON projection versus NBT, opaque versus typed packet entries, visible versus hidden devtools startup. Runtime correctness, full native layouts, all recipe instances, compression fidelity and performance remain unmeasured.

Use this family when designing export schemas, separating presentation from lossless data, reviewing borrowed snapshot payloads, or tracing a server-thread/UI publication handoff. The direct DAG gives causal order; timestamps alone were not used to infer it.

## Individual commit dispositions {#individual-commit-dispositions}

<a id="commit-1321"></a>
### 1321 · feat: add BytesDataOutput {#commit-1321}

[Commit 4a5824894fd3](https://github.com/EndstoneMC/endstone/commit/4a5824894fd3cbdb726f470b6d970628370a19cf) · 2024-07-01T15:16:45Z · Git author/committer: Vincent.

Adds a byte-buffer implementation of IDataOutput and a big-endian specialization, providing the missing serialization sink for the forthcoming palette export. Primitive writes preserve bit patterns; the big-endian float conversion uses reference reinterpretation, so portability is not independently established. String length is masked with 0x7fff rather than validated or saturated. The referenced data_io path is completed by 1322.

Source paths: `include/bedrock/common/util/bytes_data_output.h`.

<a id="commit-1322"></a>
### 1322 · refactor: move data_io.h {#commit-1322}

[Commit 1e63b0883ebc](https://github.com/EndstoneMC/endstone/commit/1e63b0883ebcbba31ee09a48b87ee637c04beec5) · 2024-07-01T15:17:06Z · Git author/committer: Vincent.

Moves data_io.h into common/util and updates its consumers. The relocation preserves the complete blob; it supplies the include path used by 1321. This is an organizational prerequisite, not a different serialization format or an independent preference for rewriting code.

Source paths: `include/bedrock/common/util/data_io.h`, `include/bedrock/core/utility/data_io.h`, `include/bedrock/nbt/nbt_io.h`, `include/bedrock/nbt/tag.h`.

<a id="commit-1323"></a>
### 1323 · feat: add ListTag::add {#commit-1323}

[Commit ecbc376254c4](https://github.com/EndstoneMC/endstone/commit/ecbc376254c4bdb482d362c7fcfe66cef55865e4) · 2024-07-01T15:17:15Z · Git author/committer: Vincent.

ListTag::add takes a unique_ptr and appends ownership, updating the list type from each incoming tag. That enables accumulation of exported compounds. There is no null or homogeneous-element check in this addition, so the last tag determines the advertised list type. This is a concrete precondition of the builder, not a validated general-purpose NBT checker.

Source paths: `include/bedrock/nbt/list_tag.h`.

<a id="commit-1324"></a>
### 1324 · feat: add block palette nbt tag to vanilla data {#commit-1324}

[Commit 517f7a5c4590](https://github.com/EndstoneMC/endstone/commit/517f7a5c45900aeb91252cd664baf79c70e738cb) · 2024-07-01T16:24:49Z · Git author/committer: Vincent.

Exports deep copies of block serialization IDs as an NBT palette and exposes the BytesDataOutput buffer. The save variant initially borrows a CompoundTag pointer, while JSON is owned. A new atomic ready flag is stored after the completed VanillaData is moved into the locator, improving 1318's cross-thread publication. Repeated requests can still queue multiple producers until 1341; text-mode output is corrected by 1325.

Source paths: `include/bedrock/common/util/bytes_data_output.h`, `include/endstone/detail/devtools/vanilla_data.h`, `src/endstone_devtools/devtools.cpp`, `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1325"></a>
### 1325 · fix: use binary mode for writing nbt files {#commit-1325}

[Commit eb85787c5a72](https://github.com/EndstoneMC/endstone/commit/eb85787c5a723f69f79b76814eee6a7bc2a775b1) · 2024-07-01T16:49:44Z · Git author/committer: Vincent.

Opens the NBT output stream in binary mode. This one-line correction prevents platform text-mode translation of serialized bytes. It changes the output transport rather than the NBT schema; no generated file was opened or round-tripped in this review.

Source paths: `src/endstone_devtools/devtools.cpp`.

<a id="commit-1326"></a>
### 1326 · feat: write gzip-compressed nbt files {#commit-1326}

[Commit 511841de1ada](https://github.com/EndstoneMC/endstone/commit/511841de1ada0867519e37375441b50c004d705b) · 2024-07-01T17:17:18Z · Git author/committer: Vincent.

Adds zstr 1.0.7 to the optional devtools dependency/component and switches NBT output to a compressed stream. JSON remains plain text. This makes the intended NBT artifact gzip-compressed; dependency internals and actual compressed output were not executed or separately audited. The stream's explicit output mode is completed next.

Source paths: `CMakeLists.txt`, `conanfile.py`, `src/endstone_devtools/devtools.cpp`.

<a id="commit-1327"></a>
### 1327 · feat: dump special tools required to mine each block type {#commit-1327}

[Commit 522511640641](https://github.com/EndstoneMC/endstone/commit/522511640641b3bd8cc5333b441b2375809a01e9) · 2024-07-01T22:12:33Z · Git author/committer: Vincent.

Computes special-tools metadata by trying every registered item against each block's default state. This is an observable default-state sample, not proof of every permutation's behavior. The same commit adds out together with binary to the zstr stream mode, a meaningful export fix hidden behind the feature-oriented title.

Source paths: `include/bedrock/world/level/block/block_legacy.h`, `src/endstone_devtools/devtools.cpp`, `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1328"></a>
### 1328 · feat: add clone() and putCompound() functions in CompoundTag {#commit-1328}

[Commit 3d911853dfcb](https://github.com/EndstoneMC/endstone/commit/3d911853dfcb4cf12d2a13d242d5092800634299) · 2024-07-02T09:15:58Z · Git author/committer: Vincent.

Adds a typed CompoundTag clone returning unique_ptr and a putCompound overload that accepts nullable ownership, moving the compound into its variant representation. This simplifies deep-copy export assembly. It does not repair the previously observed self-copy or asymmetric equality behavior; those older limitations must not be described as solved by the ownership-oriented API.

Source paths: `include/bedrock/nbt/compound_tag.h`, `src/endstone_runtime/bedrock/nbt/compound_tag.cpp`.

<a id="commit-1329"></a>
### 1329 · refactor: change type of block_palette and creative_items to ListTag in VanillaData class. {#commit-1329}

[Commit dc7ff6a26f08](https://github.com/EndstoneMC/endstone/commit/dc7ff6a26f081c076a16ed0b0e040986f7b0930f) · 2024-07-02T09:16:25Z · Git author/committer: Vincent.

Replaces JSON palette/creative-item storage with ListTag, normalizes block tags with a minecraft prefix, keys items by full names, and renames exported fields to blockStateHash and hardness. Creative compounds are constructed but not appended here. GUI/save callers are still in transition; 1330 completes them. Preserve this incomplete intermediate state rather than retrospectively assigning the final exporter to this commit.

Source paths: `include/endstone/detail/devtools/vanilla_data.h`, `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1330"></a>
### 1330 · feat: export creative item data as nbt file {#commit-1330}

[Commit cc65f77cde5e](https://github.com/EndstoneMC/endstone/commit/cc65f77cde5edcaf048ebe181b7ee9a196011ba3) · 2024-07-02T10:12:56Z · Git author/committer: Vincent.

Completes the ListTag transition: creative compounds are appended, NBT export owns a CompoundTag assembled from copied lists, and the viewer projects NBT to JSON only for display. ListTag copying now preserves the element type, repairing an earlier omission. canDropWithAnyTool is commented out rather than successfully exported. Owning the save payload removes the prior borrowed-compound coupling.

Source paths: `include/bedrock/nbt/list_tag.h`, `src/endstone_devtools/devtools.cpp`, `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1331"></a>
### 1331 · feat: add CraftingDataPacket::prepareFromRecipes {#commit-1331}

[Commit d865a8d38b7e](https://github.com/EndstoneMC/endstone/commit/d865a8d38b7ebdd4a4a6b4068f869a7b74d611b5) · 2024-07-02T11:09:03Z · Git author/committer: Vincent.

Reintroduces CraftingDataPacket::prepareFromRecipes after its removal at 1319. The runtime factory file is byte-identical to the fully read 1315 version; integration code differs and was read separately. The guarded native return-value wrapper and two platform symbols restore the packet-derived approach, without evidence that the earlier removal was a permanent architectural rejection.

Source paths: `include/bedrock/network/packet/crafting_data_packet.h`, `python/src/endstone/_internal/symbols.toml`, `src/endstone_devtools/vanilla_data.cpp`, `src/endstone_runtime/bedrock/network/packet/crafting_data_packet.cpp`.

<a id="commit-1332"></a>
### 1332 · feat: add additional data entry structures and vectors to CraftingDataPacket {#commit-1332}

[Commit b0949667f3d6](https://github.com/EndstoneMC/endstone/commit/b0949667f3d66c82573d1264b7b2ddbc35438a96) · 2024-07-02T11:24:08Z · Git author/committer: Vincent.

Models packet collections for potion mixes, container mixes and material reducers, including item IDs, auxiliary values, counts and the clearing flag. Crafting entries are still opaque pointers. These declarations are ABI scaffolding for reading the engine's packet, not a new recipe algorithm or runtime-verified layout.

Source paths: `include/bedrock/network/packet/crafting_data_packet.h`.

<a id="commit-1333"></a>
### 1333 · feat: add recipes window to DevTools {#commit-1333}

[Commit f7d6f4347492](https://github.com/EndstoneMC/endstone/commit/f7d6f43474929c805602c47ee8f8934ddb2d3c5f) · 2024-07-02T11:59:16Z · Git author/committer: Vincent.

Adds recipe viewing/export data for mixes and reducers, translating IDs through ItemRegistry::getItem. That lookup uses map.at and returns a borrowed weak-wrapper value, so a missing ID throws instead of degrading gracefully. Ordinary crafting remains TODO. The reducer's outputMeta field actually carries a count, corrected at 1340.

Source paths: `include/bedrock/world/item/registry/item_registry.h`, `include/endstone/detail/devtools/vanilla_data.h`, `src/endstone_devtools/devtools.cpp`, `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1334"></a>
### 1334 · feat: dump potion mix and container mix in DevTools {#commit-1334}

[Commit 849f896461f3](https://github.com/EndstoneMC/endstone/commit/849f896461f37165871d668d79af700ed0f9372a) · 2024-07-02T13:01:42Z · Git author/committer: Vincent.

Introduces ten crafting-entry kinds, descriptor/count layouts, and named recipe collections instead of one generic JSON object. The crafting vector remains opaque at this point. GUI categories become explicit, while the old empty crafting TODO section disappears; disappearance of that section does not itself mean crafting serialization is implemented.

Source paths: `include/bedrock/network/packet/crafting_data_packet.h`, `include/bedrock/world/item/item_descriptor_count.h`, `include/bedrock/world/item/network_item_instance_descriptor.h`, `include/bedrock/world/level/block/block.h`, `include/endstone/detail/devtools/vanilla_data.h`, `src/endstone_devtools/devtools.cpp`, `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1335"></a>
### 1335 · feat: add Recipe and Recipes class {#commit-1335}

[Commit 7f5cba032624](https://github.com/EndstoneMC/endstone/commit/7f5cba0326249334ec45671b3e13ba8a3bf3884a) · 2024-07-02T13:14:06Z · Git author/committer: Vincent.

Adds initial Recipe/Recipes class scaffolds and changes crafting_entries from vector<void*> to vector<CraftingDataEntry>. This changes element stride and lifetime semantics, so it is substantive native-layout work despite the small scaffolds. Accessor-based serialization follows in later commits; layout compatibility was not checked against a running server.

Source paths: `include/bedrock/forward.h`, `include/bedrock/network/packet/crafting_data_packet.h`, `include/bedrock/world/item/crafting/recipe.h`, `include/bedrock/world/item/crafting/recipes.h`, `include/bedrock/world/level/level_interface.h`.

<a id="commit-1336"></a>
### 1336 · feat: add more detailed recipes in DevTools {#commit-1336}

[Commit 6d07a30492af](https://github.com/EndstoneMC/endstone/commit/6d07a30492afdf547f8e7c7a55e83842d800e97e) · 2024-07-02T13:27:38Z · Git author/committer: Vincent.

Dispatches all ten enumerated recipe kinds into separate collections, but each entry is still a null JSON placeholder. Unknown kinds, including COUNT, throw. UI category counts can now exist before meaningful recipe contents do. The title's breadth must not be converted into verified full recipe support.

Source paths: `include/endstone/detail/devtools/vanilla_data.h`, `src/endstone_devtools/devtools.cpp`, `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1337"></a>
### 1337 · feat: expand Recipe class {#commit-1337}

[Commit d49df1b8ea6a](https://github.com/EndstoneMC/endstone/commit/d49df1b8ea6aca76a8eb1e8ab031a6dad0d7b6d6) · 2024-07-02T15:34:40Z · Git author/committer: Vincent.

Models Recipe fields and identifiers, result/unlocking structures and accessors. Separately, TypedServerNetId loses its virtual destructor and renames value to raw_id; removing polymorphism changes the modeled layout and is not merely a rename. Ingredient behavior is still incomplete. No external reason for the layout choice or runtime size measurement is supplied.

Source paths: `include/bedrock/world/inventory/network/item_stack_net_id_variant.h`, `include/bedrock/world/item/crafting/recipe.h`, `include/bedrock/world/item/crafting/recipe_ingredient.h`, `include/bedrock/world/item/crafting/recipe_unlocking_requirement.h`.

<a id="commit-1338"></a>
### 1338 · feat: add basic shapeless recipe info {#commit-1338}

[Commit 6063407c70da](https://github.com/EndstoneMC/endstone/commit/6063407c70daabbc11e478d738950744d008f1c8) · 2024-07-02T15:56:03Z · Git author/committer: Vincent.

Adds RecipeIngredient as a descriptor/count subtype and begins serializing shapeless IDs, UUID, tag, priority and output names. Inputs and some counts are still TODO. This is a staged transition from packet categories to useful data, not a complete shapeless implementation at this SHA.

Source paths: `include/bedrock/world/item/crafting/recipe.h`, `include/bedrock/world/item/crafting/recipe_ingredient.h`, `include/bedrock/world/item/item_descriptor_count.h`, `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1339"></a>
### 1339 · feat: dump shapeless recipe data in DevTools {#commit-1339}

[Commit e08087b0f662](https://github.com/EndstoneMC/endstone/commit/e08087b0f66209dd4c9ba0975ce7bd1b5ccb6d6e) · 2024-07-02T16:40:28Z · Git author/committer: Vincent.

Expands descriptor virtuals and mutable implementation resolution from const accessors, then exports ingredient names, counts, auxiliary values and recipe net IDs. Missing implementations yield empty/null/sentinel defaults, but a resolution result is not separately checked before use. This extends const observation through lazy mutation rather than proving a pure, failure-free accessor contract.

Source paths: `include/bedrock/world/item/item_descriptor.h`, `include/bedrock/world/item/item_stack_base.h`, `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1340"></a>
### 1340 · feat: dump all types of recipes in DevTools {#commit-1340}

[Commit 4f4c6f35df00](https://github.com/EndstoneMC/endstone/commit/4f4c6f35df007efb57b6c298a4dc32da183aca76) · 2024-07-02T23:24:05Z · Git author/committer: Vincent.

Routes all ten recipe kinds, emits shaped patterns and furnace/smithing forms, and exports thirteen collections including mixes/reducers. Recipe virtuals replace some field getters. Shaped keys initially deduplicate by item name, losing distinctions in metadata/count; smithing assumes three inputs. Reducer outputMeta becomes count. The observed implementation breadth is real, but no runtime recipe census validates completeness.

Source paths: `include/bedrock/forward.h`, `include/bedrock/world/item/crafting/recipe.h`, `src/endstone_devtools/devtools.cpp`, `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1341"></a>
### 1341 · fix: recipes with input as tag instead of name can now be dumped correctly {#commit-1341}

[Commit 4b41220d1fc0](https://github.com/EndstoneMC/endstone/commit/4b41220d1fc0653e2e2e6852fe32532e6ff3b8b3) · 2024-07-03T00:23:05Z · Git author/committer: Vincent.

Represents item-tag ingredients explicitly, nests potion item/data fields, and removes the redundant smithing-trim input array. An additional atomic should_run gate suppresses repeated single-UI-thread scheduling. The ready flag already publishes completed state; this new gate is not compare-exchange, and exceptions or enqueue failure have no retry path. The final snapshot protocol is stronger than 1318 but still has bounded assumptions.

Source paths: `include/bedrock/world/item/item_descriptor.h`, `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1344"></a>
### 1344 · feat: DevTools will now be hidden by default. Use command /devtools to display the DevTools. {#commit-1344}

[Commit 30648befccab](https://github.com/EndstoneMC/endstone/commit/30648befccab302522808d56178aba50f6b96e06) · 2024-07-05T14:12:16Z · Git author/committer: Vincent.

Changes the GLFW window to start hidden, reversing the visible default introduced at 1249. The console/devtools path can expose it when wanted. The change supports an opt-in interactive tool at startup; the commit does not state a broader philosophy about all diagnostics or user interfaces.

Source paths: `src/endstone_devtools/devtools.cpp`.

<a id="commit-1349"></a>
### 1349 · fix: shaped recipe with input item tags {#commit-1349}

[Commit 9d8752cabd60](https://github.com/EndstoneMC/endstone/commit/9d8752cabd604c2b8d55f11110bde1f4088f84ac) · 2024-07-06T08:33:31Z · Git author/committer: Vincent.

Rebuilds shaped recipes from the already serialized row-major ingredient array, retaining tag/data/count information that the earlier name-only path discarded. Reducer id is renamed item for schema consistency. Pattern-key deduplication still uses only the item-or-tag string, so distinct data/count variants of one name can share a key; this is a bounded repair, not full identity preservation.

Source paths: `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1352"></a>
### 1352 · feat: dump output items' nbt tags {#commit-1352}

[Commit 2de7402f7780](https://github.com/EndstoneMC/endstone/commit/2de7402f7780317effac97e5a32e572cc7553841) · 2024-07-06T09:09:43Z · Git author/committer: Vincent.

Serializes recipe result user-data as named big-endian NBT and embeds its Base64 representation in JSON. This preserves NBT typing that a JSON projection cannot faithfully retain. It applies to outputs reached through the recipe-object branch. Base64 is an encoding, not encryption, and this nested payload is not the gzip file-export path.

Source paths: `src/endstone_devtools/vanilla_data.cpp`.
