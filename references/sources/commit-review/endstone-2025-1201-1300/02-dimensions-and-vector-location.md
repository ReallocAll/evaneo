<!-- retrieval: {"source_ids":["public:commit:1898407388add699716b28bcb8a793d72b553ea1","public:commit:2c85e6f670e16107ac2c82ee105cde1cbb1c1941","public:commit:2e2c0f4722546d40370f059601096ae7428b2dac","public:commit:3205bea31c7dc7cac3c02c185369bdb897ebacfa","public:commit:3383527c792d74775545b07f0bab8e052daa17db","public:commit:3595ddf9dff94068a042a200b1211cbfaf2aa41f","public:commit:509ea33947ed1c7d7866533d9781ae6c53837dde","public:commit:54c73d79fc7e365969b8894abedab4c603deaa34","public:commit:5d2753895abb4dc9c6dc49b2b3224ed8c7b4846b","public:commit:602b14c71f5fe50cc6a1dcdf90adf5d750de4f9e","public:commit:8640f36a4b07e0eacfdcc60f8dda092380952ec6","public:commit:89f5a5c93664d9d3a29534b9c3ea544ac95854ea","public:commit:8bf9e206d28c8969b7ac2ae4a78178902a0e3ce4","public:commit:aa22e9d1db6ec4abe9cfb9dc09b11e37151bb7e9","public:commit:f6040d1d1c872e3b56f25c934879d85cbe9ae599"],"source_type":"public","date":"2025-11-06..2025-11-09","topics":["lifetime","concurrency","ffi","testing","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Dimensions, vectors and locations {#dimensions-vectors-and-locations}

## Causal chain {#causal-chain}


Dated forward qualification (2026-10-20): Valid for the 1236 implementation and the1201–1300 reviewed boundary: startup requests vanilla dimensions and relies on a creation connector, without enumerating dimensions that already existed. Later resolution: 1317 enumerates existing native dimensions into weak-backed wrappers; the January constructor preserves it at level.cpp31–47. The whole file is identical in both parents and the merge. Treat the earlier population gap as resolved by this history. Remaining distinct limits: The subsequent callback captures constructor-local add_dimension by reference; lifetime remains a separate source-level concern.; Subscription token destruction is not evidence of immediate disconnection: the examined token has weak_ptr state and no disconnecting destructor, with strong_self in its body.; Temporary weak-handle locks and raw returned references still do not establish persistent concurrent ownership. See [later source analysis](../endstone-2025-1301-1363/01-dimensions-maps-and-lifetimes.md#commit-1317) and [January closure](../endstone-2026-merge-closure/dossiers.md#final-state-corrections-and-retained-limits).

1202 realigns ChunkState with more native generation phases, moving Loaded from9 to13. Both the loaded-chunk traversal and callback still use >=Loaded, so Invalid0xff remains admitted by that comparison. Native enum/field changes are ABI assumptions, not validated compatibility.

1229–1238 replace a direct native Dimension reference with WeakRef, move wrapper storage from names to runtime IDs, and populate it through the native creation connector. Startup requests the three vanilla dimensions rather than enumerating existing ones.1231's ineffective fallback loop disappears in1236. Name lookup becomes case-insensitive with a the_end alias; native conversion and map views use integer IDs. The1239 merge leaves one direct member call against the now-weak field;1240 fixes it. This is why both merge-parent residuals are reviewed instead of treating a merge title as proof of correct integration.

The full connector context prevents an overclaim: Subscription has a weak_ptr and no disconnecting destructor, and SubscriptionBody contains strong_self. The discarded creation token is not evidence that registration immediately vanishes. Publisher teardown, callback thread and whether a dimension existed before connection remain external assumptions. WeakStorage::isSet checks expiration; unwrap locks into a temporary StackRefResult. EndstoneDimension::getHandle returns a raw reference after that temporary dies, so it is a validity check rather than a lasting concurrent lifetime pin. Replacing a wrapper at the same runtime ID could also invalidate public Location pointers; no concurrent test is present.

1240 expands Vector mathematics and mutators, including rotations, dot/cross, midpoint, floor and epsilon comparisons.1241 separates Location from Vector, makes a Dimension reference mandatory and relocates coordinates/angles into Location. Removing null dimension construction allows move setters to change from Result to void.1242 restores coordinate bindings, adds dimension-checked distance and direction/angle operations, and removes the newly introduced Vector sequence protocol. No explicit reason accompanies that sequence reversal. Location addition/subtraction does not check matching dimensions, while distance does; zero-length vector normalization/angle remains unchecked.

## Behavior and cost boundaries {#behavior-and-cost-boundaries}

The location redesign improves construction invariants while retaining a nonowning wrapper pointer and breaking former Vector inheritance/signatures.1294 later relies on the ID wrapper map for post-change events, and1300 relies on it for portal locations, so startup population assumptions propagate to events. Constructors/bindings/stubs/callers were read together; no Python extension or server was executed. There are no added vector/location tests in this slice.

## Per-commit decisions and revisions {#per-commit-decisions-and-revisions}

<a id="commit-1202"></a>
### Commit 1202 {#commit-1202}

[5d2753895abb](https://github.com/EndstoneMC/endstone/commit/5d2753895abb4dc9c6dc49b2b3224ed8c7b4846b) · 2025-11-06T03:17:52Z · fix: update `ChunkState`

ChunkState adds structure/decorating/neighbor upgrade phases and moves Loaded from9 to13; Invalid remains0xff. Enum alignment update, no runtime loaded-state proof.

<a id="commit-1228"></a>
### Commit 1228 {#commit-1228}

[aa22e9d1db6e](https://github.com/EndstoneMC/endstone/commit/aa22e9d1db6ec4abe9cfb9dc09b11e37151bb7e9) · 2025-11-09T13:17:58Z · fix: add missing member to `LevelChunk`

Adds native LevelChunk ticking-entity field before loaded_format, a binary-layout repair without measured ABI validation.

<a id="commit-1229"></a>
### Commit 1229 {#commit-1229}

[54c73d79fc7e](https://github.com/EndstoneMC/endstone/commit/54c73d79fc7e365969b8894abedab4c603deaa34) · 2025-11-09T15:26:04Z · refactor: replace direct `Dimension` references with `WeakRef`

Dimension wrapper stores native WeakRef instead of direct reference and throws on !isSet before unwrap; loaded chunk path accesses via getHandle. Lifetime depends on WeakRef contract and server-owned wrappers. Endpoint WeakStorage checks expired and unwrap locks a shared_ptr only for the temporary StackRefResult; returned raw reference does not itself pin lifetime beyond the call.

<a id="commit-1230"></a>
### Commit 1230 {#commit-1230}

[89f5a5c93664](https://github.com/EndstoneMC/endstone/commit/89f5a5c93664d9d3a29534b9c3ea544ac95854ea) · 2025-11-09T15:26:23Z · refactor: update `MapView::getDimension` implementation

MapView resolves native dimension validity then wrapper by name through concrete level; uses singleton accessor.

<a id="commit-1231"></a>
### Commit 1231 {#commit-1231}

[2c85e6f670e1](https://github.com/EndstoneMC/endstone/commit/2c85e6f670e16107ac2c82ee105cde1cbb1c1941) · 2025-11-09T15:29:29Z · fix: improve logging for dimension loading

Startup dimension creation checks isSet and logs failures; attempted unknown-name fallback iterates but never stores or returns found dimension, an intermediate implementation.

<a id="commit-1232"></a>
### Commit 1232 {#commit-1232}

[2e2c0f472254](https://github.com/EndstoneMC/endstone/commit/2e2c0f4722546d40370f059601096ae7428b2dac) · 2025-11-09T15:40:35Z · refactor: add `getEndstoneLevel` method to `EndstoneServer`

Concrete EndstoneServer::getEndstoneLevel accessor removes repetitive public-to-concrete casts in later callers.

<a id="commit-1233"></a>
### Commit 1233 {#commit-1233}

[8640f36a4b07](https://github.com/EndstoneMC/endstone/commit/8640f36a4b07e0eacfdcc60f8dda092380952ec6) · 2025-11-09T15:42:54Z · refactor: replace several `entt::locator` usage with `EndstoneServer::getInstance`

Command origin, damage source, map, scoreboard and dimension conversion use singleton/concrete-level accessor; dimension conversion adopts integer ID overload before its full implementation1235–1236.

<a id="commit-1234"></a>
### Commit 1234 {#commit-1234}

[509ea33947ed](https://github.com/EndstoneMC/endstone/commit/509ea33947ed1c7d7866533d9781ae6c53837dde) · 2025-11-09T15:43:01Z · refactor: make `getDimensionId` method in `IDimension` const

Native IDimension::getDimensionId becomes const, ABI declaration correction without runtime validation.

<a id="commit-1235"></a>
### Commit 1235 {#commit-1235}

[3595ddf9dff9](https://github.com/EndstoneMC/endstone/commit/3595ddf9dff94068a042a200b1211cbfaf2aa41f) · 2025-11-09T15:43:19Z · refactor: update `EndstoneLevel` class to use `std::map` for dimensions

Dimension storage changes name-key unordered_map to integer-key ordered map and declares ID lookup, removes addDimension; implementation follows1236.

<a id="commit-1236"></a>
### Commit 1236 {#commit-1236}

[f6040d1d1c87](https://github.com/EndstoneMC/endstone/commit/f6040d1d1c872e3b56f25c934879d85cbe9ae599) · 2025-11-09T15:50:31Z · refactor: update `Level::getDimension` logics

Creation connector populates runtime-ID wrappers, startup requests vanilla dimensions, name lookup scans case-insensitively with the_end alias, ID lookup direct. Returned connect subscription not stored. Endpoint Subscription contains only weak_ptr and no disconnecting destructor, while body holds strong_self; dropping this token is therefore not evidence of immediate unsubscription. Publisher lifetime and existing-dimension timing remain external assumptions. No existing-dimension enumeration remains.

<a id="commit-1237"></a>
### Commit 1237 {#commit-1237}

[3383527c792d](https://github.com/EndstoneMC/endstone/commit/3383527c792d74775545b07f0bab8e052daa17db) · 2025-11-09T17:14:15Z · refactor: update `MapView::getDimension` to use `runtime_id` from `getDimensionId`

Native getWeakRef wraps weak_from_this; MapView wrapper lookup changes name to runtimeID. Removes unused vanilla dimension-map declaration.

<a id="commit-1238"></a>
### Commit 1238 {#commit-1238}

[8bf9e206d28c](https://github.com/EndstoneMC/endstone/commit/8bf9e206d28c8969b7ac2ae4a78178902a0e3ce4) · 2025-11-09T17:16:15Z · refactor: remove redundant dimension loading log in `Level`

Removes duplicate dimension loading log from creation callback; retains registration.

<a id="commit-1240"></a>
### Commit 1240 {#commit-1240}

[1898407388ad](https://github.com/EndstoneMC/endstone/commit/1898407388add699716b28bcb8a793d72b553ea1) · 2025-11-09T18:51:16Z · feat: enhance `Vector` with new methods

Vector gains floored coordinates, epsilon equality, dot/cross/midpoint, rotations, bounds, mutators and Python operators/indexing. Zero-length normalize/angle remain unchecked. Formatter adds trailing comma. Also repairs spawnActor WeakRef accessor integration from1239. No vector tests added.

<a id="commit-1241"></a>
### Commit 1241 {#commit-1241}

[602b14c71f5f](https://github.com/EndstoneMC/endstone/commit/602b14c71f5fe50cc6a1dcdf90adf5d750de4f9e) · 2025-11-09T19:41:23Z · refactor: remove `Vector` inheritance from `Location` and adjust constructor

Location stops inheriting Vector, requires dimension reference first, stores separate coordinates, includes dimension/angles in equality, changes move setters from Result to void because null-dimension construction removed. All core/hooks/bindings constructors migrate; raw wrapper pointer lifetime remains. Python coordinate properties absent until1242. Vector setter lambdas restore None stubs.

<a id="commit-1242"></a>
### Commit 1242 {#commit-1242}

[3205bea31c7d](https://github.com/EndstoneMC/endstone/commit/3205bea31c7dc7cac3c02c185369bdb897ebacfa) · 2025-11-09T20:18:17Z · feat: extend `Location` with new methods

Location restores explicit coordinate/block/direction bindings, adds dimension-checked distance Result, numeric/in-place operations, yaw wrapping and pitch clamping. Adding/subtracting locations does not check dimensions; documented length is world-independent. Removes newly added Vector sequence protocol without explicit rationale.
