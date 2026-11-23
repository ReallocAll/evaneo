<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/scripting-nodejs-release:2"],"source_type":"public","date":"2026-08-09","topics":["testing","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-scripting-nodejs-release-2-not-working-on-linux-ubuntu"></a>
# EndstoneMC/scripting-nodejs-release #2: not working on linux ubuntu {#endstonemc-scripting-nodejs-release-2-not-working-on-linux-ubuntu}

Source: https://github.com/EndstoneMC/scripting-nodejs-release/issues/2

## Evidence and attribution {#evidence-and-attribution}

Primary author: AdemonG1tHub. Created 2026-08-09T00:54:39Z; recorded state closed; merged not applicable.

Fresh Ubuntu24.04 cannot load runtime because libc++.so.1 is missing; plugin logs a fallback to QuickJS. Wu later reports fixed for next release without details. Distinguish deployment dependency failure from JavaScript execution defect, and graceful runtime fallback from successful Node activation.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/scripting-nodejs-release/issues/2
- https://github.com/EndstoneMC/scripting-nodejs-release/issues/2#issuecomment-6169067428
