<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:442"],"source_type":"public","date":"2026-07-20","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-442-the-seed-isn-t-hiding"></a>
# EndstoneMC/endstone #442: The seed isn’t hiding {#endstonemc-endstone-442-the-seed-isn-t-hiding}

Source: https://github.com/EndstoneMC/endstone/issues/442

## Evidence and attribution {#evidence-and-attribution}

Primary author: jaydenlwk1233-byte. Created 2026-07-20T10:59:03Z; recorded state closed; merged not applicable.

Seed hiding depends on client-side chunk generation. MisledWater79 asks about that setting; the reporter confirms it is enabled, and Wu says disable it. This is operational guidance, not a cryptographic guarantee that all world-seed leakage is prevented.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/442
- https://github.com/EndstoneMC/endstone/issues/442#issuecomment-5022835133
- https://github.com/EndstoneMC/endstone/issues/442#issuecomment-5023181960
- https://github.com/EndstoneMC/endstone/issues/442#issuecomment-5025971877
