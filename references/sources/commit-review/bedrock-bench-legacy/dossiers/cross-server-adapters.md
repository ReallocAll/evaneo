<!-- retrieval: {"source_ids":["public:commit:0a49c6914171a3d325adfca5bc50cf612ea4cb8e","public:commit:13f9df244044ed39ce62af70d3954f46de997983","public:commit:655e3e486185341520890621f65d9b69a9b6067d"],"source_type":"public","date":"2026-10-12","topics":["lifetime","concurrency","ffi","performance","diagnosis","documentation","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="cross-server-adapters-and-workload-equivalence"></a>
# Cross-server adapters and workload equivalence {#cross-server-adapters-and-workload-equivalence}

Primary source: initial import `0a49c6914171a3d325adfca5bc50cf612ea4cb8e`, all 28 paths under `legacy/custom-servers/`. Implementation, configuration and script bodies were read in full except one guarded credential line; the duplicate PNX world JSON was verified by identical Git blob. Nukkit references here are the recent benchmark adapter and configuration snapshot only. Old Nukkit implementation history is excluded and supplies no personal-style evidence.

## Adapter design {#adapter-design}

`scripts/cbench.py` gives each server a concrete adapter: executable/arguments, port, bot binary, readiness and tick-counter parsers, initial effects, command translation, unsupported chaos actions and main-thread strategy. Shared orchestration performs fresh-world setup, optional world-template copy, idle/loading/steady/chaos windows, CPU/memory sampling and summaries.

The child server starts suspended on Windows, receives CPU affinity and priority, then resumes, which avoids initialization using an unintended CPU placement. This is stronger than pinning only after startup. Java uses `jcmd Thread.print` to identify the named main thread; PHP/native choices use earliest creation time. Dragonfly is Go and can move goroutines between OS threads, so the comparison renderer explicitly labels its “main thread” result inapplicable. Its process CPU remains meaningful subject to measurement limits.

Adapters encode differences rather than making them disappear:

- PocketMine uses the protocol-1001 bot and `time query`/“Time is” response. The parsed value is not proven by this adapter to be a monotonic unwrapped tick counter. Translation retains only a small command subset. Waypoints, mobs, cleanup, dimension hopping, random tick speed, weather, block edits and ticking areas are omitted.
- Nukkit uses a protocol-2193 variant with fake XUID, a helper `gametime` command, finite long-duration effects and custom `fillnear` / `dim` commands. Random-tick gamerule capitalization is changed. Summon conversion uses a capitalized mob name at a player, dropping the original random coordinate offsets. Cleanup becomes `kill @e`, with potentially broader selector semantics than the source's non-player selector. These are substantive workload substitutions.
- PowerNukkitX also uses fake XUID. Its world setup rewrites all dimension seeds to 20261010. Most commands pass through, but loot spawning is removed and waypoints are omitted.
- Dragonfly uses its custom executable, no `status` command at the adapter level, and no waypoint/summon/cleanup/random-tick/ticking-area actions. Weather, selected blocks, dimensions and other player commands are handled by its helper console.

The chaos subclass removes unsupported actions from the schedule and records translated-away commands, but removing actions changes the RNG consumption order and thus subsequent choices too. A shared seed is not a matched executed workload. “Fewer command errors” is not intrinsically a stronger server when the adapter drops unsupported work.

Java diagnostics run ten stack dumps, heap info and a ten-second jstat sample. With `--diag`, the steady window includes that diagnostic work; it is not an untouched timing run. The stack-sample top-frame frequency is suggestive attribution from sparse samples, not a statistically complete CPU profile.

## Dragonfly helper implementation {#dragonfly-helper-implementation}

`dfbench/main.go` starts from Dragonfly's example server configuration, wraps listeners to timestamp connections, sets tick range 4 in all three worlds, subscribes stdout chat, then adds a stdin console.

Entity operations look up a handle and execute through `h.Do` inside a `world.Tx`. Teleport, effect changes, damage, game mode and block operations therefore use the library's world transaction rather than mutating a player from the console goroutine. Cross-dimension transfer removes an entity under its source transaction and launches destination `Do` asynchronously, avoiding a synchronous nested world transaction. That is a useful lifecycle/ownership pattern, but a destination failure after source removal is not handled explicitly here.

The console implements a bounded block palette, selected effects and game modes, dimension lookup, time/height inspection, and stop. Unknown dimensions fall back to overworld, malformed commands often return without a structured failure response, and requested selector semantics are not generally implemented. `time` queues a world operation and waits ten seconds; `height` waits twenty. The buffered one-value completion channels prevent a late world callback from blocking after the console's timeout. `stop` closes the server and exits the process.

Its module uses `github.com/df-mc/dragonfly v0.0.0` replaced by `../../dl/dragonfly/src`. That source and the runtime `config.toml` are absent from the imported tree. The 126-line go.sum and its module/version pairs were inspected as dependency integrity declarations, not runtime validation or independent evidence of the replaced Dragonfly revision. The gophertunnel v1.62.0 checksum does not identify the local Dragonfly checkout.

## Pre-generation as a separate experimental condition {#pre-generation-as-a-separate-experimental-condition}

`pregen.py` starts Nukkit/PNX, submits a helper `pregen radius inflight` command, waits up to an hour for a PREGEN DONE line, stops, and copies a template only on that signal. The plugin implementing those custom commands is not included in this legacy source. Matching a success log does not verify coverage of all chunks.

`pnx_botpregen.py` instead visits every cell with a small bot group and raised view distance 12, allowing the real player-driven generation pipeline to work. A first pass visits 121 cells, a fill pass 100. Each group waits for a minimum dwell plus several low-delivery samples, or 240 seconds. It resets view distance to 10 in finally and saves the server world as a template. `ok=true` is set after completing the procedure and copying the world, without a per-cell absolute coverage or terrain-content check. This can create a valid procedural template while still leaving incomplete coverage.

The shell chain revisions preserve the investigation:

- `chain2.sh` tries command-based PNX pre-generation.
- `chain3.sh` switches to ten bots touring cells.
- `chain4.sh` adds a second fill pass.
- `chain5.sh` runs the PNX template with Java diagnostics.

Each then attempts to transplant PNX's LevelDB database into a Dragonfly world using a Dragonfly level.dat. Before benchmarking it probes three surface locations and rejects explicit load errors/panics or all-air output. That is a coarse compatibility smoke check. `dfprobe.py` later probes the centers of all 100 cells and classifies exactly Y=-61 grass as flat fallback. A center surface probe can reveal fallback terrain, but it cannot prove all surrounding view chunks decode correctly or represent identical worlds.

`firstrun.py` starts a server at low priority, optionally sends pre-start input, waits for readiness or timeout, sends diagnostics, and attempts a graceful stop with child cleanup on failure. It continues after a readiness timeout. `killrun.py` matches an exact tag token plus a cbench command-line substring to kill a harness and its children; this limits but does not cryptographically establish ownership. No such process action was executed in this review.

## Configuration and security/measurement scope {#configuration-and-security-measurement-scope}

The Nukkit, PocketMine and PNX configuration snapshots were read, retaining a redaction on one Nukkit credential line. Important realized differences include:

- Nukkit: compression level 5; async workers auto; per-tick sending 4; chunk cache off; chunk tick radius 4; generation/population queues 8; native LevelDB disabled with 80 MB cache; auto tick-rate reduction off.
- PocketMine: compression level 6; async compression off; async workers auto; per-tick sending 4; tick radius 4; random blocks per subchunk 3; population queue 32; autosave 6000 ticks. A delayed RakLimit plugin raises per-IP packet limits to PHP_INT_MAX so many local clients are not rejected as one abusive IP. This is a benchmark accommodation and unsuitable as generic public-server hardening advice.
- PNX: view 10, tick radius 4, base TPS 20, level thread off, auto tick-rate off; generation queue 8, send allowance 32/tick, save generated chunks on, all worker threads by default; zlib provider 3 at level 4, encryption on, RakNet limit one million with finer per-session limits still enabled. Simulation features including mobs, weather, liquid flow, random ticks and hunger are enabled. Difficulty is 1 versus the other snapshots' 2.
- Every snapshot's offline login and permissive binding belong to a localhost/isolated experiment. They must not be offered as secure production defaults.
- PocketMine auto-report sends code/settings on crash and its updater is on. Levi's separate snapshot also enables crash upload. Launching these historical configurations can cause external traffic; merely reviewing them does not authorize running them.

The static JSON's original random seed is not the seed actually used by PNX preparation, which rewrites it. Distinguish supplied configuration from effective configuration.

## Published comparison construction {#published-comparison-construction}

`endstone_ref.py` combines one performance run, the first five minutes of a separate chaos run, and memory from that chaos run. `compare.py` places those values beside custom-server steady-end memory and other results; labels partially expose this mismatch. It hardcodes “no” crash and a release name for the reference, and estimates reference CPU ms/tick using 20 TPS. Its “view never filled” threshold is a heuristic of median unique chunks below 100 rather than a per-server complete-view definition.

`csummary.py` stops parsing bot view/join samples at “jitter on,” preventing chaos from overwriting steady view accounting. It records failures, capped settle, process CPU, sampled memory peaks, omitted actions and unsupported commands. This is valuable context, but script output shape consistency does not make server feature sets, terrain generation, client protocol, storage format or applied work equivalent.

Use the source to plan fair-comparison disclosures and independent workload validation. Do not infer an overall winner from matching nominal view/tick settings or from an adapter's successful translation.
