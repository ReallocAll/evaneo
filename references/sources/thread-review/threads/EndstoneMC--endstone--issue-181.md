<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:181"],"source_type":"public","date":"2025-05-18","topics":["concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-181-bug-crash-when-executing-dispatchcommand-with-asynic-function"></a>
# EndstoneMC/endstone #181: [bug] Crash when executing dispatch_command with asynic function {#endstonemc-endstone-181-bug-crash-when-executing-dispatchcommand-with-asynic-function}

Source: https://github.com/EndstoneMC/endstone/issues/181

## Review scope and state {#review-scope-and-state}

- Thread author: pgrd1; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

pgrd1 invokes dispatch_command from endstone.asyncio.run and crashes during a give command. Wu asks for code, then explains this module uses a separate thread for I/O while BDS game logic requires the main server thread. He attributes the stack's sanity-check failure to thread-local ItemRegistry not being initialized on the async thread. The supplied coroutine has no await, so making it async adds no asynchronous I/O benefit. The reporter accepts the explanation. The reusable boundary is to keep game-state access on the server thread and marshal I/O results appropriately; the thread contains no scheduling adapter or proof that every Endstone call is thread-safe. The exact BDS diagnosis is attributed to Wu, not independently debugged here.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/181
- https://github.com/EndstoneMC/endstone/issues/181#issuecomment-2888936135
- https://github.com/EndstoneMC/endstone/issues/181#issuecomment-2888938673
- https://github.com/EndstoneMC/endstone/issues/181#issuecomment-2888973342
- https://github.com/EndstoneMC/endstone/issues/181#issuecomment-2889035234
