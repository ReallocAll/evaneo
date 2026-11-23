<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:469"],"source_type":"public","date":"2026-08-08","topics":["testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-469-server-crash"></a>
# EndstoneMC/endstone #469: server crash {#endstonemc-endstone-469-server-crash}

Source: https://github.com/EndstoneMC/endstone/issues/469

## Evidence and attribution {#evidence-and-attribution}

Primary author: SuperAnse. Created 2026-08-08T14:25:20Z; recorded state closed; merged not applicable.

Join-time null dereference follows ItemInstance::fromTag, setUserData and inventory copying on Windows 0.11.7. Wu says it should already be fixed in 0.11.8. Reporter thanks him but supplies no post-upgrade retest, so closure is not verified reproduction elimination.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/469
- https://github.com/EndstoneMC/endstone/issues/469#issuecomment-5227503004
- https://github.com/EndstoneMC/endstone/issues/469#issuecomment-5229272091
