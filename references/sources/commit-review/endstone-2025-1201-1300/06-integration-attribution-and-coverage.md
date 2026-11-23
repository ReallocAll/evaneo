<!-- retrieval: {"source_ids":["public:commit:0bc6a065b33fa388106be3d6c1e34830308ee2ee","public:commit:1ee9f8e03a0230efce17ebd1290b652a1cfd67d3","public:commit:380ea95971663e479bcad9cce721ae0574c7d2ef","public:commit:51ce819a7d8a0c7aac601fa2b31290fcec76fd95","public:commit:552177f0659c444c3c41d751561898db63d23d5a","public:commit:6c1c4d57bf316a24935e62108753c2586decf670","public:commit:6cd4ba8184e27503f63c9ebd7effe203dd22b62f","public:commit:88410ce7f26f0cb8377b0b405ec967dfbb4eb274","public:commit:ab61e552e1b83875d61ef7551da890e63614abe4","public:commit:b74fabe9b5a47cd7f3620011f81bdc948e172786","public:commit:dce1ac93d65f7bb58b762ef62e95c47251fbd6c6","public:commit:dec47164524188adffc67299002e189848b31517","public:commit:e4c3db33450291c135ca395763b1a63f35246a66","public:thread:EndstoneMC/endstone:215"],"source_type":"public","date":"2025-07-09..2025-11-14","topics":["ffi","testing","build","documentation","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Integration, attribution and bounded coverage {#integration-attribution-and-bounded-coverage}

## Exact scope and graph {#exact-scope-and-graph}

This history runs from 6 to 16 November 2025 and ends with main and stable v0.10 on separate branches. Six merges connect the branches; neither endpoint contains every change from this period.

The sprint-speed repair1203 changes the attribute default rather than only current movement speed so later sprint recalculation preserves the requested walk value.1205 fixes explicit template deduction/initialization on the Linux route. These are explicit fix intentions; no compiler or server result was reproduced.1248 and1288 update BDS1.21.122/1.21.123 tables. Whole-table TOML parsing verifies every key/scalar delta, while code changes and added/removed symbols are read semantically. Offset correctness is outside static validation.

<a id="reuse-and-credit"></a>
## Reuse and credit {#reuse-and-credit}

Main/stable merges import earlier changes and resolve mixed files. Public source history preserves original authors and branch content. PR215 and PR263 provide additional implementation context; binary font replacements are data assets rather than text source.

Later November 24 checkout and cibuildwheel updates are outside this endpoint. No upstream source, build, tests, generated stubs, extensions or native binaries were executed.

## Review boundaries {#review-boundaries}

Generated stubs are treated as changed contracts, not as a substitute for implementation. Symbol-table changes are structural source evidence; they do not establish successful compilation or runtime compatibility.

No upstream source, generator, test, extension or binary was executed. Native ABI, table values, callback threading, Python exception/hash behavior and runtime performance remain unvalidated. Intermediate reversals describe source history, not enduring personal preferences.

## Per-commit decisions and revisions {#per-commit-decisions-and-revisions}

<a id="commit-1201"></a>
### Commit 1201 {#commit-1201}

[b74fabe9b5a4](https://github.com/EndstoneMC/endstone/commit/b74fabe9b5a47cd7f3620011f81bdc948e172786) · 2025-11-06T03:05:56Z · Merge remote-tracking branch 'origin/v0.10'

Both merge-parent deltas read; release chat-before-script and movement attributes join main's map/metrics/console and newer native ABI. Mixed AttributeInstance and player resolutions retain contextual setters. Exact imported blobs and PR patches reused separately; no new independent authorship inferred.

<a id="commit-1203"></a>
### Commit 1203 {#commit-1203}

[6c1c4d57bf31](https://github.com/EndstoneMC/endstone/commit/6c1c4d57bf316a24935e62108753c2586decf670) · 2025-11-06T19:42:33Z · fix: ensure `setWalkSpeed` is not overridden by sprint toggle events

Explicit sprint-overrides-walk-speed fix: native getters/default setters propagate AttributeModificationContext and dirty notification; player writes movement default current operand after ability update. setDefaultValue accepts operand<=2 without lower check; default-only updates base. No tests added.

<a id="commit-1204"></a>
### Commit 1204 {#commit-1204}

[ab61e552e1b8](https://github.com/EndstoneMC/endstone/commit/ab61e552e1b83875d61ef7551da890e63614abe4) · 2025-11-06T19:46:53Z · docs: update CHANGELOG.md

Release changelog date and reported walk-speed/chat-order/database-log fixes updated; compare link remainsv0.10.10. Reported outcomes only.

<a id="commit-1205"></a>
### Commit 1205 {#commit-1205}

[380ea9597166](https://github.com/EndstoneMC/endstone/commit/380ea95971663e479bcad9cce721ae0574c7d2ef) · 2025-11-06T20:02:33Z · fix: add deduction guide to fix compilation error on Linux

Linux compile-fix title: explicit GameplayHandlerResult deduction guide and brace-initialized cancellation constants. No compiler run.

<a id="commit-1206"></a>
### Commit 1206 {#commit-1206}

[1ee9f8e03a02](https://github.com/EndstoneMC/endstone/commit/1ee9f8e03a0230efce17ebd1290b652a1cfd67d3) · 2025-11-06T20:04:15Z · Merge remote-tracking branch 'origin/v0.10' into v0.10

Both-parent release merge messages read; exact imported file identities account for source, no novel residual behavior.

<a id="commit-1208"></a>
### Commit 1208 {#commit-1208}

[88410ce7f26f](https://github.com/EndstoneMC/endstone/commit/88410ce7f26f0cb8377b0b405ec967dfbb4eb274) · 2025-11-06T23:03:33Z · fix(stubgen): ensure output directories exist

Stub output now creates parent directories recursively before writing; local source read, generator not executed.

<a id="commit-1214"></a>
### Commit 1214 {#commit-1214}

[dec471645241](https://github.com/EndstoneMC/endstone/commit/dec47164524188adffc67299002e189848b31517) · 2025-11-07T12:26:30Z · Merge branch 'v0.10'

Both merge-parent residuals read; imports sprint default-value setter while retaining main modifier declarations/new Vector and form code. Binary font move and empty package files verified separately.

<a id="commit-1239"></a>
### Commit 1239 {#commit-1239}

[e4c3db334502](https://github.com/EndstoneMC/endstone/commit/e4c3db33450291c135ca395763b1a63f35246a66) · 2025-11-09T17:16:59Z · Merge remote-tracking branch 'origin/v0.10'

Both-parent merge residuals read. Imports weak/runtime-ID dimension chain while retaining main spawn/map/registry/metrics/console behavior. Mixed spawnActor still calls dimension_.getBlockSourceFromMainChunkSource after dimension_ becameWeakRef, a source integration inconsistency to track. All exact imports retained byidentity, binary font accounted separately.

<a id="commit-1244"></a>
### Commit 1244 {#commit-1244}

[6cd4ba8184e2](https://github.com/EndstoneMC/endstone/commit/6cd4ba8184e27503f63c9ebd7effe203dd22b62f) · 2025-11-10T14:46:24Z · refactor: consolidate `detail` headers

Consolidates detail/common/cast/endstone headers into detail.h, changes Endstone::getServer to detail::getServer free function. Preserves platform dlsym/GetProcAddress and static cached pointer, pointer-cast mechanics and version macros; updates includes/callers. No new lifecycle invalidation.

<a id="commit-1245"></a>
### Commit 1245 {#commit-1245}

[dce1ac93d65f](https://github.com/EndstoneMC/endstone/commit/dce1ac93d65f7bb58b762ef62e95c47251fbd6c6) · 2025-11-10T22:27:33Z · Merge remote-tracking branch 'origin/main'

Both-parent conflict merge read. Public abstract MapMeta wins, including now-stale detail/endstone.h include;1246 removes it. Exact other branch imports verified.

<a id="commit-1248"></a>
### Commit 1248 {#commit-1248}

[0bc6a065b33f](https://github.com/EndstoneMC/endstone/commit/0bc6a065b33fa388106be3d6c1e34830308ee2ee) · 2025-11-10T23:27:09Z · chore: update BDS to 1.21.122.2

BDS1.21.122 metadata/version and all native symbol offsets updated on stable branch; complete symbol diff read, no ABI/runtime verification. Exact table structure audit to follow.

<a id="commit-1249"></a>
### Commit 1249 {#commit-1249}

[552177f0659c](https://github.com/EndstoneMC/endstone/commit/552177f0659c444c3c41d751561898db63d23d5a) · 2025-11-10T23:27:22Z · Merge remote-tracking branch 'origin/v0.10'

Both-parent merge applies stable BDSversion to main lazy facade while retaining main architecture and item redesign. Exact symbol/import reuse; binary font move accounted.

<a id="commit-1289"></a>
### Commit 1289 {#commit-1289}

[51ce819a7d8a](https://github.com/EndstoneMC/endstone/commit/51ce819a7d8a0c7aac601fa2b31290fcec76fd95) · 2025-11-14T20:12:27Z · feat(command): add support for `entity_type` parameter type

Adds entity_type command parameter by existing EntityType enum lookup, and documents it. Lookup uses cached enum index and at/value assumptions; no tests added.
