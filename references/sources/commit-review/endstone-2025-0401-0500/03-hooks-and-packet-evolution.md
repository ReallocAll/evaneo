<!-- retrieval: {"source_ids":["public:commit:0a3d146dc0ef61dcbdbb4e2e79f8d599f7be46f8","public:commit:2869579c88b1074d27e95b4ea4594afed2f11bd2","public:commit:2a4adfd1c2a332111da319aa1ccff879bb37738c","public:commit:3d64e6751111e546441b6a582ccdf8b3132a3e52","public:commit:43a8c3b8bf621a904183921bfd0e6ad8eb55837d","public:commit:46a0be55c9bfe7b5f9c58e155ab326705ff99e55","public:commit:491f13a67ef01a56f7357ed62d87200963f9511d","public:commit:5583413466fc05f86c8aec7b9535f63663f60e2e","public:commit:5d78c0fe3649292e2982de00c852b4676c08be88","public:commit:67a89e38b2c603194756c5f5107d5cce5492a704","public:commit:6fdf1fbb7e6c844d7d4ac3afbb89077a222b5726","public:commit:7dd7ec710ee7f5dbd2c8f1a4ba53b3e108dac05b","public:commit:7e44dec2d7242d30789d713f84ff25dea80d70c5","public:commit:7fdaa872fa69c7876f6532b16e819d4705e85088","public:commit:a17a95b98676f67b24615f3a6b8fea5fdb90f22f","public:commit:a2c24651b4c1f568e8a433618f3f8c2438bdd7a9","public:commit:bb0e7e659224e9d643ebc133e8eb20cf52614bde","public:commit:ddd269969a8f08ca400cd9e0bb4aa30d4835eb7e","public:commit:e0283ac403f42f300df8618be3c7ee73f9e042b3","public:commit:e277d632064fbb4dcdaa92607ca567e1be6b25ad","public:commit:f639c27b288a086db972f6bba4a96b13ff30ab01","public:commit:f7e2f682dbae174bdf3d766e49aa580affc79339"],"source_type":"public","date":"2025-03-18..2025-03-26","topics":["lifetime","ffi","testing","build","api","diagnosis","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Gameplay hooks and packet evolution {#gameplay-hooks-and-packet-evolution}

## Owning decorators give way to function detours {#owning-decorators-give-way-to-function-detours}

479 introduces runtime target discovery from a vtable slot. Despite the vhook name, the implementation does not replace an individual object's vtable: it reads a function address and installs a funchook code detour, recording a trampoline by detour address.481–486 migrate player, block, scripting, server-network, level and actor handlers, preserving their native forwarding/cancellation and domain callbacks while deleting owning decorator classes. Pass-through overloads need no hook.486 finishes runtime CMake linkage and removes all register/unwrap/rewrap code from server startup/destruction/reload.

The authored release narrative in488 explicitly reports fixing a crash caused by a conflict with the scripting API event system. Inference: leaving the native handler owner untouched avoids the ownership replacement that made wrappers conflict with scripting resets. That is a causal interpretation supported by the deletion/migration, not a quoted design document. Intermediate482–485 have unresolved field/source-list transitions; the final chain, not each timestamp independently, supplies the integrated implementation.

Windows/Linux slot orders differ: actor4/2; block3,1/3,5; level2,1/2,3; player3,2,1/2,3,4; scripting1/3; server-network1/2. Those are static native ABI assumptions, not validated ordinals.481 removes the helper's per-template once_flag; startup still uses process-wide init_server/init_level flags. Hooks are installed after native runPlugins and before setLevel; errors exit, no teardown/uninstall is retained, and trampoline map writes are unsynchronized. Reload no longer reinstalls handler objects. Replacement of function addresses across a wholly new server lifetime is outside the demonstrated contract.

## Send handling, cancellation and the bounded staged tip {#send-handling-cancellation-and-the-bounded-staged-tip}

409 briefly moves shared send-stream header parsing outside recipient iteration;416 moves it back. The terse fix message does not establish a more detailed authored explanation.484's migration preserves the previous invalid-recipient non-advancing iterator. It also preserves borrowed payload views and per-recipient cancellation.

452 moves StartGame seed hiding to NetworkSystem::send and453 forces resource-stack texture_pack_required false so clients can keep their own packs. The latter carries an explicit PocketMine-MP source reference. The cached client-side-generation Boolean still assumes one process-level setting.497 guards typed packet casts with a DataPacket-name check and introduces a connection/peer helper, but still calls original send.

495 adds event-owned replacement strings via setPayload; original views remain borrowed.498 then removes outgoing public event dispatch entirely from the coordinator handler, making it a no-op. Thus the invalid-recipient loop is absent at500, but this is a temporary feature gap rather than a repaired iterator implementation. The next slice owns restoration; no post500 behavior is credited here.

## Receive replacement changes ordering {#receive-replacement-changes-ordering}

498 runs the native scripting handler first; its bypass/cancel result prevents public dispatch. For incoming packets it initializes SetLocalPlayerAsInit before public receive-event parsing/cancellation, so cancellation no longer suppresses that initialization side effect. Original payload is a view; setPayload copies and changes its data pointer. On changed payload the code creates the native packet, checks size, reads, timestamps and dispatches it, then returns cancel/bypass to suppress the normal downstream path. Unknown packet/read errors stop processing; absent/closing connection instead returns true to original flow.

The replacement path uses packet ID low bits but does not restore sender/target subclient bits to the new packet, whose default is PrimaryClient. A copied Event's default string_view also is not automatically rebased to its copied owned string. These are bounded source-contract limitations; no split-screen or event-copy runtime test was performed. DataPacket remains a borrowed payload adapter, and its writeStream helper's view-refresh boundary is discussed in dossier04.

<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}


<a id="commit-409"></a>
### 409. refactor: process packet only once before iterating over recipients {#commit-409}

[f639c27b288a086db972f6bba4a96b13ff30ab01](https://github.com/EndstoneMC/endstone/commit/f639c27b288a086db972f6bba4a96b13ff30ab01) · 2025-03-18T18:46:42Z · author Vincent.

Parents: `56b514781cb89a0a42fc17b51435dfdd61bc8cb3`. Read displays: parent 1.

Moves outgoing packet header parsing outside the recipient loop, unlike the earlier380 placement. Shared send-stream payload remains borrowed; invalid-recipient iterator advancement is still absent.416 later moves parsing back inside the valid-recipient branch.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-416"></a>
### 416. fix: PacketSendEvent now works correctly again {#commit-416}

[491f13a67ef01a56f7357ed62d87200963f9511d](https://github.com/EndstoneMC/endstone/commit/491f13a67ef01a56f7357ed62d87200963f9511d) · 2025-03-20T17:36:35Z · author Vincent.

Parents: `1700c54e1c881977cefa164edda0636e09a8ef33`. Read displays: parent 1.

Moves packet header parse back inside valid-recipient branch and removes redundant inventory const_cast. Message explicitly calls PacketSendEvent fix but does not explain why; reentrant/shared-stream concerns are an inference, not authored rationale. Invalid-recipient iterator gap remains.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-449"></a>
### 449. feat: add virtual methods to `Packet` class {#commit-449}

[e0283ac403f42f300df8618be3c7ee73f9e042b3](https://github.com/EndstoneMC/endstone/commit/e0283ac403f42f300df8618be3c7ee73f9e042b3) · 2025-03-22T19:33:30Z · author Vincent.

Parents: `33e8513e8bfaead972a5ab55bb81a8a9eb9725ff`. Read displays: parent 1.

Activates Packet virtual interface with native getId/name/write/_read and common defaults; server-side checkSize rejects >0xA00000 bytes, read propagates errors. Enables typed packet inspection instead of commented virtual placeholders.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-450"></a>
### 450. refactor: simplify `DataPacket` class {#commit-450}

[3d64e6751111e546441b6a582ccdf8b3132a3e52](https://github.com/EndstoneMC/endstone/commit/3d64e6751111e546441b6a582ccdf8b3132a3e52) · 2025-03-22T19:34:09Z · author Vincent.

Parents: `e0283ac403f42f300df8618be3c7ee73f9e042b3`. Read displays: parent 1.

DataPacket inherits Packet defaults and marks actual overrides; removes duplicate checkSize/read/batching/valid implementations. Borrowed payload storage remains.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-451"></a>
### 451. feat: implement methods in `AvailableCommandsPacket` {#commit-451}

[a17a95b98676f67b24615f3a6b8fea5fdb90f22f](https://github.com/EndstoneMC/endstone/commit/a17a95b98676f67b24615f3a6b8fea5fdb90f22f) · 2025-03-22T19:43:02Z · author Vincent.

Parents: `3d64e6751111e546441b6a582ccdf8b3132a3e52`. Read displays: parent 1.

AvailableCommandsPacket supplies id/name and explicit throwing read/write placeholders, allowing a concrete header model without pretending local serialization is implemented. Native factory object still supplies real vtable where used.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-452"></a>
### 452. refactor: use a cleaner way to modify packets before sending {#commit-452}

[6fdf1fbb7e6c844d7d4ac3afbb89077a222b5726](https://github.com/EndstoneMC/endstone/commit/6fdf1fbb7e6c844d7d4ac3afbb89077a222b5726) · 2025-03-22T19:48:40Z · author Vincent.

Parents: `a17a95b98676f67b24615f3a6b8fea5fdb90f22f`. Read displays: parent 1.

Moves StartGame seed hiding from write hook to NetworkSystem::send switch before forwarding. Still caches client-side-generation once per process and mutates const packet via const_cast. Adds both platform symbol offsets, removes old write hook/CMake source, makes LevelSeed64 ctor public. Message explicitly says cleaner modification path; no proof all native send routes traverse it.

All-parent changed-file occurrences: 7. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-453"></a>
### 453. feat: allow clients to keep non-server-supplied packs when force resource pack is enabled {#commit-453}

[5d78c0fe3649292e2982de00c852b4676c08be88](https://github.com/EndstoneMC/endstone/commit/5d78c0fe3649292e2982de00c852b4676c08be88) · 2025-03-22T20:08:09Z · author Vincent.

Parents: `6fdf1fbb7e6c844d7d4ac3afbb89077a222b5726`. Read displays: parent 1.

Adds resource-pack stack layout and forces texture_pack_required=false before sending, with explicit PocketMine-MP historical source URL explaining preservation of client non-server packs. Retains server-provided pack policy elsewhere; debug print removed454. Attribution is source-comment inspiration, not claim of independent invention.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-454"></a>
### 454. chore: remove debug prints {#commit-454}

[7fdaa872fa69c7876f6532b16e819d4705e85088](https://github.com/EndstoneMC/endstone/commit/7fdaa872fa69c7876f6532b16e819d4705e85088) · 2025-03-22T20:12:48Z · author Vincent.

Parents: `5d78c0fe3649292e2982de00c852b4676c08be88`. Read displays: parent 1.

Removes resource-pack debug printf only, leaving force-false behavior intact.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-455"></a>
### 455. fix: ensure changes to the selected slot in player inventory during `BlockBreakEvent` take effect {#commit-455}

[e277d632064fbb4dcdaa92607ca567e1be6b25ad](https://github.com/EndstoneMC/endstone/commit/e277d632064fbb4dcdaa92607ca567e1be6b25ad) · 2025-03-22T22:23:14Z · author Vincent.

Parents: `7fdaa872fa69c7876f6532b16e819d4705e85088`. Read displays: parent 1.

Fixes issue159 by refreshing native block-break event item_used from currently selected inventory slot after plugin event returns uncancelled. Explicit comment allows plugin inventory changes; cancellation still returns before refresh. Actual sync ordering change, no dedicated test added.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-479"></a>
### 479. feat: add method for hooking virtual methods at runtime {#commit-479}

[ddd269969a8f08ca400cd9e0bb4aa30d4835eb7e](https://github.com/EndstoneMC/endstone/commit/ddd269969a8f08ca400cd9e0bb4aa30d4835eb7e) · 2025-03-24T23:39:32Z · author Vincent.

Parents: `3ac37b3ab1a2a7fb53c0af232699ae6396ec40ef`. Read displays: parent 1.

Adds virtual-target discovery hook: reads runtime vtable slot, installs process-wide function detour with funchook, stores trampoline by detour; template once_flag keyed by ordinal/Obj/Detour type. Does not rewrite an object's vtable. Errors exit; hook handle is not retained/uninstalled and original map unsynchronized. First object's target per specialization constrains multiple native vtable variants; no tests or runtime proof.

All-parent changed-file occurrences: 3. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-481"></a>
### 481. refactor: use vhook for player events {#commit-481}

[46a0be55c9bfe7b5f9c58e155ab326705ff99e55](https://github.com/EndstoneMC/endstone/commit/46a0be55c9bfe7b5f9c58e155ab326705ff99e55) · 2025-03-25T15:39:48Z · author Vincent.

Parents: `2fdd85f733a1bfe0215ab41dfc329598f05a1fb3`. Read displays: parent 1.

Migrates player death/quit/form/respawn/emote/interact/game-mode behavior from owning gameplay decorator to ScriptPlayerGameplayHandler function detours found via native vtable. Preserves cancellation/native forwarding and corrective game-mode packet. Windows ordinals3/2/1 versus Linux2/3/4; installs before server.setLevel within existing init_level call_once after original runPlugins. Removes inner template once_flag, so first-object limitation is now outer startup guard. No unhook path added.

All-parent changed-file occurrences: 13. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-482"></a>
### 482. refactor: use vhook for block events {#commit-482}

[67a89e38b2c603194756c5f5107d5cce5492a704](https://github.com/EndstoneMC/endstone/commit/67a89e38b2c603194756c5f5107d5cce5492a704) · 2025-03-25T16:18:20Z · author Vincent.

Parents: `46a0be55c9bfe7b5f9c58e155ab326705ff99e55`. Read displays: parent 1.

Migrates block placement/break/explosion interception to selected ScriptBlock virtual targets (Windows3/1, Linux3/5); keeps uncancelled item_used refresh455 and event block-list rewrite. Pass-through overloads are no longer hooked. Intermediate CMake/server references are not all repaired until483/486, so this patch is staged, not independently established buildable.

All-parent changed-file occurrences: 7. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-483"></a>
### 483. refactor: use vhook for script events {#commit-483}

[bb0e7e659224e9d643ebc133e8eb20cf52614bde](https://github.com/EndstoneMC/endstone/commit/bb0e7e659224e9d643ebc133e8eb20cf52614bde) · 2025-03-25T16:25:12Z · author Vincent.

Parents: `67a89e38b2c603194756c5f5107d5cce5492a704`. Read displays: parent 1.

Migrates ScriptMessageEvent cancellation/sender fallback to scripting target (Windows1/Linux3), removes block/script decorator references and changes remaining coordinator field names ahead of subsequent commits. No BlockCommandSender support added; TODO retained. Runtime CMake linkage for new sources completes486.

All-parent changed-file occurrences: 8. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-484"></a>
### 484. refactor: use vhook for server network events {#commit-484}

[2869579c88b1074d27e95b4ea4594afed2f11bd2](https://github.com/EndstoneMC/endstone/commit/2869579c88b1074d27e95b4ea4594afed2f11bd2) · 2025-03-25T16:36:18Z · author Vincent.

Parents: `bb0e7e659224e9d643ebc133e8eb20cf52614bde`. Read displays: parent 1.

Migrates chat/incoming/outgoing packet events to server-network vtable target (Windows1/Linux2), exposes shared network buffers, removes owning decorator. Existing invalid-recipient non-advancing loop and borrowed payload behavior survive migration unchanged until498. At this point plugins still run before original native scripting handler.

All-parent changed-file occurrences: 9. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-485"></a>
### 485. refactor: use vhook for level events {#commit-485}

[0a3d146dc0ef61dcbdbb4e2e79f8d599f7be46f8](https://github.com/EndstoneMC/endstone/commit/0a3d146dc0ef61dcbdbb4e2e79f8d599f7be46f8) · 2025-03-25T16:46:24Z · author Vincent.

Parents: `2869579c88b1074d27e95b4ea4594afed2f11bd2`. Read displays: parent 1.

Migrates spawn/weather events to level vtable targets (Windows2/1, Linux2/3); spawn cancellation despawns actor but returns true, weather cancellation restores individual fields. Existing semantics preserved, owning wrapper removed; final runtime linkage follows486.

All-parent changed-file occurrences: 8. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-486"></a>
### 486. refactor: use vhook for actor events {#commit-486}

[2a4adfd1c2a332111da319aa1ccff879bb37738c](https://github.com/EndstoneMC/endstone/commit/2a4adfd1c2a332111da319aa1ccff879bb37738c) · 2025-03-25T17:01:23Z · author Vincent.

Parents: `0a3d146dc0ef61dcbdbb4e2e79f8d599f7be46f8`. Read displays: parent 1.

Completes six-family migration with actor killed/removed detour (Windows4/Linux2), links all new runtime sources, deletes wrap/unwrap/register/unregister lifecycle functions and reload calls. Native handler ownership remains untouched and detours persist by function address; this avoids replacing scripting-owned handler objects. Changelog488 explicitly reports scripting event-system conflict crash fix, supplying rationale absent from terse refactor messages. Process once guards, trampoline lifetime and native vtable assumptions remain static limits.

All-parent changed-file occurrences: 10. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-493"></a>
### 493. refactor: separate definitions from declarations {#commit-493}

[f7e2f682dbae174bdf3d766e49aa580affc79339](https://github.com/EndstoneMC/endstone/commit/f7e2f682dbae174bdf3d766e49aa580affc79339) · 2025-03-26T22:57:18Z · author Vincent.

Parents: `2ea4aaf62565afa7241d72df79680bc3e20109d9`. Read displays: parent 1.

Moves Packet default implementations to cpp and adds typed dispatcher, subclient/reliability/compressibility accessors and receive timestamp. Packet::handle checks dispatcher then calls it; does not itself set is_handled or validate whole payload consumption. Supports forthcoming replacement receive path.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-494"></a>
### 494. feat: add `NetworkConnection` class {#commit-494}

[7e44dec2d7242d30789d713f84ff25dea80d70c5](https://github.com/EndstoneMC/endstone/commit/7e44dec2d7242d30789d713f84ff25dea80d70c5) · 2025-03-26T22:58:12Z · author Vincent.

Parents: `f7e2f682dbae174bdf3d766e49aa580affc79339`. Read displays: parent 1.

Declares native NetworkConnection layout/peer ownership, paused queues and close flag accessor; constructor deleted, no new connection creation. Layout is inferred native model, no size/runtime proof here.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-495"></a>
### 495. feat: add `setPayload` to `PacketSendEvent` and `PacketReceiveEvent` {#commit-495}

[7dd7ec710ee7f5dbd2c8f1a4ba53b3e108dac05b](https://github.com/EndstoneMC/endstone/commit/7dd7ec710ee7f5dbd2c8f1a4ba53b3e108dac05b) · 2025-03-26T22:59:22Z · author Vincent.

Parents: `7e44dec2d7242d30789d713f84ff25dea80d70c5`. Read displays: parent 1.

Adds setPayload to receive/send public events: replacement copied into event-owned string then view retargeted; original incoming view remains borrowed. Python byte setters added. Does not yet wire replacement behavior into dispatch;498 handles receive only. Default event copying would not rebase a self-owned view, so retention/copy semantics remain limited.

All-parent changed-file occurrences: 3. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-496"></a>
### 496. feat: add virtual methods to `NetworkPeer` {#commit-496}

[a2c24651b4c1f568e8a433618f3f8c2438bdd7a9](https://github.com/EndstoneMC/endstone/commit/a2c24651b4c1f568e8a433618f3f8c2438bdd7a9) · 2025-03-26T23:00:17Z · author Vincent.

Parents: `7dd7ec710ee7f5dbd2c8f1a4ba53b3e108dac05b`. Read displays: parent 1.

Adds NetworkPeer virtual send/receive/status/update/flush/local/encryption interface and receive-state enums, enabling direct transport calls. Native vtable ABI declaration, not implementation of transport.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-497"></a>
### 497. feat: add methods to `NetworkSystem` {#commit-497}

[5583413466fc05f86c8aec7b9535f63663f60e2e](https://github.com/EndstoneMC/endstone/commit/5583413466fc05f86c8aec7b9535f63663f60e2e) · 2025-03-26T23:01:30Z · author Vincent.

Parents: `a2c24651b4c1f568e8a433618f3f8c2438bdd7a9`. Read displays: parent 1.

Adds linear connection lookup and internal peer send helper with absent/closing/peer checks, no lock at this layer. Skips typed StartGame/resource-stack casts for DataPacket by name, avoiding reinterpretation of synthetic raw payload objects. Original send still invoked; new helper is groundwork, not send-event replacement yet.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-498"></a>
### 498. feat: handle packet payload modified via `PacketReceiveEvent::setPayload` {#commit-498}

[43a8c3b8bf621a904183921bfd0e6ad8eb55837d](https://github.com/EndstoneMC/endstone/commit/43a8c3b8bf621a904183921bfd0e6ad8eb55837d) · 2025-03-26T23:05:25Z · author Vincent.

Parents: `5583413466fc05f86c8aec7b9535f63663f60e2e`. Read displays: parent 1.

Runs original scripting handler first and honors bypass/cancel, then public callbacks. For receive, initializes SetLocalPlayerAsInit before parsing/public cancellation; copied payload is detected by pointer change, native packet is recreated, size/read checked, timestamp updated and dispatcher invoked, with false returning bypass to avoid original flow repetition. Missing/closing connection returns true, retaining original path. Subclient header bits are no longer propagated to replacement packet and default PrimaryClient remains. Outgoing handler becomes no-op, removing invalid-recipient loop but temporarily also public PacketSendEvent dispatch; no replacement send path in this slice.

All-parent changed-file occurrences: 4. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.
