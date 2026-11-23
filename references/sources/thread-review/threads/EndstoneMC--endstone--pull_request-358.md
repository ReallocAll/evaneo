<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:358"],"source_type":"public","date":"2026-04-06","topics":["ffi","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-358-feat-introduce-actortype-registry"></a>
# EndstoneMC/endstone #358: feat: introduce ActorType registry {#endstonemc-endstone-358-feat-introduce-actortype-registry}

Source: https://github.com/EndstoneMC/endstone/pull/358

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-04-06T12:32:32Z; recorded state closed; merged True.

## Problem, design and limits {#problem-design-and-limits}

ActorType becomes a registry-backed CRTP type with 150+ C++/Python constants, replacing an unscalable actor enum-style surface. The body supplies only scope and an unchecked build/runtime registry test plan. No measured outcome or collaborator reasoning appears. Generated constants should not be counted as independent decisions; inspect registry mechanics separately.

## Direct patch findings {#direct-patch-findings}

Registry population reads ActorFactory's native factory-function map at level initialization, owns each canonical string in EndstoneActorType, and stores entries in an owning std::string cache (verified exact-head core/registry.h); it is not limited to the exported constant list. Actor::getType now resolves canonical ID with getOrThrow; spawnActor takes typed ID and converts to the native definition identifier. Translation keys use entity.<key>.name, discarding namespace. Python gets reference-returned types, static identifier constants, equality/hash, a real iterator over reference-cast cached entries and len. Registry size currently constructs the identifiers vector, O(n) allocation per call. Tests cover repeated object identity, invalid None/KeyError, nonempty iteration, exported constants resolving, all actor-registry entries having constants and existing item/enchantment attributes. The exhaustive constant test assumes vanilla inventory and would reject extra custom types despite dynamic registry population. Unrelated material changes widen native command enum values/maps to64bit and disable Windows intentional-shutdown crash-output suppression; this is broader than an ActorType-only refactor. No test execution is independently verified.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (65216 characters; SHA-256 10ca42bb325a21e2afec18e728f20ed4fbac5d8fdfbd19e38bee4d6e0a6d3f4b), head cdcba6b9daf91b9fb8e8072c31ec7d6e985fb12d. For40 also verified exact-head src/endstone/core/registry.h cache ownership. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/358
