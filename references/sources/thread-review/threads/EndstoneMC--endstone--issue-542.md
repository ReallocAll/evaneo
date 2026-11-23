<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:542"],"source_type":"public","date":"2026-10-06","topics":["testing","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-542-cushions-are-not-usable-update-to-hotfix-26-52"></a>
# EndstoneMC/endstone #542: Cushions are not usable (Update to hotfix 26.52) {#endstonemc-endstone-542-cushions-are-not-usable-update-to-hotfix-26-52}

Source: https://github.com/EndstoneMC/endstone/issues/542

## Evidence and attribution {#evidence-and-attribution}

Primary author: RWRmrfrog. Created 2026-10-06T00:44:03Z; recorded state closed; merged not applicable.

Hotfix request motivated by unusable cushions and upstreamMCPE-241970. Wu reports26.52 support f37de3136 for next release. Brief availability decision; upstream issue and port implementation not independently audited.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/542
- https://github.com/EndstoneMC/endstone/issues/542#issuecomment-6014613451
