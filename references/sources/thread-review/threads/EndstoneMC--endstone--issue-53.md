<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:53"],"source_type":"public","date":"2024-09-15","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-53-bug-command-sender-should-be-player-when-using-player-performcommand"></a>
# EndstoneMC/endstone #53: [bug] Command sender should be player when using `Player::performCommand` {#endstonemc-endstone-53-bug-command-sender-should-be-player-when-using-player-performcommand}

Source: https://github.com/EndstoneMC/endstone/issues/53

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu specifies that Player::performCommand must preserve a Player sender when invoking a plugin command. Existing VirtualCommandOrigin is converted to generic CommandSender, losing player identity at callback. The requirement is semantic origin round-tripping, not merely successful text execution. No implementation is shown; contrast with ScriptAPI proxy origins in #61, which have distinct semantics and cannot be blindly cast to Player.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/53
