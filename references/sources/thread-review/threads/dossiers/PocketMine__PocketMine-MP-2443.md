<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:2443"],"source_type":"public","date":"2014-12-24","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-2443-bug-in-unconnected-pong"></a>
# PocketMine/PocketMine-MP#2443: BUG in unconnected pong {#pocketmine-pocketmine-mp-2443-bug-in-unconnected-pong}

Source: https://github.com/PocketMine/PocketMine-MP/issues/2443

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Vincent proposed changing unconnected-pong MOTD prefix from Demo to MINECON for protocol20.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
shoghicp said both prefixes worked and old prefix was unnecessary, offering to inform another contributor if vanilla defaulted to MINECON.

## Implementation and attribution {#implementation-and-attribution}
No patch/capture.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
No compatibility failure established.

## Reusable decision and costs {#reusable-decision-and-costs}
Distinguish observed canonical format from required accepted format.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [shoghicp · 2014-12-24T13:46:18Z](https://github.com/PocketMine/PocketMine-MP/issues/2443#issuecomment-68053089).
