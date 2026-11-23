<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:19"],"source_type":"public","date":"2024-06-04","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-19-feature-allow-users-to-get-player-by-name"></a>
# EndstoneMC/endstone #19: [feature] Allow users to get player by name {#endstonemc-endstone-19-feature-allow-users-to-get-player-by-name}

Source: https://github.com/EndstoneMC/endstone/issues/19

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Title-only get-player-by-name request with completion f120c20a18b2cfc7d25a010b4f7d8f80481a61dd. Case sensitivity, ambiguity, offline behavior and lifetime are unspecified.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/19
- https://github.com/EndstoneMC/endstone/issues/19#issuecomment-2148753706
- https://github.com/EndstoneMC/endstone/commit/f120c20a18b2cfc7d25a010b4f7d8f80481a61dd
