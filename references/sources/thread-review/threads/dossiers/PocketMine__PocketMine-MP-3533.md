<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3533"],"source_type":"public","date":"2015-09-27","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3533-fix-event-call-when-applying-effects"></a>
# PocketMine/PocketMine-MP#3533: Fix event call when applying effects {#pocketmine-pocketmine-mp-3533-fix-event-call-when-applying-effects}

Source: https://github.com/PocketMine/PocketMine-MP/pull/3533

Thread state: closed; merged: False.

## Problem and constraints {#problem-and-constraints}
Explicitly dispatch effect damage/heal events.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
PEMapModder explained Entity.attack already dispatches the event so proposed call fires twice; Vincent accepted correction.

## Implementation and attribution {#implementation-and-attribution}
Full Effect patch adds callEvent before poison/wither attack and regeneration heal.

Diff evidence (patch inspected, not bundled): [public PR files-changed view](https://github.com/PocketMine/PocketMine-MP/pull/3533/files) (live upstream diff, not the captured immutable patch). Declared changed files: 1.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Unmerged; no need to retain as accepted design.

## Reusable decision and costs {#reusable-decision-and-costs}
Establish which layer owns event dispatch before adding hooks; duplicate dispatch changes cancellation and side effects.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [PEMapModder · 2015-09-27T04:03:44Z](https://github.com/PocketMine/PocketMine-MP/pull/3533#issuecomment-143516160).
- [wu-vincent · 2015-09-27T04:07:00Z](https://github.com/PocketMine/PocketMine-MP/pull/3533#issuecomment-143516272).
