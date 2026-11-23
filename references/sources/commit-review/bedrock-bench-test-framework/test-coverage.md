<!-- retrieval: {"source_ids":["public:commit:8b9173691659e15cdd9dd2b4cf628081029d09cf"],"source_type":"public","date":"2026-10-12","topics":["concurrency","testing","performance","api","diagnosis","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="test-source-coverage-and-its-boundaries"></a>
# Test-source coverage and its boundaries {#test-source-coverage-and-its-boundaries}

This is an inventory of assertions read at ordinal 13, not a run report. The separate per-test source-line inventory is not included here. Parametrization expands execution counts; no collection was performed.

## `tests/fakes/test_fakes.py`: 26 test functions, 655 lines {#tests-fakes-testfakes-py-26-test-functions-655-lines}

- Seven-family process sessions check printed version, readiness, placeholder world creation, broadly advancing tick counter, socket login, view-distance clamp, teleport, available position parsing, Endstone child selection, zero stop exit and bot EOF.
- Nukkit language input verifies `eng` is sent before normal console commands.
- A boot crash checks process code 3 and collected report content.
- Idle clock stalling and explicit launcher-child discovery exercise independent branches.
- Every behavior script is parsed and required to carry a description. Seven bad-script examples reject unknown keys, wrong types, bad positions, invalid actions, invalid regex/anchor and inappropriate action keys.
- Bot selftest validates all event types against the schema; version JSON identifies module and protocol; usage failures map to 1; Go-duration examples parse.
- A TCP accept-and-close server drives all joins to fail with exit 2, stage `spawn`, zero joins, final `done` and schema validation.
- Three bots against fake BDS receive teleports and chunks, one dies/respawns, one is kicked, quit emits summaries and final counts, a four-chunk-radius stationary view contains 49 columns, and configured fake XUID appears.
- Rejected login is attributed to a02 at login; fail-on-decode exits 3 and emits `done`.
- Fetch is idempotent; prepared config has correct override categories/hash, equal defaults are omitted, behavior scripts copied, world initially absent and launch cwd/env correct.
- Reused directories and unknown variants fail rather than silently overwriting.
- Missing/truncated/garbage positions are unknown; explicit counted zero is empty.
- Supported chaos renderers and unsupported declarations are checked; only tick-speed confirmation is recognized.
- Throwaway entry-point registration appears then disappears after path/registry reset.
- Real BDS/Endstone/LeviLamina dialects read fake sample logs if installed; absence skips.
- Real driver arguments are accepted by the fake with `-version`; this validates argument syntax, not the behavior of each flag, because version returns before ordinary input validation/session execution.
- Workspace inputs resolve, scenario inheritance is honored, CPU sets expected disjoint, matrix IDs and schema copies match.
- A separate interpreter sees fake adapters and redirected root; the configured bot command prints version JSON.

Boundary: these tests establish requirements on the fake implementation and interface compatibility if executed. They do not certify real protocol behavior, complete control parity, authentic real-server log coverage or platform success. Some helpers use pipe readers, timing sleeps and daemon threads; no stress/concurrency execution evidence is present.

## `tests/integration/test_contamination.py`: 2 functions, 51 lines {#tests-integration-testcontamination-py-2-functions-51-lines}

One case waits until `alljoined` and burns a server CPU from outside owned process trees. It expects INVALID and a foreign-load reason. Another burns CPU before a matrix and expects ENV_GATE with no run directory. Both use the explicit strict machine profile. The second additionally needs `runner:run_matrix`.

Boundary: real CPU attribution would be exercised, but thresholds are host/timing dependent. Ordinary relaxed-profile fake runs do not cover this. Both cases are expected failures while their required runner entry points are absent.

## `tests/integration/test_death.py`: 5 functions, 75 lines {#tests-integration-testdeath-py-5-functions-75-lines}

Shared assertion: SERVER_FAILED, matching record exit code/status, gate-related reason and retained metrics.

- Crash after join: `died=True`, exit 3, crash file listed and copied report text present.
- Crash during boot: no ready mark and a crash directory.
- Nonzero stop: original rule fails server_alive although `died=False`.
- Hanging stop: shortened stop timeout, completion within a broad 120-second bound and nonzero server exit.
- Refused a02 login: joined 3, failed 1 and joined_all reason.

Boundary: these are the original policies. The last two stop cases are deliberately changed by later b25964a to OK plus `unclean_stop`. A subprocess exit or source assertion alone is not the reported overall benchmark status; the health evaluator interprets retained facts.

## `tests/integration/test_run_fake.py`: 14 functions, 225 lines {#tests-integration-testrunfake-py-14-functions-225-lines}

Good-run fixture drives fake BDS. Assertions cover:

1. OK status in run and metrics, zero exit, no reasons.
2. Complete raw/result/config files, no partial record, no crash folder.
3. Recorded hashes and bytes equal kept file contents.
4. Run, metrics and every bot event validate; every bot event has harness `rx_ns`.
5. Console log lines have monotonic-nanosecond and epoch-millisecond fields in order.
6. Server/version, ordered phase marks, all required milestones, four occupied spread cells and healthy joined/exit/decode facts.
7. Override categories.
8. Numeric steady TPS metrics exist, are labelled measured and lie in 18–21.
9. Probe counter is monotonic with at least ten observations, receipt no earlier than send.
10. `run.json` omits local workspace/home/cache paths and a sufficiently long hostname.
11. Reanalysis leaves metrics byte-identical and status unchanged.
12. Validation CLI accepts the record.
13. Five broken variants produce INVALID with the relevant spread, probe-monotonic, probe, decode or version gate, retaining metrics.
14. Six non-BDS fake families finish OK, retain four players, expected position-source family and correct banner.

Boundary: “measured” here denotes measurement of controlled fake data/processes. It cannot make synthetic chunks/bytes/RTT into real-server measurements. Privacy coverage is only the JSON record and specific known strings. Byte-identical reanalysis means deterministic computation from the same artifacts, not independent correctness. Run-one, analysis and validation dependencies control strict xfail.

## `tests/integration/test_runner_order.py`: 6 functions, 140 lines {#tests-integration-testrunnerorder-py-6-functions-140-lines}

Two fake arms × two repeats are expected to create four unique run IDs and directories under the matrix name. Order should be full/reduced then reduced/full; profile hash should remain identical. Dry-run should print that order and create nothing. Reporting must separate full/reduced declared fidelity and explain that reduced fidelity does less. Deliberately editing one copied profile hash must make reporting refuse; attempting to append repeats under swapped placement must refuse without new runs.

Boundary: these tests verify grouping and experiment bookkeeping from declared fake metadata. They cannot confirm actual server equivalence or feature completeness. The fixture has a matrix-wide runner dependency; report cases have an additional report dependency. The source claims a subprocess per run in its module docstring, but these six tests do not directly assert distinct process IDs.

## `tests/unit/test_adapters_contract.py`: 23 functions, 502 lines {#tests-unit-testadapterscontract-py-23-functions-502-lines}

Per-adapter tests check class attributes/protocol availability set, compatibility flags, variants, fixture dialects, optional role samples, ready-line disjointness, single-line commands, optional command snapshots, chaos declarations, unknown-position semantics and exercised-feature keys. Shared tests check dialect validation/splitting, tick-thread resolution/fallback/invalid rules, chaos rendering and unsupported errors, numeric coordinate formatting, default commands/player quoting, default feature path, crash-artifact mtime selection, invalid registry plugin rejection and unknown-server errors.

Boundary:

- A class passing validation does not imply successful fetch/install/launch.
- Recognizing some fixture lines is not an exhaustive parser correctness test.
- BDS/Endstone snapshots are absent at this commit, so snapshot checks skip.
- Missing per-role fixtures or chaos catalogue also skip; failed scenario loads are delegated to a different test module.
- Feature-file coverage checks that declared keys exist; it does not measure the feature's implementation.
- Required schema dependency can skip through the shared fixture when not installed.

## Capability inventory not fully exercised here {#capability-inventory-not-fully-exercised-here}

The source includes template-world preparation, config rewrite, reset-at-spawn clock, command loss, TPS dip, arbitrary delayed replies, player drop, command-triggered events, signal shutdown, automatic rejoin and several control operations. They are meaningful, read source, but the 76 target test definitions do not individually establish every permutation. Some have no direct assertion here; some have only a renderer or schema selftest.

Do not convert this capability list into a passing-test count. Later dedicated suites may exercise some behaviors, but their coverage must be credited to their own examined changes.
