<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:68"],"source_type":"public","date":"2024-10-01","topics":["review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-68-fix-expected-lite-dependency-tag"></a>
# EndstoneMC/endstone #68: Fix Expected Lite Dependency Tag {#endstonemc-endstone-68-fix-expected-lite-dependency-tag}

Source: https://github.com/EndstoneMC/endstone/pull/68

## Review scope and state {#review-scope-and-state}

- Thread author: thesamgordon; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (1 additions, 1 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

thesamgordon fixes expected-lite FetchContent tag 0.8.0 to v0.8.0 after a compile failure. Wu accepts and separately points to #66’s warning about building plugins against moving main. The one-line merged fix restores the dependency reference; it does not remove the need to pin Endstone’s matching ABI release. Upstream allegedly changing a tag is the author’s interpretation, not independently verified history.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/68
- https://github.com/EndstoneMC/endstone/pull/68#issuecomment-2385171971
