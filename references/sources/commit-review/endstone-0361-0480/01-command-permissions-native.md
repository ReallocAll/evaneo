<!-- retrieval: {"source_ids":["public:commit:0f66863281cb2a9dd41161a4959da805e9553520","public:commit:153a83b7218b08d5f12eb2080a8c1015ced2dcef","public:commit:30ec951158e83729a3c2f0570450cdd26404ee91","public:commit:3defe46d8e1c2bface14c2a6f1f488f0657facb6","public:commit:3f97e2ce7abed64c61ad903bedeb68b22f2abdd8","public:commit:419853abab7084f38798f3f7334336d53567278a","public:commit:444e8e364605d5617145ad5639d5030a91c7a74e","public:commit:4ec9854cc82a6aacaf4e3719b03c9e257094caea","public:commit:5048567350d859b1a3b21fcf1c379ce59c705820","public:commit:5c03b2e9f07787642d6a1a18047b47460a32e17d","public:commit:615ad68501d307d2841152f7d8cc860deccef9d7","public:commit:62de5eba6addfecb59f46114a5bdb5deba74a830","public:commit:69555715a4a558a50c2ec369dbe9308a232c4552","public:commit:75351e091a6e8c06c2049c567ea00103be228538","public:commit:7cf804bbf0088506a299f5f880a671060722f0ae","public:commit:7fdb675775a24c1d43133290c160df9ce9549999","public:commit:80153a8d560f089ca6773b3996c0fb6bd83e4087","public:commit:8995cb66130490dfcd3a5eef78d2b88c8aab4aba","public:commit:9346b850c46bb8daaaaabe42e6bd5b99edee2ef1","public:commit:9f85dff3a419bf3e2c0c5348b29fe47e03f8e6fd","public:commit:a7839d80a2fa65d06654f787efd8ac59a2e65766","public:commit:aa4afe9b5e2800448c768bb0d8f285d57af3d685","public:commit:b087458a1d1eb6d27be90efeed2f2c7f065e041a","public:commit:b439fb06fc0b857b492b4d061a410c0a7ea39989","public:commit:b76e59b502bac89965ef72281fcab5c6bd8efaba","public:commit:b9cf82cc4c300924c90b6f7ccd48abd5d8779e1c","public:commit:bbd39991cac1e2e7972acdea6d0a53f8682a7f76","public:commit:bcdfd8058655a98bc05efc903b025fc1ef585eaa","public:commit:be0f1fd001fb19563367d0fdbe19d0844d853ceb","public:commit:bf01c80144f2d90e4732b4fe1763405530386b80","public:commit:c4bf5f89b658d8014f235346d96b2a31510fa489","public:commit:c5f96ffc2cf254809dfa04f706a7fe712e6dee2a","public:commit:cbc660dc81b1a143c5ade170a59244f1335161a7","public:commit:d3adf2f0a3599ae6195bba15c4cb008da1a41af8","public:commit:d7e8726e35dd5601b0e67a2a4ee379aff98e0056","public:commit:d8663f7a0ceadc59e17737a63e2b3e71fabe9d70","public:commit:da212d79149484552a8f00225c7fc8597394fd32","public:commit:e88dfe406dcfa869f665c27a9dd8a666dae5d736","public:commit:f50857df2fbd38959fd2f5a43c298b50b9cae353","public:commit:f976ceeddef19b96cd24e8e985f2bd6308310a62"],"source_type":"public","date":"2024-03-14..2024-03-21","topics":["lifetime","concurrency","ffi","testing","build","recovery","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Command permissions, client visibility and native adapter contracts {#command-permissions-client-visibility-and-native-adapter-contracts}

## Result and evidence boundary {#result-and-evidence-boundary}

The 14–21 March 2024 changes connect the permission system from the previous unit to plugin execution, command discovery and declarative plugin metadata. Execution checks, client-visible command lists and permission-object ownership are distinct mechanisms. The sequence makes progress on each, but it does not establish that all three share an equivalent player identity or that permission changes automatically refresh client state. This dossier retains both the implementation path and its limits; it is a static historical review, not a present-day security finding or a reproduced game-server result.

Ordinal references below identify individual entries with exact SHA, parent, source, changed paths and attribution. The prior unit's permission core, command grammar and lifetime analysis are in `../endstone-0241-0360/`; all changes here are on its verified immediate descendant chain.

## Authorization becomes part of plugin execution {#authorization-becomes-part-of-plugin-execution}

368 adds a permission test before a PluginCommand forwards to its executor. Previously, the public command predicate existed and the built-in commands used it, but plugin execution did not. Returning true after denial treats the request as handled rather than requesting further usage output. The enabled-plugin check still occurs first, and the executor remains either an explicitly retained executor or the plugin owner. This ordering is a direct source observation. No execution-denial regression test is added.

371 and 372 thread permission vectors through constructors, registration and Python properties. Multiple permission names still use the earlier OR-style predicate: the list represents alternatives, not a conjunction requiring every permission. 376 makes the predicate accept a const sender while execution callbacks receive a mutable sender. Constness describes the query interface, not whether permission caches or external state can change elsewhere.

The same 368 patch replaces numeric registration flags with named constants, but accidentally changes the previous numeric 128 to NONE. 375 reports invisible commands and restores the corresponding NOT_REQUIRE_CHEAT bit. This is a useful counterexample to classifying named-constant conversion as mechanical: representation clarification and a default-value change were mixed in one commit. Later 402 temporarily clears this bit for commands being hidden from a client, and 404 removes that extra clearing. The resulting packet transformation only adds visibility flags. None of these source changes proves every host flag combination has been tested.

## Permissions: ownership, values and borrowed views {#permissions-ownership-values-and-borrowed-views}

373 adds an imperative permission-registration helper with optional parent linkage. 374 changes a caller to make_unique even while the manager still accepts shared ownership; 377 then deliberately changes manager ownership to unique_ptr. Its stated rationale is that Python-created objects will not be directly transferred into the native manager. The later metadata design realizes that boundary: a PluginDescription contains permission values, and the server copies each into a newly owned native Permission immediately before enabling the plugin. A Python description object and the active manager permission are therefore separate objects, not aliases to one shared Python override instance.

The temporary permission.h to permissions.h rename in 377 is reversed by 425. Exact blob identity proves the latter's relocated content is unchanged; unique ownership is not reversed. This is why filename reversals should not be used as evidence of an ownership reversal.

378–383 expose Permissible, attachment information and attachments to Python. Sender inheritance changes from a separately exposed ServerOperator type to Permissible with operator methods exposed directly. A bound constructor for PermissionAttachment does not itself insert that object into a Permissible's registered attachment list; the existing add_attachment operation is the path that does so. Borrowed plugin, permissible and attachment pointers retain their underlying native lifetime requirements. The reference return policies and generated stubs do not establish lifetime extension or a complete nullable type contract.

453 later makes Permission itself constructible as a Python value, exposes default/description mutation, parent operations and recalculation, and supports permission vectors in descriptions. 458 renames the Python default_value surface to default, with stubs repaired in 460. The enum contains a concrete mismatch from 378 through this endpoint: NOT_OP maps to Operator, while NOT_OPERATOR maps to NotOperator. The Python loader's string normalization in 459 therefore makes these two apparently synonymous spellings behave differently. This is a bounded source counterexample to using generated signatures as semantic validation.

The endpoint still has an uninitialized PluginManager pointer in a detached Permission. Methods test the pointer before use, but the constructor does not establish a null value. This matters specifically because 453 broadens public value construction. The previous unit's subscription-map copying and incomplete removal invalidation also remain in the full endpoint manager context: subscribing modifies a local map copy, while removePermission does not remove the object from default-pointer sets. Consequently, the added dirtyPermissibles calls express an invalidation intention without proving that all interested objects were registered correctly. These observations preserve limits on the claimed permission milestone; they are not an exhaustive audit or a statement about later versions.

## Client command visibility is a projection, not execution authorization {#client-command-visibility-is-a-projection-not-execution-authorization}

386–390 introduce the native serialization and packet interfaces needed to resend command metadata after a player's host permission level changes. The first implementation calls the original setter and then uses platform-specific pointer offsets to reach a PacketSender. The offsets are explicitly reverse-engineered, with an inline instruction about finding them in another host method. Debug output is removed in 392. The packet starts with opaque fields and vectors; 396 supplies more structure, but a commented-out size assertion is not an active ABI check.

397 filters the serialized packet through the Endstone command map. Commands missing locally, locally unregistered or denied by a temporary DummyPlayerSender are marked hidden from players and command blocks. The dummy sender knows a host command-permission level and derives operator status; it is not the real player's attachment-bearing permission object. 391 defines operator as any level other than Any, widening the prior Admin threshold. A low-but-nonzero native level can therefore receive operator defaults under this projection. The permitted case preserves the host's existing flags rather than forcibly making a command visible.

This filter improves discovery while execution remains separately checked by PluginCommand. Hiding a packet entry is not a substitute for authorization at invocation, and the dummy sender cannot be assumed equivalent to arbitrary future player permissions. Those distinctions are evidenced directly by the two code paths. No packet round-trip, per-player attachment or multiplayer integration test is present in these commits.

## From raw offsets to virtual interfaces {#from-raw-offsets-to-virtual-interfaces}

400 introduces Actor, Mob and Player scaffolding. 401 expands virtual declarations and central forward declarations; 402 switches packet sending and current permission lookup to virtual methods. This removes the particular PacketSender field-offset dependency. It replaces it with another native contract: exact inheritance, virtual-slot ordering and signatures must match the host. 403 places hasComponent differently on Windows and Linux, showing why a single source declaration order was insufficient. This is not proof of a fully documented or stable host ABI.

405 cites the Mojang protocol documentation in the commit claim and adjusts origin/output definitions, enum spelling and UUID representation. Numeric enum preservation is separately distinguishable from layout changes such as four 32-bit words becoming two 64-bit words. The external documentation itself was not independently read in this unit. Attribution is to the cited source for protocol information and to the commit author for this adapter change, not to the author for creating the game's underlying behavior.

406 adds the second concrete synchronization trigger: send the command list after the original initial-spawn method. Together with permission-setter updates, this covers joining and that host permission-level transition. There is no general hook here that resends on every Endstone attachment/default change. 407 updates hardcoded grammar symbols and explicitly leaves a note about inspecting CommandRegistry::describe when game versions change. The sequence supports version-sensitive maintenance discipline, not an automatic compatibility claim.

## Command registration becomes declarative {#command-registration-becomes-declarative}

393 separates BedrockCommand wrappers from EndstoneCommand built-ins. 394 restores local clearCommands after the much earlier 220 disabled native deregistration. It removes only plugin commands from the local map and marks their registration state accordingly; it does not erase host overloads. The new asPluginCommand discriminator supports this filtering. 436 also repairs a null dereference introduced in 347 by checking the lookup before calling that discriminator. Neither source change proves a full unload/reload protocol.

409 removes the plugin's imperative registerCommand and registerPermission helpers while moving PluginCommand back to its own header. 410 removes server registration exposure, and 411 changes Python bindings. These are public API transitions, not merely file organization. The replacement arrives through metadata builders in 429 and runtime integration in 438–439. Commands are copied as metadata into PluginCommand objects owned by the map; a custom metadata Command subclass's execution override is not the retained dispatch implementation.

439 initializes native and built-in commands, adds plugin-name enum values and registers every loaded plugin's declared commands before PostWorld enable callbacks. This fixes 438's placement after callbacks. Startup callbacks still run before this map initialization. The loop ignores registerCommand's boolean result, and the inherited registration operation can mutate native/local state before later usage parsing fails. Thus metadata-driven initialization does not create transactional registration by itself. No repeated-initialization or rollback test is supplied.

454 changes most setters to void and keeps their registered-object guard, so ignored mutations no longer return a failure indicator. Permission-list mutation remains different. Public construction of Command, restored by 428/447 after earlier protection, now serves value metadata rather than a general Python execute trampoline. The broader evolution is a move from imperative user-created runtime objects toward declarative values and host-owned runtime wrappers, with distinct lifecycle and feedback costs.

## Applying this evidence {#applying-this-evidence}

Useful questions derived from this chain are: Is a command's execution predicate actually called? Does discovery use the same identity and effective permissions? Which object owns the active permission versus its declaration? At what startup phase are commands available? Does a native adapter trade one ABI assumption for another? Does a refactor preserve flag defaults and failure ownership? These are grounded diagnostic prompts, not a universal claim about the author's preferences.

Test-package changes in this unit are usage/construction examples, not runtime authorization or host ABI tests. No compiler, test runner, server, package installation or external dependency code was executed. Reported fixes remain reported where the diff alone cannot establish their runtime outcome.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-368"></a>
### 368. feat: add enum values for CommandFlag {#commit-368}

Source: [75351e091a6e8c06c2049c567ea00103be228538](https://github.com/EndstoneMC/endstone/commit/75351e091a6e8c06c2049c567ea00103be228538) · authored 2024-03-14T15:06:35Z · parent `1a3ca242e96404ae8448f514f392d294e6671237`.

Author: **Vincent**.

Introduces named command-flag bit constants and refines native signature fields, but also inserts permission enforcement into PluginCommand execution, closing prior 360 gap for plugin commands. Denial remains handled=true. Changes default registration flag from numeric128 to NONE, unintentionally losing not-require-cheat behavior until 375 restores named bit. Native fields/flag meanings remain source-level reverse-engineering evidence.

Changed paths: `include/bedrock/command/command.h`, `include/bedrock/command/command_flag.h`, `include/bedrock/command/command_registry.h`, `include/endstone/plugin/plugin.h`, `src/endstone_core/command/command_map.cpp`.

Coverage: 124 canonical patch lines; 5 changed paths.

<a id="commit-369"></a>
### 369. refactor: CommandFlag enum values for better readability {#commit-369}

Source: [7fdb675775a24c1d43133290c160df9ce9549999](https://github.com/EndstoneMC/endstone/commit/7fdb675775a24c1d43133290c160df9ce9549999) · authored 2024-03-14T15:58:24Z · parent `75351e091a6e8c06c2049c567ea00103be228538`.

Author: **Vincent**.

Renames HIDE_FROM constants to HIDDEN_FROM with identical bit values. Source API spelling change only; no new flag behavior or host evidence.

Changed paths: `include/bedrock/command/command_flag.h`.

Coverage: 29 canonical patch lines; 1 changed paths.

<a id="commit-371"></a>
### 371. feat: add permissions to Command constructor {#commit-371}

Source: [419853abab7084f38798f3f7334336d53567278a](https://github.com/EndstoneMC/endstone/commit/419853abab7084f38798f3f7334336d53567278a) · authored 2024-03-14T16:20:45Z · parent `b55e3194a8816b27e7d9f2e933285cb281269e1b`.

Author: **Vincent**.

Threads permission lists through Command, PluginCommand and plugin registration constructors. Reuses existing setter and OR predicate, making authorization metadata available at construction instead of only after registration. No change to precedence or tests.

Changed paths: `include/endstone/command/command.h`, `include/endstone/plugin/plugin.h`.

Coverage: 57 canonical patch lines; 2 changed paths.

<a id="commit-372"></a>
### 372. feat: add python bindings of testPermission for Command class {#commit-372}

Source: [aa4afe9b5e2800448c768bb0d8f285d57af3d685](https://github.com/EndstoneMC/endstone/commit/aa4afe9b5e2800448c768bb0d8f285d57af3d685) · authored 2024-03-14T16:31:54Z · parent `419853abab7084f38798f3f7334336d53567278a`.

Author: **Vincent**.

Exposes visible/silent permission tests and mutable permission-list property to Python, threads permissions through facade registration and optional constructor adapter, and updates generated stubs. C++ enforcement from 368 and Python metadata accessibility are separate steps; no behavioral test accompanies bindings.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/plugin.py`, `src/endstone_python/command.cpp`, `src/endstone_python/plugin.cpp`.

Coverage: 136 canonical patch lines; 4 changed paths.

<a id="commit-373"></a>
### 373. feat: add registerPermission to Plugin class {#commit-373}

Source: [b9cf82cc4c300924c90b6f7ccd48abd5d8779e1c](https://github.com/EndstoneMC/endstone/commit/b9cf82cc4c300924c90b6f7ccd48abd5d8779e1c) · authored 2024-03-14T16:48:26Z · parent `aa4afe9b5e2800448c768bb0d8f285d57af3d685`.

Author: **Vincent**.

Adds plugin helpers to register permissions with optional parent, guards parent child insertion on successful registration, and replaces manager header includes with forward declarations to break dependency coupling. Parent map mutation still needs explicit recalculation under its documented contract; helper does not do it here. Public registration delegates ownership to manager rather than tracking plugin-specific permission removal.

Changed paths: `include/endstone/permissions/permission.h`, `include/endstone/plugin/plugin.h`, `include/endstone/plugin/plugin_manager.h`, `src/endstone_core/command/server_command_sender.cpp`, `src/endstone_core/permissions/default_permissions.cpp`, `src/endstone_python/server.cpp`.

Coverage: 139 canonical patch lines; 6 changed paths.

<a id="commit-374"></a>
### 374. refactor: remove [[no_discard]] {#commit-374}

Source: [b439fb06fc0b857b492b4d061a410c0a7ea39989](https://github.com/EndstoneMC/endstone/commit/b439fb06fc0b857b492b4d061a410c0a7ea39989) · authored 2024-03-14T16:54:03Z · parent `b9cf82cc4c300924c90b6f7ccd48abd5d8779e1c`.

Author: **Vincent**.

Removes nodiscard from side-effecting permission registration and changes construction from make_shared to make_unique, still converting into current shared_ptr manager API until 377. This is more than formatting but not yet unique manager ownership.

Changed paths: `include/endstone/plugin/plugin.h`.

Coverage: 35 canonical patch lines; 1 changed paths.

<a id="commit-375"></a>
### 375. fix: command not visible {#commit-375}

Source: [cbc660dc81b1a143c5ade170a59244f1335161a7](https://github.com/EndstoneMC/endstone/commit/cbc660dc81b1a143c5ade170a59244f1335161a7) · authored 2024-03-14T17:04:13Z · parent `b439fb06fc0b857b492b4d061a410c0a7ea39989`.

Author: **Vincent**.

Reported command-visibility fix restores NOT_REQUIRE_CHEAT flag lost in 368 while keeping Any native level. Also removes unused module argument from server binding initializer. Named constants prevent magic numbers only if the selected constant preserves semantics; no actual client visibility run observed.

Changed paths: `src/endstone_core/command/command_map.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/server.cpp`.

Coverage: 54 canonical patch lines; 3 changed paths.

<a id="commit-376"></a>
### 376. refactor: remove / add const qualifier {#commit-376}

Source: [bf01c80144f2d90e4732b4fe1763405530386b80](https://github.com/EndstoneMC/endstone/commit/bf01c80144f2d90e4732b4fe1763405530386b80) · authored 2024-03-14T17:14:40Z · parent `cbc660dc81b1a143c5ade170a59244f1335161a7`.

Author: **Vincent**.

Makes permission predicates accept const sender but changes command executor callback sender to mutable reference, aligning Python trampolines. Enables callbacks to change sender permission state while read-only checks remain const. This changes public virtual signature/ABI; no consumer rebuild result or mutation tests.

Changed paths: `include/endstone/command/command.h`, `include/endstone/command/command_executor.h`, `src/endstone_python/command.cpp`, `src/endstone_python/plugin.cpp`.

Coverage: 61 canonical patch lines; 4 changed paths.

<a id="commit-377"></a>
### 377. refactor: use unique_ptr as the holder for Permission as we don't need to pass objects from python. {#commit-377}

Source: [bcdfd8058655a98bc05efc903b025fc1ef585eaa](https://github.com/EndstoneMC/endstone/commit/bcdfd8058655a98bc05efc903b025fc1ef585eaa) · authored 2024-03-14T17:46:49Z · parent `bf01c80144f2d90e4732b4fe1763405530386b80`.

Author: **Vincent**.

Changes manager/default-registration Permission ownership from shared_ptr to unique_ptr, with explicit title rationale that Python need not pass objects into this owner. Borrowed query/default/subscription pointers remain. Adds empty Python permissions initializer and exact rename permission.h to permissions.h, reversed 425. Ownership rationale is specific to this API stage, not a universal preference for unique_ptr.

Changed paths: `include/endstone/detail/permissions/default_permissions.h`, `include/endstone/detail/plugin/plugin_manager.h`, `include/endstone/permissions/permission.h`, `include/endstone/permissions/permission_attachment.h`, `include/endstone/permissions/permissions.h`, `include/endstone/plugin/plugin.h`, `include/endstone/plugin/plugin_manager.h`, `src/endstone_core/permissions/default_permissions.cpp`, `src/endstone_core/permissions/permissible_base.cpp`, `src/endstone_core/plugin/plugin_manager.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/permissions.cpp`.

Coverage: 601 canonical patch lines; 12 changed paths.

<a id="commit-378"></a>
### 378. feat: add python bindings for 'PermissionDefault' and 'ServerOperator' classes {#commit-378}

Source: [615ad68501d307d2841152f7d8cc860deccef9d7](https://github.com/EndstoneMC/endstone/commit/615ad68501d307d2841152f7d8cc860deccef9d7) · authored 2024-03-14T18:00:22Z · parent `bcdfd8058655a98bc05efc903b025fc1ef585eaa`.

Author: **Vincent**.

Binds PermissionDefault aliases and ServerOperator property, generating matching stubs. NOT_OP mistakenly maps to Operator while NOT_OPERATOR maps correctly; generated stub records the same semantic mismatch. No alias-equality test. Separate ServerOperator Python surface is removed 380 while C++ interface remains.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/permissions.cpp`.

Coverage: 112 canonical patch lines; 2 changed paths.

<a id="commit-379"></a>
### 379. feat: add python bindings for Permissible {#commit-379}

Source: [d8663f7a0ceadc59e17737a63e2b3e71fabe9d70](https://github.com/EndstoneMC/endstone/commit/d8663f7a0ceadc59e17737a63e2b3e71fabe9d70) · authored 2024-03-14T18:12:42Z · parent `615ad68501d307d2841152f7d8cc860deccef9d7`.

Author: **Vincent**.

Binds Permissible query/attachment/recalculation APIs and changes base holder from shared to default, reorders initialization after plugins. Returned attachments are borrowed; effective-info return policy cannot prevent cache invalidation on recalculation. Several referenced types remain unbound and appear as ellipses in generated stubs, completed incrementally later.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/permissions.cpp`.

Coverage: 145 canonical patch lines; 3 changed paths.

<a id="commit-380"></a>
### 380. feat(python): `CommandSender` class now inherits from the `Permissible` base class {#commit-380}

Source: [bbd39991cac1e2e7972acdea6d0a53f8682a7f76](https://github.com/EndstoneMC/endstone/commit/bbd39991cac1e2e7972acdea6d0a53f8682a7f76) · authored 2024-03-14T18:28:04Z · parent `d8663f7a0ceadc59e17737a63e2b3e71fabe9d70`.

Author: **Vincent**.

Makes Python CommandSender inherit Permissible, forward-creates the latter locally before command initialization and exposes op directly on it. Removes separate Python ServerOperator type while retaining native inheritance, simplifying public Python hierarchy and binding-order requirements. This completes prior 348 explicit TODO rather than introducing permission semantics anew.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/command.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/permissions.cpp`.

Coverage: 140 canonical patch lines; 4 changed paths.

<a id="commit-381"></a>
### 381. feat(python): add bindings for PermissionAttachmentInfo {#commit-381}

Source: [e88dfe406dcfa869f665c27a9dd8a666dae5d736](https://github.com/EndstoneMC/endstone/commit/e88dfe406dcfa869f665c27a9dd8a666dae5d736) · authored 2024-03-14T18:35:14Z · parent `bbd39991cac1e2e7972acdea6d0a53f8682a7f76`.

Author: **Vincent**.

Binds PermissionAttachmentInfo constructor and readonly properties, resolving effective-permissions stub type. Constructor stores borrowed permissible/attachment without keep-alive policies; nullable default attachment remains underrepresented in stub. Binding availability does not change native cache lifetime.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/permissions.cpp`.

Coverage: 72 canonical patch lines; 2 changed paths.

<a id="commit-383"></a>
### 383. feat: add python bindings for PermissionAttachment class {#commit-383}

Source: [c4bf5f89b658d8014f235346d96b2a31510fa489](https://github.com/EndstoneMC/endstone/commit/c4bf5f89b658d8014f235346d96b2a31510fa489) · authored 2024-03-15T00:41:53Z · parent `91b22581a2ad8a944a732dc57d42879ac404e2fb`.

Author: **Vincent**.

Binds attachment mutation, borrowed plugin/permissible, removal callback and copy-of-permissions getter; adds pybind functional conversion and updates stubs. Directly constructing an attachment does not add it to PermissibleBase owned attachment list. Removal destroys manager-owned attachment while Python references can persist; no lifetime/reentrancy tests added. Native ownership semantics remain those previously reviewed.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/permissions.cpp`.

Coverage: 141 canonical patch lines; 2 changed paths.

<a id="commit-386"></a>
### 386. refactor: move hooks into separate folders {#commit-386}

Source: [f976ceeddef19b96cd24e8e985f2bd6308310a62](https://github.com/EndstoneMC/endstone/commit/f976ceeddef19b96cd24e8e985f2bd6308310a62) · authored 2024-03-15T14:21:28Z · parent `56e278a054cfc1764f8a14100aeac961820aca40`.

Author: **Vincent**.

Moves command/output/server hooks with exact blob reuse where unchanged, but also adds native serializeAvailableCommands RVO forwarding in the relocated registry file. Declaration and packet types follow 387–389, so this is not a wholly mechanical directory move or a single independently build-complete feature.

Changed paths: `src/endstone_runtime/bedrock/command.cpp`, `src/endstone_runtime/bedrock/command/command.cpp`, `src/endstone_runtime/bedrock/command/command_output.cpp`, `src/endstone_runtime/bedrock/command/command_registry.cpp`, `src/endstone_runtime/bedrock/command_output.cpp`, `src/endstone_runtime/bedrock/command_registry.cpp`, `src/endstone_runtime/bedrock/server/server_instance.cpp`, `src/endstone_runtime/bedrock/server_instance.cpp`.

Coverage: 603 canonical patch lines; 8 changed paths.

<a id="commit-387"></a>
### 387. feat: add serializeAvailableCommands method {#commit-387}

Source: [80153a8d560f089ca6773b3996c0fb6bd83e4087](https://github.com/EndstoneMC/endstone/commit/80153a8d560f089ca6773b3996c0fb6bd83e4087) · authored 2024-03-15T14:22:08Z · parent `f976ceeddef19b96cd24e8e985f2bd6308310a62`.

Author: **Vincent**.

Declares available-command serialization and names command_symbols vector, including packet header before 388 creates it. Exposes native packet generation without yet implementing per-player filtering.

Changed paths: `include/bedrock/command/command_registry.h`.

Coverage: 29 canonical patch lines; 1 changed paths.

<a id="commit-388"></a>
### 388. feat: add AvailableCommandsPacket {#commit-388}

Source: [d3adf2f0a3599ae6195bba15c4cb008da1a41af8](https://github.com/EndstoneMC/endstone/commit/d3adf2f0a3599ae6195bba15c4cb008da1a41af8) · authored 2024-03-15T14:22:20Z · parent `80153a8d560f089ca6773b3996c0fb6bd83e4087`.

Author: **Vincent**.

Adds AvailableCommandsPacket layout with owned string vectors and opaque24-byte placeholders for unknown vector members. This is a provisional ABI model, not an implemented wire serializer. Native RVO writes and local destruction depend on correctly modeled object representation;396 replaces several opaque members with vectors.

Changed paths: `include/bedrock/network/game/available_commands_packet.h`.

Coverage: 52 canonical patch lines; 1 changed paths.

<a id="commit-389"></a>
### 389. feat: add Packet and PacketSender {#commit-389}

Source: [30ec951158e83729a3c2f0570450cdd26404ee91](https://github.com/EndstoneMC/endstone/commit/30ec951158e83729a3c2f0570450cdd26404ee91) · authored 2024-03-15T14:22:31Z · parent `d3adf2f0a3599ae6195bba15c4cb008da1a41af8`.

Author: **Vincent**.

Adds minimal Packet virtual destructor and PacketSender send interface used by upcoming native hook. Describes only the represented virtual surface, not complete protocol ownership/serialization semantics.

Changed paths: `include/bedrock/network/packet.h`, `include/bedrock/network/packet_sender.h`.

Coverage: 55 canonical patch lines; 2 changed paths.

<a id="commit-390"></a>
### 390. feat: hook Player::setPermissions to send updated commands {#commit-390}

Source: [da212d79149484552a8f00225c7fc8597394fd32](https://github.com/EndstoneMC/endstone/commit/da212d79149484552a8f00225c7fc8597394fd32) · authored 2024-03-15T14:22:56Z · parent `30ec951158e83729a3c2f0570450cdd26404ee91`.

Author: **Vincent**.

Hooks Player::setPermissions after forwarding original, serializes available commands and sends packet through platform-specific packet-sender pointer offsets, with debug prints. Source identifies setLastHurtBy as place to find offsets. Visibility filtering is explicitly TODO and no measured offset/runtime verification accompanies patch;401/402 replace offset access with modeled virtual calls.

Changed paths: `include/bedrock/server/level/player.h`, `src/endstone_runtime/bedrock/server/level/player.cpp`.

Coverage: 81 canonical patch lines; 2 changed paths.

<a id="commit-391"></a>
### 391. fix: isOp function in CommandSenderAdapter {#commit-391}

Source: [c5f96ffc2cf254809dfa04f706a7fe712e6dee2a](https://github.com/EndstoneMC/endstone/commit/c5f96ffc2cf254809dfa04f706a7fe712e6dee2a) · authored 2024-03-15T14:47:06Z · parent `da212d79149484552a8f00225c7fc8597394fd32`.

Author: **Vincent**.

Changes generic sender operator mapping from Admin-and-higher named levels to every level except Any. GameDirectors now counts as operator, unlike prior 355. This is a real authorization policy change with reported fix intent, not a const/style adjustment. Unsupported mutation diagnostic now names sender.

Changed paths: `src/endstone_core/command/command_adapter.cpp`.

Coverage: 28 canonical patch lines; 1 changed paths.

<a id="commit-392"></a>
### 392. refactor: remove debug messages {#commit-392}

Source: [f50857df2fbd38959fd2f5a43c298b50b9cae353](https://github.com/EndstoneMC/endstone/commit/f50857df2fbd38959fd2f5a43c298b50b9cae353) · authored 2024-03-15T14:47:35Z · parent `c5f96ffc2cf254809dfa04f706a7fe712e6dee2a`.

Author: **Vincent**.

Removes temporary before/after packet-send printf messages and records intended future factoring into public Player/Server command synchronization. Actual send/filter behavior unchanged; TODO is a plan, not implemented abstraction.

Changed paths: `src/endstone_runtime/bedrock/server/level/player.cpp`.

Coverage: 17 canonical patch lines; 1 changed paths.

<a id="commit-393"></a>
### 393. refactor: change the base class of commands {#commit-393}

Source: [3f97e2ce7abed64c61ad903bedeb68b22f2abdd8](https://github.com/EndstoneMC/endstone/commit/3f97e2ce7abed64c61ad903bedeb68b22f2abdd8) · authored 2024-03-15T14:57:20Z · parent `f50857df2fbd38959fd2f5a43c298b50b9cae353`.

Author: **Vincent**.

Distinguishes BedrockCommand views from EndstoneCommand built-ins through named subclasses; view still refuses execution and now explains native provider. No dispatch algorithm changes. This classification supports selective cleanup in 394 without treating all commands as plugin-owned.

Changed paths: `include/endstone/detail/command/bedrock_command.h`, `include/endstone/detail/command/command_view.h`, `include/endstone/detail/command/defaults/plugins_command.h`, `include/endstone/detail/command/defaults/version_command.h`, `include/endstone/detail/command/endstone_command.h`, `src/endstone_core/command/command_map.cpp`, `src/endstone_core/command/command_view.cpp`, `src/endstone_core/command/defaults/plugins_command.cpp`, `src/endstone_core/command/defaults/version_command.cpp`.

Coverage: 210 canonical patch lines; 9 changed paths.

<a id="commit-394"></a>
### 394. feat: implement clearCommands {#commit-394}

Source: [8995cb66130490dfcd3a5eef78d2b88c8aab4aba](https://github.com/EndstoneMC/endstone/commit/8995cb66130490dfcd3a5eef78d2b88c8aab4aba) · authored 2024-03-15T15:49:22Z · parent `3f97e2ce7abed64c61ad903bedeb68b22f2abdd8`.

Author: **Vincent**.

Restores clearCommands API removed in prior 220, but implements local removal of plugin commands only, preserving native views and built-ins. It marks local command objects unregistered and erases local name/alias entries under mutex; does not unregister native registry overloads. Public wording clears all is broader than behavior. This is a revised narrower contract, not proof native unregistration became supported.

Changed paths: `include/endstone/command/command_map.h`, `include/endstone/detail/command/command_map.h`, `src/endstone_core/command/command_map.cpp`.

Coverage: 74 canonical patch lines; 3 changed paths.

<a id="commit-395"></a>
### 395. feat: add bitwise operators to CommandFlag structure {#commit-395}

Source: [62de5eba6addfecb59f46114a5bdb5deba74a830](https://github.com/EndstoneMC/endstone/commit/62de5eba6addfecb59f46114a5bdb5deba74a830) · authored 2024-03-15T16:02:38Z · parent `8995cb66130490dfcd3a5eef78d2b88c8aab4aba`.

Author: **Vincent**.

Adds value-preserving typed bitwise and assignment operators to16-bit CommandFlag, enabling masks without raw integer manipulation. Operator addition does not validate chosen bit meanings or call-site policy.

Changed paths: `include/bedrock/command/command_flag.h`.

Coverage: 50 canonical patch lines; 1 changed paths.

<a id="commit-396"></a>
### 396. feat: update CommandData structure in AvailableCommandsPacket {#commit-396}

Source: [444e8e364605d5617145ad5639d5030a91c7a74e](https://github.com/EndstoneMC/endstone/commit/444e8e364605d5617145ad5639d5030a91c7a74e) · authored 2024-03-15T16:02:56Z · parent `62de5eba6addfecb59f46114a5bdb5deba74a830`.

Author: **Vincent**.

Models packet CommandData metadata and replaces opaque vector storage with vector<CommandData> and several vector<void*> placeholders. Enables filtering but leaves nested payload element semantics incomplete; commented-out size assertion is not executed validation. Captures explicit intent to use Player virtual packet send instead of raw packet-sender offsets.

Changed paths: `include/bedrock/network/game/available_commands_packet.h`, `src/endstone_runtime/bedrock/server/level/player.cpp`.

Coverage: 63 canonical patch lines; 2 changed paths.

<a id="commit-397"></a>
### 397. feat: hide or unhide commands when Player's permission level changed {#commit-397}

Source: [3defe46d8e1c2bface14c2a6f1f488f0657facb6](https://github.com/EndstoneMC/endstone/commit/3defe46d8e1c2bface14c2a6f1f488f0657facb6) · authored 2024-03-15T16:22:05Z · parent `444e8e364605d5617145ad5639d5030a91c7a74e`.

Author: **Vincent**.

Adds available-command filtering using dummy sender derived only from permission level, hiding unregistered/unauthorized map entries with player/block flags before sending. It approximates defaults/operator state rather than real player attachments. Allowed entries retain original flags; despite title, explicit clearing of existing hidden flags is absent. This client visibility path is separate from server-side execution authorization.

Changed paths: `src/endstone_runtime/bedrock/server/level/player.cpp`.

Coverage: 68 canonical patch lines; 1 changed paths.

<a id="commit-398"></a>
### 398. feat: add cstddef for 'size_t' in player.h {#commit-398}

Source: [a7839d80a2fa65d06654f787efd8ac59a2e65766](https://github.com/EndstoneMC/endstone/commit/a7839d80a2fa65d06654f787efd8ac59a2e65766) · authored 2024-03-15T16:29:30Z · parent `3defe46d8e1c2bface14c2a6f1f488f0657facb6`.

Author: **Vincent**.

Adds cstddef for size_t used by raw player offset accessor. Header dependency repair, not a changed offset or validated ABI.

Changed paths: `include/bedrock/server/level/player.h`.

Coverage: 13 canonical patch lines; 1 changed paths.

<a id="commit-399"></a>
### 399. refactor: rename command_view.cpp to bedrock_command.cpp {#commit-399}

Source: [0f66863281cb2a9dd41161a4959da805e9553520](https://github.com/EndstoneMC/endstone/commit/0f66863281cb2a9dd41161a4959da805e9553520) · authored 2024-03-15T16:33:47Z · parent `a7839d80a2fa65d06654f787efd8ac59a2e65766`.

Author: **Vincent**.

Renames command_view.cpp to bedrock_command.cpp and wraps definition in equivalent namespace block. Same rejected-execution message/control flow; changed formatting read and relocation retained.

Changed paths: `src/endstone_core/command/bedrock_command.cpp`, `src/endstone_core/command/command_view.cpp`.

Coverage: 59 canonical patch lines; 2 changed paths.

<a id="commit-400"></a>
### 400. feat: dd Actor and Mob classes, refactor Player class {#commit-400}

Source: [b76e59b502bac89965ef72281fcab5c6bd8efaba](https://github.com/EndstoneMC/endstone/commit/b76e59b502bac89965ef72281fcab5c6bd8efaba) · authored 2024-03-19T12:33:29Z · parent `0f66863281cb2a9dd41161a4959da805e9553520`.

Author: **Vincent**.

Introduces abstract Actor→Mob→Player native inheritance scaffolding with pure destructors and notes initial-player command synchronization still needed. No gameplay methods or construction are implemented.401 fills virtual order before using sendNetworkPacket.

Changed paths: `include/bedrock/server/level/player.h`, `include/bedrock/world/actor/actor.h`, `include/bedrock/world/actor/mob.h`, `src/endstone_runtime/bedrock/server/level/player.cpp`.

Coverage: 82 canonical patch lines; 4 changed paths.

<a id="commit-401"></a>
### 401. feat: add virtual functions for Actor-related classes {#commit-401}

Source: [7cf804bbf0088506a299f5f880a671060722f0ae](https://github.com/EndstoneMC/endstone/commit/7cf804bbf0088506a299f5f880a671060722f0ae) · authored 2024-03-19T15:43:09Z · parent `b76e59b502bac89965ef72281fcab5c6bd8efaba`.

Author: **Vincent**.

Adds full represented Actor/Mob/Player virtual lists, central forward declarations and protected host methods; removes raw packet-sender accessor and declares member sendCommands. All 498-line diff read. This replaces one offset dependency with a much larger vtable/signature contract, not elimination of ABI dependence. hasComponent ordering differs by platform and is corrected 403; caller migration follows 402. Unknown forward types and host declarations are not attributed as original game logic.

Changed paths: `include/bedrock/command/command_origin.h`, `include/bedrock/forward.h`, `include/bedrock/server/level/player.h`, `include/bedrock/world/actor/actor.h`, `include/bedrock/world/actor/mob.h`.

Coverage: 501 canonical patch lines; 5 changed paths.

<a id="commit-402"></a>
### 402. refactor: use sendNetworkPacket instead of getPacketSender().send {#commit-402}

Source: [5048567350d859b1a3b21fcf1c379ce59c705820](https://github.com/EndstoneMC/endstone/commit/5048567350d859b1a3b21fcf1c379ce59c705820) · authored 2024-03-19T15:48:13Z · parent `7cf804bbf0088506a299f5f880a671060722f0ae`.

Author: **Vincent**.

Uses Player::sendNetworkPacket and actual getCommandPermissionLevel instead of passing proposed level to free helper; sends only after original setter. This completes 401 accessor removal and bases filtering on resulting state. Also clears NOT_REQUIRE_CHEAT on hidden commands, reversed 404; title hides that policy experiment.

Changed paths: `src/endstone_runtime/bedrock/server/level/player.cpp`.

Coverage: 61 canonical patch lines; 1 changed paths.

<a id="commit-403"></a>
### 403. fix: platform-specific hasComponent method in Actor header {#commit-403}

Source: [9f85dff3a419bf3e2c0c5348b29fe47e03f8e6fd](https://github.com/EndstoneMC/endstone/commit/9f85dff3a419bf3e2c0c5348b29fe47e03f8e6fd) · authored 2024-03-19T16:02:37Z · parent `5048567350d859b1a3b21fcf1c379ce59c705820`.

Author: **Vincent**.

Moves hasComponent virtual declaration to different relative positions on Linux versus Windows, repairing vtable ordering rather than changing method behavior. Highlights that matching method signatures is insufficient when platform slot order differs; no host regression run observed.

Changed paths: `include/bedrock/world/actor/actor.h`.

Coverage: 24 canonical patch lines; 1 changed paths.

<a id="commit-404"></a>
### 404. fix: flag setting in player commands {#commit-404}

Source: [69555715a4a558a50c2ec369dbe9308a232c4552](https://github.com/EndstoneMC/endstone/commit/69555715a4a558a50c2ec369dbe9308a232c4552) · authored 2024-03-19T16:03:38Z · parent `9f85dff3a419bf3e2c0c5348b29fe47e03f8e6fd`.

Author: **Vincent**.

Removes the NOT_REQUIRE_CHEAT mask-clearing added 402 while retaining hidden flags. Visibility and cheat requirements remain separate bits; preserve this immediate rollback without inventing a failure trace.

Changed paths: `src/endstone_runtime/bedrock/server/level/player.cpp`.

Coverage: 12 canonical patch lines; 1 changed paths.

<a id="commit-405"></a>
### 405. feat: update enums in accordance with mojang/bedrock-protocol-doc {#commit-405}

Source: [b087458a1d1eb6d27be90efeed2f2c7f065e041a](https://github.com/EndstoneMC/endstone/commit/b087458a1d1eb6d27be90efeed2f2c7f065e041a) · authored 2024-03-19T16:35:06Z · parent `69555715a4a558a50c2ec369dbe9308a232c4552`.

Author: **Vincent**.

Title attributes enum alignment to mojang/bedrock-protocol-doc. Renames origin kinds without changing values, expands output modes/options and changes UUID representation from four32-bit words to two64-bit halves. UUID size can remain16 while alignment changes, so this is not purely cosmetic. External protocol document itself not read; retain source attribution and unknown verification method.

Changed paths: `include/bedrock/command/command_origin.h`, `include/bedrock/command/command_output.h`, `include/bedrock/command/command_registry.h`, `include/bedrock/uuid.h`, `src/endstone_core/command/command_adapter.cpp`.

Coverage: 101 canonical patch lines; 5 changed paths.

<a id="commit-406"></a>
### 406. feat: send usable commands when a player spawns. {#commit-406}

Source: [5c03b2e9f07787642d6a1a18047b47460a32e17d](https://github.com/EndstoneMC/endstone/commit/5c03b2e9f07787642d6a1a18047b47460a32e17d) · authored 2024-03-19T16:43:01Z · parent `b087458a1d1eb6d27be90efeed2f2c7f065e041a`.

Author: **Vincent**.

Hooks ServerPlayer::doInitialSpawn, forwarding original then sending filtered commands. Complements permission-change trigger and removes earlier createNewPlayer TODO, selecting a different lifecycle point. Does not add automatic updates for later attachment changes or command registration; no client lifecycle test.

Changed paths: `include/bedrock/server/level/player.h`, `include/bedrock/server/level/server_player.h`, `src/endstone_runtime/bedrock/server/level/player.cpp`, `src/endstone_runtime/bedrock/server/level/server_player.cpp`.

Coverage: 83 canonical patch lines; 4 changed paths.

<a id="commit-407"></a>
### 407. feat: update CommandRegistry Symbol IDs {#commit-407}

Source: [4ec9854cc82a6aacaf4e3719b03c9e257094caea](https://github.com/EndstoneMC/endstone/commit/4ec9854cc82a6aacaf4e3719b03c9e257094caea) · authored 2024-03-19T17:19:05Z · parent `5c03b2e9f07787642d6a1a18047b47460a32e17d`.

Author: **Vincent**.

Updates equipment/string/position/message/JSON/block/command grammar symbol IDs and records CommandRegistry::describe as inspection point for future game updates. Concrete maintainability breadcrumb for version-sensitive constants, not automatic discovery or measured compatibility.

Changed paths: `src/endstone_runtime/bedrock/command/command_registry.cpp`.

Coverage: 34 canonical patch lines; 1 changed paths.

<a id="commit-425"></a>
### 425. refactor: rename permissions.h to permission.h {#commit-425}

Source: [be0f1fd001fb19563367d0fdbe19d0844d853ceb](https://github.com/EndstoneMC/endstone/commit/be0f1fd001fb19563367d0fdbe19d0844d853ceb) · authored 2024-03-20T10:35:45Z · parent `e3b9a28b785b096657277c402f9a1db5f98cc5ca`.

Author: **Vincent**.

Reverses 377 permission-header plural rename with exact blob identity and updates all changed includes. No ownership reversal: unique_ptr manager storage remains.

Changed paths: `include/endstone/detail/permissions/default_permissions.h`, `include/endstone/detail/plugin/plugin_manager.h`, `include/endstone/permissions/permission.h`, `include/endstone/permissions/permission_attachment.h`, `include/endstone/permissions/permissions.h`, `include/endstone/plugin/plugin.h`, `src/endstone_core/permissions/permissible_base.cpp`, `src/endstone_python/permissions.cpp`.

Coverage: 494 canonical patch lines; 8 changed paths.

<a id="commit-453"></a>
### 453. feat(python): add bindings for the Permission class {#commit-453}

Source: [153a83b7218b08d5f12eb2080a8c1015ced2dcef](https://github.com/EndstoneMC/endstone/commit/153a83b7218b08d5f12eb2080a8c1015ced2dcef) · authored 2024-03-21T01:00:41Z · parent `d40d153a940eaf1cffa50a5a553ca0b7b60435a8`.

Author: **Vincent**.

Adds Permission constructor/properties/parent/recalculation bindings, forward-creates type to resolve stub placeholders and allows permission values in metadata vectors. Manager retains unique ownership of copied native values rather than direct Python-object transfer, consistent with 377 rationale. Binding detached Permission methods inherits uninitialized manager-pointer risk; pybind STL conversion also means reference policy alone is not proof returned children dict mutates original map.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/permissions.cpp`.

Coverage: 212 canonical patch lines; 3 changed paths.

<a id="commit-456"></a>
### 456. feat: add permissions module {#commit-456}

Source: [d7e8726e35dd5601b0e67a2a4ee379aff98e0056](https://github.com/EndstoneMC/endstone/commit/d7e8726e35dd5601b0e67a2a4ee379aff98e0056) · authored 2024-03-21T02:09:11Z · parent `66a44d03a74dc0b5396a25e28a9463e1b071ae95`.

Author: **Vincent**.

Adds public permissions facade re-exporting five bound types. Discoverability/import surface only; no new permission behavior.

Changed paths: `python/src/endstone/permissions.py`.

Coverage: 15 canonical patch lines; 1 changed paths.

<a id="commit-458"></a>
### 458. fix: rename "default_value" argument to "default" {#commit-458}

Source: [9346b850c46bb8daaaaabe42e6bd5b99edee2ef1](https://github.com/EndstoneMC/endstone/commit/9346b850c46bb8daaaaabe42e6bd5b99edee2ef1) · authored 2024-03-21T02:16:31Z · parent `820ff4a3a69d50c3d858e1d1867873a251908b6a`.

Author: **Vincent**.

Renames Python Permission constructor keyword/property default_value to default. Matches upcoming declarative permission dictionaries, while C++ names remain unchanged. Generated stubs lag until 460.

Changed paths: `src/endstone_python/permissions.cpp`.

Coverage: 18 canonical patch lines; 1 changed paths.
