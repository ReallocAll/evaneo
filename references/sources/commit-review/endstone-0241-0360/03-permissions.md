<!-- retrieval: {"source_ids":["public:commit:08e2f6bfe7f477d6cbe1eb1453f96a3dd6ef007c","public:commit:09ac946f5d2bbd45f91b00263e51f48e5acaefeb","public:commit:24ed96cb1de0d7439a010f93888655a8479cf16b","public:commit:3b9b8718b881c4d22dd98d278c21185a2957befc","public:commit:59695a93d4407a358599ce3b8989310c3b90b99f","public:commit:6146d2e0e0aaadc323f2a714b01cbe77bf1b316e","public:commit:6a07098c9aa38a4106409091799901c689c6042c","public:commit:8122dbfacbcf78eb246fcbcd99639a02cc339753","public:commit:84e5357d992ac29abbaa2e62bf16f013217caf3a","public:commit:9674fb3f8a75ccae5aa7691e204dd191d9029497","public:commit:a72c254534085680fd08a05af71093137306b33f","public:commit:a769fa5bb2eeca3fbf10a025a7ed44865942a5d6","public:commit:b6e604d52a11b3f43f258844352ef2266f5853a5","public:commit:e364b134fcde9298da6c867614cbe2c35a8e6e69","public:commit:e61802eb2c159cfda325f31076d8b787c12d250b","public:commit:e6b82e2940b08b3fca799d9acb6037136c45a18c","public:commit:f4e2d37b5e91bf2c57f6a1e819da6a88fd57b673","public:commit:fba6a33c574e6a981e9ea11093009a7c8af85b2e"],"source_type":"public","date":"2024-03-11..2024-03-13","topics":["lifetime","ffi","testing","api","diagnosis","documentation","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Permission graphs, subscriptions and command enforcement {#permission-graphs-subscriptions-and-command-enforcement}

## Result and development stage {#result-and-development-stage}

336–359 build a C++ permission system from role interfaces through registration, attachment caches and built-in enforcement. It is incremental scaffolding: comments, public interfaces, concrete storage, native-origin mapping and actual checks arrive in separate commits. Python's permission base remains an explicit TODO. No permission tests or server execution are added or run in this workunit. The source supports design intent and bounded counterexamples, not a claim that authorization was complete or secure at this date.

## Roles, defaults and owned versus borrowed state {#roles-defaults-and-owned-versus-borrowed-state}

ServerOperator defines operator status; Permissible adds explicit/default queries, attachments and recalculation. PermissionDefault separates unconditional true/false from operator/nonoperator policies. Permission owns its name, description, default and child map. EndstonePluginManager stores shared Permission owners, lowercase lookup keys, raw default-set pointers and subscription indexes of borrowed Permissible pointers. Permission.init attaches the manager after registration. Its pointer is not initialized before that, so checking it for null does not establish a safe detached-object state.

PermissibleBase composes with an operator and a parent permissible. It uniquely owns attachments and effective PermissionAttachmentInfo values, whose plugin/permissible/attachment relationships are borrowed. Enumeration returns pointers into that cache; recalculation clears and rebuilds it. Consumers cannot safely assume those pointers survive a mutation. PermissionAttachment returns a copy of its map, and set/unset operations trigger recalculation. Permission.getChildren instead exposes a mutable map with an explicit caller obligation to recalculate afterward. These two APIs make different mutation/invalidation tradeoffs.

Attachments document a requirement for enabled plugins, but the concrete creation path does not check it in this unit. Removal invokes a callback before erasing the attachment, then recalculates. The observed callback timing is useful when considering lifetime and reentrancy, but no callback exception/reentrancy policy is specified. This review does not infer one.

## Registration, transfer and invalidation {#registration-transfer-and-invalidation}

343 implements registry and default/subscription storage. Its first addPermission moves a shared pointer into the map then dereferences the moved-from local. 345 explicitly reports and fixes that crash by using the stored map entry. This is a small, decisive ownership-transfer lesson: access after transfer must follow the new owner. 344 adds a nullptr guard but does not itself fix the moved-pointer problem.

Default sets are split by operator state. Recalculation removes a permission from both sets, inserts it into applicable new sets and asks subscribers to refresh. However, both subscribe functions copy the inner map into a local variable before adding the subscriber. The stored index remains empty. Thus 359's final hierarchy recalculation expresses the right dependency ordering but does not prove live invalidation worked. This is a directly visible storage/reference mismatch; no runtime diagnosis is claimed.

Removal erases registry ownership without cleaning default raw-pointer sets. clearPlugins now also destroys loaders and clears permissions/default sets, but does not clear subscription indexes. These observations limit conclusions about dynamic removal and teardown; they are not an exhaustive audit. They explain why registration, ownership and cache invalidation must be considered together rather than assigning correctness to each public method independently.

## Effective graph computation and precedence {#effective-graph-computation-and-precedence}

346 recalculates by unsubscribing old state, loading defaults for the current operator status, then expanding attachment values. Child values are XORed with inherited inversion, so denying a parent reverses the child polarity. The implementation recursively traverses child graphs without cycle detection. It inserts into the effective map with emplace, preserving an existing value instead of replacing it. Since defaults are inserted first, an attachment for an already-populated permission may fail to override it. Conflicting inherited defaults also depend on traversal through unordered sets/maps.

These are important counterexamples to reading the intended explicit/default API as a proven precedence policy. The source would benefit from tests describing positive/negative parent expansion, explicit denial over a true default, conflicting parents and cycles, but this review did not add or execute those tests. Recommendations here are future validation questions, not claims of historical test practice.

## Built-in defaults and sender identity {#built-in-defaults-and-sender-identity}

344 registers endstone and endstone.command parents with plugins/version children defaulting true for everyone. This happens after plugin enable callbacks. 359 explicitly recalculates parent permissions after children are added, following the mutable-child-map contract. Duplicate add returns null and hierarchy callers assume successful registration, so repeated enable/default-registration behavior is not established. No persistent permission configuration or disk storage is added; metadata setters explicitly describe temporary changes.

349 initially makes generic sender adapters concrete with permission delegation while isOp still returns false. 352 records planned origin-specific policies in TODO comments. 354 introduces a persistent console sender with logger-based output and immutable operator status. 355 renames it to ServerCommandSender and extracts common BaseCommandSender behavior, while the generic adapter now maps Admin/Host/Owner/Internal host permission levels to operator. Setter calls report unsupported changes. The generic adapter remains temporary per command, so its attachments are not a persistent player permission system. Specialized player, entity, block and minecart senders remain TODO.

## A permission predicate is not universal enforcement {#a-permission-predicate-is-not-universal-enforcement}

348 adds command permission lists and visible/silent predicates. An empty list permits execution; otherwise any listed permission is sufficient. That OR behavior should be stated explicitly rather than assumed to require every permission. The built-ins declare their permission names, but 358 is the commit that actually calls testPermission before their work.

A denial sends an error and returns true, indicating that the command invocation was handled. The central adapter uses true to mark output success. Authorization denial and command-handled status are therefore different meanings. The adapter and PluginCommand do not automatically call the predicate for every command at this endpoint, so attaching permission metadata is not universal protection. Python binding likewise does not expose the new Permissible inheritance yet.

## Attribution, application and limits {#attribution-application-and-limits}

Git authorship is recorded for each commit. JavaDoc-style markup removal and the project's earlier Bukkit-like claim are evidence of naming/documentation conventions, not proof of copied source or authorship of an unexamined upstream implementation. Use this dossier to ask explicit questions about graph precedence, invalidation, ownership transfer, mutable child state, sender identity and enforcement placement. Avoid turning incomplete early scaffolding into a lasting recommendation or a current security claim.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-336"></a>
### 336. feat: add ServerOperator interface {#commit-336}

[59695a93d4407a358599ce3b8989310c3b90b99f](https://github.com/EndstoneMC/endstone/commit/59695a93d4407a358599ce3b8989310c3b90b99f) · 2024-03-11T23:33:13Z · meaningful

Author: Vincent. Actual parent: `42bcdcd60cca923a1c7ceae20aaa590d0689a039`. Full individual diff read; static evidence only.

Introduces ServerOperator interface with const isOp and mutable setOp. It establishes the role contract only; no player/console implementation or binding exists yet. The later sender work deliberately gives immutable operator status to server console and maps host permission levels for other origins.

Changed paths: `include/endstone/permissions/server_operator.h`.

<a id="commit-337"></a>
### 337. feat: add Permissible class {#commit-337}

[8122dbfacbcf78eb246fcbcd99639a02cc339753](https://github.com/EndstoneMC/endstone/commit/8122dbfacbcf78eb246fcbcd99639a02cc339753) · 2024-03-11T23:42:58Z · meaningful

Author: Vincent. Actual parent: `59695a93d4407a358599ce3b8989310c3b90b99f`. Full individual diff read; static evidence only.

Defines Permissible as ServerOperator plus explicit/default permission queries, plugin-owned attachment creation/removal, recalculation and effective-permission enumeration. Documents that attachments require enabled plugins; initial API is scaffolding without enforcement or concrete ownership. Effective values initially use unordered_set of value objects, changed to borrowed pointers 343; no value hash/equality implementation accompanies this version.

Changed paths: `include/endstone/permissions/permissible.h`.

<a id="commit-338"></a>
### 338. feat: add PermissionDefualt enums {#commit-338}

[a72c254534085680fd08a05af71093137306b33f](https://github.com/EndstoneMC/endstone/commit/a72c254534085680fd08a05af71093137306b33f) · 2024-03-11T23:48:12Z · small-semantic

Author: Vincent. Actual parent: `8122dbfacbcf78eb246fcbcd99639a02cc339753`. Full individual diff read; static evidence only.

Adds four default states: unconditional true/false, operator and nonoperator. This separates permission fallback policy from explicit attachment values. Typo in commit title does not alter actual PermissionDefault type. Enum names are revised 343.

Changed paths: `include/endstone/permissions/permission_default.h`.

<a id="commit-339"></a>
### 339. feat: add PermissionAttachmentInfo {#commit-339}

[08e2f6bfe7f477d6cbe1eb1453f96a3dd6ef007c](https://github.com/EndstoneMC/endstone/commit/08e2f6bfe7f477d6cbe1eb1453f96a3dd6ef007c) · 2024-03-11T23:59:02Z · meaningful

Author: Vincent. Actual parent: `a72c254534085680fd08a05af71093137306b33f`. Full individual diff read; static evidence only.

Adds PermissionAttachmentInfo as owned permission-name/value plus borrowed Permissible reference and nullable attachment pointer. Null attachment denotes default-derived values. Initial accessors are nonconst;343 makes them const and moves the name. Object lifetime follows its eventual effective-permission cache, not callers holding returned pointers.

Changed paths: `include/endstone/permissions/permissible.h`, `include/endstone/permissions/permission_attachment_info.h`.

<a id="commit-340"></a>
### 340. feat: add PermissionAttachment {#commit-340}

[fba6a33c574e6a981e9ea11093009a7c8af85b2e](https://github.com/EndstoneMC/endstone/commit/fba6a33c574e6a981e9ea11093009a7c8af85b2e) · 2024-03-12T00:16:35Z · meaningful

Author: Vincent. Actual parent: `08e2f6bfe7f477d6cbe1eb1453f96a3dd6ef007c`. Full individual diff read; static evidence only.

Adds PermissionAttachment with borrowed plugin/permissible, owned lowercase permission map and removal callback. Set/unset immediately trigger recalculation; getPermissions returns a copy, avoiding mutation without invalidation through that accessor. remove delegates to Permissible and changes interface return to bool. Header initially calls methods on incompletely declared Permission until 346 adds its include. No enabled-plugin check or concrete ownership exists yet.

Changed paths: `include/endstone/permissions/permissible.h`, `include/endstone/permissions/permission_attachment.h`.

<a id="commit-341"></a>
### 341. docs: update docstrings of PermissionAttachment {#commit-341}

[e61802eb2c159cfda325f31076d8b787c12d250b](https://github.com/EndstoneMC/endstone/commit/e61802eb2c159cfda325f31076d8b787c12d250b) · 2024-03-12T00:17:42Z · mechanical

Author: Vincent. Actual parent: `fba6a33c574e6a981e9ea11093009a7c8af85b2e`. Full individual diff read; static evidence only.

Removes JavaDoc-style link markup from attachment comments without changing behavior. The textual convention alone is insufficient to attribute implementation to an unexamined external source.

Changed paths: `include/endstone/permissions/permission_attachment.h`.

<a id="commit-342"></a>
### 342. feat: add Permission class {#commit-342}

[e6b82e2940b08b3fca799d9acb6037136c45a18c](https://github.com/EndstoneMC/endstone/commit/e6b82e2940b08b3fca799d9acb6037136c45a18c) · 2024-03-12T11:05:04Z · meaningful

Author: Vincent. Actual parent: `e61802eb2c159cfda325f31076d8b787c12d250b`. Full individual diff read; static evidence only.

Introduces Permission metadata/default/child graph and manager-backed subscription invalidation. Child map is mutable with explicit requirement to call recalculatePermissibles after edits; setting default does so automatically. Parent creation and manager pointer injection are incomplete until 343. plugin_manager_ is not initialized in constructor, so null checks do not establish safe pre-registration use. Description/default updates are expressly temporary, not persisted configuration.

Changed paths: `include/endstone/permissions/permission.h`.

<a id="commit-343"></a>
### 343. feat: implement permission system in EndstonePluginManager {#commit-343}

[a769fa5bb2eeca3fbf10a025a7ed44865942a5d6](https://github.com/EndstoneMC/endstone/commit/a769fa5bb2eeca3fbf10a025a7ed44865942a5d6) · 2024-03-12T12:04:58Z · meaningful

Author: Vincent. Actual parent: `e6b82e2940b08b3fca799d9acb6037136c45a18c`. Full individual diff read; static evidence only.

Implements manager registration, lowercase lookup, default sets and subscription indexes using shared Permission ownership and borrowed permissible pointers. Adds init(manager), fixes addParent pointer/reference call, returns effective-info pointers and renames defaults. clearPlugins now also destroys loaders and clears permissions/default sets, a real lifecycle change beyond the title; subscription indexes remain. Initial addPermission dereferences moved-from shared_ptr, repaired 345. Both subscribe methods modify a local map copy, leaving stored subscriptions empty at this endpoint; intended invalidation and actual storage differ. Removal erases registry ownership without cleaning raw default-set pointers. These are bounded static counterexamples, not observed failures or a full security audit.

Changed paths: `include/endstone/detail/plugin/plugin_manager.h`, `include/endstone/permissions/permissible.h`, `include/endstone/permissions/permission.h`, `include/endstone/permissions/permission_attachment_info.h`, `include/endstone/permissions/permission_default.h`, `include/endstone/permissions/server_operator.h`, `include/endstone/plugin/plugin_manager.h`, `src/endstone_core/plugin/plugin_manager.cpp`.

<a id="commit-344"></a>
### 344. feat: add default permissions {#commit-344}

[3b9b8718b881c4d22dd98d278c21185a2957befc](https://github.com/EndstoneMC/endstone/commit/3b9b8718b881c4d22dd98d278c21185a2957befc) · 2024-03-12T13:19:05Z · meaningful

Author: Vincent. Actual parent: `a769fa5bb2eeca3fbf10a025a7ed44865942a5d6`. Full individual diff read; static evidence only.

Adds default endstone and endstone.command hierarchy with plugins/version children granted to everyone, and registers it after plugin enabling. Adds nullptr guard to manager registration. Parent child maps are modified after parents were registered, but final invalidation is absent until 359. Duplicate registration returns null while caller hierarchy code assumes successful registration; repeat-enable behavior has no test here.

Changed paths: `include/endstone/detail/permission/default_permissions.h`, `src/endstone_core/permission/default_permissions.cpp`, `src/endstone_core/plugin/plugin_manager.cpp`, `src/endstone_core/server.cpp`.

<a id="commit-345"></a>
### 345. fix: crash when adding permissions due to invalid (moved) pointer {#commit-345}

[b6e604d52a11b3f43f258844352ef2266f5853a5](https://github.com/EndstoneMC/endstone/commit/b6e604d52a11b3f43f258844352ef2266f5853a5) · 2024-03-12T13:30:42Z · meaningful

Author: Vincent. Actual parent: `3b9b8718b881c4d22dd98d278c21185a2957befc`. Full individual diff read; static evidence only.

Title reports crash from dereferencing moved pointer. Uses shared_ptr stored in successful map insertion rather than the moved-from local when calculating defaults. Clear transfer-of-ownership repair of 343; no change to subscription-copy or removal behavior and no captured runtime result.

Changed paths: `src/endstone_core/plugin/plugin_manager.cpp`.

<a id="commit-346"></a>
### 346. feat: add PermissibleBase {#commit-346}

[24ed96cb1de0d7439a010f93888655a8479cf16b](https://github.com/EndstoneMC/endstone/commit/24ed96cb1de0d7439a010f93888655a8479cf16b) · 2024-03-12T15:54:45Z · meaningful

Author: Vincent. Actual parent: `b6e604d52a11b3f43f258844352ef2266f5853a5`. Full individual diff read; static evidence only.

Implements composable PermissibleBase with borrowed operator/parent and unique ownership of attachments/effective-info cache. Resolves explicit values before registered or global Operator default; recalculation unsubscribes old state, expands defaults then attachments, recursively inverting child values under false parents. Attaching/removing recalculates and removal callback runs before deletion. Actual emplace keeps first value rather than overriding an existing default, while unordered default traversal can affect conflicting inherited values; no cycle detection or enabled-plugin check is added. Returned info pointers invalidate on recalculation. Singular permission directories are relocated to plural; exact unchanged header blob reused and changed include read.

Changed paths: `include/endstone/detail/permission/default_permissions.h`, `include/endstone/detail/permissions/default_permissions.h`, `include/endstone/detail/permissions/permissible_base.h`, `include/endstone/permissions/permissible.h`, `include/endstone/permissions/permission_attachment.h`, `src/endstone_core/command/command_adapter.cpp`, `src/endstone_core/permission/default_permissions.cpp`, `src/endstone_core/permissions/default_permissions.cpp`, `src/endstone_core/permissions/permissible_base.cpp`, `src/endstone_core/server.cpp`.

<a id="commit-348"></a>
### 348. feat: add permission functions to class Command {#commit-348}

[f4e2d37b5e91bf2c57f6a1e819da6a88fd57b673](https://github.com/EndstoneMC/endstone/commit/f4e2d37b5e91bf2c57f6a1e819da6a88fd57b673) · 2024-03-12T17:30:33Z · meaningful

Author: Vincent. Actual parent: `1f7a48003f5d36bab1e81f61b30c62499b881e9d`. Full individual diff read; static evidence only.

Adds command permission metadata and silent/visible predicates; empty list permits all, otherwise any listed permission suffices. CommandSender now inherits Permissible, requiring implementations 349 onward. Plugins/version declare permission names, but execution checks arrive 358. Python binding explicitly leaves Permissible base as TODO, so C++ interface expansion is not Python API parity.

Changed paths: `include/endstone/command/command.h`, `include/endstone/command/command_sender.h`, `src/endstone_core/command/defaults/plugins_command.cpp`, `src/endstone_core/command/defaults/version_command.cpp`, `src/endstone_python/command.cpp`.

<a id="commit-349"></a>
### 349. feat: add dummy implementation of methods from CommandSender {#commit-349}

[09ac946f5d2bbd45f91b00263e51f48e5acaefeb](https://github.com/EndstoneMC/endstone/commit/09ac946f5d2bbd45f91b00263e51f48e5acaefeb) · 2024-03-12T17:47:55Z · meaningful

Author: Vincent. Actual parent: `f4e2d37b5e91bf2c57f6a1e819da6a88fd57b673`. Full individual diff read; static evidence only.

Adds host origin-type enum and delegates sender permission operations to owned PermissibleBase. Initial isOp always false and setOp does nothing with TODOs; interfaces are implemented sufficiently to be concrete without claiming host semantics complete. Adapter is per-command rather than persistent player identity, so attachments on this temporary sender do not establish persistent player permissions.

Changed paths: `include/bedrock/command/command_origin.h`, `include/endstone/detail/command/command_adapter.h`, `src/endstone_core/command/command_adapter.cpp`.

<a id="commit-352"></a>
### 352. docs: add todo notes {#commit-352}

[84e5357d992ac29abbaa2e62bf16f013217caf3a](https://github.com/EndstoneMC/endstone/commit/84e5357d992ac29abbaa2e62bf16f013217caf3a) · 2024-03-12T18:37:15Z · small-semantic

Author: Vincent. Actual parent: `9838b4a82e0d37c34f655b4e477888931ccb667b`. Full individual diff read; static evidence only.

Adds intended origin-specific operator rules and player permission-update TODO while implementation still returns false and does nothing. These comments provide explicit planned policy, not implemented behavior.355 chooses actual host permission-level mapping for generic adapter instead.

Changed paths: `src/endstone_core/command/command_adapter.cpp`.

<a id="commit-354"></a>
### 354. feat: add ConsoleCommandSender for server commands {#commit-354}

[e364b134fcde9298da6c867614cbe2c35a8e6e69](https://github.com/EndstoneMC/endstone/commit/e364b134fcde9298da6c867614cbe2c35a8e6e69) · 2024-03-13T12:11:16Z · meaningful

Author: Vincent. Actual parent: `1115d40660719b59682e56035be304a8f583ab31`. Full individual diff read; static evidence only.

Adds persistent server console sender with logger-based output, constant operator=true and rejected status changes; common ServerCommandSender delegates permission behavior. Dispatch selects server sender for host Server origin and temporary adapter otherwise; specialized player/block/entity types remain TODO. Unknown commands now log and return, but diagnostic arguments are swapped relative to placeholders. Public getConsoleSender and TestServer contract require follow-up 355/356. No permission predicate is yet called centrally.

Changed paths: `include/endstone/detail/command/console_command_sender.h`, `include/endstone/detail/command/server_command_sender.h`, `include/endstone/detail/server.h`, `include/endstone/server.h`, `src/endstone_core/command/command_adapter.cpp`, `src/endstone_core/command/console_command_sender.cpp`, `src/endstone_core/command/server_command_sender.cpp`, `src/endstone_core/server.cpp`.

<a id="commit-355"></a>
### 355. refactor: rename ConsoleCommandSender {#commit-355}

[9674fb3f8a75ccae5aa7691e204dd191d9029497](https://github.com/EndstoneMC/endstone/commit/9674fb3f8a75ccae5aa7691e204dd191d9029497) · 2024-03-13T12:17:28Z · meaningful

Author: Vincent. Actual parent: `e364b134fcde9298da6c867614cbe2c35a8e6e69`. Full individual diff read; static evidence only.

Rename title hides behavior and architecture changes: ConsoleCommandSender becomes ServerCommandSender with name Server; old common class becomes BaseCommandSender shared by adapter and server. Removes explicit server reference from adapter in favor of singleton access. Implements generic isOp from Admin/Host/Owner/Internal host levels, replacing false stub, and logs unsupported mutation. Renames public server getter to getCommandSender; central dispatch still delegates permission enforcement to commands.

Changed paths: `include/endstone/detail/command/command_adapter.h`, `include/endstone/detail/command/command_sender.h`, `include/endstone/detail/command/console_command_sender.h`, `include/endstone/detail/command/server_command_sender.h`, `include/endstone/detail/server.h`, `include/endstone/server.h`, `src/endstone_core/command/command_adapter.cpp`, `src/endstone_core/command/command_sender.cpp`, `src/endstone_core/command/console_command_sender.cpp`, `src/endstone_core/command/server_command_sender.cpp`, `src/endstone_core/server.cpp`.

<a id="commit-358"></a>
### 358. feat: implement permission test in command execution {#commit-358}

[6a07098c9aa38a4106409091799901c689c6042c](https://github.com/EndstoneMC/endstone/commit/6a07098c9aa38a4106409091799901c689c6042c) · 2024-03-13T17:23:18Z · meaningful

Author: Vincent. Actual parent: `1255f6d6cb5e1c8e788b4628e2c2808872a94d51`. Full individual diff read; static evidence only.

Adds permission check at start of built-in plugins/version execute, makes predicates const and returns true after denial so error is treated as handled. Adapter then marks command output success despite denied action; this distinguishes execution-handled bool from authorization. PluginCommand and central adapter still do not automatically enforce configured permission list, so this commit is not universal enforcement.

Changed paths: `include/endstone/command/command.h`, `src/endstone_core/command/defaults/plugins_command.cpp`, `src/endstone_core/command/defaults/version_command.cpp`.

<a id="commit-359"></a>
### 359. fix: recalculate permissions on default permission registration {#commit-359}

[6146d2e0e0aaadc323f2a714b01cbe77bf1b316e](https://github.com/EndstoneMC/endstone/commit/6146d2e0e0aaadc323f2a714b01cbe77bf1b316e) · 2024-03-13T17:45:43Z · meaningful

Author: Vincent. Actual parent: `6a07098c9aa38a4106409091799901c689c6042c`. Full individual diff read; static evidence only.

Calls parent Permission::recalculatePermissibles after finishing command and core hierarchy, implementing documented invalidation requirement for mutable child maps. Adds broadcast-permission TODO. This addresses registration ordering but does not repair empty stored subscription maps from 343; no test proves live subscribers actually refresh.

Changed paths: `src/endstone_core/permissions/default_permissions.cpp`.
