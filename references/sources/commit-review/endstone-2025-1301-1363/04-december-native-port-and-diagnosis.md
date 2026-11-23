<!-- retrieval: {"source_ids":["public:commit:57b966951a4a124042b59905607fdd72d9d64a4b","public:commit:d24e5f10ce3ab6a0315e7d313350d03799009a2f","public:commit:e248c66f39d4fe184ef7f1eb539b9977e89ae39c","public:commit:f0cbdedc05d40ff10742ac3f1191c7098d50bd48"],"source_type":"public","date":"2025-12-11","topics":["lifetime","concurrency","ffi","testing","build","api","diagnosis","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# December native port and diagnosis {#december-native-port-and-diagnosis}

## Port scope and explicit evidence {#port-scope-and-explicit-evidence}

1353 is a GitHub-committed Vincent-authored aggregate for BDS 1.21.130.4, protocol 898, patch 0.10.16. Its long message retains the component progression, including signature/layout changes, two-platform symbol fixes, reload repair and the author's “works” claim for surprising text serialization. The full meaningful 77-file patch was read. Numeric symbol changes are all-key structurally checked; no native binary is executed or disassembled here. No co-author or generative-AI trailer is present; absence is not proof of no assistance.

## Eight connected areas {#eight-connected-areas}

1. **Authentication ownership and rejection timing.** ConnectionRequest/SubClientConnectionRequest lose internal verified flags/auth-info storage. Raw token access now dereferences directly. ServerNetworkHandler receives PlayerAuthenticationInfo explicitly for primary/subclient loading, while its client structure owns corresponding auth records. Ban checks move from a packet-factory wrapper to _validateLoginPacket. IP rejection precedes native validation; native nullopt rejection is preserved before identity bans; success returns auth info. Missing connection_request returns nullopt. The added hook is primary-login scoped; subclient loading forwards info but adds no equivalent ban check here.

2. **Packet representations.** AvailableCommandsPacket and DeathInfoPacket receive payload/serialization fields; resource-pack stack removes addon entries. TextPacket becomes a variant of message-only, author/message and message/parameters. Its writer emits localize, variant index, a set of literal type-name strings for the variant, type byte/body, xuid/platform ID and a presence flag for filtered text. The writer's TODO explicitly questions this representation. Local _read remains unimplemented; many payload helper declarations have no bodies in this patch. No wire compatibility proof is inferred from a source comment.

3. **Native interface/layout drift.** New outgoing packet callback, actor swing source, added/removed Mob/Item/Block/Level virtual slots, container-registry interfaces, shutdown callbacks and removed layout fields all affect ABI. Block size asserts change from 320/328 to 304/312. Comments marking old offsets are not updated evidence of current offsets. BaseAttributeMap's old size assert is removed, reducing one static constraint while its container changes.

4. **Attribute containers.** Native map changes from unordered_map to brstd::flat_map. The adapter maintains parallel key/value iterators and uses lower_bound on sorted keys, returning pair-of-reference proxies. Structured bindings with auto copy the proxy, not the AttributeInstance, so the returned instance address remains the underlying vector entry. Both vector alignment and sortedness remain native invariants; general STL iterator completeness is not proven. Name lookup becomes a pointer result but still throws when absent. Native callers dereference this pointer; no null fallback is introduced.

5. **Teleport semantics.** General actors reject removed state, set rotation first, then use entityChangeDimension or teleportTo. Players additionally reject zero health and construct a ChangeDimensionRequest with source/destination locations and use_portal=false. This replaces command-target computation/apply helpers and removes their symbols. Rotation can change before later cancellation/failure, and old command semantics are not automatically preserved. Native change paths and event ordering require their own validation.

6. **Skin, items and resources.** SerializedSkin becomes SerializedSkinRef with the same shared ThreadOwner-backed representation and updated packet/player/conversion signatures. ItemStackBase::setUserData is reimplemented locally and rebuilds or clears charged_item through ItemInstance::fromTag. Resource-pack repository presence gains a diagnostic check; addon-stack access is disabled along with the removed member. Registry reload routes through ServerInstance::onRequestResourceReload before function/registry rebuilding.

7. **Lifecycle and callbacks.** Minecraft shutdown now calls a stored move_only_function instead of an app virtual with a string. brstd function call support dereferences the native invoke table; no empty-function guard is added. DevTools starts a detached render thread during DedicatedServer startup under its build flag. Stable still uses its own interpreter/stdin lifetime flow, distinct from main's in-tree metrics/console integration.

8. **Follow-on diagnosis.** 1355 supplies the newly added Dehydration damage mapping, while unknown future values still throw descriptively. 1356 suppresses all low-priority System logs in addition to Database. 1357 repairs a Windows native loader address after issue312's item-deserialization stack. The reporter thanks the maintainer but supplies no successful retest in the captured conversation. 1359–1363 restore certificate defenses after the port removed them; that chain is detailed in dossier02.

## Tests and limits {#tests-and-limits}

No dedicated port regression tests are added in the patch. Existing native size assertions and source-level checks are evidence of intended constraints, not a demonstrated BDS runtime pass. The absence of expensive integration tests can be a scope/cost tradeoff; it cannot support a claim of measured correctness or reliability. Dependency internals, native allocators, thread shutdown and client wire behavior remain outside executed validation.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1353"></a>
## Commit 1353 {#commit-1353}

d24e5f10ce3ab6a0315e7d313350d03799009a2f · 2025-12-11T00:00:30Z

[[feature] add 1.21.130 support](https://github.com/EndstoneMC/endstone/commit/d24e5f10ce3ab6a0315e7d313350d03799009a2f)

**Change and causal context.** Large stable 1.21.130 port (protocol 898, Endstone 0.10.16) changes native vtables/layouts, auth-info ownership and packet payload representations. Full 77-file residual/message read, with symbol addresses structurally checked. Text serialization writes variant index, variant-specific literal type-name strings, type byte/body, identity and optional filtered-text flag. Attribute map becomes parallel-vector flat_map with paired-reference iterators/find. Native skin becomes SerializedSkinRef. Teleport bypasses TeleportCommand: rotates first, uses entity/player dimension-change paths or native teleport; dead/removed players return.

**Rationale and attribution.** Vincent authors a GitHub-committed squash-like aggregate with a long retained component history. No explicit co-author or AI trailer is present; do not invent attribution from style.

**Limits and counterexamples.** Detailed ABI, auth, lifecycle and serialization analysis is in dossier04. Commit message says serialization works but looks wrong; that is an author report. No binary, client or compiler validation. Certificate guard is removed here, then restored in 1359. This port lands on stable, not main1352.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: GitHub.

<a id="commit-1355"></a>
## Commit 1355 {#commit-1355}

57b966951a4a124042b59905607fdd72d9d64a4b · 2025-12-11T17:51:05Z

[fix: resolve a crash caused by missing damage cause](https://github.com/EndstoneMC/endstone/commit/57b966951a4a124042b59905607fdd72d9d64a4b)

**Change and causal context.** Adds Dehydration to damage-source mapping after the native enum extension in 1353. Unknown values now throw a descriptive runtime_error before map::at.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Known new cause is handled, but unknown future causes still fail rather than falling back. A more descriptive exception is diagnostic improvement, not universal crash prevention.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1356"></a>
## Commit 1356 {#commit-1356}

f0cbdedc05d40ff10742ac3f1191c7098d50bd48 · 2025-12-11T19:08:06Z

[refactor: suppress additional low-priority logs for `System` log area](https://github.com/EndstoneMC/endstone/commit/f0cbdedc05d40ff10742ac3f1191c7098d50bd48)

**Change and causal context.** Extends low-priority log suppression from Database to Database or System at priority <= Info. Comment identifies unknown ContentLog area mapped to System.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Filter suppresses the whole category/priority range, not only a specific noisy message. Tradeoff is lower console noise versus diagnostic loss; no performance claim.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1357"></a>
## Commit 1357 {#commit-1357}

e248c66f39d4fe184ef7f1eb539b9977e89ae39c · 2025-12-11T19:19:38Z

[fix: correct the symbols for `ItemStackBase::_loadBlocksForCanPlaceOnCanDestroy`](https://github.com/EndstoneMC/endstone/commit/e248c66f39d4fe184ef7f1eb539b9977e89ae39c)

**Change and causal context.** Changes only the Windows address of ItemStackBase::_loadBlocksForCanPlaceOnCanDestroy (1673952 to 63679168), preserving Linux values and all keys. Commit closes issue312.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** pgrd1 reports Windows 0.10.16 access violation with deserializeComponents in stack and uncertain reproduction; Vincent confirms a bug/working on fix, reporter thanks but does not retest. Address repair is exact source evidence, not independently verified success.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.
