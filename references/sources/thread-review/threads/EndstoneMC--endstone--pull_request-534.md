<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:534"],"source_type":"public","date":"2026-09-16","topics":["ffi","testing","api","documentation","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-534-feat-add-26-51-support"></a>
# EndstoneMC/endstone #534: feat: add 26.51 support {#endstonemc-endstone-534-feat-add-26-51-support}

Source: https://github.com/EndstoneMC/endstone/pull/534

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-09-16T00:30:16Z; recorded state closed; merged True.

Empty description and no discussion. The merged26.51 port must be understood from its patch; there is no prose rationale to extrapolate.

## Complete implementation and learned failure modes {#complete-implementation-and-learned-failure-modes}

All131392characters of the patch were inspected, including signature recipes, both63-entry generated symbol tables and all native declarations. Protocol2169→2193 deliberately removes the26.44/2168 login/settings and scoreboard shims from#518. The changelog tells administrators to use NetherNet and requires26.51 clients. This is a removal of compatibility policy, not only a fresh address set.

The extensive port guide records useful diagnosis failures. Length-only vtable sweeps miss net-zero edits: Actor loses canFreeze, Player adds a virtual, so Player/ServerPlayer total lengths stay constant while interior slots move. Abstract bases may emit no own table, and cpp-local classes disappear from header-only inventories. Scan hierarchy alignment and every declared class, then inspect the changed slot rather than concluding from table length. Code-pointer runs can extend into adjacent type-erased manager tables; cross-check base/derived lengths and explicit table bounds. The guide's proposed next-RIP-reference bound is a heuristic that must first reproduce known old data, not a universal ABI theorem.

Scanner negatives also require validation. lea-only string references miss SSE movups materialization of SSO literals; malformed ModRM displacement matching can return no references despite a live string. Prefer unique self-naming markers and old-binary calibration, and switch to analyzed IDA cross-references when available. Long database generation can run concurrently with RTTI/layout/section/boundary analysis. These are source-documented workflow lessons, not independently reproduced binary measurements. The guide's statement equating0xC0000409 with a vtable shift is too broad: its cited CFG fast-fail subcode supports invalid indirect dispatch, while incorrect slots are a concrete candidate, not the only cause. Likewise wire integer encoding alone does not universally prove C++ enum width; the patch describes cross-checking its cereal convention and schema.

Tail growth matters through vector stride, largest variant alternative and base-subobject layout even if no direct field accessor touches the added bytes. AttributeInstance grows128→136 and sits by value in a flat-map value vector. MutableLevelGameplayEvent gains a32-byte unknown alternative; visitor now only interprets the known weather alternative and passes others to native code. MobEffectInstance adds eight unknown bytes before factor data, fixing the claimed Windows-only variant-discriminant offset while libc++ alignment already absorbed them. Explicit unknown names preserve uncertainty rather than inventing semantics. A raw size assertion is converted to platform-aware form, but compile-time size equality still compares the model to a number, not to the running native binary.

ResourcePack becomes a single Body pointer with old fields moved behind it, and getManifest adds the dereference. ResourcePackManager changes full_stack shared_ptr→unique_ptr and reorders locking/generation storage; ResourcePackRepository inserts a nonowner pointer and new virtual slots. Item block type becomes raw pointer instead of WeakPtr, with call sites updated. New/removed virtuals span command origins, player-data, inventory/container, item descriptor, random, level listeners and ILevel. MapDataManager adds platform-sized opaque tails specifically because a second base in ServerMapDataManager depends on its size. Native semantics of unknown virtuals/members remain unverified.

Packet payloads shrink BossEvent and remove player_id; ItemUseInventoryTransaction adds uint8 HandSlot; PlaySound adds optional playback position and a bool whose declaration order differs from documented wire order. Constructor zero-init range is used as source evidence for the one-byte trailing member. The code keeps API behavior localized while adjusting payload sizes and serialization-mode offsets. EndstoneObjective equality now compares objective_.access() rather than wrapper-member addresses, allowing two handles to the same native objective to compare equal. Python registry iteration returns an actual iterator over a list of reference-cast native entries, with Iterator[T] stubs; it still eagerly materializes the list and references need native registry lifetime.

No automated regression tests are added in this patch. The guide recommends DevTools dumps because they exercise recipes/items/biomes beyond bare startup; that is a broader smoke test, not a substitute for join, event dispatch, packet and lifecycle regressions. Claimed binary/runtime observations remain source-reported here.


## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (131392 characters; SHA-256 81d15e235dba74a321deca659a741cc09eb850d4a2276c7074d1a9d8fb8b0901), head 5abf8801624762bed391bac965ebfc086a314fb4. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/534
