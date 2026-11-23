<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:63"],"source_type":"public","date":"2024-09-26","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-63-feature-encrypted-resource-pack-support"></a>
# EndstoneMC/endstone #63: [feature] Encrypted Resource Pack support {#endstonemc-endstone-63-feature-encrypted-resource-pack-support}

Source: https://github.com/EndstoneMC/endstone/issues/63

## Review scope and state {#review-scope-and-state}

- Thread author: gamezaSRC; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

gamezaSRC requests native encrypted-resource-pack support because packet APIs are unavailable, proposing either an explicit UUID/key config or automatic encryption like Allay. Wu accepts and links 53c9dc16ecc7885ea5ff1eb1a9b0faf05b96b27d as completed. The discussion does not identify which alternative shipped. Client delivery of keys limits protection against a capable recipient; the requester’s anti-leak claims should not be promoted to a security guarantee. No keys are present or reproduced and implementation is not inspected here.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/63
- https://github.com/EndstoneMC/endstone/issues/63#issuecomment-2380603221
- https://github.com/EndstoneMC/endstone/issues/63#issuecomment-2419304875
- https://github.com/EndstoneMC/endstone/commit/53c9dc16ecc7885ea5ff1eb1a9b0faf05b96b27d
