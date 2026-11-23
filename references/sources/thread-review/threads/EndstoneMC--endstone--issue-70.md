<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:70"],"source_type":"public","date":"2024-10-02","topics":["concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-70-endstone-crashed-on-linux"></a>
# EndstoneMC/endstone #70: Endstone crashed on Linux {#endstonemc-endstone-70-endstone-crashed-on-linux}

Source: https://github.com/EndstoneMC/endstone/issues/70

## Review scope and state {#review-scope-and-state}

- Thread author: batemandev; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

batemandev reports an unreproducible Linux crash with only a /me-disabling plugin and an image-only trace. Wu attributes it to BDS container closing after inspecting the trace. This is an attributed diagnosis, not independently verified here because the image has not been inspected. No fix or reproducible steps are present.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/70
- https://github.com/EndstoneMC/endstone/issues/70#issuecomment-2388423216
