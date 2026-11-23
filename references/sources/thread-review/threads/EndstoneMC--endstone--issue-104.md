<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:104"],"source_type":"public","date":"2024-12-06","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-104-addition-moderation-commands"></a>
# EndstoneMC/endstone #104: Addition Moderation Commands {#endstonemc-endstone-104-addition-moderation-commands}

Source: https://github.com/EndstoneMC/endstone/issues/104

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat requests temporary bans, mute durations and punishment history. smartcmd suggests /ability, but PrimeStrat notes education-mode dependence and lack of reasons. Wu chooses plugin implementation over built-in moderation policy, committing only to expose the ban API. This separates reusable capability from server-specific policy/workflow; it is not rejection of moderation needs or acceptance of the workaround.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/104
- https://github.com/EndstoneMC/endstone/issues/104#issuecomment-2525051896
- https://github.com/EndstoneMC/endstone/issues/104#issuecomment-2525110948
- https://github.com/EndstoneMC/endstone/issues/104#issuecomment-2552329432
