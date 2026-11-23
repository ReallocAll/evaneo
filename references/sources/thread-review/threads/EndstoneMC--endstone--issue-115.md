<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:115"],"source_type":"public","date":"2024-12-28","topics":["concurrency","build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-115-bug-unknown-error"></a>
# EndstoneMC/endstone #115: [bug] Unknown error {#endstonemc-endstone-115-bug-unknown-error}

Source: https://github.com/EndstoneMC/endstone/issues/115

## Review scope and state {#review-scope-and-state}

- Thread author: pgrd1; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

pgrd1 supplies anti-cheat add-on code and an EndstoneServer::broadcast crash plus a separate reload trace. ye111566 contributes broad memory/concurrency hypotheses and another intermittent broadcast report; these remain speculation, not verified causes. Wu requests a minimal reliable reproduction because the combined plugin/add-on spans over 10,000 lines, and tentatively attributes only the separate reload trace to BDS. A later attempted fix improves Windows according to the reporter; Linux first fails initialization with bad_array_new_length, then continues with server-start/Python attribute-call crashes despite a claimed functional build. Wu cannot reproduce locally and closes the original issue as resolved, redirecting dev-build crashes to #127. Preserve multiple failure identities and platform-specific evidence. Neither generic AI-like hypotheses nor Windows recovery establish Linux correctness; no exact broadcast-fix SHA appears.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/115
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2564266383
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2566028734
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2566030192
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2566031697
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2566797507
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2566846460
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2567038837
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2567039882
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2567074027
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2585888736
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2590023600
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2590027731
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2590030436
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2597512053
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2597814998
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2599739952
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2602922551
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2608263029
- https://github.com/EndstoneMC/endstone/issues/115#issuecomment-2613989976
