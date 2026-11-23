<!-- retrieval: {"source_ids":["public:commit:01a3ac66f0aa74aa60be0d70bf655fbd65334556","public:commit:0e45bfe4f6768c1e73c5fb2e5307c2be9b26bb93","public:commit:15f5c32373e49c8e88ad9651c85fba90b503dac1","public:commit:17ba20a0e0165aeedafa7d66d8e1f4653d2f7a50","public:commit:24eb37dc1f9d65552b90fca67edb5e979b988aee","public:commit:278f3fd6f73b7bf50a83ca723a55ebae860147b3","public:commit:2bbfc63bb4e30341be202ce44d5b2a6d39d2423f","public:commit:3c4093b8295ae4ab4112bdac0f9bcbba78a3b7bd","public:commit:40c9cfcbb33ca22d2b2e584932f758cef8fbc5cf","public:commit:4db5fc4b689d9b606818533f44c1d6f16d366bff","public:commit:543d25d01ebf53ec90c32aac4e4970231ebb386c","public:commit:5e020f61040e49b10ba16322c68a7b56bff830aa","public:commit:78371343bec5426d0f6aca53b2c2ad0c76044af6","public:commit:7fa08d43787d5f08ec0c1102678328e1b26be96b","public:commit:7fa8eeaf3067a8a974791b66e6f0caedd7c2d320","public:commit:817a5588be1c3f4f18f348b7f0257068ef3fb8cb","public:commit:83cb5e4d995b80d7a7e8bac6b6ff4db70ebccb3c","public:commit:9821ee56fd2296edbc15fc270be8015a8d627854","public:commit:9ab7696bb0c88e5f0af8507b97ee053514780947","public:commit:9c18251f17bb8631c1d1442998220bae78e4fc4a","public:commit:a5547b26cf3f3e7664e312af9bc36aae38e95e1a","public:commit:b5603f7aef5bb0cd3753b961d3371f6c2db27ef9","public:commit:b6a78473aef733d02aa99fe960ea3ffee6e52486","public:commit:baac973ac93dc49a175ff581fd94476ee348d421","public:commit:c48e5a7475e0f157eb32baad6f5a1129f9ba3f6e","public:commit:c5f58c80946ae32114603e809d27e7bbb505e41d","public:commit:c860482003f85f6a49ce708fab60aa778a7da049","public:commit:c95504e878ac2d3af056b2c8532d651b63b39916","public:commit:dc44a7270dcbc43827729d2e380e9fb1ad224de4","public:commit:de24e91ef5fd3aeb999e0e482ce18c0cb53352a0","public:commit:e0842114940fd95ee1d452db0a0004a1e0621b63","public:commit:fc32f262696c89cab6ad667ee388061c69e0edc7","public:context-commit:73d1df1b6df52bb9eaa0f49841e541dffcb3c603"],"source_type":"public","date":"2024-10-22..2024-12-18","topics":["ffi","testing","build","performance","api","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Build boundaries, release metadata and bounded mechanical dispositions {#build-boundaries-release-metadata-and-bounded-mechanical-dispositions}

## Build migration with repairs and reversals {#build-migration-with-repairs-and-reversals}

1946 moves EnTT from a pinned source revision into Conan3.14.0.1948 consolidates CI into an OS/build-type matrix, but missing platform guards are corrected1949.1950 switches core Python linkage toward module-only;1980 restores embedding support when Python's own module build is split out. Treat the endpoint and reversal as evidence, rather than extracting a preference from the short-lived intermediate.

1951/1952 move wheel building to cibuildwheel, configure CPython variants, custom manylinux images and test commands.1953 restores MSVC/CMake/Ninja setup and fail-fast:false.1966 pins ubuntu22.04/windows2019 after “latest” runners, and1981 uses a custom manylinux2_31 image after2_28. These are explicit toolchain choices, not evidence that the custom image contents were audited or binaries tested here. The image and external registries remain opaque.1968 imports a Dependabot cibuildwheel update; the dependency change remains attributable to Dependabot.

1969 and1980 replace glob-based core/Python source inclusion with explicit lists and module-local package discovery.2006 does the same for runtime and moves funchook from a local Conan recipe to FetchContent of kubo/funchook tagv1.1.3, static library and capstone. Migration is incomplete until2008 removes its Conan requirement,2009 restores UNIX libelf discovery and2011 removes its Conan runtime-component requirement. A tag name is not immutable content provenance. FetchContent was read, never run; no upstream code was installed or executed.

## Documentation and governance {#documentation-and-governance}

1934 documents architecture boundaries between header API, bindings, core, runtime hooks and devtools.1936/1962 describe and then repair Conan build commands.1935 adapts Contributor Covenant2.1 and retains external template attribution; adopted text is not evidence the author independently originated its principles.1933 colors,1954/1989 badges,1961 archive substitution and1963 ignores have concise per-SHA dispositions rather than being inflated into engineering preferences.1955 extends stale/close grace periods; this is a meaningful automation policy setting but supplies no evidence of its real effects.

Release notes at1931/1932/2005 report compatibility and features. Numeric macro/API version, changelog headings and public support claims are distinct facts. They do not prove a tag was published, CI passed, a server booted or the source was regression-free. The first owner ends at2040; the tail dossier traces0.5.7/0.5.7.1 and its migration repair without entering2025.

## Verification boundaries {#verification-boundaries}

No package install, network dependency fetch, test runner, build or native binary was executed. Workflow test commands and changed test source are evidence of configured/intended checks only. Small file moves were reviewed in no-renames form, including both deleted and added sides. The local blob-hash ledger is not distributed; the linked public commits provide accessible source changes. No title-only mechanical classification is used.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-1921"></a>
### Commit 1921 {#commit-1921}

83cb5e4d995b80d7a7e8bac6b6ff4db70ebccb3c · 2024-10-22T15:51:40Z

[docs: fix typos in CHANGELOG.md](https://github.com/EndstoneMC/endstone/commit/83cb5e4d995b80d7a7e8bac6b6ff4db70ebccb3c)


Corrects release-note Actor tag API names to addScoreboardTag/removeScoreboardTag; no implementation change.

Static review only; no upstream execution.

<a id="commit-1931"></a>
### Commit 1931 {#commit-1931}

0e45bfe4f6768c1e73c5fb2e5307c2be9b26bb93 · 2024-10-25T12:10:55Z

[docs: update README.md and CHANGELOG.md](https://github.com/EndstoneMC/endstone/commit/0e45bfe4f6768c1e73c5fb2e5307c2be9b26bb93)


README/changelog announce1.21.40/41 compatibility; no executed evidence.

Static review only; no upstream execution.

<a id="commit-1932"></a>
### Commit 1932 {#commit-1932}

17ba20a0e0165aeedafa7d66d8e1f4653d2f7a50 · 2024-10-26T08:06:26Z

[chore: release v0.5.5](https://github.com/EndstoneMC/endstone/commit/17ba20a0e0165aeedafa7d66d8e1f4653d2f7a50)


Publishes0.5.5 dated2024-10-26, opens0.5.6 section, increments patch while API stays0.5; support wording becomes1.21.40.

Static review only; no upstream execution.

<a id="commit-1933"></a>
### Commit 1933 {#commit-1933}

4db5fc4b689d9b606818533f44c1d6f16d366bff · 2024-10-27T09:55:26Z

[docs: fix icon color](https://github.com/EndstoneMC/endstone/commit/4db5fc4b689d9b606818533f44c1d6f16d366bff)


Uses theme footer foreground variable instead of hardcoded white for Discord announcement link.

Static review only; no upstream execution.

<a id="commit-1934"></a>
### Commit 1934 {#commit-1934}

3c4093b8295ae4ab4112bdac0f9bcbba78a3b7bd · 2024-10-27T12:29:36Z

[docs: add documentation about the project structure](https://github.com/EndstoneMC/endstone/commit/3c4093b8295ae4ab4112bdac0f9bcbba78a3b7bd)


Documents header-only API, Python bindings, core implementation, binary-hook runtime, Windows/OpenGL devtools and Python packaging; useful explicit boundary rationale, not proof version independence is achieved.

Static review only; no upstream execution.

<a id="commit-1935"></a>
### Commit 1935 {#commit-1935}

15f5c32373e49c8e88ad9651c85fba90b503dac1 · 2024-10-27T12:31:58Z

[docs: add Code of Conduct](https://github.com/EndstoneMC/endstone/commit/15f5c32373e49c8e88ad9651c85fba90b503dac1)


Adds Contributor Covenant2.1-derived conduct/enforcement text with project reporting address; preserve external template attribution, no original target engineering mechanism inferred.

Static review only; no upstream execution.

<a id="commit-1936"></a>
### Commit 1936 {#commit-1936}

e0842114940fd95ee1d452db0a0004a1e0621b63 · 2024-10-27T13:11:33Z

[docs: add contributing guides](https://github.com/EndstoneMC/endstone/commit/e0842114940fd95ee1d452db0a0004a1e0621b63)


Documents Conan2 setup, local funchook recipe, per-platform C++17/libc++ flags, virtual build environment, CMake presets, pip installation and MkDocs. Commands read only, not executed; typo conan detect profile is corrected1962.

Static review only; no upstream execution.

<a id="commit-1946"></a>
### Commit 1946 {#commit-1946}

9ab7696bb0c88e5f0af8507b97ee053514780947 · 2024-11-02T11:02:27Z

[chore: update entt to 3.14.0](https://github.com/EndstoneMC/endstone/commit/9ab7696bb0c88e5f0af8507b97ee053514780947)


Replaces pinned EnTT source snapshot FetchContent with Conan EnTT3.14.0 and find_package; packaging mechanism changes, external library not reviewed.

Static review only; no upstream execution.

<a id="commit-1948"></a>
### Commit 1948 {#commit-1948}

a5547b26cf3f3e7664e312af9bc36aae38e95e1a · 2024-11-05T16:32:00Z

[ci: consolidate workflows into a single CI pipeline](https://github.com/EndstoneMC/endstone/commit/a5547b26cf3f3e7664e312af9bc36aae38e95e1a)


Combines Linux/Windows CI into build-type matrix, Python3.12 and latest OS runners, reducing previous explicit OS variants. Initial Windows build step lacks OS guard and Linux compiler env is scoped only build;1949 repairs conditional/env setup. Source workflow only, no run observed.

Static review only; no upstream execution.

<a id="commit-1949"></a>
### Commit 1949 {#commit-1949}

817a5588be1c3f4f18f348b7f0257068ef3fb8cb · 2024-11-05T16:43:18Z

[ci: improve checks for OS](https://github.com/EndstoneMC/endstone/commit/817a5588be1c3f4f18f348b7f0257068ef3fb8cb)


Uses runner.os instead of matrix label checks, persists Linux CC/CXX before Conan profile detection and adds missing Windows-only guard. Repairs1948 cross-platform branch leakage.

Static review only; no upstream execution.

<a id="commit-1950"></a>
### Commit 1950 {#commit-1950}

24eb37dc1f9d65552b90fca67edb5e979b988aee · 2024-11-06T15:59:13Z

[chore: update CMakeLists.txt](https://github.com/EndstoneMC/endstone/commit/24eb37dc1f9d65552b90fca67edb5e979b988aee)


Project declares CXX only, requests Python Development.Module and links pybind11::module instead of embed; avoids requiring embedding development target for extension-oriented build. Not tested here.

Static review only; no upstream execution.

<a id="commit-1951"></a>
### Commit 1951 {#commit-1951}

278f3fd6f73b7bf50a83ca723a55ebae860147b3 · 2024-11-06T16:01:53Z

[chore: add configuration for cibuildwheel](https://github.com/EndstoneMC/endstone/commit/278f3fd6f73b7bf50a83ca723a55ebae860147b3)


Adds cibuildwheel CPython-only policy, pytest command/requirements, custom manylinux2_28 image and Clang15/libc++ installation. Tests are configured not executed; workflow setup repaired1953.

Static review only; no upstream execution.

<a id="commit-1952"></a>
### Commit 1952 {#commit-1952}

7fa8eeaf3067a8a974791b66e6f0caedd7c2d320 · 2024-11-06T16:10:28Z

[ci: use cibuildwheel to build endstone wheels](https://github.com/EndstoneMC/endstone/commit/7fa8eeaf3067a8a974791b66e6f0caedd7c2d320)


Replaces separate manual Windows/Linux wheel build/repair/test jobs with cibuildwheel2.21.3 matrix cp39-cp313 and platform tags, uploads wheelhouse, rewires publish dependency. Explicit auditwheel manylinux2_31 step disappears in favor of cibuildwheel policy; no build/publish executed.

Static review only; no upstream execution.

<a id="commit-1953"></a>
### Commit 1953 {#commit-1953}

de24e91ef5fd3aeb999e0e482ce18c0cb53352a0 · 2024-11-06T16:19:41Z

[ci: fix the new cibuildwheel workflow](https://github.com/EndstoneMC/endstone/commit/de24e91ef5fd3aeb999e0e482ce18c0cb53352a0)


Restores fail-fast:false, Windows MSVC setup, CMake/Ninja setup and verbose build logs in new cibuildwheel pipeline. Does not change Linux before-all commands.

Static review only; no upstream execution.

<a id="commit-1954"></a>
### Commit 1954 {#commit-1954}

7fa08d43787d5f08ec0c1102678328e1b26be96b · 2024-11-06T16:30:26Z

[docs: fix the badges in README.md](https://github.com/EndstoneMC/endstone/commit/7fa08d43787d5f08ec0c1102678328e1b26be96b)


README badges follow consolidated ci.yml rather than deleted OS workflows.

Static review only; no upstream execution.

<a id="commit-1955"></a>
### Commit 1955 {#commit-1955}

40c9cfcbb33ca22d2b2e584932f758cef8fbc5cf · 2024-11-06T16:34:34Z

[ci: update stale action config](https://github.com/EndstoneMC/endstone/commit/40c9cfcbb33ca22d2b2e584932f758cef8fbc5cf)


Extends stale grace from30 to60 days and close interval7 to15, updating messages. Recorded project workflow policy, no generalized personal preference.

Static review only; no upstream execution.

<a id="commit-1959"></a>
### Commit 1959 {#commit-1959}

b5603f7aef5bb0cd3753b961d3371f6c2db27ef9 · 2024-11-07T16:42:17Z

[chore: working on v0.5.6 now](https://github.com/EndstoneMC/endstone/commit/b5603f7aef5bb0cd3753b961d3371f6c2db27ef9)


Advances development patch macro to0.5.6; API version remains0.5.

Static review only; no upstream execution.

<a id="commit-1961"></a>
### Commit 1961 {#commit-1961}

fc32f262696c89cab6ad667ee388061c69e0edc7 · 2024-11-17T14:58:10Z

[feat: add .gitattributes](https://github.com/EndstoneMC/endstone/commit/fc32f262696c89cab6ad667ee388061c69e0edc7)


Marks .git_archival.txt export-subst for archive metadata expansion; no independent engineering lesson.

Static review only; no upstream execution.

<a id="commit-1962"></a>
### Commit 1962 {#commit-1962}

baac973ac93dc49a175ff581fd94476ee348d421 · 2024-11-17T15:00:13Z

[docs: fix typos in CONTRIBUTING.md](https://github.com/EndstoneMC/endstone/commit/baac973ac93dc49a175ff581fd94476ee348d421)


Corrects conan profile detect order and removes activation precondition from pip local install instructions; no build run validates instructions.

Static review only; no upstream execution.

<a id="commit-1963"></a>
### Commit 1963 {#commit-1963}

5e020f61040e49b10ba16322c68a7b56bff830aa · 2024-11-17T15:05:52Z

[chore: add dist/ directory to .gitignore](https://github.com/EndstoneMC/endstone/commit/5e020f61040e49b10ba16322c68a7b56bff830aa)


Adds dist/* to gitignore only.

Static review only; no upstream execution.

<a id="commit-1966"></a>
### Commit 1966 {#commit-1966}

9c18251f17bb8631c1d1442998220bae78e4fc4a · 2024-11-21T15:45:27Z

[ci: freeze runner os version](https://github.com/EndstoneMC/endstone/commit/9c18251f17bb8631c1d1442998220bae78e4fc4a)


Pins CI and wheel runners to ubuntu22.04/windows2019, reversing1948/1952 latest-runner adoption. No explicit failure reason or measured stability result in message.

Static review only; no upstream execution.

<a id="commit-1968"></a>

### Commit 1968 {#commit-1968}

Dated review note (2026-10-20): this merge combines the [Dependabot update](https://github.com/EndstoneMC/endstone/commit/73d1df1b6df52bb9eaa0f49841e541dffcb3c603) with commit 1967; the merge adds no further content beyond those changes. The dependency update remains attributed to Dependabot. This is static source evidence, not an upstream build, test or runtime result.

c48e5a7475e0f157eb32baad6f5a1129f9ba3f6e · 2024-11-26T20:27:12Z

[Merge remote-tracking branch 'origin/main'](https://github.com/EndstoneMC/endstone/commit/c48e5a7475e0f157eb32baad6f5a1129f9ba3f6e)


All-parent delta: first parent imports cibuildwheel2.21.3-to2.22.0; second parent byte-identical canonical patch to1967 compatibility update. Need collaborator/merge context audit before completion; no transferred authorship.

Static review only; no upstream execution.

<a id="commit-1969"></a>
### Commit 1969 {#commit-1969}

2bbfc63bb4e30341be202ce44d5b2a6d39d2423f · 2024-11-26T20:33:45Z

[refactor: add CMakeLists.txt to make `endstone_core` module self-contained](https://github.com/EndstoneMC/endstone/commit/2bbfc63bb4e30341be202ce44d5b2a6d39d2423f)


Moves core build definition into src/endstone_core/CMakeLists with explicit source enumeration and local dependency discovery, retaining linkage/install/Unix flags. Meaningful change from recursive glob to maintained source list; each later source addition must update this list.

Static review only; no upstream execution.

<a id="commit-1980"></a>
### Commit 1980 {#commit-1980}

543d25d01ebf53ec90c32aac4e4970231ebb386c · 2024-11-28T20:38:52Z

[refactor: add CMakeLists.txt to make `endstone_python` module self-contained](https://github.com/EndstoneMC/endstone/commit/543d25d01ebf53ec90c32aac4e4970231ebb386c)


Creates self-contained Python module CMake with explicit source list and local strip action. Core returns to full Python Development and pybind11::embed, reversing1950 for embedding while extension retains Development.Module. Distinguishes core embedding from module linkage.

Static review only; no upstream execution.

<a id="commit-1981"></a>
### Commit 1981 {#commit-1981}

78371343bec5426d0f6aca53b2c2ad0c76044af6 · 2024-11-28T20:39:17Z

[chore: update manylinux image for cibuildwheel](https://github.com/EndstoneMC/endstone/commit/78371343bec5426d0f6aca53b2c2ad0c76044af6)


Changes custom manylinux image from2_28 to ghcr.io/endstonemc/manylinux_2_31_x86_64; runtime platform baseline changes, image internals not inspected.

Static review only; no upstream execution.

<a id="commit-1989"></a>
### Commit 1989 {#commit-1989}

c5f58c80946ae32114603e809d27e7bbb505e41d · 2024-12-03T15:09:01Z

[docs: update README.md](https://github.com/EndstoneMC/endstone/commit/c5f58c80946ae32114603e809d27e7bbb505e41d)


README Minecraft badge updated1.21.44 only.

Static review only; no upstream execution.

<a id="commit-2005"></a>
### Commit 2005 {#commit-2005}

c860482003f85f6a49ce708fab60aa778a7da049 · 2024-12-06T07:58:46Z

[docs: update CHANGELOG.md](https://github.com/EndstoneMC/endstone/commit/c860482003f85f6a49ce708fab60aa778a7da049)


Declares0.5.6 release and1.21.50 support with inventory, ban, plugin-loader and mixed-pack changelog; source-reported release evidence only. Opens0.5.7 heading, no executed release validation.

Static review only; no upstream execution.

<a id="commit-2006"></a>
### Commit 2006 {#commit-2006}

01a3ac66f0aa74aa60be0d70bf655fbd65334556 · 2024-12-06T11:15:17Z

[deps: switch to FetchContent for funchook](https://github.com/EndstoneMC/endstone/commit/01a3ac66f0aa74aa60be0d70bf655fbd65334556)


Moves runtime to explicit per-module source list and fetches upstream funchook tagv1.1.3 with static build/capstone via FetchContent; removes Conan export steps but leaves dependency/component references repaired2008/2011 and missing libelf discovery repaired2009. Tag pin is not immutable commit provenance; no fetch/build executed.

Static review only; no upstream execution.

<a id="commit-2008"></a>
### Commit 2008 {#commit-2008}

dc44a7270dcbc43827729d2e380e9fb1ad224de4 · 2024-12-06T15:48:17Z

[fix: remove funchook in conanfile.py](https://github.com/EndstoneMC/endstone/commit/dc44a7270dcbc43827729d2e380e9fb1ad224de4)


Comments out funchook requirement after FetchContent migration; runtime component dependency still requires follow-up2011.

Static review only; no upstream execution.

<a id="commit-2009"></a>
### Commit 2009 {#commit-2009}

c95504e878ac2d3af056b2c8532d651b63b39916 · 2024-12-06T15:54:45Z

[fix: add missing dependencies in CMakeLists.txt](https://github.com/EndstoneMC/endstone/commit/c95504e878ac2d3af056b2c8532d651b63b39916)


Restores UNIX libelf find_package in new runtime subdirectory after top-level package removal2006.

Static review only; no upstream execution.

<a id="commit-2011"></a>
### Commit 2011 {#commit-2011}

b6a78473aef733d02aa99fe960ea3ffee6e52486 · 2024-12-06T18:33:02Z

[fix: remove funchook from conanfile.py](https://github.com/EndstoneMC/endstone/commit/b6a78473aef733d02aa99fe960ea3ffee6e52486)


Removes funchook from Conan runtime component requirements, completing dependency bookkeeping after2006/2008.

Static review only; no upstream execution.

<a id="commit-2018"></a>
### Commit 2018 {#commit-2018}

9821ee56fd2296edbc15fc270be8015a8d627854 · 2024-12-18T21:39:39Z

[chore(deps): bump scikit-build-core-conan version in pyproject.toml](https://github.com/EndstoneMC/endstone/commit/9821ee56fd2296edbc15fc270be8015a8d627854)


Sets scikit-build-core-conan minimum0.5.3 instead of unconstrained package; not runtime code or proof of reproducible dependency resolution.

Static review only; no upstream execution.
