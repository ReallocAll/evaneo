<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:34"],"source_type":"public","date":"2024-08-11","topics":["review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-34-feat-add-factory-method-for-itemstack-add-furnaceburnduration-to-devtools"></a>
# EndstoneMC/endstone #34: feat: add factory method for ItemStack, add furnaceBurnDuration to DevTools {#endstonemc-endstone-34-feat-add-factory-method-for-itemstack-add-furnaceburnduration-to-devtools}

Source: https://github.com/EndstoneMC/endstone/pull/34

## Review scope and state {#review-scope-and-state}

- Thread author: smartcmd; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (94 additions, 6 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

smartcmd adds ItemStack::create(Item const&, count, aux, optional NBT) and hooked FurnaceBlockActor burn-duration functions, plus Windows/Linux symbols; wu approves without rationale. DevTools switches from the raw burn-interval multiplier to BDS-computed duration for a constructed stack and baseline interval 200. A name-based factory remains commented out because macros do not yet support multiple factories; this is a documented limit rather than available API. The factory macro renames a local name variable to avoid collision and allocates raw storage before invoking the original constructor. Ownership/alignment/deallocation correctness are not proved by this PR. isReplaceable is also removed from material export without explanation. Complete diff inspected; coverage is reported, not independent execution.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/34
- https://github.com/EndstoneMC/endstone/pull/34#issuecomment-2282768049
- https://github.com/EndstoneMC/endstone/pull/34#pullrequestreview-2231856598
