<!-- retrieval: {"source_ids":["public:commit:031bf8d8460cb470ff6f450cb94e8158e92783d2","public:commit:13f6d99aff78f22975ed21ee47eaad6c31f06dba","public:commit:1f9e5d0ef952f03cac47c672422d29d420df611b","public:commit:23557f08bf375d36c04267dce8dd064f69a8734e","public:commit:2417793d966311f87fa9203d614ffae45f27edc5","public:commit:2fe2f4c1b7b6941841e7dac88f92282deebfb9c1","public:commit:3c9819438e18095842fe1ad24a979a4c7aa57cc5","public:commit:4b0c2101f92c9eaafb027cc8b21181c05d09a23c","public:commit:5b0ec62a342d5bd3ad07237fafc2cb02c57e1c51","public:commit:75e962af620309b1bbe07c85abc202c121dfaf19","public:commit:782f70816af08358c018cb167c09a5f719216eb0","public:commit:a602f7edff90ea67a3ae95830c2fd457359388c8","public:commit:a664efa2225b41a22e71531c1bd5d71e5d7876ac","public:commit:bf9bbb8b725f7f74a556acf26977d4f31cfbd812","public:commit:c167383786c03621c5577f8507745ebdc326b8f8","public:commit:c34e1c6fe505077f7198ebd86d250508fef7ab00","public:commit:c8050563dc7de21675e4fd7fa77342558e49dd63","public:commit:d97b8f1db0f2e335dbce1eb14f25554968b54b36","public:commit:d98fccb4c7f2944a2ed05b8c5fa61e4b59a2a0af","public:commit:eea2a4e80cb8dd02b5aee19f9150575b2700a524","public:commit:f363baf123c226d379c195cb6829ed8265051b6c","public:commit:f9fff26a7e5394cc3415c7aa9127841f3414a88b"],"source_type":"public","date":"2026-08-31..2026-09-02","topics":["concurrency","ffi","testing","build","performance","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="replay-policy-registry-dependence-and-hook-replacement"></a>
# Replay policy, registry dependence and hook replacement {#replay-policy-registry-dependence-and-hook-replacement}

This chain is deliberately not compressed into a final rule. Schema-only classification, a conservative name list, their union, per-ID caching, schema-only optimization and a final audited ID list represent changing hypotheses. Failed replay and allocator boundaries disprove broad claims that calling the client is automatically safe. Factory-based virtual-slot hooks replace entrypoint hooks after inlining, but retain ABI and startup assumptions.

This dossier separates observed code changes from explicit commit-message rationale and review inference. The original patches are available through the public commit links in each entry. Author-reported measurements and client checks were not repeated.

<a id="commit-079"></a>
## 079. decode a packet's fields when its row is opened {#commit-079}
[2417793d966311f87fa9203d614ffae45f27edc5](https://github.com/EndstoneMC/spyglass/commit/2417793d966311f87fa9203d614ffae45f27edc5) · authored 2026-08-31T17:05:56Z · committed 2026-08-31T17:05:56Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 630ead8356a03eaf7696c40d852c92a89430737a.

Moves inbound fields back to lazy replay unless schema recursively holds item descriptors, scanning template arguments, bases and data members with depth24/seen set and one-time static marked IDs. Explicit mechanism: client thread-local ItemRegistry exists only in packet loop; later overlay replay can assert and write null for instance descriptor, or silently produce empty stack item. This narrows73's eager fidelity guarantee and prioritizes avoiding arrival-time work. First no-context evaluation permanently caches empty set in this revision. The schema's completeness assumption immediately fails80; does not prove lazy replay generally safe.

Knowledge identity: `knowledge:commit:2417793d966311f87fa9203d614ffae45f27edc5`.

Evidence:
- diff, parent 1, numbered lines1–147; full semantic diff read.
- message, parent 1, numbered lines1–22; full message read.

Changed paths: `CHANGELOG.md`, `src/spyglass/network.cpp`, `src/spyglass/reflect.cpp`, `src/spyglass/reflect.h`.

<a id="commit-080"></a>
## 080. name the packets that have to be decoded as they arrive {#commit-080}
[1f9e5d0ef952f03cac47c672422d29d420df611b](https://github.com/EndstoneMC/spyglass/commit/1f9e5d0ef952f03cac47c672422d29d420df611b) · authored 2026-08-31T17:28:40Z · committed 2026-08-31T17:28:40Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 2417793d966311f87fa9203d614ffae45f27edc5.

Replaces incomplete schema-only classification with generous explicit18 packet-name allowlist after author reports a crash dump placing only Spyglass replay frame below client null-address assert. Getter-reached fields invisible to data/base/template walk are stated cause. Sent listed packets without captured object are now deliberately left undecoded; Capture::fields guards lazy replay. Introduces separate per-record Fields node so opening one record does not eagerly decode every later selection due shared constant ImGui ID. Conservative false positive costs CPU; false negative crashes. Preserve this as empirical reversal of79, not timeless preference for hand lists.

Knowledge identity: `knowledge:commit:1f9e5d0ef952f03cac47c672422d29d420df611b`.

Evidence:
- diff, parent 1, numbered lines1–182; full semantic diff read.
- message, parent 1, numbered lines1–22; full message read.

Changed paths: `src/spyglass/network.cpp`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/pane/packet_details.cpp`, `src/spyglass/reflect.cpp`, `src/spyglass/reflect.h`.

<a id="commit-081"></a>
## 081. ask the schema as well as the list which packets carry an item {#commit-081}
[23557f08bf375d36c04267dce8dd064f69a8734e](https://github.com/EndstoneMC/spyglass/commit/23557f08bf375d36c04267dce8dd064f69a8734e) · authored 2026-08-31T17:52:52Z · committed 2026-08-31T17:52:52Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 1f9e5d0ef952f03cac47c672422d29d420df611b.

Combines list with expanded schema walk, adding generic ItemDescriptor/ItemStack/ItemInstance names and reflected function return types. Explicit raises correctness bar from no crash to no silently empty items: stack cerealizer checks weak_ptr and returns empty, unlike unguarded instance case. Union covers different gaps but cannot establish completeness of behavior-dependent registry use;93 later rejects type-based premise entirely. Static initialization/no-context issue still present.

Knowledge identity: `knowledge:commit:23557f08bf375d36c04267dce8dd064f69a8734e`.

Evidence:
- diff, parent 1, numbered lines1–147; full semantic diff read.
- message, parent 1, numbered lines1–17; full message read.

Changed paths: `src/spyglass/network.cpp`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/reflect.cpp`, `src/spyglass/reflect.h`.

<a id="commit-082"></a>
## 082. work out a packet's decode mode the first time one arrives {#commit-082}
[f363baf123c226d379c195cb6829ed8265051b6c](https://github.com/EndstoneMC/spyglass/commit/f363baf123c226d379c195cb6829ed8265051b6c) · authored 2026-08-31T18:09:25Z · committed 2026-08-31T18:09:25Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 23557f08bf375d36c04267dce8dd064f69a8734e.

Classifies each packet ID on first encounter into atomic1024-slot Unknown/Lazy/Eager cache rather than sweeping all registered types; initial call returns Eager even if it caches Lazy, intentionally pays first arrival. Follows old-ABI dynamic setter argument constructor because data.type was thunk rather than logical field. Author links that omission to another client crash. This is not simply redundant return bug:82 explicitly motivates conservative first arrival;92 later removes it for cost. Out-of-range IDs return Lazy and null-context result is cached Lazy at this revision; later92 fixes negative caching.

Knowledge identity: `knowledge:commit:f363baf123c226d379c195cb6829ed8265051b6c`.

Evidence:
- diff, parent 1, numbered lines1–148; full semantic diff read.
- message, parent 1, numbered lines1–17; full message read.

Changed paths: `src/spyglass/network.cpp`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/reflect.cpp`, `src/spyglass/reflect.h`.

<a id="commit-083"></a>
## 083. read a sent packet where the client still holds its item registry {#commit-083}
[a664efa2225b41a22e71531c1bd5d71e5d7876ac](https://github.com/EndstoneMC/spyglass/commit/a664efa2225b41a22e71531c1bd5d71e5d7876ac) · authored 2026-08-31T18:18:53Z · committed 2026-08-31T18:18:53Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: f363baf123c226d379c195cb6829ed8265051b6c.

Adds live outgoing NetworkSystem::send hook after original returns: captures packet name, serialized sendStream body and eager fields while caller's registry is expected alive. Reconstructs inheritance, member types, stream and reflection offsets with Windows static_asserts0x168/0x208 and sizeof0x220; BinaryStream exposes buffer, NonOwnerPointer mirror introduced. Byte-only BatchedNetworkPeer fallback suppressed when rich hook installed; Android has no pattern and retains original bytes-only path. Author says declarations supplied offsets, not independently checked here. Inference: post-return shared stream must correspond to this call; ABI assertions validate local compiled mirror, not external client.85 proves send alone missed local-server broadcasts.

Knowledge identity: `knowledge:commit:a664efa2225b41a22e71531c1bd5d71e5d7876ac`.

Evidence:
- diff, parent 1, numbered lines1–328; full semantic diff read.
- message, parent 1, numbered lines1–19; full message read.

Changed paths: `src/bedrock/core/utility/binary_stream.h`, `src/bedrock/core/utility/enable_non_owner_references.h`, `src/bedrock/network/network_system.h`, `src/spyglass/network.cpp`, `src/spyglass/network.h`, `src/spyglass/signature.h`.

<a id="commit-084"></a>
## 084. say how a packet's fields were read {#commit-084}
[13f6d99aff78f22975ed21ee47eaad6c31f06dba](https://github.com/EndstoneMC/spyglass/commit/13f6d99aff78f22975ed21ee47eaad6c31f06dba) · authored 2026-08-31T18:20:32Z · committed 2026-08-31T18:20:32Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: a664efa2225b41a22e71531c1bd5d71e5d7876ac.

Adds muted read-as-arrived versus read-when-opened text to field tree to expose fidelity provenance. Implementation recomputes current decode_mode rather than storing per-record actual decode provenance, so first-packet eager/cache-lazy82 can be mislabeled and fallback unavailable fields still classify by mode.86 immediately removes this explanatory node while flattening UI; don't treat it as enduring product behavior.

Knowledge identity: `knowledge:commit:13f6d99aff78f22975ed21ee47eaad6c31f06dba`.

Evidence:
- diff, parent 1, numbered lines1–24; full semantic diff read.
- message, parent 1, numbered lines1–5; full message read.

Changed paths: `src/spyglass/overlay/pane/packet_details.cpp`.

<a id="commit-085"></a>
## 085. hook the other place a packet is written {#commit-085}
[4b0c2101f92c9eaafb027cc8b21181c05d09a23c](https://github.com/EndstoneMC/spyglass/commit/4b0c2101f92c9eaafb027cc8b21181c05d09a23c) · authored 2026-08-31T18:31:12Z · committed 2026-08-31T18:31:12Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 13f6d99aff78f22975ed21ee47eaad6c31f06dba.

Adds NetworkSystem::sendToMultiple and requires both rich send patterns before suppressing peer fallback, fixing host/singleplayer/LAN missing sends introduced83. Message reports two Header Data string xrefs and two _sendInternal callers, and explicitly requires rechecking call graph after updates. Actual post-return hook records one final sendStream and sets PrimaryClient; it does not observe each loop serialization or preserve each recipient sub-ID despite source comment saying every header is seen. Later99 moves boundary to write virtuals. Both Android patterns remain empty. Failure resolving second required pattern propagates initialization error; no runtime success inferred.

Knowledge identity: `knowledge:commit:4b0c2101f92c9eaafb027cc8b21181c05d09a23c`.

Evidence:
- diff, parent 1, numbered lines1–162; full semantic diff read.
- message, parent 1, numbered lines1–17; full message read.

Changed paths: `src/bedrock/network/network_system.h`, `src/spyglass/network.cpp`, `src/spyglass/network.h`, `src/spyglass/signature.h`.

<a id="commit-086"></a>
## 086. put a packet's id beside its name and drop a level {#commit-086}
[c34e1c6fe505077f7198ebd86d250508fef7ab00](https://github.com/EndstoneMC/spyglass/commit/c34e1c6fe505077f7198ebd86d250508fef7ab00) · authored 2026-08-31T18:31:12Z · committed 2026-08-31T18:31:12Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 4b0c2101f92c9eaafb027cc8b21181c05d09a23c.

Flattens protocol details: ID beside name, fields directly under per-record protocol node, no decode-mode row. Adds cached has_fields schema/base/custom-getter detection to avoid empty branches. Also materially adds missing lazy decode in export when details requested and no stored fields, omitted from title/message. Export executes decode_body on eligible records and may cost more than cooperative frame budget. has_fields caches false when context absent at this stage;92 fixes. Empty schema detection differs from successful materialized fields and cannot prove no data exists.

Knowledge identity: `knowledge:commit:c34e1c6fe505077f7198ebd86d250508fef7ab00`.

Evidence:
- diff, parent 1, numbered lines1–156; full semantic diff read.
- message, parent 1, numbered lines1–12; full message read.

Changed paths: `src/spyglass/overlay/export.cpp`, `src/spyglass/overlay/pane/packet_details.cpp`, `src/spyglass/reflect.cpp`, `src/spyglass/reflect.h`.

<a id="commit-087"></a>
## 087. cut the preview client its own sendToMultiple {#commit-087}
[031bf8d8460cb470ff6f450cb94e8158e92783d2](https://github.com/EndstoneMC/spyglass/commit/031bf8d8460cb470ff6f450cb94e8158e92783d2) · authored 2026-08-31T18:36:28Z · committed 2026-08-31T18:36:28Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: c34e1c6fe505077f7198ebd86d250508fef7ab00.

Corrects preview sendToMultiple signature from release stack frame0x38/cookie0x30 to0x48/0x40. Message specifies1.26.50.27 function addresses and one-match/zero-cross-match checks traced through Header Data xrefs and exception table; these are author-reported validation, no client binary supplied/run here. Rejecting no-match was correct failure behavior, not proof original configuration was functional. Send/read patterns can share bytes while one sibling cannot; avoid treating channel-wide byte identity as general rule.

Knowledge identity: `knowledge:commit:031bf8d8460cb470ff6f450cb94e8158e92783d2`.

Evidence:
- diff, parent 1, numbered lines1–13; full semantic diff read.
- message, parent 1, numbered lines1–15; full message read.

Changed paths: `src/spyglass/signature.h`.

<a id="commit-088"></a>
## 088. say what spyglass does in the README, not how {#commit-088}
[c167383786c03621c5577f8507745ebdc326b8f8](https://github.com/EndstoneMC/spyglass/commit/c167383786c03621c5577f8507745ebdc326b8f8) · authored 2026-08-31T18:41:43Z · committed 2026-08-31T18:41:43Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 031bf8d8460cb470ff6f450cb94e8158e92783d2.

README deliberately shifts from implementation mechanisms to reader-visible promises: temporary unlimited-length capture, counted drops, cancellation, version refresh/errors; removes index size, lock mechanics, render-thread dialog reason and ABI macro explanation. Keeps security/compatibility caveats. Useful communication pattern explicitly motivated by deciding whether to run, not blanket ban on technical detail. Simplified claim wrong-client installs nothing remains stronger than76 exact guard/order and should not be repeated as verified architecture.

Knowledge identity: `knowledge:commit:c167383786c03621c5577f8507745ebdc326b8f8`.

Evidence:
- diff, parent 1, numbered lines1–82; full semantic diff read.
- message, parent 1, numbered lines1–14; full message read.

Changed paths: `README.md`.

<a id="commit-089"></a>
## 089. fall back to the client's serializer when a compound walks to nothing {#commit-089}
[2fe2f4c1b7b6941841e7dac88f92282deebfb9c1](https://github.com/EndstoneMC/spyglass/commit/2fe2f4c1b7b6941841e7dac88f92282deebfb9c1) · authored 2026-08-31T19:56:29Z · committed 2026-08-31T19:56:29Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: c167383786c03621c5577f8507745ebdc326b8f8.

Restores NBT textual fallback only when mirrored compound iteration returns empty but client virtual toString is not '{}', distinguishing genuine empty from likely drift without quadratic toString on every normal branch. Message candidly says this restores content, not expansion, and points at ungated preview NBT ABI as likely cause; no assertion mirror layout is correct. Fallback can also run after budget-induced empty child traversal, so no proof every nonempty fallback means ABI drift.104 later reconstructs preview/release NBT correctly.

Knowledge identity: `knowledge:commit:2fe2f4c1b7b6941841e7dac88f92282deebfb9c1`.

Evidence:
- diff, parent 1, numbered lines1–17; full semantic diff read.
- message, parent 1, numbered lines1–20; full message read.

Changed paths: `src/spyglass/reflect.cpp`.

<a id="commit-090"></a>
## 090. size the base64 buffer and stop wrapping it through a second string {#commit-090}
[a602f7edff90ea67a3ae95830c2fd457359388c8](https://github.com/EndstoneMC/spyglass/commit/a602f7edff90ea67a3ae95830c2fd457359388c8) · authored 2026-08-31T21:22:24Z · committed 2026-08-31T21:22:24Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 2fe2f4c1b7b6941841e7dac88f92282deebfb9c1.

Reserves exact4*ceil(n/3) Base64 output and wrapper length+6 instead of geometric character growth/std::format temporary. Source still creates encoded then wrapper strings, so title's no second string is about construction overhead, not zero-copy. Author reports roughly18 reallocations for100KB; not benchmarked here. Message describes export as background thread, whereas reviewed75 cooperative advance_export is render-driven and no intervening worker change was seen; retain this inconsistency rather than silently adopting thread claim.

Knowledge identity: `knowledge:commit:a602f7edff90ea67a3ae95830c2fd457359388c8`.

Evidence:
- diff, parent 1, numbered lines1–31; full semantic diff read.
- message, parent 1, numbered lines1–14; full message read.

Changed paths: `src/spyglass/overlay/bytes.cpp`, `src/spyglass/reflect.cpp`.

<a id="commit-091"></a>
## 091. index a node's keys once it outgrows the scan {#commit-091}
[782f70816af08358c018cb167c09a5f719216eb0](https://github.com/EndstoneMC/spyglass/commit/782f70816af08358c018cb167c09a5f719216eb0) · authored 2026-08-31T21:22:41Z · committed 2026-08-31T21:22:41Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: a602f7edff90ea67a3ae95830c2fd457359388c8.

Threads optional KeyIndex through all put/append/member/NBT/variant paths; materializes hash set at256 existing entries and backfills names, retaining linear scan and zero set allocations for small objects. Fixes associative path's previously declared-but-unused set, and stops unconditional small-NBT set allocation. Duplicate-name suffix correctness preserved by backfill and insertion. Message reports crossover near200keys and16k siblings330ms->10ms with unchanged small case, but no benchmark fixture or run here. Threshold empirical report not universal constant; reviewed all propagation paths, including default nullptr arrays.

Knowledge identity: `knowledge:commit:782f70816af08358c018cb167c09a5f719216eb0`.

Evidence:
- diff, parent 1, numbered lines1–319; full semantic diff read.
- message, parent 1, numbered lines1–22; full message read.

Changed paths: `src/spyglass/reflect.cpp`.

<a id="commit-092"></a>
## 092. let the schema say which packets decode eagerly {#commit-092}
[eea2a4e80cb8dd02b5aee19f9150575b2700a524](https://github.com/EndstoneMC/spyglass/commit/eea2a4e80cb8dd02b5aee19f9150575b2700a524) · authored 2026-08-31T21:37:55Z · committed 2026-08-31T21:37:55Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 782f70816af08358c018cb167c09a5f719216eb0.

Deletes18-name list, returns schema classification on first encounter rather than forced Eager, and avoids caching unknown context/unregistered IDs in decode_mode and has_fields. Motivated by20Hz PlayerAuthInput eager work and expensive join packets. Author claims checking list against types showed12covered,2obsolete,4safelylazy NBT/registry shapes.93 promptly disproves this ItemRegistry safety inference via behavioral constraint call, important corrective evidence. Negative-cache fix remains valid independent of failed classifier policy; don't collapse entire commit to good optimization or bad rollback.

Knowledge identity: `knowledge:commit:eea2a4e80cb8dd02b5aee19f9150575b2700a524`.

Evidence:
- diff, parent 1, numbered lines1–151; full semantic diff read.
- message, parent 1, numbered lines1–28; full message read.

Changed paths: `src/spyglass/network.cpp`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/export.cpp`, `src/spyglass/reflect.cpp`, `src/spyglass/reflect.h`.

<a id="commit-093"></a>
## 093. name the packets whose read needs the item registry {#commit-093}
[75e962af620309b1bbe07c85abc202c121dfaf19](https://github.com/EndstoneMC/spyglass/commit/75e962af620309b1bbe07c85abc202c121dfaf19) · authored 2026-09-01T21:38:59Z · committed 2026-09-01T21:38:59Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: eea2a4e80cb8dd02b5aee19f9150575b2700a524.

Replaces schema classifier with12 numeric packet IDs backed by author-reported binary/header audit after ItemRegistry replay crashes at validateServerItemComponents. Explicit changes hypothesis: registry dependency lies in bound cereal/constraint functions, not member types. Reports reading61 ConstraintHandle doValidate bodies; finds getItem stack/instance, lookupByTag constraint, registry constraint; derives8directdescriptor owners+3transitive+registry=12. Excludes prior speculative StartGame/ItemStackResponse/UpdateTrade/AddActor. Removes traversal and Unknown state; IDs mirrored only as needed. Audit tied to1.26.40 and explicitly needs newer-client recheck. This final list differs materially from80's18-name crash mitigation; no independently inspected client disassembly exists in mirror.

Knowledge identity: `knowledge:commit:75e962af620309b1bbe07c85abc202c121dfaf19`.

Evidence:
- diff, parent 1, numbered lines1–135; full semantic diff read.
- message, parent 1, numbered lines1–36; full message read.

Changed paths: `src/bedrock/network/minecraft_packet_ids.h`, `src/spyglass/reflect.cpp`, `src/spyglass/reflect.h`.

<a id="commit-094"></a>
## 094. wake the writer when it has something to wake for {#commit-094}
[d98fccb4c7f2944a2ed05b8c5fa61e4b59a2a0af](https://github.com/EndstoneMC/spyglass/commit/d98fccb4c7f2944a2ed05b8c5fa61e4b59a2a0af) · authored 2026-09-01T21:44:54Z · committed 2026-09-01T21:44:54Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 75e962af620309b1bbe07c85abc202c121dfaf19.

Moves queue condition-variable notification after mutex release and only on empty->nonempty transition, avoiding immediate wake-to-block and aiming larger batches. Message explicitly relies on predicated wait and50ms poll, so lost notification is not assumed lost work. Source delta leaves queue/failure/drop accounting unchanged. Author performance rationale plausible, not verified wakeup count or throughput benchmark.

Knowledge identity: `knowledge:commit:d98fccb4c7f2944a2ed05b8c5fa61e4b59a2a0af`.

Evidence:
- diff, parent 1, numbered lines1–34; full semantic diff read.
- message, parent 1, numbered lines1–13; full message read.

Changed paths: `src/spyglass/overlay/store.cpp`.

<a id="commit-095"></a>
## 095. do not decode fields the capture is going to throw away {#commit-095}
[bf9bbb8b725f7f74a556acf26977d4f31cfbd812](https://github.com/EndstoneMC/spyglass/commit/bf9bbb8b725f7f74a556acf26977d4f31cfbd812) · authored 2026-09-01T21:44:54Z · committed 2026-09-01T21:44:54Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: d98fccb4c7f2944a2ed05b8c5fa61e4b59a2a0af.

Adds View::wants_fields: cheap12-ID eager classifier first, Capture::accepts under mutex only if eager; hook skips reflection when capture stopped or outbound disabled. Fixes CPU overhead previously paid before record's rejection, especially20Hz input. Acceptance check and later record are separate critical sections, so concurrent option transition can still waste work or accept unavailable-fields snapshot; no atomic snapshot guarantee implied. Existing full body/error capture preparation still happens, so stopped capture does not mean zero hook overhead.

Knowledge identity: `knowledge:commit:bf9bbb8b725f7f74a556acf26977d4f31cfbd812`.

Evidence:
- diff, parent 1, numbered lines1–121; full semantic diff read.
- message, parent 1, numbered lines1–10; full message read.

Changed paths: `src/spyglass/network.cpp`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/overlay/view.h`.

<a id="commit-096"></a>
## 096. give the text export the whole field, not a preview of it {#commit-096}
[5b0ec62a342d5bd3ad07237fafc2cb02c57e1c51](https://github.com/EndstoneMC/spyglass/commit/5b0ec62a342d5bd3ad07237fafc2cb02c57e1c51) · authored 2026-09-01T21:59:38Z · committed 2026-09-01T21:59:38Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: bf9bbb8b725f7f74a556acf26977d4f31cfbd812.

Separates full text-export rendering from byte-preview UI via a required full boolean on field_line/report_node. Text no longer truncates anywhere; byte export decodes the whole Base64 string while UI keeps sixteen bytes. The Base64 prefix length is derived from the byte preview cap. Fixes a 149-byte field exporting only sixteen bytes and an ellipsis despite typed storage already retaining the whole value. No default argument forces new callers to choose a policy. report_node remains depth-64 bounded, so the whole-field promise is not proof of unlimited lossless structure export.

Knowledge identity: `knowledge:commit:5b0ec62a342d5bd3ad07237fafc2cb02c57e1c51`.

Evidence:
- diff, parent 1, numbered lines1–136; full semantic diff read.
- message, parent 1, numbered lines1–21; full message read.

Changed paths: `src/spyglass/overlay/export.cpp`, `src/spyglass/overlay/pane/packet_details.cpp`, `src/spyglass/overlay/report.cpp`, `src/spyglass/overlay/report.h`.

<a id="commit-097"></a>
## 097. stop caching a name table that was asked for too early {#commit-097}
[d97b8f1db0f2e335dbce1eb14f25554968b54b36](https://github.com/EndstoneMC/spyglass/commit/d97b8f1db0f2e335dbce1eb14f25554968b54b36) · authored 2026-09-01T23:01:56Z · committed 2026-09-01T23:01:56Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 5b0ec62a342d5bd3ad07237fafc2cb02c57e1c51.

Fixes an empty packet-name table permanently initialized between overlay Present installation and network factory discovery. once_flag executes only when g_create_packet is nonnull, retrying unknown state and retaining lazy first use because the author says createPacket must not run before the client is up. The filter table exposes the bug while packet rows use getName interned at the hook. Commit99 subsequently enumerates the factory during injection, changing that startup placement. No runtime timing evidence reconciles these statements here, and the plain factory pointer is not a synchronization proof.

Knowledge identity: `knowledge:commit:d97b8f1db0f2e335dbce1eb14f25554968b54b36`.

Evidence:
- diff, parent 1, numbered lines1–44; full semantic diff read.
- message, parent 1, numbered lines1–19; full message read.

Changed paths: `src/spyglass/network.cpp`.

<a id="commit-098"></a>
## 098. build a payload for the 1.26.60 preview client {#commit-098}
[3c9819438e18095842fe1ad24a979a4c7aa57cc5](https://github.com/EndstoneMC/spyglass/commit/3c9819438e18095842fe1ad24a979a4c7aa57cc5) · authored 2026-09-02T20:35:47Z · committed 2026-09-02T20:35:47Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: d97b8f1db0f2e335dbce1eb14f25554968b54b36.

Adds the1.26.60.21 preview payload and two opaque pointer slots after mPtr in TypeDescriptor/MemberDescriptor, gated at1.26.60. Keeps the EnTT4.0.0 pin and removes descriptor size/offset assertions. Evidence is explicitly Linux BDS protocol-dumper output for1008 reflected types, extrapolated to Windows field rendering; no direct Windows measurements are supplied here. The author acknowledges losing compile-time mismatch detection while removing repetitive three-generation assertions and offsetof on non-standard-layout types. Preserve that tradeoff rather than claiming assertions are generally unnecessary. Commit99 is additionally needed because the new client's old read hook was inlined away.

Knowledge identity: `knowledge:commit:3c9819438e18095842fe1ad24a979a4c7aa57cc5`.

Evidence:
- diff, parent 1, numbered lines1–88; full semantic diff read.
- message, parent 1, numbered lines1–22; full message read.

Changed paths: `CHANGELOG.md`, `CMakeLists.txt`, `src/bedrock/cereal/context.h`, `src/bedrock/cereal/schema/basic_schema.h`.

<a id="commit-099"></a>
## 099. hook the packet read and write by swapping the vtable slot {#commit-099}
[c8050563dc7de21675e4fd7fa77342558e49dd63](https://github.com/EndstoneMC/spyglass/commit/c8050563dc7de21675e4fd7fa77342558e49dd63) · authored 2026-09-02T20:36:28Z · committed 2026-09-02T20:36:28Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 3c9819438e18095842fe1ad24a979a4c7aa57cc5.

Replaces readNoHeader, BatchedPeer and NetworkSystem entrypoint signatures with factory-discovered per-class vtable read/write swaps after1.26.60.21 inlining removed readNoHeader. Enumerates IDs1 through511, deduplicates vtable pointers, verifies factory ID, swaps read slot9 and write slot5 on Windows or6 on Itanium, and uses nonvirtual member detours with cached originals to avoid thunk recursion. Write records the newly appended stream segment and both directions retain live objects. Discovery is bounded at512, not unbounded protocol enumeration. Adds writable-page transitions, aligned release stores, a mutex-protected original map and RAII restoration; Linux restores read-only rather than the previous protection and restoration failure is ignored. Hook errors are isolated, though a factory ID mismatch returns early and a failed write swap short-circuits that class's read swap. Factory enumeration now occurs at injection despite97's late-use caution. The message reports226–230 vtables, no direct calls among230 read/write bodies, CFG behavior, Windows in-game verification on preview1.26.60.21 and stable1.26.45, and Android CI only. These are author reports, not reproduced results. A single remaining capture signature still depends on virtual layout, ABI, startup state and page permissions. All903 diff lines were reviewed.

Knowledge identity: `knowledge:commit:c8050563dc7de21675e4fd7fa77342558e49dd63`.

Evidence:
- diff, parent 1, numbered lines1–903; full semantic diff read.
- message, parent 1, numbered lines1–47; full message read.

Changed paths: `CHANGELOG.md`, `src/bedrock/network/network_system.h`, `src/bedrock/network/packet.h`, `src/spyglass/hook.cpp`, `src/spyglass/hook.h`, `src/spyglass/network.cpp`, `src/spyglass/network.h`, `src/spyglass/overlay/pane/menu_bar.cpp`, `src/spyglass/overlay/store.cpp`, `src/spyglass/overlay/windows/mouse.cpp`, `src/spyglass/signature.h`.

<a id="commit-100"></a>
## 100. never decode a packet whose first read failed {#commit-100}
[f9fff26a7e5394cc3415c7aa9127841f3414a88b](https://github.com/EndstoneMC/spyglass/commit/f9fff26a7e5394cc3415c7aa9127841f3414a88b) · authored 2026-09-02T21:04:10Z · committed 2026-09-02T21:04:10Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: c8050563dc7de21675e4fd7fa77342558e49dd63.

Stops UI lazy replay of records without kDecoded and makes an errored protocol node a leaf after the author reports replaying a failed body corrupted the heap. This also hides eagerly stored partial fields in the UI on error. A separate export path introduced86 still calls decode_body when details/body/null-fields/lazy-mode match, without checking the decoded flag; this remains at target114. The title's never-decode guarantee is therefore not global. This is a source-derived uncovered path, not a reproduced export crash. README109/110 still advertise partial failed fields, creating documentation drift.

Knowledge identity: `knowledge:commit:f9fff26a7e5394cc3415c7aa9127841f3414a88b`.

Evidence:
- diff, parent 1, numbered lines1–26; full semantic diff read.
- message, parent 1, numbered lines1–9; full message read.

Changed paths: `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/pane/packet_details.cpp`.
