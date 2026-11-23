<!-- retrieval: {"source_ids":["public:commit:4c53cc0e0d0451697769c0ae37a2848adb50fe47"],"source_type":"public","date":"2026-07-11","topics":["concurrency","testing","performance","recovery","api","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="spark02-viewer-compatibility-and-accurate-measurement-are-separate-obligations"></a>
# Viewer compatibility and accurate measurement are separate obligations {#spark02-viewer-compatibility-and-accurate-measurement-are-separate-obligations}

## Representation and explicit constraints {#representation-and-explicit-constraints}

The profiler's FrameKey is module ID plus relative virtual address; runtime address is retained for symbolization but excluded from equality/hash. Module strings are interned. CallTree logs captured leaf→root frames in reverse, accumulating counts per time window. The serializer gathers unique keys, resolves them once and flattens children before parents into references. This separates aggregation identity from human names and avoids repeatedly resolving each sample.

Linux uses dladdr dynamic symbols and demangles names, falling back to module basename plus hexadecimal RVA. The comment explicitly avoids cpptrace/libdwarf symbolization on a large stripped BDS binary because that backend can fault. Windows uses cpptrace/PDB resolution. “Can fault” is a source claim; this review did not reproduce it. The header comment still describes DWARF resolution while Linux implementation uses dladdr, an example of documentation lag.

The two proto schemas are declared vendored verbatim from lucko/spark and used as a protoc decoding oracle, not compiled into the build. Field definitions were read. A tiny write-only ProtoWriter implements varints, sign extension, fixed64 doubles, length-delimited submessages and packed scalar arrays. The source explicitly says a fixed small write-only schema is used to avoid a protobuf runtime dependency. Its statement that protoc validation occurred is not accompanied by a captured run transcript or result fixture in the target tree, so it remains author-reported.

## Wire-level choices {#wire-level-choices}

The serializer aligns all node times to an ordered union of sample windows and tick-stat windows, emitting a WindowStatistics record even for windows with no samples. Counts are multiplied by configured interval to estimate milliseconds. This assumes sampling cadence represents time; capture overhead, skipped sleeps and failed captures are not separately encoded. Post-order flattening and child references are appropriate protocol mechanisms, but only a decoder/viewer round-trip could validate complete compatibility.

Several fields are deliberately adapted to viewer expectations: native RSS is mapped to the “heap used” widget; VmSize becomes its denominator; empty-but-present Java and swap messages prevent viewer assumptions about missing nested data. Source comments explain those choices. They are compatibility mappings, not evidence BDS has a JVM heap or actual Java runtime.

## Measurement qualifications {#measurement-qualifications}

- One Endstone average TPS value is copied into last1m/5m/15m. Those are not independently measured rolling windows.
- Average MSPT is copied into mean/min/median, and current MSPT into max/p95. The labels overstate the available sample statistics if read literally.
- Window `mspt_median` is computed as sum/tick count, which is a mean. Window TPS is simply tick count for a nominal1-second window; partial windows still encode duration1000ms.
- CPU process/system utilization is captured over the profiling period, then copied into the viewer's1m/15m fields. Process CPU is normalized by total logical CPU capacity and clamped to0..1. It is not “percent of one core.”
- `/proc` read failure often returns zero/default data; captureCpuSnapshot sets valid=true regardless of successful source reads. Unknown and zero are not always distinguished.
- Profile end_time is recorded during export, after sampling stopped; export delay can alter reported duration relative to actual sampling.
- Only the server thread is targeted. Parsed `--thread` values are stored but not applied. Allocation is explicitly rejected; other stored compatibility options do not implement additional engines.

These are source-grounded limitations, not measured discrepancies. The portable lesson is to label proxy values honestly and keep widget accommodation distinct from statistical truth.

## Export and recovery paths {#export-and-recovery-paths}

The network helper writes gzipped bytes to a unique temporary file, invokes system curl with shell-quoted arguments, captures stderr, deletes temp files and extracts a content key from the Location header. Its explicit reason for system curl is avoiding another TLS stack inside the host process. Partial writes fail cleanly. However it does not set a network/connect timeout or require an HTTP success status, and a Location header is its success criterion. Blocking popen/pclose can stall shutdown through the export-thread join.

A local save path exists. Manual stop reads only that stop command's --save-to-file flag; start-time save preference is used for auto timeout but is not combined with manual stop's flag. Thus start-with-save then ordinary manual stop can upload instead. This is a concrete scope/privacy/recovery issue to test. The profile contains creator name, plugin metadata, server/version, world/entity totals and host data, so export mode should be explicit to the operator.

On upload failure the message says retry with --save-to-file, but the profiler is already stopped. The command stop path refuses when not running, and no retained-profile retry command exists. The recommendation is not directly actionable through that same command flow; a new run is required unless another recovery path is added. Local plugin save writes raw protobuf while the offline self-test writes a gzipped .sparkprofile. This review does not assume either representation is accepted by the viewer without validation.

## Test tool and limits {#test-tool-and-limits}

The offline selftest creates a worker with nested hot functions and sleeping phases, generates synthetic ticks, writes raw+compressed outputs and optionally uploads. It has no assertions on expected frame percentages, schema decode or browser rendering. Its --probe path now supplies only module/RVA and zero raw addresses to a Linux resolver that relies on runtime dladdr, so it falls back rather than reproducing the old file-based symbolization path. No tool was built/run, and --upload was never invoked.

Future acceptance should separately verify protobuf decode, viewer rendering, statistic meanings, empty profiles, filtered/partial windows, two consecutive runs, offline save, slow/failed upload, shutdown during upload and honoring start-time save intent. This source is useful for export-format review and profiling data-model design; it does not support a claim of accurate full-system performance diagnosis.

## Sources {#sources}

The [Spark source index](../repositories/spark-source-index.md) and [public implementation commit](https://github.com/EndstoneMC/spark/commit/4c53cc0e0d0451697769c0ae37a2848adb50fe47) cover ProtoWriter, sampler data, symbolization, statistics, selftest and plugin/bytebin export. The original local patch offsets are not public source line numbers.
