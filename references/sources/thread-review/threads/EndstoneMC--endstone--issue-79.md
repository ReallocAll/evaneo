<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:79"],"source_type":"public","date":"2024-10-16","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-79-bug-scriptevent-not-being-registered-properly"></a>
# EndstoneMC/endstone #79: [bug] ScriptEvent not being registered properly {#endstonemc-endstone-79-bug-scriptevent-not-being-registered-properly}

Source: https://github.com/EndstoneMC/endstone/issues/79

## Review scope and state {#review-scope-and-state}

- Thread author: zelisce; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

zelisce reports scheduled script-event delivery failure. Wu asks for dispatch return status and proposes permission/execute-as investigation. The reporter later finds the actual cause: a message starting with [] needed quoting. Preserve this correction rather than teach the initial permission hypothesis as diagnosis. The code serializes JSON player data; syntactic framing is distinct from scheduling or successful command invocation.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/79
- https://github.com/EndstoneMC/endstone/issues/79#issuecomment-2417835637
- https://github.com/EndstoneMC/endstone/issues/79#issuecomment-2417959915
- https://github.com/EndstoneMC/endstone/issues/79#issuecomment-2419243981
