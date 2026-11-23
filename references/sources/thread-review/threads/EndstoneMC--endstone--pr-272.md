<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:219","public:thread:EndstoneMC/endstone:272"],"source_type":"public","date":"2025-07-19..2025-09-30","topics":["lifetime","concurrency","ffi","testing","api","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-272-feat-1-21-110-support-wip"></a>
# EndstoneMC/endstone #272: feat: 1.21.110 support (WIP) {#endstonemc-endstone-272-feat-1-21-110-support-wip}

Source: https://github.com/EndstoneMC/endstone/pull/272

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (566 additions, 307 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu authored and merged this WIP-labelled port. The primary body is empty and there are no human comments or reviews. The sole bot report has missing-base and zero-line limitations, retained below rather than upgraded into test success.

<a id="complete-patch-inspection"></a>
### Complete patch inspection {#complete-patch-inspection}

The full 62-file diff actually targets package/symbol version 1.21.111 and network protocol 844, despite the WIP title saying 1.21.110. It updates both platform address tables and native vtables/layouts: actor swing returns bool, Mob adds carried-item attack damage, Player rearranges movement virtuals and ocean-biome storage, BlockSource moves removeBlock and removes a coordinate overload, and Level adds a shape registry slot. Block and BlockActor size assertions shrink; flammability values become uint16_t enums plus a bool-valued lava flag. These are ABI declarations and address mappings, not independently validated binary compatibility.

A significant lifecycle change removes the _resetServerScriptManager detour that disabled all plugins and reset the EndstoneServer locator. Instead init registers a static ServerInstanceStopListener, whose onServerThreadStopped disables plugins, resets the locator and returns KeepGoing. This narrows teardown to server-thread stop rather than every script-manager reset, directly relevant to the earlier /reload problem in issue #219: a script reload should not invalidate live Endstone plugin callbacks. The connection is an inference from the two inspected implementations; the empty PR body provides no explicit author rationale. EventCoordinator registration rejects duplicate live/pending listeners and defers new registration while events are queued, avoiding immediate vector mutation during dispatch. There is no new unregister implementation or independently tested callback-order proof.

Resource-pack ownership is rewritten toward shared_ptr: Pack/ResourcePack lose NonOwnerReferences inheritance, PackInstance owns a not-null shared ResourcePack, repository queries return shared references, and repository source/factory/storage structs change. Stack deserialization gains optional level_id and the caller supplies the level's ID. However the integration is deliberately incomplete in this final patch: ResourcePackRepository::_initializePackSource is commented out, its hook symbol is removed, setLevel's loadResourcePacks call is commented out, and the repository size assertion is replaced with a TODO. Therefore merged status cannot be summarized as complete custom resource-pack support for 1.21.111. Existing loading helper code is not active simply because it still compiles in the tree.

Packet adds a toString virtual and renames client_sub_id/getClientSubId to sender_sub_id/getSenderSubId. Login's request moves into payload, and ban-dispatch hooks migrate their access accordingly. The outgoing header keeps the same bit-shift arrangement while using the renamed getter; the patch alone does not validate split-screen sender/recipient semantics. disconnectClient becomes disconnectClientWithMessage throughout kick/internal-disconnect hooks and symbols. Authentication declarations remove unverified PlayFab storage, add nonce/well-formedness interfaces and service-key manager fields; this is layout/interface evidence, not proof of a new authentication protocol implementation in Endstone.

Codecov's sole comment says modified coverable lines are covered but simultaneously reports a missing base report and zero files/lines. It provides no meaningful coverage validation for these ABI and lifecycle changes. No human review, primary explanation or test transcript is present. Reusable lesson: treat version-port merge state, enabled integration paths and test evidence as separate facts; lifecycle callbacks can be a safer boundary than hooking a helper reused by reload, but shutdown timing still needs integration tests.

Exact inspected base/head: e74860b87fad5c2a0edacf0a3ff3f8ffe992a316…0a2a152ce6b3c46e3b8bdf9363fc42e61a4378c9. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/272
- https://github.com/EndstoneMC/endstone/pull/272#issuecomment-3362159445
