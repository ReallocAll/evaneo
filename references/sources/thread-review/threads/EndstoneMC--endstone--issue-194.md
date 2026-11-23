<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:194"],"source_type":"public","date":"2025-06-08","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-194-bug-behavior-pack-custom-command-integration"></a>
# EndstoneMC/endstone #194: [bug] Behavior Pack Custom Command integration {#endstonemc-endstone-194-bug-behavior-pack-custom-command-integration}

Source: https://github.com/EndstoneMC/endstone/issues/194

## Review scope and state {#review-scope-and-state}

- Thread author: ForestOfLight; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

ForestOfLight reports behavior-pack custom commands absent from autocomplete and execution on 0.8.1. Wu says>=0.8.1 should work, requests a minimal reproduction, and supplies a Script API startup callback registering test:log with Any permission and Success result. Reporter later says it works without identifying the original cause. The example supports the intended integration path from 180, but neither a new fix nor a concrete root cause is established here.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/194
- https://github.com/EndstoneMC/endstone/issues/194#issuecomment-2955911839
- https://github.com/EndstoneMC/endstone/issues/194#issuecomment-2993481816
