<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3658"],"source_type":"public","date":"2015-10-27","topics":["concurrency","testing","diagnosis","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3658-arrow-crash-fix"></a>
# PocketMine/PocketMine-MP#3658: Arrow crash fix {#pocketmine-pocketmine-mp-3658-arrow-crash-fix}

Source: https://github.com/PocketMine/PocketMine-MP/pull/3658

Thread state: closed; merged: False.

## Problem and constraints {#problem-and-constraints}
Arrow pickup crashed0.12 client; proposed removing/reducing TakeItemEntityPacket.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
willowmaster66 requested side-effect evidence rather than accepting works-on-server claim, then performed variants and a second-client observation with Intyre. Kill triggers despawn, so explicit pickup broadcast may be unnecessary. PEMapModder distinguished arrow entities from item entities and self ID0. Vincent asked whether crash fixed without other issues.

## Implementation and attribution {#implementation-and-attribution}
Final captured patch differs from broad deletion discussed: it removes broadcast and the second self-eid0 packet construction, retaining one dataPacket whose eid is real player ID. Inventory addition/kill remain. Thus tests of deleting all lines do not automatically validate final exact variant.

Diff evidence (patch inspected, not bundled): [public PR files-changed view](https://github.com/PocketMine/PocketMine-MP/pull/3658/files) (live upstream diff, not the captured immutable patch). Declared changed files: 1.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Unmerged. Thread contains useful controlled tests, but versions/patch variants not fully aligned; no test of every viewer/client combination.

## Reusable decision and costs {#reusable-decision-and-costs}
Demand observable side-effect tests and bind results to exact revision; client-specific self IDs and entity class are protocol semantics, not interchangeable integers.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [willowmaster66 · 2015-10-27T12:24:48Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151474312).
- [hmy2001 · 2015-10-27T12:33:56Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151477467).
- [hmy2001 · 2015-10-27T12:44:00Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151479796).
- [willowmaster66 · 2015-10-27T13:06:31Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151488684).
- [PEMapModder · 2015-10-27T14:00:48Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151504847).
- [HmHmmHm · 2015-10-27T14:46:46Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151525449).
- [willowmaster66 · 2015-10-27T15:27:21Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151540273).
- [PEMapModder · 2015-10-27T15:47:18Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151546629).
- [HmHmmHm · 2015-10-27T15:57:45Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151549830).
- [Intyre · 2015-10-27T16:19:26Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151556363).
- [HmHmmHm · 2015-10-27T16:43:56Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151563935).
- [willowmaster66 · 2015-10-27T17:15:00Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151574212).
- [willowmaster66 · 2015-10-27T21:30:41Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151650858).
- [HmHmmHm · 2015-10-28T00:30:58Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151683298).
- [willowmaster66 · 2015-10-28T06:20:51Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151737256).
- [HmHmmHm · 2015-10-28T08:05:07Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151757457).
- [PEMapModder · 2015-10-28T10:20:58Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-151792198).
- [wu-vincent · 2015-10-30T14:16:27Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-152537991).
- [PEMapModder · 2015-10-30T15:44:24Z](https://github.com/PocketMine/PocketMine-MP/pull/3658#issuecomment-152560633).
