<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endweave:7"],"source_type":"public","date":"2026-03-30","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endweave-7-fix-map-biome-definitions-for-v898-to-v924"></a>
# EndstoneMC/endweave #7: fix: map biome definitions for v898 to v924 {#endstonemc-endweave-7-fix-map-biome-definitions-for-v898-to-v924}

Source: https://github.com/EndstoneMC/endweave/pull/7

## Evidence and attribution {#evidence-and-attribution}

Primary author: Caldron47. Created 2026-03-30T12:55:59Z; recorded state closed; merged True.

Caldron47's biome-definition mapping patch has an empty description and Wu's LGTM. Understand correctness from the patch, not the approval alone.

## Direct patch findings {#direct-patch-findings}

Registers BIOME_DEFINITION_LIST clientbound handler, passes count and USHORT string index then maps BIOME_DEFINITION_V898→V924 for each entry. The villageType default is delegated to existing codecs rather than written inline. No test added.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (1793 characters; SHA-256 1f1fc767ab8a3e9633f2dd5ee284111ea73de4675617d071c487824daf57f0f6), head c101922c1b137d559d199276b111f518c20c1bd1. This covers the supplied PR patch, not unrelated commits or historical intermediate revisions. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endweave/pull/7
- https://github.com/EndstoneMC/endweave/pull/7#issuecomment-4154959556
