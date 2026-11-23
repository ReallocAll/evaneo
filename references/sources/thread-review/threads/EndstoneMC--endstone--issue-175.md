<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:175"],"source_type":"public","date":"2025-04-18","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-175-bug-actordamageevent-and-blockbreakevent"></a>
# EndstoneMC/endstone #175: [bug] ActorDamageEvent and BlockBreakEvent {#endstonemc-endstone-175-bug-actordamageevent-and-blockbreakevent}

Source: https://github.com/EndstoneMC/endstone/issues/175

## Review scope and state {#review-scope-and-state}

- Thread author: kleines-L; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

kleines-L distinguishes invulnerable damage-sensor/cooldown hits from actual damage, and creative sword clicks from actual block destruction. Wu's two linked patches were fully read:6fb24524cc22c216a28ee61a368a58e054c48a0d checks creative item canDestroyInCreative before emitting BlockBreakEvent; da68c2947a6f9da4cbcfd1947f0a3dc5361e7433 consults DamageSensorComponent before ActorDamageEvent, returns false for No and true for NoButSidesEffectsApply, and clarifies get/setDamage as raw damage. The fix addresses the explicitly stated damage_sensor and non-breaking-item cases; it does not transform damage into final health loss or separately demonstrate cooldown behavior. This is an important limit to the broad initial expectation: event eligibility and raw-versus-final damage are distinct API contracts.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/175
- https://github.com/EndstoneMC/endstone/issues/175#issuecomment-2889201880
- https://github.com/EndstoneMC/endstone/commit/6fb24524cc22c216a28ee61a368a58e054c48a0d
- https://github.com/EndstoneMC/endstone/commit/da68c2947a6f9da4cbcfd1947f0a3dc5361e7433
