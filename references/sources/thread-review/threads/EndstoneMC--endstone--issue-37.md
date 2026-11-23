<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:37"],"source_type":"public","date":"2024-08-21","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-37-feature-call-playerjoinevent-after-receiving-setlocalplayerinitializedpacket"></a>
# EndstoneMC/endstone #37: [feature] Call PlayerJoinEvent after receiving SetLocalPlayerInitializedPacket {#endstonemc-endstone-37-feature-call-playerjoinevent-after-receiving-setlocalplayerinitializedpacket}

Source: https://github.com/EndstoneMC/endstone/issues/37

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu identifies a lifecycle/readiness mismatch: PlayerJoinEvent fires before the client can handle form packets, making forms sent in the event invisible. Proposed and reported completed remedy is to fire after SetLocalPlayerInitializedPacket, linked to b2979a8610b4371f6910c5761e2e28d6bb08adcd. The observation motivates using client readiness rather than server-side presence as the event boundary. The linked code has not been read here, and later timing/safety issues may qualify this choice.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/37
- https://github.com/EndstoneMC/endstone/issues/37#issuecomment-2309020696
- https://github.com/EndstoneMC/endstone/commit/b2979a8610b4371f6910c5761e2e28d6bb08adcd
