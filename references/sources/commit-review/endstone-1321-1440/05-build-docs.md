<!-- retrieval: {"source_ids":["public:commit:0d23ba1cf0063fee927243ca2c3b15feca728acf","public:commit:0fc4815f637a55c980247039af42a37ff26783ff","public:commit:1484ba118d4cd8f9412cccfaac20652698b9a08b","public:commit:301d3af6770894f8996bba408994689e80b0decb","public:commit:407fb939e95812fce2bbfed7d2fb2c533e06e7f7","public:commit:4d466238290f2dd3f881937c04d4d215f7bda8cd","public:commit:538e28c7e4caa7b38d15d0e8d409672a57d53555","public:commit:5d1d003aabc65504094a3f2625e44812206d5b4e","public:commit:68f61fe9c966ca264bc08b305ecad61ed311c8d0","public:commit:6e2fe589a727e500e58d1cf8e9a1816d81f15530","public:commit:6f0a8452a6e578766a067ad5a2a18f0b0dcc5b31","public:commit:72712073c48b70e27a386422a8bb69f8800473a3","public:commit:7a5ad8250b9df09a6c3f335cb14fb0cf4ffc11e9","public:commit:8777c29ead2f209b5e1e778288cce58fe7905cee","public:commit:8aa56d140580804b91ee03a473344837e4b818de","public:commit:8adae173b5f77d6c117fe3938f1e08b05340c482","public:commit:8b16f6cfd3f80da06cd1fb20e54d4007e8572bab","public:commit:8b4a0f76b5a819d1ffddd76447bddcd4e35704c9","public:commit:8ea72ac689de30e1a395dd6b442b4aaf6ae7f541","public:commit:9ed000c2719fd51db72ca183d353a7f1c0521d83","public:commit:9f41d34da744bbdbfb96db550db1c975b1b26c10","public:commit:afb4aad2b474f6fe692abd4255346a0de82efcfb","public:commit:b7111f567ad1bfc4c99486c5d95a40760d64df9c","public:commit:b7655922cf02bd6990ee7066e1189b8a5de31762","public:commit:cb519aaf2086a65df73b0def698492024c56e818","public:commit:cd1fc20cc04e0b73a59fe73156541bac8ebe904b","public:commit:de877bcfac712374d7f7cbab0397f9b9cd249ccc","public:commit:f1dae4de20fcd3909dda0ff7c9896dd83046a464"],"source_type":"public","date":"2024-07-05..2024-07-19","topics":["ffi","testing","build","performance","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Compatibility, packaging and documentation changes {#compatibility-packaging-and-documentation-changes}


## Proportionate handling of verified maintenance {#proportionate-handling-of-verified-maintenance}

Version manifests are read as actual full diffs and then parsed to verify their exact scope. 1331 adds the restored recipe factory's two platform entries; 1368 changes all 100 addresses while preserving keys; 1388 replaces two setDimension keys with teleportTo; 1406 changes 49 Windows addresses by +32 while leaving Linux unchanged. These comparisons preserve per-SHA identity and avoid treating every numeric address as a separate design lesson. No running BDS binary was used to validate them.

Windows /INCREMENTAL:NO is added at 1387, removed at 1389 and restored at 1391. The repeated added line is exact, but the surrounding patch contexts differ. Unix -fms-extensions and later __FUNCDNAME__ consolidation are observed together; a causal relation is plausible but not explicitly explained. Removing manually spelled Linux mangled names reduces call-site duplication; it is not proof of a platform-neutral ABI. CommandVersion and README markers are tracked separately from implementation.

LevelStorage and RakPeerInterface expansion is substantive native interface modeling, not mechanical noise and not a new storage/network subsystem. All declarations were read. SystemAddress zeroing has an explicit equality-related comment and preserves the address-family/default sentinel intent. There is no runtime structure, vtable or corruption test in this unit.

## Release and documentation are operational evidence, not execution results {#release-and-documentation-are-operational-evidence-not-execution-results}

The documentation workflow moves to mike, separates released/stable from main/latest, adds its dependency and stable default, and repairs mkdocs.yml triggers. The canonical site URL changes independently. Release 0.4.9 changes a source version macro and changelog; the 0.4.10 commit changes only the changelog. Neither is evidence this review published or checked packages/site deployment.

The command tutorial supplies both language examples and a screenshot. The image was read visually and hashed in full; it depicts help/usage and a Hello World response. That remains a supplied illustration, not a reviewer execution. Missing Python imports persist until 1429, and three later tutorial headings are empty. This is a useful completeness boundary for generated documentation: examples, imports, headings and screenshots each carry different evidence.

All author/committer metadata in this unit is Vincent; dependency names, native interfaces and imported tests retain separate attribution. Formatting, badges, ignores and one-line configuration changes receive brief accurate dispositions. No broad personal preference is extracted from mechanical maintenance, and old Nukkit history is not used. Exact canonical patch/file/blob/hunk hashes support later overlap reconciliation only after base/head matching; no PR range is claimed complete here.

## Individual commit dispositions {#individual-commit-dispositions}

<a id="commit-1342"></a>
### 1342 · chore(deps): update conanfile.py {#commit-1342}

[Commit 8777c29ead2f](https://github.com/EndstoneMC/endstone/commit/8777c29ead2f209b5e1e778288cce58fe7905cee) · 2024-07-05T11:18:24Z · Git author/committer: Vincent.

Updates cpptrace 0.5.2 to 0.6.2, pybind11 2.11.1 to 2.13.1, and spdlog 1.12 to 1.14.1, while replacing fmt's open lower bound with a ~10 range. These are actual dependency-policy changes, not measured performance or compatibility results. No dependency code or install was executed.

Source paths: `conanfile.py`.

<a id="commit-1343"></a>
### 1343 · docs: update CHANGELOG.md {#commit-1343}

[Commit 9ed000c2719f](https://github.com/EndstoneMC/endstone/commit/9ed000c2719fd51db72ca183d353a7f1c0521d83) · 2024-07-05T14:11:17Z · Git author/committer: Vincent.

The changelog explicitly describes DevTools as helping community projects retrieve Bedrock Dedicated Server data and documents its Windows-only console entry point. This is source-backed purpose for the preceding exporter work. It is a product-facing claim and scope statement, not evidence that every exported value or platform was validated.

Source paths: `CHANGELOG.md`.

<a id="commit-1345"></a>
### 1345 · chore: prepare release v0.4.9 {#commit-1345}

[Commit cb519aaf2086](https://github.com/EndstoneMC/endstone/commit/cb519aaf2086a65df73b0def698492024c56e818) · 2024-07-05T16:06:39Z · Git author/committer: Vincent.

Bumps the version macro to 0.4.9 and records its July 5 release, opening the next changelog section. This synchronizes source release markers; the review did not perform or verify an actual package publication.

Source paths: `CHANGELOG.md`, `include/endstone/endstone.h`.

<a id="commit-1346"></a>
### 1346 · ci: update docs workflow {#commit-1346}

[Commit 8adae173b5f7](https://github.com/EndstoneMC/endstone/commit/8adae173b5f77d6c117fe3938f1e08b05340c482) · 2024-07-05T16:42:08Z · Git author/committer: Vincent.

Replaces force gh-deploy with mike-based versioned publishing and adds the published-release workflow path. Main and released documentation are distinguished through latest and stable/version deployment. The next commit supplies the mike dependency/configuration, so this intermediate workflow is not independently assumed runnable.

Source paths: `.github/workflows/docs.yml`.

<a id="commit-1347"></a>
### 1347 · chore(deps): add 'mike' to requirements and update mkdocs.yaml {#commit-1347}

[Commit 0d23ba1cf006](https://github.com/EndstoneMC/endstone/commit/0d23ba1cf0063fee927243ca2c3b15feca728acf) · 2024-07-05T16:45:25Z · Git author/committer: Vincent.

Adds the mike documentation dependency and stable default/alias configuration, completing the prior workflow transition. This is deployment configuration, not evidence of a successfully published site. The stable versus latest distinction is the observable policy supported by the two commits.

Source paths: `docs/requirements.txt`, `mkdocs.yml`.

<a id="commit-1348"></a>
### 1348 · docs: update site_url {#commit-1348}

[Commit cd1fc20cc04e](https://github.com/EndstoneMC/endstone/commit/cd1fc20cc04e0b73a59fe73156541bac8ebe904b) · 2024-07-06T08:19:21Z · Git author/committer: Vincent.

Changes the canonical documentation site URL from the Read the Docs address to endstone.dev. This affects generated site metadata; no broader hosting migration or live redirect behavior was inferred from the single configuration edit.

Source paths: `mkdocs.yml`.

<a id="commit-1362"></a>
### 1362 · ci: update docs.yml {#commit-1362}

[Commit 7a5ad8250b9d](https://github.com/EndstoneMC/endstone/commit/7a5ad8250b9df09a6c3f335cb14fb0cf4ffc11e9) · 2024-07-09T00:11:06Z · Git author/committer: Vincent.

Adds mkdocs.yml to documentation workflow path triggers. Configuration-only edits can now initiate the workflow. This closes an observable trigger omission; no workflow execution was performed.

Source paths: `.github/workflows/docs.yml`.

<a id="commit-1368"></a>
### 1368 · chore: update to game version v1.21.2 {#commit-1368}

[Commit 68f61fe9c966](https://github.com/EndstoneMC/endstone/commit/68f61fe9c966ca264bc08b305ecad61ed311c8d0) · 2024-07-09T23:55:44Z · Git author/committer: Vincent.

Ports the package marker and symbol manifest to game 1.21.2. All 100 symbol addresses change, along with timestamp/version; keys remain identical. The exact parsed map comparison is retained. This is version-specific compatibility maintenance without a running-server ABI check. A truncated combined display was repaired by rereading the entire diff.

Source paths: `python/src/endstone/__init__.py`, `python/src/endstone/_internal/symbols.toml`.

<a id="commit-1369"></a>
### 1369 · docs: update CHANGELOG.md {#commit-1369}

[Commit 8b16f6cfd3f8](https://github.com/EndstoneMC/endstone/commit/8b16f6cfd3f80da06cd1fb20e54d4007e8572bab) · 2024-07-10T00:00:44Z · Git author/committer: Vincent.

Records skin support, recipe NBT/shaped-tag improvements and 1.21.2 support in the changelog. Its current-skin wording is broader than the observed login-snapshot implementation. Treat release prose as an author claim constrained by source, not stronger behavioral evidence. The entire diff was reread after the combined display truncation.

Source paths: `CHANGELOG.md`.

<a id="commit-1370"></a>
### 1370 · chore: prepare release v0.4.10 {#commit-1370}

[Commit 5d1d003aabc6](https://github.com/EndstoneMC/endstone/commit/5d1d003aabc65504094a3f2625e44812206d5b4e) · 2024-07-10T00:24:03Z · Git author/committer: Vincent.

Marks 0.4.10 released and opens 0.4.11 in the changelog only. No version-header edit occurs in this commit, and no publication was performed here. The initial combined-display truncation was repaired by a full dedicated reread.

Source paths: `CHANGELOG.md`.

<a id="commit-1371"></a>
### 1371 · docs: update README.md {#commit-1371}

[Commit afb4aad2b474](https://github.com/EndstoneMC/endstone/commit/afb4aad2b474f6fe692abd4255346a0de82efcfb) · 2024-07-10T00:25:04Z · Git author/committer: Vincent.

Updates the README game-version badge to 1.21.2. This is a public compatibility label corresponding to 1368, not a second implementation or runtime test.

Source paths: `README.md`.

<a id="commit-1372"></a>
### 1372 · docs: add contents to register-commands.md {#commit-1372}

[Commit b7655922cf02](https://github.com/EndstoneMC/endstone/commit/b7655922cf02bd6990ee7066e1189b8a5de31762) · 2024-07-10T11:14:14Z · Git author/committer: Vincent.

Adds a full command-registration tutorial in Python and C++, covering declaration, callback, help and a hello response. The supplied screenshot was visually read and shows the documented interaction; it is source-provided illustration, not a reviewer-run test. Parameters/permissions/aliases remain empty headings, and missing Python Command/CommandSender imports are repaired at 1429.

Source paths: `docs/tutorials/register-commands.md`, `docs/tutorials/screenshots/command-example.png`.

<a id="commit-1377"></a>
### 1377 · chore: do not diagnose traits defined in macros. {#commit-1377}

[Commit 301d3af67708](https://github.com/EndstoneMC/endstone/commit/301d3af6770894f8996bba408994689e80b0decb) · 2024-07-11T22:12:54Z · Git author/committer: Vincent.

Configures modernize-type-traits to ignore macros. The edit narrows one clang-tidy check's macro treatment; it does not disable the entire analysis suite or demonstrate that a particular diagnostic was a false positive.

Source paths: `.clang-tidy`.

<a id="commit-1384"></a>
### 1384 · chore: update CommandVersion::CurrentVersion to 39 {#commit-1384}

[Commit 9f41d34da744](https://github.com/EndstoneMC/endstone/commit/9f41d34da744bbdbfb96db550db1c975b1b26c10) · 2024-07-12T10:20:21Z · Git author/committer: Vincent.

Raises CommandVersion's current compatibility constant from 38 to 39. This is a meaningful protocol/version marker but does not modify parsing logic or establish backward compatibility by itself.

Source paths: `src/endstone_runtime/magic.cpp`.

<a id="commit-1386"></a>
### 1386 · style: code formatting {#commit-1386}

[Commit 538e28c7e4ca](https://github.com/EndstoneMC/endstone/commit/538e28c7e4caa7b38d15d0e8d409672a57d53555) · 2024-07-12T11:26:18Z · Git author/committer: Vincent.

Formats four files, including comments and spacing. Full diffs were read and complete before/after files compare identically after whitespace removal. The audit is corroboration of the inspected changes, not a claim that arbitrary whitespace removal proves C++ equivalence. No independent design preference is extracted.

Source paths: `include/bedrock/deps/jsoncpp/value.h`, `include/bedrock/nbt/tag.h`, `src/endstone_runtime/bedrock/server/commands/command_origin_loader.cpp`, `src/endstone_runtime/main.cpp`.

<a id="commit-1387"></a>
### 1387 · feat: disable incremental linking on Windows {#commit-1387}

[Commit 72712073c48b](https://github.com/EndstoneMC/endstone/commit/72712073c48b70e27a386422a8bb69f8800473a3) · 2024-07-12T12:55:43Z · Git author/committer: Vincent.

Adds /INCREMENTAL:NO for the Windows runtime link. The same added line is removed during 1389 and restored at 1391. No benchmark, linker-failure transcript or explicit reason is supplied, so the exact option history is retained without inventing a causal explanation.

Source paths: `CMakeLists.txt`.

<a id="commit-1389"></a>
### 1389 · feat: add -fms-extensions flag to UNIX compilation {#commit-1389}

[Commit 6f0a8452a6e5](https://github.com/EndstoneMC/endstone/commit/6f0a8452a6e578766a067ad5a2a18f0b0dcc5b31) · 2024-07-12T16:19:46Z · Git author/committer: Vincent.

Adds -fms-extensions on Unix and also removes the Windows no-incremental-link option. The compiler extension plausibly supports the following __FUNCDNAME__ unification, but that causal purpose is inference from adjacency/source use. The unrelated Windows removal must not be hidden by the Unix-focused change.

Source paths: `CMakeLists.txt`.

<a id="commit-1390"></a>
### 1390 · refactor: simplify hook original calls {#commit-1390}

[Commit f1dae4de20fc](https://github.com/EndstoneMC/endstone/commit/f1dae4de20fcd3909dda0ff7c9896dd83046a464) · 2024-07-12T16:20:44Z · Git author/committer: Vincent.

Uses __FUNCDNAME__ for Level::tick's original-hook dispatch on both platforms, removing the manually written Linux mangled symbol. This reduces a duplicated symbol spelling at the call site. Compiler/ABI compatibility was not tested; it is not proof that all symbol naming is now platform-independent.

Source paths: `src/endstone_runtime/bedrock/world/level/level.cpp`.

<a id="commit-1391"></a>
### 1391 · feat: disable incremental linking on Windows {#commit-1391}

[Commit b7111f567ad1](https://github.com/EndstoneMC/endstone/commit/b7111f567ad1bfc4c99486c5d95a40760d64df9c) · 2024-07-12T16:25:04Z · Git author/committer: Vincent.

Restores /INCREMENTAL:NO on Windows. The added line is exactly identical to 1387, while surrounding Unix configuration differs. Both commits were read and retained, with explicit duplicate-content evidence rather than two independent arguments for the option.

Source paths: `CMakeLists.txt`.

<a id="commit-1392"></a>
### 1392 · refactor: simplify hook original calls {#commit-1392}

[Commit 1484ba118d4c](https://github.com/EndstoneMC/endstone/commit/1484ba118d4cd8f9412cccfaac20652698b9a08b) · 2024-07-12T16:33:03Z · Git author/committer: Vincent.

Applies the same __FUNCDNAME__ original-call convention to StartGamePacket, player/mob death, actor removal and teleport hooks. The event control flow remains unchanged in these hunks. This is consolidation of hook-symbol maintenance, not a new event feature or runtime validation of the port.

Source paths: `src/endstone_runtime/bedrock/network/packet/start_game_packet.cpp`, `src/endstone_runtime/bedrock/server/server_player.cpp`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`, `src/endstone_runtime/bedrock/world/actor/mob.cpp`.

<a id="commit-1396"></a>
### 1396 · feat: use --no-cache-dir option for pip commands {#commit-1396}

[Commit 6e2fe589a727](https://github.com/EndstoneMC/endstone/commit/6e2fe589a727e500e58d1cf8e9a1816d81f15530) · 2024-07-13T22:36:31Z · Git author/committer: Vincent.

Adds --no-cache-dir to Docker pip installs and completes Position/Location str/repr stubs. The packaging intent is reduced retained pip cache; no image-size measurement was made. The stub additions correspond to 1394 and are not new native behavior.

Source paths: `Dockerfile`, `python/src/endstone/_internal/endstone_python.pyi`.

<a id="commit-1406"></a>
### 1406 · chore: update to game version v1.21.3 {#commit-1406}

[Commit 8aa56d140580](https://github.com/EndstoneMC/endstone/commit/8aa56d140580804b91ee03a473344837e4b818de) · 2024-07-16T20:44:43Z · Git author/committer: Vincent.

Ports to game 1.21.3, changing timestamp/version and exactly 49 Windows symbol addresses by +32. Linux entries and the remaining Windows symbol are unchanged; all keys are preserved. This verified mechanical pattern is narrower than an assertion that the whole engine ABI changed uniformly or was tested.

Source paths: `python/src/endstone/__init__.py`, `python/src/endstone/_internal/symbols.toml`.

<a id="commit-1409"></a>
### 1409 · docs: update README.md {#commit-1409}

[Commit 8b4a0f76b5a8](https://github.com/EndstoneMC/endstone/commit/8b4a0f76b5a819d1ffddd76447bddcd4e35704c9) · 2024-07-16T21:10:34Z · Git author/committer: Vincent.

Updates the README game badge to 1.21.3, matching the package/manifest port. No implementation, runtime evidence or separate compatibility rationale is added.

Source paths: `README.md`.

<a id="commit-1410"></a>
### 1410 · feat: expand LevelStorage class with virtual functions {#commit-1410}

[Commit 4d466238290f](https://github.com/EndstoneMC/endstone/commit/4d466238290f2dd3f881937c04d4d215f7bda8cd) · 2024-07-17T10:19:53Z · Git author/committer: Vincent.

Expands LevelStorage into a native virtual-interface model covering categorized data, observers, snapshots, shutdown, compaction and flushing, with required forward declarations/includes. These are declarations for the engine boundary, not an implemented new persistence subsystem. A README badge-line formatting repair is also present. Vtable/layout correctness was not runtime-validated.

Source paths: `README.md`, `include/bedrock/core/threading.h`, `include/bedrock/forward.h`, `include/bedrock/world/level/level_interface.h`, `include/bedrock/world/level/storage/db_helpers.h`, `include/bedrock/world/level/storage/level_storage.h`.

<a id="commit-1411"></a>
### 1411 · feat: expand RakPeerInterface class with virtual functions {#commit-1411}

[Commit de877bcfac71](https://github.com/EndstoneMC/endstone/commit/de877bcfac712374d7f7cbab0397f9b9cd249ccc) · 2024-07-17T19:39:48Z · Git author/committer: Vincent.

Appends 32 RakPeerInterface virtual declarations for public keys, timeouts, address behavior, plugins, sockets, simulation, statistics and receive-buffer size. Existing network policy is not changed by merely declaring them. The intended native vtable model is read in full, while actual binary correspondence remains untested.

Source paths: `include/bedrock/deps/raknet/rak_peer_interface.h`.

<a id="commit-1412"></a>
### 1412 · fix: default constructor of SystemAddress {#commit-1412}

[Commit 0fc4815f637a](https://github.com/EndstoneMC/endstone/commit/0fc4815f637a55c980247039af42a37ff26783ff) · 2024-07-18T15:59:32Z · Git author/committer: Vincent.

Zeroes the entire SystemAddress union with memset and then sets AF_INET, preserving the index/port defaults. A comment ties the zeroing to equality behavior; an earlier family assignment before memset is redundant. This records a deterministic representation fix rather than a new networking feature or measured failure reproduction.

Source paths: `include/bedrock/deps/raknet/raknet_types.h`.

<a id="commit-1427"></a>
### 1427 · chore: update .gitignore {#commit-1427}

[Commit 8ea72ac689de](https://github.com/EndstoneMC/endstone/commit/8ea72ac689de30e1a395dd6b442b4aaf6ae7f541) · 2024-07-19T10:12:27Z · Git author/committer: Vincent.

The .gitignore change excludes untracked files under .cache from Git status.

Source paths: `.gitignore`.

<a id="commit-1429"></a>
### 1429 · docs: add missing imports {#commit-1429}

[Commit 407fb939e958](https://github.com/EndstoneMC/endstone/commit/407fb939e95812fce2bbfed7d2fb2c533e06e7f7) · 2024-07-19T10:25:03Z · Git author/committer: Vincent.

Adds Command and CommandSender imports to the Python command tutorial and updates highlighted line numbers. This repairs the concrete missing-import problem in 1372. No tutorial execution was performed, so the source repair is not a verified end-to-end example run.

Source paths: `docs/tutorials/register-commands.md`.
