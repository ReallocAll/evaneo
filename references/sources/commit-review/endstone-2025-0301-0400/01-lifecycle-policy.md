<!-- retrieval: {"source_ids":["public:commit:008a528a4a82f9c01f9020ec9bcd285af9699aa4","public:commit:064027b78b1e30e33c1526cf1890b96a61eb3bd6","public:commit:0b6684a726c5b8848af2c7f3bd5747910e777753","public:commit:2dad431c1c60a372a868ed0689724a942cbef396","public:commit:2e43ba5e0b270ca670e307595aff4312ab42559f","public:commit:425e1e9c6ec06a447b38bc7388a45f3d27130106","public:commit:42da234f10576a5c86257e84a50f6cfa0bf64f30","public:commit:56e75c49246d640d336b23d7a2b8e7f760222f7d","public:commit:6306522a119352c80aef438be3137d684c2916fb","public:commit:800ab564a63b39b7ce3366c41a2f068aac4a6242","public:commit:88928db918e44941a0bf71741bd3448721fbbc80","public:commit:9232f9c39d203ff8d0a480d4ad825f31fad9152c","public:commit:bfdc73067bce1d5bad7dd460fb4110fae50b046f","public:commit:c0bc94917fb260b493304de23e41e480941a7f35","public:commit:d7cda5bb2c01f84c3cc37abeaa076a200cd6d4e5","public:commit:e126a2c58daabe65672549c63637f8bca6aadba3","public:commit:e99ef7a14aa0bef133bcfdc4fc0ff8e73d62d756","public:commit:f4bf693e7b448ad6374c11f4b59048a16014a534","public:commit:fe5660f24fcfaee57c35301ad0becf2dbed9fc52","public:thread:EndstoneMC/endstone:137"],"source_type":"public","date":"2025-02-23..2025-03-06","topics":["lifetime","concurrency","ffi","testing","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Live entity ownership, event timing and native policy {#live-entity-ownership-event-timing-and-native-policy}

## Decision chain {#decision-chain}

301–303 finish the preceding slice's lifetime migration. Sibling review of296–300 establishes that actor wrappers now hold WeakEntityRef and native network lookup uses Level users. This slice removes the parallel UUID→raw-wrapper map and derives online players from the owner instead. Scoreboards use stable UUID keys and cleanup moves to disconnect. This does not make all returned pointers or PlayerInventory owning: invalid native lifetime still matters, and disconnect delivery is now part of cleanup correctness.302 intentionally allows removed entities during checked handle extraction, distinguishing removal callbacks from destroyed storage.

Event seams continue changing rather than following one timeless rule.187 moved join dispatch to initial spawn;310 moves it again to client SetLocalPlayerAsInit interception. The receive event can cancel before the initialized setter, which then changes native state and emits join/message/permission/command effects.311 consolidates packet interception under native coordinator forwarding. The setter lacks a repeated-initialization guard in the read patch. Timing relative to actual native processing and malicious/repeated client packets needs explicit tests; a title promising client readiness is not that evidence.

305 repairs a behavior lost in186: death packet delivery and SHOW_DEATH_MESSAGES-controlled public broadcast are separate actions, with console fallback.308–309 similarly preserve contextual command output: origin category, COMMAND_BLOCK_OUTPUT and SEND_COMMAND_FEEDBACK decide output type. Wrapper convenience must not silently bypass native policy.306 relocates unwrap/rewrap protection from reload to reloadData itself, broadening caller coverage without supplying exception-safe restoration or waiting for asynchronous reload completion.

328–331 reduce dependence on native addresses where local algorithms are manageable. Local command formatting, alias lookup, registry preconditions and scoreboard reference bookkeeping replace symbol calls. This exposes invariants that were previously hidden: alias targets must exist; registry access requires primary thread plus loaded level; scoreboard identity count must agree with objective membership. The native score-removal callback is still opaque, so absence of a local scores_.erase is an unresolved parity question rather than a proven reset defect.

<a id="collaborator-context"></a>
## Collaborator context {#collaborator-context}

Intervening commit0a4d5ad97d8617dca0c874a181bc937feb103f4e, PR137, is authored by daoge (GitHub smartcmd) and explicitly coauthored by Vincent. Its nine-file full patch adds item-component NBT export, creative groups JSON export and per-entry group index/category. The message records revisions away from item-level creative-group retrieval, especially block items, toward CreativeItemEntry's registry group. The final code indexes the group vector without a bound check and removes prior blockStateHash export. These are collaborator implementation and revision evidence, not a blanket Vincent preference. Public PR body is empty, one social comment supplies no technical rationale, and no reviews/review comments were returned.

## Use and limits {#use-and-limits}

Useful for lifecycle debugging, choosing event interception seams, preserving native gamerules and reducing binary symbol dependencies. No native server, client, build or tests were run. Native callbacks and layouts remain opaque where explicitly stated; no present-day behavior claim follows from this February–March2025 slice.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-301"></a>
### Commit 301 {#commit-301}

6306522a119352c80aef438be3137d684c2916fb · 2025-02-23T17:46:19Z

[refactor: remove raw pointer map for players to prevent dangling pointer issues](https://github.com/EndstoneMC/endstone/commit/6306522a119352c80aef438be3137d684c2916fb)

**Observed change.** Removes raw UUID→EndstonePlayer* registry and weak scoreboard vector. Online players are derived from valid native Level users; UUID lookup delegates native Level. Scoreboard assignments use UUID keys rather than wrapper addresses, and cleanup moves from destructor to disconnect.

**Causal interpretation.** Author explicitly targets dangling-pointer risks: derive live users from their owner instead of maintaining a parallel raw-pointer index. Stable identity keys avoid stale pointer identity, but cleanup now relies on disconnect delivery.

**Limits.** No disconnect/reconnect/lifetime tests. Returned Player* values remain borrowed, and missing disconnect can leave a UUID's board assignment.

<a id="commit-302"></a>
### Commit 302 {#commit-302}

425e1e9c6ec06a447b38bc7388a45f3d27130106 · 2025-02-23T18:30:24Z

[fix: getHandle should return the reference to actor even it's removed](https://github.com/EndstoneMC/endstone/commit/425e1e9c6ec06a447b38bc7388a45f3d27130106)

**Observed change.** EndstoneActor::getHandle explicitly includes removed entities during weak typed extraction; still throws when entity context is invalid.

**Causal interpretation.** A wrapper may need native access during removal callbacks even when ordinary lookup excludes removed actors; distinguishes removed state from destruction.

**Limits.** Does not resurrect destroyed native entities or make stored wrappers owning; no lifecycle tests.

<a id="commit-303"></a>
### Commit 303 {#commit-303}

c0bc94917fb260b493304de23e41e480941a7f35 · 2025-02-23T18:33:16Z

[refactor: simplify `Server::getOnlinePlayers` implementation](https://github.com/EndstoneMC/endstone/commit/c0bc94917fb260b493304de23e41e480941a7f35)

**Observed change.** Replaces manual optional-context online-user loop with native Level::forEachPlayer callback, returning true to continue.

**Causal interpretation.** Delegates valid-player iteration to native owner, completing301 with a smaller adapter.

**Limits.** Enumeration semantics/thread safety rely on native implementation, not tested here.

<a id="commit-304"></a>
### Commit 304 {#commit-304}

d7cda5bb2c01f84c3cc37abeaa076a200cd6d4e5 · 2025-02-23T18:33:28Z

[chore: update python binding stubs](https://github.com/EndstoneMC/endstone/commit/d7cda5bb2c01f84c3cc37abeaa076a200cd6d4e5)

**Observed change.** Adds missing Actor.is_valid Python stub and docstring covering death, despawn and not-yet-added actors.

**Causal interpretation.** Completes a preexisting binding surface; no new implementation or separate design claim.

**Limits.** Docstring alone is not proof of all lifecycle semantics.

<a id="commit-305"></a>
### Commit 305 {#commit-305}

bfdc73067bce1d5bad7dd460fb4110fae50b046f · 2025-02-25T20:24:13Z

[fix: respect `SHOW_DEATH_MESSAGES` game rule](https://github.com/EndstoneMC/endstone/commit/bfdc73067bce1d5bad7dd460fb4110fae50b046f)

**Observed change.** Models GameRule/GameRules storage and ID, getBool with bounds/default; player death still sends DeathInfo but broadcasts nonempty text only with SHOW_DEATH_MESSAGES, otherwise logs to console.

**Causal interpretation.** Restores the gamerule check lost during186's death-hook migration. Client death information, public broadcast, console logging and empty-message suppression are separate effects.

**Limits.** No native layout or gamerule tests. getBool assumes the indexed rule actually holds a bool; fallback is false.

<a id="commit-306"></a>
### Commit 306 {#commit-306}

42da234f10576a5c86257e84a50f6cfa0bf64f30 · 2025-02-27T16:21:10Z

[fix: attempt to fix a crash on `Server::reloadData`](https://github.com/EndstoneMC/endstone/commit/42da234f10576a5c86257e84a50f6cfa0bf64f30)

**Observed change.** Moves event unwrap/rewrap from reload into reloadData around requestResourceReload and loadFunctionManager.

**Causal interpretation.** Direct reloadData callers now receive the190 protection too; commit explicitly says attempt to fix a crash, not demonstrated resolution.

**Limits.** Still no exception-safe restoration or asynchronous completion wait; existing2.5-second async TODO remains.

<a id="commit-307"></a>
### Commit 307 {#commit-307}

56e75c49246d640d336b23d7a2b8e7f760222f7d · 2025-02-27T16:24:42Z

[feat: update error message for command permissions](https://github.com/EndstoneMC/endstone/commit/56e75c49246d640d336b23d7a2b8e7f760222f7d)

**Observed change.** Permission denial now uses commands.generic.error.permissions rather than commands.generic.unknown.

**Causal interpretation.** Makes user feedback reflect denial instead of pretending command absence; no permission decision changes.

**Limits.** No localization/client output tests.

<a id="commit-308"></a>
### Commit 308 {#commit-308}

064027b78b1e30e33c1526cf1890b96a61eb3bd6 · 2025-02-27T17:20:50Z

[fix: respect `SEND_COMMAND_FEEDBACK` game rule](https://github.com/EndstoneMC/endstone/commit/064027b78b1e30e33c1526cf1890b96a61eb3bd6)

**Observed change.** Computes CommandOutputType from origin and gamerules: test/automation/script DataSet, dedicated server AllOutput, command blocks LastOutput when COMMAND_BLOCK_OUTPUT false, ordinary senders Silent when SEND_COMMAND_FEEDBACK false. Command wrapper uses it instead of forced AllOutput; adds output type getter.

**Causal interpretation.** Public wrapper must preserve native contextual output policy rather than bypassing it by always collecting/showing all output.

**Limits.** No origin/gamerule matrix tests; absent level falls back AllOutput.

<a id="commit-309"></a>
### Commit 309 {#commit-309}

88928db918e44941a0bf71741bd3448721fbbc80 · 2025-02-27T17:31:43Z

[refactor: clean up the implementation of `MinecraftCommands::getOutputType`](https://github.com/EndstoneMC/endstone/commit/88928db918e44941a0bf71741bd3448721fbbc80)

**Observed change.** Refactors308 into explicit command-block switch cases and early returns; includes corrected.

**Causal interpretation.** Same decision table with less coupled intermediate state. Checked actual branches rather than treating title as proof of equivalence.

**Limits.** No independent lesson or measured result beyond preserving308 policy.

<a id="commit-310"></a>
### Commit 310 {#commit-310}

008a528a4a82f9c01f9020ec9bcd285af9699aa4 · 2025-02-27T18:52:19Z

[refactor: trigger `PlayerJoinEvent` after handling `SetLocalPlayerAsInitPacket` from the client](https://github.com/EndstoneMC/endstone/commit/008a528a4a82f9c01f9020ec9bcd285af9699aa4)

**Observed change.** Moves PlayerJoin off PlayerInitialSpawnEvent to incoming SetLocalPlayerAsInit detection, after public receive cancellation check. Adds native ServerPlayer/container-menu layout and local initialized setter; setter marks flag then fires mutable join message, permissions and commands.

**Causal interpretation.** Revises187's event seam to wait for client readiness. Source invokes the setter from packet interception rather than calling a native original; title's timing claim must be distinguished from actual event-handler ordering.

**Limits.** Setter has no already-initialized guard in this patch; duplicate init packets may repeat dispatch unless upstream filtering prevents them. No client readiness/repetition tests; size assertions are not runtime ABI validation.

<a id="commit-311"></a>
### Commit 311 {#commit-311}

e126a2c58daabe65672549c63637f8bca6aadba3 · 2025-03-01T15:09:07Z

[refactor: update the implementation of data packet events](https://github.com/EndstoneMC/endstone/commit/e126a2c58daabe65672549c63637f8bca6aadba3)

**Observed change.** Moves data packet events from allowIncoming/Outgoing detours into server-network event decorator. Uses native global receive buffer/send stream; receive cancellation cancels coordinator and suppresses join setter. Outgoing iterates recipients but returns false on any cancellation, aborting the whole event.

**Causal interpretation.** Continues coordinator consolidation while preserving packet interception and join trigger. One recipient's cancellation currently affects the broadcast, later repaired376.

**Limits.** No packet ordering/concurrency/payload lifetime tests. Single global streams are borrowed; recipient-isolation bug is source-visible.

<a id="commit-312"></a>
### Commit 312 {#commit-312}

2dad431c1c60a372a868ed0689724a942cbef396 · 2025-03-01T15:32:29Z

[feat: add constructor for `ServerPlayer`](https://github.com/EndstoneMC/endstone/commit/2dad431c1c60a372a868ed0689724a942cbef396)

**Observed change.** Declares full ServerPlayer native constructor including network, transfer manager, identity, platform/memory and callbacks.

**Causal interpretation.** ABI scaffolding for changing native version, not a new constructed public Player.

**Limits.** No body or construction test; signature changes again341.

<a id="commit-313"></a>
### Commit 313 {#commit-313}

0b6684a726c5b8848af2c7f3bd5747910e777753 · 2025-03-01T16:59:13Z

[fix: `Actor::getNameTag` and `Actor::setNameTag` now works as expected](https://github.com/EndstoneMC/endstone/commit/0b6684a726c5b8848af2c7f3bd5747910e777753)

**Observed change.** Fixes SynchedActorData hasData reversed bounds check >=→<. Models DataItem as abstract virtual interface with getId/getType/equality/clone and moves type/id into derived DataItem2; updates value field access.

**Causal interpretation.** Name-tag failure combines indexing logic and native class-layout/vtable assumptions. Valid indices previously returned false while out-of-range could index invalid memory.

**Limits.** No boundary tests or native vtable validation; DataItem2 remains abstract and is used as a layout cast.

<a id="commit-314"></a>
### Commit 314 {#commit-314}

9232f9c39d203ff8d0a480d4ad825f31fad9152c · 2025-03-03T12:22:07Z

[style: code formatting](https://github.com/EndstoneMC/endstone/commit/9232f9c39d203ff8d0a480d4ad825f31fad9152c)

**Observed change.** Reformats Python exports and joins adjacent f-string literals without changing expressions/values.

**Causal interpretation.** Content-checked formatting-only maintenance; no independent engineering preference inferred.

**Limits.** No runtime tests needed to claim only observed textual equivalence; not a general behavior certification.

<a id="commit-327"></a>
### Commit 327 {#commit-327}

fe5660f24fcfaee57c35301ad0becf2dbed9fc52 · 2025-03-05T17:15:28Z

[feat: improve error logging during plugin loading with detailed stack traces](https://github.com/EndstoneMC/endstone/commit/fe5660f24fcfaee57c35301ad0becf2dbed9fc52)

**Observed change.** Plugin entry-point load catches BaseException rather than Exception and logs full formatted traceback with entry-point name.

**Causal interpretation.** Improves diagnostic detail but also swallows SystemExit/KeyboardInterrupt-class exceptions into a failed-plugin result, a meaningful policy broadening under a logging title.

**Limits.** No import-failure or interruption tests.

<a id="commit-328"></a>
### Commit 328 {#commit-328}

f4bf693e7b448ad6374c11f4b59048a16014a534 · 2025-03-06T14:11:36Z

[feat: implement `CommandRegistry::describe`](https://github.com/EndstoneMC/endstone/commit/f4bf693e7b448ad6374c11f4b59048a16014a534)

**Observed change.** Implements command overload syntax assembly locally, calling native parameter describe, tracking requested parameter start/length, removing two platform symbols for overload describe.

**Causal interpretation.** Reduces binary-offset dependence by reimplementing a tractable wrapper algorithm.

**Limits.** start is captured before appending separating space while length excludes space; caller highlight convention needs checking. No parity/format test.

<a id="commit-329"></a>
### Commit 329 {#commit-329}

2e43ba5e0b270ca670e307595aff4312ab42559f · 2025-03-06T14:18:06Z

[feat: implement `CommandRegistry::findCommand`](https://github.com/EndstoneMC/endstone/commit/2e43ba5e0b270ca670e307595aff4312ab42559f)

**Observed change.** Implements command lookup in signature map then alias map, otherwise null; removes corresponding symbols, relocates symbolToString entries without changing values.

**Causal interpretation.** Another reduced native-call dependency, assuming aliases always reference existing signatures.

**Limits.** Map.at throws for dangling alias; no alias invariant or lookup case tests.

<a id="commit-330"></a>
### Commit 330 {#commit-330}

e99ef7a14aa0bef133bcfdc4fc0ff8e73d62d756 · 2025-03-06T17:35:46Z

[refactor: update `ItemRegistryManager::getItemRegistry`](https://github.com/EndstoneMC/endstone/commit/e99ef7a14aa0bef133bcfdc4fc0ff8e73d62d756)

**Observed change.** Replaces native ItemRegistryManager call with explicitly non-native runtime implementation: require primary thread and loaded level, log and return static invalid ref otherwise, then use Level registry. Adds ItemRegistryRef::isValid based on weak expiration; removes symbols/source entry.

**Causal interpretation.** Makes supported timing/thread preconditions explicit instead of invoking native global registry lookup in unsafe contexts.

**Limits.** isValid is point-in-time, not locked lifetime; downstream callers must handle invalid ref. No thread/startup tests.

<a id="commit-331"></a>
### Commit 331 {#commit-331}

800ab564a63b39b7ce3366c41a2f068aac4a6242 · 2025-03-06T22:30:55Z

[feat: implement `Scoreboard::resetPlayerScore`](https://github.com/EndstoneMC/endstone/commit/800ab564a63b39b7ce3366c41a2f068aac4a6242)

**Observed change.** Reimplements resetPlayerScore with score/id validation, onPlayerScoreRemoved callback and identity reference decrement/cleanup. Adds IdentityDictionary removal across player/entity/fake indices, initializes ScoreInfo, and removes reset symbols.

**Causal interpretation.** Local implementation exposes ownership/reference bookkeeping that native dispatch previously concealed.

**Limits.** Local objective score erasure is absent; endpoint callback is native-vtable dispatched and its local body is unreachable, so removal parity remains unresolved rather than proven broken. Unsigned reference count assumes consistency; identity-removal notification is TODO. No scoreboard tests.
