<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:489"],"source_type":"public","date":"2026-08-19","topics":["lifetime","ffi","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-489-feat-event-add-playershearactorevent"></a>
# EndstoneMC/endstone #489: feat(event): add PlayerShearActorEvent {#endstonemc-endstone-489-feat-event-add-playershearactorevent}

Source: https://github.com/EndstoneMC/endstone/pull/489

## Evidence and attribution {#evidence-and-attribution}

Primary author: Packeting1. Created 2026-08-19T17:17:06Z; recorded state closed; merged False.

Packeting1's shearing event is superseded by Wu's #504 with contributor credit. Wu identifies concrete integration errors: Windows vtable slot109 is openContainer rather than getInteraction117, while Linux118 happens to work; the seven-species allowlist diverges from behavior-pack interaction text and includes unrelated dyeing. The replacement resolves nonvirtual InteractComponent::getInteraction and matches shear/mooshear after native success. Drops are produced later by loot-table callbacks, so hand-building a drop list here changes vanilla behavior even without listeners. A future drop API needs a second trySpawnItems hook plus player correlation. Wu compares one real symbol and no vtable hooks with the larger proposed reconstruction; these are review claims until patches are checked.

## Direct patch findings {#direct-patch-findings}

The final rejected patch confirms Windows slot109 and Linux118, plus process-wide once-installed actor/spawner virtual hooks. It intercepts a compiler-generated inventory-transaction callback using a hand-reconstructed closure with offsets8/16/24/32, saves/restores thread_local context without an exception guard, checks a seven-species allowlist and mainhand shears, then constructs vanilla drops itself from RNG, color/variant and body/carried items. Offhand inference exists but admission still uses mainhand shears. Native interaction callback is moved into a wrapper; a thread_local RAII scope suppresses every spawner spawnItem during its execution, saves only position/throw-time, then respawns the constructed/plugin-adjusted list. This changes RNG consumption and loot behavior even without listeners, can suppress unrelated nested spawns, loses original spawner ownership, and assumes drops occur synchronously inside that callback. Cancellation clears callable and returns Failure. A broad brstd function copy/move/destruction reconstruction accompanies the event; inline moved-from callable is destroyed and heap targets deleted with actual T. There are no automated tests in the patch for callback ABI, platforms, vanilla no-listener equivalence, custom behavior packs, exception restoration or delayed drops. #504's narrower interaction-text hook is a deliberate scope reduction, not merely renaming this implementation.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (45696 characters; SHA-256 b5f1dcda90c8f52bbb80cab51d335bd110b40d4e048318400ea3534bb5acdc63), head 8f77b9e1a9403e32cf157f5b93bbff19acbf118e. For40 also verified exact-head src/endstone/core/registry.h cache ownership. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/489
- https://github.com/EndstoneMC/endstone/pull/489#issuecomment-5359687610
- https://github.com/EndstoneMC/endstone/pull/489#issuecomment-5359687783
