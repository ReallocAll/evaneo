<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:24"],"source_type":"public","date":"2024-06-30","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-24-feature-add-player-getskin"></a>
# EndstoneMC/endstone #24: [feature] Add Player::getSkin {#endstonemc-endstone-24-feature-add-player-getskin}

Source: https://github.com/EndstoneMC/endstone/issues/24

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu proposes a Skin object returned by Player::getSkin to save skins or use them for player heads. The use case/API shape are explicit; ownership, format and serialization are unspecified and no implementation is linked.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/24
