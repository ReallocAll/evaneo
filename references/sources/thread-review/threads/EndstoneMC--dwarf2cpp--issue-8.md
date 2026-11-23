<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/dwarf2cpp:8"],"source_type":"public","date":"2025-09-15","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-dwarf2cpp-8-template-declaration-should-appear-once-in-a-file"></a>
# EndstoneMC/dwarf2cpp #8: Template declaration should appear once in a file {#endstonemc-dwarf2cpp-8-template-declaration-should-appear-once-in-a-file}

Source: https://github.com/EndstoneMC/dwarf2cpp/issues/8

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu explains that emitting a primary template declaration before every explicit specialization causes repeated declarations in the same file. The example has two ComponentOperations specializations; only the first needs the template<typename T> struct ComponentOperations forward declaration. The requirement is file-level declaration deduplication while keeping all specializations. This does not imply that all repeated declarations in C++ are illegal; the thread requests cleaner reconstruction. No chosen tracking data structure or patch is present.



## Source index {#source-index}

- https://github.com/EndstoneMC/dwarf2cpp/issues/8
