<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:239"],"source_type":"public","date":"2025-08-07","topics":["concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-239-bug-server-sometimes-doesn-t-shutdown-correctly"></a>
# EndstoneMC/endstone #239: [bug] Server sometimes doesn't shutdown correctly {#endstonemc-endstone-239-bug-server-sometimes-doesn-t-shutdown-correctly}

Source: https://github.com/EndstoneMC/endstone/issues/239

## Review scope and state {#review-scope-and-state}

- Thread author: kleines-L; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

kleines-L reports incomplete long-running shutdowns, crash/restart loops, a crashpad executable Text file busy error during preparation, and a still-bound bedrock process. Wu explicitly cannot pinpoint the root cause and suggests the crash reporter may outlive the main process; delay between restarts or container lifecycle management are mitigations. The observed surviving UDP listener means a lingering crash reporter alone is not a complete demonstrated explanation. No patch, process-tree investigation, or reproduction establishes whether a supervisor, BDS child, plugin teardown or reporter is responsible.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/239
- https://github.com/EndstoneMC/endstone/issues/239#issuecomment-3268422415
