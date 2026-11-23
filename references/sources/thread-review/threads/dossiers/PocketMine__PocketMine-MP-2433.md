<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:2433"],"source_type":"public","date":"2014-12-22","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-2433-the-tps-went-to-almost-zero-when-a-player-is-joining-and-player-will-be-teleported-to-the-past-posit"></a>
# PocketMine/PocketMine-MP#2433: The TPS went to almost zero when a player is joining.And player will be teleported to the past position when they are moving very usual. {#pocketmine-pocketmine-mp-2433-the-tps-went-to-almost-zero-when-a-player-is-joining-and-player-will-be-teleported-to-the-past-posit}

Source: https://github.com/PocketMine/PocketMine-MP/issues/2433

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Vincent reported near-zero TPS during joining and movement rollback.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
shoghicp suspected device capacity for world generation and suggested flat terrain as a diagnostic.

## Implementation and attribution {#implementation-and-attribution}
No profile or code.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
No retest; hardware limitation unproven.

## Reusable decision and costs {#reusable-decision-and-costs}
Compare generated versus flat terrain to isolate generation load.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [shoghicp · 2014-12-22T15:36:38Z](https://github.com/PocketMine/PocketMine-MP/issues/2433#issuecomment-67850294).
