<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:141"],"source_type":"public","date":"2025-02-23","topics":["concurrency","recovery","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-141-bug-unknown-crash"></a>
# EndstoneMC/endstone #141: [bug] Unknown crash {#endstonemc-endstone-141-bug-unknown-crash}

Source: https://github.com/EndstoneMC/endstone/issues/141

## Review scope and state {#review-scope-and-state}

- Thread author: SuperEric1; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

SuperEric1 reports a crash triggered by one particular player joining, with no reliable reproduction. Wu attributes the stack to deserializing that player's stored world data and suggests malformed/corrupt player data in BDS, with removal as a possible recovery for someone who knows world-data editing. This is a maintainer diagnosis, not a demonstrated root cause or an independently verified safe repair; the unknown native frames alone do not establish causality. No patch or confirmation of successful recovery appears. Preserve backups and investigate the specific saved record before treating destructive data removal as a general remedy.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/141
- https://github.com/EndstoneMC/endstone/issues/141#issuecomment-2677136649
