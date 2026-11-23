<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:51"],"source_type":"public","date":"2024-09-14","topics":["concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-51-gametest-simulated-players-causes-server-crash"></a>
# EndstoneMC/endstone #51: GameTest Simulated Players Causes Server Crash {#endstonemc-endstone-51-gametest-simulated-players-causes-server-crash}

Source: https://github.com/EndstoneMC/endstone/issues/51

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat provides a GameTest-based simulated-player creation manager with deferred jobs, polling results and teleport after creation. The Windows 0.5.3 trace reaches EndstonePlayer storage emplacement from Player::teleportTo, rather than only external BDS frames. Wu confirms a bug and links cc22e6e85a3ed76ee8e11fc8d8116d405ba53dbc as fixed. The reproduction demonstrates simulated players exercise lifecycle assumptions unlike normal network joins; the exact failing invariant requires linked-code inspection and is not stated by wu here. No independent post-fix execution occurred.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/51
- https://github.com/EndstoneMC/endstone/issues/51#issuecomment-2351067577
- https://github.com/EndstoneMC/endstone/issues/51#issuecomment-2354075242
- https://github.com/EndstoneMC/endstone/commit/cc22e6e85a3ed76ee8e11fc8d8116d405ba53dbc
