<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:316"],"source_type":"public","date":"2025-12-27","topics":["ffi","testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-316-feature-implement-leftclickair-for-playerinteractevent"></a>
# EndstoneMC/endstone #316: [feature] Implement `LEFT_CLICK_AIR` for `PlayerInteractEvent` {#endstonemc-endstone-316-feature-implement-leftclickair-for-playerinteractevent}

Source: https://github.com/EndstoneMC/endstone/issues/316

## Evidence and attribution {#evidence-and-attribution}

Primary author: kleines-L. Created 2025-12-27T11:59:39Z; recorded state closed; merged not applicable.

## Problem and semantic repair {#problem-and-semantic-repair}

kleines-L showed a Python handler testing PlayerInteractEvent.action.name for LEFT_CLICK_AIR that never fired on Windows v0.10.18. wu-vincent admitted the enum existed without an implemented trigger and later linked commit 8ddcac260 on v0.11.

## Actual code {#actual-code}

The inspected commit detects PlayerAuthInputPacket::InputData::MissedSwing, constructs PlayerInteractEvent with the held item, null block, placeholder BlockFace::South and no hit position, then dispatches it. If cancelled it clears the MissedSwing input bit before ordinary packet handling, suppressing the native swing and attack sound. The packet wrapper gains setInput; docs and Python stubs change from right-clicking a block to interaction with an object or air.

## Verification and reusable rule {#verification-and-reusable-rule}

A declared enum is not proof an event can occur. Select the authoritative input signal and let cancellation modify that signal before the native behavior executes. The no-block/placeholder-face semantics match other air actions; no automated test appears in the commit, so sound suppression is a maintainer claim consistent with the code path, not a runtime result from this review.

## Code and verification boundary {#code-and-verification-boundary}

Inspected complete mirror commit 8ddcac26031ca1fe17660ca1b7d0b701ae84b4ab, including packet, player handler, API docs, binding and stub changes. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/316
- https://github.com/EndstoneMC/endstone/issues/316#issuecomment-3760821427
- https://github.com/EndstoneMC/endstone/issues/316#issuecomment-5221459079
