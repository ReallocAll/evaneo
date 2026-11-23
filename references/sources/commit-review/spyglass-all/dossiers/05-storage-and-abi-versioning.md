<!-- retrieval: {"source_ids":["public:commit:0c5b33e4cc18c1b5c860cd87ca4bc670d6099dc8","public:commit:2fe2e8f4334520db1a94187596723b2e0ff23140","public:commit:630ead8356a03eaf7696c40d852c92a89430737a","public:commit:927799d004bb31f4cb120767b7de7870221f3e0a","public:commit:9ea7149cdeaf8d9363424633f0db66cb20751886","public:commit:adcfb66cca74ff57fffb0ad9aa1f53994b0826ce","public:commit:b4f5f7f879ec0089d353093ee15e6770caf7c1b0","public:commit:bcd70451ec172b22bef29e1355f4e96fa1932360","public:commit:ce9a123f2f6c7996bbe420f3da08634e38240bab"],"source_type":"public","date":"2026-08-29..2026-08-31","topics":["lifetime","concurrency","ffi","performance","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="disk-capture-gpu-lifetime-and-versioned-abi"></a>
# Disk capture, GPU lifetime and versioned ABI {#disk-capture-gpu-lifetime-and-versioned-abi}

Disk backing changes the resource model rather than eliminating limits. Network-thread work, writer queues, index paging, field caches and exports have different budgets and lifetimes. Fences and the actual resize entrypoint fix two separate Direct3D12 hazards. The typed JSON transition improves retained fidelity while moving truncation, recursion and allocation tradeoffs elsewhere.

This dossier separates observed code changes from explicit commit-message rationale and review inference. The original patches are available through the public commit links in each entry. Author-reported measurements and client checks were not repeated.

<a id="commit-070"></a>
## 070. stream the capture to disk {#commit-070}
[b4f5f7f879ec0089d353093ee15e6770caf7c1b0](https://github.com/EndstoneMC/spyglass/commit/b4f5f7f879ec0089d353093ee15e6770caf7c1b0) · authored 2026-08-29T19:41:05Z · committed 2026-08-29T19:41:05Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 8a791412d64c7a4ea8c0679a414b069f188cb3f2.

Replaces in-memory age-evicting deque with asynchronous disk-backed capture: bounded producer queue (4MiB/4096 entries defaults),32-byte metadata entries,8192-entry paged index blocks, separate body/index streams and256-field cache. Drops overload rather than blocks client thread, tallies failures and lightweight status, streams exports and slices body search per frame. Distinguishes accepted versus written counts; no body reads for list/filter except index paging, so message's absolute 'no file read' is too broad once metadata evicts. Scratch files have magic/version and length framing, separate liveness lock and stale sweep. Returns all reflection to lazy to avoid network work and shared global tag-counter race;73 reverses for fidelity. Source-only risks include detached writer destructor lifetime, restart concurrent batch ownership, post-write counters without write-success check, newly loaded oldest block possibly immediately evicted, and unbounded auxiliary rates/block slots despite body bounds; not a runtime failure claim.72 confirms one concrete Windows lock bug. No disk capture or client injection run.

Knowledge identity: `knowledge:commit:b4f5f7f879ec0089d353093ee15e6770caf7c1b0`.

Evidence:
- diff, parent 1, numbered lines1–2327; full semantic diff read.
- message, parent 1, numbered lines1–51; full message read.

Changed paths: `CHANGELOG.md`, `CMakeLists.txt`, `README.md`, `src/spyglass/install.cpp`, `src/spyglass/network.cpp`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/export.cpp`, `src/spyglass/overlay/navigate.cpp`, `src/spyglass/overlay/navigate.h`, `src/spyglass/overlay/pane/expert_window.cpp`, `src/spyglass/overlay/pane/expert_window.h`, `src/spyglass/overlay/pane/menu_bar.cpp`, `src/spyglass/overlay/pane/packet_bytes.cpp`, `src/spyglass/overlay/pane/packet_bytes.h`, `src/spyglass/overlay/pane/packet_details.cpp`, `src/spyglass/overlay/pane/packet_details.h`, `src/spyglass/overlay/pane/packet_list.cpp`, `src/spyglass/overlay/pane/packet_list.h`, `src/spyglass/overlay/pane/statistics_window.cpp`, `src/spyglass/overlay/pane/status_bar.cpp`, `src/spyglass/overlay/report.cpp`, `src/spyglass/overlay/report.h`, `src/spyglass/overlay/store.cpp`, `src/spyglass/overlay/store.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`.

<a id="commit-071"></a>
## 071. fence the D3D12 backend {#commit-071}
[0c5b33e4cc18c1b5c860cd87ca4bc670d6099dc8](https://github.com/EndstoneMC/spyglass/commit/0c5b33e4cc18c1b5c860cd87ca4bc670d6099dc8) · authored 2026-08-29T23:07:42Z · committed 2026-08-29T23:07:42Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: b4f5f7f879ec0089d353093ee15e6770caf7c1b0.

Adds dedicated D3D12 fence/event: signal after overlay submission, wait before resetting each frame allocator, drain before buffer release and shutdown. Explicit cause: game's own bgfx fence occurs before Present-hook overlay work and cannot cover it; swapchain rotation only hid missing synchronization. Does not assume host completion guarantees plugin completion. Source handles fence/event creation failure; signal HRESULT is not checked and infinite wait path is not runtime-verified.74 fixes separate missed resize entrypoint.

Knowledge identity: `knowledge:commit:0c5b33e4cc18c1b5c860cd87ca4bc670d6099dc8`.

Evidence:
- diff, parent 1, numbered lines1–99; full semantic diff read.
- message, parent 1, numbered lines1–13; full message read.

Changed paths: `src/spyglass/overlay/windows/d3d12_backend.cpp`, `src/spyglass/overlay/windows/d3d12_backend.h`.

<a id="commit-072"></a>
## 072. lock a byte the capture never writes {#commit-072}
[2fe2e8f4334520db1a94187596723b2e0ff23140](https://github.com/EndstoneMC/spyglass/commit/2fe2e8f4334520db1a94187596723b2e0ff23140) · authored 2026-08-29T23:37:49Z · committed 2026-08-29T23:37:49Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 0c5b33e4cc18c1b5c860cd87ca4bc670d6099dc8.

Moves Windows liveness lock from byte0 to remote offset0x40000000<<32, because mandatory per-handle byte locks blocked the store's own header write. Author reports empty cap with healthy index/list and increasing counter, making silent failure deceptive. Adds writer failure reporting. Source still publishes batch counters after detected write failure, so reporting is not equivalent to transactional successful persistence. Preserves concrete causal diagnostic and observability lesson, no reproduced runtime result.

Knowledge identity: `knowledge:commit:2fe2e8f4334520db1a94187596723b2e0ff23140`.

Evidence:
- diff, parent 1, numbered lines1–34; full semantic diff read.
- message, parent 1, numbered lines1–16; full message read.

Changed paths: `src/spyglass/overlay/store.cpp`.

<a id="commit-073"></a>
## 073. keep a packet's decoded fields with the packet {#commit-073}
[ce9a123f2f6c7996bbe420f3da08634e38240bab](https://github.com/EndstoneMC/spyglass/commit/ce9a123f2f6c7996bbe420f3da08634e38240bab) · authored 2026-08-29T23:38:07Z · committed 2026-08-29T23:38:07Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 2fe2e8f4334520db1a94187596723b2e0ff23140.

Reintroduces eager inbound fields and stores them beside body/error, because replay forced CerealOnly/primary subclient cannot reproduce partially decoded original object. Outbound remains lazy with append-only .fields sidecar and per-number offsets; opt-in tree read avoids parsing every display frame. Adds thread_local tag counter for network/render coexistence. This explicitly reverses70's latency choice for fidelity and introduces eager serialization overhead; later79/93 reconsider balance. Changelog resize claim appears before74 implementation in this ordering, so documentation alone is not completion evidence.

Knowledge identity: `knowledge:commit:ce9a123f2f6c7996bbe420f3da08634e38240bab`.

Evidence:
- diff, parent 1, numbered lines1–395; full semantic diff read.
- message, parent 1, numbered lines1–28; full message read.

Changed paths: `CHANGELOG.md`, `src/spyglass/network.cpp`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/store.cpp`, `src/spyglass/overlay/store.h`, `src/spyglass/reflect.cpp`.

<a id="commit-074"></a>
## 074. hook the resize the client actually calls {#commit-074}
[927799d004bb31f4cb120767b7de7870221f3e0a](https://github.com/EndstoneMC/spyglass/commit/927799d004bb31f4cb120767b7de7870221f3e0a) · authored 2026-08-29T23:39:58Z · committed 2026-08-29T23:39:58Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: ce9a123f2f6c7996bbe420f3da08634e38240bab.

Hooks actual IDXGISwapChain3::ResizeBuffers1 slot39 in addition to original slot13. Author traces held overlay buffer refs -> failed HRESULT -> bgfx fatal -> terminate/abort on window drag, and reports dxgi bodies do not forward. Probe uses QueryInterface to obtain valid versioned vtable; both detours release/drain before native resize. Strong example of actual call-path evidence correcting a plausible API-name hook. No crash reproduction performed.

Knowledge identity: `knowledge:commit:927799d004bb31f4cb120767b7de7870221f3e0a`.

Evidence:
- diff, parent 1, numbered lines1–114; full semantic diff read.
- message, parent 1, numbered lines1–13; full message read.

Changed paths: `src/spyglass/overlay/windows/overlay.cpp`, `src/spyglass/overlay/windows/overlay.h`.

<a id="commit-075"></a>
## 075. Improve export functions {#commit-075}
[9ea7149cdeaf8d9363424633f0db66cb20751886](https://github.com/EndstoneMC/spyglass/commit/9ea7149cdeaf8d9363424633f0db66cb20751886) · authored 2026-08-31T15:30:05Z · committed 2026-08-31T15:30:05Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 927799d004bb31f4cb120767b7de7870221f3e0a.

Replaces immediate hardcoded exports with overlay-native save browser, packet scope/selection/range choices, text/CSV/JSON and raw selected-byte output, filename/platform validation, UTF-8 paths, overwrite dialog, size estimates and progress/cancel. Export snapshots options/filter/marks/written limit;12-ms budget checked every32 records streams to .part then rename, cancellation removes temporary file. This is cooperative frame work, not hard latency bound: one packet or32 heavy records can exceed budget; summary scan and directory listing remain synchronous. Estimates are heuristic, CSV always includes body despite disabled bytes checkbox; initial JSON fields are display label trees, changed78. Platform rename replacement semantics and restart-generation coherence are not tested. Pinned nlohmann JSON v3.12.0 used with replacement for invalid text. All674-line dialog and backend paths reviewed, not merely user-facing changelog.

Knowledge identity: `knowledge:commit:9ea7149cdeaf8d9363424633f0db66cb20751886`.

Evidence:
- diff, parent 1, numbered lines1–1816; full semantic diff read.
- message, parent 1, numbered lines1–1; full message read.

Changed paths: `CHANGELOG.md`, `CMakeLists.txt`, `README.md`, `src/spyglass/core/output.cpp`, `src/spyglass/core/output.h`, `src/spyglass/overlay/export.cpp`, `src/spyglass/overlay/export.h`, `src/spyglass/overlay/options.h`, `src/spyglass/overlay/pane/export_dialog.cpp`, `src/spyglass/overlay/pane/export_dialog.h`, `src/spyglass/overlay/pane/menu_bar.cpp`, `src/spyglass/overlay/pane/packet_bytes.cpp`, `src/spyglass/overlay/pane/packet_bytes.h`, `src/spyglass/overlay/report.cpp`, `src/spyglass/overlay/report.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`, `third_party/CMakeLists.txt`, `third_party/nlohmann_json/CMakeLists.txt`.

<a id="commit-076"></a>
## 076. build a payload per client version {#commit-076}
[bcd70451ec172b22bef29e1355f4e96fa1932360](https://github.com/EndstoneMC/spyglass/commit/bcd70451ec172b22bef29e1355f4e96fa1932360) · authored 2026-08-31T16:22:00Z · committed 2026-08-31T16:22:00Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 9ea7149cdeaf8d9363424633f0db66cb20751886.

Major compatibility boundary: one payload per client line because EnTT/cereal ABI changed at1.26.50, separate pinned EnTT targets, compile-time mirror offsets/member flag changes and patterns. Injector selects highest same-channel floor<=client version from filename; package identity encodes version and preview. verify_client rejects channel mismatch/older floor on Windows before network hooks; Android check empty and later version upper bound not enforced, so broad no-wrong-client/no-hooks wording exceeds exact guards (overlay installed first). Failure of overlay itself now uses external messagebox/Android log because its error window cannot exist. Message candidly states new descriptor offsets inferred from eight-byte Linux protocol-dumper shrink and only reported confirmed by1.26.50.27 field rendering, not direct binary offsets. Preserve this uncertainty and multi-version dependency exception rather than global single-version maxim.

Knowledge identity: `knowledge:commit:bcd70451ec172b22bef29e1355f4e96fa1932360`.

Evidence:
- diff, parent 1, numbered lines1–956; full semantic diff read.
- message, parent 1, numbered lines1–32; full message read.

Changed paths: `CHANGELOG.md`, `CLAUDE.md`, `CMakeLists.txt`, `README.md`, `src/bedrock/cereal/schema/basic_schema.h`, `src/bedrock/version.h`, `src/injector/main.cpp`, `src/spyglass/install.cpp`, `src/spyglass/network.cpp`, `src/spyglass/reflect.cpp`, `src/spyglass/signature.cpp`, `src/spyglass/signature.h`, `third_party/entt/CMakeLists.txt`.

<a id="commit-077"></a>
## 077. identify a client that has no package identity {#commit-077}
[adcfb66cca74ff57fffb0ad9aa1f53994b0826ce](https://github.com/EndstoneMC/spyglass/commit/adcfb66cca74ff57fffb0ad9aa1f53994b0826ce) · authored 2026-08-31T16:39:10Z · committed 2026-08-31T16:39:10Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: bcd70451ec172b22bef29e1355f4e96fa1932360.

Adds complementary standalone-client identification: package identity first, process image file-version resource plus preview marker fallback; payload reads its own mapped version resource. Explicit installation difference: Xbox image may lack resources, extracted launcher image may lack package identity. Errors emitted only after all methods fail, avoiding misleading intermediate failure. Author reports local1.26.40.5 resource/marker check; not reproduced here. Existing explicit --dll escape path and floor checks retained.

Knowledge identity: `knowledge:commit:adcfb66cca74ff57fffb0ad9aa1f53994b0826ce`.

Evidence:
- diff, parent 1, numbered lines1–186; full semantic diff read.
- message, parent 1, numbered lines1–20; full message read.

Changed paths: `CMakeLists.txt`, `src/injector/main.cpp`, `src/spyglass/signature.cpp`.

<a id="commit-078"></a>
## 078. keep a packet's fields as the values they are {#commit-078}
[630ead8356a03eaf7696c40d852c92a89430737a](https://github.com/EndstoneMC/spyglass/commit/630ead8356a03eaf7696c40d852c92a89430737a) · authored 2026-08-31T16:52:47Z · committed 2026-08-31T16:52:47Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: adcfb66cca74ff57fffb0ad9aa1f53994b0826ce.

Replaces label/children display trees with nlohmann::ordered_json values and shared immutable Fields caches: native booleans, signed/unsigned 64-bit integers and floating values; enums/UUID/diagnostics and most NBT scalars remain strings. Full text/bytes are retained, with display-only truncation and an atob(BASE64) string convention for binary. Reads byte-vector backing memory directly when array/vector shape matches. MessagePack version2 capture replaces bespoke recursive Node encoding, queue budget rises4MiB->16MiB, error frames/causes become structured. Removes the general append/append_members depth guard while keeping NBT depth16/node4096 and error depth16; recursion risks established49 are not disproved. UTF8-ish validation checks continuation structure but not all Unicode legality; JSON export replacement policy may still be lossy. Duplicate names get suffixes, but associative KeyIndex plumbing remains dead until91. Message says MessagePack cannot throw because it does not validate UTF8; allocation/type exceptions remain possible, and pack call is outside catch. Whole1697-line diff reviewed, no serialization/runtime execution. This is a substantial data-model change, not only display formatting.

Knowledge identity: `knowledge:commit:630ead8356a03eaf7696c40d852c92a89430737a`.

Evidence:
- diff, parent 1, numbered lines1–1697; full semantic diff read.
- message, parent 1, numbered lines1–28; full message read.

Changed paths: `CHANGELOG.md`, `src/spyglass/network.cpp`, `src/spyglass/overlay/bytes.cpp`, `src/spyglass/overlay/bytes.h`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/export.cpp`, `src/spyglass/overlay/pane/packet_details.cpp`, `src/spyglass/overlay/report.cpp`, `src/spyglass/overlay/report.h`, `src/spyglass/overlay/store.cpp`, `src/spyglass/overlay/store.h`, `src/spyglass/reflect.cpp`, `src/spyglass/reflect.h`.
