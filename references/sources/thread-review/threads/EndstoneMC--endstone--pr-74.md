<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:74"],"source_type":"public","date":"2024-10-11","topics":["review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-74-feat-dump-default-state-for-each-block-type"></a>
# EndstoneMC/endstone #74: feat: dump default state for each block type {#endstonemc-endstone-74-feat-dump-default-state-for-each-block-type}

Source: https://github.com/EndstoneMC/endstone/pull/74

## Review scope and state {#review-scope-and-state}

- Thread author: smartcmd; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (1 additions, 0 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

smartcmd’s merged one-line export adds defaultBlockStateHash from block_legacy.getDefaultState()->getRuntimeId(). Wu thanks them; no design reasoning is given. This links each block type to its default state in the existing exported ID space. The field name says hash while the called API says runtime ID; stability/collision semantics are not proved by this patch. Codecov is not evidence for semantic stability.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/74
- https://github.com/EndstoneMC/endstone/pull/74#issuecomment-2406657798
- https://github.com/EndstoneMC/endstone/pull/74#issuecomment-2407119510
- https://github.com/EndstoneMC/endstone/pull/74#issuecomment-2407164208
