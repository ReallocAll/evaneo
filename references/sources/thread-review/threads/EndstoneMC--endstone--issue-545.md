<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:545"],"source_type":"public","date":"2026-10-06","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-545-running-endstone-on-older-bds-versions"></a>
# EndstoneMC/endstone #545: Running Endstone on older BDS versions {#endstonemc-endstone-545-running-endstone-on-older-bds-versions}

Source: https://github.com/EndstoneMC/endstone/issues/545

## Evidence and attribution {#evidence-and-attribution}

Primary author: GlitchWorks7. Created 2026-10-06T23:20:30Z; recorded state closed; merged not applicable.

An Endstone release hooks exactly one BDS build; refusing upgrade intentionally exits rather than running mismatched native addresses. Pin the matching Endstone release for an old server, accepting loss of later fixes. Missing version.txt for manually downloaded BDS caused misleading0.0.0; next prompt should report unknown and identify required version. Separate legitimate compatibility refusal from broken diagnosis wording. Personal path was deliberately withheld by reporter and not reconstructed.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/545
- https://github.com/EndstoneMC/endstone/issues/545#issuecomment-6251500665
