<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:27"],"source_type":"public","date":"2024-07-29","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-27-bug-in-permissions-op-and-operator-have-the-same-level-of-permission"></a>
# EndstoneMC/endstone #27: [bug] In "permissions" OP and OPERATOR have the same level of permission. {#endstonemc-endstone-27-bug-in-permissions-op-and-operator-have-the-same-level-of-permission}

Source: https://github.com/EndstoneMC/endstone/issues/27

## Review scope and state {#review-scope-and-state}

- Thread author: MengHanLOVE1027; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

MengHanLOVE1027 expects OPERATOR to mean console-only and OP to include operator players, supplying a six-command permission matrix. Wu clarifies op is an alias of operator. The reporter asks for a separate console enum; no adoption appears. Permission defaults and sender identity are distinct. The thread settles alias semantics but does not implement console-only access.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/27
- https://github.com/EndstoneMC/endstone/issues/27#issuecomment-2254815708
- https://github.com/EndstoneMC/endstone/issues/27#issuecomment-2255035538
- https://github.com/EndstoneMC/endstone/issues/27#issuecomment-2255053264
