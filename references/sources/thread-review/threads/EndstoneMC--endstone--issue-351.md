<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:351"],"source_type":"public","date":"2026-03-11","topics":["concurrency","testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-351-runtasktimerasync-crashes-when-using-reload"></a>
# EndstoneMC/endstone #351: runTaskTimerAsync crashes when using /reload {#endstonemc-endstone-351-runtasktimerasync-crashes-when-using-reload}

Source: https://github.com/EndstoneMC/endstone/issues/351

## Evidence and attribution {#evidence-and-attribution}

Primary author: OPsteffOP. Created 2026-03-11T15:53:59Z; recorded state closed; merged not applicable.

## Reproduction and diagnosis {#reproduction-and-diagnosis}

OPsteffOP supplied an empty repeating async task followed by /reload, producing MSVC “resource deadlock would occur” and leaving the plugin disabled. A second reproduction directly scheduled a long-delayed async task and called cancelTasks, removing reload from the causal chain.

wu-vincent traced recursive acquisition of non-recursive tasks_mtx_: cancellation holds the task map lock, idle async doCancel calls removeTask, and removeTask reacquires the same lock. The exception unwinds before plugin re-enable. Sync tasks avoid that callback. A worker/task lock also creates a latent ABBA inversion.

## Actual code and tests {#actual-code-and-tests}

Commit 62f8d63c8 copies shared task handles under the map lock, erases sync entries there, then cancels after release. Async run/doCancel compute completion/idle state under their own mutex and remove from the scheduler only afterward. A cancelled repeating task is removed by its last worker. isRunning similarly releases the map lock before querying workers. The commit leaves its existing return of getWorkers().empty() unchanged; this review does not infer corrected running-state semantics.

Two regressions cover bulk and single cancellation of idle async tasks. Subsequent #317's fix deletes the single-task regression, which limits retained coverage despite this issue's claim of both tests. No tests were executed here. General invariant: never hold map and child-object locks simultaneously when callbacks can reenter the owner.

## Code and verification boundary {#code-and-verification-boundary}

Inspected full commit 62f8d63c8598699ab080b5bc8ed3a12eaf1130a1 and compared test retention against 43fe66ded. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/351
- https://github.com/EndstoneMC/endstone/issues/351#issuecomment-4054124499
- https://github.com/EndstoneMC/endstone/issues/351#issuecomment-4605343294
