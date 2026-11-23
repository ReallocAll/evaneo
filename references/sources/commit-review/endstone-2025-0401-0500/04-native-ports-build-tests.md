<!-- retrieval: {"source_ids":["public:commit:05ddc5ea259cb7df846d4718f84f6349e38eb2eb","public:commit:1e51cfb373efc88a5bb8116411c12efc561ba379","public:commit:1f10e4de98f14d49a9025d1988cbcd7add69a96b","public:commit:2970ded4c51f51c92d78c26d585270e0f4200277","public:commit:2b9683add889ac1910e6f48b50762d11c2102f73","public:commit:2ea4aaf62565afa7241d72df79680bc3e20109d9","public:commit:2fdd85f733a1bfe0215ab41dfc329598f05a1fb3","public:commit:33e8513e8bfaead972a5ab55bb81a8a9eb9725ff","public:commit:5398e56df0815020b304a68e146c39ca7f3533ef","public:commit:5eaf3345187dac50612df1edc45aae5540181968","public:commit:61d4af1a02778dfef4899650a0e615b8288aa2fe","public:commit:6556dfc2a7d6856b82af2a429594e518011310c0","public:commit:7f57254d4605ff1c48ad95b9a11d41b1ee572a59","public:commit:84f56c9d1a5eb2cc41f2679e2251f1f05556380b","public:commit:8e7d9edd5bcb53e48eef4c919a3a5749c81fb40e","public:commit:977146133fcc10cc633f34b6ea0b7cf716d1ce1b","public:commit:cbece3132bad3eb2d3c731687dc660ad66c75bc8","public:commit:d28d4fed9656150d4b9ba24efc55961a0ef481b9","public:commit:db676bf032f2e959a37e0c0d039dd9ae1ffd9bb3","public:commit:ee457cc3fd8d0ceff83b096301e7618ebdb592a5","public:commit:ee90b4f4412fafee7a68187cda80314175c10cf9","public:commit:fbf8f272caa5c5c20ffbcd3c3d5e850a4cfb3162","public:thread:EndstoneMC/endstone:174"],"source_type":"public","date":"2025-03-20..2025-04-16","topics":["lifetime","concurrency","ffi","testing","build","api","documentation","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native ports, release metadata and utility contracts {#native-ports-release-metadata-and-utility-contracts}

<a id="two-branch-tips-not-one-chronological-tree"></a>
## Two branch tips, not one chronological tree {#two-branch-tips-not-one-chronological-tree}

The assignment is sorted by committed_at/SHA, but its endpoint is the union of [445 preview](https://github.com/EndstoneMC/endstone/commit/7f57254d4605ff1c48ad95b9a11d41b1ee572a59) and [500 main](https://github.com/EndstoneMC/endstone/commit/ee457cc3fd8d0ceff83b096301e7618ebdb592a5).436–445 evolve1.21.80-preview.21 packet IDs, ItemGroup size, BiomeRegistry names, flags, virtuals, publisher model and Windows I18n address. They are not ancestors of500. Exact PR174 full-file patch matches are reused only at438,440,443; residual forward declaration is separately read. The boundary map gives all target ancestry membership.

Main490 moves1.21.70-preview.26 to stable1.21.70.04. EntityRegistry explicitly comments out a preview-only viewing flag. Windows Pack::createPack acquires an IPackIOProvider argument and constructs a minimal provider via a known native vtable; Linux keeps its existing signature.491 centralizes the I18n singleton and provider-vtable addresses in symbols.toml. This reduces scattered hardcoded constants without making offsets portable or runtime-verified.

The static review of the public 490 patch recorded 47 Windows and 48 Linux symbol entries, updates to all retained offsets, and one replaced Windows Pack signature. These source-level counts do not validate native offsets. The ABI-sensitive signature, flags, classes, CMake and public version hunks were read in full. No generator or native server was run.

## Packet and byte-stream scaffolding {#packet-and-byte-stream-scaffolding}

447–451 model native pack/Packet objects; AvailableCommandsPacket's local serialization methods explicitly throw 'Not implemented'.493 adds typed dispatcher and packet metadata accessors;494/496 introduce native connection and peer interfaces. Declarations and static size assertions are compatibility hypotheses, not evidence that a native executable matches them.

492 adds cursor/length/reset/raw-write methods. setReadPointer is unchecked; reset clears buffer and cursor but not sticky overflow. The varint writer mask rewrite preserves continuation-bit encoding, rather than proving a new format fix.500 expands BinaryStream's virtual ABI with documentation arguments and synchronous conditional/array callbacks, adapting item descriptors and particle serialization. The endpoint still has writeStream append without view_ refresh; inherited base constructors do not initialize BinaryStream buffer_ for write operations. Existing read varint length/shift bounds remain a separate pre-existing limitation, not newly fixed by this slice.

499's function_ref is intentionally non-owning: it stores an object/function address plus thunk. Immediate callbacks in500 last through the call, but a stored reference to a temporary does not. Six source tests cover functions, functors, lambdas and capture visibility; the TemporaryLambda test uses the reference after the temporary's full-expression and therefore cannot prove safe retention. The ConstFunctor test uses a non-const object.500 registers these tests; the existing seven BinaryStream tests cover read/copy/overflow, not writer ABI/reset/native dispatch. Tests were read, never run.

## Release and test-cost boundaries {#release-and-test-cost-boundaries}

487 bumps API0.7 and Python admission;488 documents inventory/services/resolver/enums, scripting-conflict repair and raw-packet API breaking changes;489 updates the support badge. Historical release claims are attributed to repository text, not independent verification. Removed parser error coverage407 tracks a newly valid grammar. Plugin log removal456 tracks a removed experiment. Ownership refactors update assertions/mocks rather than deleting tests. No runtime confidence is inferred from test quantity, comment style or Codecov's report.

<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}


<a id="commit-417"></a>
### 417. refactor: rename `beta` to `preview` {#commit-417}

[05ddc5ea259cb7df846d4718f84f6349e38eb2eb](https://github.com/EndstoneMC/endstone/commit/05ddc5ea259cb7df846d4718f84f6349e38eb2eb) · 2025-03-20T18:20:29Z · author Vincent.

Parents: `1f5b2f40d4646ec6cf334bef4831776b5a20b2ba`. Read displays: parent 1.

Renames 1.21.70 beta package/symbol/comment labels to preview; offsets unchanged.

All-parent changed-file occurrences: 3. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-436"></a>
### 436. feat: add PlayerLocationPacket {#commit-436}

[2b9683add889ac1910e6f48b50762d11c2102f73](https://github.com/EndstoneMC/endstone/commit/2b9683add889ac1910e6f48b50762d11c2102f73) · 2025-03-21T23:52:48Z · author Vincent.

Parents: `19ab9039c2779d4c06dd3b0470630d87180b4e39`. Read displays: parent 1.

On separate1.21.80 preview branch adds PlayerLocation packet id326 and moves EndId327, not a packet class or main-line change at500.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-437"></a>
### 437. refactor: update `ItemGroup` members {#commit-437}

[977146133fcc10cc633f34b6ea0b7cf716d1ce1b](https://github.com/EndstoneMC/endstone/commit/977146133fcc10cc633f34b6ea0b7cf716d1ce1b) · 2025-03-21T23:55:25Z · author Vincent.

Parents: `2b9683add889ac1910e6f48b50762d11c2102f73`. Read displays: parent 1.

Preview ABI removes ItemGroup count field, reducing asserted size136→128. No public inventory semantic change.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-438"></a>
### 438. refactor: rename members in `BiomeRegistry` {#commit-438}

[1e51cfb373efc88a5bb8116411c12efc561ba379](https://github.com/EndstoneMC/endstone/commit/1e51cfb373efc88a5bb8116411c12efc561ba379) · 2025-03-21T23:56:01Z · author Vincent.

Parents: `977146133fcc10cc633f34b6ea0b7cf716d1ce1b`. Read displays: parent 1.

Preview BiomeRegistry member renames exactly match completed PR174 old/new blobs and hunks; reused verified patch semantics, not repeated reading credit.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 1; exact reviewed-ancestry file reuse: 0.


<a id="commit-439"></a>
### 439. feat: add new `ActorFlags` {#commit-439}

[cbece3132bad3eb2d3c731687dc660ad66c75bc8](https://github.com/EndstoneMC/endstone/commit/cbece3132bad3eb2d3c731687dc660ad66c75bc8) · 2025-03-22T00:06:20Z · author Vincent.

Parents: `1e51cfb373efc88a5bb8116411c12efc561ba379`. Read displays: parent 1.

Preview ActorFlags adds DOES_SERVER_AUTH_ONLY_DISMOUNT123, shifting Count.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-440"></a>
### 440. refactor: remove unnecessary 'static' qualifier {#commit-440}

[5eaf3345187dac50612df1edc45aae5540181968](https://github.com/EndstoneMC/endstone/commit/5eaf3345187dac50612df1edc45aae5540181968) · 2025-03-22T00:06:42Z · author Vincent.

Parents: `cbece3132bad3eb2d3c731687dc660ad66c75bc8`. Read displays: parent 1.

Removes redundant static qualifier in preview shared constants; exact completed PR174 file identity reused.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 1; exact reviewed-ancestry file reuse: 0.


<a id="commit-441"></a>
### 441. feat: add new virtual methods for player location {#commit-441}

[2970ded4c51f51c92d78c26d585270e0f4200277](https://github.com/EndstoneMC/endstone/commit/2970ded4c51f51c92d78c26d585270e0f4200277) · 2025-03-22T00:06:58Z · author Vincent.

Parents: `5eaf3345187dac50612df1edc45aae5540181968`. Read displays: parent 1.

Preview Level interface inserts player location receiver virtual and subChunkTickAndSendRequests. Vtable-position compatibility change; no runtime validation.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-442"></a>
### 442. refactor: switch publisher to single-threaded model in `Container` {#commit-442}

[d28d4fed9656150d4b9ba24efc55961a0ef481b9](https://github.com/EndstoneMC/endstone/commit/d28d4fed9656150d4b9ba24efc55961a0ef481b9) · 2025-03-22T00:07:21Z · author Vincent.

Parents: `2970ded4c51f51c92d78c26d585270e0f4200277`. Read displays: parent 1.

Preview Container publisher switches MultiThreaded to SingleThreaded template type; native layout/concurrency contract follows build being ported, not evidence of thread-safe calls.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-443"></a>
### 443. feat: update virtual methods in `BlockLegacy` {#commit-443}

[61d4af1a02778dfef4899650a0e615b8288aa2fe](https://github.com/EndstoneMC/endstone/commit/61d4af1a02778dfef4899650a0e615b8288aa2fe) · 2025-03-22T00:13:06Z · author Vincent.

Parents: `d28d4fed9656150d4b9ba24efc55961a0ef481b9`. Read displays: parent 1.

Preview BlockLegacy virtual updates reuse exact PR174 patch; residual forward declaration PlayerLocationReceiver read. Must not apply preview vtable layout to main500.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 1; exact reviewed-ancestry file reuse: 0.


<a id="commit-444"></a>
### 444. chore: update Minecraft version to 1.21.80-preview.21 {#commit-444}

[84f56c9d1a5eb2cc41f2679e2251f1f05556380b](https://github.com/EndstoneMC/endstone/commit/84f56c9d1a5eb2cc41f2679e2251f1f05556380b) · 2025-03-22T00:18:43Z · author Vincent.

Parents: `61d4af1a02778dfef4899650a0e615b8288aa2fe`. Read displays: parent 1.

Preview Python package Minecraft version moves1.21.70-preview.26→1.21.80-preview.21.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-445"></a>
### 445. feat: update offsets for `getI18n` {#commit-445}

[7f57254d4605ff1c48ad95b9a11d41b1ee572a59](https://github.com/EndstoneMC/endstone/commit/7f57254d4605ff1c48ad95b9a11d41b1ee572a59) · 2025-03-22T00:19:48Z · author Vincent.

Parents: `84f56c9d1a5eb2cc41f2679e2251f1f05556380b`. Read displays: parent 1.

Preview Windows getI18n absolute offset changes0x60BBF20→0x622E190 for1.21.80-preview.21; Linux unchanged. Build-specific static assumption, not verified offset at runtime.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-447"></a>
### 447. feat: add `ResourcePacksInfoPacket` {#commit-447}

[ee90b4f4412fafee7a68187cda80314175c10cf9](https://github.com/EndstoneMC/endstone/commit/ee90b4f4412fafee7a68187cda80314175c10cf9) · 2025-03-22T19:04:02Z · author Vincent.

Parents: `e0fed8fb22384251676c6477751304719d65a41d`. Read displays: parent 1.

Defines native resource pack information/data layouts with pack identity, resource list, script/addon flags and size assertions80/128. This is protocol object scaffolding.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-448"></a>
### 448. refactor: change LevelSeed64 from struct to class {#commit-448}

[33e8513e8bfaead972a5ab55bb81a8a9eb9725ff](https://github.com/EndstoneMC/endstone/commit/33e8513e8bfaead972a5ab55bb81a8a9eb9725ff) · 2025-03-22T19:31:05Z · author Vincent.

Parents: `ee90b4f4412fafee7a68187cda80314175c10cf9`. Read displays: parent 1.

Changes LevelSeed64 struct signed value to class unsigned64 value initialized0; constructors temporarily private until452. Native representation declaration, not random seed behavior change on its own.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-480"></a>
### 480. refactor: remove unnecessary use of shared_ptr for `BlockData` {#commit-480}

[2fdd85f733a1bfe0215ab41dfc329598f05a1fb3](https://github.com/EndstoneMC/endstone/commit/2fdd85f733a1bfe0215ab41dfc329598f05a1fb3) · 2025-03-25T14:08:44Z · author Vincent.

Parents: `ddd269969a8f08ca400cd9e0bb4aa30d4835eb7e`. Read displays: parent 1.

Converts BlockData results to unique_ptr and setter inputs const references throughout API/core/bindings/mocks. Removes null-input errors because reference contract excludes null, so not a regression by itself. Native cast remains unchecked concrete EndstoneBlockData assumption; block-state static cast replaces former dynamic cast. No tests removed, mocks adapted.

All-parent changed-file occurrences: 13. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-487"></a>
### 487. chore: bump api version to 0.7 {#commit-487}

[fbf8f272caa5c5c20ffbcd3c3d5e850a4cfb3162](https://github.com/EndstoneMC/endstone/commit/fbf8f272caa5c5c20ffbcd3c3d5e850a4cfb3162) · 2025-03-25T17:15:16Z · author Vincent.

Parents: `2a4adfd1c2a332111da319aa1ccff879bb37738c`. Read displays: parent 1.

Bumps API0.6.2→0.7.0, admits0.7 in Python loader while retaining0.5/0.6, and reports package Minecraft version in metrics instead of runtime accessor. Python admission does not demonstrate compatibility for removed properties; C++ signature/ownership changes are ABI-relevant.

All-parent changed-file occurrences: 3. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-488"></a>
### 488. docs: update CHANGELOG.md {#commit-488}

[1f10e4de98f14d49a9025d1988cbcd7add69a96b](https://github.com/EndstoneMC/endstone/commit/1f10e4de98f14d49a9025d1988cbcd7add69a96b) · 2025-03-25T17:24:47Z · author Vincent.

Parents: `fbf8f272caa5c5c20ffbcd3c3d5e850a4cfb3162`. Read displays: parent 1.

Publishes0.7.0 March25 changelog covering1.21.70, services, resolver, anonymous enums, metadata/equipment/selected slot, scripting conflict fix and packet API breaking changes. This is explicit release narrative; test/support claims are historical statements, not independent runtime validation.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-489"></a>
### 489. docs: update README.md {#commit-489}

[db676bf032f2e959a37e0c0d039dd9ae1ffd9bb3](https://github.com/EndstoneMC/endstone/commit/db676bf032f2e959a37e0c0d039dd9ae1ffd9bb3) · 2025-03-25T17:27:03Z · author Vincent.

Parents: `1f10e4de98f14d49a9025d1988cbcd7add69a96b`. Read displays: parent 1.

Updates README Minecraft badge1.21.60→1.21.70, aligning declared support with release narrative.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-490"></a>
### 490. chore: update BDS to 1.21.70.04 {#commit-490}

[5398e56df0815020b304a68e146c39ca7f3533ef](https://github.com/EndstoneMC/endstone/commit/5398e56df0815020b304a68e146c39ca7f3533ef) · 2025-03-26T09:18:09Z · author Vincent.

Parents: `db676bf032f2e959a37e0c0d039dd9ae1ffd9bb3`. Read displays: parent 1.

Ports main from preview.26 to stable1.21.70.04: removes preview-only EntityRegistry is_viewing field; updates Windows I18n offset; Windows Pack::createPack now requires IO provider, synthesized through hardcoded vtable address while Linux keeps old signature. All47 Windows/48 Linux symbol entries structurally compared: all existing offsets change, one Windows Pack signature replacement. Literal bulk verified, native correctness not tested. Preview436–445 stays separate.

All-parent changed-file occurrences: 6. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-491"></a>
### 491. refactor: use symbol-based offsets for cleaner code {#commit-491}

[6556dfc2a7d6856b82af2a429594e518011310c0](https://github.com/EndstoneMC/endstone/commit/6556dfc2a7d6856b82af2a429594e518011310c0) · 2025-03-26T12:43:29Z · author Vincent.

Parents: `5398e56df0815020b304a68e146c39ca7f3533ef`. Read displays: parent 1.

Moves Windows I18n singleton and IO-provider vtable offsets into symbols.toml and BEDROCK_VAR helper (90743760/80388968 exactly prior hex values). Centralizes build-specific assumptions without removing them; Linux unchanged.

All-parent changed-file occurrences: 4. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-492"></a>
### 492. feat: add methods to `BinaryStream` {#commit-492}

[2ea4aaf62565afa7241d72df79680bc3e20109d9](https://github.com/EndstoneMC/endstone/commit/2ea4aaf62565afa7241d72df79680bc3e20109d9) · 2025-03-26T22:08:11Z · author Vincent.

Parents: `6556dfc2a7d6856b82af2a429594e518011310c0`. Read displays: parent 1.

Adds read-pointer/length accessors, reset and raw-byte writer. Reset clears buffer/view/read position but not sticky overflow flag; unchecked setReadPointer can make unread length underflow. Varint writer masks now0x7F with equivalent continuation-bit result, a clarity refactor rather than proven wire-format fix. Existing tests cover reader, not new reset/writer paths.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-499"></a>
### 499. feat: add `brstd::function_ref` {#commit-499}

[8e7d9edd5bcb53e48eef4c919a3a5749c81fb40e](https://github.com/EndstoneMC/endstone/commit/8e7d9edd5bcb53e48eef4c919a3a5749c81fb40e) · 2025-03-27T00:56:31Z · author Vincent.

Parents: `43a8c3b8bf621a904183921bfd0e6ad8eb55837d`. Read displays: parent 1.

Adds non-owning function_ref thunk/storage model supporting functions/objects and six tests, registered500. Lvalue functors/lambdas preserve borrowed state. TemporaryLambda test stores a pointer to an expired temporary after constructor full-expression, so it is not valid lifetime assurance; ConstFunctor test object is not const. No AI credit inferred from test style; no tests run.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-500"></a>
### 500. feat: add more methods to `BinaryStream` {#commit-500}

[ee457cc3fd8d0ceff83b096301e7618ebdb592a5](https://github.com/EndstoneMC/endstone/commit/ee457cc3fd8d0ceff83b096301e7618ebdb592a5) · 2025-03-27T01:05:15Z · author Vincent.

Parents: `8e7d9edd5bcb53e48eef4c919a3a5749c81fb40e`. Read displays: parent 1.

Expands BinaryStream's native virtual writer ABI with doc-name/note parameters, integers/floats/conditional/array callbacks; updates descriptor/particle calls and registers function_ref tests. Callbacks run synchronously, so immediate lambda arguments last through call; stored function_ref remains non-owning. Existing seven binary tests only read streams. writeStream still appends without refreshing view and inherited BinaryStream base constructors leave buffer_ unspecified for writing; reset overflow semantics unchanged. Fixed/normalized float domain/overflow and native ABI not validated. This is bounded staged endpoint, not a release-success claim.

All-parent changed-file occurrences: 5. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.
