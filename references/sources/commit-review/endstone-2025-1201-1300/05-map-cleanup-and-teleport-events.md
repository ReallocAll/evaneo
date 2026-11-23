<!-- retrieval: {"source_ids":["public:commit:12f4bb70aa69c0cfabaf6ecf73b53ed0414c022d","public:commit:1320cf171ab8c71ded7c724cb840d410120a640d","public:commit:4359c282c63bb90e6cb46ba6a88d2765e078adc1","public:commit:4ecb2b1ba4250bb806bf299943aaa8a8f3dd466e","public:commit:88965ce11107db4ea2553ac24ca325bb1cc28bb1","public:commit:ae7f359ee6009935b503967f314366db63baab10","public:commit:c0765cc521d22520d26e1dd934716f89362d3f27","public:commit:c859714d52cf1f8503d40721937daf4321eddc77","public:commit:d2ebb2b7d6a5a145958af4676a909d04e7d9e298","public:commit:d520c1938da8777f75e9e9a40e2ef9e1a36745f6"],"source_type":"public","date":"2025-11-14..2025-11-16","topics":["lifetime","ffi","api","diagnosis","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Map cleanup and teleport events {#map-cleanup-and-teleport-events}

## Explicit retention diagnosis {#explicit-retention-diagnosis}

1292 contains the clearest explicit causal rationale in the slice: stale disconnected-player map trackers hold ChunkViewSource areas, retaining chunks and memory. The comment describes a256×256 area; this is an author report, not a measurement reproduced here. The new stored gameplay-user-removed subscription scans all maps, removes the matching tracker and decoration, and marks persistent decoration changes dirty.1293 removes its temporary printf. Existing chunk-load/unload/map-create subscriptions move from AtFront to AtBack, an ordering change with no separate rationale in the message.

The cleanup costs a traversal of maps and linear tracker/decoration searches on removal. UniqueId equality chooses its comparison using only the left operand kind, without verifying the other kind; this is a cross-kind matching risk. The patch addresses this particular retention mechanism, not every chunk lifecycle problem or a measured overall leak elimination.

## Teleport route and event timing {#teleport-route-and-event-timing}


Dated forward qualification (2026-10-20): Valid for the 1297–1300 staged teleport/portal implementation and the reviewed1300 main endpoint c859714d52cf1f8503d40721937daf4321eddc77: _setDimensionTransitionComponent is a newly added empty body. Later resolution: 1301 supplies cooldown/axis/entrance-position implementation; the January merge preserves it at actor.cpp296–311. Do not describe the helper as empty at this merge. Remaining distinct limits: The portal hook still copies event-edited coordinates without adopting destination dimension/orientation changes.; 1301 does not assign every transition field and assumes the persistent cooldown component exists.; True from teleport remains request-path acceptance rather than confirmed completion; no runtime validation. See [later source analysis](../endstone-2025-1301-1363/01-dimensions-maps-and-lifetimes.md#commit-1301) and [January closure](../endstone-2026-merge-closure/dossiers.md#final-state-corrections-and-retained-limits).

1294 publishes a noncancellable dimension-change after-event, resolving old/new wrappers by runtime ID.1296 moves health from Actor to Mob and changes teleport to bool with const-reference arguments.1297 supplies the core/Python migration and replaces command-based target computation with direct native teleport or dimension transfer requests. Removed actors/dead mobs are rejected. Rotation is assigned before requesting the move. The method returns true after requesting it, so true does not mean a cross-dimension transition completed or that a subsequent PlayerTeleportEvent accepted it. The existing native teleport hook can cancel independently.

1299 declares PlayerPortalEvent as a teleport-event subtype.1300 replaces ServerPlayer::changeDimension: obtain/create destination, ask native transferer for a candidate location, call the event, return on cancellation, copy the event's edited coordinates and submit the request. It also initializes ChangeDimensionRequest::state to PrepareRegion, repairing1297's uninitialized field. The hook does not copy an edited destination dimension or orientation. Its call to _setDimensionTransitionComponent reaches a newly added empty local body rather than implementing a cooldown/transition update. No original-call fallback exists in this hook.

1290 separately makes drop_item and spawn_actor bindings explicitly nonowning references. That prevents accidental default ownership transfer, while native actor removal lifetime remains a distinct issue. Native vtable/field/symbol additions for transfer machinery are source-level porting evidence, not runtime ABI validation.

## Application and limits {#application-and-limits}

Use this chain to distinguish notification-after-action from cancellable-before-request events, to interpret boolean results honestly, and to audit all fields of an editable destination. For retention work, trace the owning object to its resource and cleanup trigger, then preserve traversal cost and lifecycle assumptions. No server, client, benchmark or concurrency test was executed.

## Per-commit decisions and revisions {#per-commit-decisions-and-revisions}

<a id="commit-1290"></a>
### Commit 1290 {#commit-1290}

[4359c282c63b](https://github.com/EndstoneMC/endstone/commit/4359c282c63bb90e6cb46ba6a88d2765e078adc1) · 2025-11-14T20:25:36Z · fix: correct return value policies for `drop_item` and `spawn_actor`

Explicit Python reference return policies for drop_item/spawn_actor prevent default owning interpretation of server-owned actor pointers. Does not independently solve native actor removal lifetime.

<a id="commit-1292"></a>
### Commit 1292 {#commit-1292}

[d520c1938da8](https://github.com/EndstoneMC/endstone/commit/d520c1938da8777f75e9e9a40e2ef9e1a36745f6) · 2025-11-15T03:11:54Z · fix(chunk): address chunk leak caused by stale map player trackers

Explicit source rationale: disconnected map trackers retain ChunkViewSource areas and memory. Stored gameplay-user-removed subscription purges player tracker and decoration from every map, marks persistent decorations dirty, and moves chunk/map subscriptions from AtFront to AtBack. UniqueId equality compares payload by left-hand kind without checking other kind. Comment reports256×256 retention, not measured here.

<a id="commit-1293"></a>
### Commit 1293 {#commit-1293}

[12f4bb70aa69](https://github.com/EndstoneMC/endstone/commit/12f4bb70aa69c0cfabaf6ecf73b53ed0414c022d) · 2025-11-15T03:12:11Z · fix(server): remove redundant debug log

Removes temporary printf from disconnect tracker cleanup; semantics unchanged.

<a id="commit-1294"></a>
### Commit 1294 {#commit-1294}

[1320cf171ab8](https://github.com/EndstoneMC/endstone/commit/1320cf171ab8c71ded7c724cb840d410120a640d) · 2025-11-15T15:11:25Z · feat(event): add `PlayerDimensionChangeEvent` for dimension transitions

Adds noncancellable PlayerDimensionChangeEvent after native change, binding dimensions by reference and resolving runtime IDs without null checks. Script handler uses singleton accessor and includes new after-event visitor; unrelated commented bed-event bindings removed.

<a id="commit-1295"></a>
### Commit 1295 {#commit-1295}

[ae7f359ee600](https://github.com/EndstoneMC/endstone/commit/ae7f359ee6009935b503967f314366db63baab10) · 2025-11-15T23:51:38Z · refactor: update `ChangeDimensionRequest` struct

Makes ChangeDimensionRequest::State public, preserves enumerator values/order and removes offset comments; fields remain uninitialized until later default-state repair.

<a id="commit-1296"></a>
### Commit 1296 {#commit-1296}

[c0765cc521d2](https://github.com/EndstoneMC/endstone/commit/c0765cc521d22520d26e1dd934716f89362d3f27) · 2025-11-16T18:29:47Z · refactor(actor): move health-related methods from `Actor` to `Mob`

Moves public health contract from Actor to Mob and simultaneously changes teleport signatures to bool/const-reference. Core/binding adaptations follow1297; intermediate interface mismatch is part of staged change.

<a id="commit-1297"></a>
### Commit 1297 {#commit-1297}

[88965ce11107](https://github.com/EndstoneMC/endstone/commit/88965ce11107db4ea2553ac24ca325bb1cc28bb1) · 2025-11-16T18:32:06Z · feat(actor): improve `teleport` method implementation

Replaces command-computed teleport with direct actor teleport or dimension-transfer APIs; false for removed/dead entities, rotation set before transfer, otherwise true after request. Player cross-dimension path constructs ChangeDimensionRequest but state is uninitialized until1300. Core/Python health moves to Mob. True reports accepted path, not completion or uncancelled native hook.

<a id="commit-1298"></a>
### Commit 1298 {#commit-1298}

[d2ebb2b7d6a5](https://github.com/EndstoneMC/endstone/commit/d2ebb2b7d6a5a145958af4676a909d04e7d9e298) · 2025-11-16T18:34:36Z · refactor: remove unused symbols

Removes unused TeleportCommand wrapper bodies and both-platform symbols after direct teleport route. No additional behavior inferred.

<a id="commit-1299"></a>
### Commit 1299 {#commit-1299}

[4ecb2b1ba425](https://github.com/EndstoneMC/endstone/commit/4ecb2b1ba4250bb806bf299943aaa8a8f3dd466e) · 2025-11-16T18:41:40Z · feat: add `PlayerPortalEvent`

Defines PlayerPortalEvent subclass of teleport event and binds/stubs it. Hook follows1300; no independent event emission yet.

<a id="commit-1300"></a>
### Commit 1300 {#commit-1300}

[c859714d52cf](https://github.com/EndstoneMC/endstone/commit/c859714d52cf1f8503d40721937daf4321eddc77) · 2025-11-16T19:20:42Z · feat: implement `PlayerPortalEvent`

Hooks ServerPlayer::changeDimension, creates target dimension, asks transferer to calculate portal destination, emits cancellable event, copies edited coordinates and submits request. Initializes request state, adds native transfer-manager ABI shapes and dimension component lookup. Does not adopt event-edited destination dimension/rotation; calls newly added empty _setDimensionTransitionComponent instead of original hook, so transition/cooldown side effect is absent in this local body. Native behavior remains unvalidated.
