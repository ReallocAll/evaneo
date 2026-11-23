<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3579"],"source_type":"public","date":"2015-10-11","topics":["concurrency","testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3579-implement-method-getresult"></a>
# PocketMine/PocketMine-MP#3579: Implement method getResult {#pocketmine-pocketmine-mp-3579-implement-method-getresult}

Source: https://github.com/PocketMine/PocketMine-MP/pull/3579

Thread state: closed; merged: False.

## Problem and constraints {#problem-and-constraints}
Shaped recipe class lacked required getResult.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Reviewer asked whether it crashed; Vincent said no current use, but interface still requires implementation. Later declared obsolete by PMMP changes.

## Implementation and attribution {#implementation-and-attribution}
Full hunk returns clone of stored output, preserving encapsulation rather than exposing mutable result.

Diff evidence (patch inspected, not bundled): [public PR files-changed view](https://github.com/PocketMine/PocketMine-MP/pull/3579/files) (live upstream diff, not the captured immutable patch). Declared changed files: 1.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Unmerged, no tests; absence of live crash does not invalidate contract repair.

## Reusable decision and costs {#reusable-decision-and-costs}
Implement interface obligations before first invocation; clone mutable outputs when caller mutation must not affect recipe.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [willowmaster66 · 2015-10-11T08:39:19Z](https://github.com/PocketMine/PocketMine-MP/pull/3579#issuecomment-147172457).
- [wu-vincent · 2015-10-11T08:57:00Z](https://github.com/PocketMine/PocketMine-MP/pull/3579#issuecomment-147173889).
- [dktapps · 2017-12-31T10:48:54Z](https://github.com/PocketMine/PocketMine-MP/pull/3579#issuecomment-354597287).
