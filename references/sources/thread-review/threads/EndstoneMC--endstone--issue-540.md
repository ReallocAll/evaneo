<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:540"],"source_type":"public","date":"2026-09-28","topics":["ffi","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-540-add-a-native-player-sendactionbar-feature-to-endstone-python-plugins"></a>
# EndstoneMC/endstone #540: add a native Player.send_action_bar() feature to endstone python plugins {#endstonemc-endstone-540-add-a-native-player-sendactionbar-feature-to-endstone-python-plugins}

Source: https://github.com/EndstoneMC/endstone/issues/540

## Evidence and attribution {#evidence-and-attribution}

Primary author: SchleroMC. Created 2026-09-28T17:49:56Z; recorded state closed; merged not applicable.

Action-bar API is implemented for0.12, not backported to0.11. Wu explains adding a virtual Player method changes vtable layout and breaks already-built C++ plugins until recompiled; even a Python user's convenience feature has a native ABI cost. This is a concrete minor-release boundary, not merely reluctance to release sooner.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/540
- https://github.com/EndstoneMC/endstone/issues/540#issuecomment-6014645521
