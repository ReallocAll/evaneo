<!-- retrieval: {"source_ids":["public:commit:0450add38306d51cae3a80a5c4f2940bb84c1f9b","public:commit:23ca36d51fd44b1cd3e96b2e4633b3f071cd0634","public:commit:5bebb3731039fee0bed4b84648b209ea92fa2035","public:commit:7f5c96c9ed24b6c7e11d1f57bdf953fad4d5aa0c","public:commit:d5009b564b7f40edc8d17c832f3fcc718205ae90","public:commit:e623dc158bd883387f52d0cacfb5ab2b5cf7aa3e","public:commit:e8bc0b7bfffb6ea5a7dd393f3910bc6ec658c356","public:commit:ea278f67a98bdf09737b29c3140dc4350dd09b4e","public:commit:f0bfef3f8c06f8230b4202755ffb30cc76aec8df"],"source_type":"public","date":"2025-01-05..2025-01-11","topics":["lifetime","ffi","testing","api","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Event decorators and public object lifetime {#event-decorators-and-public-object-lifetime}

## Cancellation contract across languages {#cancellation-contract-across-languages}

28 replaces Event's generic cancellation API with ICancellable and a Cancellable<Base> mixin. Despite the subject's CRTP wording, the template parameter is the event base rather than the derived self type.29 mirrors this in Python, deprecates the old cancelled property, adds cancel(), removes generic is_cancellable and exports server/weather bases. These are public API changes, not just internal organization.

The mixin's private isCancellable returns false through 100. EventHandler only honors ignore_cancelled when that virtual reports true, so directly checking e.isCancelled in a native handler and skipping already-cancelled plugin listeners have different outcomes. The wrapper cancellation checks can work while listener filtering remains broken. The successor worker reports115/116 repair; those commits are outside this unit and receive no credit here. This distinction is critical when using the history to discuss cancellation semantics.

## Owning forwarding handlers replace selected detours {#owning-forwarding-handlers-replace-selected-detours}

92 wraps the existing scripting handler in an Endstone-owned decorator, installs it at setLevel and removes the ScriptingEventCoordinator detour.93 does the same for weather,94 adds a block-handler forwarding shell,95 implements block break/place decisions. Original unique_ptr ownership moves into the wrapper and other events continue through the original virtual interface. This avoids some native symbol detours and concentrates event adaptation in core. It does not remove all hooks, and original-handler presence, installation order, repeated setLevel wrapping and native vtable layout remain assumptions.

For weather, cancellation restores only the relevant proposed rain/lightning bool and still forwards the native event. For block break/place, cancellation returns BypassListeners plus CoordinatorResult::Cancel and does not call the original handler. Entity lookup uses a weak entity storage and returns pass-through for absent or non-player entities. Block lookup errors are logged and fail open. The two policies should not be flattened into a generic 'cancel means stop all processing' principle.

92 removes an older null scripting-handler guard. The decorator calls handle_->handleEvent without a new null test, assuming the original exists by registration time. This is a concrete lifecycle review point; no null-triggering runtime failure is asserted. Native ValueOrRef/variant and subscription structures are updated in93, but the generic EventHandlerDispatcher still ends as an empty shell. Interface reconstruction is not blanket ABI validation.

## Shared wrappers and explosions {#shared-wrappers-and-explosions}

98 moves Block/Dimension/BlockState return values and event fields from unique/raw references to shared_ptr and makes Python's Block holder agree. This extends wrapper lifetime. It does not own the underlying BlockSource or dimension; EndstoneBlock::checkState dereferences that source, checks world height, loaded chunk and tick freshness. Every at() still creates a new wrapper, despite the API prose saying only one Block may exist per location. Shared ownership and identity canonicalization are separate contracts.

98 also introduces explosion dispatch before 99 supplies the ActorExplodeEvent header/API/bindings, so98 alone has a missing include. The handler builds shared blocks from native coordinates, emits only when the source actor is found, supports cancellation and writes edited coordinates back into the native set. An invalid block lookup skips the API event and lets native handling continue. Sourceless explosions remain a BlockExplodeEvent TODO. A substituted block from another dimension is reduced to coordinates without dimension validation. The event location is actor.getLocation rather than an independently captured explosion point, while its documentation says the actor no longer exists; the inspected implementation does not fully support that wording.

Python's block_list getter returns a vector value converted to a Python list; the setter swaps an entire vector. Reassigning the property propagates edits, while in-place modification of a returned Python list is not demonstrated to mutate the native event.99 removes the redundant knockback actor binding, and100 centralizes polymorphic type hooks so Permissible→CommandSender→Actor→Player can return appropriate registered types. Mob detection is absent at 100 and is reported in successor 101. No pybind runtime test or actor lifetime guarantee was established.

## Review use {#review-use}

Use this chain to ask precise questions during native event adaptation: who owns the original handler, which events forward, what cancellation means at each layer, whether wrapper lifetime owns native resources, which Python operations actually update C++ state, and which native offsets/vtables are assumed. Do not infer an unconditional preference against hooks or present a staged intermediate tree as a finished design.


<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}



<a id="commit-028"></a>
### 028. refactor: introduce CRTP template Cancellable for cleaner cancellable events {#commit-028}

Commit: [ea278f67a98bdf09737b29c3140dc4350dd09b4e](https://github.com/EndstoneMC/endstone/commit/ea278f67a98bdf09737b29c3140dc4350dd09b4e) · committed 2025-01-05T00:57:29Z · author Vincent.

Actual parent: `d5b996e9725217f1c91f48a62e9e61fcd4021fe1`. Full message and parent-relative patch: local source.

Moves cancellation capability into ICancellable plus Cancellable<EventType>, removes public cancellation from generic Event, and migrates event subclasses/constructors. Despite the CRTP subject this is a base-type mixin rather than self-type CRTP. Initial mixin isCancellable returns false, so EventHandler ignore-cancelled gating cannot work as intended;115 later repairs the design. Ping event also gets initialized scalar fields and changes formerly false cancellation capability. ActorUniqueID static invalid definition and explicit construction are repaired.

Changed-file coverage: 24 paths. `include/bedrock/world/actor/actor_unique_id.h`; `include/endstone/event/actor/actor_death_event.h`; `include/endstone/event/actor/actor_knockback_event.h`; `include/endstone/event/actor/actor_remove_event.h`; `include/endstone/event/actor/actor_spawn_event.h`; `include/endstone/event/actor/actor_teleport_event.h`; `include/endstone/event/block/block_break_event.h`; `include/endstone/event/block/block_place_event.h`; `include/endstone/event/cancellable.h`; `include/endstone/event/event.h`; `include/endstone/event/event_handler.h`; `include/endstone/event/player/player_chat_event.h`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-029"></a>
### 029. refactor: update Python bindings to use `Cancellable` as the base class for all cancellable events {#commit-029}

Commit: [d5009b564b7f40edc8d17c832f3fcc718205ae90](https://github.com/EndstoneMC/endstone/commit/d5009b564b7f40edc8d17c832f3fcc718205ae90) · committed 2025-01-05T01:14:03Z · author Vincent.

Actual parent: `ea278f67a98bdf09737b29c3140dc4350dd09b4e`. Full message and parent-relative patch: local source.

Makes Python cancellation an interface base, preserves deprecated cancelled with FutureWarning, adds cancel(), and exports ServerEvent/WeatherEvent bases while adjusting all stubs and concrete binding bases. Event.is_cancellable disappears. These are visible API compatibility changes beyond internal refactoring; ScriptMessageEvent remains uncancellable at this point.

Changed-file coverage: 4 paths. `include/endstone/event/server/server_event.h`; `python/src/endstone/_internal/endstone_python.pyi`; `python/src/endstone/event.py`; `src/endstone_python/event.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-092"></a>
### 092. refactor: use a cleaner way to add hook for ScriptMessageEvent {#commit-092}

Commit: [23ca36d51fd44b1cd3e96b2e4633b3f071cd0634](https://github.com/EndstoneMC/endstone/commit/23ca36d51fd44b1cd3e96b2e4633b3f071cd0634) · committed 2025-01-10T00:19:25Z · author Vincent.

Actual parent: `bb74bbbd2ee14538289377e517152c58cd461e09`. Full message and parent-relative patch: local source.

Replaces ScriptMessageEvent detour with owning ScriptingEventHandler decorator installed at setLevel, removes target symbols. Forwards mutable events and const variant after emitting API event from actor-or-console sender. Original unique_ptr moved into wrapper; prior null-handler safety guard removed and forwarding assumes nonnull. Declares GameplayHandler destructor default; missing handler teardown/reinstallation guard remains boundary. PR 122 base equals this commit but proposed third-party adapter is separate/unmerged, not this implementation.

Changed-file coverage: 9 paths. `src/bedrock/gameplayhandlers/gameplay_handler.h`; `src/bedrock/symbol_generator/symbols.toml`; `src/bedrock/world/events/scripting_event_coordinator.h`; `src/endstone/core/CMakeLists.txt`; `src/endstone/runtime/bedrock_hooks/scripting_event_coordinator.cpp → src/endstone/core/event/handlers/scripting_event_handler.cpp`; `src/bedrock/world/events/scripting_event_coordinator.h → src/endstone/core/event/handlers/scripting_event_handler.h`; `src/endstone/core/server.cpp`; `src/endstone/core/server.h`; `src/endstone/runtime/bedrock_hooks/scripting_event_coordinator.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-093"></a>
### 093. refactor: use a better way to implement weather events {#commit-093}

Commit: [e623dc158bd883387f52d0cacfb5ab2b5cf7aa3e](https://github.com/EndstoneMC/endstone/commit/e623dc158bd883387f52d0cacfb5ab2b5cf7aa3e) · committed 2025-01-11T18:12:30Z · author Vincent.

Actual parent: `7b64486fddef2d1c78809d2b27d09203dfc9c4ac`. Full message and parent-relative patch: local source.

Weather path moves from ScriptLevelGameplayHandler detour to owning LevelGameplayHandler decorator; cancelled rain/thunder individually restore old bool then native handler still runs. Event mutable storage/alias corrected, native subscriptions modeled as four16-byte weak_ptr subscriptions and listener vtable declarations expanded. Adds template dispatcher reconstruction but final EventHandlerDispatcher remains empty; do not claim complete dispatch ABI. Old scripted handler symbols/files removed and core registration renamed. Original handles assumed nonnull.

Changed-file coverage: 22 paths. `src/bedrock/scripting/event_handlers/script_event_handler.h → src/bedrock/core/utility/pub_sub/subscription.h`; `src/bedrock/core/utility/pub_sub/subscription_context.h`; `src/bedrock/gameplayhandlers/event_handler_dispatcher.h`; `src/bedrock/gameplayhandlers/level_gameplay_handler.h`; `src/bedrock/gameplayhandlers/scripting_event_handler.h`; `src/bedrock/scripting/event_handlers/script_level_gameplay_handler.h`; `src/bedrock/symbol_generator/symbols.toml`; `src/bedrock/world/events/event_variant.h`; `src/bedrock/world/events/level_event_coordinator.h`; `src/bedrock/world/events/level_event_listener.h`; `src/bedrock/world/events/level_events.h`; `src/endstone/core/CMakeLists.txt`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.

The immediate parent is Mustafa’s documentation contribution; see [separate context attribution](06-context-attribution.md#context-7b64486).


<a id="commit-094"></a>
### 094. feat: add block event handler {#commit-094}

Commit: [e8bc0b7bfffb6ea5a7dd393f3910bc6ec658c356](https://github.com/EndstoneMC/endstone/commit/e8bc0b7bfffb6ea5a7dd393f3910bc6ec658c356) · committed 2025-01-11T18:34:02Z · author Vincent.

Actual parent: `e623dc158bd883387f52d0cacfb5ab2b5cf7aa3e`. Full message and parent-relative patch: local source.

Adds BlockGameplayHandler decorator forwarding all four overload families and installs alongside weather/script handlers. Models CraftUISetResultNameEvent and optional<string> variant, includes required native layouts. No block API events yet; forwarding shell enables95. Ownership is unique_ptr wrapper of previous handler, not native function detour.

Changed-file coverage: 9 paths. `src/bedrock/gameplayhandlers/block_gameplay_handler.h`; `src/bedrock/world/events/block_event_coordinator.h`; `src/bedrock/world/events/block_events.h`; `src/endstone/core/CMakeLists.txt`; `src/endstone/core/event/handlers/block_gameplay_handler.cpp`; `src/endstone/core/event/handlers/level_gameplay_handler.h → src/endstone/core/event/handlers/block_gameplay_handler.h`; `src/endstone/core/event/handlers/level_gameplay_handler.h`; `src/endstone/core/event/handlers/scripting_event_handler.h`; `src/endstone/core/server.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-095"></a>
### 095. refactor: implement BlockBreakEvent and BlockPlaceEvent using a hookless approach {#commit-095}

Commit: [5bebb3731039fee0bed4b84648b209ea92fa2035](https://github.com/EndstoneMC/endstone/commit/5bebb3731039fee0bed4b84648b209ea92fa2035) · committed 2025-01-11T19:11:14Z · author Vincent.

Actual parent: `e8bc0b7bfffb6ea5a7dd393f3910bc6ec658c356`. Full message and parent-relative patch: local source.

Implements block break/place via coordinator variants: obtains player from weak entity stack reference, fails open for missing/nonplayer entity, logs lookup errors and continues. API cancellation returns BypassListeners+Cancel without original handler; accepted events forward. Removes GameMode::destroyBlock and Item placement detours/symbol entries. Models place-event fields/offsets. Explosion handler still trivial true. BlockState accepts const native block then const_cast stores it; lifetime not extended.

Changed-file coverage: 10 paths. `src/bedrock/symbol_generator/symbols.toml`; `src/bedrock/world/events/block_events.h`; `src/bedrock/world/gamemode/game_mode.h`; `src/bedrock/world/item/item.h`; `src/endstone/core/block/block_state.cpp`; `src/endstone/core/block/block_state.h`; `src/endstone/core/event/handlers/block_gameplay_handler.cpp`; `src/endstone/core/event/handlers/block_gameplay_handler.h`; `src/endstone/runtime/bedrock_hooks/game_mode.cpp`; `src/endstone/runtime/bedrock_hooks/item.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-098"></a>
### 098. feat: use std::shared_ptr as the holder for `Block` objects {#commit-098}

Commit: [0450add38306d51cae3a80a5c4f2940bb84c1f9b](https://github.com/EndstoneMC/endstone/commit/0450add38306d51cae3a80a5c4f2940bb84c1f9b) · committed 2025-01-11T22:17:26Z · author Vincent.

Actual parent: `16a1a1856a1ab6de37aeff59fcf968849953afdd`. Full message and parent-relative patch: local source.

Public ABI/lifetime change: Block inherits enable_shared_from_this; Dimension/Block relative and BlockState getters return Result<shared_ptr<Block>>, events own shared block/state/item holders; Python Block holder follows. Each at() still allocates new wrapper, so API comment single-object-per-location is not enforced. Explosion handling introduced before 99 header: builds block list, emits actor event, maps accepted edits to position set, cancellation propagates; invalid block lookup fails open, sourceless explosion TODO, cross-dimension block edits not checked. Shared wrapper does not own BlockSource/dimension. Intermediate commit references nonexistent ActorExplodeEvent header until 99.

Changed-file coverage: 17 paths. `include/endstone/block/block.h`; `include/endstone/block/block_state.h`; `include/endstone/endstone.hpp`; `include/endstone/event/block/block_break_event.h`; `include/endstone/event/block/block_event.h`; `include/endstone/event/block/block_place_event.h`; `include/endstone/event/player/player_interact_event.h`; `include/endstone/level/dimension.h`; `src/endstone/core/block/block.cpp`; `src/endstone/core/block/block.h`; `src/endstone/core/block/block_state.cpp`; `src/endstone/core/block/block_state.h`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-099"></a>
### 099. feat(event): add ActorExplodeEvent, called when an actor (e.g. Creeper, TNT) explodes {#commit-099}

Commit: [7f5c96c9ed24b6c7e11d1f57bdf953fad4d5aa0c](https://github.com/EndstoneMC/endstone/commit/7f5c96c9ed24b6c7e11d1f57bdf953fad4d5aa0c) · committed 2025-01-11T22:27:15Z · author Vincent.

Actual parent: `0450add38306d51cae3a80a5c4f2940bb84c1f9b`. Full message and parent-relative patch: local source.

Adds ActorExplodeEvent C++ API with owned Location and shared block vector, Python export/stub/property setter swaps list; C++ getBlockList mutable reference versus Python getter returns copy list (reassignment propagates, in-place Python list mutation not established). Documentation says source actor gone while implementation only emits if source found and uses actor current location, a contract limitation. Removes redundant ActorKnockbackEvent actor override in binding/stub; next100 polymorphic support generalizes return types.

Changed-file coverage: 4 paths. `endstone/_internal/endstone_python.pyi`; `endstone/event.py`; `include/endstone/event/actor/actor_explode_event.h`; `src/endstone/python/event.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-100"></a>
### 100. feat: add pybind11 polymorphic type hooks for actor types {#commit-100}

Commit: [f0bfef3f8c06f8230b4202755ffb30cc76aec8df](https://github.com/EndstoneMC/endstone/commit/f0bfef3f8c06f8230b4202755ffb30cc76aec8df) · committed 2025-01-11T22:52:07Z · author Vincent.

Actual parent: `7f5c96c9ed24b6c7e11d1f57bdf953fad4d5aa0c`. Full message and parent-relative patch: local source.

Moves CommandSender pybind polymorphic hook into shared poly.h used by command/event bindings; adds Player, Actor and Permissible dispatch through as* methods. Null propagates; fallback type forced to declared API type. Actor dispatch only detects Player, not Mob at this boundary (successor 101 adds it). Header depends on umbrella-before-include order. No binding/runtime tests changed.

Changed-file coverage: 3 paths. `src/endstone/python/command.cpp`; `src/endstone/python/event.cpp`; `src/endstone/python/poly.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.
