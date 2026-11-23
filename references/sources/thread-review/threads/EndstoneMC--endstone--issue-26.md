<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:26"],"source_type":"public","date":"2024-07-24","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-26-feature-add-a-reload-command"></a>
# EndstoneMC/endstone #26: [feature] Add a /reload command {#endstonemc-endstone-26-feature-add-a-reload-command}

Source: https://github.com/EndstoneMC/endstone/issues/26

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu requests unloading/reloading all plugins from disk to shorten development iteration, then links eac008b4f0794c668c3a1fb12fdfc1ce2759c8e5 as completion. This establishes a lifecycle goal, not proof that tasks, callbacks and native resources are safely cleared. Later reload failures must qualify production applicability; linked implementation not read here.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/26
- https://github.com/EndstoneMC/endstone/issues/26#issuecomment-2273791652
- https://github.com/EndstoneMC/endstone/commit/eac008b4f0794c668c3a1fb12fdfc1ce2759c8e5
