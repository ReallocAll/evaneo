<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:199"],"source_type":"public","date":"2025-06-15","topics":["ffi","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-199-feature-1-21-90-support-wip"></a>
# EndstoneMC/endstone #199: [feature] 1.21.90 support (WIP) {#endstonemc-endstone-199-feature-1-21-90-support-wip}

Source: https://github.com/EndstoneMC/endstone/pull/199

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (1043 additions, 416 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu's merged 1.21.90 port retains WIP in its title, has no primary description and only one Codecov comment. All discussion is read; no human readiness rationale or testing result is supplied. The complete patch is inspected below, with unresolved implementation details kept explicit.

### Complete patch inspection {#complete-patch-inspection}

This 67-file port pins 1.21.90-preview.28 and reenables the preview EntityRegistry field. It updates both symbol tables and several signatures, including BlockTypeRegistry callbacks from owning std::function to non-owning function_ref. Authentication changes from certificate-backed GameServerToken access to explicit authentication type and trusted player information. UserEntityIdentifier::getXuid now returns stored trusted information regardless of its legacy trust_self_signed parameter. ConnectionRequest and SubClientConnectionRequest expose typed metadata/skin getters, gated by a valid legacy multiplayer token; declarations alone do not verify the newer authentication paths.

Skin decoding moves to a new Bedrock utility. Its implementation reserves capacity in an empty string, writes through data() without first resizing, ignores the base64 decoder's success result, then resizes afterward. That violates the intended writable string range and can overwrite decoded bytes when resize initializes them. It is a concrete historical static concern, distinct from the separate existing core decoder, whose output is correctly resized to decoded length in this patch. Cape construction also still passes skin width/height despite reading cape dimensions. Image::fromArray itself simply delegates a byte view to the existing checked buffer factory.

PackSource becomes a result/options-based interface with shared pack ownership, report storage and a protected load implementation. Endstone's source returns packs and report and retains copies for enumeration, with a discovered flag preventing repeated discovery. Native pack repositories gain asynchronous refresh and more virtual methods; a ServerNetworkHandler content-key offset remains explicitly TODO. A ResourcePacksInfo patch function is only a placeholder, not implemented content-key injection.

Movement/jump cancellation and changed destinations now teleport back/forward using height-adjusted public locations. Comments acknowledge this also emits PlayerTeleportEvent, so event chaining and cancellation interactions matter. Score modifications replace a boolean with an enum and notify only on Success, but EndstoneScore::setValue tests result!=Success inside ENDSTONE_CHECK; inspecting that macro confirms it returns an error on false, so success is inverted at this revision. IntegerOverflow/UnknownOperator enum values exist without corresponding checks in the changed arithmetic. Native biome, storage, actor/network, pack and event layouts are adjusted; no tests validate these ABI changes. WIP title, merge and a bot report cannot resolve the remaining code TODOs.

Exact inspected base/head: b5735db0c82f761d04fd5e44609d3f773620fe92…85a4cb75c664dae8875b18ee0496845a80dc5ae1. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/199
- https://github.com/EndstoneMC/endstone/pull/199#issuecomment-2978257034
