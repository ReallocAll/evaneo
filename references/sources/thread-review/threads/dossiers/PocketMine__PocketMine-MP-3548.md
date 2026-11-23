<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3548"],"source_type":"public","date":"2015-10-01","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3548-fixed-fire-resistance-effect"></a>
# PocketMine/PocketMine-MP#3548: Fixed fire resistance effect {#pocketmine-pocketmine-mp-3548-fixed-fire-resistance-effect}

Source: https://github.com/PocketMine/PocketMine-MP/pull/3548

Thread state: closed; merged: False.

## Problem and constraints {#problem-and-constraints}
Fire resistance used mutually exclusive damage causes joined by AND.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent changed predicate; PEMapModder approved logic and asked indentation.

## Implementation and attribution {#implementation-and-attribution}
Full attack hunk changes hasEffect AND FIRE AND FIRE_TICK AND LAVA to hasEffect AND (FIRE OR FIRE_TICK OR LAVA).

Diff evidence (patch inspected, not bundled): [public PR files-changed view](https://github.com/PocketMine/PocketMine-MP/pull/3548/files) (live upstream diff, not the captured immutable patch). Declared changed files: 1.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Unmerged captured PR; no automated truth-table tests.

## Reusable decision and costs {#reusable-decision-and-costs}
Group alternatives explicitly under shared guard; impossible conjunctions can silently disable protection.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [PEMapModder · 2015-10-01T10:13:55Z](https://github.com/PocketMine/PocketMine-MP/pull/3548#issuecomment-144686753).
