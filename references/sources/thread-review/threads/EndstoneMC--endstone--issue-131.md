<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:131"],"source_type":"public","date":"2025-02-05","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-131-additional-spaces-in-massage-argument"></a>
# EndstoneMC/endstone #131: additional spaces in massage argument {#endstonemc-endstone-131-additional-spaces-in-massage-argument}

Source: https://github.com/EndstoneMC/endstone/issues/131

## Review scope and state {#review-scope-and-state}

- Thread author: Mih4n; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Mih4n shows message-token reconstruction inserts spaces into :hello: while prefixing another character avoids it. Wu confirms a fix in latest commit without a SHA. The important counterexample concerns punctuation/token boundary preservation rather than whitespace trimming globally. No actual parser revision is shown.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/131
- https://github.com/EndstoneMC/endstone/issues/131#issuecomment-2654571654
