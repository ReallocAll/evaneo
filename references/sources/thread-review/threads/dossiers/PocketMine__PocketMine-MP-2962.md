<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:2962"],"source_type":"public","date":"2015-04-30","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-2962-unregistergenerator-seems-not-work"></a>
# PocketMine/PocketMine-MP#2962: unregisterGenerator seems not work. {#pocketmine-pocketmine-mp-2962-unregistergenerator-seems-not-work}

Source: https://github.com/PocketMine/PocketMine-MP/issues/2962

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Prevent terrain generation around imported floating island.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent tried unregisterGenerator and proposed level.setGenerator to switch to a void generator. shoghicp clarified unregistering did not change a level generator.

## Implementation and attribution {#implementation-and-attribution}
No implementation; registry lifecycle differs from existing per-level generator.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
No successful workaround recorded.

## Reusable decision and costs {#reusable-decision-and-costs}
Separate factory registration from already-instantiated object configuration.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [shoghicp · 2015-04-30T13:07:25Z](https://github.com/PocketMine/PocketMine-MP/issues/2962#issuecomment-97768458).
