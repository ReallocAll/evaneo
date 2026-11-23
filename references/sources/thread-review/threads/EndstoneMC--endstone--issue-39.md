<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:39"],"source_type":"public","date":"2024-08-28","topics":["concurrency","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-39-feature-error-handling-related"></a>
# EndstoneMC/endstone #39: [feature]Error handling related {#endstonemc-endstone-39-feature-error-handling-related}

Source: https://github.com/EndstoneMC/endstone/issues/39

## Review scope and state {#review-scope-and-state}

- Thread author: wuliao697; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

wuliao697 dereferences getPlayer(name) before getting UUID and tries to catch runtime_error when the player is absent. Wu explains missing players return null, so dereferencing crashes and must be guarded first. The distinction is API absence-as-null versus a thrown C++ exception; catching runtime_error cannot repair invalid dereference. The supplied command also checks argument count, so the concrete missing guard is the returned player pointer, not merely argument validation. No API redesign is proposed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/39
- https://github.com/EndstoneMC/endstone/issues/39#issuecomment-2314345391
