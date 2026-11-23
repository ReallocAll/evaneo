<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:90"],"source_type":"public","date":"2024-11-14","topics":["concurrency","ffi","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-90-native-restarts"></a>
# EndstoneMC/endstone #90: native restarts {#endstonemc-endstone-90-native-restarts}

Source: https://github.com/EndstoneMC/endstone/issues/90

## Review scope and state {#review-scope-and-state}

- Thread author: Mih4n; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Mih4n requests a restart method and zelisce a command. Wu declines in-process restart because complete cleanup is difficult and could leak resources; he recommends a Docker restart policy or external loop waiting for process exit. This chooses a process boundary as the reclamation/reinitialization boundary, prioritizing reliability over a convenient API. The thread does not endorse blind crash loops or define state-saving policy; external supervision still needs shutdown/backoff design.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/90
- https://github.com/EndstoneMC/endstone/issues/90#issuecomment-2476373998
- https://github.com/EndstoneMC/endstone/issues/90#issuecomment-2501892140
