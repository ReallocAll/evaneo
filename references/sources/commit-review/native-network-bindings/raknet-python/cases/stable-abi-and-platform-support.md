<!-- retrieval: {"source_ids":["public:commit:3a541082e0ad36d347af2a96870dba4ea72f422b","public:commit:4fe0d3543a21c4942cd63bee1ebf9c3affaaf55a","public:commit:84b88dd8a126ca58df927763978d065922cda440","public:commit:98f20d3b048d93305830e2defe77c96302516fa8","public:commit:aa01145289b1321b3c1a5a63c28296c75218ef62","public:commit:b32fc4a90988352d6125b7e05a98428e660af508","public:commit:c6fad7adb13d0fee79ca7369c6a79a06d8431dfa","public:commit:ca51230a22d5e452fce89943d57f79bfaec07475","public:commit:da8773b5a350f45fe5679d2ce28fb004fbeb6182","public:commit:e841b6a61f97c1f52ecdfec6a40dac5eb1713657","public:commit:f7b722042628d1f70e79dc89b4fa3349dc5e4376"],"source_type":"public","date":"2026-07-27","topics":["concurrency","ffi","build","performance","api","diagnosis","documentation","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="rp01-a-stable-python-abi-is-only-one-dimension-of-native-package-support"></a>
# A stable Python ABI is only one dimension of native package support {#rp01-a-stable-python-abi-is-only-one-dimension-of-native-package-support}

## Build shape and scope {#build-shape-and-scope}

The empty root is followed by a Conan-Py-Build/CMake/nanobind scaffold around a static RakNet dependency. The initial Python minimum is3.9; the next commit changes it to3.12 and selects nanobind STABLE_ABI, Development.SABIModule and cp312-abi3 tagging. A C++17 build profile is packaged with the sdist. Generated native stubs and py.typed follow the extension target, reducing the need to maintain a separate handwritten typing declaration.

These choices describe the intended Python extension ABI. They do not establish that every native RakNet ABI, C++ standard-library ABI, operating system or threading environment is compatible. The underlying transport remains third-party RakNet; the wrapper's author should receive credit for integration and API decisions, not the inherited transport implementation.

The recorded uv.lock is only a tiny editable-package lock. It does not freeze Conan, nanobind or the native dependency closure, and its development version remains when the package becomes0.4.0. Reproducibility claims therefore require more than pointing to the presence of a lockfile.

## CI and publication as definitions {#ci-and-publication-as-definitions}

The build workflow defines lint plus Linux and Windows2022 cibuildwheel jobs, a cp312 build selector, wheel-test pytest execution and sdist creation. It adds an Endstone Conan remote before building. The release workflow checks a v-prefixed tag against pyproject's version, waits for build/version checks, publishes to PyPI through OIDC and then creates a GitHub release. Permissions default to read and are expanded for relevant jobs. Later lint work pins Ruff0.16.0 and excludes Markdown from formatting.

This review inspected the YAML and package metadata. It did not execute a workflow, inspect successful action logs, download/load a wheel, publish a package or verify binary compatibility on Windows. README distribution claims remain upstream claims. The title “production-grade” does not supersede the package's retained Alpha classifier or establish an operational readiness result.

## A platform experiment is reversed by a native constraint {#a-platform-experiment-is-reversed-by-a-native-constraint}

Commit024 changes the dependency to raknet/4.081-mojang and documents a BDS ABI motivation on Windows/Linux x64. It selects auto64 and briefly enables a musllinux image. Commit025 then skips musllinux and removes that override. The source explanation says RakNet overflows musl's128KB non-main-thread stack and segfaults. No crash log, stack trace, reproducer or native patch is included in the change, so the diagnosis is explicitly author-documented rather than independently demonstrated.

The useful engineering chain is not “add all wheel platforms.” It is: choose a native variant for a concrete integration requirement; attempt an additional platform; narrow the advertised support matrix when a low-level constraint remains unresolved. A stable CPython ABI does not solve thread-stack sizing. Conversely, this narrow failure does not establish a general anti-musl policy.

Do not equate the Conan package4.081-mojang with the separately reviewed wu-vincent/RakNet modernization fork. The names and provenance are different, and this task did not compare their compiled objects or ABI layouts. That distinction matters when borrowing a build fix from one repository for another.

## Reuse guidance and costs {#reuse-guidance-and-costs}

For a new native binding, enumerate Python version/tag, native dependency variant, C++ toolchain/runtime, CPU/OS and thread model as separate support dimensions. Generate stubs with the extension if their lifecycle is coupled. Treat CI configuration as a proposed validation process until actual results are available. Prefer a smaller truthful wheel matrix to an unverified broader one, and preserve the exact reason and evidence quality for exclusions so future maintainers know what would justify reopening them.

Sources: dossiers001–004,020–026 and their complete guarded diffs/messages. Build and release results were not executed or independently confirmed. No external source was substituted for missing platform evidence.

## Exact commit navigation {#exact-commit-navigation}

- [001 98f20d3b048d: Initial commit](../dossiers/001-98f20d3b048d.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/98f20d3b048d93305830e2defe77c96302516fa8)
- [002 ca51230a22d5: build: set up conan-py-build with nanobind and raknet](../dossiers/002-ca51230a22d5.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/ca51230a22d5e452fce89943d57f79bfaec07475)
- [003 e841b6a61f97: build: target the nanobind stable ABI (cp312-abi3)](../dossiers/003-e841b6a61f97.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/e841b6a61f97c1f52ecdfec6a40dac5eb1713657)
- [004 aa01145289b1: build: generate typing stubs with nanobind_add_stub](../dossiers/004-aa01145289b1.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/aa01145289b1321b3c1a5a63c28296c75218ef62)
- [020 da8773b5a350: docs: write a production-grade README](../dossiers/020-da8773b5a350.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/da8773b5a350f45fe5679d2ce28fb004fbeb6182)
- [021 b32fc4a90988: build: add uv.lock](../dossiers/021-b32fc4a90988.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/b32fc4a90988352d6125b7e05a98428e660af508)
- [022 84b88dd8a126: ci: build and release wheels with cibuildwheel](../dossiers/022-84b88dd8a126.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/84b88dd8a126ca58df927763978d065922cda440)
- [023 c6fad7adb13d: chore: refine package description and keywords](../dossiers/023-c6fad7adb13d.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/c6fad7adb13d0fee79ca7369c6a79a06d8431dfa)
- [024 3a541082e0ad: build: link against raknet/4.081-mojang and cover musllinux](../dossiers/024-3a541082e0ad.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/3a541082e0ad36d347af2a96870dba4ea72f422b)
- [025 4fe0d3543a21: ci: skip musllinux and 32-bit, pin lint ruleset, update URLs to EndstoneMC](../dossiers/025-4fe0d3543a21.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/4fe0d3543a21c4942cd63bee1ebf9c3affaaf55a)
- [026 f7b722042628: ci: pin ruff and exclude markdown from formatting](../dossiers/026-f7b722042628.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/f7b722042628d1f70e79dc89b4fa3349dc5e4376)
