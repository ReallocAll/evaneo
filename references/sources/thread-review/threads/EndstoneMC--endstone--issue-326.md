<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:326"],"source_type":"public","date":"2026-02-01","topics":["testing","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-326-cannot-start-endstone-server-when-windows-user-is-disconnected"></a>
# EndstoneMC/endstone #326: Cannot start endstone server when windows user is disconnected {#endstonemc-endstone-326-cannot-start-endstone-server-when-windows-user-is-disconnected}

Source: https://github.com/EndstoneMC/endstone/issues/326

## Evidence and attribution {#evidence-and-attribution}

Primary author: RWRmrfrog. Created 2026-02-01T20:55:58Z; recorded state closed; merged not applicable.

## Reproduction and alternatives {#reproduction-and-alternatives}

RWRmrfrog reported endstone_runtime.dll access violation when starting after disconnecting an RDP session. Defender exceptions did not help. wu-vincent requested exact Task Scheduler/service/RDP steps to distinguish Session 0 from environmental conditions and recommended Docker for unattended hosting. The reporter provided a delayed start.cmd launch followed by RDP disconnect, rejected Docker due to native host integration/resource concerns, and suggested embedding the runtime in a modified executable instead of DLL injection.

## Decision and limits {#decision-and-limits}

wu-vincent ultimately attributed the limitation to runtime DLL injection and Windows session semantics and closed as not planned under the current approach. The thread documents an explicit architecture/deployment tradeoff, but contains no binary-level proof of the precise failing operation and no validated workaround. Do not generalize the reporter's suspicion into proof that Windows universally forbids this injection.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/326
- https://github.com/EndstoneMC/endstone/issues/326#issuecomment-4099873007
- https://github.com/EndstoneMC/endstone/issues/326#issuecomment-4175880659
- https://github.com/EndstoneMC/endstone/issues/326#issuecomment-4178250370
- https://github.com/EndstoneMC/endstone/issues/326#issuecomment-4604934571
