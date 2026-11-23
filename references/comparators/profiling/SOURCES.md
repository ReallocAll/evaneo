<!-- retrieval: {"source_ids":["public:comparator-source:profiling:P01","public:comparator-source:profiling:P03","public:comparator-source:profiling:P02","public:comparator-source:profiling:L01","public:comparator-source:profiling:L02","public:comparator-source:profiling:T01","public:comparator-source:profiling:T02","public:comparator-source:profiling:T03","public:comparator-source:profiling:S03","public:comparator-source:profiling:S04","public:comparator-source:profiling:S01","public:comparator-source:profiling:S02"],"source_type":"public","date":"2026-10-20","topics":["profiling","design","validation"],"limitations":"External comparator at pinned samples; transfer guidance is independent analysis. No upstream or target implementation runtime tests were executed."} -->
# Source inventory and evidence limits {#case}

The sources were read from public web/GitHub endpoints on 2026-10-20. The pinned versions are examples, not a latest-version survey. This document summarizes upstream evidence and identifies its sources without redistributing their original files.

## Verified version identities {#section-01}

- Linux v6.17 resolves through annotated tag `6063257da111c7639d020c5f15bfb37fb839d8b6` to commit `e5f0a698b34ed76002dc5cff3804a61c80233a7a`. [Tag reference](https://api.github.com/repos/torvalds/linux/git/ref/tags/v6.17), [tag target](https://api.github.com/repos/torvalds/linux/git/tags/6063257da111c7639d020c5f15bfb37fb839d8b6).
- Tracy v0.11.1 resolves to commit `5d542dc09f3d9378d005092a4ad446bd405f819a`. [Tag reference](https://api.github.com/repos/wolfpld/tracy/git/ref/tags/v0.11.1).
- SQLite version-3.46.1 resolves to commit `f3d536d37825302e31ed0eddd811c689f38f85a3`. [Tag reference](https://api.github.com/repos/sqlite/sqlite/git/ref/tags/version-3.46.1).

Tag-to-commit resolution verifies the inspected version identity. It is not an independent cryptographic verification of release signatures.

## Sources used {#section-02}

| ID | File or page | Inspected locations | Evidence contribution |
| --- | --- | --- | --- |
| P01 | [Linux Documentation/userspace-api/perf_ring_buffer.rst](https://github.com/torvalds/linux/blob/e5f0a698b34ed76002dc5cff3804a61c80233a7a/Documentation/userspace-api/perf_ring_buffer.rst) | 438–491; 523–585 | Explicit loss contracts and synchronization protocol |
| P02 | [Linux kernel/events/ring_buffer.c](https://github.com/torvalds/linux/blob/e5f0a698b34ed76002dc5cff3804a61c80233a7a/kernel/events/ring_buffer.c) | 152–270 | Admission failure, deferred loss record, loss counters |
| P03 | [Linux kernel/events/core.c](https://github.com/torvalds/linux/blob/e5f0a698b34ed76002dc5cff3804a61c80233a7a/kernel/events/core.c) | 600–664 | Duration-feedback sample-rate limiting |
| L01 | [Linux Documentation/core-api/list.rst](https://github.com/torvalds/linux/blob/e5f0a698b34ed76002dc5cff3804a61c80233a7a/Documentation/core-api/list.rst) | 14–70 | Documented representation rationale and locality warning |
| L02 | [Linux include/linux/list.h](https://github.com/torvalds/linux/blob/e5f0a698b34ed76002dc5cff3804a61c80233a7a/include/linux/list.h) | 23–232; 282–289 | Sentinel initialization, adjacency operations, deletion/reinitialization distinction |
| T01 | [Tracy manual/tracy.tex](https://github.com/wolfpld/tracy/blob/5d542dc09f3d9378d005092a4ad446bd405f819a/manual/tracy.tex) | 519–573; 1005–1023; 1394–1398 | Explicit collection/lifetime options and boundary warnings |
| T02 | [Tracy public/client/TracyProfiler.cpp](https://github.com/wolfpld/tracy/blob/5d542dc09f3d9378d005092a4ad446bd405f819a/public/client/TracyProfiler.cpp) | 1192–1223; 1790–1812; 2047–2133 | Concrete startup, connection wait, termination phases |
| T03 | [Tracy public/client/TracySysTrace.cpp](https://github.com/wolfpld/tracy/blob/5d542dc09f3d9378d005092a4ad446bd405f819a/public/client/TracySysTrace.cpp) | 1–35; 824–880 | Corroborating sampling setup inspected; not used as a case premise |
| S01 | [sqlite.org/testing.html](https://sqlite.org/testing.html) | HTML snapshot 895–1010; coverage/mutation sections | Project account of test discrimination, delivered-build checks, cost boundaries |
| S02 | [sqlite.org/th3.html](https://sqlite.org/th3.html) | HTML snapshot 498–554; mutation/license sections | Project account; proprietary implementation not inspected |
| S03 | [SQLite test/malloc_common.tcl](https://github.com/sqlite/sqlite/blob/f3d536d37825302e31ed0eddd811c689f38f85a3/test/malloc_common.tcl) | 26–50; 326–391 | Public transient/persistent fault loop and post-injection oracle |
| S04 | [SQLite src/test_malloc.c](https://github.com/sqlite/sqlite/blob/f3d536d37825302e31ed0eddd811c689f38f85a3/src/test_malloc.c) | 29–128 | Concrete allocator failure injection mechanics |

The [source inventory](source-inventory.json) maps pinned revisions and inspected spans to the cases they support. The case documents link directly to the relevant immutable code spans. S01 and S02 are unversioned official documentation pages read on 2026-10-20; they are not pinned to a SQLite release and may since have changed. Their HTML line numbers are navigation aids and may move with the site layout.

## Interpretation rules {#section-03}

1. **Explicit rationale:** preserve the scope in which the upstream documentation states a purpose or tradeoff.
2. **Source fact:** a visible branch, ownership operation, or counter is inspectable behavior; it is not a benchmark or proof of every build configuration.
3. **Inference:** options, recommendations, and Spark application sections are analysis. They do not imply the comparator author endorsed the proposed design.
4. **Local motivation:** Spark-related findings are linked to the already completed static reviews, with their version and runtime limitations preserved. No new Spark code was changed or run.
5. **Absent evidence:** no full project history, issue/review survey, complete Linux memory-model analysis, Tracy platform matrix, TH3 source, or measured profiler performance is claimed.

## What verification does and does not mean {#section-04}

Readers can follow the pinned source links and compare cited line ranges with [source-inventory.json](source-inventory.json). Matching a source revision to its cited range can detect a mismatched evidence reference; it cannot establish source correctness, concurrency safety, performance, or test adequacy.

The test scenarios in all four profiling case studies are proposals. There were no Linux/Tracy/SQLite/Spark builds, benchmarks, runtime tests, sanitizer runs, or upstream mutations.
