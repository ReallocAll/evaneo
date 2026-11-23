<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:204"],"source_type":"public","date":"2025-06-17","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-204-answer-to-latest-v0-9-0-question-that-was-already-closed"></a>
# EndstoneMC/endstone #204: Answer to latest v0.9.0 question (that was already closed) {#endstonemc-endstone-204-answer-to-latest-v0-9-0-question-that-was-already-closed}

Source: https://github.com/EndstoneMC/endstone/issues/204

## Review scope and state {#review-scope-and-state}

- Thread author: St0rmyMindbender; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Follow-up to 203: St0rmyMindbender recognizes host version selection/auto-update as the controllable integration point and plans to ask the host. Wu explains initial new-version support uses the final BDS preview and reports extensive production-readiness testing, while recommending disable auto-updates and pin a known version for predictable operation. He cannot reproduce world loss and suggests another cause. Treat the test/readiness statement as maintainer-reported, not an independent guarantee; neither thread establishes data-deletion root cause. The practical resolution separates rapid compatibility availability from operator-controlled adoption.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/204
- https://github.com/EndstoneMC/endstone/issues/204#issuecomment-2982184755
