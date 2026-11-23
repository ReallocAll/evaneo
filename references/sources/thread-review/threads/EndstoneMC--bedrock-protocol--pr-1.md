<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/bedrock-protocol:1"],"source_type":"public","date":"2026-08-19","topics":["testing","build","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-bedrock-protocol-1-fix-the-gcc-and-clang-ci-jobs"></a>
# EndstoneMC/bedrock-protocol #1: Fix the GCC and Clang CI jobs {#endstonemc-bedrock-protocol-1-fix-the-gcc-and-clang-ci-jobs}

Source: https://github.com/EndstoneMC/bedrock-protocol/pull/1

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (93 additions, 24 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu separates two compiler portability failures from wire-format behavior. For GCC/libstdc++, a nested type with a default member initializer is not yet fully usable while its enclosing class is open; a variant instantiated there permanently acquires a deleted default constructor. The counterexample is earlier snapshot aliases, whose definitions are already complete, explaining why only ItemStackRequestCereal failed. The chosen layout emits nested definitions in an Owner_nested namespace first and exposes using aliases from Owner, retaining consumer spelling, reflection and serializer interfaces. cpp_type propagates nested_of through optional, repeated, array, map, variant and conditional field types; sibling references become bare names until Owner exists. Schema nesting being one level deep is an explicit constraint, not a general proof for arbitrary nesting. For Clang/libc++, a fold over 348 packet IDs exceeds expression depth 256; expanding into bool arrays and looping changes compile-time expression shape without changing the intended count/all-agree results. The merged patch matches 93 additions/24 deletions. Reported checks are 320 clang-cl tests, 104 compiler tests with 7 pre-existing failures, clean ruff/mypy and an endweave rebuild; Linux GCC/Clang were explicitly not locally reproduced. The body discloses AI generation. Do not convert these reported Windows checks into independent cross-platform validation.



## Source index {#source-index}

- https://github.com/EndstoneMC/bedrock-protocol/pull/1
