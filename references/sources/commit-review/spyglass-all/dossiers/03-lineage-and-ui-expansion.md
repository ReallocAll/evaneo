<!-- retrieval: {"source_ids":["public:commit:1e83001c5f67c327b7775aadda47e4b53434ae23","public:commit:49d0d1896c3bdf21bdb9365f6f6b6e1afc7b9875","public:commit:529317bc416c720cbbf2ff1e58bfdc42347464dc","public:commit:675c73c35694a0e94673f95d8b01430eda9029c0","public:commit:b93630e262c060f287f9f9ae1eafc878c33fc053","public:commit:b98bab128c5d790254eb44eb1878fa36cc32e5fa","public:commit:d66e3bac66ab10f300c4b24c33390491f6cc1569","public:commit:ebc56a336957263b6deba852899434b1c12e9407","public:commit:ebd0a6909958961c69b315e3e1a8175f35b3adb2","public:commit:f44c31f372a1765904a6d835006e9ddc3abee120","public:commit:fead20ca5cca48b42ae0f5ba958b82212d654e38","public:thread:EndstoneMC/spyglass:1"],"source_type":"public","date":"2026-08-15..2026-08-28","topics":["lifetime","concurrency","ffi","build","performance","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="legacy-ancestry-collaborator-integration-and-ui-growth"></a>
# Legacy ancestry, collaborator integration and UI growth {#legacy-ancestry-collaborator-integration-and-ui-growth}

Topological order intentionally places the legacy branch here rather than sorting by date. Five target legacy changes and irrld’s imported branch are ancestors of a history-only merge whose first-parent rewrite tree is unchanged. File or commit volume is not novelty, and a merge is not authorship of all imported code. The UI then grows and quickly reverses an overcomplicated filter design.

This dossier separates observed code changes from explicit commit-message rationale and review inference. The original patches are available through the public commit links in each entry. Author-reported measurements and client checks were not repeated.

<a id="commit-037"></a>
## 037. Stop emitting a .pdb for the injector {#commit-037}
[ebd0a6909958961c69b315e3e1a8175f35b3adb2](https://github.com/EndstoneMC/spyglass/commit/ebd0a6909958961c69b315e3e1a8175f35b3adb2) · authored 2026-08-15T14:00:34Z · committed 2026-08-15T14:00:34Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 51a64af3b5f3d674087a7604fb6f3c370780448c.

Legacy-lineage injector disables PDB generation (/DEBUG:NONE) to prevent same-basename payload/injector symbol collision and avoid useless launcher size. Message reports 283-KiB to 59-KiB reduction; that is author measurement, not this review's reproduction. Rewrite injector port 13 preserves the choice.

Knowledge identity: `knowledge:commit:ebd0a6909958961c69b315e3e1a8175f35b3adb2`.

Evidence:
- diff, parent 1, numbered lines1–16; full semantic diff read.
- message, parent 1, numbered lines1–5; full message read.

Changed paths: `CMakeLists.txt`.

<a id="commit-038"></a>
## 038. Ask for elevation instead of telling the user to go and get it {#commit-038}
[b93630e262c060f287f9f9ae1eafc878c33fc053](https://github.com/EndstoneMC/spyglass/commit/b93630e262c060f287f9f9ae1eafc878c33fc053) · authored 2026-08-15T14:00:34Z · committed 2026-08-15T14:00:34Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: ebd0a6909958961c69b315e3e1a8175f35b3adb2.

Legacy injector relaunches through UAC, preserving raw command-line quoting, current directory and child exit code; cancellation/errors remain visible through console lifetime handling. It is deployment privilege flow, not authorization to execute injection. Rewrite 13 ports it and 16 later closes the successful double-click path automatically.

Knowledge identity: `knowledge:commit:b93630e262c060f287f9f9ae1eafc878c33fc053`.

Evidence:
- diff, parent 1, numbered lines1–139; full semantic diff read.
- message, parent 1, numbered lines1–13; full message read.

Changed paths: `README.md`, `src/injector/main.cpp`.

<a id="commit-039"></a>
## 039. Scale the overlay to the window's DPI {#commit-039}
[1e83001c5f67c327b7775aadda47e4b53434ae23](https://github.com/EndstoneMC/spyglass/commit/1e83001c5f67c327b7775aadda47e4b53434ae23) · authored 2026-08-15T14:00:34Z · committed 2026-08-15T14:00:34Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: b93630e262c060f287f9f9ae1eafc878c33fc053.

Legacy Windows overlay recomputes style from default on DPI changes, avoiding cumulative scaling, and scales font rasterization without changing the host application's DPI-awareness contract. This is ownership-aware integration into a host, not a universal process-level DPI setting. Rewrite overlay inherits the implementation.

Knowledge identity: `knowledge:commit:1e83001c5f67c327b7775aadda47e4b53434ae23`.

Evidence:
- diff, parent 1, numbered lines1–68; full semantic diff read.
- message, parent 1, numbered lines1–11; full message read.

Changed paths: `src/spyglass/overlay/overlay.cpp`, `src/spyglass/overlay/overlay.h`.

<a id="commit-040"></a>
## 040. Take out the knobs and the machinery built for more than one hook {#commit-040}
[b98bab128c5d790254eb44eb1878fa36cc32e5fa](https://github.com/EndstoneMC/spyglass/commit/b98bab128c5d790254eb44eb1878fa36cc32e5fa) · authored 2026-08-19T14:22:15Z · committed 2026-08-19T14:22:15Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 1e83001c5f67c327b7775aadda47e4b53434ae23.

Legacy simplification removes five environment knobs, redundant latest report output and single-use enum/map/casting machinery; fixes raw/history limits and always reports trailing bytes, with future UI controls proposed. Original functions are published before live hooks; Direct3D atomics are removed under install-order/single-write reasoning. Critically, member readNoHeader is replaced with a free-function Packet* signature; rewrite root guidance later identifies MSVC hidden return-buffer/this register inversion from this approach, and rewrite 25 restores a true member detour. This is an important failed abstraction-removal counterexample. Patch also avoids error.message allocation across CRT boundaries and removes recursion guard; these constraints should not silently be projected to later code that changes them.

Knowledge identity: `knowledge:commit:b98bab128c5d790254eb44eb1878fa36cc32e5fa`.

Evidence:
- diff, parent 1, numbered lines1–1502; full semantic diff read.
- message, parent 1, numbered lines1–20; full message read.

Changed paths: `README.md`, `src/bedrock/network/packet.h`, `src/injector/main.cpp`, `src/spyglass/core/config.cpp`, `src/spyglass/core/config.h`, `src/spyglass/core/log.cpp`, `src/spyglass/core/output.cpp`, `src/spyglass/core/output.h`, `src/spyglass/diagnostics/builder.cpp`, `src/spyglass/diagnostics/builder.h`, `src/spyglass/diagnostics/diagnostic.h`, `src/spyglass/diagnostics/format.cpp`, `src/spyglass/diagnostics/format.h`, `src/spyglass/diagnostics/sink.cpp`, `src/spyglass/diagnostics/sink.h`, `src/spyglass/diagnostics/store.cpp`, `src/spyglass/diagnostics/store.h`, `src/spyglass/dllmain.cpp`, `src/spyglass/hook/detail.h`, `src/spyglass/hook/function_hook.cpp`, `src/spyglass/hook/function_hook.h`, `src/spyglass/hook/packet.cpp`, `src/spyglass/hook/packet.h`, `src/spyglass/hook/pattern.cpp`, `src/spyglass/hook/pattern.h`, `src/spyglass/hook/target.cpp`, `src/spyglass/hook/target.h`, `src/spyglass/overlay/backend.h`, `src/spyglass/overlay/d3d12_backend.cpp`, `src/spyglass/overlay/d3d12_backend.h`, `src/spyglass/overlay/input.h`, `src/spyglass/overlay/overlay.cpp`, `src/spyglass/overlay/overlay.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`.

<a id="commit-041"></a>
## 041. Cut releases from a workflow, and keep a changelog {#commit-041}
[675c73c35694a0e94673f95d8b01430eda9029c0](https://github.com/EndstoneMC/spyglass/commit/675c73c35694a0e94673f95d8b01430eda9029c0) · authored 2026-08-19T14:37:28Z · committed 2026-08-19T14:37:28Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: b98bab128c5d790254eb44eb1878fa36cc32e5fa.

Legacy release workflow turns ephemeral CI artifacts into versioned public assets with main/semver/tag/changelog checks and a dry-run validation path, using Windows Conan build and explicit symbol separation. Later rewrite 36 changes dependency and dual-platform packaging. Source intent and checks observed, not executed workflow success.

Knowledge identity: `knowledge:commit:675c73c35694a0e94673f95d8b01430eda9029c0`.

Evidence:
- diff, parent 1, numbered lines1–222; full semantic diff read.
- message, parent 1, numbered lines1–14; full message read.

Changed paths: `.github/workflows/release.yml`, `CHANGELOG.md`, `README.md`.

<a id="commit-042"></a>
## 042. Merge pull request #1 from irrld/linux-launcher {#commit-042}
[f44c31f372a1765904a6d835006e9ddc3abee120](https://github.com/EndstoneMC/spyglass/commit/f44c31f372a1765904a6d835006e9ddc3abee120) · authored 2026-08-19T17:56:47Z · committed 2026-08-19T17:56:47Z

Attribution: Merge by the commit author of irrld’s branch; imported implementation is attributed to the collaborator, and the head tree equals the second parent.
Parents: 1075fba8e0ea5b306ac11c1bbe53dea496ff6bfe, ca758c8a66bdd6eeaab77f07c1952f1b35894148.

Merge of collaborator irrld's ten-commit Android launcher branch into legacy history. Head tree equals second parent exactly, so no merge-only code novelty. Full first-parent patch read: host ImGui symbols/allocator/context sharing, explicit MSVC versus libc++ ABI layouts, bionic launcher entry, platform logs/output, stream capture, census and body retention, raw SPYG version-1 recording and file-based clipboard fallback. Android outbound experiment resolves RTTI/typeinfo/vtable through ELF relocations, validates candidate tables, mprotects pages and optionally patches write slot 6 using a generic six-pointer dispatcher; ambiguous self recovery restores hooks, and outbound records lack raw bodies at this point. This ABI/permission-sensitive strategy belongs to imported collaborator work, not wholly Vincent originality. UI distinguishes decoder-thread IDs, held body snapshots, keep-bodies/record/watch-sends controls and clipped latest-first traffic, limits visible hex to 4096 characters while saving full body. No upstream build/runtime was executed, and broad range checks are not a pointer-safety proof. Rewrite 43 deliberately does not adopt this tree but 9/13 had explicitly ported selected prior work. Public PR1 metadata later verifies exact base/head/merge and irrld authorship; the sole returned review is an empty APPROVED submission by xRookieFight, with no rationale to infer.

Knowledge identity: `knowledge:commit:f44c31f372a1765904a6d835006e9ddc3abee120`.

Evidence:
- diff, parent 1, numbered lines1–2283; full semantic diff read.
- diff, parent 2, numbered lines1–0; full semantic diff read.
- message, parent 1, numbered lines1–1; full message read.

Changed paths: `.gitignore`, `CMakeLists.txt`, `README.md`, `src/bedrock/bedrock.h`, `src/bedrock/core/utility/binary_stream.h`, `src/bedrock/diagnostics/log_level.h`, `src/bedrock/platform/callstack.h`, `src/bedrock/platform/check.h`, `src/bedrock/platform/result.h`, `src/spyglass/core/log.cpp`, `src/spyglass/core/output.cpp`, `src/spyglass/hook/host_symbol.cpp`, `src/spyglass/hook/host_symbol.h`, `src/spyglass/hook/outbound.cpp`, `src/spyglass/hook/outbound.h`, `src/spyglass/hook/packet.cpp`, `src/spyglass/hook/packet.h`, `src/spyglass/hook/pattern.cpp`, `src/spyglass/hook/vtables.cpp`, `src/spyglass/hook/vtables.h`, `src/spyglass/modmain.cpp`, `src/spyglass/overlay/clipboard.cpp`, `src/spyglass/overlay/clipboard.h`, `src/spyglass/overlay/launcher_overlay.cpp`, `src/spyglass/overlay/launcher_overlay.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`.

<a id="commit-043"></a>
## 043. stitch the old history back on {#commit-043}
[529317bc416c720cbbf2ff1e58bfdc42347464dc](https://github.com/EndstoneMC/spyglass/commit/529317bc416c720cbbf2ff1e58bfdc42347464dc) · authored 2026-08-28T14:26:06Z · committed 2026-08-28T14:26:06Z

Attribution: History-only merge by the commit author; head tree equals the first parent, with no new implementation.
Parents: 0a0639f0c34dbc6c6a53ca111c57a64a87cc5085, f44c31f372a1765904a6d835006e9ddc3abee120.

History-only merge restoring legacy and collaborator ancestry under the orphan rewrite. Whole-tree object identity proves head is byte-for-byte first-parent rewrite: no new implementation. All 127 second-parent changed paths and blob identities/numstats recorded in structural-043-history-merge.json. The large second-parent reconciliation is not counted as 10180 lines of novel reasoning; unique rewrite content was reviewed in 1–36 and legacy imported content in 37–42. Explicit message says existing release tags remain and comparisons become meaningful. This prevents timestamp order or merge-diff volume from distorting attribution and architecture evolution.

Knowledge identity: `knowledge:commit:529317bc416c720cbbf2ff1e58bfdc42347464dc`.

Evidence:
- diff, parent 1, numbered lines1–0; full semantic diff read.
- diff, parent 2, numbered lines1–10180; whole tree first parent equivalence plus all second parent path blob delta inventory.
- message, parent 1, numbered lines1–11; full message read.

Changed paths: `.clang-format`, `.conan2/.gitignore`, `.conan2/profiles/default`, `.conan2/remotes.json`, `.conanrc`, `.github/workflows/ci.yml`, `.github/workflows/release.yml`, `.gitignore`, `.vscode/settings.json`, `CHANGELOG.md`, `CLAUDE.md`, `CMakeLists.txt`, `CMakePresets.json`, `LICENSE`, `README.md`, `conanfile.txt`, `docs/screenshot.png`, `src/bedrock/bedrock.h`, `src/bedrock/core/utility/binary_stream.h`, `src/bedrock/diagnostics/log_level.h`, `src/bedrock/input/mouse.h`, `src/bedrock/network/batched_network_peer.h`, `src/bedrock/network/minecraft_packet_ids.h`, `src/bedrock/network/minecraft_packets.h`, `src/bedrock/network/network_connection.h`, `src/bedrock/network/network_identifier.h`, `src/bedrock/network/network_peer.h`, `src/bedrock/network/network_system.h`, `src/bedrock/network/packet.h`, `src/bedrock/platform/callstack.h`, `src/bedrock/platform/check.h`, `src/bedrock/platform/result.h`, `src/injector/main.cpp`, `src/spyglass/core/log.cpp`, `src/spyglass/core/log.h`, `src/spyglass/core/output.cpp`, `src/spyglass/core/output.h`, `src/spyglass/core/time.cpp`, `src/spyglass/core/time.h`, `src/spyglass/detail.h`, `src/spyglass/diagnostics/builder.cpp`, `src/spyglass/diagnostics/builder.h`, `src/spyglass/diagnostics/diagnostic.h`, `src/spyglass/diagnostics/format.cpp`, `src/spyglass/diagnostics/format.h`, `src/spyglass/diagnostics/sink.cpp`, `src/spyglass/diagnostics/sink.h`, `src/spyglass/diagnostics/store.cpp`, `src/spyglass/diagnostics/store.h`, `src/spyglass/dllmain.cpp`, `src/spyglass/error.cpp`, `src/spyglass/error.h`, `src/spyglass/filename.cpp`, `src/spyglass/filename.h`, `src/spyglass/filename_table.inc`, `src/spyglass/hook.cpp`, `src/spyglass/hook.h`, `src/spyglass/hook/function_hook.cpp`, `src/spyglass/hook/function_hook.h`, `src/spyglass/hook/host_symbol.cpp`, `src/spyglass/hook/host_symbol.h`, `src/spyglass/hook/outbound.cpp`, `src/spyglass/hook/outbound.h`, `src/spyglass/hook/packet.cpp`, `src/spyglass/hook/packet.h`, `src/spyglass/hook/pattern.cpp`, `src/spyglass/hook/pattern.h`, `src/spyglass/hook/vtables.cpp`, `src/spyglass/hook/vtables.h`, `src/spyglass/install.cpp`, `src/spyglass/install.h`, `src/spyglass/main.cpp`, `src/spyglass/modmain.cpp`, `src/spyglass/network.cpp`, `src/spyglass/network.h`, `src/spyglass/overlay/android/overlay.cpp`, `src/spyglass/overlay/android/symbol.cpp`, `src/spyglass/overlay/android/symbol.h`, `src/spyglass/overlay/backend.h`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/clipboard.cpp`, `src/spyglass/overlay/clipboard.h`, `src/spyglass/overlay/d3d11_backend.cpp`, `src/spyglass/overlay/d3d11_backend.h`, `src/spyglass/overlay/d3d12_backend.cpp`, `src/spyglass/overlay/d3d12_backend.h`, `src/spyglass/overlay/input.cpp`, `src/spyglass/overlay/input.h`, `src/spyglass/overlay/install.h`, `src/spyglass/overlay/launcher_overlay.cpp`, `src/spyglass/overlay/launcher_overlay.h`, `src/spyglass/overlay/overlay.cpp`, `src/spyglass/overlay/overlay.h`, `src/spyglass/overlay/pane/packet_bytes.cpp`, `src/spyglass/overlay/pane/packet_bytes.h`, `src/spyglass/overlay/pane/packet_details.cpp`, `src/spyglass/overlay/pane/packet_details.h`, `src/spyglass/overlay/pane/packet_list.cpp`, `src/spyglass/overlay/pane/packet_list.h`, `src/spyglass/overlay/pane/status_bar.cpp`, `src/spyglass/overlay/pane/status_bar.h`, `src/spyglass/overlay/pane/toolbar.cpp`, `src/spyglass/overlay/pane/toolbar.h`, `src/spyglass/overlay/theme.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`, `src/spyglass/overlay/windows/backend.h`, `src/spyglass/overlay/windows/d3d11_backend.cpp`, `src/spyglass/overlay/windows/d3d11_backend.h`, `src/spyglass/overlay/windows/d3d12_backend.cpp`, `src/spyglass/overlay/windows/d3d12_backend.h`, `src/spyglass/overlay/windows/input.cpp`, `src/spyglass/overlay/windows/input.h`, `src/spyglass/overlay/windows/mouse.cpp`, `src/spyglass/overlay/windows/mouse.h`, `src/spyglass/overlay/windows/overlay.cpp`, `src/spyglass/overlay/windows/overlay.h`, `src/spyglass/pattern.cpp`, `src/spyglass/pattern.h`, `src/spyglass/signature.cpp`, `src/spyglass/signature.h`, `third_party/CMakeLists.txt`, `third_party/expected-lite/CMakeLists.txt`, `third_party/funchook/CMakeLists.txt`, `third_party/imgui/CMakeLists.txt`, `third_party/libhat/CMakeLists.txt`.

<a id="commit-044"></a>
## 044. Add filter windows {#commit-044}
[fead20ca5cca48b42ae0f5ba958b82212d654e38](https://github.com/EndstoneMC/spyglass/commit/fead20ca5cca48b42ae0f5ba958b82212d654e38) · authored 2026-08-28T16:27:47Z · committed 2026-08-28T16:27:47Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 529317bc416c720cbbf2ff1e58bfdc42347464dc.

Adds reversible display filtering by packet type, direction and failed decode, names pre-enumerated from client factory, per-ID lifetime counts, search-scoped all/none/invert and row context actions. Incremental filtered ID deque advances over only new records, trims evicted IDs, resets when filter or session changes; unfiltered list avoids full scan. Visible filter marker and displayed-versus-retained count prevent interpreting hidden traffic as stalled capture. Removes keyboard navigation focus from destructive Restart button and avoids stealing Ctrl-F while text entry owns input. Full factory name cache initializes once; premature-empty cache is corrected much later in 97. Filter is presentation-only here.

Knowledge identity: `knowledge:commit:fead20ca5cca48b42ae0f5ba958b82212d654e38`.

Evidence:
- diff, parent 1, numbered lines1–1098; full semantic diff read.
- message, parent 1, numbered lines1–1; full message read.

Changed paths: `CHANGELOG.md`, `CMakeLists.txt`, `README.md`, `src/spyglass/network.cpp`, `src/spyglass/network.h`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/filter.cpp`, `src/spyglass/overlay/filter.h`, `src/spyglass/overlay/pane/filter_window.cpp`, `src/spyglass/overlay/pane/filter_window.h`, `src/spyglass/overlay/pane/packet_bytes.cpp`, `src/spyglass/overlay/pane/packet_list.cpp`, `src/spyglass/overlay/pane/packet_list.h`, `src/spyglass/overlay/pane/status_bar.cpp`, `src/spyglass/overlay/pane/status_bar.h`, `src/spyglass/overlay/pane/toolbar.cpp`, `src/spyglass/overlay/pane/toolbar.h`, `src/spyglass/overlay/theme.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`, `src/spyglass/overlay/windows/overlay.cpp`, `src/spyglass/signature.h`.

<a id="commit-045"></a>
## 045. lay the overlay out behind a menu bar {#commit-045}
[d66e3bac66ab10f300c4b24c33390491f6cc1569](https://github.com/EndstoneMC/spyglass/commit/d66e3bac66ab10f300c4b24c33390491f6cc1569) · authored 2026-08-28T17:04:47Z · committed 2026-08-28T17:04:47Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: fead20ca5cca48b42ae0f5ba958b82212d654e38.

Large integrated inspector UX expansion: menu-driven navigation/history/marks/time references, relative or wall clock, configurable panes/zoom, packet/body search, detached views, grouped retained decode failures, per-ID/length/rate statistics, byte interpreter, clipboard and local-file exports. Explicit reason for menus is keyboard ownership only when game releases cursor, making shortcuts intermittently available. Capture maintains counters/histograms rather than scanning deque for summary each frame, although its rates vector grows with elapsed seconds and snapshots copy it; body budget is not all-memory bound. Shared byte formatting/parsing is extracted for actual reuse; details and bytes take explicit Record so separate views work. Exports include cleartext raw bodies/base64 and docs revoke earlier no-disk claim and warn about credentials. Export path generated with seconds precision and synchronous full-string formatting under capture.visit lock; no performance/runtime success claimed. Detached windows retain numbers rather than independent record ownership at this revision. Source includes full UI wiring, report CSV escaping and byte interpreter bounds, not just menu labels.

Knowledge identity: `knowledge:commit:d66e3bac66ab10f300c4b24c33390491f6cc1569`.

Evidence:
- diff, parent 1, numbered lines1–2969; full semantic diff read.
- message, parent 1, numbered lines1–25; full message read.

Changed paths: `CHANGELOG.md`, `CMakeLists.txt`, `README.md`, `src/spyglass/core/clock.h`, `src/spyglass/core/output.cpp`, `src/spyglass/core/output.h`, `src/spyglass/network.cpp`, `src/spyglass/network.h`, `src/spyglass/overlay/bytes.cpp`, `src/spyglass/overlay/bytes.h`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/export.cpp`, `src/spyglass/overlay/export.h`, `src/spyglass/overlay/navigate.cpp`, `src/spyglass/overlay/navigate.h`, `src/spyglass/overlay/options.h`, `src/spyglass/overlay/pane/expert_window.cpp`, `src/spyglass/overlay/pane/expert_window.h`, `src/spyglass/overlay/pane/filter_window.cpp`, `src/spyglass/overlay/pane/menu_bar.cpp`, `src/spyglass/overlay/pane/menu_bar.h`, `src/spyglass/overlay/pane/packet_bytes.cpp`, `src/spyglass/overlay/pane/packet_bytes.h`, `src/spyglass/overlay/pane/packet_details.cpp`, `src/spyglass/overlay/pane/packet_details.h`, `src/spyglass/overlay/pane/packet_list.cpp`, `src/spyglass/overlay/pane/packet_list.h`, `src/spyglass/overlay/pane/statistics_window.cpp`, `src/spyglass/overlay/pane/statistics_window.h`, `src/spyglass/overlay/report.cpp`, `src/spyglass/overlay/report.h`, `src/spyglass/overlay/theme.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`, `src/spyglass/signature.h`.

<a id="commit-046"></a>
## 046. drop packets at the hook rather than only hiding them {#commit-046}
[49d0d1896c3bdf21bdb9365f6f6b6e1afc7b9875](https://github.com/EndstoneMC/spyglass/commit/49d0d1896c3bdf21bdb9365f6f6b6e1afc7b9875) · authored 2026-08-28T17:13:22Z · committed 2026-08-28T17:13:22Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: d66e3bac66ab10f300c4b24c33390491f6cc1569.

Introduces capture-time Filter inside Capture::record before retention/counters and exposes immediate-trim record/body budgets. It avoids spending retention on unwanted chunks but record construction and hook decode have already happened, so 'at the hook' is not proof of avoiding all allocation/decoding. Two nearly identical windows/buttons are separated by colors and rejected count. Message explicitly treats retention as session-dependent judgment. Entire two-filter UI is reversed next commit; preserve as an attempted alternative rather than current guidance.

Knowledge identity: `knowledge:commit:49d0d1896c3bdf21bdb9365f6f6b6e1afc7b9875`.

Evidence:
- diff, parent 1, numbered lines1–520; full semantic diff read.
- message, parent 1, numbered lines1–16; full message read.

Changed paths: `CHANGELOG.md`, `README.md`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/options.h`, `src/spyglass/overlay/pane/filter_window.cpp`, `src/spyglass/overlay/pane/filter_window.h`, `src/spyglass/overlay/pane/menu_bar.cpp`, `src/spyglass/overlay/pane/menu_bar.h`, `src/spyglass/overlay/pane/packet_list.cpp`, `src/spyglass/overlay/pane/statistics_window.cpp`, `src/spyglass/overlay/pane/status_bar.cpp`, `src/spyglass/overlay/pane/toolbar.cpp`, `src/spyglass/overlay/pane/toolbar.h`, `src/spyglass/overlay/theme.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`.

<a id="commit-047"></a>
## 047. keep one filter, and let the capture options say what is kept {#commit-047}
[ebc56a336957263b6deba852899434b1c12e9407](https://github.com/EndstoneMC/spyglass/commit/ebc56a336957263b6deba852899434b1c12e9407) · authored 2026-08-28T21:13:35Z · committed 2026-08-28T21:13:35Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 49d0d1896c3bdf21bdb9365f6f6b6e1afc7b9875.

Explicitly reverses 46's general capture filter: identical UI shapes fail to communicate irreversible omission versus reversible hiding; analogy to Wireshark is limited because its filters have distinct syntax and dialogs. Restores one display filter, retains adjustable budgets and only outbound-capture switch under Capture Options with rejected totals. Claimed halving of cost is contingent on traffic mix, not a measured guarantee. Demonstrates simplifying semantics rather than mechanically copying a mature tool's feature split.

Knowledge identity: `knowledge:commit:ebc56a336957263b6deba852899434b1c12e9407`.

Evidence:
- diff, parent 1, numbered lines1–427; full semantic diff read.
- message, parent 1, numbered lines1–15; full message read.

Changed paths: `CHANGELOG.md`, `README.md`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/options.h`, `src/spyglass/overlay/pane/filter_window.cpp`, `src/spyglass/overlay/pane/filter_window.h`, `src/spyglass/overlay/pane/menu_bar.cpp`, `src/spyglass/overlay/pane/menu_bar.h`, `src/spyglass/overlay/pane/toolbar.cpp`, `src/spyglass/overlay/pane/toolbar.h`, `src/spyglass/overlay/theme.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`.
