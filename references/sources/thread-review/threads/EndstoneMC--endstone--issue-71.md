<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:71"],"source_type":"public","date":"2024-10-05","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-71-endstoneruntime-dll-access-denied"></a>
# EndstoneMC/endstone #71: endstone_runtime.dll Access denied {#endstonemc-endstone-71-endstoneruntime-dll-access-denied}

Source: https://github.com/EndstoneMC/endstone/issues/71

## Review scope and state {#review-scope-and-state}

- Thread author: TheNotEasy; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

TheNotEasy reports LoadLibrary error 5 despite permissions/admin execution and secondary OpenThread error 18. Wu initially suggests reboot/environment trouble. The reporter supplies the confirmed resolution: replace Microsoft Store Python with the traditional installer. This refines the earlier #35 filesystem-permission explanation; their claim that #35 has the same cause remains a cross-report inference, not confirmed by that reporter. Preserve environment-distribution compatibility as the actionable finding, not a blanket instruction to escalate filesystem privileges.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/71
- https://github.com/EndstoneMC/endstone/issues/71#issuecomment-2395007943
- https://github.com/EndstoneMC/endstone/issues/71#issuecomment-2395250925
