<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:142"],"source_type":"public","date":"2025-02-24","topics":["concurrency","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-142-feature"></a>
# EndstoneMC/endstone #142: [feature] {#endstonemc-endstone-142-feature}

Source: https://github.com/EndstoneMC/endstone/issues/142

## Review scope and state {#review-scope-and-state}

- Thread author: palmmc; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

palmmc wants a plugin to replace or unregister vanilla command names, especially help; choosing a different name preserves compatibility but hurts usability. Wu explains the existing compatibility policy by comparison to Nukkit/PocketMine: vanilla commands are integrated with server behavior, so overriding them is avoided. He separately says the help screen is implemented client-side, making a server-side override insufficient. Wu is unsure whether a hidden configuration or commands.json can disable commands and invites exploration rather than promising support. xXLarryTFVWXx suggests a double-slash prefix; Slauh later links a commands.json example and palmmc considers that ideal. The external attachment is not independently inspected, so it remains another participant's workaround rather than an established API contract. No implementation or final supported override mechanism is established. Quoted email/unsubscribe material contributes no engineering evidence and is not reproduced.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/142
- https://github.com/EndstoneMC/endstone/issues/142#issuecomment-2745403510
- https://github.com/EndstoneMC/endstone/issues/142#issuecomment-2745892500
- https://github.com/EndstoneMC/endstone/issues/142#issuecomment-2745928929
- https://github.com/EndstoneMC/endstone/issues/142#issuecomment-2746274192
