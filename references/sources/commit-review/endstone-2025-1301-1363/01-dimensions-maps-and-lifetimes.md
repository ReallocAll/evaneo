<!-- retrieval: {"source_ids":["public:commit:641d0eec3c26c9a246ac072e33967e31ecda4207","public:commit:6c0e04b0a9c6cb531aa921161ec3fadef69649dc","public:commit:8b0babbe7dae604a1e84d8fb90aa5c431233c172","public:commit:ca42dc07c3da9bc55719e2143361cdb2c0afdb76"],"source_type":"public","date":"2025-11-15..2025-11-18","topics":["lifetime","ffi","testing","build","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Dimensions, maps and borrowed lifetimes {#dimensions-maps-and-borrowed-lifetimes}

## Causal reading {#causal-reading}

The prior main boundary had portal event wiring and an empty transition helper. 1301 supplies cooldown/axis/entrance-position work, while 1302 closes a Python export gap. The existing portal hook is still authoritative for destination dimension: it adopts plugin-edited coordinates without adopting the event's changed dimension. Filling a helper does not prove the whole event contract is complete.

Stable's compilation-fix commit 1305 is also a behavioral map-cleanup backport. A gameplay-user removal callback walks all maps and removes trackers/decorations. The explanatory source comment connects tracker retention to a large loaded chunk area. This is useful causal evidence for clearing cache membership at a lifecycle boundary; the magnitude and memory effect remain the author's diagnosis. Accessors, native vtable shapes, source-list entries and subscription order are part of the same integration, rather than unrelated boilerplate.

Dimension construction in 1317 explicitly hydrates wrappers from the native manager after creating vanilla dimensions. That addresses worlds whose dimensions predate subscription. But a later callback captures a local helper by reference. The local Subscription type has no disconnecting destructor; it only holds a weak_ptr, while SubscriptionBody has a strong_self member. Therefore a discarded subscription token does not prove the callback is immediately removed. The lifetime issue is the captured helper (and ultimately the wrapper owner), not an assumed RAII disconnect.

## Boundaries and tradeoffs {#boundaries-and-tradeoffs}

- Portal transition fields are only partially assigned. Persistent cooldown access assumes the component exists.
- Map cleanup is linear over maps and removes the first matching tracker. The reconstructed UniqueId comparison does not compare type tags, so mixed entity/block identities deserve care.
- Native dimension/actor/block storage remains externally owned. Weak wrappers and control blocks detect some invalidation but do not establish a common canonical lifetime policy.
- No map-memory benchmark, world-load reproduction or native callback test was run. The useful lesson is tracing initialization and teardown together with the exact ownership implementation.

Selected endpoint snapshots under context/endpoint-1352 and context/endpoint-1363 support comparisons of inherited state; unchanged lines are not analyzed further.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1301"></a>
## Commit 1301 {#commit-1301}

641d0eec3c26c9a246ac072e33967e31ecda4207 · 2025-11-16T19:44:00Z

[feat: implement `Actor::_setDimensionTransitionComponent`](https://github.com/EndstoneMC/endstone/commit/641d0eec3c26c9a246ac072e33967e31ecda4207)

**Change and causal context.** Fills the previously empty Actor::_setDimensionTransitionComponent. Nether-related transitions outside an End origin update the persistent portal cooldown and inspect portal_axis unless the stored block position equals the new BlockPos::MAX sentinel. The transition ECS component records current position and axis. Adds the native component layouts/PortalAxis enum and corrects templated BlockType::getState to return T, including an explicit fallback conversion. Exports PlayerPortalEvent to Python.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** It does not assign portal_entrance_dimension or existing_target_position; the persistent cooldown component is assumed present. The existing ServerPlayer hook still uses its original destination dimension after accepting event-modified coordinates. This is completion of part of a staged transition, not proof of complete portal semantics.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1302"></a>
## Commit 1302 {#commit-1302}

ca42dc07c3da9bc55719e2143361cdb2c0afdb76 · 2025-11-16T20:21:34Z

[fix: add missing exports](https://github.com/EndstoneMC/endstone/commit/ca42dc07c3da9bc55719e2143361cdb2c0afdb76)

**Change and causal context.** Adds PlayerDimensionChangeEvent to the Python lazy-export list, following the native event/binding introduced in the previous chunk. The one-line change repairs public discoverability without changing dispatch timing.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Static source observation only; no build, test or runtime outcome independently established.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1305"></a>
## Commit 1305 {#commit-1305}

8b0babbe7dae604a1e84d8fb90aa5c431233c172 · 2025-11-17T17:06:26Z

[fix: resolve compilation errors](https://github.com/EndstoneMC/endstone/commit/8b0babbe7dae604a1e84d8fb90aa5c431233c172)

**Change and causal context.** The compilation-fix title covers substantive stable backport work: maps/gameplay-user-manager vtables and concrete map/tracker accessors, dirty rectangles, map decoration removal, map-data enumeration, and a retained gameplay-user-removed subscription which removes the departing player from every map. Both chunk callbacks move AtFront to AtBack; scheduler gets a concrete accessor. Debug printf is temporarily added.

**Rationale and attribution.** Code comment reports stale trackers retain a 256×256 chunk region and motivates disconnect cleanup. Preserve that as author diagnosis, not independently measured memory savings. Much overlaps the sibling main-line map work; this stable occurrence is independently read, not silently counted as a separate invention.

**Limits and counterexamples.** Map tracker UniqueId equality chooses a field from the left type but never compares the two types; only the first matching tracker/decoration is erased. Native layout, callback ordering, memory retention and build success are not measured.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1317"></a>
## Commit 1317 {#commit-1317}

6c0e04b0a9c6cb531aa921161ec3fadef69649dc · 2025-11-18T13:50:53Z

[fix: resolve a dimension-related crash](https://github.com/EndstoneMC/endstone/commit/6c0e04b0a9c6cb531aa921161ec3fadef69649dc)

**Change and causal context.** DimensionManager exposes existing owned dimensions and synchronous forEachDimension traversal. EndstoneLevel first creates vanilla dimensions, enumerates all existing dimensions into weak-backed wrappers, then subscribes for later additions, avoiding dependence on creation events that may already have occurred.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** The later callback captures constructor-local add_dimension by reference, which can dangle after construction. The returned subscription is discarded, but local Subscription is only a weak_ptr shell and the body has strong_self, so token destruction does not establish immediate disconnection. No lifecycle behavior is executed.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.
