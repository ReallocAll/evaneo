<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:318"],"source_type":"public","date":"2026-01-02","topics":["testing","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-318-feature-support-download-resources-using-mirrors"></a>
# EndstoneMC/endstone #318: [feature] Support download resources using mirrors {#endstonemc-endstone-318-feature-support-download-resources-using-mirrors}

Source: https://github.com/EndstoneMC/endstone/issues/318

## Evidence and attribution {#evidence-and-attribution}

Primary author: Mooling0602. Created 2026-01-02T05:19:45Z; recorded state closed; merged not applicable.

## Problem and alternative {#problem-and-alternative}

Mooling0602 could not reach raw.githubusercontent.com from Mainland China and supplied a requests/urllib3 read-timeout trace during bootstrap index loading. The feature request proposed a configurable acceleration mirror such as xget.

wu-vincent pointed out the existing endstone --remote option. Its default is the bedrock-server-data/v2 index; an alternative endpoint may be a GitHub mirror, CDN, self-hosted service or xget-backed endpoint provided it serves the same compatible format. The reporter accepted the workaround.

## Reusable decision and boundary {#reusable-decision-and-boundary}

Prefer an existing index indirection point to hard-coded regional special cases. This addresses index reachability; the thread does not prove every resource URL embedded in an index is rewritten or that arbitrary mirrors are trustworthy. No code change or benchmark is present.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/318
- https://github.com/EndstoneMC/endstone/issues/318#issuecomment-3704482621
- https://github.com/EndstoneMC/endstone/issues/318#issuecomment-3760832187
- https://github.com/EndstoneMC/endstone/issues/318#issuecomment-3762716390
