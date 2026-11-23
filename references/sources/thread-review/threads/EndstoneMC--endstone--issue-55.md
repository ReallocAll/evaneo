<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:55"],"source_type":"public","date":"2024-09-15","topics":["concurrency","api","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-55-feature-add-player-sendrawpacket-to-allow-sending-payloads-directly-to-a-player"></a>
# EndstoneMC/endstone #55: [feature] Add `Player::sendRawPacket` to allow sending payloads directly to a player {#endstonemc-endstone-55-feature-add-player-sendrawpacket-to-allow-sending-payloads-directly-to-a-player}

Source: https://github.com/EndstoneMC/endstone/issues/55

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu proposes raw binary packet sending as an interim escape hatch for anti-cheat and other plugins, avoiding the cost of complete wrapper coverage while making plugin authors responsible for encoding. Future comprehensive wrappers are a possibility, not a commitment. The eventual completion comment changes the named API to Player::sendPacket(packet id int, payload bytes), linked to dccf908752fe503098552b5d201dd108ae741f43. Preserve that proposal-to-interface revision and the validation responsibility; stale-bot closure before completion is not the final technical state.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/55
- https://github.com/EndstoneMC/endstone/issues/55#issuecomment-2415150680
- https://github.com/EndstoneMC/endstone/issues/55#issuecomment-2546765993
- https://github.com/EndstoneMC/endstone/issues/55#issuecomment-2567145637
- https://github.com/EndstoneMC/endstone/issues/55#issuecomment-2719455317
- https://github.com/EndstoneMC/endstone/commit/dccf908752fe503098552b5d201dd108ae741f43
