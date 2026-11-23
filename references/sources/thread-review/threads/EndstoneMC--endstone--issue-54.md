<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:54"],"source_type":"public","date":"2024-09-15","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-54-feature-add-support-for-python-3-13"></a>
# EndstoneMC/endstone #54: [feature] Add support for Python 3.13 {#endstonemc-endstone-54-feature-add-support-for-python-3-13}

Source: https://github.com/EndstoneMC/endstone/issues/54

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu requests adding Python 3.13 to workflows before its release while retaining previously supported versions, and links completion 84c80eaadb7d92cce2f3b8b6d7e94aecba1ed863. The substantive constraint is additive compatibility coverage, not replacing the support matrix. Dates are historical proposal text, not current release guidance. smartcmd contributes only an emoji.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/54
- https://github.com/EndstoneMC/endstone/issues/54#issuecomment-2352613141
- https://github.com/EndstoneMC/endstone/issues/54#issuecomment-2352618377
- https://github.com/EndstoneMC/endstone/commit/84c80eaadb7d92cce2f3b8b6d7e94aecba1ed863
