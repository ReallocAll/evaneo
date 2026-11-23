<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:517"],"source_type":"public","date":"2026-08-27","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-517-map-symbol-x-bug"></a>
# EndstoneMC/endstone #517: Map Symbol x Bug {#endstonemc-endstone-517-map-symbol-x-bug}

Source: https://github.com/EndstoneMC/endstone/issues/517

## Evidence and attribution {#evidence-and-attribution}

Primary author: wago5558-alt. Created 2026-08-27T16:08:51Z; recorded state closed; merged not applicable.

Explorer-map target markers disappear under Endstone but appear in the same single-player world. Wu first points to #535; the reporter retests0.11.11 with controlled Endstone on/off and says the problem persists. Wu then promises a second correction covering explorer and other players' markers in a later0.11 release. Keep the failed first retest: closure and the merged initial filter change are not evidence the shipped0.11.11 behavior was correct.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/517
- https://github.com/EndstoneMC/endstone/issues/517#issuecomment-5441917917
- https://github.com/EndstoneMC/endstone/issues/517#issuecomment-5702966038
- https://github.com/EndstoneMC/endstone/issues/517#issuecomment-5726916747
- https://github.com/EndstoneMC/endstone/issues/517#issuecomment-5752009480
