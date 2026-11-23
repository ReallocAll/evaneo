<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3035"],"source_type":"public","date":"2015-05-19","topics":["concurrency","testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3035-not-a-plugin-problem"></a>
# PocketMine/PocketMine-MP#3035: Not a Plugin Problem {#pocketmine-pocketmine-mp-3035-not-a-plugin-problem}

Source: https://github.com/PocketMine/PocketMine-MP/issues/3035

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Same getX-on-integer crash on Android build1146, with plugin list and encoded crash archive.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent confirmed; maintainer marked repeated duplicate invalid.

## Implementation and attribution {#implementation-and-attribution}
Textual stack/code duplicates#3034; encoded archive retained but not interpreted as independent readable reasoning. See#3034 for fix pointer.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Duplicate symptom, no novel implementation or test result.

## Reusable decision and costs {#reusable-decision-and-costs}
Keep one root-cause history with per-source confirmation instead of amplifying duplicate logs.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2015-05-19T12:43:07Z](https://github.com/PocketMine/PocketMine-MP/issues/3035#issuecomment-103472309).
- [shoghicp · 2015-05-19T12:48:42Z](https://github.com/PocketMine/PocketMine-MP/issues/3035#issuecomment-103473345).
