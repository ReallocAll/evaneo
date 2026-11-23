<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:237"],"source_type":"public","date":"2025-08-05","topics":["concurrency","ffi","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-237-bug-unknown-crash"></a>
# EndstoneMC/endstone #237: [bug] Unknown Crash {#endstonemc-endstone-237-bug-unknown-crash}

Source: https://github.com/EndstoneMC/endstone/issues/237

## Review scope and state {#review-scope-and-state}

- Thread author: pgrd1; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

pgrd1's crash stack is in pybind11 virtual-base traversal/deregister_instance during Python object deallocation, with orjson further down. Wu first suspects cached invalid Player objects, then warns is_valid may itself be unsafe on a dangling wrapper and recommends retaining UUID/reacquiring. Later the same day he identifies pybind11 virtual inheritance issue 3514 and says virtual inheritance was removed. This revises both the diagnosis and the earlier182 advice; do not label the report a proven user caching error.

Full matching fix7920948b39326224d431ac446feb690f3b5f6242 inspected across 19 files: remove virtual inheritance from public Item/Mob/Player/command-sender interfaces and implementation bases, add explicit forwarding macros/overrides to disambiguate repeated interface paths, cast command senders via intended interfaces, and remove multiple_inheritance annotations where shown. It is a hierarchy/binding workaround, not a universal invalid-reference guard or the promised exception conversion. The upstream issue is cited as Wu's external diagnosis, not independently reviewed here.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/237
- https://github.com/EndstoneMC/endstone/issues/237#issuecomment-3155592113
- https://github.com/EndstoneMC/endstone/issues/237#issuecomment-3155598642
- https://github.com/EndstoneMC/endstone/issues/237#issuecomment-3155609446
- https://github.com/EndstoneMC/endstone/issues/237#issuecomment-3155615009
- https://github.com/EndstoneMC/endstone/issues/237#issuecomment-3155615292
- https://github.com/EndstoneMC/endstone/issues/237#issuecomment-3155617448
- https://github.com/EndstoneMC/endstone/issues/237#issuecomment-3156846459
