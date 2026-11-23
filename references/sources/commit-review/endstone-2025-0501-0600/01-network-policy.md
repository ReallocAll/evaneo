<!-- retrieval: {"source_ids":["public:commit:074e3369d8168ffe7e2d271ad0840b88bb5e68fa","public:commit:211bdc1dd65e95a21eb497f43c71a0c3bdfa466b","public:commit:21fff3038585eb88855b2e6b39d9b94f44932e3f","public:commit:5053644cb381587b4ff473bd7b25074537e579e5","public:commit:5684de92ab395eea653bc823226aefb2207e3355","public:commit:57e40293a93104aa67ba157b0f4dc2c1c5eb1710","public:commit:583f2d97024d574fb5874dd67200f613dbcef46c","public:commit:5a0a1829862deca2e8b5992e1aefa5a2c45ad1d8","public:commit:5ee4dd86c23a5376fc0d378598c3acec8a9cd9e2","public:commit:5ff02c947798f475928bd81e469990906e60d7a8","public:commit:7294e3bb57119fa6408e39fe9a0fc55f12af26ef","public:commit:789ec374b606db3d3ff6457aff2f74441f1f7bfa","public:commit:8161d55623d0520c0737a0f52fbf5efebd9dbbba","public:commit:bd8354471e3fae29867415240af2bd5ed2b4d1e1","public:commit:c10fe38e8c8fcc50ea7573c361391c163d284a5b","public:commit:cc080c7f876f0492d35e293fb65c644fbd479748","public:commit:e624c136529527176efa75afea651ef086ae0cd9","public:commit:ea167a2572c47743ca6c28f8f2bc2909f8236c78","public:commit:f726b972d9df18e0f9eeaa1f10b99bf4f51ff7bf","public:thread:EndstoneMC/endstone:168","public:thread:EndstoneMC/endstone:170","public:thread:EndstoneMC/endstone:171","public:thread:EndstoneMC/endstone:173"],"source_type":"public","date":"2025-03-27..2025-04-12","topics":["lifetime","ffi","testing","build","performance","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Packet ownership, configuration and player lifecycle {#packet-ownership-configuration-and-player-lifecycle}

Scope: historical 2025 ordinals listed below, with exact SHA links and offline patches. Source reasoning is static; no server, upstream code, tests or native binaries were executed.

<a id="causal-chain-and-tradeoffs"></a>
## Causal chain and tradeoffs {#causal-chain-and-tradeoffs}

Sibling's 498 removes the problematic outgoing-recipient loop and temporarily makes the scripting outgoing handler a no-op. Here 503 restores PacketSendEvent at NetworkSystem::send, where one local serialization buffer belongs to one invocation. A plugin that sends another packet recursively no longer necessarily shares that buffer. The native callback runs first; plugin cancellation then stops this send. Changed payload is recognized by its data pointer and re-encoded with the original header. Payload views remain borrowed for the callback lifetime; this is not an owning event API. Commit508 calls this path for each recipient, exchanging repeated serialization for independent filtering/cancellation.

The initial raw-packet adapter advertises ID -1 to distinguish it from native typed packets. Observer/statistics participation restored514 exposes why such identity shortcuts cross subsystem boundaries;519 returns the real ID and uses the adapter's name instead. The shutdown-fix claim comes from the author. It was not reproduced here. Packet observers still receive the original Packet object even if plugins alter serialized bytes.

Configuration505–511 replaces an unconditional resource-pack policy patch with an operator-facing, default-false TOML setting. Existing config is preserved. Constructor-only parsing and current-level access are explicit; live reload is not supplied. The source allows personal client packs only when the operator opts in, keeping vanilla enforcement as default. The earlier unconditional policy and PocketMine source credit belong to sibling453 and must not be erased by this refinement.

Issue171's reporter, Atomic69420, identifies repeated initialization packets causing repeated plugin join/perms/commands side effects and raises runtime-ID validation. Commit542 sets a wrapper-local spawned flag before callbacks, removes the native flag mutation and native initializer hook, and dispatches first-spawn work from the incoming hook. Native scripting rejection precedes this hook's plugin processing, but doFirstSpawn still precedes public PacketReceiveEvent cancellation and reparsing. Thus the patch bounds repeated plugin side effects; it does not demonstrate native runtime-ID validation, or promise cancellation suppresses join effects.

Broadcast543 retains Message/Translatable until delivery instead of translating before the broadcast event. Python stub545 follows;544 sets embedded Python's private _base_executable for multiprocessing compatibility. These are observed integration changes, not validated locale/child-process outcomes.

<a id="form-contribution-and-revisions"></a>
## Form contribution and revisions {#form-contribution-and-revisions}

Non-target daoge/smartcmd PR168, SHA1dc0af157bea9b749ede7a9352dafb1a5ab4099a, moves Button out of ActionForm, replaces button-only storage with a variant of Button/Divider/Header/Label, adds Header/Divider to modal controls, updates Python exports/bindings/stubs, and writes action forms as elements. Divider/header JSON supplies text because a source comment reports client rejection without it. The callback walks button entries only. Vincent518 changes the counter expression, while daoge PR173/8095d769c2927df8bf15b42bf242beefb2cc5688 adds the required type=button field;560 integrates it. Both versions invoke a selected empty on_click without a guard. No form rendering or callback execution was performed. The stub's116 identical conduit removals were structurally accounted, with every remaining semantic hunk read.

The accessible PR168 Copilot review says it covered2/11 files with no comments and excluded all nine C++ files as unsupported. This is explicit AI review attribution, not proof of AI code generation or comprehensive approval. PR173's primary identifies smartcmd; unavailable discussion endpoints remain a context limit.

## When useful {#when-useful}

Use this case when designing mutable packet interception, reentrant serialization, preserving native side effects, separating operator policy from protocol patching, or placing one-time lifecycle guards. Do not copy the sentinel/name tricks, borrowed payload contract, event casting or security conclusions without checking current native behavior and ownership.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-501"></a>
### Commit 501 {#commit-501}

cc080c7f876f0492d35e293fb65c644fbd479748 · 2025-03-27T01:10:20Z

[fix: use platform-specific byte swap for big-endian int writes](https://github.com/EndstoneMC/endstone/commit/cc080c7f876f0492d35e293fb65c644fbd479748)

**Observed change.** Uses _byteswap_ulong on MSVC and __builtin_bswap32 elsewhere for big-endian 32-bit writes.

**Causal interpretation.** Makes the byte-swap implementation compiler-specific while retaining the little-endian-host encoding assumption.

**Limits.** No platform compilation or non-little-endian validation.

<a id="commit-502"></a>
### Commit 502 {#commit-502}

e624c136529527176efa75afea651ef086ae0cd9 · 2025-03-27T01:23:12Z

[fix: resolve compilation errors on Linux](https://github.com/EndstoneMC/endstone/commit/e624c136529527176efa75afea651ef086ae0cd9)

**Observed change.** Casts INT_MAX to double before normalized-float scaling into signed varint64; adds <memory> to function_ref.

**Causal interpretation.** Repairs portability/precision at the expression boundary rather than changing the wire format intentionally.

**Limits.** Linux compile success is the title's claim; not executed here.

<a id="commit-503"></a>
### Commit 503 {#commit-503}

5ff02c947798f475928bd81e469990906e60d7a8 · 2025-03-27T14:29:21Z

[fix: correct the implementation of `PacketSendEvent`](https://github.com/EndstoneMC/endstone/commit/5ff02c947798f475928bd81e469990906e60d7a8)

**Observed change.** Replaces outgoing shared-stream handling with a local BinaryStream per send; runs native outgoing callbacks, writes packet header then body, exposes body to PacketSendEvent, cancels early or re-encodes changed data, updates timestamp and calls _sendInternal. DataPacket temporarily reports ID -1 while separately exposing real ID; raw bytes bypass stream-view cache. Adds a NetEventCallback virtual.

**Causal interpretation.** Per-call storage removes the shared mutable buffer implicated in reentrant sends. Borrowed event payload points into local stream until callback completion; pointer-identity change is used to detect replacement. Header includes sender/client subids. Native StartGame/resource-pack patching excludes DataPacket adapters.

**Limits.** No reentrancy test or profiler run. ID -1 is a temporary identity trick later reversed by 519. Callback acceptance and native packet patching still precede plugin event dispatch.

<a id="commit-504"></a>
### Commit 504 {#commit-504}

ea167a2572c47743ca6c28f8f2bc2909f8236c78 · 2025-03-27T14:29:28Z

[Merge remote-tracking branch 'origin/main'](https://github.com/EndstoneMC/endstone/commit/ea167a2572c47743ca6c28f8f2bc2909f8236c78)

**Observed change.** Merges the Linux expression/include fixes from 502 into outgoing-packet work; both changed files exactly equal the second-parent blobs.

**Causal interpretation.** Two-parent identity proof permits reuse of the already-read fix without inventing a second design decision.

**Limits.** No merge-specific test evidence; exact imported blobs recorded.

<a id="commit-505"></a>
### Commit 505 {#commit-505}

57e40293a93104aa67ba157b0f4dc2c1c5eb1710 · 2025-03-27T15:27:23Z

[feat(config): add `endstone.toml`](https://github.com/EndstoneMC/endstone/commit/57e40293a93104aa67ba157b0f4dc2c1c5eb1710)

**Observed change.** Bootstrap derives endstone.toml beside the server and copies packaged defaults only when absent. New settings.allow-client-packs defaults false and is documented in relation to texturepack-required.

**Causal interpretation.** Preserves existing user configuration instead of overwriting on startup; supplies a discoverable opt-in policy surface.

**Limits.** Copy/config permissions and packaging were not exercised.

<a id="commit-506"></a>
### Commit 506 {#commit-506}

5a0a1829862deca2e8b5992e1aefa5a2c45ad1d8 · 2025-03-27T15:49:56Z

[feat: add config option for client resource packs](https://github.com/EndstoneMC/endstone/commit/5a0a1829862deca2e8b5992e1aefa5a2c45ad1d8)

**Observed change.** Adds tomlplusplus dependency/linking. Server constructor parses cwd endstone.toml once, defaults allow_client_packs_ false, logs parse errors. ResourcePackStack suppression of texture-pack-required becomes conditional on opt-in; StartGame client-generation policy checks current level instead of a static cached value.

**Causal interpretation.** Restores native resource-pack enforcement by default while retaining an explicit customization. Constructor-only parse is a startup policy, not demonstrated live reload.

**Limits.** No parse/reload/client interoperability tests. Missing/wrong-type setting falls back false; native-layout writes remain version dependent.

<a id="commit-507"></a>
### Commit 507 {#commit-507}

789ec374b606db3d3ff6457aff2f74441f1f7bfa · 2025-03-27T15:52:40Z

[chore: update comment in configuration file](https://github.com/EndstoneMC/endstone/commit/789ec374b606db3d3ff6457aff2f74441f1f7bfa)

**Observed change.** Rewords the allow-client-packs comment to describe personal packs alongside required server packs.

**Causal interpretation.** Documentation refinement of the same opt-in policy, not independent implementation evidence.

**Limits.** No new behavior.

<a id="commit-508"></a>
### Commit 508 {#commit-508}

c10fe38e8c8fcc50ea7573c361391c163d284a5b · 2025-03-27T17:10:11Z

[feat: hook `NetworkSystem::sendToMultiple` for broadcast packets](https://github.com/EndstoneMC/endstone/commit/c10fe38e8c8fcc50ea7573c361391c163d284a5b)

**Observed change.** Adds sendToMultiple hook and platform symbol entries; loops recipients and invokes the single-recipient send path.

**Causal interpretation.** Reuses per-recipient filtering, cancellation and mutable-payload handling instead of one all-recipient decision. Each recipient incurs serialization and callback work.

**Limits.** No throughput measurement. The const native packet is still patched through const_cast; recipient-specific mutation must not be assumed isolated merely because stream buffers are.

<a id="commit-509"></a>
### Commit 509 {#commit-509}

5ee4dd86c23a5376fc0d378598c3acec8a9cd9e2 · 2025-03-27T17:41:30Z

[docs: update CHANGELOG.md](https://github.com/EndstoneMC/endstone/commit/5ee4dd86c23a5376fc0d378598c3acec8a9cd9e2)

**Observed change.** Adds 0.7.1 release notes and changes patch version to 1, reporting reentrant outgoing-packet crash fix, mutable payload APIs, native1.21.70.04 and operator configuration.

**Causal interpretation.** Release communication connects 503/508 to user-visible reliability; it is an author report rather than new execution evidence.

**Limits.** Release-note link still targets v0.7.0. No runtime outcome independently verified.

<a id="commit-510"></a>
### Commit 510 {#commit-510}

074e3369d8168ffe7e2d271ad0840b88bb5e68fa · 2025-03-27T17:46:34Z

[style: code clean up](https://github.com/EndstoneMC/endstone/commit/074e3369d8168ffe7e2d271ad0840b88bb5e68fa)

**Observed change.** Removes obsolete PacketSendEvent friendship and normalizes member formatting after the send rewrite.

**Causal interpretation.** Tightens access surface now that events receive payload directly; no intended protocol change.

**Limits.** No independent performance or reliability lesson.

<a id="commit-511"></a>
### Commit 511 {#commit-511}

21fff3038585eb88855b2e6b39d9b94f44932e3f · 2025-03-27T17:53:45Z

[docs: update CHANGELOG.md](https://github.com/EndstoneMC/endstone/commit/21fff3038585eb88855b2e6b39d9b94f44932e3f)

**Observed change.** Clarifies configuration prose that server packs remain required while personal packs can be allowed.

**Causal interpretation.** Separates native enforcement from the explicit personal-pack override for operators.

**Limits.** Documentation only.

<a id="commit-514"></a>
### Commit 514 {#commit-514}

8161d55623d0520c0737a0f52fbf5efebd9dbbba · 2025-03-28T13:10:28Z

[feat: notify packet observers on packet sent](https://github.com/EndstoneMC/endstone/commit/8161d55623d0520c0737a0f52fbf5efebd9dbbba)

**Observed change.** Defines IPacketObserver's virtual surface/24-byte layout and calls packetSentTo before peer send after connection/peer guards.

**Causal interpretation.** Restores observer/statistics participation bypassed by custom _sendInternal, completing more of the native send side effects.

**Limits.** At this stage DataPacket can still expose ID -1; 519 reverses that marker. Layout and observer invocation not runtime validated.

<a id="commit-517"></a>
### Commit 517 {#commit-517}

bd8354471e3fae29867415240af2bd5ed2b4d1e1 · 2025-04-06T22:52:06Z

[fix: `Player::playSound` now works as expected](https://github.com/EndstoneMC/endstone/commit/bd8354471e3fae29867415240af2bd5ed2b4d1e1)

**Observed change.** NetworkBlockPosition constructors scale integer coordinates by 8; playSound constructs it from location cast to int. Python volume/pitch defaults become 1.0.

**Causal interpretation.** Issue 170 by Cdm2883 reports play_sound inactivity on Windows 0.7.2/1.21.71; Vincent confirms bug/fix. Corrects protocol fixed-point scaling and API defaults.

**Limits.** Fractional coordinates are discarded before scaling; negative casts truncate toward zero. Reporter/maintainer statements are not our client playback validation.

<a id="commit-518"></a>
### Commit 518 {#commit-518}

211bdc1dd65e95a21eb497f43c71a0c3bdfa466b · 2025-04-06T23:07:26Z

[refactor: improve action form callback handling](https://github.com/EndstoneMC/endstone/commit/211bdc1dd65e95a21eb497f43c71a0c3bdfa466b)

**Observed change.** Changes action-form selection traversal from decrementing requested selection to a separate button-only index counter.

**Causal interpretation.** Completes daoge's mixed button/header/divider/label control model while preserving reported selection for on_submit.

**Limits.** Selected button callback is invoked without checking for an empty function; no response test. See non-target PR168 and later codec correction PR173.

<a id="commit-519"></a>
### Commit 519 {#commit-519}

7294e3bb57119fa6408e39fe9a0fc55f12af26ef · 2025-04-07T12:26:39Z

[fix: resolve crash occurring during server shutdown after `Player::sendPacket`](https://github.com/EndstoneMC/endstone/commit/7294e3bb57119fa6408e39fe9a0fc55f12af26ef)

**Observed change.** Restores DataPacket::getId to its real ID and identifies raw adapters by getName instead of negative ID; cleans parameter names.

**Causal interpretation.** Reverses the 503 sentinel after the author reports a server-shutdown crash. Native observers/other consumers can again see valid packet IDs.

**Limits.** No shutdown reproduction. Name-based static_cast relies on unique/truthful adapter naming.

<a id="commit-542"></a>
### Commit 542 {#commit-542}

583f2d97024d574fb5874dd67200f613dbcef46c · 2025-04-12T09:54:09Z

[fix: ensure `SetLocalPlayerAsInitializedPacket` is handled only once when a player joins](https://github.com/EndstoneMC/endstone/commit/583f2d97024d574fb5874dd67200f613dbcef46c)

**Observed change.** Moves first-spawn plugin work into EndstonePlayer::doFirstSpawn with spawned_ checked/set before callbacks; incoming packet hook invokes it, and native setLocalPlayerAsInitialized hook no longer sets initialized flag or dispatches join work.

**Causal interpretation.** Issue171 by Atomic69420 reports repeated initialized packets causing duplicate join/perms/commands and unchecked runtime ID. Wrapper-local once guard bounds the plugin side effect and avoids manually changing native initialization state.

**Limits.** No exploit reproduction. The patch does not itself prove native runtime-ID validation; guard persists for wrapper lifetime, and receive-event ordering remains relevant.

<a id="commit-543"></a>
### Commit 543 {#commit-543}

5053644cb381587b4ff473bd7b25074537e579e5 · 2025-04-12T10:10:33Z

[fix: death message is now correctly localised based on client language](https://github.com/EndstoneMC/endstone/commit/5053644cb381587b4ff473bd7b25074537e579e5)

**Observed change.** BroadcastMessageEvent stores Message variant rather than string; server passes original Message instead of pre-translating.

**Causal interpretation.** Keeps Translatable identity until recipient delivery, enabling per-recipient locale handling rather than freezing server-language text early.

**Limits.** API/ABI type change; no multi-locale runtime test. Stub follows545.

<a id="commit-544"></a>
### Commit 544 {#commit-544}

f726b972d9df18e0f9eeaa1f10b99bf4f51ff7bf · 2025-04-12T10:27:59Z

[fix: Python interpreter now launches correctly in multiprocessing](https://github.com/EndstoneMC/endstone/commit/f726b972d9df18e0f9eeaa1f10b99bf4f51ff7bf)

**Observed change.** Sets Python sys._base_executable alongside sys.executable when embedded interpreter path is resolved.

**Causal interpretation.** Compatibility adjustment for multiprocessing/executable discovery in embedded Python.

**Limits.** Private interpreter attribute; no spawned child or portable-distribution test.

<a id="commit-545"></a>
### Commit 545 {#commit-545}

5684de92ab395eea653bc823226aefb2207e3355 · 2025-04-12T10:31:37Z

[feat: update stubs for python bindings](https://github.com/EndstoneMC/endstone/commit/5684de92ab395eea653bc823226aefb2207e3355)

**Observed change.** Updates BroadcastMessageEvent Python getter/setter stub from str to str|Translatable.

**Causal interpretation.** Completes published typing for 543 without independent runtime behavior.

**Limits.** Stub consistency only.
