<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3527"],"source_type":"public","date":"2015-09-26","topics":["concurrency","testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3527-parameter-miss-in-level-php-line-1230"></a>
# PocketMine/PocketMine-MP#3527: Parameter miss in Level.php line 1230 {#pocketmine-pocketmine-mp-3527-parameter-miss-in-level-php-line-1230}

Source: https://github.com/PocketMine/PocketMine-MP/issues/3527

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Vincent found max called with one integer in Level lighting API, expecting0–15 range.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
huangzm15 found no internal caller and explained single-argument max expects array; Vincent emphasized plugins can still call public API. dktapps later said long fixed in PMMP.

## Implementation and attribution {#implementation-and-attribution}
No source patch supplied; concrete signature/type mismatch discussion read.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Absence of internal execution explains lack of error reports, not API correctness. No verified fixcommit.

## Reusable decision and costs {#reusable-decision-and-costs}
Public APIs need tests even when core has no caller; dead internally is not unreachable externally.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [huangzm15 · 2015-09-26T10:10:52Z](https://github.com/PocketMine/PocketMine-MP/issues/3527#issuecomment-143416960).
- [wu-vincent · 2015-09-26T10:15:29Z](https://github.com/PocketMine/PocketMine-MP/issues/3527#issuecomment-143417091).
- [wu-vincent · 2015-09-26T10:43:08Z](https://github.com/PocketMine/PocketMine-MP/issues/3527#issuecomment-143418655).
- [huangzm15 · 2015-09-26T11:49:23Z](https://github.com/PocketMine/PocketMine-MP/issues/3527#issuecomment-143426125).
- [wu-vincent · 2015-09-26T12:12:45Z](https://github.com/PocketMine/PocketMine-MP/issues/3527#issuecomment-143427571).
- [dktapps · 2017-12-31T11:27:14Z](https://github.com/PocketMine/PocketMine-MP/issues/3527#issuecomment-354598757).
