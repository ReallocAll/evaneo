<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3513"],"source_type":"public","date":"2015-09-22","topics":["concurrency","testing","recovery","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3513-big-problem-in-pm-1-6"></a>
# PocketMine/PocketMine-MP#3513: Big problem in PM 1.6 {#pocketmine-pocketmine-mp-3513-big-problem-in-pm-1-6}

Source: https://github.com/PocketMine/PocketMine-MP/issues/3513

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
All players timed out on experimental1.6build30 and could not rejoin until restart;1.5 did not show it.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Latency/stability suggestions did not explain everyone failing. Reporter said downgrading crashed for players with1.6 data; another user suggested build29. Vincent routed to forum rather than diagnosing.

## Implementation and attribution {#implementation-and-attribution}
No patch; screenshot supplemental to text.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
No controlled downgrade/retest; persisted-data compatibility remains an important constraint on rollback.

## Reusable decision and costs {#reusable-decision-and-costs}
Experimental status does not explain a failure; rollback must account for data migration.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [iksaku · 2015-09-22T03:33:15Z](https://github.com/PocketMine/PocketMine-MP/issues/3513#issuecomment-142170334).
- [ptnalexa · 2015-09-22T04:48:21Z](https://github.com/PocketMine/PocketMine-MP/issues/3513#issuecomment-142180877).
- [lucasvitegui · 2015-09-22T04:58:20Z](https://github.com/PocketMine/PocketMine-MP/issues/3513#issuecomment-142181952).
- [ptnalexa · 2015-09-22T05:00:50Z](https://github.com/PocketMine/PocketMine-MP/issues/3513#issuecomment-142182130).
- [lucasvitegui · 2015-09-22T05:06:35Z](https://github.com/PocketMine/PocketMine-MP/issues/3513#issuecomment-142183038).
- [wu-vincent · 2015-09-22T06:47:18Z](https://github.com/PocketMine/PocketMine-MP/issues/3513#issuecomment-142195527).
- [ifvictr · 2015-09-22T19:34:14Z](https://github.com/PocketMine/PocketMine-MP/issues/3513#issuecomment-142394064).
- [ghost · 2015-09-22T23:25:35Z](https://github.com/PocketMine/PocketMine-MP/issues/3513#issuecomment-142451747).
