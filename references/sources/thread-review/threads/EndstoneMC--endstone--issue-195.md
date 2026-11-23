<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:195"],"source_type":"public","date":"2025-06-09","topics":["concurrency","testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-195-feature-support-for-cdn-resource-packs"></a>
# EndstoneMC/endstone #195: [feature] Support for CDN resource packs {#endstonemc-endstone-195-feature-support-for-cdn-resource-packs}

Source: https://github.com/EndstoneMC/endstone/issues/195

## Review scope and state {#review-scope-and-state}

- Thread author: Kuma3mccm; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Kuma3mccm asks for client-direct CDN downloads to avoid serving large packs over the game server's network, assuming cdn_config.json stopped working. Mih4n's suggestion to download addons server-side is a different topology; requester explicitly distinguishes it. Wu reports testing native BDS CDN support and explains that every UUID_version entry must match a pack actually loaded in the server pack stack, illustrating a 1.0.1 manifest and local HTTP endpoint. Thus matching config text alone is insufficient if the pack is not loaded, and metadata consistency should be checked before inventing packet hooks. The tests/screenshots are Wu-reported, not executed here. The final question about encrypted CDN packs remains unanswered; success with an unencrypted example does not establish encrypted support.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/195
- https://github.com/EndstoneMC/endstone/issues/195#issuecomment-2956002519
- https://github.com/EndstoneMC/endstone/issues/195#issuecomment-2956215315
- https://github.com/EndstoneMC/endstone/issues/195#issuecomment-2956831621
- https://github.com/EndstoneMC/endstone/issues/195#issuecomment-2956851483
- https://github.com/EndstoneMC/endstone/issues/195#issuecomment-2957755836
- https://github.com/EndstoneMC/endstone/issues/195#issuecomment-2994365129
- https://github.com/EndstoneMC/endstone/issues/195#issuecomment-3087384946
