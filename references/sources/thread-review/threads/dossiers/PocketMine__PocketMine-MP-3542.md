<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3542"],"source_type":"public","date":"2015-09-30","topics":["concurrency","testing","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3542-i-cant-make-a-server-pocketmine"></a>
# PocketMine/PocketMine-MP#3542: i cant make a server [Pocketmine] {#pocketmine-pocketmine-mp-3542-i-cant-make-a-server-pocketmine}

Source: https://github.com/PocketMine/PocketMine-MP/issues/3542

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Reinstalling server after moving old files to trash failed startup.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent requested logs, then identified UDP bind address already in use; suggested locating/stopping owning process or changing port. Reporter confirmed success.

## Implementation and attribution {#implementation-and-attribution}
Readable log shows socket_bind error48 on default19132. File deletion had not guaranteed process termination.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Successful reporter resolution; exact chosen alternative unspecified.

## Reusable decision and costs {#reusable-decision-and-costs}
Inspect live resource ownership rather than filesystem state when a restarted service cannot bind.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2015-09-30T00:28:31Z](https://github.com/PocketMine/PocketMine-MP/issues/3542#issuecomment-144228056).
- [tsuhakkun · 2015-09-30T00:31:04Z](https://github.com/PocketMine/PocketMine-MP/issues/3542#issuecomment-144228338).
- [wu-vincent · 2015-09-30T00:36:12Z](https://github.com/PocketMine/PocketMine-MP/issues/3542#issuecomment-144228912).
- [tsuhakkun · 2015-09-30T00:37:11Z](https://github.com/PocketMine/PocketMine-MP/issues/3542#issuecomment-144229010).
- [wu-vincent · 2015-09-30T00:41:28Z](https://github.com/PocketMine/PocketMine-MP/issues/3542#issuecomment-144229509).
- [tsuhakkun · 2015-09-30T00:42:05Z](https://github.com/PocketMine/PocketMine-MP/issues/3542#issuecomment-144229566).
- [tsuhakkun · 2015-09-30T00:44:27Z](https://github.com/PocketMine/PocketMine-MP/issues/3542#issuecomment-144229907).
