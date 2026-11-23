<!-- retrieval: {"source_ids":["public:commit:122ac38bbbd0d47d6e164da356a2f55e17917b9a","public:commit:1556f4c0b6d505b9966e84ad7c57b4c5c73f18d4","public:commit:34aeba6d7fecc9446fff93aaf27da1ad22795d41","public:commit:3b59e3e1c215a74df3b4cda93c07ea32ac9d4adc","public:commit:3eacc09a71f082dc3163ff300e01e7eafdea032f","public:commit:3fe143b11b2d904f97723055e7aec1aa95a74335","public:commit:4f0b3053a25e953d2c49c8ed683c6983153864b9","public:commit:516dab77b9c483dd1df8a6e1e1455511d8fa1fb7","public:commit:5f2d7097e6d4eb2f87a891ef904dca08d2071442","public:commit:6e88a6777bd4d9a6e570de18bec5157798d5a98d","public:commit:75d0f365875a79519b890329a2bc7aa19e457a26","public:commit:79ab886bc8a04e9f719591128d0f4aac693795e7","public:commit:7e3d47edc5dca6dc8d7ce593b9cc390b7a06a5a5","public:commit:867200392191b0af12c9d1ae4c890ae552a08d07","public:commit:8a372bc7fb2957a3bbb807556751840c63336f9a","public:commit:9cb814e9aa3c7e3e92a4cb29336eb79d45f6a57c","public:commit:9ec74d893fa3f524e2ec76d7c27bd652b475e161","public:commit:b24760a9422dfc1008385bfffe5884736a84d17e","public:commit:b3eebd69209dd9c199a497c641433c5c72e3a20d","public:commit:b95a90933d514117e036bc94ab4c3c6fe52345d1","public:commit:bf435023a2faafbc3e85a9accf299570358a93e4","public:commit:c4efe35f3e00ccc4238a243bf8d1603704ca8f77","public:commit:ca262c95338d4363f7eddbba9224a84cdc8183ec","public:commit:cb5e571e39f105830d498489adccd41fea85b857","public:commit:d8ff276fb9d84147f6d2fc68f39fb14472f12e0d","public:commit:e9e3c7cdd86f20c0e86bd36bd681cfebb129d3f7","public:commit:eb3e71991df4dad4d5c25b3f421443b756e5ff13","public:commit:ee9030a785197a2fb572aebe9127c801f89b4690","public:commit:f571691a154c5db52e0fc9cdbf7eeb888003e119","public:commit:fdfe4a577237e2462de532dcdefd5e26b53cd111"],"source_type":"public","date":"2024-01-15..2024-03-04","topics":["ffi","testing","build","performance","recovery","api","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Build, distribution, bootstrap and test boundaries {#build-distribution-bootstrap-and-test-boundaries}

## Result and historical scope {#result-and-historical-scope}

This unit continues the first120 commits, from15 January to4 March2024. The recurring problem is keeping host ABI, local CMake, Conan consumer metadata, Python wheels and Docker images in agreement. These are separate contracts. An integration change in one does not prove another is correct, and this history contains several short-lived mismatches and reversals. All conclusions below are static source findings; no build, workflow, downloaded executable or container was executed.

## Toolchain and artifact identity {#toolchain-and-artifact-identity}

121 reverses the immediately preceding development-image CI choice: Ubuntu20.04/22.04 jobs explicitly install Clang15/libc++, use checked-in Conan settings, and configure Windows MSVC/Ninja.122 replaces cibuildwheel/custom-manylinux with explicit CPython3.9–3.12 wheel jobs and Linux auditwheel repair for manylinux_2_31_x86_64. The wheel tests install built artifacts before pytest, which is a more relevant boundary than source-only import tests. However, original and repaired wheels share one directory and wildcard selection. The source does not establish which artifact was ultimately installed or whether publication succeeded. LLVM installer scripts, action versions and floating dependency inputs still need provenance review.

124 changes Docker to separate builder and clean Python3.12 slim runtime stages. This is a real reduction in what is deliberately copied into runtime, without a measured size claim. The builder clones a branch instead of consuming the triggering checkout.125 restores scheduled/tag/branch publication,126 specifies amd64,136 disables cache, and163 switches the clone from next to the default branch. Disabling cache can mitigate stale clone layers; it cannot prove that a tag-labeled image contains the tagged source. The strong reproducibility question is the resolved commit/artifact digest, not just whether a cache was disabled. The default account is nonroot but retains passwordless sudo and a fixed default credential; the credential value is intentionally absent from this research.237 changes shell output/globs, not those privilege semantics.

## Structural refactors are consumer-contract changes {#structural-refactors-are-consumer-contract-changes}

129 moves Bedrock headers into the API tree and deletes their target;130 removes dependent references left behind.163 consolidates include/src/python/tests, changes the public target alias to endstone::headers and centralizes CMake. Exact renamed blobs are reusable context, but target names, install components, package metadata and module initialization must be examined separately. In particular, the Python extension loses its generic Conan install path while retaining wheel-component installation, global Python discovery broadens to Development, and Conan core no longer explicitly requires the headers component even though CMake still does. A downstream packaged consumer is the relevant test for propagation, not merely an in-tree link.

The merge164 is not a second independent implementation. Its tree equals branch head163, first-parent patch equals163 exactly and second-parent patch is empty. That proves absence of distinct merge-result edits; it does not establish what reviewers said in PR4. GitHub is the merge committer, while the linked author is preserved separately.166 repairs Docker metadata templating introduced by163.169–173 experiment with release-event versus tag-push triggers and release creation;173 restores the167 workflow blob exactly. No motivation for the reversal or external release outcome is supplied.

## Test scope changes and a formatting counterexample {#test-scope-changes-and-a-formatting-counterexample}

131 removes the Python plugin package fixture and lifecycle assertions.145 later supplies a synthetic singleton/version test;204 removes that test while the concrete server starts depending on native objects.221 creates an interface-based TestServer instead of fake concrete Bedrock objects. That is a useful isolation boundary for native package/plugin lifecycle, but it intentionally does not validate the concrete server command map or host offsets. A passing synthetic test, if observed, would still not establish native ABI compatibility. This review observed only the test sources.

224 is a particularly important negative example. The C/Python changes resemble ordinary formatting, but GAS assembly is line-sensitive: the patch joins instructions and directives, breaks operand lists across lines and separates register/relocation tokens. The fixture CMake selects the changed x86_64 GAS file for non-MSVC builds and32-bit files for x86. This is a strong static syntax-risk finding, not a claimed observed assembler failure. A whitespace-normalized text comparison would miss the significance. Imported funchook test designs retain their upstream provenance; this commit changes formatting and should not receive blanket original-design credit.

## Installation state and recovery {#installation-state-and-recovery}

123 refuses to install into a nonempty directory lacking the platform executable. Its explicit AssertionError survives optimized Python, unlike assert statements, but also prevents recovery from some partial installations.239 addresses cross-platform collisions more structurally by adding lowercase platform subdirectories. It converts platform/executable/runtime assertions to explicit intended exceptions, so checks remain active under optimization. There is no flat-directory migration in the patch. Existing server configuration/world state may therefore remain in an old location rather than automatically following the new install path; actual migration behavior was not tested.

236 rewrites only the exact default server-name line after extraction and validation, preserving customized names, but performs a whole-file non-atomic write and assumes server.properties exists. Executable validation is not transactional installation completion. No timeout, interrupted-write, missing-properties or migration regression tests are introduced in these commits. Earlier hash checking from prior74 remains a distinct validation layer.

## Application and limits {#application-and-limits}

Use this evidence for reproducible builds, package exports, wheel/image provenance, native versus synthetic test scope, and migration/recovery reviews. Prioritize artifact-level import/link checks and host integration separately. README compiler minima, badges and installation instructions are claims and guidance, not measured compatibility. No compiler, package or delivery choice here should be generalized into an enduring personal preference; this unit explicitly records alternatives and reversals.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-121"></a>
### 121. feat: update CI workflows {#commit-121}

[ee9030a785197a2fb572aebe9127c801f89b4690](https://github.com/EndstoneMC/endstone/commit/ee9030a785197a2fb572aebe9127c801f89b4690) · 2024-01-15T14:46:24Z · meaningful

Replaces the floating development-image CI with Ubuntu20.04/22.04 plus explicitly installed Clang15/libc++ and a checked-in Conan profile, and configures MSVC/Ninja explicitly on Windows. Coverage uses the same LLVM setup; tomli becomes conditional for Python<3.11. This reverses118's image delegation while making compiler settings visible. LLVM setup script and latest CMake action remain mutable external inputs; source workflow is not evidence of passed runs.

Changed paths: `.github/conan_profiles/linux`, `.github/workflows/ci-linux.yml`, `.github/workflows/ci-windows.yml`, `pyproject.toml`.

<a id="commit-122"></a>
### 122. feat: update CD workflows {#commit-122}

[516dab77b9c483dd1df8a6e1e1455511d8fa1fb7](https://github.com/EndstoneMC/endstone/commit/516dab77b9c483dd1df8a6e1e1455511d8fa1fb7) · 2024-01-15T16:19:14Z · meaningful

Replaces cibuildwheel/custom-manylinux with separate Windows/Linux CPython3.9–3.12 jobs using pip wheel, checked-in MSVC193/Clang profiles, installed-wheel pytest and Linux auditwheel repair targeting manylinux_2_31_x86_64. Adds full sdist checkout history. Original and repaired wheels share wheelhouse and wildcard installation/upload, an artifact-selection edge needing validation. Explicit release dependency graph follows both wheel jobs. This changes Linux compatibility floor and orchestration, not merely YAML style; no actual artifact/run inspected.

Changed paths: `.github/conan_profiles/windows`, `.github/workflows/cd.yml`, `pyproject.toml`.

<a id="commit-123"></a>
### 123. feat: improve server path handling in bootstrap {#commit-123}

[122ac38bbbd0d47d6e164da356a2f55e17917b9a](https://github.com/EndstoneMC/endstone/commit/122ac38bbbd0d47d6e164da356a2f55e17917b9a) · 2024-01-15T16:41:27Z · meaningful

Refuses to install into an existing nonempty directory lacking the expected executable, with a Windows/Linux cross-use diagnostic. Prevents silently mixing installation contents but also blocks partial-install retry rather than repairing it. The check raises AssertionError explicitly, so unlike assert statements it survives optimization. Remaining changes are indentation.

Changed paths: `endstone_python/python/endstone/_internal/bootstrap/base.py`.

<a id="commit-124"></a>
### 124. feat: update Dockerfile {#commit-124}

[9ec74d893fa3f524e2ec76d7c27bd652b475e161](https://github.com/EndstoneMC/endstone/commit/9ec74d893fa3f524e2ec76d7c27bd652b475e161) · 2024-01-16T11:24:11Z · meaningful

Switches Docker from pyenv/Ubuntu to Python3.12 slim Debian base with separate compiler builder and clean runtime stage; builds/tests repaired wheels then copies only wheels into runtime. Builder clones floating next instead of using checkout content, so image tags can disagree with source revision and cached clone can go stale. Creates a nonroot account but gives passwordless sudo and a fixed default credential (value intentionally omitted), limiting security benefit. Exposes UDP ports and launches endstone. Conan now declares runtime library and removes bedrock component, but stale smart_holder/stdc++fs metadata remains. No image execution or size measurement.

Changed paths: `.github/workflows/cd.yml`, `Dockerfile`, `conanfile.py`.

<a id="commit-125"></a>
### 125. feat: add docker publish workflow {#commit-125}

[9cb814e9aa3c7e3e92a4cb29336eb79d45f6a57c](https://github.com/EndstoneMC/endstone/commit/9cb814e9aa3c7e3e92a4cb29336eb79d45f6a57c) · 2024-01-17T17:11:23Z · meaningful

Reintroduces Docker publishing in this repository after prior109 removal: nightly schedule, next pushes and version tags publish DockerHub/GHCR with metadata and GitHub Actions cache. Read secret references only, no values retained. Builder's floating branch clone means publish trigger/ref is not yet an exact content identity. Workflow source does not establish publication success.

Changed paths: `.github/workflows/docker-publish.yml`.

<a id="commit-126"></a>
### 126. feat: update docker publish workflow to specify Linux amd64 platform {#commit-126}

[f571691a154c5db52e0fc9cdbf7eeb888003e119](https://github.com/EndstoneMC/endstone/commit/f571691a154c5db52e0fc9cdbf7eeb888003e119) · 2024-01-17T17:26:24Z · small-semantic

Pins Docker build platform to linux/amd64, matching x86_64 toolchain/host constraints. One-line explicit architecture contract; no claim of multiarch support.

Changed paths: `.github/workflows/docker-publish.yml`.

<a id="commit-127"></a>
### 127. feat: update README.md {#commit-127}

[b95a90933d514117e036bc94ab4c3c6fe52345d1](https://github.com/EndstoneMC/endstone/commit/b95a90933d514117e036bc94ab4c3c6fe52345d1) · 2024-01-17T18:00:30Z · meaningful

Expands README from title into project purpose, OS/Python compatibility claims, pip/source/Docker installation and contribution/license guidance. Template link credits Best-README-Template. Source instructions omit some explicit profile/toolchain setup and Docker examples provide no persistent volume/port mapping. Minimum/recommended compiler claims are documentation, not tested compatibility evidence; later128 corrects MSVC presentation.

Changed paths: `README.md`.

<a id="commit-128"></a>
### 128. feat: update README.md {#commit-128}

[b3eebd69209dd9c199a497c641433c5c72e3a20d](https://github.com/EndstoneMC/endstone/commit/b3eebd69209dd9c199a497c641433c5c72e3a20d) · 2024-01-19T01:51:12Z · small-semantic

Separates dependency installation from pip build and documents compiler/generator/standard-library requirements in a table, with MSVC191 minimum versus193 recommended and Clang5/15 plus libc++. Changes prior README Windows minimum claim; no new validation is supplied.

Changed paths: `README.md`.

<a id="commit-136"></a>
### 136. fix: disable cache when building docker images {#commit-136}

[fdfe4a577237e2462de532dcdefd5e26b53cd111](https://github.com/EndstoneMC/endstone/commit/fdfe4a577237e2462de532dcdefd5e26b53cd111) · 2024-01-19T12:34:46Z · meaningful

Disables Docker layer cache, consistent with avoiding stale floating-branch clone content but without fixing immutable provenance. Also changes native constructor guard to include Clang and stops using main's return value as DLL attach success. Title understates runtime edits; startup exceptions still terminate in existing main path.

Changed paths: `.github/workflows/docker-publish.yml`, `endstone_runtime/src/endstone_runtime/main.cpp`.

<a id="commit-143"></a>
### 143. feat: create .gitignore for third_party directory {#commit-143}

[b24760a9422dfc1008385bfffe5884736a84d17e](https://github.com/EndstoneMC/endstone/commit/b24760a9422dfc1008385bfffe5884736a84d17e) · 2024-01-27T03:46:00Z · mechanical_scope

Adds a141-line third_party ignore list covering Conan/CMake artifacts, IDE state, Python caches/distributions, environments and miscellaneous tool outputs. Fully inspected; no algorithm or distinctive engineering preference inferred. Broad patterns can hide relevant generated artifacts, but no accidental exclusion demonstrated.

Changed paths: `third_party/.gitignore`.

<a id="commit-158"></a>
### 158. feat: disable codecov/patch {#commit-158}

[c4efe35f3e00ccc4238a243bf8d1603704ca8f77](https://github.com/EndstoneMC/endstone/commit/c4efe35f3e00ccc4238a243bf8d1603704ca8f77) · 2024-01-29T23:22:50Z · small-semantic

Adds Codecov config with project threshold1% and disables patch status. This changes coverage gate policy, not instrumentation/tests or an observed coverage outcome. Motive is not supplied; no general anti-coverage preference inferred.

Changed paths: `codecov.yml`.

<a id="commit-159"></a>
### 159. fix: typos {#commit-159}

[5f2d7097e6d4eb2f87a891ef904dca08d2071442](https://github.com/EndstoneMC/endstone/commit/5f2d7097e6d4eb2f87a891ef904dca08d2071442) · 2024-01-29T23:39:20Z · small-semantic

Adds missing UDP mapping to GHCR Docker example and corrects CLI prompt from executable is found to is not found in the missing-file branch. User-facing typo changes factual meaning; no installation algorithm change.

Changed paths: `README.md`, `endstone_python/python/endstone/_internal/bootstrap/__init__.py`.

<a id="commit-161"></a>
### 161. feat: update default options for LIEF package in conanfile {#commit-161}

[bf435023a2faafbc3e85a9accf299570358a93e4](https://github.com/EndstoneMC/endstone/commit/bf435023a2faafbc3e85a9accf299570358a93e4) · 2024-01-30T03:36:06Z · small-semantic

Disables unused LIEF formats/C API/JSON/frozen options while retaining ELF needs for Linux symbols. Reduces configured dependency feature surface; compile time and binary-size improvements are not measured.

Changed paths: `conanfile.py`.

<a id="commit-162"></a>
### 162. feat: update default options for capstone package in conanfile {#commit-162}

[1556f4c0b6d505b9966e84ad7c57b4c5c73f18d4](https://github.com/EndstoneMC/endstone/commit/1556f4c0b6d505b9966e84ad7c57b4c5c73f18d4) · 2024-01-30T03:42:50Z · small-semantic

Disables many unused capstone architectures in dependency options, leaving required x86 support and any unspecified defaults intact. Explicit architecture pruning, not proof that every unused backend is disabled or builds are faster.

Changed paths: `conanfile.py`.

<a id="commit-163"></a>
### 163. refactor: project structure {#commit-163}

[eb3e71991df4dad4d5c25b3f421443b756e5ff13](https://github.com/EndstoneMC/endstone/commit/eb3e71991df4dad4d5c25b3f421443b756e5ff13) · 2024-01-30T10:26:43Z · meaningful

Large project reorganization mostly exact renames into include/src/python/tests, verified with rename-aware diff rather than rereading9,865 no-renames lines as new work. Real changes consolidate CMake, rename API target to endstone::headers, update package/version/test paths, split coverage/build workflows, switch branch triggers to main and Docker clone to default branch. Python extension loses generic Conan install target and keeps wheel-component install; FindPython becomes broader global Development discovery. Conan core loses explicit headers component dependency despite CMake retaining it, a consumer-contract concern. Version-required check moves CMake→preprocessor. Docker metadata expression introduced here is fixed166. Full changed hunks read, including truncated20-line deleted Python CMake file reread separately.

Changed paths: `.github/workflows/cd.yml`, `.github/workflows/ci-linux.yml`, `.github/workflows/ci-windows.yml`, `.github/workflows/coverage.yml`, `.github/workflows/docker-publish.yml`, `.github/workflows/docker.yml`, `.github/workflows/linux.yml`, `.github/workflows/wheel.yml`, `.github/workflows/windows.yml`, `.gitignore`, `CMakeLists.txt`, `Dockerfile`, `conanfile.py`, `endstone_api/CMakeLists.txt`, `endstone_api/include/bedrock/bedrock.h`, `endstone_api/include/bedrock/bedrock_log.h`, `endstone_api/include/bedrock/command/command.h`, `endstone_api/include/bedrock/command/command_origin.h`, `endstone_api/include/bedrock/command/command_registry.h`, `endstone_api/include/bedrock/command/command_version.h`, `endstone_api/include/bedrock/command/stop_command.h`, `endstone_api/include/bedrock/common.h`, `endstone_api/include/bedrock/core.h`, `endstone_api/include/bedrock/server/dedicated_server.h`, `endstone_api/include/bedrock/server/server_instance.h`, `endstone_api/include/bedrock/type_id.h`, `endstone_api/include/bedrock/uuid.h`, `endstone_api/include/endstone/logger.h`, `endstone_api/include/endstone/plugin/plugin.h`, `endstone_api/include/endstone/plugin/plugin_description.h`, `endstone_api/include/endstone/plugin/plugin_loader.h`, `endstone_api/include/endstone/plugin/plugin_manager.h`, `endstone_api/include/endstone/server.h`, `endstone_core/CMakeLists.txt`, `endstone_core/include/endstone_core/endstone_server.h`, `endstone_core/include/endstone_core/logger_factory.h`, `endstone_core/include/endstone_core/plugin/cpp_plugin_loader.h`, `endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h`, `endstone_core/src/endstone_core/endstone_server.cpp`, `endstone_core/src/endstone_core/logger_factory.cpp`, `endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp`, `endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp`, `endstone_core/test/test_endstone_server.cpp`, `endstone_core/test/test_logger.cpp`, `endstone_python/.gitignore`, `endstone_python/CMakeLists.txt`, `endstone_python/include/endstone_python/endstone_python.h`, `endstone_python/python/endstone/__init__.py`, `endstone_python/python/endstone/_internal/__init__.py`, `endstone_python/python/endstone/_internal/bootstrap/__init__.py`, `endstone_python/python/endstone/_internal/bootstrap/base.py`, `endstone_python/python/endstone/_internal/bootstrap/linux.py`, `endstone_python/python/endstone/_internal/bootstrap/windows.py`, `endstone_python/python/endstone/_internal/plugin_loader.py`, `endstone_python/python/endstone/logger.py`, `endstone_python/python/endstone/logger.pyi`, `endstone_python/python/endstone/plugin.py`, `endstone_python/python/endstone/plugin.pyi`, `endstone_python/python/endstone/server.py`, `endstone_python/python/endstone/server.pyi`, `endstone_python/src/endstone_python/endstone_python.cpp`, `endstone_python/src/endstone_python/logger.cpp`, `endstone_python/src/endstone_python/plugin/plugin.cpp`, `endstone_python/src/endstone_python/plugin/plugin_description.cpp`, `endstone_python/src/endstone_python/plugin/plugin_loader.cpp`, `endstone_python/src/endstone_python/plugin/plugin_manager.cpp`, `endstone_python/src/endstone_python/server.cpp`, `endstone_python/test/test_imports.py`, `endstone_python/test/test_plugin_description.py`, `endstone_runtime/CMakeLists.txt`, `endstone_runtime/include/endstone_runtime/hook.h`, `endstone_runtime/include/endstone_runtime/platform.h`, `endstone_runtime/include/endstone_runtime/python_plugin_loader.h`, `endstone_runtime/src/bedrock/bedrock_log.cpp`, `endstone_runtime/src/bedrock/command_registry.cpp`, `endstone_runtime/src/bedrock/common.cpp`, `endstone_runtime/src/bedrock/dedicated_server.cpp`, `endstone_runtime/src/bedrock/server_instance.cpp`, `endstone_runtime/src/bedrock/stop_command.cpp`, `endstone_runtime/src/bedrock/type_id.cpp`, `endstone_runtime/src/endstone_runtime/linux/hook.cpp`, `endstone_runtime/src/endstone_runtime/linux/platform.cpp`, `endstone_runtime/src/endstone_runtime/main.cpp`, `endstone_runtime/src/endstone_runtime/python/python_plugin_loader.cpp`, `endstone_runtime/src/endstone_runtime/windows/hook.cpp`, `endstone_runtime/src/endstone_runtime/windows/platform.cpp`, `include/bedrock/bedrock.h`, `include/bedrock/bedrock_log.h`, `include/bedrock/command/command.h`, `include/bedrock/command/command_origin.h`, `include/bedrock/command/command_registry.h`, `include/bedrock/command/command_version.h`, `include/bedrock/command/stop_command.h`, `include/bedrock/common.h`, `include/bedrock/core.h`, `include/bedrock/server/dedicated_server.h`, `include/bedrock/server/server_instance.h`, `include/bedrock/type_id.h`, `include/bedrock/uuid.h`, `include/endstone/logger.h`, `include/endstone/plugin/plugin.h`, `include/endstone/plugin/plugin_description.h`, `include/endstone/plugin/plugin_loader.h`, `include/endstone/plugin/plugin_manager.h`, `include/endstone/server.h`, `include/endstone_core/endstone_server.h`, `include/endstone_core/logger_factory.h`, `include/endstone_core/plugin/cpp_plugin_loader.h`, `include/endstone_core/plugin/endstone_plugin_manager.h`, `include/endstone_python/endstone_python.h`, `include/endstone_runtime/hook.h`, `include/endstone_runtime/platform.h`, `include/endstone_runtime/python_plugin_loader.h`, `pyproject.toml`, `python/.gitignore`, `python/src/endstone/__init__.py`, `python/src/endstone/_internal/__init__.py`, `python/src/endstone/_internal/bootstrap/__init__.py`, `python/src/endstone/_internal/bootstrap/base.py`, `python/src/endstone/_internal/bootstrap/linux.py`, `python/src/endstone/_internal/bootstrap/windows.py`, `python/src/endstone/_internal/plugin_loader.py`, `python/src/endstone/logger.py`, `python/src/endstone/logger.pyi`, `python/src/endstone/plugin.py`, `python/src/endstone/plugin.pyi`, `python/src/endstone/server.py`, `python/src/endstone/server.pyi`, `python/tests/test_imports.py`, `python/tests/test_plugin_description.py`, `src/endstone_core/endstone_server.cpp`, `src/endstone_core/logger_factory.cpp`, `src/endstone_core/plugin/cpp_plugin_loader.cpp`, `src/endstone_core/plugin/endstone_plugin_manager.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/logger.cpp`, `src/endstone_python/plugin/plugin.cpp`, `src/endstone_python/plugin/plugin_description.cpp`, `src/endstone_python/plugin/plugin_loader.cpp`, `src/endstone_python/plugin/plugin_manager.cpp`, `src/endstone_python/server.cpp`, `src/endstone_runtime/bedrock/bedrock_log.cpp`, `src/endstone_runtime/bedrock/command_registry.cpp`, `src/endstone_runtime/bedrock/common.cpp`, `src/endstone_runtime/bedrock/dedicated_server.cpp`, `src/endstone_runtime/bedrock/server_instance.cpp`, `src/endstone_runtime/bedrock/stop_command.cpp`, `src/endstone_runtime/bedrock/type_id.cpp`, `src/endstone_runtime/linux/hook.cpp`, `src/endstone_runtime/linux/platform.cpp`, `src/endstone_runtime/main.cpp`, `src/endstone_runtime/python/python_plugin_loader.cpp`, `src/endstone_runtime/windows/hook.cpp`, `src/endstone_runtime/windows/platform.cpp`, `test_package/CMakeLists.txt`, `tests/test_endstone_server.cpp`, `tests/test_logger.cpp`.

<a id="commit-164"></a>
### 164. Merge pull request #4 from EndstoneMC/next {#commit-164}

[7e3d47edc5dca6dc8d7ce593b9cc390b7a06a5a5](https://github.com/EndstoneMC/endstone/commit/7e3d47edc5dca6dc8d7ce593b9cc390b7a06a5a5) · 2024-01-30T10:30:02Z · merge_verified_reuse

Merge PR4 integrates the second parent's change without additional resolution behavior. Git records the merge author separately from GitHub as committer; imported changes retain their own authorship.

Changed paths: `.github/workflows/cd.yml`, `.github/workflows/ci-linux.yml`, `.github/workflows/ci-windows.yml`, `.github/workflows/coverage.yml`, `.github/workflows/docker-publish.yml`, `.github/workflows/docker.yml`, `.github/workflows/linux.yml`, `.github/workflows/wheel.yml`, `.github/workflows/windows.yml`, `.gitignore`, `CMakeLists.txt`, `Dockerfile`, `conanfile.py`, `endstone_api/CMakeLists.txt`, `endstone_api/include/bedrock/bedrock.h`, `endstone_api/include/bedrock/bedrock_log.h`, `endstone_api/include/bedrock/command/command.h`, `endstone_api/include/bedrock/command/command_origin.h`, `endstone_api/include/bedrock/command/command_registry.h`, `endstone_api/include/bedrock/command/command_version.h`, `endstone_api/include/bedrock/command/stop_command.h`, `endstone_api/include/bedrock/common.h`, `endstone_api/include/bedrock/core.h`, `endstone_api/include/bedrock/server/dedicated_server.h`, `endstone_api/include/bedrock/server/server_instance.h`, `endstone_api/include/bedrock/type_id.h`, `endstone_api/include/bedrock/uuid.h`, `endstone_api/include/endstone/logger.h`, `endstone_api/include/endstone/plugin/plugin.h`, `endstone_api/include/endstone/plugin/plugin_description.h`, `endstone_api/include/endstone/plugin/plugin_loader.h`, `endstone_api/include/endstone/plugin/plugin_manager.h`, `endstone_api/include/endstone/server.h`, `endstone_core/CMakeLists.txt`, `endstone_core/include/endstone_core/endstone_server.h`, `endstone_core/include/endstone_core/logger_factory.h`, `endstone_core/include/endstone_core/plugin/cpp_plugin_loader.h`, `endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h`, `endstone_core/src/endstone_core/endstone_server.cpp`, `endstone_core/src/endstone_core/logger_factory.cpp`, `endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp`, `endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp`, `endstone_core/test/test_endstone_server.cpp`, `endstone_core/test/test_logger.cpp`, `endstone_python/.gitignore`, `endstone_python/CMakeLists.txt`, `endstone_python/include/endstone_python/endstone_python.h`, `endstone_python/python/endstone/__init__.py`, `endstone_python/python/endstone/_internal/__init__.py`, `endstone_python/python/endstone/_internal/bootstrap/__init__.py`, `endstone_python/python/endstone/_internal/bootstrap/base.py`, `endstone_python/python/endstone/_internal/bootstrap/linux.py`, `endstone_python/python/endstone/_internal/bootstrap/windows.py`, `endstone_python/python/endstone/_internal/plugin_loader.py`, `endstone_python/python/endstone/logger.py`, `endstone_python/python/endstone/logger.pyi`, `endstone_python/python/endstone/plugin.py`, `endstone_python/python/endstone/plugin.pyi`, `endstone_python/python/endstone/server.py`, `endstone_python/python/endstone/server.pyi`, `endstone_python/src/endstone_python/endstone_python.cpp`, `endstone_python/src/endstone_python/logger.cpp`, `endstone_python/src/endstone_python/plugin/plugin.cpp`, `endstone_python/src/endstone_python/plugin/plugin_description.cpp`, `endstone_python/src/endstone_python/plugin/plugin_loader.cpp`, `endstone_python/src/endstone_python/plugin/plugin_manager.cpp`, `endstone_python/src/endstone_python/server.cpp`, `endstone_python/test/test_imports.py`, `endstone_python/test/test_plugin_description.py`, `endstone_runtime/CMakeLists.txt`, `endstone_runtime/include/endstone_runtime/hook.h`, `endstone_runtime/include/endstone_runtime/platform.h`, `endstone_runtime/include/endstone_runtime/python_plugin_loader.h`, `endstone_runtime/src/bedrock/bedrock_log.cpp`, `endstone_runtime/src/bedrock/command_registry.cpp`, `endstone_runtime/src/bedrock/common.cpp`, `endstone_runtime/src/bedrock/dedicated_server.cpp`, `endstone_runtime/src/bedrock/server_instance.cpp`, `endstone_runtime/src/bedrock/stop_command.cpp`, `endstone_runtime/src/bedrock/type_id.cpp`, `endstone_runtime/src/endstone_runtime/linux/hook.cpp`, `endstone_runtime/src/endstone_runtime/linux/platform.cpp`, `endstone_runtime/src/endstone_runtime/main.cpp`, `endstone_runtime/src/endstone_runtime/python/python_plugin_loader.cpp`, `endstone_runtime/src/endstone_runtime/windows/hook.cpp`, `endstone_runtime/src/endstone_runtime/windows/platform.cpp`, `include/bedrock/bedrock.h`, `include/bedrock/bedrock_log.h`, `include/bedrock/command/command.h`, `include/bedrock/command/command_origin.h`, `include/bedrock/command/command_registry.h`, `include/bedrock/command/command_version.h`, `include/bedrock/command/stop_command.h`, `include/bedrock/common.h`, `include/bedrock/core.h`, `include/bedrock/server/dedicated_server.h`, `include/bedrock/server/server_instance.h`, `include/bedrock/type_id.h`, `include/bedrock/uuid.h`, `include/endstone/logger.h`, `include/endstone/plugin/plugin.h`, `include/endstone/plugin/plugin_description.h`, `include/endstone/plugin/plugin_loader.h`, `include/endstone/plugin/plugin_manager.h`, `include/endstone/server.h`, `include/endstone_core/endstone_server.h`, `include/endstone_core/logger_factory.h`, `include/endstone_core/plugin/cpp_plugin_loader.h`, `include/endstone_core/plugin/endstone_plugin_manager.h`, `include/endstone_python/endstone_python.h`, `include/endstone_runtime/hook.h`, `include/endstone_runtime/platform.h`, `include/endstone_runtime/python_plugin_loader.h`, `pyproject.toml`, `python/.gitignore`, `python/src/endstone/__init__.py`, `python/src/endstone/_internal/__init__.py`, `python/src/endstone/_internal/bootstrap/__init__.py`, `python/src/endstone/_internal/bootstrap/base.py`, `python/src/endstone/_internal/bootstrap/linux.py`, `python/src/endstone/_internal/bootstrap/windows.py`, `python/src/endstone/_internal/plugin_loader.py`, `python/src/endstone/logger.py`, `python/src/endstone/logger.pyi`, `python/src/endstone/plugin.py`, `python/src/endstone/plugin.pyi`, `python/src/endstone/server.py`, `python/src/endstone/server.pyi`, `python/tests/test_imports.py`, `python/tests/test_plugin_description.py`, `src/endstone_core/endstone_server.cpp`, `src/endstone_core/logger_factory.cpp`, `src/endstone_core/plugin/cpp_plugin_loader.cpp`, `src/endstone_core/plugin/endstone_plugin_manager.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/logger.cpp`, `src/endstone_python/plugin/plugin.cpp`, `src/endstone_python/plugin/plugin_description.cpp`, `src/endstone_python/plugin/plugin_loader.cpp`, `src/endstone_python/plugin/plugin_manager.cpp`, `src/endstone_python/server.cpp`, `src/endstone_runtime/bedrock/bedrock_log.cpp`, `src/endstone_runtime/bedrock/command_registry.cpp`, `src/endstone_runtime/bedrock/common.cpp`, `src/endstone_runtime/bedrock/dedicated_server.cpp`, `src/endstone_runtime/bedrock/server_instance.cpp`, `src/endstone_runtime/bedrock/stop_command.cpp`, `src/endstone_runtime/bedrock/type_id.cpp`, `src/endstone_runtime/linux/hook.cpp`, `src/endstone_runtime/linux/platform.cpp`, `src/endstone_runtime/main.cpp`, `src/endstone_runtime/python/python_plugin_loader.cpp`, `src/endstone_runtime/windows/hook.cpp`, `src/endstone_runtime/windows/platform.cpp`, `test_package/CMakeLists.txt`, `tests/test_endstone_server.cpp`, `tests/test_logger.cpp`.

<a id="commit-165"></a>
### 165. feat: update github workflows {#commit-165}

[8a372bc7fb2957a3bbb807556751840c63336f9a](https://github.com/EndstoneMC/endstone/commit/8a372bc7fb2957a3bbb807556751840c63336f9a) · 2024-01-30T10:30:53Z · mechanical_scope

Renames coverage workflow, Docker job and step display labels for clarity. No changed commands, permissions or trigger behavior; fully inspected concise disposition.

Changed paths: `.github/workflows/coverage.yml`, `.github/workflows/docker.yml`.

<a id="commit-166"></a>
### 166. fix: docker build, update README.md {#commit-166}

[3b59e3e1c215a74df3b4cda93c07ea32ac9d4adc](https://github.com/EndstoneMC/endstone/commit/3b59e3e1c215a74df3b4cda93c07ea32ac9d4adc) · 2024-01-30T10:37:19Z · small-semantic

Fixes Docker metadata default-branch templating by using action Handlebars expression rather than GitHub expression, and updates/adds README badges to relocated workflows. Concrete publication configuration correction; no publish success observed.

Changed paths: `.github/workflows/docker.yml`, `README.md`.

<a id="commit-167"></a>
### 167. chore: update to setup-python@v5 {#commit-167}

[34aeba6d7fecc9446fff93aaf27da1ad22795d41](https://github.com/EndstoneMC/endstone/commit/34aeba6d7fecc9446fff93aaf27da1ad22795d41) · 2024-01-30T10:41:11Z · mechanical_scope

Updates five setup-python references from v4 to v5 across coverage, native builds and both wheel jobs. Exact dependency-major update; no independent algorithm or measured outcome.

Changed paths: `.github/workflows/coverage.yml`, `.github/workflows/linux.yml`, `.github/workflows/wheel.yml`, `.github/workflows/windows.yml`.

<a id="commit-169"></a>
### 169. chore: update README.md and wheel.yml {#commit-169}

[cb5e571e39f105830d498489adccd41fea85b857](https://github.com/EndstoneMC/endstone/commit/cb5e571e39f105830d498489adccd41fea85b857) · 2024-01-30T13:39:09Z · meaningful

Changes wheel publication from tag-push to published-release event and adds PyPI badges. Existing release creation step initially remains in publish job, illustrating intertwined trigger/action semantics. Reverted through172/173; no reason or outcome recorded.

Changed paths: `.github/workflows/wheel.yml`, `README.md`.

<a id="commit-170"></a>
### 170. docs: update README.md {#commit-170}

[e9e3c7cdd86f20c0e86bd36bd681cfebb129d3f7](https://github.com/EndstoneMC/endstone/commit/e9e3c7cdd86f20c0e86bd36bd681cfebb129d3f7) · 2024-01-31T15:24:47Z · meaningful

README formatting title hides removal of GitHub-release creation from wheel publish job and removal of .github from Docker ignore patterns, allowing Conan profiles into build context. Release flow now depends on already published release until172. No externally created release observed.

Changed paths: `.dockerignore`, `.github/workflows/wheel.yml`, `README.md`.

<a id="commit-172"></a>
### 172. revert: wheel.yml {#commit-172}

[6e88a6777bd4d9a6e570de18bec5157798d5a98d](https://github.com/EndstoneMC/endstone/commit/6e88a6777bd4d9a6e570de18bec5157798d5a98d) · 2024-01-31T17:03:38Z · meaningful

Restores tag-push wheel trigger and tag-based publish condition, reverting169's release-event selection; does not yet restore release creation. Preserve partial-revert identity rather than treating title as complete file restoration.

Changed paths: `.github/workflows/wheel.yml`.

<a id="commit-173"></a>
### 173. feat: create a release on a new tag added {#commit-173}

[d8ff276fb9d84147f6d2fc68f39fb14472f12e0d](https://github.com/EndstoneMC/endstone/commit/d8ff276fb9d84147f6d2fc68f39fb14472f12e0d) · 2024-01-31T17:12:04Z · small-semantic

Restores GitHub-release creation with built artifacts before PyPI publication. Wheel workflow blob returns exactly to its167 state after169/170/172 experiments. Actual release/publish outcomes remain unobserved.

Changed paths: `.github/workflows/wheel.yml`.

<a id="commit-209"></a>
### 209. fix: test package {#commit-209}

[867200392191b0af12c9d1ae4c890ae552a08d07](https://github.com/EndstoneMC/endstone/commit/867200392191b0af12c9d1ae4c890ae552a08d07) · 2024-03-03T17:27:09Z · mechanical

Changes the package-test dummy host from DedicatedServer to ServerInstance to match206. The fixture remains synthetic and does not validate real host layout or startup timing.

Changed paths: `test_package/src/test_server.cpp`.

<a id="commit-221"></a>
### 221. fix: test package {#commit-221}

[ca262c95338d4363f7eddbba9224a84cdc8183ec](https://github.com/EndstoneMC/endstone/commit/ca262c95338d4363f7eddbba9224a84cdc8183ec) · 2024-03-03T23:21:13Z · meaningful

Replaces fake concrete Bedrock objects with a TestServer implementing only the public Server interface and native plugin loader. Keeps load/enable/disable assertions and logger smoke calls, renames the fixture plugin and moves spdlog include from logger-factory public header to implementation. This meaningfully isolates package-consumer testing from reverse-engineered host layout, while ceasing to exercise the concrete command-map/server path. Source assertions are not observed pass results.

Changed paths: `include/endstone/detail/logger_factory.h`, `src/endstone_core/logger_factory.cpp`, `test_package/CMakeLists.txt`, `test_package/src/dummy_bedrock.cpp`, `test_package/src/test_plugin.cpp`, `test_package/src/test_server.cpp`.

<a id="commit-224"></a>
### 224. style: code formatting {#commit-224}

[3eacc09a71f082dc3163ff300e01e7eafdea032f](https://github.com/EndstoneMC/endstone/commit/3eacc09a71f082dc3163ff300e01e7eafdea032f) · 2024-03-03T23:45:15Z · meaningful

The style title conceals consequential assembly changes in imported funchook test fixtures. C/Python edits are whitespace/include ordering and macro continuation formatting, but GAS .S files merge separate instructions/directives onto one line, split .p2align operands across lines, separate register/relocation tokens and concatenate section directives. Those statement-boundary changes are a strong static assembler-syntax regression risk, not verified mechanical equivalence. Full1047-line rename-aware display was read in two consecutive ranges. Test CMake selects the modified x86_64 GAS fixture on non-MSVC x86_64, and x86 variants on32-bit; no assembler execution or CI outcome was inspected. Preserve third-party fixture attribution instead of assigning original hook-test design to this formatter commit.

Changed paths: `third_party/funchook/conanfile.py`, `third_party/funchook/test_package/libfunchook_test.c`, `third_party/funchook/test_package/libfunchook_test_noasm.c`, `third_party/funchook/test_package/libfunchook_test_x86_64_gas.S`, `third_party/funchook/test_package/libfunchook_test_x86_gas.S`, `third_party/funchook/test_package/test_main.c`, `third_party/funchook/test_package/x86_test.S`.

<a id="commit-236"></a>
### 236. feat: update server name in properties file {#commit-236}

[75d0f365875a79519b890329a2bc7aa19e457a26](https://github.com/EndstoneMC/endstone/commit/75d0f365875a79519b890329a2bc7aa19e457a26) · 2024-03-04T17:35:39Z · meaningful

After extraction and validation, rewrites server.properties to brand only a line whose stripped text exactly equals the default server name. Preserves customized names but rewrites the whole file non-atomically and assumes it exists; a missing file or interrupted write can fail after executable validation. This occurs in installation, not every startup; no migration or failure test is added.

Changed paths: `python/src/endstone/_internal/bootstrap/base.py`.

<a id="commit-237"></a>
### 237. refactor: replace echo commands with printf in Dockerfile {#commit-237}

[4f0b3053a25e953d2c49c8ed683c6983153864b9](https://github.com/EndstoneMC/endstone/commit/4f0b3053a25e953d2c49c8ed683c6983153864b9) · 2024-03-04T18:00:19Z · meaningful

Replaces Docker echo with printf and prefixes wheel globs with ./, reducing echo escape ambiguity and leading-dash filename interpretation. Fixed default account credential and passwordless sudo remain; credential value is deliberately omitted from research artifacts. printf credential input lacks the former newline, which merits environment validation; no image build was run. This is a small shell robustness change, not a security hardening claim.

Changed paths: `Dockerfile`.

<a id="commit-238"></a>
### 238. docs: update README.md {#commit-238}

[79ab886bc8a04e9f719591128d0f4aac693795e7](https://github.com/EndstoneMC/endstone/commit/79ab886bc8a04e9f719591128d0f4aac693795e7) · 2024-03-04T18:20:52Z · mechanical

README points logo to releases, consolidates badges, fixes introduction typo and adds endstone startup after installation commands. Static Python3 badge is less precise than package-supported-version metadata. Documentation changes do not prove wheel compatibility, build status or installation success.

Changed paths: `README.md`.

<a id="commit-239"></a>
### 239. refactor: bedrock server installation path {#commit-239}

[3fe143b11b2d904f97723055e7aec1aa95a74335](https://github.com/EndstoneMC/endstone/commit/3fe143b11b2d904f97723055e7aec1aa95a74335) · 2024-03-04T20:21:51Z · meaningful

Separates installation directories under lowercase linux/windows subdirectories, directly addressing123 cross-platform collision, and replaces platform/executable/runtime assert checks with explicit NotImplementedError/FileNotFoundError. Validation now survives Python optimization and raises the intended exception type. Existing flat installations are not migrated in the patch; new paths may download fresh state. Hash checks were already explicit in prior74. No installation migration/recovery test is added.

Changed paths: `python/src/endstone/_internal/bootstrap/base.py`, `python/src/endstone/_internal/bootstrap/linux.py`, `python/src/endstone/_internal/bootstrap/windows.py`.
