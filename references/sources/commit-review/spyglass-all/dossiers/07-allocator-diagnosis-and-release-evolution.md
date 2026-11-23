<!-- retrieval: {"source_ids":["public:commit:19ff904189b2cc71dbb5c7acee56a03a3ca58a27","public:commit:2a8588900df533464d276b174a9e8a348e34df4f","public:commit:30e6f730d7a75a829dcc457eb90c9aedb95f2a55","public:commit:4264c91d6244a3b9b53e1107fb0c03bca51f3855","public:commit:51aa3003a3916a7487f9b7c6102810a92bba193d","public:commit:8fb7e2cdd888b591382ad4d002e08390f3685d83","public:commit:9d39606b794da701156f8ddc53756000acbac862","public:commit:a669e33c267c7082d3791f5f8f0945540469cb34","public:commit:a919ba9f13e1c8f5dafad2725ce5e3b1aad04b0e","public:commit:b535f73db8944437d49199c6c4694ea18db159c4","public:commit:c343e5f94a85379e0304abf876e614ad64b151f9","public:commit:da92a0e767f8e1531f0760cbc0dd0c5c35df50c0","public:commit:e294efe252d5dda486f2e9cb930d6be86cbfe5e5","public:commit:f0a8f78a6c0cdaa403d5d9bd647b79f94cdde44c"],"source_type":"public","date":"2026-09-02..2026-10-18","topics":["ffi","testing","build","recovery","api","diagnosis","documentation","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="allocator-diagnosis-documentation-and-compatibility-releases"></a>
# Allocator diagnosis, documentation and compatibility releases {#allocator-diagnosis-documentation-and-compatibility-releases}

A cautious rollback does not identify a root cause. The later allocator explanation accounts for delayed heap detection and why earlier scalar paths were also affected. Screenshots and README claims are checked against actual content and source rather than repeated uncritically. Version parsing and release packaging are part of operational correctness, with bot stamps kept outside commit authorship.

This dossier separates observed code changes from explicit commit-message rationale and review inference. The original patches are available through the public commit links in each entry. Author-reported measurements and client checks were not repeated.

<a id="commit-101"></a>
## 101. show the NBT a field holds when the client hands it back by reference {#commit-101}
[19ff904189b2cc71dbb5c7acee56a03a3ca58a27](https://github.com/EndstoneMC/spyglass/commit/19ff904189b2cc71dbb5c7acee56a03a3ca58a27) · authored 2026-09-02T21:09:22Z · committed 2026-09-02T21:09:22Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: f9fff26a7e5394cc3415c7aa9127841f3414a88b.

Uses const CompoundTag in EnTT try_cast so cref-held values enter the NBT path instead of a generic class placeholder. Explains binding policy rejecting nonconst requests before the type check. Retains sizeof validation, which alone cannot establish offset or allocator ABI. The change broadens exercised data;103 rolls it back with102 while the cause is unknown, and104 restores it after diagnosing allocator ownership. Do not identify101 as the proven cause of corruption.

Knowledge identity: `knowledge:commit:19ff904189b2cc71dbb5c7acee56a03a3ca58a27`.

Evidence:
- diff, parent 1, numbered lines1–22; full semantic diff read.
- message, parent 1, numbered lines1–18; full message read.

Changed paths: `src/spyglass/reflect.cpp`.

<a id="commit-102"></a>
## 102. name a compound or a list on the row that holds it {#commit-102}
[b535f73db8944437d49199c6c4694ea18db159c4](https://github.com/EndstoneMC/spyglass/commit/b535f73db8944437d49199c6c4694ea18db159c4) · authored 2026-09-02T21:09:37Z · committed 2026-09-02T21:09:37Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 19ff904189b2cc71dbb5c7acee56a03a3ca58a27.

Adds NBT type names and client toString summaries to compound/list JSON keys, removing the empty-walk fallback because the label now carries the summary. Client toString supplies counts and element type, not necessarily a serialized subtree. The key change affects exported JSON structure as well as visual labels. Calling a virtual that returns an owning string on more tags exposes the allocator problem later diagnosed104. No automated test is added.

Knowledge identity: `knowledge:commit:b535f73db8944437d49199c6c4694ea18db159c4`.

Evidence:
- diff, parent 1, numbered lines1–65; full semantic diff read.
- message, parent 1, numbered lines1–21; full message read.

Changed paths: `src/spyglass/reflect.cpp`.

<a id="commit-103"></a>
## 103. back out the NBT field rendering until the walk is safe {#commit-103}
[9d39606b794da701156f8ddc53756000acbac862](https://github.com/EndstoneMC/spyglass/commit/9d39606b794da701156f8ddc53756000acbac862) · authored 2026-09-02T21:20:06Z · committed 2026-09-02T21:20:06Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: b535f73db8944437d49199c6c4694ea18db159c4.

Reverts101 and102's reflect.cpp blob exactly to its pre101 state after STATUS_HEAP_CORRUPTION during join. The message explicitly distinguishes the allocation where corruption is noticed from the earlier invalid operation and names both broadened paths without prematurely choosing a cause. It accepts an incorrect cref placeholder while investigating.104 later establishes that the rollback was insufficient because scalar tags had called the same toString for much longer. Preserve the uncertainty and bounded rollback, not an invented successful fix.

Knowledge identity: `knowledge:commit:9d39606b794da701156f8ddc53756000acbac862`.

Evidence:
- diff, parent 1, numbered lines1–83; full semantic diff read.
- message, parent 1, numbered lines1–20; full message read.

Changed paths: `src/spyglass/reflect.cpp`.

<a id="commit-104"></a>
## 104. read a tag out of its own fields, never through the client's toString {#commit-104}
[30e6f730d7a75a829dcc457eb90c9aedb95f2a55](https://github.com/EndstoneMC/spyglass/commit/30e6f730d7a75a829dcc457eb90c9aedb95f2a55) · authored 2026-09-02T21:53:09Z · committed 2026-09-02T21:53:09Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 9d39606b794da701156f8ddc53756000acbac862.

Restores const NBT casts and type/count labels while eliminating client Tag::toString calls from the field walk. Scalars use mirrored data members; strings and byte arrays use text_or_bytes; int arrays become native JSON arrays; container labels use mirrored sizes. Explicit cause: the client imports allocation through MallocRedirect.dll/mimalloc, returns std::string by value, and the payload's UCRT destructor frees its buffer through another heap. A later allocation detects the damage. Scalar calls explain why103's rollback was insufficient. The author reports checking1.26.60.21 mirrors field by field: virtual slot4, list+8, compound map+8 and size+0x10,48-byte variant with index+0x28. No mirror layout changes in this patch, correcting89/103's layout hypothesis. Guarded context confirms value_of returns false for a matching tag without a hidden toString call. Depth16/node4096 limits remain. The owning-container boundary rule is motivated by this incident, not proof that every other call such as getName is safe. No client execution was performed.

Knowledge identity: `knowledge:commit:30e6f730d7a75a829dcc457eb90c9aedb95f2a55`.

Evidence:
- diff, parent 1, numbered lines1–145; full semantic diff read.
- message, parent 1, numbered lines1–32; full message read.

Changed paths: `src/spyglass/reflect.cpp`.

<a id="commit-105"></a>
## 105. name the payloads a 0.3.0 release ships {#commit-105}
[a669e33c267c7082d3791f5f8f0945540469cb34](https://github.com/EndstoneMC/spyglass/commit/a669e33c267c7082d3791f5f8f0945540469cb34) · authored 2026-09-02T22:08:03Z · committed 2026-09-02T22:08:03Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 30e6f730d7a75a829dcc457eb90c9aedb95f2a55.

Prepares README filenames for0.3.0, adds the1.26.60 preview row, explains separate preview reflection ABIs, and documents the allocator crash plainly. It does not bump the actual project version; the following bot commit does. The changelog's broad no-risk and captures-unchanged wording exceeds static validation, and104 changes NBT scalar types and labels. File names in documentation are not verification of downloaded release artifacts.

Knowledge identity: `knowledge:commit:a669e33c267c7082d3791f5f8f0945540469cb34`.

Evidence:
- diff, parent 1, numbered lines1–71; full semantic diff read.
- message, parent 1, numbered lines1–11; full message read.

Changed paths: `CHANGELOG.md`, `README.md`.

<a id="commit-106"></a>
## 106. show the overlay on a client it now supports {#commit-106}
[a919ba9f13e1c8f5dafad2725ce5e3b1aad04b0e](https://github.com/EndstoneMC/spyglass/commit/a919ba9f13e1c8f5dafad2725ce5e3b1aad04b0e) · authored 2026-09-02T22:15:44Z · committed 2026-09-02T22:15:44Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: e4eaf43edd06d06d89278b20814923b799b281bc.

Replaces the main overlay screenshot with Preview26.60.21, a failed PlaySoundPacket, BinaryStream overflow frames, bytes, and a following client-to-server PacketViolationWarningPacket. Visual inspection confirms these contents. It also disproves the message's description of the prior image as a clean1.26.4x capture: the predecessor shows Preview26.50.27 and the same failed packet/error scenario. This is a version and UI refresh, not the first failure illustration. A repository image is not an independently executed client test.

Knowledge identity: `knowledge:commit:a919ba9f13e1c8f5dafad2725ce5e3b1aad04b0e`.

Evidence:
- diff, parent 1, numbered lines1–3; full semantic diff read.
- message, parent 1, numbered lines1–7; full message read.

Changed paths: `docs/screenshot.png`.

<a id="commit-107"></a>
## 107. open the overlay with F12 on Windows too {#commit-107}
[f0a8f78a6c0cdaa403d5d9bd647b79f94cdde44c](https://github.com/EndstoneMC/spyglass/commit/f0a8f78a6c0cdaa403d5d9bd647b79f94cdde44c) · authored 2026-09-02T22:30:05Z · committed 2026-09-02T22:30:05Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: a919ba9f13e1c8f5dafad2725ce5e3b1aad04b0e.

Unifies Windows toggle from Insert to F12, already used by the Linux launcher. Updates WndProc key consumption and foreground GetAsyncKeyState edge polling together, and renames insert_down state to toggle_down. README and changelog agree. The rationale removes an unexplained platform difference; it does not imply all overlay actions should have shortcuts.

Knowledge identity: `knowledge:commit:f0a8f78a6c0cdaa403d5d9bd647b79f94cdde44c`.

Evidence:
- diff, parent 1, numbered lines1–83; full semantic diff read.
- message, parent 1, numbered lines1–8; full message read.

Changed paths: `CHANGELOG.md`, `README.md`, `src/spyglass/overlay/windows/input.cpp`, `src/spyglass/overlay/windows/overlay.cpp`, `src/spyglass/overlay/windows/overlay.h`.

<a id="commit-108"></a>
## 108. name the files 0.3.0 actually shipped {#commit-108}
[c343e5f94a85379e0304abf876e614ad64b151f9](https://github.com/EndstoneMC/spyglass/commit/c343e5f94a85379e0304abf876e614ad64b151f9) · authored 2026-09-02T22:30:20Z · committed 2026-09-02T22:30:20Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: f0a8f78a6c0cdaa403d5d9bd647b79f94cdde44c.

Corrects released0.3.0 changelog filenames that still said0.2.0 and otherwise preserves the historical wording. Explicitly distinguishes a factual wrong filename from retrospective rewording. This is a narrow documentation correction without an independent algorithmic lesson; release artifact contents were not downloaded or run.

Knowledge identity: `knowledge:commit:c343e5f94a85379e0304abf876e614ad64b151f9`.

Evidence:
- diff, parent 1, numbered lines1–24; full semantic diff read.
- message, parent 1, numbered lines1–9; full message read.

Changed paths: `CHANGELOG.md`.

<a id="commit-109"></a>
## 109. say what the overlay has, not how it works {#commit-109}
[51aa3003a3916a7487f9b7c6102810a92bba193d](https://github.com/EndstoneMC/spyglass/commit/51aa3003a3916a7487f9b7c6102810a92bba193d) · authored 2026-09-02T22:50:22Z · committed 2026-09-02T22:50:22Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: c343e5f94a85379e0304abf876e614ad64b151f9.

Rewrites README around visible capabilities, adds reflection/NBT and missing menu/time-column explanations, and removes motivation and implementation details while retaining the cleartext credential caveat. No implementation changes. The partial-fields-on-failure claim conflicts with100's errored-node leaf behavior. This continues88's reader-oriented documentation choice, not evidence of the user's own writing preference.

Knowledge identity: `knowledge:commit:51aa3003a3916a7487f9b7c6102810a92bba193d`.

Evidence:
- diff, parent 1, numbered lines1–208; full semantic diff read.
- message, parent 1, numbered lines1–1; full message read.

Changed paths: `README.md`.

<a id="commit-110"></a>
## 110. trim the feature list {#commit-110}
[e294efe252d5dda486f2e9cb930d6be86cbfe5e5](https://github.com/EndstoneMC/spyglass/commit/e294efe252d5dda486f2e9cb930d6be86cbfe5e5) · authored 2026-09-02T22:51:28Z · committed 2026-09-02T22:51:28Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 51aa3003a3916a7487f9b7c6102810a92bba193d.

Compresses the feature description into panes and menu bullets without implementation changes. Retains capture limits, drops, temporary-data loss and export cancellation promises. No independent code-design lesson is claimed; this is documentation evolution. It retains the failed-partial-fields claim noted for100 and109.

Knowledge identity: `knowledge:commit:e294efe252d5dda486f2e9cb930d6be86cbfe5e5`.

Evidence:
- diff, parent 1, numbered lines1–102; full semantic diff read.
- message, parent 1, numbered lines1–1; full message read.

Changed paths: `README.md`.

<a id="commit-111"></a>
## 111. show what the details pane reads out {#commit-111}
[4264c91d6244a3b9b53e1107fb0c03bca51f3855](https://github.com/EndstoneMC/spyglass/commit/4264c91d6244a3b9b53e1107fb0c03bca51f3855) · authored 2026-09-02T23:09:11Z · committed 2026-09-02T23:09:11Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 14c851fc17c1e60ea08377e2974ac19be9ad9b28.

Adds a StartGamePacket details screenshot and caption. Visual inspection shows packet11, a nested Settings branch, booleans, numbers and named enums, with some branches collapsed and the pane scrollable. It supports the visible reflection-based example, not the caption's literal completeness claim for every field or every platform. No implementation changes.

Knowledge identity: `knowledge:commit:4264c91d6244a3b9b53e1107fb0c03bca51f3855`.

Evidence:
- diff, parent 1, numbered lines1–19; full semantic diff read.
- message, parent 1, numbered lines1–7; full message read.

Changed paths: `README.md`, `docs/details.png`.

<a id="commit-112"></a>
## 112. serve the 1.26.50 release client, and drop its preview {#commit-112}
[da92a0e767f8e1531f0760cbc0dd0c5c35df50c0](https://github.com/EndstoneMC/spyglass/commit/da92a0e767f8e1531f0760cbc0dd0c5c35df50c0) · authored 2026-09-15T21:15:07Z · committed 2026-09-15T21:15:07Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 4264c91d6244a3b9b53e1107fb0c03bca51f3855.

Adds the1.26.50 release payload and removes the superseded.50 preview. MINECRAFT_CLIENTS now uses three components for release and four for preview. Stable packed build byte saturates to0xFF so release1.26.50.5 does not disable reflection changes introduced at preview.25; preview keeps its real build. Reuses the release factory shape, reported checked on1.26.51.1 with a negative preview match, and moves the release compile ceiling below1.26.60. Explicitly references protocol-dumper282e520. Final dependency-selector inspection confirms EnTT selection compares at1.26.50, so three-component release versions still choose v4.0 correctly. README updates names and manifest version; the following bot stamps0.3.2.

Knowledge identity: `knowledge:commit:da92a0e767f8e1531f0760cbc0dd0c5c35df50c0`.

Evidence:
- diff, parent 1, numbered lines1–211; full semantic diff read.
- message, parent 1, numbered lines1–19; full message read.

Changed paths: `CHANGELOG.md`, `CMakeLists.txt`, `README.md`, `src/bedrock/version.h`, `src/spyglass/signature.h`.

<a id="commit-113"></a>
## 113. stage each launcher mod as a folder with its mod.json {#commit-113}
[8fb7e2cdd888b591382ad4d002e08390f3685d83](https://github.com/EndstoneMC/spyglass/commit/8fb7e2cdd888b591382ad4d002e08390f3685d83) · authored 2026-09-16T20:31:35Z · committed 2026-09-16T20:31:35Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 96c362fd0ea8e59e7e14b0fe5f27223b44e73318.

Stages each Android client payload in a folder with a configure-generated mod.json and updates README to copy that folder into the launcher's name/version/arch hierarchy. Reduces manual manifest and renaming work. Windows DLL/PDB staging remains at the root. The packaging contract is visible in CMake and documentation; no ZIP was built and no launcher load was tested.

Knowledge identity: `knowledge:commit:8fb7e2cdd888b591382ad4d002e08390f3685d83`.

Evidence:
- diff, parent 1, numbered lines1–64; full semantic diff read.
- message, parent 1, numbered lines1–7; full message read.

Changed paths: `CHANGELOG.md`, `CMakeLists.txt`, `README.md`.

<a id="commit-114"></a>
## 114. cut the 1.26.60 preview payload against 1.26.60.30 {#commit-114}
[2a8588900df533464d276b174a9e8a348e34df4f](https://github.com/EndstoneMC/spyglass/commit/2a8588900df533464d276b174a9e8a348e34df4f) · authored 2026-10-18T17:14:49Z · committed 2026-10-18T17:14:49Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 8fb7e2cdd888b591382ad4d002e08390f3685d83.

Raises the default preview floor from1.26.60.21 to.30 and adds a factory signature for the same0x30 stack frame with short ja instead of near ja. Retains the old set behind a nested version gate, but the one shipped payload per line intentionally stops serving.21. The message reports factory address0x1427b9a70, maximum ID0x169, one preview match and zero release1.26.45.1/1.26.52.3 matches, with unchanged mouse and vtable slots. These binary checks were not reproduced. README prepares0.3.3 filenames before the bot stamp. The October18 change proves signature maintenance persists after99 reduces hook dependencies. Runtime verify_client checks channel and patch-line floor, not preview build or upper bound; actual pattern failure remains part of compatibility rejection.

Knowledge identity: `knowledge:commit:2a8588900df533464d276b174a9e8a348e34df4f`.

Evidence:
- diff, parent 1, numbered lines1–169; full semantic diff read.
- message, parent 1, numbered lines1–16; full message read.

Changed paths: `CHANGELOG.md`, `CMakeLists.txt`, `README.md`, `src/spyglass/signature.h`.
