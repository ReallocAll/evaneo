<!-- retrieval: {"source_ids":["public:commit:05e3f888c68196827574019d085f49662f9310bf","public:commit:0822628f479461a19644cbc5e518b5d5ad941ef1","public:commit:0925ac771bd53fd1b0d94d5abf4cdd6c955ec025","public:commit:1954760eacb89dd8b7142dd15aae79fb24b71fcb","public:commit:2c7f306515233b4ab6ca798a63ba3297fc135b79","public:commit:2fc2daa771366ffe012847b64d6f6233e0bd6568","public:commit:32684966003e7b1d429ae85686d0d78b30baaa7b","public:commit:37f59b2eca2b409e6514c1deb04048e82357c5bc","public:commit:39ac169793b9b6fb0e5150934b8d0378b0203a76","public:commit:3a6e1a118c75a532bc03b41db700542dcff43e2c","public:commit:3c96463d94da99a5b0cf142f900e5943b689bd1e","public:commit:5610297207487b3bef39827f74c0f40e2340ad7d","public:commit:5661427fb15bcf3b8cfbfb8e0c92f911430ba9d7","public:commit:583c6d60c56259bdaabcbf84ee21be25b93aa731","public:commit:6898470fa963ceb400cdc03571a3423bcce46ad8","public:commit:753433be03f2d3a357f1440b8d2121b4920d5379","public:commit:757a44d820d55159964ad9ecf09746b2b9a51f0e","public:commit:7db69b7fa4eae7bd1dddda77920aaee75f6dc56a","public:commit:8e2f0c4a78b21035d48bad6e15feca7f44a1455c","public:commit:9815f26009d1b1912d385672713fb7db54fbd6e3","public:commit:9c439fb33def7000c99f707782b07c55be2763aa","public:commit:9d48aac7cc206b5cb945a43be2e8761c0cdd64e6","public:commit:9f8bbe26f854799157925cdf39921b305f65d818","public:commit:a35acc0085db06f95ee0606b4185a1d007dfb1b9","public:commit:aa826d4b9e1d9d7d0e4599fce34303b5d23dc05c","public:commit:b03b4be30ef4e9bd5febbbbda4543cd1d247daf8","public:commit:c0995512ab55cf838e2d739db0aefc2ed712a970","public:commit:c7579a84b1180c375da08f000a154ec365375ad0","public:commit:c7b6e5cca49215b832d42b155f4d3918da26593b","public:commit:ca74d16252eba9118a0eb61b42b58841b09ca223","public:commit:cf1a3e83d67c5168ebf1c65e5c6350b526cbe744","public:commit:e832f0d67356fcd4fc7efd9269d773858f686592","public:commit:e93668c70c8642dce65f116aa084dce97587b9a9","public:commit:ea35502e735315ab5e44c78a39c9ce258b54de92","public:commit:f666f998d4a7cf9e35ee7d877959ed1c2fc66f89","public:commit:f68b84d741b8c6b2af13cf133e73a36f06ed74cc","public:commit:fd0be5a409358964c9e97dd0eebfbd8bdd4d3b26"],"source_type":"public","date":"2023-12-18..2024-01-13","topics":["ffi","testing","build","performance","api","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Build, dependencies, packaging and delivery {#build-dependencies-packaging-and-delivery}

## The build is part of the ABI contract {#the-build-is-part-of-the-abi-contract}

The early public contract exchanges C++ objects with an already-built Bedrock host. Toolchain selection therefore serves binary compatibility, not merely compiler preference.5 adds Clang CI.14 changes to GCC with explicit comments about host GCC7.5/MSVC versions, plus experimental filesystem and stdc++fs support.24 drops GCC7 and those compatibility branches;94 later removes GCC8 from tested CI without changing the recipe minimum.104 explicitly chooses old libstdc++ ABI.108 finally validates Clang with libc++, citing host Clang15.0.7, even though the title incorrectly says stdc++. The actual configuration takes precedence over the title.118 replaces the remaining GCC setup with the project development image.

These are observed revisions, including contradictory intermediate states. They do not prove every intermediate commit built, or every declared compiler minimum was exercised. Useful questions for a future ABI review are: which host binary/version is the reference, which standard-library ABI is required, which compiler minima are merely declared, and what consumer compile/link requirements escape through public headers?

## Package-consumer invariants {#package-consumer-invariants}

CMake's PUBLIC/PRIVATE visibility and Conan component metadata are separate contracts.10 links dl both locally and for package consumers.44 changes fmt from header-only to compiled and exports transitive libraries.70 makes smart-holder/version definitions and native links PUBLIC in CMake;91 still needs the holder definition in Conan core metadata. A local executable passing is not enough to prove a separately packaged downstream consumer receives the same settings.

Python packaging has another joined invariant: extension target name, PYBIND11_MODULE initialization symbol, install destination, package imports and test copying must agree.18 introduces the wheel layout,53 moves the extension under _internal, and34/37 show how a namespace move can leave an sdist inclusion path stale.19–22 revise private setuptools_scm APIs, git-derived versions, import paths and spelling.60 deliberately decouples host game version from package version. Full history/tags become required inputs for some build paths; an sdist checkout and source archive do not automatically possess them.

## Dependency and environment choices {#dependency-and-environment-choices}

The pybind11 chain is FetchContent pinned commit → custom Conan smart_holder → standard ConanCenter package. Pins are more specific than branch names, but several custom archive fetches lack a content digest. Imported ConanCenter recipes and smoke tests should retain their source credit; they are integration work, not evidence that the commit author invented every recipe mechanism. Native LIEF is tried at0.13.1/0.10.1, replaced with Python LIEF0.13.2, then restored to native0.10.1. The source supports an integration experiment; no measured speed/memory advantage is supplied.

Docker revisions move from a PPA to pyenv-built Python, then reduce layers and purge packages. Claims of reduced size lack measurements in this unit. The final stage initially inherits the build environment, and caches/source can remain. Custom manylinux and development images move toolchain assumptions out of this repository; mutable latest tags reduce reproducible identification.109 removes the local Docker workflow; its title's claimed move to another repository is not verified here.

## Visibility, coverage and release evidence {#visibility-coverage-and-release-evidence}

110 tries global hidden visibility and exported C++ RTTI handling;112 backs that down to runtime-specific hiding and fixes unconditional LIEF discovery on Windows. This counsels inspecting the exact boundary being hidden instead of extracting a blanket preference.

29 imports Lars Bilke's 747-line coverage helper with contributor credits and licenses; Endstone invokes its compiler-flag function.119 replaces LCOV collection with gcovr plus llvm-cov gcov for Clang and aligns build/Debug paths.120 deletes the identical, now-unused imported module. This complete deletion is verified by blob identity, not treated as747 newly unseen semantic lines.

CI and release definitions describe intended execution: Debug/Release/compiler matrices, wheel and sdist builds, tag-gated GitHub/PyPI release, Docker publication and Codecov upload. No workflow logs, artifact inspections, performance profiles, coverage percentages or deployment outcomes were read in this workunit. Secret references were inspected as configuration names; secret values were not acquired or copied.

## How to apply this evidence {#how-to-apply-this-evidence}

Use the detailed chain to audit initialization, toolchain constraints, CMake/Conan propagation, native Python embedding versus extension linkage, source/wheel completeness, and reproducibility. Prefer a minimal downstream consumer test plus actual artifact import and host integration tests. Treat imported recipes, dependency package tests and synthetic host tests as distinct validation layers. Compiler and dependency reversals are counterexamples to overgeneralizing a lasting personal preference from one commit.

## Individual commit evidence {#individual-commit-evidence}



<a id="commit-4"></a>
### 4. feat: add github action ci {#commit-4}

- Source: [8e2f0c4a78b21035d48bad6e15feca7f44a1455c](https://github.com/EndstoneMC/endstone/commit/8e2f0c4a78b21035d48bad6e15feca7f44a1455c)
- Authored: 2023-12-18T00:05:44Z; parent: `1226cb2d1393b4b7cc660561c67d88f9a557adf0`
- Disposition: meaningful; full actual diff statically reviewed.

Introduces Windows CI across 2019/2022 runners and Debug/Release, invoking conan create with C++17, plus pyproject packaging metadata. Python wheel settings and CLI remain commented; CI source is not evidence of a passed run. Declared Python >=3.9 is broader than the selected CI interpreter 3.11.

Changed-path evidence: [.github/workflows/ci-windows.yml](https://github.com/EndstoneMC/endstone/blob/8e2f0c4a78b21035d48bad6e15feca7f44a1455c/.github/workflows/ci-windows.yml) (+39/−0); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/8e2f0c4a78b21035d48bad6e15feca7f44a1455c/pyproject.toml) (+51/−0)



<a id="commit-5"></a>
### 5. feat: add github action ci for linux {#commit-5}

- Source: [1954760eacb89dd8b7142dd15aae79fb24b71fcb](https://github.com/EndstoneMC/endstone/commit/1954760eacb89dd8b7142dd15aae79fb24b71fcb)
- Authored: 2023-12-18T00:36:44Z; parent: `8e2f0c4a78b21035d48bad6e15feca7f44a1455c`
- Disposition: meaningful; full actual diff statically reviewed.

Adds Ubuntu/Clang 11–15 CI and raises recipe minimum Clang to 7 with an explicit filesystem-support comment. The tested matrix and declared minimum are different evidence: no run result establishes support for 7.

Changed-path evidence: [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/1954760eacb89dd8b7142dd15aae79fb24b71fcb/.github/workflows/ci-linux.yml) (+45/−0); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/1954760eacb89dd8b7142dd15aae79fb24b71fcb/conanfile.py) (+1/−1)



<a id="commit-10"></a>
### 10. fix: link endstone_core with libdl on Linux {#commit-10}

- Source: [f68b84d741b8c6b2af13cf133e73a36f06ed74cc](https://github.com/EndstoneMC/endstone/commit/f68b84d741b8c6b2af13cf133e73a36f06ed74cc)
- Authored: 2023-12-19T12:05:47Z; parent: `1164f2efd4eb3318ea97df76e0bcfd72f66d7e01`
- Disposition: meaningful; full actual diff statically reviewed.

Links core against CMAKE_DL_LIBS and exports Linux dl in Conan component metadata; makes spdlog a private CMake dependency. Corrects test cwd/artifact placement so plugin discovery and executable invocation agree, and adds a Clang Docker reproduction recipe. Native target linking and downstream package-consumer linking are separately addressed.

Changed-path evidence: [conanfile.py](https://github.com/EndstoneMC/endstone/blob/f68b84d741b8c6b2af13cf133e73a36f06ed74cc/conanfile.py) (+2/−0); [dockerfile/Dockerfile.build-linux](https://github.com/EndstoneMC/endstone/blob/f68b84d741b8c6b2af13cf133e73a36f06ed74cc/dockerfile/Dockerfile.build-linux) (+15/−0); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/f68b84d741b8c6b2af13cf133e73a36f06ed74cc/endstone_core/CMakeLists.txt) (+4/−1); [test_package/conanfile.py](https://github.com/EndstoneMC/endstone/blob/f68b84d741b8c6b2af13cf133e73a36f06ed74cc/test_package/conanfile.py) (+3/−6)



<a id="commit-14"></a>
### 14. refactor: build with gcc on Linux {#commit-14}

- Source: [5610297207487b3bef39827f74c0f40e2340ad7d](https://github.com/EndstoneMC/endstone/commit/5610297207487b3bef39827f74c0f40e2340ad7d)
- Authored: 2023-12-19T17:52:28Z; parent: `4076a53158fdde21fac1ba5d877073f5d9ccf9c8`
- Disposition: meaningful; full actual diff statically reviewed.

Switches Linux recipe/CI/container from Clang to GCC, citing Bedrock Linux GCC 7.5 and Windows MSVC ABI compatibility in comments. Adds experimental-filesystem aliases for GCC<8 in public and implementation headers plus stdc++fs linkage. This is a conditional compatibility tactic, later removed when GCC7 support is dropped; it increases public-header/platform coupling.

Changed-path evidence: [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/5610297207487b3bef39827f74c0f40e2340ad7d/.github/workflows/ci-linux.yml) (+10/−18); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/5610297207487b3bef39827f74c0f40e2340ad7d/conanfile.py) (+9/−6); [dockerfile/Dockerfile.build-linux](https://github.com/EndstoneMC/endstone/blob/5610297207487b3bef39827f74c0f40e2340ad7d/dockerfile/Dockerfile.build-linux) (+2/−1); [endstone_api/include/endstone/plugin/plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/5610297207487b3bef39827f74c0f40e2340ad7d/endstone_api/include/endstone/plugin/plugin_manager.h) (+10/−3); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/5610297207487b3bef39827f74c0f40e2340ad7d/endstone_core/CMakeLists.txt) (+2/−2); [endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/5610297207487b3bef39827f74c0f40e2340ad7d/endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h) (+10/−3); [endstone_core/src/endstone_core/endstone_server.cpp](https://github.com/EndstoneMC/endstone/blob/5610297207487b3bef39827f74c0f40e2340ad7d/endstone_core/src/endstone_core/endstone_server.cpp) (+9/−1); [endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp](https://github.com/EndstoneMC/endstone/blob/5610297207487b3bef39827f74c0f40e2340ad7d/endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp) (+17/−10)



<a id="commit-16"></a>
### 16. feat: update github action ci {#commit-16}

- Source: [aa826d4b9e1d9d7d0e4599fce34303b5d23dc05c](https://github.com/EndstoneMC/endstone/commit/aa826d4b9e1d9d7d0e4599fce34303b5d23dc05c)
- Authored: 2023-12-19T18:49:38Z; parent: `cc1fd33789a1fd676372902cc5b360e6b67c107b`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces GCC containers with Ubuntu 20.04 plus setup-gcc and expands Linux/Windows jobs over Python 3.9–3.12. One following commit removes the Python axis, so this is a short-lived experiment, not proof of sustained multi-interpreter CI coverage.

Changed-path evidence: [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/aa826d4b9e1d9d7d0e4599fce34303b5d23dc05c/.github/workflows/ci-linux.yml) (+18/−9); [.github/workflows/ci-windows.yml](https://github.com/EndstoneMC/endstone/blob/aa826d4b9e1d9d7d0e4599fce34303b5d23dc05c/.github/workflows/ci-windows.yml) (+3/−2)



<a id="commit-17"></a>
### 17. refactor: remove python versions from build matrix {#commit-17}

- Source: [c0995512ab55cf838e2d739db0aefc2ed712a970](https://github.com/EndstoneMC/endstone/commit/c0995512ab55cf838e2d739db0aefc2ed712a970)
- Authored: 2023-12-19T18:54:14Z; parent: `aa826d4b9e1d9d7d0e4599fce34303b5d23dc05c`
- Disposition: small-semantic; full actual diff statically reviewed.

Removes Python matrix dimensions and restores setup-python 3.11 on both platforms while retaining compiler/build dimensions. Reverses the preceding expansion; no explicit motive or performance measurement appears.

Changed-path evidence: [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/c0995512ab55cf838e2d739db0aefc2ed712a970/.github/workflows/ci-linux.yml) (+2/−3); [.github/workflows/ci-windows.yml](https://github.com/EndstoneMC/endstone/blob/c0995512ab55cf838e2d739db0aefc2ed712a970/.github/workflows/ci-windows.yml) (+2/−3)



<a id="commit-18"></a>
### 18. feat: prepare to build wheels for windows and linux {#commit-18}

- Source: [9d48aac7cc206b5cb945a43be2e8761c0cdd64e6](https://github.com/EndstoneMC/endstone/commit/9d48aac7cc206b5cb945a43be2e8761c0cdd64e6)
- Authored: 2023-12-20T14:20:51Z; parent: `c0995512ab55cf838e2d739db0aefc2ed712a970`
- Disposition: meaningful; full actual diff statically reviewed.

Creates Python package facade, _api binary naming, CLI placeholder, Server stub/import tests, wheel-only CMake install component and cibuildwheel Windows/manylinux recipes. Package facade copies the extension module dictionary wholesale, later replaced by explicit imports. Separates Conan installation from the scikit-build build-system dependency list; both orchestration and artifact layout must align. Tests are import smoke checks only.

Changed-path evidence: [README.md](https://github.com/EndstoneMC/endstone/blob/9d48aac7cc206b5cb945a43be2e8761c0cdd64e6/README.md) (+1/−0); [endstone_api/include/endstone/server.h](https://github.com/EndstoneMC/endstone/blob/9d48aac7cc206b5cb945a43be2e8761c0cdd64e6/endstone_api/include/endstone/server.h) (+3/−0); [endstone_python/.gitignore](https://github.com/EndstoneMC/endstone/blob/9d48aac7cc206b5cb945a43be2e8761c0cdd64e6/endstone_python/.gitignore) (+1/−0); [endstone_python/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/9d48aac7cc206b5cb945a43be2e8761c0cdd64e6/endstone_python/CMakeLists.txt) (+5/−2); [endstone_python/python/endstone/__init__.py](https://github.com/EndstoneMC/endstone/blob/9d48aac7cc206b5cb945a43be2e8761c0cdd64e6/endstone_python/python/endstone/__init__.py) (+5/−0); [endstone_python/python/endstone/_bootstrap.py](https://github.com/EndstoneMC/endstone/blob/9d48aac7cc206b5cb945a43be2e8761c0cdd64e6/endstone_python/python/endstone/_bootstrap.py) (+2/−0); [endstone_python/python/endstone/server.pyi](https://github.com/EndstoneMC/endstone/blob/9d48aac7cc206b5cb945a43be2e8761c0cdd64e6/endstone_python/python/endstone/server.pyi) (+6/−0); [endstone_python/src/endstone_python/endstone_python.cpp](https://github.com/EndstoneMC/endstone/blob/9d48aac7cc206b5cb945a43be2e8761c0cdd64e6/endstone_python/src/endstone_python/endstone_python.cpp) (+1/−1); [endstone_python/test/test_endstone.py](https://github.com/EndstoneMC/endstone/blob/9d48aac7cc206b5cb945a43be2e8761c0cdd64e6/endstone_python/test/test_endstone.py) (+11/−0); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/9d48aac7cc206b5cb945a43be2e8761c0cdd64e6/pyproject.toml) (+46/−24)



<a id="commit-19"></a>
### 19. feat: automatic versioning for conanfile based on pyproject.toml {#commit-19}

- Source: [fd0be5a409358964c9e97dd0eebfbd8bdd4d3b26](https://github.com/EndstoneMC/endstone/commit/fd0be5a409358964c9e97dd0eebfbd8bdd4d3b26)
- Authored: 2023-12-20T14:47:08Z; parent: `9d48aac7cc206b5cb945a43be2e8761c0cdd64e6`
- Disposition: meaningful; full actual diff statically reviewed.

Derives Conan version through private setuptools_scm APIs using pyproject configuration, adds Python version exports and asserts their presence. The import is absolute from _version rather than endstone._version; the next revisions fix this lineage. Dynamic-version provider availability and exported source/archive behavior are not demonstrated.

Changed-path evidence: [.gitignore](https://github.com/EndstoneMC/endstone/blob/fd0be5a409358964c9e97dd0eebfbd8bdd4d3b26/.gitignore) (+1/−0); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/fd0be5a409358964c9e97dd0eebfbd8bdd4d3b26/conanfile.py) (+4/−1); [endstone_python/python/endstone/__init__.py](https://github.com/EndstoneMC/endstone/blob/fd0be5a409358964c9e97dd0eebfbd8bdd4d3b26/endstone_python/python/endstone/__init__.py) (+2/−0); [endstone_python/test/test_endstone.py](https://github.com/EndstoneMC/endstone/blob/fd0be5a409358964c9e97dd0eebfbd8bdd4d3b26/endstone_python/test/test_endstone.py) (+3/−1); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/fd0be5a409358964c9e97dd0eebfbd8bdd4d3b26/pyproject.toml) (+2/−0)



<a id="commit-20"></a>
### 20. feat: improve automatic versioning {#commit-20}

- Source: [6898470fa963ceb400cdc03571a3423bcce46ad8](https://github.com/EndstoneMC/endstone/commit/6898470fa963ceb400cdc03571a3423bcce46ad8)
- Authored: 2023-12-20T16:23:27Z; parent: `fd0be5a409358964c9e97dd0eebfbd8bdd4d3b26`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces private setuptools_scm invocation with Conan set_version using git describe and regex parsing, respecting an explicit version override. Propagates package/game versions into CMake definitions and derives four-component Minecraft version in Python/C++; CMake now fails if variables are absent. Requires tags and four release components, with no fallback or validation shown. Python attribute is initially misspelled __minecraft__version__, repaired next; no versioning runtime proof supplied.

Changed-path evidence: [conanfile.py](https://github.com/EndstoneMC/endstone/blob/6898470fa963ceb400cdc03571a3423bcce46ad8/conanfile.py) (+28/−4); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/6898470fa963ceb400cdc03571a3423bcce46ad8/endstone_core/CMakeLists.txt) (+10/−0); [endstone_core/include/endstone_core/endstone_server.h](https://github.com/EndstoneMC/endstone/blob/6898470fa963ceb400cdc03571a3423bcce46ad8/endstone_core/include/endstone_core/endstone_server.h) (+5/−3); [endstone_python/python/endstone/__init__.py](https://github.com/EndstoneMC/endstone/blob/6898470fa963ceb400cdc03571a3423bcce46ad8/endstone_python/python/endstone/__init__.py) (+4/−0); [test_package/src/test_server.cpp](https://github.com/EndstoneMC/endstone/blob/6898470fa963ceb400cdc03571a3423bcce46ad8/test_package/src/test_server.cpp) (+2/−0)



<a id="commit-21"></a>
### 21. feat: add endstone cd {#commit-21}

- Source: [757a44d820d55159964ad9ecf09746b2b9a51f0e](https://github.com/EndstoneMC/endstone/commit/757a44d820d55159964ad9ecf09746b2b9a51f0e)
- Authored: 2023-12-20T16:53:39Z; parent: `6898470fa963ceb400cdc03571a3423bcce46ad8`
- Disposition: meaningful; full actual diff statically reviewed.

Adds wheels for CPython 3.9–3.12 on Windows/manylinux plus sdist, tag-gated GitHub/PyPI publish using id-token permission and artifact restoration. Full checkout history is added to binary CI and wheel jobs for git-derived versions; sdist checkout still lacks explicit full history. Also fixes the absolute _version import. Workflow definitions show intended release gating, not an actual release or verification outcome.

Changed-path evidence: [.github/workflows/cd.yml](https://github.com/EndstoneMC/endstone/blob/757a44d820d55159964ad9ecf09746b2b9a51f0e/.github/workflows/cd.yml) (+92/−0); [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/757a44d820d55159964ad9ecf09746b2b9a51f0e/.github/workflows/ci-linux.yml) (+2/−0); [.github/workflows/ci-windows.yml](https://github.com/EndstoneMC/endstone/blob/757a44d820d55159964ad9ecf09746b2b9a51f0e/.github/workflows/ci-windows.yml) (+2/−0); [endstone_python/python/endstone/__init__.py](https://github.com/EndstoneMC/endstone/blob/757a44d820d55159964ad9ecf09746b2b9a51f0e/endstone_python/python/endstone/__init__.py) (+1/−1)



<a id="commit-24"></a>
### 24. feat: drop support for GCC 7 {#commit-24}

- Source: [3c96463d94da99a5b0cf142f900e5943b689bd1e](https://github.com/EndstoneMC/endstone/commit/3c96463d94da99a5b0cf142f900e5943b689bd1e)
- Authored: 2023-12-21T12:01:29Z; parent: `3883d65c03185804e3f4f02e483675fbea482912`
- Disposition: meaningful; full actual diff statically reviewed.

Raises minimum GCC to 8, removes 7 from CI and deletes experimental filesystem branches. Comment acknowledges Bedrock's GCC7.5 while enforcing a newer build compiler. This reverses the compatibility effort from commit 14 without providing a measured reason; public filesystem remains until commit 32.

Changed-path evidence: [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/3c96463d94da99a5b0cf142f900e5943b689bd1e/.github/workflows/ci-linux.yml) (+1/−1); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/3c96463d94da99a5b0cf142f900e5943b689bd1e/conanfile.py) (+5/−4); [endstone_api/include/endstone/plugin/plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/3c96463d94da99a5b0cf142f900e5943b689bd1e/endstone_api/include/endstone/plugin/plugin_manager.h) (+1/−7); [endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/3c96463d94da99a5b0cf142f900e5943b689bd1e/endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h) (+1/−7); [endstone_core/src/endstone_core/endstone_server.cpp](https://github.com/EndstoneMC/endstone/blob/3c96463d94da99a5b0cf142f900e5943b689bd1e/endstone_core/src/endstone_core/endstone_server.cpp) (+1/−7); [endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp](https://github.com/EndstoneMC/endstone/blob/3c96463d94da99a5b0cf142f900e5943b689bd1e/endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp) (+1/−7)



<a id="commit-29"></a>
### 29. feat: add code coverage to ci {#commit-29}

- Source: [39ac169793b9b6fb0e5150934b8d0378b0203a76](https://github.com/EndstoneMC/endstone/commit/39ac169793b9b6fb0e5150934b8d0378b0203a76)
- Authored: 2023-12-21T17:46:10Z; parent: `d08f4430f83b30568e942e29464a27f3f19d27ee`
- Disposition: meaningful; full actual diff statically reviewed.

Adds Debug coverage job (Conan install, CMake CODE_COVERAGE, ctest, lcov, Codecov) and imports a 747-line CodeCoverage.cmake module. Module credits Lars Bilke and contributors, includes BSD-style redistribution terms, prerequisite/compiler checks, flags and lcov/gcovr/fastcov targets; project calls append_coverage_compiler_flags only. No coverage percentage or successful test run is observed. Deletes obsolete GCC7 Docker recipe and exports cmake helpers in Conan.

Changed-path evidence: [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/39ac169793b9b6fb0e5150934b8d0378b0203a76/.github/workflows/ci-linux.yml) (+44/−1); [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/39ac169793b9b6fb0e5150934b8d0378b0203a76/CMakeLists.txt) (+10/−1); [cmake/CodeCoverage.cmake](https://github.com/EndstoneMC/endstone/blob/39ac169793b9b6fb0e5150934b8d0378b0203a76/cmake/CodeCoverage.cmake) (+747/−0); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/39ac169793b9b6fb0e5150934b8d0378b0203a76/conanfile.py) (+1/−1); [dockerfile/Dockerfile.build-linux](https://github.com/EndstoneMC/endstone/blob/d08f4430f83b30568e942e29464a27f3f19d27ee/dockerfile/Dockerfile.build-linux) (+0/−16)



<a id="commit-34"></a>
### 34. refactor: move internal classes to module endstone._internal {#commit-34}

- Source: [9f8bbe26f854799157925cdf39921b305f65d818](https://github.com/EndstoneMC/endstone/commit/9f8bbe26f854799157925cdf39921b305f65d818)
- Authored: 2023-12-22T02:05:09Z; parent: `9a6f84919661cd1cf304ea755aaedb38c243a8b7`
- Disposition: meaningful; full actual diff statically reviewed.

Moves bootstrap and generated version namespace under _internal and updates imports/CLI/write_to. sdist.include still refers to the old location until commit 37. Empty package marker and exact bootstrap move were verified; no independent algorithmic lesson.

Changed-path evidence: [endstone_python/.gitignore](https://github.com/EndstoneMC/endstone/blob/9f8bbe26f854799157925cdf39921b305f65d818/endstone_python/.gitignore) (+1/−1); [endstone_python/python/endstone/__init__.py](https://github.com/EndstoneMC/endstone/blob/9f8bbe26f854799157925cdf39921b305f65d818/endstone_python/python/endstone/__init__.py) (+1/−1); [endstone_python/python/endstone/_bootstrap.py](https://github.com/EndstoneMC/endstone/blob/9a6f84919661cd1cf304ea755aaedb38c243a8b7/endstone_python/python/endstone/_bootstrap.py) (+0/−2); [endstone_python/python/endstone/_internal/__init__.py](https://github.com/EndstoneMC/endstone/blob/9f8bbe26f854799157925cdf39921b305f65d818/endstone_python/python/endstone/_internal/__init__.py) (+0/−0); [endstone_python/python/endstone/_internal/_bootstrap.py](https://github.com/EndstoneMC/endstone/blob/9f8bbe26f854799157925cdf39921b305f65d818/endstone_python/python/endstone/_internal/_bootstrap.py) (+2/−0); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/9f8bbe26f854799157925cdf39921b305f65d818/pyproject.toml) (+2/−2)



<a id="commit-37"></a>
### 37. refactor: rename modules {#commit-37}

- Source: [753433be03f2d3a357f1440b8d2121b4920d5379](https://github.com/EndstoneMC/endstone/commit/753433be03f2d3a357f1440b8d2121b4920d5379)
- Authored: 2023-12-22T02:20:48Z; parent: `906bfcc4197703414dce28518fad4a67876e63ad`
- Disposition: small-semantic; full actual diff statically reviewed.

Renames internal _bootstrap/_version to bootstrap/version and aligns CLI, generated file, ignore and sdist.include. Repairs package-source inclusion left stale by commit 34; exact bootstrap rename contains no behavioral change.

Changed-path evidence: [endstone_python/.gitignore](https://github.com/EndstoneMC/endstone/blob/753433be03f2d3a357f1440b8d2121b4920d5379/endstone_python/.gitignore) (+1/−1); [endstone_python/python/endstone/__init__.py](https://github.com/EndstoneMC/endstone/blob/753433be03f2d3a357f1440b8d2121b4920d5379/endstone_python/python/endstone/__init__.py) (+1/−1); [endstone_python/python/endstone/_internal/_bootstrap.py](https://github.com/EndstoneMC/endstone/blob/906bfcc4197703414dce28518fad4a67876e63ad/endstone_python/python/endstone/_internal/_bootstrap.py) (+0/−2); [endstone_python/python/endstone/_internal/bootstrap.py](https://github.com/EndstoneMC/endstone/blob/753433be03f2d3a357f1440b8d2121b4920d5379/endstone_python/python/endstone/_internal/bootstrap.py) (+2/−0); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/753433be03f2d3a357f1440b8d2121b4920d5379/pyproject.toml) (+3/−3)



<a id="commit-44"></a>
### 44. refactor: drop option fmt/*:header_only {#commit-44}

- Source: [583c6d60c56259bdaabcbf84ee21be25b93aa731](https://github.com/EndstoneMC/endstone/commit/583c6d60c56259bdaabcbf84ee21be25b93aa731)
- Authored: 2023-12-23T02:19:28Z; parent: `8038a11021b170cbba46c567928c03bce3dc7a05`
- Disposition: meaningful; full actual diff statically reviewed.

Drops fmt header-only option, links fmt::fmt and enables transitive_libs alongside transitive_headers in Conan. Necessary downstream binary linkage follows public inline fmt usage; build-time speed or binary-size outcomes are not measured.

Changed-path evidence: [conanfile.py](https://github.com/EndstoneMC/endstone/blob/583c6d60c56259bdaabcbf84ee21be25b93aa731/conanfile.py) (+2/−2); [endstone_api/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/583c6d60c56259bdaabcbf84ee21be25b93aa731/endstone_api/CMakeLists.txt) (+2/−1)



<a id="commit-47"></a>
### 47. feat: add pybind11 recipe from conan center index {#commit-47}

- Source: [32684966003e7b1d429ae85686d0d78b30baaa7b](https://github.com/EndstoneMC/endstone/commit/32684966003e7b1d429ae85686d0d78b30baaa7b)
- Authored: 2023-12-25T18:12:37Z; parent: `e73d7a11f6e74e6746b3d3587d9a0d2f79d5555b`
- Disposition: meaningful; full actual diff statically reviewed.

Imports pybind11 recipe identified as Conan Center Index, versions/digests and package smoke tests. Recipe installs headers/build modules, suppresses upstream target creation in pybind11Common, exposes Conan components and clears package identity for header-only artifacts. This is third-party integration credit, not wholesale original algorithm authorship; sample test prints arithmetic/message results without assertions.

Changed-path evidence: [third_party/pybind11/conandata.yml](https://github.com/EndstoneMC/endstone/blob/32684966003e7b1d429ae85686d0d78b30baaa7b/third_party/pybind11/conandata.yml) (+25/−0); [third_party/pybind11/conanfile.py](https://github.com/EndstoneMC/endstone/blob/32684966003e7b1d429ae85686d0d78b30baaa7b/third_party/pybind11/conanfile.py) (+80/−0); [third_party/pybind11/test_package/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/32684966003e7b1d429ae85686d0d78b30baaa7b/third_party/pybind11/test_package/CMakeLists.txt) (+5/−0); [third_party/pybind11/test_package/conanfile.py](https://github.com/EndstoneMC/endstone/blob/32684966003e7b1d429ae85686d0d78b30baaa7b/third_party/pybind11/test_package/conanfile.py) (+53/−0); [third_party/pybind11/test_package/test.py](https://github.com/EndstoneMC/endstone/blob/32684966003e7b1d429ae85686d0d78b30baaa7b/third_party/pybind11/test_package/test.py) (+5/−0); [third_party/pybind11/test_package/test_package.cpp](https://github.com/EndstoneMC/endstone/blob/32684966003e7b1d429ae85686d0d78b30baaa7b/third_party/pybind11/test_package/test_package.cpp) (+16/−0)



<a id="commit-53"></a>
### 53. refactor: rename _api to endstone_python and move to endstone._internal package {#commit-53}

- Source: [c7579a84b1180c375da08f000a154ec365375ad0](https://github.com/EndstoneMC/endstone/commit/c7579a84b1180c375da08f000a154ec365375ad0)
- Authored: 2023-12-28T00:58:02Z; parent: `1d6fdbcf24079a85798a1b94a6c1a81e97a563ac`
- Disposition: meaningful; full actual diff statically reviewed.

Renames _api extension to endstone_python under endstone._internal and synchronizes PYBIND11_MODULE name, import wrappers, wheel install path and package-test copying. Module initialization symbol, artifact location and imports form one packaging invariant; partial renames would fail imports.

Changed-path evidence: [endstone_python/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/c7579a84b1180c375da08f000a154ec365375ad0/endstone_python/CMakeLists.txt) (+1/−4); [endstone_python/python/endstone/_internal/plugin_loader.py](https://github.com/EndstoneMC/endstone/blob/c7579a84b1180c375da08f000a154ec365375ad0/endstone_python/python/endstone/_internal/plugin_loader.py) (+2/−1); [endstone_python/python/endstone/logger.py](https://github.com/EndstoneMC/endstone/blob/c7579a84b1180c375da08f000a154ec365375ad0/endstone_python/python/endstone/logger.py) (+1/−1); [endstone_python/python/endstone/plugin.py](https://github.com/EndstoneMC/endstone/blob/c7579a84b1180c375da08f000a154ec365375ad0/endstone_python/python/endstone/plugin.py) (+2/−2); [endstone_python/python/endstone/server.py](https://github.com/EndstoneMC/endstone/blob/c7579a84b1180c375da08f000a154ec365375ad0/endstone_python/python/endstone/server.py) (+1/−1); [endstone_python/src/endstone_python/endstone_python.cpp](https://github.com/EndstoneMC/endstone/blob/c7579a84b1180c375da08f000a154ec365375ad0/endstone_python/src/endstone_python/endstone_python.cpp) (+1/−1); [test_package/conanfile.py](https://github.com/EndstoneMC/endstone/blob/c7579a84b1180c375da08f000a154ec365375ad0/test_package/conanfile.py) (+10/−5)



<a id="commit-60"></a>
### 60. refactor: remove macro ENDSTONE_MINECRAFT_VERSION {#commit-60}

- Source: [3a6e1a118c75a532bc03b41db700542dcff43e2c](https://github.com/EndstoneMC/endstone/commit/3a6e1a118c75a532bc03b41db700542dcff43e2c)
- Authored: 2023-12-31T01:06:02Z; parent: `e0ef42a510b682ba34021a3b928e5093b5acedbc`
- Disposition: meaningful; full actual diff statically reviewed.

Allows optional v tag prefix, removes ENDSTONE_MINECRAFT_VERSION generation/definition and changes server getter to Unknown pending Bedrock query. Explicitly separates build package version from host runtime version; four-part version derivation is abandoned rather than generalized.

Changed-path evidence: [conanfile.py](https://github.com/EndstoneMC/endstone/blob/3a6e1a118c75a532bc03b41db700542dcff43e2c/conanfile.py) (+1/−4); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/e0ef42a510b682ba34021a3b928e5093b5acedbc/endstone_core/CMakeLists.txt) (+0/−5); [endstone_core/src/endstone_core/endstone_server.cpp](https://github.com/EndstoneMC/endstone/blob/3a6e1a118c75a532bc03b41db700542dcff43e2c/endstone_core/src/endstone_core/endstone_server.cpp) (+1/−1)



<a id="commit-68"></a>
### 68. feat: add Dockerfile {#commit-68}

- Source: [0822628f479461a19644cbc5e518b5d5ad941ef1](https://github.com/EndstoneMC/endstone/commit/0822628f479461a19644cbc5e518b5d5ad941ef1)
- Authored: 2024-01-02T17:17:01Z; parent: `bb9219d4989fc8720099cd08205eb405d9d0096e`
- Disposition: meaningful; full actual diff statically reviewed.

Adds Ubuntu Docker build with Python3.11 PPA, Conan custom pybind export/build/install and .dockerignore. Final stage inherits build stage, retaining toolchain and source. Python3.11 invocation and generic pip3 can resolve differently; no image smoke test or size measurement is provided.

Changed-path evidence: [.dockerignore](https://github.com/EndstoneMC/endstone/blob/0822628f479461a19644cbc5e518b5d5ad941ef1/.dockerignore) (+9/−0); [Dockerfile](https://github.com/EndstoneMC/endstone/blob/0822628f479461a19644cbc5e518b5d5ad941ef1/Dockerfile) (+43/−0)



<a id="commit-72"></a>
### 72. feat: use pyenv to install python in docker {#commit-72}

- Source: [b03b4be30ef4e9bd5febbbbda4543cd1d247daf8](https://github.com/EndstoneMC/endstone/commit/b03b4be30ef4e9bd5febbbbda4543cd1d247daf8)
- Authored: 2024-01-03T00:46:03Z; parent: `acaa1bd7325904babf34e750d5423ca30857fbc9`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces distro/PPA Python with pyenv-built Python3.11, sets unbuffered UTF-8 environment, and adds compilation dependencies. curl-to-shell pyenv installation and floating 3.11 selection are supply-chain/reproducibility costs visible in recipe; no execution performed during review.

Changed-path evidence: [Dockerfile](https://github.com/EndstoneMC/endstone/blob/b03b4be30ef4e9bd5febbbbda4543cd1d247daf8/Dockerfile) (+18/−20)



<a id="commit-73"></a>
### 73. feat: add ci for docker {#commit-73}

- Source: [2c7f306515233b4ab6ca798a63ba3297fc135b79](https://github.com/EndstoneMC/endstone/commit/2c7f306515233b4ab6ca798a63ba3297fc135b79)
- Authored: 2024-01-03T09:33:04Z; parent: `b03b4be30ef4e9bd5febbbbda4543cd1d247daf8`
- Disposition: meaningful; full actual diff statically reviewed.

Adds Docker workflow publishing endstone/endstone on next pushes, tags and manual runs, with PEP440/latest metadata and secret references. It is publication automation, not merely build CI; actual secret values were neither read nor recorded. No observed push outcome.

Changed-path evidence: [.github/workflows/ci-docker.yml](https://github.com/EndstoneMC/endstone/blob/2c7f306515233b4ab6ca798a63ba3297fc135b79/.github/workflows/ci-docker.yml) (+44/−0)



<a id="commit-75"></a>
### 75. refactor: reduce docker image size {#commit-75}

- Source: [f666f998d4a7cf9e35ee7d877959ed1c2fc66f89](https://github.com/EndstoneMC/endstone/commit/f666f998d4a7cf9e35ee7d877959ed1c2fc66f89)
- Authored: 2024-01-03T16:32:46Z; parent: `a7a70a5b0c605f0e93b83be2878ab7aa16f3db26`
- Disposition: meaningful; full actual diff statically reviewed.

Consolidates install/build/purge into layers and separates Python/build stages to reduce image size; final still inherits build stage. Removes apt caches and compilation packages after use, but source/Conan caches and Python build state are not comprehensively removed. Title claims size reduction; no measured before/after bytes supplied.

Changed-path evidence: [Dockerfile](https://github.com/EndstoneMC/endstone/blob/f666f998d4a7cf9e35ee7d877959ed1c2fc66f89/Dockerfile) (+23/−27)



<a id="commit-77"></a>
### 77. fix: restore libpython for embedding Python in manylinux container {#commit-77}

- Source: [2fc2daa771366ffe012847b64d6f6233e0bd6568](https://github.com/EndstoneMC/endstone/commit/2fc2daa771366ffe012847b64d6f6233e0bd6568)
- Authored: 2024-01-03T16:54:00Z; parent: `45ab85e759bf5e91dff950d3bc25a3c69e570cb5`
- Disposition: meaningful; full actual diff statically reviewed.

Restores manylinux's archived static libpython libraries before build for embedding, citing its finalize-python script. Extension-only Python distributions and embedding requirements differ; source configuration is evidence of diagnosis but not proof the wheel now links/runs.

Changed-path evidence: [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/2fc2daa771366ffe012847b64d6f6233e0bd6568/pyproject.toml) (+5/−0)



<a id="commit-82"></a>
### 82. refactor: use FindPython, reduce cmake_minimum_required version {#commit-82}

- Source: [5661427fb15bcf3b8cfbfb8e0c92f911430ba9d7](https://github.com/EndstoneMC/endstone/commit/5661427fb15bcf3b8cfbfb8e0c92f911430ba9d7)
- Authored: 2024-01-05T01:10:43Z; parent: `8ef820192d8d65f62039981ea59050fd7ccb1b6f`
- Disposition: meaningful; full actual diff statically reviewed.

Adds explicit FindPython Interpreter+Development.Embed for core and Development.Module for extension, lowers CMake minimum from 3.24 to 3.15 after removing FetchContent override. Separates embedding versus module needs. Declared CMake floor should be checked against component availability; no validation on 3.15 supplied.

Changed-path evidence: [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/5661427fb15bcf3b8cfbfb8e0c92f911430ba9d7/CMakeLists.txt) (+1/−1); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/5661427fb15bcf3b8cfbfb8e0c92f911430ba9d7/endstone_core/CMakeLists.txt) (+1/−0); [endstone_python/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/5661427fb15bcf3b8cfbfb8e0c92f911430ba9d7/endstone_python/CMakeLists.txt) (+1/−0)



<a id="commit-85"></a>
### 85. fix: build wheel on Linux, use custom manylinux x86_64 image {#commit-85}

- Source: [0925ac771bd53fd1b0d94d5abf4cdd6c955ec025](https://github.com/EndstoneMC/endstone/commit/0925ac771bd53fd1b0d94d5abf4cdd6c955ec025)
- Authored: 2024-01-05T03:09:18Z; parent: `b184c0667d2f904a71d749564c1fa4ed86b94daf`
- Disposition: small-semantic; full actual diff statically reviewed.

Selects custom ghcr.io/endstonemc/manylinux2014_x86_64:latest for wheels. Floating image provides missing environment assumptions but reduces reproducible identification; no actual wheel build evidence supplied.

Changed-path evidence: [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/0925ac771bd53fd1b0d94d5abf4cdd6c955ec025/pyproject.toml) (+1/−0)



<a id="commit-93"></a>
### 93. refactor: static libs extraction is no longer needed with the custom manylinux image {#commit-93}

- Source: [05e3f888c68196827574019d085f49662f9310bf](https://github.com/EndstoneMC/endstone/commit/05e3f888c68196827574019d085f49662f9310bf)
- Authored: 2024-01-06T11:11:56Z; parent: `5e62c4afe7bd79410bf068b0611932f75977661d`
- Disposition: small-semantic; full actual diff statically reviewed.

Removes static-libpython extraction because custom manylinux image supplies it, per explicit title. Dependency moved into image contract; no evidence it became unnecessary for all manylinux images.

Changed-path evidence: [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/5e62c4afe7bd79410bf068b0611932f75977661d/pyproject.toml) (+0/−3)



<a id="commit-94"></a>
### 94. chore: remove GCC 8 from CI workflow {#commit-94}

- Source: [cf1a3e83d67c5168ebf1c65e5c6350b526cbe744](https://github.com/EndstoneMC/endstone/commit/cf1a3e83d67c5168ebf1c65e5c6350b526cbe744)
- Authored: 2024-01-07T23:50:24Z; parent: `05e3f888c68196827574019d085f49662f9310bf`
- Disposition: small-semantic; full actual diff statically reviewed.

Drops GCC8 from Linux matrix, retaining9–11; recipe minimum is not updated here. CI coverage contracts and supported compiler declarations therefore differ. No reason in commit body.

Changed-path evidence: [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/cf1a3e83d67c5168ebf1c65e5c6350b526cbe744/.github/workflows/ci-linux.yml) (+1/−1)



<a id="commit-100"></a>
### 100. feat: update funchook conanfile for MSVC support and add version 1.1.3 to CI {#commit-100}

- Source: [37f59b2eca2b409e6514c1deb04048e82357c5bc](https://github.com/EndstoneMC/endstone/commit/37f59b2eca2b409e6514c1deb04048e82357c5bc)
- Authored: 2024-01-08T17:02:57Z; parent: `12a2b2ecabf769da307ef16a959b71c7760e24ec`
- Disposition: meaningful; full actual diff statically reviewed.

Aligns Linux/Windows/wheel CI with funchook export version1.1.3 and chooses funchook_dll library name for shared MSVC builds. Finishes orchestration lag from backend swap; no assertion of successful CI or published artifact.

Changed-path evidence: [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/37f59b2eca2b409e6514c1deb04048e82357c5bc/.github/workflows/ci-linux.yml) (+2/−0); [.github/workflows/ci-windows.yml](https://github.com/EndstoneMC/endstone/blob/37f59b2eca2b409e6514c1deb04048e82357c5bc/.github/workflows/ci-windows.yml) (+1/−1); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/37f59b2eca2b409e6514c1deb04048e82357c5bc/pyproject.toml) (+2/−1); [third_party/funchook/conanfile.py](https://github.com/EndstoneMC/endstone/blob/37f59b2eca2b409e6514c1deb04048e82357c5bc/third_party/funchook/conanfile.py) (+5/−1)



<a id="commit-101"></a>
### 101. refactor: change function name and update conanfile requirements {#commit-101}

- Source: [e832f0d67356fcd4fc7efd9269d773858f686592](https://github.com/EndstoneMC/endstone/commit/e832f0d67356fcd4fc7efd9269d773858f686592)
- Authored: 2024-01-09T10:16:17Z; parent: `37f59b2eca2b409e6514c1deb04048e82357c5bc`
- Disposition: meaningful; full actual diff statically reviewed.

Downgrades native LIEF0.13.1 to0.10.1, disables JSON/frozen options, corrects lief::lief from system_libs to requires and adds UNIX runtime target linkage. Renames module path API to pathname consistently. This is dependency integration repair, not evidence that older releases are generally preferred; no performance or compatibility benchmark accompanies it.

Changed-path evidence: [conanfile.py](https://github.com/EndstoneMC/endstone/blob/e832f0d67356fcd4fc7efd9269d773858f686592/conanfile.py) (+11/−6); [endstone_runtime/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/e832f0d67356fcd4fc7efd9269d773858f686592/endstone_runtime/CMakeLists.txt) (+5/−0); [endstone_runtime/include/endstone_runtime/platform.h](https://github.com/EndstoneMC/endstone/blob/e832f0d67356fcd4fc7efd9269d773858f686592/endstone_runtime/include/endstone_runtime/platform.h) (+1/−1); [endstone_runtime/src/endstone_runtime/hook.cpp](https://github.com/EndstoneMC/endstone/blob/e832f0d67356fcd4fc7efd9269d773858f686592/endstone_runtime/src/endstone_runtime/hook.cpp) (+2/−2); [endstone_runtime/src/endstone_runtime/platform_windows.cpp](https://github.com/EndstoneMC/endstone/blob/e832f0d67356fcd4fc7efd9269d773858f686592/endstone_runtime/src/endstone_runtime/platform_windows.cpp) (+1/−1)



<a id="commit-104"></a>
### 104. fix(endstone_runtime): link to libstdc++ instead of libstdc++11 for ABI compatability {#commit-104}

- Source: [ca74d16252eba9118a0eb61b42b58841b09ca223](https://github.com/EndstoneMC/endstone/commit/ca74d16252eba9118a0eb61b42b58841b09ca223)
- Authored: 2024-01-10T12:37:45Z; parent: `ff92b7f5d9ad1ec766b8d62b3201966d8128ea84`
- Disposition: meaningful; full actual diff statically reviewed.

Explicitly requests gnu17 plus libstdc++ (old dual ABI) throughout CI/Docker/wheels, hides core symbols for GNU, stops stripping installed artifacts, and moves toward Python LIEF0.13.2 rather than CMake/native linking. The stated ABI motive is consistent with C++ objects crossing host/plugin boundaries. Intermediate CI still needs its dependencies aligned; install.strip=false is operationally material to introspection, not cosmetic packaging.

Changed-path evidence: [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/ca74d16252eba9118a0eb61b42b58841b09ca223/.github/workflows/ci-linux.yml) (+2/−2); [Dockerfile](https://github.com/EndstoneMC/endstone/blob/ca74d16252eba9118a0eb61b42b58841b09ca223/Dockerfile) (+1/−1); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/ca74d16252eba9118a0eb61b42b58841b09ca223/endstone_core/CMakeLists.txt) (+2/−1); [endstone_runtime/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/ca74d16252eba9118a0eb61b42b58841b09ca223/endstone_runtime/CMakeLists.txt) (+5/−12); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/ca74d16252eba9118a0eb61b42b58841b09ca223/pyproject.toml) (+3/−2)



<a id="commit-108"></a>
### 108. fix: use clang with stdc++ instead of gcc on Linux {#commit-108}

- Source: [ea35502e735315ab5e44c78a39c9ce258b54de92](https://github.com/EndstoneMC/endstone/commit/ea35502e735315ab5e44c78a39c9ce258b54de92)
- Authored: 2024-01-10T18:02:42Z; parent: `564f72311a863205d26f41ab1cfe19600cb5ec5b`
- Disposition: meaningful; full actual diff statically reviewed.

Actual Conan validation mandates Clang>=5 and libc++, despite commit title saying clang with stdc++. Comment ties this to the host built with Clang15.0.7. CI, Docker and wheels request libc++; Linux compiler setup still selects GCC until118. Removes stdc++fs, broadens hidden/exclude flags from GNU to UNIX. Title/code disagreement and the delayed CI correction prevent treating this as an already verified portable toolchain.

Changed-path evidence: [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/ea35502e735315ab5e44c78a39c9ce258b54de92/.github/workflows/ci-linux.yml) (+2/−2); [Dockerfile](https://github.com/EndstoneMC/endstone/blob/ea35502e735315ab5e44c78a39c9ce258b54de92/Dockerfile) (+1/−1); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/ea35502e735315ab5e44c78a39c9ce258b54de92/conanfile.py) (+11/−7); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/ea35502e735315ab5e44c78a39c9ce258b54de92/endstone_core/CMakeLists.txt) (+2/−2); [endstone_runtime/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/ea35502e735315ab5e44c78a39c9ce258b54de92/endstone_runtime/CMakeLists.txt) (+2/−2); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/ea35502e735315ab5e44c78a39c9ce258b54de92/pyproject.toml) (+1/−1)



<a id="commit-109"></a>
### 109. refactor: move endstone docker ci to endstone-docker repo {#commit-109}

- Source: [9815f26009d1b1912d385672713fb7db54fbd6e3](https://github.com/EndstoneMC/endstone/commit/9815f26009d1b1912d385672713fb7db54fbd6e3)
- Authored: 2024-01-10T18:03:45Z; parent: `ea35502e735315ab5e44c78a39c9ce258b54de92`
- Disposition: mechanical_scope; full actual diff statically reviewed.

Deletes this repository's Docker publish workflow. Title claims it moves to endstone-docker, but destination repository/content were not inspected here. Verified local effect is removal of the publish job; external migration completion remains unknown.

Changed-path evidence: [.github/workflows/ci-docker.yml](https://github.com/EndstoneMC/endstone/blob/ea35502e735315ab5e44c78a39c9ce258b54de92/.github/workflows/ci-docker.yml) (+0/−44)



<a id="commit-112"></a>
### 112. refactor: adjust linux-specific build options in CMakeLists {#commit-112}

- Source: [9c439fb33def7000c99f707782b07c55be2763aa](https://github.com/EndstoneMC/endstone/commit/9c439fb33def7000c99f707782b07c55be2763aa)
- Authored: 2024-01-11T22:35:19Z; parent: `305a79765b794bd9e5defae02963154f9e337cda`
- Disposition: meaningful; full actual diff statically reviewed.

Reverses global hidden visibility, core hidden flags and extension dynamic-list-cpp-typeinfo while retaining runtime hiding. Guards find_package(LIEF) with UNIX. This narrows the immediately preceding visibility experiment and repairs Windows dependency lookup; do not infer a blanket preference for or against symbol hiding.

Changed-path evidence: [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/305a79765b794bd9e5defae02963154f9e337cda/CMakeLists.txt) (+0/−1); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/305a79765b794bd9e5defae02963154f9e337cda/endstone_core/CMakeLists.txt) (+0/−1); [endstone_python/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/9c439fb33def7000c99f707782b07c55be2763aa/endstone_python/CMakeLists.txt) (+1/−3); [endstone_runtime/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/9c439fb33def7000c99f707782b07c55be2763aa/endstone_runtime/CMakeLists.txt) (+3/−1)



<a id="commit-116"></a>
### 116. feat: update workflows to reflect the removal of custom pybind11 recipe {#commit-116}

- Source: [e93668c70c8642dce65f116aa084dce97587b9a9](https://github.com/EndstoneMC/endstone/commit/e93668c70c8642dce65f116aa084dce97587b9a9)
- Authored: 2024-01-12T16:07:33Z; parent: `cdebe1d5c732c99b0822af251dd1a55370947c09`
- Disposition: mechanical_scope; full actual diff statically reviewed.

Removes now-invalid custom pybind11 export steps from Linux/Windows CI, Docker and both wheel build configurations. Exact follow-through to113; funchook export remains. No independent runtime behavior is inferred.

Changed-path evidence: [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/.github/workflows/ci-linux.yml) (+0/−2); [.github/workflows/ci-windows.yml](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/.github/workflows/ci-windows.yml) (+0/−1); [Dockerfile](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/Dockerfile) (+0/−1); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/pyproject.toml) (+0/−2)



<a id="commit-118"></a>
### 118. feat: update CI linux workflow to use endstone dev image {#commit-118}

- Source: [7db69b7fa4eae7bd1dddda77920aaee75f6dc56a](https://github.com/EndstoneMC/endstone/commit/7db69b7fa4eae7bd1dddda77920aaee75f6dc56a)
- Authored: 2024-01-13T00:42:34Z; parent: `35b4c6b749f0f88a5893fb8b7d2d82558aab8383`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces Ubuntu/GCC matrix with Debug/Release jobs inside ghcr.io/endstonemc/endstone-dev:latest, drops explicit compiler/Python installation, uses Ninja and changes workspace ownership in both jobs. This aligns CI with Clang/libc++ migration by delegating toolchain provisioning to the image, while reducing compiler-version coverage and introducing mutable-image reproducibility dependence. Image contents and run results were not inspected.

Changed-path evidence: [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/7db69b7fa4eae7bd1dddda77920aaee75f6dc56a/.github/workflows/ci-linux.yml) (+13/−28)



<a id="commit-119"></a>
### 119. feat: replace lcov with gcovr in code coverage workflow {#commit-119}

- Source: [c7b6e5cca49215b832d42b155f4d3918da26593b](https://github.com/EndstoneMC/endstone/commit/c7b6e5cca49215b832d42b155f4d3918da26593b)
- Authored: 2024-01-13T02:33:08Z; parent: `7db69b7fa4eae7bd1dddda77920aaee75f6dc56a`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces LCOV collection with gcovr XML using llvm-cov gcov, enables --coverage for GNU or Clang, follows Conan's build/Debug layout, and stops including the old coverage helper. This is coherent with the Clang image transition and fixes path/tool expectations. Codecov action still auto-discovers the report; upload success and coverage value were not observed. Test source coverage remains distinct from real Bedrock runtime coverage.

Changed-path evidence: [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/c7b6e5cca49215b832d42b155f4d3918da26593b/.github/workflows/ci-linux.yml) (+7/−7); [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/c7b6e5cca49215b832d42b155f4d3918da26593b/CMakeLists.txt) (+3/−4)



<a id="commit-120"></a>
### 120. refactor: remove unused cmake modules {#commit-120}

- Source: [a35acc0085db06f95ee0606b4185a1d007dfb1b9](https://github.com/EndstoneMC/endstone/commit/a35acc0085db06f95ee0606b4185a1d007dfb1b9)
- Authored: 2024-01-13T02:34:32Z; parent: `c7b6e5cca49215b832d42b155f4d3918da26593b`
- Disposition: mechanical_scope; full actual diff statically reviewed.

Deletes the now-unreferenced 747-line CodeCoverage.cmake after119. Blob7e45f7017c820ec5cd23918b713646ec473f8695 is identical to the full imported module read at29; deletion header and all-path inventory confirm the entire same file is removed with no other changes. Treat as verified exact deletion, not a fresh original algorithm or unseen content.

Changed-path evidence: [cmake/CodeCoverage.cmake](https://github.com/EndstoneMC/endstone/blob/c7b6e5cca49215b832d42b155f4d3918da26593b/cmake/CodeCoverage.cmake) (+0/−747)
