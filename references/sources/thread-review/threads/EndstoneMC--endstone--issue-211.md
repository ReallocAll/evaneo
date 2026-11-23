<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:211","public:thread:EndstoneMC/endstone:222"],"source_type":"public","date":"2025-07-05..2025-07-21","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-211-feature-ability-to-write-to-subprocesses"></a>
# EndstoneMC/endstone #211: [feature] Ability to write to subprocesses {#endstonemc-endstone-211-feature-ability-to-write-to-subprocesses}

Source: https://github.com/EndstoneMC/endstone/issues/211

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

<a id="engineering-reading-and-attribution"></a>
## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat needs inherited subprocess stdin for console commands, particularly graceful stop and cross-world coordination. Their Flask workaround has reload/reconnection limitations. Wu says the latest dev build should support it, but the reporter is away and supplies no retest before the captured end. PR222 contains the implementation; issue comments alone establish the requirement and author-reported availability, not completion of the downstream multiworld plugin.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/211
- https://github.com/EndstoneMC/endstone/issues/211#issuecomment-3097677512
- https://github.com/EndstoneMC/endstone/issues/211#issuecomment-3097686410
- https://github.com/EndstoneMC/endstone/issues/211#issuecomment-3097689592
