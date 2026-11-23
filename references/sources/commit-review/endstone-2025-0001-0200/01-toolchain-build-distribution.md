<!-- retrieval: {"source_ids":["public:commit:0cc67df4f8af414147a1627821ebdce9ae769d19","public:commit:175e6572ed9468520064cf6099ea0c58422488a9","public:commit:287c1ed1def343f09f714b225fe2c852078763e5","public:commit:28b1b20117c2601777f40a0cf59533e63b411151","public:commit:2b93464d80fc20a8963149bb5a5e94277c206a6a","public:commit:2c2b391142066b0a12ab13815e509fb587b1cd5e","public:commit:2d567b6642f70ed016396d9cb586cd4d2bb97e65","public:commit:32f570321aef1426283b065ae305f78ffd136883","public:commit:335687277d563f48baee4ee7386be4ce32d8ad9d","public:commit:3780da8807b8f506c6ece16c65c376f651d2ab99","public:commit:4cd28edf0c9928dfe33e31766f267727ba35ff1d","public:commit:554d8564db4548fb885c76affac9ef4b31169f7c","public:commit:55b70f7c8be79a406be1275778d592de7895e977","public:commit:592a5323062722221cdaa639f83faf3301014bb0","public:commit:5b7d3f375067170cf7d4c523be384058c40ace1e","public:commit:5bb1a09351bd83f38a486a3f7ab34c2fa50a562d","public:commit:6bd93555c0d903dbb731f4362870f63332a5353e","public:commit:7689c6c1c450e0b42936c772ec345cf19ecbe1dd","public:commit:812c0df39a95a0bff31669329eaff022a0352c11","public:commit:855684124e948f7a098c6712820bead297a13a2f","public:commit:8eb9ab80005b5ccf2a638dae1f728e2794747e38","public:commit:90b65613f83b3d2ae0be35971840140b642d4229","public:commit:948e02ec9981889e3b806de45a6d76fba44b4eb0","public:commit:a49bb90bc59a580a78cf17117456c7ec9a1cae30","public:commit:bb74bbbd2ee14538289377e517152c58cd461e09","public:commit:cd1da494b30c7b57934493a500629ba771d174d1","public:commit:d8e3f061f2f9011a412f1f537786770f489422b8","public:commit:e51df0e12a763dde465292a18f7ec7170cec54e9","public:commit:ed9673ed2f1f4c027f908d5d874186c4c1521ec6","public:commit:f0a0aa42ff77a19272188f4c869703b68c13c96a","public:commit:f4cb5564d3fbe4f3a8cefd69f94fb7bf3105dcd9","public:commit:f6c3a79e35947762cf98c38842c9b6ef4e0d77c8","public:commit:f9f0b6bfc5b82eee302479fa7a1c649de08498c8","public:commit:ff3040a9bd24c26479a2f7255b5a6c6092a6c314"],"source_type":"public","date":"2025-01-01..2025-01-11","topics":["ffi","testing","build","api","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Toolchain, build graph and distribution {#toolchain-build-graph-and-distribution}

## Decision chain and usable lessons {#decision-chain-and-usable-lessons}

The January1 changes make C++20 a project-wide contract, then repair the source consequences instead of treating the flag as sufficient. The logger's virtual signature changes to string_view, fmt compile-time format checking needs explicit runtime formats, and the public formatting helper requires a nonempty argument pack to avoid competing with plain-message calls (1–3). The Error implementation still owns a string. An API review must therefore distinguish borrowed input views from retained storage and distinguish an ABI-visible virtual change from a source-only optimization. The subject of3 claims a compilation fix; incomplete-type ordering is a code-based explanation rather than a recorded compiler diagnostic.

Compiler choice evolves over several commits. The minimum Clang threshold briefly goes10→9 before Crashpad makes LLVM16 a stated dependency requirement. The Conan comment acknowledges Bedrock's15.0.7 compiler and assumes compatibility. The later public umbrella rejects MSVC debug iterators because the Bedrock binary uses release iterators (55). These are real constraints and explicit assumptions, not evidence from an ABI compatibility matrix.88 removes Debug jobs,89 restores Linux Debug only; connecting that sequence to the explicit MSVC iterator guard is a reasonable inference, not an additional author statement.

The distribution work is an iterative chain with reversals.22 separates .dbg files, strips debug data and adds GNU debuglinks;24 temporarily comments it out without explaining why;78 restores the mechanism behind a default-OFF switch.23 separately unpacks wheels, uploads debug data and sources with sentry-cli, optionally removes symbols, then repairs/repackages. Copying Crashpad before stripping it (21) avoids modifying a cached dependency package.26 fixes an intermediate Linux shared-library install category. It would be misleading to recommend the intermediate22 wheel configuration or say Linux symbols are always separated. Uploading source files to Sentry is visible workflow behavior, not an action performed by this research. Diagnostic command logging may expose a token if passed explicitly; no actual credential or leak is asserted.

Caches are also platform-specific, not a generic recipe:10 caches all Conan home,12 adds build type,20 replaces absent matrix dimensions with literal RelWithDebInfo,89 narrows to the package directory,91 maps the Linux host cache into cibuildwheel's /host mount. The broad restore prefixes can cross build-type boundaries, with Conan package identities expected to distinguish the contents. No cache hit rate or speedup was observed.96 updates all three portable WinPython coordinates, download URL, digest and extraction path, together; the binary was not fetched or executed.

## Structural transition and tests {#structural-transition-and-tests}

52 deletes unused vendored Conan recipes and fixtures. Active FetchContent still retrieves funchook, so this is not abandonment of hooking. Fifteen deleted blobs were matched to earlier completed exact-object reviews; the one unmatched recipe was fully read. The old fixtures retain third-party provenance, including an earlier formatting regression in assembly. Their deletion is not proof those dependency tests passed.

54 moves the Python package by exact blob identity; its font is an identical binary relocation, not a new visual asset.55 changes the package metadata, includes and public plugin-builder location.59 enables the devtool target and60 uses an explicit native test source list and the new plugin filename. A crucial counterexample to title-based completion:60 removes gtest_discover_tests and the final100 tests/CMakeLists.txt still has no registration call. Building an executable is not running or discovering its tests. A successor worker reports restoration at118, outside this completed unit. No build, test, generator, compiler, wheel, native server or CI run was executed or claimed.

65 and85 state Windows/Linux build fixes, but they do not supply run logs. The Linux platform source at 100 still defines get_name while its declaration and crash caller require get_platform. This static mismatch is directly preserved in the context manifest. Likewise the generator's65 skipped entries leave the declared array size based on the input table size; a zero-default tail can exist when entries are skipped. That risk is conditional on input data, not a demonstrated release failure.

## Applicability and limits {#applicability-and-limits}

Use this chain for reviews of compiler/API migrations, native plugin ABI, platform packaging and diagnostic pipelines. Follow the complete dependency chain, separate generated settings from observed artifacts, and include intermediate reversals. Do not infer a lasting preference for a specific compiler, crash backend or cache policy merely from a temporary commit. The per-commit records below preserve every individual source identity.


<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}



<a id="commit-001"></a>
### 001. chore: update project to require C++20 standard {#commit-001}

Commit: [855684124e948f7a098c6712820bead297a13a2f](https://github.com/EndstoneMC/endstone/commit/855684124e948f7a098c6712820bead297a13a2f) · committed 2025-01-01T15:17:57Z · author Vincent.

Actual parent: `2a421c86abb6fa27e361dc12c1373acc772636f7`. Full message and parent-relative patch: local source.

Raises C++17 to C++20 consistently across Conan validation, CI, coverage, developer instructions and wheel overrides; Linux drops gnu17 for strict 20. Clang lower bound initially moves 5→10 under an explicit presumed ABI-compatibility comment. No compilation result accompanies the requirement change.

Changed-file coverage: 5 paths. `.github/workflows/ci.yml`; `.github/workflows/coverage.yml`; `CONTRIBUTING.md`; `conanfile.py`; `pyproject.toml`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-002"></a>
### 002. fix: resolve C++20 compilation errors {#commit-002}

Commit: [948e02ec9981889e3b806de45a6d76fba44b4eb0](https://github.com/EndstoneMC/endstone/commit/948e02ec9981889e3b806de45a6d76fba44b4eb0) · committed 2025-01-01T16:39:08Z · author Vincent.

Actual parent: `855684124e948f7a098c6712820bead297a13a2f`. Full message and parent-relative patch: local source.

Repairs the C++20/fmt transition rather than only changing compiler flags: logger virtual ABI takes string_view, formatting overloads require nonempty packs, runtime filename patterns use fmt::runtime, colored log prefixes become arguments to literal formats, missing plugin-name format argument is supplied, and Python logger lambdas follow the signature. Error owns copied strings despite string_view access; the Logger virtual signature is an API/ABI change. Formatting edits in Error are mechanical.

Changed-file coverage: 12 paths. `include/bedrock/server/commands/command_registry.h`; `include/endstone/detail/spdlog/spdlog_adapter.h`; `include/endstone/detail/util/error.h`; `include/endstone/logger.h`; `include/endstone/util/error.h`; `src/endstone_core/command/defaults/version_command.cpp`; `src/endstone_core/plugin/plugin_manager.cpp`; `src/endstone_core/scheduler/async_task.cpp`; `src/endstone_core/server.cpp`; `src/endstone_core/spdlog/file_log_sink.cpp`; `src/endstone_core/spdlog/spdlog_adapter.cpp`; `src/endstone_python/endstone_python.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-003"></a>
### 003. fix: resolve compilation errors {#commit-003}

Commit: [f6c3a79e35947762cf98c38842c9b6ef4e0d77c8](https://github.com/EndstoneMC/endstone/commit/f6c3a79e35947762cf98c38842c9b6ef4e0d77c8) · committed 2025-01-01T17:04:44Z · author Vincent.

Actual parent: `948e02ec9981889e3b806de45a6d76fba44b4eb0`. Full message and parent-relative patch: local source.

Moves CommandRegistry::Overload construction out of line and registerOverload template after complete CommandParameterData definition; preserves registration order and returning the vector's back element. DataItem gains a public ID alias/constructor and loses SynchedActorData friendship. Compilation fix is explicit; incomplete-type pressure is inferred from the relocation, not a quoted diagnosis.

Changed-file coverage: 3 paths. `include/bedrock/server/commands/command_registry.h`; `include/bedrock/world/actor/synched_actor_data.h`; `src/endstone_runtime/bedrock/server/commands/command_registry.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-004"></a>
### 004. chore(deps): add sentry-native dependency {#commit-004}

Commit: [a49bb90bc59a580a78cf17117456c7ec9a1cae30](https://github.com/EndstoneMC/endstone/commit/a49bb90bc59a580a78cf17117456c7ec9a1cae30) · committed 2025-01-01T17:33:36Z · author Vincent.

Actual parent: `f6c3a79e35947762cf98c38842c9b6ef4e0d77c8`. Full message and parent-relative patch: local source.

Adds sentry-native 0.7.15 and moves cpptrace's package component requirement from core to runtime, with Sentry also required by runtime. Dependency graph changes precede actual initialization.

Changed-file coverage: 1 paths. `conanfile.py`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-005"></a>
### 005. style: format codes {#commit-005}

Commit: [4cd28edf0c9928dfe33e31766f267727ba35ff1d](https://github.com/EndstoneMC/endstone/commit/4cd28edf0c9928dfe33e31766f267727ba35ff1d) · committed 2025-01-01T17:33:50Z · author Vincent.

Actual parent: `a49bb90bc59a580a78cf17117456c7ec9a1cae30`. Full message and parent-relative patch: local source.

Only wraps one Python find_python os.path.join call across lines; exact read supports no independent semantic lesson.

Changed-file coverage: 1 paths. `python/src/endstone/_internal/plugin_loader.py`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-006"></a>
### 006. refactor: rename `_devtools_enabled` to `_should_enable_devtools` {#commit-006}

Commit: [592a5323062722221cdaa639f83faf3301014bb0](https://github.com/EndstoneMC/endstone/commit/592a5323062722221cdaa639f83faf3301014bb0) · committed 2025-01-01T17:50:58Z · author Vincent.

Actual parent: `4cd28edf0c9928dfe33e31766f267727ba35ff1d`. Full message and parent-relative patch: local source.

Renames devtools settings/macros and moves compile-definition responsibility from global CMake into core's PUBLIC interface; introduces dev-build detection and revises the proposed minimum Clang 10→9. A transient mismatch remains: Conan writes ENDSTONE_ENABLE_DEVTOOLS while core tests ENDSTONE_DEVTOOLS_ENABLED; next commit repairs it. This is more than the subject's property rename.

Changed-file coverage: 7 paths. `CMakeLists.txt`; `conanfile.py`; `src/endstone_core/CMakeLists.txt`; `src/endstone_core/command/command_map.cpp`; `src/endstone_core/permissions/default_permissions.cpp`; `src/endstone_runtime/main.cpp`; `src/endstone_runtime/windows/signal_handler.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-007"></a>
### 007. feat: add CMake options for sentry {#commit-007}

Commit: [3780da8807b8f506c6ece16c65c376f651d2ab99](https://github.com/EndstoneMC/endstone/commit/3780da8807b8f506c6ece16c65c376f651d2ab99) · committed 2025-01-01T18:07:30Z · author Vincent.

Actual parent: `592a5323062722221cdaa639f83faf3301014bb0`. Full message and parent-relative patch: local source.

Introduces explicit devtools/Sentry CMake options and DSN/environment cache variables; synchronizes every devtools conditional with ENDSTONE_ENABLE_DEVTOOLS and chooses development/production from Conan version. Sentry defaults disabled at this stage.

Changed-file coverage: 4 paths. `CMakeLists.txt`; `conanfile.py`; `src/endstone_core/CMakeLists.txt`; `src/endstone_runtime/CMakeLists.txt`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-008"></a>
### 008. chore: update libc++ to 16 {#commit-008}

Commit: [ed9673ed2f1f4c027f908d5d874186c4c1521ec6](https://github.com/EndstoneMC/endstone/commit/ed9673ed2f1f4c027f908d5d874186c4c1521ec6) · committed 2025-01-01T23:14:23Z · author Vincent.

Actual parent: `3780da8807b8f506c6ece16c65c376f651d2ab99`. Full message and parent-relative patch: local source.

Moves CI, coverage, Docker and wheel compiler/libc++ setup to LLVM16; recipe comment explicitly says Crashpad requires16 while Bedrock uses15.0.7. This is a requirement and ABI assumption, not compatibility validation.

Changed-file coverage: 5 paths. `.github/workflows/ci.yml`; `.github/workflows/coverage.yml`; `Dockerfile`; `conanfile.py`; `pyproject.toml`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-009"></a>
### 009. ci: increase priority of clang alternatives {#commit-009}

Commit: [0cc67df4f8af414147a1627821ebdce9ae769d19](https://github.com/EndstoneMC/endstone/commit/0cc67df4f8af414147a1627821ebdce9ae769d19) · committed 2025-01-02T00:01:14Z · author Vincent.

Actual parent: `ed9673ed2f1f4c027f908d5d874186c4c1521ec6`. Full message and parent-relative patch: local source.

Raises clang and clang++ alternative priority100→200 in CI/coverage, leaving linker/coverage priorities100. No compiler output proves final selection.

Changed-file coverage: 2 paths. `.github/workflows/ci.yml`; `.github/workflows/coverage.yml`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-010"></a>
### 010. ci: add Conan package caching {#commit-010}

Commit: [6bd93555c0d903dbb731f4362870f63332a5353e](https://github.com/EndstoneMC/endstone/commit/6bd93555c0d903dbb731f4362870f63332a5353e) · committed 2025-01-02T00:15:01Z · author Vincent.

Actual parent: `0cc67df4f8af414147a1627821ebdce9ae769d19`. Full message and parent-relative patch: local source.

Adds whole ~/.conan2 caches keyed by runner OS and conanfile hash, with increasingly broad fallback keys; speeds are an intended benefit, not measured evidence.

Changed-file coverage: 2 paths. `.github/workflows/ci.yml`; `.github/workflows/coverage.yml`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-011"></a>
### 011. chore: update cibuildwheel config {#commit-011}

Commit: [175e6572ed9468520064cf6099ea0c58422488a9](https://github.com/EndstoneMC/endstone/commit/175e6572ed9468520064cf6099ea0c58422488a9) · committed 2025-01-02T00:16:39Z · author Vincent.

Actual parent: `6bd93555c0d903dbb731f4362870f63332a5353e`. Full message and parent-relative patch: local source.

Makes cibuildwheel's CC/CXX point at unversioned clang alternatives installed in before-all rather than interpolated versioned paths. Host environment and container configuration remain distinct.

Changed-file coverage: 1 paths. `pyproject.toml`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-012"></a>
### 012. ci: improve conan cache strategy {#commit-012}

Commit: [f4cb5564d3fbe4f3a8cefd69f94fb7bf3105dcd9](https://github.com/EndstoneMC/endstone/commit/f4cb5564d3fbe4f3a8cefd69f94fb7bf3105dcd9) · committed 2025-01-02T12:35:09Z · author Vincent.

Actual parent: `175e6572ed9468520064cf6099ea0c58422488a9`. Full message and parent-relative patch: local source.

Adds matrix build_type to Conan cache keys for CI and coverage, dropping unused cache step ID/env. Broad fallback keys still permit cache restoration across build types; Conan's own package identities must distinguish artifacts.

Changed-file coverage: 2 paths. `.github/workflows/ci.yml`; `.github/workflows/coverage.yml`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-013"></a>
### 013. feat: add Sentry when ENDSTONE_ENABLE_SENTRY is set {#commit-013}

Commit: [d8e3f061f2f9011a412f1f537786770f489422b8](https://github.com/EndstoneMC/endstone/commit/d8e3f061f2f9011a412f1f537786770f489422b8) · committed 2025-01-02T13:21:34Z · author Vincent.

Actual parent: `f4cb5564d3fbe4f3a8cefd69f94fb7bf3105dcd9`. Full message and parent-relative patch: local source.

Links runtime against sentry only when ENDSTONE_ENABLE_SENTRY; moves libelf lookup into UNIX branch. This is build wiring without new crash behavior.

Changed-file coverage: 1 paths. `src/endstone_runtime/CMakeLists.txt`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-018"></a>
### 018. ci: use conan cache when building wheels {#commit-018}

Commit: [5bb1a09351bd83f38a486a3f7ab34c2fa50a562d](https://github.com/EndstoneMC/endstone/commit/5bb1a09351bd83f38a486a3f7ab34c2fa50a562d) · committed 2025-01-03T19:15:33Z · author Vincent.

Actual parent: `376972566098080a725b9412e3d77d1b1118b364`. Full message and parent-relative patch: local source.

Extends Conan cache to wheel workflow using matrix.build_type, later replaced by literal RelWithDebInfo in20. Source changes alone cannot show useful cache hits.

Changed-file coverage: 1 paths. `.github/workflows/wheel.yml`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-020"></a>
### 020. ci: use conan cache when building portable windows build {#commit-020}

Commit: [8eb9ab80005b5ccf2a638dae1f728e2794747e38](https://github.com/EndstoneMC/endstone/commit/8eb9ab80005b5ccf2a638dae1f728e2794747e38) · committed 2025-01-03T21:01:48Z · author Vincent.

Actual parent: `d947c16f5265eb1cff760108ea21e7df9828336f`. Full message and parent-relative patch: local source.

Uses literal RelWithDebInfo for wheel cache keys and adds the same cache to portable Windows builds, aligning actual build intent instead of relying on absent matrix dimensions.

Changed-file coverage: 2 paths. `.github/workflows/wheel.yml`; `.github/workflows/windows-portable.yml`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-021"></a>
### 021. chore: reduce the size of the bundled crashpad_handler {#commit-021}

Commit: [2c2b391142066b0a12ab13815e509fb587b1cd5e](https://github.com/EndstoneMC/endstone/commit/2c2b391142066b0a12ab13815e509fb587b1cd5e) · committed 2025-01-04T00:52:39Z · author Vincent.

Actual parent: `8eb9ab80005b5ccf2a638dae1f728e2794747e38`. Full message and parent-relative patch: local source.

Copies Crashpad helper into the build tree before optional stripping, then packages that copy. Dependencies order copy after runtime and strip after copy; dependency-cache contents are not directly modified. Size reduction is stated intent, with no byte measurement.

Changed-file coverage: 1 paths. `src/endstone_runtime/CMakeLists.txt`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-022"></a>
### 022. feat: separate debug symbols from files post-build {#commit-022}

Commit: [2b93464d80fc20a8963149bb5a5e94277c206a6a](https://github.com/EndstoneMC/endstone/commit/2b93464d80fc20a8963149bb5a5e94277c206a6a) · committed 2025-01-04T13:54:34Z · author Vincent.

Actual parent: `2c2b391142066b0a12ab13815e509fb587b1cd5e`. Full message and parent-relative patch: local source.

Introduces post-build objcopy debug separation, stripping and GNU debuglink for Python/runtime on UNIX, installs .dbg and MSVC PDB artifacts, and packages loader. Runtime wheel install becomes RUNTIME-only here, which is corrected for Linux in26. This stage is reversed in24 before reintroduction as an option later.

Changed-file coverage: 2 paths. `src/endstone_python/CMakeLists.txt`; `src/endstone_runtime/CMakeLists.txt`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-023"></a>
### 023. ci: add custom scripts to upload symbols before repairing wheels {#commit-023}

Commit: [812c0df39a95a0bff31669329eaff022a0352c11](https://github.com/EndstoneMC/endstone/commit/812c0df39a95a0bff31669329eaff022a0352c11) · committed 2025-01-04T15:31:02Z · author Vincent.

Actual parent: `2b93464d80fc20a8963149bb5a5e94277c206a6a`. Full message and parent-relative patch: local source.

Adds wheel repair script to unpack wheels, upload debug files plus sources with sentry-cli, optionally remove .pdb/.dbg, then invoke auditwheel for Linux or repack Windows. Streams subprocess output and raises on nonzero status. Validates project/org/input/destination. CI passes token into containers; absent token still attempts upload until later132. Failure logging joins command args and can expose an explicitly supplied token, an observed diagnostic risk rather than evidence of a real leak. No secret value was read or executed.

Changed-file coverage: 4 paths. `.github/workflows/wheel.yml`; `conanfile.py`; `pyproject.toml`; `scripts/repair_wheel.py`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-024"></a>
### 024. ci: temporarily disable separating debug info from files {#commit-024}

Commit: [287c1ed1def343f09f714b225fe2c852078763e5](https://github.com/EndstoneMC/endstone/commit/287c1ed1def343f09f714b225fe2c852078763e5) · committed 2025-01-04T19:00:52Z · author Vincent.

Actual parent: `812c0df39a95a0bff31669329eaff022a0352c11`. Full message and parent-relative patch: local source.

Comments out UNIX debug extraction/install blocks while retaining Windows PDB installation. Subject explicitly calls it temporary; no reason beyond disabling the feature is given. Preserve this reversal in any advice about symbol packaging.

Changed-file coverage: 2 paths. `src/endstone_python/CMakeLists.txt`; `src/endstone_runtime/CMakeLists.txt`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-026"></a>
### 026. fix: endstone_runtime target on Linux platform {#commit-026}

Commit: [f9f0b6bfc5b82eee302479fa7a1c649de08498c8](https://github.com/EndstoneMC/endstone/commit/f9f0b6bfc5b82eee302479fa7a1c649de08498c8) · committed 2025-01-04T23:09:44Z · author Vincent.

Actual parent: `2aa3674861251bedddbf0c3f204cd0e417f50aca`. Full message and parent-relative patch: local source.

Repairs wheel install categories: Windows runtime/loader/PDB remain RUNTIME; UNIX shared runtime uses LIBRARY. Crashpad directory remains packaged; disabled .dbg handling stays disabled. Explicit platform-specific packaging correction follows22's regression.

Changed-file coverage: 1 paths. `src/endstone_runtime/CMakeLists.txt`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-052"></a>
### 052. refactor: remove unused conan recipes {#commit-052}

Commit: [ff3040a9bd24c26479a2f7255b5a6c6092a6c314](https://github.com/EndstoneMC/endstone/commit/ff3040a9bd24c26479a2f7255b5a6c6092a6c314) · committed 2025-01-06T16:18:29Z · author Vincent.

Actual parent: `e1a62bb226534265e82c278e8382017af15946e5`. Full message and parent-relative patch: local source.

Removes explicitly unused Conan funchook recipes and fixtures, not runtime hooking: parent active FetchContent still pins kubo/funchook v1.1.3 and disables its tests. Fifteen deleted blobs exactly match prior substantively read histories; unmatched27-line test_package/conanfile.py fully read. Existing upstream fixture attribution retained. Deletion reuse identities in052-deletion-reuse.json.

Changed-file coverage: 16 paths. `third_party/.gitignore`; `third_party/funchook/conandata.yml`; `third_party/funchook/conanfile.py`; `third_party/funchook/patches/1.1.3-0001-cmake-use-cci-capstone.patch`; `third_party/funchook/test_package/CMakeLists.txt`; `third_party/funchook/test_package/conanfile.py`; `third_party/funchook/test_package/libfunchook_test.c`; `third_party/funchook/test_package/libfunchook_test_aarch64_gas.S`; `third_party/funchook/test_package/libfunchook_test_noasm.c`; `third_party/funchook/test_package/libfunchook_test_x86_64_gas.S`; `third_party/funchook/test_package/libfunchook_test_x86_64_masm.asm`; `third_party/funchook/test_package/libfunchook_test_x86_gas.S`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.

Deleted source reuse is supported by exact prior-read blob identities in deletion audit; the one unmatched recipe was read in full.


<a id="commit-054"></a>
### 054. refactor: move python package to project root {#commit-054}

Commit: [2d567b6642f70ed016396d9cb586cd4d2bb97e65](https://github.com/EndstoneMC/endstone/commit/2d567b6642f70ed016396d9cb586cd4d2bb97e65) · committed 2025-01-06T16:31:14Z · author Vincent.

Actual parent: `94c95ed4e47dbcded562e81b4e33be4b99894d47`. Full message and parent-relative patch: local source.

Moves Python package from python/src/endstone to root/endstone:32 exact blobs including binary assets, plus4-line .gitignore deletion fully read.55 replaces generated-version ignore. No Python behavior change from identical paths.

Changed-file coverage: 33 paths. `python/src/endstone/__init__.py → endstone/__init__.py`; `python/src/endstone/__main__.py → endstone/__main__.py`; `python/src/endstone/_internal/__init__.py → endstone/_internal/__init__.py`; `python/src/endstone/_internal/bootstrap/__init__.py → endstone/_internal/bootstrap/__init__.py`; `python/src/endstone/_internal/bootstrap/base.py → endstone/_internal/bootstrap/base.py`; `python/src/endstone/_internal/bootstrap/linux.py → endstone/_internal/bootstrap/linux.py`; `python/src/endstone/_internal/bootstrap/windows.py → endstone/_internal/bootstrap/windows.py`; `python/src/endstone/_internal/endstone_python.pyi → endstone/_internal/endstone_python.pyi`; `python/src/endstone/_internal/fonts/JetBrainsMono-Regular.ttf → endstone/_internal/fonts/JetBrainsMono-Regular.ttf`; `python/src/endstone/_internal/metrics.py → endstone/_internal/metrics.py`; `python/src/endstone/_internal/plugin_loader.py → endstone/_internal/plugin_loader.py`; `python/src/endstone/_internal/symbols.toml → endstone/_internal/symbols.toml`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.




<a id="commit-055"></a>
### 055. refactor: build target `endstone::python` {#commit-055}

Commit: [28b1b20117c2601777f40a0cf59533e63b411151](https://github.com/EndstoneMC/endstone/commit/28b1b20117c2601777f40a0cf59533e63b411151) · committed 2025-01-06T17:35:39Z · author Vincent.

Actual parent: `2d567b6642f70ed016396d9cb586cd4d2bb97e65`. Full message and parent-relative patch: local source.

Staged target build: public endstone::endstone interface with fmt/expected find-or-fetch; new umbrella endstone.hpp, version/variant headers, and public plugin builders moved into plugin.h (sort/dedupe dependencies, lowercase names). MSVC debug iterator guard explicitly protects ABI against release BDS. Linux libc++/PIC forced; C++20 centralized. Python packaging moved root; build returns after Python, intentionally leaving core/runtime/tests unreachable at this stage. Test/devtool CMake extracted with paths not yet fixed. Full38-file residual read.

Changed-file coverage: 38 paths. `.gitignore`; `CMakeLists.txt`; `include/CMakeLists.txt`; `include/endstone/block/block.h`; `include/endstone/block/block_data.h`; `include/endstone/block/block_state.h`; `include/endstone/endstone.hpp`; `include/endstone/inventory/item_stack.h`; `include/endstone/plugin/plugin.h`; `include/endstone/plugin/plugin_description.h`; `include/endstone/variant.h`; `include/endstone/version.h`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.




<a id="commit-059"></a>
### 059. refactor: build target `endstone::devtools` {#commit-059}

Commit: [e51df0e12a763dde465292a18f7ec7170cec54e9](https://github.com/EndstoneMC/endstone/commit/e51df0e12a763dde465292a18f7ec7170cec54e9) · committed 2025-01-06T21:07:21Z · author Vincent.

Actual parent: `8c7dae14916dce213404ae36df433bca06c7d0ce`. Full message and parent-relative patch: local source.

Enables devtools target, removes root return but leaves runtime/tests commented. Fixes UI source paths/includes and public Bedrock include propagation; devtools namespace no longer core. NewType default constructor and nlohmann serializer added. Vanilla data scheduler retains server-thread transfer. Seven exact moves,11 residuals read.

Changed-file coverage: 18 paths. `CMakeLists.txt`; `src/bedrock/CMakeLists.txt`; `src/bedrock/util/new_type.h`; `src/endstone/core/json.h`; `src/endstone/devtools/CMakeLists.txt`; `src/endstone/devtools/devtools.cpp`; `src/endstone/devtools/devtools.h`; `src/endstone/devtools/devtools_command.cpp`; `src/endstone/devtools/imgui/imgui_file_browser.h → src/endstone/devtools/imgui_file_browser.h`; `src/endstone/devtools/imgui/imgui_impl_glfw.cpp → src/endstone/devtools/imgui_impl_glfw.cpp`; `src/endstone/devtools/imgui/imgui_impl_glfw.h → src/endstone/devtools/imgui_impl_glfw.h`; `src/endstone/devtools/imgui/imgui_impl_opengl3.cpp → src/endstone/devtools/imgui_impl_opengl3.cpp`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.




<a id="commit-060"></a>
### 060. refactor: build target `endstone::test` {#commit-060}

Commit: [335687277d563f48baee4ee7386be4ce32d8ad9d](https://github.com/EndstoneMC/endstone/commit/335687277d563f48baee4ee7386be4ce32d8ad9d) · committed 2025-01-06T21:24:01Z · author Vincent.

Actual parent: `e51df0e12a763dde465292a18f7ec7170cec54e9`. Full message and parent-relative patch: local source.

Builds explicit test executable/plugin against new target names; reinstates top-level enable_testing/GTest/coverage and fixed plugin filenames. Crucially drops gtest_discover_tests here (restoration outside first 100; successor worker reports118), so building executable alone is not discovery evidence. Moves/namespace rewrites audited. Runtime removes obsolete moved sources; duplicate hook_error header transiently added, removed61. Adds plugin export macro. No tests run.

Changed-file coverage: 16 paths. `CMakeLists.txt`; `include/endstone/plugin/plugin.h`; `src/endstone/runtime/CMakeLists.txt`; `src/endstone/runtime/hook_error.h`; `tests/CMakeLists.txt`; `tests/endstone/core/test_base64.cpp`; `tests/endstone/core/command/test_command_lexer.cpp → tests/endstone/core/test_command_lexer.cpp`; `tests/endstone/core/command/test_command_usage_parser.cpp → tests/endstone/core/test_command_usage_parser.cpp`; `tests/endstone/core/plugin/test_cpp_plugin_loader.cpp → tests/endstone/core/test_cpp_plugin_loader.cpp`; `tests/endstone/core/test_logger_factory.cpp`; `tests/endstone/core/ban/test_player_ban_list.cpp → tests/endstone/core/test_player_ban_list.cpp`; `tests/endstone/core/plugin/test_plugin.cpp → tests/endstone/core/test_plugin.cpp`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.




<a id="commit-065"></a>
### 065. fix: build on Windows {#commit-065}

Commit: [cd1da494b30c7b57934493a500629ba771d174d1](https://github.com/EndstoneMC/endstone/commit/cd1da494b30c7b57934493a500629ba771d174d1) · committed 2025-01-07T16:49:44Z · author Vincent.

Actual parent: `86e79dc1e58d55f129c70d6f64bd627d0d71ec82`. Full message and parent-relative patch: local source.

Windows build repairs: generator returns failures and skips zero offsets, but array size remains input table.size (trailing zero-initialized entries if skipped). Adds native symbols for BlockLegacy and ItemRegistryManager, removes obsolete Explosion/ItemStack ctor/ToString entries. Removes duplicate MinecraftCommands compile body, updates runtime sources/includes/platform namespace, deletes obsolete70-entry include. Linux include/name inconsistencies still pending. Title states Windows build fix; no CI result inferred.

Changed-file coverage: 10 paths. `src/bedrock/symbol_generator/main.cpp`; `src/bedrock/symbol_generator/symbols.toml`; `src/endstone/core/hooks/minecraft_commands.cpp`; `src/endstone/core/platform_linux.cpp`; `src/endstone/core/platform_windows.cpp`; `src/endstone/runtime/CMakeLists.txt`; `src/endstone/runtime/hook.cpp`; `src/endstone/runtime/linux/hook.cpp → src/endstone/runtime/linux.cpp`; `src/endstone/runtime/windows/hook.cpp → src/endstone/runtime/windows.cpp`; `src/endstone/runtime/windows/symbols.inc`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.




<a id="commit-068"></a>
### 068. refactor: merge `endstone::devtools` into `endstone::core` {#commit-068}

Commit: [32f570321aef1426283b065ae305f78ffd136883](https://github.com/EndstoneMC/endstone/commit/32f570321aef1426283b065ae305f78ffd136883) · committed 2025-01-07T22:54:03Z · author Vincent.

Actual parent: `3f9ff1b6fc6a9a908f24cba37ae1f0c1d3d91d46`. Full message and parent-relative patch: local source.

Devtools becomes optional subtarget of core, source paths reunited; core links devtools privately and devtools core publicly (static cycle needing build system support). Removes redundant dependency links inherited from Bedrock and old standalone devtools install.9 exact moves17 residuals. Runtime still launches detached devtools renderer. No GUI/runtime validation.

Changed-file coverage: 26 paths. `CMakeLists.txt`; `src/endstone/core/CMakeLists.txt`; `src/endstone/core/block/block_state.h`; `src/endstone/core/command/command_map.cpp`; `src/endstone/devtools/CMakeLists.txt → src/endstone/core/devtools/CMakeLists.txt`; `src/endstone/devtools/devtools.cpp → src/endstone/core/devtools/devtools.cpp`; `src/endstone/devtools/devtools.h → src/endstone/core/devtools/devtools.h`; `src/endstone/devtools/devtools_command.cpp → src/endstone/core/devtools/devtools_command.cpp`; `src/endstone/devtools/devtools_command.h → src/endstone/core/devtools/devtools_command.h`; `src/endstone/devtools/imgui_file_browser.h → src/endstone/core/devtools/imgui_file_browser.h`; `src/endstone/devtools/imgui_impl_glfw.cpp → src/endstone/core/devtools/imgui_impl_glfw.cpp`; `src/endstone/devtools/imgui_impl_glfw.h → src/endstone/core/devtools/imgui_impl_glfw.h`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.




<a id="commit-078"></a>
### 078. chore: add CMake option to separate debug info into .dbg files on Linux {#commit-078}

Commit: [7689c6c1c450e0b42936c772ec345cf19ecbe1dd](https://github.com/EndstoneMC/endstone/commit/7689c6c1c450e0b42936c772ec345cf19ecbe1dd) · committed 2025-01-09T01:45:11Z · author Vincent.

Actual parent: `de8bdd0f34cdea984f581cff12ad786a9160814b`. Full message and parent-relative patch: local source.

Adds default-OFF ENDSTONE_SEPARATE_DEBUG_INFO; conditionally objcopy keep-debug/strip/add-debuglink and install .dbg for Python+runtime on UNIX. Restores formerly commented tooling behind opt-in; wheel repair uploads/strip separately. No artifacts produced or association validated.

Changed-file coverage: 3 paths. `CMakeLists.txt`; `src/endstone/python/CMakeLists.txt`; `src/endstone/runtime/CMakeLists.txt`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-085"></a>
### 085.  fix: linux build {#commit-085}

Commit: [554d8564db4548fb885c76affac9ef4b31169f7c](https://github.com/EndstoneMC/endstone/commit/554d8564db4548fb885c76affac9ef4b31169f7c) · committed 2025-01-09T18:02:34Z · author Vincent.

Actual parent: `1bc2bda8a8778e0f979c314f171d2532976588f9`. Full message and parent-relative patch: local source.

Linux build repairs add -fms-extensions and netdb.h and remove non-constexpr fmt formatting from missing-symbol consteval branch. Syncs Linux native symbols; replaces local ItemStackBase setUserData/charged-item reconstruction with BEDROCK_CALL, removes ItemInstance::fromTag. Adds Explosion constructor declaration. Fixes platform header path but Linux still defines get_name instead of declared get_platform at 100. No build executed.

Changed-file coverage: 10 paths. `src/bedrock/CMakeLists.txt`; `src/bedrock/deps/raknet/socket_includes.h`; `src/bedrock/symbol.h`; `src/bedrock/symbol_generator/symbols.toml`; `src/bedrock/world/item/item_instance.cpp`; `src/bedrock/world/item/item_instance.h`; `src/bedrock/world/item/item_stack_base.cpp`; `src/bedrock/world/level/explosion.h`; `src/endstone/core/platform_linux.cpp`; `src/endstone/runtime/hook.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-088"></a>
### 088. chore: change action runner os version {#commit-088}

Commit: [f0a0aa42ff77a19272188f4c869703b68c13c96a](https://github.com/EndstoneMC/endstone/commit/f0a0aa42ff77a19272188f4c869703b68c13c96a) · committed 2025-01-09T18:20:56Z · author Vincent.

Actual parent: `4a7c9627c2cc8b40911025dcc44a8a1f606d13d8`. Full message and parent-relative patch: local source.

CI matrix removes Debug temporarily and chooses ubuntu20.04; wheel runner ubuntu-latest. Follows MSVC debug-iterator ABI guard; explicit rationale in this commit absent.89 re-adds Linux Debug only. No CI outcomes read.

Changed-file coverage: 2 paths. `.github/workflows/ci.yml`; `.github/workflows/wheel.yml`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-089"></a>
### 089. ci: update workflows and Dockerfile for cache and testing paths {#commit-089}

Commit: [5b7d3f375067170cf7d4c523be384058c40ace1e](https://github.com/EndstoneMC/endstone/commit/5b7d3f375067170cf7d4c523be384058c40ace1e) · committed 2025-01-09T19:23:36Z · author Vincent.

Actual parent: `f0a0aa42ff77a19272188f4c869703b68c13c96a`. Full message and parent-relative patch: local source.

Restores Debug only for Linux, narrows Conan cache to package directory, fixes coverage cache literal Debug where matrix field unavailable, and updates Docker pytest path after54 package migration. Does not restore gtest_discover_tests removed60. Cache/build config are not validation outcomes.

Changed-file coverage: 5 paths. `.github/workflows/ci.yml`; `.github/workflows/coverage.yml`; `.github/workflows/wheel.yml`; `.github/workflows/windows-portable.yml`; `Dockerfile`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-090"></a>
### 090. fix: split multiline log messages before logging {#commit-090}

Commit: [55b70f7c8be79a406be1275778d592de7895e977](https://github.com/EndstoneMC/endstone/commit/55b70f7c8be79a406be1275778d592de7895e977) · committed 2025-01-09T20:08:35Z · author Vincent.

Actual parent: `5b7d3f375067170cf7d4c523be384058c40ace1e`. Full message and parent-relative patch: local source.

Splits all adapter log messages on newline with C++20 ranges; native log bridge also uses string_view split instead of manual trimming/substrings. Trailing whitespace is no longer trimmed; empty-line behavior follows split implementation. Logging retains severity checking but no newline test added. Source buffer lifetime covers synchronous calls; async sink semantics not audited.

Changed-file coverage: 2 paths. `src/endstone/core/spdlog/spdlog_adapter.cpp`; `src/endstone/runtime/bedrock_hooks/bedrock_event_logger.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-091"></a>
### 091. ci: allow conan cache in cibuildwheel containers {#commit-091}

Commit: [bb74bbbd2ee14538289377e517152c58cd461e09](https://github.com/EndstoneMC/endstone/commit/bb74bbbd2ee14538289377e517152c58cd461e09) · committed 2025-01-09T20:53:41Z · author Vincent.

Actual parent: `55b70f7c8be79a406be1275778d592de7895e977`. Full message and parent-relative patch: local source.

Exposes Linux host Conan cache inside cibuildwheel via CONAN_HOME=/host${HOME}/.conan2 and environment pass-through. Existing Sentry token pass retained; no credentials copied/read or workflows run. Bounded packaging/cache change.

Changed-file coverage: 1 paths. `.github/workflows/wheel.yml`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-096"></a>
### 096. chore: update Python version for the portable build {#commit-096}

Commit: [90b65613f83b3d2ae0be35971840140b642d4229](https://github.com/EndstoneMC/endstone/commit/90b65613f83b3d2ae0be35971840140b642d4229) · committed 2025-01-11T19:52:16Z · author Vincent.

Actual parent: `5bebb3731039fee0bed4b84648b209ea92fa2035`. Full message and parent-relative patch: local source.

Portable build pins WinPython3.12.8 instead3.12.3, replaces URL/hash/extraction path together. Digest statically retained; binary not downloaded/executed and compatibility unproven.

Changed-file coverage: 1 paths. `.github/workflows/windows-portable.yml`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.
