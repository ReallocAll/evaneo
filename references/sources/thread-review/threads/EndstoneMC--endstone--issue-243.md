<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:243"],"source_type":"public","date":"2025-08-09","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-243-drop-item-error"></a>
# EndstoneMC/endstone #243: Drop Item error {#endstonemc-endstone-243-drop-item-error}

Source: https://github.com/EndstoneMC/endstone/issues/243

## Review scope and state {#review-scope-and-state}

- Thread author: Arduinonk; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Arduinonk calls dimension.drop_item during quit on 0.10.3 and gets AttributeError. Wu explains the method is not in API 0.10 and is planned for 0.11. This is a runtime/documentation-version mismatch, not evidence that the shown drop loop was executed successfully or that item loss on quit is safe. No patch or later retest here.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/243
- https://github.com/EndstoneMC/endstone/issues/243#issuecomment-3171890229
- https://github.com/EndstoneMC/endstone/issues/243#issuecomment-3172574641
