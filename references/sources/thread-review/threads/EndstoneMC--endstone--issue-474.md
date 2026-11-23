<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:474"],"source_type":"public","date":"2026-08-09","topics":["testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-474-add-api-access-to-item-frame-contents"></a>
# EndstoneMC/endstone #474: Add API access to Item Frame contents {#endstonemc-endstone-474-add-api-access-to-item-frame-contents}

Source: https://github.com/EndstoneMC/endstone/issues/474

## Evidence and attribution {#evidence-and-attribution}

Primary author: barrywade. Created 2026-08-09T18:58:48Z; recorded state closed; merged not applicable.

barrywade needs item-frame contents without coordinate-based workarounds. Wu reports capture_state returning an ItemFrame block state for regular/glow frames, optional item, rotation in 45-degree steps and drop chance; assigning an item resets rotation. Bedrock models this as block state rather than Bukkit's entity despite familiar naming. Claimed implemented on develop for next release; code not independently inspected here.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/474
- https://github.com/EndstoneMC/endstone/issues/474#issuecomment-5245846041
