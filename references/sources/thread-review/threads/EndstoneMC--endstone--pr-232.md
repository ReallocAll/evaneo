<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:232"],"source_type":"public","date":"2025-07-27","topics":["review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-232-avg-tps-shows-own-color"></a>
# EndstoneMC/endstone #232: Avg TPS shows own color {#endstonemc-endstone-232-avg-tps-shows-own-color}

Source: https://github.com/EndstoneMC/endstone/pull/232

## Review scope and state {#review-scope-and-state}

- Thread author: MisledWater79; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (17 additions, 6 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

MisledWater79's merged status fix snapshots current/average TPS separately and computes each color against the same <12 red,<17 gold,otherwise green thresholds. Average TPS and its MSPT line now use average-derived color instead of current-derived color. Full small patch read; Wu approves. This corrects diagnostic presentation, not tick measurement or server performance.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/232
- https://github.com/EndstoneMC/endstone/pull/232#issuecomment-3126618537
