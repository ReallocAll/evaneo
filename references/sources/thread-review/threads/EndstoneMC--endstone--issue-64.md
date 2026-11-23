<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:64"],"source_type":"public","date":"2024-09-29","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-64-feature-add-possibility-to-perform-scriptevent-command"></a>
# EndstoneMC/endstone #64: [feature] Add possibility to perform `/scriptevent` command. {#endstonemc-endstone-64-feature-add-possibility-to-perform-scriptevent-command}

Source: https://github.com/EndstoneMC/endstone/issues/64

## Review scope and state {#review-scope-and-state}

- Thread author: oliverperzyk; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

oliverperzyk needs privileged script-event IPC while retaining entity source identity; temporarily granting OP is rejected by the requester as unsafe. tutinoko2048 initially argues the broadcast belongs outside Player; oliver clarifies entity/world origins and proposes Entity/Server methods. Wu reports testing console dispatch of execute as "player" run scriptevent, with a linked test-plugin case, as the intended way to elevate command execution while preserving actor context. zelisce notes direct console scriptevent works; oliver explains that loses entity origin. Thus the disagreement resolves two different requirements, delivery and sender identity. No new native method is established. String interpolation/escaping of player names is not validated by this thread.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/64
- https://github.com/EndstoneMC/endstone/issues/64#issuecomment-2381317529
- https://github.com/EndstoneMC/endstone/issues/64#issuecomment-2381339412
- https://github.com/EndstoneMC/endstone/issues/64#issuecomment-2381454668
- https://github.com/EndstoneMC/endstone/issues/64#issuecomment-2397871509
- https://github.com/EndstoneMC/endstone/issues/64#issuecomment-2419259680
- https://github.com/EndstoneMC/endstone/issues/64#issuecomment-2419373639
