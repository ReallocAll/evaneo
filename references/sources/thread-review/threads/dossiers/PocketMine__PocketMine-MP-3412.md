<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3412"],"source_type":"public","date":"2015-08-25","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3412-sethealth-bug"></a>
# PocketMine/PocketMine-MP#3412: setHealth() bug {#pocketmine-pocketmine-mp-3412-sethealth-bug}

Source: https://github.com/PocketMine/PocketMine-MP/issues/3412

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
setHealth(20) apparently killed client while server considered player alive, preventing respawn.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
alejandroliu observed /kill could resynchronize death and allow respawn. Contributors disputed client/server ownership; Vincent asked why attack/heal, which call setHealth, differ. TigerHix later confirmed same plugin code worked1.4 but failed1.6. Final comment says should be fixed#3978.

## Implementation and attribution {#implementation-and-attribution}
No fix patch in issue; gist and#3978 not yet inspected.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Open causal questions: setter wire representation, death-state synchronization, version differences. Final should-be-resolved is weaker than reporter retest.

## Reusable decision and costs {#reusable-decision-and-costs}
Test client/server state agreement, not only health field assignment; trace direct and wrapped setter paths.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [Creeperface01 · 2015-08-25T11:16:49Z](https://github.com/PocketMine/PocketMine-MP/issues/3412#issuecomment-134557178).
- [ptnalexa · 2015-08-30T22:35:27Z](https://github.com/PocketMine/PocketMine-MP/issues/3412#issuecomment-136210994).
- [xpyctum · 2015-09-14T07:51:48Z](https://github.com/PocketMine/PocketMine-MP/issues/3412#issuecomment-139987636).
- [ghost · 2015-09-15T22:02:12Z](https://github.com/PocketMine/PocketMine-MP/issues/3412#issuecomment-140559388).
- [alejandroliu · 2015-09-23T07:40:00Z](https://github.com/PocketMine/PocketMine-MP/issues/3412#issuecomment-142520514).
- [dancing-ipsum · 2015-10-02T06:12:32Z](https://github.com/PocketMine/PocketMine-MP/issues/3412#issuecomment-144934044).
- [alejandroliu · 2015-10-02T07:22:05Z](https://github.com/PocketMine/PocketMine-MP/issues/3412#issuecomment-144941970).
- [PEMapModder · 2015-10-02T10:23:02Z](https://github.com/PocketMine/PocketMine-MP/issues/3412#issuecomment-144985454).
- [wu-vincent · 2015-10-02T11:21:01Z](https://github.com/PocketMine/PocketMine-MP/issues/3412#issuecomment-144993639).
- [Intyre · 2015-10-04T22:35:01Z](https://github.com/PocketMine/PocketMine-MP/issues/3412#issuecomment-145395030).
- [TigerHix · 2016-01-03T16:48:09Z](https://github.com/PocketMine/PocketMine-MP/issues/3412#issuecomment-168517656).
- [PEMapModder · 2016-03-07T10:16:41Z](https://github.com/PocketMine/PocketMine-MP/issues/3412#issuecomment-193193088).

## Supplemental verification (supersedes earlier acquisition gaps) {#supplemental-verification-supersedes-earlier-acquisition-gaps}
Linked PEMapModder #3978 is acquired (54 files); only issue-relevant health/attribute synchronization chain is inspected, not the whole hunger/food feature. Living.setHealth calls parent then updates HEALTH attribute; mutations mark attributes desynchronized; AttributeMap.needSend filters syncable dirty entries; Player.entityBaseTick sends UpdateAttributesPacket for local entity 0 and marks entries synchronized. This gives a concrete mechanism for synchronizing setter state with client health. PR body explicitly lists #3412 resolved and it merged. No isolated retest proves every reported variant; #3978 is not credited as wholly read or Vincent-authored.
