<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:47"],"source_type":"public","date":"2024-09-04","topics":["concurrency","ffi","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-47-bug-i-can-t-load-dll-plugins"></a>
# EndstoneMC/endstone #47: [bug]I can't Load DLL Plugins {#endstonemc-endstone-47-bug-i-can-t-load-dll-plugins}

Source: https://github.com/EndstoneMC/endstone/issues/47

## Review scope and state {#review-scope-and-state}

- Thread author: wellwhz; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

wellwhz runs Docker on Windows and expects a DLL plugin to load while wheels work. Wu distinguishes host OS from container runtime: the image runs Linux and requires a .so plugin. The evidence concerns native binary format/ABI, not a general inability to load C++ plugins. No successful retry is recorded.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/47
- https://github.com/EndstoneMC/endstone/issues/47#issuecomment-2329480811
