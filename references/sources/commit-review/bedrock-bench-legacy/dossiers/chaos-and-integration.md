<!-- retrieval: {"source_ids":["public:commit:0a49c6914171a3d325adfca5bc50cf612ea4cb8e","public:commit:13f9df244044ed39ce62af70d3954f46de997983","public:commit:655e3e486185341520890621f65d9b69a9b6067d"],"source_type":"public","date":"2026-10-12","topics":["ffi","testing","performance","diagnosis","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="chaos-behavioral-checks-and-integration-test-meaning"></a>
# Chaos, behavioral checks and integration-test meaning {#chaos-behavioral-checks-and-integration-test-meaning}

Sources: initial commit `0a49c6914171a3d325adfca5bc50cf612ea4cb8e`, Windows/Linux `chaos.py`, Windows `intest.py`, Linux `intest_linux.py`, Windows `bench_metrics.py`, Linux `metrics_linux.py`, `windows/chains/wf_chaos.py`, plus the adapter subclass discussed in the cross-server dossier. All were read without execution.

## Stress coverage {#stress-coverage}

Windows chaos schedules independent action families for reconnect/quick disconnect, stacked players, waypoint toggles, game-mode changes, kills, mob/loot spawning, cleanup, kicks, dimension trips, far teleports and disconnect-during-load, random tick speed, weather, block edits and ticking areas. A heap with a sequence number orders delayed callbacks, avoiding comparison of function objects when due times tie. Bot events maintain online/away/flash/killed state, and successful respawns schedule effects and a return home.

The main loop uses a seeded `random.Random` if supplied, but the default seed is unspecified. Action periods are jittered 0.6–1.4×. When the console backlog exceeds 150, most new action families are skipped and counted; `list` remains enabled. Delayed callbacks still run. This deliberately limits unbounded queue growth but means a slower arm receives different executed stress. Each action is logged as intent; actual console acknowledgements are needed to establish application.

Windows monitor samples TPS, tick-thread cycles, memory, handles, threads, online count and backlog, splits error-like feedback from other errors and gathers hook verification summaries. Action/monitor exceptions are caught as harness errors and the run continues. A crash flag is the death event, while “not respawned” is the remaining requested-kill map. Some kills may fail or target an already disconnected player, so that map is not a pure server-respawn defect count.

Linux chaos has a separate implementation, different action frequencies and mobs, different teleport heights/coordinates, global versus fixed home changes, cleanup every 300 seconds rather than 90, and different block workloads. It sends unpaced console commands through the ordinary Linux Server wrapper; high-frequency gametime probes do not get the Windows priority queue. Its quick-disconnect delay calls global `random.uniform` rather than the seeded chaos generator. These differences are visible source facts.

Most importantly, Linux chaos launches a separate `loadbot-linux-chaos` with `-chaos` and sends `rejoin <name>`. The imported full Go bot accepts `-control` and `reconnect <name>`, and has no `-chaos` flag. The claimed Linux bot source is therefore not reconstructable merely by cross-compiling the added Go main. The integration runner instead explicitly expects a different Linux build of the Windows control-capable bot.

Linux monitor stops if server or bot container dies, collects logs, crash_reports and sentry-native files, retains the run volume on crash/report, and otherwise deletes it. Its summary initially groups TPS using locally queued randomtick state (`rts0`), not the server's acknowledgment. It can break on bot exit without setting the server crash flag. Preserve `bots_exited`, measured duration and phase completion alongside crash.

## Applied versus queued regimes {#applied-versus-queued-regimes}

The later analytical scripts in the same import address one key measurement flaw. `metrics_linux.chaos` and `wf_chaos.analyze` parse actual “randomtickspeed has been updated” responses and compute both queued/applied counts or separate groupings. That is stronger evidence of workload application than the scheduler's intent log.

Their samples are still categorized by the regime at the interval endpoint; a ten/five-second interval can span several regimes. `metrics_linux.py`'s opening description says start-of-window while its function comment and implementation use end-of-window. The detailed dossier follows code, not that stale description. Window-specific time-in-regime accounting is useful, but time-of-day clocks and midnight behavior remain limitations.

`wf_chaos` aligns monotonic gametime samples to wall log times by median matching gametime values, then reports memory ranges and error kinds. Repeated counter values keep the first log match; dropped/duplicated answers and clock jumps can complicate that offset. Its cycle-derived process CPU sums only threads present in the final snapshot and uses zero as the missing-start value, unlike other helpers that omit newly created threads. Do not combine these estimators as identical measurements.

## Behavioral “verify” scans {#behavioral-verify-scans}

`VerifyScan` recognizes cumulative divergence/check counts for:

- Dimension player iteration and packet recipients.
- Active-player counts.
- Locator pair/no-op/table decisions and unexpected sends.
- Locator waypoint growth/update.
- Chunk publisher missed sends and non-tie ordering differences.

It retains the latest cumulative result per hook, representative raw summaries, and first/recent divergence details. An emitted summary with all zeros produces “clean”; no verify lines produces `None`, not an automatic pass. This avoids one false-confidence path.

However, clean means no recognized divergence in emitted instrumentation. It does not require a particular hook to appear, a positive number of checks, a nonzero exercise count, or all expected scenarios. Unknown verification text may become a raw summary without failing. Expected checks and deliberate negative controls are therefore required before claiming behavioral equivalence. Equal-distance reorder count is parsed but intentionally not included in order divergence, preserving the source's narrower equivalence boundary.

## Integration runner and parser {#integration-runner-and-parser}

Windows `intest.run` uses the endstone_test plugin's startup and player-join suites. Two bots normally join; a00 is granted operator permission, sends `/test`, `/test sender`, `/test broadcast`, then reconnects as operator and waits again. Linux builds a dedicated image from a specified plugin snapshot (`a1b4e89bb` in a local directory), installing pytest 9.1.1, Pillow 12.3.0 and Babel 2.18.0, and performs the same two-round protocol. The plugin source itself is outside this import; a comment about its pytest fixture fix is provenance intent, not proof the correct snapshot was installed.

Both parsers collect pytest session starts, summaries, FAILED/ERROR lines and failure sections. A “Name” log heuristically assigns subsequent sessions to a player's join. They report NO TESTS RAN if there are no sessions, FAIL for recognized failures/errors or missing summaries, otherwise PASS. They do not enforce an expected suite list, exact player count, minimum passed count, or successful contents of the player command probes. A completed session with zero passed and only skips/deselections can pass. They collect command output as evidence rather than assert its semantics.

The Python programs write verdict files but do not consistently return a failing process exit solely because the verdict is FAIL. Some shell workflows only inspect process rc. `wf_final.sh` is stronger: it explicitly requires JSON `verdict == PASS` before starting the final performance run. Other chains run an integration command and log rc without reading its verdict. A marker saying “done” or a zero harness exit must not be translated into all tests passed.

## What this supports {#what-this-supports}

The source demonstrates targeted attempt coverage across cache invalidation, disconnect cleanup, chunk publication, dimension transfer, lifecycle races and protocol recovery. It also shows why stress results are unsuitable as a clean speed ranking without work accounting. There is no execution here, no reproduction of reported tests, and no proof of absence of defects. Use these mechanisms to design a bounded test matrix with per-action acknowledgment, expected coverage, cancellation checks and explicit failure propagation.
