<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:125"],"source_type":"public","date":"2025-01-13","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-125-endstone-breaks-minecraft-education-edition-textures"></a>
# EndstoneMC/endstone #125: Endstone Breaks Minecraft Education Edition Textures {#endstonemc-endstone-125-endstone-breaks-minecraft-education-edition-textures}

Source: https://github.com/EndstoneMC/endstone/issues/125

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat reports education-world textures work in vanilla BDS but become invisible/question marks under Endstone; SuperEric1 confirms. Wu asks for a world reproduction, receives an archive and later reports resolution. The archive/code fix was not inspected, so preserve compatibility regression and reproduction-led workflow without inventing pack-loading root cause.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/125
- https://github.com/EndstoneMC/endstone/issues/125#issuecomment-2588633273
- https://github.com/EndstoneMC/endstone/issues/125#issuecomment-2590110381
- https://github.com/EndstoneMC/endstone/issues/125#issuecomment-2590132369
- https://github.com/EndstoneMC/endstone/issues/125#issuecomment-2608322541
