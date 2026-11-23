<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:509"],"source_type":"public","date":"2026-08-21","topics":["lifetime","ffi","testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-509-feat-command-add-a-brigadier-style-command-tree-api"></a>
# EndstoneMC/endstone #509: feat(command): add a Brigadier-style command tree API {#endstonemc-endstone-509-feat-command-add-a-brigadier-style-command-tree-api}

Source: https://github.com/EndstoneMC/endstone/pull/509

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-08-21T17:02:28Z; recorded state open; merged False.

## Typed commands remain a draft {#typed-commands-remain-a-draft}
Wu's open 0.13 proposal supplies C++ Brigadier-style nested builders and Python decorators, while retaining legacy usage strings/raw argument handlers. It addresses ambiguous overloads, repeated parsing and manual branch dispatch. Python annotations, Annotated metadata and defaulted optional parameters keep configuration separate from user parameter names; runtime builders remain possible.
Root-to-executable paths flatten into native overloads. Literal branches use single-value enums for client completion, allocator identity selects the execution branch, and indexed argument storage avoids dependence on parse arrival order. Optional middle arguments become separate overloads. ctx.get<T> reports available keys; permissions may show an error while requires predicates silently hide a branch, with updateCommands refreshing visibility. Mangled type-name tags plus virtual kind avoid std::any and cross-DSO dynamic_cast/RTTI identity failures on Linux. Selector arguments retain actual actors and require two symbols per platform.
The body records fixes to a temporary registerOverload object and a mistagged enum lookup. Block positions, positions, block states and integer ranges are explicitly unsupported; Python custom arguments, overload coalescing and shared backend work remain future. 353 C++ tests (21 new) and nine Python tests are claimed, but no live server test was performed. It is neither merged nor a validated retail-client grammar solution; #554 fixes current built-ins separately.

## Full implementation and constraints {#full-implementation-and-constraints}

All160042characters of the captured patch were inspected. Builders are shared handles, so copying/mutating either copy changes the same tree. Children merge solely by name, incoming handler wins, permissions accumulate as OR and requirements as AND; node kind/argument-type conflicts are not rejected. Flattening records every executable root-to-node path, rejects node cycles and direct greedy-message/raw-text children, and caps64overloads explicitly to limit each client's command-list bandwidth. Custom argument native-type cycles are not guarded, and greedy validation checks only direct kind, not a Custom→Message chain.

Registrar borrows native grammar, creates unique single-value enums for literals, dynamic suggestion sets for soft enums, and stable deque-owned parameter names. It validates all parameter shapes before command insertion, but creating enums during preparation already mutates registry and no rollback is shown for later failure. Capturing allocators bind each adapter to its exact overload; indexed custom storage is string or native selector rather than append-order token collection. Native selector200byte layout/default tests and two symbols per platform are added; results become actual actor/player handles and single-target cardinality is enforced. Type-erased results compare mangled type-name strings across modules, avoiding pointer-identity RTTI assumptions but still requiring compatible compiler/ABI. Legacy parseNode logic is extracted unchanged into a shared helper.

## Proposal-versus-code gaps {#proposal-versus-code-gaps}

Python decorator creates a single argument chain with executable prefixes after the last mandatory parameter; it supports trailing omission, not arbitrary omission of optional middle parameters. Nullable annotation without a Python default is marked optional, but handler omits that keyword, so a missing required Python argument can still raise TypeError. Annotated-wrapped optionality is not unwrapped at the optional-detection stage. Exposed json() parses nlohmann::json on C++ side, but toPython handles only bool/int/float/string and actor handles/vectors: Python JSON argument retrieval throws unsupported-type error. message() and rawText differ in native grammar, but the conversion path returns text for both and contains no selector expansion. Failed requires predicates and failed permissions both yield the same permission error in TreeCommand::run, contrary to the documented silent-predicate distinction. Player command-list filtering does hide failed paths but assumes native overload order matches stored order. Owner is used for diagnostics during registration, not stored in TreeCommand; per-plugin disable/unload cleanup is not implemented by this patch. A static reading does not establish lifetime safety for callbacks retained across plugin unload.

## Tests and reusable choices {#tests-and-reusable-choices}

Added21C++tests cover selector sizes/enums/defaults, custom-type native-kind resolution, tree shape, executable parents, no-handler/greedy/cycle/budget errors and same-name merging. NinePython tests cover decorator metadata, branch names/permissions, trailing-default shape and annotation rejection/inference. They do not execute real command parsing, client hints, selector resolution, permission predicates, numerical conversion, malformed/range/NaN values, JSON retrieval, callback/module teardown or middle omission. Numeric float conversion uses stof and comparisons without explicit finite check; NaN does not fail ordinary bounds comparisons. Public unsupported position/block-state/range factories remain advertised and fail registration. The useful portable pattern is bounded tree-to-native grammar adaptation with stable storage and explicit error context, accompanied by integration tests for every promised semantic distinction rather than relying on shape-only tests or the source-reported353-test run.


## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (160042 characters; SHA-256 478da1a2398341782b2f592591d77d047b9b8c00832e29631def88ca96b070e0), head bd9bbb6e35320d84870f8cadf114c9154e217e8a. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/509
