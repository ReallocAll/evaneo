<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:343"],"source_type":"public","date":"2026-03-06","topics":["ffi","testing","api","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-343-feat-add-debugshape-api"></a>
# EndstoneMC/endstone #343: feat: add DebugShape API {#endstonemc-endstone-343-feat-add-debugshape-api}

Source: https://github.com/EndstoneMC/endstone/pull/343

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-03-06T17:44:26Z; recorded state closed; merged False.

## Discussion disposition {#discussion-disposition}

Unmerged DebugShape API PR superseding #208; no reasoning or discussion beyond that link.

The full associated patch was subsequently inspected; test execution is not independently verified.

## Direct patch findings {#direct-patch-findings}

Implementation provides six CRTP value shapes with fluent color/scale/rotation setters and boxbound, line/arrowlength, arrowhead controls, text. Only arrow segments clamp3..128; other values have no finite/positive validation. Per-player descending uint64 IDs beginMAX to reduce script-API collisions; shape IDs are remembered in an unordered_set. add converts color bytes to floats, resolves native dimension, computes line/arrow endpoints from pitch/yaw, visits variant into native DebugDrawerPacket and sends only to player. remove sends time_left_total_sec=0 only for remembered ID, remove-all batches knownIDs then clears set. This is snapshot creation, not a retained editable shape or expiration/attachment API; no tests or runtime visual validation are in patch. Unmerged state remains important, and the raw native payload layout has no size assertions in this patch.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (39920 characters; SHA-256 393805be69678c33e9fb502fe4bc24ede62e1f2e537803ffb074f5b442beed2e), head c208acb10b8b1bf9eb0a8ceb0eeb9af7dfbe7308. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/343
