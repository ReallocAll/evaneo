<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:465"],"source_type":"public","date":"2026-08-07","topics":["testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-465-clients-time-out-on-bds-1-26-40-because-endstone-sends-an-incomplete-raknet-pong"></a>
# EndstoneMC/endstone #465: Clients time out on BDS 1.26.40 because Endstone sends an incomplete RakNet Pong {#endstonemc-endstone-465-clients-time-out-on-bds-1-26-40-because-endstone-sends-an-incomplete-raknet-pong}

Source: https://github.com/EndstoneMC/endstone/issues/465

## Evidence and attribution {#evidence-and-attribution}

Primary author: pgrd1. Created 2026-08-07T13:03:08Z; recorded state closed; merged not applicable.

A Windows/Python3.11 local server emits an empty 33-byte PONG and times out. pgrd1 reports a patched DLL restores joining without a UDP proxy. Wu initially rejects treating this as an unconditional native bug and links #423; later #423 investigation changed the answer. The final fix reinitializes the handler announcement then restores the configured server name, rather than blindly overwriting all world-advertisement flags. The ZIP was acquired and its complete inventory inspected: it contains only endstone_runtime.dll (4,503,040 bytes), with no source or test material. The DLL was not executed or reverse-engineered, so it does not independently validate the claimed patch.

## Code and verification boundary {#code-and-verification-boundary}

Inspected 03c70ae5b12e5182c2883019e193a71570a23cb2 in the #423 review. This issue is a second reproduction, not independent proof of every early hypothesis. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Source and available attachment links are listed under Traceability; the separate acquisition and inspection ledger is not included in this distribution. ZIP contains only a DLL. Archive inventory inspected; binary not executed or reverse-engineered and no source-level patch claim verified from it.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/465
- https://github.com/EndstoneMC/endstone/issues/465#issuecomment-5217549261
- https://github.com/EndstoneMC/endstone/issues/465#issuecomment-5217773436
- https://github.com/EndstoneMC/endstone/issues/465#issuecomment-5217842628
- https://github.com/user-attachments/files/30830843/endstone-runtime-pongfix3-only-win64-cp311.2.zip
