<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:475"],"source_type":"public","date":"2026-08-11","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-475-color-particle"></a>
# EndstoneMC/endstone #475: Color Particle {#endstonemc-endstone-475-color-particle}

Source: https://github.com/EndstoneMC/endstone/issues/475

## Evidence and attribution {#evidence-and-attribution}

Primary author: barrywade. Created 2026-08-11T20:51:22Z; recorded state closed; merged not applicable.

Molang JSON RGB does not tint falling dust. Wu distinguishes serialization from interpretation: the wrapper transmits variables, but only particle definitions consuming them can respond; falling dust derives color from its block, and a custom resource pack is the suggested route. Dict-shaped molang_variables is planned for 0.12. These are maintainer claims about the particular built-ins, not an independent audit of every vanilla particle or proof that every submitted variable was encoded correctly.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/475
- https://github.com/EndstoneMC/endstone/issues/475#issuecomment-5495044440
