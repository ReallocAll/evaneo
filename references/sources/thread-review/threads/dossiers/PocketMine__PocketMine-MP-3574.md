<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3574"],"source_type":"public","date":"2015-10-09","topics":["concurrency","testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3574-crash-when-player-gets-kicked-with-custom-message"></a>
# PocketMine/PocketMine-MP#3574: Crash when player gets kicked with custom message.. {#pocketmine-pocketmine-mp-3574-crash-when-player-gets-kicked-with-custom-message}

Source: https://github.com/PocketMine/PocketMine-MP/issues/3574

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Custom whitelist kick during login left inventory null before setHeldItemSlot.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
ifvictr requested minimal plugin set; willowmaster66 asked exact reproduction. Reporter identified ReasonWL. Vincent proposed removing generated32/64bit PHP files; PEMapModder explicitly said this had nothing to do with architecture-specific files. No evidence supports the deletion suggestion.

## Implementation and attribution {#implementation-and-attribution}
Readable stack reaches login path after event; snippet checks cancellation then uses inventory. Potential lifecycle issue after plugin kick is hypothesis, not proved code path. Encoded crash archive not executed.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
No minimal reproduction or fix/retest. Plugin list is long but not causal proof; unsupported EssentialsPE blame also appears.

## Reusable decision and costs {#reusable-decision-and-costs}
After callbacks, validate connection/lifecycle state before using resources callbacks may dispose. Preserve rejected troubleshooting advice as rejected, not a rule to reuse.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [ifvictr · 2015-10-10T03:15:24Z](https://github.com/PocketMine/PocketMine-MP/issues/3574#issuecomment-147027674).
- [wu-vincent · 2015-10-10T03:27:11Z](https://github.com/PocketMine/PocketMine-MP/issues/3574#issuecomment-147028645).
- [inxomnyaa · 2015-10-10T06:16:18Z](https://github.com/PocketMine/PocketMine-MP/issues/3574#issuecomment-147045160).
- [wu-vincent · 2015-10-10T06:25:07Z](https://github.com/PocketMine/PocketMine-MP/issues/3574#issuecomment-147045427).
- [inxomnyaa · 2015-10-10T06:39:11Z](https://github.com/PocketMine/PocketMine-MP/issues/3574#issuecomment-147046448).
- [wu-vincent · 2015-10-10T06:43:46Z](https://github.com/PocketMine/PocketMine-MP/issues/3574#issuecomment-147046596).
- [PEMapModder · 2015-10-10T06:48:05Z](https://github.com/PocketMine/PocketMine-MP/issues/3574#issuecomment-147046794).
- [wu-vincent · 2015-10-10T06:49:47Z](https://github.com/PocketMine/PocketMine-MP/issues/3574#issuecomment-147047054).
- [inxomnyaa · 2015-10-10T06:52:59Z](https://github.com/PocketMine/PocketMine-MP/issues/3574#issuecomment-147047146).
- [ghost · 2015-10-10T21:11:53Z](https://github.com/PocketMine/PocketMine-MP/issues/3574#issuecomment-147126006).
- [willowmaster66 · 2015-10-11T12:06:11Z](https://github.com/PocketMine/PocketMine-MP/issues/3574#issuecomment-147186541).
- [inxomnyaa · 2015-10-11T12:53:58Z](https://github.com/PocketMine/PocketMine-MP/issues/3574#issuecomment-147190999).
- [ghost · 2015-10-11T20:55:21Z](https://github.com/PocketMine/PocketMine-MP/issues/3574#issuecomment-147244660).
