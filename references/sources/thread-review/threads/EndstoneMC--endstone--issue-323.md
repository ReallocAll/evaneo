<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:323"],"source_type":"public","date":"2026-01-13","topics":["testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-323-feature-dynamic-property-api"></a>
# EndstoneMC/endstone #323: [feature] Dynamic Property API {#endstonemc-endstone-323-feature-dynamic-property-api}

Source: https://github.com/EndstoneMC/endstone/issues/323

## Evidence and attribution {#evidence-and-attribution}

Primary author: MisledWater79. Created 2026-01-13T16:39:56Z; recorded state open; merged not applicable.

## Need and staged design {#need-and-staged-design}

MisledWater79 requested world/entity dynamic properties for transferring or persisting data between ScriptAPI scripts and Endstone plugins. wu-vincent described a two-stage plan: low-level NBT access in v0.11.0 because dynamic properties are stored internally as NBT, then a dedicated world/entity Dynamic Property API in v0.12.0.

## Reusable decision and limits {#reusable-decision-and-limits}

Build a general representation layer before a higher-level convenience API, preserving interoperability while reducing raw-NBT burden later. The issue remains open in the snapshot. These version targets are a plan, not proof of delivery; no patch, storage layout, concurrency or compatibility test is included.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/323
- https://github.com/EndstoneMC/endstone/issues/323#issuecomment-3760840514
