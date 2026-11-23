<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:557"],"source_type":"public","date":"2026-10-18","topics":["testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-557-getserverplayer-scans-all-players-on-every-packet-when-packetsendevent-is-registered"></a>
# EndstoneMC/endstone #557: getServerPlayer() scans ALL players on every packet when PacketSendEvent is registered {#endstonemc-endstone-557-getserverplayer-scans-all-players-on-every-packet-when-packetsendevent-is-registered}

Source: https://github.com/EndstoneMC/endstone/issues/557

## Evidence and attribution {#evidence-and-attribution}

Primary author: jv2w. Created 2026-10-18T13:43:12Z; recorded state closed; merged not applicable.

PacketSendEvent/ReceiveEvent player lookup scans all users; reporter estimates movement fanout can multiply into cubic work and measures6µs at2players versus24µs at20,~4000calls/s. Turning off packet re-send restores40-playerMSPT100–200→~20 but does not isolate native send cost. Wu's40-player reproduction reports~1µs/~10MSPT and still lands O(1) lookup c2c778adf. Reporter accepts environment may dominate and requests the exact benchmark plugin; no reply captured. Keep structural complexity improvement separate from explaining the production slowdown, and connect superseded #548.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/557
- https://github.com/EndstoneMC/endstone/issues/557#issuecomment-6251334238
- https://github.com/EndstoneMC/endstone/issues/557#issuecomment-6264155133
