<!-- retrieval: {"source_ids":["public:commit:0a49c6914171a3d325adfca5bc50cf612ea4cb8e","public:commit:655e3e486185341520890621f65d9b69a9b6067d"],"source_type":"public","date":"2026-10-12","topics":["concurrency","testing","build","performance","documentation","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="legacy-benchmark-source-review"></a>
# Legacy benchmark source review {#legacy-benchmark-source-review}

This is a static engineering review of the source portion of EndstoneMC/bedrock-bench's initial import, commit `0a49c6914171a3d325adfca5bc50cf612ea4cb8e` (ordinal 0). It also checks that source's presence at `13f9df244044ed39ce62af70d3954f46de997983` (ordinal 2) and removal at `655e3e486185341520890621f65d9b69a9b6067d` (ordinal 26). No upstream program, test, build script, server, bot, or workflow was executed.

## Useful findings {#useful-findings}

- The imported harness is a historical experiment snapshot, not a standalone reproducible benchmark distribution. Several imported scripts still require missing sibling modules, binaries, build directories, server plugins, or machine-specific paths.
- Exact Git object comparison attributes 362 of the 372 vendored gophertunnel files to unmodified upstream v1.62.0. Eight files have small local changes; two loadbot programs were added. This is not 372 independently authored target implementations.
- All 455 assigned source/configuration/script paths are byte-identical at ordinal 2 and immediately before ordinal 26. Ordinal 2 does not move or modify this source. Ordinal 26 removes all 455 paths; only the all-options LeviOptimize JSON has an identical surviving copy in the new server configuration tree.
- “All joined,” “settled,” “90% view,” CPU milliseconds per tick, and “clean verification” each have narrower meanings than their names suggest. The dossiers explain their exact formulas and failure modes.
- Windows and Linux chaos are distinct workloads, including different commands, action sets and schedules. A common random seed would not make executed work equal; queueing, dropped commands and bot replies further change it.
- Archived benchmark outcomes remain reported results. Static inspection explains mechanisms and limitations; it does not reproduce performance, prove crash freedom, or validate Windows/Linux behavior.

## Reading routes {#reading-routes}

1. [Source and dependency attribution](dossiers/vendor-and-loadbots.md): exact upstream identities, all local protocol deltas, workload and bot-accounting semantics.
2. [Platform runners and measurement](dossiers/platform-runners-and-metrics.md): fresh worlds, isolation, time bases, process/thread selection, settle and completion.
3. [Cross-server adaptations](dossiers/cross-server-adapters.md): feature substitutions, pre-generation, Dragonfly transaction boundaries, configuration and fair-comparison limits.
4. [Chaos and integration validation](dossiers/chaos-and-integration.md): stress scheduling, executed-versus-queued work, verification meaning and test parser limits.
5. [Builds, coordination and LeviLamina](dossiers/build-coordination-and-levilamina.md): staging provenance, lock ownership, marker semantics, build failures and configuration migration.

The original result files are outside this source review scope. See the [legacy results analysis](../bedrock-bench-blogs/legacy-results-analysis.md#coverage-and-provenance) and [imported results and removal](../bedrock-bench-all/dossiers/import-results-and-removal.md#evidence-and-scope); new package code at ordinal 2 is reviewed in the [commit-level history](../bedrock-bench-all/dossiers/commit-by-commit.md#002-13f9df244044ed39ce62af70d3954f46de997983-add-the-bedrockbench-package-foundation-and-shared-contracts), and the [chronological design map](../bedrock-bench-all/dossiers/chronological-design-map.md#chronological-design-map) covers subsequent evolution. Pure third-party imports are explicitly disposed as byte-identical dependencies, not falsely marked fully semantically read. The third-party author's LICENSE is retained with source excerpts.
