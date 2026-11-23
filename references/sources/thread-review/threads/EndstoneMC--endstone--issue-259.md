<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:259"],"source_type":"public","date":"2025-08-27","topics":["concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-259-bug-crash-on-armor-item-get-example-player-inventory-helmet"></a>
# EndstoneMC/endstone #259: [bug] crash on armor item get (example: player.inventory.helmet) {#endstonemc-endstone-259-bug-crash-on-armor-item-get-example-player-inventory-helmet}

Source: https://github.com/EndstoneMC/endstone/issues/259

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat initially reports helmet access in PlayerQuitEvent, then broadens it to any armor read and suspects custom-item addons even when no armor is worn. Wu cannot reproduce without addons; private-pack sharing is discussed but the pack is not public evidence. Reporter confirms no crashes on 0.10.5.dev60, while Wu explicitly remains uncertain about root cause and says the fix is based on guesses. Subsequent 265 reports a new failure on that same build. Keep the successful retest bounded to its observed scenario and duration; do not promote a tentative workaround into a proven lifetime or addon root cause.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/259
- https://github.com/EndstoneMC/endstone/issues/259#issuecomment-3229877198
- https://github.com/EndstoneMC/endstone/issues/259#issuecomment-3234717572
- https://github.com/EndstoneMC/endstone/issues/259#issuecomment-3263886914
- https://github.com/EndstoneMC/endstone/issues/259#issuecomment-3264037539
- https://github.com/EndstoneMC/endstone/issues/259#issuecomment-3266539173
- https://github.com/EndstoneMC/endstone/issues/259#issuecomment-3267399134
- https://github.com/EndstoneMC/endstone/issues/259#issuecomment-3267458902
- https://github.com/EndstoneMC/endstone/issues/259#issuecomment-3268386489
