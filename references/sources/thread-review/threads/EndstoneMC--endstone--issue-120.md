<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:120"],"source_type":"public","date":"2025-01-06","topics":["concurrency","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-120-bug-the-sendmaessage-of-commandsender-class-don-t-support-asynchrony"></a>
# EndstoneMC/endstone #120: [bug] The send_maessage of CommandSender class don't support asynchrony {#endstonemc-endstone-120-bug-the-sendmaessage-of-commandsender-class-don-t-support-asynchrony}

Source: https://github.com/EndstoneMC/endstone/issues/120

## Review scope and state {#review-scope-and-state}

- Thread author: Packeting1; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Packeting 1 starts Python threads for send_message/print while sleeping in the command handler, observing delayed messages. Wu says the Python API wraps C++ functions that do not natively support asyncio/coroutines. That clarifies lack of async contract but does not establish whether this specific delay is GIL, main-thread dispatch or blocking sleep. The example is not a sanctioned pattern for worker-thread game API access.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/120
- https://github.com/EndstoneMC/endstone/issues/120#issuecomment-2608204814
