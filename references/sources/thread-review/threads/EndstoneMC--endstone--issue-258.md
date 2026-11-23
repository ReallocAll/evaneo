<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:258"],"source_type":"public","date":"2025-08-27","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-258-feature-enforce-message-type-as-the-last-argument-when-registering-commands"></a>
# EndstoneMC/endstone #258: [feature] Enforce message type as the last argument when registering commands {#endstonemc-endstone-258-feature-enforce-message-type-as-the-last-argument-when-registering-commands}

Source: https://github.com/EndstoneMC/endstone/issues/258

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu turns 255's diagnosis into explicit registration requirements: message must be last; otherwise registration fails with a clear error/warning, because a malformed custom signature corrupts parsing for unrelated native/custom commands. Both checklist entries are marked done, but no patch or test result is linked in this issue. This is a precise boundary-validation requirement and author-reported completion, not independent implementation verification.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/258
