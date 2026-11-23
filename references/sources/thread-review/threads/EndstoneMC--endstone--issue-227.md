<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:227"],"source_type":"public","date":"2025-07-24","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-227-bug-resource-pack-loading-bugs"></a>
# EndstoneMC/endstone #227: [bug] resource pack loading bugs {#endstonemc-endstone-227-bug-resource-pack-loading-bugs}

Source: https://github.com/EndstoneMC/endstone/issues/227

## Review scope and state {#review-scope-and-state}

- Thread author: JinHyone; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

JinHyone reports resource-pack loading hanging for multiple clients under Endstone but succeeding with the same world's native BDS executable. Wu cannot reproduce and speculates a client bug. The reporter's differential observation must be retained rather than discarded by that speculation; no minimal pack, independently inspected attachment, root cause, or fix exists.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/227
- https://github.com/EndstoneMC/endstone/issues/227#issuecomment-3263891755
