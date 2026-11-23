<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:186"],"source_type":"public","date":"2025-05-22","topics":["concurrency","ffi","testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-186-feature-improve-player-object-creation-logic"></a>
# EndstoneMC/endstone #186: [feature] Improve Player Object Creation Logic {#endstonemc-endstone-186-feature-improve-player-object-creation-logic}

Source: https://github.com/EndstoneMC/endstone/issues/186

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu proposes separating connection identity from spawned native actor identity. Create EndstonePlayer immediately after RakNet connection with SocketAddress/ClientID, keep it in the server player map while entity_id is invalid, attach the real native Player after login, and remove on disconnect. The motivation is early PacketSend/Receive events needed by multi-version plugins. Proposed tests explicitly require invalid isValid during Login/RequestNetworkSettings, valid after login for LevelEvent/PlayerAuthInput, and disconnect-packet events. These are test requirements, not test results. A closed issue with no patch/discussion does not prove rollout. The design requires consumers to distinguish connection-level operations from native actor methods even though both share a Player wrapper.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/186
