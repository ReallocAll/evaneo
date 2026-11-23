<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:165"],"source_type":"public","date":"2025-03-24","topics":["concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-165-bug-crash-on-reload"></a>
# EndstoneMC/endstone #165: [bug] Crash on reload {#endstonemc-endstone-165-bug-crash-on-reload}

Source: https://github.com/EndstoneMC/endstone/issues/165

## Review scope and state {#review-scope-and-state}

- Thread author: SuperEric1; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

SuperEric1 reports reload crashes with a Python plugin and addon on Linux 0.6.2, noting similar historical Windows symptoms. Wu closes this as duplicate 156 and says the scripting API event-handler hooking strategy will change to fix the common root cause. The stack reaches reloadData from full reload, but the private addon and exact cause are unavailable; duplicate classification is the maintainer's assessment. Issue156 later reports a 0.7.0 fix. Do not conflate this with issue 144's separate direct-reload listener-lifecycle patch or claim the reporter validated a repair here.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/165
- https://github.com/EndstoneMC/endstone/issues/165#issuecomment-2749647511
