<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2026-10-20","topics":["profiling","design","validation"],"limitations":"External comparator at pinned samples; transfer guidance is independent analysis. No upstream or target implementation runtime tests were executed."} -->
# Profiler contracts and tradeoffs from Linux, Tracy, and SQLite {#case}

This comparison uses pinned public sources. No upstream program, test suite, profiler, or benchmark was executed.

The useful transfer is a way to choose contracts before writing code: account for missing evidence, specify shutdown ownership, reduce representable invalid states, and make tests reject a believable wrong answer. It is not a recommendation to import the Linux kernel, adopt Tracy wholesale, or reproduce SQLite's testing budget.

## Read in this order {#section-01}

1. [perf loss and observer cost](perf-loss-and-budget.md). Decide what the profile can honestly claim before deciding its sampling frequency or queue implementation.
2. [Tracy lifetime and delivery](tracy-lifetime-and-delivery.md). Decide whether data delivery, prompt shutdown, and unload safety are guarantees or conditional goals.
3. [representation before conditionals](representation-before-conditionals.md). Remove a real exceptional state when possible; do not hide it behind a clever container or universal abstraction.
4. [SQLite-style discriminating tests](sqlite-discriminating-tests.md). Ask which plausible wrong implementation each assertion would catch.

These are independent case studies, joined by the needs of an in-process C/C++ sampling profiler. The [perf loss case](perf-loss-and-budget.md#case) and [Tracy lifetime case](tracy-lifetime-and-delivery.md#case) concern different external projects; their transport and concurrency designs are not interchangeable.

## Design-before-code card for Codex {#section-02}

This is an original synthesis, not a statement from the comparator projects. Optional case-specific aid: for a substantial profiler change, one short page can help. This is not a required workflow or an extra lookup gate:

- **Question being measured:** which thread, clock, workload phase, and population? Is the result CPU occupancy, wall time, or a labelled estimate?
- **Smallest useful contract:** what must still be true when capture fails, the consumer stalls, or the host unloads the plugin?
- **Existing facility:** what can the platform or an already accepted library do? Record unsupported targets and permission constraints before proposing a new mechanism.
- **Ownership and states:** who owns each capture buffer, run, queue, result, and callback? Which event establishes that no writer remains?
- **Limits and loss:** state the memory/work budget, full-buffer behavior, and how uncertainty reaches the user.
- **Options:** compare the simplest viable baseline with one realistic alternative. Include integration cost and future maintenance, not only source line count.
- **Chosen representation:** name the invariant it simplifies and any remaining special cases. Avoid a new framework when a local data-model change suffices.
- **Discriminator:** list one normal-case and one failure/interleaving test, each with its expected observable result and a plausible mutant it defeats.
- **Evidence needed:** separate deterministic correctness, real-platform lifetime safety, and overhead measurements. A pass in one category is not a pass in the others.
- **Stop condition:** what measured evidence would reject the change or send it back to design? Do not invent numerical budgets on the user's behalf.

The default should be a small proposal and a small test seam, not a generated subsystem. Increase machinery only when an identified requirement cannot be satisfied otherwise.

## Application to Spark and attribution {#section-03}

The existing [Spark lifecycle review](../../sources/commit-review/plugin-api-evolution/cases/spark-profiler-lifecycle.md) and [measurement/export review](../../sources/commit-review/plugin-api-evolution/cases/spark-measurement-and-export.md) supply the local motivation. They are static reviews of commit `4c53cc0e0d0451697769c0ae37a2848adb50fe47`, not runtime reproductions. This comparison does not independently establish every Spark finding.

The Linux list documentation credits Nicolas Frattaroli. Its documented rationale does not establish who authored or reviewed the separately cited implementation.

## Evidence and verification {#section-04}

- [SOURCES.md](SOURCES.md): human-readable inventory and limitations.
- [source-inventory.json](source-inventory.json): pinned source revisions, inspected spans, and the claims each source supports.

The Markdown is self-contained enough to use offline. Source bodies are not included. Pinned commit URLs let a later reviewer retrieve the same code. Two SQLite documentation pages are unversioned and may change; the source notes identify when they were read. No claim is made that these selected versions are the latest available.
