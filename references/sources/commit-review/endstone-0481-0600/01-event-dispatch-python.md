<!-- retrieval: {"source_ids":["public:commit:03e79b753a3b7aa1b428404d16a138c9df8d8b28","public:commit:07371848f22c180fed87db59520d15f375edd646","public:commit:07f15bcde24a72f42bb5f940f74145057a141a3a","public:commit:0cb6184911a4ad83c468a33c645a4c454bbc23ce","public:commit:24c82a5fcaa9b79ed027a098905bd62c12adf986","public:commit:2c6f9263f075a11c11f1a746b2bfb16bf56b61ae","public:commit:3d0cdff650d360578b935be30ff38a4ed6728f7b","public:commit:49c13d27e47caf1a7d35126bc12e783506641e06","public:commit:4d35685c756e11c5129c4374cc0249509f8fd67c","public:commit:5bae2949240505c4c7acd874757ba23a33157fdd","public:commit:5f4db999d111a191c4226126bcc2933d622da379","public:commit:60e65ab35c064aec0e3bcc4b6ff34ab5f99f2fc4","public:commit:692e85ea83b83346c3978075a50caf539ca5e346","public:commit:71a2a2839e67bff82445d5ee51f1537bf0934a76","public:commit:76babceb43e442fc5029111457f4caddf16ff109","public:commit:8a2678eb324aa8d821b86a0ff4318acd69611df6","public:commit:8ddfd2f14ee44380156c3b214b1f89ea79221a58","public:commit:b984b7f5d14739089c8dcb9b7eb9b38e1e2df851","public:commit:bd397d6c4ae49578313e59cca4a7b3a87070510a","public:commit:c5a5a1aa8487bf796619ec337a80e20a3bd98fd8","public:commit:c86eb9e191a3a324ded6682d333180f8a51d318a","public:commit:da4ea6348713402da22446d754c3b47c3cedc736","public:commit:f0f653a50b9d649f52816e9f589bfc8aa680468f","public:commit:f22a4d4af4aa8fcdf01851d5b813a75ef91f3ee4","public:commit:f504a876f31c19978bf98762e622a72c892e156a","public:commit:fc86211238664cffc1addcd1eda2b2b74c3a6a9b"],"source_type":"public","date":"2024-03-22..2024-04-06","topics":["lifetime","concurrency","ffi","testing","build","api","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Event dispatch, Python discovery and shared object identity {#event-dispatch-python-discovery-and-shared-object-identity}

## Result and scope {#result-and-scope}

This unit begins on 22 March 2024 with the manager implementation that was still TODO at ordinal 480. By the endpoint on 8 April, native and Python plugins can register callbacks, lifecycle/console/ping/weather paths create events, and the interface distinguishes cancellation from notification. The chain does not establish a general safe custom-event system, automatic thread marshalling, complete unload cleanup or tested host behavior. Those boundaries are important to the design history, rather than reasons to erase the genuine implementation progress.

The linked public commits document the event containers and callback ownership changes. This dossier follows parent edges; the bot merge at 497 is discussed in the build dossier. External PR discussion is not used to infer implementation rationale.

## Dispatch grows from containers into a usable manager {#dispatch-grows-from-containers-into-a-usable-manager}

481 supplies the two missing manager operations. Registration inserts an EventHandler into a HandlerList selected by event-name string, but only for an enabled plugin. Dispatch selects the same string-keyed list, obtains its ordered snapshot and skips disabled plugins. Each callback is surrounded by a std::exception catch so one ordinary exception can be logged while later handlers continue. The handler independently verifies its expected event name and honors ignore_cancelled only for cancellable events that are already cancelled.

The underlying HandlerList uses an ordered map of priority to vectors. That preserves priority order and insertion order within one priority, while a baked raw-pointer vector avoids rebuilding the traversal until registration changes. Its mutex protects collection mutation and snapshot creation. It does not turn the returned pointers into owning references, nor does it protect the manager's separate unordered map. The callback can mutate cancellation and later handlers observe the same event. A Monitor priority is documented as observation-only, but no enforcement prevents a callback from changing the event at that priority. These are source-level mechanics, not measured scheduling or throughput claims.

483 restores getEventName after the previous unit's short getName excursion. Static names are introduced to let typed templates choose a route without constructing an event. The spelling is temporarily inconsistent: ServerCommandEvent uses name while ServerLoadEvent and then templates use NAME; 517 completes the console constant repair. This matters because the template's static_cast from Event to EventType is supported by a routing convention, not runtime type checking. A string collision or a mismatched custom name violates that convention. The source does not show tests that deliberately exercise such a mismatch.

484 adds member-function and free-callback conveniences on Plugin. The receiver is borrowed by reference. 494 replaces a plain function pointer with std::function so captured callables can participate. 499 renames the registration method but accidentally introduces another pointer level in the member signature; 502 repairs it. This is a compact example of source-level API churn having a real type-system effect even when described as a rename. It should not be elevated into an enduring preference for one spelling.

## Python discovery replaces a finite binding experiment {#python-discovery-replaces-a-finite-binding-experiment}

489–492 establish priorities, Event and manager bindings. Python exposes cancellation as a property and asynchronous as a method. Event is abstract and receives neither a public constructor nor a trampoline implementing its pure virtual methods. Consequently these changes expose existing event instances and manager operations, but do not by themselves make arbitrary Python-defined native event subclasses constructible. The nested Result enum describes deny/default/allow concepts without wiring a universal host-action decision mechanism.

494 binds one explicit Plugin registration specialization, ServerLoadEvent. 496 adds normal-priority and false-ignore-cancelled defaults, and 498 catches generated signatures up. 500 removes that finite specialization instead of indefinitely adding another binding for each event class. The replacement in 501–504 is a generic Python discovery layer over manager.register_event. This is an observed alternative-and-replacement chain; no review objection explaining the choice was captured here.

The decorator annotates the original callable with marker, priority and cancellation attributes. It neither registers the handler nor changes how it is called. Plugin.register_events performs registration later by iterating dir(listener), evaluating getattr, finding marked callables and inspecting the bound signature. It requires exactly one parameter whose annotation is an actual class derived from Event. It prefers the annotated class's NAME and falls back to its Python class name. The plugin must already be enabled, and a null listener is rejected. A user therefore has to call register_events at an appropriate lifecycle point; Plugin.__init__ does not do it automatically.

This simple reflection design has specific boundaries. Postponed/string annotations are not resolved with get_type_hints, so a syntactically plausible annotation may fail the actual-class test. Properties/descriptors can run during getattr. Repeating registration can add another callback because no identity-deduplication pass appears. An invalid signature is logged and skipped rather than aborting all listener discovery. These are useful implementation constraints for future extension, not reproduced user failures or a claim about later versions.

503 simultaneously deletes Event copy construction/assignment and changes the Python callback adapter to accept Event pointers, wrapping the native Event reference as its address. The direction of the change supports a shared-mutable-identity intent: cancellation must affect the event the native caller will inspect. The callback is copied into a native std::function, so its callable lifetime is retained by the handler. The native Event itself is commonly stack-scoped in the emitting hook. There is no explicit contract here for retaining a Python event wrapper beyond callback completion, and no lifetime regression test accompanies the change. Do not equate callback retention with ownership of every argument it receives.

## Lifecycle events describe completed transitions {#lifecycle-events-describe-completed-transitions}

485 emits ServerLoadEvent after PostWorld plugins are enabled and before the original native thread-started callback. It has only the Startup load type. Its noncancellable nature makes it notification, not a veto on startup. The later vtable integration adds another step after the original callback; this means the ServerLoadEvent occurs before weather vtable hooks are installed at the endpoint. Event availability and plugin enabled state are separate startup milestones.

506 adds PluginEnableEvent and PluginDisableEvent after setEnabled performs the corresponding callback. An enabling plugin can register during onEnable and then observe its own enable event because its state is already enabled. A disabling plugin has already become disabled when its disable event is dispatched, so the manager's disabled-plugin filter excludes its own handlers. Other still-enabled plugins can observe that notification. A lifecycle callback exception follows existing loader/trampoline behavior; no transactional rollback is introduced by emitting an event afterward.

507 arranges local forward-created binding wrappers so Plugin can be registered before concrete events referring to it. This continues the previous unit's movement away from static pybind wrapper objects with troublesome interpreter lifetime. Constructors are initially exposed for some concrete events, but 532 removes them from server/plugin event bindings as it adds weather bindings. That is a public construction-surface reversal: observing framework-created events becomes the consistent binding pattern. It is not simply an additive weather feature.

## Thread affinity is validation, not execution transfer {#thread-affinity-is-validation-not-execution-transfer}

508 fills the dispatch TODO with two checks: an asynchronous event is rejected on the server thread, and a synchronous event is rejected off it. Rejection logs and returns. There is no queue, scheduler, retry or automatic conversion to asynchronous execution. The earlier comment about synchronized nesting does not become a nesting guard. The ping path explicitly constructs Event(true), whereas ordinary lifecycle/console/weather events use synchronous defaults.

509 moves the native threading query out of the core manager into Server.isPrimaryThread, implemented by EndstoneServer through Bedrock threading and by the test server as true. This is a useful dependency inversion: the manager can depend on a server abstraction without linking the native host thread symbol into a simple test. The constant test answer does not validate thread identity, off-thread rejection or concurrency behavior.

Endpoint full context confirms the manager map remains unsynchronized even though an async worker dispatch is permitted. HandlerList's internal lock does not cover map insertion, plugin destruction or the lifetime of raw pointers already copied into a dispatch snapshot. clearPlugins clears loaders and plugin references but does not clear event_handlers_. Handlers borrow Plugin references and can retain Python callables. Thus disabling is a dispatch eligibility rule, while destroying/unloading requires another lifetime protocol that is not completed by these changes. This is a bounded counterexample to treating the roadmap's completed event API checkbox as proof of full unload safety.

## Python API corrections and persistent limits {#python-api-corrections-and-persistent-limits}

493 exposes permission lookups, removals, defaults and subscriptions with borrowed return policies. It does not add ownership-transfer construction into the manager. The endpoint still contains the prior subscription-map-copy behavior and incomplete permission-removal invalidation; binding an operation does not repair its native implementation. 557 fixes the specific NOT_OP alias that had mapped to Operator since 378, while NOT_OPERATOR already mapped correctly. 588's generated stubs finally reflect that correction and Spectator's numeric change to 3. Those generated observations are distinct from a test of effective authorization or protocol behavior.

588 adds Level name/time, Server level lookup/list and weather level properties. A missing native level returns nullptr, while the stub says Level rather than an optional type. Reference policies preserve a borrowed relationship; they do not demonstrate safe access after server shutdown. Endpoint source also still binds Server.name to getVersion and PluginLoader.disable_plugin to enablePlugin. These are inherited counterexamples, not new changes blamed on 588 or this unit. They limit claims of complete Python/native API equivalence.

## Evidence for reuse {#evidence-for-reuse}

Key technical boundaries are event type identity, decorator behavior, object/callback lifetime, disable versus destruction, thread checks versus scheduling, and event timing relative to startup. This is static review: no compiler, Python import, tests or game server was run. Public commits are linked with each entry.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-481"></a>
### 481. feat: implement callEvent and registerEvent in PluginManager {#commit-481}

Source: [24c82a5fcaa9b79ed027a098905bd62c12adf986](https://github.com/EndstoneMC/endstone/commit/24c82a5fcaa9b79ed027a098905bd62c12adf986) · authored 2024-03-22T14:15:16Z. Actual parent(s): `e4c7a22d1f5ea98b75d93b4fc12aaa03c34e91be`.

Author: **Vincent**.

Implements the previously empty manager dispatch and registration bodies. Handler lists are keyed by event name; registration rejects disabled plugins, dispatch skips disabled plugins and isolates std::exception per callback. List validates event-name identity. Thread-affinity checks remain TODO and manager map access is unsynchronized; borrowed plugin and returned handler-pointer lifetimes still need lifecycle coordination. This immediately supersedes ordinal 480’s unfinished-dispatch boundary, without proving every event path is wired.

First-parent changed paths: `include/endstone/detail/plugin/plugin_manager.h`, `include/endstone/event/event_handler.h`, `include/endstone/event/handler_list.h`, `src/endstone_core/plugin/plugin_manager.cpp`.

Coverage: 144 canonical first-parent patch lines; 144 across all actual parents.

<a id="commit-483"></a>
### 483. refactor: rename getName to getEventName in class Event {#commit-483}

Source: [0cb6184911a4ad83c468a33c645a4c454bbc23ce](https://github.com/EndstoneMC/endstone/commit/0cb6184911a4ad83c468a33c645a4c454bbc23ce) · authored 2024-03-22T14:54:05Z. Actual parent(s): `207248a7ddbb39a872417586e83f35aa287da349`.

Author: **Vincent**.

Reverses ordinal 476 naming, restoring getEventName across base, concrete event, handler and manager; adds static name string for template registration. Concrete ServerCommandEvent uses lowercase name while later registration moves to uppercase NAME. Public API spelling and dependent type contract change, not new routing behavior.

First-parent changed paths: `include/endstone/event/event.h`, `include/endstone/event/event_handler.h`, `include/endstone/event/server/server_command_event.h`, `src/endstone_core/plugin/plugin_manager.cpp`.

Coverage: 65 canonical first-parent patch lines; 65 across all actual parents.

<a id="commit-484"></a>
### 484. feat: add registerEventHandler function to Plugin class {#commit-484}

Source: [bd397d6c4ae49578313e59cca4a7b3a87070510a](https://github.com/EndstoneMC/endstone/commit/bd397d6c4ae49578313e59cca4a7b3a87070510a) · authored 2024-03-22T14:55:33Z. Actual parent(s): `0cb6184911a4ad83c468a33c645a4c454bbc23ce`.

Author: **Vincent**.

Adds Plugin convenience templates for member and free callbacks. They route by EventType static name and static_cast the incoming Event reference, borrowing member receiver by reference. This is ergonomic type adaptation whose safety still depends on string/type consistency and receiver lifetime. Incidental version-command indentation is mechanical; no callback tests.

First-parent changed paths: `include/endstone/plugin/plugin.h`, `src/endstone_core/command/defaults/version_command.cpp`.

Coverage: 46 canonical first-parent patch lines; 46 across all actual parents.

<a id="commit-485"></a>
### 485. feat: add ServerLoadEvent which will be called when server started {#commit-485}

Source: [da4ea6348713402da22446d754c3b47c3cedc736](https://github.com/EndstoneMC/endstone/commit/da4ea6348713402da22446d754c3b47c3cedc736) · authored 2024-03-22T15:27:03Z. Actual parent(s): `bd397d6c4ae49578313e59cca4a7b3a87070510a`.

Author: **Vincent**.

Adds noncancellable ServerLoadEvent and emits it after PostWorld plugin enable but before forwarding the original thread-started host callback. Only Startup load type exists; reload remains TODO. This is the first concrete native emission path in this event chain. Static NAME differs from template name until 486.

First-parent changed paths: `include/endstone/event/server/server_load_event.h`, `src/endstone_runtime/bedrock/server/server_instance.cpp`.

Coverage: 90 canonical first-parent patch lines; 90 across all actual parents.

<a id="commit-486"></a>
### 486. fix: registerEventHandler template functions in plugin.h {#commit-486}

Source: [c86eb9e191a3a324ded6682d333180f8a51d318a](https://github.com/EndstoneMC/endstone/commit/c86eb9e191a3a324ded6682d333180f8a51d318a) · authored 2024-03-22T15:28:40Z. Actual parent(s): `da4ea6348713402da22446d754c3b47c3cedc736`.

Author: **Vincent**.

Changes template registration from EventType::name to EventType::NAME, matching ServerLoadEvent introduced in 485. ServerCommandEvent still has the earlier lowercase declaration at this point. Adjacent interface repair plus wrapping only, not evidence all custom events satisfy the convention.

First-parent changed paths: `include/endstone/plugin/plugin.h`.

Coverage: 28 canonical first-parent patch lines; 28 across all actual parents.

<a id="commit-489"></a>
### 489. feat(python): add bindings for EventPriority {#commit-489}

Source: [07f15bcde24a72f42bb5f940f74145057a141a3a](https://github.com/EndstoneMC/endstone/commit/07f15bcde24a72f42bb5f940f74145057a141a3a) · authored 2024-03-22T17:24:14Z. Actual parent(s): `93f5584f1a0e461c0c91e5ba038b25bc4dc562fb`.

Author: **Vincent**.

Adds Python EventPriority enum, public event facade and generated stubs, and registers event binding initialization. Numeric order matches native enum; unrelated generated whitespace is noise. No dispatch, monitor immutability or ordering test is added.

First-parent changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/event.py`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/event.cpp`.

Coverage: 197 canonical first-parent patch lines; 197 across all actual parents.

<a id="commit-490"></a>
### 490. feat(python): add bindings for Event class {#commit-490}

Source: [8ddfd2f14ee44380156c3b214b1f89ea79221a58](https://github.com/EndstoneMC/endstone/commit/8ddfd2f14ee44380156c3b214b1f89ea79221a58) · authored 2024-03-22T17:38:25Z. Actual parent(s): `07f15bcde24a72f42bb5f940f74145057a141a3a`.

Author: **Vincent**.

Exposes Event name/cancellation and asynchronous query plus nested Result enum, with priority documentation and binding initialization before plugin bindings. Base Event has no Python constructor/trampoline; this does not enable arbitrary Python-defined native event subclasses. asynchronous is bound as a method, while cancellation is a property. Result remains descriptive rather than host-action enforcement.

First-parent changed paths: `include/endstone/event/event.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/event.cpp`.

Coverage: 206 canonical first-parent patch lines; 206 across all actual parents.

<a id="commit-491"></a>
### 491. feat(python): add bindings for ServerLoadEvent {#commit-491}

Source: [5f4db999d111a191c4226126bcc2933d622da379](https://github.com/EndstoneMC/endstone/commit/5f4db999d111a191c4226126bcc2933d622da379) · authored 2024-03-22T17:50:31Z. Actual parent(s): `8ddfd2f14ee44380156c3b214b1f89ea79221a58`.

Author: **Vincent**.

Adds constructible ServerLoadEvent binding, nested load enum and type/name/cancellability accessors, with C++ Startup spelling migration and matching native emission update. Python retains uppercase STARTUP alias. Inherited cancellation semantics still make it noncancellable.

First-parent changed paths: `include/endstone/event/server/server_load_event.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/event.cpp`, `src/endstone_runtime/bedrock/server/server_instance.cpp`.

Coverage: 117 canonical first-parent patch lines; 117 across all actual parents.

<a id="commit-492"></a>
### 492. feat(python): add call_event and register_event to PluginManager class {#commit-492}

Source: [b984b7f5d14739089c8dcb9b7eb9b38e1e2df851](https://github.com/EndstoneMC/endstone/commit/b984b7f5d14739089c8dcb9b7eb9b38e1e2df851) · authored 2024-03-22T17:56:25Z. Actual parent(s): `5f4db999d111a191c4226126bcc2933d622da379`.

Author: **Vincent**.

Binds manager call_event and register_event through pybind functional conversion and generates signatures. Callbacks initially use Event references; ordinal 503 introduces explicit pointer adaptation and deletes event copying. No callback-lifetime or copy-identity test here.

First-parent changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/plugin.cpp`.

Coverage: 51 canonical first-parent patch lines; 51 across all actual parents.

<a id="commit-493"></a>
### 493. feat(python): add permission-related functions to PluginManager {#commit-493}

Source: [71a2a2839e67bff82445d5ee51f1537bf0934a76](https://github.com/EndstoneMC/endstone/commit/71a2a2839e67bff82445d5ee51f1537bf0934a76) · authored 2024-03-22T18:02:40Z. Actual parent(s): `b984b7f5d14739089c8dcb9b7eb9b38e1e2df851`.

Author: **Vincent**.

Exposes permission manager lookup/removal/default/subscription APIs and registered permission set. No Python addPermission ownership-transfer method is added, consistent with native value-copy registration design. Borrowed permissions can be removed through this API; reference return policies do not establish safety after deletion. Existing core subscription-map copying remains unchanged.

First-parent changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/plugin.cpp`.

Coverage: 113 canonical first-parent patch lines; 113 across all actual parents.

<a id="commit-494"></a>
### 494. feat(python): add register_event_handler to Plugin class {#commit-494}

Source: [8a2678eb324aa8d821b86a0ff4318acd69611df6](https://github.com/EndstoneMC/endstone/commit/8a2678eb324aa8d821b86a0ff4318acd69611df6) · authored 2024-03-22T18:12:25Z. Actual parent(s): `71a2a2839e67bff82445d5ee51f1537bf0934a76`.

Author: **Vincent**.

Changes the free-function callback template to std::function, enabling captured/Python callables, and binds only the ServerLoadEvent specialization on Plugin via a macro. This finite specialization approach is later removed in favor of generic decorator discovery. Arguments have no Python defaults until 496.

First-parent changed paths: `include/endstone/plugin/plugin.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/plugin.cpp`.

Coverage: 67 canonical first-parent patch lines; 67 across all actual parents.

<a id="commit-495"></a>
### 495. feat(python): import additional classes in endstone event module {#commit-495}

Source: [f22a4d4af4aa8fcdf01851d5b813a75ef91f3ee4](https://github.com/EndstoneMC/endstone/commit/f22a4d4af4aa8fcdf01851d5b813a75ef91f3ee4) · authored 2024-03-22T18:15:54Z. Actual parent(s): `8a2678eb324aa8d821b86a0ff4318acd69611df6`.

Author: **Vincent**.

Re-exports Event and ServerLoadEvent through public event module. Import ergonomics only; underlying bindings already exist.

First-parent changed paths: `python/src/endstone/event.py`.

Coverage: 10 canonical first-parent patch lines; 10 across all actual parents.

<a id="commit-496"></a>
### 496. feat(python): add default values for register_event_handler arguments in plugin module {#commit-496}

Source: [5bae2949240505c4c7acd874757ba23a33157fdd](https://github.com/EndstoneMC/endstone/commit/5bae2949240505c4c7acd874757ba23a33157fdd) · authored 2024-03-22T18:26:14Z. Actual parent(s): `f22a4d4af4aa8fcdf01851d5b813a75ef91f3ee4`.

Author: **Vincent**.

Adds normal-priority/false-ignore-cancelled Python defaults and changes C++ priority enum spelling to PascalCase while preserving numbers and uppercase Python names. Generated signature defaults catch up in 498. Public C++ spelling migration is distinct from unchanged runtime order.

First-parent changed paths: `include/endstone/event/event_priority.h`, `include/endstone/plugin/plugin.h`, `src/endstone_python/event.cpp`, `src/endstone_python/plugin.cpp`.

Coverage: 101 canonical first-parent patch lines; 101 across all actual parents.

<a id="commit-498"></a>
### 498. refactor: using py::overload_cast on template functions is redundant {#commit-498}

Source: [2c6f9263f075a11c11f1a746b2bfb16bf56b61ae](https://github.com/EndstoneMC/endstone/commit/2c6f9263f075a11c11f1a746b2bfb16bf56b61ae) · authored 2024-03-22T19:26:35Z. Actual parent(s): `65a9a47ecb109f880621875e6dfc1077d68aceab`.

Author: **Vincent**.

Removes redundant py::overload_cast around explicitly specialized registration template and updates generated stub defaults to match 496. Same selected callable and runtime defaults; verified source simplification.

First-parent changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/plugin.cpp`.

Coverage: 31 canonical first-parent patch lines; 31 across all actual parents.

<a id="commit-499"></a>
### 499. refactor: rename registerEventHandler to registerEvent in Plugin class {#commit-499}

Source: [49c13d27e47caf1a7d35126bc12e783506641e06](https://github.com/EndstoneMC/endstone/commit/49c13d27e47caf1a7d35126bc12e783506641e06) · authored 2024-03-23T12:51:35Z. Actual parent(s): `2c6f9263f075a11c11f1a746b2bfb16bf56b61ae`.

Author: **Vincent**.

Renames C++ Plugin registerEventHandler to registerEvent, but also accidentally changes member-function pointer parameter to pointer-to-member-function-pointer. Ordinal 502 repairs that extra star. Python binding still targets old name until 500 removes it; do not call this purely behavior-preserving.

First-parent changed paths: `include/endstone/plugin/plugin.h`.

Coverage: 26 canonical first-parent patch lines; 26 across all actual parents.

<a id="commit-500"></a>
### 500. refactor: update python bindings {#commit-500}

Source: [fc86211238664cffc1addcd1eda2b2b74c3a6a9b](https://github.com/EndstoneMC/endstone/commit/fc86211238664cffc1addcd1eda2b2b74c3a6a9b) · authored 2024-03-23T12:58:21Z. Actual parent(s): `49c13d27e47caf1a7d35126bc12e783506641e06`.

Author: **Vincent**.

Removes the ServerLoadEvent-only Plugin Python registration binding and macro rather than just renaming it. Generic manager registration remains, and decorator-based facade replaces the specialized entry in 501–504. Generated stub removal follows 503.

First-parent changed paths: `src/endstone_python/plugin.cpp`.

Coverage: 27 canonical first-parent patch lines; 27 across all actual parents.

<a id="commit-501"></a>
### 501. feat: add event_handler decorator {#commit-501}

Source: [c5a5a1aa8487bf796619ec337a80e20a3bd98fd8](https://github.com/EndstoneMC/endstone/commit/c5a5a1aa8487bf796619ec337a80e20a3bd98fd8) · authored 2024-03-23T12:58:35Z. Actual parent(s): `fc86211238664cffc1addcd1eda2b2b74c3a6a9b`.

Author: **Vincent**.

Introduces event_handler decorator supporting bare and configured use. It annotates the original function with marker/priority/cancellation attributes; it does not register anything or wrap execution itself. Actual discovery follows 503.

First-parent changed paths: `python/src/endstone/event.py`.

Coverage: 22 canonical first-parent patch lines; 22 across all actual parents.

<a id="commit-502"></a>
### 502. fix: registerEvent signature {#commit-502}

Source: [76babceb43e442fc5029111457f4caddf16ff109](https://github.com/EndstoneMC/endstone/commit/76babceb43e442fc5029111457f4caddf16ff109) · authored 2024-03-23T17:11:22Z. Actual parent(s): `c5a5a1aa8487bf796619ec337a80e20a3bd98fd8`.

Author: **Vincent**.

Repairs the extra pointer level introduced by 499 in the member callback signature. Restores original member-function invocation contract; no independent algorithm or test.

First-parent changed paths: `include/endstone/plugin/plugin.h`.

Coverage: 13 canonical first-parent patch lines; 13 across all actual parents.

<a id="commit-503"></a>
### 503. feat: add 'register_events' method to automatically register events from an 'event_handler' decorator {#commit-503}

Source: [03e79b753a3b7aa1b428404d16a138c9df8d8b28](https://github.com/EndstoneMC/endstone/commit/03e79b753a3b7aa1b428404d16a138c9df8d8b28) · authored 2024-03-23T21:33:04Z. Actual parent(s): `76babceb43e442fc5029111457f4caddf16ff109`.

Author: **Vincent**.

Adds Plugin.register_events scanning callable marked attributes, requiring one bound parameter with class annotation, then routing via annotation name. Deletes Event copy operations and adapts Python callback conversion explicitly through Event pointers, preserving shared mutable event identity rather than relying on reference conversion. The first discovery version lacks Event-subclass checks and NAME routing; 504 adds them. No automatic call from Plugin.__init__ is added; users must register.

First-parent changed paths: `include/endstone/event/event.h`, `include/endstone/plugin/plugin_manager.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/plugin.py`, `src/endstone_python/plugin.cpp`.

Coverage: 113 canonical first-parent patch lines; 113 across all actual parents.

<a id="commit-504"></a>
### 504. feat: add more checks in register_events method {#commit-504}

Source: [07371848f22c180fed87db59520d15f375edd646](https://github.com/EndstoneMC/endstone/commit/07371848f22c180fed87db59520d15f375edd646) · authored 2024-03-23T22:58:20Z. Actual parent(s): `03e79b753a3b7aa1b428404d16a138c9df8d8b28`.

Author: **Vincent**.

Requires enabled plugin and non-null listener, rejects handlers unless their sole annotation is an actual Event subclass, and prefers class NAME with class-name fallback. Direct inspect.signature annotations mean postponed/string annotations are not resolved. dir/getattr may evaluate descriptors, and repeated calls can register duplicates. Removing redundant ServerLoadEvent cancellable binding retains inherited behavior. These are bounded discovery contracts, not tested failures.

First-parent changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/plugin.py`, `src/endstone_python/event.cpp`.

Coverage: 92 canonical first-parent patch lines; 92 across all actual parents.

<a id="commit-506"></a>
### 506. feat: add PluginEnableEvent and PluginDisableEvent {#commit-506}

Source: [60e65ab35c064aec0e3bcc4b6ff34ab5f99f2fc4](https://github.com/EndstoneMC/endstone/commit/60e65ab35c064aec0e3bcc4b6ff34ab5f99f2fc4) · authored 2024-03-24T12:26:50Z. Actual parent(s): `d98b7a1766f9871301c0f061af174d2a7bf334df`.

Author: **Vincent**.

Adds borrowed-plugin lifecycle events and emits them after setEnabled completes its callback. Enabled listeners can observe their own enable event; disabled-plugin filtering means the target does not receive its own disable event. Events are noncancellable notifications, not vetoes. Callback failure/exception semantics still follow existing loader and Python trampoline handling.

First-parent changed paths: `include/endstone/event/server/plugin_disable_event.h`, `include/endstone/event/server/plugin_enable_event.h`, `include/endstone/event/server/server_load_event.h`, `include/endstone/plugin/plugin_loader.h`.

Coverage: 166 canonical first-parent patch lines; 166 across all actual parents.

<a id="commit-507"></a>
### 507. feat: add PluginEnableEvent and PluginDisableEvent {#commit-507}

Source: [3d0cdff650d360578b935be30ff38a4ed6728f7b](https://github.com/EndstoneMC/endstone/commit/3d0cdff650d360578b935be30ff38a4ed6728f7b) · authored 2024-03-24T12:36:30Z. Actual parent(s): `60e65ab35c064aec0e3bcc4b6ff34ab5f99f2fc4`.

Author: **Vincent**.

Binds lifecycle event construction and plugin access, exports them publicly, and forward-creates Event/Priority wrappers locally so plugin types can be initialized before concrete event bindings. Removes redundant concrete accessors inherited from Event. Borrowed plugin lifetime is not extended by the event constructor; no lifecycle callback tests.

First-parent changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/event.py`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/event.cpp`.

Coverage: 174 canonical first-parent patch lines; 174 across all actual parents.

<a id="commit-508"></a>
### 508. feat: improve asynchronous event handling in PluginManager {#commit-508}

Source: [4d35685c756e11c5129c4374cc0249509f8fd67c](https://github.com/EndstoneMC/endstone/commit/4d35685c756e11c5129c4374cc0249509f8fd67c) · authored 2024-03-25T10:23:55Z. Actual parent(s): `3d0cdff650d360578b935be30ff38a4ed6728f7b`.

Author: **Vincent**.

Implements two previously planned dispatch guards using native assigned-server-thread identity: async events on server thread and synchronous events off it are logged and dropped. No scheduling or synchronized-nesting check is implemented. Async worker dispatch remains allowed while manager event-map synchronization is unchanged. Native threading layout/API introduces a host dependency into core manager, moved behind Server in 509.

First-parent changed paths: `include/bedrock/threading.h`, `src/endstone_core/plugin/plugin_manager.cpp`, `src/endstone_runtime/bedrock/threading.cpp`.

Coverage: 108 canonical first-parent patch lines; 108 across all actual parents.

<a id="commit-532"></a>
### 532. feat(python): add bindings for weather events {#commit-532}

Source: [f0f653a50b9d649f52816e9f589bfc8aa680468f](https://github.com/EndstoneMC/endstone/commit/f0f653a50b9d649f52816e9f589bfc8aa680468f) · authored 2024-03-26T15:50:59Z. Actual parent(s): `588b22a142f23a15add7b80c09d6b5a971db8cc2`.

Author: **Vincent**.

Adds Python weather event queries, but also removes constructors for all previously constructible concrete server/plugin events. Python now observes framework-originated events rather than manufacturing these native event instances. Weather types are bound directly under Event; world property remains TODO. This public constructor removal is substantive despite an additive title.

First-parent changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/event.py`, `src/endstone_python/event.cpp`.

Coverage: 128 canonical first-parent patch lines; 128 across all actual parents.

<a id="commit-557"></a>
### 557. fix: correct python bindings of `NOT_OP` enum in permissions.cpp {#commit-557}

Source: [692e85ea83b83346c3978075a50caf539ca5e346](https://github.com/EndstoneMC/endstone/commit/692e85ea83b83346c3978075a50caf539ca5e346) · authored 2024-04-04T14:17:31Z. Actual parent(s): `a9f30d23933d92ad61a3abc3ca797192b2fbe0fd`.

Author: **Vincent**.

Fixes Python NOT_OP alias to NotOperator, resolving the exact mismatch introduced at378 and retained through prior480. NOT_OPERATOR already mapped correctly. A one-line repair changes authorization defaults chosen by normalized Python string; generated stub equality is not the correctness criterion.

First-parent changed paths: `src/endstone_python/permissions.cpp`.

Coverage: 13 canonical first-parent patch lines; 13 across all actual parents.

<a id="commit-588"></a>
### 588. feat(python): add bindings for Level class {#commit-588}

Source: [f504a876f31c19978bf98762e622a72c892e156a](https://github.com/EndstoneMC/endstone/commit/f504a876f31c19978bf98762e622a72c892e156a) · authored 2024-04-06T19:29:56Z. Actual parent(s): `4f3cb37afdefb8fb39b12907441c4e8ca6da1906`.

Author: **Vincent**.

Binds Level name/time and Server levels/get_level, exports Python level module, updates stubs for weather level and earlier NOT_OP/Spectator corrections. Explicit borrowed policies for server returns preserve native ownership; get_level stub omits optionality despite native nullptr-on-miss. Existing Server.name still calls getVersion. Generated stub updates are evidence of API surface, not independent host validation.

First-parent changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/level.py`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/event.cpp`, `src/endstone_python/level.cpp`, `src/endstone_python/server.cpp`.

Coverage: 207 canonical first-parent patch lines; 207 across all actual parents.
