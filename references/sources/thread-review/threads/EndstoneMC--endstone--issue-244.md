<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:244"],"source_type":"public","date":"2025-08-10","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-244-bug-endstone-server-displays-a-banned-message-if-not-whitelisted"></a>
# EndstoneMC/endstone #244: [bug] Endstone server displays a banned message if not whitelisted {#endstonemc-endstone-244-bug-endstone-server-displays-a-banned-message-if-not-whitelisted}

Source: https://github.com/EndstoneMC/endstone/issues/244

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat reports a banned-message screen for an allowlist denial on 0.10.3. Wu says vanilla BDS also exhibits it and tentatively ties it to the newly enabled disconnect UI. The reporter's proposed relation to death-message bugs remains speculation. No independently checked upstream cause or Endstone fix is supplied.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/244
- https://github.com/EndstoneMC/endstone/issues/244#issuecomment-3173888722
