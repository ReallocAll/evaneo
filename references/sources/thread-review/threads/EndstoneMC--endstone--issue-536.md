<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:536"],"source_type":"public","date":"2026-09-17","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-536-poplar-leaves-decay-incorrectly-on-bds-1-26-51-with-endstone-0-11-11"></a>
# EndstoneMC/endstone #536: Poplar leaves decay incorrectly on BDS 1.26.51 with Endstone 0.11.11 {#endstonemc-endstone-536-poplar-leaves-decay-incorrectly-on-bds-1-26-51-with-endstone-0-11-11}

Source: https://github.com/EndstoneMC/endstone/issues/536

## Evidence and attribution {#evidence-and-attribution}

Primary author: wago5558-alt. Created 2026-09-17T14:23:13Z; recorded state closed; merged not applicable.

Only new poplar leaves decay despite intact trunks; reporter clearly distinguishes single-player comparison from an unperformed plain-BDS A/B. Selectively cancelling LeavesDecayEvent is a useful localization clue, not a root-cause proof alone. Wu identifies stale copied block lists in Endstone's reimplemented native decay check: neither poplar logs nor leaves were recognized. 43d537e60 reportedly restores the lists. Reusable risk: reimplementing vanilla behavior carries data-maintenance obligations when new block families arrive.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/536
- https://github.com/EndstoneMC/endstone/issues/536#issuecomment-5722323090
