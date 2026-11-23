<!-- retrieval: {"source_ids":["public:commit:02859be4f4438b0303348f9bd175328c972964c2","public:commit:0910b70e04c9d47d095fa9bad6d76c72760bf1b2","public:commit:0a0cfb520c14d5770351ec3c13fb51f3ab8b4ff7","public:commit:341996b87c8c3e036f95816a0ca9f0fac00b3f2c","public:commit:3ee7f66a57b65529571359784bddac6ce0afec2c","public:commit:4152dbf365502be416c733d563b3bd81184aed1c","public:commit:48fa7497a4df6bfe03da46bd3f932ecc1e3ca3fd","public:commit:55685e979a48aeed71626523a8247f2168767b85","public:commit:6294e9e6f68b9178946502710077f872c22c2316","public:commit:65031cef88ea83090588d99472461aaafbe8f220","public:commit:70a1122bcadd80d6b0015371016b97d037bb1a7a","public:commit:721e51fc625a1e8bd187eff1eb99646d5e88df2e","public:commit:8a7109bb33a22b529a8a7b2ef6056f27f6267afd","public:commit:a6ae581a4e026404efb408b33262c65d091393c4","public:commit:c332ac3a24aa75363e5d44adae560646aba4ceb4","public:commit:cbaa01b15fb4cf955fe27da07e2880da01d499c6","public:commit:e76774897189b16a133a744c16c0c8f75cc2486f","public:commit:fd895823425de7f6a7116003431efe6839585f5d","public:thread:EndstoneMC/endstone:125"],"source_type":"public","date":"2025-01-12..2025-01-29","topics":["lifetime","concurrency","ffi","testing","build","performance","api","diagnosis","documentation","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# World resources, chunks and operational diagnostics {#world-resources-chunks-and-operational-diagnostics}

<a id="preserve-native-state-that-serialization-does-not-describe"></a>
## Preserve native state that serialization does not describe {#preserve-native-state-that-serialization-does-not-describe}

PrimeStrat's issue125 reports broken education-edition textures on Endstone, compared with normal BDS; SuperEric1 confirms. Vincent requests a world and PrimeStrat supplies a ZIP. Commit161 stops reconstructing the native LEVEL resource-pack stack solely from world configuration plus custom packs: it deserializes custom packs separately and appends them to the existing stack, preserving native chemistry/vanilla entries. Encryption keys and load logging remain. Vincent reports resolution in the issue after the commit. That is an author-reported outcome, not this review's reproduction; the archive was neither downloaded nor executed. Source: https://github.com/EndstoneMC/endstone/issues/125 .175/179 move this responsibility into server initialization, and186 places it before post-world plugin enablement.

## World and packet boundaries {#world-and-packet-boundaries}

103 supplies native sound packet/position declarations and108 completes public API, Python surface and send implementation. Factory-created native packets carry defaults and layout assumptions that were not exercised against a client.121 removes scaled integer conversion from vanilla-data dumps using floating truncation: it avoids the fixed-width conversion hazard but changes rounding semantics and is not a general floating-point overflow proof.173/178 centralize hashed block names, which179 uses to define highest block as non-air. That differs from the API prose's impassable wording; native getHeight is a virtual declaration, so empty/negative-column behavior remains unverified. Location overloads use coordinates in the receiver dimension. New highest methods and later loaded-chunk enumeration are not exposed in Python in this slice.

195–198 model native chunk storage/state and expose a minimal public Chunk identity. EndstoneChunk keeps copied coordinates and a borrowed dimension, avoiding a persistent strong LevelChunk reference but not preserving the world's lifetime.199 locks weak chunks temporarily and accepts state>=Loaded. The explicit unsigned Invalid0xff value is above Loaded9, so the filter admits the sentinel. Atomic state access does not synchronize iteration of the weak storage map.200 uses this allocating enumeration merely to count chunks for status. These are direct static costs/edge cases, not measured failures or performance regressions.

## Observability is a unit and meaning contract {#observability-is-a-unit-and-meaning-contract}

129/130 reconstruct ServerInstance/timing access and statistical storage. Current tick work includes scheduler heartbeat plus the native tick; TPS is capped, usage is capped at1, and averages use20 slots. Brace initialization with one value initializes only the first slot, affecting early averages.170/171 add threads, memory, world counts and MSPT;172 corrects Linux kB-to-byte conversion. Windows WorkingSet/PagefileUsage and Linux VmRSS/VmSize have different meanings, so a shared label does not make them identical physical-memory metrics. The Windows first-enumeration failure path leaves the opened snapshot handle unclosed.185 later fixes get_platform linking.

At endpoint200, usage is still a0..1 ratio printed with a percent sign and no factor100. Status also allocates per-chunk wrappers and rescans actors for each dimension. The code provides monitoring capability, not actual performance evidence. No TPS/MSPT values, process memory measurements, screenshots or native benchmark runs were collected.

## Apply to a new task {#apply-to-a-new-task}

Before replacing a native resource collection, establish which entries are synthesized outside persistent configuration. For snapshots, distinguish copied identity from retained native lifetime and define invalid/sentinel states separately from ordered progress. For diagnostics, specify units, warm-up behavior, platform semantics, saturation and collection cost; verify output scaling independently of the underlying measurement. The proposed checks are future validation work, not completed runtime tests.


## Per-commit evidence {#per-commit-evidence}

<a id="commit-103"></a>
### Commit 103 {#commit-103}

fd895823425de7f6a7116003431efe6839585f5d · 2025-01-12T13:37:40Z

[feat: add PlaySoundPacket](https://github.com/EndstoneMC/endstone/commit/fd895823425de7f6a7116003431efe6839585f5d)

**Observed change.** Adds native NetworkBlockPosition and PlaySoundPacket layout (name, position, volume, pitch) and includes it in player implementation; no send implementation yet.

**Causal interpretation.** This is dependency scaffolding for108, not independently working sound API.

**Limits.** No packet serialization or ABI size tests added.

<a id="commit-108"></a>
### Commit 108 {#commit-108}

70a1122bcadd80d6b0015371016b97d037bb1a7a · 2025-01-12T15:39:39Z

[feat: add `playSound`, `stopSound` and `stopAllSounds` to `Player`](https://github.com/EndstoneMC/endstone/commit/70a1122bcadd80d6b0015371016b97d037bb1a7a)

**Observed change.** Completes playSound/stopSound/stopAllSounds across public API, implementation, Python and stub. Uses native packet factory, fills name/position/volume/pitch or stop_all, and sends to player; inherited BlockPos constructors enable position construction.

**Causal interpretation.** Factory-created packets retain native type/initialization; stopSound relies on factory defaults for stop flags. Also resolves inherited name property and reorders existing bindings.

**Limits.** No wire-format, sound-position scaling, default flag or client playback tests; sound behavior not verified.

<a id="commit-121"></a>
### Commit 121 {#commit-121}

a6ae581a4e026404efb408b33262c65d091393c4 · 2025-01-14T16:59:11Z

[fix: integer overflows in rounding function](https://github.com/EndstoneMC/endstone/commit/a6ae581a4e026404efb408b33262c65d091393c4)

**Observed change.** Replaces scaled-double→int rounding in vanilla-data dumps with std::trunc(value*10^n)/10^n(default6), across properties and all bounding shapes; dump level parameters become const.

**Causal interpretation.** Removes fixed-width integer conversion overflow but changes numerical semantics from nearest rounding to truncation toward zero. Floating scale overflow and precision are not globally solved.

**Limits.** No boundary tests or emitted data comparison included; crash/overflow prevention not run.

<a id="commit-129"></a>
### Commit 129 {#commit-129}

341996b87c8c3e036f95816a0ca9f0fac00b3f2c · 2025-01-14T21:17:13Z

[feat: add `Timer` and `LoopbackPacketSender` class](https://github.com/EndstoneMC/endstone/commit/341996b87c8c3e036f95816a0ca9f0fac00b3f2c)

**Observed change.** Expands ServerInstance layout with network, LoopbackPacketSender, simulation/real Timer ownership; getter Minecraft becomes pointer and packet sender getter added. Models Timer methods/fields and GameSession constructors/reference sender. EndstoneServer exposes native getServer, removes convenience commands/network getters and updates all call sites.

**Causal interpretation.** Native ownership/layout modeling unlocks direct packet sender access needed151; wider native access trades convenience encapsulation for explicit object traversal.

**Limits.** Timer declaration is not a working timer implementation. Pointer-returning Minecraft is generally dereferenced without null guard; initialization-order assumption. No layout/run proof.

<a id="commit-130"></a>
### Commit 130 {#commit-130}

02859be4f4438b0303348f9bd175328c972964c2 · 2025-01-14T21:33:39Z

[feat: add `SharedConstants`](https://github.com/EndstoneMC/endstone/commit/02859be4f4438b0303348f9bd175328c972964c2)

**Observed change.** Introduces SharedConstants20ticks/s,50ms/tick, trial/subclient constants; rewires server stats arrays and calculations; include cleanup and relaxed global/constant naming rules.

**Causal interpretation.** Removes duplicate tick constants but does not alter measurement model. Existing aggregate array initialization only populates first slot(nonzero), not all slots, so startup averages need caution.

**Limits.** No actual TPS/accuracy/performance measurement.

<a id="commit-161"></a>
### Commit 161 {#commit-161}

721e51fc625a1e8bd187eff1eb99646d5e88df2e · 2025-01-22T21:36:37Z

[fix: append custom packs to the level pack stack instead of replacing them to preserve vanilla packs (e.g., chemistry)](https://github.com/EndstoneMC/endstone/commit/721e51fc625a1e8bd187eff1eb99646d5e88df2e)

**Observed change.** Fix#125 changes custom resource-pack loading from rebuilding/replacing LEVEL stack from world JSON to deserializing only custom packs and move-appending them to the existing native stack. Keeps encryption-key insertion and per-pack logging; uses contains for keys.

**Causal interpretation.** Preserves vanilla-generated entries such as chemistry assets, instead of assuming a serialized world list completely represents native state. PrimeStrat supplied the education-world bug and reproduction ZIP; SuperEric1 confirmed it. Vincent asked for a world, then reported resolution after this commit.

**Limits.** Author-reported resolution in issue125 is not this review's reproduction. Linked world archive was not downloaded or run; captured text and exact code path were reviewed.

<a id="commit-170"></a>
### Commit 170 {#commit-170}

8a7109bb33a22b529a8a7b2ef6056f27f6267afd · 2025-01-24T17:00:07Z

[feat: add more statistics to `/status` command](https://github.com/EndstoneMC/endstone/commit/8a7109bb33a22b529a8a7b2ef6056f27f6267afd)

**Observed change.** Expands status to current/average TPS, tick usage, process thread count/memory and per-dimension actor counts. Linux reads /proc/self/status; Windows counts threads via Toolhelp and reads WorkingSet/PagefileUsage.

**Causal interpretation.** Operational observability requires units and platform semantics as well as counters. Linux values initially remain kB while formatter expects bytes, fixed172; the usage ratio is formatted as a percent without multiplying100.

**Limits.** No measurements captured. Windows Thread32First failure leaves the opened snapshot handle unclosed. Linux VmSize and Windows PagefileUsage are not identical concepts of total physical memory. get_name link mismatch remains until185.

<a id="commit-171"></a>
### Commit 171 {#commit-171}

e76774897189b16a133a744c16c0c8f75cc2486f · 2025-01-24T17:16:28Z

[feat: improve `status` command](https://github.com/EndstoneMC/endstone/commit/e76774897189b16a133a744c16c0c8f75cc2486f)

**Observed change.** Adds MSPT alongside TPS and improves world/dimension labels in status.

**Causal interpretation.** Showing work duration with capped TPS distinguishes headroom and overloaded ticks better than TPS alone; this is display capability, not benchmark evidence.

**Limits.** Does not fix170 usage-percent scaling or Linux memory units; no output snapshot/test.

<a id="commit-172"></a>
### Commit 172 {#commit-172}

55685e979a48aeed71626523a8247f2168767b85 · 2025-01-24T18:15:27Z

[fix: return memory usage in bytes on Linux](https://github.com/EndstoneMC/endstone/commit/55685e979a48aeed71626523a8247f2168767b85)

**Observed change.** Converts Linux /proc memory kB to bytes before formatting and removes leftover Mob::die declaration.

**Causal interpretation.** Repairs a concrete cross-platform unit contract and finishes detour cleanup166.

**Limits.** No runtime numeric comparison; usage-percent scaling remains unchanged.

<a id="commit-173"></a>
### Commit 173 {#commit-173}

0a0cfb520c14d5770351ec3c13fb51f3ab8b4ff7 · 2025-01-24T20:52:57Z

[feat: add `BedrockBlockNames`](https://github.com/EndstoneMC/endstone/commit/0a0cfb520c14d5770351ec3c13fb51f3ab8b4ff7)

**Observed change.** Adds hashed BedrockBlockNames::Air and compares ItemStack full-name hash to it instead of constructing/comparing a literal string; preserves existing null/count checks.

**Causal interpretation.** Uses the native hashed identifier representation at a frequently reached predicate, with explicit semantic target.

**Limits.** No measured speedup or hash-collision behavior claim; hashed identity assumptions are inherited.

<a id="commit-178"></a>
### Commit 178 {#commit-178}

cbaa01b15fb4cf955fe27da07e2880da01d499c6 · 2025-01-24T21:53:54Z

[feat: add `Block::getName`](https://github.com/EndstoneMC/endstone/commit/cbaa01b15fb4cf955fe27da07e2880da01d499c6)

**Observed change.** Native Block exposes hashed getName; removes BlockLegacy getFullNameId and updates public block/data/state plus devtools to use the block's full hashed name.

**Causal interpretation.** Centralizes identity at the actual native block object rather than reconstructing through legacy metadata, preserving full-name string use at public boundaries.

**Limits.** No runtime registry/name comparison; hashed-name ABI is assumed.

<a id="commit-179"></a>
### Commit 179 {#commit-179}

65031cef88ea83090588d99472461aaafbe8f220 · 2025-01-24T21:54:25Z

[feat: add `Dimension::getHighestBlockAt`](https://github.com/EndstoneMC/endstone/commit/65031cef88ea83090588d99472461aaafbe8f220)

**Observed change.** Makes Dimension block lookups const; adds highest Y/block methods using native getHeight with predicate name!=Air; removes old EndstoneLevel resource loading to complete175. Location overload uses coordinates in the receiver dimension.

**Causal interpretation.** The implementation defines highest as non-air, despite prose mentioning impassable. A coordinate-based overload does not validate or adopt Location's dimension.

**Limits.** Native getHeight is a virtual declaration only here; empty-column/negative-Y behavior not implemented or verified locally. Highest methods lack Python binding/stub in this slice.

<a id="commit-195"></a>
### Commit 195 {#commit-195}

6294e9e6f68b9178946502710077f872c22c2316 · 2025-01-25T23:50:24Z

[feat(chunk): add `ChunkSource`](https://github.com/EndstoneMC/endstone/commit/6294e9e6f68b9178946502710077f872c22c2316)

**Observed change.** Defines ChunkSource's broad native virtual interface and weak chunk storage map, expands Dimension fields to own chunk source and adds getter.

**Causal interpretation.** Establishes the native storage seam for enumerating currently resident chunks without owning the underlying chunks indefinitely.

**Limits.** Reverse-engineered method order/layout unvalidated; some offset comments are inconsistent/stale. No load/save/async operations implemented or tested here.

<a id="commit-196"></a>
### Commit 196 {#commit-196}

48fa7497a4df6bfe03da46bd3f932ecc1e3ca3fd · 2025-01-25T23:58:32Z

[feat(chunk): add `ChunkState`](https://github.com/EndstoneMC/endstone/commit/48fa7497a4df6bfe03da46bd3f932ecc1e3ca3fd)

**Observed change.** Defines ChunkState unsigned-byte values from Unloaded0 through Loaded9, plus Invalid0xff; adds DamageSource documentation text.

**Causal interpretation.** Sentinel state must be considered separately from ordinal progression;199's >=Loaded later admits Invalid.

**Limits.** No native enum/layout verification. Documentation does not repair borrowed damage-source lifetime.

<a id="commit-197"></a>
### Commit 197 {#commit-197}

c332ac3a24aa75363e5d44adae560646aba4ceb4 · 2025-01-29T15:21:23Z

[feat(chunk): add `Chunk` class](https://github.com/EndstoneMC/endstone/commit/c332ac3a24aa75363e5d44adae560646aba4ceb4)

**Observed change.** Adds abstract Chunk coordinate/level/dimension API, C++ umbrella include, Python class/re-export/module/stub with reference-returning level/dimension bindings. Also relaxes Conan compiler/version validation while retaining C++20,x86_64,Win/Linux and Linux libc++ constraints.

**Causal interpretation.** A minimal identity API can precede mutating chunk operations. Removing compiler gates increases accepted configurations but does not establish their ABI compatibility.

**Limits.** No implementation until198 or compiler matrix results. The unrelated toolchain-policy relaxation must not be hidden under the chunk feature title.

<a id="commit-198"></a>
### Commit 198 {#commit-198}

3ee7f66a57b65529571359784bddac6ce0afec2c · 2025-01-29T15:51:33Z

[feat(chunk): implements `EndstoneChunk`](https://github.com/EndstoneMC/endstone/commit/3ee7f66a57b65529571359784bddac6ce0afec2c)

**Observed change.** Implements native LevelChunk getters and atomic state access, replaces selected pointer fields with references, and adds EndstoneChunk storing coordinate values plus borrowed EndstoneDimension reference.

**Causal interpretation.** Public chunk identity can survive native chunk unload without holding LevelChunk alive; world/dimension lifetime is still external.

**Limits.** Atomic state read does not make the containing storage map iteration safe. Native layout/coordinate conversion untested; no Python lifetime pin to dimension.

<a id="commit-199"></a>
### Commit 199 {#commit-199}

4152dbf365502be416c733d563b3bd81184aed1c · 2025-01-29T16:00:58Z

[feat(chunk): add `Dimension::getLoadedChunks` to fetch all loaded chunk](https://github.com/EndstoneMC/endstone/commit/4152dbf365502be416c733d563b3bd81184aed1c)

**Observed change.** Adds Dimension::getLoadedChunks by iterating weak native storage, skipping expired entries, locking each weak_ptr and accepting state>=Loaded, then allocating unique EndstoneChunk wrappers.

**Causal interpretation.** Weak storage is observed without extending ownership beyond each loop; public snapshots are coordinate wrappers rather than live native chunks.

**Limits.** Unsigned Invalid0xff satisfies >=Loaded9. No map lock/thread restriction is enforced here, and no new Python binding for this method in the slice. No unload/concurrency/state-sentinel tests.

<a id="commit-200"></a>
### Commit 200 {#commit-200}

0910b70e04c9d47d095fa9bad6d76c72760bf1b2 · 2025-01-29T16:13:08Z

[feat: add chunk data to `status` command output](https://github.com/EndstoneMC/endstone/commit/0910b70e04c9d47d095fa9bad6d76c72760bf1b2)

**Observed change.** Status now counts loaded chunks by building the full getLoadedChunks wrapper vector per dimension and calling size; adjusts MSPT/world/dimension wording and actor-count loops.

**Causal interpretation.** Reuses public enumeration for observability, but counting now pays allocation/enumeration costs and inherits its state filter.

**Limits.** No measured overhead or server data. Usage remains a0..1 ratio printed with percent sign rather than scaled100; tests are not added.
