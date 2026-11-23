<!-- retrieval: {"source_ids":["public:commit:00df7f5c1038d96eab1602155fae15b34c3d1ffc","public:commit:10c9f1e7b1e548aa849697494f5d86be2b384ac7","public:commit:12ec15ae5ca67d2a0cecdfcb4d554a247ddc7bfb","public:commit:24be0676bcc129280f9ee4a624203f527db65512","public:commit:2ea50701eb06ae42f3c91483609461f055fb2b3d","public:commit:311caa5ccc30ac811d384a05e8b57e9a71c0da4d","public:commit:330575b0f4c1694d4d9c65cf58847b0aa0f38cf2","public:commit:43d4648a8d9c9a2a7fe47400f9b6e3813730b65c","public:commit:4983c893629884f2d9ea22df077211be307ca713","public:commit:53a8a0ce03d58e6fb21b5afab1f4c70b7b6b07b4","public:commit:60dac04449b08763ff2e4d5dbb9eb73a740a10b5","public:commit:6d87a336929b5d8888de9d1d233b85702f6a9201","public:commit:71f2c96e2a5f2605f0f688504bba8c554830ed9a","public:commit:8a791412d64c7a4ea8c0679a414b069f188cb3f2","public:commit:8e7c9a8d98028544a77dded320e9e77fb722eb75","public:commit:98e405ed2496cd3a612f96e783b79f0d45543e34","public:commit:a6286a8b2d3bc8de34759d7f4c65fc493b64b26d","public:commit:cbf3fa744f163bc781ae7e7fe0296555ebc46476","public:commit:f8786759715d0293a37eb3655a01a9b8e1b5c1e0","public:commit:fd0465f8da9e4cdd89e390749651d30bb50633ff","public:commit:fd2344e3bb624a67dec012adbf4bb95eb7841d72","public:commit:ff907b04d937e6ccd197748b76676ff87ea38047"],"source_type":"public","date":"2026-08-28..2026-08-29","topics":["lifetime","concurrency","ffi","testing","build","recovery","review","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="reflection-reconstruction-and-nbt-representation"></a>
# Reflection reconstruction and NBT representation {#reflection-reconstruction-and-nbt-representation}

Reflection avoids maintaining another wire protocol implementation but still requires exact ABI mirrors, safe lifetime assumptions and behavior-aware context. Template/type names and local sizeof assertions are narrower evidence than layout correctness. NBT evolves from bounded raw reconstruction through native containers and client formatting; the later allocator diagnosis must remain attached to recommendations about borrowing client methods.

This dossier separates observed code changes from explicit commit-message rationale and review inference. The original patches are available through the public commit links in each entry. Author-reported measurements and client checks were not repeated.

<a id="commit-048"></a>
## 048. decode packet fields through the client's own cereal reflection {#commit-048}
[8e7c9a8d98028544a77dded320e9e77fb722eb75](https://github.com/EndstoneMC/spyglass/commit/8e7c9a8d98028544a77dded320e9e77fb722eb75) · authored 2026-08-28T23:27:40Z · committed 2026-08-28T23:27:40Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: ebc56a336957263b6deba852899434b1c12e9407.

Adds pinned EnTT/cereal mirrors and lazy field inspection using saved client ReflectionCtx, factory-created throwaway packet, original readNoHeader, CerealOnly mode and client schema walk. Outgoing strips header varint so body meaning matches inbound. Handles scalars/enums, bases, members, custom getters, sequence/maps, depth/node/item/text ceilings, and failure context. One-entry cache initially rebuilds when alternating windows, fixed 58; atomic context pointer publication does not itself establish lifetime across disconnect. Message's 'whatever client read' is stronger than mechanism: this is re-decoding under forced CerealOnly, not capturing original object, later corrected. Type-hash assertions pin names and local ABI shapes, not every running-client offset; 49 itself clarifies this. No independent protocol implementation is added, but replay can still differ from original decoding and is not behavior-free.

Knowledge identity: `knowledge:commit:8e7c9a8d98028544a77dded320e9e77fb722eb75`.

Evidence:
- diff, parent 1, numbered lines1–941; full semantic diff read.
- message, parent 1, numbered lines1–28; full message read.

Changed paths: `CHANGELOG.md`, `CMakeLists.txt`, `src/bedrock/cereal/context.h`, `src/bedrock/cereal/schema/basic_schema.h`, `src/bedrock/core/utility/enable_non_owner_references.h`, `src/bedrock/network/packet.h`, `src/bedrock/network/serialization_mode.h`, `src/spyglass/network.cpp`, `src/spyglass/network.h`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/pane/packet_details.cpp`, `src/spyglass/reflect.cpp`, `src/spyglass/reflect.h`, `third_party/CMakeLists.txt`, `third_party/entt/CMakeLists.txt`.

<a id="commit-049"></a>
## 049. bind the client's meta context, and read through variants and optionals {#commit-049}
[f8786759715d0293a37eb3655a01a9b8e1b5c1e0](https://github.com/EndstoneMC/spyglass/commit/f8786759715d0293a37eb3655a01a9b8e1b5c1e0) · authored 2026-08-29T00:03:48Z · committed 2026-08-29T00:03:48Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 8e7c9a8d98028544a77dded320e9e77fb722eb75.

Binds module-local EnTT locator to borrowed client context with no-op deleter so implicit meta handles resolve real registered types without deleting client subobject. Adds size-checked raw-layout optional/variant unwrapping and info().name fallback. Repository guidance records actual reported failures: recursive base traversal exhausting 1-MiB stack, inferred slots/offsets costing injection cycles, incomplete vector element mirrors, concurrent build-tree corruption. These are author reports, not reproduced tests. Bounds on storage offsets reduce obvious mismatch but do not establish every STL variant alignment/index layout. Guidance distinguishes type-name hash from layout proof and insists on real call sites/vtables. Store as revision-scoped development evidence, not current agent instructions.

Knowledge identity: `knowledge:commit:f8786759715d0293a37eb3655a01a9b8e1b5c1e0`.

Evidence:
- diff, parent 1, numbered lines1–157; full semantic diff read.
- message, parent 1, numbered lines1–30; full message read.

Changed paths: `CLAUDE.md`, `src/spyglass/reflect.cpp`.

<a id="commit-050"></a>
## 050. resolve conditionally serialized members, vectors and hashed strings {#commit-050}
[2ea50701eb06ae42f3c91483609461f055fb2b3d](https://github.com/EndstoneMC/spyglass/commit/2ea50701eb06ae42f3c91483609461f055fb2b3d) · authored 2026-08-29T00:55:09Z · committed 2026-08-29T00:55:09Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: f8786759715d0293a37eb3655a01a9b8e1b5c1e0.

Conditionally serialized members return a closure instead of value; invokes the discovered serialization thunk with a zeroed inert 1024-byte SerializerContext and uses dynamic setter type as fallback. Explicit rationale says const-reference makes inert context safe, but constness prevents ordinary writes, not reads, so source alone cannot prove that safety claim. Adds three-pointer std::vector fallback when EnTT lacks container traits, checks positive element size, 3-pointer total size and divisible range; null/empty vector falls back at this stage. Adds HashedString mirror and extended enum names. Pointer arithmetic/range plausibility are guards, not a general memory-safety proof.

Knowledge identity: `knowledge:commit:2ea50701eb06ae42f3c91483609461f055fb2b3d`.

Evidence:
- diff, parent 1, numbered lines1–140; full semantic diff read.
- message, parent 1, numbered lines1–26; full message read.

Changed paths: `src/bedrock/cereal/schema/basic_schema.h`, `src/bedrock/core/string/string_hash.h`, `src/spyglass/reflect.cpp`.

<a id="commit-051"></a>
## 051. flatten the type dispatch so a new case is a sibling {#commit-051}
[43d4648a8d9c9a2a7fe47400f9b6e3813730b65c](https://github.com/EndstoneMC/spyglass/commit/43d4648a8d9c9a2a7fe47400f9b6e3813730b65c) · authored 2026-08-29T12:56:42Z · committed 2026-08-29T12:56:42Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 2ea50701eb06ae42f3c91483609461f055fb2b3d.

Refactors optional/vector/variant dispatch into sibling precedence branches with is_specialization and bytes_of helpers. Full residual diff preserves behavior: context lookup and immutable type resolution repeated per branch, object data reached via value.base rather than wrapper storage. Explicit copy/paste hazard motivates the helper, a concrete counterexample to overgeneralizing 'no helpers'. No runtime behavior or speedup claim verified.

Knowledge identity: `knowledge:commit:43d4648a8d9c9a2a7fe47400f9b6e3813730b65c`.

Evidence:
- diff, parent 1, numbered lines1–136; full semantic diff read.
- message, parent 1, numbered lines1–24; full message read.

Changed paths: `src/spyglass/reflect.cpp`.

<a id="commit-052"></a>
## 052. collapse a single-field wrapper into the field it wraps {#commit-052}
[330575b0f4c1694d4d9c65cf58847b0aa0f38cf2](https://github.com/EndstoneMC/spyglass/commit/330575b0f4c1694d4d9c65cf58847b0aa0f38cf2) · authored 2026-08-29T13:04:43Z · committed 2026-08-29T13:06:10Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 43d4648a8d9c9a2a7fe47400f9b6e3813730b65c.

Flattens single-member wrappers only with no bases, exactly one reflected member, successful value getter and no conditional serialization thunk; keeps outer user-facing member name, inner fallback. Packet roots use separate append_members path and retain their payload node. Explicit asymmetric risk: extra click is preferable to accidentally hiding real fields, so no speculative base-member counting. Depth increment bounds recursive wrappers. The author-reported count of 79/336 reflected types was not independently recreated.

Knowledge identity: `knowledge:commit:330575b0f4c1694d4d9c65cf58847b0aa0f38cf2`.

Evidence:
- diff, parent 1, numbered lines1–29; full semantic diff read.
- message, parent 1, numbered lines1–32; full message read.

Changed paths: `src/spyglass/reflect.cpp`.

<a id="commit-053"></a>
## 053. render mce::UUID as a canonical uuid string {#commit-053}
[12ec15ae5ca67d2a0cecdfcb4d554a247ddc7bfb](https://github.com/EndstoneMC/spyglass/commit/12ec15ae5ca67d2a0cecdfcb4d554a247ddc7bfb) · authored 2026-08-29T13:09:23Z · committed 2026-08-29T13:09:23Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 330575b0f4c1694d4d9c65cf58847b0aa0f38cf2.

Formats mce::UUID two words into canonical 8-4-4-4-12 representation. Explicit byte-order provenance is composition of Endstone fromMinecraft and str/Java most/least significant rendering; review did not reproduce Endstone implementation here. Size mirror only; deliberately declines self-asserting an unobserved type hash because that proves nothing. Failed type match preserves generic branch. This is careful falsifiability and readability reasoning, not novel UUID format design.

Knowledge identity: `knowledge:commit:12ec15ae5ca67d2a0cecdfcb4d554a247ddc7bfb`.

Evidence:
- diff, parent 1, numbered lines1–43; full semantic diff read.
- message, parent 1, numbered lines1–25; full message read.

Changed paths: `src/bedrock/platform/uuid.h`, `src/spyglass/reflect.cpp`.

<a id="commit-054"></a>
## 054. unwrap unique_ptr and shared_ptr into the value they point at {#commit-054}
[ff907b04d937e6ccd197748b76676ff87ea38047](https://github.com/EndstoneMC/spyglass/commit/ff907b04d937e6ccd197748b76676ff87ea38047) · authored 2026-08-29T13:14:40Z · committed 2026-08-29T13:14:40Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 12ec15ae5ca67d2a0cecdfcb4d554a247ddc7bfb.

Uses EnTT pointer-like trait and its client-instantiated dereference vtable to unwrap unique_ptr/shared_ptr by reference, including null case, rather than manually reading guessed offsets. One shared dispatch path gives hard-to-trigger shared_ptr the same mechanism as common item input unique_ptr; message explicitly acknowledges limited exercisability. Element-void limitation discussed rather than hidden. No actual pointer behavior executed in this review.

Knowledge identity: `knowledge:commit:ff907b04d937e6ccd197748b76676ff87ea38047`.

Evidence:
- diff, parent 1, numbered lines1–21; full semantic diff read.
- message, parent 1, numbered lines1–33; full message read.

Changed paths: `src/spyglass/reflect.cpp`.

<a id="commit-055"></a>
## 055. render a serialize-as type as the type it serializes to {#commit-055}
[6d87a336929b5d8888de9d1d233b85702f6a9201](https://github.com/EndstoneMC/spyglass/commit/6d87a336929b5d8888de9d1d233b85702f6a9201) · authored 2026-08-29T13:35:00Z · committed 2026-08-29T13:35:00Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: ff907b04d937e6ccd197748b76676ff87ea38047.

Recognizes cereal GetterDescriptor payloads and invokes serialize-as getter through full value dispatcher, so item/recipe representation containers/scalars/wrappers get proper rendering. Does not branch on setter alone because alsoReadAs is an alternate input form and would hide primary fields. Keeps root custom-getter fallback because packet schemas delegate to payload. Getter/setter names and sizes pinned by asserted observed client immediates/allocation sizes; that reverse-engineering evidence is reported in message, not a newly observed binary. Distinguishes representation from object layout.

Knowledge identity: `knowledge:commit:6d87a336929b5d8888de9d1d233b85702f6a9201`.

Evidence:
- diff, parent 1, numbered lines1–62; full semantic diff read.
- message, parent 1, numbered lines1–37; full message read.

Changed paths: `src/bedrock/cereal/schema/basic_schema.h`, `src/spyglass/reflect.cpp`.

<a id="commit-056"></a>
## 056. render a compound tag as its entry count {#commit-056}
[98e405ed2496cd3a612f96e783b79f0d45543e34](https://github.com/EndstoneMC/spyglass/commit/98e405ed2496cd3a612f96e783b79f0d45543e34) · authored 2026-08-29T13:58:42Z · committed 2026-08-29T13:58:42Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 6d87a336929b5d8888de9d1d233b85702f6a9201.

Adds minimal CompoundTag count-only mirror: Windows tree head+size versus libc++ begin/end+size, opaque node pointers prevent accidental traversal. Compares runtime meta size to local sizeof before reading count and verifies observed type hash. Explicit phase strategy proposes plausible entry counts before chasing nodes; plausible count alone is weak validation, not proof of offset correctness. Reflected scalar tags differ from hand-written nonreflective Compound/List/arrays. This minimal approach is shortly replaced by full Windows NBT, later direct shared layouts and rollback.

Knowledge identity: `knowledge:commit:98e405ed2496cd3a612f96e783b79f0d45543e34`.

Evidence:
- diff, parent 1, numbered lines1–82; full semantic diff read.
- message, parent 1, numbered lines1–40; full message read.

Changed paths: `src/bedrock/nbt/compound_tag.h`, `src/bedrock/nbt/tag.h`, `src/spyglass/reflect.cpp`.

<a id="commit-057"></a>
## 057. say what the field tree covers now {#commit-057}
[fd0465f8da9e4cdd89e390749651d30bb50633ff](https://github.com/EndstoneMC/spyglass/commit/fd0465f8da9e4cdd89e390749651d30bb50633ff) · authored 2026-08-29T13:59:47Z · committed 2026-08-29T13:59:47Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 98e405ed2496cd3a612f96e783b79f0d45543e34.

Updates one user-facing changelog bullet to state observable reach (UUIDs, items, wrappers, NBT count) rather than separate implementation commits. Explicit audience distinction: a person running tool cares about fields visible, not pointer/serialize-as milestones. Does not claim additional implementation or tests.

Knowledge identity: `knowledge:commit:fd0465f8da9e4cdd89e390749651d30bb50633ff`.

Evidence:
- diff, parent 1, numbered lines1–16; full semantic diff read.
- message, parent 1, numbered lines1–6; full message read.

Changed paths: `CHANGELOG.md`.

<a id="commit-058"></a>
## 058. cache decoded fields on the record they belong to {#commit-058}
[10c9f1e7b1e548aa849697494f5d86be2b384ac7](https://github.com/EndstoneMC/spyglass/commit/10c9f1e7b1e548aa849697494f5d86be2b384ac7) · authored 2026-08-29T15:43:19Z · committed 2026-08-29T15:43:19Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: fd0465f8da9e4cdd89e390749651d30bb50633ff.

Moves fields from single-entry global memo to each retained Record. Capture copies identity/body under lock, performs lazy outbound replay outside lock, caches only if same body pointer remains (protects eviction/restart replacement). Also starts eager inbound field extraction from actual post-read packet rather than replay. This network-thread cost is not emphasized by cache title, but is a material architecture change. Removes general element/node caps and raises depth64 for complete export; increases potential per-packet work/memory and adds catch-all C++ exception boundary (not general invalid-memory recovery). No performance measurements. Inbound failed object still reflected here until100. Later79/93 reconsider eager versus lazy.

Knowledge identity: `knowledge:commit:10c9f1e7b1e548aa849697494f5d86be2b384ac7`.

Evidence:
- diff, parent 1, numbered lines1–495; full semantic diff read.
- message, parent 1, numbered lines1–19; full message read.

Changed paths: `src/spyglass/network.cpp`, `src/spyglass/network.h`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/pane/packet_details.cpp`, `src/spyglass/overlay/pane/packet_details.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/reflect.cpp`, `src/spyglass/reflect.h`.

<a id="commit-059"></a>
## 059. render a compound tag as the tree it holds {#commit-059}
[4983c893629884f2d9ea22df077211be307ca713](https://github.com/EndstoneMC/spyglass/commit/4983c893629884f2d9ea22df077211be307ca713) · authored 2026-08-29T15:17:42Z · committed 2026-08-29T15:17:42Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: fd0465f8da9e4cdd89e390749651d30bb50633ff.

Parallel Windows NBT branch adds concrete scalar/list/array mirrors and hand-walked MSVC tree/variant. Type discriminant and list element kind drive dispatch without virtual calls. Message provides reported PDB/call-site offsets (node112 bytes, key32, value64, discriminant40), while Android deliberately stays count-only because binary node layout unverified. Independent tree-descent stack64, tag depth16, item64 and node4096 limits bound some loops; pointer alignment and counts are not full validity checks. No runtime validation by this review. This deliberately guarded manual alternative is replaced in64 and later unsafe expansion is rolled back103.

Knowledge identity: `knowledge:commit:4983c893629884f2d9ea22df077211be307ca713`.

Evidence:
- diff, parent 1, numbered lines1–477; full semantic diff read.
- message, parent 1, numbered lines1–38; full message read.

Changed paths: `CHANGELOG.md`, `src/bedrock/nbt/byte_array_tag.h`, `src/bedrock/nbt/byte_tag.h`, `src/bedrock/nbt/compound_tag.h`, `src/bedrock/nbt/compound_tag_variant.h`, `src/bedrock/nbt/double_tag.h`, `src/bedrock/nbt/float_tag.h`, `src/bedrock/nbt/int64_tag.h`, `src/bedrock/nbt/int_array_tag.h`, `src/bedrock/nbt/int_tag.h`, `src/bedrock/nbt/list_tag.h`, `src/bedrock/nbt/short_tag.h`, `src/bedrock/nbt/string_tag.h`, `src/bedrock/nbt/tag.h`, `src/spyglass/reflect.cpp`.

<a id="commit-060"></a>
## 060. give the tag walk its own bounds {#commit-060}
[00df7f5c1038d96eab1602155fae15b34c3d1ffc](https://github.com/EndstoneMC/spyglass/commit/00df7f5c1038d96eab1602155fae15b34c3d1ffc) · authored 2026-08-29T15:28:38Z · committed 2026-08-29T15:28:38Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 4983c893629884f2d9ea22df077211be307ca713.

Separates NBT element/node budgets from general reflected field budgets before merging branches: resets tag-node counter at tag entry so export-driven removal of general caps in58 does not silently remove NBT bounds. Concrete coordination across concurrent work, not redundant constants. Counter is global at this revision, so source does not establish race-free parallel walks.

Knowledge identity: `knowledge:commit:00df7f5c1038d96eab1602155fae15b34c3d1ffc`.

Evidence:
- diff, parent 1, numbered lines1–55; full semantic diff read.
- message, parent 1, numbered lines1–7; full message read.

Changed paths: `src/spyglass/reflect.cpp`.

<a id="commit-061"></a>
## 061. Merge branch 'nbt-windows' {#commit-061}
[fd2344e3bb624a67dec012adbf4bb95eb7841d72](https://github.com/EndstoneMC/spyglass/commit/fd2344e3bb624a67dec012adbf4bb95eb7841d72) · authored 2026-08-29T15:43:25Z · committed 2026-08-29T15:43:25Z

Attribution: Integration merge by the commit author; per-parent deltas are accounted for without double-counting equivalent code.
Parents: 10c9f1e7b1e548aa849697494f5d86be2b384ac7, 00df7f5c1038d96eab1602155fae15b34c3d1ffc.

Merges nbt-windows onto record-cache branch. Complete first-parent patch read; second-parent addition/deletion vectors across every changed path exactly equal already-read58, recorded in structural-061-cache-merge.json. No extra merge-only implementation discovered. Important integration preserves tag-specific bounds while general fields no longer have count/node cap; this would be lost by linearizing commits only by timestamps.

Knowledge identity: `knowledge:commit:fd2344e3bb624a67dec012adbf4bb95eb7841d72`.

Evidence:
- diff, parent 1, numbered lines1–482; full semantic diff read.
- diff, parent 2, numbered lines1–495; complete changed line vector equivalence to fully reviewed058.
- message, parent 1, numbered lines1–1; full message read.

Changed paths: `CHANGELOG.md`, `src/bedrock/nbt/byte_array_tag.h`, `src/bedrock/nbt/byte_tag.h`, `src/bedrock/nbt/compound_tag.h`, `src/bedrock/nbt/compound_tag_variant.h`, `src/bedrock/nbt/double_tag.h`, `src/bedrock/nbt/float_tag.h`, `src/bedrock/nbt/int64_tag.h`, `src/bedrock/nbt/int_array_tag.h`, `src/bedrock/nbt/int_tag.h`, `src/bedrock/nbt/list_tag.h`, `src/bedrock/nbt/short_tag.h`, `src/bedrock/nbt/string_tag.h`, `src/bedrock/nbt/tag.h`, `src/spyglass/reflect.cpp`, `src/spyglass/network.cpp`, `src/spyglass/network.h`, `src/spyglass/overlay/capture.cpp`, `src/spyglass/overlay/capture.h`, `src/spyglass/overlay/pane/packet_details.cpp`, `src/spyglass/overlay/pane/packet_details.h`, `src/spyglass/overlay/view.cpp`, `src/spyglass/reflect.h`.

<a id="commit-062"></a>
## 062. stop counting a compound's entries {#commit-062}
[311caa5ccc30ac811d384a05e8b57e9a71c0da4d](https://github.com/EndstoneMC/spyglass/commit/311caa5ccc30ac811d384a05e8b57e9a71c0da4d) · authored 2026-08-29T16:10:00Z · committed 2026-08-29T16:10:00Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: fd2344e3bb624a67dec012adbf4bb95eb7841d72.

Removes compound entry-count label now expandable tree exposes children; lists retain counts because cardinality is central. Small presentation rationale only. Later67 restores count via client summary, so not a durable blanket anti-count preference.

Knowledge identity: `knowledge:commit:311caa5ccc30ac811d384a05e8b57e9a71c0da4d`.

Evidence:
- diff, parent 1, numbered lines1–13; full semantic diff read.
- message, parent 1, numbered lines1–7; full message read.

Changed paths: `src/spyglass/reflect.cpp`.

<a id="commit-063"></a>
## 063. drop the type prefix from tag rows {#commit-063}
[71f2c96e2a5f2605f0f688504bba8c554830ed9a](https://github.com/EndstoneMC/spyglass/commit/71f2c96e2a5f2605f0f688504bba8c554830ed9a) · authored 2026-08-29T16:24:38Z · committed 2026-08-29T16:24:38Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 311caa5ccc30ac811d384a05e8b57e9a71c0da4d.

Removes two-letter tag-type prefixes from every NBT row because name scanning matters and value/tree convey most type information. Full tag cases changed, underlying data unchanged. Changelog temporarily still promises prefixes until later cleanup, a documentation lag worth distinguishing from implementation.

Knowledge identity: `knowledge:commit:71f2c96e2a5f2605f0f688504bba8c554830ed9a`.

Evidence:
- diff, parent 1, numbered lines1–80; full semantic diff read.
- message, parent 1, numbered lines1–7; full message read.

Changed paths: `src/spyglass/reflect.cpp`.

<a id="commit-064"></a>
## 064. walk a compound tag through its own map and variant {#commit-064}
[a6286a8b2d3bc8de34759d7f4c65fc493b64b26d](https://github.com/EndstoneMC/spyglass/commit/a6286a8b2d3bc8de34759d7f4c65fc493b64b26d) · authored 2026-08-29T16:39:50Z · committed 2026-08-29T16:39:50Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 71f2c96e2a5f2605f0f688504bba8c554830ed9a.

Replaces handwritten MSVC map nodes and raw variant discriminant with faithful std::map/std::variant declarations and native iteration/visit, enabling Android path using platform STL. Message assumes same standard library as host; size assertions confirm local compiled shapes, not complete target-build compatibility or validity of every live object. Removes manual left-descent depth stack while retains count loop, tag depth and nodes. This changes fault exposure: native iterator internals are not bounded by the former explicit traversal stack. Later rollback demonstrates that 'native declarations' alone does not guarantee safe runtime mirroring.

Knowledge identity: `knowledge:commit:a6286a8b2d3bc8de34759d7f4c65fc493b64b26d`.

Evidence:
- diff, parent 1, numbered lines1–228; full semantic diff read.
- message, parent 1, numbered lines1–19; full message read.

Changed paths: `CHANGELOG.md`, `src/bedrock/nbt/compound_tag.h`, `src/bedrock/nbt/compound_tag_variant.h`, `src/bedrock/nbt/end_tag.h`, `src/spyglass/reflect.cpp`.

<a id="commit-065"></a>
## 065. show every entry of a tag {#commit-065}
[24be0676bcc129280f9ee4a624203f527db65512](https://github.com/EndstoneMC/spyglass/commit/24be0676bcc129280f9ee4a624203f527db65512) · authored 2026-08-29T16:43:46Z · committed 2026-08-29T16:43:46Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: a6286a8b2d3bc8de34759d7f4c65fc493b64b26d.

Removes64-element NBT cap to avoid hiding searched entries; changes compound loop to range-for and lists/arrays to full sizes. Retains depth16/node4096 but global node return does not stop outer iteration, and int-array entries bypass append_tag counter, so message's claim node budget bounds whole cost is incomplete. Adds strongly worded source guideline to declare actual client STL types instead of hand layouts, referencing Endstone. Keep this as revision-specific principle with later counterexamples, not universal safety rule.

Knowledge identity: `knowledge:commit:24be0676bcc129280f9ee4a624203f527db65512`.

Evidence:
- diff, parent 1, numbered lines1–95; full semantic diff read.
- message, parent 1, numbered lines1–13; full message read.

Changed paths: `CLAUDE.md`, `src/spyglass/reflect.cpp`.

<a id="commit-066"></a>
## 066. render tag values through the client's toString {#commit-066}
[cbf3fa744f163bc781ae7e7fe0296555ebc46476](https://github.com/EndstoneMC/spyglass/commit/cbf3fa744f163bc781ae7e7fe0296555ebc46476) · authored 2026-08-29T16:52:55Z · committed 2026-08-29T16:52:55Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 24be0676bcc129280f9ee4a624203f527db65512.

Adds Tag virtual declarations through toString and delegates scalar/string/array formatting to client virtual. Explicit slot proof reported from four Windows vtables rather than declaration counting. Arrays lose element/sample information; lists/compounds initially excluded under assumption they serialize whole subtrees. This reintroduces vptr call surface59 deliberately avoided. Output truncates after client call, so length bound does not bound work inside toString. Both assumptions and tradeoffs matter;67 corrects summary assumption and104 ultimately returns to direct reads.

Knowledge identity: `knowledge:commit:cbf3fa744f163bc781ae7e7fe0296555ebc46476`.

Evidence:
- diff, parent 1, numbered lines1–111; full semantic diff read.
- message, parent 1, numbered lines1–21; full message read.

Changed paths: `src/bedrock/nbt/tag.h`, `src/spyglass/reflect.cpp`.

<a id="commit-067"></a>
## 067. let every tag say what it is {#commit-067}
[60dac04449b08763ff2e4d5dbb9eb73a740a10b5](https://github.com/EndstoneMC/spyglass/commit/60dac04449b08763ff2e4d5dbb9eb73a740a10b5) · authored 2026-08-29T16:56:04Z · committed 2026-08-29T16:56:04Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: cbf3fa744f163bc781ae7e7fe0296555ebc46476.

Corrects66's explicit wrong assumption: list and compound toString are one-line summaries, so all nonbyte values use client wording and include type/cardinality. Byte-array keeps sample child because summary omits payload. This is evidence-led correction rather than consistency for its own sake; no external binary recheck performed here.

Knowledge identity: `knowledge:commit:60dac04449b08763ff2e4d5dbb9eb73a740a10b5`.

Evidence:
- diff, parent 1, numbered lines1–55; full semantic diff read.
- message, parent 1, numbered lines1–14; full message read.

Changed paths: `src/spyglass/reflect.cpp`.

<a id="commit-068"></a>
## 068. write down why a slot is read rather than counted {#commit-068}
[53a8a0ce03d58e6fb21b5afab1f4c70b7b6b07b4](https://github.com/EndstoneMC/spyglass/commit/53a8a0ce03d58e6fb21b5afab1f4c70b7b6b07b4) · authored 2026-08-29T17:04:23Z · committed 2026-08-29T17:04:23Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 60dac04449b08763ff2e4d5dbb9eb73a740a10b5.

Documents concrete reason declaration-counted vtable slot can be wrong: MSVC overload-group ordering, illustrated by Tag print overloads. Recorded as author reverse-engineering finding for this toolchain, not unqualified cross-ABI rule; maintaining correct source declaration may be necessary even when slot order differs.

Knowledge identity: `knowledge:commit:53a8a0ce03d58e6fb21b5afab1f4c70b7b6b07b4`.

Evidence:
- diff, parent 1, numbered lines1–18; full semantic diff read.
- message, parent 1, numbered lines1–10; full message read.

Changed paths: `CLAUDE.md`.

<a id="commit-069"></a>
## 069. print a byte tag as a number {#commit-069}
[8a791412d64c7a4ea8c0679a414b069f188cb3f2](https://github.com/EndstoneMC/spyglass/commit/8a791412d64c7a4ea8c0679a414b069f188cb3f2) · authored 2026-08-29T17:06:22Z · committed 2026-08-29T17:06:22Z

Attribution: GitHub-linked author attribution; originality remains limited by ports and dependencies noted below.
Parents: 53a8a0ce03d58e6fb21b5afab1f4c70b7b6b07b4.

Overrides ByteTag::toString with numeric unsigned-byte formatting after reported client bug creating value-length strings of0x01, yielding blank/garbage boolean fields. Message says other tag summaries checked against same packet, an author-reported manual test. Strong counterexample to unconditional delegation to client formatting: preserve native semantics where correct, local fix where observed behavior is wrong.

Knowledge identity: `knowledge:commit:8a791412d64c7a4ea8c0679a414b069f188cb3f2`.

Evidence:
- diff, parent 1, numbered lines1–31; full semantic diff read.
- message, parent 1, numbered lines1–11; full message read.

Changed paths: `src/spyglass/reflect.cpp`.
