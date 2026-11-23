<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:317"],"source_type":"public","date":"2025-12-31","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-317-scheduler-tasks-ignore-delay-parameter"></a>
# EndstoneMC/endstone #317: Scheduler tasks ignore delay parameter {#endstonemc-endstone-317-scheduler-tasks-ignore-delay-parameter}

Source: https://github.com/EndstoneMC/endstone/issues/317

## Evidence and attribution {#evidence-and-attribution}

Primary author: zl9545. Created 2025-12-31T17:37:19Z; recorded state closed; merged not applicable.

## Problem and discriminating evidence {#problem-and-discriminating-evidence}

zl9545 demonstrated delay=200 tasks registered in on_enable and ServerLoadEvent executing immediately on an older world, while a tiny new world delayed about ten seconds. A 5.07 MB world failed only at initial startup; the same world after /reload behaved correctly. wu-vincent first asked whether it was universal, then used these observations to identify a clock-origin mismatch, not a file-size performance problem.

## Root cause and actual fix {#root-cause-and-actual-fix}

Tasks compute nextRun=current_tick+delay while the scheduler counter is still zero before its first heartbeat. BDS supplies a persisted ever-increasing world tick, so on an old world the first incoming tick already exceeds the due tick. Commit 43fe66ded anchors optional base_tick_ to the first incoming value and normalizes current_tick=current_tick-base+1. The +1 deliberately preserves the Nth-heartbeat contract for delay N.

## Tests, revision costs, and reuse {#tests-revision-costs-and-reuse}

The new RunTaskLaterWhenFirstTickIsLarge regression schedules delay 5, starts at 5,000,000 and verifies no immediate execution, then execution on the fifth heartbeat. Static inspection also finds the same commit removes the CancelSingleAsyncTaskDoesNotDeadlock regression for #351; that is a real coverage loss outside the main fix and should not be silently omitted. No tests were run here. Clock normalization is the reusable design: choose session-relative time before scheduling and ensure startup, reload and persisted-state cases share the same origin.

## Code and verification boundary {#code-and-verification-boundary}

Inspected complete mirror commit 43fe66ded63dd817d3714546d1354096d02b035d and its scheduler regression test; also observed removal of the separate single-async-cancel deadlock test. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/317
- https://github.com/EndstoneMC/endstone/issues/317#issuecomment-3760805470
- https://github.com/EndstoneMC/endstone/issues/317#issuecomment-3762625320
- https://github.com/EndstoneMC/endstone/issues/317#issuecomment-4606026502
