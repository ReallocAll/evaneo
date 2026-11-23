<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:91"],"source_type":"public","date":"2024-11-15","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-91-feature-add-source-attribute-for-actordeathevent-and-isplayer-attribute-for-actor"></a>
# EndstoneMC/endstone #91: [feature]Add source attribute for ActorDeathEvent and is_player attribute for Actor {#endstonemc-endstone-91-feature-add-source-attribute-for-actordeathevent-and-isplayer-attribute-for-actor}

Source: https://github.com/EndstoneMC/endstone/issues/91

## Review scope and state {#review-scope-and-state}

- Thread author: umarurize; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

umarurize requests killer/source access and Actor.is_player. xXLarryTFVWXx suggests Python isinstance based on inheritance; wu confirms isinstance(actor, Player) and reports damage-source actor at event.damage_source.actor, linked to 9d28eeab006debc63c5484097bd00c0b28bed33d. Final API carries a richer damage source rather than merely the originally requested direct source field, and reuses type relationships rather than adding a redundant boolean. Null/environmental source semantics are not described.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/91
- https://github.com/EndstoneMC/endstone/issues/91#issuecomment-2508893976
- https://github.com/EndstoneMC/endstone/issues/91#issuecomment-2614132487
- https://github.com/EndstoneMC/endstone/commit/9d28eeab006debc63c5484097bd00c0b28bed33d
