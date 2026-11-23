<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:525"],"source_type":"public","date":"2026-09-05","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-525-bug-endstonebossbar-send-uses-player-uuid-to-the-boss"></a>
# EndstoneMC/endstone #525: [bug] EndstoneBossBar::send() uses player uuid to the boss {#endstonemc-endstone-525-bug-endstonebossbar-send-uses-player-uuid-to-the-boss}

Source: https://github.com/EndstoneMC/endstone/issues/525

## Evidence and attribution {#evidence-and-attribution}

Primary author: nikastro-w. Created 2026-09-05T18:31:38Z; recorded state closed; merged not applicable.

Multiple boss bars overwrite because boss_id equals recipient player ID. A minimal two-bar report identifies the collision. Wu later points to a489ad95c. #532 explains why merely allocating a fresh unique ID is insufficient: the client must know a corresponding actor and dimension-change queries must also be handled. Thus this report's valid diagnosis does not establish the proposed minimal repair.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/525
- https://github.com/EndstoneMC/endstone/issues/525#issuecomment-6251909577
