<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endweave:13"],"source_type":"public","date":"2026-04-04","topics":["testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endweave-13-crash-on-invalid-packetsendevent"></a>
# EndstoneMC/endweave #13: Crash on invalid PacketSendEvent {#endstonemc-endweave-13-crash-on-invalid-packetsendevent}

Source: https://github.com/EndstoneMC/endweave/issues/13

## Evidence and attribution {#evidence-and-attribution}

Primary author: ForestOfLight. Created 2026-04-04T23:41:55Z; recorded state closed; merged not applicable.

A Python MemoryError in PacketSendEvent precedes server exit after hours without visible players. Wu attributes it to exhausted RAM and categorically excludes Endstone/plugin involvement. The log supports allocation failure but does not establish its cause; malformed length allocation or a leak cannot be ruled out from this thread. No memory profile, packet dump or independent fix. Preserve the overstrong attribution as the maintainer's claim, not settled diagnosis.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endweave/issues/13
- https://github.com/EndstoneMC/endweave/issues/13#issuecomment-4187943301
