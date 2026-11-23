<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:72"],"source_type":"public","date":"2024-10-07","topics":["concurrency","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-72-feature-add-i18n-api-for-multilingual-support-in-endstone"></a>
# EndstoneMC/endstone #72: [feature] Add i18n API for Multilingual Support in Endstone {#endstonemc-endstone-72-feature-add-i18n-api-for-multilingual-support-in-endstone}

Source: https://github.com/EndstoneMC/endstone/issues/72

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu proposes namespace-directed localization: endstone.* keys translated on server using Endstone files; other keys fall back to BDS language files when needed and translatable client messages remain intact so resource packs can localize them. Explicit server translation is exposed through getLanguage().translate(key, params), inspired by PocketMine/Nukkit. This separates translation ownership and client extensibility. Only emoji/stale-bot replies follow, so implementation and exact fallback semantics are not established.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/72
- https://github.com/EndstoneMC/endstone/issues/72#issuecomment-2398214233
- https://github.com/EndstoneMC/endstone/issues/72#issuecomment-2525310232
- https://github.com/EndstoneMC/endstone/issues/72#issuecomment-2560294745
