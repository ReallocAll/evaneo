<!-- retrieval: {"source_ids":["public:commit:0a61d7f232f7093610a77644008c29bf60066564","public:commit:1037aa6fe2d1146b09879b3cc49f516c141a1843","public:commit:1cdcf85c946efea9db549a543edc08402b1f8662","public:commit:39b885aa7afd9dd067027121536ca021d19bd80c","public:commit:3d5aacd054c14ca69600fad53a3b0e9e35491a44","public:commit:624aa5a7768fc5012c03d7f1f58c03049b2dd9d9","public:commit:6ce631d54c095c39e00538807f58427350ab623b","public:commit:7e02e75cebefd7cc4ceeba5902533c2d5e0b7211","public:commit:801c57c95c1c53c5caf380fc19c2ca15c9b2486b","public:commit:8a38c8aae6d2376459163591ba4f6af5ba1b5c1a","public:commit:8ba169c463a33ce82b1956ef31832b57a6a68079","public:commit:8ec4188bf7cab7d5714d616c8f37e735f104e590","public:commit:91b01aee98b3d01594a5f41e281a93498c2fe432","public:commit:a1a5e5603df712c7668de0ef55aa662bb271d5c7","public:commit:b041664b4dfad8124bfab98815e0dfbe0f51fa49","public:commit:f3a8b638d86a8063590621314a1a41f4803c3164"],"source_type":"public","date":"2024-04-21..2024-04-29","topics":["lifetime","concurrency","ffi","testing","build","api","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Scheduler prototype, simplification, tests and handle ownership {#scheduler-prototype-simplification-tests-and-handle-ownership}

## Useful conclusion {#useful-conclusion}

The strongest supported rationale is explicit in786: after a basic scheduler implementation, heartbeat, tests, lifecycle, thread safety and simplification still need work. Subsequent commits enact that agenda in stages. A custom linked queue and cancellation-command mechanism is discarded for a library queue plus a task index; tests reveal/fix the delayed-call path and uninitialized scheduler counters; public handles move from raw pointers to shared_ptr, including Python holders. This is a useful case of iterating the operational contract, not evidence that a concurrent queue alone makes the whole service thread-safe.

Endpoint840 still has meaningful limits: task owner is a borrowed Plugin, pending-task enumeration returns raw pointers, cancellation state/current tick are plain fields, heap storage is iterated rather than priority-popped, and server tick_count is not initialized. Preserve these as counterexamples to overgeneralized lessons and as bounded future verification questions. This research did not run tests or expand into a full concurrency audit.

## Interface and state experiments before execution exists {#interface-and-state-experiments-before-execution-exists}

727 introduces Task with ID, owner, sync/cancelled queries, cancel and callable run. It always reports sync and cancellation is TODO.729 proposes scheduleTask/scheduleDelayedTask/scheduleRepeatingTask returning optional IDs, with delay and period measured in ticks. The concrete scheduler is only a priority queue plus atomic ID allocator; it does not yet implement the interface. Task gets creation time, period, next-run and a shared next link, but its constructor does not initialize the supplied period or next-run.

783 adds a Pending/Cancelled/Processing/Done state enum, initializes period, makes queries const and guards an empty callable.784 lets Task.cancel delegate to a borrowed Scheduler.785 changes the user-facing methods to runTask/runTaskLater/runTaskTimer and returns a borrowed Task pointer instead of optional ID. Documentation promises next-tick execution and an unordered pending-list view. These are sequential alternatives observed in the source; there is no external review explaining why each was chosen.

786 finally inherits Scheduler and supplies admission checks for empty callable or disabled plugin. It introduces an atomic raw tail with shared next links, a sentinel/internal task form, runner map locking and cancellation tasks that mutate queues later. The heartbeat remains empty. Several implementation gaps are visible: runTaskLater passes0 instead of delay; handle moves its shared_ptr then returns get() from the moved-from handle; counters are uninitialized; erase/remove sequences are incomplete. Its own message acknowledges unfinished lifecycle/thread safety/testing, so this is a prototype to understand, not an exemplar to transplant.

## Simplification changes the ownership graph and cancellation mechanism {#simplification-changes-the-ownership-graph-and-cancellation-mechanism}

787 removes the state enum, linked-next storage, scheduler reference and internal task constructor. A task now owns its callable, borrows Plugin and contains a local cancelled bool. cancel only marks that bool. This temporarily breaks the still-old scheduler until789, so commits are not independent build snapshots.788 adds concurrentqueue1.0.4, and789 replaces the custom queue with moodycamel::ConcurrentQueue of shared tasks.

The new architecture separates three roles:

- pending ingress carries shared tasks waiting to enter the server-thread execution structure;
- tasks_ is a mutex-protected ID→shared-task index for cancellation/query;
- queue_ groups tasks by execution tick, with vectors intended to prioritize by next-run/creation time.

runTaskTimer assigns next-run=current_tick+delay, enqueues and indexes the task. A failed enqueue returns null. Cancellation by ID/plugin marks the task then removes it from the index; remaining queue references retain the object until drained. This avoids the custom cancellation-command tasks and shared linked nodes. However, direct Task.cancel does not immediately erase the task index. A cancelled task discarded during initial pending drain is skipped without index erase, so direct cancellation can leave a stale indexed entry at this endpoint. isQueued is index membership, whereas getPendingTasks filters cancelled tasks; their answers can therefore differ.

The heartbeat first drains ingress, clamps overdue next-run to current tick, then processes all due groups. It catches std::exception from a task and logs it. Repeating tasks are scheduled relative to the current execution tick, so a skipped tick produces one run followed by a new future period rather than catching up every missed period. Work added during a running task is placed in pending ingress, which is drained only at the start of the next heartbeat. This supports next-tick deferral, although current_tick_ is updated only at the end, so scheduling from inside a callback uses the previous stored tick when calculating delay.

Completion marks a one-shot task cancelled after removing it from tasks_. There is no separate completed status after787, so isCancelled conflates natural completion with cancellation. A repeating task that cancels itself may still be re-enqueued once and then skipped. Enqueue failure on repeat is not checked, unlike first admission. These details define the actual endpoint contract; the documentation's brief method names do not capture them all.

## IDs and ordering: local repairs have limited reach {#ids-and-ordering-local-repairs-have-limited-reach}

790 wraps IDs to1 and checks existing task-map keys under a mutex; it also sets current_task before run and clears it afterward, allowing isRunning to answer during callbacks. Allocation and later insertion remain separate operations, and the code has no full-space termination rule. This is a practical occupied-ID check, not a proof of all wrap/concurrent allocation cases.

791 supplies the previously unused comparator to push_heap and changes its arguments to shared_ptr. It compares next-run and then steady-clock creation time. But the execution loop walks the vector directly rather than repeatedly popping the heap. A heap guarantees its top priority, not sorted traversal of all elements. Thus the comment/intent of deterministic ordering must not be promoted to a verified FIFO guarantee for three or more equal-tick tasks. The tests added later do not assert ordering. No dependency internals were executed or independently audited.

## Wire into server, then test the public contract {#wire-into-server-then-test-the-public-contract}

792 gives EndstoneServer unique ownership of scheduler and console sender, initialized after the plugin manager.793 calls server.tick before native Minecraft::tickSimtime. The server increments tick_count_ and forwards it to heartbeat.794 initializes scheduler current_tick/current_task but does not initialize the separate server tick_count_ declared793; endpoint header and constructor reads confirm that gap. It would be misleading to say the counter issue is globally fixed just because the unit-tested scheduler counters are.

794 adds eight test scenarios: immediate next-heartbeat execution, delayed execution after five ticks, repetition, cancel one, cancel all for a plugin, running-state query inside callback, queued-state query and pending-task enumeration. The same commit repairs runTaskLater's ignored delay, an exact example where adding tests changes behavior rather than merely increasing test count. Plugin lifecycle setters become protected so the mock can enable itself.

Coverage is bounded. Tests manually drive heartbeat from zero and destroy scheduler before plugin/server. They do not exercise the real native tick hook, same-tick ordering, concurrent scheduling/cancellation, callback-created delayed tasks, direct Task.cancel index cleanup, disabled/empty admissions, thrown callback, queue allocation failure or plugin unload. Initial tests also retain raw Task pointers and access them after one-shot execution; scheduler ownership can already be gone. Nothing in this review asserts that these tests passed.

## Shared handles repair one lifetime boundary, not every owner {#shared-handles-repair-one-lifetime-boundary-not-every-owner}

795 exposes Task/Scheduler to Python with borrowed return policies and callable conversion. It also adds Server.get_player and broadcast bindings in the same commit.796 changes scheduling returns to shared_ptr<Task>, binds Python Task with a shared holder and updates tests to retain returned handles. The running test captures its actual handle rather than assuming ID1. This makes completion-time queries on returned task objects survive scheduler removal.

The reason for shared ownership is not explicitly stated beyond the commit title; preventing dangling public handles is an inference strongly supported by the before/after API and tests. The task still borrows Plugin, and getPendingTasks still returns raw pointers. Holding a task can extend its captured callable's lifetime beyond server/plugin lifecycle. Endpoint PluginManager disable/clear does not call scheduler.cancelTasks. Therefore, shared task ownership is not a complete guarantee for owner/callback safety or Python interpreter shutdown. Prior server-reset-under-GIL behavior is relevant history, but this unit does not prove all externally retained shared task objects die under that guard.

## Transferable reasoning, attribution and limits {#transferable-reasoning-attribution-and-limits}

A proportionate lesson is to test the exact user-facing delayed/cancellation/retained-handle paths and separate queue ownership from service/owner lifetime. The queue-library replacement is a local simplification, not evidence against all custom data structures. The scheduler is sync-execution-only even though it uses concurrent ingress; no asynchronous task implementation is added. All commits here are Vincent-authored; moodycamel's queue is an external dependency whose internals were not read. No external collaborator rationale, benchmark or test-run result is available in this unit.

Prior reviewed context: event threading and dispatch, [Python boundary and shutdown-related caveats](../endstone-0601-0720/03-python-surface.md). No new reading of excluded historical sources is implied.

## Individual source dispositions {#individual-source-dispositions}

<a id="commit-727"></a>
### 727 · feat(scheduler): add task interface {#commit-727}

[91b01aee98b3d01594a5f41e281a93498c2fe432](https://github.com/EndstoneMC/endstone/commit/91b01aee98b3d01594a5f41e281a93498c2fe432) · 2024-04-21T22:32:13Z · Vincent (author and committer).

Adds Task interface and concrete plugin-borrowed callable/task-ID implementation; sync always true, cancel TODO, cancelled flag never changed. Runnable executes directly; scheduler ownership/lifetime not implemented.


<a id="commit-729"></a>
### 729 · feat: improve Task and Scheduler class {#commit-729}

[7e02e75cebefd7cc4ceeba5902533c2d5e0b7211](https://github.com/EndstoneMC/endstone/commit/7e02e75cebefd7cc4ceeba5902533c2d5e0b7211) · 2024-04-21T23:18:12Z · Vincent (author and committer).

Design scaffold adds tick delay/period scheduling API returning optional IDs and priority ordering next-run then creation-time. Concrete scheduler only allocates IDs and pending queue, does not yet inherit public Scheduler. Task constructor accepts period but fails to initialize period_/next_run_; cancel/isCancelled remain TODO. Shared next link unused. Later783–791 replace this scaffold.


<a id="commit-783"></a>
### 783 · refactor: improve EndstoneTask {#commit-783}

[624aa5a7768fc5012c03d7f1f58c03049b2dd9d9](https://github.com/EndstoneMC/endstone/commit/624aa5a7768fc5012c03d7f1f58c03049b2dd9d9) · 2024-04-26T23:26:12Z · Vincent (author and committer).

Task scaffold gains const queries/status enum, initializes period, guards empty callable; public cancel still TODO. Internal cancel0 marks Cancelled; next-run still assigned externally.


<a id="commit-784"></a>
### 784 · refactor: improve EndstoneTask by adding a reference to the Scheduler {#commit-784}

[8ba169c463a33ce82b1956ef31832b57a6a68079](https://github.com/EndstoneMC/endstone/commit/8ba169c463a33ce82b1956ef31832b57a6a68079) · 2024-04-26T23:40:09Z · Vincent (author and committer).

Adds borrowed Scheduler reference so Task.cancel delegates cancelTask(id); later787 removes this coupling in favor of local cancelled flag.


<a id="commit-785"></a>
### 785 · refactor: update Scheduler class {#commit-785}

[1cdcf85c946efea9db549a543edc08402b1f8662](https://github.com/EndstoneMC/endstone/commit/1cdcf85c946efea9db549a543edc08402b1f8662) · 2024-04-26T23:57:56Z · Vincent (author and committer).

Changes public scheduler from optional IDs to borrowed Task pointers, names runTask/runTaskLater/runTaskTimer and adds pending-task enumeration. Documents next-tick sync contract and unordered pending list. Ownership hazard later addressed796.


<a id="commit-786"></a>
### 786 · feat: basic implementation of Scheduler {#commit-786}

[39b885aa7afd9dd067027121536ca021d19bd80c](https://github.com/EndstoneMC/endstone/commit/39b885aa7afd9dd067027121536ca021d19bd80c) · 2024-04-27T01:19:47Z · Vincent (author and committer).

Basic scheduler explicitly lists unfinished heartbeat/tests/lifecycle/thread safety/simplification in message. Implements custom atomic-tail/shared-next queue, cancellation command tasks and runner maps; heartbeat still empty. runTaskLater discards delay, handle returns moved-from shared_ptr.get(), counters uninitialized and erase/remove logic partial. Preserve as acknowledged prototype, not adopted safe concurrency pattern.


<a id="commit-787"></a>
### 787 · refactor: simplify EndstoneTask {#commit-787}

[b041664b4dfad8124bfab98815e0dfbe0f51fa49](https://github.com/EndstoneMC/endstone/commit/b041664b4dfad8124bfab98815e0dfbe0f51fa49) · 2024-04-27T16:34:01Z · Vincent (author and committer).

Simplifies Task by removing status enum, linked next node, scheduler reference and special cancellation-task constructor; cancel now sets local bool. Existing scheduler still expects removed machinery until789. Explicit simplification in title, not independent thread-safety proof.


<a id="commit-788"></a>
### 788 · chore(deps): add concurrentqueue/1.0.4 {#commit-788}

[8ec4188bf7cab7d5714d616c8f37e735f104e590](https://github.com/EndstoneMC/endstone/commit/8ec4188bf7cab7d5714d616c8f37e735f104e590) · 2024-04-27T16:46:02Z · Vincent (author and committer).

Adds concurrentqueue1.0.4 to core dependencies in CMake and Conan, preparing replacement of custom pending queue. Dependency implementation not independently read.


<a id="commit-789"></a>
### 789 · feat: implement Scheduler for sync tasks {#commit-789}

[801c57c95c1c53c5caf380fc19c2ca15c9b2486b](https://github.com/EndstoneMC/endstone/commit/801c57c95c1c53c5caf380fc19c2ca15c9b2486b) · 2024-04-27T17:59:57Z · Vincent (author and committer).

Replaces custom linked queue/cancellation tasks with moodycamel pending queue, shared task map under mutex and tick-keyed execution queues. Implements heartbeat, exception logging, repeat requeue and deferred cancellation. Queue comparator initially unused, current task not set, delay bug remains until794. Thread-safe ingress container does not make plain cancelled/current_tick fields safe; getPendingTasks returns borrowed pointers.


<a id="commit-790"></a>
### 790 · feat: avoid id conflicting edge cases {#commit-790}

[1037aa6fe2d1146b09879b3cc49f516c141a1843](https://github.com/EndstoneMC/endstone/commit/1037aa6fe2d1146b09879b3cc49f516c141a1843) · 2024-04-27T18:08:35Z · Vincent (author and committer).

Tracks current_task around execution and checks ID reuse under task-map mutex after wrapping to1. Avoids occupied IDs but allocation and map insertion are separate; no exhaustive concurrent wrap test or full-ID-space fallback.


<a id="commit-791"></a>
### 791 · fix: push_heap with comparator {#commit-791}

[f3a8b638d86a8063590621314a1a41f4803c3164](https://github.com/EndstoneMC/endstone/commit/f3a8b638d86a8063590621314a1a41f4803c3164) · 2024-04-28T09:59:30Z · Vincent (author and committer).

Supplies TaskComparator to push_heap, comparing next-run then creation-time. Execution still iterates heap storage without pop_heap, so full FIFO/creation order is not guaranteed for3+tasks; comparator repair alone is not ordered-drain proof.


<a id="commit-792"></a>
### 792 · feat: add Server::getScheduler {#commit-792}

[6ce631d54c095c39e00538807f58427350ab623b](https://github.com/EndstoneMC/endstone/commit/6ce631d54c095c39e00538807f58427350ab623b) · 2024-04-28T10:08:00Z · Vincent (author and committer).

Server owns Scheduler unique_ptr and exposes borrowed service; converts console sender to unique_ptr initialized after plugin manager/loader. MockServer updated. Newservice lifecycle tied server, no automatic plugin-disable cancellation yet.


<a id="commit-793"></a>
### 793 · feat: server and scheduler tick {#commit-793}

[3d5aacd054c14ca69600fad53a3b0e9e35491a44](https://github.com/EndstoneMC/endstone/commit/3d5aacd054c14ca69600fad53a3b0e9e35491a44) · 2024-04-29T10:51:30Z · Vincent (author and committer).

Hooks Minecraft::tickSimtime to server.tick before original, increments tick_count and heartbeats scheduler. tick_count_ declaration lacks initializer and constructor unchanged; later794 initializes scheduler counters only. No native timing measurement.


<a id="commit-794"></a>
### 794 · feat: add tests for Scheduler {#commit-794}

[8a38c8aae6d2376459163591ba4f6af5ba1b5c1a](https://github.com/EndstoneMC/endstone/commit/8a38c8aae6d2376459163591ba4f6af5ba1b5c1a) · 2024-04-29T11:26:07Z · Vincent (author and committer).

Adds8 GTest scheduler scenarios: immediate/delayed/repeating/cancel one/cancel plugin/running/queued/pending. Fixes ignored delay and initializes scheduler counters; makes Plugin lifecycle setters protected for mock enable. Raw Task pointers accessed after execution in tests can outlive scheduler ownership, motivating796 inferred. No concurrent/order/empty/disabled/exception tests, no tests executed.


<a id="commit-795"></a>
### 795 · feat(python): add bindings for Scheduler {#commit-795}

[0a61d7f232f7093610a77644008c29bf60066564](https://github.com/EndstoneMC/endstone/commit/0a61d7f232f7093610a77644008c29bf60066564) · 2024-04-29T11:43:24Z · Vincent (author and committer).

Adds Python scheduler/task bindings and facade, plus Server.get_player/broadcast APIs. Raw Task returns initially reference policy; UUID input now exposes existing665 caster load path. Stubs omit nullable results. Server.name still bound getVersion. API exposure makes ownership/conversion correctness consequential, no Python scheduler tests added.


<a id="commit-796"></a>
### 796 · refactor: use shared_ptr for the scheduled Task {#commit-796}

[a1a5e5603df712c7668de0ef55aa662bb271d5c7](https://github.com/EndstoneMC/endstone/commit/a1a5e5603df712c7668de0ef55aa662bb271d5c7) · 2024-04-29T12:10:33Z · Vincent (author and committer).

Changes scheduling returns to shared_ptr<Task> and Python shared holder, updates tests to retain handles and obtain actual task IDs. Resolves borrowed-handle lifetime after task completion for these returns; pending-task list still raw and Task.owner still borrowed Plugin. Retained callable ownership can extend capture lifetime; not full plugin/server lifetime guarantee.
