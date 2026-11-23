<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:369"],"source_type":"public","date":"2026-04-07","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-369-fix-correct-type-annotations-for-plugin-and-eventhandler"></a>
# EndstoneMC/endstone #369: fix: correct type annotations for Plugin and event_handler {#endstonemc-endstone-369-fix-correct-type-annotations-for-plugin-and-eventhandler}

Source: https://github.com/EndstoneMC/endstone/pull/369

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-04-07T17:21:07Z; recorded state closed; merged True.

## Problem, design and limits {#problem-design-and-limits}

Plugin class variables inferred as bare None rejected subclass string values; event_handler's stub returned None, triggering mypy func-returns-value/untyped-decorator errors and downstream type ignores in endweave. The fix promises correct class-variable and decorator typing without forcing consumers to suppress diagnostics. Both decorator forms need validation. The plan is unchecked and body discloses Claude Code generation; exact generated versus hand-authored patch changes require inspection.

## Direct patch findings {#direct-patch-findings}

Full patch is broader than type annotations: adds runtime guards for absent asyncio loop, plugin description/server UUID, missing wheel name, missing entry-point distribution, and nonstring author metadata. Decorator overloads preserve arbitrary callable signature in both bare/factory forms; nullable callbacks and object comparison types repair stubs, vector in-place scalar overloads are added, metrics dictionaries/charts/futures annotated and many platform internals silenced with targeted ignores. Plugin runtime load/default_permission annotations are str|None while shipped stubs use enums, a discrepancy retained here. Stub generator injects decorator TypeVar. No static checker fixture or new test verifies the promised accepted/rejected consumer programs; changed custom-event test is formatting only. Runtime guard additions require behavioral consideration even though motivation is typing.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (42340 characters; SHA-256 d2bee8f129b5c4c8913db8d530b8c0729da6954e0c8ecfb827756925d9a0f75a), head f713d674705b8380c83d26f4d9f9d256d801556d. For47 also inspected exact-head include/endstone/identifier.h. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/369
