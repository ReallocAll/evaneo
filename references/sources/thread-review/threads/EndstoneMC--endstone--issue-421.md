<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:421"],"source_type":"public","date":"2026-07-01","topics":["lifetime","ffi","testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-421-permission-attachments-are-use-after-free-when-removed-while-still-referenced-shared-ownership-fix-abi-bre"></a>
# EndstoneMC/endstone #421: Permission attachments are use-after-free when removed while still referenced (shared-ownership fix, ABI-breaking) {#endstonemc-endstone-421-permission-attachments-are-use-after-free-when-removed-while-still-referenced-shared-ownership-fix-abi-bre}

Source: https://github.com/EndstoneMC/endstone/issues/421

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-07-01T00:07:07Z; recorded state closed; merged not applicable.

## Ownership failure {#ownership-failure}

Split from #325, this issue removes reload as a necessary condition: iterating effective_permissions while removing attachments is enough. PermissibleBase unique_ptr containers own attachments and infos while Python receives raw borrowed pointers. Removal frees an attachment then recalculation clears every info; iteration continues through a stale snapshot. reference_internal cannot protect erased pointees merely by keeping the parent alive.

## Proposed complete repair {#proposed-complete-repair}

Use shared_ptr containers, info→attachment strong ownership and shared pybind holders, returning co-owning handles rather than reference policies. No info/attachment cycle is claimed because attachments do not point back to infos. Reload adds a second hazard: surviving attachments refer to destroyed plugins and possibly unloaded C++ DLLs. Extend shared ownership to Plugin, preserve module-capturing deleters until the final reference drops, and use per-load-unique shadow DLL names so Windows locks on old modules do not block a new reload.

## Tradeoffs, ABI and migration {#tradeoffs-abi-and-migration}

This deliberately permits stale-but-valid snapshots and keeps disabled plugins/modules alive while references survive, avoiding a detach sweep at the cost of delayed resource release. No ABI-safe subset is claimed: both public class layouts/inline methods and virtual addAttachment/getEffectivePermissions return types change. Since 0.11.x plugins share an exact major.minor ABI gate, this targets develop/0.12; C++ callers using auto* migrate to auto, Python syntax remains unchanged.

The issue is closed with no comments or linked implementation in the captured body. Treat this as a detailed design proposal, not proof the full shared-ownership graph shipped. Java GC is the semantic model being recreated, not a reason unique_ptr is generally wrong.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/421
