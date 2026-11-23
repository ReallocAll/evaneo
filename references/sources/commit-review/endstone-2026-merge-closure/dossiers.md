<!-- retrieval: {"source_ids":["public:commit:8ee24e2405a7648a4244b96303aefbc9b3a5f84e","public:context-commit:324bbfbfb52616fd72751c97409256d3a4c7c0cc","public:context-commit:52f4c9b1df1d2eeffc5aec685546cace8fe99069","public:context-commit:545efac3af53b201b4cb1b4fa072684f7a3e9c63","public:context-commit:9c16f1239c6f5cbb30923cbe7da0115d4e29327e","public:context-commit:fbe2d4d46b5d4f8cf54add19d1c03e27a30db7dd"],"source_type":"public","date":"2026-01-16","topics":["lifetime","ffi","testing","build","performance","api","diagnosis","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="january-2026-merge-supplementary-inherited-history-closure"></a>
# January 2026 merge: integration notes {#january-2026-merge-supplementary-inherited-history-closure}

## Merge scope {#scope-and-attribution}

This supplement examines [merge 8ee24e2405a7648a4244b96303aefbc9b3a5f84e](https://github.com/EndstoneMC/endstone/commit/8ee24e2405a7648a4244b96303aefbc9b3a5f84e) and its integration with the January ABI port. Its conclusions combine the public merge history with the linked technical histories.

This supplement covers the merge integration and five nearby commits. The linked public commit history and technical dossiers preserve the original authorship and explicit coauthor credit.

No upstream code, project tooling, build, native binary, installer, server, workflow or tests were executed. The recorded review is source-level evidence; neither compiled ABI compatibility nor runtime correctness follows. The original current-Git remerge view remains a reconstruction, not a historical conflict transcript.

## Five related commits {#five-newly-completed-contexts}

Four commits update dependency action versions. The fifth changes the Windows portable Python bundle version; its message describes earlier CMake and optimization iterations that do not appear in the final patch. Later workflow versions provide context, but do not prove artifact availability or successful publication.

<a id="context-52f4c9b1df1d2eeffc5aec685546cace8fe99069"></a>

### chore(deps): bump pypa/cibuildwheel from 3.3.0 to 3.3.1 (#322) {#context-52f4c9b1df1d2eeffc5aec685546cace8fe99069}

Source: [52f4c9b1df1d2eeffc5aec685546cace8fe99069](https://github.com/EndstoneMC/endstone/commit/52f4c9b1df1d2eeffc5aec685546cace8fe99069).

Git author: Dependabot [bot]; no coauthor or signoff trailer.

Bumps cibuildwheel 3.3.0 to 3.3.1 at exactly two workflow uses. The complete delta changes no matrix, build command, artifact name, permission, or publication condition.

Verified version-substitution-only disposition; no dependency implementation or compatibility claim.


<a id="context-fbe2d4d46b5d4f8cf54add19d1c03e27a30db7dd"></a>

### chore(deps): bump actions/download-artifact from 6 to 7 (#315) {#context-fbe2d4d46b5d4f8cf54add19d1c03e27a30db7dd}

Source: [fbe2d4d46b5d4f8cf54add19d1c03e27a30db7dd](https://github.com/EndstoneMC/endstone/commit/fbe2d4d46b5d4f8cf54add19d1c03e27a30db7dd).

Git author: Dependabot [bot]; no coauthor or signoff trailer.

Bumps download-artifact 6 to 7 in wheel and Windows-portable publication jobs. Existing artifact patterns and dist paths are unchanged; whole final workflow context retains merge-multiple and release-published gating.

Verified version-substitution-only disposition; no download, publish, or runner compatibility was tested.


<a id="context-324bbfbfb52616fd72751c97409256d3a4c7c0cc"></a>

### chore(deps): bump actions/cache from 4 to 5 (#314) {#context-324bbfbfb52616fd72751c97409256d3a4c7c0cc}

Source: [324bbfbfb52616fd72751c97409256d3a4c7c0cc](https://github.com/EndstoneMC/endstone/commit/324bbfbfb52616fd72751c97409256d3a4c7c0cc).

Git author: Dependabot [bot]; no coauthor or signoff trailer.

Bumps cache 4 to 5 at seven uses across six workflows: CI Conan, coverage Conan, two Docker-layer caches, docs cache, wheel Conan and portable Conan. Cache paths, key expressions and adjacent build steps remain unchanged.

Verified seven identical tag substitutions; no cache service internals, migration performance, or hit-rate claim.


<a id="context-545efac3af53b201b4cb1b4fa072684f7a3e9c63"></a>

### chore(deps): bump actions/upload-artifact from 5 to 6 (#313) {#context-545efac3af53b201b4cb1b4fa072684f7a3e9c63}

Source: [545efac3af53b201b4cb1b4fa072684f7a3e9c63](https://github.com/EndstoneMC/endstone/commit/545efac3af53b201b4cb1b4fa072684f7a3e9c63).

Git author: Dependabot [bot]; no coauthor or signoff trailer.

Bumps upload-artifact 5 to 6 for wheel and portable zip uploads. Artifact names and paths are unchanged; the whole wheel workflow shows a separate release-gated publish job depending on build_wheels.

Verified version-substitution-only disposition; successful artifact production/publication is not observed.


<a id="context-9c16f1239c6f5cbb30923cbe7da0115d4e29327e"></a>

### Update windows-portable python version to 3.13.7 (#303) {#context-9c16f1239c6f5cbb30923cbe7da0115d4e29327e}

Source: [9c16f1239c6f5cbb30923cbe7da0115d4e29327e](https://github.com/EndstoneMC/endstone/commit/9c16f1239c6f5cbb30923cbe7da0115d4e29327e).

Git author: zevlaoxie2010; the commit message credits Vincent as coauthor.

Changes the portable bundle from WinPython 3.12.8 to the configured 3.13.7 URL, replacement SHA256 and WP_BINARY_DIR, while selecting cp313-win_amd64 instead of cp312. Full workflow read shows the SHA256 is checked before installer invocation and the configured directory is then used for pip installation, cleaning and copying.

Message mentions AVX/O2/CMake iterations, but the actual net delta modifies only the workflow's four values. No optimization implementation survives in this delta. Artifact availability, embedded directory spelling/layout, installer behavior and wheel/bundle compatibility remain unverified. Git author zevlaoxie2010 and the message crediting Vincent as coauthor are both retained.


## Reconcile newer main with the incoming ABI port {#reconcile-newer-main-with-the-incoming-abi-port}

The merge has first parent `9c16f1239c6f5cbb30923cbe7da0115d4e29327e`, incoming parent `2b1d39150120d90b9fccf3a331e4402122feca57`, and merge base `6e4b448c5533405c1e60d4751862472c76a2f335`. The original proof's 394 paths differ from parent 2. Of these, 381 exactly inherit parent 1's mode/blob; the other 13 mix later-main structure with incoming port changes. These 13 are not all 73 first-parent changed paths: the other 60 first-parent paths can be incoming-parent-identical and therefore absent from the parent-2 delta.

Tree equality distinguishes paths inherited from main, shared-history origins and branch-specific changes; it establishes reuse boundaries, not reasons, tests or ownership. The linked commit histories preserve original authorship, while branch-specific conclusions remain tied to their source dossiers.

The January ABI port and its follow-up fixes are analyzed in [the main January dossier](../endstone-2026/dossiers.md#january-port) and [the December port history](../endstone-2025-1301-1363/04-december-native-port-and-diagnosis.md#commit-1353). The later connection cleanup appears in [its source dossier](../endstone-2025-1301-1363/02-input-defense-and-connection-cleanup.md#commit-1361). These changes retain their original authorship; the public merge history is not a historical conflict transcript.

Three integration lessons now have concrete earlier-history support:

- Main's bool teleport, const-reference Location and nonnullable dimension contract come from the 1296–1300 chain. That history distinguishes a submitted transfer request from completed movement. Crucially,1301 fills the helper that was empty at1300; the January endpoint preserves its cooldown/axis/entrance-position work. The portal hook's destination/orientation-edit limits remain separate. The staged empty body must not be presented as the January final state.
- Main's weak Dimension handles and runtime-ID wrapper registry require an explicit lifetime argument.1317 later enumerates existing dimensions, closing the earlier population gap; the January constructor preserves that enumeration. Its asynchronous callback still captures a constructor-local helper by reference. Dropping the connector token is not evidence of immediate unsubscription, and temporary native handle locks do not provide a persistent lifetime pin for returned references. Native field removal is a different ABI question.
- Main's lazy Python facade, interpreter initialization without automatic finalization, and stdin/console ownership are deliberate evolved states. The merge combines them with new native layouts and gated detached DevTools rendering. It does not establish coordinated thread teardown or erase the earlier lifecycle tradeoffs.

The following exact per-path links make these conclusions inspectable without importing blanket authorship or rereading entire branches.

### 1. endstone/__init__.py {#integration-1}

Keeps main's lazy-loader package facade and changes only Minecraft version 1.21.124 to 1.21.130. This does not revert the package/submodule ownership transition.

Complete first-parent path delta, 12 lines. Earlier completed context: [1023 / 660a6bc85ffd](../endstone-2025-1001-1100/02-python-packages-and-stubs.md#commit-1023).


### 2. src/bedrock/forward.h {#integration-2}

Adds container-registry access/tracker/serialization forwards, ITickingSystem, authentication-validator and ItemCooldownType names. Existing later-main transfer and wrapper declarations remain; declarations alone prove no runtime implementation.

Complete first-parent path delta, 38 lines. Earlier completed context: [1300 / c859714d52cf](../endstone-2025-1201-1300/05-map-cleanup-and-teleport-events.md#commit-1300).


### 3. src/bedrock/server/dedicated_server.h {#integration-3}

Changes the shutdown virtual override to zero arguments while preserving main's server shape. Calling convention/vtable compatibility still requires the target binary.

Complete first-parent path delta, 13 lines. Earlier completed context: [1140 / 79b9c90d918a](../endstone-2025-1101-1200/06-branches-releases-and-context.md#commit-1140).


### 4. src/bedrock/world/actor/actor.cpp {#integration-4}

Adapts native health/maximum-health and getAttribute access from reference to pointer results. Incoming name lookup still throws when missing; a pointer return must not be mistaken for a new nullable/not-found contract. The completed main transition helper from1301 survives unchanged by this 31-line integration delta.

Complete first-parent path delta, 31 lines. Earlier completed context: [1136 / 007de2eef4fc](../endstone-2025-1101-1200/03-interface-ownership-and-events.md#commit-1136); [1296 / c0765cc521d2](../endstone-2025-1201-1300/05-map-cleanup-and-teleport-events.md#commit-1296); [1297 / 88965ce11107](../endstone-2025-1201-1300/05-map-cleanup-and-teleport-events.md#commit-1297); [1301 / 641d0eec3c26](../endstone-2025-1301-1363/01-dimensions-maps-and-lifetimes.md#commit-1301); [1353 / d24e5f10ce3a](../endstone-2025-1301-1363/04-december-native-port-and-diagnosis.md#commit-1353).


### 5. src/bedrock/world/actor/actor.h {#integration-5}

Adds ActorSwingSource to swing, switches getAttribute declaration to pointer, and keeps the later-main mutable-attribute contract. These are native ABI signatures, not implemented public attribute-registry functionality.

Complete first-parent path delta, 30 lines. Earlier completed context: [1136 / 007de2eef4fc](../endstone-2025-1101-1200/03-interface-ownership-and-events.md#commit-1136); [1296 / c0765cc521d2](../endstone-2025-1201-1300/05-map-cleanup-and-teleport-events.md#commit-1296).


### 6. src/bedrock/world/item/item.h {#integration-6}

Changes Item virtual-slot layout and tint strategy: body armor, resistance/attack sounds, equip sound relocation, tint variant, cooldown type and disabled former color slots. Main's later registry-backed ItemType reference and restored owned ItemStack string storage remain separate public/core decisions; header inspection is not binary validation.

Complete first-parent path delta, 74 lines. Earlier completed context: [1252 / 8f1a3c1d3587](../endstone-2025-1201-1300/01-typed-identifiers-and-registries.md#commit-1252); [1333 / 42f5b9d11965](../endstone-2025-1301-1363/03-api-error-and-ownership-migration.md#commit-1333); [1338 / 5aa11cc6a93c](../endstone-2025-1301-1363/03-api-error-and-ownership-migration.md#commit-1338).


### 7. src/bedrock/world/level/block/block_type.h {#integration-7}

Disables canConnect and is_interaction_, changes canBeBuiltOver's final parameter to BlockType, and removes argument names elsewhere. Distinguish cosmetic declaration edits from slot/field/signature changes.

Complete first-parent path delta, 51 lines. Earlier completed context: [1300 / c859714d52cf](../endstone-2025-1201-1300/05-map-cleanup-and-teleport-events.md#commit-1300).


### 8. src/bedrock/world/level/dimension/dimension.h {#integration-8}

Removes the native light-texture builder field while retaining the rest of main's Dimension model. Shared later history1317 already enumerates existing dimensions, so the earlier1236 population gap is not the January endpoint. The by-reference capture of the constructor-local helper and weak-handle lifetime limits are separate concerns.

Complete first-parent path delta, 13 lines. Earlier completed context: [1229 / 54c73d79fc7e](../endstone-2025-1201-1300/02-dimensions-and-vector-location.md#commit-1229); [1236 / f6040d1d1c87](../endstone-2025-1201-1300/02-dimensions-and-vector-location.md#commit-1236); [1241 / 602b14c71f5f](../endstone-2025-1201-1300/02-dimensions-and-vector-location.md#commit-1241); [1317 / 6c0e04b0a9c6](../endstone-2025-1301-1363/01-dimensions-maps-and-lifetimes.md#commit-1317).


### 9. src/bedrock/world/level/level_interface.h {#integration-9}

Adds three container-registry virtuals and generation-request cleanup; disables tick-death methods; adjusts skin reference and const cache access. Main's map manager and later interface context survive; no runtime ordering validation.

Complete first-parent path delta, 44 lines. Earlier completed context: [1091 / 6af0fb0d2287](../endstone-2025-1001-1100/04-map-rendering-and-events.md#commit-1091); [1236 / f6040d1d1c87](../endstone-2025-1201-1300/02-dimensions-and-vector-location.md#commit-1236).


### 10. src/endstone/core/player.cpp {#integration-10}

Moves text factory calls to TextPacketPayload and command/constraint access under packet.payload. Preserves main's player behavior and bool/const-reference teleport contract instead of restoring the old incoming API. Success still describes request submission rather than confirmed completion. Main1301 fills the former empty transition helper; event-modified destination dimension/orientation remain separate limitations.

Complete first-parent path delta, 63 lines. Earlier completed context: [1294 / 1320cf171ab8](../endstone-2025-1201-1300/05-map-cleanup-and-teleport-events.md#commit-1294); [1296 / c0765cc521d2](../endstone-2025-1201-1300/05-map-cleanup-and-teleport-events.md#commit-1296); [1297 / 88965ce11107](../endstone-2025-1201-1300/05-map-cleanup-and-teleport-events.md#commit-1297); [1299 / 4ecb2b1ba425](../endstone-2025-1201-1300/05-map-cleanup-and-teleport-events.md#commit-1299); [1300 / c859714d52cf](../endstone-2025-1201-1300/05-map-cleanup-and-teleport-events.md#commit-1300); [1301 / 641d0eec3c26](../endstone-2025-1301-1363/01-dimensions-maps-and-lifetimes.md#commit-1301).


### 11. src/endstone/core/server.cpp {#integration-11}

Adds a missing-resource-repository guard, changes shutdown to the zero-argument native request, and routes data reload through ServerInstance. Main typed registries and map-removal cleanup remain inherited. Later1339 uses plain reference policy on the called registry binding path; an unused reference_internal helper does not establish lifetime retention across reload.

Complete first-parent path delta, 33 lines. Earlier completed context: [1221 / 3eee3292306b](../endstone-2025-1201-1300/01-typed-identifiers-and-registries.md#commit-1221); [1252 / 8f1a3c1d3587](../endstone-2025-1201-1300/01-typed-identifiers-and-registries.md#commit-1252); [1292 / d520c1938da8](../endstone-2025-1201-1300/05-map-cleanup-and-teleport-events.md#commit-1292); [1339 / 2597eeca495d](../endstone-2025-1301-1363/03-api-error-and-ownership-migration.md#commit-1339).


### 12. src/endstone/runtime/CMakeLists.txt {#integration-12}

Adds -fno-delete-null-pointer-checks to the UNIX runtime compilation options while retaining main's runtime embedding arrangement. It supports the merge's defensive certificate hook but is not a portable null-this guarantee.

Complete first-parent path delta, 13 lines. Earlier completed context: [1157 / b41738ebca20](../endstone-2025-1101-1200/04-python-metrics-and-lifecycle.md#commit-1157).


### 13. src/endstone/runtime/bedrock_hooks/dedicated_server.cpp {#integration-13}

Keeps main's stdin_close and interpreter lifecycle; adds gated detached DevTools rendering before calling original server start. There is still no join here. Main's finalization-crash mitigation and native-reader takeover are preserved, without implying full shutdown safety.

Complete first-parent path delta, 25 lines. Earlier completed context: [1180 / b5621efdcbe0](../endstone-2025-1101-1200/05-console-build-and-deployment.md#commit-1180); [1184 / 8274c60bf919](../endstone-2025-1101-1200/05-console-build-and-deployment.md#commit-1184); [1187 / b6a10258725c](../endstone-2025-1101-1200/04-python-metrics-and-lifecycle.md#commit-1187).


<a id="final-state-corrections-and-retained-limits"></a>
## Final-state corrections and retained limits {#final-state-corrections-and-retained-limits}

### portal-helper-completed {#portal-helper-completed}

The helper was empty at1300 but1301 supplies portal cooldown, axis and entrance-position work. Guarded January endpoint lines296–311 preserve this implementation. The missing destination/orientation adoption in the separate portal hook remains; do not present the staged empty helper as January's final state.

Sources: [1300](../endstone-2025-1201-1300/05-map-cleanup-and-teleport-events.md#commit-1300); [1301](../endstone-2025-1301-1363/01-dimensions-maps-and-lifetimes.md#commit-1301). Exact endpoint proof: endpoint-semantic-reconciliation.json.

### existing-dimensions-populated {#existing-dimensions-populated}

1317 enumerates native existing dimensions after requesting vanilla dimensions. January constructor lines31–47 preserve it. The later callback still captures the local add_dimension closure by reference, so replacing the population gap does not establish callback lifetime safety.

Sources: [1236](../endstone-2025-1201-1300/02-dimensions-and-vector-location.md#commit-1236); [1317](../endstone-2025-1301-1363/01-dimensions-maps-and-lifetimes.md#commit-1317). Exact endpoint proof: endpoint-semantic-reconciliation.json.

### scoreboard-inverted-check-inherited {#scoreboard-inverted-check-inherited}

The exact parent1 blob inherited by January retains1349's objective == nullptr Preconditions predicate: nonnull success throws; null passes toward dereference. This is a source-level inherited defect, not a reproduced runtime result or a desirable design preference.

Sources: [1349](../endstone-2025-1301-1363/03-api-error-and-ownership-migration.md#commit-1349). Exact endpoint proof: endpoint-semantic-reconciliation.json.

### item-reinit-limitation-inherited {#item-reinit-limitation-inherited}

The January blob equals the final main1352 endpoint and parent1. The final owner's complete source-context analysis records the local string-view reinit body as empty; converting its callers from Result to exceptions does not supply the missing native implementation.

Sources: [1351](../endstone-2025-1301-1363/03-api-error-and-ownership-migration.md#commit-1351). Exact endpoint proof: endpoint-semantic-reconciliation.json.

## Current closure boundary {#current-closure-boundary}

The January merge combines the ABI port with later main-branch state. The endpoint corrections above describe inherited implementation and remaining limits; public commit history preserves author and coauthor credit.
