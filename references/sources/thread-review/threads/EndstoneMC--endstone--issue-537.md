<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:537"],"source_type":"public","date":"2026-09-18","topics":["ffi","testing","performance","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-537-maps-in-simulated-chunks-are-initialized-every-tick"></a>
# EndstoneMC/endstone #537: Maps in simulated chunks are initialized every tick {#endstonemc-endstone-537-maps-in-simulated-chunks-are-initialized-every-tick}

Source: https://github.com/EndstoneMC/endstone/issues/537

## Evidence and attribution {#evidence-and-attribution}

Primary author: ForestOfLight. Created 2026-09-18T20:25:30Z; recorded state closed; merged not applicable.

MapInitializeEvent repeats each tick for maps in simulated/ticking-area chunks and causes a performance regression from26.45 to26.51. Reporter includes profiler screenshots, clean logs and a no-player custom-world repro; the environment field inconsistently says1.21.51 while prose says1.26.51. Wu says recent commits fix it and a hotfix is forthcoming, without naming a commit or explaining mechanism. All three profiler screenshots were subsequently inspected; numerical observations and later implementation evidence follow.

## Additional source and attachment inspection {#additional-source-and-attachment-inspection}

All three images were inspected. The metrics capture shows TPS 7.73/7.85/8.13 (1/5/15m), median MSPT 126 and 95th percentile 141, with TPS falling over the displayed half-hour. One server-thread stack attributes 54.65% to scheduler heartbeat, 53.90% to EndstoneServer::getMap and 41.77% to MapDataManager::_loadMapData. A later capture shows scheduler heartbeat at 5.80% and Level::tick at 14.70%. These are separate reporter-selected profiles, not a controlled before/after benchmark, and do not by themselves identify an ABI error.

The complete later commit 7ad256cc1fd58a60a5c3900599fc65f630ac3914 (2026-10-06, seven files) supplies the mechanism and Fixes #537. Its author reports BDS 1.26.51 split deserialization from publication; the Windows pattern still named _loadMapData actually hit _deserializeMapData, whose hidden return pointer was mistaken for a returned map. A stack-derived map ID then caused deferred get_map lookups to miss and requeue themselves. Linux getMapSavedData missed the deferred container-load path. The patch replaces both platform hooks with _publishMapData, passes ownership of the unique_ptr to the original, and only schedules an event when it returns a nonnull inserted map. It captures the publication uuid, not the map's deserialized internal ID, because stored mapId can differ.

Both signature recipes and symbol tables are updated to matching call sites, with explicit pointer-return/unique_ptr argument types. The commit reports unique matches in BDS 1.26.52.3 and headless Windows/Linux tests: 2,000 absent-ID get_map calls leave no tasks and both direct/chest loads emit once. Those experiments are authored claims; no test fixture is included and this review did not run them. The important reusable rule is to hook the actual publication boundary and verify ABI return conventions, rather than trusting a familiar symbol label after an upstream function split.

## Code and verification boundary {#code-and-verification-boundary}

All distinct supplied diagnostic evidence and complete relevant follow-up commit patches/messages were inspected. Public sources are linked under Traceability; the original acquisition, hashes, and per-file inspection inventories are not distributed. No runtime reproduction. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Attachment coverage: A screenshot corroborates only visible content, not runtime causality.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/537
- https://github.com/EndstoneMC/endstone/issues/537#issuecomment-5735918846
- https://github.com/user-attachments/assets/3420587b-52ac-477a-b57e-15ac0af9a9ec
- https://github.com/user-attachments/assets/2f8305aa-78fe-4bfd-b37c-79826f40263f
- https://github.com/user-attachments/assets/65dbd141-988d-40ef-809f-e348574a880a
- https://github.com/EndstoneMC/endstone/commit/7ad256cc1fd58a60a5c3900599fc65f630ac3914
