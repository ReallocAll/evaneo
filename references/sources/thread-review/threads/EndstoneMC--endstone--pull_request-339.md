<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:339"],"source_type":"public","date":"2026-02-27","topics":["lifetime","testing","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-339-fix-plugin-manager-reverse-destruction-order-of-loaders-to-fix-access"></a>
# EndstoneMC/endstone #339: fix(plugin-manager): reverse destruction order of loaders to fix access {#endstonemc-endstone-339-fix-plugin-manager-reverse-destruction-order-of-loaders-to-fix-access}

Source: https://github.com/EndstoneMC/endstone/pull/339

## Evidence and attribution {#evidence-and-attribution}

Primary author: engsr6982. Created 2026-02-27T14:54:09Z; recorded state closed; merged True.

## Failure, ownership and actual patch {#failure-ownership-and-actual-patch}

engsr6982 identified shutdown crashes when a native plugin registers a custom JS/Lua loader after built-in C++ and Python loaders. If the C++ loader unloads that plugin's dynamic library first, the custom loader's virtual destructor points into unloaded code. The author's general claim that vector always destroys forward should not be promoted to a portable C++ guarantee; the required invariant is explicit dependency-safe destruction order.

The complete patch adds an EndstonePluginManager destructor that pops loaders from the back, uses the same pop_back loop in clearPlugins instead of clear(), and disables plugins in reverse registration order. wu-vincent accepted it with LGTM; no tests or further objections are captured.

## Reusable decision and costs {#reusable-decision-and-costs}

Objects whose methods/destructors live inside a module must die before the owner unloads that module. Explicit LIFO cleanup can encode construction dependencies when registration order truly reflects dependency order. The patch does not prove arbitrary plugin dependency graphs are solved; clearPlugins still has a dependency-graph TODO.

## Code and verification boundary {#code-and-verification-boundary}

Inspected all 1,468 characters of the captured patch: manager destructor declaration/implementation, reverse disable traversal and reverse loader cleanup. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/339
- https://github.com/EndstoneMC/endstone/pull/339#issuecomment-3973480156
