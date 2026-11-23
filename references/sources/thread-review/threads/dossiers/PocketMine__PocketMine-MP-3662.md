<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3662"],"source_type":"public","date":"2015-10-31","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3662-fix-autosave-in-playerquitevent"></a>
# PocketMine/PocketMine-MP#3662: Fix autoSave in PlayerQuitEvent {#pocketmine-pocketmine-mp-3662-fix-autosave-in-playerquitevent}

Source: https://github.com/PocketMine/PocketMine-MP/pull/3662

Thread state: closed; merged: True.

## Problem and constraints {#problem-and-constraints}
PlayerQuitEvent constructor ignored autoSave argument.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
No discussion.

## Implementation and attribution {#implementation-and-attribution}
Full hunk assigns supplied $autoSave instead of true; default parameter remains true and setter still coerces bool.

Diff evidence (patch inspected, not bundled): [public PR files-changed view](https://github.com/PocketMine/PocketMine-MP/pull/3662/files) (live upstream diff, not the captured immutable patch). Declared changed files: 1.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Merged, no tests.

## Reusable decision and costs {#reusable-decision-and-costs}
Constructor parameters must propagate to stored policy; test explicit false separately from default true.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
