<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:73"],"source_type":"public","date":"2024-10-07","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-73-feature-add-an-event-for-scriptevent-command"></a>
# EndstoneMC/endstone #73: [feature] Add an event for `/scriptevent` command {#endstonemc-endstone-73-feature-add-an-event-for-scriptevent-command}

Source: https://github.com/EndstoneMC/endstone/issues/73

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu proposes ScriptEventCommandEvent carrying sender, message_id and message to bridge plugins with scripting add-ons, referencing the Script API after-event. A completion commit 2b6111f39e1c83ae41a4570bfe41849b51f05e97 is linked. The discussion specifies envelope identity and payload rather than a language-specific IPC transport. Delivery timing, cancellation and sender subtype handling require implementation review, not inference from the proposed name.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/73
- https://github.com/EndstoneMC/endstone/issues/73#issuecomment-2420135371
- https://github.com/EndstoneMC/endstone/commit/2b6111f39e1c83ae41a4570bfe41849b51f05e97
