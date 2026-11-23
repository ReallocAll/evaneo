<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:113"],"source_type":"public","date":"2024-12-26","topics":["review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-113-feat-dump-more-liquid-data-for-block-states"></a>
# EndstoneMC/endstone #113: feat: dump more liquid data for block states {#endstonemc-endstone-113-feat-dump-more-liquid-data-for-block-states}

Source: https://github.com/EndstoneMC/endstone/pull/113

## Review scope and state {#review-scope-and-state}

- Thread author: smartcmd; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (4 additions, 3 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

smartcmd initially proposes getLiquidDetectionRule; wu requests changes because that method does not exist on BDS Block, preferring getDirectData() exposing the real component data. The final merged patch follows that request, returning a const BlockComponentDirectData reference and reading can_contain_liquid/on_liquid_touches at the export layer. Export names change to canContainLiquidSource and liquidReactionOnTouch. This preserves fidelity of reconstructed native types and keeps derived convenience/serialization logic outside them. Inline original proposal, reviewer objection and final code are all available; this is stronger evidence than a generic approval.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/113
- https://github.com/EndstoneMC/endstone/pull/113#issuecomment-2562326269
- https://github.com/EndstoneMC/endstone/pull/113#discussion_r1899117178
- https://github.com/EndstoneMC/endstone/pull/113#pullrequestreview-2524932700
