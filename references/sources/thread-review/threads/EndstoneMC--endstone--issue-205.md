<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:205"],"source_type":"public","date":"2025-06-18","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-205-bug-jigsawstructuremetadata-error"></a>
# EndstoneMC/endstone #205: [bug]jigsaw_structure_metadata error {#endstonemc-endstone-205-bug-jigsawstructuremetadata-error}

Source: https://github.com/EndstoneMC/endstone/issues/205

## Review scope and state {#review-scope-and-state}

- Thread author: KeSaite; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

KeSaite observes empty joint_type jigsaw metadata errors after 0.8.2→0.9.0. Wu says the same occurs in vanilla BDS and suggests ignoring it or using a new world. No independent vanilla comparison, attachment reading, or underlying fix is recorded. This is a maintainer upstream attribution; creating a fresh diagnostic world is distinct from deleting a valuable existing one and the thread supplies no need to destroy data.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/205
- https://github.com/EndstoneMC/endstone/issues/205#issuecomment-2983377383
