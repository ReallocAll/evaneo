<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3595"],"source_type":"public","date":"2015-10-13","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3595-better-grass-spreading-and-added-dirt"></a>
# PocketMine/PocketMine-MP#3595: Better grass spreading and added dirt {#pocketmine-pocketmine-mp-3595-better-grass-spreading-and-added-dirt}

Source: https://github.com/PocketMine/PocketMine-MP/pull/3595

Thread state: closed; merged: False.

## Problem and constraints {#problem-and-constraints}
Add light-dependent grass death/spread resembling PC behavior.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent approved generically; author later acknowledged an issue found by mwvent without specifying correction.

## Implementation and attribution {#implementation-and-attribution}
Full Grass hunk read. Moves random xyz assignment into spread loop but reads them before assignment. Low light dispatches Dirt spread event without applying new state. Spread requires metadata0x0F and absolute z<=2, unusual constraints not explained by body. Four random attempts otherwise use light thresholds4/9 and cancellable events.

Diff evidence (patch inspected, not bundled): [public PR files-changed view](https://github.com/PocketMine/PocketMine-MP/pull/3595/files) (live upstream diff, not the captured immutable patch). Declared changed files: 1.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Unmerged, known unspecified issue; positive reaction not validation.

## Reusable decision and costs {#reusable-decision-and-costs}
Check variable lifetime and event-versus-state mutation separately; visual feature intent cannot establish algorithm correctness.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2015-10-13T11:06:39Z](https://github.com/PocketMine/PocketMine-MP/pull/3595#issuecomment-147684300).
- [inxomnyaa · 2015-10-13T11:08:08Z](https://github.com/PocketMine/PocketMine-MP/pull/3595#issuecomment-147684524).
- [inxomnyaa · 2015-11-20T11:52:36Z](https://github.com/PocketMine/PocketMine-MP/pull/3595#issuecomment-158374057).
