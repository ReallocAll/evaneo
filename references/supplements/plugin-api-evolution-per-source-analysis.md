<!-- retrieval: {"source_ids":["public:commit:23f9839b16e600c08c409889a9298347d776eb16","public:commit:316b5acf307af522041ff091280398b7970e9ba8","public:commit:4c53cc0e0d0451697769c0ae37a2848adb50fe47","public:commit:8cc11d8a26a7088f3943f260f0266d14d3b00d5e"],"source_type":"public","date":"2026-07-11..2026-07-12","topics":["ffi","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Additional per-source analysis and source qualifications {#additional-per-source-causal-analysis}

These supplemental notes record commit-specific engineering observations and evidence limits alongside the main source analyses. Public commit links identify the inspected revisions; no runtime result is independently verified here. A repeated review-scope qualification describes a limit of the analysis, not necessarily a change made by every listed commit.

<a id="commit-4c53cc0e0d0451697769c0ae37a2848adb50fe47"></a>
## Initial commit: endstone-spark, a spark-style native profiler for BDS {#commit-4c53cc0e0d0451697769c0ae37a2848adb50fe47}

Evidence limits: Windows backend is explicitly unexercised by source author; this review also finds portability gaps.

Evidence limits: Source comments about validation/ABI/scheduler bugs are author claims unless independently scoped in cases.

### Provenance {#commit-4c53cc0e0d0451697769c0ae37a2848adb50fe47-provenance}

Public source: https://github.com/EndstoneMC/spark/commit/4c53cc0e0d0451697769c0ae37a2848adb50fe47

Source date: 2026-07-11T23:59:56Z


<a id="commit-23f9839b16e600c08c409889a9298347d776eb16"></a>
## docs: frame as a native port of spark to Endstone {#commit-23f9839b16e600c08c409889a9298347d776eb16}

Evidence limits: Windows backend is explicitly unexercised by source author; this review also finds portability gaps.

Evidence limits: Source comments about validation/ABI/scheduler bugs are author claims unless independently scoped in cases.

### Provenance {#commit-23f9839b16e600c08c409889a9298347d776eb16-provenance}

Public source: https://github.com/EndstoneMC/spark/commit/23f9839b16e600c08c409889a9298347d776eb16

Source date: 2026-07-12T00:07:04Z


<a id="commit-8cc11d8a26a7088f3943f260f0266d14d3b00d5e"></a>
## build: use conanfile.txt instead of conanfile.py {#commit-8cc11d8a26a7088f3943f260f0266d14d3b00d5e}

Evidence limits: Windows backend is explicitly unexercised by source author; this review also finds portability gaps.

Evidence limits: Source comments about validation/ABI/scheduler bugs are author claims unless independently scoped in cases.

### Provenance {#commit-8cc11d8a26a7088f3943f260f0266d14d3b00d5e-provenance}

Public source: https://github.com/EndstoneMC/spark/commit/8cc11d8a26a7088f3943f260f0266d14d3b00d5e

Source date: 2026-07-12T00:07:04Z


<a id="commit-316b5acf307af522041ff091280398b7970e9ba8"></a>
## docs: add GPLv3 LICENSE (matching spark) {#commit-316b5acf307af522041ff091280398b7970e9ba8}

Evidence limits: Windows backend is explicitly unexercised by source author; this review also finds portability gaps.

Evidence limits: Source comments about validation/ABI/scheduler bugs are author claims unless independently scoped in cases.

### Provenance {#commit-316b5acf307af522041ff091280398b7970e9ba8-provenance}

Public source: https://github.com/EndstoneMC/spark/commit/316b5acf307af522041ff091280398b7970e9ba8

Source date: 2026-07-12T00:12:32Z
