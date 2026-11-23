<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:548"],"source_type":"public","date":"2026-10-10","topics":["ffi","testing","performance","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-548-perf-network-look-up-the-peer-and-player-in-o-1-on-the-packet-event-path"></a>
# EndstoneMC/endstone #548: perf(network): look up the peer and player in O(1) on the packet event path {#endstonemc-endstone-548-perf-network-look-up-the-peer-and-player-in-o-1-on-the-packet-event-path}

Source: https://github.com/EndstoneMC/endstone/pull/548

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-10-10T13:44:35Z; recorded state closed; merged False.

Two scans per eventful packet motivate connection/weak-player caching. Match native batched_peer identity, not just network ID, because twin connections can share IDs. Keep entries until peer expiry so reentrant plugin sends cannot invalidate an outer hook's ID. Per-subclient WeakEntityRef rescans only before login or after removal; no-listener fast path unchanged.239 tests/build claimed, planned100–300 spread-bot ABBA and150-player profiles unchecked. Closed unmerged, superseded by c2c778adf. #557 confirms optimization accepted without reproducing reporter's large slowdown.

## Direct patch findings {#direct-patch-findings}

Static unordered_map keyed by peer address stores weak peer, copied ID and four WeakEntityRefs. Reuses only unexpired peer entries, erases expired entries on misses, matches connection.batched_peer exactly, rescans player on expired weak entity, handles out-of-range subIDs without indexing. Event paths use cached ID/player, removed getId chainwalk/friend. No benchmark results in patch; final c2c778adf not yet compared.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (6744 characters; SHA-256 bad021389b9c1d5020de5412258ff190910184467752d63b6180b32347ba1f65), head 6369d047770bb6a69d044b297d87e02c1225b944. This covers the supplied PR patch, not unrelated commits or historical intermediate revisions. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/548
- https://github.com/EndstoneMC/endstone/pull/548#issuecomment-6251334495
