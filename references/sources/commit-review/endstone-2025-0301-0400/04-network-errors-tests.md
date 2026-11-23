<!-- retrieval: {"source_ids":["public:commit:0268d7ce5e23eff393346074f054298fb367c720","public:commit:07362783b0d56fe5f13963d3189b47b65be7f058","public:commit:1473fd5a550ea27871d875039a024610d18b9d0f","public:commit:1c8d9e896daa1227a71e7df3e208eb3590013c85","public:commit:36dfdefdc08cd81ef56b4c95ad147d9a0e395fe2","public:commit:54b59302b21ad85f094ec4a045dd37352f41db37","public:commit:5b47ebf781658c603e7d39d3138fefb53a04affe","public:commit:6147db4b242a5440586e56de45ad6052f9cf497e","public:commit:6821b19285f5d61de5cf096a642c3c6458e6a848","public:commit:7212d677378ad6a0fa7ad2f82765f218f177619f","public:commit:74b1026f73e6666b0574f75b6b625afcc7728c10","public:commit:876128cecdabaaf7a48a58c7e9eb2e0367345999","public:commit:929999b975fb76e6e58ee89a321e8fc60444346a","public:commit:b24d4e82105d9688c0a292af109ed810735b02e7","public:commit:b3f5b1c7d7268b4dbb05b0a02e3d0614f3befe11","public:commit:c7647dc9a1b9983694a4db8dc76c185df10f9b82","public:commit:caf2351137bcdc0485109412dfab9104e9e343c9","public:commit:dbe10270660ca2a45bf315a0c6ae8cc4eeaa9e11","public:commit:dccf908752fe503098552b5d201dd108ae741f43","public:commit:dfd0d25dd91e65c861d6ccd7e1b1970c19f50638","public:commit:e790d467ceb2e95289c117605b46a62c51b8b98c","public:commit:ebbf2f48f08ae5fc7e4a1bb800166d9582b61b2c","public:commit:ed5dae28a848cc6a80bc15e96f2a0cd51bcdf919","public:commit:ee9d5ecd5ce48d8a16d8d330ccc13bfc79dc3d98","public:commit:f5c5d0c490833a9ad5ae72f6deda64bd21f0c5d2"],"source_type":"public","date":"2025-03-11..2025-03-14","topics":["lifetime","ffi","testing","build","performance","api","diagnosis","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Raw packet API, error propagation and test-driven repairs {#raw-packet-api-error-propagation-and-test-driven-repairs}

## Public and native boundary {#public-and-native-boundary}

362–378 replace DataPacket event names and the narrow typed Packet hierarchy with PacketReceive/SendEvent plus integer ID and payload bytes excluding the header. C++ string_view and Player& remain borrowed; Python payload getters create bytes copies. The new DataPacket is an internal native-vtable adapter with borrowed storage, not a public wire-schema validator.374 restores sending after staged deletions,375 restores particles through direct serialization, and378 narrows Python send_packet to bytes. The endpoint still has endstone/network.py importing the removed Packet types; deleting native bindings and stub exports did not complete every Python facade migration.

311 inherited the earlier whole-broadcast cancellation behavior.376 erases only a cancelled recipient, but a non-Player/expired recipient never advances the iterator.380 says parse once but still places parsing inside the recipient loop. Both findings follow exact control flow and persist in the400 main context; no hang or performance experiment was run. The shared send/receive streams and reentrant plugin callbacks also deserve targeted lifetime tests. BinaryStream.writeStream appends without refreshing its cached view, unlike write, so its view/serialization boundary needs validation rather than assuming append is sufficient.

## Error design and observed repairs {#error-design-and-observed-repairs}

365–372 make native Result/expected conversions explicit, attach file/line/context to ErrorInfo, format nested branches and propagate errors through NBT.379 fixes portability mistakes in constructor ordering, macro token pasting and va_list initialization. ReadOnlyBinaryStream initially tests the accumulated masked value’s continuation bit, effectively stopping after one byte.389 fixes this to inspect the original byte and makes overflow sticky while adding seven tests. This is evidence of a real implementation correction paired with tests, not merely the existence of a test file.

The new tests cover borrowed/copied buffer identity, cursor initialization, ordinary byte reads, single-/multi-byte varints300/65535 and exhaustion. They do not constrain overlong varints, and the loop has no shift-width bound. The three ErrorInfo tests assert marker/context/branch text, not complete diagnostic correctness. CallStack’s vector constructor still assigns the shadowing parameter to itself; normal one-frame construction follows a different path. ListTag and NbtIo still ignore nested load results even after the broader propagation refactor, and untrusted list sizes can request allocation without an explicit bound.

## Integration and reuse {#integration-and-reuse}

382 combines the network branch with main’s independent MSVC iterator guard;383 carries it to beta, and392 imports service/tests/layout updates. Imported final blobs and deletion identities are proven per file; all six mixed-blob both-parent residuals were read. Merge completion is integration coverage, not a second independent implementation insight.

## Use and limits {#use-and-limits}

Useful for raw protocol API design, Python/C++ ownership boundaries, cancellation granularity, checking optimization claims against scope and designing malformed-input regressions. Eighteen new tests across this slice were read (eight service, seven stream, three error tests); none were executed. No exploitability or runtime crash claim is established by the conditional static concerns.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-362"></a>
### Commit 362 {#commit-362}

6147db4b242a5440586e56de45ad6052f9cf497e · 2025-03-11T16:43:49Z

[refactor(event)!: rename packet-related events](https://github.com/EndstoneMC/endstone/commit/6147db4b242a5440586e56de45ad6052f9cf497e)

**Observed change.** Breaking rename DataPacketReceive/SendEvent→PacketReceive/SendEvent across headers, C++ NAME, Python bindings/exports/stubs.

**Causal interpretation.** Simplifies public vocabulary before separating packet header and payload; no compatibility aliases retained.

**Limits.** Existing plugins must migrate names; data layout still old at this step.

<a id="commit-363"></a>
### Commit 363 {#commit-363}

dbe10270660ca2a45bf315a0c6ae8cc4eeaa9e11 · 2025-03-11T17:22:57Z

[refactor: remove PacketCodec](https://github.com/EndstoneMC/endstone/commit/dbe10270660ca2a45bf315a0c6ae8cc4eeaa9e11)

**Observed change.** Removes PacketCodec, traits, PacketAdapter and old sendPacket implementation, including the sole spawn-particle codec and old read stub.

**Causal interpretation.** Clears the typed packet abstraction for an unrestricted ID/payload interface; replacement follows374–375.

**Limits.** Intermediate commit lacks replacement methods; no equivalence or runtime continuity claim.

<a id="commit-364"></a>
### Commit 364 {#commit-364}

6821b19285f5d61de5cf096a642c3c6458e6a848 · 2025-03-11T18:39:46Z

[refactor: update `Player::sendPacket` to send raw data](https://github.com/EndstoneMC/endstone/commit/6821b19285f5d61de5cf096a642c3c6458e6a848)

**Observed change.** Deletes Packet/PacketType/SpawnParticleEffect public C++ classes and native Python network binding target; changes Player.sendPacket to integer ID plus string_view.

**Causal interpretation.** Removes the one-packet typed facade and moves serialization responsibility to caller while preserving native Packet adapter internally later.

**Limits.** Temporary API/implementation gap until374; endstone/network.py is not deleted in this slice and can retain imports of removed types.

<a id="commit-365"></a>
### Commit 365 {#commit-365}

876128cecdabaaf7a48a58c7e9eb2e0367345999 · 2025-03-11T20:55:43Z

[refactor: improve the implementation of Bedrock::Result](https://github.com/EndstoneMC/endstone/commit/876128cecdabaaf7a48a58c7e9eb2e0367345999)

**Observed change.** Adds ErrorInfo code/callstack/branches, frame/context builder and richer Result representation.

**Causal interpretation.** Creates a structured error path for local binary parsing instead of only opaque native expected values.

**Limits.** CallStack vector constructor self-assigns its frames parameter, leaving member empty; remains400. Initial Result constructors are revised369; no tests yet.

<a id="commit-366"></a>
### Commit 366 {#commit-366}

dfd0d25dd91e65c861d6ccd7e1b1970c19f50638 · 2025-03-11T20:56:17Z

[refactor: add packet id and payload to `PacketReceiveEvent`, remove `data`](https://github.com/EndstoneMC/endstone/commit/dfd0d25dd91e65c861d6ccd7e1b1970c19f50638)

**Observed change.** PacketReceiveEvent now stores packet_id and borrowed payload excluding header; Python exposes bytes copy and readonly ID.

**Causal interpretation.** Makes wire framing explicit and avoids asking every plugin to decode header.

**Limits.** Handler call site corrected373; C++ payload and player references are callback-lifetime borrows, no retention guarantee.

<a id="commit-367"></a>
### Commit 367 {#commit-367}

caf2351137bcdc0485109412dfab9104e9e343c9 · 2025-03-12T12:03:20Z

[fix: iterator debugging check on MSVC](https://github.com/EndstoneMC/endstone/commit/caf2351137bcdc0485109412dfab9104e9e343c9)

**Observed change.** Includes iterator header under MSVC before asserting _ITERATOR_DEBUG_LEVEL==0 instead of skipping assertion if macro undefined.

**Causal interpretation.** Comment explicitly ties nonzero debugging iterators to incompatibility with Release-built BDS ABI.

**Limits.** Compile-time precondition only, no MSVC build or complete ABI guarantee.

<a id="commit-368"></a>
### Commit 368 {#commit-368}

ebbf2f48f08ae5fc7e4a1bb800166d9582b61b2c · 2025-03-12T21:51:41Z

[feat: implement various methods in `ReadOnlyBinaryStream`](https://github.com/EndstoneMC/endstone/commit/ebbf2f48f08ae5fc7e4a1bb800166d9582b61b2c)

**Observed change.** Implements ReadOnlyBinaryStream borrowed/copied view, bounds/wrap checks, byte and varint reads with ErrorInfo propagation.

**Causal interpretation.** Moves parsing into inspectable local code, separating view ownership and cursor movement.

**Limits.** Overflow flag not set on failure until389. Varint tests value's bit7 after masking rather than input continuation bit and stops after first byte; fixed389. No length/shift bound.

<a id="commit-369"></a>
### Commit 369 {#commit-369}

c7647dc9a1b9983694a4db8dc76c185df10f9b82 · 2025-03-12T21:52:02Z

[refactor: improve `Bedrock::Result`](https://github.com/EndstoneMC/endstone/commit/c7647dc9a1b9983694a4db8dc76c185df10f9b82)

**Observed change.** Refines Result with expected constructors, ignoreError/discardError/asExpected/logError; adds file/line/context error macros and rethrow frame attachment.

**Causal interpretation.** Explicit conversion/error-flow methods support native error propagation while preserving details for logging.

**Limits.** Nonportable ##MESSAGE and va_list initialization corrected379. No general proof of safe printf formatting for arbitrary message contents.

<a id="commit-370"></a>
### Commit 370 {#commit-370}

0268d7ce5e23eff393346074f054298fb367c720 · 2025-03-12T21:52:15Z

[feat: add custom formatter for `CallStack`](https://github.com/EndstoneMC/endstone/commit/0268d7ce5e23eff393346074f054298fb367c720)

**Observed change.** Adds fmt formatters for callstack context, frame, framed context and frame vector joined by newlines.

**Causal interpretation.** Makes structured native-error data usable in diagnostics, including optional area/level.

**Limits.** Formatting does not repair365's vector-constructor loss; no formatter snapshot test.

<a id="commit-371"></a>
### Commit 371 {#commit-371}

5b47ebf781658c603e7d39d3138fefb53a04affe · 2025-03-12T21:52:27Z

[feat: add custom formatter for `LogLevel` and `LogArea`](https://github.com/EndstoneMC/endstone/commit/5b47ebf781658c603e7d39d3138fefb53a04affe)

**Observed change.** Formats LogLevel and LogAreaID using magic_enum names.

**Causal interpretation.** Keeps log-context names readable without maintaining parallel manual switches.

**Limits.** Unknown values yield library naming behavior; no enum-completeness test.

<a id="commit-372"></a>
### Commit 372 {#commit-372}

07362783b0d56fe5f13963d3189b47b65be7f058 · 2025-03-12T21:52:51Z

[refactor: improve error handling in nbt-related classes](https://github.com/EndstoneMC/endstone/commit/07362783b0d56fe5f13963d3189b47b65be7f058)

**Observed change.** Updates scalar/array/list/compound/NbtIo reads to explicit Result error conversion and rethrow frames; unknown Tag ID creates bad_message.

**Causal interpretation.** Propagates low-level read errors with local context rather than reducing all to boolean success.

**Limits.** ListTag nested tag load and NbtIo named-tag load still ignore nested results; list/int-array sizes remain allocation concerns. No NBT malformed-input tests added.

<a id="commit-373"></a>
### Commit 373 {#commit-373}

7212d677378ad6a0fa7ad2f82765f218f177619f · 2025-03-12T21:53:34Z

[fix: update PacketReceiveEvent constructor](https://github.com/EndstoneMC/endstone/commit/7212d677378ad6a0fa7ad2f82765f218f177619f)

**Observed change.** Handler decodes unsigned varint header, masks10-bit packet ID and exposes remaining payload; parse failure cancels. Adds magic_enum package linkage.

**Causal interpretation.** Completes366's handler/API migration and error logging; sender/target sub-IDs extracted but unused.

**Limits.** Until389 the decoder's continuation bug corrupts multibyte framing. Shared network receive buffer is borrowed; no reentrant packet test.

<a id="commit-374"></a>
### Commit 374 {#commit-374}

ed5dae28a848cc6a80bc15e96f2a0cd51bcdf919 · 2025-03-12T23:44:00Z

[feat: re-implement `Player::sendPacket`](https://github.com/EndstoneMC/endstone/commit/ed5dae28a848cc6a80bc15e96f2a0cd51bcdf919)

**Observed change.** Adds DataPacket native adapter with int ID/borrowed payload, checkSize threshold0xA00000 for server receive, writeStream forwarding; reinstates Player.sendPacket.

**Causal interpretation.** A small native-vtable adapter preserves existing sendNetworkPacket while allowing arbitrary payload types.

**Limits.** No ID/schema validation, read does not advance cursor, payload not owned. writeStream appends without refreshing destination view_, unlike write; native use and reallocation consequences untested.

<a id="commit-375"></a>
### Commit 375 {#commit-375}

1473fd5a550ea27871d875039a024610d18b9d0f · 2025-03-12T23:55:02Z

[feat: re-implement `Player::sendParticle`](https://github.com/EndstoneMC/endstone/commit/1473fd5a550ea27871d875039a024610d18b9d0f)

**Observed change.** Restores particle serialization directly into BinaryStream and invokes raw sendPacket; initializes cursor/overflow fields and default stream.

**Causal interpretation.** Preserves particle field order including dimension, actor−1, position, effect name, optional Molang; no typed public packet required.

**Limits.** Default ctor initially refers to base storage in base initializer, revised379. Native receiver/schema and payload lifetime untested.

<a id="commit-376"></a>
### Commit 376 {#commit-376}

e790d467ceb2e95289c117605b46a62c51b8b98c · 2025-03-12T23:59:58Z

[fix: canceling a single receipt's PacketSendEvent for broadcast packets no longer affects other receipts](https://github.com/EndstoneMC/endstone/commit/e790d467ceb2e95289c117605b46a62c51b8b98c)

**Observed change.** Outgoing broadcast iterates mutable recipients and erases only the recipient whose event is cancelled.

**Causal interpretation.** Fixes311's any-recipient-cancellation aborting whole broadcast.

**Limits.** If WeakEntityRef cannot unwrap Player, neither erase nor increment executes, so loop can stall. No invalid-recipient/broadcast regression test; persists400.

<a id="commit-377"></a>
### Commit 377 {#commit-377}

ee9d5ecd5ce48d8a16d8d330ccc13bfc79dc3d98 · 2025-03-13T00:04:00Z

[refactor: add packet id and payload to `PacketSendEvent`, remove `data`](https://github.com/EndstoneMC/endstone/commit/ee9d5ecd5ce48d8a16d8d330ccc13bfc79dc3d98)

**Observed change.** PacketSendEvent mirrors receive ID/payload API, removes data property, decodes header and forwards remaining bytes.

**Causal interpretation.** Unifies ingress/egress event contract and cancellation behavior.

**Limits.** Parsing still per recipient; packet/player/payload lifetime and reentrancy remain untested.

<a id="commit-378"></a>
### Commit 378 {#commit-378}

74b1026f73e6666b0574f75b6b625afcc7728c10 · 2025-03-13T00:08:17Z

[feat: update python bindings](https://github.com/EndstoneMC/endstone/commit/74b1026f73e6666b0574f75b6b625afcc7728c10)

**Observed change.** Removes old typed Packet exports from generated stub and changes send_packet signature to ID and bytes. Pybind lambda takes py::bytes explicitly.

**Causal interpretation.** Ensures raw binary Python argument rather than accidental Unicode conversion surface.

**Limits.** Synchronous conversion/use assumed; retained native payload is not owned. Endpoint endstone/network.py still imports all three removed types; facade migration is incomplete.

<a id="commit-379"></a>
### Commit 379 {#commit-379}

36dfdefdc08cd81ef56b4c95ad147d9a0e395fe2 · 2025-03-13T00:34:00Z

[fix: compilation errors on Linux](https://github.com/EndstoneMC/endstone/commit/36dfdefdc08cd81ef56b4c95ad147d9a0e395fe2)

**Observed change.** Default BinaryStream base constructed with empty view then bound to initialized storage; removes invalid macro token paste and zero-initializes va_list.

**Causal interpretation.** Fixes concrete C++ portability issues instead of relying on Windows compiler tolerance.

**Limits.** No compiler execution. writeStream still omits view refresh and varint issue remains until389.

<a id="commit-380"></a>
### Commit 380 {#commit-380}

929999b975fb76e6e58ee89a321e8fc60444346a · 2025-03-13T00:41:04Z

[refactor: only parse the outgoing packet once](https://github.com/EndstoneMC/endstone/commit/929999b975fb76e6e58ee89a321e8fc60444346a)

**Observed change.** Moves outgoing header parsing outside successful Player-unwrapping branch but leaves it inside recipient for-loop.

**Causal interpretation.** Title says only parse once; actual scope does not establish that optimization and now parses even invalid recipients.

**Limits.** No measured parse-count/performance result.376 stalled-iterator case remains.

<a id="commit-381"></a>
### Commit 381 {#commit-381}

1c8d9e896daa1227a71e7df3e208eb3590013c85 · 2025-03-13T00:41:11Z

[style: code clean up](https://github.com/EndstoneMC/endstone/commit/1c8d9e896daa1227a71e7df3e208eb3590013c85)

**Observed change.** Normalizes local include spelling/order and removes space before semicolon.

**Causal interpretation.** Exact mechanical cleanup; no independent engineering preference or behavioral result.

**Limits.** No build run.

<a id="commit-382"></a>
### Commit 382 {#commit-382}

dccf908752fe503098552b5d201dd108ae741f43 · 2025-03-13T00:42:17Z

[refactor: redesign the network API and events](https://github.com/EndstoneMC/endstone/commit/dccf908752fe503098552b5d201dd108ae741f43)

**Observed change.** Merges network redesign branch into main;42 of43 changed/deleted tree entries match second parent, umbrella header combines packet removal with main's MSVC guard.

**Causal interpretation.** Ancestry and per-file blob identity reuse362–381 substantive reading; both-parent residual for umbrella header read fully.

**Limits.** No new independent network feature credit for integration; merge tree is not runtime validation.

<a id="commit-383"></a>
### Commit 383 {#commit-383}

f5c5d0c490833a9ad5ae72f6deda64bd21f0c5d2 · 2025-03-13T00:46:30Z

[Merge remote-tracking branch 'origin/main' into feat/1.21.70-support](https://github.com/EndstoneMC/endstone/commit/f5c5d0c490833a9ad5ae72f6deda64bd21f0c5d2)

**Observed change.** Merges main network redesign into1.21.70-support.41 of46 changed/deleted entries match second parent; five mixed files combine raw packet API, dynamic address facade, certificate removal and Windows winext build.

**Causal interpretation.** Read both-parent residuals for all mixed blobs; semantic union preserves both branch changes rather than attributing merge as new implementation.

**Limits.** No conflicts in combined diff, but that alone was not used as review proof. Beta branch is not an ancestor of400 main endpoint.

<a id="commit-389"></a>
### Commit 389 {#commit-389}

b3f5b1c7d7268b4dbb05b0a02e3d0614f3befe11 · 2025-03-14T18:30:54Z

[test: add tests for `ReadOnlyBinaryStream`](https://github.com/EndstoneMC/endstone/commit/b3f5b1c7d7268b4dbb05b0a02e3d0614f3befe11)

**Observed change.** Adds seven ReadOnlyBinaryStream tests and fixes continuation check to inspect byte, sets overflow sticky, moves constructor out-of-line and exposes hasOverflowed.

**Causal interpretation.** Tests motivate implementation repairs: multi-byte300/65535 decoding and exhausted-buffer error flag are asserted, not just tests added.

**Limits.** No tests executed. No overlong varint/shift-width bound, truncated continuation, zero-length-after-overflow, writeStream view-refresh or copying-stream lifetime tests.

<a id="commit-390"></a>
### Commit 390 {#commit-390}

b24d4e82105d9688c0a292af109ed810735b02e7 · 2025-03-14T18:42:06Z

[test: add tests for `Bedrock::ErrorInfo`](https://github.com/EndstoneMC/endstone/commit/b24d4e82105d9688c0a292af109ed810735b02e7)

**Observed change.** Moves binary tests unchanged into bedrock folder and adds three ErrorInfo formatting tests for Error marker, custom context and branch marker repetition.

**Causal interpretation.** Provides minimal diagnostics regression coverage and aligns test organization with native layer.

**Limits.** First test does not assert actual error text; branches test only counts marker occurrence. Vector CallStack constructor, rethrow chain and printf logging are untested.

<a id="commit-392"></a>
### Commit 392 {#commit-392}

54b59302b21ad85f094ec4a045dd37352f41db37 · 2025-03-14T21:31:35Z

[Merge remote-tracking branch 'origin/main' into feat/1.21.70-support](https://github.com/EndstoneMC/endstone/commit/54b59302b21ad85f094ec4a045dd37352f41db37)

**Observed change.** Merges eight main service/test/network-layout commits384–391 into beta; all23 first-parent changed/deleted entries equal second parent blobs.

**Causal interpretation.** Exact content and ancestry proof permit reuse of already-read implementation and tests, preserving branch causality.

**Limits.** No independent implementation credit or runtime verification;393 modifies beta immediately afterward.
