<!-- retrieval: {"source_ids":["public:commit:08e705bf80e4ac8bee3874e04aa4316f4b5530f0","public:commit:19db5951f7fd412e6ba21652fe3b6d8d720a8c90","public:commit:1bc2bda8a8778e0f979c314f171d2532976588f9","public:commit:3999130e27203483de6ab6a19f41e5a4b504bf7e","public:commit:3f9ff1b6fc6a9a908f24cba37ae1f0c1d3d91d46","public:commit:4a7c9627c2cc8b40911025dcc44a8a1f606d13d8","public:commit:6d44e4183058fed4a7f04c32f00e12864be03835","public:commit:6f5a5cf2defd64a579d6a6ccbef50b5d28ddf648","public:commit:81ac461d1753476b110fae38694cbebe8923cbd6","public:commit:86e79dc1e58d55f129c70d6f64bd627d0d71ec82","public:commit:94c95ed4e47dbcded562e81b4e33be4b99894d47","public:commit:9fd538b41ceff741121428c84aeb8a189af1ae96","public:commit:a06201524bda2e9155925d7b4ae48c2ae36b0019","public:commit:a68b7d54b3b2feffa77f1c89d7889d810c3c6424","public:commit:b41f450196dbe3592fdd68e496a4923f08d8d3c5","public:commit:e202af151f11d0d9afdb2ce1a5521c935801dcfd","public:commit:fd70ddc49222bb40cc6c17ff65d54b766e809a74","public:thread:EndstoneMC/endstone:263"],"source_type":"public","date":"2025-01-06..2025-09-08","topics":["lifetime","ffi","testing","build","performance","api","diagnosis","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Project layout, direct native calls and hook originals {#project-layout-direct-native-calls-and-hook-originals}

## Remove duplicated reading without erasing the migration {#remove-duplicated-reading-without-erasing-the-migration}

53 has 672 rename-aware file changes.510 are exact old/new blobs,159 are exact documented namespace/include rewrites, and only3 have remaining semantic residuals. The audit records every source/destination/blob and the allowed spelling substitutions. Across twelve related migration commits there are 599 identical blobs,269 exact rewrites and298 residual file changes. Every residual was read. A move's unchanged implementation is not counted as a newly read independent design; namespace and target-level changes are still part of the reviewed architecture.

The reorganization is staged.55 builds Python then returns;56 adds Bedrock;57 adds core;59 removes the return while runtime/tests remain commented;60 restores tests;61 restores runtime. Bedrock becomes a static native-declaration/implementation target, public API is an interface target, core owns Endstone abstractions and later devtools, and runtime owns actual native detours. Copying hook sources while splitting bodies causes transient duplicate/missing definitions repaired by57,66,71 and73. A title such as 'build target' does not mean every intermediate tree is independently releasable.

## Two address paths, with different invariants {#two-address-paths-with-different-invariants}

Before the split, hook original lookup also served unhooked native functions.56 starts a separate symbol-call path.61 checks decorated symbol membership at compile time,62 builds hook targets from that same table,64 generates a header from platform-specific TOML, and82 makes the offset lookup consteval. Direct BEDROCK_CALL then adds a compile-time offset to the process executable base and reconstructs the typed function pointer.84 caches base retrieval in function-local statics. This removes runtime linear symbol lookup for the direct-call path, but no profiling or speedup measurement accompanies it.

Hook calls must instead use the installed trampoline.81 replaces detour-address/string maps with a hash-of-decorated-symbol map and removes fallback native target insertion. Symbol capture outside lambdas is important: __FUNCDNAME__ inside the lambda would identify the wrong function.83 makes the integral constant value explicit. Hash collisions are not checked in the visible emplace path; that is a boundary of this implementation, not evidence any observed symbol pair collides. Export/ELF detour discovery and target table synchronization still matter.

Member function pointer reconstruction preserves a raw address plus zero adjustment with a source DOI comment. That is not a general portable C++ cast. The DOI is retained as upstream source attribution; its paper was not independently reviewed here. Native constructors become explicit BEDROCK_CTOR calls using decorated constructor symbols in 71. ServerScoreboard supplies local virtual methods that throw unreachable while relying on the native constructor to establish the native object/vtable. That is an ABI/lifetime assumption, not a standard-C++ proof.

<a id="generator-and-boundary-limits"></a>
## Generator and boundary limits {#generator-and-boundary-limits}

The generator is read as source, never executed. It selects the compilation platform's symbol table, emits constexpr pairs and is wired as a CMake dependency.65 propagates directory/open errors rather than silently returning success, and skips zero offsets, but declared array capacity remains table.size. Literal symbol strings and offsets are data derived from the native version1.21.50; no current-version compatibility is implied.

PR 122 proposes an unmerged LeviLamina adapter on a separate head. Its OEOTYAN adapter and Jonathan Stoler parser retain their authorship, and Wu's closure directs users to LeviStone rather than endorsing the proposal. Sharing a base revision with Endstone does not establish adoption.


<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}



<a id="commit-053"></a>
### 053. refactor: use new project structure {#commit-053}

Commit: [94c95ed4e47dbcded562e81b4e33be4b99894d47](https://github.com/EndstoneMC/endstone/commit/94c95ed4e47dbcded562e81b4e33be4b99894d47) · committed 2025-01-06T16:29:23Z · author Vincent.

Actual parent: `ff3040a9bd24c26479a2f7255b5a6c6092a6c314`. Full message and parent-relative patch: local source.

Large new project structure:672 files audited,510 exact blobs,159 exact namespace/include rewrites,3 residuals read. Bedrock implementation under src/bedrock, core/Python implementation under src/endstone; detail→core/python. Removed endstone.h splits not yet repaired. Adds brstd overloaded helper. Root compile definitions marked TODO target scope. Moves do not imply new design or rereading unchanged semantics.

Changed-file coverage: 672 paths. `CMakeLists.txt`; `include/endstone/endstone.h`; `include/bedrock/app_platform_listener.h → src/bedrock/app_platform_listener.h`; `include/bedrock/bedrock.h → src/bedrock/bedrock.h`; `src/endstone_runtime/bedrock/certificates/certificate.cpp → src/bedrock/certificates/certificate.cpp`; `include/bedrock/certificates/certificate.h → src/bedrock/certificates/certificate.h`; `src/endstone_runtime/bedrock/certificates/extended_certificate.cpp → src/bedrock/certificates/extended_certificate.cpp`; `include/bedrock/certificates/extended_certificate.h → src/bedrock/certificates/extended_certificate.h`; `src/endstone_runtime/bedrock/certificates/web_token.cpp → src/bedrock/certificates/web_token.cpp`; `include/bedrock/certificates/web_token.h → src/bedrock/certificates/web_token.h`; `include/bedrock/common_types.h → src/bedrock/common_types.h`; `src/endstone_runtime/bedrock/config/player_capabilities.cpp → src/bedrock/config/player_capabilities.cpp`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.




<a id="commit-056"></a>
### 056. refactor: build target `bedrock::bedrock` {#commit-056}

Commit: [9fd538b41ceff741121428c84aeb8a189af1ae96](https://github.com/EndstoneMC/endstone/commit/9fd538b41ceff741121428c84aeb8a189af1ae96) · committed 2025-01-06T19:24:20Z · author Vincent.

Actual parent: `28b1b20117c2601777f40a0cf59533e63b411151`. Full message and parent-relative patch: local source.

Builds static bedrock::bedrock with target-scoped ENTT layout definitions/dependencies and source list; removes Python/Endstone JSON coupling from native layer, places Json conversion in core. SYMCALL begins replacing trampoline calls for call-only wrappers; get_symbol_addr remains declaration and Windows shell. Hook bodies copied to core, pending duplicate cleanup. ItemRegistryManager removes local primary-thread/loaded-level guard in favor native call. RakNet ToString locally uses numeric getnameinfo/address+port, no buffer length; equality checks address/port without explicit other-family check. BlockPatternEvent modeled fields/weak refs replace padding; no ABI execution.18 exact copies87 residuals read.

Changed-file coverage: 105 paths. `CMakeLists.txt`; `cmake/EndstoneHeaders.cmake`; `src/bedrock/CMakeLists.txt`; `src/bedrock/bedrock.h`; `src/bedrock/common_types.h`; `src/bedrock/core/file/path.cpp`; `src/bedrock/core/threading/async.h`; `src/bedrock/deps/json/value.cpp`; `src/bedrock/deps/json/value.h`; `src/bedrock/deps/raknet/raknet_types.cpp`; `src/bedrock/deps/raknet/raknet_types.h`; `src/bedrock/forward.h`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.




<a id="commit-057"></a>
### 057. refactor: build target `endstone::core` {#commit-057}

Commit: [a68b7d54b3b2feffa77f1c89d7889d810c3c6424](https://github.com/EndstoneMC/endstone/commit/a68b7d54b3b2feffa77f1c89d7889d810c3c6424) · committed 2025-01-06T20:15:56Z · author Vincent.

Actual parent: `9fd538b41ceff741121428c84aeb8a189af1ae96`. Full message and parent-relative patch: local source.

Enables core target before root return, reconciles104 exact namespace/include rewrites and67 residual files; splits native methods away from copied hook sources, but Actor::getEndstoneActor0 deletion not restored until66. Native ServerScoreboard factory declaration restored. MaxPlayers200 replaces macro. Permission factory removes lazy option and constructor now recalculates; constructor+factory can recalculate twice and require initialized locator. Runtime hook/cast/symbol infrastructure relocated; old factory allocation macro remains. JSON specialization adds template<> and qualified enum cases. Native constructors/ABI remain incomplete.

Changed-file coverage: 171 paths. `CMakeLists.txt`; `include/endstone/inventory/item_stack.h`; `include/endstone/plugin/plugin.h`; `src/bedrock/CMakeLists.txt`; `src/bedrock/deps/raknet/socket_includes.h`; `src/bedrock/forward.h`; `src/bedrock/locale/i18n.cpp`; `src/bedrock/network/packet.cpp`; `src/endstone/core/hooks/crafting_data_packet.cpp → src/bedrock/network/packet/crafting_data_packet.cpp`; `src/bedrock/network/packet/crafting_data_packet.h`; `src/bedrock/network/server_network_handler.cpp`; `src/bedrock/network/server_network_handler.h`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.




<a id="commit-061"></a>
### 061. feat: implement compilation-time symbol check for ENDSTONE_SYMCALL {#commit-061}

Commit: [b41f450196dbe3592fdd68e496a4923f08d8d3c5](https://github.com/EndstoneMC/endstone/commit/b41f450196dbe3592fdd68e496a4923f08d8d3c5) · committed 2025-01-06T22:59:00Z · author Vincent.

Actual parent: `335687277d563f48baee4ee7386be4ce32d8ad9d`. Full message and parent-relative patch: local source.

Compile-time membership static_assert for ENDSTONE_SYMCALL and macro now returns std::invoke; every caller return updated. Initial constexpr70-entry Windows symbols table, base-address cached then linear lookup. Linux table still absent; this is staged Windows-first work. Root runtime target restored, loader path fixed, hook namespace/error function adjusted. Full meaningful diff read including70 symbol entries; correctness of offsets against actual BDS untested.

Changed-file coverage: 30 paths. `.clang-tidy`; `CMakeLists.txt`; `src/bedrock/locale/i18n.cpp`; `src/bedrock/network/packet.cpp`; `src/bedrock/network/packet/crafting_data_packet.cpp`; `src/bedrock/platform/assigned_thread.cpp`; `src/bedrock/resources/pack.cpp`; `src/bedrock/resources/resource_pack_stack.cpp`; `src/bedrock/server/commands/command.cpp`; `src/bedrock/server/commands/command_origin_loader.cpp`; `src/bedrock/server/commands/command_registry.cpp`; `src/bedrock/server/commands/command_utils.cpp`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-062"></a>
### 062. feat: use compilation-time symbols for hooking targets {#commit-062}

Commit: [08e705bf80e4ac8bee3874e04aa4316f4b5530f0](https://github.com/EndstoneMC/endstone/commit/08e705bf80e4ac8bee3874e04aa4316f4b5530f0) · committed 2025-01-06T23:16:13Z · author Vincent.

Actual parent: `b41f450196dbe3592fdd68e496a4923f08d8d3c5`. Full message and parent-relative patch: local source.

Hook targets now built from same compile-time symbol table via foreach_symbol instead of loading symbols.toml at runtime. Platform detour discovery remains export/ELF based. Debug target logging remains; error_category definition matches declaration. Cached nonempty unordered_map initialization has no synchronization beyond local variable construction, untested.

Changed-file coverage: 4 paths. `src/endstone/runtime/hook.cpp`; `src/endstone/runtime/linux/hook.cpp`; `src/endstone/runtime/symbol.h`; `src/endstone/runtime/windows/hook.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-063"></a>
### 063. refactor: remove unused call in getGameVersionString {#commit-063}

Commit: [6d44e4183058fed4a7f04c32f00e12864be03835](https://github.com/EndstoneMC/endstone/commit/6d44e4183058fed4a7f04c32f00e12864be03835) · committed 2025-01-06T23:19:03Z · author Vincent.

Actual parent: `08e705bf80e4ac8bee3874e04aa4316f4b5530f0`. Full message and parent-relative patch: local source.

Removes discarded has_symbol call in Common::getGameVersionString; macro already owns static_assert membership and return. No additional functional change observed.

Changed-file coverage: 1 paths. `src/bedrock/shared_constants.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-064"></a>
### 064. feat: add symbol generator {#commit-064}

Commit: [86e79dc1e58d55f129c70d6f64bd627d0d71ec82](https://github.com/EndstoneMC/endstone/commit/86e79dc1e58d55f129c70d6f64bd627d0d71ec82) · committed 2025-01-07T16:36:45Z · author Vincent.

Actual parent: `6d44e4183058fed4a7f04c32f00e12864be03835`. Full message and parent-relative patch: local source.

Adds own C++ build-time TOML symbol generator and INTERFACE generated-header target; Bedrock depends on generated symbols. Moves cast/platform helpers to public detail and symbol API into bedrock. Generator chooses compile platform table, emits fixed table.size array with literal symbols, reports parse errors; directory/open errors initially return void then main succeeds (fixed65). Neither generator nor upstream build executed. Original symbols.toml exact move verified. Membership/lookup remain linear and full residual read.

Changed-file coverage: 32 paths. `src/endstone/runtime/cast.h → include/endstone/detail/cast.h`; `src/endstone/core/platform.h → include/endstone/detail/platform.h`; `src/bedrock/CMakeLists.txt`; `src/bedrock/locale/i18n.cpp`; `src/bedrock/network/packet.cpp`; `src/bedrock/network/packet/crafting_data_packet.cpp`; `src/bedrock/network/server_network_handler.cpp`; `src/bedrock/platform/assigned_thread.cpp`; `src/bedrock/resources/pack.cpp`; `src/bedrock/resources/resource_pack_stack.cpp`; `src/bedrock/server/commands/command.cpp`; `src/bedrock/server/commands/command_origin_loader.cpp`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.




<a id="commit-067"></a>
### 067. feat: add ItemRegistry::lookupByName {#commit-067}

Commit: [3f9ff1b6fc6a9a908f24cba37ae1f0c1d3d91d46](https://github.com/EndstoneMC/endstone/commit/3f9ff1b6fc6a9a908f24cba37ae1f0c1d3d91d46) · committed 2025-01-07T20:01:31Z · author Vincent.

Actual parent: `60a39d6ab36eb4c69a7ff2cf5748d5ac3cb95fa2`. Full message and parent-relative patch: local source.

Adds native private ItemRegistry::lookupByName wrapper and Windows offset, friend ItemRegistryRef preserves external access route. SYMCALL diagnostic also includes __FUNCSIG__, later platform repairs needed. Names/aux parsing delegated to native code, no local normalization claims.

Changed-file coverage: 4 paths. `src/bedrock/symbol.h`; `src/bedrock/symbol_generator/symbols.toml`; `src/bedrock/world/item/registry/item_registry.cpp`; `src/bedrock/world/item/registry/item_registry.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-071"></a>
### 071. refactor: move hooks to `endstone::runtime` {#commit-071}

Commit: [6f5a5cf2defd64a579d6a6ccbef50b5d28ddf648](https://github.com/EndstoneMC/endstone/commit/6f5a5cf2defd64a579d6a6ccbef50b5d28ddf648) · committed 2025-01-08T22:02:32Z · author Vincent.

Actual parent: `2b4fa21574fe4a095c2221873d51df6fd1d7919d`. Full message and parent-relative patch: local source.

Moves hooks from core to runtime:19 exact moves17 residuals. Native ServerScoreboard switches artificial factory/name rewriting to real constructor plus BEDROCK_CTOR using decorated ctor name; native ctor expected to install native vtable, local virtual bodies throw unreachable. Destructor base defaults supplied. ItemStackBase integer init reverts to native wrapper, replacing69 local reconstruction; ToString symbol restored. Crash should_report changes true→false unconditionally, suppressing Sentry callback reporting rather than merely refactoring. Member-pointer hook wrapper qualified detail::fp_cast. No execution verifies ABI/lifetime.

Changed-file coverage: 36 paths. `src/bedrock/world/events/scoreboard_event_listener.h → include/endstone/detail/utility.h`; `include/endstone/version.h`; `src/bedrock/symbol.h`; `src/bedrock/symbol_generator/symbols.toml`; `src/bedrock/world/events/event_coordinator.h`; `src/bedrock/world/events/scoreboard_event_listener.h`; `src/bedrock/world/item/item_stack_base.cpp`; `src/bedrock/world/scores/scoreboard.cpp`; `src/bedrock/world/scores/scoreboard.h`; `src/bedrock/world/scores/server_scoreboard.cpp`; `src/bedrock/world/scores/server_scoreboard.h`; `src/endstone/core/CMakeLists.txt`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.




<a id="commit-073"></a>
### 073. fix: remove duplicated definition {#commit-073}

Commit: [e202af151f11d0d9afdb2ce1a5521c935801dcfd](https://github.com/EndstoneMC/endstone/commit/e202af151f11d0d9afdb2ce1a5521c935801dcfd) · committed 2025-01-08T22:59:13Z · author Vincent.

Actual parent: `bf266464caef8346cd934f307f93656dd322f808`. Full message and parent-relative patch: local source.

Deletes duplicated ServerNetworkHandler::updateServerAnnouncement hook body; remaining native SYMCALL implementation supplies actual call. Static migration repair, not removal of announcement updating.

Changed-file coverage: 1 paths. `src/endstone/runtime/bedrock_hooks/server_network_handler.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-080"></a>
### 080. refactor: remove unused headers {#commit-080}

Commit: [3999130e27203483de6ab6a19f41e5a4b504bf7e](https://github.com/EndstoneMC/endstone/commit/3999130e27203483de6ab6a19f41e5a4b504bf7e) · committed 2025-01-09T14:48:47Z · author Vincent.

Actual parent: `391585f17c34d09a1af4330ee39e20610d85d794`. Full message and parent-relative patch: local source.

Unused spdlog includes and blank line removed; inspected changes contain no intended behavior change.

Changed-file coverage: 3 paths. `src/endstone/core/command/command_sender.cpp`; `src/endstone/core/command/server_command_sender.cpp`; `src/endstone/runtime/bedrock_hooks/game_mode.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-081"></a>
### 081. refactor(hook): always use symbols for original function lookup {#commit-081}

Commit: [19db5951f7fd412e6ba21652fe3b6d8d720a8c90](https://github.com/EndstoneMC/endstone/commit/19db5951f7fd412e6ba21652fe3b6d8d720a8c90) · committed 2025-01-09T15:40:54Z · author Vincent.

Actual parent: `3999130e27203483de6ab6a19f41e5a4b504bf7e`. Full message and parent-relative patch: local source.

Original hook dispatch switches detour-pointer/string maps to one EnTT hashed-symbol map; explicit decorated names captured outside lambdas keep original symbol identity. Installs only hooked originals, removes fallback insertion of unhooked native targets (now separate Bedrock call path). Hash collision detection absent in visible emplace path; runtime lookup still hash-based. No benchmark.

Changed-file coverage: 11 paths. `src/endstone/runtime/bedrock_hooks/actor.cpp`; `src/endstone/runtime/bedrock_hooks/game_mode.cpp`; `src/endstone/runtime/bedrock_hooks/level.cpp`; `src/endstone/runtime/bedrock_hooks/mob.cpp`; `src/endstone/runtime/bedrock_hooks/player.cpp`; `src/endstone/runtime/bedrock_hooks/script_level_gameplay_handler.cpp`; `src/endstone/runtime/bedrock_hooks/scripting_event_coordinator.cpp`; `src/endstone/runtime/bedrock_hooks/server_player.cpp`; `src/endstone/runtime/bedrock_hooks/start_game_packet.cpp`; `src/endstone/runtime/hook.cpp`; `src/endstone/runtime/hook.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-082"></a>
### 082. feat: optimise symbol-based calls by consteval offset computation {#commit-082}

Commit: [fd70ddc49222bb40cc6c17ff65d54b766e809a74](https://github.com/EndstoneMC/endstone/commit/fd70ddc49222bb40cc6c17ff65d54b766e809a74) · committed 2025-01-09T17:11:31Z · author Vincent.

Actual parent: `19db5951f7fd412e6ba21652fe3b6d8d720a8c90`. Full message and parent-relative patch: local source.

Consteval get_symbol computes offsets or fails compile-time; BEDROCK_CALL becomes expression without hidden return, all native callers updated accordingly. Constructor helper offset becomes non-type template parameter. Removes runtime linear scan for direct symbol calls while runtime module base remains queried per call until84 caches it. Claim optimization mechanism only; no measured speedup.

Changed-file coverage: 25 paths. `src/bedrock/locale/i18n.cpp`; `src/bedrock/network/packet.cpp`; `src/bedrock/network/packet/crafting_data_packet.cpp`; `src/bedrock/network/server_network_handler.cpp`; `src/bedrock/platform/assigned_thread.cpp`; `src/bedrock/resources/pack.cpp`; `src/bedrock/resources/resource_pack_stack.cpp`; `src/bedrock/server/commands/command.cpp`; `src/bedrock/server/commands/command_origin_loader.cpp`; `src/bedrock/server/commands/command_registry.cpp`; `src/bedrock/server/commands/command_utils.cpp`; `src/bedrock/server/commands/minecraft_commands.cpp`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-083"></a>
### 083. feat: use symbol hash for function lookup in hooked calls {#commit-083}

Commit: [81ac461d1753476b110fae38694cbebe8923cbd6](https://github.com/EndstoneMC/endstone/commit/81ac461d1753476b110fae38694cbebe8923cbd6) · committed 2025-01-09T17:15:14Z · author Vincent.

Actual parent: `fd70ddc49222bb40cc6c17ff65d54b766e809a74`. Full message and parent-relative patch: local source.

Hook lookup macro explicitly uses integral_constant::value for compile-time symbol hash, reduces missing-original diagnostic to generic string; includes symbol.h temporarily (removed85). Clearer constant expression, no new collision checking.

Changed-file coverage: 2 paths. `src/endstone/runtime/hook.cpp`; `src/endstone/runtime/hook.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-084"></a>
### 084. feat: optimise module base retrieval with static initialisation {#commit-084}

Commit: [1bc2bda8a8778e0f979c314f171d2532976588f9](https://github.com/EndstoneMC/endstone/commit/1bc2bda8a8778e0f979c314f171d2532976588f9) · committed 2025-01-09T17:15:34Z · author Vincent.

Actual parent: `81ac461d1753476b110fae38694cbebe8923cbd6`. Full message and parent-relative patch: local source.

Caches module and executable bases in function-local static lambda on both Windows/Linux; pathname helpers still query. Exception on first Windows discovery can retry initialization under C++ semantics; assumes process module base stable for lifetime. No timing measurement.

Changed-file coverage: 2 paths. `src/endstone/core/platform_linux.cpp`; `src/endstone/core/platform_windows.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-086"></a>
### 086. refactor: remove debug logs in `endstone::runtime` {#commit-086}

Commit: [a06201524bda2e9155925d7b4ae48c2ae36b0019](https://github.com/EndstoneMC/endstone/commit/a06201524bda2e9155925d7b4ae48c2ae36b0019) · committed 2025-01-09T18:11:26Z · author Vincent.

Actual parent: `554d8564db4548fb885c76affac9ef4b31169f7c`. Full message and parent-relative patch: local source.

Removes per-detour debug and symbol-enumeration timing logs and unused target lookup in Linux/Windows runtime discovery. No claimed performance measurement; source logging removed.

Changed-file coverage: 2 paths. `src/endstone/runtime/linux.cpp`; `src/endstone/runtime/windows.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-087"></a>
### 087. refactor: remove unused headers {#commit-087}

Commit: [4a7c9627c2cc8b40911025dcc44a8a1f606d13d8](https://github.com/EndstoneMC/endstone/commit/4a7c9627c2cc8b40911025dcc44a8a1f606d13d8) · committed 2025-01-09T18:16:58Z · author Vincent.

Actual parent: `a06201524bda2e9155925d7b4ae48c2ae36b0019`. Full message and parent-relative patch: local source.

Despite unused-headers title, changes remaining hook target/install debug calls to SPDLOG_DEBUG macros (compile-time filtering can differ), besides removing unused headers. No change to mapping/install sequence observed.

Changed-file coverage: 3 paths. `src/endstone/runtime/hook.cpp`; `src/endstone/runtime/linux.cpp`; `src/endstone/runtime/windows.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.
