<!-- retrieval: {"source_ids":["public:commit:0102824f0a0c27f6504989729bb716f9d600a389","public:commit:06abe3c782136892e0fa2dac5b4ecd45fc36ab18","public:commit:095911b1757a9b0ffe4e808f62eeab088ca7b3ce","public:commit:0a69ee3d9ee15920de8cdaba2c466c016c62d37c","public:commit:0d35ccfa25dd5673daef14d9e7310583ee5bcdc1","public:commit:12767cf5585bdaf2ff049b4a17acccce30f746f5","public:commit:295e76054cb212fc44236d4bca0e5945a5101166","public:commit:2baf0e951976aac5fd0bab2992645d676d95de62","public:commit:3a54aab0dd60347b9e21214e4135e94c76645948","public:commit:3e7d5bd869fdfcf6a623dd79bdfe0194eb10d868","public:commit:449160dc2e8918c5b4a750df03ac38d39ebd56c6","public:commit:4df58eea3f6f4fa2052640cef7fe96312a6facf6","public:commit:529c2fade2e33bb4b9d14e6e3ef88d0bbf1bce5c","public:commit:5b78f74a197b21cbe89393e2bcc4da1ebb28a811","public:commit:67e57267cca26f5f3f59ca6f866d706519553e70","public:commit:6ca3f27365156b92d6a61aa3c0a908f861293602","public:commit:6dfbcd387024f1b7bdb14af23df9b7c58cea5982","public:commit:71a8e0fb30c720e88124bd942d6eee5afb4252f9","public:commit:733f5b3f6d2169a7aa7982d0928a6ec39e82c336","public:commit:809b3ca3773331027ccadbc0cd6008e3278553e8","public:commit:8e18f36933f0317681e3331bae423c51ace08460","public:commit:8f5f6c4637aa2f18eb33e6eb847e155c6ab30d8f","public:commit:9e68e6140a9cae4fa85bb10f8f7a855eeac48213","public:commit:c9a8d9bb14f30fade84ebd20fb558f8d7a1ea209","public:commit:f4fd8215d016b25974fba0e4040c94136dad66da","public:commit:f63813ee89c0e9febffeb263ec2a820a61f7964f"],"source_type":"public","date":"2025-01-12..2025-01-25","topics":["lifetime","concurrency","ffi","testing","build","recovery","api","diagnosis","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Event coordination, cancellation and lifecycle {#event-coordination-cancellation-and-lifecycle}

## Decision chain and working model {#decision-chain-and-working-model}

These are historical changes ending at commit200 (2025-01-29). Read the indexed per-commit entries below for exact source identity, evidence and limits. Source inspection is complete for this assigned slice; runtime behavior is unverified.

The first100 sibling dossier establishes owned wrappers around scripting, weather and block event handlers. This slice extends that approach to player forms (111), chat (112), interactions (113–114), level spawn (153), actor death (165–166), removal (181) and player death/join/quit (186–188). Each wrapper holds the vendor's original handler in a unique_ptr, selectively visits a native variant, translates public cancellation into native handler/coordinator return values where available, then forwards unaffected events. Removing a function detour is more than a symbol-table cleanup: callback order can move from after the original method to before the original event handler. Spawn cancellation despawns but still forwards. Public event names and C++ classes therefore cannot stand in for behavioral-equivalence evidence.

Cancellation is a three-part contract: the public capability, language binding and native side effect must agree. Commit115 repairs the false isCancellable result, adds ScriptMessageEvent native cancellation, and116 updates Python inheritance. Game-mode change initially stays noncancellable in119 because an inline author comment says the vendor sends client packets regardless, causing desynchronization.151 deliberately reverses that choice: it broadcasts the old mode with a replay tick before returning native cancellation. This is compensation across a client/server boundary, not proof of an upstream fix. No cancellation regression tests or native client traces accompany these changes.

The owned-wrapper architecture reveals a lifecycle constraint in190. Vincent's message reports a crash reloading with Script API. Simply forwarding through a base interface was not sufficient for vendor reload expectations: all six wrappers now return their original unique_ptr before reloadData and are installed again afterwards. The code establishes original-handler identity during that interval. It does not prove asynchronous resource reload completion, guarantee reinstallation if an exception occurs, or make unchecked static_cast unwrap idempotent. Destructor unregistration also assumes level initialization completed and wrappers are installed. These preconditions are useful review questions, not demonstrated crash reproductions.

## API presence versus reachable behavior {#api-presence-versus-reachable-behavior}

Piston payload/API work120/122 is unfinished: the native handler remains TODO and no public dispatch is supplied. Emote163 and respawn164 have public classes, bindings, stubs and handler methods, yet endpoint200 confirms their visitor predicates sit in the CoordinatorResult visitor, whose alternatives exclude both types. Both belong to the void variant, whose visitor does not select them. This is an exact source reachability gap despite complete-looking API surface. The native ABI shells must still match variant order, payload size, virtual slot and platform alignment; declared static assertions only constrain this compilation, not the running vendor binary.

Other migration review traps: ordinary weak extraction excludes removed actors, so181 may miss ActorRemovedEvent depending on when native removed_ becomes true;186 suppresses the vendor death sender and broadcasts itself without the old shouldShowDeathMessages gate;187/188 change join/quit ordering relative to native handling. These are bounded static concerns, with native emission timing and actual gamerule behavior untested.185's initialization guards and --no-undefined expose some failures earlier but are not synchronization or rollback.

## Apply to a new task {#apply-to-a-new-task}

When replacing hooks with event decorators, enumerate all variant alternatives and return semantics; compare pre/post-original ordering; identify borrowed payload lifetimes; spell out ownership during startup, shutdown and reload; and test cancellation at observable side effects, not only the boolean property. A useful test matrix would include retained callback objects, absent entities, each void/coordinator variant, repeated reload, exception/partial initialization, death gamerules and game-mode client reconciliation. This review proposes that matrix; it did not execute it.


## Per-commit evidence {#per-commit-evidence}

<a id="commit-111"></a>
### Commit 111 {#commit-111}

8e18f36933f0317681e3331bae423c51ace08460 · 2025-01-12T17:19:31Z

[refactor: clean up player events implementation](https://github.com/EndstoneMC/endstone/commit/8e18f36933f0317681e3331bae423c51ace08460)

**Observed change.** Replaces PlayerEventCoordinator sendEvent binary hook/symbols with owned PlayerGameplayHandler decorator in native coordinator. Decorator visits form close/response and delegates native behavior; weak entity lookup tolerates missing actor. Form IDs become uint32_t consistently in packet,event,callbacks and map. EndstoneMob explicitly resolves asMob.

**Causal interpretation.** Moves event interception to modeled gameplay-handler ownership, retaining original handler in unique_ptr and native forwarding. Existing0xffff form-ID starting point remains an explicit Script API collision mitigation.

**Limits.** At this stage actor lookup lacks isPlayer guard(fixed113). Form callbacks always return true, so native forwarding remains. Ownership/reload implications examined later190; no runtime proof.

<a id="commit-112"></a>
### Commit 112 {#commit-112}

9e68e6140a9cae4fa85bb10f8f7a855eeac48213 · 2025-01-12T18:24:49Z

[refactor: improve chat event](https://github.com/EndstoneMC/endstone/commit/9e68e6140a9cae4fa85bb10f8f7a855eeac48213)

**Observed change.** Replaces _displayGameMessage hook with ServerNetworkEventHandler decorator and native mutable event variant. Chat layout now includes filtered_message and targets; adds incoming/outgoing packet alternatives. Splits server instance/network event headers and corrects server instance nonowner fields. Plugin cancellation bypasses listeners with CoordinatorResult::Cancel; modified text then forwards original handler and logs.

**Causal interpretation.** Interception is relocated to protocol's event coordinator while preserving default handler; complete variant alternatives matter to ABI. Mutable chat data propagates plugin edits.

**Limits.** No packet-event public behavior added; merely layout alternatives. No runtime filter/logging correctness verification. getMessage return type must govern whether std::move actually moves.

<a id="commit-113"></a>
### Commit 113 {#commit-113}

71a8e0fb30c720e88124bd942d6eee5afb4252f9 · 2025-01-12T18:53:17Z

[refactor: improve PlayerInteractEvent](https://github.com/EndstoneMC/endstone/commit/71a8e0fb30c720e88124bd942d6eee5afb4252f9)

**Observed change.** Moves block interaction from GameMode::useItemOn hook to PlayerInteractWithBlockBeforeEvent. Locks weak player, adds isPlayer checks, resolves loaded block, wraps nullable item, dispatches cancellation then forwards native handler. EndstoneItemStack accepts const native ItemStack but stores const_cast pointer. Removes reserved ConnectionOriginal event workaround.

**Causal interpretation.** Event boundary preserves native cancellation semantics through CoordinatorResult and avoids version-specific method hook. isPlayer guards repair unsafe typed access from111.

**Limits.** Wrapper remains a borrowed native item despite shared_ptr wrapper; const_cast/lifetime implications require care. Missing block logs and forwards; no test for retained callback item.

<a id="commit-114"></a>
### Commit 114 {#commit-114}

295e76054cb212fc44236d4bca0e5945a5101166 · 2025-01-12T19:09:32Z

[refactor: improve PlayerInteractActorEvent](https://github.com/EndstoneMC/endstone/commit/295e76054cb212fc44236d4bca0e5945a5101166)

**Observed change.** Moves actor interaction from GameMode::interact to PlayerInteractWithEntityBeforeEvent, validates player and target weak refs, emits public event and translates cancellation. Removes GameMode symbols and obsolete/empty hook files/build entries.

**Causal interpretation.** Continues111–113 coordinator-decorator migration; no event if either entity is unavailable, native default behavior still forwards.

**Limits.** No automated interaction/cancellation test; original hook location vector was already unused.

<a id="commit-115"></a>
### Commit 115 {#commit-115}

6ca3f27365156b92d6a61aa3c0a908f861293602 · 2025-01-12T19:44:55Z

[fix: cancellable event interface](https://github.com/EndstoneMC/endstone/commit/6ca3f27365156b92d6a61aa3c0a908f861293602)

**Observed change.** Corrects Cancellable::isCancellable false→true, drops constexpr virtual declarations and redundant false overrides. ScriptMessageEvent now inherits Cancellable<ServerEvent>; scripting decorator translates plugin cancellation into bypass+cancel, with actor-or-console sender fallback and BlockCommandSender still TODO. Unrelated crash should_report false→true re-enables reporting.

**Causal interpretation.** Cancellation requires agreement between type hierarchy, capability check and native propagation; an API method alone was insufficient. Crash-report policy reversal must be retained separately from title.

**Limits.** No tests added for cancellation or crash reporting. Reporting change observed in code, not permission or telemetry execution.

<a id="commit-116"></a>
### Commit 116 {#commit-116}

06abe3c782136892e0fa2dac5b4ecd45fc36ab18 · 2025-01-12T20:04:45Z

[fix: ScriptMessageEvent should be cancellable](https://github.com/EndstoneMC/endstone/commit/06abe3c782136892e0fa2dac5b4ecd45fc36ab18)

**Observed change.** Completes115 Python side: ScriptMessageEvent pybind bases include ICancellable and stub inherits Cancellable.

**Causal interpretation.** C++ and Python inheritance metadata must agree for users to access cancellation.

**Limits.** No Python regression tests.

<a id="commit-119"></a>
### Commit 119 {#commit-119}

f63813ee89c0e9febffeb263ec2a820a61f7964f · 2025-01-12T22:08:06Z

[feat: add `PlayerGameModeChangeEvent`](https://github.com/EndstoneMC/endstone/commit/f63813ee89c0e9febffeb263ec2a820a61f7964f)

**Observed change.** Adds noncancellable public/Python PlayerGameModeChangeEvent and central GameMode conversion helper. Native mutable game-mode event is visited but always forwards. Author comment explains intentional constraint: BDS sends client mode packets irrespective of cancellation, creating client/server disagreement, also reported with Script API.

**Causal interpretation.** A seemingly available cancel hook is withheld until downstream client state can be repaired; this is a concrete compatibility tradeoff, later reversed151 with a workaround. Mapping unknown native types defaults Survival; invalid public enum reaches unreachable.

**Limits.** BDS bug is author-reported, not reproduced. Public include and stub exported; no tests.

<a id="commit-120"></a>
### Commit 120 {#commit-120}

3e7d5bd869fdfcf6a623dd79bdfe0194eb10d868 · 2025-01-12T22:34:44Z

[feat: add member fields for PistonActionEvent](https://github.com/EndstoneMC/endstone/commit/3e7d5bd869fdfcf6a623dd79bdfe0194eb10d868)

**Observed change.** Models PistonActionEvent block-source handle, position, byte PistonState and attached-block flag; visits piston action but handler is TODO returning true.

**Causal interpretation.** ABI/data preparation is distinct from working public piston support.

**Limits.** No emitted piston event or implementation outcome.

<a id="commit-122"></a>
### Commit 122 {#commit-122}

449160dc2e8918c5b4a750df03ac38d39ebd56c6 · 2025-01-14T16:59:29Z

[feat: add `BlockPistonEvent` base event](https://github.com/EndstoneMC/endstone/commit/449160dc2e8918c5b4a750df03ac38d39ebd56c6)

**Observed change.** Adds BlockPistonEvent holding shared block and borrowed Player&, includes it in block handler, but no dispatch/getter/cancellable inheritance despite cancellable include.

**Causal interpretation.** Incomplete scaffold must not be advertised as functioning piston or cancellation API.

**Limits.** 120 handler remains TODO. No Python exposure/test.

<a id="commit-151"></a>
### Commit 151 {#commit-151}

095911b1757a9b0ffe4e808f62eeab088ca7b3ce · 2025-01-15T21:04:52Z

[feat: make PlayerGameModeChangeEvent cancellable](https://github.com/EndstoneMC/endstone/commit/095911b1757a9b0ffe4e808f62eeab088ca7b3ce)

**Observed change.** Reverses119: PlayerGameModeChangeEvent becomes Cancellable<PlayerEvent>, Python gains ICancellable. On cancellation the native adapter broadcasts UpdatePlayerGameType with from_game_mode, unique actor ID and ReplayStateComponent current tick (fallback0), then returns Cancel/BypassListeners. Adds replay/history/policy/tick ABI shells and packet fields. Generated stub also adds111 identical conduit methods, structurally verified separately.

**Causal interpretation.** Cancellation becomes useful only after explicitly compensating the already-sent client mode update; this is a workaround for the earlier author-described client/server desynchronization, rather than evidence that the vendor bug vanished.

**Limits.** No client/server reproduction or regression test. Native replay layout and broadcast behavior unvalidated. All meaningful residual hunks read;111 repeated stub blocks are not111 independent lessons.

<a id="commit-152"></a>
### Commit 152 {#commit-152}

529c2fade2e33bb4b9d14e6e3ef88d0bbf1bce5c · 2025-01-15T21:38:01Z

[feat: add actor events](https://github.com/EndstoneMC/endstone/commit/529c2fade2e33bb4b9d14e6e3ef88d0bbf1bce5c)

**Observed change.** Reconstructs actor event payloads: weak entity references, ItemInstance, effects/duration, damage source pointers, definition modifier, HitResult/projectile/armor/riding data replace opaque padding. Adds ActorGameplayHandler's three virtual overloads and real coordinator handler/subscriptions, preserving event alternative order. Introduces supporting enums/handles and enforces uppercase class constants in clang-tidy.

**Causal interpretation.** Native integration requires exact payload shape and vtable/variant order before event bridging; declarations alone do not emit public events. This is substantive ABI modeling, not a cosmetic header split.

**Limits.** Layouts inferred in source/static assertions are not validated against a running binary; no new functional tests or complete damage-source implementation yet.

<a id="commit-153"></a>
### Commit 153 {#commit-153}

4df58eea3f6f4fa2052640cef7fe96312a6facf6 · 2025-01-15T22:20:26Z

[refactor: ActorSpawnEvent](https://github.com/EndstoneMC/endstone/commit/4df58eea3f6f4fa2052640cef7fe96312a6facf6)

**Observed change.** Moves ActorSpawnEvent from Actor::_postReloadActorAdded detour to LevelAddedActorEvent decorator. Non-player spawn cancellation calls despawn but still forwards the native event. Level coordinator becomes explicit EventCoordinator, and the level variant replaces ScriptInitialize with ScriptingWorldInitialize carrying script object/scope handles; full game-rule value/type/index declarations replace placeholders.

**Causal interpretation.** Consolidates interception on native event coordinators, but ordering changes: old detour called original before dispatch; new decorator dispatches before forwarding. Cancel means despawn here, not bypassing original listeners.

**Limits.** No ordering/reentrancy/despawn regression test. Script handles are reverse-engineered ABI models; cancellation does not prove the actor was never observed elsewhere.

<a id="commit-154"></a>
### Commit 154 {#commit-154}

6dfbcd387024f1b7bdb14af23df9b7c58cea5982 · 2025-01-15T23:33:24Z

[feat: add BlockSourceListener](https://github.com/EndstoneMC/endstone/commit/6dfbcd387024f1b7bdb14af23df9b7c58cea5982)

**Observed change.** Defines BlockSourceListener's complete pure-virtual callback surface and makes BlockSourceHandle a noncopyable abstract listener with a source pointer and bool conversion; removes old empty interface declarations.

**Causal interpretation.** A pointer-sized stand-in is insufficient when vendor objects participate in listener inheritance/vtable dispatch. The handle records liveness without taking ownership.

**Limits.** Dereference operators still assume a non-null source; native invalidation and virtual slot correspondence not exercised.

<a id="commit-163"></a>
### Commit 163 {#commit-163}

3a54aab0dd60347b9e21214e4135e94c76645948 · 2025-01-22T23:14:58Z

[feat: add `PlayerEmoteEvent`](https://github.com/EndstoneMC/endstone/commit/3a54aab0dd60347b9e21214e4135e94c76645948)

**Observed change.** Adds public/Python PlayerEmoteEvent with emote ID and a native handler adapter; event is noncancellable. However its visitor test is added to PlayerGameplayEvent<CoordinatorResult>, while PlayerEmoteEvent belongs to the void variant.

**Causal interpretation.** API/stub availability and a named handler do not prove reachable dispatch; the variant membership and selected visitor must match.164 qualifies the native type but does not move it to the correct variant.

**Limits.** Confirmed against full player_events.h and player_gameplay_handler.cpp at200: the void visitor lacks emote and the coordinator variant cannot contain it. Static unreachable-branch finding, no runtime test.

<a id="commit-164"></a>
### Commit 164 {#commit-164}

f4fd8215d016b25974fba0e4040c94136dad66da · 2025-01-22T23:25:15Z

[feat: add `PlayerRespawnEvent`](https://github.com/EndstoneMC/endstone/commit/f4fd8215d016b25974fba0e4040c94136dad66da)

**Observed change.** Adds noncancellable public/Python PlayerRespawnEvent and handler; qualifies global native emote/respawn event names to avoid namespace collision. Both remain tested in the CoordinatorResult visitor, but both native types are void-variant alternatives.

**Causal interpretation.** Correct name qualification fixes one integration concern without fixing dispatch topology. Respawn API currently exposes player only, with no replacement location or cancellation.

**Limits.** The wrong-variant condition remains at200. No observed event firing or end-to-end Python example.

<a id="commit-165"></a>
### Commit 165 {#commit-165}

0a69ee3d9ee15920de8cdaba2c466c016c62d37c · 2025-01-23T15:39:14Z

[feat: add custom `ActorEventCoordinator`](https://github.com/EndstoneMC/endstone/commit/0a69ee3d9ee15920de8cdaba2c466c016c62d37c)

**Observed change.** Adds owned EndstoneActorGameplayHandler decorator with three forwarding overloads and installs it with other coordinators during level setup. Adds friend access and concrete ActorDamageSource include.

**Causal interpretation.** Establishes a single native actor-event interception seam while preserving original handler ownership and default forwarding, preparing166 death and181 removal.

**Limits.** Assumes initialized original handler and correct vtable/layout. Reload lifecycle is not handled until190.

<a id="commit-166"></a>
### Commit 166 {#commit-166}

5b78f74a197b21cbe89393e2bcc4da1ebb28a811 · 2025-01-23T15:53:01Z

[refactor: improve the implementation of `ActorDeathEvent`](https://github.com/EndstoneMC/endstone/commit/5b78f74a197b21cbe89393e2bcc4da1ebb28a811)

**Observed change.** Removes Mob::die hook/symbol and dispatches non-player ActorDeathEvent from ActorKilledEvent in the actor decorator, followed by original forwarding.

**Causal interpretation.** Migration reduces dedicated detours, but type-safe Mob extraction depends on167 and callback ordering/native event timing differ from the removed hook.

**Limits.** No death delivery equivalence test. Player death remains on its separate path until186; this commit calls Mob::tryGetFromEntity before the next commit defines it.

<a id="commit-175"></a>
### Commit 175 {#commit-175}

733f5b3f6d2169a7aa7982d0928a6ec39e82c336 · 2025-01-24T21:24:25Z

[refactor: move initialisation logics into EndstoneServer class](https://github.com/EndstoneMC/endstone/commit/733f5b3f6d2169a7aa7982d0928a6ec39e82c336)

**Observed change.** Moves startup, level, resource-pack and coordinator wiring into EndstoneServer methods. Hooks call originals before server initialization/level setup, changing earlier order. Destructor acquires GIL internally and disables plugins; outer GIL around locator reset is removed. Resource loading temporarily remains duplicated until179.

**Causal interpretation.** Centralizes initialization responsibilities, but hook order and destruction scope are part of behavior. Post-world plugins initially run before handler registration, corrected186.

**Limits.** A local server-destructor GIL guard ends before member destruction, so Python-owning members need their own protection. Context inspection confirms PythonPluginLoader already acquires the GIL in its destructor and explicitly decrefs/releases obj_. Do not infer a demonstrated GIL bug from guard scope alone. No staged-init or teardown test.

<a id="commit-180"></a>
### Commit 180 {#commit-180}

0d35ccfa25dd5673daef14d9e7310583ee5bcdc1 · 2025-01-24T22:18:52Z

[fix: correct the implementation of `Actor::isRemoved`](https://github.com/EndstoneMC/endstone/commit/0d35ccfa25dd5673daef14d9e7310583ee5bcdc1)

**Observed change.** Actor::isRemoved stops treating every non-alive actor as removed and reads removed_; adds const/nonconst Level getters casting ILevel.

**Causal interpretation.** Dead actors can still be valid event subjects; separating death from removal is necessary for death-source/entity lookup consistency.

**Limits.** The new native field and declaration model arrives181. No object-layout validation or death-to-removal sequence test.

<a id="commit-181"></a>
### Commit 181 {#commit-181}

8f5f6c4637aa2f18eb33e6eb847e155c6ab30d8f · 2025-01-24T22:19:27Z

[refactor: `ActorRemoveEvent`](https://github.com/EndstoneMC/endstone/commit/8f5f6c4637aa2f18eb33e6eb847e155c6ab30d8f)

**Observed change.** Moves ActorRemoveEvent from Actor::remove detour to native ActorRemovedEvent and expands Actor fields/interfaces through removed_ and later state; adds ILevel pointer, high precision matrix and const tag-registry access.

**Causal interpretation.** Continues the coordinator migration but changes temporal semantics: native removed notification may arrive after removed_ is set, while default weak extraction excludes removed actors.

**Limits.** No runtime evidence of event timing; potential skipped removals is conditional. Native offset comments and declared layout are not proof of binary compatibility.

<a id="commit-185"></a>
### Commit 185 {#commit-185}

c9a8d9bb14f30fade84ebd20fb558f8d7a1ea209 · 2025-01-24T23:40:58Z

[fix: compilation errors on Linux](https://github.com/EndstoneMC/endstone/commit/c9a8d9bb14f30fade84ebd20fb558f8d7a1ea209)

**Observed change.** Repairs Linux get_name/get_platform mismatch; exposes explicit server lifecycle methods instead of hook friends; null-initializes server pointer and adds double-init/level/repository guards; links core with --no-undefined on Unix.

**Causal interpretation.** Link-time unresolved-symbol failure and explicit initialization state checks surface integration errors earlier, after the prior platform/lifecycle refactors.

**Limits.** No Linux build run. Guards are initialization checks, not thread synchronization or complete partial-startup recovery.

<a id="commit-186"></a>
### Commit 186 {#commit-186}

67e57267cca26f5f3f59ca6f866d706519553e70 · 2025-01-25T00:14:47Z

[refactor: `PlayerDeathEvent`](https://github.com/EndstoneMC/endstone/commit/67e57267cca26f5f3f59ca6f866d706519553e70)

**Observed change.** Moves player death from ServerPlayer::die hook to PlayerDamageEvent when !isAlive; closes forms, dispatches PlayerDeath, honors modified/empty death text, sends DeathInfo and broadcasts. Disables native death sender once during setLevel; registers handlers and packs before PostWorld plugins.

**Causal interpretation.** Consolidates event ownership and fixes175's post-world registration ordering. Removing the old proxy's shouldShowDeathMessages gate changes which layer enforces the gamerule.

**Limits.** Static possible gamerule regression: new explicit broadcast has no equivalent check in this path. Alive damage remains TODO. No repeated-damage/death-order or message regression test.

<a id="commit-187"></a>
### Commit 187 {#commit-187}

0102824f0a0c27f6504989729bb716f9d600a389 · 2025-01-25T00:30:53Z

[refactor: `PlayerJoinEvent`](https://github.com/EndstoneMC/endstone/commit/0102824f0a0c27f6504989729bb716f9d600a389)

**Observed change.** Moves PlayerJoin dispatch from setLocalPlayerAsInitialized hook to PlayerInitialSpawnEvent; retains translated/custom/empty message behavior, permission recalculation and command update.

**Causal interpretation.** The seam changes from a particular initialization call to a native lifecycle event. Old dispatch followed original call; decorator dispatch precedes original handler.

**Limits.** No evidence that native event frequency/order exactly matches removed hook, including respawn/reconnect cases.

<a id="commit-188"></a>
### Commit 188 {#commit-188}

2baf0e951976aac5fd0bab2992645d676d95de62 · 2025-01-25T00:46:03Z

[refactor: `PlayerQuitEvent`](https://github.com/EndstoneMC/endstone/commit/2baf0e951976aac5fd0bab2992645d676d95de62)

**Observed change.** Moves quit handling from disconnect detour to PlayerDisconnectEvent, calls wrapper disconnect then plugin event and mutable broadcast before forwarding original handler. Removes detour/symbol and empty server-level source.

**Causal interpretation.** Unifies player lifecycle at the coordinator seam while preserving user-facing text customization; cleanup/permission/subscription work still relies on wrapper disconnect.

**Limits.** No disconnect ordering/double-notification test; native handler timing differs from detour timing. Removing a symbol entry alone does not prove every obsolete declaration is removed.

<a id="commit-189"></a>
### Commit 189 {#commit-189}

809b3ca3773331027ccadbc0cd6008e3278553e8 · 2025-01-25T01:51:51Z

[refactor: remove getServerThread global function](https://github.com/EndstoneMC/endstone/commit/809b3ca3773331027ccadbc0cd6008e3278553e8)

**Observed change.** isPrimaryThread uses ServerInstance's actual std::thread ID instead of global ID assigned in the thread hook; models expanded server instance fields including flags, mutex, event coordinator and SPSC queue layout shell; removes hook/global symbol.

**Causal interpretation.** Derives thread identity from the owning object and removes mutable global initialization coordination.

**Limits.** Queue is a layout placeholder with padding, not a queue implementation. Server pointer/thread initialization and native layout remain preconditions; no concurrency test.

<a id="commit-190"></a>
### Commit 190 {#commit-190}

12767cf5585bdaf2ff049b4a17acccce30f746f5 · 2025-01-25T14:40:58Z

[fix: resolve a crash caused by compatibility issues with the script API during server reload](https://github.com/EndstoneMC/endstone/commit/12767cf5585bdaf2ff049b4a17acccce30f746f5)

**Observed change.** Author reports Script API reload crash. All six event decorators gain unwrap moving out original unique_ptr. Server unregisters wrappers before reloadData and wraps originals again afterward; destructor also unregisters after disabling plugins.

**Causal interpretation.** Vendor reload can expect its own concrete handler identity, so transparent forwarding is insufficient: ownership must temporarily restore the native handler, then reapply decoration.

**Limits.** static_cast unwrap assumes non-null exact wrapper type; no idempotence/state guard or exception-safe restoration. reloadData merely requests resource reload and loads functions; asynchronous completion is not proved, and existing2.5-second async-task TODO remains. No crash reproduction.
