<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:277"],"source_type":"public","date":"2025-10-14","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-277-player-walkspeed-doesn-t-do-anything"></a>
# EndstoneMC/endstone #277: player.walk_speed doesn't do anything {#endstonemc-endstone-277-player-walkspeed-doesn-t-do-anything}

Source: https://github.com/EndstoneMC/endstone/issues/277

## Review scope and state {#review-scope-and-state}

- Thread author: kleines-L; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

kleines-L reports walk_speed property changes without physical movement change, unlike fly_speed. Wu links ea77de244420de9d2592d7e62104d274218b6a70 for 0.10.11. Full patch read: getter switches from stored ability float to native getSpeed; setter still sets/syncs ability but additionally writes current minecraft:movement attribute. Thus the old API updated a representation without the effective movement attribute. No bounds/null-attribute handling or reporter retest is demonstrated; this is a targeted state-synchronization repair, not evidence that arbitrary speed values are safe.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/277
- https://github.com/EndstoneMC/endstone/issues/277#issuecomment-3494641530
- https://github.com/EndstoneMC/endstone/commit/ea77de244420de9d2592d7e62104d274218b6a70
