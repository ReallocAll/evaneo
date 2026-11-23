<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:324"],"source_type":"public","date":"2026-01-17","topics":["ffi","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-324-feat-add-blockfromtoevent"></a>
# EndstoneMC/endstone #324: feat: add BlockFromToEvent {#endstonemc-endstone-324-feat-add-blockfromtoevent}

Source: https://github.com/EndstoneMC/endstone/pull/324

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-01-17T18:29:42Z; recorded state closed; merged True.

## Patch lineage and revision {#patch-lineage-and-revision}

This merged replacement explicitly says “Move #299,” so killcerr's original work remains part of its provenance even though wu-vincent opened this PR. Compared with #299, it adopts ENDSTONE_EVENT macros, corrects BlockFormEvent's class spelling and BlockGrowEvent::getNewState, documents the event hierarchy, exports headers, adds native facing masks/opposites and liquid-detection rules, and changes the trigger guard from primary-thread checking to excluding instant-tick positions.

## Actual behavior and review caveat {#actual-behavior-and-review-caveat}

The hook calls _canSpreadTo and !region.isInstaticking, dispatches a cancellable source/destination event, and skips the original spread when cancelled. The helper checks min height, loaded-block presence, same material/lava, and directional blocking rules. The captured final patch returns _isLiquidBlocking(...) directly from _canSpreadTo, whereas #299 rejected a true blocking result. The subsequent commit chain below confirms and fixes this inversion; it must not be attributed to the final behavior after those fixes.

BlockFormEvent and BlockGrowEvent declarations/docstrings are included, but their existence does not show corresponding runtime triggers. In particular later #329 scopes BlockFormEvent much more narrowly than its generic snow/ice documentation. No tests or authored review discussion appear; 27 reported commits are not individually reconstructed here.

## Additional source and attachment inspection {#additional-source-and-attachment-inspection}

All changes and messages of three follow-up commits were read directly. 72ce69200c50deacc486f418f318335a96c2c946 negates `_isLiquidBlocking`, checks the destination block for lava blocking rather than the source liquid, and initially compares Material types. 889e7929595ad5eca180fc62d73ce4f5bd2f1525 replaces that type comparison with identity (`this == &rhs`). db1796490452f734bd1cb1e676845bf2c85b9b08 passes the destination position to its directional flow predicate and consistently names the destination block. These are distinct semantic repairs immediately after #324, not evidence that the initial squash was already correct. No regression test is added in these three patches. All three public commit links are listed below; the original hash ledger is not distributed.

## Code and verification boundary {#code-and-verification-boundary}

Inspected complete captured 16,370-character patch and compared it with #299; all discussion components are empty. Complete relevant follow-up commit patches/messages inspected; the public revisions are linked below, but the historical hash/parent/path ledger is not distributed. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/324
- https://github.com/EndstoneMC/endstone/commit/72ce69200c50deacc486f418f318335a96c2c946
- https://github.com/EndstoneMC/endstone/commit/889e7929595ad5eca180fc62d73ce4f5bd2f1525
- https://github.com/EndstoneMC/endstone/commit/db1796490452f734bd1cb1e676845bf2c85b9b08
