<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:215"],"source_type":"public","date":"2025-07-09","topics":["lifetime","ffi","testing","api","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-215-feat-complete-the-map-api-wip"></a>
# EndstoneMC/endstone #215: feat: complete the Map API (WIP) {#endstonemc-endstone-215-feat-complete-the-map-api-wip}

Source: https://github.com/EndstoneMC/endstone/pull/215

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (1412 additions, 119 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu's merged Map API PR has an empty description, no human reviews and one later stale-bot message. WIP/stale wording is not treated as proof of abandonment or completeness. The full patch establishes the implementation and its remaining limits below.

### Complete patch inspection {#complete-patch-inspection}

The 52-file patch connects map creation, filled-map metadata, render layers, cursors and packet interception. Server::createMap allocates native saved data at the selected dimension's spawn with scale 3, then returns a cached map view. MapMeta stores an optional map UUID in NBT, can clear it, and resolves it through the server; a present ID need not resolve to an existing map. Native metadata cloning and a type-specific factory preserve map fields rather than reducing everything to generic item metadata.

Canvases store 128×128 ABGR pixels and cursor copies. Out-of-bounds writes are ignored and reads return 0; image drawing clips via these guards. Changed pixels mark each tracked actor's dirty rectangle. The previous nullable/base-pixel layer API is removed: each renderer starts with the accumulated prior buffer and passes its resulting buffer forward. Contextual renderers get per-player canvases; shared renderers use an invalid-actor sentinel. Render exceptions are logged, and subsequent composition proceeds. Cursors accumulate across layers; native rendering currently includes only decorations matching the recipient player's ID.

The nextUpdatePacket hook first asks native code for an update and only renders if a packet already exists and the tracked entity resolves to a player. It replaces pixel/decorations vectors, preserving the packet's existing other fields. This means changing cursors alone or an otherwise idle custom renderer does not independently force an update here; full-buffer replacement also deserves validation against native rectangle width/height/start fields. The added symbol is Windows-only in this patch, so Linux hook availability is not established by this PR. No rendering tests or runtime captures accompany it.

Lifetime and persistence remain concrete limits. A function-static map-ID cache retains views holding references to saved data without visible teardown. Per-player canvas/cache entries have no shown disconnect eviction. Renderer mutation during iteration has no snapshot protection. setLocked/setUnlimitedTracking explicitly comment out dirty-save marking, while dimension changes also lack a dirty mark in the new setter. Cursor setter validates direction 0..15, but its constructor does not. Map metadata treats numeric ID 0 as absent when loading. These are revision-bounded edge cases, not evidence of universally broken maps.

Python trampolines pass map/canvas/player by reference and add keep_alive for renderers. A custom pybind holder trait accepts unique_ptr<Base> for derived metadata, with an explanatory comment about deletion through adjusted pointers; it is a framework-internal specialization that warrants version-specific validation. The equality helper calls meta1.notUncommon(meta1) rather than meta1.notUncommon(meta2), potentially making mixed generic/map comparisons asymmetric. Tests only add the server mock method.

Exact inspected base/head: 0995e28601d0fad2f813c0f9c0435c547ac54c1f…bc6e6019bbaa80e6ebf0bccd0d0bd1478052760a. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/215
- https://github.com/EndstoneMC/endstone/pull/215#issuecomment-3393657482
