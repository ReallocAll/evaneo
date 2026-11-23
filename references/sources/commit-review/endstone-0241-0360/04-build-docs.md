<!-- retrieval: {"source_ids":["public:commit:014cfb9fc5ee8d60b7a44d510e9338372cc1dd60","public:commit:071b788b51610c9ac0ae1adb2259c05b108feb36","public:commit:110b00c5cd2a75b4d8ec8295711a57d14de2bb78","public:commit:1ea6e9d29f343ca40a90b078733ed543bcec4b14","public:commit:2eb5782db7a6eccbf8de798cbc88e9b18f647c33","public:commit:3330217dc8cd1a8d177b692fafea5ab7024b16dd","public:commit:349f0abf9ec0b13f5045d01c87a6ac64f8af9e2c","public:commit:42bcdcd60cca923a1c7ceae20aaa590d0689a039","public:commit:4aafb09d0c1e620ca41f9dcce0f712032564b369","public:commit:53de1d91ffcd2dcfca1789c63c8ab74e9b69d824","public:commit:58d0d14052fe309515cab3f30184b201446ec717","public:commit:5c89e7266bd3f8388621b5be8d1df8ba8b19619a","public:commit:61b3b00f1e7991d2ba2d6e430e83401e4c166acd","public:commit:642d781effc39138e1e5897d494ba7899dea0379","public:commit:783d1a8cb9eec8a49b0a97d8bf1ff8176ddff210","public:commit:79b7386f7a8c48524247cdce21d2e662a718d3e6","public:commit:8ffb0bcb9bafdbef14d5680a861dca76a2abe9a4","public:commit:9838b4a82e0d37c34f655b4e477888931ccb667b","public:commit:9e29c533592e886052c48094e14344e646fd5c2e","public:commit:bb51b7e2d690402e53af8965e8657f3391849597","public:commit:c65af029b3a0b8fb16858a89e286d6d9377b140e","public:commit:c9c810dfce8b73b47618309966377cf0a18ab7a1","public:commit:e31556168202ba5ff57da3747a0938e4e8648bc7","public:commit:f9c2c89888d36549709643050e48db9865a01408","public:commit:fb62ba97b2851a070c0b78ae0647f7da63ca0f6e"],"source_type":"public","date":"2024-03-04..2024-03-13","topics":["ffi","testing","build","performance","api","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Build scope, documentation, bootstrap and workflow permissions {#build-scope-documentation-bootstrap-and-workflow-permissions}

## Result and evidence boundaries {#result-and-evidence-boundaries}

The noncore changes in this unit refine build reporting, setup guidance, Python packaging documentation and CI defaults while commands and permissions evolve. Several commit titles say docs, refactor or CI even when the patch changes runtime semantics. Each diff was examined before classification. Verified navigation/formatting/generated scaffolds receive brief dispositions; they do not become independent architectural principles.

## Coverage denominator and synthetic test scope {#coverage-denominator-and-synthetic-test-scope}

243 restricts gcovr to src/. This changes reported coverage scope and excludes inline public-header implementation from the denominator. It does not show fewer tests being executed or provide a measured coverage result. Coverage percentages across this point require the filter context. The native ABI and much public API behavior are not validated merely by a favorable filtered report.

272 and 300 update synthetic TestServer to match newly added command methods and shared-pointer signatures, but implementations return null. 356 supplies the new sender getter with a static ServerCommandSender, whose getServer reaches the production singleton. These are interface-conformance repairs, not permission or real-host integration tests. The research ran no build, compiler, package install, workflow or host executable. Source-level CI fixes must not be reported as observed CI passes.

## Bootstrap gains a host-setting side effect {#bootstrap-gains-a-host-setting-side-effect}

311 queries Windows loopback exemptions for the Minecraft package and starts an elevated CheckNetIsolation add operation when absent. This is a substantive security-sensitive setting change embedded in server startup. The surrounding create flow does not establish successful completion, and launching an elevated process is not the same as waiting for and checking its result. The query path can also raise before startup continues.

This research only read that source. It did not execute the command, request elevation or alter a host exemption. The historical implementation is relevant when reviewing installer/bootstrap consent and failure handling: configuration inspection, requesting elevated mutation, asynchronous completion and application startup should not be conflated. No external Windows documentation or current platform behavior was verified here.

## Documentation toolchain and deployment are separate {#documentation-toolchain-and-deployment-are-separate}

329 is the default MkDocs scaffold, read in full and classified as generated. 330 gives the site project identity and Material styling. 331 adds Read the Docs with Ubuntu 22.04/Python 3.12, documentation requirements and installation of the native project. 333 removes project installation, leaving the static documentation dependency path. The effect decouples documentation generation from native extension/toolchain setup; no captured failure log proves why it was chosen.

332 changes the config suffix through an exact blob-identical rename. 334 adds a badge and 335 configures repository/search/theme/navigation and a mike version-provider UI. The patch does not install mike or add a version deployment pipeline. A UI provider setting, badge or repository link is not evidence that versioned documentation was built or published. The Material dependency remains unpinned in these additions. Historical intent and observed publication status remain separate.

## Roadmaps and user-facing claims {#roadmaps-and-user-facing-claims}

263 describes cross-platform support, Bukkit-like APIs and Python/C++ tradeoffs, with exclusivity and performance positioning. 274 introduces a dated roadmap with approximate durations; 310 and 328 update completion states. These are contemporaneous project claims and plans. This review does not independently verify market exclusivity, benchmarks, platform minimums or actual milestone completeness. Later unfinished permission/callback work illustrates why a roadmap checkmark is not a full behavioral audit.

273 clarifies advanced build instructions using C++17 and Ninja and moves Docker earlier. The examples do not establish durable data-volume handling or actual compiler compatibility. Navigation fixes, badge links, punctuation and test naming are retained with their SHA identities but no inflated design inference. 281's millisecond timestamp format is a modest observability improvement; it supplies no new diagnostic event or measured overhead.

## Workflow token defaults {#workflow-token-defaults}

360 adds top-level read-all permissions to five workflows. This makes token defaults explicit in source. The Docker job still declares packages: write, so an all-jobs-read-only summary would be wrong. Reading secret variable references does not disclose their values, and this review did not inspect credentials or change repository settings. This historical source change is not a claim that current GitHub workflows have the same settings or that every job-specific permission is minimal.

## Practical use {#practical-use}

Use this evidence for reporting-scope comparisons, package/test boundary reviews, setup side-effect inventories and documentation deployment checks. For each claim ask whether the source changes a configuration, implements a runtime path, adds an executable test, or actually records a measured result. Most commits here establish only one of those layers. Keep brief mechanical dispositions brief while retaining runtime changes hidden under apparently harmless titles.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-243"></a>
### 243. feat: test coverage of source code files (src/) only {#commit-243}

[3330217dc8cd1a8d177b692fafea5ab7024b16dd](https://github.com/EndstoneMC/endstone/commit/3330217dc8cd1a8d177b692fafea5ab7024b16dd) · 2024-03-04T23:51:05Z · small-semantic

Author: Vincent. Actual parent: `cc74b0aa29d77e98a789b2f9739034739697382b`. Full individual diff read; static evidence only.

Limits gcovr reporting to src/, excluding public/header-inline implementation and test sources from the coverage denominator. Does not change which tests execute or supply measured coverage; interpret later percentages under this changed scope.

Changed paths: `.github/workflows/coverage.yml`.

<a id="commit-259"></a>
### 259. chore: update .clang-tidy {#commit-259}

[bb51b7e2d690402e53af8965e8657f3391849597](https://github.com/EndstoneMC/endstone/commit/bb51b7e2d690402e53af8965e8657f3391849597) · 2024-03-05T12:55:23Z · mechanical

Author: Vincent. Actual parent: `86f72dba0eb0e7821aea5aa3d392aef0975a2e35`. Full individual diff read; static evidence only.

Reorders existing clang-tidy exclusions and additionally disables performance-enum-size. This is an explicit lint-policy change relevant to native enum ABI sizes; no reason or measured performance result is supplied.

Changed paths: `.clang-tidy`.

<a id="commit-263"></a>
### 263. docs: update README.md {#commit-263}

[c65af029b3a0b8fb16858a89e286d6d9377b140e](https://github.com/EndstoneMC/endstone/commit/c65af029b3a0b8fb16858a89e286d6d9377b140e) · 2024-03-05T13:36:52Z · mechanical

Author: Vincent. Actual parent: `a3af52df4f82237ec36e7387828158f307e85bf4`. Full individual diff read; static evidence only.

Adds README feature positioning: cross-platform native host support, game parity, simple startup, Bukkit-like API and Python/C++ tradeoffs. These are project claims, including exclusivity/performance implications, not independently verified market or benchmark facts.

Changed paths: `README.md`.

<a id="commit-272"></a>
### 272. ci: fix test package {#commit-272}

[e31556168202ba5ff57da3747a0938e4e8648bc7](https://github.com/EndstoneMC/endstone/commit/e31556168202ba5ff57da3747a0938e4e8648bc7) · 2024-03-05T23:56:13Z · small-semantic

Author: Vincent. Actual parent: `56e09bc9f5fb30540e08ba17df14804d5dee594e`. Full individual diff read; static evidence only.

Updates synthetic TestServer for new virtual command methods, returning nullptr for both. Restores interface conformance without testing command lookup or registration behavior; source CI fix is not observed CI success.

Changed paths: `test_package/src/test_server.cpp`.

<a id="commit-273"></a>
### 273. docs: update README.md {#commit-273}

[9e29c533592e886052c48094e14344e646fd5c2e](https://github.com/EndstoneMC/endstone/commit/9e29c533592e886052c48094e14344e646fd5c2e) · 2024-03-06T00:01:35Z · small-semantic

Author: Vincent. Actual parent: `e31556168202ba5ff57da3747a0938e4e8648bc7`. Full individual diff read; static evidence only.

Moves Docker before advanced source-building instructions and specifies C++17/Ninja Conan arguments in collapsed details. This clarifies intended setup rather than proving toolchain compatibility; Docker examples still lack persistent storage mapping.

Changed paths: `README.md`.

<a id="commit-274"></a>
### 274. docs: update README.md {#commit-274}

[53de1d91ffcd2dcfca1789c63c8ab74e9b69d824](https://github.com/EndstoneMC/endstone/commit/53de1d91ffcd2dcfca1789c63c8ab74e9b69d824) · 2024-03-06T00:22:56Z · small-semantic

Author: Vincent. Actual parent: `9e29c533592e886052c48094e14344e646fd5c2e`. Full individual diff read; static evidence only.

Adds dated roadmap, example-template links and rough milestone durations/statuses: loader marked done, command system underway, later permissions/events pending. Preserve as contemporaneous project claims/plans, not verified completeness or delivery estimates.

Changed paths: `README.md`.

<a id="commit-278"></a>
### 278. docs: update README.md {#commit-278}

[349f0abf9ec0b13f5045d01c87a6ac64f8af9e2c](https://github.com/EndstoneMC/endstone/commit/349f0abf9ec0b13f5045d01c87a6ac64f8af9e2c) · 2024-03-06T12:08:54Z · mechanical

Author: Vincent. Actual parent: `8c9f7e9dfe2fa8e9a8df481541e38ffa226e73e0`. Full individual diff read; static evidence only.

Renames README milestone section/link to Get Started with Plugins without changing roadmap data or code.

Changed paths: `README.md`.

<a id="commit-279"></a>
### 279. refactor(test): rename test_chat_colors to test_color_format {#commit-279}

[79b7386f7a8c48524247cdce21d2e662a718d3e6](https://github.com/EndstoneMC/endstone/commit/79b7386f7a8c48524247cdce21d2e662a718d3e6) · 2024-03-06T12:21:58Z · mechanical

Author: Vincent. Actual parent: `349f0abf9ec0b13f5045d01c87a6ac64f8af9e2c`. Full individual diff read; static evidence only.

Renames the color-constant test function to match ColorFormat. Assertions and covered behavior are unchanged.

Changed paths: `python/tests/test_color_format.py`.

<a id="commit-281"></a>
### 281. refactor: logging configuration {#commit-281}

[014cfb9fc5ee8d60b7a44d510e9338372cc1dd60](https://github.com/EndstoneMC/endstone/commit/014cfb9fc5ee8d60b7a44d510e9338372cc1dd60) · 2024-03-06T13:52:54Z · small-semantic

Author: Vincent. Actual parent: `f7cf1388333ad371395e21c156c9b8c4e174a845`. Full individual diff read; static evidence only.

Adds explicit date/time format with millisecond precision to bootstrap logging. Helps align event timestamps; no new diagnostic events or measured logging overhead.

Changed paths: `python/src/endstone/_internal/bootstrap/__init__.py`.

<a id="commit-284"></a>
### 284. docs: update README.md {#commit-284}

[c9c810dfce8b73b47618309966377cf0a18ab7a1](https://github.com/EndstoneMC/endstone/commit/c9c810dfce8b73b47618309966377cf0a18ab7a1) · 2024-03-06T14:50:02Z · mechanical

Author: Vincent. Actual parent: `fa159c8dd32f325ab6109637ec7d00704d9ab3e7`. Full individual diff read; static evidence only.

Rewords README navigation as Get started/Plugins and adds links to Python/license badges. No implementation or compatibility change.

Changed paths: `README.md`.

<a id="commit-285"></a>
### 285. docs: update README.md {#commit-285}

[783d1a8cb9eec8a49b0a97d8bf1ff8176ddff210](https://github.com/EndstoneMC/endstone/commit/783d1a8cb9eec8a49b0a97d8bf1ff8176ddff210) · 2024-03-06T14:50:25Z · mechanical

Author: Vincent. Actual parent: `c9c810dfce8b73b47618309966377cf0a18ab7a1`. Full individual diff read; static evidence only.

Corrects encoded README anchor target only; no independent engineering lesson.

Changed paths: `README.md`.

<a id="commit-300"></a>
### 300. ci: fix test_package {#commit-300}

[5c89e7266bd3f8388621b5be8d1df8ba8b19619a](https://github.com/EndstoneMC/endstone/commit/5c89e7266bd3f8388621b5be8d1df8ba8b19619a) · 2024-03-07T00:33:51Z · mechanical

Author: Vincent. Actual parent: `e65a25b17c96424de8df8f07aa4aef009e46a3ba`. Full individual diff read; static evidence only.

Changes TestServer registration argument to shared_ptr to match 298. Stub still returns nullptr; no new registration behavior coverage.

Changed paths: `test_package/src/test_server.cpp`.

<a id="commit-310"></a>
### 310. docs: update README.md {#commit-310}

[110b00c5cd2a75b4d8ec8295711a57d14de2bb78](https://github.com/EndstoneMC/endstone/commit/110b00c5cd2a75b4d8ec8295711a57d14de2bb78) · 2024-03-08T11:59:17Z · small-semantic

Author: Vincent. Actual parent: `26d35af5f66c6e2cf12d0a5fcd0c8a4ab463af74`. Full individual diff read; static evidence only.

README refines Windows minimums, marks C++/Python command APIs complete and permissions underway, while core command system remains underway. Also removes unused native reserved parameter name. Milestone labels and OS claims are dated documentation, not verified test matrices.

Changed paths: `README.md`, `src/endstone_runtime/main.cpp`.

<a id="commit-311"></a>
### 311. feat: add loopback exemption check in Windows bootstrap {#commit-311}

[1ea6e9d29f343ca40a90b078733ed543bcec4b14](https://github.com/EndstoneMC/endstone/commit/1ea6e9d29f343ca40a90b078733ed543bcec4b14) · 2024-03-08T16:21:31Z · meaningful

Author: Vincent. Actual parent: `110b00c5cd2a75b4d8ec8295711a57d14de2bb78`. Full individual diff read; static evidence only.

Windows bootstrap checks Minecraft package loopback exemption and launches elevated CheckNetIsolation to add it when absent. Server creation ignores returned success and elevated-launch result is not completion verification; subprocess query can raise. This introduces a security-sensitive host-setting side effect into startup. Research inspected source only and did not execute or grant any exemption.

Changed paths: `python/src/endstone/_internal/bootstrap/windows.py`.

<a id="commit-328"></a>
### 328. docs: update README.md {#commit-328}

[58d0d14052fe309515cab3f30184b201446ec717](https://github.com/EndstoneMC/endstone/commit/58d0d14052fe309515cab3f30184b201446ec717) · 2024-03-11T16:55:21Z · mechanical

Author: Vincent. Actual parent: `5fe2eae7c42b01063e3277b64d892e652ba92451`. Full individual diff read; static evidence only.

README marks command core complete and event core underway. This is project-reported milestone status, not proof all remaining command edge cases or tests are complete.

Changed paths: `README.md`.

<a id="commit-329"></a>
### 329. docs: add mkdocs {#commit-329}

[2eb5782db7a6eccbf8de798cbc88e9b18f647c33](https://github.com/EndstoneMC/endstone/commit/2eb5782db7a6eccbf8de798cbc88e9b18f647c33) · 2024-03-11T18:16:44Z · generated-verified

Author: Vincent. Actual parent: `58d0d14052fe309515cab3f30184b201446ec717`. Full individual diff read; static evidence only.

Adds default 17-line MkDocs welcome/example page and one-line My Docs configuration. Full generated scaffold inspected; no Endstone-specific documentation mechanism or preference inferred.

Changed paths: `docs/index.md`, `mkdocs.yml`.

<a id="commit-330"></a>
### 330. docs: update mkdocs.yml {#commit-330}

[4aafb09d0c1e620ca41f9dcce0f712032564b369](https://github.com/EndstoneMC/endstone/commit/4aafb09d0c1e620ca41f9dcce0f712032564b369) · 2024-03-11T18:20:01Z · small-semantic

Author: Vincent. Actual parent: `2eb5782db7a6eccbf8de798cbc88e9b18f647c33`. Full individual diff read; static evidence only.

Names documentation Endstone, selects Material theme and adds GitHub/PyPI/Docker social links. Configuration intent only; no published site or installed theme validation.

Changed paths: `mkdocs.yml`.

<a id="commit-331"></a>
### 331. docs: add .readthedocs.yml {#commit-331}

[642d781effc39138e1e5897d494ba7899dea0379](https://github.com/EndstoneMC/endstone/commit/642d781effc39138e1e5897d494ba7899dea0379) · 2024-03-11T18:23:16Z · meaningful

Author: Vincent. Actual parent: `4aafb09d0c1e620ca41f9dcce0f712032564b369`. Full individual diff read; static evidence only.

Adds Read the Docs Ubuntu 22.04/Python 3.12 MkDocs build, docs requirements and pip installation of local project. This initially couples documentation to native project build dependencies;333 removes the package install. mkdocs-material remains unpinned; no documentation build executed.

Changed paths: `.readthedocs.yml`, `docs/requirements.txt`.

<a id="commit-332"></a>
### 332. refactor: rename .readthedocs.yml to .readthedocs.yaml {#commit-332}

[61b3b00f1e7991d2ba2d6e430e83401e4c166acd](https://github.com/EndstoneMC/endstone/commit/61b3b00f1e7991d2ba2d6e430e83401e4c166acd) · 2024-03-11T18:23:56Z · mechanical

Author: Vincent. Actual parent: `642d781effc39138e1e5897d494ba7899dea0379`. Full individual diff read; static evidence only.

Exact blob-identical rename of Read the Docs configuration .yml to .yaml. No content change or rereading as new semantics needed.

Changed paths: `.readthedocs.yaml`, `.readthedocs.yml`.

<a id="commit-333"></a>
### 333. refactor: remove pip install . from .readthedocs.yaml {#commit-333}

[8ffb0bcb9bafdbef14d5680a861dca76a2abe9a4](https://github.com/EndstoneMC/endstone/commit/8ffb0bcb9bafdbef14d5680a861dca76a2abe9a4) · 2024-03-11T18:28:04Z · meaningful

Author: Vincent. Actual parent: `61b3b00f1e7991d2ba2d6e430e83401e4c166acd`. Full individual diff read; static evidence only.

Removes pip installation of the native project from documentation build, retaining only docs requirements. Decouples static docs generation from native extension/toolchain setup; reason is inferred from effect, not a recorded failure log.

Changed paths: `.readthedocs.yaml`.

<a id="commit-334"></a>
### 334. docs: update README.md {#commit-334}

[f9c2c89888d36549709643050e48db9865a01408](https://github.com/EndstoneMC/endstone/commit/f9c2c89888d36549709643050e48db9865a01408) · 2024-03-11T18:36:13Z · mechanical

Author: Vincent. Actual parent: `8ffb0bcb9bafdbef14d5680a861dca76a2abe9a4`. Full individual diff read; static evidence only.

Adds documentation badge/link and final newline to configuration. Does not prove successful documentation publication.

Changed paths: `.readthedocs.yaml`, `README.md`.

<a id="commit-335"></a>
### 335. docs: update mkdocs.yml {#commit-335}

[42bcdcd60cca923a1c7ceae20aaa590d0689a039](https://github.com/EndstoneMC/endstone/commit/42bcdcd60cca923a1c7ceae20aaa590d0689a039) · 2024-03-11T21:17:09Z · small-semantic

Author: Vincent. Actual parent: `f9c2c89888d36549709643050e48db9865a01408`. Full individual diff read; static evidence only.

Configures repository link, mike version-provider UI, search, theme toggles and navigation features. Does not add mike to requirements or a version-deployment pipeline, so configuration is not proof versioned docs exist.

Changed paths: `mkdocs.yml`.

<a id="commit-351"></a>
### 351. style: code formatting {#commit-351}

[9838b4a82e0d37c34f655b4e477888931ccb667b](https://github.com/EndstoneMC/endstone/commit/9838b4a82e0d37c34f655b4e477888931ccb667b) · 2024-03-12T18:17:25Z · mechanical

Author: Vincent. Actual parent: `7af8eb265da90e87fed7c6b651df6a0ccfeeab08`. Full individual diff read; static evidence only.

Verified include-order and brace-layout-only formatting in registry and adapter. Unlike prior 224 assembly formatting, no line-sensitive source is changed here; no independent architectural inference.

Changed paths: `include/bedrock/command/command_registry.h`, `src/endstone_core/command/command_adapter.cpp`.

<a id="commit-356"></a>
### 356. ci: fix test_package {#commit-356}

[071b788b51610c9ac0ae1adb2259c05b108feb36](https://github.com/EndstoneMC/endstone/commit/071b788b51610c9ac0ae1adb2259c05b108feb36) · 2024-03-13T12:27:34Z · small-semantic

Author: Vincent. Actual parent: `9674fb3f8a75ccae5aa7691e204dd191d9029497`. Full individual diff read; static evidence only.

Updates TestServer to implement new getCommandSender using static ServerCommandSender. This restores interface conformance but sender getServer still reaches production singleton rather than this fake TestServer. Fixture change is not a new permission/host integration test or evidence those methods were exercised.

Changed paths: `test_package/src/test_server.cpp`.

<a id="commit-360"></a>
### 360. ci: explicitly specify permissions: read-all on top level {#commit-360}

[fb62ba97b2851a070c0b78ae0647f7da63ca0f6e](https://github.com/EndstoneMC/endstone/commit/fb62ba97b2851a070c0b78ae0647f7da63ca0f6e) · 2024-03-13T17:46:37Z · meaningful

Author: Vincent. Actual parent: `6146d2e0e0aaadc323f2a714b01cbe77bf1b316e`. Full individual diff read; static evidence only.

Adds explicit top-level permissions: read-all to coverage/Docker/Linux/wheel/Windows workflows. Makes default token intent explicit, but Docker job still explicitly requests packages: write, so do not describe every job as read-only. Secret references are variable names, not disclosed values. No workflows executed or permission settings changed by this research.

Changed paths: `.github/workflows/coverage.yml`, `.github/workflows/docker.yml`, `.github/workflows/linux.yml`, `.github/workflows/wheel.yml`, `.github/workflows/windows.yml`.
