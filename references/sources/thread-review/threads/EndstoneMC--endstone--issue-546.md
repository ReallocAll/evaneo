<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:546"],"source_type":"public","date":"2026-10-08","topics":["ffi","testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-546-playerlist-is-decoded-once-per-recipient-to-fill-the-show-player-cache"></a>
# EndstoneMC/endstone #546: PlayerList is decoded once per recipient to fill the show-player cache {#endstonemc-endstone-546-playerlist-is-decoded-once-per-recipient-to-fill-the-show-player-cache}

Source: https://github.com/EndstoneMC/endstone/issues/546

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-10-08T14:34:29Z; recorded state open; merged not applicable.

Open develop-only regression from #501: PlayerList bypasses hidden-actor gates, fully decodes skins per recipient and keeps per-recipient AddEntry copies solely for later showActor. Join storms therefore incur N decodes and roughlyN² skin entries even with no hidden users. Wu estimates236ms/s decode and323 vs83ms/s network cost at100players/20joins/s by multiplying measured per-packet cost, explicitly not end-to-end measurement; steady play unaffected. Proposed gate by global/recipient hidden state, remove cache and use native ILevel::getPlayerList keyed by shown player's client UUID, or construct from live Player. Needs faithful PlayerListEntry layout/mapping. A current native entry also avoids stale re-show data. Proposal remains open, not implemented evidence.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/546
