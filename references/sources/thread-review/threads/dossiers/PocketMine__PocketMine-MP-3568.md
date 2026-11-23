<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3568"],"source_type":"public","date":"2015-10-07","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3568-fixed-recursive-call"></a>
# PocketMine/PocketMine-MP#3568: Fixed recursive call {#pocketmine-pocketmine-mp-3568-fixed-recursive-call}

Source: https://github.com/PocketMine/PocketMine-MP/pull/3568

Thread state: closed; merged: True.

## Problem and constraints {#problem-and-constraints}
setMaxStackSize recursively called itself indefinitely.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent replaced recursion; PeratX approved and Pub4Game asked about branch placement.

## Implementation and attribution {#implementation-and-attribution}
Full hunk assigns (int)$size to maxStackSize.

Diff evidence (patch inspected, not bundled): [public PR files-changed view](https://github.com/PocketMine/PocketMine-MP/pull/3568/files) (live upstream diff, not the captured immutable patch). Declared changed files: 1.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Merged; no range validation added or tests supplied.

## Reusable decision and costs {#reusable-decision-and-costs}
Setter delegation must terminate in state mutation; type conversion is separate from valid-value constraints.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [PeratX · 2015-10-07T12:47:59Z](https://github.com/PocketMine/PocketMine-MP/pull/3568#issuecomment-146186292).
- [Pub4Game · 2015-10-07T21:54:13Z](https://github.com/PocketMine/PocketMine-MP/pull/3568#issuecomment-146343912).
