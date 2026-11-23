<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:117"],"source_type":"public","date":"2025-01-01","topics":["concurrency","build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-117-build-issue"></a>
# EndstoneMC/endstone #117: Build Issue {#endstonemc-endstone-117-build-issue}

Source: https://github.com/EndstoneMC/endstone/issues/117

## Review scope and state {#review-scope-and-state}

- Thread author: ThePhoenixFox; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

ThePhoenixFox’s Raspberry Pi install selects an old source archive, fails on missing CMakePresets, then local building hits PlayerDeathManager size 136 versus expected 128. Wu explains supported amd64 wheels normally avoid builds; unsupported architecture falls back to source, but BDS has no corresponding architecture. The aarch64 wheel in the log contradicts the ambiguous PI OS x64 label. ABI static assertions are useful fail-fast evidence, not checks to disable to force a build.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/117
- https://github.com/EndstoneMC/endstone/issues/117#issuecomment-2568312343
- https://github.com/EndstoneMC/endstone/issues/117#issuecomment-2568512499
