<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:556"],"source_type":"public","date":"2026-10-18","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-556-serverlistpingevent-not-called-when-ping-response-is-128-bytes-signed-char-length-check"></a>
# EndstoneMC/endstone #556: ServerListPingEvent not called when ping response is 128+ bytes (signed char length check) {#endstonemc-endstone-556-serverlistpingevent-not-called-when-ping-response-is-128-bytes-signed-char-length-check}

Source: https://github.com/EndstoneMC/endstone/issues/556

## Evidence and attribution {#evidence-and-attribution}

Primary author: jv2w. Created 2026-10-18T05:49:05Z; recorded state closed; merged not applicable.

Signed char in two-byte big-endian PONG length decoding makes low byte>=0x80 negative, causing the validation check to bypass ServerListPingEvent and send vanilla MOTD. jv2w confirms shortening styled-name bytes below128 restores event firing; byte length, not displayed character count, matters. Wu points to cb2bcf1a9. This is strongly localized reporter evidence but the corrected commit remains uninspected here.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/556
- https://github.com/EndstoneMC/endstone/issues/556#issuecomment-6246277721
- https://github.com/EndstoneMC/endstone/issues/556#issuecomment-6251175649
