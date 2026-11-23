<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/cpp-example-plugin:1"],"source_type":"public","date":"2024-07-29","topics":["concurrency","build","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-cpp-example-plugin-1-i-can-t-build-the-example-plugin"></a>
# EndstoneMC/cpp-example-plugin #1: I can't build the example plugin {#endstonemc-cpp-example-plugin-1-i-can-t-build-the-example-plugin}

Source: https://github.com/EndstoneMC/cpp-example-plugin/issues/1

## Review scope and state {#review-scope-and-state}

- Thread author: HuQisQwQ; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

HuQisQwQ reports MSVC LNK2038: the plugin has _ITERATOR_DEBUG_LEVEL 2 while fmt objects use 0, followed by LNK1319. Wu identifies Debug builds as ABI-incompatible with Endstone and BDS, recommends deleting stale build output and choosing Release or RelWithDebInfo, then closes with permission to reopen. This is a binary-contract diagnosis, not merely a compiler syntax error. The reporter provides no successful rebuild confirmation; closure alone cannot prove the remedy worked for that environment.



## Source index {#source-index}

- https://github.com/EndstoneMC/cpp-example-plugin/issues/1
- https://github.com/EndstoneMC/cpp-example-plugin/issues/1#issuecomment-2255031670
- https://github.com/EndstoneMC/cpp-example-plugin/issues/1#issuecomment-2260709235
