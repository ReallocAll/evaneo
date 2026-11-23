<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:207"],"source_type":"public","date":"2025-06-20","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-207-bug-client-side-texture-packs-can-not-be-denied"></a>
# EndstoneMC/endstone #207: [bug] client side texture packs can not be denied {#endstonemc-endstone-207-bug-client-side-texture-packs-can-not-be-denied}

Source: https://github.com/EndstoneMC/endstone/issues/207

## Review scope and state {#review-scope-and-state}

- Thread author: Arduinonk; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Arduinonk reports allow-client-packs=false plus texturepack-required=true no longer excludes client packs on 0.9.1. Wu cannot reproduce, invites a video, and closes after no reproducible evidence arrives. This is a counterclaim to the 162 policy implementation, not proof that the option universally regressed or that user configuration was wrong. No patch or runtime confirmation exists.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/207
- https://github.com/EndstoneMC/endstone/issues/207#issuecomment-2993556961
- https://github.com/EndstoneMC/endstone/issues/207#issuecomment-2993599813
- https://github.com/EndstoneMC/endstone/issues/207#issuecomment-2993600196
- https://github.com/EndstoneMC/endstone/issues/207#issuecomment-2994221105
- https://github.com/EndstoneMC/endstone/issues/207#issuecomment-3039357163
