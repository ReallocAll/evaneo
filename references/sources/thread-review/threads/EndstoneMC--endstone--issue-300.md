<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:300"],"source_type":"public","date":"2025-11-22","topics":["lifetime","ffi","testing","diagnosis","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-300-libc-abi-pure-virtual-function-called"></a>
# EndstoneMC/endstone #300: libc++abi: Pure virtual function called! {#endstonemc-endstone-300-libc-abi-pure-virtual-function-called}

Source: https://github.com/EndstoneMC/endstone/issues/300

## Evidence and attribution {#evidence-and-attribution}

Primary author: DayOfMagic. Created 2025-11-22T21:27:40Z; recorded state closed; merged not applicable.

## Failure and diagnosis {#failure-and-diagnosis}

DayOfMagic reported intermittent Linux v0.10.15 crashes on player departure, with two Python reproduction attachments. wu-vincent considered an invalid retained player reference the likely cause: a plugin can store a player and call the API after disconnect. He identified overall object-lifetime management as work for the next version and closed the report.

## Evidence boundary and decision {#evidence-boundary-and-decision}

The response is explicitly probabilistic, not proof from a supplied stack or patch. Both supplied Python files were subsequently read in full; the exact crash site remains unproven. Preserve the lifetime boundary: retaining a language binding must not imply that the underlying native player remains valid. Closure does not demonstrate a delivered lifetime fix.

## Additional source and attachment inspection {#additional-source-and-attachment-inspection}

Both supplied files were read completely, without execution. `playerquit.py` snapshots name/XUID, inventory, ender chest, experience and health synchronously before submitting scalar/list data to async database/logging coroutines; this path does not itself pass Player to inventory_save. Its `if not player` only checks the wrapper at that moment and is not a native lifetime guarantee. The combat condition uses `not hub OR not afk`, which is true for every server name since a name cannot have both distinct prefixes; this is a separate static logic problem, not established as the pure-virtual crash cause. It dispatches a kill command during departure, another behavior requiring lifecycle care.

`inventory.py` reveals a clearer retained-object hazard: inventory_load(player) awaits a database query, schedules lambdas retaining player for experience/health/ender-chest updates, awaits another 0.1 seconds, then schedules an apply_inventory closure retaining player. No online/identity revalidation occurs when those callbacks run. Even the error path reads player.name and schedules a player-related command. This supports the maintainer's invalid-player hypothesis, but no supplied native stack or executed reproduction proves which callback caused the reported failure. A safer design would snapshot identity/data before suspension and resolve a currently valid player on the server thread immediately before each mutation. The file also iterates 36 ender-chest indices, but the relevant historic inventory bounds were not verified and no out-of-range diagnosis is asserted.

## Code and verification boundary {#code-and-verification-boundary}

Inspected both complete reporter Python attachments (playerquit.py and inventory.py). No upstream player-lifetime fix was supplied or independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Source and available attachment links are listed under Traceability; the separate acquisition and inspection ledger is not included in this distribution. Reporter source read completely without execution; no runtime causal proof.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/300
- https://github.com/EndstoneMC/endstone/issues/300#issuecomment-3760377332
- https://github.com/user-attachments/files/23691801/playerquit.py
- https://github.com/user-attachments/files/23691802/inventory.py
