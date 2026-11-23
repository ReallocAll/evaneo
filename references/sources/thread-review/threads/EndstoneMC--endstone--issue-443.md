<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:443"],"source_type":"public","date":"2026-07-22","topics":["testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-443-nbt-serialization-crash"></a>
# EndstoneMC/endstone #443: NBT serialization crash {#endstonemc-endstone-443-nbt-serialization-crash}

Source: https://github.com/EndstoneMC/endstone/issues/443

## Evidence and attribution {#evidence-and-attribution}

Primary author: SuperAnse. Created 2026-07-22T14:55:45Z; recorded state closed; merged not applicable.

The reporter's held firework-star NBT string conversion crashes through unsigned-byte ArrayTag formatting, nested CompoundTag formatting, pybind11 and a form handler. The complete 120-frame trace was read; repeating every frame adds no causal information. Wu points to b29755099 for the next release. The same correction as #432 removes empty-array indexing and formats all elements via a separator; zero-length tags explain why an unrelated-looking item triggers it. The pasted illustrative snippet has a syntax omission, so it was not treated as executable reproduction.

## Code and verification boundary {#code-and-verification-boundary}

Inspected full b29755099098dd477606bb3c8662e9b18b76370f while reviewing #432: range iteration replaces indexing, and C++/Python empty, singleton and multi-element array tests are added. See pull_request-432 dossier. Attachment data itself was not opened. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/443
- https://github.com/EndstoneMC/endstone/issues/443#issuecomment-5078818079
