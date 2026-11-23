<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:267"],"source_type":"public","date":"2025-09-24","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-267-feature-พอร-ตปล-กอ-น-voice-chat-จาก-lse-node-js-เป-น-python-สำหร-บ-endstone-บนล-น-กซ"></a>
# EndstoneMC/endstone #267: [feature] พอร์ตปลั๊กอิน voice chat จาก lse node.js เป็น Python สำหรับ Endstone บนลินุกซ์ {#endstonemc-endstone-267-feature-พอร-ตปล-กอ-น-voice-chat-จาก-lse-node-js-เป-น-python-สำหร-บ-endstone-บนล-น-กซ}

Source: https://github.com/EndstoneMC/endstone/issues/267

## Review scope and state {#review-scope-and-state}

- Thread author: Blue-oon; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Blue-oon's Thai request proposes porting an LSE Node.js voice-chat plugin to Python on Linux Endstone, with WebSockets, server-issued binding codes, mute/room/speaker status, and simple deployment; a bridge's performance concern is the requester's assumption, not measured. Wu asks for English and rejects inclusion in loader core because this belongs in a separate plugin. The architectural scope decision is engineering-relevant despite language/procedural content. No voice transport, authentication scheme, code, or permission to port another project's implementation is established.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/267
- https://github.com/EndstoneMC/endstone/issues/267#issuecomment-3328028061
