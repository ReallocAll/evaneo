<!-- retrieval: {"source_ids":["public:commit:034e9dcb79dfd14cd39383dfbf1e6aebb7f2245d","public:commit:0a691ab693ebc7f067f3e20b3266fdb44a50c10a","public:commit:0b834bcaa4acdf0951c9a1d299d6a4012fa7a7c5","public:commit:119c1266100033a7dc314035c6cbd675ac83a7a8","public:commit:1e10e945c81e308d0cc0c1ffef2749e2ca7b016d","public:commit:1e9318416364a1f2676c5cba76c61cd16e81a445","public:commit:2ee05a34131d0222c54346ef86df0aaf0fc5572b","public:commit:393e0ce837ea283dd260446db6893c28088f20a6","public:commit:46d2a272797f0b1145f8aa65ac134752ad6242c0","public:commit:486964de6b0c56ff8b06d578c81326d0dc7795bd","public:commit:52444acbf49f67028498c1315f03df8188791203","public:commit:5bb6318ad25aff1fff45bad0ae9cac7a788b34fc","public:commit:61ac85b6780ba234e19da11971abcdff77bab572","public:commit:638df789fe0769a3e03eabae7d2702f510971c42","public:commit:6869bc45082dfb8e64a2a5569d53aa6437fcb91c","public:commit:71abaa37aa5e727cfc236ef59d2269b7c952139a","public:commit:7b6ebf72d9940e7dd1c4a42ac28849a0a393aaed","public:commit:7c662b6efec7c1ea87bac4baca214fb90110dafb","public:commit:9da18b12db3ceeb1d8e52e645f7ca3a423331da2","public:commit:a9c54a84c4410b991091426d9744eb82efcb2e30","public:commit:b16ad112bacec82b5adc046acf6cc8c4d41d519c","public:commit:b4b02028ec4db00f3d23c2d036c6a3675419d9d6","public:commit:bdda06e5991f9dcf0139d671139ce13a45460f07","public:commit:c8690ba06ef637b03e86453f23be49da0240dc84","public:commit:d1f6e566ee8a2e81dd29f35a2af2c4ce5f59c9a8","public:commit:f65a4c204a6143c5cd54c7dbfbd8f8215732eaf8","public:commit:faabbe25416df7c7061ded2e926e3eb7d9912992"],"source_type":"public","date":"2024-05-18..2024-06-04","topics":["lifetime","ffi","testing","build","performance","api","diagnosis","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Command execution: ownership repair, three origin strategies and a revised permission boundary {#command-execution-ownership-repair-three-origin-strategies-and-a-revised-permission-boundary}

## The causal problem is larger than a command method {#the-causal-problem-is-larger-than-a-command-method}

This sequence begins with a concrete ownership defect in the previously reviewed ordinal960: a retained unique_ptr and a new CommandContext both own the same origin pointer. [966](#commit-966) removes the retained owner and constructs a fresh origin per call. This bounds the earlier defect to the historical interval; it must not be carried into later snapshots as if it were still present. It also separates memory ownership from semantic origin correctness. A safely owned object can still have the wrong position, entity, permissions or clone behavior for native command execution.

Three implemented alternatives are visible, rather than a hypothetical list of design options. First,965–966 use a locally implemented PluginCommandOrigin: generic Plugin identity, zero positions, no entity and elevated capabilities. Second,972–977 restore the native factory and wrap its player-derived origin in a decorator. Third,978 and the local NBT work make a native loader available, and996–998 remove the decorator in favor of loading a Virtual origin with GameDirectorEntityServer records. No PR discussion in this unit explains a comprehensive up-front design. The record supports iterative correction of concrete native-command behavior, not a claim that the final representation was the original plan.

## Why the decorator was insufficient as first written {#why-the-decorator-was-insufficient-as-first-written}

The player adapter in975 retains native player UUID, network/subclient identity, Level and positional behavior while overriding capability queries. However, native code can clone an origin. The initial generic forwarding clone returns the underlying implementation's clone, losing the adapter overrides.977 explicitly names /function permission behavior and repairs both clone methods to preserve the adapter type. This is a useful transferable case: a decorator's behavioral contract includes operations that manufacture another instance, not just ordinary getters. The observed repair does not prove serialization is complete; its adapter still throws for serialize.

The next replacement explicitly claims /execute support in997. Instead of manually implementing every origin virtual function, Endstone constructs a CompoundTag with Virtual outer type, Origin and OutputReceiver records keyed by actor unique ID, and command version38, then asks the host loader for an owned native origin. The nested CommandPosition is initially included and removed in998. It is fair to infer that the representation is being narrowed to what the host loader needs. It is not fair to invent the author's reason for the removal or assert all coordinate semantics were tested. The source message reports that /execute works; this review performs no native execution.

## Reuse becomes a public server operation {#reuse-becomes-a-public-server-operation}

1074–1077 centralize conversion and dispatch. asConsole and asPlayer identify the implemented sender categories; fromEndstone builds an Owner-level dedicated-server origin for console, using overworld and the first Level, or the Virtual/GameDirector record for a player. Server::dispatchCommand owns the common path and Player::performCommand delegates. Python exposes the same method rather than implementing a second execution engine. This reduces duplicated construction, while leaving concrete host assumptions: at least one Level exists, the Endstone sender is the expected concrete type, and a supported conversion returns a native origin. Unsupported custom senders return null, but CommandContext::getOrigin dereferences its pointer. The public signature is broader than the safely implemented cases in this snapshot.

The changelog's 'temporarily operator' wording in999 is intent shorthand. The code creates an elevated command origin; it does not temporarily call setOp on the player and restore it. Persistent player privilege state, the permission system's view of a sender, and native origin authority must remain separate concepts. No claim about a user's account permissions follows from this source.

## Permission enforcement is revised after a compatibility regression {#permission-enforcement-is-revised-after-a-compatibility-regression}

1067 assigns vanilla wrappers minecraft.commands.<canonical-name>.1070 adds a centralized native executeCommand gate requiring a command-map entry, a mapped Endstone sender and permission.1071 moves the gate before events and changes silent denial into a user message; unavailable advertised commands also become Internal as well as hidden. These are two distinct controls: client command visibility and execution-time checking. The early gate rejects Virtual origins because toEndstone only maps Player and DedicatedServer. That directly conflicts with the new performCommand representation.

1078 explicitly says performCommand works again. It allows unmapped origins through to the native engine, applying Endstone permission checks/events only when a sender maps. It also separates denied-permission and event-cancelled result codes.1080 registers aliases to the same shared BedrockCommand and lets unknown map names fall through as well. Final full-file context confirms the condition is `command && sender`: only that intersection gets the additional Endstone permission/event layer. Native execution still runs afterward for other cases. This is a bounded compatibility decision visible in the code, not evidence that all native validation disappears or that permissive fallback is a general design preference.

Alias repair is a second boundary lesson. The wrapper's command map must represent aliases consistently if it is used as an execution gate. Making native aliases share the canonical command object also shares its permission identity. No independent alias permission strings are added. Unknown-name fallthrough reduces reliance on a complete wrapper map, at the cost of the wrapper's checks/events no longer being universal. Existing command parsing strips a leading slash and splits on the first space; no new tokenizer or whitespace normalization is introduced.

## Evidence, tests and applicability {#evidence-tests-and-applicability}

All relevant parent-relative diffs and final origin, command context, adapter, wrapper map, public command and permission-base files were read. Changed tests update mocks and namespaces for new abstract APIs; they are not dispatch, clone, /execute or alias regression tests. No runtime tests, native calls, benchmark or upstream code were executed. issue14 is merely referenced elsewhere; no unseen review objection is invented here. Useful retrieval cases: fixing ownership while preserving host identity, decorator clone semantics, serialization as a native factory bridge, diagnosing a permission gate that rejects internally generated origins, and separating client visibility from actual execution policy. The chronology and final snapshot matter more than a slogan about either security or convenience.


## Individual commit dispositions {#individual-commit-dispositions}


<a id="commit-961"></a>
### 961: chore(deps): add jsoncpp/1.9.5 {#commit-961}

Source: [0a691ab693ebc7f067f3e20b3266fdb44a50c10a](https://github.com/EndstoneMC/endstone/commit/0a691ab693ebc7f067f3e20b3266fdb44a50c10a). Authored 2024-05-18T23:21:36Z; Git author Vincent. Disposition: dependency.

Adds jsoncpp/1.9.5 to Conan and links jsoncpp into the core CMake dependency set. This supplies the concrete Json::Value type used by the command-origin output callback in964. Dependency selection rationale and comparative evaluation are not stated; no library code was executed or independently reviewed.


<a id="commit-962"></a>
### 962: feat: add BlockPos and Vec3::ZERO {#commit-962}

Source: [61ac85b6780ba234e19da11971abcdff77bab572](https://github.com/EndstoneMC/endstone/commit/61ac85b6780ba234e19da11971abcdff77bab572). Authored 2024-05-18T23:21:52Z; Git author Vincent. Disposition: implementation.

Adds integer BlockPos coordinates and shared ZERO constants for BlockPos/Vec3, supporting the position methods of the proposed PluginCommandOrigin. This is a small native representation prerequisite, not a measured optimization.


<a id="commit-964"></a>
### 964: refactor: update CommandOrigin function signature {#commit-964}

Source: [b16ad112bacec82b5adc046acf6cc8c4d41d519c](https://github.com/EndstoneMC/endstone/commit/b16ad112bacec82b5adc046acf6cc8c4d41d519c). Authored 2024-05-18T23:24:55Z; Git author Vincent. Disposition: abi_correction.

Changes the output callback from an opaque void pointer to Json::Value&&, removes the earlier host fromCommandOriginData declaration and exposes UUID to subclasses. This prepares the custom origin route. Its removal is temporary:972 restores the host factory, before996 removes that route again.


<a id="commit-965"></a>
### 965: feat: add PluginCommandOrigin for Player::performCommand {#commit-965}

Source: [a9c54a84c4410b991091426d9744eb82efcb2e30](https://github.com/EndstoneMC/endstone/commit/a9c54a84c4410b991091426d9744eb82efcb2e30). Authored 2024-05-18T23:29:31Z; Git author Vincent. Disposition: implementation.

Introduces a complete PluginCommandOrigin subclass borrowing native Level/Dimension. It identifies as Plugin/Virtual, grants GameDirectors and permissive chat/tell/selector/cheat capabilities, returns zero position and no entity, clones a fresh wrapper, and leaves serialization throwing Not implemented. The native factory implementation is deleted. This is an elevated generic origin, not yet a player-faithful origin and not wired into performCommand until966.


<a id="commit-966"></a>
### 966: fix: Player::performCommand {#commit-966}

Source: [7c662b6efec7c1ea87bac4baca214fb90110dafb](https://github.com/EndstoneMC/endstone/commit/7c662b6efec7c1ea87bac4baca214fb90110dafb). Authored 2024-05-18T23:32:50Z; Git author Vincent. Disposition: corrective_revision.

Removes the player’s retained command_origin_ and constructs a fresh unique PluginCommandOrigin for each CommandContext. This eliminates960’s two unique_ptr owners of the same raw origin; init retains only the network handler. The fix is source-proven ownership correction, with no crash reproduction here. The resulting zero-position/generic-origin behavior is replaced by later player-aware approaches.


<a id="commit-972"></a>
### 972: feat: re-add CommandOrigin::fromCommandOriginData {#commit-972}

Source: [46d2a272797f0b1145f8aa65ac134752ad6242c0](https://github.com/EndstoneMC/endstone/commit/46d2a272797f0b1145f8aa65ac134752ad6242c0). Authored 2024-05-19T04:04:23Z; Git author Vincent. Disposition: alternative_restored.

Restores the native fromCommandOriginData factory implementation deleted965, changes execute-position return qualification and makes setUUID public while reformatting virtual declarations. This restores a previously read source blob and chooses another origin construction path, rather than progressing only toward the generic PluginCommandOrigin.


<a id="commit-974"></a>
### 974: feat: add CommandOriginAdapter {#commit-974}

Source: [faabbe25416df7c7061ded2e926e3eb7d9912992](https://github.com/EndstoneMC/endstone/commit/faabbe25416df7c7061ded2e926e3eb7d9912992). Authored 2024-05-19T04:05:22Z; Git author Vincent. Disposition: alternative_implementation.

Replaces the PluginCommandOrigin header with CommandOriginAdapter holding an owned native origin. Its virtual methods forward to that implementation except serialization, which still throws. Its initial clone returns the underlying clone, losing adapter behavior. The old implementation file survives until975, so the transition is not a single self-contained rename.


<a id="commit-975"></a>
### 975: feat: Player::performCommand now executes commands at higher permission level {#commit-975}

Source: [71abaa37aa5e727cfc236ef59d2269b7c952139a](https://github.com/EndstoneMC/endstone/commit/71abaa37aa5e727cfc236ef59d2269b7c952139a). Authored 2024-05-19T04:06:32Z; Git author Vincent. Disposition: behavioral_revision.

Deletes the generic origin implementation and adds PlayerCommandOriginAdapter around a native player-derived origin built with UUID/network/subclient/Level information. It preserves native player position/entity behavior while overriding command capabilities to elevated values. performCommand switches to this adapter and passes true for the later-named suppress_output flag. It does not toggle the player’s persistent operator state.


<a id="commit-976"></a>
### 976: feat: add python bindings for Player::performCommand {#commit-976}

Source: [638df789fe0769a3e03eabae7d2702f510971c42](https://github.com/EndstoneMC/endstone/commit/638df789fe0769a3e03eabae7d2702f510971c42). Authored 2024-05-19T04:10:06Z; Git author Vincent. Disposition: python_api.

Exposes Player.perform_command and updates the stub. The Python surface follows the current elevated-origin C++ behavior; it adds no separate Python-side permission or lifetime policy.


<a id="commit-977"></a>
### 977: fix: permission issues when run `/function` with `Player::performCommand` {#commit-977}

Source: [5bb6318ad25aff1fff45bad0ae9cac7a788b34fc](https://github.com/EndstoneMC/endstone/commit/5bb6318ad25aff1fff45bad0ae9cac7a788b34fc). Authored 2024-05-20T12:43:57Z; Git author Vincent. Disposition: corrective_revision.

Explicitly fixes /function permission behavior by making both base and player adapter clones preserve their wrapper class. This is concrete evidence that clone must retain behavioral overrides;975’s wrapper was insufficient when native execution cloned its origin. No generic ban on delegation follows.


<a id="commit-978"></a>
### 978: feat: add CommandOriginLoader {#commit-978}

Source: [c8690ba06ef637b03e86453f23be49da0240dc84](https://github.com/EndstoneMC/endstone/commit/c8690ba06ef637b03e86453f23be49da0240dc84). Authored 2024-05-20T14:25:10Z; Git author Vincent. Disposition: alternative_prerequisite.

Adds CommandOriginLoader::load taking CompoundTag and ServerLevel, with platform-aware native return-value handling. This is the third construction route, later wired by997. The mere presence of a loader declaration does not mean all NBT serialization operations are implemented.


<a id="commit-993"></a>
### 993: feat: add CommandPosition {#commit-993}

Source: [1e10e945c81e308d0cc0c1ffef2749e2ca7b016d](https://github.com/EndstoneMC/endstone/commit/1e10e945c81e308d0cc0c1ffef2749e2ca7b016d). Authored 2024-05-21T01:59:53Z; Git author Vincent. Disposition: nbt_bridge.

Adds CommandPosition serialization of offsets, relative flags and local flag into CompoundTag. Ordinary default construction leaves some members without explicit initialization;997 uses this path and998 removes that nested position tag. The later removal’s reason is not stated, so avoiding uninitialized data is a possible effect rather than an asserted author motive.


<a id="commit-994"></a>
### 994: feat: add Actor::getOrCreateUniqueID {#commit-994}

Source: [6869bc45082dfb8e64a2a5569d53aa6437fcb91c](https://github.com/EndstoneMC/endstone/commit/6869bc45082dfb8e64a2a5569d53aa6437fcb91c). Authored 2024-05-21T02:00:21Z; Git author Vincent. Disposition: native_identity.

Adds a not-null persistent-component accessor and Actor::getOrCreateUniqueID for command-origin serialization. It returns an existing non-sentinel ID or asks the Level for a new one and uses getOrAddComponent. The final getOrAdd wrapper uses EnTT get_or_emplace, so a pre-existing sentinel component is not explicitly overwritten here. Host invariants and observed failure are unknown.


<a id="commit-996"></a>
### 996: refactor: clean up CommandOrigin {#commit-996}

Source: [bdda06e5991f9dcf0139d671139ce13a45460f07](https://github.com/EndstoneMC/endstone/commit/bdda06e5991f9dcf0139d671139ce13a45460f07). Authored 2024-05-21T02:01:13Z; Git author Vincent. Disposition: alternative_removed.

Deletes CommandOriginAdapter and the restored native factory implementation. The next commit replaces remaining player use with CommandOriginLoader, so this is a staging point in an observed alternative replacement, not an unexplained cleanup or proof the intermediate tree builds.


<a id="commit-997"></a>
### 997: refactor: Player::performCommand is reimplemented, now works with `/execute` command {#commit-997}

Source: [9da18b12db3ceeb1d8e52e645f7ca3a423331da2](https://github.com/EndstoneMC/endstone/commit/9da18b12db3ceeb1d8e52e645f7ca3a423331da2). Authored 2024-05-21T02:29:49Z; Git author Vincent. Disposition: behavioral_revision.

The explicit claim is that /execute now works with performCommand. Player execution constructs a Virtual origin containing GameDirectorEntityServer origin/output receiver records with the actor’s unique ID, version38 and initially a serialized CommandPosition, then loads it through the native loader and moves ownership into CommandContext. Adds inline to local compound put methods. This replaces the decorator approach; the message reports success but no native execution was performed here.


<a id="commit-998"></a>
### 998: refactor: simplify Player::performCommand {#commit-998}

Source: [d1f6e566ee8a2e81dd29f35a2af2c4ce5f59c9a8](https://github.com/EndstoneMC/endstone/commit/d1f6e566ee8a2e81dd29f35a2af2c4ce5f59c9a8). Authored 2024-05-21T02:58:47Z; Git author Vincent. Disposition: behavioral_revision.

Removes the nested CommandPosition from performCommand’s NBT. Native loader defaults now determine that aspect instead of locally serialized default fields. The patch is small but changes construction semantics; no explicit rationale or test explains why this representation is sufficient.


<a id="commit-1067"></a>
### 1067: feat: add permissions for vanilla commands {#commit-1067}

Source: [0b834bcaa4acdf0951c9a1d299d6a4012fa7a7c5](https://github.com/EndstoneMC/endstone/commit/0b834bcaa4acdf0951c9a1d299d6a4012fa7a7c5). Authored 2024-06-03T06:20:55Z; Git author Vincent. Disposition: permission_model.

Adds a BedrockCommand constructor that assigns minecraft.commands.<canonical-name> permissions, overriding any passed permission vector after base construction. This equips native command wrappers for Endstone permission checks. It does not yet enforce those checks in native dispatch;1070 does that.


<a id="commit-1068"></a>
### 1068: feat: improve error logging in PermissibleBase::addAttachment {#commit-1068}

Source: [b4b02028ec4db00f3d23c2d036c6a3675419d9d6](https://github.com/EndstoneMC/endstone/commit/b4b02028ec4db00f3d23c2d036c6a3675419d9d6). Authored 2024-06-03T06:21:17Z; Git author Vincent. Disposition: lifecycle_guard.

Rejects permission attachments from disabled plugins with a specific log and null return; the name/value overload now checks null before updating/recalculating. This is a lifecycle validity rule and null-dereference prevention, not merely improved error wording. No lifecycle test is added.


<a id="commit-1069"></a>
### 1069: feat(command): add "entity" type {#commit-1069}

Source: [f65a4c204a6143c5cd54c7dbfbd8f8215732eaf8](https://github.com/EndstoneMC/endstone/commit/f65a4c204a6143c5cd54c7dbfbd8f8215732eaf8). Authored 2024-06-03T06:25:04Z; Git author Vincent. Disposition: api_alias.

Adds entity as another command-usage alias for the existing Selection symbol alongside actor/player/target. This broadens accepted vocabulary without a new parser implementation.


<a id="commit-1070"></a>
### 1070: feat(command): add permission test in MinecraftCommands::executeCommand {#commit-1070}

Source: [034e9dcb79dfd14cd39383dfbf1e6aebb7f2245d](https://github.com/EndstoneMC/endstone/commit/034e9dcb79dfd14cd39383dfbf1e6aebb7f2245d). Authored 2024-06-03T07:36:11Z; Git author Vincent. Disposition: permission_gate.

Centralizes origin-to-sender conversion for Player/DedicatedServer, rewires CommandAdapter and adds native executeCommand permission checks. Unknown command, unmapped origin or denied permission all return CommandNotFound; cancellation now also uses that code. This rejects Virtual origins used by performCommand, and the old player-entity type check is removed. Later1078/1080 revise these boundaries; do not report this transient strict gate as final policy.


<a id="commit-1071"></a>
### 1071: feat(command): improve permission checking {#commit-1071}

Source: [119c1266100033a7dc314035c6cbd675ac83a7a8](https://github.com/EndstoneMC/endstone/commit/119c1266100033a7dc314035c6cbd675ac83a7a8). Authored 2024-06-03T08:16:24Z; Git author Vincent. Disposition: permission_revision.

Moves permission checking before events and uses testPermission with a user-facing denial instead of the silent check. Unauthorized advertised commands also receive Internal permission in addition to hidden flags. Runtime rejection and client visibility are separate mechanisms; the Virtual-origin rejection remains until1078.


<a id="commit-1074"></a>
### 1074: feat: add CommandSender::asConsole {#commit-1074}

Source: [2ee05a34131d0222c54346ef86df0aaf0fc5572b](https://github.com/EndstoneMC/endstone/commit/2ee05a34131d0222c54346ef86df0aaf0fc5572b). Authored 2024-06-03T16:30:06Z; Git author Vincent. Disposition: conversion_prerequisite.

Adds virtual CommandSender::asConsole with null default and a concrete console override, plus EndstonePlayer’s native getHandle accessor. This prepares conversion from supported public sender types to native origins. Custom senders still return null unless they implement the supported casts.


<a id="commit-1075"></a>
### 1075: feat: add CommandOrigin::fromEndstone {#commit-1075}

Source: [486964de6b0c56ff8b06d578c81326d0dc7795bd](https://github.com/EndstoneMC/endstone/commit/486964de6b0c56ff8b06d578c81326d0dc7795bd). Authored 2024-06-03T16:58:49Z; Git author Vincent. Disposition: conversion_implementation.

Adds fromEndstone: console loads a DedicatedServer NBT origin with Owner permission, zero request ID and overworld using the first Level; players load the prior Virtual/GameDirector entity record; unsupported senders return null. Level’s native accessor becomes getHandle. These are explicit host assumptions, and the public dispatch added next does not validate a null conversion.


<a id="commit-1076"></a>
### 1076: feat: add Server::dispatchCommand {#commit-1076}

Source: [7b6ebf72d9940e7dd1c4a42ac28849a0a393aaed](https://github.com/EndstoneMC/endstone/commit/7b6ebf72d9940e7dd1c4a42ac28849a0a393aaed). Authored 2024-06-03T17:09:57Z; Git author Vincent. Disposition: public_dispatch.

Adds Server::dispatchCommand, routes Player::performCommand through it and updates mocks/scheduler test namespaces. A fresh loaded origin is moved into CommandContext and executeCommand is called with suppressed output. Context::getOrigin dereferences its pointer, so unsupported custom senders remain outside the safe implemented contract. Mock compilation updates are not behavioral dispatch tests.


<a id="commit-1077"></a>
### 1077: feat: add python bindings for Server::dispatchCommand {#commit-1077}

Source: [52444acbf49f67028498c1315f03df8188791203](https://github.com/EndstoneMC/endstone/commit/52444acbf49f67028498c1315f03df8188791203). Authored 2024-06-03T17:14:12Z; Git author Vincent. Disposition: python_api.

Adds Python dispatch_command and stubs, renames the argument consistently and catches the lava docstring correction in the stub. The Python method inherits the supported-sender constraints and native permission/origin behavior; it adds no independent validation.


<a id="commit-1078"></a>
### 1078: fix: Player::performCommand now works again {#commit-1078}

Source: [393e0ce837ea283dd260446db6893c28088f20a6](https://github.com/EndstoneMC/endstone/commit/393e0ce837ea283dd260446db6893c28088f20a6). Authored 2024-06-04T02:07:27Z; Git author Vincent. Disposition: corrective_boundary_revision.

Explicitly restores performCommand by allowing unmapped native origins through instead of rejecting null toEndstone. Known command lookup remains required at this stage. Permission checks/events run only for mapped senders; denied and cancelled results regain distinct codes. Virtual-origin execution therefore skips this Endstone permission/event layer and relies on native origin behavior. This is an observed compatibility tradeoff, not proof of a universal security policy.


<a id="commit-1080"></a>
### 1080: fix: aliases of vanilla commands can now be executed {#commit-1080}

Source: [1e9318416364a1f2676c5cba76c61cd16e81a445](https://github.com/EndstoneMC/endstone/commit/1e9318416364a1f2676c5cba76c61cd16e81a445). Authored 2024-06-04T05:27:26Z; Git author Vincent. Disposition: corrective_boundary_revision.

Registers vanilla aliases against the same shared BedrockCommand and removes unconditional rejection when the Endstone map lacks a command. Permission checks and player/console events now run only if both command and sender map; other cases fall through to native execution. This repairs alias availability and reduces wrapper/native-map disagreement costs, while making Endstone checking deliberately partial at this snapshot. No claim of bypassing native validation or present-day behavior is made.
