<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:167"],"source_type":"public","date":"2025-03-29","topics":["concurrency","ffi","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-167-bug-resource-pack-hook-crash---linux"></a>
# EndstoneMC/endstone #167: [bug] Resource Pack Hook Crash - Linux {#endstonemc-endstone-167-bug-resource-pack-hook-crash---linux}

Source: https://github.com/EndstoneMC/endstone/issues/167

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat's host upgrades BDS to 1.21.71 while running Endstone 0.7.1 built for 1.21.70, producing a ResourcePackRepository hook-too-short error. Wu identifies version mismatch, later releases 0.7.2 compatibility, but explicitly declines a same-day-support guarantee and argues Endstone should manage the BDS version. ImKringle, identifying as a Bisect Hosting employee, reports changing the host updater to skip its independent BDS update when Endstone is enabled; reporter thanks both fixes. This preserves two remedies: immediate compatible release and ownership of version coordination to prevent recurrence. The hosting script itself is not public in the thread and its implementation was not independently inspected.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/167
- https://github.com/EndstoneMC/endstone/issues/167#issuecomment-2763212883
- https://github.com/EndstoneMC/endstone/issues/167#issuecomment-2763338462
- https://github.com/EndstoneMC/endstone/issues/167#issuecomment-2763579020
- https://github.com/EndstoneMC/endstone/issues/167#issuecomment-2763639639
- https://github.com/EndstoneMC/endstone/issues/167#issuecomment-2763642354
- https://github.com/EndstoneMC/endstone/issues/167#issuecomment-2763679764
