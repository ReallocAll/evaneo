<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3429"],"source_type":"public","date":"2015-08-30","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3429-fixed-color-in-some-language"></a>
# PocketMine/PocketMine-MP#3429: Fixed color in some language {#pocketmine-pocketmine-mp-3429-fixed-color-in-some-language}

Source: https://github.com/PocketMine/PocketMine-MP/pull/3429

Thread state: closed; merged: False.

## Problem and constraints {#problem-and-constraints}
Formatting color leaked after version insertion in localized server-start line.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent added WHITE after AQUA version. shoghicp rejected piecemeal formatting codes in favor of planned format system/compiler that permits arbitrary surrounding colors.

## Implementation and attribution {#implementation-and-attribution}
Full one-hunk Server patch read: AQUA+version becomes AQUA+version+WHITE. Fix hardcodes reset color rather than restoring prior semantic style.

Diff evidence (patch inspected, not bundled): [public PR files-changed view](https://github.com/PocketMine/PocketMine-MP/pull/3429/files) (live upstream diff, not the captured immutable patch). Declared changed files: 1.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Unmerged; planned formatter not implemented here.

## Reusable decision and costs {#reusable-decision-and-costs}
Structured formatting avoids ad hoc reset codes and preserves translator/layout freedom.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [shoghicp · 2015-08-30T13:56:48Z](https://github.com/PocketMine/PocketMine-MP/pull/3429#issuecomment-136139759).
