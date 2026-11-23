<!-- retrieval: {"source_ids":["public:commit:6532f281bed55fa628713f5f970f96e3d19a009b"],"source_type":"public","date":"2026-10-12","topics":["lifetime","concurrency","ffi","testing","performance","diagnosis","documentation","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="levilamina-introduction-immutable-packages-controlled-configuration-and-comparison-limits"></a>
# LeviLamina introduction: immutable packages, controlled configuration, and comparison limits {#levilamina-introduction-immutable-packages-controlled-configuration-and-comparison-limits}

## Identity, reading, and attribution {#identity-reading-and-attribution}

Source: [EndstoneMC/bedrock-bench commit 6532f281bed55fa628713f5f970f96e3d19a009b](https://github.com/EndstoneMC/bedrock-bench/commit/6532f281bed55fa628713f5f970f96e3d19a009b), ordinal 20, “Add the LeviLamina adapter and its matrix,” authored 2026-10-12 15:38:25 UTC. Its parent is `6e7194282641d0105cfcb7470858fdb968a4a705`.

This is a static source review; no upstream code was built, tested or run.

Vincent authored the commit, and its message explicitly credits Claude Opus 5.5 as coauthor; the source does not divide the implementation between them. Comments, configuration labels, and documentation describe the submitted implementation, not an individual preference. LiteLDev's LeviLamina, PreLoader, PeEditor, CrashLogger, runtime-data, and LeviOptimize are separately authored upstream products; this adapter does not claim invention of their mechanisms.

This is a historical introduction snapshot. Later removal of variants, simplification of feature metadata, and replacement of full configuration snapshots are covered by the [main history dossier](../../bedrock-bench-all/dossiers/configuration-and-attribution-evolution.md); those later choices must not be projected backward.

## Problem and comparison design {#problem-and-comparison-design}

LeviLamina is a Windows mod loader around Mojang's BDS. The harness needs to compare a concrete package stack while retaining the identity of the BDS executable it hosts, optional optimization mods, allocator, native support processes, and changed settings. Merely attaching the label “LeviLamina” would hide several experimental variables.

The added matrix specifies four arms: vanilla BDS 1.26.51.1; LeviLamina 26.51.6; that release with LeviOptimize's fresh-install defaults; and the same release with the three additional optimization switches enabled. All use the hosted BDS build, the `spread100` scenario, three repeats, rotated order, 60-second cooldown, and one retry of an invalid run. These are declared experiment inputs, not measurements. No new result data accompanies the commit.

The adapter rejects a requested `arm.bds` that differs from its pinned dependency. Its documentation separately says a comparison beside only BDS 1.26.52.3 is flagged `different_bds_build`. This keeps engine-version differences visible rather than interpreting every performance difference as loader overhead or optimization. It does not by itself isolate allocator effects, additional threads, or CrashLogger attachment costs.

The base adapter inherits BDS command semantics, fresh-world preparation, property rendering, tick probing, and native executable provenance through `BdsFamily`. The registry discovers concrete modules rather than maintaining a new central name list; inspection of the existing registry confirms why this commit can add an adapter without modifying registration code. The shared base is contextual evidence, not newly authored code in this commit.

## Package provenance and install lifecycle {#package-provenance-and-install-lifecycle}

`artifacts/levilamina.toml` pins six GitHub release assets with exact size and SHA-256:

| Package | Pinned release | Installation role |
|---|---|---|
| LeviLamina | 26.51.6 | `LeviLamina/` becomes `plugins/LeviLamina/` |
| PreLoader | 1.16.3 | `bin/PreLoader.dll` becomes root `PreLoader.dll` |
| PeEditor | 3.9.2 | root `PeEditor.exe`, invoked once while staging |
| CrashLogger | 1.3.3 | executable under `plugins/LeviLamina/` |
| bedrock-runtime-data | 26.51.1-server.7 | root `bedrock_runtime_data` file |
| LeviOptimize | 0.17.0 | optional `plugins/LeviOptimize/` package |

The manifest says its dependency versions and placements come from package `tooth.json` files. That statement and the actual declared URLs/hashes were read; this review did not download release archives or independently reconstruct all upstream dependency resolutions. The pins establish the identity the harness intends to consume, not a source-to-binary reproducibility or package-security audit. BDS itself remains a separately pinned Mojang artifact from the shared BDS catalog.

`packages_of` validates that platform tables use `windows-<package>`, rejects unknown per-package extras, requires nonempty release and placement maps, rejects absolute/traversal/drive/backslash paths, and requires directory markers on both sides of a directory placement. `place_package` permits directory merging only when individual destination files do not already exist. A package cannot quietly overwrite BDS or a prior package's file. Missing selected source files/directories fail with an artifact-specific message.

The install sequence is:

1. Obtain the correct BDS install through the shared verified fetch path.
2. Obtain the five base packages, adding LeviOptimize only for its two variants.
3. Copy BDS into an empty staging directory; safely extract packages into a temporary `.unpack` subtree; place selected files in declared order; remove unpack scratch data.
4. Run `PeEditor.exe -mb` with that server directory as cwd, no stdin, captured UTF-8 output, and a 300-second timeout.
5. Require zero exit and the existence of `bedrock_server_mod.exe`; record the completed install tree hash and patched executable hash.
6. Make the cached install read-only, then copy it into a fresh writable run directory and recheck the copied executable hash.

PeEditor's output is produced by an opaque pinned utility. The harness verifies that the output exists and subsequently retains its observed identity; it does not compare that patched executable with a predeclared expected patched hash. The copied BDS hash plus package hashes identify inputs, while the new tree/executable hashes record the result. This is stronger than running a patcher anew during every measurement, but it is not a proof of deterministic patch output or harmless code.

The install cache key includes BDS tree hash and package content hashes. Base and optimization arms receive different installs; both optimization configurations share the same package install because their run-time config is written later. Changing the configuration should not force another native patching run. A local `arm.artifact` replaces only the LeviLamina zip; BDS and supporting packages remain pinned. The metadata records that package as `local`, and documentation says such results are unpublished-artifact comparisons.

Shared `fetch.ensure_install` rehashes an existing tree and rejects mismatch with its sidecar. An important boundary in that context is that an absent or malformed sidecar is reconstructed from the current tree. Therefore the mechanism detects mutations relative to an intact recorded hash; it is not authenticated tamper resistance against removal of both content and its evidence. No such mutation was performed in this review.

### Legal and platform boundaries {#legal-and-platform-boundaries}

The documentation names the Minecraft EULA and the LeviMC closed-source agreement for PreLoader/PeEditor. The manifest marks those latter packages `eula = "levimc"`; a missing acceptance flag raises before network download, as the unit test specifies. Already-cached or matching user-supplied artifacts use the shared cached/local path before that gate.

At this exact commit, the inspected `fetch.py` EULA registry contains only the Minecraft entry. Unknown `levimc` therefore receives a generic license label with no link in the CLI error/report, although the new server documentation supplies the LeviMC link. This is a static discoverability limitation, not a missing acceptance gate. The single existing `--accept-eula`/Minecraft-named environment flag is documented as accepting both agreements. This research accepted no agreements and fetched or executed no upstream package.

Fetch rejects non-Windows hosts and Docker; construction is allowed on other systems for contract tests. Launch rejects Docker and starts the modified executable directly. The distinction lets platform-independent tests inspect the adapter without pretending the native toolchain is available.

## Configuration ownership, drift, and semantic readback {#configuration-ownership-drift-and-semantic-readback}

The repository adds exact snapshots of PreLoader version 1, LeviLamina config version 42, and LeviOptimize config version 18. The documentation explains why fresh config is necessary: LeviLamina merges older config values over new defaults, while LeviOptimize rewrites config at shutdown. Reusing a prior run's directory could retain settings nobody selected for the present experiment.

`prepare_extra` writes each selected JSON document anew. It disables only the two upload settings in the base arm: CrashLogger's Sentry upload and LeviLamina usage statistics. Each change records category `harness`, file, dotted key, old/new JSON value, and reason. Crash logging itself remains enabled, including its external debugger attachment. Vulnerability protections, connection-frequency limits, force-enable-cheat-command setting, NetherNet defaults, log rotation, and PreLoader color logging remain at the checked-in snapshot values.

After the run, `readback` compares all written JSON leaves, not byte formatting. Dictionaries are flattened into dotted paths, arrays and empty dictionaries remain leaves, keys are sorted, and values are serialized to canonical JSON. Reformatting without changed values passes; missing files, malformed JSON, added/removed leaves, or changed values produce config-readback problems. At most five changed keys are named with a remainder count. Base `server.properties` readback checks the selected BDS property keys separately.

This design records desired persistent config and detects on-disk mutation. It does not prove the server used each value internally or that linked native mods did not change behavior elsewhere. Full snapshots also require release-specific maintenance: the README explicitly instructs starting each added release manually and comparing generated schemas/config versions. Later history's move to writing only owned telemetry leaves is a real change in strategy, not something this introduction already does.

The JSON `flatten` helper uses dotted paths as identifiers. This fits the supplied configurations; no general escape mechanism for literal dots in JSON keys is established. The input is controlled configuration, so this is a portability boundary rather than an observed miscomparison.

## Optimization variants and the metadata gap {#optimization-variants-and-the-metadata-gap}

The base is labeled fidelity V1 because it hosts BDS gameplay while routing allocation through statically linked mimalloc and applying packet/vulnerability protections. The allocator is declared in manifest metadata and explicitly copied into facts, because shared module scanning would not identify a separately mapped allocator DLL.

The default LeviOptimize variant is not an “all optimizations” arm. The source explains that a fresh install turns on `fixChunkLeak` and the dormant timing diagnostic. The leak fix removes disconnected players from map-tracking lists so those references no longer retain chunks. A no-disconnect spread run does not exercise this; churn does. The documentation warns that installations upgraded from older LeviOptimize releases can preserve additional enabled settings and therefore do not represent the fresh-install variant.

The `levioptimize-all` template differs from the default template in exactly three leaves:

- `features.optMovingBlock`: moving piston block entities reach clients without their contents while moving; the documentation says simulation/saving remain unchanged.
- `features.optSeenPercent`: explosion exposure is reused for a position within one tick, so successive same-location explosions may reuse results despite intervening block changes.
- `features.optPushEntity.enable`: enables the push path, including skipping zero-vector pushes.

The push-count limit remains `-1`, and `unlimitedPlayerPush` remains `false` in both templates. Consequently “every switch on” is an imprecise prose shorthand: the reproducible definition is those actual template values and the exact three-leaf diff. No inference about upstream optimization correctness follows from the label.

Loading LeviOptimize itself is a `nonvanilla` manifest override; each additional changed leaf also receives that category and a required explanation. The documentation labels both variants V2 and identifies altered behavior, but openly states that the feature schema is keyed only by server version. As a result, `run.json` uses LeviLamina's V1/base rows for the variants. The table and footnotes must accompany any interpretation. This is a known machine-readable fidelity gap, not evidence of equal gameplay. Tests verify the three changed keys and the unchanged unlimited limit; they do not repair variant-level feature representation.

The added spread matrix deliberately avoids the stated altered-feature triggers. That narrows what the comparison could test: it cannot show the variants are equivalent under redstone, explosions, collision-heavy play, or disconnect churn. A small or absent spread difference is not evidence that the optimization has no effect in other workloads.

## Console, process metrics, and failures {#console-process-metrics-and-failures}

The console dialect replaces BDS's prefix/level/version/ready patterns while retaining BDS tick, position, and command behavior. It accepts three-letter LeviLamina levels and long PreLoader levels. Every prefixed continuation line is stripped before the BDS JSON position parser sees it; bare `Quit correctly` is preserved as an unclassified line. The version parser requires LeviLamina's version suffix rather than accepting a plain BDS banner. Readiness recognizes both the timed LeviLamina message and bare BDS-style `Server started.`.

The supplied full-session fixture is explicitly synthetic. It includes startup, the specific benign NetherNet transport warning block, spawn, tick replies, multiline positions, unknown command, fatal error, and shutdown. The point is parsing behavior, not a recorded server run. Level counts are expressly not cross-server performance/health comparators.

The measured process is `bedrock_server_mod.exe`. The inherited tick rule selects the lowest-ID `MC_SERVER` thread; documentation says Windows has one, while the common rule also handles inherited names on Linux BDS. LeviLamina adds pool/logger diagnostic group regexes. The claim of roughly 28 additional threads is attributed to earlier measurements, not verified by these additions.

CrashLogger's separate process CPU is excluded from `process_cores`; any debugger-attachment overhead charged to the server remains included and is not isolated. This boundary should accompany process comparisons. Crash artifacts combine run-local `logs/crash` with matching executable-prefixed files from LocalAppData CrashDumps, restricted by modification time. The test exercises a new run-local report versus an older report. It does not test real debugger crash capture.

## Test evidence and its limits {#test-evidence-and-its-limits}

The added Python file contains 35 named test methods, some parameterized. The count is a source inventory, not an executed/passing count. Important specified contracts include:

- registration, protocol, platform and variant validation, shared BDS commands, thread-group matches, and every synthetic dialect role;
- artifact catalog consistency, exact BDS dependency, release-version URLs, EULA gating, feature-key presence, templates, and all matrix arms;
- malformed package metadata, traversal/path/directory errors, overwrite refusal, and missing placement sources;
- PeEditor argv/cwd/stdin/timeout contract, nonzero return, missing output, and missing executable;
- native-only fetch, unpinned versions, BDS mismatch, immutable install shape, cache reuse, package-set sharing, and local artifact substitution;
- fresh JSON writes, categorized overrides, missing variant package, formatting-insensitive readback, changed/missing config, direct launch, declared allocator/runtime facts, and crash-age filtering.

The download fixture creates tiny zip stand-ins, reports fake artifact hashes, substitutes host detection, and replaces PeEditor with a Python file write/rename. It verifies orchestration contracts but not real release integrity, executable patching, Windows launch, allocator behavior, telemetry shutdown, or performance. These tests were read, not run. No performance gain, successful smoke, native ABI correctness, or behavioral equivalence was independently established.

## Portable use {#portable-use}

Use this case when adding a native wrapper/plugin host to a benchmark: preserve the underlying engine version, make package composition a first-class input, stage irreversible installation work outside the measurement window, distinguish written settings from defaults, detect persistent config drift, and name process boundaries. Do not mechanically copy its full-snapshot strategy into a changing vendor schema, or equate a shared engine binary with identical effective work. Preserve the concrete variation table and metadata limitations whenever this source is retrieved for “fair comparison,” “optional optimizations,” “native package provenance,” or “config readback.”
