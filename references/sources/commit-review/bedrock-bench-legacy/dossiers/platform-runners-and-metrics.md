<!-- retrieval: {"source_ids":["public:commit:0a49c6914171a3d325adfca5bc50cf612ea4cb8e","public:commit:13f9df244044ed39ce62af70d3954f46de997983","public:commit:655e3e486185341520890621f65d9b69a9b6067d"],"source_type":"public","date":"2026-10-12","topics":["concurrency","build","performance","recovery","diagnosis","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="platform-runners-measurement-and-failure-boundaries"></a>
# Platform runners, measurement and failure boundaries {#platform-runners-measurement-and-failure-boundaries}

Sources: initial commit `0a49c6914171a3d325adfca5bc50cf612ea4cb8e`, `legacy/windows/run_endstone.py`, `bench_metrics.py`, `legacy/linux/bench.py`, `metrics_linux.py`, `compare3.py`, and `legacy/windows/chains/wf_{cores,threads,uniq,wake,netcmp}.py`. All listed source bodies were read; the Levi runner's exact differences from the Windows runner were reviewed separately.

## Experiment construction {#experiment-construction}

Both runners target offline RakNet with view distance 10, tick distance 4, maximum 200 players, seed 20261010 and CSG enabled. They separate server and bot CPU sets, teleport joined bots to height 300 in 640-block-spaced cells, protect players with effects, observe loading, then measure steady state. These are constraints of the archived experiment, not an all-purpose recommended server configuration.

Windows launches either BDS directly or an Endstone CLI parent, discovers the BDS child, pins the BDS to performance cores and the launcher/bots to efficiency cores, and raises BDS priority. It records installed binary hashes, selected modules and thread names. Each run removes the selected world. DLL installation uses temporary files plus `os.replace`, compares source/destination SHA256, and refuses to swap while a BDS process from the same directory is still running. Finally it restores original server.properties and the pristine package binaries. Missing files in an experimental arm silently fall back to pristine DLL/PYD/PDB counterparts by design, but the recorded “from” field makes that mixture inspectable.

The Windows runner optionally suspends the thread owning the hidden DevTools window. It repeatedly suspends it, reads an x64 thread context, and keeps it suspended only when RIP resolves into endstone_runtime.dll. This is invasive counterfactual instrumentation intended to separate a known spinning renderer cost. Running with DevTools suspended is not the ordinary release behavior. Suspension, whether it succeeded and pre-suspension CPU are recorded, and the finally block resumes the thread.

Linux is orchestrated from the historical Windows host through Docker, despite the filename. It invokes `tasklist` for host interference and uses a Windows BDS ZIP cache path. A base BDS volume is unpacked once; each trial receives a fresh volume copy. Bots share the server container's network namespace and dial localhost, avoiding Docker's UDP proxy. Vanilla runs inside the wheel-built image with a direct BDS entry point to keep userland matched. The allocator variant optionally preloads glibc rather than the bundled allocator, and `/proc/maps` evidence is collected. Container CPU sets, image ID, wheel SHA256, properties and selected version lines are recorded.

Fresh copies, CPU affinity and transport matching reduce confounding, but neither runner proves exclusive machine use. Foreign BDS/bots/containers are warnings, not automatic invalidation. Thread pools may still size themselves from machine-wide topology, independent of cpusets. The old Linux image builder expects an `image/Dockerfile` not present in this imported source layout. Several Windows helper modules and Linux bot binaries are likewise absent. This source is useful historical evidence but does not suffice to replay the runs unaided.

## Phases and what “settled” establishes {#phases-and-what-settled-establishes}

The Windows sequence is idle, optional profiled join storm, loading/settle with periodic nudges, spread check, unprofiled steady, optional profiled steady. Linux collects idle, whole loading and steady windows with snapshots. Nudging alternates a 16-block horizontal offset for bots still above Y=290 with fewer than a threshold of unique chunks. It can repair a stuck load state, but introduces additional server work and changes the workload differently for slower/stuck arms.

Default settle tests require a minimum duration plus fleet unique-chunk rate below 0.1 per bot per second. A maximum duration cuts off loading. Windows optionally requires a minimum final view for every bot; Linux does not have that option here. A stalled client, a dropped client, or missing telemetry can lower the rate. `uniq_rate` returns zero with insufficient samples. A cap is a stopping condition, not proof of completed loading. Linux records `settle_capped`; the Windows runner logs the cap but does not set an equivalent explicit result field.

Windows fails a timeout waiting for ALLJOINED; Linux only warns and proceeds. In either case the bot's ALLJOINED marker already includes failed attempts. Spread is checked by nearest grid-cell occupancy, player count and worst offset. Windows queries server positions, while the custom-server adapter uses bot-reported positions. The checks are printed/saved rather than used as strict validity gates. There is no guarantee of identical settled world state from equal nominal settings alone.

## TPS and CPU formulas {#tps-and-cpu-formulas}

TPS is change in reported gametime divided by elapsed host time between console responses. The underlying console command, its scheduling delay and parsing must be trustworthy. Arrival-time differences can reflect console delay as well as tick progress. The implementations generally filter nonpositive elapsed time, but do not reject counter resets/wraps or attach request-response identities.

Windows metrics assign each interval to the phase containing its endpoint, which can include an interval spanning a boundary. Linux `tps_samples` instead selects probe points inside the phase before differencing. This makes counts and boundary treatment differ.

“Lowest 15 s” also has several implementations:

- Linux `tps_min` / metrics use nonoverlapping 15-second wall bins.
- Levi metrics use sliding windows spanning three successive probe intervals, which may not be exactly 15 seconds.
- `wf_wake.minima` scans from each probe until elapsed time reaches span−0.5 seconds.

These are related but not interchangeable statistics. Legacy quantiles use nearest rank by Python `round(q*(n−1))`, and `wf_wake.med` chooses the upper middle item rather than averaging both middle items. They differ from `statistics.median` for even-sized samples. A reported p90 must retain the implementation.

Linux reads thread utime+stime from `/proc/<pid>/task/<tid>/stat`, hardcodes 100 ticks/second, and timestamps the snapshot before the Docker exec finishes. It selects the numerically smallest TID named MC_SERVER because children may inherit the name. That is an explicitly coded heuristic, not platform-independent proof of the tick thread. Threads missing from the first snapshot contribute zero; threads exited before the second disappear. Process CPU derived by summing surviving threads undercounts some thread churn.

Windows has both CPU-cycle/TSC-based and thread CPU-time paths through missing historical helper modules. The imported scripts do show which tuple element they consume: Windows chaos uses cycles/TSC; custom-server main-thread summaries use CPU seconds. `wf_cores.py` reads a per-run tsc_hz variable but its helper still divides by a fixed 2.1 GHz constant. `wf_netcmp` keys named threads in a dictionary, so duplicate names can overwrite each other. These are analytic hazards, not measured evidence of corruption in a particular saved run.

MC_SERVER milliseconds/second divided by TPS yields tick-thread CPU milliseconds per tick. It excludes blocked time, worker execution, and sleeping; it is not wall-time tick duration. `compare.py` even divides the Endstone reference by a fixed 20 rather than a measured TPS. Keep “CPU” in every downstream description.

## Join/view metrics and clocks {#join-view-metrics-and-clocks}

Windows join latency matches the first server “Player connected” line to the bot's first JOINED line by display name. It uses time of day and has no midnight rollover handling. Linux estimates whole-hour offset between host and server log clocks, then subtracts; this assumes those clocks differ only by a stable whole-hour zone offset. The custom summary has a limited one-day rollover heuristic. These do not provide an epoch/monotonic join identity.

View t90 finds the first dump at or above 90% of the last observed unique count and subtracts the first teleport time. It is neither an absolute required chunk count nor complete-view correctness. Dump cadence and variable run endpoints materially affect it. `compare3.delivery` measures fleet cumulative thresholds from the first teleport, which is different again from a median per-bot threshold.

Error counts are regex classification. Words such as “crash,” “exception” and “ERROR” can appear in benign diagnostics, while errors outside the regex may be missed. Levi's summary removes a recognized transport warning banner; that exclusion is specific to this comparison. Preserve raw log access and classification rules.

## Shutdown and recovery {#shutdown-and-recovery}

Windows DeathWatch records early BDS or launcher exit, interrupts waits, gathers recent crash-like files outside worlds plus a log tail, marks stopping before normal shutdown, and performs finally cleanup. A ServerDied exception is caught and logged without rethrowing, so process exit code alone does not make the run valid. Result death fields and completed phase evidence matter.

Linux stops bots with a container INT, escalates to removal/kill, sends BDS stop, and removes named containers and run volumes in finally. The recorded server exit is the docker-run subprocess result. Its performance summary defines “crashed” as absence of a steady window or nonzero server exit, combining incompletion and crash. Neither label should be paraphrased as proof of an actual native crash without corresponding logs.

The Windows writer prioritizes gametime commands over normal commands and uses a gap at least one estimated tick long when pacing is enabled. Normal work can backlog or starve. Stop bypasses that queue. Reader/writer workers are daemons and log streams are closed without an explicit pump join, leaving shutdown races possible in static control flow.

## Reuse {#reuse}

For a new benchmark, record observed rather than intended workload, phase boundaries in one clock domain, actual process identity, completed prerequisites, explicit failure reasons, probe uncertainty and raw artifacts. Preserve CPU versus wall semantics and allow invalid/incomplete outcomes to remain visible. The historical corrections and limitations are more reusable than copying the runner unchanged.
