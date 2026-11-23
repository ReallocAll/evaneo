<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:130"],"source_type":"public","date":"2025-02-04","topics":["concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-130-bug-crash-on-reload-with-a-player-logged-in"></a>
# EndstoneMC/endstone #130: [bug] Crash on reload with a player logged in. {#endstonemc-endstone-130-bug-crash-on-reload-with-a-player-logged-in}

Source: https://github.com/EndstoneMC/endstone/issues/130

## Review scope and state {#review-scope-and-state}

- Thread author: palmmc; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

palmmc gives a reproducible reload-with-online-players crash in dirtyPermissibles during default-permission re-registration. Wu links 391585f17c34d09a1af4330ee39e20610d85d794 as likely duplicate of #115; reporter says latest dev build no longer crashes. This adds stronger reproduction/retest evidence to the permissions/broadcast lifecycle cluster, but exact patch mechanism is not read here.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/130
- https://github.com/EndstoneMC/endstone/issues/130#issuecomment-2637362989
- https://github.com/EndstoneMC/endstone/issues/130#issuecomment-2637542408
- https://github.com/EndstoneMC/endstone/commit/391585f17c34d09a1af4330ee39e20610d85d794
