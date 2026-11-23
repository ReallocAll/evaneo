<!-- retrieval: {"source_ids":["public:commit:0d23eb936662137b2da4a7384f25c550f58f0299","public:commit:0e10da5bfce61c42f7d6dc9bb46847f337a37e6d","public:commit:35bf7cee473b536a5e74b438bdd8af65558cb2f5","public:commit:38aece60586f4099f5e563e17709f1d690bed1c4","public:commit:39eb6a2f2f73ed91e1e2b27ec272079c162bb869","public:commit:3cbe7236a77619e0bb4f144adfdc5848e79ce5c3","public:commit:3ce3f818c33d9494bae32cdde891d4b39d2eb7e4","public:commit:50314e8242cdb33e5a139d8d54a5d834a8ccb258","public:commit:55d4825d58d2273e5a26d47f68909d09e97a4294","public:commit:64e80c5a63fab3d6b223d81298bdef0e53f98ba5","public:commit:7d8fd820aaac80b8d800c88a23c6b973f4e56739","public:commit:8c55632510a901fe4e70af847d6e3596816ad550","public:commit:aba832d08b68f9b67545517376fcbc88f9fa0d22","public:commit:b5382dc2e9122cc10b8b1abc0f90c54f4a8fea84","public:commit:c741676170120d85d9f8636abe0cf3711abda67d","public:commit:cb80afd05586a06c2a024944b40e7940ce12de2f","public:commit:e34dd2c06d0dd2d3d1aca56da5ccdb9d24a4eb03","public:commit:f06179e5df53fc822303768a08ed458b669440b0","public:commit:f0daf169e6019adabb483813c4acafb70d697bc9","public:commit:f2ae092f05089552b5dbfbd7a014d0b6ad32faa5"],"source_type":"public","date":"2026-08-27..2026-08-28","topics":["lifetime","concurrency","ffi","testing","build","performance","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="capture-boundaries-display-identity-and-observability"></a>
# Capture boundaries, display identity and observability {#capture-boundaries-display-identity-and-observability}

The first meaningful capture boundary was wrong for inbound packets: the peer supplied batches. Per-packet read results become the source of names and errors, and owned copies separate UI lifetime from client lifetime. Synthetic failure injection is briefly present and then disabled. Source-filename recovery and input ownership require platform-specific binary evidence. Release automation is inspected as source only.

This dossier separates observed code changes from explicit commit-message rationale and review inference. The original patches are available through the public commit links in each entry. Author-reported measurements and client checks were not repeated.

<a id="commit-017"></a>
## 017. scaffold the Wireshark layout {#commit-017}
[55d4825d58d2273e5a26d47f68909d09e97a4294](https://github.com/EndstoneMC/spyglass/commit/55d4825d58d2273e5a26d47f68909d09e97a4294) · authored 2026-08-27T23:43:25Z · committed 2026-08-27T23:43:25Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: a39e5b1970597053c56e7cd05430727f89d9128f.

Creates Wireshark-shaped toolbar/list/details/bytes/status model and draggable splitters. Each pane has one public draw function receiving Capture; view owns layout. Fixture login rows and partial byte row are deliberate visual test data, not real capture results; details remain empty. Table-per-byte aligns proportional Mojangles glyph widths. Start/stop/restart are model toggles before real hooks arrive.

Knowledge identity: `knowledge:commit:55d4825d58d2273e5a26d47f68909d09e97a4294`.

Evidence:
- diff, parent 1, numbered lines1–540; full semantic diff read.
- message, parent 1, numbered lines1–17; full message read.

Changed paths: `CMakeLists.txt`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/pane/packet_bytes.cpp`, `src/spyglass/overlay/pane/packet_bytes.h`, `src/spyglass/overlay/pane/packet_details.cpp`, `src/spyglass/overlay/pane/packet_details.h`, `src/spyglass/overlay/pane/packet_list.cpp`, `src/spyglass/overlay/pane/packet_list.h`, `src/spyglass/overlay/pane/status_bar.cpp`, `src/spyglass/overlay/pane/status_bar.h`, `src/spyglass/overlay/pane/toolbar.cpp`, `src/spyglass/overlay/pane/toolbar.h`, `src/spyglass/overlay/theme.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`.

<a id="commit-018"></a>
## 018. draw the overlay font at 13 pixels {#commit-018}
[b5382dc2e9122cc10b8b1abc0f90c54f4a8fea84](https://github.com/EndstoneMC/spyglass/commit/b5382dc2e9122cc10b8b1abc0f90c54f4a8fea84) · authored 2026-08-27T23:43:25Z · committed 2026-08-27T23:43:25Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 55d4825d58d2273e5a26d47f68909d09e97a4294.

Font size 16 -> 13 pixels only. No explicit deeper rationale or independent engineering principle.

Knowledge identity: `knowledge:commit:b5382dc2e9122cc10b8b1abc0f90c54f4a8fea84`.

Evidence:
- diff, parent 1, numbered lines1–13; full semantic diff read.
- message, parent 1, numbered lines1–1; full message read.

Changed paths: `src/spyglass/overlay/windows/overlay.cpp`.

<a id="commit-019"></a>
## 019. size the panes against the window instead of pinning them {#commit-019}
[cb80afd05586a06c2a024944b40e7940ce12de2f](https://github.com/EndstoneMC/spyglass/commit/cb80afd05586a06c2a024944b40e7940ce12de2f) · authored 2026-08-27T23:53:26Z · committed 2026-08-27T23:53:26Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: b5382dc2e9122cc10b8b1abc0f90c54f4a8fea84.

Replaces fixed pixel pane heights with shares recomputed per frame; splitter drag adjusts fraction. Dynamic minimum is bounded by available space, panes live in child leaving footer fixed, main scrollbar disabled. Details stays compile-visible behind false constexpr until useful. Explicit bug: window shrink previously overflowed and scrolled status away. Source arithmetic reviewed; no visual runtime test performed.

Knowledge identity: `knowledge:commit:cb80afd05586a06c2a024944b40e7940ce12de2f`.

Evidence:
- diff, parent 1, numbered lines1–98; full semantic diff read.
- message, parent 1, numbered lines1–15; full message read.

Changed paths: `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`.

<a id="commit-020"></a>
## 020. part the offset, the hex and the text {#commit-020}
[aba832d08b68f9b67545517376fcbc88f9fa0d22](https://github.com/EndstoneMC/spyglass/commit/aba832d08b68f9b67545517376fcbc88f9fa0d22) · authored 2026-08-27T23:53:26Z · committed 2026-08-27T23:53:26Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: cb80afd05586a06c2a024944b40e7940ce12de2f.

Adds style-spacing gaps between offset/hex/text table regions rather than hardcoded width, keeping separation with style scaling. Small readability adjustment with explicit comparison to Wireshark.

Knowledge identity: `knowledge:commit:aba832d08b68f9b67545517376fcbc88f9fa0d22`.

Evidence:
- diff, parent 1, numbered lines1–47; full semantic diff read.
- message, parent 1, numbered lines1–5; full message read.

Changed paths: `src/spyglass/overlay/pane/packet_bytes.cpp`.

<a id="commit-021"></a>
## 021. draw the overlay font at 11 pixels {#commit-021}
[38aece60586f4099f5e563e17709f1d690bed1c4](https://github.com/EndstoneMC/spyglass/commit/38aece60586f4099f5e563e17709f1d690bed1c4) · authored 2026-08-27T23:53:26Z · committed 2026-08-27T23:53:26Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: aba832d08b68f9b67545517376fcbc88f9fa0d22.

Font size 13 -> 11 pixels only. Retain identity but no independent principle or test claim.

Knowledge identity: `knowledge:commit:38aece60586f4099f5e563e17709f1d690bed1c4`.

Evidence:
- diff, parent 1, numbered lines1–13; full semantic diff read.
- message, parent 1, numbered lines1–1; full message read.

Changed paths: `src/spyglass/overlay/windows/overlay.cpp`.

<a id="commit-022"></a>
## 022. add the network peer headers {#commit-022}
[50314e8242cdb33e5a139d8d54a5d834a8ccb258](https://github.com/EndstoneMC/spyglass/commit/50314e8242cdb33e5a139d8d54a5d834a8ccb258) · authored 2026-08-28T00:30:06Z · committed 2026-08-28T00:30:06Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 38aece60586f4099f5e563e17709f1d690bed1c4.

Adds Apache-noticed Endstone-derived NetworkPeer/Connection/Identifier/System reconstructions. Message argues for minimal needed ABI surface: opaque-sized identifier avoids pulling RakNet, NetworkSystem has only used methods and no unused fields. Initial identifier static size assert 176 exists; 24 changes storage/alignment and removes assertion. Attribution belongs to Endstone-derived types, not entirely novel local design.

Knowledge identity: `knowledge:commit:50314e8242cdb33e5a139d8d54a5d834a8ccb258`.

Evidence:
- diff, parent 1, numbered lines1–314; full semantic diff read.
- message, parent 1, numbered lines1–12; full message read.

Changed paths: `src/bedrock/network/batched_network_peer.h`, `src/bedrock/network/network_connection.h`, `src/bedrock/network/network_identifier.h`, `src/bedrock/network/network_peer.h`, `src/bedrock/network/network_system.h`.

<a id="commit-023"></a>
## 023. capture packets off BatchedNetworkPeer {#commit-023}
[f2ae092f05089552b5dbfbd7a014d0b6ad32faa5](https://github.com/EndstoneMC/spyglass/commit/f2ae092f05089552b5dbfbd7a014d0b6ad32faa5) · authored 2026-08-28T01:17:55Z · committed 2026-08-28T01:17:55Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 50314e8242cdb33e5a139d8d54a5d834a8ccb258.

Implements actual capture at BatchedNetworkPeer send and receive boundaries, first 4096-entry bounded mutex-protected deque, varint id, direction-derived endpoints. Detour declarations deliberately remove virtual inheritance so taking member address yields real body rather than virtual-call thunk causing recursive jumps with no useful stack. fp_cast reconstructs member pointers preserving member ABI; platform constructor helpers distinguish MSVC/Itanium. Windows scans text with libhat; Android custom executable-map scan initially lacks patterns. Both demand a unique match and refuse guesses. Install steps catch failures separately into an overlay error store. Message explicitly reports silent throws costing memory dumps; observes counterexample to preceding simplification. Later 25 corrects the assumption that receive boundary represents named individual packets.

Knowledge identity: `knowledge:commit:f2ae092f05089552b5dbfbd7a014d0b6ad32faa5`.

Evidence:
- diff, parent 1, numbered lines1–1019; full semantic diff read.
- message, parent 1, numbered lines1–22; full message read.

Changed paths: `CMakeLists.txt`, `src/bedrock/network/batched_network_peer.h`, `src/spyglass/detail.h`, `src/spyglass/error.cpp`, `src/spyglass/error.h`, `src/spyglass/hook.h`, `src/spyglass/install.cpp`, `src/spyglass/install.h`, `src/spyglass/main.cpp`, `src/spyglass/network.cpp`, `src/spyglass/network.h`, `src/spyglass/overlay/android/overlay.cpp`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/pane/packet_list.cpp`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`, `src/spyglass/overlay/windows/overlay.cpp`, `src/spyglass/overlay/windows/overlay.h`, `src/spyglass/pattern.cpp`, `src/spyglass/pattern.h`, `src/spyglass/signature.h`.

<a id="commit-024"></a>
## 024. hold NetworkIdentifier's fields as words rather than bytes {#commit-024}
[e34dd2c06d0dd2d3d1aca56da5ccdb9d24a4eb03](https://github.com/EndstoneMC/spyglass/commit/e34dd2c06d0dd2d3d1aca56da5ccdb9d24a4eb03) · authored 2026-08-28T01:17:55Z · committed 2026-08-28T01:17:55Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: f2ae092f05089552b5dbfbd7a014d0b6ad32faa5.

Changes opaque NetworkIdentifier storage from byte arrays to int64 words and removes size static_assert, plus reformatting. Actual semantic effect is increased natural alignment and resulting padding; title offers no deeper explanation. Do not label mere formatting or claim verified ABI size without target compilation. This type is soon bypassed by hooks that avoid connection layout entirely.

Knowledge identity: `knowledge:commit:e34dd2c06d0dd2d3d1aca56da5ccdb9d24a4eb03`.

Evidence:
- diff, parent 1, numbered lines1–48; full semantic diff read.
- message, parent 1, numbered lines1–1; full message read.

Changed paths: `src/bedrock/network/network_identifier.h`.

<a id="commit-025"></a>
## 025. name inbound packets off Packet::readNoHeader {#commit-025}
[0d23eb936662137b2da4a7384f25c550f58f0299](https://github.com/EndstoneMC/spyglass/commit/0d23eb936662137b2da4a7384f25c550f58f0299) · authored 2026-08-28T01:41:17Z · committed 2026-08-28T01:41:17Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: e34dd2c06d0dd2d3d1aca56da5ccdb9d24a4eb03.

Moves inbound capture to member Packet::readNoHeader after concrete packet exists, obtaining client getId/getName and actual Result; outgoing remains Batched send and initially only id. Reconstructs binary stream, Result/ErrorInfo/CallStack types and preserves MSVC-vs-Android string layout offsets. Single Record replaces row/packet/storage duplication; presentation derives labels, immutable shared body survives eviction, clipper fetches only visible rows and bad count is maintained incrementally. This is a causal correction to 23: receive supplied batches. Initial body retained only consumed range, corrected by 28. Stream parser has no explicit varint length bound here; no safety proof inferred.

Knowledge identity: `knowledge:commit:0d23eb936662137b2da4a7384f25c550f58f0299`.

Evidence:
- diff, parent 1, numbered lines1–853; full semantic diff read.
- message, parent 1, numbered lines1–31; full message read.

Changed paths: `src/bedrock/common_types.h`, `src/bedrock/core/utility/binary_stream.h`, `src/bedrock/diagnostics/log_area.h`, `src/bedrock/diagnostics/log_level.h`, `src/bedrock/network/batched_network_peer.h`, `src/bedrock/network/minecraft_packet_ids.h`, `src/bedrock/network/packet.h`, `src/bedrock/platform/callstack.h`, `src/bedrock/platform/check.h`, `src/bedrock/platform/result.h`, `src/spyglass/network.cpp`, `src/spyglass/network.h`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/pane/packet_bytes.cpp`, `src/spyglass/overlay/pane/packet_list.cpp`, `src/spyglass/overlay/pane/status_bar.cpp`, `src/spyglass/overlay/theme.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`, `src/spyglass/signature.h`.

<a id="commit-026"></a>
## 026. show why a packet failed to decode {#commit-026}
[f0daf169e6019adabb483813c4acafb70d697bc9](https://github.com/EndstoneMC/spyglass/commit/f0daf169e6019adabb483813c4acafb70d697bc9) · authored 2026-08-28T02:04:12Z · committed 2026-08-28T02:04:12Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 0d23eb936662137b2da4a7384f25c550f58f0299.

Adds owned recursive ErrorInfo-to-Node copying, preserving error category/value, frames/context and branches, enabling details tree without retaining client string_views. Outgoing names obtained from createPacket via decltype signature and cached per id. Adds Id column and enables details. Importantly the patch deliberately truncates first SubChunkPacket once as an in-client failure experiment; message reports PacketViolationWarning and connection survival with line numbers but stripped filenames. This is author-reported experiment, not this review's test result, and it is disabled next. A bounded synthetic failure path must not be silently described as passive capture.

Knowledge identity: `knowledge:commit:f0daf169e6019adabb483813c4acafb70d697bc9`.

Evidence:
- diff, parent 1, numbered lines1–381; full semantic diff read.
- message, parent 1, numbered lines1–36; full message read.

Changed paths: `src/bedrock/core/utility/binary_stream.h`, `src/bedrock/network/minecraft_packets.h`, `src/spyglass/network.cpp`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/pane/packet_details.cpp`, `src/spyglass/overlay/pane/packet_list.cpp`, `src/spyglass/overlay/view.cpp`, `src/spyglass/signature.h`.

<a id="commit-027"></a>
## 027. follow the tail of the capture until told otherwise {#commit-027}
[64e80c5a63fab3d6b223d81298bdef0e53f98ba5](https://github.com/EndstoneMC/spyglass/commit/64e80c5a63fab3d6b223d81298bdef0e53f98ba5) · authored 2026-08-28T02:13:35Z · committed 2026-08-28T02:13:35Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: f0daf169e6019adabb483813c4acafb70d697bc9.

Stable packet-number selection replaces shifting deque index. Evicted selected packet resolves empty; restart clears selection because numbering restarts. Auto-tail compares previous-layout scroll position/max at frame start; SetScrollHereY follows clipper cursor instead of stale maximum. For frozen viewport, eviction count times measured row height corrects offset. Message gives concrete frame-timing rationale; this is UI identity and scrolling correctness rather than just convenience.

Knowledge identity: `knowledge:commit:64e80c5a63fab3d6b223d81298bdef0e53f98ba5`.

Evidence:
- diff, parent 1, numbered lines1–232; full semantic diff read.
- message, parent 1, numbered lines1–35; full message read.

Changed paths: `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/pane/packet_list.cpp`, `src/spyglass/overlay/pane/packet_list.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`.

<a id="commit-028"></a>
## 028. mark the bytes a failed decode never reached {#commit-028}
[f06179e5df53fc822303768a08ed458b669440b0](https://github.com/EndstoneMC/spyglass/commit/f06179e5df53fc822303768a08ed458b669440b0) · authored 2026-08-28T02:23:28Z · committed 2026-08-28T02:23:28Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 64e80c5a63fab3d6b223d81298bdef0e53f98ba5.

Keeps full remaining body rather than only consumed bytes so failed-decoder unread tail is available; unread count determines highlighted boundary, avoiding redundant stop field. Hex and text tint same range. Disables destructive SubChunk experiment behind compiled false constant, preserving compilability for future rechecks. Note message describes full packet bytes broadly while exact implementation starts at entry read pointer; do not infer an included wire header if that pointer already follows it.

Knowledge identity: `knowledge:commit:f06179e5df53fc822303768a08ed458b669440b0`.

Evidence:
- diff, parent 1, numbered lines1–131; full semantic diff read.
- message, parent 1, numbered lines1–21; full message read.

Changed paths: `src/spyglass/network.cpp`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/pane/packet_bytes.cpp`.

<a id="commit-029"></a>
## 029. cut the packet patterns for the android client {#commit-029}
[8c55632510a901fe4e70af847d6e3596816ad550](https://github.com/EndstoneMC/spyglass/commit/8c55632510a901fe4e70af847d6e3596816ad550) · authored 2026-08-28T12:23:00Z · committed 2026-08-28T12:23:00Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: f06179e5df53fc822303768a08ed458b669440b0.

Adds Android patterns plus detailed reverse-engineering recipes from surviving error strings, xrefs, exception function indexes, jump-table structure, vtable neighbor confirmation and Android relocation/RTTI cross-check. Explains distinct destructor slot counts and evolving packet-id bounds. Reports preview rejecting missing patterns rather than guessing. This is unusually important preserved mechanism evidence and a counterexample to literal 'no comments' guidance. Recipes are current to named client versions, not universal binary offsets or proof against future clients.

Knowledge identity: `knowledge:commit:8c55632510a901fe4e70af847d6e3596816ad550`.

Evidence:
- diff, parent 1, numbered lines1–81; full semantic diff read.
- message, parent 1, numbered lines1–29; full message read.

Changed paths: `src/spyglass/signature.h`.

<a id="commit-030"></a>
## 030. let libhat do the matching on both platforms {#commit-030}
[3ce3f818c33d9494bae32cdde891d4b39d2eb7e4](https://github.com/EndstoneMC/spyglass/commit/3ce3f818c33d9494bae32cdde891d4b39d2eb7e4) · authored 2026-08-28T12:23:42Z · committed 2026-08-28T12:23:42Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 8c55632510a901fe4e70af847d6e3596816ad550.

Removes custom Android parser/memchr matcher in favor of already-linked libhat. Keeps only code-region discovery platform-specific because launcher linker hides Android client from standard module enumeration. Common find parses once, counts all matches across regions and rejects 0 or >1. Message notes vectorization and more complete ambiguity counts, plus leading-wildcard acceptance; no measured speedup claimed. Existing three patterns unaffected by parsing extension. A dependency is reused for platform-neutral algorithm while unavoidable host plumbing stays local.

Knowledge identity: `knowledge:commit:3ce3f818c33d9494bae32cdde891d4b39d2eb7e4`.

Evidence:
- diff, parent 1, numbered lines1–158; full semantic diff read.
- message, parent 1, numbered lines1–19; full message read.

Changed paths: `src/spyglass/pattern.cpp`.

<a id="commit-031"></a>
## 031. draw the bytes as a hex view rather than a table {#commit-031}
[35bf7cee473b536a5e74b438bdd8af65558cb2f5](https://github.com/EndstoneMC/spyglass/commit/35bf7cee473b536a5e74b438bdd8af65558cb2f5) · authored 2026-08-28T12:46:34Z · committed 2026-08-28T12:46:34Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 3ce3f818c33d9494bae32cdde891d4b39d2eb7e4.

Replaces the per-byte ImGui table with a custom clipped grid, measuring printable glyph advances once per font/size and centering proportional Mojangles glyphs. Adds hit-testing, drag/shift selection, outlines across rows, keyboard and touch-friendly find, overlapping matches, formatting (dump, stream, printable, C array, base64) and a bounded 64-KiB text-preview fallback for process-local clipboard. Whole packet remains available to formatting, while drawing grows with visible rows. Does not mutate the Android host font atlas midframe. Explicit latency rationale is not a measured performance result; optional monospace handling is simplified in 33.

Knowledge identity: `knowledge:commit:35bf7cee473b536a5e74b438bdd8af65558cb2f5`.

Evidence:
- diff, parent 1, numbered lines1–783; full semantic diff read.
- message, parent 1, numbered lines1–48; full message read.

Changed paths: `src/spyglass/overlay/pane/packet_bytes.cpp`, `src/spyglass/overlay/pane/packet_bytes.h`, `src/spyglass/overlay/pane/status_bar.cpp`, `src/spyglass/overlay/pane/status_bar.h`, `src/spyglass/overlay/theme.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`.

<a id="commit-032"></a>
## 032. count the whole capture and retain it by size {#commit-032}
[0e10da5bfce61c42f7d6dc9bb46847f337a37e6d](https://github.com/EndstoneMC/spyglass/commit/0e10da5bfce61c42f7d6dc9bb46847f337a37e6d) · authored 2026-08-28T12:46:53Z · committed 2026-08-28T12:46:53Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 35bf7cee473b536a5e74b438bdd8af65558cb2f5.

Replaces 4096-only retention with a 65536-record ceiling and 64-MiB body budget, retaining a sole oversize packet. Counters become lifetime totals independent of eviction; errors and metadata are outside the body budget. Message explicitly contrasts resource-pack bodies with chat packets. This is bounded body retention, not a proof that total process memory is bounded to 64 MiB.

Knowledge identity: `knowledge:commit:0e10da5bfce61c42f7d6dc9bb46847f337a37e6d`.

Evidence:
- diff, parent 1, numbered lines1–111; full semantic diff read.
- message, parent 1, numbered lines1–23; full message read.

Changed paths: `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/pane/status_bar.cpp`.

<a id="commit-033"></a>
## 033. stop the game reading the mouse while the overlay holds it {#commit-033}
[c741676170120d85d9f8636abe0cf3711abda67d](https://github.com/EndstoneMC/spyglass/commit/c741676170120d85d9f8636abe0cf3711abda67d) · authored 2026-08-28T13:20:17Z · committed 2026-08-28T13:20:17Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 0e10da5bfce61c42f7d6dc9bb46847f337a37e6d.

Separates input ownership from visibility. Windows GameInput bypasses ordinary mouse messages, so a shared MouseDevice::feed detour blocks game polling only while cursor is free and ImGui wants the mouse. WndProc captures according to ImGui flags, tracks key/button down-up pairing, clears state on focus loss and passes raw input/bookkeeping through. Moves toggle polling into render thread and gates error window on visibility; diagnostic counters remain compiled off. Adds hashed source filenames: all 694 table pairs independently recomputed with documented seeded FNV1a64, zero mismatches and no duplicates. Table's claimed client-version provenance is source evidence; no binaries were reanalyzed. Input-hook correctness was not runtime tested.

Knowledge identity: `knowledge:commit:c741676170120d85d9f8636abe0cf3711abda67d`.

Evidence:
- diff, parent 1, numbered lines1–1466; full meaningful diff read plus all694 generated hash rows verified.
- message, parent 1, numbered lines1–34; full message read.

Changed paths: `CLAUDE.md`, `CMakeLists.txt`, `src/bedrock/input/mouse.h`, `src/spyglass/filename.cpp`, `src/spyglass/filename.h`, `src/spyglass/filename_table.inc`, `src/spyglass/network.cpp`, `src/spyglass/overlay/pane/packet_bytes.cpp`, `src/spyglass/overlay/pane/packet_details.cpp`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/windows/input.cpp`, `src/spyglass/overlay/windows/input.h`, `src/spyglass/overlay/windows/mouse.cpp`, `src/spyglass/overlay/windows/mouse.h`, `src/spyglass/overlay/windows/overlay.cpp`, `src/spyglass/overlay/windows/overlay.h`, `src/spyglass/signature.h`.

<a id="commit-034"></a>
## 034. follow the 1.26.50.27 preview client {#commit-034}
[39eb6a2f2f73ed91e1e2b27ec272079c162bb869](https://github.com/EndstoneMC/spyglass/commit/39eb6a2f2f73ed91e1e2b27ec272079c162bb869) · authored 2026-08-28T13:44:10Z · committed 2026-08-28T13:44:10Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: c741676170120d85d9f8636abe0cf3711abda67d.

Chooses a Windows release/preview pattern set using the in-image wide Minecraft Preview marker before scanning. This avoids guessing across partially matching builds and does not depend on a window that may not exist yet. Recipes document changed prologues, frame offsets and branch shapes; Android retains its own pattern set. Exact-version pattern selection is explicit fail-closed compatibility, not generic future-version support.

Knowledge identity: `knowledge:commit:39eb6a2f2f73ed91e1e2b27ec272079c162bb869`.

Evidence:
- diff, parent 1, numbered lines1–208; full semantic diff read.
- message, parent 1, numbered lines1–25; full message read.

Changed paths: `CMakeLists.txt`, `src/spyglass/network.cpp`, `src/spyglass/signature.cpp`, `src/spyglass/signature.h`.

<a id="commit-035"></a>
## 035. carry the README and the changelog onto the rewrite {#commit-035}
[7d8fd820aaac80b8d800c88a23c6b973f4e56739](https://github.com/EndstoneMC/spyglass/commit/7d8fd820aaac80b8d800c88a23c6b973f4e56739) · authored 2026-08-28T13:54:54Z · committed 2026-08-28T13:54:54Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 39eb6a2f2f73ed91e1e2b27ec272079c162bb869.

Rewrites README and unreleased changelog to describe current capture, bounded bodies, inspection and installation rather than obsolete diagnostic windows/CI claims. Adds MIT license while retaining prior third-party notices; keeps historical 0.1 release history. Documents unsanitized capture privacy risk. Adds a screenshot, visually inspected: Preview26.50.27, failed PlaySoundPacket, BinaryStream overflow frames and following client-to-server PacketViolationWarningPacket. Removed disk diagnostics are later reintroduced for a different session-capture purpose in 70. README no-client-writes wording concerns removed vtable writes; machine-code hooks still mutate the running client, so it must not be generalized to no process mutation.

Knowledge identity: `knowledge:commit:7d8fd820aaac80b8d800c88a23c6b973f4e56739`.

Evidence:
- diff, parent 1, numbered lines1–290; full semantic diff read.
- message, parent 1, numbered lines1–25; full message read.

Changed paths: `CHANGELOG.md`, `CMakeLists.txt`, `LICENSE`, `README.md`, `docs/screenshot.png`.

<a id="commit-036"></a>
## 036. cut releases from this line {#commit-036}
[3cbe7236a77619e0bb4f144adfdc5848e79ce5c3](https://github.com/EndstoneMC/spyglass/commit/3cbe7236a77619e0bb4f144adfdc5848e79ce5c3) · authored 2026-08-28T14:03:37Z · committed 2026-08-28T14:03:37Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 7d8fd820aaac80b8d800c88a23c6b973f4e56739.

Limits CI to main and introduces release pipeline with branch/semver/tag/changelog validation, dry-run checks, exact tagged revision builds, version replacement verification, atomic commit/tag push, and separately packaged Windows binaries/symbols and Android payload. Prior-tag ancestry check is essential because this branch began as an orphan rewrite; 43 later restores ancestry without changing the rewrite tree. Source workflow is reviewed; no release execution or artifact success observed.

Knowledge identity: `knowledge:commit:3cbe7236a77619e0bb4f144adfdc5848e79ce5c3`.

Evidence:
- diff, parent 1, numbered lines1–243; full semantic diff read.
- message, parent 1, numbered lines1–18; full message read.

Changed paths: `.github/workflows/ci.yml`, `.github/workflows/release.yml`, `README.md`.
