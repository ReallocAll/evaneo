<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3541"],"source_type":"public","date":"2015-09-29","topics":["concurrency","testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3541-server-crashes-daily"></a>
# PocketMine/PocketMine-MP#3541: server crashes daily {#pocketmine-pocketmine-mp-3541-server-crashes-daily}

Source: https://github.com/PocketMine/PocketMine-MP/issues/3541

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Daily1.6dev29 crash after0.12.1 upgrade exhausted256MiB PHP limit while building batched packet string.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent urged reading dump; Vaults1 identified memory limit and suggested more allocation. No one established a leak or unexpected batch growth.

## Implementation and attribution {#implementation-and-attribution}
Full readable dump/stack and repeated encoded archive field inspected as archive, not executed. Allocation site concatenates length-prefixed packet bytes.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
No post-change retest; raising limit is capacity mitigation, not proved root repair. No plugins listed.

## Reusable decision and costs {#reusable-decision-and-costs}
Distinguish allocation failure site, configured limit, peak workload and retained-memory leak before concluding issue solved.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2015-09-30T00:27:38Z](https://github.com/PocketMine/PocketMine-MP/issues/3541#issuecomment-144227957).
- [Vaults1 · 2015-09-30T03:26:00Z](https://github.com/PocketMine/PocketMine-MP/issues/3541#issuecomment-144271998).
- [ptnalexa · 2015-09-30T05:54:25Z](https://github.com/PocketMine/PocketMine-MP/issues/3541#issuecomment-144289131).
- [Vaults1 · 2015-09-30T12:24:38Z](https://github.com/PocketMine/PocketMine-MP/issues/3541#issuecomment-144379799).
- [Ambelokopoi · 2015-09-30T13:08:59Z](https://github.com/PocketMine/PocketMine-MP/issues/3541#issuecomment-144390250).
