<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:251"],"source_type":"public","date":"2025-08-20","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-251-bug-message-argument-fails-with-ending-number"></a>
# EndstoneMC/endstone #251: [bug] message argument fails with ending number {#endstonemc-endstone-251-bug-message-argument-fails-with-ending-number}

Source: https://github.com/EndstoneMC/endstone/issues/251

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat reports message arguments ending in digits failing, but Wu supplies successful title/ban counterexamples and reporter cannot reproduce on retest and closes. No defect or fix is established here. Later 255 finds a command-registry poisoning cause for a similar symptom; that later evidence should be cross-referenced rather than retroactively claiming this withdrawn report was independently reproduced.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/251
- https://github.com/EndstoneMC/endstone/issues/251#issuecomment-3220342780
- https://github.com/EndstoneMC/endstone/issues/251#issuecomment-3220888892
- https://github.com/EndstoneMC/endstone/issues/251#issuecomment-3220933519
