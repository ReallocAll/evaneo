<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:220"],"source_type":"public","date":"2025-07-19","topics":["ffi","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-220-fix-server-name-call-in-python-api"></a>
# EndstoneMC/endstone #220: Fix Server.name call in Python API {#endstonemc-endstone-220-fix-server-name-call-in-python-api}

Source: https://github.com/EndstoneMC/endstone/pull/220

## Review scope and state {#review-scope-and-state}

- Thread author: cenk; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (1 additions, 1 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

cenk's merged one-line binding fix maps Python Server.name to Server::getName rather than getVersion; the version binding remains unchanged. Full patch read. Wu's thanks adds no further rationale. This is a concrete binding-target mismatch, not an API redesign.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/220
- https://github.com/EndstoneMC/endstone/pull/220#issuecomment-3094434808
