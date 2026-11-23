<!-- retrieval: {"source_ids":["public:commit:060840273afe7660f73316c1d2e701ed62311b91","public:commit:0bf5f3d77af406c0645889dce0883935730e74e5","public:commit:0dcdc551a41ea4dd73756a3b4b2c692e5e25ca64","public:commit:13349506865df325d6ef5d89d102fd18231abb1d","public:commit:2c3568763b991cbf79b90a240d8c19ad36df3a10","public:commit:2d78844fe557632ea1d5cc74ac219a195b3209e7","public:commit:35d0b83b61447ea07894d6f46ff8feea0ab49d55","public:commit:3644c122f713cba3e640a3f62b08364648e38441","public:commit:3a4c3e43eadbf9e27ff78c21342c5aaa32314f9c","public:commit:3dfaca009f1bb1b46c104c8dc944d8fae8ebada3","public:commit:4a2fbd69d43da5ac97c160f36c3f77bc574cac3f","public:commit:5a1e276ead3eade8df751e92eb4a735d77a42895","public:commit:5af32615dbb715988fb6cb949da3c454a7581634","public:commit:5b9323f37aa3121763fb5eef0fb7ea79f6b18066","public:commit:6a311b7c3ff06c2a5bc5f3ae7664619ac2e95531","public:commit:6e7239a53e85c9078578bfd3a5f5ef2257981cba","public:commit:6f4a756a836b160dbb90f486ee005e2be411b10e","public:commit:748f9c547354bf06f23de73b5f2ef5f69694ebb3","public:commit:80e0accddfd252901e42c6a9435c4ecc69b915a9","public:commit:8ac80836abf877d83d65300c47a150513b5feb7f","public:commit:9940b3ef949a3d9cac0fa1778e0bd8af9e7a5274","public:commit:9c1f172d383d7dc23826a036c59fc8e0bc931602","public:commit:9f91ff413db8d761b4a39c48bb2082767d508672","public:commit:b439afe27c2d3d3ca7ab4f2b88ed3855629db8a7","public:commit:bd87e074692744b9ce9c981f4aeb21c803b34917","public:commit:c66aaaa891d3d4afbe7098dd04a146ddf741c2eb","public:commit:c6c38d5dbb35f34427f727ddce6307c27db7108e","public:commit:ca530363009dbcba7e57b035e6c8ff78c075ee4a","public:commit:ca641719faeb7cd06cb7de982cf7f2ed341c43c2","public:commit:d2498414844b27ea626677b279a2cc340b5d41f2","public:commit:ea93be9539d19f546627c0b7b80fbc5dd8197fca","public:commit:f6e94b217d0bcdd17bb68c57716084d4bd649724","public:commit:fad9205077074a4a9498bbf0c8836d9f463e9baa"],"source_type":"public","date":"2024-06-26..2024-07-01","topics":["lifetime","concurrency","ffi","testing","build","recovery","api","diagnosis","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# DevTools: live inspection to owned snapshots {#devtools-live-inspection-to-owned-snapshots}

## The feature grows in several distinct stages {#the-feature-grows-in-several-distinct-stages}

The first GUI is a detached thread, hidden window and ImGui demo (1244), then a console-only /debug entry point (1246), a persistent hideable single window (1247) and live block inspection (1249). Hiding on close avoids losing the tool during a server session, but also bypasses normal termination. The source shows global window/show state, direct calls across command/render contexts and incomplete initialization cleanup. These limitations are retained alongside the useful interface work; no stable shutdown cause or platform lifecycle guarantee is invented.

A cached JSON snapshot and recursive viewer arrive at 1255. Caching allows presentation after the live world guards are no longer needed (1262), but initially extraction still traverses the host on the UI thread. The snapshot's contents broaden from palette identity to block properties, material, collision/color samples, tags and items. Primitive arrays initially display the whole array repeatedly and are corrected at 1268. A save dialog's Open operation clears the default filename; 1273 fixes initialization order. These are specific feedback-driven repairs visible in source, with no supplied user-session measurement.

## Output schema evolution preserves the data model {#output-schema-evolution-preserves-the-data-model}

Material data starts repeated under each block (1264), becomes a numeric dictionary/reference (1271), briefly uses ID/name objects (1273), then moves to name keys and eventually name-only references (1279/1285). Types and states separate at 1278: common tags/material relationships belong to types, while physics/serialization live with individual states. Inverse tag indexes support discovery across names. The record retains every intermediate schema rather than reporting only the final one as an enduring preference.

Collision shape is queried at Overworld position 0,0,0, map color at 0,10,0, and the shape validity return is ignored. Some native properties depend on world/location/state, so the exports are observations under those choices, not automatically timeless ground truth. Six-decimal rounding reduces representation noise (1292/1307), but its int intermediate limits its useful range. NBT-to-JSON loses tag widths and empty-container distinctions, described in the separate serialization dossier. Consumers should treat these files as inspection data with assumptions, not a universal format specification.

## Module isolation is a staged rewrite, not a transparent move {#module-isolation-is-a-staged-rewrite-not-a-transparent-move}

The Conan/CMake split at 1298–1299 precedes 1300's deletion of the whole old GUI and empty new render/show/hide functions. This is a visible temporary loss of functionality. JSON helpers, a loop, data structures, windows, About and saving are reintroduced across 1301–1313. The interface also becomes /devtools with a corrected dev alias, and feature-disabled builds eventually omit the command entirely rather than returning the earlier unavailability message. No claim is made that each intermediate commit is deployable or that branch/PR policy endorsed such staging.

VanillaData separates extraction from rendering at 1303. Returning nullptr when not ready (1304) distinguishes readiness from an empty dataset. At 1313 file selection retains an owning JSON copy in a variant, so choosing a destination no longer depends on a borrowed pointer to a mutable selected dataset. The ordinary cleanup path now deletes the dialog and nulls globals; failures and detached shutdown still lack a complete protocol. File creation remains raw ofstream without error reporting, overwrite checks or recovery logic.

The decisive threading change is [1318](05-ownership-scheduler-boundaries.md#commit-1318): native extraction is scheduled on the server thread, a local snapshot is filled, then it is published. That is explicit source evidence for a thread-affinity boundary. The UI's locator reads, repeated pending requests and publication synchronization are not fully coordinated in these commits. Do not mistake server-thread extraction for a proved complete concurrent handoff.

## Ownership, dependencies and final boundary {#ownership-dependencies-and-final-boundary}

Dear ImGui backends are third-party code whose exact reuse is documented in the build dossier. The 1,079-line file-browser addition was fully read, but its upstream authorship is not declared in that new header; no personal-style inference is assigned to the component internals. Fonts were structurally identified and hashed rather than visually audited. About explicitly credits all Endstone contributors and Dear ImGui. None of this authorizes claiming Vincent authored imported library implementations.

At 1320 block/item/material/tag/creative JSON selections exist in source, while NBT palette and recipes remain TODO. Seven JSON export choices do not mean seven validated data sets. No GUI was launched, file exported, host traversed or screenshot produced. Use the dossier for extraction/presentation separation, readiness contracts, staged refactor costs and owning export snapshots, while carrying the documented native/concurrent/persistence limits forward.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1244"></a>
### 1244: feat(gui): add devtools window {#commit-1244}

Source: [3dfaca009f1bb1b46c104c8dc944d8fae8ebada3](https://github.com/EndstoneMC/endstone/commit/3dfaca009f1bb1b46c104c8dc944d8fae8ebada3), 2024-06-26T09:39:11Z; git author Vincent. Disposition: staging.

Starts a detached runtime thread that initializes GLFW/OpenGL/ImGui and a hidden 100x100 window with demo/multi-viewport behavior. This is the first desktop tool scaffold. Early failures return without comprehensive cleanup and the thread has no joined shutdown contract. It demonstrates a running-loop design in source, not a tested lifecycle on the supported platforms.

<a id="commit-1245"></a>
### 1245: feat(gui): use DroidSans as default font {#commit-1245}

Source: [2c3568763b991cbf79b90a240d8c19ad36df3a10](https://github.com/EndstoneMC/endstone/commit/2c3568763b991cbf79b90a240d8c19ad36df3a10), 2024-06-26T10:00:00Z; git author Vincent. Disposition: asset_integration.

Adds Droid Sans as a bundled font and loads it relative to the runtime module. The entire font blob was hashed, its sfnt table bounds and identifying metadata inspected; glyph rendering was not audited. Font internals belong to their original authors. The locally authored change is packaging/path/loading integration, superseded by the JetBrains Mono choice at 1258.

<a id="commit-1246"></a>
### 1246: feat: add /debug command to open up DevTools {#commit-1246}

Source: [35d0b83b61447ea07894d6f46ff8feea0ab49d55](https://github.com/EndstoneMC/endstone/commit/35d0b83b61447ea07894d6f46ff8feea0ab49d55), 2024-06-26T11:02:57Z; git author Vincent. Disposition: substantive.

Adds an operator-permission /debug command restricted to the console, initially toggling a global show flag and increasing font scale. This keeps desktop invocation out of normal player commands. The flag is shared with the detached GUI thread without a shown synchronization mechanism; command authorization and thread coordination are separate concerns.

<a id="commit-1247"></a>
### 1247: feat: improve DevTools {#commit-1247}

Source: [9940b3ef949a3d9cac0fa1778e0bd8af9e7a5274](https://github.com/EndstoneMC/endstone/commit/9940b3ef949a3d9cac0fa1778e0bd8af9e7a5274), 2024-06-26T11:43:32Z; git author Vincent. Disposition: substantive.

Replaces the show flag with a global GLFW window pointer, a 1280x720 single-window layout and explicit show/hide calls. Closing hides the window and resets the close flag instead of terminating the loop. That is a concrete usability choice, but it also makes ordinary close bypass normal cleanup. The patch does not marshal GLFW calls between command and render threads.

<a id="commit-1249"></a>
### 1249: feat: add blocks to DevTools {#commit-1249}

Source: [060840273afe7660f73316c1d2e701ed62311b91](https://github.com/EndstoneMC/endstone/commit/060840273afe7660f73316c1d2e701ed62311b91), 2024-06-26T16:37:08Z; git author Vincent. Disposition: substantive.

Makes DevTools visible initially, adds docked About/Blocks/demo views and directly iterates the first live level's palette after server/level guards. DPI changes rebuild the font atlas and texture, but scaling a local ImGuiStyle copy does not assign that style back. Adds CompoundTag iteration for inspection. Native reads still occur on the GUI thread at this stage.

<a id="commit-1255"></a>
### 1255: feat: add Json visualizer in DevTools {#commit-1255}

Source: [5af32615dbb715988fb6cb949da3c454a7581634](https://github.com/EndstoneMC/endstone/commit/5af32615dbb715988fb6cb949da3c454a7581634), 2024-06-27T08:37:36Z; git author Vincent. Disposition: substantive.

Adds a recursive ImGui JSON tree viewer and a cached palette snapshot. The initial primitive-array branch renders the whole array for each element; 1268 fixes it to render the individual element. A hard-coded nlohmann ABI-version namespace in the forward declaration is repaired at 1259. Caching reduces repeated host traversal but is not yet a thread/lifetime protocol.

<a id="commit-1258"></a>
### 1258: feat: replace DroidSans.ttf with JetBrainsMono-Regular.ttf {#commit-1258}

Source: [3a4c3e43eadbf9e27ff78c21342c5aaa32314f9c](https://github.com/EndstoneMC/endstone/commit/3a4c3e43eadbf9e27ff78c21342c5aaa32314f9c), 2024-06-27T09:19:17Z; git author Vincent. Disposition: mixed_change.

Replaces Droid Sans with JetBrains Mono Regular and updates its loading path. The patch also adds burn/flame odds, light/emission, explosion resistance, friction and destroy speed to block exports, so it is not font-only. Both added/deleted binary assets have exact identity coverage; no font-rendering or numeric-value correctness claim is made.

<a id="commit-1259"></a>
### 1259: feat: add save blocks to DevTools {#commit-1259}

Source: [0dcdc551a41ea4dd73756a3b4b2c692e5e25ca64](https://github.com/EndstoneMC/endstone/commit/0dcdc551a41ea4dd73756a3b4b2c692e5e25ca64), 2024-06-27T10:18:26Z; git author Vincent. Disposition: substantive.

Adds the complete 1,079-line ImGuiFileBrowser component and integrates JSON saving through filesystem paths and ofstream. All 1,215 raw patch lines were read in two contiguous pages. The file includes selection/filter/directory/Windows-drive logic; its upstream author is not declared in the addition, so imported-looking internals receive no independent personal-style credit. Export has no local stream-error handling or overwrite confirmation. Open clears the prematurely assigned default filename, fixed at 1273.

<a id="commit-1262"></a>
### 1262: refactor: improve logics in DevTools::showBlockWindow {#commit-1262}

Source: [ea93be9539d19f546627c0b7b80fbc5dd8197fca](https://github.com/EndstoneMC/endstone/commit/ea93be9539d19f546627c0b7b80fbc5dd8197fca), 2024-06-27T11:13:25Z; git author Vincent. Disposition: corrective.

Changes the block window so an already populated snapshot can be displayed without requiring the server/level to remain available on every render. Initial population still checks them. This narrows the live dependency of presentation, but does not prove snapshot freshness, invalidation or safe publication across threads.

<a id="commit-1264"></a>
### 1264: feat: add material to block data in DevTools {#commit-1264}

Source: [fad9205077074a4a9498bbf0c8836d9f463e9baa](https://github.com/EndstoneMC/endstone/commit/fad9205077074a4a9498bbf0c8836d9f463e9baa), 2024-06-27T12:00:06Z; git author Vincent. Disposition: substantive.

Adds nested material properties to each block's exported JSON and wraps the viewer in a child region. This is the first material schema, later normalized into a shared dictionary and references. Preserve the schema evolution when comparing output consumers; it is not an enduring final per-block duplication preference.

<a id="commit-1267"></a>
### 1267: feat: add "canContainLiquid" to block data in DevTools {#commit-1267}

Source: [f6e94b217d0bcdd17bb68c57716084d4bd649724](https://github.com/EndstoneMC/endstone/commit/f6e94b217d0bcdd17bb68c57716084d4bd649724), 2024-06-27T13:32:08Z; git author Vincent. Disposition: substantive.

Adds canContainLiquid to exported block data, removes a duplicate name field in favor of serialization identity, and completes AABB/Actor includes required by the native interface. This is incremental viewer coverage, with no new lifetime model or measured liquid-behavior test.

<a id="commit-1268"></a>
### 1268: feat: add "collisionShape" to block data in DevTools {#commit-1268}

Source: [ca641719faeb7cd06cb7de982cf7f2ed341c43c2](https://github.com/EndstoneMC/endstone/commit/ca641719faeb7cd06cb7de982cf7f2ed341c43c2), 2024-06-27T21:04:31Z; git author Vincent. Disposition: mixed_change.

Queries collision AABB using the Overworld source at position 0,0,0 and adds the necessary BlockSource access path. The native validity result is ignored, so exported bounds are one context-dependent sample rather than universal shape truth. Separately fixes JSON primitive-array rendering to use each element's dump instead of repeating the entire array.

<a id="commit-1270"></a>
### 1270: refactor: use CollapsingHeader {#commit-1270}

Source: [b439afe27c2d3d3ca7ab4f2b88ed3855629db8a7](https://github.com/EndstoneMC/endstone/commit/b439afe27c2d3d3ca7ab4f2b88ed3855629db8a7), 2024-06-28T09:01:43Z; git author Vincent. Disposition: mixed_change.

Renames cached blocks to block_states, changes sections to CollapsingHeader and starts a materials placeholder. Removes the demo toggle while still displaying the demo unconditionally, so this is more than a widget-name substitution. Subsequent UI commits remove/reorganize demo behavior; the intermediate state is retained.

<a id="commit-1271"></a>
### 1271: feat: add mapColor to block data in DevTools {#commit-1271}

Source: [c6c38d5dbb35f34427f727ddce6307c27db7108e](https://github.com/EndstoneMC/endstone/commit/c6c38d5dbb35f34427f727ddce6307c27db7108e), 2024-06-28T10:31:29Z; git author Vincent. Disposition: substantive.

Adds map color sampled from the Overworld at 0,10,0, Color RGBA hex conversion/viewing and a numeric-key material dictionary referenced from states. toHexString emits a leading # while the parser expects eight digits; the viewer strips it. Also extends the ordered BlockLegacy virtual surface and Direction/Flip declarations. Entire patch was reread after a truncated combined display. The sampled color is not proven world-independent.

<a id="commit-1273"></a>
### 1273: feat: add block tags in DevTools {#commit-1273}

Source: [2d78844fe557632ea1d5cc74ac219a195b3209e7](https://github.com/EndstoneMC/endstone/commit/2d78844fe557632ea1d5cc74ac219a195b3209e7), 2024-06-28T11:36:15Z; git author Vincent. Disposition: mixed_change.

Builds an inverse tag-to-block-name index with deduplicated names and adds typed CompoundTag::getString with empty fallback. Materials temporarily become ID/name reference objects. Reorders file-browser setup to Open before SetInputName, fixing lost default filenames. These are separate data and interaction repairs in one patch; no export round-trip or persistence recovery test is added.

<a id="commit-1277"></a>
### 1277: feat: use BlockTypeRegistry::forEachBlock and BlockLegacy::forEachBlockPermutation to iterate over all block states (block permutations) {#commit-1277}

Source: [ca530363009dbcba7e57b035e6c8ff78c075ee4a](https://github.com/EndstoneMC/endstone/commit/ca530363009dbcba7e57b035e6c8ff78c075ee4a), 2024-06-28T14:46:44Z; git author Vincent. Disposition: substantive.

Switches the dumper from palette iteration to every registry block type and its non-null permutations, explicitly aiming to include all block states. Tags/materials move to once-per-type work. This is a meaningful correction to the enumeration source, not just a faster loop. Source intent is clear; no independent runtime census verifies that all possible states are returned.

<a id="commit-1278"></a>
### 1278: feat: add block types in DevTools {#commit-1278}

Source: [6a311b7c3ff06c2a5bc5f3ae7664619ac2e95531](https://github.com/EndstoneMC/endstone/commit/6a311b7c3ff06c2a5bc5f3ae7664619ac2e95531), 2024-06-28T15:12:50Z; git author Vincent. Disposition: substantive.

Separates block_types, containing shared material/tags, from block_states, containing state-specific physics/serialization, and adds matching export choices. Adds an Items scaffold and static UI/DPI state. This reduces repeated type-level data and distinguishes identity layers; migration/versioning of the evolving output schema is not introduced.

<a id="commit-1279"></a>
### 1279: feat: use material name as the key in materials.json {#commit-1279}

Source: [9c1f172d383d7dc23826a036c59fc8e0bc931602](https://github.com/EndstoneMC/endstone/commit/9c1f172d383d7dc23826a036c59fc8e0bc931602), 2024-06-28T15:18:44Z; git author Vincent. Disposition: schema_change.

Keys materials by their names while temporarily retaining numeric IDs inside values, and invokes the placeholder Items window. This is an intermediate schema between numeric dictionaries and the name-only references at 1285. Do not turn the short-lived redundant numeric field into a lasting design preference.

<a id="commit-1285"></a>
### 1285: refactor: simplify material type in DevTools {#commit-1285}

Source: [5a1e276ead3eade8df751e92eb4a735d77a42895](https://github.com/EndstoneMC/endstone/commit/5a1e276ead3eade8df751e92eb4a735d77a42895), 2024-06-29T20:25:02Z; git author Vincent. Disposition: schema_change.

Removes numeric IDs from the materials dictionary and makes block types reference only material names. This completes the observed numeric-key to ID/name-object to name-only sequence. The change favors human-readable exported relationships in this tool; no compatibility layer for older exported schemas appears.

<a id="commit-1289"></a>
### 1289: feat: add item tags to DevTools {#commit-1289}

Source: [d2498414844b27ea626677b279a2cc340b5d41f2](https://github.com/EndstoneMC/endstone/commit/d2498414844b27ea626677b279a2cc340b5d41f2), 2024-06-29T21:49:08Z; git author Vincent. Disposition: substantive.

Makes ItemTag derive from HashedString, exposes item tags, builds the inverse tag index and offers export. This grows inspection coverage using the current item access path. It adds no separate weak-pointer safety fix and does not establish that item tags and block tags have the same lifecycle or semantics.

<a id="commit-1291"></a>
### 1291: feat: add more item properties to DevTools {#commit-1291}

Source: [8ac80836abf877d83d65300c47a150513b5feb7f](https://github.com/EndstoneMC/endstone/commit/8ac80836abf877d83d65300c47a150513b5feb7f), 2024-06-29T22:17:33Z; git author Vincent. Disposition: staging.

Adds attack, armor, toughness and damageability properties, plus block thickness, while temporarily commenting out maximum-stack output after 1290's signature change. This is a staged repair, not a decision to exclude stack size permanently. The final descriptor-backed path returns at 1293.

<a id="commit-1292"></a>
### 1292: fix: json float precision {#commit-1292}

Source: [80e0accddfd252901e42c6a9435c4ecc69b915a9](https://github.com/EndstoneMC/endstone/commit/80e0accddfd252901e42c6a9435c4ecc69b915a9), 2024-06-29T22:48:30Z; git author Vincent. Disposition: corrective.

Normalizes selected exported floating values to six decimal places using multiply, signed half-step, int conversion and division. The intent is less noisy JSON precision. Because the intermediate integer is bounded, the helper is unsuitable as a general large-range numeric codec; this review did not run it or infer measured output quality beyond the source transformation.

<a id="commit-1294"></a>
### 1294: feat: add isSolidBlocking to material data in DevTools {#commit-1294}

Source: [9f91ff413db8d761b4a39c48bb2082767d508672](https://github.com/EndstoneMC/endstone/commit/9f91ff413db8d761b4a39c48bb2082767d508672), 2024-06-30T11:38:28Z; git author Vincent. Disposition: substantive.

Adds Material::isSolidBlocking, computed as not never-buildable and blocks-motion, and exports it. This is a derived inspection property from already modeled flags. It does not introduce new native collision behavior or prove equivalence with every host notion of solidity.

<a id="commit-1300"></a>
### 1300: refactor: move devtools related files to endstone_devtools {#commit-1300}

Source: [748f9c547354bf06f23de73b5f2ef5f69694ebb3](https://github.com/EndstoneMC/endstone/commit/748f9c547354bf06f23de73b5f2ef5f69694ebb3), 2024-06-30T22:33:13Z; git author Vincent. Disposition: staging.

Deletes the complete old GUI implementation and creates new devtools render/show/hide stubs with empty bodies; all 871 patch lines, including the old 620-line deletion, were read. Renames /debug to /devtools and its permission, initially giving /dev an incorrect leading slash alias. Feature-disabled builds omit the command. This is not behavior-preserving relocation: functionality is rebuilt across 1301–1313.

<a id="commit-1301"></a>
### 1301: feat: add imgui json helper {#commit-1301}

Source: [4a2fbd69d43da5ac97c160f36c3f77bc574cac3f](https://github.com/EndstoneMC/endstone/commit/4a2fbd69d43da5ac97c160f36c3f77bc574cac3f), 2024-06-30T22:38:32Z; git author Vincent. Disposition: staging.

Restores the JSON viewer and NBT conversion in a dedicated helper unit after the module split. Core rendering/conversion behavior follows the previously read implementation; the broader GUI is not yet restored. Subsequent 1303 moves NBT conversion to the data layer, separating presentation from extraction more clearly.

<a id="commit-1302"></a>
### 1302: feat: add basic gui loop {#commit-1302}

Source: [6e7239a53e85c9078578bfd3a5f5ef2257981cba](https://github.com/EndstoneMC/endstone/commit/6e7239a53e85c9078578bfd3a5f5ef2257981cba), 2024-06-30T22:55:47Z; git author Vincent. Disposition: substantive.

Restores the basic GLFW/ImGui loop, initial DPI-sized window, global pointer show/hide and a hidden-window notice, and fixes the command alias to dev without a slash. The detached lifetime, local-only style scaling and incomplete early-failure cleanup remain. This restores a shell for windows/data rather than completing every old feature in one refactor.

<a id="commit-1303"></a>
### 1303: feat: add vanilla data struct and dumper {#commit-1303}

Source: [c66aaaa891d3d4afbe7098dd04a146ddf741c2eb](https://github.com/EndstoneMC/endstone/commit/c66aaaa891d3d4afbe7098dd04a146ddf741c2eb), 2024-06-30T23:12:11Z; git author Vincent. Disposition: substantive.

Introduces VanillaData and a locator-backed snapshot/dumper separate from the GUI, moving NBT projection into that layer and collecting block/item data. The first getter returns an empty static reference before readiness and emplaces the snapshot before filling it, still on the UI thread. This is separation of responsibilities, with publication/thread constraints addressed only later.

<a id="commit-1304"></a>
### 1304: feat: add block and item window {#commit-1304}

Source: [0bf5f3d77af406c0645889dce0883935730e74e5](https://github.com/EndstoneMC/endstone/commit/0bf5f3d77af406c0645889dce0883935730e74e5), 2024-06-30T23:24:41Z; git author Vincent. Disposition: api_change.

Changes VanillaData::get to return nullptr when data is unavailable instead of a shared empty reference, reconnects Blocks/Items windows and initializes docking once. The UI can now distinguish not ready from a genuinely empty dataset. This state contract does not yet provide an in-progress flag or thread-safe asynchronous publication.

<a id="commit-1305"></a>
### 1305: feat: add about window {#commit-1305}

Source: [5b9323f37aa3121763fb5eef0fb7ea79f6b18066](https://github.com/EndstoneMC/endstone/commit/5b9323f37aa3121763fb5eef0fb7ea79f6b18066), 2024-06-30T23:35:05Z; git author Vincent. Disposition: substantive.

Adds an About window, initially closed and not docked, with Endstone version, all-contributor credit, Apache licensing and Dear ImGui attribution. This is explicit project/dependency credit in the shipped UI, not evidence that Vincent alone authored every displayed component.

<a id="commit-1311"></a>
### 1311: feat: dump basic creative item data {#commit-1311}

Source: [6f4a756a836b160dbb90f486ee005e2be411b10e](https://github.com/EndstoneMC/endstone/commit/6f4a756a836b160dbb90f486ee005e2be411b10e), 2024-07-01T08:42:52Z; git author Vincent. Disposition: staging.

Adds basic creative-item export using ItemStackBase::getName and auxiliary value. This is the first consumer of 1310's naming path. 1312 switches away after adding a crash warning, so this intermediate human-facing name is not the final creative-item identifier contract.

<a id="commit-1313"></a>
### 1313: feat: add save files in DevTools {#commit-1313}

Source: [3644c122f713cba3e640a3f62b08364648e38441](https://github.com/EndstoneMC/endstone/commit/3644c122f713cba3e640a3f62b08364648e38441), 2024-07-01T10:34:43Z; git author Vincent. Disposition: substantive.

Restores file export in the new module with a variant holding an owning JSON copy rather than a pointer to selected live data, creates a data directory and offers seven JSON datasets. NBT palette export remains TODO. Normal cleanup deletes the browser and nulls globals, but stream failures/overwrite handling and detached shutdown remain unproven. Snapshot ownership at export is a concrete improvement distinct from host-object ownership.

<a id="commit-1314"></a>
### 1314: refactor: `tags` attribute is now only added to the data when not null {#commit-1314}

Source: [bd87e074692744b9ce9c981f4aeb21c803b34917](https://github.com/EndstoneMC/endstone/commit/bd87e074692744b9ce9c981f4aeb21c803b34917), 2024-07-01T10:42:17Z; git author Vincent. Disposition: schema_change.

Omits tags when the constructed tag value is null for block types/items, instead of emitting a null field. This makes absence the schema representation for untagged entries. It does not change the separate inverse indexes or establish a formal schema version/migration policy.

<a id="commit-1320"></a>
### 1320: feat: add dumpRecipes {#commit-1320}

Source: [13349506865df325d6ef5d89d102fd18231abb1d](https://github.com/EndstoneMC/endstone/commit/13349506865df325d6ef5d89d102fd18231abb1d), 2024-07-01T14:21:21Z; git author Vincent. Disposition: staging.

Changes dumpRecipes to obtain level.getRecipes directly and leave the body TODO, removing the stale CraftingDataPacket include/use and completing a needed ItemInstance include. This closes the temporary dependency gap from 1319. Despite the feature title, recipe extraction/export is unfinished at the assignment boundary; no recipe capability should be inferred from the helper's presence.
