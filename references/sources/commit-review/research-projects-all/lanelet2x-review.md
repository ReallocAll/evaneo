<!-- retrieval: {"source_ids":["public:commit:00aa9228651dc730ec6c567cede3784aee5f7508","public:commit:0195c63c8f1e2165150fb17a514d9f56516d948d","public:commit:0a8b069884403ee8b6815bf64786dcb12705e030","public:commit:1376b7bd001933ce0ad25c59c250910ec9d5dce0","public:commit:14991e12eaf1925fb32b6a9f4c80d7e3dec571ea","public:commit:18a338ba4ea4992f294716aca8270a61ae775922","public:commit:1f1e04dc0754c71212b244004af1396e46cb6a74","public:commit:21674a16b150f80d92546989c37cc618e1b7a199","public:commit:24082b2faa9b1b945b64ee67b3c770f94073ec14","public:commit:2adb59bb77a27b857e2988f6c67236aba6f096a4","public:commit:2cd7db4e8537f001f5b25cd2ad484b30f548ab1e","public:commit:2e457eea57d75faea645691149132d565c51316d","public:commit:31d3a9154b94a0bab825563a9c0edf257120cea4","public:commit:3c9f0d50dc6ca7c1461b6b90029a43b04125179e","public:commit:3d12059418e224ead0c39783429f3f5b0e9c5a87","public:commit:45ba2ec8fd239b3085a80f0f8777710fcc884f40","public:commit:4dd0773b386e001cdcbc69911f267db6419217f6","public:commit:4ebf46baaed49553e31ddf5a9c1db403c8e7c15b","public:commit:59dff2c4ff01eb0b36bf1c0eba4396dd65946043","public:commit:600296edffeaaed4209c10221da6c2e4456a9522","public:commit:66a6f18f9ff7df126e93721ce886d5f69a36b55d","public:commit:67c1e2bbb90eed568cda2c7efd4ed0617ac5e2f3","public:commit:6a947aa0adf883ae061831f472a2cd0cc3e4059a","public:commit:7057445b355207946bf3fd500bb611882f368b44","public:commit:7b15536da8a2c6ce36d672143c29d02a9b89dc99","public:commit:7b3e7803faec7eaace96a568ba99f37c5673b3ea","public:commit:7c290422cc33f72ec44ef4ea0110da05b56140d8","public:commit:7cd5e3d1de2e7abb26ca02f344a24001057c2dde","public:commit:7e4725f4725bc63d1b130357ad63ea5bc4738951","public:commit:7e86eb6a19c5b742f0de6991c4a2d1e6c91be4d7","public:commit:8004a9ae6a2e5e3f04685c3c37f5eb6118be57d8","public:commit:8456e4e37a02bf000da282bcd60e16628b6e630a","public:commit:8f1bf9a1f471b2a32ddea4a342a0bdfdeca92724","public:commit:9a0296bcc405db769d80f01b977ef027c3c91347","public:commit:a199a909e526e33ca2cbe5dc724515d887350530","public:commit:a2731802d29ab6bccf2611d1fd6a89d2f5c63401","public:commit:ac5ed41b3ae13aa787ea429c58546f983c6d31a4","public:commit:b28e5bdd4d875d04c17787951fd755fe5dd5d098","public:commit:b42a0ded686e27aa8e9d85ab0a23a5ac45065964","public:commit:b4b9df4a887a02257798b9740e20e4a0b3fd1272","public:commit:bdd604587ad6403068f1864680e18e87e665b88a","public:commit:c568ca1c9a4a105484486489d3e9bf6e70091c3e","public:commit:c729821bfdc40f62b41be0f7bc1fec3337fc80ec","public:commit:cb96f178a3e67b7600a5666bc9ac269be25e2892","public:commit:cb97b5b0b293583ed6f51096622a21d370a5ce6b","public:commit:cdc4d6109a7cb2dda10f20af32bda013a5ad6e78","public:commit:ce99dcc21ad70ebf6ba9bdcd896e812025b13d5e","public:commit:df37128241d06418c1c4471d890ff7563c77fa13","public:commit:df3fcb02d07b7fc26f742afdf9439d3d2712e9da","public:commit:e55d298bf7f118dd39fc89e66994734540875f73","public:commit:e80788d0c73f43c201391e8f0387efeb598529d3","public:commit:ec0c02fb33c30089869c6c42d0963c541c46e5a4","public:commit:f311f6ac63151260e752ef6bedda71028445410e","public:commit:f5a46faabf2ff711ceaa3064109b959cb8f3d3ce","public:commit:f6708f5e51d90271a2a79931c5c25e0dcf8920fc","public:commit:fb3a3f6200da4b00665a9f22f3668ee39379b173"],"source_type":"public","date":"2023-11-19..2025-10-16","topics":["ffi","testing","build","api","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="wu-vincent-lanelet2x-per-sha-review"></a>
# wu-vincent/lanelet2x — per-SHA review {#wu-vincent-lanelet2x-per-sha-review}

56 reviewed commits. Commit messages and meaningful changes were reviewed; structural exceptions are explicit. No runtime validation.

## 1. feat: use conan2 instead of conan, replace mrt_cmake with plain cmake commands {#1-feat-use-conan2-instead-of-conan-replace-mrtcmake-with-plain-cmake-commands}

[600296edffeaaed4209c10221da6c2e4456a9522](https://github.com/wu-vincent/lanelet2x/commit/600296edffeaaed4209c10221da6c2e4456a9522) · 2023-11-19T19:24:59Z

Begins the ROS/mrt-to-standalone migration with Conan 2 CMakeToolchain/CMakeDeps and a plain root/core build. Other modules remain disabled here. This is incremental packaging work over existing Lanelet2 algorithms, not a complete standalone product at this point.

## 2. feat: guard gcc pragmas {#2-feat-guard-gcc-pragmas}

[00aa9228651dc730ec6c567cede3784aee5f7508](https://github.com/wu-vincent/lanelet2x/commit/00aa9228651dc730ec6c567cede3784aee5f7508) · 2023-11-19T19:35:41Z

Guards GCC diagnostic pragmas around Eigen and adjusts initializer formatting. The meaningful boundary is compiler-specific syntax, not a geometry or numerical change.

## 3. fix: compile errors {#3-fix-compile-errors}

[8456e4e37a02bf000da282bcd60e16628b6e630a](https://github.com/wu-vincent/lanelet2x/commit/8456e4e37a02bf000da282bcd60e16628b6e630a) · 2023-11-19T19:41:10Z

Adds Windows symbol export and math constants, qualifies dependent names in HybridMap/PrimitiveLayer, and disambiguates a shared-pointer exception test. These are compile/lookup portability repairs, not new data structures.

## 4. feat: create conan package for lanelet2 {#4-feat-create-conan-package-for-lanelet2}

[2e457eea57d75faea645691149132d565c51316d](https://github.com/wu-vincent/lanelet2x/commit/2e457eea57d75faea645691149132d565c51316d) · 2023-11-19T22:59:47Z

Adds the Conan package lifecycle and three-OS build/test CI, replacing ROS container assumptions. The early default shared=False still coexists with explicitly SHARED CMake targets; later history resolves that mismatch. Workflow text is not evidence of passing runs.

## 5. feat: add lanelet2_io {#5-feat-add-lanelet2io}

[cdc4d6109a7cb2dda10f20af32bda013a5ad6e78](https://github.com/wu-vincent/lanelet2x/commit/cdc4d6109a7cb2dda10f20af32bda013a5ad6e78) · 2023-11-19T23:42:06Z

Ports lanelet2_io CMake and direct Boost/pugixml dependencies. The Tempfile helper replaces mkdtemp with a literal lanelet2_io_test.XXXXXX directory and create-if-absent, losing unique-directory semantics. Parallel tests with equal filenames can collide; this is a static counterexample, not an observed failed run.

## 6. feat: update ci.yaml {#6-feat-update-ci-yaml}

[7e4725f4725bc63d1b130357ad63ea5bc4738951](https://github.com/wu-vincent/lanelet2x/commit/7e4725f4725bc63d1b130357ad63ea5bc4738951) · 2023-11-19T23:57:03Z

Makes build/test jobs depend on formatting and adds a compilation database for clang-tidy through Conan/CMake. Distinguish formatting enforcement from later non-enforcement of tidy findings.

## 7. fix: lanelet2_io tests {#7-fix-lanelet2io-tests}

[66a6f18f9ff7df126e93721ce886d5f69a36b55d](https://github.com/wu-vincent/lanelet2x/commit/66a6f18f9ff7df126e93721ce886d5f69a36b55d) · 2023-11-20T09:12:39Z

Reconnects IO tests, copies map fixtures into the build tree, adjusts fixture paths, and adds projection linking with GeographicLib. Windows runtime DLL copies are manually enumerated here and evolve into target-closure copying later.

## 8. fix: localeconv() on macos {#8-fix-localeconv-on-macos}

[18a338ba4ea4992f294716aca8270a61ae775922](https://github.com/wu-vincent/lanelet2x/commit/18a338ba4ea4992f294716aca8270a61ae775922) · 2023-11-20T09:32:30Z

Changes std::localeconv to global localeconv and reformats signatures for macOS compilation. Existing decimal-locale handling remains; no claim of locale-independent numeric correctness follows.

## 9. misc: do not enforce clang-tidy {#9-misc-do-not-enforce-clang-tidy}

[df3fcb02d07b7fc26f742afdf9439d3d2712e9da](https://github.com/wu-vincent/lanelet2x/commit/df3fcb02d07b7fc26f742afdf9439d3d2712e9da) · 2023-11-20T09:42:34Z

Comments out the clang-tidy failure gate while formatting still gates the build. This commit records a local CI choice, not a durable dislike of static analysis or evidence that warnings were fixed.

## 10. feat: add lanelet2_traffic_rules {#10-feat-add-lanelet2trafficrules}

[7e86eb6a19c5b742f0de6991c4a2d1e6c91be4d7](https://github.com/wu-vincent/lanelet2x/commit/7e86eb6a19c5b742f0de6991c4a2d1e6c91be4d7) · 2023-11-20T09:42:47Z

Adds the standalone traffic-rules library/test target and links its existing core dependency. Built-in traffic-rule semantics remain upstream.

## 11. feat: add lanelet2_routing {#11-feat-add-lanelet2routing}

[24082b2faa9b1b945b64ee67b3c770f94073ec14](https://github.com/wu-vincent/lanelet2x/commit/24082b2faa9b1b945b64ee67b3c770f94073ec14) · 2023-11-20T11:56:03Z

Adds standalone routing targets/tests, changes the vertex map key to size_t, and moves constexpr relation constants into lambdas for compilation. The routing tempfile has the same fixed-directory limitation as IO. No routing algorithm invention is supported.

## 12. fix: macos build {#12-fix-macos-build}

[67c1e2bbb90eed568cda2c7efd4ed0617ac5e2f3](https://github.com/wu-vincent/lanelet2x/commit/67c1e2bbb90eed568cda2c7efd4ed0617ac5e2f3) · 2023-11-20T11:59:29Z

Adds an explicit string header to Exceptions.h for macOS. A self-contained-header dependency repair, with no independent architectural lesson beyond the local include contract.

## 13. fix: lanelet2_routing tests on MSVC {#13-fix-lanelet2routing-tests-on-msvc}

[a199a909e526e33ca2cbe5dc724515d887350530](https://github.com/wu-vincent/lanelet2x/commit/a199a909e526e33ca2cbe5dc724515d887350530) · 2023-11-21T10:09:13Z

Moves a test fixture from namespace static state to inline static class state for MSVC. Later C++14 reversion replaces this approach; do not treat the intermediate C++17 form as final policy.

## 14. feat: add numpy and ninja as requirements {#14-feat-add-numpy-and-ninja-as-requirements}

[1376b7bd001933ce0ad25c59c250910ec9d5dce0](https://github.com/wu-vincent/lanelet2x/commit/1376b7bd001933ce0ad25c59c250910ec9d5dce0) · 2023-11-21T10:10:16Z

Adds Ninja and NumPy and raises the pip CMake minimum. Dependency declaration only; successful availability across all operating systems is not demonstrated here.

## 15. feat: use ninja as the generator on all platforms {#15-feat-use-ninja-as-the-generator-on-all-platforms}

[0195c63c8f1e2165150fb17a514d9f56516d948d](https://github.com/wu-vincent/lanelet2x/commit/0195c63c8f1e2165150fb17a514d9f56516d948d) · 2023-11-21T10:22:52Z

Forces Ninja in the Conan toolchain and simplifies CI build steps. The Windows branch is later explicitly relaxed, providing a counterexample to a universal-generator preference.

## 16. feat: add lanelet2_validation {#16-feat-add-lanelet2validation}

[3c9f0d50dc6ca7c1461b6b90029a43b04125179e](https://github.com/wu-vincent/lanelet2x/commit/3c9f0d50dc6ca7c1461b6b90029a43b04125179e) · 2023-11-21T11:03:48Z

Adds standalone validation library, validator executable discovery, dependencies, and tests. Tool target/install variable naming is still in transition; this is integration of existing validators, not new validation algorithms.

## 17. feat: update ci.yaml, add ci status to README.md {#17-feat-update-ci-yaml-add-ci-status-to-readme-md}

[ce99dcc21ad70ebf6ba9bdcd896e812025b13d5e](https://github.com/wu-vincent/lanelet2x/commit/ce99dcc21ad70ebf6ba9bdcd896e812025b13d5e) · 2023-11-21T11:43:08Z

Adds the MSVC developer environment for Ninja and updates CI badge links toward the fork. The developer-environment dependency explains part of the platform-specific generator handling.

## 18. feat: add lanelet2_matching {#18-feat-add-lanelet2matching}

[f6708f5e51d90271a2a79931c5c25e0dcf8920fc](https://github.com/wu-vincent/lanelet2x/commit/f6708f5e51d90271a2a79931c5c25e0dcf8920fc) · 2023-11-21T12:52:34Z

Ports matching CMake, fixes canonical include paths, and integrates tests and DLL staging. Existing probabilistic matching and geometry belong to upstream authors.

## 19. refactor: code cleanup {#19-refactor-code-cleanup}

[b28e5bdd4d875d04c17787951fd755fe5dd5d098](https://github.com/wu-vincent/lanelet2x/commit/b28e5bdd4d875d04c17787951fd755fe5dd5d098) · 2023-11-21T14:34:37Z

Removes ROS package manifests/rosdoc/custom build remnants, applies GNUInstallDirs, and relocates debugger helpers byte-for-byte. Exact helper moves are structurally verified; the algorithms in moved scripts are not attributed to a file move. Native install/build dependency changes were read separately.

- Limit: The two debugger-script moves were checked for matching Git blob identities, not re-read as independent implementations.

## 20. chore: cmake_minimum_required 3.21 {#20-chore-cmakeminimumrequired-3-21}

[e55d298bf7f118dd39fc89e66994734540875f73](https://github.com/wu-vincent/lanelet2x/commit/e55d298bf7f118dd39fc89e66994734540875f73) · 2023-11-21T16:38:08Z

Raises CMake minimum to 3.21, replaces manually listed DLL copies with TARGET_RUNTIME_DLLS on Windows, uses Boost headers target, and begins a Python CMake target. This first Python source glob is corrected in the next commit.

## 21. feat: add lanelet2_python {#21-feat-add-lanelet2python}

[8f1bf9a1f471b2a32ddea4a342a0bdfdeca92724](https://github.com/wu-vincent/lanelet2x/commit/8f1bf9a1f471b2a32ddea4a342a0bdfdeca92724) · 2023-11-21T17:15:01Z

Enables Python bindings, fixes source-directory globbing, enables Boost.Python, finds Python development/interpreter support, links all native components, and adds MSVC /bigobj. This is binding/build integration over the existing API.

## 22. feat: add pyproject.toml {#22-feat-add-pyproject-toml}

[8004a9ae6a2e5e3f04685c3c37f5eb6118be57d8](https://github.com/wu-vincent/lanelet2x/commit/8004a9ae6a2e5e3f04685c3c37f5eb6118be57d8) · 2023-11-21T18:21:50Z

Adds scikit-build-core pyproject configuration and SOABI Python module construction while removing the ROS metapackage. Deletes stale generated clang-tidy/CodeClimate artifacts; those are schema/count/hash dispositioned, not reread as original source. An initially copied project description is corrected later.

- Limit: Deleted generated clang-tidy-fixes.yaml and codeclimate.json received schema/count/hash checks, not a semantic reading of every generated diagnostic.

## 23. feat: do not force the use of ninja on Windows {#23-feat-do-not-force-the-use-of-ninja-on-windows}

[45ba2ec8fd239b3085a80f0f8777710fcc884f40](https://github.com/wu-vincent/lanelet2x/commit/45ba2ec8fd239b3085a80f0f8777710fcc884f40) · 2023-11-22T08:38:23Z

Stops forcing Ninja on Windows and uses the multi-configuration Conan preset there. Early wheel test-option spelling is corrected later. Platform accommodation rather than one universally preferred build generator.

## 24. feat: build wheel {#24-feat-build-wheel}

[6a947aa0adf883ae061831f472a2cd0cc3e4059a](https://github.com/wu-vincent/lanelet2x/commit/6a947aa0adf883ae061831f472a2cd0cc3e4059a) · 2023-11-22T10:36:32Z

Builds wheel staging and module naming, Windows DLL discovery, dynamic version metadata, and Python-test cleanup. Auto-importing the native package to read its version is an intermediate build-time coupling later removed. Test changes largely preserve existing API expectations.

## 25. feat: enable continuous deployment {#25-feat-enable-continuous-deployment}

[e80788d0c73f43c201391e8f0387efeb598529d3](https://github.com/wu-vincent/lanelet2x/commit/e80788d0c73f43c201391e8f0387efeb598529d3) · 2023-11-23T01:04:00Z

Adds cibuildwheel CI/CD across Windows/Linux/macOS and CPython versions, source distribution and tag publishing configuration, plus installed-wheel pytest commands. Linux restores the manylinux static Python archive and forces source builds for reported b2 incompatibility. No publish, wheel-install success, or license acceptance was performed by this review.

## 26. fix: project description {#26-fix-project-description}

[cb96f178a3e67b7600a5666bc9ac269be25e2892](https://github.com/wu-vincent/lanelet2x/commit/cb96f178a3e67b7600a5666bc9ac269be25e2892) · 2023-11-23T01:34:38Z

Corrects the copied project description to Lanelet2. A verified metadata repair, not evidence about independent architecture or personal writing style.

## 27. feat: update CMakeLists.txt {#27-feat-update-cmakelists-txt}

[2cd7db4e8537f001f5b25cd2ad484b30f548ab1e](https://github.com/wu-vincent/lanelet2x/commit/2cd7db4e8537f001f5b25cd2ad484b30f548ab1e) · 2023-11-23T17:04:22Z

Moves SKBUILD RPATH handling to root CMake and stages dependency shared libraries into build/lib for wheel repair. This is an intermediate repair staging strategy; an absolute build path alone would not make a relocatable delivered wheel.

## 28. feat: update conanfile.py {#28-feat-update-conanfile-py}

[b42a0ded686e27aa8e9d85ab0a23a5ac45065964](https://github.com/wu-vincent/lanelet2x/commit/b42a0ded686e27aa8e9d85ab0a23a5ac45065964) · 2023-11-23T17:43:36Z

Adds a macOS loader-relative RPATH to the staged Boost.Filesystem dylib. Later expands to all staged Boost dylibs. Local repair configuration, with no runtime loader result.

## 29. Merge remote-tracking branch 'origin/master' {#29-merge-remote-tracking-branch-origin-master}

[3d12059418e224ead0c39783429f3f5b0e9c5a87](https://github.com/wu-vincent/lanelet2x/commit/3d12059418e224ead0c39783429f3f5b0e9c5a87) · 2023-11-23T21:34:08Z

Merges the fork-authored RPATH/staging branch and description branch. Both parent deltas and merge-base/side history were checked; no independent algorithm change is introduced by the merge identity.

## 30. feat: use std::filesystem instead of boost::filesystem {#30-feat-use-std-filesystem-instead-of-boost-filesystem}

[1f1e04dc0754c71212b244004af1396e46cb6a74](https://github.com/wu-vincent/lanelet2x/commit/1f1e04dc0754c71212b244004af1396e46cb6a74) · 2023-11-24T11:44:19Z

Attempts std::filesystem to remove Boost.Filesystem/atomic/system dependencies and removes obsolete ROS/Conan helper scripts. Shortly reverted to preserve C++14; the attempted modernization cannot be promoted to final design intent.

## 31. feat: update README.md {#31-feat-update-readme-md}

[2adb59bb77a27b857e2988f6c67236aba6f096a4](https://github.com/wu-vincent/lanelet2x/commit/2adb59bb77a27b857e2988f6c67236aba6f096a4) · 2023-11-24T12:10:41Z

Rewrites README around the standalone fork with upstream authorship retained, documents Conan/Python installation, and aligns library staging/install paths for wheel repair. Documentation support claims remain reported, not reproduced.

## 32. fix: revert std::filesystem {#32-fix-revert-std-filesystem}

[fb3a3f6200da4b00665a9f22f3668ee39379b173](https://github.com/wu-vincent/lanelet2x/commit/fb3a3f6200da4b00665a9f22f3668ee39379b173) · 2023-11-24T12:34:11Z

Reverts std::filesystem, restores Boost, and returns C++ to 14. Reworks static test fixture lifetime through a function-local static but temporarily declares the fixture member incorrectly; a later focused fix completes it. macOS RPATH patching expands across Boost dylibs.

## 33. refactor: format codes {#33-refactor-format-codes}

[7b15536da8a2c6ce36d672143c29d02a9b89dc99](https://github.com/wu-vincent/lanelet2x/commit/7b15536da8a2c6ce36d672143c29d02a9b89dc99) · 2023-11-24T12:50:14Z

Formats C++ and Python binding code and changes formatter configuration. Existing geometry, serialization, and binding behavior are not newly authored because of formatting. Classifier cleanup continues later.

## 34. fix: repair wheels on Linux and MacOS {#34-fix-repair-wheels-on-linux-and-macos}

[ec0c02fb33c30089869c6c42d0963c541c46e5a4](https://github.com/wu-vincent/lanelet2x/commit/ec0c02fb33c30089869c6c42d0963c541c46e5a4) · 2023-11-24T12:53:12Z

Corrects repair staging from build_path to source_path/build/lib, matching the CMake RPATH/install contract. Evidence of a coordinated path fix, not measured successful wheel repair.

## 35. feat: update ci.yaml {#35-feat-update-ci-yaml}

[4ebf46baaed49553e31ddf5a9c1db403c8e7c15b](https://github.com/wu-vincent/lanelet2x/commit/4ebf46baaed49553e31ddf5a9c1db403c8e7c15b) · 2023-11-24T12:57:55Z

Pins formatter tooling to version 17 and temporarily applies checks beyond changed files. CI scope/configuration only.

## 36. feat: update ci.yaml {#36-feat-update-ci-yaml}

[c568ca1c9a4a105484486489d3e9bf6e70091c3e](https://github.com/wu-vincent/lanelet2x/commit/c568ca1c9a4a105484486489d3e9bf6e70091c3e) · 2023-11-24T13:01:24Z

Removes the explicit files-changed-only override. The diff supports the configuration change but gives no reason; no motive is invented.

## 37. fix: lanelet2_routing tests {#37-fix-lanelet2routing-tests}

[21674a16b150f80d92546989c37cc618e1b7a199](https://github.com/wu-vincent/lanelet2x/commit/21674a16b150f80d92546989c37cc618e1b7a199) · 2023-11-24T14:29:21Z

Fixes the routing-test fixture declaration into a reference initialized by getTestData(). This closes the concrete C++14 fixture regression introduced during filesystem reversion.

## 38. refactor: use standard BUILD_TESTING instead of LANELET2_ENABLE_TESTING {#38-refactor-use-standard-buildtesting-instead-of-lanelet2enabletesting}

[0a8b069884403ee8b6815bf64786dcb12705e030](https://github.com/wu-vincent/lanelet2x/commit/0a8b069884403ee8b6815bf64786dcb12705e030) · 2023-11-24T14:39:08Z

Renames the custom test switch to BUILD_TESTING, makes GTest a test requirement, and calls cmake.test(). The string comparison with OFF is narrower than conventional CMake boolean handling; two module guards are corrected next.

## 39. fix: conanfile.py to respect BUILD_SHARED_LIBS {#39-fix-conanfile-py-to-respect-buildsharedlibs}

[f5a46faabf2ff711ceaa3064109b959cb8f3d3ce](https://github.com/wu-vincent/lanelet2x/commit/f5a46faabf2ff711ceaa3064109b959cb8f3d3ce) · 2023-11-24T15:01:59Z

Makes add_library respect BUILD_SHARED_LIBS, adds static-output suffixes, updates Conan package metadata, and replaces native-package import for version lookup with a literal version. Component dependency metadata is refined later.

## 40. fix: add missing tests {#40-fix-add-missing-tests}

[59dff2c4ff01eb0b36bf1c0eba4396dd65946043](https://github.com/wu-vincent/lanelet2x/commit/59dff2c4ff01eb0b36bf1c0eba4396dd65946043) · 2023-11-24T15:05:59Z

Updates core and IO to the new BUILD_TESTING guard. The title says missing tests, but the diff reconnects existing test configuration rather than adding new test algorithms.

## 41. feat: prepare for release v1.2.1 {#41-feat-prepare-for-release-v1-2-1}

[7057445b355207946bf3fd500bb611882f368b44](https://github.com/wu-vincent/lanelet2x/commit/7057445b355207946bf3fd500bb611882f368b44) · 2023-11-25T02:40:41Z

Prepares 1.2.1 with Conan component names/dependency graph and external-consumer examples, relocatable example discovery, Python tutorial cleanup, and wheel tests for examples as well as bindings. Existing tutorial algorithms retain upstream credit. An extra sdist upload name using absent matrix variables is removed later.

## 42. refactor: python script clean up {#42-refactor-python-script-clean-up}

[7cd5e3d1de2e7abb26ca02f344a24001057c2dde](https://github.com/wu-vincent/lanelet2x/commit/7cd5e3d1de2e7abb26ca02f344a24001057c2dde) · 2023-11-25T02:53:12Z

Cleans Python command-line helpers: explicit module imports, main guards, iteritems to items, and a usable default participant. This improves import/use boundaries, but the not-found print still concatenates int args.has_id with a string, so cleanup does not establish Python3 path completeness.

## 43. refactor: remove unused files {#43-refactor-remove-unused-files}

[a2731802d29ab6bccf2611d1fd6a89d2f5c63401](https://github.com/wu-vincent/lanelet2x/commit/a2731802d29ab6bccf2611d1fd6a89d2f5c63401) · 2023-11-25T02:57:26Z

Removes obsolete GitLab ROS/Conan1 CI and an empty gitmodules file. Verified cleanup only; removing old integration support is a product boundary, not proof of all downstream compatibility.

## 44. refactor: only install libs and headers {#44-refactor-only-install-libs-and-headers}

[f311f6ac63151260e752ef6bedda71028445410e](https://github.com/wu-vincent/lanelet2x/commit/f311f6ac63151260e752ef6bedda71028445410e) · 2023-11-25T02:59:34Z

Restricts non-wheel install content to libraries/headers, removing map resources/docs/scripts from several install paths. Consumers needing example data must provide it separately; installation simplification trades away bundled resources.

## 45. release: lanelet2x v1.2.1 {#45-release-lanelet2x-v1-2-1}

[7c290422cc33f72ec44ef4ea0110da05b56140d8](https://github.com/wu-vincent/lanelet2x/commit/7c290422cc33f72ec44ef4ea0110da05b56140d8) · 2023-11-25T12:07:56Z

Release-labelled metadata/CI cleanup removes the redundant invalid-matrix sdist upload, enables pip caching, and uses specific OS classifiers. This source commit does not itself verify that version 1.2.1 was published.

## 46. feat: use conan to build in CI {#46-feat-use-conan-to-build-in-ci}

[31d3a9154b94a0bab825563a9c0edf257120cea4](https://github.com/wu-vincent/lanelet2x/commit/31d3a9154b94a0bab825563a9c0edf257120cea4) · 2023-11-27T00:59:47Z

Moves CI from separate manual configure/build/CTest steps to conan create and an explicit shared=True option matrix. The recipe still calls tests; this is packaged-consumer-oriented CI configuration.

## 47. feat: build as static library {#47-feat-build-as-static-library}

[9a0296bcc405db769d80f01b977ef027c3c91347](https://github.com/wu-vincent/lanelet2x/commit/9a0296bcc405db769d80f01b977ef027c3c91347) · 2023-11-27T02:31:30Z

Adds static/shared CI coverage and relocates built-in regulatory-element, parser/writer, traffic-rule, and validator registrars into their factory translation units. This creates symbol-reference reachability from factory use to implementations in static archives. Test fixture paths become source-root explicit and Windows DLL copy tolerates empty closures. No measured linker/runtime result is claimed.

## 48. feat: build as static library by default {#48-feat-build-as-static-library-by-default}

[cb97b5b0b293583ed6f51096622a21d370a5ce6b](https://github.com/wu-vincent/lanelet2x/commit/cb97b5b0b293583ed6f51096622a21d370a5ce6b) · 2023-11-30T09:48:17Z

Makes Conan static libraries the default, preserves shared=True for Python wheel prebuilds, and declares transitive Boost headers. A concrete split between C++ consumer distribution and Python extension packaging, not a blanket preference for static linking.

## 49. merge from upstream {#49-merge-from-upstream}

[bdd604587ad6403068f1864680e18e87e665b88a](https://github.com/wu-vincent/lanelet2x/commit/bdd604587ad6403068f1864680e18e87e665b88a) · 2023-12-07T23:41:52Z

Imports upstream GeocentricProjector origin initialization and its tutorial test, reverting tutorial formatting to the upstream version. Both final blobs exactly match upstream a41d75b authored by Michał Antkiewicz. This merge integrates the upstream change; the numerical-origin fix and test are credited upstream.

## 50. Merge branch 'fzi-forschungszentrum-informatik:master' into master {#50-merge-branch-fzi-forschungszentrum-informatik-master-into-master}

[df37128241d06418c1c4471d890ff7563c77fa13](https://github.com/wu-vincent/lanelet2x/commit/df37128241d06418c1c4471d890ff7563c77fa13) · 2023-12-07T23:42:28Z

Ancestry-only merge: tree equals first parent bdd604. Second-parent aggregate represents previously reviewed fork work against upstream, not new original authorship. Whole aggregate is structurally mapped to earlier fork changes; no duplicated 277748-byte semantic-read claim.

- Limit: Second-parent cumulative fork diff not reread literally: merge tree equals first parent, upstream-only changed paths have exact upstream blob identity, and fork-side history is covered by preceding entries.

## 51. feat: update Dockerfile {#51-feat-update-dockerfile}

[ac5ed41b3ae13aa787ea429c58546f983c6d31a4](https://github.com/wu-vincent/lanelet2x/commit/ac5ed41b3ae13aa787ea429c58546f983c6d31a4) · 2023-12-08T00:30:08Z

Replaces ROS Docker staging with a Python3.11 slim/Conan/Python-package recipe and updates README commands. The replacement no longer includes the old explicit non-root user and uses floating image/dependency choices; no image was built or executed. A guarded old deleted line remains opaque.

- Limit: 1 guarded line(s) remain opaque; not read or recovered.

## 52. Merge remote-tracking branch 'origin/master' {#52-merge-remote-tracking-branch-origin-master}

[4dd0773b386e001cdcbc69911f267db6419217f6](https://github.com/wu-vincent/lanelet2x/commit/4dd0773b386e001cdcbc69911f267db6419217f6) · 2023-12-08T00:30:18Z

Merges Docker and upstream integration branches. Parent1 patch is byte-identical to bdd604; parent2 patch is byte-identical to ac5ed41. Both previously read changes retain their original attribution and guard limitations; no new lesson counted for the merge.

- Limit: Exact raw-diff SHA256 matches separately read bdd604 (parent1) or ac5ed41 (parent2).
- Limit: Exact raw-diff SHA256 matches separately read bdd604 (parent1) or ac5ed41 (parent2).
- Limit: 1 guarded line(s) remain opaque; not read or recovered.

## 53. feat: add code coverage {#53-feat-add-code-coverage}

[7b3e7803faec7eaace96a568ba99f37c5673b3ea](https://github.com/wu-vincent/lanelet2x/commit/7b3e7803faec7eaace96a568ba99f37c5673b3ea) · 2023-12-08T01:25:17Z

Adds Debug GCC coverage integration, LCOV collection after CTest, Codecov upload config, and an attributed 747-line CodeCoverage.cmake helper. Full helper text was read, but Lars Bilke and other listed contributors retain authorship; no exact external-version equivalence is asserted. Default test-enabled GCC builds now receive coverage flags. No coverage percentage or passing run is supplied.

## 54. feat: add codecov badge {#54-feat-add-codecov-badge}

[b4b9df4a887a02257798b9740e20e4a0b3fd1272](https://github.com/wu-vincent/lanelet2x/commit/b4b9df4a887a02257798b9740e20e4a0b3fd1272) · 2023-12-08T01:45:54Z

Adds a Codecov badge. Badge configuration is not measured coverage or evidence of successful upload.

## 55. Update README.md {#55-update-readme-md}

[14991e12eaf1925fb32b6a9f4c80d7e3dec571ea](https://github.com/wu-vincent/lanelet2x/commit/14991e12eaf1925fb32b6a9f4c80d7e3dec571ea) · 2023-12-11T15:33:48Z

Corrects macOS capitalization in README. No independent engineering lesson.

## 56. Update README.md {#56-update-readme-md}

[c729821bfdc40f62b41be0f7bc1fec3337fc80ec](https://github.com/wu-vincent/lanelet2x/commit/c729821bfdc40f62b41be0f7bc1fec3337fc80ec) · 2023-12-20T23:47:33Z

Clarifies README availability on Windows/Linux/macOS. This is an author-reported support claim; local source review did not verify installation/runtime on those systems.
