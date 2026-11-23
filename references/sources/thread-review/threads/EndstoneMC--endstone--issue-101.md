<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:101"],"source_type":"public","date":"2024-12-06","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-101-unknown-error-log"></a>
# EndstoneMC/endstone #101: Unknown Error Log {#endstonemc-endstone-101-unknown-error-log}

Source: https://github.com/EndstoneMC/endstone/issues/101

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat reports repeated boundary-access errors during join-time cinematic camera/teleport, without reliable reproduction. All repeated traces show EndstoneBlock::checkState → at → GameMode::useItemOn for the same coordinates. Wu asks version and says fixed since 0.5.6.dev70. No reporter confirmation or exact fix appears. Do not infer the coordinates are genuinely outside the physical world; #102 suggests broken BlockSource context as a related hypothesis.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/101
- https://github.com/EndstoneMC/endstone/issues/101#issuecomment-2522264524
