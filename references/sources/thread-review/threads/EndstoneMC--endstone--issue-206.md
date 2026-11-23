<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:206"],"source_type":"public","date":"2025-06-19","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-206-bug-failed-to-install-dll-error-1114"></a>
# EndstoneMC/endstone #206: [bug]Failed to install(dll error 1114) {#endstonemc-endstone-206-bug-failed-to-install-dll-error-1114}

Source: https://github.com/EndstoneMC/endstone/issues/206

## Review scope and state {#review-scope-and-state}

- Thread author: ViciiX; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

ViciiX's Windows 1114 report initially prompts umarurize's VC runtime suggestion and Wu's speculative runner-upgrade hypothesis. The reporter links an ARM64 redistributable despite declaring amd64, then reveals a hand-edited __minecraft_version__ forcing 1.21.91 into an Endstone build expecting preview28. Wu explains the version string only changes which BDS binary is downloaded; it cannot adapt hooks/ABI. Correcting this leads to explicit successful startup, and Wu later announces 0.9.1 support. Preserve this diagnosis evolution: the final verified outcome supports mismatched binaries, not the earlier runtime speculation. The download/extraction log also shows configuration preservation; no software was installed in this review.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/206
- https://github.com/EndstoneMC/endstone/issues/206#issuecomment-2987578520
- https://github.com/EndstoneMC/endstone/issues/206#issuecomment-2987743550
- https://github.com/EndstoneMC/endstone/issues/206#issuecomment-2987870895
- https://github.com/EndstoneMC/endstone/issues/206#issuecomment-2987871844
- https://github.com/EndstoneMC/endstone/issues/206#issuecomment-2987874017
- https://github.com/EndstoneMC/endstone/issues/206#issuecomment-2987917328
- https://github.com/EndstoneMC/endstone/issues/206#issuecomment-2988011961
- https://github.com/EndstoneMC/endstone/issues/206#issuecomment-2988107284
- https://github.com/EndstoneMC/endstone/issues/206#issuecomment-2988238282
