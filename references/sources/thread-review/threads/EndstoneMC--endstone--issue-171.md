<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:171"],"source_type":"public","date":"2025-04-10","topics":["concurrency","ffi","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-171-bug-serverplayer-setlocalplayerasinitialized-is-unsafe"></a>
# EndstoneMC/endstone #171: [bug] ServerPlayer::setLocalPlayerAsInitialized is unsafe {#endstonemc-endstone-171-bug-serverplayer-setlocalplayerasinitialized-is-unsafe}

Source: https://github.com/EndstoneMC/endstone/issues/171

## Review scope and state {#review-scope-and-state}

- Thread author: Atomic69420; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Atomic69420 reports repeated initialization packets causing duplicate joins, permission recalculation, and command refresh, and also questions runtime-ID validation. Wu acknowledges an overlooked issue and says it is addressed; intervening social comments add no evidence. Full matching fix583f2d97024d574fb5874dd67200f613dbcef46c was inspected: a spawned_ flag gates EndstonePlayer::doFirstSpawn, set before callbacks; incoming packet handling uses the sender's resolved player, and the old setLocalPlayerAsInitialized hook is removed. This establishes idempotence of Endstone join effects and avoids directly rewriting the native initialization flag there. It does not visibly add an explicit payload-runtime-ID comparison, so the entire reporter allegation must not be labeled independently verified fixed. No exploit execution was performed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/171
- https://github.com/EndstoneMC/endstone/issues/171#issuecomment-2794839202
- https://github.com/EndstoneMC/endstone/issues/171#issuecomment-2795084712
- https://github.com/EndstoneMC/endstone/issues/171#issuecomment-2795105345
- https://github.com/EndstoneMC/endstone/issues/171#issuecomment-2795225033
- https://github.com/EndstoneMC/endstone/issues/171#issuecomment-2798765111
