<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:106"],"source_type":"public","date":"2024-12-10","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-106-bug-setting-player-allowflight-to-false-in-playerjoinevent-handler-causes-players-to-lose-the-ability-to-b"></a>
# EndstoneMC/endstone #106: [bug] setting `Player.allow_flight` to `False` in `PlayerJoinEvent` handler causes players to lose the ability to break blocks {#endstonemc-endstone-106-bug-setting-player-allowflight-to-false-in-playerjoinevent-handler-causes-players-to-lose-the-ability-to-b}

Source: https://github.com/EndstoneMC/endstone/issues/106

## Review scope and state {#review-scope-and-state}

- Thread author: ye111566; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

ye111566 inconsistently reports setting allow_flight False versus example True; wu asks where it happens and isolates PlayerJoinEvent. He attributes loss of block interaction to a known client-side timing bug and recommends a command or delayed task rather than setting it directly during join. Do not normalize away the True/False inconsistency or promise a particular delay. The observation is lifecycle-sensitive ability updates, with a workaround but no code fix/test.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/106
- https://github.com/EndstoneMC/endstone/issues/106#issuecomment-2530857466
- https://github.com/EndstoneMC/endstone/issues/106#issuecomment-2546009253
- https://github.com/EndstoneMC/endstone/issues/106#issuecomment-2546038220
- https://github.com/EndstoneMC/endstone/issues/106#issuecomment-2546042180
- https://github.com/EndstoneMC/endstone/issues/106#issuecomment-2546165680
- https://github.com/EndstoneMC/endstone/issues/106#issuecomment-2546175114
