<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:265"],"source_type":"public","date":"2025-09-20","topics":["concurrency","testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-265-reopening-issue-crash-on-item-meta-grab"></a>
# EndstoneMC/endstone #265: Reopening Issue: Crash on Item Meta Grab {#endstonemc-endstone-265-reopening-issue-crash-on-item-meta-grab}

Source: https://github.com/EndstoneMC/endstone/issues/265

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat reopens the item-meta crash after initial 259 success: on 0.10.5.dev60 with 20+ players, one disconnect triggers getItemMeta→getType and string construction failure. Wu links e6046b06865102a1fd57e2a488f97a0bb9084418. Full patch inspected: getType tests item && *item instead of item && !item->isNull before dereferencing getItem, otherwise uses air. This distinguishes the stack's full truth/validity predicate from the narrower null flag. No user retest follows; it addresses the guard but does not by itself prove every custom-item registry lookup or stale object is valid. The recurrence is essential counterevidence against treating 259 as final.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/265
- https://github.com/EndstoneMC/endstone/issues/265#issuecomment-3338538326
- https://github.com/EndstoneMC/endstone/commit/e6046b06865102a1fd57e2a488f97a0bb9084418)
