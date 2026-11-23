<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:139"],"source_type":"public","date":"2025-02-21","topics":["concurrency","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-139-feature-refactor-endstone-core-endstoneactor-class"></a>
# EndstoneMC/endstone #139: [feature] refactor `endstone::core::EndstoneActor` class {#endstonemc-endstone-139-feature-refactor-endstone-core-endstoneactor-class}

Source: https://github.com/EndstoneMC/endstone/issues/139

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu identifies direct references from EndstoneActor to Minecraft entities as dangling-pointer risks after deletion. He proposes a visitor/proxy using WeakRef<EntityContext>, validation before every operation and public Actor::isValid for retained handles. This makes lifetime observation explicit instead of exposing a stale native reference. Closed state alone does not prove implementation or specify whether invalid access throws/returns errors. Check-once is insufficient if operations can invalidate context; the proposal’s per-operation validation is the relevant invariant.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/139
