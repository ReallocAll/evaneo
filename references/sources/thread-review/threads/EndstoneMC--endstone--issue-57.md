<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:57"],"source_type":"public","date":"2024-09-17","topics":["concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-57-feature-save-the-world-when-on-server-crash"></a>
# EndstoneMC/endstone #57: [feature] Save the world when on server crash {#endstonemc-endstone-57-feature-save-the-world-when-on-server-crash}

Source: https://github.com/EndstoneMC/endstone/issues/57

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu proposes saving at crash time to limit unsaved progress; alternatives are more frequent automatic saves and manual saves, both leaving gaps. LeviLamina is mentioned as prior art. No code, feasibility result or safety discussion follows, only thanks/stale closures. Therefore retain the desired outcome and alternatives as a proposal; do not teach crash-handler saving as established safe practice. Thread text does not address corrupted state, lock ownership or signal-safe I/O, all important unresolved constraints before implementation.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/57
- https://github.com/EndstoneMC/endstone/issues/57#issuecomment-2356935782
- https://github.com/EndstoneMC/endstone/issues/57#issuecomment-2423230582
- https://github.com/EndstoneMC/endstone/issues/57#issuecomment-2438838456
- https://github.com/EndstoneMC/endstone/issues/57#issuecomment-2563098865
- https://github.com/EndstoneMC/endstone/issues/57#issuecomment-2584181000
