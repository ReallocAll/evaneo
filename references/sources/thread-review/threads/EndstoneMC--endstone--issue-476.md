<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:476"],"source_type":"public","date":"2026-08-12","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-476-per-player-entity-and-block-visibility"></a>
# EndstoneMC/endstone #476: Per-player entity and block visibility {#endstonemc-endstone-476-per-player-entity-and-block-visibility}

Source: https://github.com/EndstoneMC/endstone/issues/476

## Evidence and attribution {#evidence-and-attribution}

Primary author: THEBOSS9345. Created 2026-08-12T02:19:42Z; recorded state closed; merged not applicable.

THEBOSS9345 asks for stable per-player visibility APIs instead of raw packet logic. Wu points to #501: hide/show/can-see actor methods with plugin references, visibility events and client-only block changes in 0.12. Actor terminology reflects Bedrock; the block spoof does not mutate server world state. Packeting's earlier timing comment is not an implementation guarantee.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/476
- https://github.com/EndstoneMC/endstone/issues/476#issuecomment-5302118003
- https://github.com/EndstoneMC/endstone/issues/476#issuecomment-5319708880
- https://github.com/EndstoneMC/endstone/issues/476#issuecomment-5495104840
