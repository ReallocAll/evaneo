<!-- retrieval: {"source_ids":["public:commit:0f4ec903e6bf52002e552276420d16bcf215563b","public:commit:262a776ca2b792992653c9893d171ff9fe024124","public:commit:26f6c7ade678e1ac4ce2ea1814fbb0acd6b6fe55","public:commit:27803d16f3b5519e91ee6acbe42b670bf6cdaf3f","public:commit:39fe54e51c66788558fa055ce5d9e16bce9b2a15","public:commit:4163a98bf8667446e49b371c1769431ed16cce1a","public:commit:462d10f67db40dfed98f989d42b7bdd410bf00bd","public:commit:501467b515d108f965b55a1045aaf69bc2e236dd","public:commit:5c7be0a67bac7ba9c0c62e6bc9345401abbc86c3","public:commit:60cfec2e76cf28fe2faba78ffd5becbcd294cd63","public:commit:62d59c12579ee76cb9caaaee02ca393755b49ab6","public:commit:79edf358e9842e8b9e11180119cfcd7b4a181307","public:commit:97368d443af5a416a77ca2edfe4fa20deb88d602","public:commit:974f084805599a05a75ccba67928441349c6ab0f","public:commit:9d6350b1f93b99ca739fbde004e57ccbbc5051c8","public:commit:9ea55d09ecfd0c9b88c931b340dd2b29a72d9776","public:commit:b7169e80ac55670ca2ccea7f6a69858e2955d830","public:commit:ba5e7a63f4c223cb7187db264e35178e752b46b7","public:commit:c87946095eba87939d9c5ec57b3e359ca2b82a77","public:commit:cc22e6e85a3ed76ee8e11fc8d8116d405ba53dbc","public:commit:d14a39a3566bfccb073f40372becdef1a6e5a71a","public:commit:e1dea3f66995058b5b0479d37976a995d23fdbb9","public:commit:ea5a0ecf8e9eb98d6fdf72f6a4a0f56c3640193b","public:commit:f233f6476cdb7da765b9f62df247ff63ea7ac2c2"],"source_type":"public","date":"2024-09-14..2024-10-07","topics":["concurrency","ffi","testing","build","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native models and the 1.21.30 transition {#native-models-and-the-1-21-30-transition}

Scope: Endstone commits 1801–1920, September 14–October 22, 2024. These notes follow related implementation areas during this period.

## Causal reading and applicability {#causal-reading-and-applicability}

The September 14–16 refactors make native Bedrock representations more explicit, then the September 18–19 transition updates both platform hooks and several event/layout assumptions for 1.21.30. The relevant distinction is representation, ABI and public behavior: a renamed header may preserve a body, while a nearby enum width, variant member, virtual slot or pointer type changes compatibility. The full large patches were read rather than classified by their “refactor” titles. Exact R100 relocations and recurring license headers receive structural reuse; modified declarations and bodies remain individually covered.

The most useful negative chain is 1822 → 1831. Recovering a real largest payload and asserting variant size addresses one ABI dimension, but adding a missing emote alternative later repairs discriminator order without necessarily altering that size. Use this evidence to remember that native-model validation needs field offsets, alignment, virtual order, enum values and variant membership as well as total size. This is an inference from the two observed repairs, not a documented universal author rule. Likewise the ChunkPos union in 1806 is a concrete reason not to equate “typed” with “correct.” The later player/network capabilities and readonly online-mode work extend the native surface without changing authentication policy.

The historical review compared Windows and Linux symbol maps separately; its manifest-audit JSON is not distributed. Platform support badges, commit titles and sizeof assertions are reported claims or static mechanisms. There was no running BDS, packet capture, native disassembly validation, compiler or test execution in this unit. Engine-owned behavior behind recovered declarations remains prior context where already reviewed, or unknown where not observed. External issues #51 and #60 were not read here; the local changes and claimed problem are sufficient for bounded analysis but not full issue-resolution certification.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1801"></a>
### Commit 1801 · refactor: bedrock threading {#commit-1801}

Source: [4163a98bf8667446e49b371c1769431ed16cce1a](https://github.com/EndstoneMC/endstone/commit/4163a98bf8667446e49b371c1769431ed16cce1a). Authored 2024-09-14T17:38:23Z; committed 2024-09-14T17:38:23Z. Git author: Vincent; committer: Vincent.


The broad threading split relocates result and queue declarations and moves AssignedThread::isOnThread out of line without changing the thread-ID comparison. New AsyncBase/IAsyncInfo declarations describe cancellation, status and result interfaces; this is native-model groundwork, not an implemented cancellation or scheduling guarantee. Include adjustments and removal of unused declarations are read as part of the same patch. The useful distinction is between recovering a native interface and supplying its behavior.

Changed-source navigation: `include/bedrock/core/result.h`, `include/bedrock/core/threading.h`, `include/bedrock/core/threading/async.h`, `include/bedrock/core/threading/enable_queue_for_main_thread.h`, `include/bedrock/core/threading/enable_queue_for_thread.h`, `include/bedrock/core/utility/binary_stream.h`, `include/bedrock/nbt/tag.h`; plus 12 paths not listed here.

<a id="commit-1802"></a>
### Commit 1802 · fix: correct entity components for compatibility with version 1.21.20 changes {#commit-1802}

Source: [501467b515d108f965b55a1045aaf69bc2e236dd](https://github.com/EndstoneMC/endstone/commit/501467b515d108f965b55a1045aaf69bc2e236dd). Authored 2024-09-14T19:13:46Z; committed 2024-09-14T19:13:46Z. Git author: Vincent; committer: Vincent.


The 1.21.20 component model replaces generic flag components with specifically named types, which matters to EnTT type identity, and routes water/lava checks through the corresponding previous-state flags. Built-in components become four non-null pointers; AABB shape and walking animation fields become explicit. Passenger information now contains the expanded strict entity context and actor ID. ActorOwnerComponent exposes a dereferenced unique owner, and tryGetFromEntity consequently loses the earlier owner-null check. These are representation and behavior changes inside a large refactor, not just renamed headers. Native layout and component availability remain unexecuted assumptions.

Changed-source navigation: `include/bedrock/core/type_id.h`, `include/bedrock/core/utility/type_id.h`, `include/bedrock/entity/components/aabb_shape_component.h`, `include/bedrock/entity/components/actor_data_component_base.h`, `include/bedrock/entity/components/actor_data_flag_component.h`, `include/bedrock/entity/components/actor_owner_component.h`, `include/bedrock/entity/components/actor_rotation_component.h`; plus 31 paths not listed here.

<a id="commit-1803"></a>
### Commit 1803 · refactor: network packets {#commit-1803}

Source: [60cfec2e76cf28fe2faba78ffd5becbcd294cd63](https://github.com/EndstoneMC/endstone/commit/60cfec2e76cf28fe2faba78ffd5becbcd294cd63). Authored 2024-09-14T21:08:31Z; committed 2024-09-14T21:08:31Z. Git author: Vincent; committer: Vincent.


Networking declarations move into more specific headers, but the patch also widens NetworkIdentifier's NetherNet identifier from 32 to 64 bits, gives AvailableCommandsPacket concrete vector element types and ordering, and adds typed connection fallback and unconnected-pong configuration. SerializedAbilities separates player and command permission fields. MoveActorAbsoluteHeader becomes a bitfield model; command flag categories become scoped types while retaining bit meanings. Boss colors gain RebeccaPurple at 6 and move White to 7, propagated publicly in 1804. TransferPacket gains reload_world without a member initializer; no claim is made about every native construction path. The packet-ID relocation was read in full, including the repaired initially truncated middle; unchanged bulk is not counted as a new design preference.

Changed-source navigation: `include/bedrock/common_types.h`, `include/bedrock/entity/components/user_entity_identifier_component.h`, `include/bedrock/network/compressibility.h`, `include/bedrock/network/connection.h`, `include/bedrock/network/connection_definition.h`, `include/bedrock/network/connection_request.h`, `include/bedrock/network/disconnection_request_info.h`; plus 37 paths not listed here.

<a id="commit-1804"></a>
### Commit 1804 · refactor: command related classes {#commit-1804}

Source: [0f4ec903e6bf52002e552276420d16bcf215563b](https://github.com/EndstoneMC/endstone/commit/0f4ec903e6bf52002e552276420d16bcf215563b). Authored 2024-09-14T22:07:50Z; committed 2024-09-14T22:07:50Z. Git author: Vincent; committer: Vincent.


MCRESULT receives explicit category/construction and isSuccess access instead of exposed fields. CommandRegistry replaces placeholders with typed enum lookup, symbol sets and callbacks; notably an enum-lookup value becomes 64-bit and parameter-symbol storage changes size. Dimension-change requests own CompoundTag data rather than an opaque pointer. Public and Python BarColor values follow the native change, including White=7. Rotation utility and command-origin declarations are reorganized, with call sites updated. This couples private ABI recovery to public compatibility; deleting unused PlayerListEntry/ContentIdentity placeholders does not demonstrate removal of a working user feature.

Changed-source navigation: `include/bedrock/core/utility/mc_result.h`, `include/bedrock/forward.h`, `include/bedrock/platform/build_platform.h`, `include/bedrock/server/commands/command.h`, `include/bedrock/server/commands/command_origin.h`, `include/bedrock/server/commands/command_origin_data.h`, `include/bedrock/server/commands/command_origin_identity.h`; plus 18 paths not listed here.

<a id="commit-1805"></a>
### Commit 1805 · refactor: world related classes {#commit-1805}

Source: [462d10f67db40dfed98f989d42b7bdd410bf00bd](https://github.com/EndstoneMC/endstone/commit/462d10f67db40dfed98f989d42b7bdd410bf00bd). Authored 2024-09-14T23:53:28Z; committed 2024-09-14T23:53:28Z. Git author: Vincent; committer: Vincent.


The world-model split recovers Item field order, unsigned maximum-stack and descriptor-stack sizes, use animation and flags. Recipe results replace padding with an unloaded-result vector; scoreboard state adds a weak manager and tracked objectives. Minecraft's network owner registry becomes typed, and ILevel replaces unknown virtual entries with named operations and return types. Ability access still lacks new type-transition validation, and attribute member renaming preserves its dirty-state behavior. These changes improve representational specificity without independently proving binary compatibility; the raw 1,402-line patch was read in three pages.

Changed-source navigation: `include/bedrock/core/utility/non_owner_pointer.h`, `include/bedrock/deps/raknet/rak_peer_interface.h`, `include/bedrock/entity/components/abilities_component.h`, `include/bedrock/entity/components/actor_type_flag_component.h`, `include/bedrock/entity/components/attributes_component.h`, `include/bedrock/entity/components/replay_state_config.h`, `include/bedrock/entity/gamerefs_entity/entity_registry.h`; plus 64 paths not listed here.

<a id="commit-1806"></a>
### Commit 1806 · refactor: block and level classes {#commit-1806}

Source: [c87946095eba87939d9c5ec57b3e359ca2b82a77](https://github.com/EndstoneMC/endstone/commit/c87946095eba87939d9c5ec57b3e359ca2b82a77). Authored 2024-09-15T17:36:37Z; committed 2024-09-15T17:36:37Z. Git author: Vincent; committer: Vincent.


Block state becomes a small cached payload plus typed direct component pointers instead of anonymous padding. NewType-based IDs and brightness wrappers affect conversions, while the BlockSource interfaces are reorganized into const/non-const inheritance and DimensionOwnerPtr replaces a raw-source representation. SharedMutex and typed cache storage replace unknown native details; SolidBlocking is removed from the modeled legacy flags. The patch's ChunkPos nested union makes x and z overlap, a static counterexample to treating a cleaner-looking model as automatically correct. No runtime coordinate failure is asserted. All 1,354 raw lines were read; changed behavior is separated from unchanged moved bodies.

Changed-source navigation: `include/bedrock/common_types.h`, `include/bedrock/core/container/cache.h`, `include/bedrock/forward.h`, `include/bedrock/gamerefs/gamerefs_shareptr/owner_storage_shareptr.h`, `include/bedrock/server/commands/command_registry.h`, `include/bedrock/util/new_type.h`, `include/bedrock/world/level/block/actor/block_actor.h`; plus 26 paths not listed here.

<a id="commit-1807"></a>
### Commit 1807 · refactor: event-related classes {#commit-1807}

Source: [5c7be0a67bac7ba9c0c62e6bc9345401abbc86c3](https://github.com/EndstoneMC/endstone/commit/5c7be0a67bac7ba9c0c62e6bc9345401abbc86c3). Authored 2024-09-15T19:04:39Z; committed 2024-09-15T19:04:39Z. Git author: Vincent; committer: Vincent.


Event coordinators, listeners and handlers are split into dedicated files. ConstEventVariant and coordinator result types make dispatch structure explicit, and the Linux game-rule variant membership changes. GameplayHandlerResult reverses the earlier field ordering to handler result then return value. Full subsequent weather-hook context returns the original result, so this review does not invent an aggregate-initializer regression there. The initial generic dispatcher is incomplete and hard-wired to actor details; 1808 retreats to placeholders. InteractionResult gains named success/swing/failure factories. Startup/shutdown bodies and the existing GIL rationale move unchanged: this patch is not evidence of a new shutdown fix. All 1,989 raw lines were read.

Changed-source navigation: `include/bedrock/entity/gamerefs_entity/weak_storage_entity.h`, `include/bedrock/forward.h`, `include/bedrock/gameplayhandlers/coordinator_result.h`, `include/bedrock/gameplayhandlers/event_handler_dispatcher.h`, `include/bedrock/gameplayhandlers/gameplay_handler.h`, `include/bedrock/gameplayhandlers/gameplay_handler_result.h`, `include/bedrock/gameplayhandlers/level_gameplay_handler.h`; plus 60 paths not listed here.

<a id="commit-1808"></a>
### Commit 1808 · refactor: gameplay handlers {#commit-1808}

Source: [39fe54e51c66788558fa055ce5d9e16bce9b2a15](https://github.com/EndstoneMC/endstone/commit/39fe54e51c66788558fa055ce5d9e16bce9b2a15). Authored 2024-09-16T09:39:16Z; committed 2024-09-16T09:39:16Z. Git author: Vincent; committer: Vincent.


The immediate follow-up removes the unusable generic dispatcher/ScriptEventHandler internals and leaves empty template shells, while specifying LevelGameplayHandler's two event virtuals and the script handler destructor. This is a compile-oriented reduction of the previous refactor's ambition, not completion of generic event dispatch. Full related handler, strict context and weather-hook files were read to distinguish actual layout changes from speculation. The observed alternative is concrete minimal declarations after an overextended initial model.

Changed-source navigation: `include/bedrock/gameplayhandlers/event_handler_dispatcher.h`, `include/bedrock/gameplayhandlers/level_gameplay_handler.h`, `include/bedrock/scripting/event_handlers/script_event_handler.h`, `include/bedrock/scripting/event_handlers/script_level_gameplay_handler.h`.

<a id="commit-1812"></a>
### Commit 1812 · ci: fix compilation errors {#commit-1812}

Source: [d14a39a3566bfccb073f40372becdef1a6e5a71a](https://github.com/EndstoneMC/endstone/commit/d14a39a3566bfccb073f40372becdef1a6e5a71a). Authored 2024-09-16T11:32:00Z; committed 2024-09-16T11:32:00Z. Git author: Vincent; committer: Vincent.


Restores the EntityContext include required by the weak-storage header after the event-model refactor. This is a specific dependency repair, with no independent API behavior or style inference.

Changed-source navigation: `include/bedrock/entity/gamerefs_entity/weak_storage_entity.h`.

<a id="commit-1813"></a>
### Commit 1813 · ci: add Python 3.13 support to workflow for wheel build {#commit-1813}

Source: [97368d443af5a416a77ca2edfe4fa20deb88d602](https://github.com/EndstoneMC/endstone/commit/97368d443af5a416a77ca2edfe4fa20deb88d602). Authored 2024-09-16T14:49:29Z; committed 2024-09-16T14:49:29Z. Git author: Vincent; committer: Vincent.


Besides adding Linux Python 3.13, this commit broadens native wrapper selection from a category check to hasType(Mob) OR hasCategory(Mob). That changes which concrete wrapper is constructed and is semantically important despite the CI-oriented title. The native actor still must satisfy the cast's assumptions; the patch does not establish those for every engine actor.

Changed-source navigation: `.github/workflows/wheel.yml`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`.

<a id="commit-1814"></a>
### Commit 1814 · fix: prevent server crash when spawning a simulated player without a valid network identifier (#51) {#commit-1814}

Source: [cc22e6e85a3ed76ee8e11fc8d8116d405ba53dbc](https://github.com/EndstoneMC/endstone/commit/cc22e6e85a3ed76ee8e11fc8d8116d405ba53dbc). Authored 2024-09-16T21:39:33Z; committed 2024-09-16T21:39:33Z. Git author: Vincent; committer: Vincent.


For the reported simulated-player crash (#51), the network identifier's fourth category is named Invalid, and unsupported NetherNet/Invalid cases no longer throw while forming an Endstone player address. The object can retain its default address and proceed through normal player handling. This is tolerance of a missing/unsupported network address, not an authentication-policy change. The external issue and simulated-player runtime were not independently exercised.

Changed-source navigation: `include/bedrock/network/network_identifier.h`, `src/endstone_core/player.cpp`, `src/endstone_runtime/bedrock/network/network_identifier.cpp`.

<a id="commit-1818"></a>
### Commit 1818 · feat: add BiomeRegistry class {#commit-1818}

Source: [27803d16f3b5519e91ee6acbe42b670bf6cdaf3f](https://github.com/EndstoneMC/endstone/commit/27803d16f3b5519e91ee6acbe42b670bf6cdaf3f). Authored 2024-09-17T12:02:37Z; committed 2024-09-17T12:02:37Z. Git author: Vincent; committer: Vincent.


Adds explicit biome/tag registry models and enumerates non-null, non-empty biomes by ID. The patch does not introduce locking merely because the registry has an atomic closed flag. It also changes command-origin output receiver and Entity handling, temporarily follows a virtual origin's receiver, and logs serialized origin data. These command experiments are revised in 1819; they should not be treated as a stable final routing policy. Native tag IDs introduced here become relevant to the later actor-tag implementation.

Changed-source navigation: `include/bedrock/forward.h`, `include/bedrock/server/commands/command_origin.h`, `include/bedrock/util/biome_tag_registry_types.h`, `include/bedrock/util/id_type.h`, `include/bedrock/util/tag_registry.h`, `include/bedrock/world/level/biome/biome.h`, `include/bedrock/world/level/biome/registry/biome_registry.h`; plus 5 paths not listed here.

<a id="commit-1820"></a>
### Commit 1820 · feat: add support for BDS v1.21.30 on Windows (part 1) {#commit-1820}

Source: [79edf358e9842e8b9e11180119cfcd7b4a181307](https://github.com/EndstoneMC/endstone/commit/79edf358e9842e8b9e11180119cfcd7b4a181307). Authored 2024-09-18T11:26:42Z; committed 2024-09-18T11:26:42Z. Git author: Vincent; committer: Vincent.


The Windows 1.21.30 update changes the RVA map alongside Item rarity virtuals, mining-component fields, Block direct-data size, a removed legacy-block virtual, and an ILevel hardcore virtual. Python's expected native version advances before the Linux address map, which follows in 1825. A five-second initialization delay is introduced and then removed in 1822; no supported rationale for that temporary delay is supplied. Symbol-map values were structurally compared, and the initially truncated map lines were reread. Address correctness and binary layout remain untested here.

Changed-source navigation: `include/bedrock/world/interactions/mining/mine_block_item_effect_type.h`, `include/bedrock/world/item/item.h`, `include/bedrock/world/item/item_helper.h`, `include/bedrock/world/item/rarity.h`, `include/bedrock/world/level/block/block.h`, `include/bedrock/world/level/block/block_legacy.h`, `include/bedrock/world/level/block/components/block_component_direct_data.h`; plus 4 paths not listed here.

<a id="commit-1821"></a>
### Commit 1821 · fix: remove debug codes {#commit-1821}

Source: [974f084805599a05a75ccba67928441349c6ab0f](https://github.com/EndstoneMC/endstone/commit/974f084805599a05a75ccba67928441349c6ab0f). Authored 2024-09-18T12:49:04Z; committed 2024-09-18T12:49:04Z. Git author: Vincent; committer: Vincent.


Removes temporary command-token debugging and periodic logger flushing from runtime initialization while leaving 1820's delay in place. The next commit restores periodic flushing and removes the delay, so this short-lived state is not a stable logging preference.

Changed-source navigation: `src/endstone_core/command/command_adapter.cpp`, `src/endstone_runtime/main.cpp`.

<a id="commit-1822"></a>
### Commit 1822 · fix: player event coordinator crash caused by changes in player event size {#commit-1822}

Source: [262a776ca2b792992653c9893d171ff9fe024124](https://github.com/EndstoneMC/endstone/commit/262a776ca2b792992653c9893d171ff9fe024124). Authored 2024-09-18T13:12:58Z; committed 2024-09-18T13:12:58Z. Git author: Vincent; committer: Vincent.


The reported player-event coordinator crash is addressed by replacing a dummy largest-event payload with actual before/after block-interaction fields, including raw ItemStack storage for otherwise unavailable construction. Variant sizes are asserted at 384, 232 and 48 bytes. The startup delay is removed and periodic flushing restored. Later 1831 must still insert a missing emote variant despite the aggregate size checks, showing why size agreement alone does not establish variant-index correctness. These are author-reported fixes and compile-time assertions, not reviewer-run native tests.

Changed-source navigation: `include/bedrock/world/events/player_events.h`, `include/bedrock/world/interactions/mining/mine_block_item_effect_type.h`, `include/bedrock/world/item/item_helper.h`, `include/bedrock/world/item/rarity.h`, `src/endstone_runtime/main.cpp`.

<a id="commit-1823"></a>
### Commit 1823 · feat: update protocol related enums {#commit-1823}

Source: [f233f6476cdb7da765b9f62df247ff63ea7ac2c2](https://github.com/EndstoneMC/endstone/commit/f233f6476cdb7da765b9f62df247ff63ea7ac2c2). Authored 2024-09-18T13:16:56Z; committed 2024-09-18T13:16:56Z. Git author: Vincent; committer: Vincent.


Adds the two new packet IDs 316/317 and moves the end marker to 318. New disconnect reasons are modeled as well; a duplicated numeric reason value remains visible in the patch. No protocol capture establishes whether that duplication is intentional. This is a small but meaningful protocol-model update, not just an enum formatting change.

Changed-source navigation: `include/bedrock/network/disconnection_request_info.h`, `include/bedrock/network/packet.h`.

<a id="commit-1824"></a>
### Commit 1824 · feat: update current command version to 42 {#commit-1824}

Source: [ea5a0ecf8e9eb98d6fdf72f6a4a0f56c3640193b](https://github.com/EndstoneMC/endstone/commit/ea5a0ecf8e9eb98d6fdf72f6a4a0f56c3640193b). Authored 2024-09-18T13:47:47Z; committed 2024-09-18T13:47:47Z. Git author: Vincent; committer: Vincent.


Raises the native command version from 41 to 42 for the new game version. The concrete compatibility constant is verified; acceptance by a live command engine is not.

Changed-source navigation: `src/endstone_runtime/magic.cpp`.

<a id="commit-1825"></a>
### Commit 1825 · feat: add support for BDS v1.21.30 on Linux (wip) {#commit-1825}

Source: [e1dea3f66995058b5b0479d37976a995d23fdbb9](https://github.com/EndstoneMC/endstone/commit/e1dea3f66995058b5b0479d37976a995d23fdbb9). Authored 2024-09-18T19:44:37Z; committed 2024-09-18T19:44:37Z. Git author: Vincent; committer: Vincent.


Updates Linux hook addresses for 1.21.30, explicitly still described as work in progress. The historical review recorded each changed TOML value, but the linked public commit provides the source patch. This supplies the platform counterpart to 1820 without independently validating any address against a running binary.

Changed-source navigation: `python/src/endstone/_internal/symbols.toml`.

<a id="commit-1829"></a>
### Commit 1829 · feat: complete the structure of class Biome {#commit-1829}

Source: [9d6350b1f93b99ca739fbde004e57ccbbc5051c8](https://github.com/EndstoneMC/endstone/commit/9d6350b1f93b99ca739fbde004e57ccbbc5051c8). Authored 2024-09-19T13:08:05Z; committed 2024-09-19T13:08:05Z. Git author: Vincent; committer: Vincent.


Expands Biome into named native fields and changes export values from bare IDs to objects containing id, a consumer-visible JSON schema change. The new ID offset comment says 188 rather than 180, but the previous virtual pointer plus fields already account for that difference; the comment alone does not prove an actual eight-byte offset fix. This distinction prevents a misleading ABI success story from a header cleanup.

Changed-source navigation: `include/bedrock/forward.h`, `include/bedrock/world/level/biome/biome.h`, `src/endstone_devtools/vanilla_data.cpp`.

<a id="commit-1831"></a>
### Commit 1831 · fix: resolve server crash when a player uses an emote {#commit-1831}

Source: [ba5e7a63f4c223cb7187db264e35178e752b46b7](https://github.com/EndstoneMC/endstone/commit/ba5e7a63f4c223cb7187db264e35178e752b46b7). Authored 2024-09-19T16:04:25Z; committed 2024-09-19T16:04:25Z. Git author: Vincent; committer: Vincent.


Inserts the missing player emote event into the native event variant to address the reported emote crash. Its significance is variant membership/index order, not a larger maximum object size. Read alongside 1822, it provides a concrete negative example: matching sizeof assertions does not validate the discriminator mapping. No gameplay execution was performed.

Changed-source navigation: `include/bedrock/world/events/player_events.h`.

<a id="commit-1832"></a>
### Commit 1832 · chore: remove const qualifier to suppress build warning {#commit-1832}

Source: [26f6c7ade678e1ac4ce2ea1814fbb0acd6b6fe55](https://github.com/EndstoneMC/endstone/commit/26f6c7ade678e1ac4ce2ea1814fbb0acd6b6fe55). Authored 2024-09-19T16:23:30Z; committed 2024-09-19T16:23:30Z. Git author: Vincent; committer: Vincent.


Removes const from the modeled Biome field to address the reported warning. This adjusts the declaration; it does not demonstrate a newly supported mutation operation or a broader preference against const.

Changed-source navigation: `include/bedrock/world/level/biome/biome.h`.

<a id="commit-1834"></a>
### Commit 1834 · fix(raknet): resolve crash during server pong handling {#commit-1834}

Source: [9ea55d09ecfd0c9b88c931b340dd2b29a72d9776](https://github.com/EndstoneMC/endstone/commit/9ea55d09ecfd0c9b88c931b340dd2b29a72d9776). Authored 2024-09-25T13:58:32Z; committed 2024-09-25T13:58:32Z. Git author: Vincent; committer: Vincent.


The outbound unconnected-pong hook now requires its advertised string length to equal the remaining packet bytes, rather than only rejecting zero length. Full function context shows that packet ID/header bytes are accessed before a comprehensive minimum-length check, so this is a consistency guard rather than general buffer-safety validation. It is an outbound send hook; this review does not recast it as a proven remotely exploitable inbound parser. The claimed #60 fix remains unexecuted.

Changed-source navigation: `src/endstone_runtime/bedrock/deps/raknet/raknet_socket2.cpp`.

<a id="commit-1868"></a>
### Commit 1868 · feat: add PlayerCapabilities {#commit-1868}

Source: [62d59c12579ee76cb9caaaee02ca393755b49ab6](https://github.com/EndstoneMC/endstone/commit/62d59c12579ee76cb9caaaee02ca393755b49ab6). Authored 2024-10-05T08:53:48Z; committed 2024-10-05T08:53:48Z. Git author: Vincent; committer: Vincent.


Adds native PlayerCapabilities interfaces and an adapter that delegates ability access and derives operator status from player permissions. Level::isUsableLevel becomes a simple not-tearing-down predicate. Neither declaration establishes lifecycle synchronization or protects every later use after the check; these are native capability and state adapters.

Changed-source navigation: `include/bedrock/config/player_capabilities.h`, `include/bedrock/forward.h`, `include/bedrock/world/actor/player/player.h`, `include/bedrock/world/level/level.h`, `include/bedrock/world/level/level_interface.h`, `src/endstone_runtime/bedrock/config/player_capabilities.cpp`, `src/endstone_runtime/bedrock/world/actor/player/player.cpp`; plus 1 paths not listed here.

<a id="commit-1874"></a>
### Commit 1874 · feat: add Server::getOnlineMode {#commit-1874}

Source: [b7169e80ac55670ca2ccea7f6a69858e2955d830](https://github.com/EndstoneMC/endstone/commit/b7169e80ac55670ca2ccea7f6a69858e2955d830). Authored 2024-10-07T21:58:59Z; committed 2024-10-07T21:58:59Z. Git author: Vincent; committer: Vincent.


Exposes readonly online_mode from the native require_trusted_authentication flag and reports it as a metrics DrilldownPie. Native network configuration structures become more explicit to reach that field; mocks adapt to the new Server method. This reads authentication configuration and does not change it. Layout correctness and emitted telemetry were not executed, and the mock changes contain no new assertions.

Changed-source navigation: `include/bedrock/forward.h`, `include/bedrock/network/network_permissions.h`, `include/bedrock/network/network_server_config.h`, `include/bedrock/network/server_network_handler.h`, `include/bedrock/server/deny_list.h`, `include/endstone/detail/server.h`, `include/endstone/server.h`; plus 6 paths not listed here.
