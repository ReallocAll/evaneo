<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3490"],"source_type":"public","date":"2015-09-15","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3490-invalid-name-error"></a>
# PocketMine/PocketMine-MP#3490: Invalid name! Error {#pocketmine-pocketmine-mp-3490-invalid-name-error}

Source: https://github.com/PocketMine/PocketMine-MP/issues/3490

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Xbox gamertag containing spaces failed name validation.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent suggested allowing spaces in Player.php regex; shoghicp warned this breaks command tokenization. A later color-name report adds separate invalid-name possibility.

## Implementation and attribution {#implementation-and-attribution}
No patch. Regex relaxation alone leaves downstream grammar assumptions unchanged.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
No retest or full-name handling design.

## Reusable decision and costs {#reusable-decision-and-costs}
Validate identity syntax with every consumer, especially command parsers, rather than changing only ingress validation.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2015-09-15T04:59:37Z](https://github.com/PocketMine/PocketMine-MP/issues/3490#issuecomment-140281409).
- [wu-vincent · 2015-09-15T06:24:04Z](https://github.com/PocketMine/PocketMine-MP/issues/3490#issuecomment-140292363).
- [shoghicp · 2015-09-15T07:10:09Z](https://github.com/PocketMine/PocketMine-MP/issues/3490#issuecomment-140300869).
- [ghost · 2017-07-06T03:03:51Z](https://github.com/PocketMine/PocketMine-MP/issues/3490#issuecomment-313282783).
