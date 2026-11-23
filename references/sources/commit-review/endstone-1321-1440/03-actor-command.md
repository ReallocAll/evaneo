<!-- retrieval: {"source_ids":["public:commit:041a0d51cb4d2c85cb8a04f8367f8497efdbdc96","public:commit:16760a97b8916f762143c860c14f5ac34b508f3e","public:commit:1db6f98ba8a17373a6fda133fe4ade53f8fbc0be","public:commit:4f4042c98d3ac68a4ed737d788552a0a1b138614","public:commit:5866e0e50918d65a9ca174a93b17720f8bab3c5f","public:commit:67131ffbec62c4212e8998f0f8ba6a9108608715","public:commit:67cdc208a746f4ed45e01b1fd0d14736856699bb","public:commit:68b7ed63e3f9698e25a27569a42e9733ad08b835","public:commit:7b60b1caf680f176dca1efbbee37474e3642a55a","public:commit:7d8427895c83d0e7d434f664993441ae93c09185","public:commit:862ea2b7d888ef3da07baa1cba0b57372d814832","public:commit:8b36912de145abdba513fc2ce09a94249223b889","public:commit:912a3dfe728f78ffeea2ebd8fca86a3c1e0259ad","public:commit:9f5ce7e9c1076ef4b04b9398f2a5358cc7fdcaac","public:commit:a240d200dd79d7de9cb3d51a39ede4561f6162ac","public:commit:a3f2f28f266227d85eebddd4cff6e269fe288c47","public:commit:a45b088b84fa1d054dc01042b2fb278437b45141","public:commit:a6542c81701f65dee81f0fa9bd392c1c4f388798","public:commit:a78161542cc0cc15f708fd97c274bff391d5d78c","public:commit:ac2bf9b27cd37ac52a514bdd856b825e91ee3e9f","public:commit:b109a602d25a52cb03b5292e7b206aed801a9668","public:commit:b7ac94ffde54d35bebb93ea13c6a632308ae7831","public:commit:d1c2e07cbdbced3d7eeb3b957c5bbe74ed1a330e","public:commit:d848d40369528100b16f79b3481a9de85d9d14e5","public:commit:eb7bb3f032a884e913663dcff586e08d2d238a29","public:commit:f16d16c2b71cb81931647aea2eefcee30cb21416"],"source_type":"public","date":"2024-07-11..2024-07-16","topics":["lifetime","ffi","testing","api","diagnosis","documentation","review","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Actor, command and lifecycle boundaries {#actor-command-and-lifecycle-boundaries}


## Typed wrappers evolve through actual revisions {#typed-wrappers-evolve-through-actual-revisions}

Mob is inserted between Actor and Player, then aligned in Python. Initial EndstoneMob scaffolding is completed later by explicit forwarding through the dual-inheritance adapter and a Player/Mob/generic factory branch. A similar console marker provides Python callbacks a specific ConsoleCommandSender type. PyCommandExecutor reuse through multiple inheritance is tried at 1378, then undone at 1380 while duplicating dispatch. The retained behavior is typed player/console callbacks plus generic fallback; the source does not state why the reuse design was abandoned. Do not infer a fixed preference for or against duplication/inheritance from one intermediate form.

The rotation sequence is similarly concrete: native wrapped angles and body yaw appear first, the public argument order shifts, and 1405 settles public yaw,pitch versus native pitch,yaw. Documentation warns that AI can override rotation. No runtime animation/interpolation evidence is available. Titles and transfer are packet-producing API additions with explicit factory assumptions; their existence is not proof of a client effect or validated timing/address input.

## Mutable events and effective operations are separate {#mutable-events-and-effective-operations-are-separate}

ActorTeleportEvent is explicitly for nonplayers. Its initial hook honors cancellation but ignores mutated destination data, even after Python exposes mutable Location values. 1399 applies destination coordinates with an X/Z copy mistake, repaired at 1407. The complete final hook still ignores destination dimension and angles, and changing from_location is descriptive rather than a source-world mutation. Deleting a rotation TODO at 1407 does not implement rotation. This chain supports checking how event changes are consumed by the underlying operation, not assuming setters imply complete semantics.

Position/Location diagnostic formatting makes dimensions/angles visible, but the same patch removes a public Vector::toString method. API-surface changes are preserved rather than hidden as formatting. DimensionType, by contrast, is an alias for the exact prior specialization and is treated proportionately as naming consolidation.

## Centralized failure policy is not transactional state {#centralized-failure-policy-is-not-transactional-state}

1408 moves lifecycle catches from Python overrides to shared manager/loader boundaries. That broadens consistent logging to native plugins and prevents enable/disable events after a callback throws. Full Plugin::setEnabled context shows the state flag is assigned before the callback, with no rollback. Thus failed enable can leave enabled true, and a later enable attempt is skipped; failed onLoad plugins remain registered for later processing. Logging also calls description getters outside or within error paths, and only std::exception is caught. These are bounded source observations, not a claim of an observed production incident.

All actual commits and changed tests were read; the console mock edits adapt return types, without new behavioral assertions. No builds, clients or plugins were run. Use this dossier for trampoline/type identity, interface hierarchy evolution, event consumption, argument-order contracts and lifecycle error-boundary design. The prior/full native model is context, not authorship of engine behavior.

## Individual commit dispositions {#individual-commit-dispositions}

<a id="commit-1373"></a>
### 1373 · feat: add Mob class and re-parent Player class to Mob class {#commit-1373}

[Commit 041a0d51cb4d](https://github.com/EndstoneMC/endstone/commit/041a0d51cb4d2c85cb8a04f8367f8497efdbdc96) · 2024-07-11T15:24:56Z · Git author/committer: Vincent.

Inserts Mob between Actor and Player in the public hierarchy and introduces an EndstoneMob adapter with dual inheritance. This models shared living-entity behavior, but the initial adapter does not yet forward all Actor abstract methods. The complete generic-mob wrapper/factory dispatch arrives at 1404, so this scaffold should not be credited as finished general Mob support.

Source paths: `include/endstone/actor/mob.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/mob.h`, `include/endstone/detail/player.h`, `include/endstone/player.h`, `src/endstone_core/actor/mob.cpp`, `src/endstone_core/player.cpp`.

<a id="commit-1374"></a>
### 1374 · feat: add python binding for Mob class {#commit-1374}

[Commit d848d4036952](https://github.com/EndstoneMC/endstone/commit/d848d40369528100b16f79b3481a9de85d9d14e5) · 2024-07-11T15:29:36Z · Git author/committer: Vincent.

Mirrors the new Mob hierarchy in Python and the public export/stub surface, making Player inherit Mob there too. This is cross-language type alignment rather than new entity behavior. It remains subject to the native adapter's staged completion.

Source paths: `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/actor.py`, `src/endstone_python/actor.cpp`, `src/endstone_python/endstone_python.cpp`.

<a id="commit-1375"></a>
### 1375 · feat: add Mob::isGliding {#commit-1375}

[Commit a6542c81701f](https://github.com/EndstoneMC/endstone/commit/a6542c81701f65dee81f0fa9bd392c1c4f388798) · 2024-07-11T15:41:34Z · Git author/committer: Vincent.

Adds isGliding through native Mob state, the Endstone adapter and Player forwarding, and introduces the Python property. The adapter temporarily carries a separate borrowed mob reference. This is an actual behavior accessor; the next commit mainly completes annotations/docs rather than creating the binding for the first time.

Source paths: `include/endstone/actor/mob.h`, `include/endstone/detail/actor/mob.h`, `include/endstone/detail/player.h`, `src/endstone_core/actor/mob.cpp`, `src/endstone_core/player.cpp`, `src/endstone_python/actor.cpp`.

<a id="commit-1376"></a>
### 1376 · feat: add python binding for Mob::isGliding {#commit-1376}

[Commit 7b60b1caf680](https://github.com/EndstoneMC/endstone/commit/7b60b1caf680f176dca1efbbee37474e3642a55a) · 2024-07-11T15:43:48Z · Git author/committer: Vincent.

Completes is_gliding stub/documentation and nodiscard annotations, with formatting adjustments. The binding already existed at 1375 despite this commit's wording. No independent engine behavior or test result is added.

Source paths: `include/endstone/actor/mob.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/actor.cpp`.

<a id="commit-1378"></a>
### 1378 · refactor: re-parent PyPlugin to PyCommandExecutor class {#commit-1378}

[Commit eb7bb3f032a8](https://github.com/EndstoneMC/endstone/commit/eb7bb3f032a884e913663dcff586e08d2d238a29) · 2024-07-11T22:13:43Z · Git author/committer: Vincent.

Moves PyCommandExecutor beside the plugin trampoline, uses multiple inheritance to reuse it in PyPlugin, and dispatches player/console senders with more specific Python types. The as_player binding is removed. This is a real reuse experiment, subsequently reversed at 1380; no reason for the reversal is supplied in the commit record.

Source paths: `src/endstone_python/command.cpp`, `src/endstone_python/plugin.cpp`.

<a id="commit-1379"></a>
### 1379 · feat: add ConsoleCommandSender class {#commit-1379}

[Commit 912a3dfe728f](https://github.com/EndstoneMC/endstone/commit/912a3dfe728f78ffeea2ebd8fca86a3c1e0259ad) · 2024-07-11T22:29:02Z · Git author/committer: Vincent.

Adds a public ConsoleCommandSender marker and covariant console/server return types. The concrete adapter explicitly forwards the permission/sender interface across its dual bases while retaining console operator behavior. Test mocks change signature to match, without new behavioral assertions. The additional virtual/type relationships are API/ABI changes, not merely Python annotations.

Source paths: `include/endstone/command/command_sender.h`, `include/endstone/command/console_command_sender.h`, `include/endstone/detail/command/command_adapter.h`, `include/endstone/detail/command/console_command_sender.h`, `include/endstone/detail/command/server_command_sender.h`, `include/endstone/detail/server.h`, `include/endstone/server.h`, `src/endstone_core/command/console_command_sender.cpp`, `src/endstone_core/server.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/plugin.cpp`, `tests/plugin/test_cpp_plugin_loader.cpp`, `tests/scheduler/test_scheduler.cpp`.

<a id="commit-1380"></a>
### 1380 · feat(python): use isinstance to check if a command sender is a Player or ConsoleCommandSender {#commit-1380}

[Commit 8b36912de145](https://github.com/EndstoneMC/endstone/commit/8b36912de145abdba513fc2ce09a94249223b889) · 2024-07-11T23:00:18Z · Git author/committer: Vincent.

Exposes ConsoleCommandSender to Python and removes the stale as_player stub. It also reverses PyPlugin's multiple-inheritance reuse, duplicating typed onCommand dispatch in separate trampolines while retaining a generic-sender fallback. The observed outcome is clearer runtime Python type identity; an anti-inheritance or anti-duplication doctrine is not supported by this short reversal.

Source paths: `include/endstone/command/console_command_sender.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/command.py`, `src/endstone_python/command.cpp`, `src/endstone_python/plugin.cpp`.

<a id="commit-1381"></a>
### 1381 · feat: add Player::sendTitle and Player::resetTitle {#commit-1381}

[Commit a78161542cc0](https://github.com/EndstoneMC/endstone/commit/a78161542cc0cc15f708fd97c274bff391d5d78c) · 2024-07-12T09:38:26Z · Git author/committer: Vincent.

Introduces title/subtitle sending through two SetTitle packets and a reset packet, with default timings 10/70/20. The packet layout and API are new; existing TextPacket casts receive only local syntax cleanup. Initial dynamic casts are replaced at 1383. No timing-range validation or client rendering test accompanies this change.

Source paths: `include/bedrock/network/packet/set_title_packet.h`, `include/endstone/detail/player.h`, `include/endstone/player.h`, `src/endstone_core/player.cpp`.

<a id="commit-1382"></a>
### 1382 · feat: add Player::sendTitle and Player::resetTitle {#commit-1382}

[Commit 68b7ed63e3f9](https://github.com/EndstoneMC/endstone/commit/68b7ed63e3f9698e25a27569a42e9733ad08b835) · 2024-07-12T09:47:30Z · Git author/committer: Vincent.

Makes title operations const and adds Python bindings/stubs with matching defaults. Its subject repeats the prior commit but the patch is different, so both identities are retained. This completes cross-language exposure; it does not independently verify title timing or reset semantics on a client.

Source paths: `include/endstone/detail/player.h`, `include/endstone/player.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_core/player.cpp`, `src/endstone_python/endstone_python.cpp`.

<a id="commit-1383"></a>
### 1383 · fix: replace calls to `std::dynamic_pointer_cast` with `std::static_pointer_cast` {#commit-1383}

[Commit 9f5ce7e9c107](https://github.com/EndstoneMC/endstone/commit/9f5ce7e9c1076ef4b04b9398f2a5358cc7fdcaac) · 2024-07-12T09:58:00Z · Git author/committer: Vincent.

Replaces three SetTitle dynamic_pointer_cast operations with static_pointer_cast. The code now relies directly on the packet factory's ID/type correspondence. Avoid attributing a particular RTTI failure or performance gain: the source shows the assumption change, not a measured explanation or a runtime type check.

Source paths: `src/endstone_core/player.cpp`.

<a id="commit-1385"></a>
### 1385 · feat: add DimensionType {#commit-1385}

[Commit 16760a97b891](https://github.com/EndstoneMC/endstone/commit/16760a97b8916f762143c860c14f5ac34b508f3e) · 2024-07-12T11:24:47Z · Git author/committer: Vincent.

Introduces DimensionType as an alias for the exact existing AutomaticID<Dimension,int> specialization and substitutes it through native interfaces/constants with the required include. The represented type stays identical. This improves naming and consistency without a new dimension-identity format.

Source paths: `include/bedrock/world/actor/actor.h`, `include/bedrock/world/actor/player/player.h`, `include/bedrock/world/level/dimension/dimension.h`, `include/bedrock/world/level/dimension/dimension_interface.h`, `include/bedrock/world/level/dimension/vanilla_dimensions.h`, `include/bedrock/world/level/level_interface.h`.

<a id="commit-1388"></a>
### 1388 · feat: add ActorTeleportEvent {#commit-1388}

[Commit ac2bf9b27cd3](https://github.com/EndstoneMC/endstone/commit/ac2bf9b27cd37ac52a514bdd856b825e91ee3e9f) · 2024-07-12T15:45:12Z · Git author/committer: Vincent.

Replaces an unused setDimension hook with Actor::teleportTo and corresponding platform symbols. A cancellable event is emitted only for nonplayers before calling the original. from/to are mutable Location values, but accepted destination changes are initially ignored; the TODO makes this intermediate limitation explicit. Later commits progressively apply XYZ, not the whole Location.

Source paths: `include/bedrock/world/actor/actor.h`, `include/endstone/event/actor/actor_teleport_event.h`, `python/src/endstone/_internal/symbols.toml`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`.

<a id="commit-1393"></a>
### 1393 · feat: add python bindings for ActorTeleportEvent {#commit-1393}

[Commit 7d8427895c83](https://github.com/EndstoneMC/endstone/commit/7d8427895c83d0e7d434f664993441ae93c09185) · 2024-07-12T20:41:42Z · Git author/committer: Vincent.

Exposes ActorTeleportEvent and mutable from_location/to_location to Python with stubs/docs. At this SHA the hook still ignores destination edits, even though the API accepts them; cancellation is already respected. This records the distinction between binding availability and completed event-effect semantics.

Source paths: `include/endstone/event/actor/actor_teleport_event.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/event.py`, `src/endstone_python/event.cpp`.

<a id="commit-1394"></a>
### 1394 · feat: add __repr__ for Position and Location class {#commit-1394}

[Commit f16d16c2b71c](https://github.com/EndstoneMC/endstone/commit/f16d16c2b71cb81931647aea2eefcee30cb21416) · 2024-07-12T21:14:29Z · Git author/committer: Vincent.

Adds Position/Location string and repr forms with coordinates, angles and a dimension name or None, and normalizes Vector/Socket formatting. It also removes the public C++ Vector::toString method, so it is not cosmetic-only. The representations are diagnostic text; no round-trip/eval guarantee is established.

Source paths: `include/endstone/util/vector.h`, `src/endstone_python/level.cpp`, `src/endstone_python/util.cpp`.

<a id="commit-1395"></a>
### 1395 · chore: update todos {#commit-1395}

[Commit 67cdc208a746](https://github.com/EndstoneMC/endstone/commit/67cdc208a746f4ed45e01b1fd0d14736856699bb) · 2024-07-12T21:18:29Z · Git author/committer: Vincent.

Clarifies the teleport TODO to mention rotation because the hooked original accepts a Vec3 position, and removes a separate actor-factory TODO without implementing new factory behavior. These are comments, not completion of either capability. The final hook still needs to be inspected rather than trusting TODO disappearance later.

Source paths: `src/endstone_runtime/bedrock/world/actor/actor.cpp`.

<a id="commit-1397"></a>
### 1397 · feat: add Player::transfer {#commit-1397}

[Commit d1c2e07cbdbc](https://github.com/EndstoneMC/endstone/commit/d1c2e07cbdbced3d7eeb3b957c5bbe74ed1a330e) · 2024-07-15T15:07:18Z · Git author/committer: Vincent.

Adds TransferPacket and Player::transfer, filling address/port and sending the factory-created packet. The method does not validate the address or port range. This implements a protocol request; it does not prove a successful connection to another server, and no actual transfer was attempted.

Source paths: `include/bedrock/network/packet/transfer_packet.h`, `include/endstone/detail/player.h`, `include/endstone/player.h`, `src/endstone_core/player.cpp`.

<a id="commit-1398"></a>
### 1398 · feat: add python binding for Player::transfer {#commit-1398}

[Commit 5866e0e50918](https://github.com/EndstoneMC/endstone/commit/5866e0e50918d65a9ca174a93b17720f8bab3c5f) · 2024-07-15T19:37:04Z · Git author/committer: Vincent.

Exposes transfer to Python with a default port of 19132 and updates the stub. The C++ interface requires a port explicitly. This deliberate language-surface default is separate from the packet implementation and does not add destination validation.

Source paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/endstone_python.cpp`.

<a id="commit-1399"></a>
### 1399 · feat: update Actor::teleportTo {#commit-1399}

[Commit 862ea2b7d888](https://github.com/EndstoneMC/endstone/commit/862ea2b7d888ef3da07baa1cba0b57372d814832) · 2024-07-16T15:29:02Z · Git author/committer: Vincent.

Begins applying the teleport event's accepted destination but mistakenly constructs position as Z,Y,Z. Rotation remains TODO and player calls retain their original position path. The subsequent 1407 fix is a direct causal correction, providing a concrete counterexample to equating event setter exposure with correct behavior.

Source paths: `src/endstone_runtime/bedrock/world/actor/actor.cpp`.

<a id="commit-1400"></a>
### 1400 · feat: add Actor::hasType {#commit-1400}

[Commit 1db6f98ba8a1](https://github.com/EndstoneMC/endstone/commit/1db6f98ba8a17373a6fda133fe4ade53f8fbc0be) · 2024-07-16T17:28:56Z · Git author/committer: Vincent.

Models ActorTypeComponent and implements hasType as a nonzero bitmask intersection from a persistent component. This supplies generic Mob classification for 1404; it is not exact enum equality and has no null guard. The declaration describes expected engine state, not a newly validated universal classification rule.

Source paths: `include/bedrock/entity/components/actor_type_component.h`, `include/bedrock/world/actor/actor.h`, `include/bedrock/world/actor/actor_type.h`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`.

<a id="commit-1401"></a>
### 1401 · feat: add Mob::setYBodyRotation {#commit-1401}

[Commit a45b088b84fa](https://github.com/EndstoneMC/endstone/commit/a45b088b84fa1d054dc01042b2fb278437b45141) · 2024-07-16T17:57:53Z · Git author/committer: Vincent.

Adds the native body-rotation component with current/previous float fields and a Mob setter for current body yaw. Previous yaw is not updated by this setter. This is the narrow native mechanism later used by the public rotation adapter.

Source paths: `include/bedrock/entity/components/mob_body_rotation_component.h`, `include/bedrock/world/actor/mob.h`, `src/endstone_runtime/bedrock/world/actor/mob.cpp`.

<a id="commit-1402"></a>
### 1402 · feat: add Actor::setRotationWrapped {#commit-1402}

[Commit 67131ffbec62](https://github.com/EndstoneMC/endstone/commit/67131ffbec62c4212e8998f0f8ba6a9108608715) · 2024-07-16T18:35:12Z · Git author/committer: Vincent.

Introduces degree normalization to [-180,180) and a rotation utility that wraps incoming current angles and existing previous angles independently. It does not snapshot the old current rotation into previous. The Actor wrapper writes the built-in rotation component; interpolation behavior is not measured or inferred beyond those assignments.

Source paths: `include/bedrock/core/math/math.h`, `include/bedrock/entity/utilities/rotation_utility.h`, `include/bedrock/world/actor/actor.h`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`.

<a id="commit-1403"></a>
### 1403 · feat: add Actor::setRotation {#commit-1403}

[Commit b109a602d25a](https://github.com/EndstoneMC/endstone/commit/b109a602d25a52cb03b5292e7b206aed801a9668) · 2024-07-16T19:39:27Z · Git author/committer: Vincent.

Adds Actor::setRotation(yaw,pitch), warning that AI may override it, and forwards the two values into a native Vec2. The ordering is still under revision: 1404 temporarily changes the public order and 1405 restores yaw/pitch while explicitly arranging native pitch/yaw storage.

Source paths: `include/endstone/actor/actor.h`, `include/endstone/detail/actor/actor.h`, `src/endstone_core/actor/actor.cpp`.

<a id="commit-1404"></a>
### 1404 · feat: implement EndstoneMob {#commit-1404}

[Commit a3f2f28f2662](https://github.com/EndstoneMC/endstone/commit/a3f2f28f266227d85eebddd4cff6e269fe288c47) · 2024-07-16T19:52:34Z · Git author/committer: Vincent.

Completes EndstoneMob's explicit sender/permission/Actor forwarding across its dual bases and routes Player through it. The native factory now selects Player first, then the Mob bitmask, then generic Actor. Rotation passes through the Mob wrapper and updates body yaw; argument-order inconsistencies introduced in this step are repaired at 1405.

Source paths: `include/endstone/actor/actor.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/mob.h`, `include/endstone/detail/player.h`, `src/endstone_core/actor/actor.cpp`, `src/endstone_core/actor/mob.cpp`, `src/endstone_core/player.cpp`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`.

<a id="commit-1405"></a>
### 1405 · feat: add python binding for Actor::setRotation {#commit-1405}

[Commit 4f4042c98d3a](https://github.com/EndstoneMC/endstone/commit/4f4042c98d3ac68a4ed737d788552a0a1b138614) · 2024-07-16T20:00:49Z · Git author/committer: Vincent.

Restores the public yaw,pitch order consistently, sends native Vec2 as pitch,yaw, and retains Mob body-yaw updates. Python receives set_rotation and the actor dimension property. This completes the observed ordering revision chain, without proving that AI, interpolation or a mutable teleport Location will use these setters automatically.

Source paths: `include/endstone/actor/actor.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/mob.h`, `include/endstone/detail/player.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_core/actor/actor.cpp`, `src/endstone_core/actor/mob.cpp`, `src/endstone_core/player.cpp`, `src/endstone_python/actor.cpp`.

<a id="commit-1407"></a>
### 1407 · fix: Actor::teleportTo {#commit-1407}

[Commit b7ac94ffde54](https://github.com/EndstoneMC/endstone/commit/b7ac94ffde54d35bebb93ea13c6a632308ae7831) · 2024-07-16T20:49:43Z · Git author/committer: Vincent.

Corrects the teleport destination to X,Y,Z. It removes the rotation TODO but does not invoke rotation or dimension changes; the full final hook confirms only cancellation and destination coordinates are applied for nonplayers. Source behavior therefore remains narrower than mutating every field of the exposed Location value.

Source paths: `src/endstone_runtime/bedrock/world/actor/actor.cpp`.

<a id="commit-1408"></a>
### 1408 · refactor: move exception handling for plugin loading to PluginManager {#commit-1408}

[Commit a240d200dd79](https://github.com/EndstoneMC/endstone/commit/a240d200dd79d7de9cb3d51a39ede4561f6162ac) · 2024-07-16T21:05:02Z · Git author/committer: Vincent.

Moves lifecycle exception handling out of Python-only overrides into PluginManager onLoad and PluginLoader enable/disable, covering native plugins too. Errors skip enable/disable events, but Plugin::setEnabled writes the flag before invoking callbacks and is not rolled back. Failed onLoad plugins remain registered. getDescription failures and non-std exceptions are not universally caught. This centralizes policy without making lifecycle transitions transactional.

Source paths: `include/endstone/plugin/plugin_loader.h`, `src/endstone_core/plugin/plugin_manager.cpp`, `src/endstone_python/plugin.cpp`.
