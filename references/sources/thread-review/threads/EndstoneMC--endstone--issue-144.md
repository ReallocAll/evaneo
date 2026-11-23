<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:144"],"source_type":"public","date":"2025-02-27","topics":["concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-144-bug-crash-on-self-server-reloaddata"></a>
# EndstoneMC/endstone #144: [bug] Crash on self.server.reload_data() {#endstonemc-endstone-144-bug-crash-on-self-server-reloaddata}

Source: https://github.com/EndstoneMC/endstone/issues/144

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat supplies a concrete Windows 0.6.2.dev30 reproduction: invoke server.reload_data from an in-game command; the stack reaches EndstoneServer::reloadData. Wu links commit 42da234f10576a5c86257e84a50f6cfa0bf64f30 and the reporter explicitly confirms scripts reload without crashing. Full linked patch was inspected in the local mirror: unregisterEventListeners/registerEventListeners move from the outer reload method into reloadData, enclosing requestResourceReload and loadFunctionManager. This makes direct reloadData calls observe the same listener-lifecycle boundary as full reload, rather than protecting only one caller. The commit title itself calls this an attempted fix; the subsequent reproduction confirmation is stronger evidence for this particular scenario, not a guarantee for all reload-related failures.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/144
- https://github.com/EndstoneMC/endstone/issues/144#issuecomment-2688517625
- https://github.com/EndstoneMC/endstone/issues/144#issuecomment-2688537340
- https://github.com/EndstoneMC/endstone/commit/42da234f10576a5c86257e84a50f6cfa0bf64f30
