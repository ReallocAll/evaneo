<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:263"],"source_type":"public","date":"2025-09-08","topics":["concurrency","ffi","testing","api","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-263-refactor-improve-package-structure"></a>
# EndstoneMC/endstone #263: [refactor] Improve package structure {#endstonemc-endstone-263-refactor-improve-package-structure}

Source: https://github.com/EndstoneMC/endstone/pull/263

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Complete Git diff reviewed statically (6151 additions, 4993 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu authored and merged the package-structure refactor. The primary body and all three discussion components are empty, so there is no attributed design explanation or reviewer consensus beyond the submitted code and merged state.

### Complete patch inspection {#complete-patch-inspection}

The complete Git diff reconciles the connector's missing 4,314 deleted stub lines: metadata and local patch both contain 6,151 additions and 4,993 deletions across 87 files. The connector patch had only 679 deletions. The removed monolithic stub was compared structurally against every replacement stub without importing upstream code: 145 class/function definitions are identical after AST formatting and known type-qualification normalization; the seven nonidentical union entries are fully read in stub-217-delta.txt. Three are docstring whitespace; the substantive changes are Location, removal of Position, Scoreboard.add_objective and addition of event_handler's declaration. All module-level imports/exports/docstrings were read separately and comment-token multisets are identical. stub-217-mapping.json records each old/new path and normalized hash. Identical relocated declarations are mechanically verified, not presented as newly designed APIs or line-by-line rereading of thousands of unchanged declarations. Font, metrics and bootstrap-base moves are exact renames in the Git diff.

The native module changes from endstone._internal.endstone_python to endstone._python and introduces 18 thematic native submodules. Classes needed as bases or cross-references are registered before their detailed initializers. The Python facade becomes matching packages using lazy_loader.attach; py.typed and package-local .pyi files make typing discoverable at public import locations. The new dependency is unpinned in this change. EventPriority and the Python Plugin subclass remain eager imports because the decorator default/base class needs them. event_handler still attaches metadata attributes and returns the original callable. Public facades newly expose BanEntry and RenderType. Several stubs still reference private endstone._python package paths, so this is not complete elimination of private implementation names from typing surfaces. Root lazy exports also include native submodules; import-order consistency between root attributes and richer Python wrapper packages warrants testing rather than an assumed guarantee.

CLI entry points, version generation, plugin loader and metrics imports are updated together. Shared-library, debug-symbol and Detours installation moves from _internal to the root package. The unchanged bootstrap base computes the runtime path as Path(__file__).parent.parent; inspecting that code at the exact head confirms it now resolves the root package, matching the new installation directory. A head search finds no endstone._internal reference under src/endstone. This is path-coordination evidence, not a wheel installation test. Stub generation targets _python and no longer strips qualification by a global string replacement; the old rewriting block is commented out.

This refactor intentionally contains API changes. C++ Vector<T> becomes a single float Vector, with converting constructors and float-valued arithmetic. Existing double-based tests are switched to the float type but no new precision/overflow/zero-normalization cases are added. normalize still divides by length without a zero guard. Position is deleted in C++, Python binding and public exports. Location now directly inherits Vector, owns a nullable borrowed Dimension pointer and takes over the floored block-coordinate accessors. It moves into the level binding initializer. Thus existing C++ Vector<double>/Position consumers and Python imports of Position require migration; the title alone understates compatibility impact. Location.dimension's stub remains nonoptional although construction can leave it null. No ownership extension for Dimension is added.

Scoreboard.add_objective changes from a required display_name string to an optional string defaulting to the objective name via a lambda. Actor knockback uses the common event macro while its vector types and player-interaction vector construction migrate to the new Vector. These are independently meaningful behavior/signature changes, not consequences inferred from file movement. No discussion documents alternatives or migration policy, and no test execution is reported in the thread. All non-stub patch hunks were read; no upstream code was executed.

Exact inspected base/head: f00efc635bb349244a2d4c350e129e06cf952088…8f03ba3735b18dbd6199e7232d5b6e075dc82678. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/263
