<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:368"],"source_type":"public","date":"2026-04-07","topics":["ffi","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-368-feat-support-custom-python-events-with-optional-cancellation"></a>
# EndstoneMC/endstone #368: feat: support custom Python events with optional cancellation {#endstonemc-endstone-368-feat-support-custom-python-events-with-optional-cancellation}

Source: https://github.com/EndstoneMC/endstone/pull/368

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-04-07T16:27:42Z; recorded state closed; merged True.

## Problem, design and limits {#problem-design-and-limits}

Python custom events need a pybind trampoline and optional cancellation independent of C++ template inheritance. The proposal uses PyEvent plus pure-Python Cancellable mixin, module.qualname names for custom events to avoid collisions, short built-in names, and a private virtual Event::isCancelled for common dispatch. PyEvent bridges cancellation through _cancelled and checks mixin membership. Deprecated cancelled is removed in favor of is_cancelled. Tests are proposed for construction, async state, cancellation/reset and priority/ignore_cancelled dispatch; all plan boxes remain unchecked. The body discloses Claude Code generation, which is provenance, not proof of human authorship of every rationale or successful validation.

## Direct patch findings {#direct-patch-findings}

Final patch adds pure-Python Cancellable backed by getattr(_cancelled, False), setter and cancel(); removes deprecated cancelled from stubs/native bindings. PyEvent derives Event/ICancellable, acquires the GIL for Python name/cancellation access, and uses isinstance with the mixin to report cancellability. The private virtual Event::isCancelled default is false; existing native Cancellable template overrides it (exact-head cancellable.h also inspected), so dispatch unifies native/custom events. Built-in registration uses class __name__, custom registration module.qualname; PyEvent uses qualname for built-in names, a nested-built-in corner not tested. Python tests cover custom naming, async flag, default/reset cancellation, identity, priority and ignore_cancelled delivery. They are committed test definitions, not executed evidence. Remaining diff includes mechanical registry/NBT/mock-plugin formatting.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (20510 characters; SHA-256 2e24fa5e4c52998d1b8997cd986b350df1a976c3bb00560e33fbd4e497f84708), head 016d34183bccba43c0969b841e0bb15f467fd53a. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/368
