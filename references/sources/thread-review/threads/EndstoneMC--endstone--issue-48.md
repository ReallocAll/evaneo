<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:48"],"source_type":"public","date":"2024-09-05","topics":["lifetime","concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-48-bug-reload-command-should-stop-and-remove-all-scheduled-tasks"></a>
# EndstoneMC/endstone #48: [bug] `/reload` command should stop and remove all scheduled tasks {#endstonemc-endstone-48-bug-reload-command-should-stop-and-remove-all-scheduled-tasks}

Source: https://github.com/EndstoneMC/endstone/issues/48

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu reports repeating tasks surviving plugin unload/reload, causing duplicate scheduling on re-enable. Desired invariant is stop and remove all tasks owned by a plugin before unloading it. No patch is linked, so the thread defines the lifecycle/resource-ownership requirement but not concurrency, in-flight cancellation or teardown guarantees.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/48
