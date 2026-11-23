<!-- retrieval: {"source_ids":["public:commit:01f1f6a9915c3a959df88b74af9d3f0a337838f5","public:commit:05233c3cff64c459be4e07a9666c6bd6ded8d75f","public:commit:0b8521a4b55422ac6e6a69dacde311a7592b6281","public:commit:0c4044621735c2b104273fe1d553bc4c8c389d35","public:commit:1f43ec3b93afed9ef20dbb660717e715c7d75401","public:commit:2930093f963f9dfe77606c47a0b8fd697a1decfb","public:commit:41d3a21a7884ef97cbf2bb56b0b2eef75efc2939","public:commit:490aa8b5fa03286fdb6d52f062af52a2987816b5","public:commit:4d49536ff46fa4b84c8df6e648135d0ddcd1a4a5","public:commit:58692ee4848ec8690aedb736a85b9efcf6ae5d98","public:commit:6171dc04fc840de555ee3e54ac72fc58ee73ef98","public:commit:6268f6fee9f246f5e7eb2cc9236131cb5bb8a5a2","public:commit:64f6e4490ab5883c32ae8fb963545a6c89cb66fa","public:commit:6562b300e4b2e8d4fcb0408bd44de61c21ced9b7","public:commit:6665adcc63fdbf28138228c29d9d743a2571eee3","public:commit:6e750546515927d7ce55f78f1c985e390c1b1369","public:commit:949e983c7599067cf12fea8d3ca3978135c6cd3f","public:commit:9900ae54d54fbf14ded19963b5b82b6042da9e27","public:commit:b2e09477e834896d4552c31d974b3bcf138b779f","public:commit:cbfc5d64fe59511e9068795ea87754e1133d6626","public:commit:ce4d4f4566e6f08ec9f4086b76ad5118343a53dc","public:commit:d45be8eccc58df568acd81b3786770921e52a68c","public:commit:e4bef17e87851e7802b14e3f93539118f5863a12","public:commit:eea9527982d5198b322fce73f9efcff3c9deb630","public:commit:f943b05b77fe7e0b948dfb07b3446361811195d9","public:commit:fc119ec94f03b817b0ea6da9144efcbd793b2508","public:thread:EndstoneMC/endstone:150","public:thread:EndstoneMC/endstone:180"],"source_type":"public","date":"2025-03-06..2025-05-20","topics":["lifetime","ffi","testing","build","api","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Dynamic command interoperability and explicit grants {#dynamic-command-interoperability-and-explicit-grants}


<a id="stated-problem-and-implemented-direction"></a>
## Stated problem and implemented direction {#stated-problem-and-implemented-direction}

PR180 explicitly targets custom commands registered through the beta Script API, LegacyScriptEngine in the LeviStone downstream project, and issue150's inability to let non-operators execute operator commands through permission attachments. Issue150 reports the limitation on Windows0.6.2.dev38; Wu first acknowledges that the old design cannot express it, then reports the feature implemented in PR180. These are attributed author statements, not independently reproduced compatibility results.

The source direction is coherent: avoid preallocating a snapshot of vanilla wrappers; obtain a native wrapper on demand; keep a shared_ptr alive through dispatch; and retain only custom commands in Endstone's map. Native CommandOrigin is translated to the supported console/player/actor sender types, while the outer hook retains native fallback for unsupported origins. The new wrapper compiles and executes through MinecraftCommands and translates output. Unsupported wrapper-origin conversion still throws; the design does not promise arbitrary senders.

Removing a global registry snapshot/restore is important for coexistence. Restoring one saved global state could erase commands registered later by another system. Targeted cleanup removes Endstone signatures, aliases and enum values while leaving other registrants' state. That coexistence benefit is inferred from the implementation and matches the stated interop goals; there is no cross-loader regression test in this slice.

## Revisions rather than a straight-line design {#revisions-rather-than-a-straight-line-design}

The implementation is deliberately reconstructed through intermediate commits, not only the merged PR patch.622 declares a wrapper before628 implements execution;625 leaves stale preallocation code until627. The alias availability predicate is initially inverted and630 repairs it.633 tries soft enums for plugin parameters and PluginName, then634 returns those uses to hard enums. Soft-enum Add/Replace machinery remains. The record does not state why that experiment was reversed, so neither performance nor client limitations should be invented as the reason.

Targeted unregistration reuses empty enum entries and intentionally exempts Boolean/Block, but634 compares character pointers.647 repairs content comparison with string_view. Constraint cleanup remains a TODO. The native enum pair width briefly moves from32 to64 bits and640 restores32; this affects layout despite a cleanup-style title. Symbol offsets, enum widths and signedness were inspected statically, not validated against a running binary.

Permission handling also changes twice.637 uses a wrapper fallback when no permission node exists.638 registers defaults after world initialization.639 replaces the fallback with lazy node registration, performs the Endstone permission check, and lowers the compiled command's native permission requirement to Any. This is per-command lowering, not global operator promotion.641 filters AvailableCommands per player and fixes the reversed setOp ternary.648 then limits lowering to levels below Host and hides Host-or-higher commands from the advertisement, preserving a native administrative boundary that the first version broadened.

651 addresses external permission changes: wrapper setOp updates immediately, and the server tick polls online players to detect native changes outside the wrapper. The correctness mechanism introduces O(online players) work inside the timed tick. No measurement establishes its cost, and an overhead concern alone does not invalidate the need for synchronization.

## Merge, tests and portability limits {#merge-tests-and-portability-limits}

642 has two parents, its tree equals the second parent's tree, and its second-parent delta is empty. Its first-parent aggregate exactly matches the imported620–641 branch. Full constituent revisions were read; completed PR180 patches are reused only when old/new blobs and every hunk match. The public merge commit and its parents expose the ancestry. A GitHub merge committer is not a separate source author or runtime tester.

No automated command reload, custom-registration coexistence, alias-collision, host-permission or packet-advertisement regression test is added here. The captured PR has no comments/reviews beyond its body. Source demonstrates mechanisms and fixes, while the PR body reports compatibility. This case is useful for extensible registries, permission layering and cross-loader ownership, with native ABI and client behavior still requiring runtime validation.

Discussion context: [PR180](https://github.com/EndstoneMC/endstone/pull/180), [issue150](https://github.com/EndstoneMC/endstone/issues/150). The linked public PR and issue contain inspectable discussion; the historical capture is not distributed and no global thread completion is claimed.

## Per-commit decisions and revisions {#per-commit-decisions-and-revisions}

<a id="commit-620"></a>
### Commit 620 {#commit-620}

[b2e09477e834](https://github.com/EndstoneMC/endstone/commit/b2e09477e834896d4552c31d974b3bcf138b779f) · 2025-05-16T22:23:03Z · chore: add EndstoneCommandMap as a friend class in CommandRegistry

Grants EndstoneCommandMap friendship to native registry, enabling upcoming targeted map/enum cleanup. Duplicate existing friend tolerated, not separate API behavior.


<a id="commit-621"></a>
### Commit 621 {#commit-621}

[2930093f963f](https://github.com/EndstoneMC/endstone/commit/2930093f963f9dfe77606c47a0b8fd697a1decfb) · 2025-05-16T22:48:25Z · refactor: clean up `CommandFlag` structure

CommandFlag clean-up matches completed PR180 exact old/new blobs and complete hunks; preserves bit representation while modernizing structure/operators. Reused semantic patch evidence, own message/context read.


<a id="commit-622"></a>
### Commit 622 {#commit-622}

[6562b300e4b2](https://github.com/EndstoneMC/endstone/commit/6562b300e4b2e8d4fcb0408bd44de61c21ced9b7) · 2025-05-16T22:53:26Z · feat: add MinecraftCommandWrapper

Adds MinecraftCommandWrapper scaffold/build entry: translated native description, per-overload usages and minecraft.command.<name> permission, borrowed const registry. execute declared but not implemented until628; intermediate commit is staged, not standalone completion.


<a id="commit-623"></a>
### Commit 623 {#commit-623}

[e4bef17e8785](https://github.com/EndstoneMC/endstone/commit/e4bef17e87851e7802b14e3f93539118f5863a12) · 2025-05-16T22:53:48Z · refactor: make `CommandRegistry::describe` const

Makes describe(signature,overload) const/nodiscard to support622's borrowed const registry; no logic change.


<a id="commit-624"></a>
### Commit 624 {#commit-624}

[41d3a21a7884](https://github.com/EndstoneMC/endstone/commit/41d3a21a7884ef97cbf2bb56b0b2eef75efc2939) · 2025-05-16T22:54:28Z · refactor: improve `Command` class

Command registration accepts/stores const CommandMap pointer and marks allowChangesFrom nodiscard; identity ownership policy unchanged, supports wrapper registration from const lookup. No tests.


<a id="commit-625"></a>
### Commit 625 {#commit-625}

[6171dc04fc84](https://github.com/EndstoneMC/endstone/commit/6171dc04fc840de555ee3e54ac72fc58ee73ef98) · 2025-05-16T23:06:38Z · refactor: create command wrappers on demand in `CommandMap`

Explicit message: no preallocated vanilla wrappers, generate on demand to handle dynamic registration. getCommand now shared_ptr and dispatch retains it; custom map stores custom commands only and native lookup returns a fresh registered wrapper. Deletes old MinecraftCommand, but leaves obsolete setMinecraftCommands body until627. Alias availability condition accidentally inverted, repaired630. Snapshot restore still present here, removed633.


<a id="commit-626"></a>
### Commit 626 {#commit-626}

[64f6e4490ab5](https://github.com/EndstoneMC/endstone/commit/64f6e4490ab5883c32ae8fb963545a6c89cb66fa) · 2025-05-17T16:26:49Z · refactor: remove unused wrappers

Deletes old CommandWrapper and CommandOutputWithSender/CMake entry. Removes duplicated compile/origin/output forwarding implementation and padding-based sender propagation; new native wrapper628 and adapter627 replace responsibilities, so staged intermediate dependencies must be respected.


<a id="commit-627"></a>
### Commit 627 {#commit-627}

[0b8521a4b554](https://github.com/EndstoneMC/endstone/commit/0b8521a4b55422ac6e6a69dacde311a7592b6281) · 2025-05-17T16:27:16Z · chore: clean up codes

Deletes stale vanilla preallocation/permission registration body; adapter uses native-origin-derived sender with fallback instead of output padding. Player command advertisement/server plugin lookup adapted to shared_ptr. Range lowercase and enum static type cleanup. Exact adapter/output deltas reused fromPR180. Removal of initial permissions is subsequently addressed637–639.


<a id="commit-628"></a>
### Commit 628 {#commit-628}

[6665adcc63fd](https://github.com/EndstoneMC/endstone/commit/6665adcc63fdbf28138228c29d9d743a2571eee3) · 2025-05-17T16:51:48Z · feat: implement `MinecraftCommandWrapper`

Implements native command wrapper: checks Endstone permission, builds native origin for console/player/actor, compiles reconstructed command line, executes and translates output; unsupported origin throws. Uses MinecraftCommands handle rather than const registry. Port of prior wrapper responsibilities, not new proof of arbitrary sender/origin support.


<a id="commit-629"></a>
### Commit 629 {#commit-629}

[d45be8eccc58](https://github.com/EndstoneMC/endstone/commit/d45be8eccc58df568acd81b3786770921e52a68c) · 2025-05-17T16:52:00Z · chore: clean up codes

CommandMap handle becomes MinecraftCommands and accesses registry through it, completing628 construction dependency. Registry snapshot functions still exist here; no standalone novel behavior.


<a id="commit-630"></a>
### Commit 630 {#commit-630}

[58692ee4848e](https://github.com/EndstoneMC/endstone/commit/58692ee4848ec8690aedb736a85b9efcf6ae5d98) · 2025-05-17T17:06:08Z · fix: correct alias handling logic in command registration

Fixes625 alias predicate to reserve only names with no existing command, preventing collision acceptance and rejection of free aliases. No automated regression test added.


<a id="commit-631"></a>
### Commit 631 {#commit-631}

[cbfc5d64fe59](https://github.com/EndstoneMC/endstone/commit/cbfc5d64fe59511e9068795ea87754e1133d6626) · 2025-05-17T20:28:51Z · feat: add `CommandRegistry::setSoftEnumValues`

Adds soft-enum Replace packet path: existing enum only, replaces storage then callback broadcasts native-created packet. Adds concrete SoftEnum/ConstrainedValue layouts; Enum value pairs temporarily32→64bit. No creation on missing key or callback checks; native layout later640 reverts pair width.


<a id="commit-632"></a>
### Commit 632 {#commit-632}

[6e7505465159](https://github.com/EndstoneMC/endstone/commit/6e750546515927d7ce55f78f1c985e390c1b1369) · 2025-05-17T20:45:51Z · feat: add `CommandRegistry::addSoftEnumValues`

Adds soft-enum Add path appending values and broadcasting delta, no deduplication. Moves allocation functor in Overload constructor. APIs retained even when plugin parameter migration634 reverses.


<a id="commit-633"></a>
### Commit 633 {#commit-633}

[9900ae54d54f](https://github.com/EndstoneMC/endstone/commit/9900ae54d54fbf14ded19963b5b82b6042da9e27) · 2025-05-17T21:07:09Z · feat: use soft enum instead of enum for plugin command parameters

Experimental migration: plugin parameters and PluginName use soft enums; removes global native registry snapshot/restore in favor of per-custom-command unregister. Native reload removed through new unregister path. Reuses Boolean/Block hardenum symbols, adds symbol helper declarations/default0. addSoftEnum and unregister are only declared at this stage;634 reverses soft-enum plugin use and implements targeted cleanup. Reason beyond feature title not stated.


<a id="commit-634"></a>
### Commit 634 {#commit-634}

[f943b05b77fe](https://github.com/EndstoneMC/endstone/commit/f943b05b77fe7e0b948dfb07b3446361811195d9) · 2025-05-17T22:51:55Z · feat: implement command unregistration logic

Targeted unregistration clears custom enum values except Boolean/Block, removes aliases from CommandName/CommandAliases and command signature, leaves enum constraints TODO. Reverts633 plugin parameters/PluginName to hard enums and reuses empty enum entries, preserving other registrants rather than restoring a global snapshot. Exemption initially compares const-char pointers to literals, fixed647. Registry lookup widths corrected64→32; Python registry includes completed. No automated reload/cross-loader tests.


<a id="commit-635"></a>
### Commit 635 {#commit-635}

[949e983c7599](https://github.com/EndstoneMC/endstone/commit/949e983c7599067cf12fea8d3ca3978135c6cd3f) · 2025-05-17T22:58:33Z · chore: clean up includes

Converts native-wrapper system-style include to project quoted include and orders it; behavior unchanged.


<a id="commit-636"></a>
### Commit 636 {#commit-636}

[6268f6fee9f2](https://github.com/EndstoneMC/endstone/commit/6268f6fee9f246f5e7eb2cc9236131cb5bb8a5a2) · 2025-05-18T14:46:08Z · feat: add various methods to `CommandRegistry`

Implements native enum/name lookups and exposes map MinecraftCommands handle for player packet filtering. findEnum uses fromEnumValueIndex instead of enum-kind symbol; current subsequent caller strips flags with toIndex, so not by itself a demonstrated bug there. Other helpers declared only; no test.


<a id="commit-637"></a>
### Commit 637 {#commit-637}

[fc119ec94f03](https://github.com/EndstoneMC/endstone/commit/fc119ec94f03b817b0ea6da9144efcbd793b2508) · 2025-05-18T16:31:37Z · feat: improve permission checks in `MinecraftCommandWrapper`

Makes permission tests virtual and permissions protected; native wrapper falls back to native Any versus operator status if none of its permission nodes exists. Stores native permission level. Superseded639 by lazy registration, not lasting permission architecture.


<a id="commit-638"></a>
### Commit 638 {#commit-638}

[eea9527982d5](https://github.com/EndstoneMC/endstone/commit/eea9527982d5198b322fce73f9efcff3c9deb630) · 2025-05-18T16:32:08Z · feat: register permissions for vanilla commands

PostWorld registers core vanilla permissions through DefaultPermissions, with idempotent helper and harmless-command defaults in exact reusedPR180 patch. Separates permission setup from removed vanilla wrapper preallocation.


<a id="commit-639"></a>
### Commit 639 {#commit-639}

[01f1f6a9915c](https://github.com/EndstoneMC/endstone/commit/01f1f6a9915c3a959df88b74af9d3f0a337838f5) · 2025-05-18T17:10:44Z · feat: allow non-op players to run operator commands when explicitly permitted

Explicit nonoperator permission feature: wrapper lazily registers native permission node, checks Endstone grant then lowers compiled command instance permission toAny. Removes637 fallback/virtual APIs, sends unknown-command rather than permission-denied. This initially also lowers host commands, narrowed648; no global operator promotion.


<a id="commit-640"></a>
### Commit 640 {#commit-640}

[4d49536ff46f](https://github.com/EndstoneMC/endstone/commit/4d49536ff46fa4b84c8df6e648135d0ddcd1a4a5) · 2025-05-18T17:17:41Z · chore: clean up codes

Removes obsolete permission_level_ and protected visibility; restores native Enum vector pair width64→32. Despite cleanup title, native layout correction is meaningful; no binary layout validation.


<a id="commit-641"></a>
### Commit 641 {#commit-641}

[490aa8b5fa03](https://github.com/EndstoneMC/endstone/commit/490aa8b5fa03286fdb6d52f062af52a2987816b5) · 2025-05-18T17:59:48Z · feat: remove semantic constraints when sending `AvailableCommandsPacket`

Per-player AvailableCommands filters by Endstone permissions, marks permitted entriesAny and removes matching host/elevated constraints but keeps others such as cheat restrictions. Fixes setOp true→Admin/false→Any reversed ternary. SemanticConstraint underlying uint8_t specified. Later648 excludes host commands from advertisement entirely. Uses registry constraint lookup .at; no packet/native integration test.


<a id="commit-642"></a>
### Commit 642 {#commit-642}

[0c4044621735](https://github.com/EndstoneMC/endstone/commit/0c4044621735c2b104273fe1d553bc4c8c389d35) · 2025-05-18T18:07:18Z · refactor: Command API (#180)

MergePR180 imports620–641, tree identical to second parent and empty second-parent delta. Vincent author/GitHub committer, explicit goals Script API custom-command compatibility, LeviStone LegacyScriptEngine and issue150 explicit non-op permissions. Full imported source chain plus exact completedPR file/hunk evidence reused; no new merge resolution. Claimed compatibility is not independently executed.


<a id="commit-647"></a>
### Commit 647 {#commit-647}

[1f43ec3b93af](https://github.com/EndstoneMC/endstone/commit/1f43ec3b93afed9ef20dbb660717e715c7d75401) · 2025-05-19T23:24:47Z · fix: fix string comparison

Fixes634 Boolean/Block hard-enum exemption from pointer comparison to string_view content comparison, protecting shared enums during custom unregistration. Direct causal repair to priorPR180 boundary, no new test.


<a id="commit-648"></a>
### Commit 648 {#commit-648}

[05233c3cff64](https://github.com/EndstoneMC/endstone/commit/05233c3cff64c459be4e07a9666c6bd6ded8d75f) · 2025-05-19T23:27:37Z · fix: only allow host commands to be executed by the host

Narrows639 escalation: only native permission belowHost is loweredAny; host/owner retains native gate. Player command packet hides allHost-or-higher commands, rendering its previous host-constraint-removal branch unreachable. TODO explicitly says remove after permission refactor. This is policy correction, not a blanket permission bypass.


<a id="commit-651"></a>
### Commit 651 {#commit-651}

[ce4d4f4566e6](https://github.com/EndstoneMC/endstone/commit/ce4d4f4566e6f08ec9f4086b76ad5118343a53dc) · 2025-05-20T00:28:24Z · fix: recalculate permissions when a player's operator status changes

Moves native setPermissions implementation out of runtime hook; Endstone setOp immediately recalculates permissions/commands and tracks last status, while each server tick detects native/external op changes after tick_function. Fixes stale permission cache for changes outside wrapper; adds O(online players) poll and includes it in measured tick duration. Explicit correctness reason, no measured overhead or test.

