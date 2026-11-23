<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:473"],"source_type":"public","date":"2026-08-09","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-473-can-mapitemsaveddata-class-be-implemented"></a>
# EndstoneMC/endstone #473: Can MapItemSavedData class be implemented? {#endstonemc-endstone-473-can-mapitemsaveddata-class-be-implemented}

Source: https://github.com/EndstoneMC/endstone/issues/473

## Evidence and attribution {#evidence-and-attribution}

Primary author: SuperAnse. Created 2026-08-09T16:05:13Z; recorded state closed; merged not applicable.

A request to expose native MapItemSavedData is declined in favor of stable MapMeta, MapView, MapRenderer, MapCanvas and MapCursor capabilities. Wu asks which operation is missing rather than promising an unstable BDS class. Reusable boundary: expose user tasks through public abstractions, not reverse-engineered internal types merely because they exist.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/473
- https://github.com/EndstoneMC/endstone/issues/473#issuecomment-5232669113
