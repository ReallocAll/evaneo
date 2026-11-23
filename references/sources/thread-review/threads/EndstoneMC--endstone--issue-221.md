<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:221"],"source_type":"public","date":"2025-07-20","topics":["concurrency","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-221-bug-error-while-importing-form-button-class-in-python-api"></a>
# EndstoneMC/endstone #221: [bug] Error while importing Form.Button class in Python API {#endstonemc-endstone-221-bug-error-while-importing-form-button-class-in-python-api}

Source: https://github.com/EndstoneMC/endstone/issues/221

## Review scope and state {#review-scope-and-state}

- Thread author: cenk; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

cenk cannot import Button directly from endstone.form. Wu explains historical nesting under ActionForm because only that form supported buttons, and promises a binding refactor exposing Button at module level. The term subclass in the conversation describes nesting here and should not be read as evidence of inheritance from ActionForm. No implementation link or retest appears; the future flattening is a plan motivated by API discoverability/expanded controls.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/221
- https://github.com/EndstoneMC/endstone/issues/221#issuecomment-3095941059
