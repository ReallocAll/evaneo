<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:233"],"source_type":"public","date":"2025-08-01","topics":["ffi","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-233-feat-improve-playerdeathevent-wip"></a>
# EndstoneMC/endstone #233: [feat] Improve `PlayerDeathEvent` (WIP) {#endstonemc-endstone-233-feat-improve-playerdeathevent-wip}

Source: https://github.com/EndstoneMC/endstone/pull/233

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: False.
- Evidence: Public PR and patch reviewed statically (45 additions, 42 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu's closed/unmerged PlayerDeathEvent proposal seeks pre-death access plus keep-inventory/level and respawn-experience controls, referencing Bukkit. Full 4-file patch read: remove post-damage dead-player handling, hook ServerPlayer::die, emit the event/send death info/broadcast before calling original die, and add platform symbols. It does not add the promised inventory/level controls. Death-info uses the original native message while broadcast uses the event-mutated optional message, an existing distinction carried into the proposed path. The proposal is neither shipped nor a completed Bukkit-equivalent contract;234 is a related unmerged extension.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/233
