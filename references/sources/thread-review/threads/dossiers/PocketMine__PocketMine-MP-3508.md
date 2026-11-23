<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3508"],"source_type":"public","date":"2015-09-20","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3508-bug-when-transporting-the-player"></a>
# PocketMine/PocketMine-MP#3508: Bug when transporting the player {#pocketmine-pocketmine-mp-3508-bug-when-transporting-the-player}

Source: https://github.com/PocketMine/PocketMine-MP/issues/3508

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Transferred player remained connected to first server.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
shoghicp called it client-side; Vincent asked why not fix client.

## Implementation and attribution {#implementation-and-attribution}
No protocol trace, cleanup patch or actionable mechanism.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Unresolved ownership assertion.

## Reusable decision and costs {#reusable-decision-and-costs}
No implementation conclusion.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [shoghicp · 2015-09-20T13:57:43Z](https://github.com/PocketMine/PocketMine-MP/issues/3508#issuecomment-141786551).
- [wu-vincent · 2015-09-20T14:19:14Z](https://github.com/PocketMine/PocketMine-MP/issues/3508#issuecomment-141791973).
