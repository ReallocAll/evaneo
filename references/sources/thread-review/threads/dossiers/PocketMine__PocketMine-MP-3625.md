<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3625"],"source_type":"public","date":"2015-10-18","topics":["concurrency","testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3625-fixed-wrong-exception-message"></a>
# PocketMine/PocketMine-MP#3625: Fixed wrong exception message {#pocketmine-pocketmine-mp-3625-fixed-wrong-exception-message}

Source: https://github.com/PocketMine/PocketMine-MP/pull/3625

Thread state: closed; merged: False.

## Problem and constraints {#problem-and-constraints}
Exception diagnostic printed the default value twice rather than a label.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
No discussion.

## Implementation and attribution {#implementation-and-attribution}
Full one-line patch changes interpolated $defaultValue label to literal defaultValue; range condition unchanged.

Diff evidence (patch inspected, not bundled): [public PR files-changed view](https://github.com/PocketMine/PocketMine-MP/pull/3625/files) (live upstream diff, not the captured immutable patch). Declared changed files: 1.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Unmerged; deterministic diagnostic-only correction.

## Reusable decision and costs {#reusable-decision-and-costs}
Keep error labels stable so numeric values remain interpretable.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
