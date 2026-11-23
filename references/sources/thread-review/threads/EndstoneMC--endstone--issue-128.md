<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:128"],"source_type":"public","date":"2025-01-28","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-128-bug-it-seems-to-occured-a-conflict-between-the-plugin-and-the-behavior-pack"></a>
# EndstoneMC/endstone #128: [bug] It seems to occured  a conflict between the plugin and the behavior pack. {#endstonemc-endstone-128-bug-it-seems-to-occured-a-conflict-between-the-plugin-and-the-behavior-pack}

Source: https://github.com/EndstoneMC/endstone/issues/128

## Review scope and state {#review-scope-and-state}

- Thread author: JinHyone; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

JinHyone suspects overlapping ScriptAPI/plugin handlers, supplies dev94 startup trace, then confirms latest build resolves it after wu requests upgrading. This is a version-sensitive resolved report related to #127; overlap remains the reporter’s hypothesis, not an established causal rule.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/128
- https://github.com/EndstoneMC/endstone/issues/128#issuecomment-2618947261
- https://github.com/EndstoneMC/endstone/issues/128#issuecomment-2619120491
- https://github.com/EndstoneMC/endstone/issues/128#issuecomment-2620755800
