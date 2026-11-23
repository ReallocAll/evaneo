<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:308"],"source_type":"public","date":"2025-12-03","topics":["testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-308-feature-bug-minecraft-education-edition-dedicated-server"></a>
# EndstoneMC/endstone #308: [Feature/Bug] Minecraft Education Edition Dedicated Server {#endstonemc-endstone-308-feature-bug-minecraft-education-edition-dedicated-server}

Source: https://github.com/EndstoneMC/endstone/issues/308

## Evidence and attribution {#evidence-and-attribution}

Primary author: pelijot. Created 2025-12-03T19:05:37Z; recorded state closed; merged not applicable.

## Problem and explicit scope decision {#problem-and-explicit-scope-decision}

pelijot tried the Education Edition dedicated-server beta. Version parsing produced 0.0.0 rather than 1.21.110-beta1; manually changing the expected version did not resolve a startup crash. Output includes FUNCHOOK_ERROR_CANNOT_FIX_IP_RELATIVE when hooking Player::take and the education server build identity. wu-vincent explicitly stated there was no plan to support this BDS variant.

## Reusable lesson and limits {#reusable-lesson-and-limits}

Bypassing a version guard does not establish binary/hook compatibility. This is a scope rejection, not a diagnosed parser-only bug or proven unsupported-platform workaround. No patch or successful reproduction after change is recorded.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/308
- https://github.com/EndstoneMC/endstone/issues/308#issuecomment-3608718988
