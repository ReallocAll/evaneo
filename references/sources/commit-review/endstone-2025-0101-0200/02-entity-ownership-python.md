<!-- retrieval: {"source_ids":["public:commit:05f0a5127429719cb9635a81d4d175ec9818c500","public:commit:064f11363df1bd08c8af90b7db103cb5e877aecf","public:commit:0f79aec3dc9fa0011f574ca6b71b9b5abd1ebbb5","public:commit:10251b7ad86a354729059d7e42eb680eff65abbd","public:commit:13d4ab54264916b8600fba2517b88625f745d342","public:commit:13db38e64ab42b6a5aea554352b3feb52a6d5195","public:commit:6afcb13c8abcd47124f5741e1d455e6efed9fc7a","public:commit:76418abd20cafb2a86b54e0f71d7b8a30a33a900","public:commit:83a6a25f07cf70b6ca04527111ad4a3425bc7845","public:commit:95f9ee6a18f89b2148e25c85da79660856e3dbea","public:commit:a52312f1f251a7b25a405b2429c631a92110cb9e","public:commit:a68fd253a1cb60a32fb26283cab23d1d5da57054","public:commit:aaf55212e715699f5f3be62803a2dc2e7482d684","public:commit:ad7772ae60f8d56d1daeb110d833b637b85e1ba4","public:commit:b8c54efa76fc74cbd3925b345d8f760a152d321e","public:commit:bbbcac31a344fd6bd7442b98904b49330eef8bf1","public:commit:bcf86bdc6af9c1e6f4e6a14092dd30f5303af4ed","public:commit:ea2201597a0bb0fcb5a91ea33b71e2b284c9d820","public:commit:f1f4bbf005dca31025496223921f88b898b19e12","public:commit:f762b1e1cc1a12462fb1977a055417592ce9bd7b","public:thread:EndstoneMC/endstone:91"],"source_type":"public","date":"2024-11-15..2025-01-24","topics":["lifetime","concurrency","ffi","testing","api","documentation","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Entity references, typed wrappers and Python boundaries {#entity-references-typed-wrappers-and-python-boundaries}

## From a weak handle to a usable entity {#from-a-weak-handle-to-a-usable-entity}

The native player payload reconstruction101 creates the demand for reliable extraction. The sequence155–160 distinguishes configuration/ABI shape, weak ownership, ECS validity and dynamic type. PUBLIC ENTT_NO_MIXIN and storage/page-size assertions make assumptions visible across consumers. EntityContext is a registry/ID view with an explicit registry.valid check. Shared-pointer storage now retains the lock rather than obtaining a raw pointer from a temporary owner; entity weak storage returns an optional context only after checking registry and entity validity. Player extraction requires PlayerComponent. Adapters skip Endstone dispatch when resolution fails and continue native forwarding.

This is a specific improvement, not universal memory safety. Entity contexts still borrow registry state; typed Actor pointers are not lifetime pins; const component access can remain mutable. OwnerPtr162 filters empty and wrong-level actors during enumeration, but no lock protects all concurrent invalidation.176 makes excluding removed entities the default and177 allows explicit overrides.180 separates dead from removed so a dead event subject need not disappear immediately.167's initial Mob test requires both exact type and category;182 relaxes that to either while making hasCategory an all-bits test. Its separate hasType function still performs exact equality for any nonzero request, so the name must not be taken as proof of a generic subset predicate.

<a id="wrapper-identity-and-language-contracts"></a>
## Wrapper identity and language contracts {#wrapper-identity-and-language-contracts}

183 first returns a cached ECS wrapper, then uses centralized Player/Mob extraction to choose its derived type.101's Python polymorphic bridge adds Mob between Actor and Player; this supports isinstance-based identification discussed in issue91. Wrapper identity helps repeated lookups, but lifetime is still tied to the entity component.106 introduces OfflinePlayer identity as a base of Player without implementing a disk-backed offline lookup.107 reorders virtual declarations without changing bodies; that is mechanical source organization with possible vtable ABI consequences.110 centralizes pybind headers and custom casters while preserving include order.

168 makes ActorEvent typed by Actor or Mob. Python's new MobEvent derives Event independently of ActorEvent, so a death event's class ancestry changes for consumers;184 later repairs the missing public export. Stronger static type information should be reviewed alongside source/API compatibility, not described as automatically backward compatible.113's shared wrapper around a const-cast native ItemStack and174's non-owning pointer accessors provide further counterexamples to treating smart-pointer spelling as payload ownership. A noexcept dereference path invoking a throwing check can terminate, and non-owner default/reset/destructor behavior requires separate scrutiny.

## Apply to a new task {#apply-to-a-new-task}

Trace a reference through owner existence, registry generation/ID validity, native type, removal state, wrapper cache and Python return policy. Ask exactly what object each smart pointer owns. Keep source compatibility, C++ ABI compatibility and Python isinstance behavior as separate checks. The code supplies useful mechanisms and visible limitations; it supplies no concurrent lifetime stress test, ABI test or measured overhead reduction.


## Per-commit evidence {#per-commit-evidence}

<a id="commit-101"></a>
### Commit 101 {#commit-101}

10251b7ad86a354729059d7e42eb680eff65abbd · 2025-01-11T23:34:08Z

[feat: add members for player events](https://github.com/EndstoneMC/endstone/commit/10251b7ad86a354729059d7e42eb680eff65abbd)

**Observed change.** Fills previously empty native player-event alternatives with WeakRef<EntityContext>, ItemStack, positions, damage-source ownership, game-mode and input fields. Replaces opaque ItemStack-sized arrays now that ItemStack is constructible; retains explicit 384/232-byte variant static assertions. Adds fixed-width/input enums, command-sender asMob and Mob override, and Python polymorphic dispatch Actor→Mob→Player.

**Causal interpretation.** ABI reconstruction requires both alternative layout and variant size, not just matching event names. The more specific Python type dispatch avoids treating all mobs as players. Static assertions are source constraints, not a verified native layout measurement.

**Limits.** No added executable tests; before/after native header context read in patches. Raw pointers exposed by asMob remove constness intentionally; no lifetime proof.

<a id="commit-106"></a>
### Commit 106 {#commit-106}

6afcb13c8abcd47124f5741e1d455e6efed9fc7a · 2025-01-12T15:01:42Z

[feat: add python binding for `OfflinePlayer` class](https://github.com/EndstoneMC/endstone/commit/6afcb13c8abcd47124f5741e1d455e6efed9fc7a)

**Observed change.** Introduces public OfflinePlayer identity interface(name, UUID), Player multiple inheritance from Mob and OfflinePlayer, and coordinated pybind bases, top-level import/export, stub and Skin docs.

**Causal interpretation.** Identity abstraction is made visible consistently in C++ and Python. The interface description promises disk-retrievable identity but this patch supplies no offline storage lookup implementation.

**Limits.** No persistence or offline-query runtime functionality claimed. Pure virtual getName returns string despite documentation mentioning null.

<a id="commit-107"></a>
### Commit 107 {#commit-107}

76418abd20cafb2a86b54e0f71d7b8a30a33a900 · 2025-01-12T15:21:14Z

[refactor: reorder methods in Player class](https://github.com/EndstoneMC/endstone/commit/76418abd20cafb2a86b54e0f71d7b8a30a33a900)

**Observed change.** Reorders Player virtual declarations and corresponding EndstonePlayer overrides into identity/action/experience/presentation/entity groups; introduces TODO slots, no method-body changes.

**Causal interpretation.** Source organization is mechanical but virtual declaration reordering can change a C++ vtable ABI; do not label binary compatibility preserved.

**Limits.** No ABI validation or binary compatibility evidence.

<a id="commit-109"></a>
### Commit 109 {#commit-109}

bcf86bdc6af9c1e6f4e6a14092dd30f5303af4ed · 2025-01-12T16:08:20Z

[feat: add getter and setter for player's sneaking and sprinting state](https://github.com/EndstoneMC/endstone/commit/bcf86bdc6af9c1e6f4e6a14092dd30f5303af4ed)

**Observed change.** Adds player sneak/sprint property APIs and Python properties. Native Actor/Mob getters read status flags; Endstone setters forward native setSneaking/setSprinting.

**Causal interpretation.** Keeps wrapper surface aligned with native state machinery rather than writing flags directly from public setters.

**Limits.** No simulation or client synchronization tests.

<a id="commit-110"></a>
### Commit 110 {#commit-110}

f1f4bbf005dca31025496223921f88b898b19e12 · 2025-01-12T17:13:57Z

[refactor: add a common header for the python binding](https://github.com/EndstoneMC/endstone/commit/f1f4bbf005dca31025496223921f88b898b19e12)

**Observed change.** Replaces repeated Python-binding includes with common endstone_python.h loading chrono,functional,operators,pybind,stl,filesystem before Endstone headers and custom polymorphic/type casters across16 translation units.

**Causal interpretation.** Centralizes caster visibility and preserves required pybind-before-Endstone include ordering noted by deleted scoreboard comment.

**Limits.** Header consolidation may broaden dependencies; no compile-time benefit measured.

<a id="commit-155"></a>
### Commit 155 {#commit-155}

95f9ee6a18f89b2148e25c85da79660856e3dbea · 2025-01-22T17:45:31Z

[fix: add the missing ENTT_NO_MIXIN definition for entt](https://github.com/EndstoneMC/endstone/commit/95f9ee6a18f89b2148e25c85da79660856e3dbea)

**Observed change.** Adds ENTT_NO_MIXIN as a PUBLIC compile definition for core.

**Causal interpretation.** Entt template configuration is an ABI contract across consumers, not just a private optimization; subsequent157 enforces expected plain storage and page size.

**Limits.** No mixed-consumer ABI test; one-line configuration change supports the156–158 model rather than an independent general preference.

<a id="commit-156"></a>
### Commit 156 {#commit-156}

ea2201597a0bb0fcb5a91ea33b71e2b284c9d820 · 2025-01-22T17:46:15Z

[feat: add methods in `EntityContext`](https://github.com/EndstoneMC/endstone/commit/ea2201597a0bb0fcb5a91ea33b71e2b284c9d820)

**Observed change.** EntityContext gains registry.valid(entity) isValid, copy/move constructors, deleted assignments and const entity ID; names registry alias and exposes protected entity/registry accessors.

**Causal interpretation.** A copied context is a view over the same ECS registry/ID, not ownership. Explicit validity becomes the precondition later used when locking weak references.

**Limits.** Const component access remains mutable. _getRegistryId returns entity_, despite its name; do not infer an independently modeled registry identifier.

<a id="commit-157"></a>
### Commit 157 {#commit-157}

83a6a25f07cf70b6ca04527111ad4a3425bc7845 · 2025-01-22T17:48:45Z

[refactor: clean up the implementation of `EntityId` type](https://github.com/EndstoneMC/endstone/commit/83a6a25f07cf70b6ca04527111ad4a3425bc7845)

**Observed change.** Makes EntityId default to invalid(-1), hides raw conversion behind friends, moves entt traits and EnTTRegistry alias alongside it. Replaces a bespoke storage specialization with static assertions for2048 page size and expected plain storage under ENTT_NO_MIXIN.

**Causal interpretation.** Moves assumptions from an ad hoc storage override into centralized configuration plus compile-time checks; reduces accidental construction of arbitrary entity IDs.

**Limits.** Static assertions constrain the compiled headers only, not compatibility with the live native registry or all plugin build flags.

<a id="commit-158"></a>
### Commit 158 {#commit-158}

13d4ab54264916b8600fba2517b88625f745d342 · 2025-01-22T20:00:56Z

[refactor: correct the implementation of `gamerefs` objects](https://github.com/EndstoneMC/endstone/commit/13d4ab54264916b8600fba2517b88625f745d342)

**Observed change.** Reworks GameRefs storage/facade layers: weak shared pointers lock into a retained shared_ptr; entity weak registry locks and registry.valid are checked before producing optional EntityContext; StackRefResult exposes bool/value/operators through protected storage APIs. WeakEntityRef::tryUnwrap<T> performs checked context lookup then T::tryGetFromEntity. Actor dimension/devtools call sites adapt.

**Causal interpretation.** Separates whether a weak reference was set, whether its owner still exists, and whether its entity ID remains valid. Eliminates the old temporary shared-owner/raw-pointer access pattern for shared storage.

**Limits.** Entity results and returned Actor pointers are still non-owning views; no general concurrent registry or actor lifetime guarantee.32/24-byte layout assertions are not runtime proof.

<a id="commit-159"></a>
### Commit 159 {#commit-159}

b8c54efa76fc74cbd3925b345d8f760a152d321e · 2025-01-22T20:17:06Z

[feat: add `Player::tryGetFromEntity`](https://github.com/EndstoneMC/endstone/commit/b8c54efa76fc74cbd3925b345d8f760a152d321e)

**Observed change.** Adds Player::tryGetFromEntity by requiring PlayerComponent before using Actor lookup and casting.

**Causal interpretation.** Type-specific extraction is centralized instead of trusting arbitrary actor pointers at every event adapter; used broadly160 and in canonical factory183.

**Limits.** Component presence/type compatibility remains a native invariant; no adversarial component or removed-entity test.

<a id="commit-160"></a>
### Commit 160 {#commit-160}

f762b1e1cc1a12462fb1977a055417592ce9bd7b · 2025-01-22T20:19:27Z

[refactor: use WeakEntityRef in event handlers](https://github.com/EndstoneMC/endstone/commit/f762b1e1cc1a12462fb1977a055417592ce9bd7b)

**Observed change.** Migrates event adapters for chat/forms/interactions/block/death and actor spawn to WeakEntityRef::tryUnwrap, centralizing null, expired and type checks. Selected native player event payloads become WeakEntityRef.

**Causal interpretation.** Invalid or no-longer-resolvable entities now skip Endstone dispatch and retain default native forwarding, instead of dereferencing optional storage or duplicating isPlayer checks.

**Limits.** This is fail-open event behavior, not retention of the entity. Event callback references and shared block wrappers still depend on external native lifetimes.

<a id="commit-162"></a>
### Commit 162 {#commit-162}

a68fd253a1cb60a32fb26283cab23d1d5da57054 · 2025-01-22T22:08:03Z

[refactor: correct implementation of `OwnerStorageEntity` and `OwnerPtr`](https://github.com/EndstoneMC/endstone/commit/a68fd253a1cb60a32fb26283cab23d1d5da57054)

**Observed change.** Makes entity OwnerStorage noncopyable with checked optional access; OwnerPtr gains explicit bool/value/operators and common storage facade. Owner-to-stack conversion handles empty owners. Level actor enumeration checks owner presence, actor validity and same level before exposing actors.

**Causal interpretation.** Carries the158 distinction between owned storage, optional availability and borrowed stack view through enumeration instead of unchecked get calls.

**Limits.** No concurrency or cross-level lifecycle tests. Successful extraction is still a point-in-time view, not an enduring pin on an actor.

<a id="commit-167"></a>
### Commit 167 {#commit-167}

05f0a5127429719cb9635a81d4d175ec9818c500 · 2025-01-23T15:59:04Z

[feat: add `Mob::tryGetFromEntity`](https://github.com/EndstoneMC/endstone/commit/05f0a5127429719cb9635a81d4d175ec9818c500)

**Observed change.** Adds Mob::tryGetFromEntity after Actor lookup, rejecting unless both isType(Mob) and hasCategory(Mob) hold.

**Causal interpretation.** Centralizes typed extraction but the initial conjunction is stricter than the later intended acceptance rule;182 changes it to accept either type or category.

**Limits.** Do not present167 alone as the final type policy. No test covers distinct native actors satisfying only one condition.

<a id="commit-168"></a>
### Commit 168 {#commit-168}

a52312f1f251a7b25a405b2429c631a92110cb9e · 2025-01-23T16:39:07Z

[refactor: change ActorEvent to support templated actor types](https://github.com/EndstoneMC/endstone/commit/a52312f1f251a7b25a405b2429c631a92110cb9e)

**Observed change.** Templates ActorEvent by actor type; death and knockback use Mob, while spawn/remove/teleport/explode use Actor. Python introduces MobEvent deriving Event separately from ActorEvent, and updates event bindings/stubs and player-death inheritance.

**Causal interpretation.** Typed event access prevents representing a death/knockback subject as an arbitrary non-mob actor, but changes Python isinstance hierarchy and C++ source contracts.

**Limits.** MobEvent is not publicly re-exported until184. Python MobEvent is not an ActorEvent subclass in this binding; consumers need migration awareness. No compatibility tests.

<a id="commit-174"></a>
### Commit 174 {#commit-174}

aaf55212e715699f5f3be62803a2dc2e7482d684 · 2025-01-24T21:12:00Z

[refactor: simplify NonOwnerPointer constructors](https://github.com/EndstoneMC/endstone/commit/aaf55212e715699f5f3be62803a2dc2e7482d684)

**Observed change.** NonOwnerPointer gains implicit pointer/reference construction, explicit bool, defaulted copy/move and const/nonconst operators; reset/destructor still operate through checked _get.

**Causal interpretation.** Improves use of vendor-style non-owning pointers without conferring ownership. The checked accessor throws on invalidity while operators are noexcept, and a throwing reset in a destructor can terminate.

**Limits.** These exception/lifetime hazards are static observations, including pre-existing behavior; no guarantee that default or invalid non-owner pointers are safely destructible.

<a id="commit-176"></a>
### Commit 176 {#commit-176}

bbbcac31a344fd6bd7442b98904b49330eef8bf1 · 2025-01-24T21:43:05Z

[feat: set default value for 'include_removed' in tryGetFromEntity](https://github.com/EndstoneMC/endstone/commit/bbbcac31a344fd6bd7442b98904b49330eef8bf1)

**Observed change.** Sets include_removed=false defaults on Actor, Mob and Player typed extraction APIs.

**Causal interpretation.** Makes safe ordinary lookup the default, with exceptional removed-entity access explicit.

**Limits.** Default validity is dependent on native removed state, corrected180; removed-event adapters must consider whether they need the exceptional path.

<a id="commit-177"></a>
### Commit 177 {#commit-177}

064f11363df1bd08c8af90b7db103cb5e877aecf · 2025-01-24T21:43:18Z

[feat: add variadic template support to `tryUnwrap` method](https://github.com/EndstoneMC/endstone/commit/064f11363df1bd08c8af90b7db103cb5e877aecf)

**Observed change.** WeakEntityRef::tryUnwrap perfectly forwards optional arguments to T::tryGetFromEntity instead of hard-coding false.

**Causal interpretation.** Keeps the centralized safe default while allowing lifecycle-specific callers to request removed entities.

**Limits.** No call in the removal adapter181 opts into include_removed=true by200; emission timing determines the consequence.

<a id="commit-182"></a>
### Commit 182 {#commit-182}

ad7772ae60f8d56d1daeb110d833b637b85e1ba4 · 2025-01-24T23:01:49Z

[fix: correct the implementation of `Actor::hasCategory`](https://github.com/EndstoneMC/endstone/commit/ad7772ae60f8d56d1daeb110d833b637b85e1ba4)

**Observed change.** Changes hasCategory to require all requested category bits; adds ActorType mask operator and hasType; Mob extraction now rejects only if neither exact Mob type nor Mob category matches, relaxing167. Wrapper factory follows type-or-category logic.

**Causal interpretation.** Type identity and category membership are different contracts. Correcting the conjunction improves valid Mob extraction while all-bits category checks remove ambiguous partial matches.

**Limits.** hasType branches on a nonzero requested ActorType value and then requires exact equality; only a zero request reaches the trivially true subset check. It therefore is not a general subset predicate despite the bitmask expression. No category/type matrix tests.

<a id="commit-183"></a>
### Commit 183 {#commit-183}

13db38e64ab42b6a5aea554352b3feb52a6d5195 · 2025-01-24T23:15:08Z

[refactor: simplify `Actor::getEndstoneActor`](https://github.com/EndstoneMC/endstone/commit/13db38e64ab42b6a5aea554352b3feb52a6d5195)

**Observed change.** Canonical EndstoneActor wrapper factory first returns cached ECS component, then uses Player::tryGetFromEntity and Mob::tryGetFromEntity to select derived wrapper, eliminating duplicated type tests and exception path.

**Causal interpretation.** One typed lookup policy and cached wrapper identity reduce divergent public/Python type behavior.

**Limits.** Cached wrapper lifetime remains tied to the entity component; externally retained references are not kept alive by this cache.

<a id="commit-184"></a>
### Commit 184 {#commit-184}

0f79aec3dc9fa0011f574ca6b71b9b5abd1ebbb5 · 2025-01-24T23:16:11Z

[feat: export MobEvent in event.py](https://github.com/EndstoneMC/endstone/commit/0f79aec3dc9fa0011f574ca6b71b9b5abd1ebbb5)

**Observed change.** Adds MobEvent import/export in endstone.event.

**Causal interpretation.** Completes the public Python surface introduced168; mechanical integration repair, not a separate architecture lesson.

**Limits.** Does not restore MobEvent-as-ActorEvent inheritance or add compatibility tests.
