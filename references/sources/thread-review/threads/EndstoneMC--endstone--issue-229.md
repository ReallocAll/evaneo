<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:229","public:thread:EndstoneMC/endstone:254"],"source_type":"public","date":"2025-07-25..2025-08-25","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-229-feature-add-format-support-to-playerchatevent"></a>
# EndstoneMC/endstone #229: [feature] Add format support to PlayerChatEvent {#endstonemc-endstone-229-feature-add-format-support-to-playerchatevent}

Source: https://github.com/EndstoneMC/endstone/issues/229

## Review scope and state {#review-scope-and-state}

- Thread author: Znofficial; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

<a id="engineering-reading-and-attribution"></a>
## Engineering reading and attribution {#engineering-reading-and-attribution}

Znofficial asks for Bukkit-like chat formatting, reliable cancellation with multiple plugins, and optional prefix lookup. Wu plans format support and later points to 254/API 0.11; he recommends event.cancel over the deprecated cancelled property and HIGHEST handlers for final pipeline changes. This acknowledges handler ordering and later plugins' ability to overwrite state rather than guaranteeing an irreversible cancellation latch. The optional prefix hook is not promised. PR254 carries code review; this issue preserves the motivating ecosystem interoperability concern.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/229
- https://github.com/EndstoneMC/endstone/issues/229#issuecomment-3127815266
- https://github.com/EndstoneMC/endstone/issues/229#issuecomment-3221035786
