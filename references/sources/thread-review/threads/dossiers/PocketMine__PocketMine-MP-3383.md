<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3383"],"source_type":"public","date":"2015-08-17","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3383-running-up-slabs-makes-you-jump"></a>
# PocketMine/PocketMine-MP#3383: Running up slabs makes you jump {#pocketmine-pocketmine-mp-3383-running-up-slabs-makes-you-jump}

Source: https://github.com/PocketMine/PocketMine-MP/issues/3383

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Running up alternating half slabs caused jumping.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Reporter clarified1.5dev1262 and reproduced only multiplayer, not singleplayer. A recommended TruFix plugin was challenged by Vincent as logging only; reporter confirmed relevant code was commented out. shoghicp called it client-side, but comparative test challenged simple attribution.

## Implementation and attribution {#implementation-and-attribution}
No fix patch. Plugin effectiveness criticism is thread evidence, not independent plugin audit.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
No resolved mechanism. Screenshot depicts test layout, not measured collision trace.

## Reusable decision and costs {#reusable-decision-and-costs}
Inspect alleged workarounds and preserve controlled server/offline counterexamples before assigning blame.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [ghost · 2015-08-18T22:47:21Z](https://github.com/PocketMine/PocketMine-MP/issues/3383#issuecomment-132380149).
- [inxomnyaa · 2015-08-19T04:45:12Z](https://github.com/PocketMine/PocketMine-MP/issues/3383#issuecomment-132444240).
- [ghost · 2015-08-20T12:43:58Z](https://github.com/PocketMine/PocketMine-MP/issues/3383#issuecomment-132995176).
- [inxomnyaa · 2015-08-20T19:20:21Z](https://github.com/PocketMine/PocketMine-MP/issues/3383#issuecomment-133133884).
- [inxomnyaa · 2015-09-24T11:11:05Z](https://github.com/PocketMine/PocketMine-MP/issues/3383#issuecomment-142899522).
- [ghost · 2015-09-24T20:47:31Z](https://github.com/PocketMine/PocketMine-MP/issues/3383#issuecomment-143046359).
- [inxomnyaa · 2015-09-25T05:58:31Z](https://github.com/PocketMine/PocketMine-MP/issues/3383#issuecomment-143136426).
- [wu-vincent · 2015-09-25T06:17:35Z](https://github.com/PocketMine/PocketMine-MP/issues/3383#issuecomment-143138760).
- [inxomnyaa · 2015-09-25T06:47:11Z](https://github.com/PocketMine/PocketMine-MP/issues/3383#issuecomment-143143821).
- [shoghicp · 2015-09-25T07:57:40Z](https://github.com/PocketMine/PocketMine-MP/issues/3383#issuecomment-143152928).
- [inxomnyaa · 2015-09-25T10:15:55Z](https://github.com/PocketMine/PocketMine-MP/issues/3383#issuecomment-143181273).
- [inxomnyaa · 2015-09-25T10:25:30Z](https://github.com/PocketMine/PocketMine-MP/issues/3383#issuecomment-143182609).
