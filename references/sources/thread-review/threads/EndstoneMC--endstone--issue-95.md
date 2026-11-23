<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:95"],"source_type":"public","date":"2024-11-28","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-95-feature-hooking"></a>
# EndstoneMC/endstone #95: [feature] hooking {#endstonemc-endstone-95-feature-hooking}

Source: https://github.com/EndstoneMC/endstone/issues/95

## Review scope and state {#review-scope-and-state}

- Thread author: yurasulima; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

yurasulima requests public hooks/documentation as an escape hatch while high-level features mature. Wu declines because the project aims to shield users from risky, version-fragile, nonportable hooks requiring reverse engineering. He still allows C++ consumers to choose external hook libraries. This is a boundary on supported abstraction/maintenance responsibility, not a ban on advanced extensions or a claim Endstone itself avoids hooks.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/95
- https://github.com/EndstoneMC/endstone/issues/95#issuecomment-2552392841
