<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:219"],"source_type":"public","date":"2025-07-19","topics":["lifetime","concurrency","ffi","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-219-bug-reloaddata-function-crashs-the-server-with-script-api"></a>
# EndstoneMC/endstone #219: [bug] .reload_data() function crashs the server with script api {#endstonemc-endstone-219-bug-reloaddata-function-crashs-the-server-with-script-api}

Source: https://github.com/EndstoneMC/endstone/issues/219

## Review scope and state {#review-scope-and-state}

- Thread author: usxrDev; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

usxrDev demonstrates reload_data succeeding through native scriptevent but crashing when a Script API custom/r command calls scriptevent, even through system.run. Wu explains reload destroys/recreates the Script API command registry while the custom command's callback is still in flight and must return its status; native scriptevent is outside that registry. He is unsure Endstone can solve it. This is a reentrant teardown/lifetime problem, not generic proof that reload_data always crashes, and scheduling one intermediate call does not necessarily unwind the owning callback stack. No patch or safe deferred-reload implementation is supplied; the explanation remains the maintainer's diagnosis.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/219
- https://github.com/EndstoneMC/endstone/issues/219#issuecomment-3095931377
