<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:430"],"source_type":"public","date":"2026-07-10","topics":["testing","performance","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-430-feature-sendactionbar"></a>
# EndstoneMC/endstone #430: [feature] send_actionbar {#endstonemc-endstone-430-feature-sendactionbar}

Source: https://github.com/EndstoneMC/endstone/issues/430

## Evidence and attribution {#evidence-and-attribution}

Primary author: DayOfMagic. Created 2026-07-10T20:04:18Z; recorded state closed; merged not applicable.

## Need and outcome {#need-and-outcome}

DayOfMagic was sending ScriptAPI events for thirty players each second to display action bars and reported performance cost. wu-vincent states player.send_action_bar(text) was added for the next release. No benchmark or implementation detail; preserve the demand for a direct API and avoid quantifying unmeasured gains.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/430
- https://github.com/EndstoneMC/endstone/issues/430#issuecomment-5079147536
