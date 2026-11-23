<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:230"],"source_type":"public","date":"2025-07-26","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-230-bug-causes-argument-to-get-cut-short"></a>
# EndstoneMC/endstone #230: [bug] "=" causes argument to get cut short {#endstonemc-endstone-230-bug-causes-argument-to-get-cut-short}

Source: https://github.com/EndstoneMC/endstone/issues/230

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat's player argument truncates selectors at '=' on 0.9.5.dev99, blocking plugin-side target-filter parsing. Wu says it should be fixed in the latest dev build, without code link or reporter retest. Preserve the intended requirement to retain the full selector expression; this thread does not establish a built-in selector evaluator or a verified parser mechanism.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/230
- https://github.com/EndstoneMC/endstone/issues/230#issuecomment-3127766981
