<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:76"],"source_type":"public","date":"2024-10-12","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-76-bug-when-i-create-a-boss-bar-and-set-it-up-through-addplayer-the-boss-bar-is-seen-for-0-1-seconds-and-then-"></a>
# EndstoneMC/endstone #76: [bug] When I create a boss bar and set it up through add_player, the boss bar is seen for 0.1 seconds and then disappears. {#endstonemc-endstone-76-bug-when-i-create-a-boss-bar-and-set-it-up-through-addplayer-the-boss-bar-is-seen-for-0-1-seconds-and-then-}

Source: https://github.com/EndstoneMC/endstone/issues/76

## Review scope and state {#review-scope-and-state}

- Thread author: pgrd1; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

pgrd1 reports a transient bossbar and supplies a short event-handler reproduction after wu requests one. Wu cannot reproduce with the same code and closes awaiting more information. No cause or fix is established; do not infer garbage-collection lifetime from the local variable alone when the maintainer explicitly observes persistence.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/76
- https://github.com/EndstoneMC/endstone/issues/76#issuecomment-2417544801
- https://github.com/EndstoneMC/endstone/issues/76#issuecomment-2419488445
- https://github.com/EndstoneMC/endstone/issues/76#issuecomment-2420229302
- https://github.com/EndstoneMC/endstone/issues/76#issuecomment-2460257722
