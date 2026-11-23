<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:185"],"source_type":"public","date":"2025-05-20","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-185-feature"></a>
# EndstoneMC/endstone #185: [feature] {#endstonemc-endstone-185-feature}

Source: https://github.com/EndstoneMC/endstone/issues/185

## Review scope and state {#review-scope-and-state}

- Thread author: Arduinonk; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Arduinonk reports upgrades overwriting config/default/permissions.json, removing the locally enabled @minecraft/server-net module and breaking dependent behavior packs; SuperEric1 confirms. Wu reports a recent fix without linking it. This is a migration/preservation requirement: update distributed binaries while preserving administrator configuration. The JSON snippet is illustrative and includes a comment, not necessarily a literal valid JSON file. No exact patch is claimed here; the later issue 206 extraction log independently shows existing config and permissions files being skipped, consistent with preservation but not a full regression test.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/185
- https://github.com/EndstoneMC/endstone/issues/185#issuecomment-2895903962
- https://github.com/EndstoneMC/endstone/issues/185#issuecomment-2899224385
