<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:33"],"source_type":"public","date":"2024-08-10","topics":["ffi","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-33-feat-item-add-missing-fields-in-item-h"></a>
# EndstoneMC/endstone #33: feat(item): add missing fields in Item.h {#endstonemc-endstone-33-feat-item-add-missing-fields-in-item-h}

Source: https://github.com/EndstoneMC/endstone/pull/33

## Review scope and state {#review-scope-and-state}

- Thread author: smartcmd; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (12 additions, 4 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

smartcmd authors an ABI/header correction and DevTools export; wu says LGTM. Item’s furnace-XP virtual method changes reference to pointer, and a 64-bit unknown at offset 512 becomes two floats at 512/516. New exports read burn-interval multiplier and call XP multiplier with nullptr. This is concrete layout/signature work plus data extraction, not reasoning authored by wu. The 12-addition/4-deletion patch is complete. Codecov reports unchanged 7.81% overall coverage and no uncovered changed coverable lines, which cannot establish the reconstructed ABI is correct.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/33
- https://github.com/EndstoneMC/endstone/pull/33#issuecomment-2280819702
- https://github.com/EndstoneMC/endstone/pull/33#issuecomment-2281136808
