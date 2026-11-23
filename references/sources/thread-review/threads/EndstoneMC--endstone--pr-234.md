<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:234"],"source_type":"public","date":"2025-08-01","topics":["ffi","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-234-feat-improve-actordeathevent-and-playerdeathevent-wip"></a>
# EndstoneMC/endstone #234: [feat] Improve `ActorDeathEvent` and `PlayerDeathEvent` (WIP) {#endstonemc-endstone-234-feat-improve-actordeathevent-and-playerdeathevent-wip}

Source: https://github.com/EndstoneMC/endstone/pull/234

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: False.
- Evidence: Public PR and patch reviewed statically (273 additions, 55 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu's unmerged 234 extends 233's pre-death-hook proposal with dropped_exp on ActorDeathEvent and Python bindings. Full 16-file patch read. It obtains the native death XP before callbacks, then replaces ExperienceRewardComponent's death expression with a constant reflecting the event; player and non-player paths are handled separately. Documentation correctly distinguishes XP spawned from XP removed from an entity. The patch still does not implement keep-inventory/level or respawn-level methods promised in the body. New ExpressionNode copy code copies the base IComplexExpression rather than cloning a dynamic subtype, so it cannot be assumed to preserve arbitrary complex-expression semantics. The temporary reward initialization also replaces bred/death expression vectors, not merely a scalar. This incomplete proposal was closed by stale automation, not merged; no runtime validation is present.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/234
- https://github.com/EndstoneMC/endstone/pull/234#issuecomment-3393657463
- https://github.com/EndstoneMC/endstone/pull/234#issuecomment-3448923224
