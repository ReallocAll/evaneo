<!-- retrieval: {"source_ids":["public:commit:1e68d72e208b85327251903f9e8c380e8dbcd338","public:commit:2c9e13e3f8b4d83a5cce412f52b269da58b57b64","public:commit:4e6c8f30bc5fffb81fdcf4792348c2abadf51b38","public:commit:6ed7faf87c6febe70f007a51f3012f90db376513","public:commit:817e73f6cdae5607b1994a0a11cb20576934c2f2","public:commit:8d02cd762d3f9c62abc36af738319bc129d298f3","public:commit:b1b99131093662c60bc83d7744fbc695f3d48a84","public:commit:c86d6a9f03b2aa04f74ab7a4789c182345c62b41","public:commit:d18292a7e9c2a5fa06d5822cd79180c6a98e728d","public:commit:df24589f4f4c68ed6e27444fc979c5b28eb6d582","public:context-commit:45a5c556142b66c28e87b02b764c10f834a77bd8"],"source_type":"public","date":"2024-11-07..2024-12-22","topics":["lifetime","ffi","testing","build","recovery","diagnosis","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Callback-safe iteration and resource-pack lifecycle {#callback-safe-iteration-and-resource-pack-lifecycle}

## Loading APIs create a reentrancy boundary {#loading-apis-create-a-reentrancy-boundary}

1988 adds loading from a single file or a list of files, delegates ownership to plugin loaders and centralizes manager initialization, names, logger/data-folder setup and onLoad. Python loading gains wheel metadata/install handling and module-cache/local-directory cleanup. Pip's return code is not checked in the changed implementation, dependency/load-before resolution remains TODO, and caught onLoad exceptions are logged while initPlugin returns true after registering the plugin. A registration can therefore exist despite failed initialization.

Calling plugin code while iterating plugin_loaders_ allows onLoad to register another loader and invalidate vector iterators.2019 snapshots raw loader pointers before the directory loop. unique_ptr pointees survive owning-vector reallocation, so this is a targeted solution for append-driven invalidation and intentionally defers newly registered loaders until a later pass. It does not protect loader removal/destruction or promise dependency order. The full2040 manager context also shows loadPlugin(file) still iterates the live loader vector while invoking initPlugin, so the repaired directory path does not establish universal reentrancy safety. clearPlugins destroys loaders; the adjacent completed reload dossier already documents unresolved scheduler/task lifetime limits.

## Packs: composition, recovery and a regression {#packs-composition-recovery-and-a-regression}

1986 replaces the level pack stack using conventional world_resource_packs.json plus zipped packs, instead of treating zipped packs only as an addon stack.1987 repairs the world-file path.2001 accepts JSON comments and catches parsing exceptions;2002 adds exception details to diagnostics. Semantic array/object validation, later push_back/deserialization and null native pack-stack results are outside that parse catch. Missing JSON and no loaded packs can leave null JSON; the native deserialize contract was not independently established.

The1986 cleanup also removes inserting encryption keys into content_keys_.2021 restores that population and2022 moves forwarding keys to the network handler beside resource-pack loading, eliminating reliance on the PostWorld plugin enable phase. Full endpoint context confirms insert does not overwrite existing entries and no stale-key clearing is added. This supports the lifecycle coupling explanation while leaving repeated reload/key-rotation behavior unverified.

## Disconnect forwarding {#disconnect-forwarding}

1958 repairs a separate lifecycle path: an absent Endstone player wrapper previously prevented forwarding native disconnect entirely. The hook now fires the optional event only when a wrapper exists and forwards the native call regardless. It also changes comparison of the quit message to the original translation key, not just control flow. Do not reduce that patch to “always call original” without preserving the message behavior.

## Attribution and limits {#attribution-and-limits}

2020's first-parent feature delta is the collaborator ping-setter patch; second-parent delta is the already-reviewed2019 loader repair. The full collaborator message includes many squashed historical subject lines and coauthor trailers, so titles/trailers alone are not independent change credit. Exact parent-relative equality and separate provenance determine what the merge adds. External PR/issue discussions were not reviewed here. No plugin, subprocess, resource decryption or live disconnect was executed.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-1958"></a>
### Commit 1958 {#commit-1958}

c86d6a9f03b2aa04f74ab7a4789c182345c62b41 · 2024-11-07T16:41:54Z

[fix: display correct disconnect screen for players not on allow list](https://github.com/EndstoneMC/endstone/commit/c86d6a9f03b2aa04f74ab7a4789c182345c62b41)


Previously disconnectClient returned before original call if no EndstonePlayer wrapper, breaking allowlist rejection. New path always forwards native disconnect, conditionally emits cancellable PlayerKickEvent only when wrapper exists. Reason comparison changes from translated kick_message to original key, so untouched translated text may now replace key; native disconnect semantics not tested.

Static review only; no upstream execution.

<a id="commit-1986"></a>
### Commit 1986 {#commit-1986}

d18292a7e9c2a5fa06d5822cd79180c6a98e728d · 2024-12-02T18:25:15Z

[feat: improve logic for loading zipped resource packs](https://github.com/EndstoneMC/endstone/commit/d18292a7e9c2a5fa06d5822cd79180c6a98e728d)


Moves zipped-pack append into explicit loadResourcePacks, loads existing world pack JSON first and replaces LEVEL stack rather than unused ADDON stack, logs resolved manifests/encryption flag. Initial path uses resource-pack directory, corrected1987. Removes content_keys_ insertion along with old logging, causing encrypted-key registration regression restored2021/2022. JSON load lacks exception handling until2001.

Static review only; no upstream execution.

<a id="commit-1987"></a>
### Commit 1987 {#commit-1987}

817e73f6cdae5607b1994a0a11cb20576934c2f2 · 2024-12-02T19:07:40Z

[fix: correct path to `world_resource_packs.json`](https://github.com/EndstoneMC/endstone/commit/817e73f6cdae5607b1994a0a11cb20576934c2f2)


Uses current_path/worlds/level_id/world_resource_packs.json rather than resource pack repository path, preserving append order and LEVEL replacement.

Static review only; no upstream execution.

<a id="commit-1988"></a>
### Commit 1988 {#commit-1988}

2c9e13e3f8b4d83a5cce412f52b269da58b57b64 · 2024-12-03T14:49:55Z

[feat: add PluginManager::loadPlugin to load plugins from a single file](https://github.com/EndstoneMC/endstone/commit/2c9e13e3f8b4d83a5cce412f52b269da58b57b64)


Adds single-file and file-vector loading across manager/loader/Python APIs, centralizes directory scanning and initPlugin validation/registration/onLoad. C++ loader now owns instances immediately; manager returns borrowed pointers. Python moves module invalidation/.local cleanup into constructor, installs one wheel via pkginfo/distribution entry points, retains global installed discovery once. pip return code remains unchecked; duplicate-name/dependency ordering unresolved. onLoad now executes during iteration and can register loaders, introducing iterator invalidation repaired2019. Exception catches log but initPlugin still reports true; no plugin execution performed.

Static review only; no upstream execution.

<a id="commit-2001"></a>
### Commit 2001 {#commit-2001}

4e6c8f30bc5fffb81fdcf4792348c2abadf51b38 · 2024-12-05T17:08:50Z

[fix: prevent server crash when comments are present in `world_resource_packs.json`](https://github.com/EndstoneMC/endstone/commit/4e6c8f30bc5fffb81fdcf4792348c2abadf51b38)


Parses world_resource_packs.json with comment support and catches parse exceptions instead of letting them escape. Logging initially omits what(); malformed semantic entries and later deserialize remain outside this catch.

Static review only; no upstream execution.

<a id="commit-2002"></a>
### Commit 2002 {#commit-2002}

1e68d72e208b85327251903f9e8c380e8dbcd338 · 2024-12-05T17:23:40Z

[feat: improve error logging to include exception details when JSON loading fails](https://github.com/EndstoneMC/endstone/commit/1e68d72e208b85327251903f9e8c380e8dbcd338)


Adds exception what() to resource-pack JSON load error, making2001 recovery observable; no additional recovery branch.

Static review only; no upstream execution.

<a id="commit-2019"></a>
### Commit 2019 {#commit-2019}

6ed7faf87c6febe70f007a51f3012f90db376513 · 2024-12-20T12:41:41Z

[fix: potential iterator invalidation during plugin loading](https://github.com/EndstoneMC/endstone/commit/6ed7faf87c6febe70f007a51f3012f90db376513)


Snapshots raw PluginLoader pointers before invoking load/onLoad, avoiding iterator invalidation when callbacks register new unique-owned loaders. Existing pointees remain stable on vector reallocation; newly registered loaders intentionally deferred to later pass. Does not implement dependency ordering or protect removal/destruction.

Static review only; no upstream execution.

<a id="commit-2020"></a>

### Commit 2020 {#commit-2020}

8d02cd762d3f9c62abc36af738319bc129d298f3 · 2024-12-20T12:41:48Z

[Merge remote-tracking branch 'origin/main'](https://github.com/EndstoneMC/endstone/commit/8d02cd762d3f9c62abc36af738319bc129d298f3)


The first-parent delta imports the writable ping GUID/IPv4/IPv6-port API and Python surfaces; the second-parent delta repeats the 2019 loader snapshot fix. The ping API originated with the contributor whose change this merge imports.

Static review only; no upstream execution.

<a id="commit-2021"></a>
### Commit 2021 {#commit-2021}

df24589f4f4c68ed6e27444fc979c5b28eb6d582 · 2024-12-20T17:11:38Z

[fix: encrypted resource packs now work again](https://github.com/EndstoneMC/endstone/commit/df24589f4f4c68ed6e27444fc979c5b28eb6d582)


Restores nonempty encrypted pack keys into content_keys_ during source loading, deleted in1986. Existing PostWorld transfer then works by source inspection; commit claim encrypted packs work again is not executed evidence.

Static review only; no upstream execution.

<a id="commit-2022"></a>
### Commit 2022 {#commit-2022}

b1b99131093662c60bc83d7744fbc695f3d48a84 · 2024-12-22T15:04:21Z

[refactor: move content key handling to resource pack loading process](https://github.com/EndstoneMC/endstone/commit/b1b99131093662c60bc83d7744fbc695f3d48a84)


Moves content-key transfer to EndstoneLevel::loadResourcePacks alongside stack deserialization, removing PostWorld plugin-phase coupling; network insert remains non-overwriting and no stale-key clear is added.

Static review only; no upstream execution.
