<!-- retrieval: {"source_ids":["public:commit:029dd84fd950f239c819dc2f7f6674bfa38cdddc","public:commit:0593715942e33b30be1cf6260303023b7a00d1ca","public:commit:0b3415edeb204685d292fccd287aacfe52fab923","public:commit:0dab2f9c17314499fed508d360b210074baf6baa","public:commit:1b4a8a6543de08d2cf7ee7d38d3c21d155990508","public:commit:1cad477326254c865499d8ba8256b193e85d006f","public:commit:21769c7d61de789bc8754a7bf38b6ffbc06667cd","public:commit:3a32b5b2ea042b1ae920b973775d73e107ac145d","public:commit:61949822a8ea903a3e31670ccc35873be73967d5","public:commit:8d9433adccbd1ff33b7c8c8dbf4b6784916652b9","public:commit:93b8c2108e7e803f220eff30fee457d25969af97","public:commit:99419531745e1d4c5bc9e913cddb230aac643efe","public:commit:99d25471aa3e621e70671120f31e66c408d86aaf","public:commit:a34d754c7ca5ab996969852200d68e2ba7bd0b54","public:commit:a4fed3d2419df3ec7084655efb595a74d8d3625a","public:commit:b5a4beb39c30b465954759c35c9b97a7abe7f070","public:commit:be85283d64791459484505d5c761dae06c6e8fb2","public:commit:c2b325fe3e37394ef9ac5d165dec5697af262804","public:commit:c5355f140c3990423be49124950d5b6262094236","public:commit:c852ad42ec4de22b42bfb4d0fdc8f7a4738d2512","public:commit:d5d7954b7c6dd1940c2fbb9ba55056dcf651c8a9","public:commit:dd51f75ed6a90759d4a86fda55220c7e02d2b787","public:commit:e09da40a34350401c190392eaf564cbe82400ae7","public:commit:e9c1423d61df58aaded9d25a96ec9f599497dc2a"],"source_type":"public","date":"2024-04-19..2024-04-29","topics":["lifetime","concurrency","ffi","testing","api","diagnosis","documentation","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Events, permission initialization and broadcast {#events-permission-initialization-and-broadcast}

## Useful conclusion {#useful-conclusion}

This interval develops event support as a sequence of native interception experiments, not as a single uniform cancellation abstraction. Chat eventually modifies the native message and suppresses the original call when cancelled. Player/console command events suppress native execution when cancelled but do not forward a changed command string. Login cancellation requests a disconnect and then still calls native load. A caller must inspect the interception point and value write-back before relying on the public event setter or cancellable flag. This conclusion is a source-observed integration lesson, not an asserted author maxim.

Permission work is equally causal: constructor-time recalculation is tried, a shared-state lifecycle crash is reported, and initialization is moved to known server/player lifecycle points. A small reference-versus-copy fix then makes subscription indexing actually work. Broadcast is built on that repaired index plus a second permission check. The chain supports explicit initialization and secondary-index correctness as useful engineering concerns; it does not establish that all lifetime problems or permission semantics are resolved.

## Chat: resolve the actor once, mutate the value that native code will consume {#chat-resolve-the-actor-once-mutate-the-value-that-native-code-will-consume}

At721 the native ChatEvent mirror changes from opaque storage to message, sender weak context, recipient-related data and name.722 revises that recipient field into optional excluded recipients and hooks the script network event handler. It locks the sender registry via a borrowed WeakRef dereference, reconstructs EntityContext and looks up an actor. A successful player event can cancel with Deny/Deny. However, modified event text is only used in the console log; the native ChatEvent still contains the original text. The source also models a script handler virtual entry without an independent layout test.

723 removes that hook completely and intercepts ServerNetworkHandler::_displayGameMessage instead. Its arguments already include a Player, so no weak sender lookup is needed. The plugin event runs first, cancellation returns before native dispatch, and the approved text is copied into ChatEvent before calling original. This fixes the observable write-back gap. The getter returns a string by value, so moving that temporary does not empty the event's stored message; the subsequent log reads the same final text. The commit does not say why this hook was selected, so simpler direct player access is an inference from its arguments, not a quoted motive.

This also makes getEndstoneActor/getEndstonePlayer callable on const native objects while still lazily creating ECS wrapper components. Const here is not a promise of registry immutability. The implementation casts away the native object's constness to construct a wrapper, relying on the underlying host object actually being mutable and alive. Python724 exposes a borrowed player plus mutable message;734 repairs a copied join-event docstring. Neither binding extends native entity lifetime.

## Commands and login: similar interface, materially different semantics {#commands-and-login-similar-interface-materially-different-semantics}

731 mirrors native /say output to console after original delivery, using native localization.732 logs player commands before dispatch and retains the existing console event.734 adds the analogous player event, including mutable command and Python setter, but briefly leaves an unconditional cancellation statement after plugin dispatch.735 removes it four minutes later. That pair is a concrete counterexample to treating the feature-introduction SHA as independently usable. It is also the same kind of temporary forced-cancellation mistake observed in actor spawning685–686, but no shared causal explanation is established.

The endpoint command hook still forwards the original CommandContext. Neither player nor console event's changed command is written back. Cancellation is functional by returning CommandsDisabled; mutation is only a public surface at this point. Logging occurs before player event dispatch, so a cancelled attempt is still logged. Null origin-entity handling is assumed rather than guarded. These are bounded source consequences, not reproduced crashes or a request to audit every command path.

800 finally fills the login TODO retained since early player wrappers. It constructs PlayerLoginEvent before native _loadNewPlayer, lets plugins set kick text and cancel, then calls disconnectClient with the native identity/subclient and NoReason. Empty text selects skip-message. Crucially, the original load call is unconditional afterward. This might rely on native disconnected state being honored, but that behavior is not present in the mirror and has not been tested. It is inaccurate to summarize this as a proven transactional refusal before all loading work.801 binds the event with borrowed player lifetime and message setter. Endpoint full context confirms this ordering remains through840.

## Permission initialization: eager constructor, lazy shared state, explicit lifecycle {#permission-initialization-eager-constructor-lazy-shared-state-explicit-lifecycle}

738 recalculates Endstone permissions after native Player::setPermissions and before available-command resend. The wrapper's duplicate recalculation is removed740. The wrapper also gains an early return when requested operator state already matches, but retains the earlier reversed mapping: true selects Any while false selects GameDirectors, despite isOp meaning native level is not Any. Recalculation makes caches follow native state; it does not repair that state transformation.

740 adds recalculatePermissions inside PermissibleBase construction. This operation consults the global EndstoneServer and delegates isOp through the owner. Its prerequisites therefore exceed simple member initialization.742 explicitly attributes a crash to the shared permissible base outliving the server, then changes the namespace-static object into a function-local static. The observed implementation delays construction; it does not make the object server-owned or demonstrate a complete shutdown-order proof. The endpoint class has no custom destructor that calls clearPermissions. We cannot infer an exact destructor stack or conflate this report with the much earlier unknown shutdown failure137 or later GIL teardown309.

745 removes constructor recalculation and explicitly performs it after server initialization, after the join event, and in a one-time lazy unique_ptr initializer for generic actors.747 ensures actor construction reaches that initializer. This is a real revision away from eager constructor side effects. The generic actor permission object remains shared across generic actors, null-opable and static-duration. Humans/players retain their own permissible base. Join listeners run before the explicit post-join recalc; permission fallback can still consult registered defaults, so 'no permissions before join' would be too strong.

741 extracts clearPermissions and calls it before quit listeners and native disconnect. It removes subscription entries and effective permission records, but not attachment storage. A quit listener can also invoke APIs again, so this is an explicit protocol point rather than a proof that no late resubscription occurs. No automatic destructor cleanup is introduced. This distinction matters when transferring the design to entity-component ownership: lifetime delegation does not eliminate external indexes holding borrowed pointers.

743–745 rename the generic and concrete sender hierarchy in separate commits.743 deletes BaseCommandSender while ServerCommandSender still references it;744 moves delegation into ServerCommandSender;745 updates server and adapter consumers to the new ConsoleCommandSender/generic roles. Bodies mostly preserve behavior, but the intermediate commits are not complete standalone migrations. The console remains always-op and logs an error rather than changing its status.

## Broadcast depends on a repaired subscription index {#broadcast-depends-on-a-repaired-subscription-index}

739 registers admin/operator and user/true permission defaults.746 fixes two long-standing copies of nested maps to references, allowing permission/default subscriptions to persist. This is a direct continuation of the earlier343 implementation, not a new theory inferred from a title.747 exposes broadcast but leaves its loop as TODO.748 adds an explicit asCommandSender query: real command senders return themselves; a permissible delegate forwards its owner or returns null.749 then filters indexed candidates by both sender identity and hasPermission, deduplicates pointers and sends. Index membership alone is not treated as permission grant.

750 adds an event with mutable message and a read-only recipient snapshot. Broadcast loops the original recipient set after dispatch, and Python's STL conversion is not a supported mutable selection mechanism. The event is marked async when called off the server thread so it satisfies the existing dispatcher check. That flag does not lock event-handler registries, permission maps or native recipients. Endpoint context shows those maps remain unsynchronized; safe async use is not established by naming. Completion of a broadcast or retention of event wrappers also does not own the underlying players.

## Evidence limits and applicability {#evidence-limits-and-applicability}

All changes are authored/committed by Vincent in this interval. No PR discussion, alternative proposal from a collaborator, test result or performance measurement was read for these commits. Claimed reasons are limited to commit messages and inline comments; the library/native interfaces are dependency context, not evidence that Vincent designed their internals. Useful application: design tests that distinguish cancellation from value mutation and borrowed lifetime, initialize dependent services only after prerequisites exist, and verify secondary indexes with actual mutations. Counterexamples retained above prevent turning these changes into blanket endorsements.

Prior reviewed context: [permissions and early actor lifetime](../endstone-0601-0720/02-actor-player-lifecycle.md), earlier command/event integration. These are navigation to eligible Endstone history, not old Nukkit precedent.

## Individual source dispositions {#individual-source-dispositions}

<a id="commit-722"></a>
### 722 · feat: add PlayerChatEvent {#commit-722}

[0b3415edeb204685d292fccd287aacfe52fab923](https://github.com/EndstoneMC/endstone/commit/0b3415edeb204685d292fccd287aacfe52fab923) · 2024-04-19T11:46:15Z · Vincent (author and committer).

Introduces cancellable mutable PlayerChatEvent through ScriptServerNetworkEventHandler, resolves sender through weak registry/entity context, logs post-plugin message, denies native handling on cancellation. Does not copy modified message into native ChatEvent, so log and sent text can diverge. Chat exclude field becomes optional vector, placeholder type fixed; removes ScriptLevelGameplayHandler pure virtual destructor. Replaced723 rather than stabilized here.


<a id="commit-723"></a>
### 723 · feat: hook ServerNetworkHandler::_displayGameMessage for PlayerChatEvent {#commit-723}

[c2b325fe3e37394ef9ac5d165dec5697af262804](https://github.com/EndstoneMC/endstone/commit/c2b325fe3e37394ef9ac5d165dec5697af262804) · 2024-04-19T13:50:01Z · Vincent (author and committer).

Moves chat interception from script coordinator to ServerNetworkHandler::_displayGameMessage with direct native Player, avoiding manual weak sender resolution. Copies event message back before native call and returns early on cancellation. Actor/player wrapper getters become const while lazily mutating registry through const_cast. No explicit motive for hook choice; simpler sender access and restored message mutation are observed.


<a id="commit-724"></a>
### 724 · feat(python): add binding for PlayerChatEvent {#commit-724}

[99d25471aa3e621e70671120f31e66c408d86aaf](https://github.com/EndstoneMC/endstone/commit/99d25471aa3e621e70671120f31e66c408d86aaf) · 2024-04-19T13:59:17Z · Vincent (author and committer).

Exposes borrowed player and mutable chat message in Python binding/stub/facade. Player docstring mistakenly says joins server, corrected734; no separate Python event constructor.


<a id="commit-731"></a>
### 731 · feat: log message of `/say` command to console {#commit-731}

[c852ad42ec4de22b42bfb4d0fdc8f7a4738d2512](https://github.com/EndstoneMC/endstone/commit/c852ad42ec4de22b42bfb4d0fdc8f7a4738d2512) · 2024-04-23T12:25:14Z · Vincent (author and committer).

Hooks native /say message send, calls original then logs localized chat.type.announcement through I18n. Console observability added without replacing native delivery.


<a id="commit-732"></a>
### 732 · feat: log command issued by players to console {#commit-732}

[be85283d64791459484505d5c761dae06c6e8fb2](https://github.com/EndstoneMC/endstone/commit/be85283d64791459484505d5c761dae06c6e8fb2) · 2024-04-23T12:35:32Z · Vincent (author and committer).

Command hook now branches player/console/other origins, logs player commands and retains cancellable console event before common native forwarding. Player origin assumes non-null entity, rejects nonplayer entity by exception. Player preprocess event remains TODO. Console event mutation still not written to CommandContext.


<a id="commit-733"></a>
### 733 · docs: update documentations in server_command_event.h {#commit-733}

[93b8c2108e7e803f220eff30fee457d25969af97](https://github.com/EndstoneMC/endstone/commit/93b8c2108e7e803f220eff30fee457d25969af97) · 2024-04-23T12:46:30Z · Vincent (author and committer).

Clarifies console ServerCommandEvent getter wording from user to server; no behavioral change.


<a id="commit-734"></a>
### 734 · feat: add PlayerCommandEvent and its python bindings {#commit-734}

[029dd84fd950f239c819dc2f7f6674bfa38cdddc](https://github.com/EndstoneMC/endstone/commit/029dd84fd950f239c819dc2f7f6674bfa38cdddc) · 2024-04-23T12:47:57Z · Vincent (author and committer).

Adds cancellable mutable PlayerCommandEvent C++/Python facade/stub and hook, fixes chat player docstring. Unconditional event.setCancelled(true) after dispatch disables every handled player command in this intermediate SHA;735 removes it. Both player and console modified command values remain disconnected from original CommandContext.


<a id="commit-735"></a>
### 735 · fix: oops {#commit-735}

[8d9433adccbd1ff33b7c8c8dbf4b6784916652b9](https://github.com/EndstoneMC/endstone/commit/8d9433adccbd1ff33b7c8c8dbf4b6784916652b9) · 2024-04-23T12:51:17Z · Vincent (author and committer).

Removes unconditional player-command cancellation from734. Plugin-requested cancellation remains; no fix to command-string mutation forwarding.


<a id="commit-736"></a>
### 736 · refactor: remove `/debug` command {#commit-736}

[d5d7954b7c6dd1940c2fbb9ba55056dcf651c8a9](https://github.com/EndstoneMC/endstone/commit/d5d7954b7c6dd1940c2fbb9ba55056dcf651c8a9) · 2024-04-23T13:06:38Z · Vincent (author and committer).

Deletes built-in /debug registration, permission and implementation that toggled global logger level for console. Actual feature removal, no replacement or explicit reason in commit; not merely file cleanup.


<a id="commit-738"></a>
### 738 · feat: recalculate permissions when permission level is changed {#commit-738}

[e09da40a34350401c190392eaf564cbe82400ae7](https://github.com/EndstoneMC/endstone/commit/e09da40a34350401c190392eaf564cbe82400ae7) · 2024-04-23T16:28:34Z · Vincent (author and committer).

Recalculates permissions after native permission changes before resending commands; adds setOp no-op when already same and temporary duplicate recalc in wrapper. Existing inverted Any/GameDirectors assignment remains.740 removes duplicate; repeated same-value guard does not repair setter inversion.


<a id="commit-739"></a>
### 739 · feat: add default broadcast permissions {#commit-739}

[21769c7d61de789bc8754a7bf38b6ffbc06667cd](https://github.com/EndstoneMC/endstone/commit/21769c7d61de789bc8754a7bf38b6ffbc06667cd) · 2024-04-23T16:33:15Z · Vincent (author and committer).

Adds broadcast admin/operator and user/true default permission tree under shared root, derives childnames from parent and recalculates. Prepares subscription-based recipient selection, not broadcasting yet.


<a id="commit-740"></a>
### 740 · fix: call recalculatePermissions in PermissibleBase's constructor {#commit-740}

[61949822a8ea903a3e31670ccc35873be73967d5](https://github.com/EndstoneMC/endstone/commit/61949822a8ea903a3e31670ccc35873be73967d5) · 2024-04-23T17:35:19Z · Vincent (author and committer).

Moves recalculation into PermissibleBase constructor and removes duplicate wrapper recalc from738. This eagerly accesses global server/virtual operator state during owner construction;745 explicitly relocates initialization to lifecycle points. No runtime failure claim beyond later742 message.


<a id="commit-741"></a>
### 741 · fix: clear permissions on player disconnect {#commit-741}

[c5355f140c3990423be49124950d5b6262094236](https://github.com/EndstoneMC/endstone/commit/c5355f140c3990423be49124950d5b6262094236) · 2024-04-23T17:39:52Z · Vincent (author and committer).

Extracts clearPermissions unsubscribe/default cleanup and invokes player disconnect cleanup before PlayerQuitEvent and native disconnect. Attachments remain stored; effective permission entries/subscriptions cleared. Teardown protocol explicit rather than destructor-driven; quit handlers can observe cleared permissions.


<a id="commit-742"></a>
### 742 · fix: crash due to the lifecycle of shared permissible base outlives the lifecycle of server instance {#commit-742}

[b5a4beb39c30b465954759c35c9b97a7abe7f070](https://github.com/EndstoneMC/endstone/commit/b5a4beb39c30b465954759c35c9b97a7abe7f070) · 2024-04-23T21:05:06Z · Vincent (author and committer).

Explicitly reports crash because shared permissible base outlives server. Replaces namespace static with function-local static, delaying construction until use. Shared generic-actor state remains and destruction is still static-duration; source does not prove complete shutdown-order solution.745 adds lazy unique_ptr initializer with explicit recalc. Keep reported cause separate from inferred initialization-order benefit.


<a id="commit-743"></a>
### 743 · refactor: rename ServerCommandSender to ConsoleCommandSender {#commit-743}

[1b4a8a6543de08d2cf7ee7d38d3c21d155990508](https://github.com/EndstoneMC/endstone/commit/1b4a8a6543de08d2cf7ee7d38d3c21d155990508) · 2024-04-23T21:06:34Z · Vincent (author and committer).

First half of sender rename moves console behavior to ConsoleCommandSender while deleting BaseCommandSender source/header. Existing ServerCommandSender still references removed base until744; downstream adapters/server change745. Behavior bodies preserved, intermediate source not independently complete.


<a id="commit-744"></a>
### 744 · refactor: rename BaseCommandSender to ServerCommandSender {#commit-744}

[1cad477326254c865499d8ba8256b193e85d006f](https://github.com/EndstoneMC/endstone/commit/1cad477326254c865499d8ba8256b193e85d006f) · 2024-04-23T21:06:55Z · Vincent (author and committer).

Second half renames generic BaseCommandSender to ServerCommandSender, restoring delegation implementations and making console subclass responsible for name/operator/log output. Constructors retain by-value PermissibleBase option; final adapters updated745.


<a id="commit-745"></a>
### 745 · fix: add missing calls to recalculatePermissions {#commit-745}

[0593715942e33b30be1cf6260303023b7a00d1ca](https://github.com/EndstoneMC/endstone/commit/0593715942e33b30be1cf6260303023b7a00d1ca) · 2024-04-23T21:53:43Z · Vincent (author and committer).

Completes sender hierarchy uses; removes eager PermissibleBase constructor recalc and calls explicitly after server initialization, after join event, and once in lazy shared actor unique_ptr initializer. This places server-dependent work after availability, but generic state remains shared/static and player join listeners run before this recalc. Native permission-change hook remains.


<a id="commit-746"></a>
### 746 · fix: subscribeToPermission and subscribeToDefaultPerms has no effect {#commit-746}

[99419531745e1d4c5bc9e913cddb230aac643efe](https://github.com/EndstoneMC/endstone/commit/99419531745e1d4c5bc9e913cddb230aac643efe) · 2024-04-23T22:20:56Z · Vincent (author and committer).

Fixes subscription-map copies to references in permission and default-permission registration, making registrations persist. Direct repair of343-era bug observed earlier. This enables later broadcast lookup and default-change invalidation; no tests added.


<a id="commit-747"></a>
### 747 · feat: add broadcast function to Server class {#commit-747}

[e9c1423d61df58aaded9d25a96ec9f599497dc2a](https://github.com/EndstoneMC/endstone/commit/e9c1423d61df58aaded9d25a96ec9f599497dc2a) · 2024-04-23T22:46:47Z · Vincent (author and committer).

Adds Server broadcast/broadcastMessage API and mocks, moves getters unchanged, forces shared actor permission initialization in constructor. Broadcast body only enumerates subscriptions with TODO, no sends yet. New public virtuals and reordering alter C++ interface; Python Server broadcast binding not added in this diff.


<a id="commit-748"></a>
### 748 · feat: add asCommandSender function to Permissible {#commit-748}

[a4fed3d2419df3ec7084655efb595a74d8d3625a](https://github.com/EndstoneMC/endstone/commit/a4fed3d2419df3ec7084655efb595a74d8d3625a) · 2024-04-23T22:53:13Z · Vincent (author and committer).

Adds explicit Permissible→CommandSender query, CommandSender returns self and PermissibleBase forwards operator owner or null. Enables recipient typing without RTTI assumption; generic shared null-owner permission base is not a sender.


<a id="commit-749"></a>
### 749 · feat: implement Server::broadcast {#commit-749}

[3a32b5b2ea042b1ae920b973775d73e107ac145d](https://github.com/EndstoneMC/endstone/commit/3a32b5b2ea042b1ae920b973775d73e107ac145d) · 2024-04-23T23:06:23Z · Vincent (author and committer).

Implements broadcast using subscription index then actual hasPermission check, set-deduplicates sender pointers and sends; adds formatting overload and const-ref signatures/mocks. Uses both candidate index and current authorization rather than assuming subscription means grant. Event interception remains TODO.


<a id="commit-750"></a>
### 750 · feat: add BroadcastMessageEvent and its python bindings {#commit-750}

[dd51f75ed6a90759d4a86fda55220c7e02d2b787](https://github.com/EndstoneMC/endstone/commit/dd51f75ed6a90759d4a86fda55220c7e02d2b787) · 2024-04-23T23:22:08Z · Vincent (author and committer).

Adds cancellable BroadcastMessageEvent with mutable message and read-only recipient set, async flag derived from caller thread; sends modified message only if uncancelled. Python STL conversion produces exposed set, not a documented editable recipient channel; runtime loops original recipients. Async designation alone does not synchronize permission maps or guarantee recipient lifetime.


<a id="commit-800"></a>
### 800 · feat: implement PlayerLoginEvent {#commit-800}

[a34d754c7ca5ab996969852200d68e2ba7bd0b54](https://github.com/EndstoneMC/endstone/commit/a34d754c7ca5ab996969852200d68e2ba7bd0b54) · 2024-04-29T15:11:08Z · Vincent (author and committer).

Implements cancellable PlayerLoginEvent before native load; cancellation calls native disconnect with NoReason and configurable kick text/skip-empty flag, then still invokes original _loadNewPlayer. Thus cancellation requests disconnect rather than short-circuiting load. Makes reason enum public and SubClientId unsigned8bit. Uses previously cached wrapper/address/UUID; no null identity fallback.


<a id="commit-801"></a>
### 801 · feat(python): add bindings for PlayerLoginEvent {#commit-801}

[0dab2f9c17314499fed508d360b210074baf6baa](https://github.com/EndstoneMC/endstone/commit/0dab2f9c17314499fed508d360b210074baf6baa) · 2024-04-29T15:17:03Z · Vincent (author and committer).

Exposes borrowed login player and mutable kick_message in Python binding/stub/event facade. Cancellation timing remains800, no new prevention guarantee.
