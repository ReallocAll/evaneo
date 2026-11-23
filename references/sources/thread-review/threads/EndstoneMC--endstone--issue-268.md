<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:268"],"source_type":"public","date":"2025-09-27","topics":["concurrency","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-268-feature-events-that-are-canceled-override-script-api-s-canceled-events"></a>
# EndstoneMC/endstone #268: [feature] Events that are canceled override Script API's canceled events {#endstonemc-endstone-268-feature-events-that-are-canceled-override-script-api-s-canceled-events}

Source: https://github.com/EndstoneMC/endstone/issues/268

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat wants Endstone chat handling before Script API cancellation. Wu clarifies a four-stage contract: Endstone event first; its cancellation stops Script API; mutations flow into Script API; Script API cancellation still prevents sending. Requester confirms. Wu flags future Script API message mutability as a possible final-writer conflict and links completed887296ee1bf72d18c1d155f5edfe8b4ce678da8c for 0.10.11. Full patch read: ChatEvent gets an original-handler callback; unresolved players use original; Endstone validation/cancellation precede it; event.message is copied before original; a non-Continue result propagates; custom-format delivery then bypasses native double-send. A later difference branch compares Endstone text with post-original text, so future mutation semantics still need deliberate resolution. This does not authorize overriding Script API cancellation after it has occurred; the accepted request is ordering, not unconditional Endstone supremacy.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/268
- https://github.com/EndstoneMC/endstone/issues/268#issuecomment-3493607249
- https://github.com/EndstoneMC/endstone/issues/268#issuecomment-3493710138
- https://github.com/EndstoneMC/endstone/issues/268#issuecomment-3493714185
