<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:52"],"source_type":"public","date":"2024-09-15","topics":["concurrency","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-52-bug-server-crashes-when-using-a-map-with-beta-api-enabled"></a>
# EndstoneMC/endstone #52: [bug] Server crashes when using a map with beta api enabled {#endstonemc-endstone-52-bug-server-crashes-when-using-a-map-with-beta-api-enabled}

Source: https://github.com/EndstoneMC/endstone/issues/52

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu reports a beta-API-enabled map crash and supplies a world archive. The trace shows a string length_error during RakNet Send_Windows_Linux_360NoVDP string assignment followed by termination. It locates the symptom but does not prove a buffer-length/ABI cause or a fix. No comments, patch or validation are recorded. World attachment was not downloaded/executed; its behavior remains an evidence limit.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/52
