<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:428"],"source_type":"public","date":"2026-07-09","topics":["testing","performance","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-428-ability-to-control-updating-of-client-on-block-settype"></a>
# EndstoneMC/endstone #428: Ability to control updating of client on block setType {#endstonemc-endstone-428-ability-to-control-updating-of-client-on-block-settype}

Source: https://github.com/EndstoneMC/endstone/issues/428

## Evidence and attribution {#evidence-and-attribution}

Primary author: MisledWater79. Created 2026-07-09T04:29:23Z; recorded state closed; merged not applicable.

## Requested optimization and boundary decision {#requested-optimization-and-boundary-decision}

MisledWater79 wanted setType to suppress client updates during bulk chunk edits, potentially only in a chunk-load callback. wu-vincent distinguishes Bukkit applyPhysics (neighbor simulation) from client notification, and rejects a core option because existing packet APIs can cancel outgoing UpdateBlock packets and send affected chunks afterward. A plugin knows recipient selection and resend timing; core would have to guess.

This chooses composable low-level capability over another convenience flag. It imposes plugin responsibility for consistency and final resynchronization; no packet batching benchmark or sample implementation is supplied. Reopen if the packet API has a real capability gap.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/428
- https://github.com/EndstoneMC/endstone/issues/428#issuecomment-5495246637
