<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:111"],"source_type":"public","date":"2024-12-23","topics":["lifetime","concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-111-bug-server-crash-when-the-actionform-callback-function-uses-sending-the-kill-command-to-kill-the-player-wh"></a>
# EndstoneMC/endstone #111: [bug]server crash when the actionform callback function uses sending the "kill" command to kill the player who opened the form! {#endstonemc-endstone-111-bug-server-crash-when-the-actionform-callback-function-uses-sending-the-kill-command-to-kill-the-player-wh}

Source: https://github.com/EndstoneMC/endstone/issues/111

## Review scope and state {#review-scope-and-state}

- Thread author: ye111566; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

ye111566 gives a deterministic ActionForm button that kills the same survival player, with onFormResponse crash. The body offers hypotheses about invalid player resources/concurrency and proposes checks, deferral or blocking self-kill; these are reporter speculation, not established diagnosis. Wu confirms fixed in latest commit but provides no SHA. Cross-reference #32: callback-induced mutation is a distinct edge case from the earlier captured-this fix. No exact final mechanism can be inferred.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/111
- https://github.com/EndstoneMC/endstone/issues/111#issuecomment-2559852013
