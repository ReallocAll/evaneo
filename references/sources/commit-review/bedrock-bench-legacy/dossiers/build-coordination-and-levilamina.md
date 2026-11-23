<!-- retrieval: {"source_ids":["public:commit:0a49c6914171a3d325adfca5bc50cf612ea4cb8e","public:commit:13f9df244044ed39ce62af70d3954f46de997983","public:commit:655e3e486185341520890621f65d9b69a9b6067d"],"source_type":"public","date":"2026-10-12","topics":["lifetime","concurrency","ffi","testing","build","performance","api","diagnosis","documentation","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="build-provenance-coordination-and-levilamina-comparison"></a>
# Build provenance, coordination and LeviLamina comparison {#build-provenance-coordination-and-levilamina-comparison}

Sources: [initial import](https://github.com/EndstoneMC/bedrock-bench/commit/0a49c6914171a3d325adfca5bc50cf612ea4cb8e), including the Windows chain scripts, Linux shell/PowerShell/Docker files, and LeviLamina harness/configuration/research files. Nothing in these scripts was run.

## Serialized experiments and multi-worker handoffs {#serialized-experiments-and-multi-worker-handoffs}

The shell chains serialize builds and benchmark jobs through a shared `BENCH_LOCK` created with shell noclobber. They put an owner label and time in the file, wait if it exists, and remove it only when the label matches. Later Windows/Linux wrappers add EXIT traps, so ordinary exits and errors release their lock. Each job gets its own lock, allowing other queued experiments between a build and its measurement.

This is useful operational evidence: compiling or running another server can invalidate measurements, so coordination extends beyond one process. Markers such as build done, rerun done, Windows done and Linux go communicate dependencies between workers.

There are important limits:

- Labels are strings, not unique process-bound ownership tokens. Several custom chains share the same `custom-bench` prefix and sometimes reuse an existing lock merely because it has that prefix. Concurrent processes using that label could mistake another process's lock for their own.
- Early custom chain functions have no EXIT trap. Some chains keep waiting for a marker without timeout, PID/start-time validation or stale-owner recovery.
- Completion markers are often touched in an EXIT trap even on early failure. Others write “ended early,” but downstream gates only test file existence. A completion signal says the attempt terminated; its contents and artifacts determine success.
- Several orchestration scripts continue after a failed job because they do not use fail-fast shell settings or inspect the returned rc before proceeding. Some combine phases from separate attempts.

Portable lesson: use unique ownership and explicit terminal states; record attempted, completed, failed and validated separately. This is static analysis of the historical scripts, not a claim that their actual worker coordination failed.

## Windows artifact staging {#windows-artifact-staging}

`wf_stage.py` reads a build marker for candidate DLL, directory or wheel paths; otherwise it falls back to a known repository build path. It clears the destination arm, checks DLL modification time against a minimum, copies the DLL and adjacent PDB or extracts those names from a wheel, then records hashes.

It captures current checkout HEAD, dirty status, diff content and a truncated diff digest; it also snapshots untracked source files named by status. That retains much more than a version label, helping distinguish an uncommitted experiment from a release.

The limit is provenance: a current working-tree diff is not proof those bytes produced the DLL. The fallback path can select a different build unless hashes and logs are correlated, and wheel extraction does not receive the same DLL freshness check. Metadata belongs to the attempted staging process. The later runner's source/destination hash check proves copy integrity, not build causality.

The scripts name separate network, memory, chunk-generation and wake-threshold arms and preserve whether a run was profiled. They test fixed worker wake thresholds 0 and 0.01 seconds, with the latter explicitly copied as an uncommitted source change. These names and source checks are experiment definitions; no comparative performance outcome is inferred here.

## Linux wheel build and validation {#linux-wheel-build-and-validation}

`build_wheel.ps1` creates a detached worktree at an explicit commit, optionally copies a listed set of working-tree source files, compares changed paths against that exact list, and requires a chosen text fragment in the diff for the threshold experiment. It prints HEAD/diff and preserves the cibuildwheel exit code across worktree cleanup. This is a useful guard against accidentally building unrelated uncommitted files.

It pins the wheel target to CPython 3.14 manylinux x86-64 and gives builds distinct dev versions. Its container mounts a shared Conan cache. Version stamping via SETUPTOOLS_SCM_PRETEND_VERSION does not make a dirty patch into that release. `CIBW_TEST_COMMAND=true` explicitly skips the wheel test command; a built wheel is not an executed test pass.

`build_verify.ps1` selects a verification branch and writes a host profile defining ENDSTONE_VERIFY_PERF through `tools.build:defines`, because a comment says the wrapper overrides the alternative CMake extra-variables path. Later chains inspect the runtime shared object inside the wheel for `[verify]` strings before using it. That checks that verification-related text is present, not that hooks are enabled or exercised.

Unlike the general build helper, the verification helper does not preserve and exit with the cibuildwheel rc; it logs that code, then cleanup runs Git commands that can alter the process's last-exit status. Shell chains additionally check wheel presence and marker strings, but neither replaces a fully verified build/test result. This distinction should survive in a downstream build-failure diagnosis guide.

The final Linux chain queries the remote branch head, fetches only if necessary, verifies the commit object, builds that resolved commit, and copies the wheel before integration. Another chain accepts a commit from a named handoff marker and warns if it lacks an expected ancestor. A warning is not a hard ancestry gate. These steps expose moving-branch risk without fully eliminating it.

The two imported Dockerfiles use Python 3.14 slim-bookworm and install curl support, then either PyPI Endstone 0.11.13 or local wheels. Image tags, apt packages and indirect Python dependencies are not content-locked here. Moreover, the actual Linux runner references an `image/Dockerfile`, not these `docker/base` and `docker/fix` paths. These are retained artifacts rather than proof of the exact effective image recipe.

## LeviLamina runner: verified reuse and exact differences {#levilamina-runner-verified-reuse-and-exact-differences}

`harness/run_levi.py` is an adaptation of Windows `run_endstone.py`. A full unified source comparison was used to read the changed code while retaining the already-read shared body. Changes are:

- Choose a server directory, executable and output root instead of fixed BDS paths.
- Discover the chosen executable by name and launch it directly in the existing “vanilla” branch.
- Recognize LeviLamina's alternate server-ready line and log prefix.
- Include Levi/preloader/mimalloc modules in recorded module metadata.
- Broaden chaos error recognition to Levi error/fatal abbreviations.

The core phases, CPU placement, chunk accounting, nudges, Windows sampler dependencies and cleanup remain shared. Here `--vanilla` means “launch directly without the Endstone launcher”; it can still launch LeviLamina's modified executable. It must not be interpreted as proof that the server is unmodified vanilla.

`firststart.py` temporarily applies benchmark properties to generate configs/inspect console responses, then restores the properties. Its finally block does not cover all process teardown on startup errors. `run_one.sh` locks one run and explicitly checks both rc and died_during_run afterward.

`wf_levi.sh` runs plugin-default, loader-only, all-options, matched-BDS-version vanilla and chaos arms. It parks/removes the plugin directory for loader-only runs and restores the default config through a trap. It continues logging subsequent runs even if a prior run fails. `wf_levi2.sh` explicitly reruns the loader-only arm because the first overlapped a Minecraft client; that is a reported contamination and retry rationale in source comments. `wf_levi3.sh` adds second samples to explore run-to-run noise. The scripts alone do not establish the resulting measurements.

## Configuration and imported research claims {#configuration-and-imported-research-claims}

`LeviOptimize.config.default.json` enables fixChunkLeak and the timing command; moving-block, exposure cache and the entity-push group are disabled. `optall` turns the latter groups on but keeps maxPushTimes=-1 and unlimitedPlayerPush=false. “All options” is therefore shorthand for these enabled groups, not every possible behavioral modifier. The LeviLamina default JSON enables statistics, crash Sentry upload, vulnerability fixes and NetherNet patches. The loader's network path remains RakNet under the benchmark properties.

The 172-line `research.md` was read in full. It is the imported author's dated research report, not newly revalidated external evidence. It cites pinned LeviOptimize v0.17.0 and LeviLamina v26.51.6 plus historical tags/issues. Its mechanisms and caveats are useful, but its claims about “latest,” platform support, absence of benchmarks, open issues and unreleased compile compatibility are bounded to its 2026-10-12 research date.

The report distinguishes:

- Config deserialization dispatch that installs hooks at load and removes them at disable; migration merges stored user values over new defaults, so fresh and upgraded installs can differ.
- Map-tracker cleanup on disconnect releasing shared chunk views, which has no work in a steady run with no disconnects.
- Piston packet trimming that omits moved block-entity data, same-tick explosion exposure caching invalidated only at tick end, and push caps that change visible behavior. Intended optimization is not automatically strict vanilla equivalence.
- A presumed zero-vector push no-op that cannot be proved from the mod source alone.
- Removed player-lookup/network/hopper/timer/redstone caches or replacements, with reported crash/desync and ABI-layout risks.
- Loader-level mimalloc on Windows versus plugin-specific features. Loader-only is the appropriate within-version baseline for separating plugin contribution; it is not a no-allocator-change baseline.
- BDS 1.26.51.1 versus Endstone's 1.26.52 experiment, making direct cross-version causal attribution unsafe.

The report's “V0/V1/V2” behavior classes are its analytical labels, not a certified equivalence classification. Claims such as all repository issues containing no measurements require a separate exhaustive external-source audit if reused as present-tense facts. The current review establishes what this report said and how the supplied configs/runner operationalize it, without executing linked projects or repeating its external research as independently proven.

## Engineering uses {#engineering-uses}

Retrieve this dossier for native build provenance, dirty-tree experiment isolation, staged artifact verification, multi-agent experiment locking, completion markers, loader/plugin baselines, configuration migration and performance-versus-behavior claims. It includes both safeguards and counterexamples so the history is not flattened into unconditional advice.
