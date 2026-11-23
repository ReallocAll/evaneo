<!-- retrieval: {"source_ids":["public:commit:4c53cc0e0d0451697769c0ae37a2848adb50fe47"],"source_type":"public","date":"2026-07-11","topics":["lifetime","concurrency","ffi","testing","build","performance","documentation","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="spark01-native-sampling-needs-a-lifecycle-proof-not-only-background-threads"></a>
# Native sampling needs a lifecycle proof, not only background threads {#spark01-native-sampling-needs-a-lifecycle-proof-not-only-background-threads}

## Source and objective {#source-and-objective}

The initial `EndstoneMC/spark` commit `4c53cc0e0d0451697769c0ae37a2848adb50fe47` adds the entire native profiler on July11,2026. All 3,861 patch lines were read in bounded sections, including commands, capture, aggregation, serialization, networking, docs and self-test. Three subsequent reviewed commits change wording, Conan recipe format and license, not the runtime core. Git attributes the initial commit to Vincent; source explicitly credits lucko/spark for schema/protocol/viewer. No AI attribution appears in the four target messages. Neither lack of a trailer nor the initial-commit shape establishes how code was produced.

Goal stated by README: sample native BDS work beyond plugin callbacks and visualize it in the existing spark viewer. The independent `spark_core` contains no Endstone dependency. Plugin code obtains server-thread ID, passes tick durations, gathers metadata on the main thread and delegates CPU-intensive export. This is a useful decomposition; it is not proof of safety or coverage of all BDS work. Only one target thread is actually sampled, despite accepting thread-related option storage.

## Capture and aggregation design {#capture-and-aggregation-design}

Linux capture installs SIGPROF, publishes one fixed CaptureBuffer pointer, signals the target thread with tgkill, and waits on a semaphore. The handler calls cpptrace's signal-safe raw unwinder into a256-frame buffer and posts completion. Expensive object-address conversion and symbolization are outside the handler. `arm` checks signal-safe-unwind capability and warms the path. Conan explicitly requires libunwind for this capability. Capture is serialized by the sampler thread.

The sampler sleeps for a configured interval, checks whether the target appears runnable, captures, drops leading Linux signal frames, turns raw addresses into module/RVA keys and discards apparent sleep frames when requested. It queues samples stamped with tick ID and one-second window. A separate aggregator consumes tick events and sample queues, buffers per-tick samples, filters short ticks and constructs a root→leaf call tree. Stop first joins the producer, then tells aggregation to drain, joins the aggregator and disarms capture.

Windows has a different implementation: suspend target, retrieve CONTEXT, StackWalk64, then resume and close the handle. Its source explicitly says it was not exercised on real Windows BDS. Sleeping-thread detection is TODO and always samples; sleep-frame filtering returns false. These are observable limits, not parity with Linux.

## Static failure cases worth preserving {#static-failure-cases-worth-preserving}

1. **Restart does not reset run state.** Sampler::start changes config/start_time and starts threads but does not clear tree, modules, current_tick or window_ticks. Profiler is a persistent plugin member and permits start after stop/cancel. Thus a second run can retain old counts/tree/windows while its time origin resets. No repeat-run self-test exists. This follows directly from state ownership; no live run was performed.
2. **Live sample count crosses ownership unsafely.** The command's info path calls Profiler::sampleCount→Sampler::sampleCount→CallTree::sampleCount, which iterates a std::map while the aggregator modifies it. No lock/atomic snapshot protects that map. The other exported data is documented as valid after stop; sampleCount is queried during running. A safe design needs an atomic published counter or synchronized snapshot.
3. **Tick events can outrun samples.** Aggregator drains tick events before samples. A completed tick event can be consumed before its same-tick sample reaches the bucket; the event is not retained. With filtering enabled, late buckets are eventually discarded by the eight-tick cleanup or at stop, regardless of the tick's true duration. Concurrent queues do not establish total ordering across two producers/queues. This is a static ordering risk, not measured sample loss.
4. **Signal timeout is not request cancellation.** The handler loads a shared buffer pointer once. A timeout clears the global slot, but does not acknowledge that a handler which already loaded the pointer has finished writing. A late signal/completion can cross a later request; there is no generation ID. During stop, the sampler's local buffer may cease to exist while a delayed handler remains possible. Serialized requests alone do not prove the single-slot handshake safe under timeout.
5. **Signal ownership is process-global.** arm replaces SIGPROF without saving the prior handler; disarm installs SIG_DFL rather than restoring it. It does not destroy the semaphore, and a sigaction failure after sem_init lacks cleanup. Other profilers/host signal users and repeated arms need explicit coexistence rules.
6. **Main-thread stop can still wait.** Joining the sampler may wait for a sampling interval or up to the capture timeout, then aggregation drain. The source's “fast join” and README's “server tick never stalls” are stated intentions, not demonstrated bounds. No upper bound on user interval is enforced.

## Plugin shutdown and export {#plugin-shutdown-and-export}

Plugin disable cancels a running profiler, joins its own export thread, then cancels scheduled tasks. Normal finish snapshots Endstone data before stopping samples, then starts a member std::thread for export. It captures only `this` in callbacks; source claims this helps avoid libc++ std::function ABI issues. Treat that as a stated workaround, not a general ABI guarantee.

Export can block in system curl without a timeout, so disable's join is unbounded. The background result schedules a main-thread callback; when disabled, the currently captured Endstone scheduler validates plugin enabled and may reject it. There is no explicit cancellation/error state transition for a failed hop-back. The export serialization call lies outside the try/catch that surrounds compression/upload, so an exception there can escape the worker. These boundaries need tests and a terminal-state policy.

## Outcomes and applicability {#outcomes-and-applicability}

The source provides an inspectable architecture and real error checks for inability to arm capture, start twice and unsupported allocation profiling. There is no measurement of overhead, no runtime reproduction in this review and no guarantee of complete native stack recovery. The offline tool exercises only one start/stop with synthetic work and prints results, not repeat lifecycle or concurrency assertions.

Retrieve this case when building a native diagnostic plugin or auditing “move work to a background thread” claims. Preserve the useful isolation of capture, aggregation and export, but require lifetime/ownership proofs for signal buffers, plugin unload, run reset, live counters and inter-queue ordering before reusing the implementation.

## Evidence {#evidence}

Use the [Spark source index](../repositories/spark-source-index.md) and [public initial commit](https://github.com/EndstoneMC/spark/commit/4c53cc0e0d0451697769c0ae37a2848adb50fe47) for the inspected capture, profiler, sampler and plugin code. Original local patch offsets are not public source line numbers. See SPARK02 for data correctness and SPARK03 for dependencies and historical rationale.
