<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:360"],"source_type":"public","date":"2026-04-06","topics":["testing","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-360-refactor-replace-string-based-registry-lookup-with-std-typeindex"></a>
# EndstoneMC/endstone #360: refactor: replace string-based registry lookup with std::type_index {#endstonemc-endstone-360-refactor-replace-string-based-registry-lookup-with-std-typeindex}

Source: https://github.com/EndstoneMC/endstone/pull/360

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-04-06T14:34:26Z; recorded state closed; merged True.

## Problem, design and limits {#problem-design-and-limits}

Replace registry-name strings with std::type_index(typeid(T)), remove per-type naming macro/RegistryType, bridge typed Registry<T> through type-erased IRegistry virtuals, and expose one opaque Python Registry instead of generated per-type bindings. Python get_registry extracts std::type_info from py::type, removing a fold-expression dispatch list. This confines type erasure to the binding boundary and removes string drift/registration boilerplate. Build and integration checklist remains unchecked; the complete patch was subsequently inspected below, with no test execution.

## Direct patch findings {#direct-patch-findings}

Replaces string keys/macros with std::type_index/typeid registry lookup; type-erased get0/forEach0/type_info support one Python PyRegistry facade and __len__. Python obtains pybind type metadata, casts references without ownership, and materializes iteration as list. C++getRegistry blindly dereferences missing lookup, while Python returns None for unsupported type. Critically the captured head contains literal ``}; in actor_type.h; verified with git show exact8f69bd2f, so this snapshot is syntactically invalid despite merged flag. The merge commit b71df7c also contains the literal backticks in actor_type.h, independently checked with git show. Thus the defect is present in both captured head and merged tree; a later corrective commit has not been traced here.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (14073 characters; SHA-256 aa9bafb62050a8b8fe83d45e09cd92740c6f5ee7ce04a27deca88e455f27cbdd), head 8f69bd2f1768e3418e2a390ef0353a9752362f78. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/360
