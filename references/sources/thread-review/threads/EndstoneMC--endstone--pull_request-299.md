<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:299"],"source_type":"public","date":"2025-11-21","topics":["ffi","testing","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-299-feat-add-blockfromtoevent"></a>
# EndstoneMC/endstone #299: feat: add BlockFromToEvent {#endstonemc-endstone-299-feat-add-blockfromtoevent}

Source: https://github.com/EndstoneMC/endstone/pull/299

## Evidence and attribution {#evidence-and-attribution}

Primary author: killcerr. Created 2025-11-21T17:45:16Z; recorded state closed; merged False.

## Problem and patch {#problem-and-patch}

killcerr proposed BlockFromToEvent; the primary body is empty. The patch introduces a cancellable event owning source/destination Block wrappers, a LiquidBlock::_trySpreadTo hook, eligibility checking, Windows offsets and CMake integration. The hook only emits on the primary thread and when the destination can receive liquid. Cancellation returns before the original spread; otherwise the original is called. Eligibility excludes below-min-height positions, same material, lava, and native liquid-blocking checks.

## Revision/disposition and limits {#revision-disposition-and-limits}

The patch also contains early BlockGrowEvent/BlockFormEvent scaffolding: the declared class is spelled BlockFromEvent while its event macro names BlockFormEvent, and BlockGrowEvent exposes its new-state field through getToBlock. These static observations show unfinished adjacent work rather than a tested final interface. Seven commits are reported but per-commit evolution was not reconstructed. wu-vincent closed this unmerged PR with a link to replacement #324; implementation authorship must credit killcerr rather than assigning the entire later patch to the merging maintainer.

No tests or human review rationale are captured. Reusable pattern: guard event injection with native eligibility, enforce cancellation before side effects, and track replacement PRs rather than treating closure as rejection of the feature.

## Code and verification boundary {#code-and-verification-boundary}

Inspected the complete captured 8,813-character PR diff and all discussion. File headers are absent from this connector patch; symbol and include names identify the relevant implementation. Replacement #324 is separately assigned. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/299
- https://github.com/EndstoneMC/endstone/pull/299#issuecomment-3764188476
