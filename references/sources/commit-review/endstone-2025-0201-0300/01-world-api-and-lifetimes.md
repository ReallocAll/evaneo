<!-- retrieval: {"source_ids":["public:commit:0f0de32dfb43747e8e8b2cbf36b038d8a1c80ce3","public:commit:10e2748ffc1654219c8d81ac3926eb4f22d77ef7","public:commit:222e9ae7b71e84cd7dc03e62c37d0ecb729bc204","public:commit:274dca39a8b496ff1fa2ccb7756d9a9a41e9e24d","public:commit:38c43f4acf7172d012edc55ae08f71728a9f6f72","public:commit:3b5a0c42d518c6dfa04d49258269f1425801cea0","public:commit:441b2b14ceff65dbdb5cb6c6400edc5beb956da0","public:commit:4bdbd29d75ee65c7a062bcd5c8a2fbe474568308","public:commit:64509e386e737d0946b440fbc731934cad1dbb17","public:commit:75a2d76735b88f00932556fd0984f5893f15f59d","public:commit:789099ec07a12c8114fd30daec3999d5f8acd5a1","public:commit:7c7e4b943a7346b41b2186e818c665f5aa656b4c","public:commit:8e144ea31667dc436cce1a546940659ba4cc95fa","public:commit:ad73c24e827d6319d2b5752bcded49184035c64e","public:commit:ae2f77d0083f08e6745a516b91f474a46a0e28c4","public:commit:bb3bcc44655a533ea414e49787a078886c54b373","public:commit:de49d084e7917fde9c0ff87ece490dfe88e97d39","public:commit:e115658d4237673aa9002f033debd8882452b2ec","public:commit:e177ef72c12d01a7ef24664568b1d2631f32b94a","public:commit:e1f55fa4f1fb1f13f9c0b1121957233c1ad37903","public:commit:eebdf50f9c4ad7dd28a529ac691b9ad55ce80234","public:commit:fcb843dc085a15b5d0dc995d14d79944313b5ef7"],"source_type":"public","date":"2025-01-29..2025-02-23","topics":["lifetime","ffi","testing","api","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# World APIs, event ownership and actor lifetime {#world-apis-event-ownership-and-actor-lifetime}

## Causal result {#causal-result}

This unit first makes world/block APIs easier to call, then adds a different kind of explicit invalidation to actors. These are distinct contracts. In211–215 live Block wrappers are always created; loaded/ticking/height checks and Result-valued getters disappear, while captured BlockState becomes uniquely owned. An owning smart pointer to a wrapper does not own its BlockSource or world. Setters still reject bad parse/null inputs but native placement failure is not propagated. The source does not establish that arbitrary coordinates or retained wrappers are safe merely because creation succeeds.

Damage events203–205 similarly own their Endstone DamageSource wrapper while borrowing its const native damage payload. The hook is Mob-specific and excludes client-side, invulnerable and dead actors before callback dispatch; plugins can cancel or replace floating-point damage. That is a synchronous interception policy, not a retained immutable damage snapshot. Python reference-return policies do not extend the native damage payload's life.

Native EventVariant copying206–209 is a particularly useful counterexample: move-only ValueOrRef avoids implicit owned copies, then explicit variant copying produces ref/cref alternatives to the original value. Copyability is restored by aliasing, not deep copying. The staged206 tree still has direct variant callers and default-copy incompatibilities;209 repairs those call sites. A claim that every individual historical commit compiled would exceed the evidence.

Actor removal290 raises the lifecycle stakes. Player::remove deliberately logs and directs callers to kick. In296–299 Actor/Mob/Player wrapper fields stop holding native references and use WeakEntityRef. Registry and entity validity are rechecked when unwrapping; checked handle access throws if the actor is gone. isValid is the safe Boolean probe implemented as unwrap plus isAlive, whereas isDead and most getters use the throwing handle path. This improves detection of invalid entities but is not ownership or synchronization against concurrent/reentrant destruction. The endpoint snapshots show PlayerInventory still holding native Player& and Container&; the migration is not system-wide lifetime safety.

## Collaborator integration and world boundaries {#collaborator-integration-and-world-boundaries}

Merge214 imports daoge/smartcmd's PR132 collision-shape exporter, changing one six-number collision box to an array of boxes under the same collisionShape key. API breakage for JSON consumers is relevant even though the key is preserved; the source history retains daoge/smartcmd's authorship.

219 introduces a concrete coordinate-layout mistake: x and z are alternatives in an anonymous union, so the z write overwrites x. The same declaration persists at300. Loaded-chunk Python access201 inherits the prior199 state comparison rather than supplying new validity validation. Highest-block binding289 also changes returned height by minus one, a semantic repair hidden by the binding-oriented title.

## Applying the evidence {#applying-the-evidence}

For plugin API design, distinguish live location wrappers, captured state ownership, event-borrowed payloads and expiring entity handles. Ask which errors remain observable after simplifying return types, and which retained child objects bypass the parent's invalidation guard. The changes support this decision checklist; they do not support a universal preference for shared versus unique ownership.

Tests in this slice focus on ABI utilities, not block coordinates, damage-retention, weak expiry or Python event retention. No source, tests or server were executed here. See endpoint context, [collaborator record](06-context-attribution.md), and the commit-specific records below.


<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}


<a id="commit-201"></a>
### 201. feat(python): add loaded_chunks property to Dimension class binding {#commit-201}

[bb3bcc44655a533ea414e49787a078886c54b373](https://github.com/EndstoneMC/endstone/commit/bb3bcc44655a533ea414e49787a078886c54b373) · 2025-01-29T16:52:55Z · author Vincent.

Parents: `0910b70e04c9d47d095fa9bad6d76c72760bf1b2`. Full message and sources: parent 1.

Exposes Dimension.loaded_chunks in the Python binding/stub; native implementation comes from prior199 and inherits its loaded-state filter and wrapper-allocation behavior. Status formatting change is whitespace only. No Python lifetime or allocation measurement supplied.

Coverage: 3 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-202"></a>
### 202. feat: add `Actor::isDead` {#commit-202}

[222e9ae7b71e84cd7dc03e62c37d0ecb729bc204](https://github.com/EndstoneMC/endstone/commit/222e9ae7b71e84cd7dc03e62c37d0ecb729bc204) · 2025-02-01T17:00:02Z · author Vincent.

Parents: `bb3bcc44655a533ea414e49787a078886c54b373`. Full message and sources: parent 1.

Adds native Actor::isDead by querying IsDeadFlagComponent, preparing hurt-event filtering. This is a native helper, not yet a new public Endstone Actor property. Component marker has no payload; no runtime ECS validation performed.

Coverage: 3 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-203"></a>
### 203. feat: add `ActorDamageEvent` {#commit-203}

[441b2b14ceff65dbdb5cb6c6400edc5beb956da0](https://github.com/EndstoneMC/endstone/commit/441b2b14ceff65dbdb5cb6c6400edc5beb956da0) · 2025-02-01T17:00:18Z · author Vincent.

Parents: `222e9ae7b71e84cd7dc03e62c37d0ecb729bc204`. Full message and sources: parent 1.

Adds cancellable ActorDamageEvent for Mob, float damage setter and owned DamageSource wrapper; hooks Mob::_hurt on both platform symbol tables. Client-side, invulnerable or dead actors return false before dispatch. Plugins may cancel or replace damage passed to original, retaining knock/ignite arguments. DamageSource now borrows const native payload, so owning its wrapper does not make callback retention safe. Python binding is already added here with reference policy;204 completes public exports/stub. No damage clamping or lifetime test added.

Coverage: 8 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-204"></a>
### 204. feat: add python bindings for `ActorDamageEvent` {#commit-204}

[4bdbd29d75ee65c7a062bcd5c8a2fbe474568308](https://github.com/EndstoneMC/endstone/commit/4bdbd29d75ee65c7a062bcd5c8a2fbe474568308) · 2025-02-01T17:03:55Z · author Vincent.

Parents: `441b2b14ceff65dbdb5cb6c6400edc5beb956da0`. Full message and sources: parent 1.

Completes ActorDamageEvent Python stub/export list, including mutable damage and read-only damage_source. Native pybind class already exists in203. Export-list diff read completely; no separate behavior beyond API discoverability inferred.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-205"></a>
### 205. feat: add `ActorDamageByBlockSource` {#commit-205}

[274dca39a8b496ff1fa2ccb7756d9a9a41e9e24d](https://github.com/EndstoneMC/endstone/commit/274dca39a8b496ff1fa2ccb7756d9a9a41e9e24d) · 2025-02-01T17:34:32Z · author Vincent.

Parents: `4bdbd29d75ee65c7a062bcd5c8a2fbe474568308`. Full message and sources: parent 1.

Declares ActorDamageByBlockSource subclass and implements getBlock as dereferencing stored const Block pointer. Constructor, isBlockSource, death message and clone are only declarations in this change; raw pointer neither owns nor validates block lifetime. Native layout scaffolding is not a complete public block-damage implementation.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-206"></a>
### 206. feat: make `ValueOrRef` movable but not copyable {#commit-206}

[e1f55fa4f1fb1f13f9c0b1121957233c1ad37903](https://github.com/EndstoneMC/endstone/commit/e1f55fa4f1fb1f13f9c0b1121957233c1ad37903) · 2025-02-02T10:35:49Z · author Vincent.

Parents: `274dca39a8b496ff1fa2ccb7756d9a9a41e9e24d`. Full message and sources: parent 1.

Makes ValueOrRef explicitly move-only, initializes union alternatives through constructors and restores const-correct value access. EventVariantImpl hides its variant behind visit, while EventRef requests default copying despite now noncopyable variant elements;209 supplies explicit reference-based variant copying. Existing callers still access event.variant until209, so this intermediate change is not a proved buildable tree. Coordinator Continue spelling0x1→1 has no value change.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-207"></a>
### 207. feat: move `DimensionType` to separate header file {#commit-207}

[eebdf50f9c4ad7dd28a529ac691b9ad55ce80234](https://github.com/EndstoneMC/endstone/commit/eebdf50f9c4ad7dd28a529ac691b9ad55ce80234) · 2025-02-02T11:16:44Z · author Vincent.

Parents: `e1f55fa4f1fb1f13f9c0b1121957233c1ad37903`. Full message and sources: parent 1.

Separates DimensionType alias into its own header and updates includes. Also removes three unimplemented OwnerPtr declarations (getWeakRef and null comparisons), beyond the title. Type alias value/layout remains AutomaticID<Dimension,int>; no new ownership semantics implemented.

Coverage: 6 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-208"></a>
### 208. refactor: remove redundant object copying in `Player::getPing` {#commit-208}

[38c43f4acf7172d012edc55ae08f71728a9f6f72](https://github.com/EndstoneMC/endstone/commit/38c43f4acf7172d012edc55ae08f71728a9f6f72) · 2025-02-02T14:53:51Z · author Vincent.

Parents: `eebdf50f9c4ad7dd28a529ac691b9ad55ce80234`. Full message and sources: parent 1.

Allows implicit AddressOrGUID construction from SystemAddress/RakNetGUID and passes player's GUID directly to GetAveragePing instead of naming an adapter local. A required implicit conversion can still create a temporary; the source change alone proves neither a copy count nor speedup. Existing component/peer assumptions unchanged.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-209"></a>
### 209. refactor: use `EventVariantImpl::visit` instead of `std::visit` {#commit-209}

[e177ef72c12d01a7ef24664568b1d2631f32b94a](https://github.com/EndstoneMC/endstone/commit/e177ef72c12d01a7ef24664568b1d2631f32b94a) · 2025-02-02T14:54:59Z · author Vincent.

Parents: `38c43f4acf7172d012edc55ae08f71728a9f6f72`. Full message and sources: parent 1.

Repairs206 integration: all gameplay handlers use EventVariantImpl::visit and EventVariantImpl copying constructs a reference alternative to the original event value, choosing cref/ref via constness. EventRef separately constrains const/nonconst source constructors and asserts copyability. This is aliasing copy, not deep event ownership; reference lifetime remains external. Player damage visitor removes unused alive-branch TODO, retaining death handling. No event-reference lifetime tests added.

Coverage: 7 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-210"></a>
### 210. refactor: move ansi codes lookup map from header to implementation file {#commit-210}

[10e2748ffc1654219c8d81ac3926eb4f22d77ef7](https://github.com/EndstoneMC/endstone/commit/10e2748ffc1654219c8d81ac3926eb4f22d77ef7) · 2025-02-02T14:56:35Z · author Vincent.

Parents: `e177ef72c12d01a7ef24664568b1d2631f32b94a`. Full message and sources: parent 1.

Moves ANSI mapping to one static const class map defined in the implementation, instead of one const map per formatter instance. Entries are unchanged; this changes storage/allocation topology as well as file placement. No performance measurement. Formatting-code source citation remains upstream attribution, not independently reviewed documentation.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-211"></a>
### 211. refactor: remove state checking from EndstoneBlock::at {#commit-211}

[7c7e4b943a7346b41b2186e818c665f5aa656b4c](https://github.com/EndstoneMC/endstone/commit/7c7e4b943a7346b41b2186e818c665f5aa656b4c) · 2025-02-08T15:03:10Z · author Vincent.

Parents: `10e2748ffc1654219c8d81ac3926eb4f22d77ef7`. Full message and sources: parent 1.

EndstoneBlock::at now always creates a shared wrapper instead of checking loaded/ticking/world-height validity. Block break/interact/explosion adaptation stops suppressing events on wrapper-creation errors. Placement still calls getRelative(...).value() without checking its Result, an intermediate mismatch removed213. This shifts validation policy; it does not make native BlockSource lifetime owned or all coordinates valid.

Coverage: 4 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-212"></a>
### 212. refactor: remove std::enable_shared_from_this from BlockState {#commit-212}

[64509e386e737d0946b440fbc731934cad1dbb17](https://github.com/EndstoneMC/endstone/commit/64509e386e737d0946b440fbc731934cad1dbb17) · 2025-02-08T15:10:29Z · author Vincent.

Parents: `7c7e4b943a7346b41b2186e818c665f5aa656b4c`. Full message and sources: parent 1.

Reverses shared ownership for captured BlockState: captureState returns unique_ptr, BlockPlaceEvent owns unique_ptr and pybind uses default holder; BlockState no longer inherits enable_shared_from_this. Block wrappers remain shared. This is a public ABI/ownership distinction between live location wrappers and captured state, not just base-class cleanup.

Coverage: 6 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-213"></a>
### 213. refactor: simplify error handling for methods in `Block` class {#commit-213}

[fcb843dc085a15b5d0dc995d14d79944313b5ef7](https://github.com/EndstoneMC/endstone/commit/fcb843dc085a15b5d0dc995d14d79944313b5ef7) · 2025-02-10T22:31:55Z · author Vincent.

Parents: `64509e386e737d0946b440fbc731934cad1dbb17`. Full message and sources: parent 1.

Removes Block::isValid and checkState entirely, makes getters/relative blocks and Dimension block lookups return values/shared pointers rather than Result. Setters retain parse/null-data errors but no loaded/ticking/height validation; setBlock return value is not checked. Cleans211's unchecked Result.value call by changing the return type. Public error and ABI contract changes are broader than simplified syntax; no runtime safety argument supplied.

Coverage: 7 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-214"></a>
### 214. Merge remote-tracking branch 'origin/main' {#commit-214}

[ad73c24e827d6319d2b5752bcded49184035c64e](https://github.com/EndstoneMC/endstone/commit/ad73c24e827d6319d2b5752bcded49184035c64e) · 2025-02-10T22:32:38Z · author Vincent.

Parents: `fcb843dc085a15b5d0dc995d14d79944313b5ef7`, `88ee0265be71cf8e07fe376cc346d79cfdb12087`. Full message and sources: parent 1, parent 2.

Two-parent merge imports daoge's88ee0265 PR132 collision-shape exporter. First-parent delta exactly equals that collaborator's patch; second-parent delta exactly equals prior target chain211–213, with no additional resolution change. Context patch read once with author attribution kept separate. Export format changes collisionShape from one six-coordinate box to a list of six-coordinate boxes via addCollisionShapes and ADL to_json, retaining the field name. Merge involvement is not sole authorship.

Coverage: 15 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-215"></a>
### 215. refactor: simplify error handling for methods in `BlockState` class {#commit-215}

[3b5a0c42d518c6dfa04d49258269f1425801cea0](https://github.com/EndstoneMC/endstone/commit/3b5a0c42d518c6dfa04d49258269f1425801cea0) · 2025-02-10T22:42:55Z · author Vincent.

Parents: `ad73c24e827d6319d2b5752bcded49184035c64e`. Full message and sources: parent 1.

Extends213's plain-pointer/error simplification to BlockState: getBlock returns shared_ptr and update overloads return bool, preserving type-mismatch false unless force. Removes now-inapplicable lookup error propagation. Also reformats/renames parameters in collaborator collision-shape forwarding without changing its call arguments. No update failure test added.

Coverage: 6 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-219"></a>
### 219. feat: add `ChunkPos` class {#commit-219}

[ae2f77d0083f08e6745a516b91f474a46a0e28c4](https://github.com/EndstoneMC/endstone/commit/ae2f77d0083f08e6745a516b91f474a46a0e28c4) · 2025-02-11T12:04:24Z · author Vincent.

Parents: `f40f8800e2e23ddb4efb2dfaea5c7ea7eec7413e`. Full message and sources: parent 1.

Adds ChunkPos constructors, initializes packed storage and floors Vec3 through BlockPos before shifting coordinates by4. The nested anonymous union places x and z in the same storage rather than a struct, so assigning z overwrites x in this intermediate declaration. Removes explicit on BlockPos(Vec3), allowing implicit conversion. Parameter names in ChunkSource only clarify intent; no coordinate tests added.

Coverage: 3 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-220"></a>
### 220. feat: improve `Level::getDimension` {#commit-220}

[789099ec07a12c8114fd30daec3999d5f8acd5a1](https://github.com/EndstoneMC/endstone/commit/789099ec07a12c8114fd30daec3999d5f8acd5a1) · 2025-02-11T12:36:10Z · author Vincent.

Parents: `ae2f77d0083f08e6745a516b91f474a46a0e28c4`. Full message and sources: parent 1.

Accepts exact lowercase the_end alias before lowercasing dimensions for lookup. Other mixed-case underscore spellings are not normalized by that pre-lowercase equality branch. std::ranges::transform replaces std::transform; no broader alias or locale contract inferred.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-289"></a>
### 289. feat: add python bindings for `Dimension::getHighestBlockAt` {#commit-289}

[75a2d76735b88f00932556fd0984f5893f15f59d](https://github.com/EndstoneMC/endstone/commit/75a2d76735b88f00932556fd0984f5893f15f59d) · 2025-02-21T12:11:34Z · author Vincent.

Parents: `18ab3c33a98079d51e2bdd1314015c888d956695`. Full message and sources: parent 1.

Adds highest-block Python bindings/stubs and changes core returned height to native height minus1. Title hides off-by-one behavior repair; no test establishes empty-world/min-height boundary.

Coverage: 4 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-290"></a>
### 290. feat: add `Actor::remove` to despawn an actor from the world {#commit-290}

[0f0de32dfb43747e8e8b2cbf36b038d8a1c80ce3](https://github.com/EndstoneMC/endstone/commit/0f0de32dfb43747e8e8b2cbf36b038d8a1c80ce3) · 2025-02-21T14:14:02Z · author Vincent.

Parents: `75a2d76735b88f00932556fd0984f5893f15f59d`. Full message and sources: parent 1.

Adds Actor::remove through C++ hierarchy and Python. Nonplayers forward native remove; Player override logs an error and directs callers to kick instead of removing. This lifetime-sensitive feature precedes weak-handle migration296–299.

Coverage: 9 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-296"></a>
### 296. refactor: `endstone::Actor` now manages WeakEntityRef instead of direct reference {#commit-296}

[8e144ea31667dc436cce1a546940659ba4cc95fa](https://github.com/EndstoneMC/endstone/commit/8e144ea31667dc436cce1a546940659ba4cc95fa) · 2025-02-23T14:49:32Z · author Vincent.

Parents: `b7a6338257fd0732b7a11c64c096f3b38f127e7d`. Full message and sources: parent 1.

Introduces EntityContext weak-ref access and changes EndstoneActor stored native Actor& to WeakEntityRef. Does not yet rewrite all users, so this is a staged migration completed299. Weak registry/entity identity is not strong lifetime ownership.

Coverage: 8 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-297"></a>
### 297. feat: add `Actor::isValid` {#commit-297}

[de49d084e7917fde9c0ff87ece490dfe88e97d39](https://github.com/EndstoneMC/endstone/commit/de49d084e7917fde9c0ff87ece490dfe88e97d39) · 2025-02-23T16:17:48Z · author Vincent.

Parents: `8e144ea31667dc436cce1a546940659ba4cc95fa`. Full message and sources: parent 1.

Adds Actor::isValid public API and Python property plus const handle accessor; implementation arrives299. Docs promise false for dead/despawned/not-added entities, but code-level predicate must be read separately.

Coverage: 3 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-299"></a>
### 299. refactor: access actor handles using WeakEntityRef {#commit-299}

[e115658d4237673aa9002f033debd8882452b2ec](https://github.com/EndstoneMC/endstone/commit/e115658d4237673aa9002f033debd8882452b2ec) · 2025-02-23T16:54:47Z · author Vincent.

Parents: `d86e3e8463543ac81b369753b325d0854d63b99c`. Full message and sources: parent 1.

Rewrites Actor/Mob/Player operations and scoreboard/boss/command/server users through weak-handle unwrap, removing stored Mob&/Player&. getHandle now throws runtime_error if missing; isValid returns unwrap-success and isAlive. isDead and other ordinary getters can therefore throw after despawn rather than being universally safe probes. Type-checked weak unwrap replaces an explicit player test for block placement. Player inventory still originates from native Player reference, so migration is not a proof every dependent wrapper is lifetime-safe. No weak-expiry/reentrancy tests were added.

Coverage: 12 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.
