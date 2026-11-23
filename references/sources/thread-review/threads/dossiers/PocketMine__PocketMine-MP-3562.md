<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3562"],"source_type":"public","date":"2015-10-06","topics":["concurrency","testing","build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3562-messages-incorrect-in-last-build-0-error-is-back"></a>
# PocketMine/PocketMine-MP#3562: Messages incorrect in last build/{%0} error is back {#pocketmine-pocketmine-mp-3562-messages-incorrect-in-last-build-0-error-is-back}

Source: https://github.com/PocketMine/PocketMine-MP/issues/3562

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Localized join/leave logs emitted translation keys.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent suspected plugin logging raw getLeaveMessage. Reporter retested without plugins and still failed, clarified latest stable1.5 versus another healthy bleeding1.6build43. Downgrade lost trapdoor/gate sounds.

## Implementation and attribution {#implementation-and-attribution}
No patch.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Plugin hypothesis contradicted; branch/version differences and downgrade cost preserved.

## Reusable decision and costs {#reusable-decision-and-costs}
A clean-plugin reproduction is stronger than assuming unchanged plugins cannot interact with updated core.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2015-10-06T10:23:00Z](https://github.com/PocketMine/PocketMine-MP/issues/3562#issuecomment-145813636).
- [inxomnyaa · 2015-10-06T11:03:52Z](https://github.com/PocketMine/PocketMine-MP/issues/3562#issuecomment-145823085).
- [ghost · 2015-10-06T12:30:41Z](https://github.com/PocketMine/PocketMine-MP/issues/3562#issuecomment-145842158).
- [inxomnyaa · 2015-10-06T13:08:05Z](https://github.com/PocketMine/PocketMine-MP/issues/3562#issuecomment-145851359).
- [ghost · 2015-10-06T19:58:07Z](https://github.com/PocketMine/PocketMine-MP/issues/3562#issuecomment-145980131).
- [inxomnyaa · 2015-10-06T21:54:55Z](https://github.com/PocketMine/PocketMine-MP/issues/3562#issuecomment-146012868).
- [ghost · 2015-10-07T01:52:24Z](https://github.com/PocketMine/PocketMine-MP/issues/3562#issuecomment-146054727).
