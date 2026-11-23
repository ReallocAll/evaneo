<!-- retrieval: {"source_ids":["public:commit:00598559bd9de0fc4db1d52555093da4341b9b30","public:commit:0098ee9775723201dbf494c8a78d55261b6bb0ef","public:commit:0fa6a7d7930529683950816fc444b589bb9d6566","public:commit:10bd3a37812bc70f34022153960d045aa62167a4","public:commit:1544e8cb3ca9a9d89bbda64f4ec685eed3de68ae","public:commit:3297d0e9177f4bd4e108931d21c3ad12e83fa67e","public:commit:3a928b8c764642e80eedda938bf4e58fd7b2d2b3","public:commit:484f6066161b81ab6a63f726b84ab3aa3dd47023","public:commit:4e1f1317a1c5f93444a9a891106b42bbc0aa645d","public:commit:4f3cb37afdefb8fb39b12907441c4e8ca6da1906","public:commit:5cecbfe64834cf325d3ebafb096a1752a920956e","public:commit:735eb92099ab19bbedb235d21e4e9ff2744b82e4","public:commit:7b03380c107db7d807aea7dd85a639c7d0dd0ec0","public:commit:7ebad908e827d0fbe47786db020b4ca2045e1864","public:commit:862d445fedf8444883b1cfbf5e50858f2fd75e72","public:commit:8964d34b5cabce1274fe1537664da3b9a44df21e","public:commit:9ed3c790a4758cdba3b5c81ece7cc7a14bbf26eb","public:commit:a2eee77906cf7748b3b00f193e5455e3dd0a4cc1","public:commit:a32e57ffdf41c9ef522061bba044dce46cff8d3c","public:commit:a7fdc9c2b959ec17b75ae5961a9596d4c6eb7c2d","public:commit:b2963c0d98c2011cafc39a9fa38fbd05709e27d6","public:commit:b59cdefe8584e303c74025c7602983cb8ac79f9a","public:commit:bab0df1575792e1ad9a22e1a41f94d3ac90b699e","public:commit:cb1a34e5b7f7b281b153a4dceca933186daa517a","public:commit:cb29540449ab2fa5a89671bf6b394490653c090a","public:commit:d25bc41eca88ffb19aed805a3fb492bfa04eec67","public:commit:d7840335055b141078cd15258a1019326f1e8aff","public:commit:f027c22e08c8845b10887c00b45d3a17bd6c83a4","public:commit:f14cf337a40817583e793edd43910cbd0a5864d6","public:commit:f3acfecbb7c9f00e5c11c20a319f27632652940d","public:commit:f99cebbd77b39f6f14e1ac1eeb24aceb8bc1c3a2","public:commit:fb05ac61fc1e9879f057aa8186fd56e8f8c236f0","public:commit:ff6fd3e5e285085e0da9af98933ed9d573929dcb"],"source_type":"public","date":"2024-03-26..2024-04-08","topics":["lifetime","concurrency","ffi","testing","build","api","diagnosis","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Vtable hooks, level ownership and version-sensitive maintenance {#vtable-hooks-level-ownership-and-version-sensitive-maintenance}

## Result: a revised hook architecture, with explicit remaining assumptions {#result-a-revised-hook-architecture-with-explicit-remaining-assumptions}

560–600 develop per-object virtual-method interception into a shared per-native-type table view and hook clone, integrate it with public Level wrappers, and centralize selected game-version constants. The sequence includes missing lookup state, invalid-index control flow, reported crashes, temporary disabling, a concrete Linux prefix-index bug and a return from explicit native fields to an offset accessor. Its value is the sequence of attempted designs and corrections. It does not justify calling vtable replacement portable or fully validated.

Read this dossier with the native-event dossier for the weather and return-value context. Ordinals 595 and 596 are parallel identical changes from 594, followed by an empty-content merge at 597. They are not successive cleanup revisions. The exact DAG, tree identity and all-parent patch proofs are persisted independently of the prose.

## First design: per-object clone and automatic restoration {#first-design-per-object-clone-and-automatic-restoration}

560 introduces VmtHook with a borrowed target reference. It reads the target's vptr, scans entries until zero, allocates a clone, installs it and restores the original in the destructor. Copy and move are disabled, making the wrapper the sole controller of its allocated copy. This is a familiar RAII shape, but the native table is assumed to be null-terminated and the target must outlive the wrapper. Neither condition is established by the patch. Installation silently ignores an out-of-range slot while uninstallation initially lacks a bound check, so the two operations have different failure contracts.

561 moves pointer conversion into cast.h and evolves the helper to VirtualTable. The new callOriginal looks up the slot by detour address, but hook does not populate the lookup map. 563 supplies that missing mapping and makes failed installation/original lookup fatal. Its invalid-unhook branch logs yet continues into the write; 564 adds termination. This short chain supports careful attention to state that a refactor introduces, rather than assuming the moved helper retains the old direct-index behavior.

562 moves weather handling into an adapter holding a VirtualTable member. The adapter's member function is written into the native object's table. Native dispatch supplies a native-handler this pointer, while the new member body tries to access adapter-owned state. That mismatch is directly inferable from the source. 576 later reports a vmt-hook crash and removes stateful adapter access, but it changes several other conditions at once, so this research does not claim the mismatch was the sole measured cause.

565 makes native slot selection explicit: weather slot 3 on Windows and 4 on Linux. It also reverses the interception order. Native original handling now runs first; a Deny in either outcome field returns immediately without Endstone callbacks. Otherwise the plugin events can restore proposed rain/thunder values. Respecting native veto before extension callbacks is observable policy. Whether resetting an input afterward reverses a native side effect depends on the caller/handler contract and is not proven by this patch. Preserve that limitation when borrowing the pattern.

## Level wrappers make context available {#level-wrappers-make-context-available}

566 adds a large ILevel virtual interface plus forward declarations and supporting types. Most methods are declarations for host access, not newly implemented game algorithms. Exact order, inheritance, platform-tail slots and type signatures determine which native function is called. 567 makes these methods pure virtual, adds nodiscard/includes and removes redundant void spelling. It also changes a long parameter to int32_t, which is width-sensitive on Linux, and accidentally edits the license comment. 572 repairs the comment. This is a useful counterexample to treating a large style patch as semantically empty without reading it.

572 adds a much smaller public Endstone Level interface: name, relative time read and time write. EndstoneLevel borrows a native Level and delegates directly; it does not own the game world. 573 gives EndstoneServer unique ownership of wrappers in a lowercase-name map. Lookup is case-insensitive and returns nullptr if absent; enumeration returns borrowed pointers in unspecified hash-map order. A duplicate wrapper is rejected and destroyed. The diagnostic says the level was prevented from loading, but native loading is not cancelled by this code: only wrapper insertion is rejected.

568 creates the native level-initialized hook, and 574 registers the wrapper before forwarding its original callback. No unload/removal API is added. Consequently lifetime reasoning needs both map ownership and the native world's lifetime; unique_ptr of a wrapper does not own the referenced native Level. Python bindings at 588 expose these borrowed wrappers and mutable time, with no added scheduling or range normalization. This is a deliberately small public abstraction layered over a large ABI surface.

575 connects gameplay-handler adapter construction to EndstoneLevel construction. It locates the native handler through coordinator word offsets 14/15. The table is therefore replaced during wrapper construction, before the original level-initialized callback completes. 576 defers hook installation until after the original server-thread-started callback. At that point the framework has already enabled PostWorld plugins and emitted ServerLoadEvent. This ordering is an important startup contract: a plugin can be enabled and receive the server-load notification before the weather hook is installed. Future late-loaded levels are not shown receiving the same installation automatically.

## Reported crash produces several coordinated changes {#reported-crash-produces-several-coordinated-changes}

576 replaces the unbounded null scan with explicit sizes, 11 Windows and 12 Linux. It copies the entries together with a negative type-info prefix and stores original-table access in EnTT's locator. The detour no longer depends on a per-adapter member. It forwards the received this pointer and chooses Windows explicit-return-buffer versus Linux ordinary return. A separate initialization method runs after the native startup callback, rather than from wrapper construction. EnTT becomes a declared CMake and Conan dependency; 577 corrects the Conan component's lowercase package namespace.

These changes address different assumptions: table extent, pre-address metadata, object identity, return convention and installation timing. The commit title reports a crash fix, but no isolated experiment or test output shows which was necessary or sufficient. The source still writes the hook at an index measured from the allocation start while installing a vptr measured after the prefix. That mismatch remains until 586. Automatic destructor restoration is also removed: the global hook/table objects outlive individual stack adapters, and uninstall becomes an explicit operation rather than guaranteed RAII cleanup.

578 tries another representation for the coordinator: a concrete Pimpl with vectors/counters, a size104 assertion and a unique_ptr gameplay handler, including an extra Linux field. At the same time it comments out installation and removes broad provisional sendEvent hooks. 583 discards those concrete fields/assertion and returns to the offset accessor. This is an observed representation reversal. It supports maintaining a record of abandoned assumptions, not an inference that the author permanently prefers raw offsets over structures.

579 replaces the project's Singleton implementation with EnTT locator across the runtime. The old initialize path throws if an instance already exists; value_or expresses reuse of an existing service. That change can affect repeated initialization behavior. The server's explicit disable/reset sequence remains under a held Python GIL, preserving the earlier teardown rationale from ordinal 309. The older Windows forced-exit workaround at 137 had an explicitly unknown shutdown cause; nothing here retroactively identifies that earlier symptom. Vtable/table locators are different global services and are not reset with the server in the observed shutdown function.

## Separate view and clone, then repair address origins {#separate-view-and-clone-then-repair-address-origins}

583 makes VirtualTable a nonowning view of original entries and VirtualTableHook an owner of cloned storage. Specialized init chooses detours, and the handler initially becomes a static function receiving the native object explicitly. The clone is initially inline static per type. 585 changes it to a member allocation of the hook instance, while the actual caller still obtains one hook per native type from a locator. It also changes the detour back to a state-free member method. This is not the same problem as 562: the body now uses the locator and received native this instead of accessing an adapter data member.

586 fixes the concrete prefix error by writing at Index + typeinfo_size. The installed vptr points at clone + typeinfo_size, so a virtual call at Index now reaches the intended overwritten entry. The commit explicitly identifies nonzero type-info size on Linux/clang; Windows currently uses zero. The arithmetic supports that platform-specific symptom without requiring a speculative host trace. The prefix size had changed from one Windows/two Linux in 576 to zero Windows/two Linux in 583, so this history is not a single immutable ABI rule.

594 introduces another offset: the platform's slot-number adjustment, default zero Windows and one Linux, permitting the same logical weather base index 3 in both call and hook templates. This slot offset is distinct from the negative type-info prefix. At the endpoint, clone writes use base index plus platform slot offset plus storage prefix; original calls use base index plus platform slot offset. Mixing the two coordinate origins was the actual corrected problem. Other native classes need independent evidence for their slot relationship.

The endpoint view's at/call and hook-writing helper have no bounds checks, unlike the temporary fatal checks in 563/576. The first locator initialization captures one original vptr for a native type, and later targets reuse it. The design therefore assumes those targets share a compatible table. There is an uninstall method but no observed lifecycle invocation restoring every target before table destruction or server reset. These are bounded residual assumptions to preserve alongside the fix, not an exhaustive memory-safety audit.

## Identifying the level from the native receiver {#identifying-the-level-from-the-native-receiver}

587 gives WeatherEvent a borrowed Level reference. The detour enumerates server wrappers and compares each native gameplay-handler address with its received this address. On a match it creates level-aware rain/thunder events; on no match it logs critical and terminates. This trades an O(number of levels) lookup and a strict invariant for direct context stored in the adapter. It avoids assuming adapter members exist in a native object, but depends on complete wrapper registration and compatible native handler identity. No multi-level or unload race test is present.

595 adds leave-game and actor-added native hooks at logical indices 6 and 10. They resolve the level, log and forward the native result. They do not emit new public Endstone leave/actor events. The weather implementation is relocated into a local class without changing its original-first/veto behavior. 596 has a style title but is a byte-identical patch from the same parent with an identical full tree. 597 merges the two same-content branches, with zero changed lines against either parent. The merge preserves history, not a new implementation endorsement or conflict-resolution insight.

## Centralizing update-sensitive knowledge {#centralizing-update-sensitive-knowledge}

599 moves unchanged command-symbol IDs into magic.cpp and supplies unusually explicit rationale: no trivial runtime derivation is currently available, so the constants need rechecking at each game update, with CommandRegistry::describe named as the investigation location. 600 adds the ScriptLevelGameplayHandler table-size specialization there and removes repeated size arguments from callers. This is a practical maintenance boundary: callers request the type's known extent, while one version-sensitive file carries the selected values.

The centralization is partial. Coordinator field offsets, variant placeholders, native method declarations and platform slot adjustments still live elsewhere. The file is not an automatic compatibility detector and the selected game version is not a proof those values match every host binary. The portable lesson is to record both the constant and how it was derived, together with the update trigger and known platform variants. That conclusion is grounded in comments and revisions; it is not a universal rule inferred from the author's identity.

## Applying the history {#applying-the-history}

For a native adapter, useful review questions are: where is the vptr address point; which entries precede it; how many callable entries are copied; which object is this; who owns the clone and native target; when is installation safe; how is the original return ABI represented; and what reinitializes state after unload? This chain contains concrete failed or revised answers to most of those questions. No upstream code, host binary or tests were executed, and no reported crash was independently reproduced. The exact diff and blob evidence makes the claims auditable without pretending static reading establishes runtime compatibility.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-523"></a>
### 523. refactor: platform-specific hooking logic {#commit-523}

Source: [10bd3a37812bc70f34022153960d045aa62167a4](https://github.com/EndstoneMC/endstone/commit/10bd3a37812bc70f34022153960d045aa62167a4) · authored 2024-03-26T12:56:29Z. Actual parent(s): `9b72254a7c27b7a95178c0f76a64d21bbc9678ad`.

Author: **Vincent**.

Factors duplicated Windows/Linux install/error handling into common hook.cpp; platform functions now enumerate detours/targets, common code maintains original pointers by both detour and symbol name. Missing-original lookup changes from nullptr return to critical log and terminate. Linux extraction temporarily references removed local detours and header name overload disagrees with definition; 524 repairs both. Full diff reread independently after initial batch display truncation. No hook execution or runtime success claim.

First-parent changed paths: `include/endstone/detail/hook.h`, `src/endstone_runtime/hook.cpp`, `src/endstone_runtime/linux/hook.cpp`, `src/endstone_runtime/windows/hook.cpp`.

Coverage: 517 canonical first-parent patch lines; 517 across all actual parents.

<a id="commit-524"></a>
### 524. fix: get_targets function on Linux {#commit-524}

Source: [8964d34b5cabce1274fe1537664da3b9a44df21e](https://github.com/EndstoneMC/endstone/commit/8964d34b5cabce1274fe1537664da3b9a44df21e) · authored 2024-03-26T13:04:48Z. Actual parent(s): `10bd3a37812bc70f34022153960d045aa62167a4`.

Author: **Vincent**.

Repairs Linux get_targets after 523 by collecting local symbols without stale detours lookup, matching shared installer filtering. Changes declaration from const char* to const std::string& to match implementation. Target map scope expands to all selected symbols; actual installed hooks still follow detours.

First-parent changed paths: `include/endstone/detail/hook.h`, `src/endstone_runtime/linux/hook.cpp`.

Coverage: 35 canonical first-parent patch lines; 35 across all actual parents.

<a id="commit-526"></a>
### 526. feat: add call original method overloads to optionally take function names {#commit-526}

Source: [5cecbfe64834cf325d3ebafb096a1752a920956e](https://github.com/EndstoneMC/endstone/commit/5cecbfe64834cf325d3ebafb096a1752a920956e) · authored 2024-03-26T14:00:39Z. Actual parent(s): `d08c0cdf9338718ed5db8dab8f66650b1b1aebd5`.

Author: **Vincent**.

Adds optional symbol-name lookup for member-function normal/RVO adapters and free-function RVO adapter, with new macros. This bypasses detour pointer identification for cases such as virtual methods while retaining typed signature and platform-specific hidden-result ordering. Non-RVO free function overload remains unchanged. Names are manually supplied ABI identities, not runtime overload inference.

First-parent changed paths: `include/endstone/detail/hook.h`.

Coverage: 110 canonical first-parent patch lines; 110 across all actual parents.

<a id="commit-560"></a>
### 560. feat: add vmt hook {#commit-560}

Source: [a32e57ffdf41c9ef522061bba044dce46cff8d3c](https://github.com/EndstoneMC/endstone/commit/a32e57ffdf41c9ef522061bba044dce46cff8d3c) · authored 2024-04-04T22:27:44Z. Actual parent(s): `a32757a56c9210ed859b446d763546206a05b7b5`.

Author: **Vincent**.

Introduces per-object VmtHook: scans vtable until null, clones entries, replaces target vptr, restores on destruction, deletes copy/move. This makes target lifetime and native table extent implicit; null termination is not established. install silently ignores out-of-range index while uninstall lacks a bound check. No application site yet.

First-parent changed paths: `include/endstone/detail/hook.h`.

Coverage: 79 canonical first-parent patch lines; 79 across all actual parents.

<a id="commit-561"></a>
### 561. refactor: move fp_cast to cast.h, move class VirtualTable to virtual_table.h {#commit-561}

Source: [1544e8cb3ca9a9d89bbda64f4ec685eed3de68ae](https://github.com/EndstoneMC/endstone/commit/1544e8cb3ca9a9d89bbda64f4ec685eed3de68ae) · authored 2024-04-04T23:00:38Z. Actual parent(s): `a32e57ffdf41c9ef522061bba044dce46cff8d3c`.

Author: **Vincent**.

Moves function-pointer cast unchanged into cast.h and replaces VmtHook with VirtualTable API. Original lookup now keys on detour, but hook does not populate the hooks_ map, making the new callOriginal path unresolved until563. This is substantive API/control-flow change despite relocation framing; ABI-sensitive member-pointer conversion remains.

First-parent changed paths: `include/endstone/detail/cast.h`, `include/endstone/detail/hook.h`, `include/endstone/detail/virtual_table.h`.

Coverage: 374 canonical first-parent patch lines; 374 across all actual parents.

<a id="commit-562"></a>
### 562. refactor: hook gameplay handler methods using vmt hook {#commit-562}

Source: [3a928b8c764642e80eedda938bf4e58fd7b2d2b3](https://github.com/EndstoneMC/endstone/commit/3a928b8c764642e80eedda938bf4e58fd7b2d2b3) · authored 2024-04-04T23:01:04Z. Actual parent(s): `1544e8cb3ca9a9d89bbda64f4ec685eed3de68ae`.

Author: **Vincent**.

Moves weather interception into EndstoneLevelGameplayHandler adapter with VirtualTable member and slot3 detour; native ScriptLevelGameplayHandler declaration becomes empty. Installed member function accesses adapter state even though native dispatch supplies native-handler this. This concrete mismatch is an inference from source, not a uniquely proven crash cause;576 later reports a vmt-hook crash and removes per-adapter state. Integration is not present yet.

First-parent changed paths: `include/bedrock/event/gameplay_handler.h`, `include/bedrock/gameplay_handler.h`, `include/endstone/detail/gameplay_handler.h`, `src/endstone_core/gameplay_handler.cpp`, `src/endstone_runtime/bedrock/event/gameplay_handler.cpp`.

Coverage: 242 canonical first-parent patch lines; 242 across all actual parents.

<a id="commit-563"></a>
### 563. feat: update hook/unhook methods and improve error handling in VirtualTable class {#commit-563}

Source: [f99cebbd77b39f6f14e1ac1eeb24aceb8bc1c3a2](https://github.com/EndstoneMC/endstone/commit/f99cebbd77b39f6f14e1ac1eeb24aceb8bc1c3a2) · authored 2024-04-04T23:13:24Z. Actual parent(s): `3a928b8c764642e80eedda938bf4e58fd7b2d2b3`.

Author: **Vincent**.

Populates detour→slot lookup and makes bad installation/original lookup fatal, repairing561 missing-map behavior. unhook logs an invalid index but initially falls through into an out-of-range write;564 closes that branch. Original mapping is not erased on unhook.

First-parent changed paths: `include/endstone/detail/virtual_table.h`.

Coverage: 84 canonical first-parent patch lines; 84 across all actual parents.

<a id="commit-564"></a>
### 564. fix: add missing std::terminate {#commit-564}

Source: [b2963c0d98c2011cafc39a9fa38fbd05709e27d6](https://github.com/EndstoneMC/endstone/commit/b2963c0d98c2011cafc39a9fa38fbd05709e27d6) · authored 2024-04-04T23:14:30Z. Actual parent(s): `f99cebbd77b39f6f14e1ac1eeb24aceb8bc1c3a2`.

Author: **Vincent**.

Adds terminate after invalid-unhook diagnostic, preventing the fallthrough write introduced in563. Explicit failure contract replaces continuing after an invariant violation.

First-parent changed paths: `include/endstone/detail/virtual_table.h`.

Coverage: 12 canonical first-parent patch lines; 12 across all actual parents.

<a id="commit-565"></a>
### 565. feat: account for different vtable method index on Windows and Linux {#commit-565}

Source: [f14cf337a40817583e793edd43910cbd0a5864d6](https://github.com/EndstoneMC/endstone/commit/f14cf337a40817583e793edd43910cbd0a5864d6) · authored 2024-04-04T23:30:24Z. Actual parent(s): `b2963c0d98c2011cafc39a9fa38fbd05709e27d6`.

Author: **Vincent**.

Renames adapter, selects weather slot3 Windows/4 Linux, and changes event ordering: original handler now runs first; native Deny in either result field suppresses Endstone callbacks. Otherwise weather cancellation restores proposed native booleans after original returns. This preserves native veto priority but cannot undo any side effects already performed by original; caller consumption remains unverified.

First-parent changed paths: `include/endstone/detail/gameplay_handler.h`, `include/endstone/detail/gameplay_handler_adapter.h`, `include/endstone/detail/virtual_table.h`, `src/endstone_core/gameplay_handler.cpp`, `src/endstone_core/gameplay_handler_adapter.cpp`.

Coverage: 296 canonical first-parent patch lines; 296 across all actual parents.

<a id="commit-566"></a>
### 566. feat: add ILevel {#commit-566}

Source: [d7840335055b141078cd15258a1019326f1e8aff](https://github.com/EndstoneMC/endstone/commit/d7840335055b141078cd15258a1019326f1e8aff) · authored 2024-04-05T00:52:29Z. Actual parent(s): `f14cf337a40817583e793edd43910cbd0a5864d6`.

Author: **Vincent**.

Introduces broad native ILevel virtual interface and supporting forward declarations, Core::PathBuffer and NonOwnerPointer alias. This is ABI surface reconstruction enabling later level/coordinator calls, not implementation of hundreds of game features. Method ordering, platform tail slots and opaque void-pointer types are host-layout assumptions. NonOwnerPointer is represented as shared_ptr despite its name; ownership semantics are not proven by the alias.

First-parent changed paths: `include/bedrock/bedrock.h`, `include/bedrock/command/command_origin.h`, `include/bedrock/core.h`, `include/bedrock/event/event_coordinator.h`, `include/bedrock/forward.h`, `include/bedrock/level/level.h`, `include/bedrock/level/level_interface.h`, `include/bedrock/mce.h`, `include/bedrock/uuid.h`.

Coverage: 871 canonical first-parent patch lines; 871 across all actual parents.

<a id="commit-567"></a>
### 567. style: code cleanup {#commit-567}

Source: [f027c22e08c8845b10887c00b45d3a17bd6c83a4](https://github.com/EndstoneMC/endstone/commit/f027c22e08c8845b10887c00b45d3a17bd6c83a4) · authored 2024-04-05T01:10:44Z. Actual parent(s): `d7840335055b141078cd15258a1019326f1e8aff`.

Author: **Vincent**.

Large cleanup makes ILevel methods pure virtual, defaults destructor, adds includes/nodiscard, removes void parameter spelling and top-level return const, and renames underscored methods. It also changes setServerTickOffset long→int32_t, a width-sensitive declaration change on Linux, and short→int16_t. Accidental license-comment =0 is repaired572. Full diff was reread in three contiguous pages after initial tool truncation; style title is not evidence of semantic neutrality.

First-parent changed paths: `include/bedrock/level/level_interface.h`.

Coverage: 809 canonical first-parent patch lines; 809 across all actual parents.

<a id="commit-568"></a>
### 568. feat: hook ServerInstanceEventCoordinator::sendServerLevelInitialized {#commit-568}

Source: [0098ee9775723201dbf494c8a78d55261b6bb0ef](https://github.com/EndstoneMC/endstone/commit/0098ee9775723201dbf494c8a78d55261b6bb0ef) · authored 2024-04-05T01:11:23Z. Actual parent(s): `f027c22e08c8845b10887c00b45d3a17bd6c83a4`.

Author: **Vincent**.

Adds ServerInstanceEventCoordinator::sendServerLevelInitialized export/detour forwarding original only. Establishes lifecycle interception point; no public load event or wrapper registration until574.

First-parent changed paths: `include/bedrock/event/event_coordinator.h`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 49 canonical first-parent patch lines; 49 across all actual parents.

<a id="commit-570"></a>
### 570. feat: define Color class in mce.h {#commit-570}

Source: [735eb92099ab19bbedb235d21e4e9ff2744b82e4](https://github.com/EndstoneMC/endstone/commit/735eb92099ab19bbedb235d21e4e9ff2744b82e4) · authored 2024-04-05T01:31:56Z. Actual parent(s): `020a250abb7668a1fa12ec94a5bafc535fca71fd`.

Author: **Vincent**.

Defines mce::Color as four public float components RGBA, replacing forward declaration. Native value representation is now concrete; no packing/conversion tests included.

First-parent changed paths: `include/bedrock/mce.h`.

Coverage: 18 canonical first-parent patch lines; 18 across all actual parents.

<a id="commit-572"></a>
### 572. feat: add Level and EndstoneLevel class {#commit-572}

Source: [484f6066161b81ab6a63f726b84ab3aa3dd47023](https://github.com/EndstoneMC/endstone/commit/484f6066161b81ab6a63f726b84ab3aa3dd47023) · authored 2024-04-05T10:02:56Z. Actual parent(s): `dfa72c16745b19a1f51e7fab1c45e1aa8fbea1fb`.

Author: **Vincent**.

Adds public Level interface for name/time and EndstoneLevel borrowing native Level reference. Calls getLevelId/getTime/setTime directly; no range normalization, scheduling or thread check. Ownership remains with native host, while wrapper ownership is added573. Also repairs567 malformed license comment.

First-parent changed paths: `include/bedrock/level/level_interface.h`, `include/endstone/detail/level/level.h`, `include/endstone/level/level.h`, `src/endstone_core/level/level.cpp`.

Coverage: 149 canonical first-parent patch lines; 149 across all actual parents.

<a id="commit-573"></a>
### 573. feat: manage levels in Server class {#commit-573}

Source: [a2eee77906cf7748b3b00f193e5455e3dd0a4cc1](https://github.com/EndstoneMC/endstone/commit/a2eee77906cf7748b3b00f193e5455e3dd0a4cc1) · authored 2024-04-05T10:03:19Z. Actual parent(s): `484f6066161b81ab6a63f726b84ab3aa3dd47023`.

Author: **Vincent**.

Adds Server level enumeration/lookup and owned wrapper map. Names are lowercased for case-insensitive keys; duplicate wrapper is rejected/logged. Returned raw pointers borrow map-owned wrappers; iteration order follows unordered_map. No unload/removal contract or native lifetime synchronization appears. Duplicate message says prevented from loading, but this code prevents wrapper insertion rather than native world loading.

First-parent changed paths: `include/endstone/detail/server.h`, `include/endstone/server.h`, `src/endstone_core/server.cpp`.

Coverage: 109 canonical first-parent patch lines; 109 across all actual parents.

<a id="commit-574"></a>
### 574. feat: add level instance to server on load {#commit-574}

Source: [ff6fd3e5e285085e0da9af98933ed9d573929dcb](https://github.com/EndstoneMC/endstone/commit/ff6fd3e5e285085e0da9af98933ed9d573929dcb) · authored 2024-04-05T10:10:26Z. Actual parent(s): `a2eee77906cf7748b3b00f193e5455e3dd0a4cc1`.

Author: **Vincent**.

Registers owned EndstoneLevel wrapper in server before forwarding native level-initialized callback. Connects572/573 to lifecycle. Does not establish order relative to every possible later native load/unload; no standalone level-loaded public event.

First-parent changed paths: `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 33 canonical first-parent patch lines; 33 across all actual parents.

<a id="commit-575"></a>
### 575. feat: hook virtual methods from EndstoneGameplayHandlerAdapter {#commit-575}

Source: [fb05ac61fc1e9879f057aa8186fd56e8f8c236f0](https://github.com/EndstoneMC/endstone/commit/fb05ac61fc1e9879f057aa8186fd56e8f8c236f0) · authored 2024-04-05T11:29:37Z. Actual parent(s): `ff6fd3e5e285085e0da9af98933ed9d573929dcb`.

Author: **Vincent**.

Connects adapter construction to EndstoneLevel constructor and reads gameplay handler by platform word offsets14/15 from native coordinator. Adds EnableNonOwnerReferences layout and inheritance. This activates earlier vptr replacement while level wrapper is being created, before original initialization callback returns;576 explicitly defers installation.

First-parent changed paths: `include/bedrock/bedrock.h`, `include/bedrock/event/event_coordinator.h`, `include/bedrock/gameplay_handler.h`, `include/endstone/detail/gameplay_handler_adapter.h`, `include/endstone/detail/level/level.h`, `src/endstone_core/gameplay_handler_adapter.cpp`, `src/endstone_core/level/level.cpp`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 170 canonical first-parent patch lines; 170 across all actual parents.

<a id="commit-576"></a>
### 576. fix: crash due to vmt hook {#commit-576}

Source: [d25bc41eca88ffb19aed805a3fb492bfa04eec67](https://github.com/EndstoneMC/endstone/commit/d25bc41eca88ffb19aed805a3fb492bfa04eec67) · authored 2024-04-05T17:47:46Z. Actual parent(s): `fb05ac61fc1e9879f057aa8186fd56e8f8c236f0`.

Author: **Vincent**.

Reported vmt-hook crash drives broad redesign: explicit table sizes replace null scanning; copies include negative type-info prefix; original table held in EnTT locator; state-free detour passes received this explicitly and uses platform-specific return handling. Installation is deferred until after original server-thread-started callback, following PostWorld plugin enabling and ServerLoadEvent. Removes automatic target restoration ownership, adds EnTT build/package dependency and platform-selection macro. Copy writes still omit prefix offset, fixed586; source does not isolate which combined change resolved reported crash.

First-parent changed paths: `CMakeLists.txt`, `conanfile.py`, `include/bedrock/event/actor_event.h`, `include/bedrock/event/block_event.h`, `include/bedrock/server/server_instance.h`, `include/endstone/detail/gameplay_handler_adapter.h`, `include/endstone/detail/level/level.h`, `include/endstone/detail/virtual_table.h`, `include/endstone/endstone.h`, `src/endstone_core/gameplay_handler_adapter.cpp`, `src/endstone_core/level/level.cpp`, `src/endstone_core/plugin/cpp_plugin_loader.cpp`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`, `src/endstone_runtime/bedrock/minecraft.cpp`, `src/endstone_runtime/bedrock/server/server_instance.cpp`.

Coverage: 450 canonical first-parent patch lines; 450 across all actual parents.

<a id="commit-578"></a>
### 578. feat: add EventCoordinatorPimpl {#commit-578}

Source: [0fa6a7d7930529683950816fc444b589bb9d6566](https://github.com/EndstoneMC/endstone/commit/0fa6a7d7930529683950816fc444b589bb9d6566) · authored 2024-04-06T11:13:16Z. Actual parent(s): `c796fca9c1c136f5ad89fc2877fa4d3abfa77931`.

Author: **Vincent**.

Attempts concrete EventCoordinatorPimpl with three vectors/counters and size104 assertion, exposes unique_ptr gameplay handler with Linux extra field. Simultaneously comments out weather hook installation and removes all provisional actor/block/player/level sendEvent hooks and unsafe dump helper. This is a retreat from broad experimental interception, not additive completion of event support;583 abandons concrete coordinator fields and resumes offset accessor.

First-parent changed paths: `include/bedrock/event/event_coordinator.h`, `src/endstone_core/gameplay_handler_adapter.cpp`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 215 canonical first-parent patch lines; 215 across all actual parents.

<a id="commit-579"></a>
### 579. refactor: replace Singleton<T> with entt::locator<T> {#commit-579}

Source: [cb1a34e5b7f7b281b153a4dceca933186daa517a](https://github.com/EndstoneMC/endstone/commit/cb1a34e5b7f7b281b153a4dceca933186daa517a) · authored 2024-04-06T11:21:34Z. Actual parent(s): `0fa6a7d7930529683950816fc444b589bb9d6566`.

Author: **Vincent**.

Replaces project Singleton with EnTT locator throughout command, permissions, network and lifecycle callers. Initialize now value_or(instance) reuses an existing service rather than old setInstance throwing on duplicate; dependency semantics not independently audited. Explicit GIL-acquired plugin disabling/server reset remains, preserving309 teardown rationale. Vtable locators are distinct and not reset alongside server. Recursion lint suppression does not implement cycle prevention.

First-parent changed paths: `include/endstone/detail/command/command_adapter.h`, `include/endstone/detail/permissions/default_permissions.h`, `include/endstone/detail/singleton.h`, `include/endstone/detail/virtual_table.h`, `src/endstone_core/command/command_adapter.cpp`, `src/endstone_core/command/command_sender.cpp`, `src/endstone_core/command/defaults/plugins_command.cpp`, `src/endstone_core/command/defaults/version_command.cpp`, `src/endstone_core/gameplay_handler_adapter.cpp`, `src/endstone_core/permissions/default_permissions.cpp`, `src/endstone_core/permissions/permissible_base.cpp`, `src/endstone_runtime/bedrock/command/minecraft_commands.cpp`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`, `src/endstone_runtime/bedrock/level/actor/player.cpp`, `src/endstone_runtime/bedrock/raknet/socket2.cpp`.

Coverage: 458 canonical first-parent patch lines; 458 across all actual parents.

<a id="commit-580"></a>
### 580. refactor: replace size_t with std::size_t {#commit-580}

Source: [862d445fedf8444883b1cfbf5e50858f2fd75e72](https://github.com/EndstoneMC/endstone/commit/862d445fedf8444883b1cfbf5e50858f2fd75e72) · authored 2024-04-06T11:25:24Z. Actual parent(s): `cb1a34e5b7f7b281b153a4dceca933186daa517a`.

Author: **Vincent**.

Qualifies size_t as std::size_t across declarations/casts and reformats commented disabled hook code. Actual expressions/offsets/storage and disabled state remain unchanged.

First-parent changed paths: `include/bedrock/event/actor_event.h`, `include/bedrock/event/item_event.h`, `include/bedrock/event/player_event.h`, `include/bedrock/raknet/types.h`, `include/endstone/detail/command/command_lexer.h`, `include/endstone/detail/spdlog/log_sink.h`, `include/endstone/detail/virtual_table.h`, `src/endstone_core/gameplay_handler_adapter.cpp`, `src/endstone_core/spdlog/log_sink.cpp`, `src/endstone_core/spdlog/text_formatter.cpp`, `src/endstone_runtime/bedrock/bedrock_log.cpp`, `src/endstone_runtime/bedrock/minecraft.cpp`, `src/endstone_runtime/bedrock/raknet/socket2.cpp`, `src/endstone_runtime/bedrock/server/server_instance.cpp`, `src/endstone_runtime/linux/os.cpp`, `src/endstone_runtime/windows/hook.cpp`.

Coverage: 357 canonical first-parent patch lines; 357 across all actual parents.

<a id="commit-581"></a>
### 581. refactor: replace all usages of size_t, uint64_t, uint32_t, uint16_t, uint8_t, and int64_t with their std:: alternatives {#commit-581}

Source: [4e1f1317a1c5f93444a9a891106b42bbc0aa645d](https://github.com/EndstoneMC/endstone/commit/4e1f1317a1c5f93444a9a891106b42bbc0aa645d) · authored 2024-04-06T11:28:30Z. Actual parent(s): `862d445fedf8444883b1cfbf5e50858f2fd75e72`.

Author: **Vincent**.

Qualifies fixed-width integer and uintptr_t aliases with std:: throughout native/public declarations and casts; widths and enum values unchanged. Full actual diff verified; unlike567 long→int32_t, no width-changing replacement.

First-parent changed paths: `include/bedrock/bedrock_log.h`, `include/bedrock/command/command_flag.h`, `include/bedrock/command/command_registry.h`, `include/bedrock/command/minecraft_commands.h`, `include/bedrock/event/event_coordinator.h`, `include/bedrock/level/actor/actor.h`, `include/bedrock/level/actor/player.h`, `include/bedrock/level/level_interface.h`, `include/bedrock/mce.h`, `include/bedrock/network/game/available_commands_packet.h`, `include/bedrock/raknet/types.h`, `include/bedrock/type_id.h`, `include/endstone/detail/command/command_lexer.h`, `include/endstone/detail/virtual_table.h`, `include/endstone/logger.h`, `src/endstone_runtime/bedrock/raknet/socket2.cpp`, `src/endstone_runtime/bedrock/raknet/types.cpp`.

Coverage: 411 canonical first-parent patch lines; 411 across all actual parents.

<a id="commit-583"></a>
### 583. refactor: vmt hook {#commit-583}

Source: [00598559bd9de0fc4db1d52555093da4341b9b30](https://github.com/EndstoneMC/endstone/commit/00598559bd9de0fc4db1d52555093da4341b9b30) · authored 2024-04-06T15:28:20Z. Actual parent(s): `777727a00ddc3cce6b52b00ce1ca92201d1a7de0`.

Author: **Vincent**.

Separates borrowed VirtualTable view from VirtualTableHook owning clone, restores native coordinator offset accessor and weather installation, removes concrete Pimpl layout assertion/fields. Introduces static detour with explicit native self and specialized init, platform return branches, and shared clone per type. Hook writes still omit Linux prefix; bounds checks removed. Native wrappers remain ABI assumptions; step is a design revision, not behavior-preserving relocation.

First-parent changed paths: `include/bedrock/event/event_coordinator.h`, `include/bedrock/event/gameplay_handler.h`, `include/bedrock/gameplay_handler.h`, `include/endstone/detail/gameplay_handler_adapter.h`, `include/endstone/detail/level/level.h`, `include/endstone/detail/virtual_table.h`, `src/endstone_core/gameplay_handler_adapter.cpp`, `src/endstone_core/level/level.cpp`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`, `src/endstone_runtime/bedrock/event/gameplay_handler.cpp`.

Coverage: 556 canonical first-parent patch lines; 556 across all actual parents.

<a id="commit-585"></a>
### 585. refactor: move virtual method detours to EndstoneLevelGameplayHandler {#commit-585}

Source: [b59cdefe8584e303c74025c7602983cb8ac79f9a](https://github.com/EndstoneMC/endstone/commit/b59cdefe8584e303c74025c7602983cb8ac79f9a) · authored 2024-04-06T17:56:23Z. Actual parent(s): `74cf1a5bd899c16ca7ca0c19da0d6eac6160c19e`.

Author: **Vincent**.

Returns weather detour from static self parameter to state-free member method; clone becomes per hook instance rather than inline static buffer, while locator still shares one hook per native type. Removes function-address info logging and adds event-name debug logging. This does not reintroduce562 adapter-state access because detour uses external locator, not own data members.

First-parent changed paths: `include/bedrock/event/gameplay_handler.h`, `include/endstone/detail/virtual_table.h`, `src/endstone_runtime/bedrock/event/gameplay_handler.cpp`.

Coverage: 112 canonical first-parent patch lines; 112 across all actual parents.

<a id="commit-586"></a>
### 586. fix: incorrect vmt hook with typeinfo size > 0 (i.e. clang / Linux) {#commit-586}

Source: [f3acfecbb7c9f00e5c11c20a319f27632652940d](https://github.com/EndstoneMC/endstone/commit/f3acfecbb7c9f00e5c11c20a319f27632652940d) · authored 2024-04-06T18:51:58Z. Actual parent(s): `b59cdefe8584e303c74025c7602983cb8ac79f9a`.

Author: **Vincent**.

Repairs clone write index by adding typeinfo_size, matching the pointer installed at clone+prefix. Commit explicitly identifies typeinfo>0 Linux/clang failure. Renames install/uninstall and factors generic handler installer. This is a concrete offset-origin mismatch and fix; Windows currently uses prefix0, so symptom platform split follows arithmetic.

First-parent changed paths: `include/endstone/detail/virtual_table.h`, `src/endstone_core/level/level.cpp`.

Coverage: 60 canonical first-parent patch lines; 60 across all actual parents.

<a id="commit-587"></a>
### 587. feat: add getLevel method to WeatherEvent class {#commit-587}

Source: [4f3cb37afdefb8fb39b12907441c4e8ca6da1906](https://github.com/EndstoneMC/endstone/commit/4f3cb37afdefb8fb39b12907441c4e8ca6da1906) · authored 2024-04-06T19:21:05Z. Actual parent(s): `f3acfecbb7c9f00e5c11c20a319f27632652940d`.

Author: **Vincent**.

Adds borrowed Level reference to WeatherEvent and concrete constructors, resolving earlier world-identity TODO. Native detour scans server wrappers for matching gameplay-handler address; missing match logs critical and terminates. Python weather/thunder level properties added before Level binding588. The Thunder getter spelling names WeatherChangeEvent inherited method, whose declaring base is shared WeatherEvent; do not infer sibling cast bug from spelling alone.

First-parent changed paths: `include/bedrock/event/gameplay_handler.h`, `include/endstone/detail/level/level.h`, `include/endstone/event/weather/thunder_change_event.h`, `include/endstone/event/weather/weather_change_event.h`, `include/endstone/event/weather/weather_event.h`, `src/endstone_core/level/level.cpp`, `src/endstone_python/event.cpp`, `src/endstone_runtime/bedrock/event/gameplay_handler.cpp`.

Coverage: 178 canonical first-parent patch lines; 178 across all actual parents.

<a id="commit-594"></a>
### 594. feat: add offset template parameter to vmt hook-related method for cross-platform compatibility {#commit-594}

Source: [7b03380c107db7d807aea7dd85a639c7d0dd0ec0](https://github.com/EndstoneMC/endstone/commit/7b03380c107db7d807aea7dd85a639c7d0dd0ec0) · authored 2024-04-06T23:30:48Z. Actual parent(s): `7dffd278fd227352b36110ad8bb5f2505586d72b`.

Author: **Vincent**.

Adds default platform slot Offset0 Windows/1 Linux to VirtualTable::call and hook, simplifying weather base index to3. This offset is separate from negative type-info prefix corrected586; both must be included in clone writes. Only this handler’s slot relation is evidenced, not a universal native-vtable rule.

First-parent changed paths: `include/endstone/detail/virtual_table.h`, `src/endstone_runtime/bedrock/event/gameplay_handler.cpp`.

Coverage: 53 canonical first-parent patch lines; 53 across all actual parents.

<a id="commit-595"></a>
### 595. feat: add hooks for LevelStartLeaveGameEvent and LevelAddedActorEvent {#commit-595}

Source: [a7fdc9c2b959ec17b75ae5961a9596d4c6eb7c2d](https://github.com/EndstoneMC/endstone/commit/a7fdc9c2b959ec17b75ae5961a9596d4c6eb7c2d) · authored 2024-04-06T23:56:36Z. Actual parent(s): `7b03380c107db7d807aea7dd85a639c7d0dd0ec0`.

Author: **Vincent**.

Adds HandlerResult enum and installs native leave-game/actor-added slot hooks6/10. Both resolve level, log debug and forward original; they do not emit public Endstone event types. Weather logic is relocated intact into local handler class. Author-date ties596, but both descend directly from594 rather than one revising the other.

First-parent changed paths: `include/bedrock/event/gameplay_handler.h`, `src/endstone_runtime/bedrock/event/gameplay_handler.cpp`.

Coverage: 171 canonical first-parent patch lines; 171 across all actual parents.

<a id="commit-596"></a>
### 596. style: clean up code {#commit-596}

Source: [bab0df1575792e1ad9a22e1a41f94d3ac90b699e](https://github.com/EndstoneMC/endstone/commit/bab0df1575792e1ad9a22e1a41f94d3ac90b699e) · authored 2024-04-06T23:56:36Z. Actual parent(s): `7b03380c107db7d807aea7dd85a639c7d0dd0ec0`.

Author: **Vincent**.

Despite style title, patch is byte-identical to substantive595 from the same parent594; full tree identity also verified. Preserved as separate SHA/commit metadata and duplicate implementation occurrence, not a second design revision. No stylistic delta exists between their trees.

First-parent changed paths: `include/bedrock/event/gameplay_handler.h`, `src/endstone_runtime/bedrock/event/gameplay_handler.cpp`.

Coverage: 171 canonical first-parent patch lines; 171 across all actual parents.

<a id="commit-597"></a>
### 597. Merge remote-tracking branch 'origin/main' {#commit-597}

Source: [cb29540449ab2fa5a89671bf6b394490653c090a](https://github.com/EndstoneMC/endstone/commit/cb29540449ab2fa5a89671bf6b394490653c090a) · authored 2024-04-07T00:03:34Z. Actual parent(s): `bab0df1575792e1ad9a22e1a41f94d3ac90b699e`, `a7fdc9c2b959ec17b75ae5961a9596d4c6eb7c2d`.

Author: **Vincent**.

Merge has parents 596 and 595 with identical trees, so it consolidates ancestry without distinct conflict-resolution changes. This is a static source finding; no runtime behavior is inferred.

First-parent changed paths: none; verified empty tree diff.

Coverage: 0 canonical first-parent patch lines; 0 across all actual parents.

<a id="commit-598"></a>
### 598. style: clean up code {#commit-598}

Source: [7ebad908e827d0fbe47786db020b4ca2045e1864](https://github.com/EndstoneMC/endstone/commit/7ebad908e827d0fbe47786db020b4ca2045e1864) · authored 2024-04-07T00:04:05Z. Actual parent(s): `cb29540449ab2fa5a89671bf6b394490653c090a`.

Author: **Vincent**.

Removes now-redundant using declarations after class relocation and renames local parameter handler_→handler consistently. No event order, callback or native slot changes.

First-parent changed paths: `src/endstone_runtime/bedrock/event/gameplay_handler.cpp`.

Coverage: 32 canonical first-parent patch lines; 32 across all actual parents.

<a id="commit-599"></a>
### 599. feat: move hard-coded values to magic.cpp {#commit-599}

Source: [9ed3c790a4758cdba3b5c81ece7cc7a14bbf26eb](https://github.com/EndstoneMC/endstone/commit/9ed3c790a4758cdba3b5c81ece7cc7a14bbf26eb) · authored 2024-04-08T10:31:58Z. Actual parent(s): `7ebad908e827d0fbe47786db020b4ca2045e1864`.

Author: **Vincent**.

Centralizes unchanged command-symbol constants in magic.cpp with explicit maintenance rationale: no trivial runtime derivation currently, recheck each game update, use CommandRegistry::describe as discovery location. This is documented technical debt/upgrade procedure, not claim constants are timeless or automatically validated.

First-parent changed paths: `src/endstone_runtime/bedrock/command/command_registry.cpp`, `src/endstone_runtime/magic.cpp`.

Coverage: 96 canonical first-parent patch lines; 96 across all actual parents.

<a id="commit-600"></a>
### 600. feat: move virtual table sizes to magic.cpp {#commit-600}

Source: [3297d0e9177f4bd4e108931d21c3ad12e83fa67e](https://github.com/EndstoneMC/endstone/commit/3297d0e9177f4bd4e108931d21c3ad12e83fa67e) · authored 2024-04-08T11:00:38Z. Actual parent(s): `9ed3c790a4758cdba3b5c81ece7cc7a14bbf26eb`.

Author: **Vincent**.

Moves per-native-type vtable size into static specialization in magic.cpp (11 Windows/12 Linux), removing runtime size argument from view/hook/install helper. Consolidates update-sensitive values with symbol constants while retaining platform slot/prefix distinctions. Native header offsets and variant sizes elsewhere are not centralized by this patch. No runtime size verification introduced.

First-parent changed paths: `include/endstone/detail/virtual_table.h`, `src/endstone_core/level/level.cpp`, `src/endstone_runtime/magic.cpp`.

Coverage: 126 canonical first-parent patch lines; 126 across all actual parents.
