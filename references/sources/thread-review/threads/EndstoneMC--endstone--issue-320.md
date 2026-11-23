<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:320"],"source_type":"public","date":"2026-01-05","topics":["testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-320-playerportalevent-documented-but-unavailable"></a>
# EndstoneMC/endstone #320: PlayerPortalEvent documented but unavailable. {#endstonemc-endstone-320-playerportalevent-documented-but-unavailable}

Source: https://github.com/EndstoneMC/endstone/issues/320

## Evidence and attribution {#evidence-and-attribution}

Primary author: japtain-cack. Created 2026-01-05T16:16:46Z; recorded state closed; merged not applicable.

## Diagnosis {#diagnosis}

japtain-cack could not import PlayerPortalEvent after pip installing v0.10.18 despite finding it in /latest Python reference docs. wu-vincent explained /latest documents the development API; /stable corresponds to released software, and this event was not in v0.10.18.

## Reuse and limits {#reuse-and-limits}

Check documentation channel and installed package version before diagnosing a missing binding. This is a version-alignment support resolution; no broken import fix or code change is claimed.

## Additional source and attachment inspection {#additional-source-and-attachment-inspection}

The screenshot shows the /latest reference listing PlayerPortalEvent with PlayerTeleportEvent as its base, while the page repository badge says v0.10.18. The visible badge can therefore reinforce the user’s version confusion; it is not proof that the installed release exported the event.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Source and available attachment links are listed under Traceability; the separate acquisition and inspection ledger is not included in this distribution. A screenshot corroborates only visible content, not runtime causality.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/320
- https://github.com/EndstoneMC/endstone/issues/320#issuecomment-3760441210
- https://github.com/user-attachments/assets/23908de5-da75-470e-bac9-671c670ce206
