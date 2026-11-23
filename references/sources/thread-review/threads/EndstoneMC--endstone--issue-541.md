<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:541"],"source_type":"public","date":"2026-10-05","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-541-bug-explosions-wind-charge-items-and-wind-burst-mace-enchantment-do-not-function"></a>
# EndstoneMC/endstone #541: [Bug] Explosions, Wind Charge items, and Wind Burst mace enchantment do not function {#endstonemc-endstone-541-bug-explosions-wind-charge-items-and-wind-burst-mace-enchantment-do-not-function}

Source: https://github.com/EndstoneMC/endstone/issues/541

## Evidence and attribution {#evidence-and-attribution}

Primary author: ducklingwhoo. Created 2026-10-05T17:51:23Z; recorded state closed; merged not applicable.

Reporter alleges clean-server TNT/wind charge/mace failure and guesses missing hooks. Wu cannot reproduce: fresh-world TNT damage/knockback/ActorExplodeEvent and wind charges work on Windows and LinuxPython3.14. Requests OS/container, plugins/packs, startup-through-explosion log and same-world vanilla BDS A/B. No follow-up isolates cause; closed state must not be converted to confirmed missing symbols or fix.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/541
- https://github.com/EndstoneMC/endstone/issues/541#issuecomment-6015133980
