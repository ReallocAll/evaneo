<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:375"],"source_type":"public","date":"2026-04-10","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-375-playerdropitemevent-doesn-t-cancel-correctly-if-item-is-thrown-out-of-main-hand"></a>
# EndstoneMC/endstone #375: PlayerDropItemEvent doesn't cancel correctly if item is thrown out of main hand {#endstonemc-endstone-375-playerdropitemevent-doesn-t-cancel-correctly-if-item-is-thrown-out-of-main-hand}

Source: https://github.com/EndstoneMC/endstone/issues/375

## Evidence and attribution {#evidence-and-attribution}

Primary author: kleines-L. Created 2026-04-10T15:50:46Z; recorded state closed; merged not applicable.

## Disposition and evidence boundary {#disposition-and-evidence-boundary}

kleines-L reported that cancelling a main-hand drop made items vanish, while dropping from inventory cancelled correctly. warpanda1 could not reproduce and requested code; none appears. wu-vincent later points to #446 as fixed for the next release. Preserve the path-dependent reproduction and unresolved test evidence; the thread alone gives neither root cause nor a verified fix.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/375
- https://github.com/EndstoneMC/endstone/issues/375#issuecomment-5158751148
- https://github.com/EndstoneMC/endstone/issues/375#issuecomment-5389560840
