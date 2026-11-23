<!-- retrieval: {"source_ids":["public:commit:08d27356a6a6d97ed692ff65b9f78d0d0f0aa723","public:commit:11d9c80e560ce0de1e5aba4e80ea84a87241ea31","public:commit:50373afd233cd72daf8df72a417fb42b954d8e87","public:commit:6e6662e73c3291e044f86534443180d0613d8c74","public:commit:81794818a24d31f104373ecbe62f4d8c147ebc59","public:commit:dc383150db7a94ea4bb48a60b09b26781e196af5","public:commit:e6e8033b010977d5aed1e4f4b113014767516637"],"source_type":"public","date":"2024-06-29..2024-07-01","topics":["lifetime","concurrency","ffi","testing","diagnosis","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Ownership and scheduler boundaries {#ownership-and-scheduler-boundaries}

## A dated ownership experiment, not a single stable rule {#a-dated-ownership-experiment-not-a-single-stable-rule}

The registry scaffold at 1281 introduces custom pointer layouts. SharedPtr becomes operational on June 29 (1286), deleting the object at the last shared count and retaining the control block for weak references. WeakPtr then gains promotion/expiration operations (1287), with friendship and a changed promotion guard at 1288. The default weak control-block member remains uninitialized, and check-then-increment is not an atomic acquire-if-live protocol. These concrete limits matter because native object representation and C++ ownership semantics are being made to coexist.

On July 1, 1312 removes promotion entirely: WeakPtr exposes raw pointer-style access and item consumers stop retaining a shared handle during the read. This is a real reversal of the just-added interface. The final model is borrowed access, so the host registry/item lifetime must protect those reads. No commit message here gives a general rationale for abandoning lock, and no race/destruction experiment establishes which implementation was intended to own native objects in every path. Preserve dates and local behavior instead of selecting one revision as the author's timeless ownership philosophy.

The same patch warns that ItemStackBase::getName crashes and switches creative output to a full item identifier. That warning establishes an observed problem in the source commentary, not its cause. The ownership change, virtual-name call, native model and thread context all coexist. It would be unsupported to assert that raw access caused the crash, or that the later thread change definitively cured it. Removing the warning at 1318 is recorded without upgrading it to measured success.

## Scheduling native work changes more than the call site {#scheduling-native-work-changes-more-than-the-call-site}

The pre-existing scheduler had plugin-owned tasks. At 1316 addTask centralizes queue/map insertion but loses the prior enqueue-failure return path. At 1317 a plugin-less one-shot task supports internal server work. The owner member changes from reference to pointer, yet the plugin-less constructor leaves it uninitialized and getOwner dereferences it unconditionally. Full scheduler context confirms cancellation by plugin still uses that owner contract. This is an immediate boundary mismatch created by widening who may schedule, not a speculative claim about a particular crash occurring.

At 1318, VanillaData::get queues the native dump to run on the server thread. The lambda builds a local dataset before emplacing it in the locator. That ordering improves on 1303's publish-before-fill approach and directly expresses thread-affinity intent in a comment and title. However, before the first result exists, several GUI reads can each enqueue work; there is no in-progress marker. Locator availability/read access occurs on the GUI side while emplacement occurs on the server side, and this source does not show synchronization for that shared publication. The concurrent queue only covers task transport, not every surrounding mutable object or registry lifetime.

## Costs, alternatives actually observed, and limits {#costs-alternatives-actually-observed-and-limits}

Observed alternatives are retained: shared promotion versus raw borrowed access; synchronous UI extraction versus server-scheduled extraction; publish-then-fill versus local-fill-then-publish; required Plugin ownership versus internal tasks without a Plugin. There is no need to invent a broader architecture proposal to explain the changes. A future implementation applying the lessons would need to decide ownerless cancellation semantics, queue-failure handling, in-flight suppression, result publication and host lifetime explicitly. Those are implications of the read code, not completed work or measured defects in a deployed version.

Use this case for task systems that outgrow their original ownership assumption and for UI tools reading thread-affine engine state. It supports distinguishing data ownership, object lifetime, execution context and publication. No tests were added in this unit and no upstream code was executed. Static source evidence is strong for the described transitions; shutdown causes, race manifestation and crash causality remain unknown.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1286"></a>
### 1286: feat: implement SharedPtr {#commit-1286}

Source: [08d27356a6a6d97ed692ff65b9f78d0d0f0aa723](https://github.com/EndstoneMC/endstone/commit/08d27356a6a6d97ed692ff65b9f78d0d0f0aa723), 2024-06-29T20:59:42Z; git author Vincent. Disposition: substantive.

Implements the custom SharedPtr control block with shared/weak counts, copy increments, moves, copy-swap/reset and last-shared deletion of the object, followed by control-block deletion when no weak references remain. These are host-interoperability models, not std::shared_ptr. Atomic counts alone do not prove coordinated concurrent lifetime safety for the separately stored pointer/control block.

<a id="commit-1287"></a>
### 1287: feat: implement WeakPtr {#commit-1287}

Source: [e6e8033b010977d5aed1e4f4b113014767516637](https://github.com/EndstoneMC/endstone/commit/e6e8033b010977d5aed1e4f4b113014767516637), 2024-06-29T21:20:07Z; git author Vincent. Disposition: staging.

Implements custom WeakPtr copy/move/destruction/reset, expired and lock. The default control-block pointer is not initialized; lock checks a count and then increments separately rather than using an atomic promotion protocol. It also accesses private SharedPtr state until friendship is added next. This intermediate implementation must not be summarized as established safe weak ownership.

<a id="commit-1288"></a>
### 1288: feat: add basic item data to DevTools {#commit-1288}

Source: [dc383150db7a94ea4bb48a60b09b26781e196af5](https://github.com/EndstoneMC/endstone/commit/dc383150db7a94ea4bb48a60b09b26781e196af5), 2024-06-29T21:33:53Z; git author Vincent. Disposition: mixed_change.

Adds WeakPtr friendship and changes lock's acceptance condition from positive shared count to non-null pointee. Expands item data queries, tags/export scaffolding and removes the demo window. The condition change does not by itself close a concurrent destruction/promotion race; later 1312 removes promotion entirely. Preserve the GUI feature and ownership experiment as separate facts.

<a id="commit-1312"></a>
### 1312: feat: expand creative item details in DevTools {#commit-1312}

Source: [50373afd233cd72daf8df72a417fb42b954d8e87](https://github.com/EndstoneMC/endstone/commit/50373afd233cd72daf8df72a417fb42b954d8e87), 2024-07-01T09:37:50Z; git author Vincent. Disposition: mixed_change.

Removes custom WeakPtr::lock/expired in favor of raw get, dereference, arrow and bool access, and updates item consumers accordingly. Adds a comment that calling getName leads to a crash, while creative exports use the full item identifier instead and add damage, NBT and block runtime ID. Borrowed access no longer retains the item during use. The patch does not establish that the ownership reversal caused the reported crash.

<a id="commit-1316"></a>
### 1316: refactor: add EndstoneScheduler::addTask {#commit-1316}

Source: [81794818a24d31f104373ecbe62f4d8c147ebc59](https://github.com/EndstoneMC/endstone/commit/81794818a24d31f104373ecbe62f4d8c147ebc59), 2024-07-01T11:19:23Z; git author Vincent. Disposition: mixed_change.

Extracts EndstoneScheduler::addTask to centralize queue insertion and task-map registration. In doing so, drops the previous enqueue-failure branch that returned null: the helper ignores the enqueue result and stores the task anyway. This is a semantic failure-path change under a refactor title, not merely code motion. No queue-pressure test is supplied.

<a id="commit-1317"></a>
### 1317: feat: allow the server to enqueue a task without a plugin instance {#commit-1317}

Source: [6e6662e73c3291e044f86534443180d0613d8c74](https://github.com/EndstoneMC/endstone/commit/6e6662e73c3291e044f86534443180d0613d8c74), 2024-07-01T11:31:55Z; git author Vincent. Disposition: api_change.

Allows a server task without a Plugin by adding a one-shot runTask overload and Task constructor. Converts the owner reference to a pointer, but the plugin-less constructor does not initialize it and getOwner still dereferences it. Full scheduler context shows cancellation-by-plugin assumes every task has an owner. The new internal use case therefore exposes an unresolved owner-contract boundary.

<a id="commit-1318"></a>
### 1318: feat: ensure the dumper is run on server thread instead of UI thread {#commit-1318}

Source: [11d9c80e560ce0de1e5aba4e80ea84a87241ea31](https://github.com/EndstoneMC/endstone/commit/11d9c80e560ce0de1e5aba4e80ea84a87241ea31), 2024-07-01T11:40:22Z; git author Vincent. Disposition: substantive.

Explicitly schedules native dumping on the server thread instead of the UI thread. Builds a local VanillaData, fills it and then publishes through the locator, improving the order relative to 1303. Removes the getName crash comment. The thread change is stated; a causal crash fix is not measured. Repeated UI requests can queue work before publication, and locator read/write synchronization is not shown.
