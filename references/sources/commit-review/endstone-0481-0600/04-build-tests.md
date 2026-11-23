<!-- retrieval: {"source_ids":["public:commit:020a250abb7668a1fa12ec94a5bafc535fca71fd","public:commit:13934efa0b3b1b39e10dd32ab9d3a01f2114c53d","public:commit:207248a7ddbb39a872417586e83f35aa287da349","public:commit:3496014cbcf787e1c589f6bd274ea63f74bd2647","public:commit:65a9a47ecb109f880621875e6dfc1077d68aceab","public:commit:71334a1814ae47563dab606100c1b80194b576b6","public:commit:74cf1a5bd899c16ca7ca0c19da0d6eac6160c19e","public:commit:777727a00ddc3cce6b52b00ce1ca92201d1a7de0","public:commit:7cae4dd3d6c9c16f5ffedfcae2ec05a1c96c058a","public:commit:7dffd278fd227352b36110ad8bb5f2505586d72b","public:commit:832abe60580a8758f8a600a09108f444c8bd2a34","public:commit:93f5584f1a0e461c0c91e5ba038b25bc4dc562fb","public:commit:a7cb51fc2d7f5b5b0a553840cf95238c3f0833a6","public:commit:c5c5fc37f76273539f1574a31a5793c974bfec7d","public:commit:c796fca9c1c136f5ad89fc2877fa4d3abfa77931","public:commit:d98b7a1766f9871301c0f061af174d2a7bf334df","public:commit:de2e019b588b83d1ded806caf764b2f3d104beec","public:commit:de77a93ce1d31a894da9b8cd7d3f4810ee7ad7cf","public:commit:dfa72c16745b19a1f51e7fab1c45e1aa8fbea1fb"],"source_type":"public","date":"2024-03-22..2024-04-06","topics":["lifetime","concurrency","ffi","testing","build","performance","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Build boundaries, test replacement and operational claims {#build-boundaries-test-replacement-and-operational-claims}

## Result and evidence boundary {#result-and-evidence-boundary}

This unit changes testing from a disabled Conan consumer package toward in-tree GTest/GMock loader tests, adds EnTT and adjusts public dependency linkage, introduces a console debug command and revises the plugin metadata macro. It also contains roadmap/version/format changes that are deliberately treated proportionately. The central distinction is between a declared test/configuration change and a verified execution result. All affected test source and configuration was read; no build, import, test runner, package creation, server launch or workflow execution occurred in this research.

## Dependency and collaborator attribution {#dependency-and-collaborator-attribution}

487 adds weekly Dependabot proposals for root pip and GitHub Actions. It declares update automation, not automatic merging. 497 merges the action-release update from softprops/action-gh-release v1 to v2. The side commit is authored by dependabot[bot] and committed by GitHub. The merge is attributed to Vincent (Zhengyu) Wu/GitHub. Its first-parent patch is exactly the side branch's action-version patch; its second-parent patch imports the event/Python work already present on main. Both full parent diffs were read and exact equivalence verified. There are no separate merge-resolution changes.

This distinction prevents crediting the merge author with writing the bot patch or all inherited main changes. It also prevents a metadata-only completion: the second-parent view was examined and reconciled. The external action's source and release notes were not read, so the local version bump supports a configuration observation rather than a detailed claim about v2's behavior. No PR discussion or approval is inferred from GitHub being the committer.

510 moves magic_enum to public core linkage as ping parsing begins using it. 576 adds EnTT to CMake and Conan for service-location/table management. 577 repairs the Conan component requirement from the CMake-style EnTT::EnTT spelling to entt::entt. Package recipe component names and generated CMake imported targets are related but distinct interfaces. Endpoint configuration retains CMake's EnTT::EnTT target. These source-level corrections do not prove a consumer package build passed.

509's test-package fix is architectural rather than a simple test edit: PluginManager stops reaching directly into native threading and asks Server.isPrimaryThread. The test implementation returns true. That isolates core tests from the host thread symbol, but the stubbed answer cannot validate real thread affinity or rejection of wrong-thread events. Testability and tested behavior must be recorded separately.

## Disabling, replacing and deleting a consumer test {#disabling-replacing-and-deleting-a-consumer-test}

571 renames test_package to test_package_ with five exact-identical file blobs. No source text changes, yet the directory name is the conventional Conan discovery hook. The explicit commit message calls this a temporary disable. This is therefore an operationally meaningful path change, not harmless rename noise. The exact blob identities allow source-content reuse without hiding the disabled integration point.

589 adds a GMock-derived Server and CppPluginLoader tests. The cases cover nonexistent versus valid library load, loading a directory containing one fixture and expected platform extension filters. Logger call counts are asserted, and 593 adds plugin name/version assertions. A shared fixture plugin is built against the public headers and contains declarative command/permission metadata and lifecycle logging methods.

Those are useful loader checks, but they are not equivalent to the removed consumer suite. The old Conan test consumed the packaged endstone CMake configuration, built a small server/plugin pair, loaded through EndstonePluginManager and asserted plugin enabled state before/after manager enable/disable. It also exercised logger calls. The new cases call CppPluginLoader directly and check metadata/filter results; the fixture's onEnable/onDisable methods are not evidence they are actually exercised by these tests. Neither suite validates the native game's ABI, and the new suite does not establish exported package-consumer target correctness.

591's message says the tests are already covered by GTest. The diff shows removal of the disabled suite, but no one-to-one lifecycle/package assertions replacing those old checks. That claim should be preserved as the author's stated rationale while coverage equivalence remains unproven. The deleted TestServer also lacks the newly added pure virtual level methods, so the old source had become stale while disabled. This is a dated tradeoff, not a judgment that the deleted tests were all currently runnable or that the replacement had no value.

590 moves tests into command/plugin subdirectories using identical blobs. Its CMake executable source glob is initially nonrecursive, so moved cases are no longer included by that pattern until 592 switches to GLOB_RECURSE with CONFIGURE_DEPENDS. The fixture plugin source is also picked up by the broad executable glob, and there is no explicit executable-to-fixture target dependency in the observed CMake. These are source/build graph facts; no failing build is asserted. A full default build may still build both targets, while a narrowly selected target is a different path.

590 separately narrows gcovr's filter from src/ to src/endstone_core/. That changes what a coverage percentage describes. A higher or lower reported number across the boundary cannot by itself establish improved testing of runtime/Python code, and no actual report was captured in this unit. Test movement, source discovery and coverage measurement scope are three changes that need separate accounting.

## Metadata initialization moves earlier in library lifetime {#metadata-initialization-moves-earlier-in-library-lifetime}

593 revises ENDSTONE_PLUGIN. Previously a static builder existed, and each exported factory call invoked a description-initialization function before constructing the plugin. Afterward a derived static builder runs the user's metadata body in its constructor, and the factory only constructs the plugin. Macro users migrate from plugin.description/plugin.command syntax to unqualified builder members. That is a source-level DSL change, not merely formatting.

The observed benefit is that the initializer body no longer reruns on every factory call. Existing builder maps/sets already reuse keys or accumulate values, so it would be too strong to claim all earlier metadata necessarily duplicated on each load. The change does shift execution to shared-library static initialization, before the loader calls the factory or checks the plugin's declared API version. Static initialization ordering, exceptions and interactions with other globals are therefore part of the new lifetime boundary. The tests add basic name/version assertions, not explicit repeat-factory or static-initialization failure cases.

The prior unit's native compatibility gate still occurs after the library is loaded and the factory returns. Endpoint source still returns early on incompatible API before wrapping the raw plugin pointer in unique_ptr, and the accepted module handle is not managed as an unloading owner in this loader. These inherited ownership limits are not repaired by the new macro or tests. The relevant connection is that moving setup earlier changes what has already executed by the time a gate rejects a plugin.

## Debugging controls and configuration policy {#debugging-controls-and-configuration-policy}

584 adds /debug with an operator-default permission and an additional exact-identity check against the server console sender. Endpoint CommandAdapter context routes DedicatedServer origins to that exact singleton sender, while other origins get an adapter object. An operator player is therefore not sufficient under this implementation. The required boolean argument selects Debug or Info logging and emits a confirmation. The direct method indexes args[0], relying on normal command parsing to provide it. This is a logging threshold toggle, not a profiler, a global subsystem debug mode or an unrestricted in-game control. No runtime command test accompanies it.

569 disables misc-include-cleaner in clang-tidy, and 582 changes value-template-parameter naming to CamelCase while updating matching template names. The former changes analysis policy; the latter is a naming rule/source synchronization. 580–581 consistently qualify size and fixed-width integer types with std:: without changing their widths or expressions. These are verified small/mechanical dispositions, unlike 567's long-to-int32_t declaration change hiding inside a style patch. The method is to inspect the real diff first, then scale the analysis to what changed.

558 selects Minecraft 1.20.73 and updates the README badge. That is a bounded version-selection change, not proof of compatibility with every reverse-engineered table or native layout. The public GameMode numeric repair and pybind alias correction are substantive separate commits and are not swallowed into version noise.

## Roadmaps, evidence and future use {#roadmaps-evidence-and-future-use}

482/488/505 mark event API milestones underway/complete. These are dated project communications. They cannot erase the concrete distinctions established in the other dossiers: manager dispatch was implemented at 481, reflection registration arrived later, async validation is not scheduling, console rewriting is not wired back, provisional coordinator hooks were removed, and unload lifetimes remain incomplete. A roadmap's granularity can be coarser than the implementation's guarantees.

For future engineering work, this chain supports checking whether a test moved out of discovery, whether package-consumer and unit-test layers are both covered, whether a coverage filter changed, whether a metadata factory runs initialization once or repeatedly, and whether dependency names refer to the same build namespace. These are evidence-based review prompts rather than claims about a universal preferred workflow. Exact per-source coverage and changed test paths are below; reported fixes stay reported, and runtime validation remains unperformed.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-482"></a>
### 482. docs: update README.md {#commit-482}

Source: [207248a7ddbb39a872417586e83f35aa287da349](https://github.com/EndstoneMC/endstone/commit/207248a7ddbb39a872417586e83f35aa287da349) · authored 2024-03-22T14:53:39Z. Actual parent(s): `24c82a5fcaa9b79ed027a098905bd62c12adf986`.

Author: **Vincent**.

Roadmap changes C++ event API from pending to underway. Dated status claim only; no executable changes.

First-parent changed paths: `README.md`.

Coverage: 13 canonical first-parent patch lines; 13 across all actual parents.

<a id="commit-487"></a>
### 487. chore(ci) : setup dependabot {#commit-487}

Source: [de2e019b588b83d1ded806caf764b2f3d104beec](https://github.com/EndstoneMC/endstone/commit/de2e019b588b83d1ded806caf764b2f3d104beec) · authored 2024-03-22T17:10:59Z. Actual parent(s): `c86eb9e191a3a324ded6682d333180f8a51d318a`.

Author: **Vincent (Zhengyu) Wu**.

Adds weekly Dependabot updates for root pip and GitHub Actions ecosystems. This declares automated dependency proposals, not automatic merge or test success. Git author Vincent (Zhengyu) Wu and committer GitHub are preserved; next merge imports a bot-authored action bump.

First-parent changed paths: `.github/dependabot.yml`.

Coverage: 16 canonical first-parent patch lines; 16 across all actual parents.

<a id="commit-488"></a>
### 488. docs: update README.md {#commit-488}

Source: [93f5584f1a0e461c0c91e5ba038b25bc4dc562fb](https://github.com/EndstoneMC/endstone/commit/93f5584f1a0e461c0c91e5ba038b25bc4dc562fb) · authored 2024-03-22T17:11:14Z. Actual parent(s): `de2e019b588b83d1ded806caf764b2f3d104beec`.

Author: **Vincent**.

Marks C++ event API complete and Python underway in README. Treat as dated scope claim; async checks and lifetime limitations remain separately recorded.

First-parent changed paths: `README.md`.

Coverage: 13 canonical first-parent patch lines; 13 across all actual parents.

<a id="commit-497"></a>
### 497. Merge pull request #6 from EndstoneMC/dependabot/github_actions/softprops/action-gh-release-2 {#commit-497}

Source: [65a9a47ecb109f880621875e6dfc1077d68aceab](https://github.com/EndstoneMC/endstone/commit/65a9a47ecb109f880621875e6dfc1077d68aceab) · authored 2024-03-22T18:38:49Z. Actual parent(s): `5bae2949240505c4c7acd874757ba23a33157fdd`, `aaba999c82c7aa048df755cfde58273f72d613b7`.

Author: **Vincent (Zhengyu) Wu**.

Merges PR #6: first-parent diff only upgrades softprops/action-gh-release v1 to v2, authored on side branch by dependabot[bot]. Both full parent diffs read; second-parent diff imports already reviewed 489–496 event/Python changes. No distinct resolution edits found by exact patch/tree checks recorded in merge coverage. Merge attribution is Vincent (Zhengyu) Wu/GitHub, not authorship of bot dependency work. External action implementation/release notes were not read.

First-parent changed paths: `.github/workflows/wheel.yml`.

Coverage: 13 canonical first-parent patch lines; 638 across all actual parents.

<a id="commit-505"></a>
### 505. docs: update README.md {#commit-505}

Source: [d98b7a1766f9871301c0f061af174d2a7bf334df](https://github.com/EndstoneMC/endstone/commit/d98b7a1766f9871301c0f061af174d2a7bf334df) · authored 2024-03-23T23:08:13Z. Actual parent(s): `07371848f22c180fed87db59520d15f375edd646`.

Author: **Vincent**.

Marks Python event API complete while event core remains underway. README status only, not proof of thread checks, native cancellation or callback-lifetime completeness.

First-parent changed paths: `README.md`.

Coverage: 13 canonical first-parent patch lines; 13 across all actual parents.

<a id="commit-509"></a>
### 509. ci: fix test_package {#commit-509}

Source: [de77a93ce1d31a894da9b8cd7d3f4810ee7ad7cf](https://github.com/EndstoneMC/endstone/commit/de77a93ce1d31a894da9b8cd7d3f4810ee7ad7cf) · authored 2024-03-25T10:44:05Z. Actual parent(s): `4d35685c756e11c5129c4374cc0249509f8fd67c`.

Author: **Vincent**.

Title says test-package fix but adds public Server.isPrimaryThread and moves the native thread dependency out of PluginManager into EndstoneServer. TestServer supplies true, allowing core manager linkage without host threading symbol. This is a dependency-inversion/testability change, not a test of real thread-affinity behavior.

First-parent changed paths: `include/endstone/detail/server.h`, `include/endstone/server.h`, `src/endstone_core/plugin/plugin_manager.cpp`, `src/endstone_core/server.cpp`, `test_package/src/test_server.cpp`.

Coverage: 97 canonical first-parent patch lines; 97 across all actual parents.

<a id="commit-510"></a>
### 510. chore: update .clang-tidy and CMakeLists.txt {#commit-510}

Source: [c5c5fc37f76273539f1574a31a5793c974bfec7d](https://github.com/EndstoneMC/endstone/commit/c5c5fc37f76273539f1574a31a5793c974bfec7d) · authored 2024-03-25T11:34:21Z. Actual parent(s): `de77a93ce1d31a894da9b8cd7d3f4810ee7ad7cf`.

Author: **Vincent**.

Moves magic_enum from private runtime linkage to public core linkage and changes constexpr-variable naming rule. Transitive dependency exposure supports core use in ping event parsing; no library upgrade or algorithm change.

First-parent changed paths: `.clang-tidy`, `CMakeLists.txt`.

Coverage: 35 canonical first-parent patch lines; 35 across all actual parents.

<a id="commit-514"></a>
### 514. fix: compilation errors on Linux with clang {#commit-514}

Source: [a7cb51fc2d7f5b5b0a553840cf95238c3f0833a6](https://github.com/EndstoneMC/endstone/commit/a7cb51fc2d7f5b5b0a553840cf95238c3f0833a6) · authored 2024-03-25T12:43:44Z. Actual parent(s): `8ace9966d1f82d3492e6ba2a0022ada3efb9352c`.

Author: **Vincent**.

Adds cstddef to RakNet types after a reported Linux clang compilation error. Direct declaration dependency repair only; no compiler run in this research.

First-parent changed paths: `include/bedrock/raknet/types.h`.

Coverage: 12 canonical first-parent patch lines; 12 across all actual parents.

<a id="commit-558"></a>
### 558. feat: game update v1.20.73 {#commit-558}

Source: [13934efa0b3b1b39e10dd32ab9d3a01f2114c53d](https://github.com/EndstoneMC/endstone/commit/13934efa0b3b1b39e10dd32ab9d3a01f2114c53d) · authored 2024-04-04T14:21:59Z. Actual parent(s): `692e85ea83b83346c3978075a50caf539ca5e346`.

Author: **Vincent**.

Updates selected game version and README badge1.20.72→1.20.73. Full diff verified as version selection only; no compatibility tests or download result inferred.

First-parent changed paths: `README.md`, `python/src/endstone/__init__.py`.

Coverage: 24 canonical first-parent patch lines; 24 across all actual parents.

<a id="commit-569"></a>
### 569. style: update clang-tidy configuration. {#commit-569}

Source: [020a250abb7668a1fa12ec94a5bafc535fca71fd](https://github.com/EndstoneMC/endstone/commit/020a250abb7668a1fa12ec94a5bafc535fca71fd) · authored 2024-04-05T01:12:49Z. Actual parent(s): `0098ee9775723201dbf494c8a78d55261b6bb0ef`.

Author: **Vincent**.

Disables misc-include-cleaner in clang-tidy and reorders another exclusion. Changes static-analysis policy, not source includes or runtime behavior; no rationale stated.

First-parent changed paths: `.clang-tidy`.

Coverage: 15 canonical first-parent patch lines; 15 across all actual parents.

<a id="commit-571"></a>
### 571. refactor: temporarily disable conan test_package {#commit-571}

Source: [dfa72c16745b19a1f51e7fab1c45e1aa8fbea1fb](https://github.com/EndstoneMC/endstone/commit/dfa72c16745b19a1f51e7fab1c45e1aa8fbea1fb) · authored 2024-04-05T09:55:32Z. Actual parent(s): `735eb92099ab19bbedb235d21e4e9ff2744b82e4`.

Author: **Vincent**.

Renames all five test_package files to test_package_ with exact identical blobs. Explicitly disables Conan conventional package-consumer test discovery temporarily; path change is operationally meaningful despite content identity. Later589 adds GTest loader tests and591 removes this suite.

First-parent changed paths: `test_package/.gitignore`, `test_package/CMakeLists.txt`, `test_package/conanfile.py`, `test_package/src/test_plugin.cpp`, `test_package/src/test_server.cpp`, `test_package_/.gitignore`, `test_package_/CMakeLists.txt`, `test_package_/conanfile.py`, `test_package_/src/test_plugin.cpp`, `test_package_/src/test_server.cpp`.

Coverage: 696 canonical first-parent patch lines; 696 across all actual parents.

<a id="commit-577"></a>
### 577. fix: conan package {#commit-577}

Source: [c796fca9c1c136f5ad89fc2877fa4d3abfa77931](https://github.com/EndstoneMC/endstone/commit/c796fca9c1c136f5ad89fc2877fa4d3abfa77931) · authored 2024-04-05T22:09:48Z. Actual parent(s): `d25bc41eca88ffb19aed805a3fb492bfa04eec67`.

Author: **Vincent**.

Corrects Conan component dependency EnTT::EnTT to entt::entt while CMake imported target remains EnTT::EnTT. Package naming and CMake naming are distinct contracts. No package build was executed here.

First-parent changed paths: `conanfile.py`.

Coverage: 13 canonical first-parent patch lines; 13 across all actual parents.

<a id="commit-582"></a>
### 582. style: update ValueTemplateParameterCase naming convention in .clang-tidy {#commit-582}

Source: [777727a00ddc3cce6b52b00ce1ca92201d1a7de0](https://github.com/EndstoneMC/endstone/commit/777727a00ddc3cce6b52b00ce1ca92201d1a7de0) · authored 2024-04-06T11:31:10Z. Actual parent(s): `4e1f1317a1c5f93444a9a891106b42bbc0aa645d`.

Author: **Vincent**.

Changes value-template-parameter naming rule to CamelCase and renames VirtualTable Index parameters consistently. No slot arithmetic or branch change.

First-parent changed paths: `.clang-tidy`, `include/endstone/detail/virtual_table.h`.

Coverage: 84 canonical first-parent patch lines; 84 across all actual parents.

<a id="commit-584"></a>
### 584. feat: add /debug command {#commit-584}

Source: [74cf1a5bd899c16ca7ca0c19da0d6eac6160c19e](https://github.com/EndstoneMC/endstone/commit/74cf1a5bd899c16ca7ca0c19da0d6eac6160c19e) · authored 2024-04-06T17:53:17Z. Actual parent(s): `00598559bd9de0fc4db1d52555093da4341b9b30`.

Author: **Vincent**.

Adds console-only /debug command and operator-default permission. Identity check requires exact server command sender object, not merely op status. Boolean argument sets logger Debug or Info and prints status; direct execute assumes args[0] exists, relying on command parsing. No profiling or global-debug-state feature implied.

First-parent changed paths: `include/endstone/detail/command/defaults/debug_command.h`, `src/endstone_core/command/command_map.cpp`, `src/endstone_core/command/defaults/debug_command.cpp`, `src/endstone_core/permissions/default_permissions.cpp`.

Coverage: 128 canonical first-parent patch lines; 128 across all actual parents.

<a id="commit-589"></a>
### 589. test: add tests for CppPluginLoader {#commit-589}

Source: [832abe60580a8758f8a600a09108f444c8bd2a34](https://github.com/EndstoneMC/endstone/commit/832abe60580a8758f8a600a09108f444c8bd2a34) · authored 2024-04-06T22:47:55Z. Actual parent(s): `f504a876f31c19978bf98762e622a72c892e156a`.

Author: **Vincent**.

Adds GMock Server and loader GTests for missing/valid file, directory loading and platform extension filters, plus shared test plugin built from same header API. Tests check loader paths/log calls, not manager enable/disable lifecycle or native host integration. CMake broad test glob also includes fixture plugin source; no explicit executable→fixture target dependency shown. Test source read only.

First-parent changed paths: `CMakeLists.txt`, `include/endstone/detail/plugin/cpp_plugin_loader.h`, `tests/test_cpp_plugin_loader.cpp`, `tests/test_plugin.cpp`.

Coverage: 206 canonical first-parent patch lines; 206 across all actual parents.

<a id="commit-590"></a>
### 590. refactor: move test files {#commit-590}

Source: [71334a1814ae47563dab606100c1b80194b576b6](https://github.com/EndstoneMC/endstone/commit/71334a1814ae47563dab606100c1b80194b576b6) · authored 2024-04-06T22:53:50Z. Actual parent(s): `832abe60580a8758f8a600a09108f444c8bd2a34`.

Author: **Vincent**.

Moves test files with exact blob identity and narrows gcovr filter from all src to src/endstone_core. Nonrecursive CMake glob is not yet updated for moved nested tests, repaired592. Coverage scope changes independently of test relocation; percentages across boundary are not directly comparable.

First-parent changed paths: `.github/workflows/coverage.yml`, `CMakeLists.txt`, `tests/command/test_command_lexer.cpp`, `tests/command/test_command_usage_parser.cpp`, `tests/plugin/test_cpp_plugin_loader.cpp`, `tests/plugin/test_plugin.cpp`, `tests/test_command_lexer.cpp`, `tests/test_command_usage_parser.cpp`, `tests/test_cpp_plugin_loader.cpp`, `tests/test_logger.cpp`, `tests/test_logger_factory.cpp`, `tests/test_plugin.cpp`.

Coverage: 1188 canonical first-parent patch lines; 1188 across all actual parents.

<a id="commit-591"></a>
### 591. refactor: remove `test_package` directory as tests are already covered by GTest {#commit-591}

Source: [3496014cbcf787e1c589f6bd274ea63f74bd2647](https://github.com/EndstoneMC/endstone/commit/3496014cbcf787e1c589f6bd274ea63f74bd2647) · authored 2024-04-06T22:56:41Z. Actual parent(s): `71334a1814ae47563dab606100c1b80194b576b6`.

Author: **Vincent**.

Deletes disabled Conan test_package_ with explicit claim tests covered by GTest. Old suite consumed packaged endstone CMake targets and asserted manager load/enable/disable transitions;589 loader tests cover a narrower different layer. Thus replacement claim is not proven equivalence. Deleted TestServer also lacks newly added pure virtual level methods; suite was already disabled571. Fixture plugin blob is identical to newly copied589 test.

First-parent changed paths: `test_package_/.gitignore`, `test_package_/CMakeLists.txt`, `test_package_/conanfile.py`, `test_package_/src/test_plugin.cpp`, `test_package_/src/test_server.cpp`.

Coverage: 348 canonical first-parent patch lines; 348 across all actual parents.

<a id="commit-592"></a>
### 592. fix: recursively glob test source files {#commit-592}

Source: [7cae4dd3d6c9c16f5ffedfcae2ec05a1c96c058a](https://github.com/EndstoneMC/endstone/commit/7cae4dd3d6c9c16f5ffedfcae2ec05a1c96c058a) · authored 2024-04-06T22:59:57Z. Actual parent(s): `3496014cbcf787e1c589f6bd274ea63f74bd2647`.

Author: **Vincent**.

Changes test collection to GLOB_RECURSE CONFIGURE_DEPENDS, restoring discovery of nested files moved590. Also collects nested fixture plugin source into test executable as previous broad glob did; no test run outcome inferred.

First-parent changed paths: `CMakeLists.txt`.

Coverage: 13 canonical first-parent patch lines; 13 across all actual parents.

<a id="commit-593"></a>
### 593. refactor: improve ENDSTONE_PLUGIN macro {#commit-593}

Source: [7dffd278fd227352b36110ad8bb5f2505586d72b](https://github.com/EndstoneMC/endstone/commit/7dffd278fd227352b36110ad8bb5f2505586d72b) · authored 2024-04-06T23:17:23Z. Actual parent(s): `7cae4dd3d6c9c16f5ffedfcae2ec05a1c96c058a`.

Author: **Vincent**.

Moves ENDSTONE_PLUGIN description setup from per-factory init function to constructor of static derived builder. Metadata DSL now uses unqualified members instead of plugin prefix. This avoids repeating initialization on each factory call, but shifts execution to shared-library static initialization and remains globally stored. Adds name/version assertions, not explicit repeated-factory or initialization-failure tests. Breaking source-level macro-body change accompanies concise title.

First-parent changed paths: `include/endstone/plugin/plugin.h`, `tests/plugin/test_cpp_plugin_loader.cpp`, `tests/plugin/test_plugin.cpp`.

Coverage: 104 canonical first-parent patch lines; 104 across all actual parents.
