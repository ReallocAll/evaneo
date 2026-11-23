<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:553"],"source_type":"public","date":"2026-10-16","topics":["testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-553-crash-on-startup-when-enable-script-false"></a>
# EndstoneMC/endstone #553: Crash on startup when enable-script=false {#endstonemc-endstone-553-crash-on-startup-when-enable-script-false}

Source: https://github.com/EndstoneMC/endstone/issues/553

## Evidence and attribution {#evidence-and-attribution}

Primary author: jv2w. Created 2026-10-16T09:49:51Z; recorded state closed; merged not applicable.

With enable-script=false BDS omits its scripting handler, but lifecycle setup dereferences it before vhook creation. jv2w supplies debugger null rcx/read0 plus stack; asks for null guards including other handlers. Wu reports b7dac6c07 fixes startup. Optional native subsystems need presence checks before installing hooks; no proof here of every other handler's audit.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/553
- https://github.com/EndstoneMC/endstone/issues/553#issuecomment-6243095597
