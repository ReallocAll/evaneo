<!-- retrieval: {"source_ids":["public:commit:0511c706b576478c996440781e92db98f17587cc","public:commit:05eb07afcca0428f2eeb5c5877439b08cc9baca5","public:commit:103c30125f3ba7be0c0f70a3ff5450a33454f566","public:commit:1f9653accb4c327dffa45c95e8a3d68e4bc78267","public:commit:226f2f0a8713f0fffa89d1b7cfab12a6568b74d8","public:commit:38290cc0fc392edcddc1b0d51779cf8c85470593","public:commit:3bc1d75afd140d1a3845efa940e90675878ae2ef","public:commit:3df7240f9b2d407dcb49a24bfaec544b9c571a0f","public:commit:412b7131b132e50fd5d46617be05d44e1d8b40d5","public:commit:54b2a78ef6ca9fbdaeb0b4ec9246e27c71dafea5","public:commit:5b316c8ecf4ab898fd6beaa946565f20911f3e9b","public:commit:6163dcb8f247bd50a188cd4dbe2b1dd0aa55daae","public:commit:6528c11ec611bc1daac966634dc0fbdeda16c554","public:commit:689b81a0ff4763147aaf68f09cfcc35583599ced","public:commit:6b764c60bcf0aa67df0a9b53157e54f89e9c4e7d","public:commit:8c47e549ffea66de2d02f6d3ad01692bfa8ca3ce","public:commit:a83cc4ee3d5721d7bc755afb573d782e2bd4f2de","public:commit:c602bc74df9158d25b9d65e0179d52fddb38996c","public:commit:cc2850faf8c3bcb4db6cc7628aebc2287cd2ed29","public:commit:ccad37dd9bd26ddd8b2244a38af526f06f480126","public:commit:db4730f985e1594be2421dae5abd9ffad1e665f9","public:commit:e8338dedc19cc2645565da31a0ed380d9256d1e6","public:commit:ebc9b1910633b4b6d005ffe6efcd1cd308ade73a","public:commit:f022ef1e108bf55a0221bdac3e520d0ce9535b98","public:thread:EndstoneMC/endstone:147"],"source_type":"public","date":"2025-03-03..2025-03-17","topics":["concurrency","ffi","testing","build","performance","api","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Crash reporting, launch integration and distribution {#crash-reporting-launch-integration-and-distribution}

## Reversals are part of the evidence {#reversals-are-part-of-the-evidence}

315–318 move crashpad provisioning into a pinned Python dependency, use RelWithDebInfo and restore pybind11_add_module after the earlier manual binding build.319 then selects breakpad, but321 exactly reverts319 on all its changed paths; only the intervening Dependabot workflow updates remain. The message gives no explanation for reversal.323 tries an in-process backend on Linux/FreeBSD,324 clears LD_PRELOAD before runtime initialization, and325 restores the default crashpad backend. The explicit LD_PRELOAD rationale is preventing inheritance into spawned crash-handler processes. It is process-wide and can also remove unrelated preload configuration. Changelog326 reports outcomes; static review does not verify those reports.

Sentry fatal-app-exit filtering294 belongs to the sibling slice and remains useful context, not new completion credit here. Crash-report policy, human-readable crash text, uploader/backend availability, process inheritance and symbol artifacts are separate mechanisms. No single backend switch proves the whole reporting path works.

## Packaging and launch boundaries {#packaging-and-launch-boundaries}

343 introduces v2 metadata with preview/release selection and exact version matching.347 repairs URL composition that could drop the v2 prefix;361 corrects the stable channel spelling to release.360 fixes nested f-string quoting against the project’s declared Python>=3.9 support and adds nonzero-exit diagnostics. Metadata version equality and downloaded SHA validation are intended gates, not proof that the selected native symbol table is correct.

350–354 replace the Python remote-memory/thread injector with a pinned Microsoft Detours submodule and small synchronous pybind winext wrapper. The local interface and CMake/workflow integration were read fully; the external Detours implementation was not. The wrapper builds an environment block, invokes the ANSI process API, waits, retrieves exit code and closes handles. Review limits include Unicode paths, unchecked wait outcome, GIL retention, environment-inheritance semantics and toolchain guards. This is a migration of responsibility to a dependency, not elimination of injection complexity.

398–399 pin auditwheel6.2.0 in both cibuildwheel repair and Docker paths. The matching pin is observed; no specific upstream regression or successful repaired wheel is established.

## Attribution and applicability {#attribution-and-applicability}

320 integrates Dependabot’s cibuildwheel2.22→2.23 update. Its two final blobs exactly match the bot commit and the full bot patch was read. Embedded ARM/PyPy release notes are upstream claims, not Vincent’s own implementation or measured Endstone compatibility. Useful when reconstructing deployment failures, launch boundaries, crash-handler subprocess inheritance and reversible dependency choices. No packages installed, dependencies executed, CI run or distribution artifacts tested.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-315"></a>
### Commit 315 {#commit-315}

103c30125f3ba7be0c0f70a3ff5450a33454f566 · 2025-03-03T12:27:54Z

[chore: add `sentry-crashpad` dependency](https://github.com/EndstoneMC/endstone/commit/103c30125f3ba7be0c0f70a3ff5450a33454f566)

**Observed change.** Adds pinned sentry-crashpad Python dependency, copies handler package directory into server path during preparation, sets Linux executable permission, removes explicit module-relative Sentry handler path.

**Causal interpretation.** Moves helper delivery from native library bundle to separately packaged executable dependency and server working directory.

**Limits.** Uses a private dependency helper API; Linux chmod derives mode from server executable, not handler. No package content, licensing, launch or compatibility audit.

<a id="commit-316"></a>
### Commit 316 {#commit-316}

cc2850faf8c3bcb4db6cc7628aebc2287cd2ed29 · 2025-03-03T12:28:16Z

[chore: change build type to `RelWithDebInfo` for wheels](https://github.com/EndstoneMC/endstone/commit/cc2850faf8c3bcb4db6cc7628aebc2287cd2ed29)

**Observed change.** Wheel CMake build type Release→RelWithDebInfo.

**Causal interpretation.** Requests optimized symbol-bearing artifacts through standard configuration, setting up318 helper restoration.

**Limits.** No wheel symbol or optimization inspection.

<a id="commit-317"></a>
### Commit 317 {#commit-317}

0511c706b576478c996440781e92db98f17587cc · 2025-03-03T12:36:04Z

[refactor: do not include `crashpad_handler` directly with endstone](https://github.com/EndstoneMC/endstone/commit/0511c706b576478c996440781e92db98f17587cc)

**Observed change.** Removes CMake copying/installing crashpad executable beside Endstone shared library.

**Causal interpretation.** Completes315 packaging authority shift; helper should come from Python dependency instead of duplicated native bundle.

**Limits.** No wheel content/install verification; alternative non-Python distribution paths not proven.

<a id="commit-318"></a>
### Commit 318 {#commit-318}

a83cc4ee3d5721d7bc755afb573d782e2bd4f2de · 2025-03-03T14:04:32Z

[refactor: simplify CMakeLists.txt](https://github.com/EndstoneMC/endstone/commit/a83cc4ee3d5721d7bc755afb573d782e2bd4f2de)

**Observed change.** Restores pybind11_add_module and removes explicit extension/hidden visibility/LTO/windows extras wiring; explicit MSVC optimization/debug flags remain.

**Causal interpretation.** Reverses148's manual module replacement after316 switches to RelWithDebInfo. The code shows consolidation, but no explicit reason or helper-version audit is supplied.

**Limits.** Do not claim stripping/symbol outcome without build artifacts or helper inspection; no build run.

<a id="commit-319"></a>
### Commit 319 {#commit-319}

412b7131b132e50fd5d46617be05d44e1d8b40d5 · 2025-03-03T15:48:24Z

[feat: switch sentry backend to `breakpad` for better compatibility on Linux platforms](https://github.com/EndstoneMC/endstone/commit/412b7131b132e50fd5d46617be05d44e1d8b40d5)

**Observed change.** Switches Conan Sentry backend crashpad→breakpad globally despite Linux-focused title; removes packaged crashpad dependency/copy. Reorganizes crash formatting and installs Windows terminate/purecall/SIGABRT handlers which print and quick_exit.

**Causal interpretation.** Compatibility experiment spans packaging and fatal-error capture paths, not a single option. Explicit title gives intended Linux compatibility, not measured success.

**Limits.** Reverted by321 shortly after. No crash reproduction, signal-safety proof or outcome evidence; extra Windows handlers do not necessarily upload Sentry events.

<a id="commit-320"></a>
### Commit 320 {#commit-320}

8c47e549ffea66de2d02f6d3ad01692bfa8ca3ce · 2025-03-03T15:49:22Z

[chore(deps): bump pypa/cibuildwheel from 2.22.0 to 2.23.0 (#147)](https://github.com/EndstoneMC/endstone/commit/8c47e549ffea66de2d02f6d3ad01692bfa8ca3ce)

**Observed change.** Two-parent PR147 integration updates cibuildwheel2.22→2.23 in wheel and Windows-portable workflows; lengthy message carries Dependabot upstream release/changelog text.

**Causal interpretation.** Routine dependency integration, with upstream feature claims attributed to bot-sourced release notes rather than Vincent implementation or tested project support.

**Limits.** Both-parent/imported-ancestor audit required; no upstream release code/CI execution or ARM/PyPy support claim from these two version edits.

<a id="commit-321"></a>
### Commit 321 {#commit-321}

5b316c8ecf4ab898fd6beaa946565f20911f3e9b · 2025-03-03T16:19:21Z

[Revert "feat: switch sentry backend to `breakpad` for better compatibility on Linux platforms"](https://github.com/EndstoneMC/endstone/commit/5b316c8ecf4ab898fd6beaa946565f20911f3e9b)

**Observed change.** Explicitly reverts319, restoring crashpad option/package/copy and original crash-handler formatting/callback paths, removing added Windows termination handlers.

**Causal interpretation.** A reverted experiment is counterevidence against treating breakpad as an established choice. Exact reversed blob pairs will be audited.

**Limits.** No explicit revert rationale beyond message; do not invent failure cause.

<a id="commit-322"></a>
### Commit 322 {#commit-322}

1f9653accb4c327dffa45c95e8a3d68e4bc78267 · 2025-03-03T16:24:06Z

[fix: crash message format](https://github.com/EndstoneMC/endstone/commit/1f9653accb4c327dffa45c95e8a3d68e4bc78267)

**Observed change.** Moves hexadecimal prefix outside fixed-width label formatting for exception/signal diagnostics.

**Causal interpretation.** Narrow output alignment repair, independent of backend correctness.

**Limits.** No generated crash output inspected.

<a id="commit-323"></a>
### Commit 323 {#commit-323}

c602bc74df9158d25b9d65e0179d52fddb38996c · 2025-03-03T17:31:36Z

[feat: use `inproc` backend for crash reporting on Linux](https://github.com/EndstoneMC/endstone/commit/c602bc74df9158d25b9d65e0179d52fddb38996c)

**Observed change.** Removes global crashpad option and selects inproc for FreeBSD/Linux in Conan config_options.

**Causal interpretation.** Separates platform backend policy after rejected breakpad experiment; Windows defaults remain dependency-controlled.

**Limits.** FreeBSD remains outside declared project platform validation; selecting an option is not end-to-end support. Reversed325.

<a id="commit-324"></a>
### Commit 324 {#commit-324}

db4730f985e1594be2421dae5abd9ffad1e665f9 · 2025-03-05T11:39:34Z

[fix: unset 'LD_PRELOAD' to prevent forked child processes from loading the module](https://github.com/EndstoneMC/endstone/commit/db4730f985e1594be2421dae5abd9ffad1e665f9)

**Observed change.** Splits runtime init from entrypoints; Linux constructor unsets LD_PRELOAD before init, Windows DllMain calls init directly.

**Causal interpretation.** Author explicitly prevents child processes inheriting preload and reloading Endstone. Relevant to out-of-process crashpad helper spawning and recursive initialization.

**Limits.** Process-wide environment mutation removes other preload entries too; no fork/exec or helper reproduction. Loaded parent module remains loaded.

<a id="commit-325"></a>
### Commit 325 {#commit-325}

05eb07afcca0428f2eeb5c5877439b08cc9baca5 · 2025-03-05T16:41:32Z

[feat: re-enable crashpad on Linux](https://github.com/EndstoneMC/endstone/commit/05eb07afcca0428f2eeb5c5877439b08cc9baca5)

**Observed change.** Comments out inproc override so dependency default permits crashpad on Linux again.

**Causal interpretation.** Causal sequence319→321→323→324→325 distinguishes failed/temporary backend workarounds from environmental inheritance repair.

**Limits.** Backend re-enable is observed;326 author changelog says Linux crash reporting works, not independently verified.

<a id="commit-326"></a>
### Commit 326 {#commit-326}

f022ef1e108bf55a0221bdac3e520d0ce9535b98 · 2025-03-05T16:52:04Z

[docs: update CHANGELOG.md](https://github.com/EndstoneMC/endstone/commit/f022ef1e108bf55a0221bdac3e520d0ce9535b98)

**Observed change.** Changelog records packet events, Actor.remove, highest-block Python API and fixes for usage percentages, bossbars, death/feedback gamerules, client-ready join and Linux crash reporting.

**Causal interpretation.** Release-facing author report aggregates earlier changes; useful intent/outcome attribution but not a substitute for source/tests.

**Limits.** Only changelog delta reviewed here; no actual runtime results inferred, especially for fixes authored in sibling201–300.

<a id="commit-333"></a>
### Commit 333 {#commit-333}

3df7240f9b2d407dcb49a24bfaec544b9c571a0f · 2025-03-09T15:11:37Z

[chore: release v0.6.2](https://github.com/EndstoneMC/endstone/commit/3df7240f9b2d407dcb49a24bfaec544b9c571a0f)

**Observed change.** Updates changelog0.6.2 release date/compare links, opens0.6.3 unreleased and increments patch macro to2.

**Causal interpretation.** Release bookkeeping explicitly claims1.21.62 support; no independent design lesson.

**Limits.** No release asset/install validation.

<a id="commit-343"></a>
### Commit 343 {#commit-343}

38290cc0fc392edcddc1b0d51779cf8c85470593 · 2025-03-09T22:06:02Z

[feat: switch to remote index v2](https://github.com/EndstoneMC/endstone/commit/38290cc0fc392edcddc1b0d51779cf8c85470593)

**Observed change.** Moves bootstrap to remote index v2, advertises1.21.70-beta.26, selects preview for prereleases and stable otherwise, validates metadata version and uses platform URL/hash.

**Causal interpretation.** Separates target selection from distribution metadata; exact version mismatch is rejected before download.

**Limits.** urljoin with a base lacking trailing slash drops v2; fixed347. Nested f-string double quotes need Python3.12; corrected360. No remote install or hash verification run.

<a id="commit-347"></a>
### Commit 347 {#commit-347}

6b764c60bcf0aa67df0a9b53157e54f89e9c4e7d · 2025-03-09T22:54:10Z

[fix: correct metadata URL construction logic](https://github.com/EndstoneMC/endstone/commit/6b764c60bcf0aa67df0a9b53157e54f89e9c4e7d)

**Observed change.** Builds metadata URL by slash-joining base/channel/version/metadata.json instead of urljoin.

**Causal interpretation.** Preserves the v2 path segment that343's URL resolution could replace.

**Limits.** Does not generally normalize leading/trailing slashes; no downloader tests.

<a id="commit-350"></a>
### Commit 350 {#commit-350}

ccad37dd9bd26ddd8b2244a38af526f06f480126 · 2025-03-10T13:31:39Z

[chore: add `detours` as submodule](https://github.com/EndstoneMC/endstone/commit/ccad37dd9bd26ddd8b2244a38af526f06f480126)

**Observed change.** Adds Microsoft Detours gitlink pinned b2bf32a657be1114b173ad28d2d65463ca4c466f with official GitHub source; CMake lists ten source files and builds/installs static library.

**Causal interpretation.** Introduces a maintained external process-injection mechanism rather than preserving all injector code locally.

**Limits.** Gitlink identity/build integration reviewed; external Detours implementation not fetched or audited and no dependency code executed.

<a id="commit-351"></a>
### Commit 351 {#commit-351}

6163dcb8f247bd50a188cd4dbe2b1dd0aa55daae · 2025-03-10T13:34:58Z

[chore: limit detours dep to MSVC](https://github.com/EndstoneMC/endstone/commit/6163dcb8f247bd50a188cd4dbe2b1dd0aa55daae)

**Observed change.** Guards Detours target with MSVC and sets Windows build options including /MT,/Zi,/W4,/WX,/Od.

**Causal interpretation.** Constrains dependency build to toolchain expectations, but Windows consumer later uses WIN32 condition.

**Limits.** No MSVC/non-MSVC Windows build verification; option presence does not establish working CRT linkage.

<a id="commit-352"></a>
### Commit 352 {#commit-352}

54b2a78ef6ca9fbdaeb0b4ec9246e27c71dafea5 · 2025-03-10T13:42:06Z

[feat: add `winext` module for Windows](https://github.com/EndstoneMC/endstone/commit/54b2a78ef6ca9fbdaeb0b4ec9246e27c71dafea5)

**Observed change.** Adds synchronous winext.create_process via DetourCreateProcessWithDllExA, env-map block, process wait/exit-code and handle cleanup; exports runtime DllMain at ordinal1 NONAME.

**Causal interpretation.** Moves injection into C++/Detours and exposes a narrow Python boundary, avoiding manual remote-thread orchestration.

**Limits.** ANSI path API replaces wide path support later; wait result unchecked, no GIL release, no Windows run. Empty environment map means inherit rather than explicitly empty.

<a id="commit-353"></a>
### Commit 353 {#commit-353}

ebc9b1910633b4b6d005ffe6efcd1cd308ade73a · 2025-03-10T13:53:26Z

[feat: use DetourCreateProcessWithDllExA to launch the server process on Windows](https://github.com/EndstoneMC/endstone/commit/ebc9b1910633b4b6d005ffe6efcd1cd308ade73a)

**Observed change.** Removes Python ctypes suspended-process allocation/write/remote-thread/thread-resume injector. Bootstrap.run delegates platform run, prepares environment; Linux uses Popen/wait and Windows winext plus symbol path.

**Causal interpretation.** Shrinks custom OS injection code and centralizes launch environment, delegating complexity to pinned Detours.

**Limits.** Loss of explicit Unicode Windows path handling is source-visible; no process failure, signal, injection or exit-code tests.

<a id="commit-354"></a>
### Commit 354 {#commit-354}

3bc1d75afd140d1a3845efa940e90675878ae2ef · 2025-03-10T14:20:36Z

[ci: checkout submodules in all GitHub workflows](https://github.com/EndstoneMC/endstone/commit/3bc1d75afd140d1a3845efa940e90675878ae2ef)

**Observed change.** Enables submodule checkout in five workflows.

**Causal interpretation.** Required acquisition step for the new gitlink; repository checkout alone would lack Detours source.

**Limits.** Workflow configuration inspected, no CI result or supply-chain implementation audit.

<a id="commit-360"></a>
### Commit 360 {#commit-360}

689b81a0ff4763147aaf68f09cfcc35583599ced · 2025-03-10T22:31:55Z

[fix: resolve a crash on Linux due to incorrect function address](https://github.com/EndstoneMC/endstone/commit/689b81a0ff4763147aaf68f09cfcc35583599ced)

**Observed change.** Corrects Linux Level::tick symbol145524866→145524864; logs nonzero server exit then pauses two seconds; fixes nested f-string quotes.

**Causal interpretation.** Combines a native-address repair with visible bootstrap failure diagnostics and Python syntax compatibility.

**Limits.** Title reports startup crash resolved, but no crash reproduction or Linux execution performed.

<a id="commit-361"></a>
### Commit 361 {#commit-361}

e8338dedc19cc2645565da31a0ed380d9256d1e6 · 2025-03-10T23:05:48Z

[refactor: update channel from "stable" to "release"](https://github.com/EndstoneMC/endstone/commit/e8338dedc19cc2645565da31a0ed380d9256d1e6)

**Observed change.** Changes stable metadata channel spelling to release.

**Causal interpretation.** Aligns consumer path with release-index naming; preview selection unchanged.

**Limits.** Remote index/install availability unverified.

<a id="commit-398"></a>
### Commit 398 {#commit-398}

226f2f0a8713f0fffa89d1b7cfab12a6568b74d8 · 2025-03-17T15:11:18Z

[chore: fix auditwheel version](https://github.com/EndstoneMC/endstone/commit/226f2f0a8713f0fffa89d1b7cfab12a6568b74d8)

**Observed change.** Pins auditwheel6.2.0 in cibuildwheel repair command.

**Causal interpretation.** Narrows packaging tool variability on one build path.

**Limits.** No explicit underlying incompatibility explanation or wheel repair result supplied.

<a id="commit-399"></a>
### Commit 399 {#commit-399}

6528c11ec611bc1daac966634dc0fbdeda16c554 · 2025-03-17T16:06:24Z

[chore: fix auditwheel version](https://github.com/EndstoneMC/endstone/commit/6528c11ec611bc1daac966634dc0fbdeda16c554)

**Observed change.** Applies same auditwheel6.2.0 pin to Docker wheel-build path.

**Causal interpretation.** Keeps two distribution paths aligned; distinct file, same dependency decision as398.

**Limits.** No Docker/image execution or portability validation.
