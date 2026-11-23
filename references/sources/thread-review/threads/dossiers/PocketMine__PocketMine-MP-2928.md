<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:2928"],"source_type":"public","date":"2015-04-23","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-2928-color-issue-is-still-there"></a>
# PocketMine/PocketMine-MP#2928: Color issue is still there. {#pocketmine-pocketmine-mp-2928-color-issue-is-still-there}

Source: https://github.com/PocketMine/PocketMine-MP/issues/2928

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Followup color failure after a supposed Windows fix, using unchanged start.cmd.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Another user reported Windows7x64 success and specified build1078 plus commit2ea8835b12ce7a3dbb4829dd76605cd211306555.

## Implementation and attribution {#implementation-and-attribution}
No patch captured in this issue; linked fix not yet inspected. Screenshot is supplemental to precise textual symptom.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Reporter does not confirm build1078 or repair.

## Reusable decision and costs {#reusable-decision-and-costs}
Preserve negative retest and exact build boundaries; another machine working is not refutation.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [L3ice · 2015-04-23T12:02:50Z](https://github.com/PocketMine/PocketMine-MP/issues/2928#issuecomment-95560356).
