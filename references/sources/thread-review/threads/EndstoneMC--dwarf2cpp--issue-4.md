<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/dwarf2cpp:4"],"source_type":"public","date":"2025-09-13","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-dwarf2cpp-4-fix-special-types-array-type-pointer-to-function-type-with-names"></a>
# EndstoneMC/dwarf2cpp #4: Fix special types (array type, pointer to function type) with names {#endstonemc-dwarf2cpp-4-fix-special-types-array-type-pointer-to-function-type-with-names}

Source: https://github.com/EndstoneMC/dwarf2cpp/issues/4

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu supplies two concrete declarator counterexamples. An array name/dimension must remain attached to the declaration after the identity<char>::type type expression; inserting the whole named array inside the template argument produces the wrong C++ declaration. A function-pointer name belongs inside (*del), before its argument list, rather than after an abstract pointer type. These examples require declarator-aware rendering rather than concatenating a type string and identifier. Closed state does not identify the parser/printer change or a regression test.



## Source index {#source-index}

- https://github.com/EndstoneMC/dwarf2cpp/issues/4
