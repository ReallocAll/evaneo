<!-- retrieval: {"source_ids":["public:commit:0c6fa223963a6c3ec380d7bd18845ef2e6c1134c","public:commit:26cbcbe025e191ae89013e06cec591c2257d4ef2","public:commit:2b6111f39e1c83ae41a4570bfe41849b51f05e97","public:commit:c4d472a300bb929c59a13b517e2ac5cbaad13dec","public:commit:f7f248153350fc3d6d5754666adb97d3d5648614"],"source_type":"public","date":"2024-10-17","topics":["lifetime","ffi","api","diagnosis","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Scripting events and bounded shutdown repair {#scripting-events-and-bounded-shutdown-repair}

Scope: Endstone commits 1801–1920, September 14–October 22, 2024. These notes follow related implementation areas during this period.

## Startup and shutdown contracts {#startup-and-shutdown-contracts}

The scripting chain proceeds from pass-through hook, to borrowed/noncopyable event references, to a null-handler startup guard, to a public event. The explicit /scriptevent-on-enable crash rationale in 1899 concerns a missing native handler. Adding the public event in 1900 before that check introduces its own dependency on the Endstone level, so the earlier guard cannot be advertised as proof that every startup phase is now safe. The public event is marked cancellable but its cancellation state is not consulted. That mismatch is retained as a counterexample to reasoning from an API declaration alone.

EventRef's noncopyable reference wrapper clarifies borrowing but does not extend a payload's lifetime. ScriptMessageEvent similarly borrows the sender; fallback to console and a block-sender TODO preserve the scope of source identity support. Exact endpoint comparison shows the reviewed hook remains unchanged at 1920; no unobserved later fix is invented.

The repeated Ctrl+C fix is separately bounded. Both platform handlers check for a registered server before accessing it. Its explicit cause is useful evidence for this dated shutdown failure, but it does not establish async-signal safety or explain earlier shutdown problems whose causes were unknown. The inherited GIL shutdown comment moved in 1807 is context, not another fix authored in that relocation. Neither scripts nor the upstream server were executed during review.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1897"></a>
### Commit 1897 · feat: add hook for ScriptingEventCoordinator::sendEvent {#commit-1897}

Source: [f7f248153350fc3d6d5754666adb97d3d5648614](https://github.com/EndstoneMC/endstone/commit/f7f248153350fc3d6d5754666adb97d3d5648614). Authored 2024-10-17T12:23:05Z; committed 2024-10-17T12:23:05Z. Git author: Vincent; committer: Vincent.


Models ScriptCommandMessageEvent with actor, block and initiator optionals and installs a scripting coordinator hook that initially just calls the original. Both platform symbol additions are reviewed; unrelated symbol ordering is mechanical. This is event interception groundwork, not yet a public ScriptMessageEvent or a functioning cancellation policy.

Changed-source navigation: `include/bedrock/world/events/scripting_event_coordinator.h`, `include/bedrock/world/events/scripting_events.h`, `python/src/endstone/_internal/symbols.toml`, `src/endstone_runtime/bedrock/world/events/scripting_event_coordinator.cpp`.

<a id="commit-1898"></a>
### Commit 1898 · feat: delete the copy constructor of EventRef {#commit-1898}

Source: [c4d472a300bb929c59a13b517e2ac5cbaad13dec](https://github.com/EndstoneMC/endstone/commit/c4d472a300bb929c59a13b517e2ac5cbaad13dec). Authored 2024-10-17T13:52:18Z; committed 2024-10-17T13:52:18Z. Git author: Vincent; committer: Vincent.


EventRef becomes explicitly noncopyable and wraps a borrowed reference; ConstEventVariant is flattened into its revised representation. Hook calls reconstruct an EventRef from the current event instead of copying the wrapper. This prevents one kind of accidental wrapper copying but does not extend event lifetime, making retained references outside the dispatch call still unsupported by this code alone.

Changed-source navigation: `include/bedrock/world/events/event_variant.h`, `include/bedrock/world/events/scripting_events.h`, `src/endstone_runtime/bedrock/world/events/player_event_coordinator.cpp`, `src/endstone_runtime/bedrock/world/events/scripting_event_coordinator.cpp`.

<a id="commit-1899"></a>
### Commit 1899 · fix: calling `/scriptevent` in plugin's `on_enable` no longer causes a server crash (blame mojang) {#commit-1899}

Source: [0c6fa223963a6c3ec380d7bd18845ef2e6c1134c](https://github.com/EndstoneMC/endstone/commit/0c6fa223963a6c3ec380d7bd18845ef2e6c1134c). Authored 2024-10-17T14:29:39Z; committed 2024-10-17T14:29:39Z. Git author: Vincent; committer: Vincent.


The stated fix targets /scriptevent invoked during plugin on_enable. The hook checks the native scripting-event-handler pointer and returns Continue when it is absent. A code comment attributes the original crash to the engine dereferencing that pointer unconditionally; the local guard is observed, while that native diagnosis is reported rather than independently disassembled/reproduced. Later event delivery is added before this guard, so the guard's scope must remain precise.

Changed-source navigation: `include/bedrock/gameplayhandlers/scripting_event_handler.h`, `include/bedrock/world/events/scripting_event_coordinator.h`, `src/endstone_runtime/bedrock/world/events/scripting_event_coordinator.cpp`.

<a id="commit-1900"></a>
### Commit 1900 · feat(event): add ScriptMessageEvent to for messages sent by `/scriptevent` command {#commit-1900}

Source: [2b6111f39e1c83ae41a4570bfe41849b51f05e97](https://github.com/EndstoneMC/endstone/commit/2b6111f39e1c83ae41a4570bfe41849b51f05e97). Authored 2024-10-17T17:44:20Z; committed 2024-10-17T17:44:20Z. Git author: Vincent; committer: Vincent.


Adds the public/Python ScriptMessageEvent and resolves an actor sender when possible, otherwise using console; block sender support is left TODO. The event declares itself cancellable, but the hook never consults its cancelled flag before continuing, a direct API/implementation mismatch. It also obtains the server level before checking the native scripting handler, so 1899's null-handler repair does not by itself establish safe access in every startup phase. The sender is borrowed. The full hook is verified unchanged through 1920; no invented later cancellation fix is credited.

Changed-source navigation: `include/bedrock/world/events/scripting_event_coordinator.h`, `include/endstone/event/server/script_message_event.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/event.py`, `src/endstone_python/event.cpp`, `src/endstone_runtime/bedrock/world/events/scripting_event_coordinator.cpp`.

<a id="commit-1901"></a>
### Commit 1901 · fix: resolve a crash when Ctrl+C is pressed more than once to shut down the server {#commit-1901}

Source: [26cbcbe025e191ae89013e06cec591c2257d4ef2](https://github.com/EndstoneMC/endstone/commit/26cbcbe025e191ae89013e06cec591c2257d4ef2). Authored 2024-10-17T18:14:09Z; committed 2024-10-17T18:14:09Z. Git author: Vincent; committer: Vincent.


Both Linux and Windows signal handlers check the server locator before fetching it and requesting shutdown, addressing the stated crash from repeated Ctrl+C. This specifically guards a missing service after teardown. It does not prove general async-signal safety, concurrency protection or complete shutdown idempotence. It is a documented cause for this later failure and should not be retroactively used to explain earlier shutdown crashes whose cause remained unknown.

Changed-source navigation: `src/endstone_runtime/linux/signal_handler.cpp`, `src/endstone_runtime/windows/signal_handler.cpp`.
