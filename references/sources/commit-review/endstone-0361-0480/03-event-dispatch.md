<!-- retrieval: {"source_ids":["public:commit:05c4338995e1ed2ed9586c87f71d03ef41dd73d1","public:commit:237543714729b3dc53423f5d3f8485d1187eae5d","public:commit:4f899135573bda8d1296f8277a863bb1f8a89baa","public:commit:4fcbbcd3af8f3d30f2bf87ea0ebbbadf360b5a28","public:commit:50cd25fd74b4b2a66e5fb106cb6136d47d2566fb","public:commit:5554319ee926d4806ef7961c8787536ea100bce8","public:commit:765f35d3725b094ba5df1081d8b332f7b88ea3e8","public:commit:778c7fcaf7de85bced10ff35eac5008dad845d34","public:commit:827ecafa413dc37f9e3ac0ea81f6af5a05477fdd","public:commit:8bd2fa26308b1f6687e6a09660d8ad56d9a5f86f","public:commit:9127d0814ac8fbfa5f7ea806f24485e9a90e24b0","public:commit:968c683d5953e63a2345168d847ca949d247ede2","public:commit:a064f7f367fd9f8291cd9907ea685c6abe4919e8","public:commit:a0eb5076e7cbc6cc18e6abd522ad0c1c313e267e","public:commit:cdde83e30610be02912bef31421d0fae5224b7b4","public:commit:e4c7a22d1f5ea98b75d93b4fc12aaa03c34e91be","public:commit:eb7774a50bd402b0fb551548929c20588e7908ab"],"source_type":"public","date":"2024-03-21..2024-03-22","topics":["lifetime","concurrency","ffi","testing","performance","api","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Event architecture in progress: ownership, ordering and dispatch responsibility {#event-architecture-in-progress-ownership-ordering-and-dispatch-responsibility}

## Endpoint result: abstractions exist, manager dispatch does not yet run {#endpoint-result-abstractions-exist-manager-dispatch-does-not-yet-run}

The 21–22 March 2024 sequence begins event support and repeatedly reallocates responsibility among Event, EventListener/EventHandler, HandlerList and PluginManager. At ordinal 480, event values, cancellation, priorities, handler execution and a handler container exist, but concrete manager registration and dispatch remain TODO bodies. No native command hook emits ServerCommandEvent and no Python event API is added in this range. This unfinished endpoint is important: a broad feature title or callable public method must not be mistaken for operational event support.

The unit is bounded at 480, so the next implementation step is unknown here. The chronology below follows verified parent links. It preserves intermediate designs without treating temporary compile/interface mismatches as mature architectural choices.

## Priority is a contract distinct from an enum {#priority-is-a-contract-distinct-from-an-enum}

464 defines six priorities from Lowest through Monitor and documents low-to-high execution. Monitor is described as observing results without modifying the event. That is a usage convention: callbacks still receive a mutable Event reference, and the type system or dispatcher does not enforce a read-only Monitor view.

468's first HandlerList uses a greater comparator, so its map traversal is high-to-low, contrary to the documentation. 478 switches to an ascending map when replacing the templated container. The change therefore both refactors representation and corrects the documented order. Within a priority, vectors preserve registration sequence. No test asserts priority order or same-priority stability, and the manager has no functional registration path at this endpoint.

471 only wraps comments/whitespace and receives a short mechanical disposition. It does not become an independent lesson about event ordering merely because it touches priority documentation.

## Cancellation moves from a subclass into the common event interface {#cancellation-moves-from-a-subclass-into-the-common-event-interface}

465 gives Event a name, asynchronous-construction flag and Result enum describing deny/default/allow. Result is not wired into host action handling here. 466 introduces a separate CancellableEvent with its own cancellation state, but does not expose an asynchronous forwarding constructor.

467 moves cancellation state into Event, guarded by virtual isCancellable, and makes the asynchronous query nonvirtual. For a brief intermediate state the old subclass still has its own cancellation methods and state. Access through the base and through the subclass can therefore differ. 470 removes that redundant abstraction when introducing ServerCommandEvent. 473 makes isCancellable pure virtual, requiring each concrete event to state its policy explicitly.

At the endpoint, setCancelled is a no-op for noncancellable events, and isCancelled reports false for them. A handler may choose to skip already-cancelled events, but cancellation does not inherently stop delivery to every later handler. Nor does setting the flag itself cancel a server operation: the eventual native emission/consumption path must inspect it. That path is absent in this assignment. This distinction between event-state mutation and host-action enforcement is directly supported by the code.

## Dispatch first belongs to the event, then is removed from it {#dispatch-first-belongs-to-the-event-then-is-removed-from-it}

467 adds a pure dispatch operation. 468 gives a templated HandlerList a loop over listeners, and 469 makes PluginManager.callEvent forward to the event's dispatch. 470's ServerCommandEvent owns a HandlerList per event instance and uses it for that dispatch. There is no corresponding registration path populating the list. A newly created event does not gain subscribers merely because it contains a container.

475 adds a string-keyed registerEvent API to the manager, but its implementation is empty except for a TODO. 476 renames getEventName to getName; ServerCommandEvent remains on the old override until 479. 477 changes EventListener to a non-template EventHandler, with dependent include/container changes following in 478–479. Those staggered edits are explicit source-compatibility transitions, not evidence that every individual commit is independently buildable.

479 removes Event.dispatch and ServerCommandEvent's per-instance list. It also removes the manager's forwarding call, leaving callEvent with only planned checks. This is a transfer of architectural responsibility awaiting a centralized implementation, not a behavior-preserving rename. The direction toward a manager-owned registry is an inference from the removed per-event state and the new manager registration surface; no complete registry exists yet to establish its final design.

## Handler execution, filtering and identity {#handler-execution-filtering-and-identity}

473 implements a listener as an owned std::function callback, priority, borrowed Plugin reference and ignore_cancelled flag. It skips a cancellable event that is already cancelled only when that flag is true. It does not itself test whether the plugin remains enabled, hold the plugin alive or catch callback exceptions. These responsibilities could be supplied by a later manager or lifecycle protocol, but are not demonstrated here. 474 repairs the list's invocation name to match this implementation.

480 adds a string event-name discriminator to the now type-erased handler before cancellation filtering. This allows one common Event reference signature instead of a compile-time handler specialization for each event type. It also makes name identity part of the routing contract: two different concrete event types reporting the same string are indistinguishable at this layer. No dynamic type validation or namespace mechanism is supplied by this patch. This is a tradeoff in the observed representation, not a claim that string-based routing is inherently wrong.

ServerCommandEvent borrows its CommandSender and owns a mutable command string. A comment explicitly considers whether to use an Endstone Command instead. The string representation can describe an unparsed or rewritten console input; the typed representation would need a different relationship to command resolution. That latter comparison is an inference about the alternatives, while the open question itself is source evidence. The callback must not outlive the borrowed sender without an additional lifetime contract. No asynchronous console dispatch is shown.

## Cached handler snapshots and synchronization boundaries {#cached-handler-snapshots-and-synchronization-boundaries}

478 changes HandlerList to unique ownership of EventHandler objects grouped by priority. Registration/removal and lazy cache access hold a mutex. A dirty flag avoids repeatedly flattening the priority map into a vector; getHandlers returns a copy of that vector of raw pointers. Removing a particular handler or all handlers belonging to a plugin invalidates the cache.

The mutex protects container operations and cache rebuilding, but it is released before a caller uses the returned pointers. Concurrent unregister can destroy an object present in an earlier snapshot. Thus the source does not establish a safe concurrent callback-execution protocol merely by using a mutex. A correct future design could choose serialized dispatch/unregistration, retained snapshot ownership, deferred reclamation or another explicit lifetime strategy; none of those alternatives is implemented or claimed as an author preference in this range.

The returned vector is also copied on each call, even when flattening is cached. The optimization avoids rebuilding the ordered pointer sequence, not every allocation or copy. No benchmark quantifies its value, and no stress test validates callback mutation during iteration. Keeping these exact boundaries is more useful than describing the structure generically as a thread-safe event bus.

## Async metadata and explicit unimplemented constraints {#async-metadata-and-explicit-unimplemented-constraints}

472 records intended checks relating isAsynchronous to the server thread and synchronized code. These are comments, not guards or scheduling. They remain visible in the final no-op callEvent body. A flag on Event tells a future dispatcher what policy to apply; it does not move execution to another thread. The unit contains no queue, executor or thread handoff implementing that policy.

A future reviewer should therefore carry forward four open contracts: where event names map to handler lists, how plugin disable/unload unregisters handlers, how returned snapshots remain alive during callback execution, and where thread-affinity/cancellation is enforced at native call sites. These are known gaps at a historical boundary, not invented requirements for this research to implement.

## Evidence and application {#evidence-and-application}

All seventeen event-family commits were read fully. The only mechanical edit is comment wrapping; API additions with empty bodies remain semantic scaffolding and are not counted as completed dispatch. No tests were added for ordering, cancellation, callback exceptions, plugin lifetime, async restrictions or native command rewriting, and no upstream code was executed.

The portable engineering insight is to track responsibility and completion separately: a documented priority, event state flag, public registration signature, mutex-protected container and native interception hook each solve different parts of a system. This sequence is useful precisely because it exposes those parts arriving separately and being revised, rather than presenting an endpoint as a finished event architecture.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-464"></a>
### 464. feat: add EventPriority enums {#commit-464}

Source: [eb7774a50bd402b0fb551548929c20588e7908ab](https://github.com/EndstoneMC/endstone/commit/eb7774a50bd402b0fb551548929c20588e7908ab) · authored 2024-03-21T16:42:19Z · parent `5a7f4a2b4136fb490b481fdcee065a37768917f5`.

Author: **Vincent**.

Defines six event priorities with documented low-to-high execution and Monitor as observe-only convention. Enum alone enforces neither ordering nor mutation restrictions; initial 468 comparator contradicts documented order until 478.

Changed paths: `include/endstone/event/event_priority.h`.

Coverage: 60 canonical patch lines; 1 changed paths.

<a id="commit-465"></a>
### 465. feat: add Event base class {#commit-465}

Source: [778c7fcaf7de85bced10ff35eac5008dad845d34](https://github.com/EndstoneMC/endstone/commit/778c7fcaf7de85bced10ff35eac5008dad845d34) · authored 2024-03-21T16:47:33Z · parent `eb7774a50bd402b0fb551548929c20588e7908ab`.

Author: **Vincent**.

Introduces abstract Event name, async construction flag and Result enum. Result describes deny/default/allow semantics but is not connected to dispatch or any host action here. Async is metadata, not scheduling implementation.

Changed paths: `include/endstone/event/event.h`.

Coverage: 72 canonical patch lines; 1 changed paths.

<a id="commit-466"></a>
### 466. feat: add CancellableEvent class {#commit-466}

Source: [765f35d3725b094ba5df1081d8b332f7b88ea3e8](https://github.com/EndstoneMC/endstone/commit/765f35d3725b094ba5df1081d8b332f7b88ea3e8) · authored 2024-03-21T16:51:11Z · parent `778c7fcaf7de85bced10ff35eac5008dad845d34`.

Author: **Vincent**.

Adds separate CancellableEvent with own bool state and cancellation accessors. No async-forwarding constructor and no server cancellation enforcement.467 moves cancellation into base while subclass remains briefly, then 470 removes duplicate abstraction.

Changed paths: `include/endstone/event/cancellable_event.h`.

Coverage: 60 canonical patch lines; 1 changed paths.

<a id="commit-467"></a>
### 467. feat: add dispatch and cancel functions to Event class {#commit-467}

Source: [8bd2fa26308b1f6687e6a09660d8ad56d9a5f86f](https://github.com/EndstoneMC/endstone/commit/8bd2fa26308b1f6687e6a09660d8ad56d9a5f86f) · authored 2024-03-21T18:05:04Z · parent `765f35d3725b094ba5df1081d8b332f7b88ea3e8`.

Author: **Vincent**.

Adds pure dispatch to Event, base cancellation state guarded by virtual isCancellable and nonvirtual async query. This tries polymorphic cancellation without casting separate subclass. Existing CancellableEvent temporarily has separate shadowed cancellation methods/state, so base/derived access can differ until 470 deletion.

Changed paths: `include/endstone/event/event.h`.

Coverage: 90 canonical patch lines; 1 changed paths.

<a id="commit-468"></a>
### 468. feat: add EventListener and HandlerList {#commit-468}

Source: [50cd25fd74b4b2a66e5fb106cb6136d47d2566fb](https://github.com/EndstoneMC/endstone/commit/50cd25fd74b4b2a66e5fb106cb6136d47d2566fb) · authored 2024-03-21T18:05:22Z · parent `8bd2fa26308b1f6687e6a09660d8ad56d9a5f86f`.

Author: **Vincent**.

Creates templated EventListener placeholder and HandlerList dispatching priority map vectors. Comparator greater orders high priorities first, opposite documented low-first order; no registration API yet. Types are scaffolding, not functioning plugin subscription.

Changed paths: `include/endstone/event/event_listener.h`, `include/endstone/event/handler_list.h`.

Coverage: 89 canonical patch lines; 2 changed paths.

<a id="commit-469"></a>
### 469. feat: add callEvent method to PluginManager {#commit-469}

Source: [a064f7f367fd9f8291cd9907ea685c6abe4919e8](https://github.com/EndstoneMC/endstone/commit/a064f7f367fd9f8291cd9907ea685c6abe4919e8) · authored 2024-03-21T18:05:56Z · parent `50cd25fd74b4b2a66e5fb106cb6136d47d2566fb`.

Author: **Vincent**.

Adds manager callEvent forwarding to event-owned dispatch, with explicit incomplete-implementation TODO. This assigns dispatch responsibility to each event object initially;479 removes that design before replacement manager dispatch exists.

Changed paths: `include/endstone/detail/plugin/plugin_manager.h`, `include/endstone/plugin/plugin_manager.h`, `src/endstone_core/plugin/plugin_manager.cpp`.

Coverage: 58 canonical patch lines; 3 changed paths.

<a id="commit-470"></a>
### 470. feat: add ServerCommandEvent {#commit-470}

Source: [5554319ee926d4806ef7961c8787536ea100bce8](https://github.com/EndstoneMC/endstone/commit/5554319ee926d4806ef7961c8787536ea100bce8) · authored 2024-03-21T18:08:41Z · parent `a064f7f367fd9f8291cd9907ea685c6abe4919e8`.

Author: **Vincent**.

Adds ServerCommandEvent borrowing sender, owning mutable command string, marking cancellable and owning its own templated HandlerList. Removes separate CancellableEvent now replaced by base state. Per-instance handler list has no registration path and no native command hook fires this event yet; TODO asks string versus Command representation.

Changed paths: `include/endstone/event/cancellable_event.h`, `include/endstone/event/server/server_command_event.h`.

Coverage: 147 canonical patch lines; 2 changed paths.

<a id="commit-471"></a>
### 471. style: code formatting {#commit-471}

Source: [a0eb5076e7cbc6cc18e6abd522ad0c1c313e267e](https://github.com/EndstoneMC/endstone/commit/a0eb5076e7cbc6cc18e6abd522ad0c1c313e267e) · authored 2024-03-21T18:08:49Z · parent `5554319ee926d4806ef7961c8787536ea100bce8`.

Author: **Vincent**.

Whitespace/comment wrapping only in priority docs. Execution order and values unchanged.

Changed paths: `include/endstone/event/event_priority.h`.

Coverage: 22 canonical patch lines; 1 changed paths.

<a id="commit-472"></a>
### 472. docs: add todos {#commit-472}

Source: [4fcbbcd3af8f3d30f2bf87ea0ebbbadf360b5a28](https://github.com/EndstoneMC/endstone/commit/4fcbbcd3af8f3d30f2bf87ea0ebbbadf360b5a28) · authored 2024-03-21T18:20:46Z · parent `a0eb5076e7cbc6cc18e6abd522ad0c1c313e267e`.

Author: **Vincent**.

Records intended thread-affinity checks for synchronous/asynchronous event calls but adds no guards. Preserve as explicit design constraint still pending at 480, not proof events are scheduled or synchronized.

Changed paths: `src/endstone_core/plugin/plugin_manager.cpp`.

Coverage: 16 canonical patch lines; 1 changed paths.

<a id="commit-473"></a>
### 473. feat: implement EventListener {#commit-473}

Source: [827ecafa413dc37f9e3ac0ea81f6af5a05477fdd](https://github.com/EndstoneMC/endstone/commit/827ecafa413dc37f9e3ac0ea81f6af5a05477fdd) · authored 2024-03-22T10:44:10Z · parent `4fcbbcd3af8f3d30f2bf87ea0ebbbadf360b5a28`.

Author: **Vincent**.

Implements listener as owned std::function plus priority, borrowed plugin and ignore_cancelled flag. Skips already-cancelled cancellable event only when requested, otherwise invokes callback. Makes isCancellable pure to require explicit policy. Plugin enabled-state, exception boundary and lifetime are not enforced here; handler list call name repaired 474.

Changed paths: `include/endstone/event/event.h`, `include/endstone/event/event_listener.h`.

Coverage: 75 canonical patch lines; 2 changed paths.

<a id="commit-474"></a>
### 474. refactor: rename onEvent to callEvent {#commit-474}

Source: [cdde83e30610be02912bef31421d0fae5224b7b4](https://github.com/EndstoneMC/endstone/commit/cdde83e30610be02912bef31421d0fae5224b7b4) · authored 2024-03-22T10:44:35Z · parent `827ecafa413dc37f9e3ac0ea81f6af5a05477fdd`.

Author: **Vincent**.

Changes handler-list invocation from onEvent to callEvent to match 473 implementation. Completes adjacent interface rename without changing priority order or cancellation rules.

Changed paths: `include/endstone/event/handler_list.h`.

Coverage: 13 canonical patch lines; 1 changed paths.

<a id="commit-475"></a>
### 475. feat: add registerEvent function to PluginManager {#commit-475}

Source: [4f899135573bda8d1296f8277a863bb1f8a89baa](https://github.com/EndstoneMC/endstone/commit/4f899135573bda8d1296f8277a863bb1f8a89baa) · authored 2024-03-22T11:28:36Z · parent `cdde83e30610be02912bef31421d0fae5224b7b4`.

Author: **Vincent**.

Adds string-keyed registerEvent API to manager, but concrete body remains TODO. This is callable surface with no registration effect, not completed event support. EventListener include remains until rename cleanup 479.

Changed paths: `include/endstone/detail/plugin/plugin_manager.h`, `include/endstone/plugin/plugin_manager.h`, `src/endstone_core/plugin/plugin_manager.cpp`.

Coverage: 78 canonical patch lines; 3 changed paths.

<a id="commit-476"></a>
### 476. refactor: rename getEventName to getName in Event class {#commit-476}

Source: [968c683d5953e63a2345168d847ca949d247ede2](https://github.com/EndstoneMC/endstone/commit/968c683d5953e63a2345168d847ca949d247ede2) · authored 2024-03-22T12:14:55Z · parent `4f899135573bda8d1296f8277a863bb1f8a89baa`.

Author: **Vincent**.

Renames abstract event identifier getEventName to getName; ServerCommandEvent override remains stale until 479. Preserve phased interface migration and source compatibility gap.

Changed paths: `include/endstone/event/event.h`.

Coverage: 13 canonical patch lines; 1 changed paths.

<a id="commit-477"></a>
### 477. refactor: rename EventListener class to EventHandler {#commit-477}

Source: [237543714729b3dc53423f5d3f8485d1187eae5d](https://github.com/EndstoneMC/endstone/commit/237543714729b3dc53423f5d3f8485d1187eae5d) · authored 2024-03-22T12:15:09Z · parent `968c683d5953e63a2345168d847ca949d247ede2`.

Author: **Vincent**.

Renames EventListener to EventHandler and removes template parameter, moving toward type-erased Event callbacks. Header/include and HandlerList updates follow 478/479. Same borrowed plugin/cancellation behavior retained; no RTTI-based filtering introduced.

Changed paths: `include/endstone/event/event_handler.h`, `include/endstone/event/event_listener.h`.

Coverage: 139 canonical patch lines; 2 changed paths.

<a id="commit-478"></a>
### 478. feat: implement thread-safe HandlerList {#commit-478}

Source: [05c4338995e1ed2ed9586c87f71d03ef41dd73d1](https://github.com/EndstoneMC/endstone/commit/05c4338995e1ed2ed9586c87f71d03ef41dd73d1) · authored 2024-03-22T12:15:28Z · parent `237543714729b3dc53423f5d3f8485d1187eae5d`.

Author: **Vincent**.

Replaces templated list with unique-owned handlers grouped by ascending priority, mutex-protected registration/removal and lazily baked raw-pointer snapshot cache. Fixes earlier descending order. Cache invalidation avoids repeated flattening, but returned pointers outlive lock and can dangle during concurrent unregister; thread-safe container operations do not prove safe callback execution. No event stress tests or snapshot ownership protocol.

Changed paths: `include/endstone/event/handler_list.h`.

Coverage: 120 canonical patch lines; 1 changed paths.

<a id="commit-479"></a>
### 479. refactor: remove dispatch function in Event class {#commit-479}

Source: [9127d0814ac8fbfa5f7ea806f24485e9a90e24b0](https://github.com/EndstoneMC/endstone/commit/9127d0814ac8fbfa5f7ea806f24485e9a90e24b0) · authored 2024-03-22T12:16:46Z · parent `05c4338995e1ed2ed9586c87f71d03ef41dd73d1`.

Author: **Vincent**.

Removes event-owned dispatch and per-instance HandlerList, repairs ServerCommandEvent getName and renamed include. Manager callEvent now does nothing except TODO comments, pending central dispatch implementation. This is architectural reallocation in progress, not equivalent behavior-preserving cleanup.

Changed paths: `include/endstone/event/event.h`, `include/endstone/event/server/server_command_event.h`, `src/endstone_core/plugin/plugin_manager.cpp`.

Coverage: 66 canonical patch lines; 3 changed paths.

<a id="commit-480"></a>
### 480. feat: update EventHandler to include event filtering {#commit-480}

Source: [e4c7a22d1f5ea98b75d93b4fc12aaa03c34e91be](https://github.com/EndstoneMC/endstone/commit/e4c7a22d1f5ea98b75d93b4fc12aaa03c34e91be) · authored 2024-03-22T12:32:43Z · parent `9127d0814ac8fbfa5f7ea806f24485e9a90e24b0`.

Author: **Vincent**.

Adds event-name filter to type-erased EventHandler before cancellation check and moves name/executor into storage. Routing uses string equality rather than C++ dynamic type, so same-name event identity must be controlled. Manager registration/dispatch remain unimplemented at this bounded endpoint; no native event emission or Python event bindings claimed.

Changed paths: `include/endstone/event/event_handler.h`.

Coverage: 43 canonical patch lines; 1 changed paths.
