<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:127"],"source_type":"public","date":"2025-01-24","topics":["concurrency","build","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-127-crash-on-latest-dev-build"></a>
# EndstoneMC/endstone #127: Crash on latest dev build {#endstonemc-endstone-127-crash-on-latest-dev-build}

Source: https://github.com/EndstoneMC/endstone/issues/127

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat’s dev175 startup crash improves in a later build, but dev193 /reload crashes in reloadData. Wu supplies 12767cf5585bdaf2ff049b4a17acccce30f746f5 and asks broader retesting. pgrd1 separately reports Linux Python-call crashes; wu suspects corrupted installation without reproducing, but reinstall/version changes do not fix them in the final report. JinHyone reports older stable broadcast crashes with ScriptAPI and multiple users; wu identifies that as #115’s already-fixed case. Preserve these separate branches: startup improvement, linked reload fix, old-version duplicate and unresolved Linux evidence. Closed metadata does not turn the contradicted Python-installation hypothesis into fact.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/127
- https://github.com/EndstoneMC/endstone/issues/127#issuecomment-2613576171
- https://github.com/EndstoneMC/endstone/issues/127#issuecomment-2613728969
- https://github.com/EndstoneMC/endstone/issues/127#issuecomment-2613800040
- https://github.com/EndstoneMC/endstone/issues/127#issuecomment-2613991561
- https://github.com/EndstoneMC/endstone/issues/127#issuecomment-2614520882
- https://github.com/EndstoneMC/endstone/issues/127#issuecomment-2617244903
- https://github.com/EndstoneMC/endstone/issues/127#issuecomment-2618091498
- https://github.com/EndstoneMC/endstone/issues/127#issuecomment-2626281155
- https://github.com/EndstoneMC/endstone/issues/127#issuecomment-2626875233
- https://github.com/EndstoneMC/endstone/issues/127#issuecomment-2629467066
- https://github.com/EndstoneMC/endstone/commit/12767cf5585bdaf2ff049b4a17acccce30f746f5
