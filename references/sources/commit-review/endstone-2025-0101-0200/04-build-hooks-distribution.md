<!-- retrieval: {"source_ids":["public:commit:06a9c696befb10f8bac98c1b4184bbec778335cb","public:commit:169fbf3bc23346d63aa8b7c81fe0191ac6135454","public:commit:1c1823702715a0eed880204960e56cca89c9c833","public:commit:1cd59c15aab3f05a5381878dbab5ad7646cd1af7","public:commit:1d8d08a5d5691b8521a16e96a4b23147db0ff25c","public:commit:2ac4db97db8f849957659a29a069548b90af7d25","public:commit:318603cd3a823420120dc0a8f321915fa090778c","public:commit:325f532ec252415f17bc7d05d88dbb394b856de6","public:commit:3c7f46266cf713f38ba332ca09b9e773d3ccfc76","public:commit:3e39abf21a4e3afc558ebe8fbf967d983b863b59","public:commit:53f6182ab2f219ac67fbc1dd4e79bf31045af94c","public:commit:6d40025233a2e23747fc1dfa0658ce7a38669fc9","public:commit:7636ebebb024ac54a7f21957a8e3925a76a60905","public:commit:77e3175e46e495e03f892078f383bea916159802","public:commit:792c20ec588d1790902b14569c0d0e2627beb23e","public:commit:7fa3c53c63e47583d70ea1305a91007948783099","public:commit:961e4d59bb93fc07ef943e3fd9e0d61cd5f37ae4","public:commit:98e80cb9e95d8ebd7034f5cc19471ef550d2777a","public:commit:98fe4a33882f6ac32e53b47f97a5ef3dd60f8dde","public:commit:be3830ca4081df50179edf47104837deaf581ad0","public:commit:c2761d53737278a03fe9afc9ef36d503b4a9fdff","public:commit:c571a5d8b2cacf22afcd73d166793109908c3a81","public:commit:cd2725882f18714a0ea332bd8c86e1e6b623b949","public:commit:cd8b2d05eb27e3460d7dcbd75f9bf0ee5a6b5087","public:commit:e0640f6f10ab04b842ae83ccd890a1034b6bef5a","public:commit:e22666aace03832e0efc0478efcd214c142bc943","public:commit:e464dba535d27102ae3c0a65085efa39b2902056","public:commit:e4cac590b176af41369d2a2b000601570c63de54","public:commit:ee9c9082b4a96fc20cb6dd1ac9bcc8ac5ab7cded","public:commit:ef1f0e4dcd4749d9c730c2a0bfb8aa48d1217d43","public:commit:f5786bea7dda6bad8c556a40d3a4c9c4553041b3","public:thread:EndstoneMC/endstone:124"],"source_type":"public","date":"2025-01-12..2025-01-15","topics":["lifetime","concurrency","ffi","testing","build","performance","api","diagnosis","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Build, hook lookup and distribution integration {#build-hook-lookup-and-distribution-integration}

<a id="follow-the-artifact-not-only-the-build-command"></a>
## Follow the artifact, not only the build command {#follow-the-artifact-not-only-the-build-command}

This slice repairs the first100 source-layout/build migration across docs triggers117, CTest discovery118, platform includes102 and eventually Linux symbol naming185 (event/lifecycle dossier). Kaniteru's PR124 supplies include(FetchContent) for the standalone include project. The exact imported commit is ed5b7f9b4ca9cb1f97ef92ca3f7234c05df7157e;105 merges it while the other parent carries Vincent's sound scaffolding and version bump. Both parent deltas, merge base and imported source are verified. The merge's first-parent delta exactly equals the imported patch. Vincent's thank-you is acknowledgement, not authorship of Kaniteru's fix or a test result.

123 sets installation permissions so crashpad's packaged helper can execute, but applies executable permissions throughout the copied directory.132 makes Sentry symbol upload conditional on an available token; it does not mean symbol stripping is disabled.139 turns Conan into dependency/toolchain provisioning and moves project build/test responsibility into CMake/scikit-build and CI. This shifts version authority too:141 uses the full wheel/backend version with a header fallback.140 keeps release optimization with debug information, and148 replaces pybind11_add_module with explicit module/extension/visibility/LTO/platform pieces to avoid implicit stripping. Removing the helper's automation means the replacement must preserve every required platform behavior, not only the one unwanted strip step.

Docker133 switches from cloning a possibly different source to building the current context.134–138 adjust registry matrices, login permissions, build cache and exact wheel installation;136 restores missing packages:write, and138 installs the concrete discovered wheel rather than trusting package-name resolution.142 places dependency-only Conan setup before the source copy to improve cache reuse and restores native-specific flags.143 removes obsolete cache-dance machinery;144 splits release cache naming while retaining broader fallback. Cache keys and source-context provenance matter to reproducibility, but no cache-hit, upload or wheel-install results were observed.

CI146 initially points at an incorrect build directory;147 repairs it and Ninja selection;148 temporarily removes Ninja during module build changes;149 restores it. These small follow-ups are evidence of integration iteration, not independent deep preferences.150 passes funchook's options as cache booleans, disables its install and removes forced Capstone selection. Dependency bumps127 and compiler validation relaxation197 are source policy changes, not independent audits of external packages or proof of compiler ABI support.

## Hook original-function lookup {#hook-original-function-lookup}

124 moves the original-function map to a function-local static and stops treating string-view data as guaranteed null-terminated strings; the title reports a UB/crash fix without isolating a reproducer.125 caches original lookups per compile-time hash, avoiding repeated map lookup.126 changes the cache to a pointer to the map's value so later updates remain observable. This assumes the map element remains alive and first-use/reentrant access is safe. A mutable lazy assignment is not automatically synchronized merely because the containing pointer has static storage. There is no benchmark or race reproducer in this slice, so use this as a mechanism and review checklist, not a speed claim.

## Apply to a new task {#apply-to-a-new-task}

Trace source provenance through context, dependency resolution, build tree, wheel file, symbol upload/strip, helper permissions and final install. Separately establish test registration and actual test execution. For replacing build helpers, enumerate the flags/visibility/naming behavior they previously supplied. For hook caching, state ownership, initialization timing, mutation visibility and concurrency assumptions. All100 assigned patches were statically reviewed; no CMake/Conan/build/CI/native test was executed.


## Per-commit evidence {#per-commit-evidence}

<a id="commit-102"></a>
### Commit 102 {#commit-102}

325f532ec252415f17bc7d05d88dbb394b856de6 · 2025-01-12T00:13:25Z

[ fix: compilation errors on Linux](https://github.com/EndstoneMC/endstone/commit/325f532ec252415f17bc7d05d88dbb394b856de6)

**Observed change.** Adds explicit complete-type/includes needed on Linux and public BlockLegacy update constants; rewrites seven expected.and_then block operations into explicit success/error propagation, preserving invalid-state errors and block update flags.

**Causal interpretation.** Compiler portability can require removing convenience monadic syntax without changing error behavior. Block writes still distinguish physics (neighbors+clients) from clients-only.

**Limits.** Compilation success is title-reported, not run. No regression tests supplied.

<a id="commit-104"></a>
### Commit 104 {#commit-104}

e22666aace03832e0efc0478efcd214c142bc943 · 2025-01-12T13:44:39Z

[chore: bump version to v0.6.0](https://github.com/EndstoneMC/endstone/commit/e22666aace03832e0efc0478efcd214c142bc943)

**Observed change.** Version macros change0.5.7→0.6.0, therefore API_VERSION0.5→0.6.

**Causal interpretation.** Mechanical release marker, not a standalone engineering preference.

**Limits.** No release or runtime outcome inferred.

<a id="commit-105"></a>
### Commit 105 {#commit-105}

cd2725882f18714a0ea332bd8c86e1e6b623b949 · 2025-01-12T13:45:10Z

[Merge remote-tracking branch 'origin/main'](https://github.com/EndstoneMC/endstone/commit/cd2725882f18714a0ea332bd8c86e1e6b623b949)

**Observed change.** Two-parent merge imports include(FetchContent) in include/CMakeLists.txt. Second-parent imported commit ed5b7f9b4ca9cb1f97ef92ca3f7234c05df7157e is Kaniteru's PR124 fix. Second-parent diff contains Vincent103–104 sound scaffolding and version bump only; base is325f532ec252415f17bc7d05d88dbb394b856de6.

**Causal interpretation.** Standalone include project must load FetchContent before fallback dependency declarations. Integration credit belongs to Vincent; imported implementation credit belongs to Kaniteru.

**Limits.** Both parent diffs and branch history read; no conflict-resolution-specific changes observed. Captured PR124 has no description, one thank-you comment from Vincent and no reviews. No build run; merge integration is not authorship of Kaniteru's patch.

<a id="commit-117"></a>
### Commit 117 {#commit-117}

792c20ec588d1790902b14569c0d0e2627beb23e · 2025-01-12T20:09:59Z

[ci: fix workflow paths for docs](https://github.com/EndstoneMC/endstone/commit/792c20ec588d1790902b14569c0d0e2627beb23e)

**Observed change.** Docs workflow path filter python/**→endstone/** after source-layout migration.

**Causal interpretation.** Mechanical downstream CI repair; source relocation must include workflow trigger dependencies.

**Limits.** No workflow run verified.

<a id="commit-118"></a>
### Commit 118 {#commit-118}

1cd59c15aab3f05a5381878dbab5ad7646cd1af7 · 2025-01-12T20:17:18Z

[fix: add the missing `gtest_discover_tests`](https://github.com/EndstoneMC/endstone/commit/1cd59c15aab3f05a5381878dbab5ad7646cd1af7)

**Observed change.** Adds gtest_discover_tests(endstone_test) after test target/link configuration.

**Causal interpretation.** Building a test executable does not register its cases with CTest; discovery is a separate integration step.

**Limits.** No tests executed or count asserted.

<a id="commit-123"></a>
### Commit 123 {#commit-123}

1c1823702715a0eed880204960e56cca89c9c833 · 2025-01-14T18:20:06Z

[ fix: make crash_handler executable by setting the right permissions](https://github.com/EndstoneMC/endstone/commit/1c1823702715a0eed880204960e56cca89c9c833)

**Observed change.** CMake crashpad-directory installation now sets owner rwx/group rx/world rx file permissions.

**Causal interpretation.** Bundling a helper executable needs executable bits retained through packaging; code explicitly addresses deployment artifact permissions.

**Limits.** Mode applies all files in copied directory, not solely handler. No wheel permissions or process launch tested.

<a id="commit-124"></a>
### Commit 124 {#commit-124}

7636ebebb024ac54a7f21957a8e3925a76a60905 · 2025-01-14T18:20:40Z

[ fix: prevent a crash due to an undefined behaviour](https://github.com/EndstoneMC/endstone/commit/7636ebebb024ac54a7f21957a8e3925a76a60905)

**Observed change.** Replaces namespace-global original-function map with function-local static accessor; symbol keys now passed as strings rather than key.data(), and hash insertion uses explicit value(name.c_str()).

**Causal interpretation.** Mitigates initialization-order/lifetime assumptions and string-view null-termination misuse, but commit title alone does not isolate which caused reported undefined-behavior crash.

**Limits.** No reproducer, stack trace or runtime verification supplied.

<a id="commit-125"></a>
### Commit 125 {#commit-125}

98fe4a33882f6ac32e53b47f97a5ef3dd60f8dde · 2025-01-14T18:37:48Z

[feat: add caching for `endstone::hook::get_original`](https://github.com/EndstoneMC/endstone/commit/98fe4a33882f6ac32e53b47f97a5ef3dd60f8dde)

**Observed change.** Moves hook helpers/platform symbol enumeration under details and adds hash-template original lookup cache; wrapper macro performs one map lookup then reuses cached pointer.

**Causal interpretation.** Avoids repeated hash lookup on detour calls while retaining compile-time symbol hash. Install still creates/prepares/installs each funchook and inserts original afterwards.

**Limits.** No speed measurement. Mutable lazy-cache assignment after static null initialization is not itself synchronized; no concurrent-first-use or hook-reentrancy test.

<a id="commit-126"></a>
### Commit 126 {#commit-126}

98e80cb9e95d8ebd7034f5cc19471ef550d2777a · 2025-01-14T18:43:32Z

[refactor: adjust `get_original` to use a pointer-to-pointer approach](https://github.com/EndstoneMC/endstone/commit/98e80cb9e95d8ebd7034f5cc19471ef550d2777a)

**Observed change.** Changes original lookup to void*& and per-symbol cache to pointer-to-map-value, returning current *original instead of frozen copy.

**Causal interpretation.** Allows cached callers to observe changes to stored original pointer while avoiding map lookup. Depends on map-node lifetime; no erase support is shown.

**Limits.** No concurrency/lifetime tests; cache initialization race consideration from125 remains.

<a id="commit-127"></a>
### Commit 127 {#commit-127}

6d40025233a2e23747fc1dfa0658ce7a38669fc9 · 2025-01-14T20:27:46Z

[chore(deps): update multiple dependencies to their latest versions](https://github.com/EndstoneMC/endstone/commit/6d40025233a2e23747fc1dfa0658ce7a38669fc9)

**Observed change.** Version-only bumps Boost1.85→1.86, cpptrace0.7.1→0.7.5, magic_enum0.9.5→0.9.7, ms-gsl4.0→4.1, pybind2.13.1→2.13.6, sentry0.7.15→0.7.17, imgui1.90.8→1.91.5, gtest1.14→1.15.

**Causal interpretation.** Mechanical dependency maintenance, not proof latest versions fix a specific defect.

**Limits.** No release-note audit or build validation claimed.

<a id="commit-128"></a>
### Commit 128 {#commit-128}

cd8b2d05eb27e3460d7dcbd75f9bf0ee5a6b5087 · 2025-01-14T20:32:56Z

[chore: update conanfile.py](https://github.com/EndstoneMC/endstone/commit/cd8b2d05eb27e3460d7dcbd75f9bf0ee5a6b5087)

**Observed change.** Conan package metadata moves cpptrace/sentry requirements to core; devtools dependencies fold into core and runtime depends only core.

**Causal interpretation.** Aligns recipe component graph with previous layout consolidation. Transient core.requires also contains literal core self-reference; recipe packaging metadata is removed139.

**Limits.** No Conan package graph run.

<a id="commit-131"></a>
### Commit 131 {#commit-131}

7fa3c53c63e47583d70ea1305a91007948783099 · 2025-01-14T21:51:27Z

[chore: fix the build directory for scikit-build](https://github.com/EndstoneMC/endstone/commit/7fa3c53c63e47583d70ea1305a91007948783099)

**Observed change.** Scikit-build build-dir fixed to build/{wheel_tag}.

**Causal interpretation.** Separates build artifacts by wheel ABI tag and enables reuse within compatible tag.

**Limits.** No build performed.

<a id="commit-132"></a>
### Commit 132 {#commit-132}

318603cd3a823420120dc0a8f321915fa090778c · 2025-01-14T21:52:49Z

[feat: skip uploading debug files when no auth token is provided](https://github.com/EndstoneMC/endstone/commit/318603cd3a823420120dc0a8f321915fa090778c)

**Observed change.** Wheel repair uploads debug files/include-sources only when auth token present; optional stripping still runs without upload and messages make branch explicit.

**Causal interpretation.** Developer builds need not fail for absent release credentials, but stripping without successful archival can discard debug artifacts.

**Limits.** No upload made; no token read. No wheel output checked.

<a id="commit-133"></a>
### Commit 133 {#commit-133}

53f6182ab2f219ac67fbc1dd4e79bf31045af94c · 2025-01-14T23:07:08Z

[ci: update docker build pipeline](https://github.com/EndstoneMC/endstone/commit/53f6182ab2f219ac67fbc1dd4e79bf31045af94c)

**Observed change.** Docker builds current checked-out context rather than cloning upstream; ignores CI/dist artifacts, uses CMake3.31.4 and repair_wheel path, installs/tests repaired wheel then copies only wheelhouse to final stage. Removes no-cache flags and destination-dir precheck.

**Causal interpretation.** Build provenance now tracks tested checkout/PR instead of remote branch tip; packaging/repaired wheel is the tested artifact.

**Limits.** pytest command in Dockerfile is a configured test, not evidence of pass. Exact source context still depends dockerignore.

<a id="commit-134"></a>
### Commit 134 {#commit-134}

1d8d08a5d5691b8521a16e96a4b23147db0ff25c · 2025-01-15T00:26:40Z

[ci: update Docker workflow to add caching and secrets](https://github.com/EndstoneMC/endstone/commit/1d8d08a5d5691b8521a16e96a4b23147db0ff25c)

**Observed change.** Combines registries into matrix, adds local Buildx layer cache and token secret mount, Conan package cache mount and cache-rotation workaround. DockerHub build only on tags; GHCR otherwise; push suppressed for PR.

**Causal interpretation.** Attempts reuse and avoids baking token in build ARG; original handler token absence132 allows uncredentialed builds. Login steps lose PR suppression and prior GHCR package write permission is lost until136.

**Limits.** No secret accessed or CI run. Matrix-login availability/permissions unverified.

<a id="commit-135"></a>
### Commit 135 {#commit-135}

06a9c696befb10f8bac98c1b4184bbec778335cb · 2025-01-15T00:42:47Z

[ci: use cibuildwheel for Windows portable build](https://github.com/EndstoneMC/endstone/commit/06a9c696befb10f8bac98c1b4184bbec778335cb)

**Observed change.** Portable Windows flow builds cp312-win_amd64 via cibuildwheel, checks WinPython download hash, installs Endstone from wheelhouse with --no-index rather than building source in embedded interpreter.

**Causal interpretation.** Reuses wheel pipeline and validated distribution, decouples compiler environment from portable runtime.

**Limits.** --no-index can prevent dependency resolution; corrected137–138. No Windows execution.

<a id="commit-136"></a>
### Commit 136 {#commit-136}

e464dba535d27102ae3c0a65085efa39b2902056 · 2025-01-15T00:47:53Z

[ci: add write permissions for packages](https://github.com/EndstoneMC/endstone/commit/e464dba535d27102ae3c0a65085efa39b2902056)

**Observed change.** Restores packages:write job permission after134 workflow consolidation.

**Causal interpretation.** Necessary publishing capability was lost during job merge; mechanical integration fix.

**Limits.** No publishing performed or proven.

<a id="commit-137"></a>
### Commit 137 {#commit-137}

c571a5d8b2cacf22afcd73d166793109908c3a81 · 2025-01-15T01:22:38Z

[ci: inject cache mounts into Docker while building](https://github.com/EndstoneMC/endstone/commit/c571a5d8b2cacf22afcd73d166793109908c3a81)

**Observed change.** Replaces local layer-cache rotation with GHA Buildx cache plus cache-dance mapping Conan mount to actions/cache keyed conanfile; restores Python index access by dropping --no-index portable install.

**Causal interpretation.** BuildKit mount contents and image layers are separate cache stores, hence explicit mount extraction/injection. Portable dependencies require index access; selecting correct local artifact remains addressed138.

**Limits.** No timing/cache-hit verification; cache-dance removed143 after142 strategy changes.

<a id="commit-138"></a>
### Commit 138 {#commit-138}

e0640f6f10ab04b842ae83ccd890a1034b6bef5a · 2025-01-15T14:41:23Z

[ci: fix windows portable build pipeline](https://github.com/EndstoneMC/endstone/commit/e0640f6f10ab04b842ae83ccd890a1034b6bef5a)

**Observed change.** Portable install selects first *.whl from wheelhouse and passes exact FullName to pip.

**Causal interpretation.** Pins produced artifact instead of allowing named package resolution to prefer registry release.

**Limits.** Assumes first matching wheel is intended; no multiple-wheel guard or Windows validation.

<a id="commit-139"></a>
### Commit 139 {#commit-139}

3e39abf21a4e3afc558ebe8fbf967d983b863b59 · 2025-01-15T15:13:56Z

[refactor: simplify conanfile](https://github.com/EndstoneMC/endstone/commit/3e39abf21a4e3afc558ebe8fbf967d983b863b59)

**Observed change.** Conan becomes dependency/toolchain generator: removes git-derived project version, build/test/package/package_info methods and irrelevant capstone options. Devtools variable only set when enabled; optional explicit version temporarily retained.

**Causal interpretation.** Separation of dependency resolution from CMake/scikit-build orchestration; CI must stop conan create (done146). Reduces duplicate metadata authority.

**Limits.** Not a claim equivalent Conan-consumer packaging remains supported; those surfaces are removed.

<a id="commit-140"></a>
### Commit 140 {#commit-140}

f5786bea7dda6bad8c556a40d3a4c9c4553041b3 · 2025-01-15T15:36:00Z

[chore: add optimized compiler and linker flags](https://github.com/EndstoneMC/endstone/commit/f5786bea7dda6bad8c556a40d3a4c9c4553041b3)

**Observed change.** Wheel build type Release; adds platform-specific optimization plus debug information across core, Python and runtime (/O2,/Zi,/Gy,DEBUG,REF,ICF or -O2,-g,-DNDEBUG). Keeps optional separate Unix Python symbols.

**Causal interpretation.** Optimized release artifacts can remain diagnosable. Flags applied unconditionally by platform rather than per-config, so nominal Debug builds also acquire optimizations/NDEBUG.

**Limits.** No performance,size or symbolic-stack benchmark; pybind stripping still undermines goal until148.

<a id="commit-141"></a>
### Commit 141 {#commit-141}

c2761d53737278a03fe9afc9ef36d503b4a9fdff · 2025-01-15T16:05:09Z

[refactor: use version from skbuild](https://github.com/EndstoneMC/endstone/commit/c2761d53737278a03fe9afc9ef36d503b4a9fdff)

**Observed change.** Moves version macros to detail/common.h with fallback0.6.0; scikit-build full project version overrides core compile definition. Removes server #error and crashpad strip target; shared includes updated.

**Causal interpretation.** Build frontend supplies release/dev version while standalone headers retain fallback; avoiding unconditional strip preserves diagnostic payload.

**Limits.** No generated version or wheel check; external includes of old version.h break.

<a id="commit-142"></a>
### Commit 142 {#commit-142}

2ac4db97db8f849957659a29a069548b90af7d25 · 2025-01-15T16:21:40Z

[refactor: improve caching opportunities in Dockerfile](https://github.com/EndstoneMC/endstone/commit/2ac4db97db8f849957659a29a069548b90af7d25)

**Observed change.** Reorders Docker layers: copy only conanfile and install C++ dependencies before full source copy, removing Conan cache mount. Keeps secret mounted only build step; final stage pip installs all copied wheels. Adds optimize/debug flags to bedrock target and removes recipe version variable.

**Causal interpretation.** Stable dependency-only layer now carries package cache, allowing source edits to reuse it;143 removes obsolete mount-dance integration. Existing final nonroot user is also given passwordless sudo, so USER alone is not strong confinement.

**Limits.** No measured speed gain or image security audit; upstream script installers unexecuted.

<a id="commit-143"></a>
### Commit 143 {#commit-143}

961e4d59bb93fc07ef943e3fd9e0d61cd5f37ae4 · 2025-01-15T16:23:37Z

[ci: remove unused caching steps](https://github.com/EndstoneMC/endstone/commit/961e4d59bb93fc07ef943e3fd9e0d61cd5f37ae4)

**Observed change.** Removes actions/cache+cache-dance Conan steps after142 eliminates corresponding cache mount; GHA layer caching retained.

**Causal interpretation.** Avoid redundant cache mechanisms once dependencies reside in cacheable image layer.

**Limits.** No CI run.

<a id="commit-144"></a>
### Commit 144 {#commit-144}

169fbf3bc23346d63aa8b7c81fe0191ac6135454 · 2025-01-15T16:35:13Z

[ci: update Conan cache keys to use 'Release' build type](https://github.com/EndstoneMC/endstone/commit/169fbf3bc23346d63aa8b7c81fe0191ac6135454)

**Observed change.** Wheel/portable Conan cache keys switch RelWithDebInfo→Release with broad fallback keys retained.

**Causal interpretation.** Reflects new build identity, reducing primary-key mismatch; fallback can still restore mixed older entries which Conan must validate.

**Limits.** No cache correctness test.

<a id="commit-145"></a>
### Commit 145 {#commit-145}

3c7f46266cf713f38ba332ca09b9e773d3ccfc76 · 2025-01-15T16:35:25Z

[docs: update build instructions in CONTRIBUTING.md](https://github.com/EndstoneMC/endstone/commit/3c7f46266cf713f38ba332ca09b9e773d3ccfc76)

**Observed change.** Contribution docs align Conan/build presets/environment paths with Release default and update example CMake version3.31.2.

**Causal interpretation.** Build-system migration includes operator-facing commands; removing explicit build_type assumes default Release profile.

**Limits.** Documented commands not executed.

<a id="commit-146"></a>
### Commit 146 {#commit-146}

e4cac590b176af41369d2a2b000601570c63de54 · 2025-01-15T16:41:56Z

[ci: update CI workflow](https://github.com/EndstoneMC/endstone/commit/e4cac590b176af41369d2a2b000601570c63de54)

**Observed change.** CI matrix narrows to Release; conan create becomes install, then explicit CMake configure/build and ctest steps.

**Causal interpretation.** Repairs pipeline for dependency-only recipe139, makes test step visible. Initial configure location does not match later build directory, corrected147.

**Limits.** CTest instruction is not a passing test record; matrix loses RelWithDebInfo coverage.

<a id="commit-147"></a>
### Commit 147 {#commit-147}

77e3175e46e495e03f892078f383bea916159802 · 2025-01-15T17:14:57Z

[ci: fix CMake build directory](https://github.com/EndstoneMC/endstone/commit/77e3175e46e495e03f892078f383bea916159802)

**Observed change.** CI enters build/Release, configures source../.. with relative toolchain and Ninja, builds current directory; ctest keeps matching directory.

**Causal interpretation.** Source/build/toolchain paths must be mutually consistent after changing orchestration.

**Limits.** No workflow result.

<a id="commit-148"></a>
### Commit 148 {#commit-148}

ef1f0e4dcd4749d9c730c2a0bfb8aa48d1217d43 · 2025-01-15T17:52:52Z

[chore: prevent symbol stripping from Python bindings in Release mode](https://github.com/EndstoneMC/endstone/commit/ef1f0e4dcd4749d9c730c2a0bfb8aa48d1217d43)

**Observed change.** Replaces pybind11_add_module with plain MODULE library, explicit pybind11::module/extension/hidden visibility, optional LTO and windows_extras, preserving custom debug handling instead of pybind helper's Release stripping. Also temporarily removes Ninja from CI configure.

**Causal interpretation.** Convenience CMake helper had hidden artifact mutation; explicit reconstruction keeps needed extension/link properties while controlling symbol lifecycle.

**Limits.** No binary-symbol verification. CI generator omission repaired149.

<a id="commit-149"></a>
### Commit 149 {#commit-149}

ee9c9082b4a96fc20cb6dd1ac9bcc8ac5ab7cded · 2025-01-15T18:02:01Z

[ci: make sure Ninja generator is used on Windows](https://github.com/EndstoneMC/endstone/commit/ee9c9082b4a96fc20cb6dd1ac9bcc8ac5ab7cded)

**Observed change.** Restores -G Ninja to CI configure after148 removal.

**Causal interpretation.** Windows default generator must match Conan toolchain/build layout; small repair, not independent preference evidence.

**Limits.** No Windows validation.

<a id="commit-150"></a>
### Commit 150 {#commit-150}

be3830ca4081df50179edf47104837deaf581ad0 · 2025-01-15T18:29:32Z

[chore: update CMake options for funchook](https://github.com/EndstoneMC/endstone/commit/be3830ca4081df50179edf47104837deaf581ad0)

**Observed change.** Sets funchook shared/tests/install options as CMake cache BOOLs; disables install and stops forcing capstone disassembler.

**Causal interpretation.** FetchContent subproject options need correct cache semantics; embedded dependency shouldn't install unrelated artifacts.

**Limits.** No forced override of user cache values; default disassembler choice not independently inspected here.
