<!-- retrieval: {"source_ids":["public:commit:05fcebee9cfcd3bef4a471cc31993e1392c0ec29","public:commit:15e963e6790cf142d6eeffc3b481f6e133286601","public:commit:321158e45a7fb48e1a6c30f9bfb64427e25f2f01","public:commit:59fec7d0b3ae069c74de8079b7372d0090c3c437","public:commit:6143e21bfab910957a43240452a967cd6cefed9d","public:commit:6fb24524cc22c216a28ee61a368a58e054c48a0d","public:commit:71fd3c45d2efd7ddf87403c38c88c67a49a63a78","public:commit:991253a882892bdb50fa936d56e127cbea70e758","public:commit:ad336ebcf2e5877a1800804a0a0c13bc967a181c","public:commit:bb026497328ca728d17ff10c1350e7ae76ca9146","public:commit:bf183941b91da81662efc2defb952838e8343dca","public:commit:d29ea13a7c97cc635d6b78c63265206117589a17","public:commit:d8acbb9489e1767e34245eaa592def6f6ee4749e","public:commit:da68c2947a6f9da4cbcfd1947f0a3dc5361e7433","public:commit:dae5bbdeca98cb04202a45623e0a2ecf8615edb0","public:commit:ef8c9012d11e1ea591110743b50cc0084f8a6ba7","public:commit:f6406c033497c36e1396d2e6855758aeb76f233d","public:thread:EndstoneMC/endstone:175","public:thread:EndstoneMC/endstone:185"],"source_type":"public","date":"2025-04-18..2025-05-21","topics":["lifetime","concurrency","ffi","testing","build","performance","api","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Release claims, updater preservation and lifecycle reversals {#release-claims-updater-preservation-and-lifecycle-reversals}


## Releases and native compatibility {#releases-and-native-compatibility}

615/616 package0.8.0, and649/652 package0.8.1. Changelogs are useful authored accounts of intended features, not execution evidence.649 accidentally deletes earlier0.8.0 feature bullets and650 restores them; this is a documentation repair rather than a feature removal/reintroduction. Python loader minor-version acceptance is updated with the API version.

The three Bedrock updates are verified proportionately.617 changes all49 symbol values on each platform;646 changes13 of50 Windows entries and no Linux values;655 changes40 of50 Windows and all50 Linux values. There are no key additions/removals in those version-only table updates. The linked public commits expose the per-key changes; these source values do not validate native addresses.617 and646 numeric patches were read;655's bulk is fully structurally checked rather than pretending each offset independently conveys an engineering lesson. Native addresses, layouts, hook correctness and binary compatibility were not tested.

<a id="background-work-is-added-and-withdrawn"></a>
## Background work is added and withdrawn {#background-work-is-added-and-withdrawn}

618 introduces an import-time daemon thread and one shared asyncio loop. run submits a coroutine with run_coroutine_threadsafe and returns a Future. There is no plugin owner, explicit cancellation scope or shutdown function.643 explicitly removes the module temporarily. The record does not say why, so missing lifecycle controls are an observed limit, not an attributed reason for withdrawal. At700 this helper is absent. This is a useful counterexample to reading an isolated feature commit as a permanent recommended concurrency model.

## Event semantics from issue175 {#event-semantics-from-issue175}

The reporter distinguishes attempted action from actual effect: a prohibited Creative tool can still trigger BlockBreakEvent, and an invulnerable custom actor can trigger ActorDamageEvent.644 checks canDestroyInCreative before publishing the block event.645 consults the native damage sensor before publishing actor damage, returning false for no damage and true for the no-damage-with-side-effects variant while skipping the original hurt call. The native call uses will_trigger=false. Those exact control paths are established; the enum name alone does not establish preservation of all native side effects or all cooldown behavior. Damage is documented as raw rather than post-mitigation. Wu's issue response specifically claims damage-sensor and Creative-tool fixes, not every initially requested damage behavior.

<a id="safer-update-defaults-with-bounded-overwrite-exceptions"></a>
## Safer update defaults, with bounded overwrite exceptions {#safer-update-defaults-with-bounded-overwrite-exceptions}

Issue185 describes repeatedly losing a config/default/permissions.json change that enables @minecraft/server-net; another participant confirms it.656 changes extraction from preserving three named files to preserving existing files by default. Only the executable, behavior_packs, resource_packs, definitions and named shipped documentation/filter/release-note paths are overwritten. New files are still extracted. Any skipped existing archive entry suppresses the subsequent server.properties rewrite, a broader condition than merely finding that properties file.

The source preserves user configuration more broadly but still overwrites allowlisted pack content and can leave shipped files outside the list stale. Extraction is not made transactional. Existing integrity checks and download mechanics are context, not new guarantees introduced by656. No updater was run and no source ZIP was extracted during this review.

653 repairs Linux wheel cache ownership after building;654 moves Docker caches to OS/SHA keys with prefix fallback, enabling fresh cache saves while reusing older layers. These imply storage/reuse tradeoffs, but CI success, cache hit rates and performance were not measured. Detours gitlink reversals elsewhere are recorded as dependency identities only; nested submodule code was not reviewed.

Discussion context: [issue175](https://github.com/EndstoneMC/endstone/issues/175), [issue185](https://github.com/EndstoneMC/endstone/issues/185). Tests here are absent for updater preservation, native event effect semantics and coroutine shutdown. This case supports careful release attribution, preservation-first migration and explicit ownership of background work.

## Per-commit decisions and revisions {#per-commit-decisions-and-revisions}

<a id="commit-615"></a>
### Commit 615 {#commit-615}

[ef8c9012d11e](https://github.com/EndstoneMC/endstone/commit/ef8c9012d11e1ea591110743b50cc0084f8a6ba7) · 2025-05-11T20:35:45Z · docs: update CHANGELOG.md

0.8.0 changelog reports1.21.80.3, registry/enchantment/repair/unbreakable APIs and PlayerDeathEvent template fix, labels Result simplified. Corrects older release links. These are authored release claims, no runtime verification.


<a id="commit-616"></a>
### Commit 616 {#commit-616}

[ad336ebcf2e5](https://github.com/EndstoneMC/endstone/commit/ad336ebcf2e5877a1800804a0a0c13bc967a181c) · 2025-05-11T20:36:30Z · chore: bump version to 0.8.0

Bumps API/version0.7.3→0.8.0 and Python loader adds0.8 to supported minor versions; no independent mechanism or performance lesson.


<a id="commit-617"></a>
### Commit 617 {#commit-617}

[bf183941b91d](https://github.com/EndstoneMC/endstone/commit/bf183941b91da81662efc2defb952838e8343dca) · 2025-05-14T16:54:20Z · chore: update BDS to 1.21.81.2

Updates advertised Minecraft1.21.81 and native symbol timestamp/version/Windows+Linux offsets for BDS1.21.81.2. All numeric address changes read; no ABI offset correctness inferred or binary loaded.


<a id="commit-618"></a>
### Commit 618 {#commit-618}

[dae5bbdeca98](https://github.com/EndstoneMC/endstone/commit/dae5bbdeca98cb04202a45623e0a2ecf8615edb0) · 2025-05-14T19:04:38Z · feat: add `endstone.asyncio` for running coroutines to a background thread

Adds import-time daemon thread/shared asyncio loop and run_coroutine_threadsafe returning Future; no explicit stop/cancel/plugin ownership lifecycle. Title explicitly aims background coroutine execution. Later643 removes module temporarily, so do not infer permanent recommended async API.


<a id="commit-619"></a>
### Commit 619 {#commit-619}

[d8acbb9489e1](https://github.com/EndstoneMC/endstone/commit/d8acbb9489e1767e34245eaa592def6f6ee4749e) · 2025-05-14T19:04:48Z · style: code formatting

Stubgen argument-list formatting only; identical arguments/order and behavior, no independent lesson.


<a id="commit-643"></a>
### Commit 643 {#commit-643}

[f6406c033497](https://github.com/EndstoneMC/endstone/commit/f6406c033497c36e1396d2e6855758aeb76f233d) · 2025-05-18T18:14:38Z · refactor: temporarily remove `endstone.asyncio` module

Explicitly temporarily removes618 asyncio module; deletion is exact blob001420bd. No stated reason, so daemon cleanup risks cannot be presented as author motivation. No async helper at later main boundary.


<a id="commit-644"></a>
### Commit 644 {#commit-644}

[6fb24524cc22](https://github.com/EndstoneMC/endstone/commit/6fb24524cc22c216a28ee61a368a58e054c48a0d) · 2025-05-18T19:55:24Z · fix: prevent BlockBreakEvent from firing with items that cannot break blocks in creative mode

Issue175: before BlockBreakEvent in Creative, reject nonnull held item whose native canDestroyInCreative is false. Prevents event for prohibited tool path; no survival behavior change. Returnfalse propagates through existing event hook; runtime breadth untested.


<a id="commit-645"></a>
### Commit 645 {#commit-645}

[da68c2947a6f](https://github.com/EndstoneMC/endstone/commit/da68c2947a6f9da4cbcfd1947f0a3dc5361e7433) · 2025-05-18T20:39:25Z · fix: respect the `damage_sensor` component when calling ActorDamageEvent

Issue175: before ActorDamageEvent consult native DamageSensorComponent with will_trigger=false, returnfalse forNo ortrue forNoButSidesEffectsApply. Documents event damage as raw; adds native layout/DealsDamage enum and platform symbols. Early return means original hurt is skipped on both paths; correct native side-effect semantics require runtime confirmation, not inferred from enum spelling.


<a id="commit-646"></a>
### Commit 646 {#commit-646}

[6143e21bfab9](https://github.com/EndstoneMC/endstone/commit/6143e21bfab910957a43240452a967cd6cefed9d) · 2025-05-19T22:03:21Z · chore: update BDS to 1.21.82

BDS1.21.82 update changes advertised version/timestamp and selected Windows offsets; Linux table unchanged. Numeric patch read, no address validation or upstream execution.


<a id="commit-649"></a>
### Commit 649 {#commit-649}

[71fd3c45d2ef](https://github.com/EndstoneMC/endstone/commit/71fd3c45d2efd7ddf87403c38c88c67a49a63a78) · 2025-05-19T23:35:18Z · docs: update CHANGELOG.md

0.8.1 changelog reports1.21.82.1, command interop/grants and issue175 event gating. Accidentally removes0.8.0 registry/meta feature bullets; next650 restores. Release prose is author assertion, not test evidence.


<a id="commit-650"></a>
### Commit 650 {#commit-650}

[bb026497328c](https://github.com/EndstoneMC/endstone/commit/bb026497328ca728d17ff10c1350e7ae76ca9146) · 2025-05-19T23:37:09Z · docs: update CHANGELOG.md

Restores0.8.0 registry/enchantment/repair/unbreakable changelog bullets removed649; documentation repair only, no implementation reversal.


<a id="commit-652"></a>
### Commit 652 {#commit-652}

[05fcebee9cfc](https://github.com/EndstoneMC/endstone/commit/05fcebee9cfcd3bef4a471cc31993e1392c0ec29) · 2025-05-20T11:18:07Z · chore: bump version to 0.8.1

Patch version0.8.0→0.8.1, API minor unchanged; release bookkeeping only.


<a id="commit-653"></a>
### Commit 653 {#commit-653}

[991253a88289](https://github.com/EndstoneMC/endstone/commit/991253a882892bdb50fa936d56e127cbea70e758) · 2025-05-20T12:24:10Z · ci: add step to ensure Conan home folder permissions

Linux wheel workflow chowns ~/.conan2 to runner user after build, intended Conan cache permissions repair. Command read, never executed; effect/CI success not claimed.


<a id="commit-654"></a>
### Commit 654 {#commit-654}

[321158e45a7f](https://github.com/EndstoneMC/endstone/commit/321158e45a7fb48e1a6c30f9bfb64427e25f2f01) · 2025-05-20T13:44:42Z · ci: add restore keys to docker layer cache

Both Docker publication jobs replace one fixed cache key with OS+SHA keys and OS-prefix fallback, allowing new save entries while reusing earlier layers. Inferred cache freshness/storage tradeoff, no timing measurements.


<a id="commit-655"></a>
### Commit 655 {#commit-655}

[59fec7d0b3ae](https://github.com/EndstoneMC/endstone/commit/59fec7d0b3ae069c74de8079b7372d0090c3c437) · 2025-05-21T20:36:15Z · chore: update BDS to 1.21.83

Advertises1.21.83; structurally verified all50keys/platform unchanged,40Windows and50Linux offset values changed, version/timestamp updated. Numeric bulk verified proportionately; no address correctness or binary execution.


<a id="commit-656"></a>
### Commit 656 {#commit-656}

[d29ea13a7c97](https://github.com/EndstoneMC/endstone/commit/d29ea13a7c97cc635d6b78c63265206117589a17) · 2025-05-21T20:56:55Z · fix: ensure only certain server files are overwritten during update

Fix185 flips updater from special-case preservation of3configs to default preserve existing files, overwriting only executable, behavior_packs/*,definitions/*,resource_packs/* and named shipped docs/filter/release-notes. New files still extract; any skipped existing entry disables server.properties modification. Broader preservation helps world/config safety but allowlisted pack paths still overwrite and unusual shipped files outside list may remain stale. No transactional update/runtime test.


<a id="commit-657"></a>
### Commit 657 {#commit-657}

[15e963e6790c](https://github.com/EndstoneMC/endstone/commit/15e963e6790cf142d6eeffc3b481f6e133286601) · 2025-05-21T20:57:56Z · style: code clean up

Restores progress-constructor indentation changed656; pure formatting, no independent behavior lesson.

