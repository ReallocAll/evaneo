<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:136"],"source_type":"public","date":"2025-02-20","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-136-bug-unknown-error-in-0-6-0"></a>
# EndstoneMC/endstone #136: [bug] Unknown error in 0.6.0 {#endstonemc-endstone-136-bug-unknown-error-in-0-6-0}

Source: https://github.com/EndstoneMC/endstone/issues/136

## Review scope and state {#review-scope-and-state}

- Thread author: JinHyone; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

JinHyone’s 0.6.0 trace matches proxied permission checking in #135 but they explicitly say no execute-as command was used. Wu requests latest dev build and reporter confirms resolution. This broadens the trigger beyond explicit execute-as; the shared stack and common fix support linkage without claiming an identical user action.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/136
- https://github.com/EndstoneMC/endstone/issues/136#issuecomment-2670898906
- https://github.com/EndstoneMC/endstone/issues/136#issuecomment-2671174206
- https://github.com/EndstoneMC/endstone/issues/136#issuecomment-2671176774
- https://github.com/EndstoneMC/endstone/issues/136#issuecomment-2671274173
- https://github.com/EndstoneMC/endstone/issues/136#issuecomment-2671345299
- https://github.com/EndstoneMC/endstone/issues/136#issuecomment-2671381761
- https://github.com/EndstoneMC/endstone/issues/136#issuecomment-2671878977
