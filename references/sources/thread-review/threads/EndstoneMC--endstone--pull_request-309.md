<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:309"],"source_type":"public","date":"2025-12-09","topics":["lifetime","ffi","testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-309-feature-1-21-130-support-wip"></a>
# EndstoneMC/endstone #309: [feature] 1.21.130 support (WIP) {#endstonemc-endstone-309-feature-1-21-130-support-wip}

Source: https://github.com/EndstoneMC/endstone/pull/309

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2025-12-09T18:32:36Z; recorded state closed; merged True.

## Discussion finding {#discussion-finding}

Version-support PR authored by wu-vincent, merged after 60 reported commits, 77 changed files, 849 additions and 617 deletions. Primary body and all three discussion components are empty. There is no discussion-level rationale or test report. The complete 139,364-character captured patch was subsequently inspected; findings follow.

## Complete port patch {#complete-port-patch}

Every139364characters of the captured patch was inspected, including both platform symbol tables. Protocol860→898 and version1.21.130 coincide with ownership, authentication, wire layout and teleport changes. ConnectionRequest/SubClientConnectionRequest no longer own verified auth information or an is_verified flag; getData unconditionally dereferences raw_token_. Auth information instead travels separately through native validate/load/create-player calls. Ban filtering moves from a packet-dispatch wrapper to _validateLoginPacket: reject IP bans first, guard missing request, call native validation, only inspect names/UUID/XUID after optional authentication succeeds, reject identity bans, then return auth_info. This narrows the interception point to authentication itself. The earlier certificate hook's3MB JSON/object/chain<=3 validation is deleted; the patch supplies no evidence proving the native new validator provides an equivalent resource bound.

TextPacket is redesigned around a payload variant (message-only, author/message, message/parameters), localize, XUID/platform and optional filtered message. Its writer emits string labels for all possible message types before the selected byte; an explicit TODO questions that encoding. Filtered text becomes a presence boolean plus optional string. _read still throws Not implemented. Later#327 removes those label lists and changes the filtered-text representation again, so this revision cannot be treated as a durable protocol model. Other packet changes include AvailableCommands payload separation/serialization mode, DeathInfo flattening, removal of resource-pack addon IDs and SerializedSkinRef renaming through packet/player/API conversion.

Flat-map support is substantive: split key/value storage with random-access-like proxy iterators, lower_bound lookup and key-equivalence checks, plus a no-value mapped-container adapter for flat_set. Dereference returns a pair of references; binding auto [id, instance] preserves references. BaseAttributeMap changes from unordered_map to this representation and removes its old size assertion. Lookup becomes pointer-returning, while call sites dereference it and rely on names being present; absent names still throw. The change is necessary ABI modeling, not evidence that flat maps universally outperform hash maps. Move-only callable invocation gains the virtual dispatch through its internal function table, enabling Minecraft's new request-shutdown callback.

Teleport no longer calls native TeleportCommand compute/apply helpers. Actors reject removed state, set rotation, then use entityChangeDimension across dimensions or teleportTo with fixed flags in-dimension. Players separately reject dead/removed state and submit ChangeDimensionRequest with portal/respawn false. This changes lifecycle paths and requires collision, velocity, rotation, cross-dimension and dead-player integration tests; none are added. Server shutdown switches from IMinecraftApp message callback to a move-only void callback, resource reload dispatch moves to ServerInstance, and resource-pack initialization gains a descriptive missing-repository error. DevTools now starts as a detached render thread when enabled, without a join/stop handshake added here.

ItemStackBase::setUserData becomes local assignment plus charged-item reconstruction from the charged compound via newly mapped ItemInstance::fromTag; missing charged data resets the cached item. New actor/enchantment/swing flags and gameplay event variant order, added/removed Item/Mob/Block/ILevel virtual methods, resource-pack revision bytes, removed addon stack and adjusted block sizes must all match the exact native build. Both platform tables refresh addresses and remove obsolete Teleport/Certificate/setUserData entries while adding changed authentication/fromTag signatures. The patch adds no automated regressions for auth limits, serializer wire bytes, flat-map reference behavior, charged-item invalidation, teleport or shutdown lifecycle. Full source inspection validates the changes and their limits, not their runtime correctness.


## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (139364 characters; SHA-256 7211dd61b6ae130be8d99e8db81978d879c3bb96a8833c4f81721811b68b01d2), head 80c01a1821dd31f37451194a11501a57c0b0e04d. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/309
