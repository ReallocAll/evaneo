<!-- retrieval: {"source_ids":["public:commit:0e5dac660a529e32609b42553b8b9a43d9c9bc76","public:commit:15b95752114405adc039cf4155b644bf081de1c9","public:commit:1603c1e6b355b4772518ffb790c1bcb49c994e65","public:commit:18e4ee7265487b3584ae76cc6e7888f2c6687e65","public:commit:2c9c90ef32935a6c289b0277104e6701c3d32bfe","public:commit:443eecf41957385e3d84f2e17a9f1352446f7a6b","public:commit:65ff3f7d34cd488d8db2d7ac29df5e69e6e5d454","public:commit:6640348cd0989dd957068491d3a13f44d1b104d6","public:commit:6e439f74b0c04edd35bdd135dbf98701e6be041a","public:commit:84c80eaadb7d92cce2f3b8b6d7e94aecba1ed863","public:commit:8504a1fec65cbca4287db2191db5baa4b814ad43","public:commit:a25b58b424aa237b30290ee2fc3230d6acb24c29","public:commit:a3b76bc46e71c38f868fba2e41d7c8c8fafb314c","public:commit:d1a582e2fefac7dc1066fc7d8886794edf482212","public:commit:e3ea3fab28918ffc4431a8ffea9e9747c20656a6","public:commit:f55d8693bd28c55ad5062127c9a240557e57c2e1","public:commit:f8d57072e69ac0f260b9f083bbcfed24d85ee7eb","public:context-commit:5aec5c908fab6339add4317302298c72e1e4a30a","public:context-commit:7e66d0cf9768c82538cdca34f7b1c1b343ee7173","public:context-commit:ab5d9f3c8d56c190ae763305317507d00d0d7de3","public:context-commit:b8e78c6fa19b9a114c5d9bab0a004d5c5b0128b7","public:context-commit:bf066cec5ca4dac65dce727d607fb723ed129817","public:context-commit:e40c942da7a590875b8b8fc5c225f492c82d14c0","public:context-commit:f16793ca25ca71f3bd3cbea4353e93912f1716cf"],"source_type":"public","date":"2024-09-16..2024-10-22","topics":["lifetime","ffi","testing","build","api","diagnosis","documentation","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Build, DevTools, documentation and collaborator integration {#build-devtools-documentation-and-collaborator-integration}

Scope: Endstone history from ordinals 1801–1920, September 14–October 22, 2024. The entries below follow the APIs and runtime integrations developed during this period.

## Proportionate maintenance and attribution {#proportionate-maintenance-and-attribution}

Workflow, version, stub and sponsor changes accompany consumer guidance. Marketing assets include changed images, while classifiers and support badges remain claims rather than runtime evidence. The CI-titled 1813 also changes actor classification, so its title alone does not describe its effect.

Collaborator changes include CoolLoong's biome/export branch and merge of main; daoge's block-shape export, enchant value and default block-state hash; and Loudbook's expected-lite tag repair. Their public commit records preserve those authorships alongside Vincent's later integration. Merge history does not imply endorsement of every imported line.

DevTools headless error buffering is lifecycle work following daoge's contribution. Release notes provide explicit contracts for player-command permissions and C++ Result/Python exceptions, but contain date/API-name discrepancies. Those discrepancies are not silently corrected into stronger evidence. Linked public commits preserve contributor authorship.

No wheel, compiler, package installer, GL window, game server or upstream test was executed. Documentation and marketing changes support navigation and release chronology, not independent technical conclusions beyond their content.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1810"></a>
### Commit 1810 · ci: add Python 3.13 support to workflow for wheel build {#commit-1810}

Source: [84c80eaadb7d92cce2f3b8b6d7e94aecba1ed863](https://github.com/EndstoneMC/endstone/commit/84c80eaadb7d92cce2f3b8b6d7e94aecba1ed863). Authored 2024-09-16T11:05:30Z; committed 2024-09-16T11:05:30Z. Git author: Vincent; committer: Vincent.


The Windows wheel workflow adds Python 3.13 and prerelease support. This verifies the requested CI matrix/configuration change, not successful wheel construction or runtime support. Linux follows separately in 1813 and 1815.

Changed-source navigation: `.github/workflows/wheel.yml`.

<a id="commit-1815"></a>
### Commit 1815 · ci: allow pre-release Python versions in the build workflow {#commit-1815}

Source: [6e439f74b0c04edd35bdd135dbf98701e6be041a](https://github.com/EndstoneMC/endstone/commit/6e439f74b0c04edd35bdd135dbf98701e6be041a). Authored 2024-09-16T21:41:11Z; committed 2024-09-16T21:41:11Z. Git author: Vincent; committer: Vincent.


Enables prerelease Python versions for the Linux wheel path, completing the configuration started in 1813. No execution or broader compatibility result is inferred from this one workflow edit.

Changed-source navigation: `.github/workflows/wheel.yml`.

<a id="commit-1817"></a>
### Commit 1817 · feat: update python bindings {#commit-1817}

Source: [a25b58b424aa237b30290ee2fc3230d6acb24c29](https://github.com/EndstoneMC/endstone/commit/a25b58b424aa237b30290ee2fc3230d6acb24c29). Authored 2024-09-16T23:22:47Z; committed 2024-09-16T23:22:47Z. Git author: Vincent; committer: Vincent.


Updates the Python stub's boss colors to match 1804, including RebeccaPurple and White's new numeric value. This is compatibility bookkeeping for an already reviewed API change, not another independent color design decision.

Changed-source navigation: `python/src/endstone/_internal/endstone_python.pyi`.

<a id="commit-1826"></a>
### Commit 1826 · feat: v1.21.30 is now fully supported {#commit-1826}

Source: [0e5dac660a529e32609b42553b8b9a43d9c9bc76](https://github.com/EndstoneMC/endstone/commit/0e5dac660a529e32609b42553b8b9a43d9c9bc76). Authored 2024-09-18T20:23:50Z; committed 2024-09-18T20:23:50Z. Git author: Vincent; committer: Vincent.


The README support badge now claims full 1.21.30 support. This is a dated project claim following the platform map updates, not new runtime evidence and not proof that all subsequent crash fixes were already known.

Changed-source navigation: `README.md`.

<a id="commit-1827"></a>
### Commit 1827 · feat[devtool]: add biome export, add exportAll Button (#58) {#commit-1827}

Source: [a3b76bc46e71c38f868fba2e41d7c8c8fafb314c](https://github.com/EndstoneMC/endstone/commit/a3b76bc46e71c38f868fba2e41d7c8c8fafb314c). Authored 2024-09-19T11:50:47Z; committed 2024-09-19T11:50:47Z. Git author: Vincent; committer: GitHub.


Integrates CoolLoong's biome export and Export All work. Biome identifiers become available in exported vanilla data, and the DevTools UI can write all artifacts together. The actual branch commits and both merge-parent comparisons were examined; the second-parent delta is empty. Two concrete limits remain in the imported implementation: Export All can reach missing data, and its creative-items NBT write uses the block-palette payload. The static callback captures a render-local data directory that is alive through that render loop; a lifetime concern on a later render invocation is only conditional, not an immediate dangling-reference claim. Credit belongs to CoolLoong, with target attribution limited to integration.

Changed-source navigation: `include/bedrock/world/level/biome/biome.h`, `include/endstone/detail/devtools/vanilla_data.h`, `src/endstone_devtools/devtools.cpp`, `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1828"></a>
### Commit 1828 · docs: update CHANGELOG.md {#commit-1828}

Source: [2c9c90ef32935a6c289b0277104e6701c3d32bfe](https://github.com/EndstoneMC/endstone/commit/2c9c90ef32935a6c289b0277104e6701c3d32bfe). Authored 2024-09-19T12:05:18Z; committed 2024-09-19T12:05:18Z. Git author: Vincent; committer: Vincent.


The 0.5.4 notes credit collaborators, document the simulated-player and command fixes, and explicitly warn that `performCommand` now uses the player's permissions. The stated alternative is server dispatch using execute-as for callers that need the prior elevated behavior. This is useful migration rationale for 1816; it is not independent proof of the issue reports or runtime outcomes. The release notes preserve individual contributor names.

Changed-source navigation: `CHANGELOG.md`.

<a id="commit-1830"></a>
### Commit 1830 · chore: release v0.5.4 {#commit-1830}

Source: [6640348cd0989dd957068491d3a13f44d1b104d6](https://github.com/EndstoneMC/endstone/commit/6640348cd0989dd957068491d3a13f44d1b104d6). Authored 2024-09-19T13:15:06Z; committed 2024-09-19T13:15:06Z. Git author: Vincent; committer: Vincent.


Bumps the public header patch version to 0.5.4. The release marker is preserved as its own identity, with no independent engineering lesson.

Changed-source navigation: `include/endstone/endstone.h`.

<a id="commit-1833"></a>
### Commit 1833 · chore: release v0.5.4.1 (hotfix) {#commit-1833}

Source: [e3ea3fab28918ffc4431a8ffea9e9747c20656a6](https://github.com/EndstoneMC/endstone/commit/e3ea3fab28918ffc4431a8ffea9e9747c20656a6). Authored 2024-09-19T16:33:57Z; committed 2024-09-19T16:33:57Z. Git author: Vincent; committer: Vincent.


Records the emote crash hotfix in the changelog. The entry's 2023 date conflicts with the actual 2024 commit chronology and is retained as a documentation error, not used to reorder the causal chain. No additional implementation is present.

Changed-source navigation: `CHANGELOG.md`.

<a id="commit-1838"></a>
### Commit 1838 · docs: add Bisect Hosting banner to README.md {#commit-1838}

Source: [8504a1fec65cbca4287db2191db5baa4b814ad43](https://github.com/EndstoneMC/endstone/commit/8504a1fec65cbca4287db2191db5baa4b814ad43). Authored 2024-09-27T11:16:56Z; committed 2024-09-27T11:16:56Z. Git author: Vincent; committer: Vincent.


Adds the BisectHosting README sponsorship and a WebP banner. The binary was extracted, hashed and visually inspected: it advertises the Endstone promotion and discount with decorative game imagery. There is no executable content or technical design conclusion to infer from this marketing asset.

Changed-source navigation: `README.md`, `docs/assets/bisecthosting-banner.webp`.

<a id="commit-1839"></a>
### Commit 1839 · docs: add Bisect Hosting to home page {#commit-1839}

Source: [d1a582e2fefac7dc1066fc7d8886794edf482212](https://github.com/EndstoneMC/endstone/commit/d1a582e2fefac7dc1066fc7d8886794edf482212). Authored 2024-09-27T11:59:44Z; committed 2024-09-27T11:59:44Z. Git author: Vincent; committer: Vincent.


Updates homepage sponsorship/promotion content, replaces the Discord presentation with a static SVG, and removes the Ko-fi badge. The full textual change was read; it is documentation/marketing maintenance with no independent software-architecture inference.

Changed-source navigation: `docs/index.md`, `docs/overrides/main.html`.

<a id="commit-1840"></a>
### Commit 1840 · refactor: suppress error message when OpenGL is unavailable {#commit-1840}

Source: [15b95752114405adc039cf4155b644bf081de1c9](https://github.com/EndstoneMC/endstone/commit/15b95752114405adc039cf4155b644bf081de1c9). Authored 2024-09-29T11:10:57Z; committed 2024-09-29T11:10:57Z. Git author: Vincent; committer: Vincent.


Buffers GLFW initialization errors until the user requests the DevTools UI, reducing unwanted headless-startup noise, and cleans up the created window/GLFW state when GLEW initialization fails. Full DevTools context was read; this does not establish general thread safety or all failure-path cleanup. The immediate parent is daoge's separately read block-shape export contribution, not the previous target ordinal. That contribution exposes outline, visual, UI and liquid clip shapes and is credited separately, with its squash body not treated as proof that every listed intermediate revision was individually recovered.

Changed-source navigation: `src/endstone_devtools/devtools.cpp`.

<a id="commit-1852"></a>
### Commit 1852 · Merge remote-tracking branch 'origin/main' {#commit-1852}

Source: [f8d57072e69ac0f260b9f083bbcfed24d85ee7eb](https://github.com/EndstoneMC/endstone/commit/f8d57072e69ac0f260b9f083bbcfed24d85ee7eb). Authored 2024-09-30T13:12:06Z; committed 2024-09-30T13:12:06Z. Git author: Vincent; committer: Vincent.


Merges daoge's one-line enchantValue addition to vanilla item export (PR #65). The first-parent delta is the collaborator's export feature; the second-parent delta exactly reproduces already-read 1851, with every endpoint blob verified and an empty remerge diff. This avoids rereading inherited block changes without transferring their authorship or claiming full PR discussion coverage.

Changed-source navigation: `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1862"></a>
### Commit 1862 · Merge remote-tracking branch 'origin/main' {#commit-1862}

Source: [65ff3f7d34cd488d8db2d7ac29df5e69e6e5d454](https://github.com/EndstoneMC/endstone/commit/65ff3f7d34cd488d8db2d7ac29df5e69e6e5d454). Authored 2024-10-01T11:57:43Z; committed 2024-10-01T11:57:43Z. Git author: Vincent; committer: Vincent.


Merges Loudbook's expected-lite GIT_TAG correction from 0.8.0 to v0.8.0 (PR #68). The fix changes the dependency tag used during acquisition; it is not an error-handling design.

Changed-source navigation: `cmake/EndstoneHeaders.cmake`.

<a id="commit-1894"></a>
### Commit 1894 · chore: add Python 3.13 to classifiers in pyproject.toml {#commit-1894}

Source: [1603c1e6b355b4772518ffb790c1bcb49c994e65](https://github.com/EndstoneMC/endstone/commit/1603c1e6b355b4772518ffb790c1bcb49c994e65). Authored 2024-10-16T17:13:43Z; committed 2024-10-16T17:13:43Z. Git author: Vincent; committer: Vincent.


Adds Python 3.13 to package classifiers. This is a distribution support declaration, distinct from the earlier workflow configuration and from actual wheel/runtime validation.

Changed-source navigation: `pyproject.toml`.

<a id="commit-1903"></a>
### Commit 1903 · fix: correct the name of function in tutorial {#commit-1903}

Source: [443eecf41957385e3d84f2e17a9f1352446f7a6b](https://github.com/EndstoneMC/endstone/commit/443eecf41957385e3d84f2e17a9f1352446f7a6b). Authored 2024-10-20T00:26:33Z; committed 2024-10-20T00:26:33Z. Git author: Vincent; committer: Vincent.


Renames the scheduler tutorial's example functions from send_time to say_hi without changing their behavior. It is verified example maintenance, not a scheduler implementation fix.

Changed-source navigation: `docs/tutorials/schedule-tasks.md`.

<a id="commit-1917"></a>
### Commit 1917 · docs: update CHANGELOG.md {#commit-1917}

Source: [18e4ee7265487b3584ae76cc6e7888f2c6687e65](https://github.com/EndstoneMC/endstone/commit/18e4ee7265487b3584ae76cc6e7888f2c6687e65). Authored 2024-10-22T13:53:56Z; committed 2024-10-22T13:53:56Z. Git author: Vincent; committer: Vincent.


The changelog explicitly explains the new C++ Result policy and its Python exception translation, alongside the new APIs. Its tag method names use addTag/removeTag rather than the actual addScoreboardTag/removeScoreboardTag API, and an old 2023 release-date typo remains. This is evidence of intended user-facing error behavior and migration, qualified by the source-level deviations preserved in dossier 03 rather than treated as blanket proof of completion.

Changed-source navigation: `CHANGELOG.md`.

<a id="commit-1918"></a>
### Commit 1918 · docs: update CHANGELOG.md {#commit-1918}

Source: [f55d8693bd28c55ad5062127c9a240557e57c2e1](https://github.com/EndstoneMC/endstone/commit/f55d8693bd28c55ad5062127c9a240557e57c2e1). Authored 2024-10-22T14:19:36Z; committed 2024-10-22T14:19:36Z. Git author: Vincent; committer: Vincent.


Adds the command-output wrapper feature to the changelog. The implementation and borrowed/callback semantics are already analyzed at 1870–1872; this entry supplies release communication, not another implementation decision.

Changed-source navigation: `CHANGELOG.md`.


## Additional collaborator source records {#additional-collaborator-source-records}

The linked public commits and their parents preserve the contributor and merge history for these changes.

<a id="collaborator-7e66d0cf"></a>

### Collaborator 7e66d0cf {#collaborator-7e66d0cf}

Source: [7e66d0cf9768c82538cdca34f7b1c1b343ee7173](https://github.com/EndstoneMC/endstone/commit/7e66d0cf9768c82538cdca34f7b1c1b343ee7173). Author: CoolLoong; committer: CoolLoong. Authored 2024-09-18T22:47:51+08:00; committed 2024-09-18T22:47:51+08:00.

Adds the native Biome name/ID model, collects registered biomes into VanillaData, and adds a dedicated DevTools export/display section. This extends the existing export architecture rather than introducing a new storage framework. The initial exported mapping is later changed by target ordinal 1829 to objects containing id, so consumer schema evolution must remain visible. The whole actual first-parent patch was read. No GUI or export file was generated by the reviewer.

<a id="collaborator-e40c942d"></a>

### Collaborator e40c942d {#collaborator-e40c942d}

Source: [e40c942da7a590875b8b8fc5c225f492c82d14c0](https://github.com/EndstoneMC/endstone/commit/e40c942da7a590875b8b8fc5c225f492c82d14c0). Author: CoolLoong; committer: CoolLoong. Authored 2024-09-19T09:30:59+08:00; committed 2024-09-19T09:30:59+08:00.

Merges main into the biome-export branch. Its first-parent diff imports the Linux 1.21.30 address-map and support-badge changes, both read directly in this collaborator patch and already owned by target 1825–1826. The second-parent diff is exactly the already-read biome-export patch from 7e66d0cf: the historical review recorded matching canonical bytes and endpoint blobs, but its merge-audit JSON is not distributed. The remerge diff is empty. This is synchronization/context, not additional independent feature authorship.

<a id="collaborator-bf066cec"></a>

### Collaborator bf066cec {#collaborator-bf066cec}

Source: [bf066cec5ca4dac65dce727d607fb723ed129817](https://github.com/EndstoneMC/endstone/commit/bf066cec5ca4dac65dce727d607fb723ed129817). Author: CoolLoong; committer: CoolLoong. Authored 2024-09-19T10:33:12+08:00; committed 2024-09-19T10:33:12+08:00.

Adds Export All, writing the collected vanilla artifacts together through a UI callback. Full function context distinguishes actual defects from overstatement: the button is not guarded like the per-data controls and can dereference absent data, and the creative-items NBT output is supplied block-palette data. The static callback borrows a directory variable local to the active render invocation, so it is alive during that loop; reuse across a subsequent render invocation is a conditional lifetime concern rather than a proven immediate dangling reference. Neither output generation nor GUI behavior was executed. The target merge 1827 incorporates this contribution without a separate resolution patch.

<a id="collaborator-ab5d9f3c"></a>

### Collaborator ab5d9f3c {#collaborator-ab5d9f3c}

Source: [ab5d9f3c8d56c190ae763305317507d00d0d7de3](https://github.com/EndstoneMC/endstone/commit/ab5d9f3c8d56c190ae763305317507d00d0d7de3). Author: daoge; committer: GitHub. Authored 2024-09-28T18:58:32+08:00; committed 2024-09-28T11:58:32+01:00.

The author is daoge and the commit explicitly co-authors Vincent. It exposes native block outline, visual, UI and liquid clip shapes through modeled methods/delegates and adds these shapes to DevTools export. The squash message lists preceding adjustments to validity checking, unused camera shape removal and native method signatures. Only the actual squash diff and parent/result context are reviewed here; the listed branch revisions are not silently credited as separately recovered commits. The liquid-clip native call returns a validity boolean that the export path does not use, so data interpretation still depends on native behavior and initialization. No geometric correctness or ABI invocation was tested. This is the immediate non-target parent of 1840, explaining the DAG gap.

<a id="collaborator-5aec5c90"></a>

### Collaborator 5aec5c90 {#collaborator-5aec5c90}

Source: [5aec5c908fab6339add4317302298c72e1e4a30a](https://github.com/EndstoneMC/endstone/commit/5aec5c908fab6339add4317302298c72e1e4a30a). Author: daoge; committer: GitHub. Authored 2024-09-30T15:46:52+08:00; committed 2024-09-30T08:46:52+01:00.

Adds Item::getEnchantValue() to the item export object under enchantValue. The actual change is one export field, so a short disposition is sufficient. Target 1852 merges it; the unrelated block Result changes visible relative to the branch parent are exact inherited reuse, not daoge-authored work. PR #65 discussion is not examined in this unit.

<a id="collaborator-f16793ca"></a>

### Collaborator f16793ca {#collaborator-f16793ca}

Source: [f16793ca25ca71f3bd3cbea4353e93912f1716cf](https://github.com/EndstoneMC/endstone/commit/f16793ca25ca71f3bd3cbea4353e93912f1716cf). Author: Loudbook; committer: GitHub. Authored 2024-10-01T04:47:29-04:00; committed 2024-10-01T09:47:29+01:00.

Corrects expected-lite FetchContent GIT_TAG from 0.8.0 to v0.8.0. This is a concrete dependency-ref spelling repair credited to Loudbook. The target merge 1862 imports it while its opposite-parent view contains the separately read ownership rollback. No dependency fetch or build was run. PR #68 discussion is outside this unit.

<a id="collaborator-b8e78c6f"></a>

### Collaborator b8e78c6f {#collaborator-b8e78c6f}

Source: [b8e78c6fa19b9a114c5d9bab0a004d5c5b0128b7](https://github.com/EndstoneMC/endstone/commit/b8e78c6fa19b9a114c5d9bab0a004d5c5b0128b7). Author: daoge; committer: GitHub. Authored 2024-10-11T18:30:08+08:00; committed 2024-10-11T11:30:08+01:00.

Adds defaultBlockStateHash to each exported block type by asking for its default state hash. This one-line addition is credited to daoge. It is the immediate non-target parent of 1878, so chronological target adjacency alone would miss the imported export change. Full actual diff read; PR #74 conversation and runtime hash stability are not established.
