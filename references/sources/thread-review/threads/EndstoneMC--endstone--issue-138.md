<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:138"],"source_type":"public","date":"2025-02-20","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-138-bug-always-showing-death-messages-even-with-the-gamerule-showdeathmessages-set-to-false-and-not-translatin"></a>
# EndstoneMC/endstone #138: [bug] Always showing death messages even with the gamerule "showdeathmessages" set to false, and not translating to other languages properly {#endstonemc-endstone-138-bug-always-showing-death-messages-even-with-the-gamerule-showdeathmessages-set-to-false-and-not-translatin}

Source: https://github.com/EndstoneMC/endstone/issues/138

## Review scope and state {#review-scope-and-state}

- Thread author: SuperEric1; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

SuperEric1 reports death messages ignoring gamerule and client language, plus command feedback ignoring its gamerule. Wu confirms refactor regression, links bfdc73067bce1d5bad7dd460fb4110fae50b046f for death messages, then asks for separate feedback semantics and links 064027b78b1e30e33c1526cf1890b96a61eb3bd6 after clarification. This preserves two fixes and host behavioral contracts: suppression and localization. No patch/test was independently read here.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/138
- https://github.com/EndstoneMC/endstone/issues/138#issuecomment-2674684461
- https://github.com/EndstoneMC/endstone/issues/138#issuecomment-2687912208
- https://github.com/EndstoneMC/endstone/issues/138#issuecomment-2687956913
- https://github.com/EndstoneMC/endstone/issues/138#issuecomment-2688619844
- https://github.com/EndstoneMC/endstone/commit/bfdc73067bce1d5bad7dd460fb4110fae50b046f
- https://github.com/EndstoneMC/endstone/commit/bfdc73067bce1d5bad7dd460fb4110fae50b046f)
- https://github.com/EndstoneMC/endstone/commit/064027b78b1e30e33c1526cf1890b96a61eb3bd6
