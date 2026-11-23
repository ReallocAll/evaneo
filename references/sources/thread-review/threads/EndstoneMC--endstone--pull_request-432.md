<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:432"],"source_type":"public","date":"2026-07-15","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-432-fix-nbt-handle-empty-bytearraytag-in-std-formatter"></a>
# EndstoneMC/endstone #432: fix(nbt): handle empty ByteArrayTag in std::formatter {#endstonemc-endstone-432-fix-nbt-handle-empty-bytearraytag-in-std-formatter}

Source: https://github.com/EndstoneMC/endstone/pull/432

## Evidence and attribution {#evidence-and-attribution}

Primary author: killcerr. Created 2026-07-15T16:38:33Z; recorded state closed; merged False.

## Original correction and final revision {#original-correction-and-final-revision}

killcerr's unmerged patch for #443 guards begin()!=end() before formatting the first byte, casts byte values to int, and captures each format_to return iterator. wu-vincent replaced it with commit b29755099 to avoid duplicating first/subsequent element formatting.

The final loop starts with an empty separator, formats separator+value+b for every element, then changes separator to comma and emits the closing bracket. Empty input naturally produces [B;]. Added C++ and Python checks cover empty, singleton and multiple byte arrays and empty/multiple int arrays.

Credit killcerr for identifying the empty-range defect and wu-vincent for the unified loop/tests. Tests were inspected, not run. Prefer loops whose zero-iteration behavior is already correct to special-casing an unchecked first element.

## Code and verification boundary {#code-and-verification-boundary}

Inspected the complete original 699-character diff and full final commit b29755099098dd477606bb3c8662e9b18b76370f including C++/Python tests. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/432
- https://github.com/EndstoneMC/endstone/pull/432#issuecomment-5078817820
