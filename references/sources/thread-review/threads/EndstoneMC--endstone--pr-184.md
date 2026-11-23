<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:184"],"source_type":"public","date":"2025-05-18","topics":["ffi","testing","api","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-184-refactor-permission-api"></a>
# EndstoneMC/endstone #184: Refactor Permission API {#endstonemc-endstone-184-refactor-permission-api}

Source: https://github.com/EndstoneMC/endstone/pull/184

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (345 additions, 487 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu motivates this breaking API change by console-only administration: a Bukkit-like operator/non-operator boolean cannot represent a separate console default. The body targets v0.10.0, proposes DEFAULT/OPERATOR/CONSOLE, moves operator mutation to Player, removes unused ProxiedCommandSender and gives the migration from op=True to level=PermissionLevel.OPERATOR. One Codecov comment and no human reviews are captured. Merge does not establish release packaging; the 39-file implementation is inspected below.

### Complete patch inspection {#complete-patch-inspection}

The code consistently implements three levels: Default, Operator and Console. Operator defaults apply to both Operator and Console; NotOperator applies only to Default; Console defaults apply exactly to Console. Generic Permissible exposes a read-only level, while only Player retains isOp/setOp. Console always returns Console; player level derives from operator status; an unsupported native origin maps Host-or-higher to Console, above-Any to Operator, otherwise Default. Consequently the Console level represents elevated native authority as well as a literal terminal.

Permissions remain overridable. hasPermission checks effective attachment/child values before default policy. Therefore PermissionDefault::Console is a default allocation, not an absolute prohibition on granting that permission to a player. Native host-level command wrappers now use the Console default, then remove the native instance's permission restriction after the Endstone check. This completes the permission transfer begun in 180 and removes temporary host-level exclusions from command advertising. A plugin requiring a strictly terminal-only operation would need to validate sender identity separately rather than assume a default is an immutable boundary.

Default permission storage changes from unordered sets to a sequenced, hashed-unique Boost container, and the public C++ query becomes a vector preserving registration order. Recalculation clears and rebuilds effective permissions, subscribes by level, and unsubscribes all three levels on cleanup. However the changed default-recalculation code dirties only levels included by the new default; a formerly included level changing to False or a different level deserves a regression test for cached stale grants. The Python stub still says set[Permission] despite the C++ vector return, a documentation mismatch at this revision.

Core wildcard parents and devtools default to Console; individual administrative commands retain Operator defaults and ordinary commands retain permissive defaults. ProxiedCommandSender and its unused native branch/bindings are removed rather than assigned fabricated semantics. C++ headers, Python exports and bindings all migrate boolean op arguments to PermissionLevel. No new security or migration tests are included.

Exact inspected base/head: 81afdfea118431ab779822c0243f5d4e4e59c608…49baeef35e51bfe9b4353e438d88a0e5d6c2aca0. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/184
- https://github.com/EndstoneMC/endstone/pull/184#issuecomment-2892505497
