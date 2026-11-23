<!-- retrieval: {"source_ids":["public:commit:00af57fb415d7887f188a2290eb82e49192295af","public:commit:0703b3080d3aac7aad0de31ad6a712293254a981","public:commit:21fb1662a06170ab7b81f63bed77a2372b450e12","public:commit:283557607c4064a3e1006ec59cb0109693181054","public:commit:343680ec8f840fe7b150b6b8668b22302030abae","public:commit:38456a48ee9b2f8fcbec0788cecb6a9fa0e1a281","public:commit:3b82f8a4fa9e835a1ed6e41e2d538ae8c1f1836e","public:commit:3cfbb21ec522d78eb338c9c4f68de9cae2a05fc8","public:commit:427ccda13c783bfe0f97a2254b8f93fc80e6dc0b","public:commit:6b8173675ad11b2cbcf1c3ecc4b4163681d72c07","public:commit:74d654a8b72ced46915002083026a547b406a37f","public:commit:74ddfc9d8c7621fd17ef2f62a6d26fa1f746101f","public:commit:948061766b90049da70bd71d2defdda7e4cd71c0","public:commit:9ef876e601590c34d342c7a6b6948ccd1474d2db","public:commit:a35832b5e6a7fff325c97479bf033633b7ea5725","public:commit:d3ea43469005580d35b208746d286193ef249971","public:commit:ea13dae11a6edc42cd9cff344d294408f2bea60d","public:commit:ebdb9e4e7b85355443019d9c937ad83c697ef7a4","public:commit:fc60ae07527929bef7437e378f6985a3e7408b19"],"source_type":"public","date":"2024-05-02..2024-05-04","topics":["lifetime","concurrency","ffi","testing","api","review","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Level identity, player indexing and borrowed Python returns {#level-identity-player-indexing-and-borrowed-python-returns}

## The problem changes before the API settles {#the-problem-changes-before-the-api-settles}

The prior history modeled a wrapper per native dimension and later selected Overworld for weather. [845](#commit-845) changes the unit of identity: one EndstoneLevel represents one native Level, loads its dimensions, and filters actors by level identity. This removes dimension-derived level names and the old direct dimension accessor. The new Dimension class is still mostly a type scaffold. The useful architectural observation is a concrete correction of the abstraction boundary, not a claim that the final hierarchy was evident from the beginning.

Public interface placement changes in844 affect C++ includes and Python imports. A byte-identical moved header still creates a consumer migration when the supported path changes. Later [spatial ownership work](03-spatial-ownership.md) makes Level handles shared and position references weak, but that is a separate dated transition, not part of844's relocation.

## Enumeration follows wrapper lifecycle after an ABI correction {#enumeration-follows-wrapper-lifecycle-after-an-abi-correction}

846 first reads the native player list and scans it for UUID lookup.852 corrects the assumed first field from a Player reference to ActorUniqueID and replaces that strategy with a server registry maintained by EndstonePlayer construction/destruction. The native-list route and wrapper-index route are observed alternatives; there is no review record here proving why one was preferred beyond the explicit fix and changed implementation.

The resulting map owns neither the Player nor the underlying native object. Visibility begins when the wrapper is constructed and ends when destroyed. That is not identical by definition to successful login, even though846's title says logged-in players. Constructor registration also assumes unique UUIDs: emplace can decline a duplicate and destruction erases by key. No synchronization or duplicate-login scenario is newly tested. These limits keep the useful design explanation honest without requiring an unbounded concurrency audit.

Kick in872 stores a raw network-handler pointer before login listeners run and allows cancellation to request disconnection. It still invokes original loadNewPlayer after the cancellation branch. Therefore 'cancelled login' here means a disconnection request in that control flow, not a demonstrated short-circuit of native loading. The final init method changes again in959/960 to prepare command origin state; see the command dossier.

## Python surfaces have their own evolution {#python-surfaces-have-their-own-evolution}

SocketAddress replaces string-plus-port access and groups related address data into a value type. The Python repr spelling and changelog method name are corrected separately in858. No network address parser, port range check or special IPv6 formatting is implemented. Value-initialization changes narrowly in870; no general default-construction policy is inferred.

asPlayer is a nullable virtual query.874 initially binds it as a property,875 makes it a method, and876 explicitly selects borrowed-reference return policy. This is strong local evidence that pointer ownership at the C++/Python boundary matters. It does not establish universal lifetime safety: reference policy avoids adoption but does not keep the host player alive. The stub's non-null declaration is also narrower than the base implementation permits. ServerEvent's C++ hierarchy and Python's still-direct Event bases provide another example where language surfaces are not identical.

Ping is exposed as a duration, converted to timedelta rather than an ambiguous number. Command advertisement is refreshed after join listeners and permission recalculation, so plugins can influence initial visibility. No added automatic refresh for every later permission attachment is visible in877/878. These sequencing details are more useful than a broad slogan about 'clean APIs.'

## Evidence and use {#evidence-and-use}

Whole parent-relative diffs and final server/player/level/binding context were read. Mock signature updates are compile-facing source adaptations, not behavioral tests. No native server or Python binding was executed. Git attribution is Vincent for these changes; no independent collaborator endorsement is inferred. Apply this family to wrapper identity, native-container uncertainty, registry lifecycle, borrowed returns, binding registration order, and API migration checks. Retrieve the specific revision rather than applying one end-state ownership rule to the whole chain.

## Per-commit source dispositions {#per-commit-source-dispositions}

<a id="commit-844"></a>
### 844 · refactor: move Level class {#commit-844}

[Full commit a35832b5e6a7fff325c97479bf033633b7ea5725](https://github.com/EndstoneMC/endstone/commit/a35832b5e6a7fff325c97479bf033633b7ea5725) · 2024-05-02T13:36:14Z · parent `4a5ff0f3f4e67e88deb719df9fa6b938270b9780` · api_refactor.

Relocates the public Level header into endstone/level/level.h and updates consumers, while moving Python registration into its own translation unit and introducing endstone.level rather than retaining Level at the root package. The header relocation is exact-content reuse where hashes match, but the include/import surface changes are externally observable and cannot be dismissed as a file move. Documentation/navigation are changed with the API.

Changed paths: `docs/reference/python/index.md`, `docs/reference/python/level.md`, `include/endstone/detail/level/level.h`, `include/endstone/detail/server.h`, `include/endstone/event/weather/weather_event.h`, `include/endstone/level/level.h`, `include/endstone/server.h`, `mkdocs.yml`, `python/src/endstone/__init__.py`, `python/src/endstone/level.py`, `src/endstone_core/level/level.cpp`, `src/endstone_core/server.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/level.cpp`, `src/endstone_runtime/bedrock/world/level/event/event_coordinator.cpp`, `src/endstone_runtime/bedrock/world/level/event/gameplay_handler.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-845"></a>
### 845 · refactor: Level now manages multiple Dimensions {#commit-845}

[Full commit 0703b3080d3aac7aad0de31ad6a712293254a981](https://github.com/EndstoneMC/endstone/commit/0703b3080d3aac7aad0de31ad6a712293254a981) · 2024-05-02T13:48:13Z · parent `a35832b5e6a7fff325c97479bf033633b7ea5725` · architecture_revision.

Replaces three EndstoneLevel wrappers per native level, previously named by dimension, with one wrapper that loads the three native dimensions. Actor membership now compares the native level rather than dimension, the level name becomes the native level ID alone, and the old getDimension API disappears. Dimension changes from enum to a class with a nested Type, but this commit does not finish a usable runtime Dimension wrapper. Weather no longer selects an Overworld wrapper. This revises ordinals696/768, rather than demonstrating an invariant design maintained from inception.

Changed paths: `CHANGELOG.md`, `include/endstone/detail/level/level.h`, `include/endstone/level/dimension.h`, `include/endstone/level/level.h`, `src/endstone_core/level/level.cpp`, `src/endstone_runtime/bedrock/world/level/event/event_coordinator.cpp`, `src/endstone_runtime/bedrock/world/level/event/gameplay_handler.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-846"></a>
### 846 · feat: add `Server::getOnlinePlayers` for getting all logged in players {#commit-846}

[Full commit 283557607c4064a3e1006ec59cb0109693181054](https://github.com/EndstoneMC/endstone/commit/283557607c4064a3e1006ec59cb0109693181054) · 2024-05-02T14:13:34Z · parent `0703b3080d3aac7aad0de31ad6a712293254a981` · feature_then_corrected.

Introduces online-player enumeration through the native player list and changes UUID lookup from a native lookup to scanning the returned wrappers. Its reconstructed PlayerListEntry starts with a Player reference, an ABI assumption corrected in852 to ActorUniqueID. Mock interface updates establish compile-facing accommodation, not a behavioral enumeration test. The title promises logged-in players; the later constructor/destructor registry has a different observable lifetime boundary.

Changed paths: `include/bedrock/forward.h`, `include/bedrock/server/player_list_entry.h`, `include/bedrock/world/level/level_interface.h`, `include/endstone/detail/server.h`, `include/endstone/server.h`, `src/endstone_core/server.cpp`, `tests/plugin/test_cpp_plugin_loader.cpp`, `tests/scheduler/test_scheduler.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-848"></a>
### 848 · feat: add python bindings for Server::getOnlinePlayers {#commit-848}

[Full commit d3ea43469005580d35b208746d286193ef249971](https://github.com/EndstoneMC/endstone/commit/d3ea43469005580d35b208746d286193ef249971) · 2024-05-02T14:23:57Z · parent `e774552e92435267471bca720b588f07317ad7e8` · binding.

Adds Server.online_players to Python and the stub with reference_internal return policy. It exposes846's current enumeration implementation, including its then-incorrect native layout; Python registration is not an independent validation of the host list.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/endstone_python.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-849"></a>
### 849 · feat: add base class ServerEvent {#commit-849}

[Full commit 74d654a8b72ced46915002083026a547b406a37f](https://github.com/EndstoneMC/endstone/commit/74d654a8b72ced46915002083026a547b406a37f) · 2024-05-02T14:30:17Z · parent `d3ea43469005580d35b208746d286193ef249971` · api_refactor.

Introduces ServerEvent between Event and the server-specific event classes, including forwarding the asynchronous flag for broadcast events. The corresponding Python classes still declare Event as their bound base; this commit does not expose ServerEvent as a Python type. The useful distinction is a C++ event taxonomy change, with a cross-language surface that is not yet symmetric.

Changed paths: `include/endstone/event/server/broadcast_message_event.h`, `include/endstone/event/server/plugin_disable_event.h`, `include/endstone/event/server/plugin_enable_event.h`, `include/endstone/event/server/server_command_event.h`, `include/endstone/event/server/server_event.h`, `include/endstone/event/server/server_list_ping_event.h`, `include/endstone/event/server/server_load_event.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-850"></a>
### 850 · feat: remove Event::Result {#commit-850}

[Full commit 9ef876e601590c34d342c7a6b6948ccd1474d2db](https://github.com/EndstoneMC/endstone/commit/9ef876e601590c34d342c7a6b6948ccd1474d2db) · 2024-05-02T14:30:30Z · parent `74d654a8b72ced46915002083026a547b406a37f` · api_removal.

Removes the unused Event::Result tri-state enum and its Python enum registration while retaining Boolean cancellation. Registration code also moves. This is a real public enum removal, not merely event cleanup; no alternate cancellation protocol or migration test is added here.

Changed paths: `include/endstone/event/event.h`, `src/endstone_python/event.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-851"></a>
### 851 · style: format codes {#commit-851}

[Full commit 74ddfc9d8c7621fd17ef2f62a6d26fa1f746101f](https://github.com/EndstoneMC/endstone/commit/74ddfc9d8c7621fd17ef2f62a6d26fa1f746101f) · 2024-05-02T14:31:37Z · parent `9ef876e601590c34d342c7a6b6948ccd1474d2db` · mechanical.

Verified formatting changes in three files. No independently changed API behavior or new rationale was found; adjacent event changes retain their own identities and analyses.

Changed paths: `include/bedrock/server/network/server_network_handler.h`, `include/endstone/detail/actor/actor.h`, `src/endstone_core/command/console_command_sender.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-852"></a>
### 852 · fix: Server::getOnlinePlayers {#commit-852}

[Full commit ebdb9e4e7b85355443019d9c937ad83c697ef7a4](https://github.com/EndstoneMC/endstone/commit/ebdb9e4e7b85355443019d9c937ad83c697ef7a4) · 2024-05-02T15:02:49Z · parent `74ddfc9d8c7621fd17ef2f62a6d26fa1f746101f` · corrective_lifecycle.

Repairs846's native PlayerListEntry field to ActorUniqueID, but stops depending on that list for the public enumeration. EndstoneServer instead maintains UUID-to-raw-Player pointers, with EndstonePlayer construction registering and destruction erasing itself; lookup and enumeration use this registry. This avoids the incorrect list interpretation while tying visibility to wrapper lifetime, not an explicit successful-login transition. The map does not own players, has no new synchronization, and emplace/erase assumes UUID uniqueness. These are scope limits, not evidence of an observed concurrent or duplicate-login failure.

Changed paths: `CHANGELOG.md`, `include/bedrock/server/player_list_entry.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/player.h`, `include/endstone/detail/server.h`, `src/endstone_core/player.cpp`, `src/endstone_core/server.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-854"></a>
### 854 · refactor: `Player::getAddress` now returns a `SocketAddress` instead of `std::string` {#commit-854}

[Full commit 948061766b90049da70bd71d2defdda7e4cd71c0](https://github.com/EndstoneMC/endstone/commit/948061766b90049da70bd71d2defdda7e4cd71c0) · 2024-05-02T22:44:46Z · parent `ed2522d24e917f3bb9b7d3c5f9dd9da576e1be30` · api_refactor.

Replaces Player's string address and separate getPort API with a SocketAddress value storing hostname and uint32 port, returned by const reference. Adds the C++ utility, Python class/export, repr/str and stub changes, with changelog migration text. The initial empty default constructor does not initialize the port;870 later changes value-initialization behavior. String formatting is simple hostname:port and adds no validation or IPv6 bracket policy. The stub also removes Event.Result and advertises Level.actors ahead of855, showing that stubs and bindings briefly move at different speeds.

Changed paths: `CHANGELOG.md`, `include/endstone/detail/player.h`, `include/endstone/level/level.h`, `include/endstone/player.h`, `include/endstone/util/socket_address.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/util.py`, `src/endstone_core/player.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/util.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-855"></a>
### 855 · feat: add python bindings for `Level::getActors` {#commit-855}

[Full commit 21fb1662a06170ab7b81f63bed77a2372b450e12](https://github.com/EndstoneMC/endstone/commit/21fb1662a06170ab7b81f63bed77a2372b450e12) · 2024-05-02T22:45:03Z · parent `948061766b90049da70bd71d2defdda7e4cd71c0` · binding.

Adds Python Level.actors and pybind11 STL conversion support. No explicit return policy is supplied on this property, and the change adds no actor-lifetime test. It completes the binding advertised in854's stub, while the native Level actor enumeration was already present.

Changed paths: `src/endstone_python/level.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-857"></a>
### 857 · refactor: update endstone_python.cpp {#commit-857}

[Full commit fc60ae07527929bef7437e378f6985a3e7408b19](https://github.com/EndstoneMC/endstone/commit/fc60ae07527929bef7437e378f6985a3e7408b19) · 2024-05-02T22:52:30Z · parent `9a6c14a207ec32b6846ed404c794860bcc6a44f9` · mechanical.

Reorders online_players and get_level registration in endstone_python.cpp. The bound names, signatures and implementations remain unchanged; no independent design claim is supported.

Changed paths: `src/endstone_python/endstone_python.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-858"></a>
### 858 · fix: typo {#commit-858}

[Full commit 38456a48ee9b2f8fcbec0788cecb6a9fa0e1a281](https://github.com/EndstoneMC/endstone/commit/38456a48ee9b2f8fcbec0788cecb6a9fa0e1a281) · 2024-05-03T11:06:01Z · parent `fc60ae07527929bef7437e378f6985a3e7408b19` · small_correction.

Corrects the changelog's removed-method name from getHost to getPort and changes Python repr's type spelling from SockAddr to SocketAddress. The latter is observable representation text; this is a small correction rather than an entirely behavior-free formatting commit.

Changed paths: `CHANGELOG.md`, `src/endstone_python/util.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-872"></a>
### 872 · feat: add `Player::kick` {#commit-872}

[Full commit 343680ec8f840fe7b150b6b8668b22302030abae](https://github.com/EndstoneMC/endstone/commit/343680ec8f840fe7b150b6b8668b22302030abae) · 2024-05-04T10:28:58Z · parent `aa2d3fb1b0a35fc8c4c672da7e8b03cabf2082d1` · feature_lifetime.

Adds Player::kick via a stored ServerNetworkHandler pointer initialized in the new-player hook before login-event handling. Cancelled login now invokes kick, but the hook still calls the original loadNewPlayer afterward, so cancellation is not implemented as an early return. Native Minecraft members change reference to pointer representations and NonOwnerPointer becomes a wrapper around shared_ptr-shaped storage. These layout declarations do not prove shared ownership of host objects. The player pointer is not independently initialized or guarded before this hook establishes it.

Changed paths: `include/bedrock/common/minecraft.h`, `include/bedrock/memory.h`, `include/endstone/detail/player.h`, `include/endstone/player.h`, `src/endstone_core/player.cpp`, `src/endstone_runtime/bedrock/server/network/server_network_handler.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-873"></a>
### 873 · feat: add `CommandSender::asPlayer` to downcast a CommandSender to Player {#commit-873}

[Full commit 3b82f8a4fa9e835a1ed6e41e2d538ae8c1f1836e](https://github.com/EndstoneMC/endstone/commit/3b82f8a4fa9e835a1ed6e41e2d538ae8c1f1836e) · 2024-05-04T11:12:58Z · parent `343680ec8f840fe7b150b6b8668b22302030abae` · api_feature.

Adds a virtual nullable asPlayer query to CommandSender and overrides it for players; Actor's asCommandSender returns a mutable pointer through const_cast. This gives callers explicit downcasting without requiring a caller-side RTTI expression, but neither type query extends lifetime. The nullable base implementation matters for Python annotations added next.

Changed paths: `include/endstone/command/command_sender.h`, `include/endstone/detail/permissions/permissible_base.h`, `include/endstone/permissions/permissible.h`, `include/endstone/player.h`, `src/endstone_core/permissions/permissible_base.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-874"></a>
### 874 · feat: add python bindings for `Player::kick` {#commit-874}

[Full commit 00af57fb415d7887f188a2290eb82e49192295af](https://github.com/EndstoneMC/endstone/commit/00af57fb415d7887f188a2290eb82e49192295af) · 2024-05-04T11:13:42Z · parent `3b82f8a4fa9e835a1ed6e41e2d538ae8c1f1836e` · binding_then_corrected.

Adds Python kick and initially exposes as_player as a property. CommandSender is registered before Actor/Player, then populated later so return types can resolve. The stub declares a non-null Player even though the base C++ query can return null.875 changes property to method and876 corrects ownership policy; these are separate public/binding revisions.

Changed paths: `CHANGELOG.md`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/command.cpp`, `src/endstone_python/endstone_python.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-875"></a>
### 875 · feat: add python bindings for `CommandSender::sendErrorMessage` {#commit-875}

[Full commit ea13dae11a6edc42cd9cff344d294408f2bea60d](https://github.com/EndstoneMC/endstone/commit/ea13dae11a6edc42cd9cff344d294408f2bea60d) · 2024-05-04T11:23:29Z · parent `00af57fb415d7887f188a2290eb82e49192295af` · binding_then_corrected.

Adds send_error_message and changes as_player from a read-only property to a callable method. The method initially uses pybind11's default return policy for a raw pointer, creating an ownership hazard corrected in876. This is both an API-shape change and a transient policy gap, not simply a missing method exposure.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/command.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-876"></a>
### 876 · fix: use py::return_value_policy::reference for as_player {#commit-876}

[Full commit 6b8173675ad11b2cbcf1c3ecc4b4163681d72c07](https://github.com/EndstoneMC/endstone/commit/6b8173675ad11b2cbcf1c3ecc4b4163681d72c07) · 2024-05-04T11:42:43Z · parent `ea13dae11a6edc42cd9cff344d294408f2bea60d` · corrective_ownership.

Applies explicit return_value_policy::reference to as_player. This prevents the binding from adopting the existing Player pointer as a new owner. It is a precise borrowed-return fix, not a guarantee that the native player remains alive while arbitrary Python references persist; no keep-alive or unload invalidation protocol is added here.

Changed paths: `src/endstone_python/command.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-877"></a>
### 877 · feat: add `Player::getPing` and `Player::updateCommands` {#commit-877}

[Full commit 3cfbb21ec522d78eb338c9c4f68de9cae2a05fc8](https://github.com/EndstoneMC/endstone/commit/3cfbb21ec522d78eb338c9c4f68de9cae2a05fc8) · 2024-05-04T15:26:53Z · parent `6b8173675ad11b2cbcf1c3ecc4b4163681d72c07` · api_feature.

Adds ping as a millisecond duration from RakPeer's average-ping API and moves command-update behavior into the public Player wrapper. Command-list serialization filters using registered Endstone command permissions and hides commands unavailable to both player/block contexts. Spawn handling calls join listeners, recalculates permissions and then updates visible commands; the native permission hook also refreshes. This orders initial advertisement after plugin changes, but the commit does not make every later permission attachment automatically trigger a refresh.

Changed paths: `include/bedrock/world/actor/player/player.h`, `include/endstone/detail/player.h`, `include/endstone/player.h`, `src/endstone_core/player.cpp`, `src/endstone_runtime/bedrock/server/level/server_player.cpp`, `src/endstone_runtime/bedrock/world/actor/player/player.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-878"></a>
### 878 · feat: python bindings for `Player::getPing` and `Player:;updateCommands` {#commit-878}

[Full commit 427ccda13c783bfe0f97a2254b8f93fc80e6dc0b](https://github.com/EndstoneMC/endstone/commit/427ccda13c783bfe0f97a2254b8f93fc80e6dc0b) · 2024-05-04T15:32:35Z · parent `3cfbb21ec522d78eb338c9c4f68de9cae2a05fc8` · binding.

Exposes ping through pybind11 chrono as a Python timedelta and adds update_commands, stubs and changelog entries. The native duration's milliseconds are preserved by conversion rather than presented as an unlabelled integer. No networking or client-command synchronization test is added.

Changed paths: `CHANGELOG.md`, `include/endstone/player.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/endstone_python.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.
