<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:15"],"source_type":"public","date":"2024-05-31","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-15-feature-allow-developers-to-modify-vanilla-commands"></a>
# EndstoneMC/endstone #15: [feature] Allow developers to modify vanilla commands {#endstonemc-endstone-15-feature-allow-developers-to-modify-vanilla-commands}

Source: https://github.com/EndstoneMC/endstone/issues/15

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu demonstrates denying a vanilla command through an individual player attachment: player.add_attachment(plugin, "minecraft.command.me", False). This narrows the broad modify-command request to permission-mediated disabling for that player. It does not establish deregistration, parser modification or global disabling; no patch/test is linked.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/15
- https://github.com/EndstoneMC/endstone/issues/15#issuecomment-2186877987
