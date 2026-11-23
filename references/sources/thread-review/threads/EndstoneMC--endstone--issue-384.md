<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:384"],"source_type":"public","date":"2026-04-20","topics":["lifetime","testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-384-unknow-crash-when-call-callevent"></a>
# EndstoneMC/endstone #384: Unknow Crash when call callEvent {#endstonemc-endstone-384-unknow-crash-when-call-callevent}

Source: https://github.com/EndstoneMC/endstone/issues/384

## Evidence and attribution {#evidence-and-attribution}

Primary author: BackstabDev. Created 2026-04-20T12:19:03Z; recorded state closed; merged not applicable.

## Debugging and conceptual correction {#debugging-and-conceptual-correction}

BackstabDev attempted chain mining by constructing BlockBreakEvent and calling callEvent, crashing on Windows. Rezn1r suggested clone() because the event owns a unique_ptr<Block>; borrowed block ownership could otherwise be misrepresented. The reporter confirmed clone stopped the crash, but the block remained.

wu-vincent explained that event dispatch notifies listeners, it does not perform the native action. Set the block type to minecraft:air and explicitly drop selected ItemStacks via Dimension::dropItem when drops are desired. This is contributor-led lifetime diagnosis followed by a command-versus-notification API clarification.

The exact type of the reporter's i.getBlock() is not shown, so double-free is Rezn1r's hypothesis supported by the successful workaround, not independently proven. Nor does setting air automatically reproduce all mining physics, drops or built-in event semantics. Keep those responsibilities explicit.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/384
- https://github.com/EndstoneMC/endstone/issues/384#issuecomment-4416040940
- https://github.com/EndstoneMC/endstone/issues/384#issuecomment-4422507200
- https://github.com/EndstoneMC/endstone/issues/384#issuecomment-4604444759
