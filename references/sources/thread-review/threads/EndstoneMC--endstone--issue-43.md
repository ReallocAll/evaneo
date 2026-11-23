<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:43"],"source_type":"public","date":"2024-09-01","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-43-feature-add-ban-and-banip-as-built-in-commands"></a>
# EndstoneMC/endstone #43: [feature] Add `/ban` and `/banip` as built-in commands {#endstonemc-endstone-43-feature-add-ban-and-banip-as-built-in-commands}

Source: https://github.com/EndstoneMC/endstone/issues/43

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu proposes ban/banip for online and previously seen offline players. Because BDS LevelDB keys are UUID-based with player_ prefix, name-based offline lookup needs a separate name→UUID cache updated on joins; Bukkit usercache.json is an explicit prior-art option. Last-known IP and other extra data might live in an endstone compound tag. Both file format reuse and tag name are tentative proposals. A later completion link a6652196d55cdd4a5c056d59191612d1f3d18b81 exists, but without its code this does not prove all proposed storage choices shipped. The reusable reasoning is selecting indexes from query needs while distinguishing core identity from supplementary metadata.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/43
- https://github.com/EndstoneMC/endstone/issues/43#issuecomment-2424210246
- https://github.com/EndstoneMC/endstone/issues/43#issuecomment-2558622325
- https://github.com/EndstoneMC/endstone/commit/a6652196d55cdd4a5c056d59191612d1f3d18b81
