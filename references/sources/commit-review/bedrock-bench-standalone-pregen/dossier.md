<!-- retrieval: {"source_ids":["public:commit:f3a696cc01d7438a7bcbab1c37a93df14dff4d35"],"source_type":"public","date":"2026-10-12","topics":["lifetime","concurrency","ffi","testing","build","performance","recovery","api","diagnosis","documentation","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="adapter-integration-configuration-provenance-and-template-acceptance"></a>
# Adapter integration, configuration provenance, and template acceptance {#adapter-integration-configuration-provenance-and-template-acceptance}

## Identity, bounds, and useful result {#identity-bounds-and-useful-result}

Source: [EndstoneMC/bedrock-bench commit](https://github.com/EndstoneMC/bedrock-bench/commit/f3a696cc01d7438a7bcbab1c37a93df14dff4d35). It adds PocketMine-MP, Nukkit, PowerNukkitX and world pre-generation. Vincent is the author and Claude Opus 5.5 is explicitly credited as coauthor; the source does not divide the work between them.

The implementation creates a common native-runtime installation/configuration layer, three explicit server adapters, and a reusable world-template pipeline. Its strongest transferable mechanism is keeping release/runtime/helper inputs, configuration categories, written values, and world provenance separately inspectable. Its main inference limit is equally important: template acceptance checks a per-cell coverage report and a saved tree hash, but the bot-tour report counts client-received chunks and shutdown does not require a clean exit. It does not establish that every required chunk survives a restart.

This is an offline source review. Reported durations and failure thresholds in committed documentation remain author-reported; no benchmark was run.

## 1. Why the common layer exists {#1-why-the-common-layer-exists}

These engines do not share BDS configuration, launch, console, movement or generation behavior. A generic command renderer would erase meaningful differences. The new `StandaloneServer` instead shares the part that really is common: install a release plus runtime, preserve default config text, create a writable fresh server copy, render a typed override plan, record changed settings, and read written settings back after a run. Nukkit and PowerNukkitX add a `JavaServer` layer; PocketMine uses a pinned PHP build. Server-specific command capability remains local to each adapter.

Existing context matters. At this SHA the registry discovers concrete subclasses by module inspection and checks class contracts. It filters abstract/shared classes using class identity and an own `name`; no central registration edit is needed. The existing CLI maps `prepare-world` to the lazy `pregen:prepare_world` entry, and this commit supplies that implementation.

The cross-server matrix uses three rotated repeats, a 60-second cooldown, and one rerun of invalid attempts. It pairs `spread100` and `spread100-pregen` where supported, includes both default and `no-watchdog` Nukkit, and keeps PocketMine and Dragonfly on the fresh scenario in this matrix. BDS/Endstone and BDS/LeviLamina pairings retain their respective base builds. These declarations are experiment design, not completed comparison results.

## 2. Release, runtime, helper, and cache identity {#2-release-runtime-helper-and-cache-identity}

The catalogs pin server download URL, size and SHA-256, plus version/build context. Nukkit uses an exact timestamped snapshot associated with `b3caad6`; PocketMine uses 5.44.3; PowerNukkitX uses 3.0.5. Runtime pins cover Windows and Linux Temurin JDK 21.0.12.1+1 and PocketMine PHP build 524. The JDK intentionally includes `javac` for the helper and `jcmd` for OS-thread identification. PHP points to an immutable build tag instead of a moving latest artifact, and Linux declares its extension directory.

A runtime install is keyed by runtime/platform/artifact identity. A server install key includes server/version, release SHA, runtime artifact SHA and additional source hashes where helpers are built/copied. Server and runtime trees are hashed separately and combined into the reported install identity. Native runtime files remain in their immutable cache; only the `server/` subtree becomes the run's writable copy. The copy's release file is checked against its installed hash. This makes a helper edit invalidate the affected install instead of silently reusing the old helper.

`fetch_release` distinguishes a pinned catalog download from an explicit local artifact. The explicit local path is adopted under its own content hash and tagged local; it is not compared with the selected release's pin. A matching catalog entry can still provide runtime metadata. In contrast, the artifact-directory route through existing `fetch.obtain` verifies the pinned size/hash. This distinction is necessary when interpreting an artifact as released versus locally supplied.

The source includes tar path/type/link-target checks and dispatches ZIP extraction to the shared checked extractor. Tar extraction uses the standard data filter when available; the fallback handles checked members on older Python versions. Tests cover ordinary executables, relative symlinks and simple escaping names/targets. They do not establish universal archive safety, all link-chain behavior or all platform edge cases. No downloaded binary was executed during this review.

Contextual trust limit: `ensure_install` rehashes an existing cache tree and compares its sidecar, but recreates a missing/unreadable sidecar using the current tree. Thus the ordinary immutable-cache guarantee assumes the retained baseline metadata is trustworthy; it is not a defense against coordinated cache/metadata modification. The target's template loader is stricter about a missing report. Both are local provenance mechanisms, not signed attestations.

## 3. Configuration: three separate questions {#3-configuration-three-separate-questions}

The configuration plan explicitly separates harness prerequisites, parity settings and rescue settings. Each pin supplies a reason and may name a default, type, include-variant or skip-variant rule. Unknown table/type/variant entries, unsupported formats, missing reasons and duplicate unconditional pins are rejected. The plan derives values from the run context, including CPU count, ports, view/tick distances, seed, player count and autosave interval.

The writer answers three different questions:

1. What was shipped? Nukkit extracts its English YAML from the pinned JAR; PocketMine extracts its YAML from the PHAR without executing PHP. Where no file value exists, a declared default provides the comparison baseline.
2. What was changed? Only differences from that baseline become `Override` records with category and reason.
3. What was written? Every written value is tracked and semantically read back, including values equal to defaults. Boolean spellings can normalize; reformatting and unrelated new server keys do not automatically invalidate a run.

The YAML helper is intentionally a narrow indentation/scalar editor, not a general YAML parser. It preserves surrounding content/newline style, replaces scalar values, can replace a whole mapping with `{}`, and rejects nesting under a scalar. It does not promise full YAML grammar support. That constraint matters when extending an adapter to a different upstream configuration format.

A planned setting is also not necessarily an observed runtime fact. The Nukkit/PM helper override records say the network packet limit is lifted, but the helpers apply it later after startup. Nukkit catches reflection/channel errors and logs a warning. The adapter does not require a success acknowledgment before treating the installation/configuration as ready. The inherited `facts` contract describes observed facts, while several new fields are derived from written configuration or chosen launch arguments. These should be interpreted as configured intent unless independently confirmed.

## 4. Nukkit: preserve the default failure, expose rescue as a separate arm {#4-nukkit-preserve-the-default-failure-expose-rescue-as-a-separate-arm}

Nukkit uses protocol 2193 and the bot's fake-XUID compatibility flag. Its dialect handles console prefixes, short/full Git build identity, player entry, helper tick replies and readiness. It compiles a small helper against the selected JAR with the pinned runtime's `javac --release 21`, UTF-8, disabled annotation processing and deterministic JAR packaging. Files are sorted with fixed ZIP timestamps/permissions; the helper-source tree participates in the cache key.

The helper provides tick counter, complete position list, bounded command vocabulary for nearby blocks/dimensions, and pre-generation. Numeric output uses a stable locale. Nearby fill accepts only grass, farmland, leaves or sapling, clamps height and iterates inclusive bounds. Its coordinates/radius/count arguments have basic validation, but it is an internal operator tool, not a generally resource-bounded public service. Dimension routing is explicit; unsupported targets fail. Position parsing returns unknown for incomplete replies, distinguishing missing evidence from an empty online population.

All bots share loopback, so a per-IP packet limit can become a harness artifact. The helper schedules a one-time startup adjustment: it finds RakNet interfaces, reflects their channel collection and sets the channel packet limit to the maximum integer. The operation logs success/failure; it is not a continuously verified invariant. A warning or delayed/unavailable interface can leave the intended limit unapplied.

The stock watchdog remains in the default arm. Documentation reports that a first autosave after roughly 17,600 generated chunks could exceed its 60-second threshold, even ending with process code zero. A separate `no-watchdog` variant sets `debug.level=2`, acknowledges the accompanying extra debug logging, and categorizes it as rescue. The report is not silently converted into the default workload. Disabling adaptive world tick throttling is recorded as parity: otherwise world slowdown can be hidden behind a normally ticking server. Allow-flight suppresses the hover kick; it does not establish BDS-equivalent physics.

Commands are capability-specific. Effects use a long numeric duration, not unsupported `infinite`; selectors are refused where needed. Entity summoning transforms names for this engine and explicitly cannot honor all BDS-style positional behavior. Loot, random tick speed, waypoint and ticking-area actions remain unsupported instead of becoming no-ops. This is a practical API-boundary lesson: preserve unsupported status through orchestration so successful command submission cannot masquerade as equivalent work.

## 5. PocketMine and PowerNukkitX: analogous contracts, different semantics {#5-pocketmine-and-powernukkitx-analogous-contracts-different-semantics}

PocketMine uses protocol 1001 and the separate legacy bot frontend. Its console dialect recognizes PHP/server levels and unprefixed command replies. Launch uses the pinned PHP executable, no wizard, no ANSI, an unset `PHPRC`, and on Linux the declared extension directory. These environment/argument changes are recorded. A PHP helper returns server tick/positions and schedules RakLib packet-limit removal after 20 ticks. The reported loopback default is 200 packets per tick with a 300-second block; the helper's existence and intended adjustment are not proof it applied on a real build.

The default arm disables the reported 1,024-MiB main-thread hard limit as a named rescue change; `stock` leaves it in place. Committed docs report a stop around 23 seconds during a prior 100-bot join. No run underlying that number was independently examined here. The distinction is preserved instead of treating a memory-rescued result as stock performance. Its supported chaos surface is limited to player-related commands; unsupported simulation features stay explicit.

The nonexecuting PHAR reader finds the manifest after the halt-compiler stub, parses entries, supports raw/deflated members, and verifies uncompressed length and CRC. It refuses unsupported bzip2 compression. Tests build their own small unsigned PHAR fixtures. These checks support extracting a known shipped config, not full PHAR execution/signature validation; normal artifact identity comes from the outer release pin, while explicit local artifacts have the trust distinction above.

PowerNukkitX uses protocol 2193/fake-XUID and the Java base without a helper. Console build parsing normalizes the version and drops a snapshot suffix; the artifact pin supplies stronger build identity. Fresh-world preparation writes all three dimension seeds into a committed JSON world-config template. Because configuration can exist before world data, the freshness path is `worlds/<level>/db`, not the containing directory. The adapter verifies every written fresh-world dimension seed afterward. Template runs deliberately preserve the template's own world configuration instead of rewriting it, relying on the template report/tree boundary.

Its YAML plan increases the per-IP packet limit and disables adaptive tick changes and loading every level. The per-session limits remain unchanged and are documented. Positions fall back to bot reports. Its BDS-like chaos dialect filters out unsupported/unsafe equivalents, including cleanup that would also kill players in this engine. Capability similarity is therefore not assumed from shared command names.

## 6. JVM observation: one bounded lookup, then conservative fallback {#6-jvm-observation-one-bounded-lookup-then-conservative-fallback}

The Java base fixes initial and maximum heap to the same positive `M`/`G` setting and forces UTF-8 console streams. It records those launch differences and the runtime's release-file version. The GC field says the JVM default rather than measuring collector behavior.

For tick CPU attribution, the base asks the selected JDK's `jcmd <pid> Thread.print` once, after it has the server process and native tool path. It parses the OS thread ID from the JDK 21 bracketed decimal field or older `nid` representation, then uses the ID only while present in live thread samples. Otherwise it falls back to the existing Java-main-name rule. Failure is not repeatedly retried, and Docker lacks that local native lookup. Tests stub tool output/failure and thread lists. They establish intended selection logic, not real OS/JVM attachment permissions, startup timing, thread lifetime or profiler accuracy.

## 7. World pre-generation: two pipelines with unequal evidence {#7-world-pre-generation-two-pipelines-with-unequal-evidence}

The scenario asks each server to generate its own template, avoiding cross-engine world-format/generator substitution. `world_key` includes seed, level name, radius, bot/cell count, columns, spacing and origin. The default radius 12 has 441 chunks in its exact integer disc; default minimum coverage is 99% in every cell. A report carries per-cell count, engine/version/scenario/variant, pipeline, elapsed time, harness version and eventual tree hash. The cache path is keyed by server/version/scenario, deliberately allowing the same world across variants such as the watchdog comparison.

### Plugin path {#plugin-path}

Nukkit's `PreGen.java` creates one batch per grid row, deduplicates that row's chunk disc, and orders chunks by coordinates modulo three to reduce neighboring population contention. It limits outstanding population requests to 64 by default. Finished row areas are unloaded in groups of 256 per tick to avoid one giant save/unload spike. The check phase calls the engine's populated predicate for each requested disc, logs per-cell found/expected totals, unloads those chunks, saves the level, emits completion and cancels its repeating task.

This is a concrete attempt to move generation and verification outside the measured run. Its comment says checks reload saved chunks. At the inspected boundary, however, unload return values are ignored, and the same process's engine API supplies the check; this review did not inspect that pinned engine's storage implementation. It does not restart the server to prove recovery. Generation can keep retrying until the harness's four-hour plugin timeout; there is no single-job exclusion or general upper resource bound in the helper command.

The Python parser accepts cell-count lines and the completion pattern. Missing cell indices become zero coverage, so ordinary incomplete output fails. Duplicate indices overwrite earlier counts; the completion line's declared cell count is not separately cross-checked, and expected counts are taken from the helper. The tests inject complete/partial strings into a fake console, rather than execute this Java helper.

### Bot tour {#bot-tour}

Other adapters use ten bots or fewer, visiting cells in rounds. The derived scenario is fresh, raises server view distance to the template radius and changes bot count/prefix; other bot parameters remain inherited. The placer handles round zero. The tour then polls every five seconds, dwells at least 20 seconds, leaves on all-cell coverage, 30 seconds without growth across the round, or a 300-second cap. It retries a teleport once if that bot has never arrived. A server-death callback interrupts the tour.

A visit counts as arrived within four chunks of its center; only reported x/z are checked. Coverage is the maximum latest progress-row `in_view` seen during the visit, capped at the exact-disc expected count. The granted-radius guard rejects a too-small nonempty set of spawned events. It does not independently check row freshness, bot-process liveness, dimension, exact requested chunk membership or all-spawn-event completeness.

The real bot context narrows the claim further: `ChunkTracker.InView` counts unique received chunk columns within granted radius plus one around the bot's current chunk/dimension. The tour's denominator is the exact template-radius disc around the target center. Radius tolerance and arrival tolerance can therefore admit received chunks that do not prove each required center-disc chunk exists. Client receipt also does not prove persistence. This is a source-established semantic mismatch, not a measured incidence or a claim that every generated template is bad.

## 8. Failure lifecycle and what a hash cannot certify {#8-failure-lifecycle-and-what-a-hash-cannot-certify}

`prepare_world` rejects non-template scenarios and non-native execution. Existing templates are verified/reused before building. A nonblocking machine lock prevents overlapping builder work; placement/fetch errors and bot-process errors map to environment-gate failure, template construction failures to server-failed, and insufficient report coverage to invalid. It retains build logs, writes a report before validation, stores only a report with no reported problems, then releases the lock/removes its work copy in `finally`. These are explicit failure classes rather than a single generic unsuccessful run.

After generation the builder always calls `_stop`. If the process remains alive it sends stop, waits, then kills on timeout. It closes handles regardless. The return code is not required to be zero; a kill does not add a validation error. Afterward only a nonempty world directory is required before returning the report. Thus a coverage-complete tour can reach storage after an unclean stop. The forced-stop unit test checks kill/close behavior, not rejection of the resulting world. The plugin path has its own earlier save/check attempt, but the surrounding cleanup still supplies no clean-stop guarantee.

Stored worlds are staged into a read-only tree, hashed, and accompanied by a separate JSON report. Tree and report are not committed as one atomic pair. A missing report is refused on reuse. The generic staging helper lets an already-existing final directory win a rename race; the report writer then hashes that final tree. CLI machine locking reduces normal competition, but the storage helper itself does not bind the candidate report to a concurrently winning tree through a candidate-hash comparison. No race was executed here.

`verified_template` rechecks the stored report's own problems, tree hash and exact `world_key`. It does not independently validate unique cell indices/coordinates, recompute expected disc counts, compare the report threshold with a newly stricter scenario threshold, or check report server/version/variant against an expected adapter identity. Notably `min_coverage` is absent from `world_key`; reuse is judged by the stored threshold. These are trust/schema boundaries for locally generated reports, not evidence of an adversarial exploit. The test that reuses a synthetic report with a different embedded version shows that identity checking is not the asserted contract.

A tree hash proves the cached bytes have not changed relative to the retained report. It cannot prove the report was truthful, all cell coordinates were visited, shutdown saved cleanly, feature semantics matched another engine, or the world can restart without generation. Those require distinct observations.

## 9. Tests, outcomes and application {#9-tests-outcomes-and-application}

The commit contains 111 static Python test functions: 17 Nukkit, 18 PocketMine, 13 PowerNukkitX, 38 shared standalone and 25 pregen. Parameterized cases are not counted as executed tests. All five modules and six synthetic fixture files were read; [test-coverage.md](test-coverage.md) records each test name and intended boundary.

Most installs use placeholder JARs, synthetic runtimes and monkeypatched fetch/build functions. The optional compiler test uses a trivial demo class, not the actual Nukkit helper against the pinned real API. Fake console and fake tour worlds simulate process replies and time. No target suite, compiler, PHP runtime, JVM, bot, server, download or benchmark was run in this research. Fixture assertions and authored empirical notes therefore remain different evidence classes.

Portable uses supported by this case:

- Add an adapter by sharing installation/configuration mechanics while keeping command/fidelity differences explicit.
- Track every written configuration value, even when it does not qualify as an override; preserve a separate category/reason for actual changes.
- Keep a failing default arm and its rescue variant identifiable; do not silently improve the baseline being compared.
- Give generated-state caches a report and integrity hash, but independently design coverage, shutdown and recovery validators.
- Test parser/writer/state-machine behavior deterministically, then identify the real runtime/API and persistence checks those tests leave open.
- Prefer an unknown measurement to guessing a thread identity when exact lookup/fallback cannot establish it.

No broad claim about present-day personality or universal preferred design follows from one jointly attributed commit. Later evolution and Docker removal belong to the broader history review; this dossier establishes the exact state introduced at ordinal 25.
