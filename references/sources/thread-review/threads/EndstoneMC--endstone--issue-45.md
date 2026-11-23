<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:45"],"source_type":"public","date":"2024-09-03","topics":["concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-45-crash-during-gameplay"></a>
# EndstoneMC/endstone #45: Crash during gameplay {#endstonemc-endstone-45-crash-during-gameplay}

Source: https://github.com/EndstoneMC/endstone/issues/45

## Review scope and state {#review-scope-and-state}

- Thread author: Nat456Gaming; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Nat456Gaming reports one Linux Mint survival crash with no plugins and no corruption after restart. The trace contains the Endstone signal handler then unsymbolized BDS frames. Wu says it appears to originate in BDS, cannot reproduce and closes pending a deterministic reproduction. That attribution is his diagnosis, not proof that hooks cannot affect BDS frames. The useful triage constraint is insufficient reproducibility/symbol information; no patch or established root cause is supplied.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/45
- https://github.com/EndstoneMC/endstone/issues/45#issuecomment-2326301246
- https://github.com/EndstoneMC/endstone/issues/45#issuecomment-2326389720
