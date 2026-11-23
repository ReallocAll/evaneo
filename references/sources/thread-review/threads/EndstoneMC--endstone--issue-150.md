<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:150","public:thread:EndstoneMC/endstone:180"],"source_type":"public","date":"2025-03-06..2025-05-16","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-150-bug-permission-error"></a>
# EndstoneMC/endstone #150: [bug] Permission Error? {#endstonemc-endstone-150-bug-permission-error}

Source: https://github.com/EndstoneMC/endstone/issues/150

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

<a id="engineering-reading-and-attribution"></a>
## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat expects a minecraft.command.kick attachment to authorize a non-operator regardless of visitor/member/operator status. Wu first states that the existing Command/Permission API design does not support this use case, then reports implementation in PR180 for the next release. The temporal distinction matters: a limitation of the earlier design becomes an asserted forthcoming capability, rather than evidence that arbitrary permission attachments always overrode native permission levels. PR180's dossier carries the separate implementation review; no standalone code change or user retest is present here.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/150
- https://github.com/EndstoneMC/endstone/issues/150#issuecomment-2852334101
- https://github.com/EndstoneMC/endstone/issues/150#issuecomment-2887822669
- https://github.com/EndstoneMC/endstone/issues/150#issuecomment-2889125721
