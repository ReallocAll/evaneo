<!-- retrieval: {"source_ids":["public:commit:05d37e9edb823973066701e6f0f66ecc73c76792","public:commit:08982083e9c84e4c761831528c1a53080042e5fa","public:commit:1039a488a00642f782a851a6266357639885382a","public:commit:11cd5c134d67898de6e886a4d60b68601af9359b","public:commit:1c0dd877f31a7de953d73fc7206bc27f3be1dce2","public:commit:1d3a68d538446fc74b5b2c7739f792cbe2034d9b","public:commit:20c373be038455440302084fb710aa50b2d1b200","public:commit:277c6aba59b33659eb8cf5b0739ee6530dc5789c","public:commit:2895b92cac66938dec174fa20342e5aba93466d9","public:commit:37640d1dd3c6c3b9716da4a0fa10e2d7503846d7","public:commit:3e8621fcf2a751dab87d94db64e98c5a95d6cf65","public:commit:4157d93e3da4c5786b14640517da9cb092b0312f","public:commit:440956bae085b652af6bcee556527fde1bd2a992","public:commit:459ca70abac9dcb5aa439b5e6242748fc3d61159","public:commit:4a6b23224e78b27f935e0f21f7033340a4d8b0ea","public:commit:50daff9c6d791df6b3906f87da5ee9007d7fe718","public:commit:50e10410cb7ba6e1712958d310c03e6c279c8e38","public:commit:52fb61478cafbc5a159e27d2f74ab21a5a858669","public:commit:643824997e37dce69fd39aad28100e04e8c5029a","public:commit:6479cd1491095b488fb46ec6ab95d687a8e71ff1","public:commit:6719a3a114a9a66e8c2b5adbedc0da7eab28b468","public:commit:67be266e8985c3654dfcf764e803b5bf079ca93c","public:commit:6c809076962b5455dfa3604265a05a3ad0d7127a","public:commit:7372d30778b646f56541d74d98fee91a8301d088","public:commit:7bb52cfd131fe1749a5e0a90ea001cab26b5a58f","public:commit:7f43551555c94947fd9e395b10f6e223fdd04263","public:commit:83bf1e962623343edad41cf393d94bfc745842fd","public:commit:8ae466281a2115611a57625096ca12c78087a3e7","public:commit:91395d27068ed9f8fb1d52512745628178de4d37","public:commit:92cac9f787bb1f917fd51fe59034d7095af33b49","public:commit:942a7af7f88217adff53642375741b37a6aae765","public:commit:9b39e28c8e838d7bcb034aba3dea60f3a0e8a5e4","public:commit:a75067827ba6b3cebc213aad01093a54c0b0bd83","public:commit:b435062a9497bcb8d45f07a797c8a8e1c9c59c36","public:commit:be2392270d68e714a0ae16933b840471b1cddde8","public:commit:c6bf29b27fdceba21877eb0bb43746976b5f1fbc","public:commit:cbc43dc3f8428ae9dd4613acc5afbbacc62035e0","public:commit:cbfd1f47a65388e9f1a69495130dc4f81824738a","public:commit:d87764fac02f37ecbc3ce65a16259a81e60b0ebf","public:commit:da9f899ae8813a92844a4a36b87f77fa417dacb0","public:commit:e8a1dd641193dafbc82866c33317112dbac84d80","public:commit:e8c6837d4c9b7863e4651549fbbfb60f66ea8ddf","public:commit:f00f5d58a453fbb9f32b7e9ad885159b208f2029","public:commit:fcd866fcfc7cd558a289a45a4d48595f23cb5afb","public:thread:EndstoneMC/endstone:168","public:thread:EndstoneMC/endstone:169","public:thread:EndstoneMC/endstone:173","public:thread:EndstoneMC/endstone:174"],"source_type":"public","date":"2025-03-28..2025-05-06","topics":["lifetime","concurrency","ffi","testing","build","performance","api","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Staged native ABI support and distribution {#staged-native-abi-support-and-distribution}

<a id="branches-and-mechanical-evidence"></a>
## Branches and mechanical evidence {#branches-and-mechanical-evidence}

The assignment is the exact 2025-only committed_at/SHA slice, not a linear first-parent log. Main moves through1.21.71/72/73 while the preview branch models1.21.80. Merge527 imports earlier work436–500 plus current changes, retaining preview packet IDs;546 briefly selects1.21.72 from neither parent version before547 advances preview.28. Merge575 lands PR174, and577 switches to the release ABI. Every merge has both-parent hashes, imported ancestry and per-path second-parent blob comparison; mixed files are read against both parents. Repeated imported changes receive identity-based reuse, not extra independent idea credit.

Five large numeric-table commits are audited by parsing all TOML keys/types/scalars and comparing every value:515,520,547,559,577. The386 numeric changes are counted separately from meaningful signature removals/renames, version/timestamp values and non-table changes. Symbol tables are historical reverse-engineering declarations; this analysis does not certify offsets or compatibility with any executable. Smaller symbol additions/removals are read in their full diffs.

## Ownership and native layout {#ownership-and-native-layout}

Repository/context/provider changes530–551 propagate across constructor signatures, fields, dependent sizes and call sites. Pack548 removes the fabricated Windows provider-vtable route and requires a real provider;550 clones it from the engine factory and transfers ownership into the custom pack source. Temporary invalid template declarations and stale size assertions are repaired551. Pubsub modeling separates Aggregate/Discard policy and single/multi/strict-threaded bases. This describes native shape; it is not an independently verified concurrency implementation.

Native source evolves through provisional fields: Container's unknown pointer557 is removed558; a provisional Mob component pointer is removed561; NetworkIdentifier's anonymous bytes become a24-byte transport-ID variant; EntityRegistry's preview-only viewing flag is disabled for release577. These reversals are important counterexamples to treating header offsets/comments as stable facts. Gamerule insertion534 shifts existing IDs; virtual-slot additions/removals539/552 and return-by-value ItemDescriptor556 alter ABI obligations even where titles say cleanup.

<a id="build-cache-and-test-costs"></a>
## Build, cache and test costs {#build-cache-and-test-costs}

Runner522 moves Linux20.04 to22.04. Docker523 changes cache transport,526 adds save-capable cache action,525 limits DockerHub publication to tags, and524 narrows Conan fallback keys. All workflows were read, not executed. Dependabot's non-target PR169 changes cibuildwheel2.23.0→2.23.2 in wheel and Windows-portable workflows; PR176 subsequently changes2.23.2→2.23.3 in the same two workflows. Bot authorship and upstream release-note claims are retained separately.

PR174's existing captured Codecov message simultaneously claims all modified coverable lines covered and0.00% project coverage, with report44 commits behind main. Neither is a meaningful runtime validation of these native layouts. No CI, benchmark, package install, symbol generator or upstream tests ran here. Test refactors573–574 are covered in the enchantment dossier as lower-cost shared scaffolding rather than automatically negative test removal.

## Attribution and limits {#attribution-and-limits}

Vincent owns target commits/integration; native Bedrock behavior and declarations do not imply authorship of the proprietary engine. daoge's form patches and dependabot's workflow bump remain credited through merges. PR174 body is empty, so no detailed undocumented rationale is invented. Release notes509/516/576 are claims of intended/user-facing outcomes; repeated v0.7.0 links are recorded as documentation defects, not used as release identity proof.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-515"></a>
### Commit 515 {#commit-515}

08982083e9c84e4c761831528c1a53080042e5fa · 2025-03-28T17:11:53Z

[chore: update BDS to 1.21.71.01](https://github.com/EndstoneMC/endstone/commit/08982083e9c84e4c761831528c1a53080042e5fa)

**Observed change.** Bumps supported native version 1.21.70 to 1.21.71 and updates timestamp/address tables: 48 Windows and 49 Linux numeric values. Adds invoke helper and routes BEDROCK_CALL through it; supplied function name is unused.

**Causal interpretation.** Separates mechanical address refresh from the meaningful invocation wrapper. All keys/types/scalars and numeric changes are structurally enumerated.

**Limits.** Address correctness against binaries not verified. Wrapper forwards arguments but not its func parameter; no compilation.

<a id="commit-516"></a>
### Commit 516 {#commit-516}

440956bae085b652af6bcee556527fde1bd2a992 · 2025-03-29T15:15:57Z

[docs: update CHANGELOG.md](https://github.com/EndstoneMC/endstone/commit/440956bae085b652af6bcee556527fde1bd2a992)

**Observed change.** Adds 0.7.2 notes for native 1.21.71, item damage, runtime block IDs and packet statistics.

**Causal interpretation.** Records the staged API/native release narrative; title/release prose does not substitute for feature tests.

**Limits.** Patch macro does not become 2 in this change; release link still points to v0.7.0.

<a id="commit-520"></a>
### Commit 520 {#commit-520}

7372d30778b646f56541d74d98fee91a8301d088 · 2025-04-08T16:42:33Z

[chore: update BDS to 1.21.72.02](https://github.com/EndstoneMC/endstone/commit/7372d30778b646f56541d74d98fee91a8301d088)

**Observed change.** Bumps native version 1.21.71 to 1.21.72, updates 49 Windows and 49 Linux numeric values, and corrects AppPlatformIOProvide to AppPlatformIOProvider in symbol and lookup.

**Causal interpretation.** Typographical symbol-key agreement is a substantive exception within a largely numeric address update.

**Limits.** Native addresses and compatibility not executed/verified.

<a id="commit-521"></a>
### Commit 521 {#commit-521}

37640d1dd3c6c3b9716da4a0fa10e2d7503846d7 · 2025-04-08T16:55:58Z

[refactor: remove redundant signature](https://github.com/EndstoneMC/endstone/commit/37640d1dd3c6c3b9716da4a0fa10e2d7503846d7)

**Observed change.** Deletes the CommandRegistry::createCommand wrapper and its Windows/Linux symbol-table entries.

**Causal interpretation.** Removes one custom native call surface rather than preserving an unused compatibility layer.

**Limits.** No call-site/runtime regression test; removal itself is the observed evidence, not a general anti-abstraction preference.

<a id="commit-522"></a>
### Commit 522 {#commit-522}

91395d27068ed9f8fb1d52512745628178de4d37 · 2025-04-08T16:57:12Z

[ci: update Ubuntu runner to 22.04](https://github.com/EndstoneMC/endstone/commit/91395d27068ed9f8fb1d52512745628178de4d37)

**Observed change.** Moves Linux Release/Debug-with-coverage CI runners from Ubuntu 20.04 to 22.04; Windows remains unchanged.

**Causal interpretation.** Updates hosted-build baseline for both build variants in tandem.

**Limits.** Workflow read, not run; package/ABI consequences not measured.

<a id="commit-523"></a>
### Commit 523 {#commit-523}

67be266e8985c3654dfcf764e803b5bf079ca93c · 2025-04-08T17:04:17Z

[ci(docker): use local cache in favour of gha cache exporter](https://github.com/EndstoneMC/endstone/commit/67be266e8985c3654dfcf764e803b5bf079ca93c)

**Observed change.** Replaces Docker build GHA cache exporter with local /tmp cache restore plus new-cache rotation.

**Causal interpretation.** Changes cache transport while preserving the build/publish purpose; next 526 adds an actual save-capable action.

**Limits.** This intermediate version restores but does not independently save through the restore action. No cache-hit observation.

<a id="commit-524"></a>
### Commit 524 {#commit-524}

8ae466281a2115611a57625096ca12c78087a3e7 · 2025-04-08T17:13:35Z

[ci: remove redundant restore-keys from GitHub workflows](https://github.com/EndstoneMC/endstone/commit/8ae466281a2115611a57625096ca12c78087a3e7)

**Observed change.** Removes broad Conan restore prefixes, retaining build-type-specific matching.

**Causal interpretation.** Narrower fallback avoids reusing less-specific cache entries; compatibility rationale is inferred from keys, not stated author evidence.

**Limits.** No dependency resolution/build outcome.

<a id="commit-525"></a>
### Commit 525 {#commit-525}

e8a1dd641193dafbc82866c33317112dbac84d80 · 2025-04-08T19:58:16Z

[ci: refactor docker workflow](https://github.com/EndstoneMC/endstone/commit/e8a1dd641193dafbc82866c33317112dbac84d80)

**Observed change.** Splits Docker publishing into GHCR work and a DockerHub job gated on tags; each gets local build cache setup.

**Causal interpretation.** Avoids DockerHub work on ordinary non-tag builds while retaining release publication.

**Limits.** No credentials or secret values accessed; workflow expressions and secret references only. No publish performed.

<a id="commit-526"></a>
### Commit 526 {#commit-526}

92cac9f787bb1f917fd51fe59034d7095af33b49 · 2025-04-08T20:50:02Z

[ci: use `actions/cache` to cache docker layers](https://github.com/EndstoneMC/endstone/commit/92cac9f787bb1f917fd51fe59034d7095af33b49)

**Observed change.** Changes actions/cache/restore to actions/cache so the Docker local cache can be saved as well as restored.

**Causal interpretation.** Closes the missing persistence step introduced in 523.

**Limits.** Fixed cache-key semantics were not exercised; no claim of observed hit-rate improvement.

<a id="commit-527"></a>
### Commit 527 {#commit-527}

83bf1e962623343edad41cf393d94bfc745842fd · 2025-04-08T20:51:50Z

[Merge branch 'main' into feat/1.20.80-support](https://github.com/EndstoneMC/endstone/commit/83bf1e962623343edad41cf393d94bfc745842fd)

**Observed change.** Integrates main into the preview branch. Of 150 changed file entries, 148 match imported-parent blobs/deletions; two mixed files preserve preview packet ID PlayerLocation 326 while integrating Packet methods/dispatcher, and select version 1.21.80-preview.27.

**Causal interpretation.** Reuses exactly identified own commits, 55 earlier-target commits reviewed by sibling, and non-target PR168/169 context. The title says 1.20.80 although source is 1.21.80 preview.

**Limits.** Not chronological linear progression. Both-parent residuals and provenance audited; no new binary-layout validation.

<a id="commit-528"></a>
### Commit 528 {#commit-528}

20c373be038455440302084fb710aa50b2d1b200 · 2025-04-08T21:32:26Z

[feat: update enums](https://github.com/EndstoneMC/endstone/commit/20c373be038455440302084fb710aa50b2d1b200)

**Observed change.** Adds AsyncJoinTaskDenied disconnect reason 118 and deprecates existing packet IDs PassengerJump 20, PlayerInput 57, CompressedBiomeDefinitionList 301 without renumbering them.

**Causal interpretation.** Preserves wire identities while marking protocol evolution in preview definitions.

**Limits.** Declaration accuracy not independently compared with native traffic.

<a id="commit-529"></a>
### Commit 529 {#commit-529}

277c6aba59b33659eb8cf5b0739ee6530dc5789c · 2025-04-08T21:32:47Z

[feat: update `PackReport` class members](https://github.com/EndstoneMC/endstone/commit/277c6aba59b33659eb8cf5b0739ee6530dc5789c)

**Observed change.** Moves PackReport boolean fields from near location to the end, removing stale offsets/comments.

**Causal interpretation.** An ABI layout change concealed by terse cleanup-like content; must be read as field order, not cosmetic formatting.

**Limits.** No sizeof/native binary validation beyond source declarations.

<a id="commit-530"></a>
### Commit 530 {#commit-530}

f00f5d58a453fbb9f32b7e9ad885159b208f2029 · 2025-04-08T21:37:26Z

[feat: update `CommandParameterData` class members](https://github.com/EndstoneMC/endstone/commit/f00f5d58a453fbb9f32b7e9ad885159b208f2029)

**Observed change.** Reworks ResourcePackRepository ownership/reference fields, command context and constructor dependencies. CommandParameterData gains two custom storage function pointers and matching constructor parameters; registry aliases are updated.

**Causal interpretation.** Tracks preview native ABI changes across repository construction and command parameter representation.

**Limits.** Repository size assertions remain stale in this intermediate commit until 551; no compile/run.

<a id="commit-531"></a>
### Commit 531 {#commit-531}

7bb52cfd131fe1749a5e0a90ea001cab26b5a58f · 2025-04-08T21:40:46Z

[feat: update `MinecraftCommands` class members](https://github.com/EndstoneMC/endstone/commit/7bb52cfd131fe1749a5e0a90ea001cab26b5a58f)

**Observed change.** Introduces ICommandsContextProvider virtual methods for level/network ID/command completion and places its reference before command registry/output fields.

**Causal interpretation.** Separates command execution context from the MinecraftCommands storage, matching revised native object shape.

**Limits.** Vtable and field ordering are modeled, not verified against binary execution.

<a id="commit-532"></a>
### Commit 532 {#commit-532}

6c809076962b5455dfa3604265a05a3ad0d7127a · 2025-04-08T21:48:16Z

[feat: add `Bedrock::PubSub::ReturnPolicyType`](https://github.com/EndstoneMC/endstone/commit/6c809076962b5455dfa3604265a05a3ad0d7127a)

**Observed change.** Adds Aggregate/Discard return-policy types and parameterizes subscription/dispatch publisher types with an Aggregate default.

**Causal interpretation.** Extends the native pubsub type model for revised callback return handling.

**Limits.** Mostly declarations/type structure; no dispatch/concurrency behavior implemented or tested here.

<a id="commit-533"></a>
### Commit 533 {#commit-533}

1039a488a00642f782a851a6266357639885382a · 2025-04-08T21:57:53Z

[refactor: remove `ClientJoinedEvent`](https://github.com/EndstoneMC/endstone/commit/1039a488a00642f782a851a6266357639885382a)

**Observed change.** Removes ClientJoinedEvent from native player void-event variant.

**Causal interpretation.** Tracks event variant membership rather than independently changing plugin join dispatch.

**Limits.** The later 542 lifecycle change must be read separately; variant correctness untested.

<a id="commit-534"></a>
### Commit 534 {#commit-534}

52fb61478cafbc5a159e27d2f74ab21a5a858669 · 2025-04-08T21:58:05Z

[feat: update game rules index](https://github.com/EndstoneMC/endstone/commit/52fb61478cafbc5a159e27d2f74ab21a5a858669)

**Observed change.** Inserts LOCATOR_BAR gamerule at 17, shifts subsequent native IDs and count to 43.

**Causal interpretation.** Numeric enum insertion affects later policy lookups (including command feedback/death messages), so it cannot be treated as an isolated feature flag.

**Limits.** No native gamerule behavior validation.

<a id="commit-535"></a>
### Commit 535 {#commit-535}

2895b92cac66938dec174fa20342e5aba93466d9 · 2025-04-08T21:58:13Z

[feat: update actor method parameters](https://github.com/EndstoneMC/endstone/commit/2895b92cac66938dec174fa20342e5aba93466d9)

**Observed change.** Drops the NetworkSettings argument from Actor::sendMotionPacketIfNeeded virtual declaration.

**Causal interpretation.** Maintains preview virtual signature shape.

**Limits.** No native-call ABI test.

<a id="commit-536"></a>
### Commit 536 {#commit-536}

1c0dd877f31a7de953d73fc7206bc27f3be1dce2 · 2025-04-08T22:11:13Z

[feat: update actor data ids](https://github.com/EndstoneMC/endstone/commit/1c0dd877f31a7de953d73fc7206bc27f3be1dce2)

**Observed change.** Adds actor data IDs 134/135 for camera-related values and advances count to 136.

**Causal interpretation.** Appends wire-data declarations without renumbering earlier values.

**Limits.** No serialization/client validation.

<a id="commit-537"></a>
### Commit 537 {#commit-537}

cbc43dc3f8428ae9dd4613acc5afbbacc62035e0 · 2025-04-08T22:11:18Z

[feat: update actor flags](https://github.com/EndstoneMC/endstone/commit/cbc43dc3f8428ae9dd4613acc5afbbacc62035e0)

**Observed change.** Makes ActorType count explicitly 124 without otherwise changing values.

**Causal interpretation.** Clarifies stable numeric boundary before subsequent additions.

**Limits.** Mechanical declaration, no independent design preference.

<a id="commit-538"></a>
### Commit 538 {#commit-538}

1d3a68d538446fc74b5b2c7739f792cbe2034d9b · 2025-04-08T22:11:29Z

[feat: add happy ghast actor type](https://github.com/EndstoneMC/endstone/commit/1d3a68d538446fc74b5b2c7739f792cbe2034d9b)

**Observed change.** Adds HappyGhast entity type 147 combined with Animal category bits.

**Causal interpretation.** Models a new native entity classification in the preview branch.

**Limits.** No spawning or entity behavior test.

<a id="commit-539"></a>
### Commit 539 {#commit-539}

4157d93e3da4c5786b14640517da9cb092b0312f · 2025-04-08T22:11:44Z

[feat: update the virtual methods of `Container`](https://github.com/EndstoneMC/endstone/commit/4157d93e3da4c5786b14640517da9cb092b0312f)

**Observed change.** Adds Container first-empty-slot, first-item and reverse-find-first-slot virtual members.

**Causal interpretation.** Tracks new native vtable slots; downstream concrete-container declaration adjustments follow in 558.

**Limits.** No call verification or offset proof.

<a id="commit-540"></a>
### Commit 540 {#commit-540}

d87764fac02f37ecbc3ce65a16259a81e60b0ebf · 2025-04-08T22:11:58Z

[feat: update `Minecraft` class members](https://github.com/EndstoneMC/endstone/commit/d87764fac02f37ecbc3ce65a16259a81e60b0ebf)

**Observed change.** Adds DefaultCommandsContextProvider member before MinecraftCommands in Minecraft.

**Causal interpretation.** Completes storage-side context-provider modeling begun in 531.

**Limits.** Native object layout unverified.

<a id="commit-541"></a>
### Commit 541 {#commit-541}

a75067827ba6b3cebc213aad01093a54c0b0bd83 · 2025-04-12T08:54:56Z

[chore: update BDS to 1.21.73.01](https://github.com/EndstoneMC/endstone/commit/a75067827ba6b3cebc213aad01093a54c0b0bd83)

**Observed change.** Changes advertised supported main-line Minecraft version to 1.21.73 without a symbol-table patch.

**Causal interpretation.** Main release metadata evolves independently of the preview branch.

**Limits.** Does not establish that prior addresses are compatible with new native binary.

<a id="commit-546"></a>
### Commit 546 {#commit-546}

b435062a9497bcb8d45f07a797c8a8e1c9c59c36 · 2025-04-16T09:18:23Z

[Merge remote-tracking branch 'refs/remotes/origin/main' into feat/1.21.80-support](https://github.com/EndstoneMC/endstone/commit/b435062a9497bcb8d45f07a797c8a8e1c9c59c36)

**Observed change.** Merges main fixes 541–545 into preview; nine of ten changed entries match imported parent. The mixed version file selects 1.21.72, below both preview.27 and main 1.21.73, before547 sets preview.28.

**Causal interpretation.** Both-parent inspection exposes a transient version regression that a merge title would hide.

**Limits.** No compatibility inference from the temporary version string.

<a id="commit-547"></a>
### Commit 547 {#commit-547}

11cd5c134d67898de6e886a4d60b68601af9359b · 2025-04-16T09:22:50Z

[feat: update BDS version to 1.21.80.28 (Windows)](https://github.com/EndstoneMC/endstone/commit/11cd5c134d67898de6e886a4d60b68601af9359b)

**Observed change.** Sets preview.28 metadata/timestamp and changes 48 Windows addresses, deleting obsolete AppPlatformIOProvider vtable key; Linux table unchanged.

**Causal interpretation.** Windows update is a staged platform change; Linux catches up559.

**Limits.** Numeric tables structurally audited, not address-resolved or run.

<a id="commit-548"></a>
### Commit 548 {#commit-548}

9b39e28c8e838d7bcb034aba3dea60f3a0e8a5e4 · 2025-04-16T09:29:32Z

[refactor: remove overloads of `Pack::createPack`](https://github.com/EndstoneMC/endstone/commit/9b39e28c8e838d7bcb034aba3dea60f3a0e8a5e4)

**Observed change.** Requires explicit IPackIOProvider in Pack::createPack on both platforms, removing Windows fake-vtable provider path. Adds getOnDiskScratchPath virtual.

**Causal interpretation.** Moves native pack creation toward the engine's real provider ownership rather than constructing an incomplete provider surrogate.

**Limits.** Call-site ownership is completed550; no pack loading test.

<a id="commit-549"></a>
### Commit 549 {#commit-549}

cbfd1f47a65388e9f1a69495130dc4f81824738a · 2025-04-16T09:44:59Z

[feat: update `FastDispatchPublisherBase`](https://github.com/EndstoneMC/endstone/commit/cbfd1f47a65388e9f1a69495130dc4f81824738a)

**Observed change.** Splits pubsub dispatch base into single-threaded, mutex+atomic multi-threaded, and mutex-only strict-threaded variants; adds lock wrappers and selectors.

**Causal interpretation.** Represents different synchronization strategies explicitly in native type models.

**Limits.** Declarations do not prove lock behavior or race freedom; no execution.

<a id="commit-550"></a>
### Commit 550 {#commit-550}

942a7af7f88217adff53642375741b37a6aae765 · 2025-04-16T10:02:24Z

[feat: init pack io within the constructor of `EndstonePackSource`](https://github.com/EndstoneMC/endstone/commit/942a7af7f88217adff53642375741b37a6aae765)

**Observed change.** Models PackSourceFactory members/provider cloning and threads owned provider through EndstonePackSource and Pack creation; server obtains provider from repository factory. Adds default command context declaration.

**Causal interpretation.** Completes548's provider dependency through construction and ownership. Initial SourcesList<PackSourceT> declaration is repaired551.

**Limits.** No provider lifetime/pack loading test; intermediate compile correctness not assumed.

<a id="commit-551"></a>
### Commit 551 {#commit-551}

50daff9c6d791df6b3906f87da5ee9007d7fe718 · 2025-04-16T13:11:08Z

[feat: add `PackCommand::IPackCommandPipeline`](https://github.com/EndstoneMC/endstone/commit/50daff9c6d791df6b3906f87da5ee9007d7fe718)

**Observed change.** Adds IPackCommandPipeline non-owner-reference support, fixes SourcesList primary template, updates ResourcePackRepository size assertions to600/528 and required MapItemSavedData include.

**Causal interpretation.** Repairs incomplete type/size integration from530/550, preserving the staged nature of ABI work.

**Limits.** Assertions are source evidence only; no build.

<a id="commit-552"></a>
### Commit 552 {#commit-552}

3e8621fcf2a751dab87d94db64e98c5a95d6cf65 · 2025-04-17T02:21:25Z

[fix: correct the virtual table of `IResourcePackRepository`](https://github.com/EndstoneMC/endstone/commit/3e8621fcf2a751dab87d94db64e98c5a95d6cf65)

**Observed change.** Removes requestReloadDynamicPackagePacks virtual member from repository interface.

**Causal interpretation.** Tracks preview virtual-table removal.

**Limits.** No native-call compatibility verification.

<a id="commit-553"></a>
### Commit 553 {#commit-553}

da9f899ae8813a92844a4a36b87f77fa417dacb0 · 2025-04-17T08:08:37Z

[feat: update the base class of `EventCoordinator`s](https://github.com/EndstoneMC/endstone/commit/da9f899ae8813a92844a4a36b87f77fa417dacb0)

**Observed change.** EventCoordinatorPimpl replaces EnableNonOwnerReferences inheritance with its own virtual destructor and protected subscriber storage; adjusts Scoreboard/ServerScoreboard sizes downward16 and asserts reference-support base24.

**Causal interpretation.** Coordinates base-layout removal with dependent native object sizes, rather than a standalone local class cleanup.

**Limits.** No binary sizeof/layout verification; removal is not proof of general ownership-policy change.

<a id="commit-554"></a>
### Commit 554 {#commit-554}

4a6b23224e78b27f935e0f21f7033340a4d8b0ea · 2025-04-17T08:45:35Z

[feat: update members of `NetworkIdentifier` and `ServerNetworkHandler`](https://github.com/EndstoneMC/endstone/commit/4a6b23224e78b27f935e0f21f7033340a4d8b0ea)

**Observed change.** Expands NetworkIdentifier with unknown16-byte data plus uint64 before GUID; rearranges ServerNetworkHandler clients map, task group and callback fields; adds observer size assertion.

**Causal interpretation.** Intermediate reverse-engineered layout placeholders are explicit and later named in561.

**Limits.** Unknown fields and inconsistent offset commentary remain uncertainty, not verified semantics.

<a id="commit-555"></a>
### Commit 555 {#commit-555}

c6bf29b27fdceba21877eb0bb43746976b5f1fbc · 2025-04-17T08:47:56Z

[feat: update `MinecraftPacketIds`](https://github.com/EndstoneMC/endstone/commit/c6bf29b27fdceba21877eb0bb43746976b5f1fbc)

**Observed change.** Adds ClientboundControlSchemeSet packet327 and moves EndId328.

**Causal interpretation.** Preview protocol enum extension.

**Limits.** No packet codec/traffic test.

<a id="commit-556"></a>
### Commit 556 {#commit-556}

05d37e9edb823973066701e6f0f66ecc73c76792 · 2025-04-17T09:33:00Z

[refactor: `ItemDescriptor::getFullName` now returns by value](https://github.com/EndstoneMC/endstone/commit/05d37e9edb823973066701e6f0f66ecc73c76792)

**Observed change.** Changes ItemDescriptor, BaseDescriptor and InternalItemDescriptor getFullName from const std::string& to std::string by value; makes EMPTY_INGREDIENT_HASH constexpr.

**Causal interpretation.** Makes returned name ownership explicit rather than borrowing a reference; declaration and implementation move together. Native virtual return ABI changes as well.

**Limits.** No allocation/performance measurements; native integration not run.

<a id="commit-557"></a>
### Commit 557 {#commit-557}

7f43551555c94947fd9e395b10f6e223fdd04263 · 2025-04-18T04:02:50Z

[feat: update various class members](https://github.com/EndstoneMC/endstone/commit/7f43551555c94947fd9e395b10f6e223fdd04263)

**Observed change.** Adds preview EntityRegistry is_viewing_ field, provisional Mob DeathTickingComponent pointer, native Player offset changes, Container unknown pointer and ItemGroup optional-stack size136.

**Causal interpretation.** Exploratory ABI modeling exposes provisional fields rather than final facts; 558/561 retract some of them.

**Limits.** Comments/TODOs and source assertions are not binary confirmation.

<a id="commit-558"></a>
### Commit 558 {#commit-558}

be2392270d68e714a0ae16933b840471b1cddde8 · 2025-04-18T07:34:55Z

[fix: correct members of `Player` class](https://github.com/EndstoneMC/endstone/commit/be2392270d68e714a0ae16933b840471b1cddde8)

**Observed change.** Retracts Container unknown pointer, models embedded PlayerUIContainer, and changes Container pure virtual declarations to nonpure native declarations/default destructor.

**Causal interpretation.** Allows a concrete embedded native container representation without inventing a padding array; reverses a provisional layout field.

**Limits.** Native method implementations remain external; no instantiated execution/build validation.

<a id="commit-559"></a>
### Commit 559 {#commit-559}

e8c6837d4c9b7863e4651549fbbfb60f66ea8ddf · 2025-04-19T12:24:48Z

[feat: update linux symbols](https://github.com/EndstoneMC/endstone/commit/e8c6837d4c9b7863e4651549fbbfb60f66ea8ddf)

**Observed change.** Updates Linux preview table: Pack::createPack key now includes IPackIOProvider and47 retained addresses change; Windows table unchanged.

**Causal interpretation.** Completes staged Linux symbol adaptation after Windows547 and provider548/550.

**Limits.** All keys/scalars audited; actual address correctness remains unverified.

<a id="commit-560"></a>
### Commit 560 {#commit-560}

6719a3a114a9a66e8c2b5adbedc0da7eab28b468 · 2025-04-22T05:59:22Z

[Merge remote-tracking branch 'origin/main' into feat/1.21.80-support](https://github.com/EndstoneMC/endstone/commit/6719a3a114a9a66e8c2b5adbedc0da7eab28b468)

**Observed change.** Imports daoge's PR173 button-codec fix, exact second-parent form_codec blob.

**Causal interpretation.** Mixed action-form elements need explicit type=button; complements PR168 and selection handling518.

**Limits.** No client form rendering test; PR173 primary available but reviews/comments partially inaccessible.

<a id="commit-561"></a>
### Commit 561 {#commit-561}

643824997e37dce69fd39aad28100e04e8c5029a · 2025-04-23T11:16:55Z

[feat: add `NetherNet::NetworkID`](https://github.com/EndstoneMC/endstone/commit/643824997e37dce69fd39aad28100e04e8c5029a)

**Observed change.** Names the previous unknown NetworkIdentifier storage as a24-byte variant of monostate, P2P remote uint64 and Realms UUID. Removes the provisional Mob DeathTickingComponent pointer/TODO.

**Causal interpretation.** Replaces layout placeholders with a concrete transport identity model and retracts a speculative field.

**Limits.** Field naming/type accuracy not proved by removing TODO; no ABI test.

<a id="commit-562"></a>
### Commit 562 {#commit-562}

459ca70abac9dcb5aa439b5e6242748fc3d61159 · 2025-04-28T03:17:04Z

[feat: add comparison operators](https://github.com/EndstoneMC/endstone/commit/459ca70abac9dcb5aa439b5e6242748fc3d61159)

**Observed change.** Adds default strong ordering for P2P/Realms transport IDs, UUID equality/inequality and lexicographic signed64-half less-than.

**Causal interpretation.** Supplies value-comparison requirements for variant/native identifier use.

**Limits.** Ordering convention is structural, not network identity equivalence proof; no compile/test.

<a id="commit-575"></a>
### Commit 575 {#commit-575}

6479cd1491095b488fb46ec6ab95d687a8e71ff1 · 2025-05-06T08:20:59Z

[[feature] 1.21.80 support (#174)](https://github.com/EndstoneMC/endstone/commit/6479cd1491095b488fb46ec6ab95d687a8e71ff1)

**Observed change.** Merges1.21.80 support PR174 with55 changed entries exactly matching second parent; imports41 commits (31 own-slice and10 earlier-target preview commits).

**Causal interpretation.** Release integration combines staged Windows/Linux/native-layout work. Existing PR174 base/head/merge identities match; code is reused only by exact commit/blob lineage.

**Limits.** Codecov reports0.00% project coverage and all modified coverable lines covered; neither statement proves meaningful native coverage. No runtime validation.

<a id="commit-576"></a>
### Commit 576 {#commit-576}

50e10410cb7ba6e1712958d310c03e6c279c8e38 · 2025-05-06T16:09:09Z

[chore: prepare for version 0.7.3](https://github.com/EndstoneMC/endstone/commit/50e10410cb7ba6e1712958d310c03e6c279c8e38)

**Observed change.** Adds0.7.3 release notes, Minecraft1.21.80 badge and patch1→3. Reports new controls and join/localization/multiprocessing fixes.

**Causal interpretation.** Release-facing account links changes to user-facing behavior; daoge collaboration is established from original PR commits, not an explicit credit in this changelog.

**Limits.** Release URL still v0.7.0. Author outcome claims not independently verified.

<a id="commit-577"></a>
### Commit 577 {#commit-577}

fcd866fcfc7cd558a289a45a4d48595f23cb5afb · 2025-05-06T20:01:20Z

[chore: update BDS to 1.21.80.3](https://github.com/EndstoneMC/endstone/commit/fcd866fcfc7cd558a289a45a4d48595f23cb5afb)

**Observed change.** Switches preview.28 to release1.21.80 and refreshes48 addresses on each platform; comments out preview EntityRegistry is_viewing_ field.

**Causal interpretation.** Demonstrates release-vs-preview ABI divergence; beta field cannot be carried into release solely because the feature version is close.

**Limits.** 96 numeric changes audited structurally, no binary address/size proof.
