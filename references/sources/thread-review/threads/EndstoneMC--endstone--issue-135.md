<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:135"],"source_type":"public","date":"2025-02-19","topics":["concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-135-bug-crash-on-player-spawn"></a>
# EndstoneMC/endstone #135: [bug] Crash on player spawn {#endstonemc-endstone-135-bug-crash-on-player-spawn}

Source: https://github.com/EndstoneMC/endstone/issues/135

## Review scope and state {#review-scope-and-state}

- Thread author: SuperEric1; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

SuperEric1’s no-plugin player-spawn crash with private add-ons reaches EndstoneProxiedCommandSender::hasPermission. Wu asks specifically about execute-as on spawn; reporter confirms a private mcfunction and offers Discord sharing. Wu reports release 0.6.1 fixes it. Private code was not accessed. kleines-L later reports behavior-pack-dependent silent disconnect, which is a different symptom not resolved in this thread. Do not merge it into the fixed crash.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/135
- https://github.com/EndstoneMC/endstone/issues/135#issuecomment-2670036165
- https://github.com/EndstoneMC/endstone/issues/135#issuecomment-2670043908
- https://github.com/EndstoneMC/endstone/issues/135#issuecomment-2671381243
- https://github.com/EndstoneMC/endstone/issues/135#issuecomment-2671395201
