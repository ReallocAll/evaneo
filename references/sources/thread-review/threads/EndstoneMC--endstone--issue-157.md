<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:157"],"source_type":"public","date":"2025-03-17","topics":["concurrency","ffi","build","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-157-endstone-arm64-support"></a>
# EndstoneMC/endstone #157: Endstone ARM64 Support {#endstonemc-endstone-157-endstone-arm64-support}

Source: https://github.com/EndstoneMC/endstone/issues/157

## Review scope and state {#review-scope-and-state}

- Thread author: trainerjeo; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

trainerjeo asks for Raspberry Pi ARM64 support after pip/wheel/Docker failures. legitbox points to the upstream BDS architecture constraint, and Wu confirms Endstone depends on native BDS support: ARM64 would be reconsidered if Mojang provides an official build; emulation is only a possible slower workaround. Slauh's phone-server idea is speculative. ugoi's later Docker question receives no answer. Container packaging alone does not remove the native architecture dependency; this is a historical support policy, not an independently checked statement about present-day Mojang builds.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/157
- https://github.com/EndstoneMC/endstone/issues/157#issuecomment-2728205563
- https://github.com/EndstoneMC/endstone/issues/157#issuecomment-2728220297
- https://github.com/EndstoneMC/endstone/issues/157#issuecomment-2729634981
- https://github.com/EndstoneMC/endstone/issues/157#issuecomment-3194601973
