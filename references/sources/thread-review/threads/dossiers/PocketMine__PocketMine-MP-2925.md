<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:2925"],"source_type":"public","date":"2015-04-22","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-2925-colors-doesn-t-work-properly-on-windows"></a>
# PocketMine/PocketMine-MP#2925: Colors doesn't work properly on Windows. {#pocketmine-pocketmine-mp-2925-colors-doesn-t-work-properly-on-windows}

Source: https://github.com/PocketMine/PocketMine-MP/issues/2925

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Minecraft section-sign formatting codes printed literally on Windows mintty.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent said latest build still failed; shoghicp asked whether normal start.cmd was used and suspected text replacement.

## Implementation and attribution {#implementation-and-attribution}
Concrete log shows raw formatting tokens, not merely wrong ANSI colors. Followup#2928 supplies launch-script confirmation.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
No patch/retest here.

## Reusable decision and costs {#reusable-decision-and-costs}
Trace game-format translation separately from terminal ANSI support.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [PEMapModder · 2015-04-22T09:59:16Z](https://github.com/PocketMine/PocketMine-MP/issues/2925#issuecomment-95107932).
- [wu-vincent · 2015-04-22T10:00:49Z](https://github.com/PocketMine/PocketMine-MP/issues/2925#issuecomment-95109521).
- [shoghicp · 2015-04-22T13:46:13Z](https://github.com/PocketMine/PocketMine-MP/issues/2925#issuecomment-95183722).
