<!-- retrieval: {"source_ids":["public:commit:09a8a846a6e419da2c31886f8a2d6983cf9bba79","public:commit:0fe98094c447abcb9a1806e6b7a2d7b9943dcddc","public:commit:1e33ebc125bae1d34257f42fb4ce8d0c21091d38","public:commit:2505d29ad740a10cf599ae72748e0ea65cd34f52","public:commit:276a5c3ae0748a4b14efc1f1350fd1bc9bec6b55","public:commit:2f5cb9436f84996e32f3010ec74f558036893edb","public:commit:30ab36b7e6e26b1cf1ac1b6f4ec97c7c2901da6a","public:commit:406b845ed497fdec304018c43c417e273f5420b3","public:commit:513e82e98b95bfc81d8ae0428f51783595000ba2","public:commit:619cc6929c7f50abdaa0adff7f592ba8c63499aa","public:commit:8b14b464f12de98468992d26d4f838b98c859936","public:commit:8dcb223d693c88d99337215bb5441c45bc7f7646","public:commit:8f97da2a5f1d9a22a8547c61dd0b0b61d8336b3d","public:commit:9c7ba186fb765ab621d84d5bcf9313a0b8f814ff","public:commit:a39e5b1970597053c56e7cd05430727f89d9128f","public:commit:f04ae1f71cee81f660a68055106a975c762f6ab0"],"source_type":"public","date":"2026-08-27","topics":["lifetime","ffi","build","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="foundation-and-platform-ownership"></a>
# Foundation and platform ownership {#foundation-and-platform-ownership}

The rewrite begins as an independent root. Its explicit agent guidance is historical repository evidence, not research authority. Conan, logging and naming choices evolve within days. Windows owns its rendering context while the Linux launcher hosts an Android/bionic payload that must borrow the host ImGui ABI. Read these choices with the later observability and allocator counterexamples.

This dossier separates observed code changes from explicit commit-message rationale and review inference. The original patches are available through the public commit links in each entry. Author-reported measurements and client checks were not repeated.

<a id="commit-001"></a>
## 001. scaffold the build and the three entry points {#commit-001}
[30ab36b7e6e26b1cf1ac1b6f4ec97c7c2901da6a](https://github.com/EndstoneMC/spyglass/commit/30ab36b7e6e26b1cf1ac1b6f4ec97c7c2901da6a) · authored 2026-08-27T22:33:15Z · committed 2026-08-27T22:33:15Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: empty-tree root.

Root of the August rewrite scaffolds three entry points and one CMake project. The initial CLAUDE.md states repository-local agent rules: plain prose, client names/layouts retained, no general helper unless reused or public, member detours retain member signatures, strict unique pattern matching, one dependency manager and one build description. These are evidence of explicit repository guidance at this revision, not current agent instructions or timeless preferences. It recounts an MSVC hidden-return-buffer/member-this register mismatch that was quiet on Itanium; this is a reported prior incident, not independently reproduced. Initial code has no hooks or overlay. The Conan mandate is reversed by 4, while comments later become essential ABI evidence; preserve both counterexamples.

Knowledge identity: `knowledge:commit:30ab36b7e6e26b1cf1ac1b6f4ec97c7c2901da6a`.

Evidence:
- diff, parent 1, numbered lines1–233; full semantic diff read.
- message, parent 1, numbered lines1–5; full message read.

Changed paths: `.gitignore`, `CLAUDE.md`, `CMakeLists.txt`, `conanfile.txt`, `src/injector/main.cpp`, `src/spyglass/dllmain.cpp`, `src/spyglass/modmain.cpp`.

<a id="commit-002"></a>
## 002. say that the non-Windows target is Android, not Linux {#commit-002}
[276a5c3ae0748a4b14efc1f1350fd1bc9bec6b55](https://github.com/EndstoneMC/spyglass/commit/276a5c3ae0748a4b14efc1f1350fd1bc9bec6b55) · authored 2026-08-27T22:35:31Z · committed 2026-08-27T22:35:31Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 30ab36b7e6e26b1cf1ac1b6f4ec97c7c2901da6a.

Corrects the platform model: Linux launcher hosts an Android x86_64/bionic client and payload, so 'Linux' is not the target ABI. Documents NDK cross-build through Conan and distinguishes Endstone's other recipe consumers. Documentation-only correction, no runtime behavior change; later Conan removal supersedes dependency details.

Knowledge identity: `knowledge:commit:276a5c3ae0748a4b14efc1f1350fd1bc9bec6b55`.

Evidence:
- diff, parent 1, numbered lines1–52; full semantic diff read.
- message, parent 1, numbered lines1–8; full message read.

Changed paths: `CLAUDE.md`.

<a id="commit-003"></a>
## 003. gate the entry point on _WIN32 instead of on the source list {#commit-003}
[2505d29ad740a10cf599ae72748e0ea65cd34f52](https://github.com/EndstoneMC/spyglass/commit/2505d29ad740a10cf599ae72748e0ea65cd34f52) · authored 2026-08-27T22:38:00Z · committed 2026-08-27T22:38:00Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 276a5c3ae0748a4b14efc1f1350fd1bc9bec6b55.

Consolidates dllmain/modmain into an _WIN32-gated entry.cpp with one payload source list and common install rule; only the genuinely Windows-only injector target remains conditional in CMake. The message explicitly motivates avoiding parallel source-list maintenance. Empty entry bodies remain; compilation was not run.

Knowledge identity: `knowledge:commit:2505d29ad740a10cf599ae72748e0ea65cd34f52`.

Evidence:
- diff, parent 1, numbered lines1–99; full semantic diff read.
- message, parent 1, numbered lines1–6; full message read.

Changed paths: `CMakeLists.txt`, `src/spyglass/dllmain.cpp`, `src/spyglass/entry.cpp`, `src/spyglass/modmain.cpp`.

<a id="commit-004"></a>
## 004. fetch dependencies with FetchContent instead of Conan {#commit-004}
[8f97da2a5f1d9a22a8547c61dd0b0b61d8336b3d](https://github.com/EndstoneMC/spyglass/commit/8f97da2a5f1d9a22a8547c61dd0b0b61d8336b3d) · authored 2026-08-27T22:45:40Z · committed 2026-08-27T22:45:40Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 2505d29ad740a10cf599ae72748e0ea65cd34f52.

Replaces Conan with per-dependency third_party CMake FetchContent definitions, updates explicit repository guidance, pins expected-lite v0.9.0, funchook v1.1.3, libhat v0.11.1 and the launcher's exact ImGui revision. ImGui gets local build definitions and Windows backends from its own checkout. A shared launcher ImGuiContext makes revision equality an ABI requirement, not merely reproducibility. Disconnected updates avoid routine network queries but pin changes may require one reconnect; separate preset build trees refetch dependencies. Windows entry starts work on a thread rather than inside DllMain work body. No rationale is supplied for a universal preference against Conan beyond this project's chosen structure.

Knowledge identity: `knowledge:commit:8f97da2a5f1d9a22a8547c61dd0b0b61d8336b3d`.

Evidence:
- diff, parent 1, numbered lines1–297; full semantic diff read.
- message, parent 1, numbered lines1–13; full message read.

Changed paths: `CLAUDE.md`, `CMakeLists.txt`, `CMakePresets.json`, `conanfile.txt`, `src/spyglass/entry.cpp`, `src/spyglass/main.cpp`, `third_party/CMakeLists.txt`, `third_party/expected-lite/CMakeLists.txt`, `third_party/funchook/CMakeLists.txt`, `third_party/imgui/CMakeLists.txt`, `third_party/libhat/CMakeLists.txt`.

<a id="commit-005"></a>
## 005. keep the clang-cl pin out of the shared preset base {#commit-005}
[1e33ebc125bae1d34257f42fb4ce8d0c21091d38](https://github.com/EndstoneMC/spyglass/commit/1e33ebc125bae1d34257f42fb4ce8d0c21091d38) · authored 2026-08-27T22:46:53Z · committed 2026-08-27T22:46:53Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 8f97da2a5f1d9a22a8547c61dd0b0b61d8336b3d.

Moves clang-cl compiler cache entries into a Windows-only preset ancestor. Explicit rationale: a cache compiler setting would override the NDK toolchain's compiler selection. Keeps generator/build path shared. This is dependency/toolchain precedence reasoning, not cosmetic JSON reshuffling.

Knowledge identity: `knowledge:commit:1e33ebc125bae1d34257f42fb4ce8d0c21091d38`.

Evidence:
- diff, parent 1, numbered lines1–43; full semantic diff read.
- message, parent 1, numbered lines1–6; full message read.

Changed paths: `CMakePresets.json`.

<a id="commit-006"></a>
## 006. build the mod through presets too {#commit-006}
[513e82e98b95bfc81d8ae0428f51783595000ba2](https://github.com/EndstoneMC/spyglass/commit/513e82e98b95bfc81d8ae0428f51783595000ba2) · authored 2026-08-27T22:49:38Z · committed 2026-08-27T22:49:38Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 1e33ebc125bae1d34257f42fb4ce8d0c21091d38.

Adds symmetrical debug/release/relwithdebinfo Windows and Android configure/build presets. Android takes ANDROID_NDK_ROOT, x86_64 and android-26; host/environment conditions hide unusable presets. Updates guidance to match. This reduces misleading build choices; does not prove every listed preset worked.

Knowledge identity: `knowledge:commit:513e82e98b95bfc81d8ae0428f51783595000ba2`.

Evidence:
- diff, parent 1, numbered lines1–128; full semantic diff read.
- message, parent 1, numbered lines1–7; full message read.

Changed paths: `CLAUDE.md`, `CMakePresets.json`.

<a id="commit-007"></a>
## 007. build both platforms in CI {#commit-007}
[8b14b464f12de98468992d26d4f838b98c859936](https://github.com/EndstoneMC/spyglass/commit/8b14b464f12de98468992d26d4f838b98c859936) · authored 2026-08-27T22:51:10Z · committed 2026-08-27T22:51:10Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 513e82e98b95bfc81d8ae0428f51783595000ba2.

Adds CI for Windows host SDK/STL and Ubuntu-hosted Android cross-compilation, stages via install rules, uploads artifacts, and cancels obsolete same-ref runs. Message explicitly chooses Linux runner for lower cost and leaves NDK at runner-image version, identifying future pinning if libc++ compatibility moves. No tests or observed CI logs accompany the source.

Knowledge identity: `knowledge:commit:8b14b464f12de98468992d26d4f838b98c859936`.

Evidence:
- diff, parent 1, numbered lines1–73; full semantic diff read.
- message, parent 1, numbered lines1–11; full message read.

Changed paths: `.github/workflows/ci.yml`.

<a id="commit-008"></a>
## 008. keep the dependencies out of the artifact, and ship symbols {#commit-008}
[f04ae1f71cee81f660a68055106a975c762f6ab0](https://github.com/EndstoneMC/spyglass/commit/f04ae1f71cee81f660a68055106a975c762f6ab0) · authored 2026-08-27T22:56:29Z · committed 2026-08-27T22:56:29Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 8b14b464f12de98468992d26d4f838b98c859936.

Adds FetchContent EXCLUDE_FROM_ALL to all four dependencies and raises CMake minimum to 3.28, preventing transitive install rules from putting dependency headers/libs in the artifact. CI switches to RelWithDebInfo; payload PDB is optionally installed, Android carries DWARF. Explicit crash-symbol motivation. Source configuration does not verify artifact contents or runtime stack traces.

Knowledge identity: `knowledge:commit:f04ae1f71cee81f660a68055106a975c762f6ab0`.

Evidence:
- diff, parent 1, numbered lines1–122; full semantic diff read.
- message, parent 1, numbered lines1–12; full message read.

Changed paths: `.github/workflows/ci.yml`, `CMakeLists.txt`, `CMakePresets.json`, `third_party/expected-lite/CMakeLists.txt`, `third_party/funchook/CMakeLists.txt`, `third_party/imgui/CMakeLists.txt`, `third_party/libhat/CMakeLists.txt`.

<a id="commit-009"></a>
## 009. wire up the overlay on both platforms {#commit-009}
[9c7ba186fb765ab621d84d5bcf9313a0b8f814ff](https://github.com/EndstoneMC/spyglass/commit/9c7ba186fb765ab621d84d5bcf9313a0b8f814ff) · authored 2026-08-27T23:01:26Z · committed 2026-08-27T23:01:26Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: f04ae1f71cee81f660a68055106a975c762f6ab0.

Ports dual-platform overlay. Windows probes DXGI/D3D vtables, hooks Present/ResizeBuffers and D3D12 ExecuteCommandLists, discovers a direct queue, creates its own ImGui context, subclasses input, chooses D3D12 then D3D11, and rebuilds default style when DPI changes. D3D11 retains backbuffer target; D3D12 retains per-buffer allocator/resource, descriptor pool and barriers but initially lacks explicit GPU completion fences (fixed by 71). Android resolves launcher ELF symbol tables from executable plus load base, prioritizes symtab for non-rdynamic builds, validates ImGui version, adopts host allocator/context and hooks Render. It owns neither rendering backend nor context. Hook RAII installs/uninstalls/destroys funchook state. Logging/output/time are ported here and removed immediately next. Message says ported from main; do not attribute all inherited implementation originality to this patch.

Knowledge identity: `knowledge:commit:9c7ba186fb765ab621d84d5bcf9313a0b8f814ff`.

Evidence:
- diff, parent 1, numbered lines1–1530; full semantic diff read.
- message, parent 1, numbered lines1–11; full message read.

Changed paths: `CMakeLists.txt`, `CMakePresets.json`, `src/spyglass/core/log.cpp`, `src/spyglass/core/log.h`, `src/spyglass/core/output.cpp`, `src/spyglass/core/output.h`, `src/spyglass/core/time.cpp`, `src/spyglass/core/time.h`, `src/spyglass/hook/function_hook.cpp`, `src/spyglass/hook/function_hook.h`, `src/spyglass/hook/host_symbol.cpp`, `src/spyglass/hook/host_symbol.h`, `src/spyglass/main.cpp`, `src/spyglass/overlay/backend.h`, `src/spyglass/overlay/d3d11_backend.cpp`, `src/spyglass/overlay/d3d11_backend.h`, `src/spyglass/overlay/d3d12_backend.cpp`, `src/spyglass/overlay/d3d12_backend.h`, `src/spyglass/overlay/input.cpp`, `src/spyglass/overlay/input.h`, `src/spyglass/overlay/install.h`, `src/spyglass/overlay/launcher_overlay.cpp`, `src/spyglass/overlay/overlay.cpp`, `src/spyglass/overlay/overlay.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`.

<a id="commit-010"></a>
## 010. split the overlay by platform, and cut what it does not need yet {#commit-010}
[8dcb223d693c88d99337215bb5441c45bc7f7646](https://github.com/EndstoneMC/spyglass/commit/8dcb223d693c88d99337215bb5441c45bc7f7646) · authored 2026-08-27T23:06:22Z · committed 2026-08-27T23:06:22Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 9c7ba186fb765ab621d84d5bcf9313a0b8f814ff.

Full structural pairing verifies 12 platform file moves and reads every residual delta. Files self-gate into empty wrong-platform translation units; CMake has one explicit flat source list. Removes unused log/output/timestamp subsystem, disables ImGui ini persistence, simplifies namespace and FunctionHook placement, adds compile_commands editor settings. Render/input algorithms preserved except removed logging. Silent startup catches now remain; 23 later restores visible error reporting after reported diagnosis costs. Thus this simplification is not an unconditional recommendation to discard observability.

Knowledge identity: `knowledge:commit:8dcb223d693c88d99337215bb5441c45bc7f7646`.

Evidence:
- diff, parent 1, numbered lines1–2740; complete move pairing plus full residual delta read.
- message, parent 1, numbered lines1–10; full message read.

Changed paths: `.vscode/settings.json`, `CMakeLists.txt`, `src/spyglass/core/log.cpp`, `src/spyglass/core/log.h`, `src/spyglass/core/output.cpp`, `src/spyglass/core/output.h`, `src/spyglass/core/time.cpp`, `src/spyglass/core/time.h`, `src/spyglass/hook.cpp`, `src/spyglass/hook.h`, `src/spyglass/hook/function_hook.cpp`, `src/spyglass/hook/function_hook.h`, `src/spyglass/hook/host_symbol.cpp`, `src/spyglass/hook/host_symbol.h`, `src/spyglass/main.cpp`, `src/spyglass/overlay/android/host_symbol.cpp`, `src/spyglass/overlay/android/host_symbol.h`, `src/spyglass/overlay/android/launcher_overlay.cpp`, `src/spyglass/overlay/backend.h`, `src/spyglass/overlay/d3d11_backend.cpp`, `src/spyglass/overlay/d3d11_backend.h`, `src/spyglass/overlay/d3d12_backend.cpp`, `src/spyglass/overlay/d3d12_backend.h`, `src/spyglass/overlay/input.cpp`, `src/spyglass/overlay/input.h`, `src/spyglass/overlay/install.h`, `src/spyglass/overlay/launcher_overlay.cpp`, `src/spyglass/overlay/overlay.cpp`, `src/spyglass/overlay/overlay.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`, `src/spyglass/overlay/windows/backend.h`, `src/spyglass/overlay/windows/d3d11_backend.cpp`, `src/spyglass/overlay/windows/d3d11_backend.h`, `src/spyglass/overlay/windows/d3d12_backend.cpp`, `src/spyglass/overlay/windows/d3d12_backend.h`, `src/spyglass/overlay/windows/input.cpp`, `src/spyglass/overlay/windows/input.h`, `src/spyglass/overlay/windows/overlay.cpp`, `src/spyglass/overlay/windows/overlay.h`.

<a id="commit-011"></a>
## 011. name the Android overlay after what it is {#commit-011}
[0fe98094c447abcb9a1806e6b7a2d7b9943dcddc](https://github.com/EndstoneMC/spyglass/commit/0fe98094c447abcb9a1806e6b7a2d7b9943dcddc) · authored 2026-08-27T23:07:51Z · committed 2026-08-27T23:07:51Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 8dcb223d693c88d99337215bb5441c45bc7f7646.

Byte-identical Android launcher_overlay.cpp -> overlay.cpp move, verified over entire source body; updates CMake only. Explicit naming rationale: the launcher is how context is found, not what the overlay is. No new runtime lesson.

Knowledge identity: `knowledge:commit:0fe98094c447abcb9a1806e6b7a2d7b9943dcddc`.

Evidence:
- diff, parent 1, numbered lines1–193; complete move pairing plus full residual delta read.
- message, parent 1, numbered lines1–4; full message read.

Changed paths: `CMakeLists.txt`, `src/spyglass/overlay/android/launcher_overlay.cpp`, `src/spyglass/overlay/android/overlay.cpp`.

<a id="commit-012"></a>
## 012. shorten host_symbol to symbol {#commit-012}
[619cc6929c7f50abdaa0adff7f592ba8c63499aa](https://github.com/EndstoneMC/spyglass/commit/619cc6929c7f50abdaa0adff7f592ba8c63499aa) · authored 2026-08-27T23:08:25Z · committed 2026-08-27T23:08:25Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 0fe98094c447abcb9a1806e6b7a2d7b9943dcddc.

Entire old/new symbol files compared. Header byte-identical; implementation include path changes; CMake and consumer include updated. Function host_symbol retains its name because it distinguishes host executable from a library symbol. This is a precise file-name shortening, not a recommendation to erase semantic distinctions.

Knowledge identity: `knowledge:commit:619cc6929c7f50abdaa0adff7f592ba8c63499aa`.

Evidence:
- diff, parent 1, numbered lines1–321; complete move pairing plus full residual delta read.
- message, parent 1, numbered lines1–5; full message read.

Changed paths: `CMakeLists.txt`, `src/spyglass/overlay/android/host_symbol.cpp`, `src/spyglass/overlay/android/host_symbol.h`, `src/spyglass/overlay/android/overlay.cpp`, `src/spyglass/overlay/android/symbol.cpp`, `src/spyglass/overlay/android/symbol.h`.

<a id="commit-013"></a>
## 013. port the injector {#commit-013}
[406b845ed497fdec304018c43c417e273f5420b3](https://github.com/EndstoneMC/spyglass/commit/406b845ed497fdec304018c43c417e273f5420b3) · authored 2026-08-27T23:09:46Z · committed 2026-08-27T23:09:46Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 619cc6929c7f50abdaa0adff7f592ba8c63499aa.

Ports injector with RAII process/local handles, Windows error text, process/module checks, canonical payload path, UAC runas relaunch preserving arguments/current directory/child exit code, app-package read/execute ACL grant, remote LoadLibraryW and error-only console hold precursor. Read-only review: none of these security-sensitive operations were executed. Message says unchanged port from main. /DEBUG:NONE for injector avoids its spyglass.pdb colliding with same-base-name payload PDB. Packaging and process permissions are part of deployment behavior; not general authority for an assistant to perform injection or ACL changes.

Knowledge identity: `knowledge:commit:406b845ed497fdec304018c43c417e273f5420b3`.

Evidence:
- diff, parent 1, numbered lines1–334; full semantic diff read.
- message, parent 1, numbered lines1–10; full message read.

Changed paths: `CMakeLists.txt`, `src/injector/main.cpp`.

<a id="commit-014"></a>
## 014. draw the overlay in Mojangles on Windows {#commit-014}
[2f5cb9436f84996e32f3010ec74f558036893edb](https://github.com/EndstoneMC/spyglass/commit/2f5cb9436f84996e32f3010ec74f558036893edb) · authored 2026-08-27T23:15:36Z · committed 2026-08-27T23:15:36Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 406b845ed497fdec304018c43c417e273f5420b3.

Windows discovers Mojangles relative to executable package root; no version/install path hardcoding. Pixel snapping and no oversampling match pixel-font rendering. NoLoadError avoids assertion if missing, permitting default font fallback. Android inherits launcher font. Explicit platform ownership explains the asymmetry.

Knowledge identity: `knowledge:commit:2f5cb9436f84996e32f3010ec74f558036893edb`.

Evidence:
- diff, parent 1, numbered lines1–35; full semantic diff read.
- message, parent 1, numbered lines1–13; full message read.

Changed paths: `src/spyglass/overlay/windows/overlay.cpp`.

<a id="commit-015"></a>
## 015. show the overlay as soon as it attaches {#commit-015}
[09a8a846a6e419da2c31886f8a2d6983cf9bba79](https://github.com/EndstoneMC/spyglass/commit/09a8a846a6e419da2c31886f8a2d6983cf9bba79) · authored 2026-08-27T23:20:43Z · committed 2026-08-27T23:20:43Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 2f5cb9436f84996e32f3010ec74f558036893edb.

Changes overlay initial visibility to true. Explicit UX rationale: injection is deliberate, so show its result without another action; hotkeys still hide it. One-bit behavior change, no general always-show preference.

Knowledge identity: `knowledge:commit:09a8a846a6e419da2c31886f8a2d6983cf9bba79`.

Evidence:
- diff, parent 1, numbered lines1–13; full semantic diff read.
- message, parent 1, numbered lines1–4; full message read.

Changed paths: `src/spyglass/overlay/view.h`.

<a id="commit-016"></a>
## 016. close the injector window when the injection worked {#commit-016}
[a39e5b1970597053c56e7cd05430727f89d9128f](https://github.com/EndstoneMC/spyglass/commit/a39e5b1970597053c56e7cd05430727f89d9128f) · authored 2026-08-27T23:20:43Z · committed 2026-08-27T23:20:43Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 09a8a846a6e419da2c31886f8a2d6983cf9bba79.

ConsoleHold gains success flag: double-click error remains visible but successful injector exits automatically. Existing terminal process ownership check retained. The purpose is error readability without a redundant success confirmation.

Knowledge identity: `knowledge:commit:a39e5b1970597053c56e7cd05430727f89d9128f`.

Evidence:
- diff, parent 1, numbered lines1–34; full semantic diff read.
- message, parent 1, numbered lines1–4; full message read.

Changed paths: `src/injector/main.cpp`.
