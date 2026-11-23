<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3463"],"source_type":"public","date":"2015-09-11","topics":["concurrency","testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3463-player-hasfirstplayed-returns-a-consistent-value"></a>
# PocketMine/PocketMine-MP#3463: Player::hasFirstPlayed returns a consistent value {#pocketmine-pocketmine-mp-3463-player-hasfirstplayed-returns-a-consistent-value}

Source: https://github.com/PocketMine/PocketMine-MP/issues/3463

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
hasPlayedBefore always true for Player because constructor already assigns Compound namedtag.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
shoghicp emphasized common IPlayer interface including OfflinePlayer; PrimusLV proposed hasJoinedBefore. Vincent argued Player existence implied first play; PEMapModder corrected that Player is allocated on connection before username arrives.

## Implementation and attribution {#implementation-and-attribution}
No patch; lifecycle correction is substantive.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
No final API redesign.

## Reusable decision and costs {#reusable-decision-and-costs}
Connection allocation, authenticated identity, first login and historical play are distinct states; interface uniformity must not erase semantics.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [shoghicp · 2015-09-11T13:45:39Z](https://github.com/PocketMine/PocketMine-MP/issues/3463#issuecomment-139550927).
- [PrimusLV · 2015-09-11T15:03:30Z](https://github.com/PocketMine/PocketMine-MP/issues/3463#issuecomment-139569516).
- [wu-vincent · 2015-09-13T06:54:31Z](https://github.com/PocketMine/PocketMine-MP/issues/3463#issuecomment-139847857).
- [PEMapModder · 2015-09-13T06:56:03Z](https://github.com/PocketMine/PocketMine-MP/issues/3463#issuecomment-139847894).
