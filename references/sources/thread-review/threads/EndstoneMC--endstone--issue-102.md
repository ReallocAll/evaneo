<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:102"],"source_type":"public","date":"2024-12-06","topics":["concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-102-custom-block-caused-crash"></a>
# EndstoneMC/endstone #102: Custom Block Caused Crash? {#endstonemc-endstone-102-custom-block-caused-crash}

Source: https://github.com/EndstoneMC/endstone/issues/102

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat’s 0.5.6.dev69 trace shows string copy in Dimension::getEndstoneDimension during Item placement. Wu tentatively links broken BlockSource and asks to retest dev70+. The version precedes the claimed fix, but no response confirms recovery. This is a contextual-object diagnostic hypothesis, not proof a custom block definition itself is invalid.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/102
- https://github.com/EndstoneMC/endstone/issues/102#issuecomment-2522270605
