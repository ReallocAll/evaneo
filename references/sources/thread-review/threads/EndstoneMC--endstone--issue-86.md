<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:86"],"source_type":"public","date":"2024-11-02","topics":["concurrency","build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-86-it-s-not-working-in-arm64-debian"></a>
# EndstoneMC/endstone #86: it's not working in arm64 debian {#endstonemc-endstone-86-it-s-not-working-in-arm64-debian}

Source: https://github.com/EndstoneMC/endstone/issues/86

## Review scope and state {#review-scope-and-state}

- Thread author: Xwens-e; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Xwens-e shows an ARM64 source-wheel build failing during CMake generator setup. Wu identifies a deeper platform constraint: no ARM64 BDS binary. Fixing Ninja alone therefore would not produce a supported native runtime. This is a dependency-platform boundary rather than a universal claim about compiler feasibility or emulation.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/86
- https://github.com/EndstoneMC/endstone/issues/86#issuecomment-2453006602
