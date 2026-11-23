<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:329"],"source_type":"public","date":"2026-02-12","topics":["ffi","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-329-feature-add-blockformevent"></a>
# EndstoneMC/endstone #329: [feature] add BlockFormEvent {#endstonemc-endstone-329-feature-add-blockformevent}

Source: https://github.com/EndstoneMC/endstone/issues/329

## Evidence and attribution {#evidence-and-attribution}

Primary author: incredibleopyt. Created 2026-02-12T12:22:38Z; recorded state closed; merged not applicable.

## Requested behavior versus delivered scope {#requested-behavior-versus-delivered-scope}

incredibleopyt requested BlockFormEvent; qaustria asked for scope, eliciting examples of environmental ice and liquid-generated cobblestone/obsidian. wu-vincent later reported #521 on develop for 0.12. It fires before lava becomes obsidian, cobblestone or basalt, providing the lava block and proposed new state; cancellation preserves lava and suppresses extinguishing effects.

Snow, ice and concrete are explicitly absent. Concrete may be feasible later; snow/ice logic is inlined into BDS chunk ticking with no isolated trigger point and is not planned. Reusable lesson: named API parity must state actual native trigger coverage. Hook availability, not conceptual similarity alone, determines scope. This is a maintainer implementation claim; #521's patch is outside this assigned record.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/329
- https://github.com/EndstoneMC/endstone/issues/329#issuecomment-3891117274
- https://github.com/EndstoneMC/endstone/issues/329#issuecomment-3891350902
- https://github.com/EndstoneMC/endstone/issues/329#issuecomment-5496437272
