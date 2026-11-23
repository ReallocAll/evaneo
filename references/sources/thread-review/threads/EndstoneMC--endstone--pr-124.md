<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:124"],"source_type":"public","date":"2025-01-12","topics":["build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-124-add-missing-include-in-cmake"></a>
# EndstoneMC/endstone #124: add missing 'include' in cmake {#endstonemc-endstone-124-add-missing-include-in-cmake}

Source: https://github.com/EndstoneMC/endstone/pull/124

## Review scope and state {#review-scope-and-state}

- Thread author: kaniteru; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (2 additions, 0 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

kaniteru adds include(FetchContent) before the module’s functions are called. Wu thanks them; merged two-line fix inspected. It makes the CMake file’s module dependency explicit.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/124
- https://github.com/EndstoneMC/endstone/pull/124#issuecomment-2585727677
