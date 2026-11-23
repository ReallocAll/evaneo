<!-- retrieval: {"source_ids":["public:commit:097cf19d77c388903a36a442b2ba45b48811ce17","public:commit:2aa3674861251bedddbf0c3f204cd0e417f50aca","public:commit:376972566098080a725b9412e3d77d1b1118b364","public:commit:391585f17c34d09a1af4330ee39e20610d85d794","public:commit:60a39d6ab36eb4c69a7ff2cf5748d5ac3cb95fa2","public:commit:8c7dae14916dce213404ae36df433bca06c7d0ce","public:commit:bf266464caef8346cd934f307f93656dd322f808","public:commit:d947c16f5265eb1cff760108ea21e7df9828336f","public:commit:dd98b697026abd66cc8b1abbf184ba0f5e133587","public:commit:ecee99b3fdfb941dd7c49f55141aa79546e257ca"],"source_type":"public","date":"2025-01-02..2025-01-09","topics":["lifetime","concurrency","ffi","testing","build","recovery","diagnosis","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Crash handling, shutdown and permission lifetime {#crash-handling-shutdown-and-permission-lifetime}

## Two distinct lifecycles {#two-distinct-lifecycles}

14 introduces an optional Sentry RAII shell, with unfinished handler path and an unregistered callback.15 chooses Breakpad briefly;17 replaces that with unconditional server-owned CrashHandler using Crashpad, packages its executable next to the runtime, registers diagnostics and initializes a project endpoint.19 adds readable exception/signal names and an explicit report-filter hook. That hook initially always accepts, changes to always reject in 71, and remains false at 100. Returning Sentry null after decref is distinct from not printing a local crash trace: local trace/snippet output still occurs. A successor reports re-enabling at115. This is evidence of an unfinished filter, not a stable policy about what crash data should be transmitted.

25 separates graceful INT/TERM shutdown from fatal reporting. The server owns both handlers; shutdown schedules a task that asks native Minecraft to stop. The new Windows console callback and Linux sigaction callback still call into server/scheduler machinery. No async-signal-safety review or successful runtime signal test is supplied. Destruction resets defaults instead of restoring saved handlers. On Windows registration names console_ctrl_handler, while destruction uses SetConsoleCtrlHandler(nullptr,FALSE); these are not symmetric operations. Later moving these files into core (58) improves target placement but does not by itself establish correct process-level signal lifecycle.

Crash reporting also depends on module/executable discovery, helper placement and shutdown order. The source uses .sentry-native storage, release/environment tags and module-adjacent helpers; Sentry init's result is not checked in the inspected constructor. Native stack reconstruction and source snippets are diagnostic mechanisms, not a guarantee of safe work during memory corruption.66 relocates helper build/install work to core while retaining a runtime dependency.79 moves crash and signal members earlier in the declaration order, which makes them outlive many server members under reverse C++ member destruction.

## Broadcast crash investigation, not a proved universal fix {#broadcast-crash-investigation-not-a-proved-universal-fix}

The exact commit 79 message says it attempts to resolve dangling pointers in Server::broadcast and links issue 115. This gives a direct commit-to-issue relationship missing from the earlier standalone thread dossier. In final context, permission subscription tables store raw Permissible pointers; broadcast obtains those pointers, converts to CommandSender, checks permission and sends messages. A destroyed permission object remaining subscribed can therefore be hazardous.79 adds destructor unsubscription, removes the redundant factory recalculation, moves command-sender permission setup into explicit init, and reorders server members so the plugin manager outlives the console sender. Temporary origin wrappers call init before command dispatch. The previous72 lazy pimpl solution is superseded.

The comment says cleanup is skipped after the plugin manager is destroyed, but the actual helper checks server-locator existence and then dereferences plugin_manager_. That is not an independent proof of plugin-manager liveness in every teardown route. Removing player.disconnect's manual clear moves responsibility to ownership destruction. A review must verify who owns player wrappers and when their permission objects disappear rather than assuming disconnect and destruction are identical.

The completed issue 115 dossier, plus selected source comments checked here, preserves multiple people and failure identities. pgrd1 reports anti-cheat/plugin-triggered broadcast crashes and a separate reload crash. ye111566 offers memory/concurrency hypotheses; these are not diagnoses. Wu asks for a minimal reproducible example and tentatively attributes only the separate reload stack to BDS. Later Windows recovery is reported, while Linux startup and Python attribute-call failures continue; Wu says Linux had not yet been tested on January14, cannot reproduce later crashes, and closes the original issue while redirecting dev-build failures to127. This unit does not reproduce any report or establish which exact build all reporters ran.

## Evidence boundaries {#evidence-boundaries}

All 100 commit authors/committers are Vincent, with GitHub-linked wu-vincent attribution. No coauthor/AI-assistance trailer is present. Reporter testing and collaborator hypotheses are separately credited. Context includes the final raw-pointer subscription operations, broadcast body, constructor/member order, destructor guard, signal implementation and crash callback. These support a precise lifecycle analysis, not a present-day bug report against current Endstone.


<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}



<a id="commit-014"></a>
### 014. feat: add SentryHandler {#commit-014}

Commit: [ecee99b3fdfb941dd7c49f55141aa79546e257ca](https://github.com/EndstoneMC/endstone/commit/ecee99b3fdfb941dd7c49f55141aa79546e257ca) · committed 2025-01-02T13:52:54Z · author Vincent.

Actual parent: `d8e3f061f2f9011a412f1f537786770f489422b8`. Full message and parent-relative patch: local source.

Adds conditional SentryHandler RAII shell, compile definitions for DSN/environment, nonempty DSN static_assert, database/release/environment setup and close. Handler-path and stack-printing remain TODOs, on_crash is not registered here, and construction is not added until17. Defaults environment to development.

Changed-file coverage: 4 paths. `CMakeLists.txt`; `include/endstone/detail/sentry_handler.h`; `src/endstone_runtime/CMakeLists.txt`; `src/endstone_runtime/sentry_handler.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-015"></a>
### 015. feat: set sentry-native backend to breakpad {#commit-015}

Commit: [dd98b697026abd66cc8b1abbf184ba0f5e133587](https://github.com/EndstoneMC/endstone/commit/dd98b697026abd66cc8b1abbf184ba0f5e133587) · committed 2025-01-02T16:06:49Z · author Vincent.

Actual parent: `ecee99b3fdfb941dd7c49f55141aa79546e257ca`. Full message and parent-relative patch: local source.

Selects breakpad in Conan briefly;17 explicitly changes it to crashpad. Do not turn this intermediate backend choice into a settled preference.

Changed-file coverage: 1 paths. `conanfile.py`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-016"></a>
### 016. feat: raise errors when attempting to build with unsupported architectures {#commit-016}

Commit: [097cf19d77c388903a36a442b2ba45b48811ce17](https://github.com/EndstoneMC/endstone/commit/097cf19d77c388903a36a442b2ba45b48811ce17) · committed 2025-01-02T23:24:44Z · author Vincent.

Actual parent: `dd98b697026abd66cc8b1abbf184ba0f5e133587`. Full message and parent-relative patch: local source.

Rejects non-x86_64 Conan builds explicitly before OS/compiler validation. Public native compatibility boundary is narrowed rather than silently attempting unsupported targets.

Changed-file coverage: 1 paths. `conanfile.py`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-017"></a>
### 017. feat: introduce the new crash handler based on crashpad and sentry-native {#commit-017}

Commit: [376972566098080a725b9412e3d77d1b1118b364](https://github.com/EndstoneMC/endstone/commit/376972566098080a725b9412e3d77d1b1118b364) · committed 2025-01-03T19:03:47Z · author Vincent.

Actual parent: `097cf19d77c388903a36a442b2ba45b48811ce17`. Full message and parent-relative patch: local source.

Replaces optional SentryHandler with unconditional server-owned CrashHandler, switches breakpad→crashpad, removes Sentry configuration switches, supplies a module-adjacent handler path and project reporting endpoint, registers crash callback, records release/environment, and packages the helper. Local diagnostics include raw/object addresses, symbols, source locations and snippets. TODO acknowledges missing BDS/plugin-origin filtering. The Linux callback initially accesses ctx.signum on a pointer, repaired by19. Loader becomes a dedicated source/target instead of a compile-definition-controlled dual purpose source. Server still links across core/runtime ownership before the later target reorganization.

Changed-file coverage: 9 paths. `CMakeLists.txt`; `conanfile.py`; `include/endstone/detail/sentry_handler.h → include/endstone/detail/crash_handler.h`; `include/endstone/detail/server.h`; `src/endstone_core/server.cpp`; `src/endstone_runtime/CMakeLists.txt`; `src/endstone_runtime/crash_handler.cpp`; `src/endstone_runtime/loader.cpp → src/endstone_runtime/runtime_loader.cpp`; `src/endstone_runtime/sentry_handler.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-019"></a>
### 019. refactor: add readable message in crash handler {#commit-019}

Commit: [d947c16f5265eb1cff760108ea21e7df9828336f](https://github.com/EndstoneMC/endstone/commit/d947c16f5265eb1cff760108ea21e7df9828336f) · committed 2025-01-03T19:45:02Z · author Vincent.

Actual parent: `5bb1a09351bd83f38a486a3f7ab34c2fa50a562d`. Full message and parent-relative patch: local source.

Maps Windows exceptions and Linux signals to readable names/descriptions, fixes pointer access, and refactors callback printing. Adds a should_report hook with event decref/null on rejection, but implementation always returns true: filtering is explicitly unfinished. Capturing traces/iostream formatting inside crash callbacks is visible; signal-safety is not established.

Changed-file coverage: 1 paths. `src/endstone_runtime/crash_handler.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-025"></a>
### 025. refactor: simplify the signal handler {#commit-025}

Commit: [2aa3674861251bedddbf0c3f204cd0e417f50aca](https://github.com/EndstoneMC/endstone/commit/2aa3674861251bedddbf0c3f204cd0e417f50aca) · committed 2025-01-04T22:58:59Z · author Vincent.

Actual parent: `287c1ed1def343f09f714b225fe2c852078763e5`. Full message and parent-relative patch: local source.

Separates fatal crash reporting from graceful shutdown signals: server owns CrashHandler plus SignalHandler; the latter installs Windows console/C signal handlers or Linux sigaction for INT/TERM and resets defaults on destruction. Removes broad fatal-signal handlers, terminate/purecall handlers and quick_exit paths now delegated to Sentry. New Linux action remains SA_RESETHAND and callback directly requests shutdown; restoration uses defaults rather than prior handlers. Windows destructor calls SetConsoleCtrlHandler(nullptr,FALSE), which is visibly not symmetric with registering console_ctrl_handler; no runtime assertion of successful removal is warranted.

Changed-file coverage: 7 paths. `include/endstone/detail/server.h`; `include/endstone/detail/signal_handler.h`; `src/endstone_core/server.cpp`; `src/endstone_runtime/CMakeLists.txt`; `src/endstone_runtime/crash_handler.cpp`; `src/endstone_runtime/linux/signal_handler.cpp`; `src/endstone_runtime/windows/signal_handler.cpp → src/endstone_runtime/signal_handler.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-058"></a>
### 058. refactor: move crash_handler and signal_handler to `endstone::core` {#commit-058}

Commit: [8c7dae14916dce213404ae36df433bca06c7d0ce](https://github.com/EndstoneMC/endstone/commit/8c7dae14916dce213404ae36df433bca06c7d0ce) · committed 2025-01-06T20:47:02Z · author Vincent.

Actual parent: `a68b7d54b3b2feffa77f1c89d7889d810c3c6424`. Full message and parent-relative patch: local source.

Moves crash/signal ownership into core and links Sentry there; platform abstraction os→get_module/executable functions. Crash output changes platform labels; helper still module-adjacent. Linux implements get_name while declaration asks get_platform, still present at 100. Removes unused VirtualTable helper. Hook namespace becomes endstone::hook and macros use pointer reconstruction. Runtime build list not fully cleaned until60.1 exact move plus8 residual files read.

Changed-file coverage: 9 paths. `src/endstone/core/CMakeLists.txt`; `src/endstone/runtime/crash_handler.cpp → src/endstone/core/crash_handler.cpp`; `src/endstone/core/os.h → src/endstone/core/platform.h`; `src/endstone/runtime/linux/os.cpp → src/endstone/core/platform_linux.cpp`; `src/endstone/runtime/windows/os.cpp → src/endstone/core/platform_windows.cpp`; `src/endstone/runtime/signal_handler.cpp → src/endstone/core/signal_handler.cpp`; `src/endstone/core/virtual_table.h`; `src/endstone/runtime/CMakeLists.txt`; `src/endstone/runtime/hook.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.




<a id="commit-066"></a>
### 066. fix: add missing implementations {#commit-066}

Commit: [60a39d6ab36eb4c69a7ff2cf5748d5ac3cb95fa2](https://github.com/EndstoneMC/endstone/commit/60a39d6ab36eb4c69a7ff2cf5748d5ac3cb95fa2) · committed 2025-01-07T19:40:00Z · author Vincent.

Actual parent: `cd1da494b30c7b57934493a500629ba771d174d1`. Full message and parent-relative patch: local source.

Restores missing Actor::getEndstoneActor0 wrapper factory in core: ECS-cached shared wrapper chooses player/mob/actor and validates player type. Moves Crashpad copy/strip/install to core while dependency still runtime; fixes devtool platform include/use. Explicit missing-implementations message, static only.

Changed-file coverage: 4 paths. `src/endstone/core/CMakeLists.txt`; `src/endstone/core/actor/actor.cpp`; `src/endstone/devtools/devtools.cpp`; `src/endstone/runtime/CMakeLists.txt`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-072"></a>
### 072. fix: lazy initialize in ServerCommandSender {#commit-072}

Commit: [bf266464caef8346cd934f307f93656dd322f808](https://github.com/EndstoneMC/endstone/commit/bf266464caef8346cd934f307f93656dd322f808) · committed 2025-01-08T22:54:05Z · author Vincent.

Actual parent: `6f5a5cf2defd64a579d6a6ccbef50b5d28ddf648`. Full message and parent-relative patch: local source.

ServerCommandSender defers PermissibleBase creation until first permission operation via mutable pimpl; injected permission pointer remains supported. This follows57 removing lazy factory behavior and eagerly recalculating in constructor. Deferred initialization avoids premature server-locator use by inference; title explicitly lazy initialize. Lazy mechanism replaced79 with explicit two-phase init.

Changed-file coverage: 3 paths. `src/endstone/core/command/command_origin_wrapper.h`; `src/endstone/core/command/server_command_sender.cpp`; `src/endstone/core/command/server_command_sender.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-079"></a>
### 079. fix: attempt to resolve crashes caused by dangling pointers when invoking Server::broadcast {#commit-079}

Commit: [391585f17c34d09a1af4330ee39e20610d85d794](https://github.com/EndstoneMC/endstone/commit/391585f17c34d09a1af4330ee39e20610d85d794) · committed 2025-01-09T02:51:17Z · author Vincent.

Actual parent: `7689c6c1c450e0b42936c772ec345cf19ecbe1dd`. Full message and parent-relative patch: local source.

Explicit attempt to repair dangling-pointer crashes in Server::broadcast, linked #115. PermissibleBase destructor unsubscribes permissions if server locator exists; factory stops second recalculation. ServerCommandSender lazy access replaced explicit init after object exists, command-origin wrapper initialized before use; console constructed early then init in server.init. Player.disconnect no longer clears subscriptions; ownership destructor does. Server member order moves plugin manager before sender and long-lived crash/signal first so reverse destruction better aligns lifetime. Source condition checks locator existence, not an independently proven live plugin manager; no reproduced fix. Thread reports later Windows recovery and unresolved distinct Linux failures; causes beyond this attempt remain uncertain.

Changed-file coverage: 9 paths. `src/endstone/core/command/minecraft_command_adapter.cpp`; `src/endstone/core/command/server_command_sender.cpp`; `src/endstone/core/command/server_command_sender.h`; `src/endstone/core/permissions/permissible.h`; `src/endstone/core/permissions/permissible_base.cpp`; `src/endstone/core/permissions/permissible_base.h`; `src/endstone/core/player.cpp`; `src/endstone/core/server.cpp`; `src/endstone/core/server.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.
