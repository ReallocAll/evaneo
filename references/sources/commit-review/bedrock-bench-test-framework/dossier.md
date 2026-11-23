<!-- retrieval: {"source_ids":["public:commit:8b9173691659e15cdd9dd2b4cf628081029d09cf"],"source_type":"public","date":"2026-10-12","topics":["lifetime","concurrency","testing","build","performance","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="fake-systems-as-executable-contracts-with-an-explicit-fidelity-ceiling"></a>
# Fake systems as executable contracts, with an explicit fidelity ceiling {#fake-systems-as-executable-contracts-with-an-explicit-fidelity-ceiling}

## 1. Source identity and evidentiary status {#1-source-identity-and-evidentiary-status}

Target: `8b9173691659e15cdd9dd2b4cf628081029d09cf`, “Add the fake servers and bots, the adapter contract test and the integration tests,” authored and committed 2026-10-12 14:20:04 UTC. Parent: `1259ada6931a365c000258f73f64655703700096`. Repository: EndstoneMC/bedrock-bench. Public provenance: [commit](https://github.com/EndstoneMC/bedrock-bench/commit/8b9173691659e15cdd9dd2b4cf628081029d09cf).

Vincent authored the commit, and its message explicitly credits Claude Opus 5.5 as coauthor. The message gives no substantive rationale beyond its title. No review, CI or execution result accompanies this source.

The commit adds fake systems, adapter contracts and test assertions. The source is reviewed statically; no tests or benchmark runtime were executed.

The 76 `test_*` function definitions are a static count, not collected parametrizations, tests executed, tests passed or independent engineering principles.

## 2. Problem and design placement {#2-problem-and-design-placement}

The README states the practical objective: drive `bbench run-one` quickly without downloading Minecraft, accepting its EULA or requiring the real Go load bot. The fake server and bot are standard-library Python. The adapter and workspace helper depend on the actual benchmark package, psutil and pytest. The substitute programs are launched as subprocesses instead of monkeypatching away the process and pipe boundaries.

The prior package already declares a `ServerAdapter` boundary: fetch, prepare a fresh working directory with categorized overrides, derive a launch specification, identify the measured process, parse console lines, render commands and collect crash files. Metrics and phases should consume the interface rather than recognizing server names. The fake adapter intentionally occupies that same boundary.

This division supports two different kinds of evidence:

1. Static/unit contracts can check a dialect or command renderer against samples without launching a game server.
2. A running fake can exercise actual OS processes, stdout/stdin plumbing, registration, temporary workspaces, timing, deliberate faults and resulting artifact assembly.

Neither makes the fake an implementation of game physics, the Bedrock protocol, generation, networking load or server performance. The lower cost comes from reducing those concerns, not from reproducing them cheaply.

### Historical implementation state {#historical-implementation-state}

At the target commit, `src/bedrock_bench/runner.py`, `phases.py` and `results.py` are absent from the Git tree. `cli.py` already names their future entry points. `resolve_entry` raises `NotImplementedError` only when the addressed module/function is missing; dependency-import failures inside an existing module propagate. `needs()` catches that specific missing-command signal and applies `pytest.mark.xfail(..., strict=True)`.

Consequently, these integration tests are submitted expectations awaiting implementation. An expected failure can cover the whole test or fixture while the required entry point is absent; it does not establish how far execution got. Strictness prevents an unexpected pass from disappearing as success, but does not distinguish one expected failure cause from every other failure inside that test. Entry-point existence also does not prove feature completeness.

Later ordinal 18 (`25d29132ba7ad9335d3ba6599a9fbf2180f48327`) implements the environment override promised here: parse `BBENCH_BOT_CMD` as a nonempty JSON string array, retain the scenario's normal bot arguments, give the replacement no fabricated executable hash/version, and append `bot_override` to nonstandard provenance. Only these relevant later sections were read here; broader lifecycle coverage belongs to the main history dossier.

## 3. Workspace, isolation and plugin boundary {#3-workspace-isolation-and-plugin-boundary}

`tests/fakes/bench.py` provides a temporary environment rather than requiring the real project checkout to be mutated:

- Copies the schemas, fake feature files and short scenarios under a per-test root.
- Writes a throwaway `.dist-info` with a `bedrock_bench.adapters` entry point for `fakes.fake_adapter`, exercising the third-party registration route.
- Makes that metadata and `tests/` available through `PYTHONPATH`; uses `BBENCH_ROOT` and `BBENCH_CACHE` to redirect name resolution and caches.
- Uses a JSON argv prefix for the substitute bot rather than a shell string.
- Divides the available affinity set roughly in half for server versus bots; pins the harness with bots; writes machine and matrix TOML through a deliberately small serializer.
- Reduces phase durations to seconds, disables matrix cooldown and invalid-run retries, and normally loosens contamination gates so a developer workstation does not invalidate an ordinary fake smoke run.

The distinction between relaxed and strict gates is explicit. Foreign-core thresholds are 1024 in the ordinary profile; strict tests restore 0.25 mean global/server-set foreign cores, 1.5 peak and 0.85 bot CPU fraction, with a short idle check. A green ordinary fake test would therefore say little about default contamination-gate sensitivity. Separate contamination cases start a CPU-burning subprocess owned by the test, outside the measured harness/server/bot trees.

`Run` exposes exit status and optional artifact directory, and reports stdout/stderr tails on assertion failure. `Background` redirects both outputs to files, avoiding a full pipe when the test waits before reading. Its timeout path kills recursively discovered children and the harness. `wait_for_mark` polls `run.partial.json`, tolerating transient file/read/JSON errors until a mark, process exit or deadline.

Important limits:

- `free_port()` probes a port and adjacent port for TCP and UDP, then releases them. This checks immediate availability, not reservation; another process can still bind before launch.
- With only one available CPU, `FakeBench.create` reuses the same set for bots and server, while the workspace self-test expects disjoint sets. This is a source-visible constrained-host limitation, not a locally observed failure.
- The ordinary foreground `bbench()` timeout relies on `subprocess.run` and does not implement `Background.kill`'s recursive cleanup. An inherited-pipe/child-process failure needs separate scrutiny; the source does not establish whole-tree timeout cleanup on that route.
- The helper intentionally inherits other host environment values, including an existing `PYTHONPATH`. It is test-workspace isolation, not a hermetic sandbox.

Ordinal 19 (`6e7194282641d0105cfcb7470858fdb968a4a705`) later changes port selection from an ephemeral allocation to random candidates in 20000–49149, avoiding Windows dynamic-range reservations according to its source comment. It doubles the attempts but still does not hold the sockets until launch.

## 4. Fake adapter: exercise invariants without a download {#4-fake-adapter-exercise-invariants-without-a-download}

`fake_adapter.py` models the real lifecycle:

- `fetch` hashes relative paths plus contents of the fake-server script and all behavior scripts, installs through cache staging and returns an artifact with source `build`, not a release/download claim.
- `prepare` rejects a nonempty working directory, writes `server.properties`, returns its SHA-256 and records only values changed from the fake defaults.
- Overrides distinguish harness choices such as port, server name and offline login from parity choices such as seed, view distance, player limit, gamemode and CSG.
- A fresh world is declared before the fake creates its files. A template scenario requires `ctx.template`, copies it, hashes the template contents and marks the world nonfresh/custom.
- `launch` returns argv, cwd, environment-removal names and optional first-start language input. It uses the base Python interpreter when available so a Windows virtual-environment launcher does not accidentally introduce a second process layer.
- Endstone intentionally has an extra launcher process. `server_process` discovers a descendant whose argv contains `--role server`, with a deadline and launcher-liveness check.
- `tick_thread_rule` is `first_created`; `crash_paths` is `crash_reports`; facts identify the fake family, default allocator and configured CSG.

The source records the fake configuration correctly for its own model. It does not validate a real server's defaults, deployment archive, EULA route, binary authenticity or child-executable identification. Matching a fake role argument is useful for process-tree plumbing but weaker than matching a real executable identity.

### Position semantics {#position-semantics}

Three families use multiline `querytarget` JSON; PocketMine and Dragonfly use a counted `POS` block; Nukkit and PowerNukkitX return no server position command, selecting bot observations instead.

The adapters return `None` for absent, truncated or unparsable output. A complete `Positions of 0 players:` block returns `[]`. That distinction matters: missing observation must not become a measured empty world. Unit tests explicitly encode it.

The JSON parser bracket-matches a controlled fake transcript before decoding; it is not a general JSON-stream tokenizer. The counted-line parser requires the number of recognized rows to equal the announced count. Tested invalid examples are narrow, so robustness against arbitrary console text, adversarial player names or numerical edge cases is not established.

### Chaos rendering {#chaos-rendering}

Supported renderers cover kick, kill, gamemode, weather, list, random tick speed and far teleport. Summon, cleanup, dimensions, block operations, ticking areas, waypoints and stacks are explicitly unsupported because the fake does not simulate them. `applied()` recognizes only the randomtickspeed confirmation. A command renderer or confirmation line does not imply the fake models the downstream game workload: effects, weather and gamemode largely produce response text.

## 5. Console family fidelity {#5-console-family-fidelity}

Seven distinct families make parser variations explicit:

- BDS: dated bracket prefix, bare continuation lines, `Server started.`, `time query gametime`, multiline `querytarget`.
- Endstone: time-only bracket prefix on every line, WARNING/CRITICAL levels, its own version banner, and a child server under a launcher.
- LeviLamina: millisecond time, three-letter levels plus preloader aliases, logger names, `Server started in (...)` and a composite BDS/LeviLamina version banner.
- PocketMine: server-thread/logger prefix, `Done (...)`, helper `gametime` and `positions`, player join broadcasts.
- Nukkit: padded log level, first-start `eng` answer, helper gametime and bot positions.
- PowerNukkitX: thread-name prefix, no language prompt, vanilla gametime and bot positions.
- Dragonfly: two prefix styles, unprefixed chat joins, helper commands and panic-like crash output.

The BDS and LeviLamina fake transport notices deliberately appear at error level but should be benign. The adapter contract differentiates canonical severity from known harmless text rather than treating every error-labelled line as a failed run.

The fake output generator and fake dialect regexes share `Family` definitions. This is a sensible way to keep the test system internally coherent, but is a common-source oracle: compatible mistakes in both can pass. `test_real_adapter_reads_the_fake_family` supplies a partially independent check by feeding generated logs to the real BDS, Endstone and LeviLamina adapters, including readiness, version, ticks, player entry, benign banner and positions. It skips unavailable adapters. At ordinal 13 only BDS/Endstone real adapter implementations are present; LeviLamina is added later. The other fake families have no equivalent real-adapter cross-check in this test.

The generic contract test also reads checked-in real log fixtures rather than only fake samples. It checks that important patterns match some fixture data and that encountered raw levels have mappings. These are examples, not exhaustive acceptance/rejection tests across releases, localizations, line fragmentation or logging modes.

## 6. Scripted server and failure lifecycle {#6-scripted-server-and-failure-lifecycle}

`fake_server.py` maintains a main tick loop, a console-reader thread, an accept thread and a reader per peer. Reader threads put input on queues; the main loop interprets commands, mutates players, fires events and processes timers. Output for a response is assembled together and flushed. The listener is localhost IPv4 TCP, and peers exchange one JSON object per line.

After optional language input and a configurable boot delay, the fake writes a placeholder world directory and `level.dat`, binds its socket, emits readiness and begins ticking. It increments a counter, optionally busy-spins for `tick_cost_ms`, and sleeps to a target TPS. If far behind, it abandons a half-second backlog rather than emitting a large catch-up burst. A “stall without players” mode keeps the loop alive but stops the tick counter; “reset at first spawn” resets it. Both make clock assumptions testable without claiming those are valid real-server counters.

Scripts configure delays, rates, refused players, command dropping, missing/garbled positions, wrong banners, stop behavior and timed faults. Events anchor to start, ready, first spawn, all spawn attempts completed, or the first matching console command. `all_spawned` counts rejected names as completed attempts, letting post-join failure scripts fire even if not every player joined.

The 12 supplied variants are:

- `crash-at-boot`: crash after 0.2 s during a 1 s boot.
- `crash-after-join`: crash 3.5 s after all spawn attempts completed.
- `decode-error`: send a synthetic undecodable-packet indicator to a01 after 0.5 s.
- `dip-on-join`: target 12 TPS for two seconds from first spawn, then recover to 20.
- `drop-commands`: silently lose every third non-probe command.
- `exit-nonzero`: return 1 after an ordinary stop.
- `hang-on-stop`: acknowledge stop but remain alive.
- `positions-truncated`: return only an incomplete position block.
- `probe-silent-after-join`: suppress probe answers for 600 s starting two seconds after all attempts.
- `reject-join`: refuse a02's login.
- `tick-stalls-idle`: stop the tick counter when nobody is spawned.
- `wrong-version`: print `0.0.0-other`.

Unknown top-level keys, incorrect top-level value kinds, unsupported tick/position modes, invalid event actions/anchors/regexes and unknown event fields are rejected. The validator does not fully type-check each action-specific payload. For example, `tps.value` is later converted to float by the executor. Validation is sufficient for the shipped scripts and their tested invalid examples; it is not a complete schema for arbitrary input.

Crash writes a timestamp/PID report with family, reason and tick, prints the family crash text, and returns the specified exit code. Normal stop closes sockets, waits a configured delay, optionally rewrites config, prints quit output and returns the configured code. A hung server stops processing console/network queues and ticks, while event/timer handling and the maximum-lifetime check remain in the loop. EOF on stdin requests stop when the loop is able to consume it.

Both programs terminate with `os._exit` after flushing stdout to avoid interpreter-finalization problems from daemon stdin threads. The server has a default 900-second maximum lifetime, but this is not comprehensive protection against every blocking operation. `Peer.send` uses blocking `sendall`; the simple JSON transport is not engineered as a hostile-peer implementation.

## 7. Fake bot: transport-compatible events versus modeled measurements {#7-fake-bot-transport-compatible-events-versus-modeled-measurements}

The fake bot accepts the real driver's ordinary argument names and Go-style duration/boolean spellings. It emits version/build JSON identifying itself as fake. A selftest emits one of each expected event and validates those records against the bot-event schema.

Each bot has identity, join state, retry/deadline, connection, session number, position/view, chunk set and counters. Socket readers attach their socket identity to queued messages; the main loop discards messages from stale connections. Spawn and connection-closed events distinguish login/spawn failure from a post-join drop. Optional retry/rejoin and death/respawn paths permit lifecycle tests. Graceful quit closes online bots, emits `left`, summaries for bots that ever joined, final stat/packet events and `done`. The separate exit codes are usage 1, zero successful joins 2, decode-fail mode 3 and normal completion 0.

The data plane is intentionally modeled:

- Chunk delivery consumes a floating rate budget supplied in the fake server's spawn response. It fills nearby missing disc cells first; no actual LevelChunk is transmitted.
- A CSG-on fake delivers a disc at half the radius. This provides a controlled difference, not a model of real client-side generation.
- A requested radius is clamped to fake view distance; the server chooses CSG from its config and does not negotiate the client request.
- Movement advances a local circle and periodically reports coordinates to the fake server. There is no authoritative collision, physics or correction application.
- Packet mix uses configured per-second rates and fixed typical byte sizes. TX packets are estimated as 20 per online bot-second and 80 bytes each.
- RTT emits fixed 2.0/8.0/9.5 ms percentiles/max, with synthetic sample counts. It does not send latency probes.
- The decode-error event is triggered by an ordinary valid JSON `garbage` instruction, not a malformed Bedrock packet or a decoder failure.
- The world is placeholder content; no generation, storage-engine durability, mob AI or game simulation happens.

Thus the harness can validate how it consumes, timestamps, aggregates and classifies these records, but the resulting “measured” availability label is scoped to fake inputs and elapsed fake-process behavior. It is not evidence for real throughput, bytes, RTT, CSG effectiveness or parity.

### Concrete control gaps relative to the real bot {#concrete-control-gaps-relative-to-the-real-bot}

The README's “same stdin protocol” description is broader than the implementation:

- Real `bots/core/control.go` accepts bot name or index `i`; the fake `_control` only looks up a bot name.
- Real reconnect can close a live session and accepts `delay_ms`, default 3000. The fake only schedules an already-offline bot immediately.
- Real radius can target one bot or all online bots. The fake requires a named online bot; the fake server ignores the `radius` operation.
- The fake stores/toggles a jitter flag, but the simulation never consumes it.
- The real parser rejects unknown JSON fields and invalid control values; the fake parser passes arbitrary dictionary fields through to a permissive dispatcher.
- `loadscreen` is accepted as a flag without a corresponding loading-screen interaction.

These are static observations from both implementations, not executed failures. The 013 integration scenario is steady, short and stationary, so it does not exercise those deeper chaos behaviors. A passing fake suite cannot be promoted to full real-bot protocol/control parity. A change involving these operations needs direct real-bot contract tests or a more faithful fake.

## 8. Evidence preservation and outcome classification {#8-evidence-preservation-and-outcome-classification}

The intended good run keeps compressed console, command and bot logs; probe, thread, tick, process and machine series; copied config; `run.json`; and `metrics.json`. It replaces the partial record and excludes a crash directory on the happy path. Tests require file hashes and byte lengths, schema validity, harness arrival timestamps, monotonic console timestamps, phase marks, spread counts, version matching and categorized overrides.

`analyze` is expected to regenerate metrics byte-for-byte from artifacts; `validate` is expected to accept the result. This tests deterministic downstream analysis for the same record, not truth of the synthetic inputs or bit-identical timing across independent executions. Privacy assertions prohibit the workspace/cache/home paths and hostname in `run.json`; they do not scan every output artifact or prove comprehensive anonymization.

Invalid cases attach gate-specific reasons for missing/truncated spread, stalled ticks, missing probes, decode errors and wrong versions. Failed-server cases retain metrics and crash evidence instead of dropping the run. The source treats absence of evidence and actual server outcomes as separate categories, although final status precedence depends on the health implementation.

The initial death tests classify boot/mid-run crash, failed join, nonzero exit after stop and hanging stop as `server_failed`, with exit code 4. That is historical policy, not the final rule.

### Relevant correction and reversal {#relevant-correction-and-reversal}

Ordinal 19 prevents a missing spread observation after a crash from adding a spread failure when the run had settled but had no spread source. This protects failure attribution: a dead server should not accidentally become mere invalid instrumentation because an observation could no longer be made.

Later [b25964a68bdffe0acbd77dd2df9bbb02420b78ea](https://github.com/EndstoneMC/bedrock-bench/commit/b25964a68bdffe0acbd77dd2df9bbb02420b78ea) explicitly distinguishes death before teardown from a bad stop after the measured windows. The latter stays OK with `unclean_stop`, the stop timeout becomes 10 seconds, analysis version changes to 3, report text explains the flag, and the two affected integration tests change accordingly. This is an explicit reinterpretation of what a benchmark outcome should mean, not merely relaxed test timing.

[5695726b49a1e2d8440c874f55e5ae767b7dd82e](https://github.com/EndstoneMC/bedrock-bench/commit/5695726b49a1e2d8440c874f55e5ae767b7dd82e) then ignores persisted old `server_alive: exit code ...` reasons during recomputation so old records can acquire the new rule. The preceding change already recognizes the old “still running ... killed” reason. The retained fact of a death before teardown remains a failure and must not turn into the stop-only flag.

Portable conclusion: if outcome rules evolve, update tests, report wording, analysis version and compatibility with stored reasons together. Do not silently rewrite history as though the current rule was always in force.

## 9. Generic adapter contract: what is enforced and what is optional {#9-generic-adapter-contract-what-is-enforced-and-what-is-optional}

The 502-line unit module applies a common check to every currently registered real adapter and all seven fake adapters:

- Concrete class and class-attribute validation, recognized bot protocol, well-formed dialect and unique allowlisted compatibility flags.
- Known variants construct under at least one runtime; an unknown variant is rejected.
- Prefix, ready/version/player/tick samples match; all fixture raw severity labels have mappings; ready text cannot also parse as tick/player entry.
- Commands are nonempty, trimmed, single-line and preserve expected player/coordinates.
- Known chaos actions are rendered or explicitly marked unsupported.
- Empty position observation is `None`.
- Feature declarations cover scenario-exercised keys for every pinned version or declared range.

Shared tests cover named-group and newline validation, unknown severity as unknown, unambiguous tick-thread rules, unsupported-action errors, coordinate formatting, player quoting, default feature paths, crash mtime cutoff, invalid plugin rejection and unknown server configuration errors.

Not every declared protection is mandatory at this point:

- Command snapshot tests skip absent snapshots; neither BDS nor Endstone snapshot exists in the target tree.
- Per-role TOML samples skip when missing.
- Chaos catalogue coverage skips when the catalogue is absent.
- The schema fixture uses `pytest.importorskip("jsonschema")`; the dependency is in the dev group but schema tests can skip when it is unavailable.
- Scenario loading errors are skipped inside this coverage helper, with a comment delegating validity to separate config tests.
- “Protocol has a bot build” is a set membership check for 2193/1001, not verification that a usable executable exists.

These are incremental scaffolding choices. They need explicit accounting before claiming comprehensive contract coverage.

## 10. Reuse in engineering work {#10-reuse-in-engineering-work}

Use this source when:

1. Adding an external-process adapter: reuse the shared lifecycle boundary and add independent sample logs plus process-tree cases before trying expensive real runs.
2. Designing a harness: put reproducible faults behind the same artifact/event interfaces so failures remain inspectable results.
3. Debugging invalid benchmark outcomes: distinguish missing observation, harness error, server death, refused work and post-measurement stop behavior.
4. Testing plugin systems: register through the real package-discovery route and verify registry refresh/removal, not only direct class instantiation.
5. Testing reporting fairness: use explicitly synthetic feature declarations to verify separate report groups without pretending to measure game parity.
6. Evolving result schemas or health rules: retain raw evidence, deterministic recomputation and versioned interpretation.

Counterweights:

- Shared fake producer/parser definitions reduce drift while reducing independence; pair them with authentic captured fixtures.
- Fast simulation reduces cost while omitting transport, physics, real load and much control semantics.
- Strict xfail is useful for staged development but cannot be reported as a pass; missing snapshots and optional schemas must stay visible.
- Timeouts and process cleanup must be checked along every execution route, not inferred from one helper.
- A single coauthored change is evidence of this repository's submitted design, not an exclusive, permanent personal preference.

## 11. Remaining limits and stopping condition {#11-remaining-limits-and-stopping-condition}

All meaningful target source and message content is covered. No target files are deferred. Related bot, lifecycle, metrics, native-adapter, and later-history details are covered by neighboring review dossiers; their claims remain historical source analysis, not new runtime verification.

No pytest, benchmark, fake server, fake bot, external binary, package import, dependency install or game-server execution was performed. No runtime results were synthesized. Independent real-server log authenticity, full platform behavior, complete later changes to every fake path, and live upstream CI are not established here. No need to execute was inferred from source-review authorization.
