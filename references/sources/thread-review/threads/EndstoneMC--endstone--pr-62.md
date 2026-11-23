<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:62"],"source_type":"public","date":"2024-09-26","topics":["review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-62-feat-devtools-add-more-block-shapes-data"></a>
# EndstoneMC/endstone #62: feat(devtools): add more block shapes' data {#endstonemc-endstone-62-feat-devtools-add-more-block-shapes-data}

Source: https://github.com/EndstoneMC/endstone/pull/62

## Review scope and state {#review-scope-and-state}

- Thread author: smartcmd; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (70 additions, 1 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

smartcmd adds forwarding methods for camera collision, outline, visual, UI and liquid-clip shapes, then exports four new AABB arrays per block permutation at a sampled position. Wu only thanks them. The actual diff removes zero initialization from collision_shape, adds uninitialized local buffers and ignores return flags for collision/liquid shapes; absent-shape handling therefore needs separate validation. Camera collision forwarding is added but not exported here. This data extraction observes context-sensitive geometry at fixed coordinates, not a proof of universal shape invariance. Codecov reports low total coverage and a stale comparison, not geometry correctness.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/62
- https://github.com/EndstoneMC/endstone/pull/62#issuecomment-2377119824
- https://github.com/EndstoneMC/endstone/pull/62#issuecomment-2378342613
- https://github.com/EndstoneMC/endstone/pull/62#issuecomment-2380602464
