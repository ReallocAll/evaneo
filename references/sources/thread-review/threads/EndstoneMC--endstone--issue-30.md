<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:30"],"source_type":"public","date":"2024-07-31","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-30-feature-endstone-should-remove-quotes-from-selector-parameters"></a>
# EndstoneMC/endstone #30: [feature] Endstone should remove quotes from selector parameters {#endstonemc-endstone-30-feature-endstone-should-remove-quotes-from-selector-parameters}

Source: https://github.com/EndstoneMC/endstone/issues/30

## Review scope and state {#review-scope-and-state}

- Thread author: killcerr; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu declines blanket quote stripping because string quotes can be intentional. Selector player/actor quotes represent escaping, while ordinary strings remain plugin responsibility. Linked patch 6c8ec8d716e48d66ec0ba6156388324610f0a565 was read: removeQuotes strips only paired outer quotes when length is at least two, applied to HardNonTerminal::Id tokens during parse-tree reconstruction. Interior/unmatched quotes survive. The implementation is narrower than removing every quote; no test result appears.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/30
- https://github.com/EndstoneMC/endstone/issues/30#issuecomment-2260700824
- https://github.com/EndstoneMC/endstone/issues/30#issuecomment-2260947833
- https://github.com/EndstoneMC/endstone/commit/6c8ec8d716e48d66ec0ba6156388324610f0a565
