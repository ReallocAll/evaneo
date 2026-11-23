<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:257"],"source_type":"public","date":"2025-08-26","topics":["concurrency","ffi","build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-257-installer-crashed"></a>
# EndstoneMC/endstone #257: Installer crashed {#endstonemc-endstone-257-installer-crashed}

Source: https://github.com/EndstoneMC/endstone/issues/257

## Review scope and state {#review-scope-and-state}

- Thread author: WonderGDad; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

WonderGDad's Pi installer falls back to source-build and fails on a missing CMakePresets.json, then cannot find endstone. Wu explains the underlying native ARM incompatibility and proposes an amd64 container with emulation (QEMU), not native ARM wheels. The packaging error itself is not shown fixed; emulation addresses the platform route and may entail performance cost. No installer, container, or upstream script was executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/257
- https://github.com/EndstoneMC/endstone/issues/257#issuecomment-3227621680
