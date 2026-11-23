<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3034"],"source_type":"public","date":"2015-05-19","topics":["concurrency","testing","build","diagnosis","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3034-server-crash-build-1147-while-joining-client-build-11"></a>
# PocketMine/PocketMine-MP#3034: server crash build 1147 while joining client build 11 {#pocketmine-pocketmine-mp-3034-server-crash-build-1147-while-joining-client-build-11}

Source: https://github.com/PocketMine/PocketMine-MP/issues/3034

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Joining build1147 crashed calling getX on integer in Level chunk ticking.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent confirmed same error; shoghicp identified fix0c6d8b9.

## Implementation and attribution {#implementation-and-attribution}
Full stack/context read: loaders iteration assumes objects, actual value integer; chunk coordinate/hash variables in excerpt also warrant checking. Linked fix not inspected yet.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Specific failure established, fix attribution not independently verified.

## Reusable decision and costs {#reusable-decision-and-costs}
Collection value/key shape is an API invariant; inspect its producer rather than treating a method call failure as plugin blame.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2015-05-19T12:43:57Z](https://github.com/PocketMine/PocketMine-MP/issues/3034#issuecomment-103472446).
- [shoghicp · 2015-05-19T12:50:11Z](https://github.com/PocketMine/PocketMine-MP/issues/3034#issuecomment-103473845).

## Supplemental verification (supersedes earlier acquisition gaps) {#supplemental-verification-supersedes-earlier-acquisition-gaps}
Full linked 0c6d8b9 commit fetched and read. Level separates loaderCounter (integer reference counts) from loaders (ChunkLoader objects), registers/removes them together, and uses chunkX/chunkZ rather than undefined x/z for tick hashes. This directly explains getX being called on an integer. An unrelated armor packet change sets the network channel before encoding/reuse. No local execution or tests.
