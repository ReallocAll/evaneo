<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:535"],"source_type":"public","date":"2026-09-16","topics":["testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-535-fix-map-preserve-static-map-decorations"></a>
# EndstoneMC/endstone #535: fix(map): preserve static map decorations {#endstonemc-endstone-535-fix-map-preserve-static-map-decorations}

Source: https://github.com/EndstoneMC/endstone/pull/535

## Evidence and attribution {#evidence-and-attribution}

Primary author: HP-network. Created 2026-09-16T00:49:28Z; recorded state closed; merged True.

HP-network preserves decorations without entity IDs while continuing recipient-specific filtering. Local syntax check is blocked by missing Boost; diff --check is the only completed check. Wu rebases onto0.11 and removes the filter entirely, because CraftMapRenderer's source behavior shows every decoration; other-player markers should survive too. #517 records that the first release/retest still failed, so distinguish proposed partial predicate from final filter removal and release timing.

## Direct patch findings {#direct-patch-findings}

Final diff removes recipient-ID filter altogether, not just allows static IDs; changelog explicitly includes other-player markers. No tests added. This verifies final code shape while #517 release retest remains separate.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (1481 characters; SHA-256 dded40402d78d1207aa4089b8dcd528ace8e4f85be9c04c6c625d7e2b348f659), head d22a00d2a0b781794e20a95b032abfcb0df8380e. This covers the supplied PR patch, not unrelated commits or historical intermediate revisions. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/535
- https://github.com/EndstoneMC/endstone/pull/535#issuecomment-5702962223
