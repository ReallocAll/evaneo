<!-- retrieval: {"source_ids":["public:commit:04382f6c1f157046339225ab6de16204e13d6763","public:commit:06ce8871e4ce49b09079845f097f839e23a094e5","public:commit:0d0c48ebbed993642ae800cb12db5c182e9a2c2d","public:commit:15ed7ff932eb79239933e368e40cfc0a9d5d3e21","public:commit:2b1d39150120d90b9fccf3a331e4402122feca57","public:commit:2e9873f0a61452f18127360655bc976896a58231","public:commit:38bfc6c53df32792d1ec798ab61ae8254272c762","public:commit:6e4b448c5533405c1e60d4751862472c76a2f335","public:commit:73b97731312275fd488176f4c12ad55b6384fb14","public:commit:81d3ee0391bdae8e80b719db999b110c14e9ac7b","public:commit:85ff264f0c5b7cb883dca3f24e2772b2e73fb28c","public:commit:92569ca1b2eda7acc2972022fc6ab260c0233fad","public:commit:96ee3a8d37421e697db0f30b31362c6e23822a12","public:commit:9b5a77bb8e86d38cb7517e2c65fc9880356d3688","public:commit:a87b940e1d79d1cc5d677f0fe529d51e0a218e05","public:commit:b209f49ab18ba0e97d64e98bce40d5b877a28260","public:commit:b5fb6c8c55533a845417eb5c8fe85e70154a3dd4","public:commit:da9b2316c79829f93579d15afdad095af7d57118","public:commit:dc6d78e0f2d48ffcb88fda15e53ddfd50a2fae85","public:commit:f454f49adbad2448e66c3cafe497dd191fc38a74","public:commit:f6751f87e4411563c51d2bc8c165ca4fdbe6d376"],"source_type":"public","date":"2025-11-17..2025-12-14","topics":["ffi","testing","build","performance","recovery","api","diagnosis","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Input defense and connection cleanup {#input-defense-and-connection-cleanup}

## Defense in layers, with revisions preserved {#defense-in-layers-with-revisions-preserved}

Certificate handling starts by rejecting unexpected JSON root/chain shapes and long chains (1306), then adds a document-size cap before parsing (1307). Accepted inputs still delegate to native parsing. The guard catches exceptions and returns an empty token with no parent, rather than modifying authentication state directly. It is removed during the December compatibility port (1353), restored with a chain limit of ten (1359), then paired with a null-this validate hook and UNIX compiler option (1360–1361). These are separate historical decisions. Neither a changelog nor the presence of a guard proves comprehensive validation or portable C++ safety.

The item-hang repair replaces a native parser with a restricted marker/version decoder. It supplies NBT parsing and can-place/can-destroy component loops, then switches the block-name resolver back to a native symbol. Compound parsing now stops at End. List parsing gains type and empty-list checks. However the reconstructed NBT reader discards nested load Results, negative list lengths still reach reserve, and count/depth/resource limits are not established in these bodies. This is evidence for checking error propagation across the complete call chain, not for claiming a proven exploitable path or an exhaustive security audit.

Disconnect behavior evolves through explicit alternatives:

1. 1319 marks a connection disconnected and stops local receive processing.
2. 1326 synthesizes a local Disconnect packet to trigger cleanup, then touches the saved connection pointer.
3. 1328 removes the flag/receive guard and avoids using that pointer after synthetic dispatch.
4. 1329 closes only primary-client transport through NetworkSystem, replacing synthetic dispatch.
5. 1330 disables the added close call despite its version-bump title.
6. 1331 corrects the native onConnectionClosed signature by adding session_summary, then restores the explicit close.

The final path is not all six mechanisms at once. Native disconnect notification runs first; primary clients then invoke full local/remote close. Subclients retain the shared transport. Packet limiting is enabled separately through reloadpacketlimitconfig, and RakNet connection-frequency limiting is moved before native peer startup. Return values, configured thresholds and throughput remain unverified.

## Error contracts and costs {#error-contracts-and-costs}

The parser hooks return early through void APIs and can leave partial state. Empty-compound recovery trades availability for loss of invalid payload data. Native delegation reduces reconstructed code but increases dependence on exact symbols; issue312 later exposes that dependency. Rate limiting and same-IP connection limits can affect legitimate bursts/shared-address clients, but no measured tuning rationale is present.

The final null-this guard depends on compiler behavior; -fno-delete-null-pointer-checks applies to the whole UNIX runtime target. std::launder is not a general pointer validator, and a normal C++ null member call is not made valid by the source spelling alone. These are bounded static cautions, not runtime claims.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1306"></a>
## Commit 1306 {#commit-1306}

da9b2316c79829f93579d15afdad095af7d57118 · 2025-11-17T20:22:17Z

[fix: patch a vulnerability caused by improperly sized certificate chains](https://github.com/EndstoneMC/endstone/commit/da9b2316c79829f93579d15afdad095af7d57118)

**Change and causal context.** Adds a certificate input detour and matching symbol/CMake wiring. It parses JSON, requires an object whose chain is an array of at most three elements, delegates only accepted shapes, catches exceptions and returns an empty token/null parent otherwise. Login IP-ban checking moves before native login handling and before connection-request inspection; identity bans remain afterward. Removes the map debug printf and updates advertised Minecraft version.

**Rationale and attribution.** Commit explicitly describes improperly sized certificate chains as a vulnerability; implementation is defensive bounded delegation.

**Limits and counterexamples.** Initial guard has no input byte cap, element-type validation or minimum chain length. The original void login dispatcher supplies no explicit success result before identity access. No exploit or operational outcome is reproduced.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1307"></a>
## Commit 1307 {#commit-1307}

2e9873f0a61452f18127360655bc976896a58231 · 2025-11-17T20:56:28Z

[fix: add input size validation in `UnverifiedCertificate::fromString`](https://github.com/EndstoneMC/endstone/commit/2e9873f0a61452f18127360655bc976896a58231)

**Change and causal context.** Adds a 0x300000-byte maximum before JSON parsing, bounding the accepted certificate document size as well as the chain count. Oversized input takes the same empty-certificate failure path.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** The cap does not itself prove bounded JSON recursion, CPU cost or complete certificate validity; native accepted-input processing still runs.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1308"></a>
## Commit 1308 {#commit-1308}

9b5a77bb8e86d38cb7517e2c65fc9880356d3688 · 2025-11-17T23:17:04Z

[feat: add `StringByteInput`](https://github.com/EndstoneMC/endstone/commit/9b5a77bb8e86d38cb7517e2c65fc9880356d3688)

**Change and causal context.** Stages BytesDataInput and StringByteInput/BigEndianStringByteInput layouts and virtual result-returning interfaces. StringByteInput holds an index and borrowed string_view; the .cpp contains only an include. IDataOutput moves before IDataInput and size parameters become size_t where shown. CMake adds the translation unit.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** This commit declares most input behavior without definitions; do not call it a complete safe byte-reader implementation. The borrowed buffer lifetime remains external.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1309"></a>
## Commit 1309 {#commit-1309}

73b97731312275fd488176f4c12ad55b6384fb14 · 2025-11-18T00:08:34Z

[feat: add `readNamedCompoundTag` and `readOrGetEmpty` methods to `NbtIo`](https://github.com/EndstoneMC/endstone/commit/73b97731312275fd488176f4c12ad55b6384fb14)

**Change and causal context.** Adds NbtIo::readNamedCompoundTag: validate the leading type, read the root name, allocate/load CompoundTag. readOrGetEmpty logs a failed root result and supplies an empty compound fallback.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** The result of tag->load is discarded. Existing readNamedTag also discards nested load results, so structurally successful root parsing is not equivalent to complete payload validation. Empty fallback is an intentional recovery behavior with possible information loss.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1310"></a>
## Commit 1310 {#commit-1310}

81d3ee0391bdae8e80b719db999b110c14e9ac7b · 2025-11-18T00:33:05Z

[fix: resolve a vulnerability in item deserialisation that can cause the server to hang](https://github.com/EndstoneMC/endstone/commit/81d3ee0391bdae8e80b719db999b110c14e9ac7b)

**Change and causal context.** Replaces native Item::readUserData with a detour: read short marker, allow -1 only with version 1, parse NBT through readOrGetEmpty and set it, allow marker 0 without NBT, reject other markers, then deserialize components. Adds declaration/friend access, symbols and runtime source.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** underlying_stream is unused; errors return from a void API without a propagated rejection status. The new deserializeComponents body arrives in 1311. Title reports a server-hang vulnerability; no independent reproduction or security-completeness claim.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1311"></a>
## Commit 1311 {#commit-1311}

f6751f87e4411563c51d2bc8c165ca4fdbe6d376 · 2025-11-18T00:56:32Z

[feat: implement `ItemStackBase::_loadBlocksForCanPlaceOnCanDestroy`](https://github.com/EndstoneMC/endstone/commit/f6751f87e4411563c51d2bc8c165ca4fdbe6d376)

**Change and causal context.** Implements component decoding as two count/string loops for can_place_on and can_destroy followed by compare-hash refresh. Each read failure exits early. Initial block-name resolver prepends minecraft:, resolves complex aliases, and appends borrowed native block-type pointers.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Signed counts are not explicitly bounded or rejected when negative; partial reads can leave appended state and skip hash refresh. Resolver failure is ignored by callers and existing lists are not cleared here. This stage is replaced by native delegation in 1312.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1312"></a>
## Commit 1312 {#commit-1312}

dc6d78e0f2d48ffcb88fda15e53ddfd50a2fae85 · 2025-11-18T01:14:00Z

[feat: update symbols.toml](https://github.com/EndstoneMC/endstone/commit/dc6d78e0f2d48ffcb88fda15e53ddfd50a2fae85)

**Change and causal context.** Adds the can-place/can-destroy loader symbol on both platforms and replaces its new local resolver with BEDROCK_CALL, retaining the previous body only as comments.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** The title mentions only symbols, but active implementation changes. Native dependency and correct address identity now govern behavior; December 1357 later repairs the Windows address, illustrating this tradeoff.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1313"></a>
## Commit 1313 {#commit-1313}

b5fb6c8c55533a845417eb5c8fe85e70154a3dd4 · 2025-11-18T01:49:59Z

[fix: correct the implementation of `CompoundTag::load` and `ListTag::load`](https://github.com/EndstoneMC/endstone/commit/b5fb6c8c55533a845417eb5c8fe85e70154a3dd4)

**Change and causal context.** CompoundTag::load now stops on End instead of inserting it and continuing. ListTag::load rejects out-of-range type, zero length or End-typed lists before reserve.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Negative lengths are not rejected and convert to an allocation size at reserve; positive counts and depth remain unbounded here. Child load results remain ignored. Rejecting zero length changes empty-list compatibility; these guards are not an exhaustive deserialization proof.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1319"></a>
## Commit 1319 {#commit-1319}

f454f49adbad2448e66c3cafe497dd191fc38a74 · 2025-11-18T19:47:05Z

[fix: prevent packet spam from disconnected clients](https://github.com/EndstoneMC/endstone/commit/f454f49adbad2448e66c3cafe497dd191fc38a74)

**Change and causal context.** First disconnect hardening stage sets NetworkConnection::disconnected_ after native disconnect notification and checks it before each receive loop iteration, returning NoData without reading more. The code explains that a malicious client can ignore the notification.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** This first approach stops local processing but is not full transport/resource cleanup. Later 1326–1331 revise it repeatedly; do not summarize the final behavior from this initial patch.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1320"></a>
## Commit 1320 {#commit-1320}

15ed7ff932eb79239933e368e40cfc0a9d5d3e21 · 2025-11-18T19:47:21Z

[feat: enable packet rate limiting by default](https://github.com/EndstoneMC/endstone/commit/15ed7ff932eb79239933e368e40cfc0a9d5d3e21)

**Change and causal context.** At level setup, dispatches reloadpacketlimitconfig through the server sender after registries and death-message suppression. The returned command result is discarded; unrelated visitor formatting is mechanical.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** This enables the native configured limiter by command, not a locally implemented rate algorithm. Thresholds, command success and performance are unverified.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1322"></a>
## Commit 1322 {#commit-1322}

85ff264f0c5b7cb883dca3f24e2772b2e73fb28c · 2025-11-18T22:59:50Z

[feat: enable RakNet connection frequency limiting](https://github.com/EndstoneMC/endstone/commit/85ff264f0c5b7cb883dca3f24e2772b2e73fb28c)

**Change and causal context.** After native peer startup, calls SetLimitIPConnectionFrequency(true) for nonnull gameplay peers; changelog advertises it. Code comment describes a 100 ms same-IP limit.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** The stated interval is a source comment/native contract, not independently verified. It applies by peer purpose and can affect clients sharing an IP; no tuning or measurements shown.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1323"></a>
## Commit 1323 {#commit-1323}

96ee3a8d37421e697db0f30b31362c6e23822a12 · 2025-11-18T23:09:26Z

[refactor: clean up codes](https://github.com/EndstoneMC/endstone/commit/96ee3a8d37421e697db0f30b31362c6e23822a12)

**Change and causal context.** Moves SetLimitIPConnectionFrequency before the original startup call and returns the original result directly.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Despite cleanup title, initialization order changes. It no longer waits for a startup result before setting the peer option; effect is not executed.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1326"></a>
## Commit 1326 {#commit-1326}

06ce8871e4ce49b09079845f097f839e23a094e5 · 2025-11-21T18:41:42Z

[fix: ensure the connection is probably closed](https://github.com/EndstoneMC/endstone/commit/06ce8871e4ce49b09079845f097f839e23a094e5)

**Change and causal context.** Adds Packet::setSenderSubId and DisconnectPacket layout, then synthesizes a Disconnect packet through the local handler before setting the stored connection disconnected. Intended to force cleanup rather than trusting client acknowledgement.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** The connection pointer is acquired before packet handling and used afterward; cleanup could invalidate it. The native dispatcher behavior is not reproduced. This implementation is superseded by 1328–1331.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1328"></a>
## Commit 1328 {#commit-1328}

04382f6c1f157046339225ab6de16204e13d6763 · 2025-11-21T19:09:34Z

[refactor: improve connection logics](https://github.com/EndstoneMC/endstone/commit/04382f6c1f157046339225ab6de16204e13d6763)

**Change and causal context.** Removes the disconnected receive-loop guard and inline flag setter, adds channel pause bitset accessors and network-close declarations, and always synthesizes the Disconnect packet without retaining/using a connection pointer afterward.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** The title is broad, but the receive behavior and cleanup dependency materially change. There is no longer the earlier local NoData guard; rely on the ensuing cleanup path, not both mechanisms at once.

Offline full message: message. Full deltas: parent 1.
Author: endstone; committer: endstone.

<a id="commit-1329"></a>
## Commit 1329 {#commit-1329}

a87b940e1d79d1cc5d677f0fe529d51e0a218e05 · 2025-11-21T19:51:19Z

[fix: enforce proper connection closure](https://github.com/EndstoneMC/endstone/commit/a87b940e1d79d1cc5d677f0fe529d51e0a218e05)

**Change and causal context.** Replaces synthetic Disconnect dispatch with explicit NetworkSystem::closeConnection for primary clients only. closeConnection invokes onConnectionClosed and then the remote connector close method.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Initial call omits a native session-summary parameter, repaired in 1331. Primary-only closing avoids tearing down a shared transport for a subclient, but no subclient cleanup proof is added.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1330"></a>
## Commit 1330 {#commit-1330}

0d0c48ebbed993642ae800cb12db5c182e9a2c2d · 2025-11-21T20:18:14Z

[chore: bump version to v0.10.15](https://github.com/EndstoneMC/endstone/commit/0d0c48ebbed993642ae800cb12db5c182e9a2c2d)

**Change and causal context.** Comments out the explicit closeConnection call, leaving the primary-client branch empty. No version constant changes despite the version-bump title.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** This is a temporary behavioral rollback of the added transport close. Preserve it as a reversal, not release-only metadata.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1331"></a>
## Commit 1331 {#commit-1331}

6e4b448c5533405c1e60d4751862472c76a2f335 · 2025-11-22T00:41:40Z

[fix: resolve a crash in `NetworkSystem::closeConnection`](https://github.com/EndstoneMC/endstone/commit/6e4b448c5533405c1e60d4751862472c76a2f335)

**Change and causal context.** Extends ConnectionCallbacks::onConnectionClosed with const Json::Value& session_summary and supplies {} from closeConnection. Re-enables primary-client close after native disconnect, through the server network accessor, and removes extra no-player logging.

**Rationale and attribution.** Title explicitly attributes the crash to closeConnection; the patch makes the missing parameter visible and restores the previously disabled mitigation.

**Limits and counterexamples.** The source repairs an ABI call signature rather than only adding a null guard. Native cleanup/close may invalidate referenced connection-related data; no runtime safety or rate-limit effectiveness is established.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1359"></a>
## Commit 1359 {#commit-1359}

38bfc6c53df32792d1ec798ab61ae8254272c762 · 2025-12-14T17:36:50Z

[feat: add `UnverifiedCertificate::fromString` hook with JSON validation logic](https://github.com/EndstoneMC/endstone/commit/38bfc6c53df32792d1ec798ab61ae8254272c762)

**Change and causal context.** Restores the certificate fromString detour removed by 1353, with CMake/header/symbol wiring. Keeps 0x300000 byte cap and object/array validation, but allows up to ten chain entries instead of three; catches exceptions and returns empty certificate otherwise.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** No element-type/minimum-chain or recursive JSON budget validation appears. Commit message says native attempted fix failed; retain that as author diagnosis without inventing exploit evidence.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1360"></a>
## Commit 1360 {#commit-1360}

92569ca1b2eda7acc2972022fc6ab260c0233fad · 2025-12-14T17:58:26Z

[fix: add `Certificate::validate` hook to fix a null pointer-related crash (blame mojang)](https://github.com/EndstoneMC/endstone/commit/92569ca1b2eda7acc2972022fc6ab260c0233fad)

**Change and causal context.** Adds Certificate::validate detour/symbols which checks std::launder(this) for null and returns false, otherwise forwards time/self-signed/expiry parameters unchanged.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Calling a member with null this is outside normal C++ object preconditions and launder is not a general validator. Optimizer/platform assumptions matter; this patch alone is not a portable safety proof.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1361"></a>
## Commit 1361 {#commit-1361}

b209f49ab18ba0e97d64e98bce40d5b877a28260 · 2025-12-14T18:20:12Z

[fix: ensure the fix works on Linux](https://github.com/EndstoneMC/endstone/commit/b209f49ab18ba0e97d64e98bce40d5b877a28260)

**Change and causal context.** Adds -fno-delete-null-pointer-checks to the entire UNIX runtime target and simplifies the validate null check; temporarily adds an unused validate_ptr helper.

**Rationale and attribution.** Title claims ensuring the fix works on Linux; source shows compiler-assumption mitigation, with no local measured verification.

**Limits and counterexamples.** Compiler option is a targeted low-level workaround with target-wide code-generation scope. It does not make arbitrary invalid pointers valid or prove Windows/Linux parity. No compiler run or native test conducted.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1363"></a>
## Commit 1363 {#commit-1363}

2b1d39150120d90b9fccf3a331e4402122feca57 · 2025-12-14T18:27:22Z

[refactor: remove unused `validate_ptr` helper function in `certificate.cpp`](https://github.com/EndstoneMC/endstone/commit/2b1d39150120d90b9fccf3a331e4402122feca57)

**Change and causal context.** Removes the unused validate_ptr helper from 1361, retaining the actual std::launder(this) guard and compile flag. This is maximal assigned stable tip.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Mechanical cleanup does not change the null-this assumptions or establish successful runtime mitigation.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.
