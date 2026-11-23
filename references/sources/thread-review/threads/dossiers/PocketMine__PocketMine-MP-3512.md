<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3512"],"source_type":"public","date":"2015-09-22","topics":["concurrency","testing","api","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3512-fixed-crash-when-using-plugin-getlogger"></a>
# PocketMine/PocketMine-MP#3512: Fixed crash when using Plugin::getLogger() {#pocketmine-pocketmine-mp-3512-fixed-crash-when-using-plugin-getlogger}

Source: https://github.com/PocketMine/PocketMine-MP/pull/3512

Thread state: closed; merged: False.

## Problem and constraints {#problem-and-constraints}
PluginLogger failed class loading because Logger.logException was unimplemented.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Author initially tried destructor based on old1.3 experience; PEMapModder asked why and explained no static Plugin::getLogger call was involved, correcting Vincent. Actual fatal error exposed missing interface method; author revised. shoghicp said equivalent work already in local branch.

## Implementation and attribution {#implementation-and-attribution}
Full final patch implements logException(Throwable,trace): derives severity from code, truncates message newline, cleans path, logs formatted class/message/location then debug stack frames. Destructor idea absent in final.

Diff evidence (patch inspected, not bundled): [public PR files-changed view](https://github.com/PocketMine/PocketMine-MP/pull/3512/files) (live upstream diff, not the captured immutable patch). Declared changed files: 1.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Unmerged duplicate/local-branch claim, no tests. Error handling must satisfy actual current interface, not remembered old requirement.

## Reusable decision and costs {#reusable-decision-and-costs}
Read exact missing-method diagnostics; revise hypotheses explicitly and keep method-reference notation distinct from executable static calls.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [PEMapModder · 2015-09-22T10:03:24Z](https://github.com/PocketMine/PocketMine-MP/pull/3512#issuecomment-142233071).
- [wu-vincent · 2015-09-22T11:59:43Z](https://github.com/PocketMine/PocketMine-MP/pull/3512#issuecomment-142266497).
- [PEMapModder · 2015-09-22T14:55:35Z](https://github.com/PocketMine/PocketMine-MP/pull/3512#issuecomment-142312968).
- [willowmaster66 · 2015-09-22T15:00:11Z](https://github.com/PocketMine/PocketMine-MP/pull/3512#issuecomment-142314327).
- [LukeDarling · 2015-09-22T15:02:13Z](https://github.com/PocketMine/PocketMine-MP/pull/3512#issuecomment-142315377).
- [LukeDarling · 2015-09-22T15:08:13Z](https://github.com/PocketMine/PocketMine-MP/pull/3512#issuecomment-142318006).
- [PEMapModder · 2015-09-22T23:55:34Z](https://github.com/PocketMine/PocketMine-MP/pull/3512#issuecomment-142456016).
- [LukeDarling · 2015-09-23T02:51:00Z](https://github.com/PocketMine/PocketMine-MP/pull/3512#issuecomment-142475446).
- [shoghicp · 2015-09-23T12:47:19Z](https://github.com/PocketMine/PocketMine-MP/pull/3512#issuecomment-142587539).
- [LukeDarling · 2015-09-23T21:52:41Z](https://github.com/PocketMine/PocketMine-MP/pull/3512#issuecomment-142741056).
