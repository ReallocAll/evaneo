<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:550"],"source_type":"public","date":"2026-10-13","topics":["concurrency","ffi","testing","performance","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-550-perf-level-feed-the-chunk-generation-workers"></a>
# EndstoneMC/endstone #550: perf(level): feed the chunk generation workers {#endstonemc-endstone-550-perf-level-feed-the-chunk-generation-workers}

Source: https://github.com/EndstoneMC/endstone/pull/550

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-10-13T17:02:15Z; recorded state open; merged False.

## Faster chunk dispatch with an unresolved throughput tradeoff {#faster-chunk-dispatch-with-an-unresolved-throughput-tradeoff}
Open PR550 challenges terrain-cost intuition:100spread players wait~430s despite seven mostly idle generators, because dispatcher scores every pending chunk against every player and launches~29 tasks. One byte patch raises2n/6n caps to8n/24n; one new scoring hook and extended influence snapshot prune players by float-safe distance/4 and directional bounds while calling native scoring on a thread-local reduced policy. Exactness, not approximate priority, is the design constraint.
Nine million shipped-machine-code queries per platform reportedly show no mismatch with sanitizers clean. First4096 calls/thread and1/4096 thereafter shadow native; mismatch/unexpected layout warns and falls back. Three same-machine Windows100walking-bot runs halve median view load428→212s, p90532→243, chunks/s58.6→107. SteadyTPS falls19.81→19.12 consistently and is unexplained; observed result still far from47–50s model. No warnings does not prove untested layouts safe.
Linux builds/236tests and unique signatures are claimed but no live Linux run. Windows128-byte policy layout derives from disassembly. Source comparisons to Altay/Dragonfly are context-specific benchmarks, not independently reproduced here. Open/unmerged status and performance regression must remain visible.

## Direct patch findings {#direct-patch-findings}

Full diff confirms two-layer optimization: worker-count shift3→1 makes8n/24n cap instead of2n/6n, plus eight fixed policy slots holding versioned immutable influence snapshots. Update holds a slot mutex around native swap and snapshot; mismatch in map/vector counts disables all snapshots. Readers cache snapshots thread-locally, fall back for missing/odd versions, fewer than16 players or possible int32 distance overflow, and always retain non-player/unusual vertical-direction influences. Candidate pruning uses nearest native score,17×bound² conservative distance threshold, and directional tolerance; original scorer runs on a partially constructed thread-local policy containing only lock/vector. That depends on native method touching only those reconstructed fields, a significant ABI assumption beyond sizeof assertions. Initial4096 and every4096th call return native expected score while checking mismatch; stable-version mismatch globally disables optimization. Fixed slots are never reclaimed in this patch, so policy churn can exhaust optimization capacity; stale address reuse is not tested. The shadow harness,9million-query benchmark and end-to-end results are described in the body, not committed as executable tests here.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (29064 characters; SHA-256 3ac96705984a54fef0a66140b69d3e7779d7b7bf1ba847fc51b405ec7eaa72aa), head 569653076feb1b5256b391271723d007003ea044. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/550
