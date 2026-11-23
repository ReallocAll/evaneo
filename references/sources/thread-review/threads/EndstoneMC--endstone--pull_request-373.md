<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:373"],"source_type":"public","date":"2026-04-09","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-373-feat-add-identifier-type-for-python-bindings"></a>
# EndstoneMC/endstone #373: feat: add Identifier type for Python bindings {#endstonemc-endstone-373-feat-add-identifier-type-for-python-bindings}

Source: https://github.com/EndstoneMC/endstone/pull/373

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-04-09T23:10:48Z; recorded state closed; merged True.

## Problem, design and limits {#problem-design-and-limits}

Identifier<T> was flattened to Python str, losing namespace/key structure and static domain distinctions. PyIdentifier exposes structured fields and generic Identifier[T] stubs, accepts strings for compatibility, compares to str, and requires nonempty namespace/key. __str__ on registry objects must return str rather than the newly wrapped identifier. The body claims type checkers can distinguish DimensionId from ActorTypeId; this is static typing, not necessarily runtime parameter enforcement. Build, integration and stub regeneration plans are unchecked; breaking output-type implications deserve inspection.

## Direct patch findings {#direct-patch-findings}

PyIdentifier owns namespace/key strings, splits at the last colon and supplies defaultminecraft; empty explicit components are rejected, but arbitrary characters/multiple-colon namespace are allowed. Runtime generic subscription returns the same class for everyT, so cross-domain IDs are accepted at runtime. Its hash uses Python's hash(str) consistently with canonical-string equality. Type caster owns temporary storage_ so nonowning C++Identifier string_views remain valid for the call, accepts strings and PyIdentifier, and returns owning wrapper. Exact-head include/endstone/identifier.h confirms nonowning views and no constructor validation: plain-string argument path can still accept empty components that explicit PyIdentifier rejects. New BlockType/ItemType hashes use C++combined component hashes while equality with Python strings remains, so cross-type equal/hash consistency is a risk distinct from correctly implemented PyIdentifier hashing. Stub generator tracks nested class ownership by indentation, but bare-constant regex only allows word/dot halves and one colon; multi-colon potion identifiers/hyphenated IDs need coverage. Runtime two-argument constructor is absent from custom replacementstub. Tests only change existing registry constant discovery fromstr→Identifier; no new constructor/hash/domain/stub regression tests are added. Captured diff also changes declaredMinecraftversion26.12→26.20.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (59203 characters; SHA-256 6627d8195e821067b80a9b8885e10e389563273f1a67ed128dc9ad963212643d), head 8f54f64cd5d83718265d03a11c22ac455c520fca. For47 also inspected exact-head include/endstone/identifier.h. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/373
