<!-- retrieval: {"source_ids":[],"source_type":"synthetic","date":"2026-11-16","topics":["testing","maintainability","complexity","navigation"],"limitations":"Curated navigation and judgment synthesis, not independent verification or project policy."} -->
# Maintainable testing and complexity reduction: evidence navigation {#case}

## Scope and selection {#scope}

These focused case studies trace **why maintainers rejected or removed implementation and testing complexity**. Emphasis is EndstoneMC's review and revision history, with mature-project primary guidance as comparison. These are *case-specific judgments*, not universal line limits or a test-coverage target.

## Starting points {#cases}

- **Test infrastructure deleted for reasons documented by reviewer:** [Endstone: thread-state wrapper](endstone-thread-state.md); [Endstone: metrics bridge, chart and boundary tests](endstone-metrics.md); [Endstone: duplicate test_package](endstone-test-package.md); [Endstone: mock scaffolding](endstone-mocks.md).
- **Implementations narrowed after evidence:** [Endstone: network caching](endstone-network-cache.md); [Endstone: command grammar](endstone-command-grammar.md); [Endstone: justified generic polymorphism](endstone-polymorphism.md); [Endstone: dependency-owned cache cleanup](endstone-conan-workaround.md); [Endstone: corrected native ABI model](endstone-abi-diagnosis.md); [Endstone: standard plugin loading](endstone-plugin-loader.md); [Bedrock: protocol compiler scaffold](bedrock-protocol-compiler.md); [starter plugins](starter-plugins.md); [Bedrock: removed wire codec scope](bedrock-wire-scope.md); [Bedrock: reflection-backed Python binding](bedrock-reflection-binding.md).
- **Necessary complexity counterexample:** [Endstone: async unload safety](endstone-async-counterexample.md).

Two newer cases in [EndstoneMC/bedrock-protocol PR #2](https://github.com/EndstoneMC/bedrock-protocol/pull/2) (October–November 2026) document independent architecture reversals, not repeats of the initial scope reduction in the [Bedrock protocol compiler case](bedrock-protocol-compiler.md). The supporting [PR #2 engineering synthesis](../../sources/commit-review/bedrock-protocol-pr2-2026/ENGINEERING_SYNTHESIS.md) also covers build/packaging verification and protocol-wire corrections without duplicating the earlier historical corpus.

## Comparisons and budget interpretation {#comparison}

- [Repository snapshot](../../comparators/maintainable-testing/repository-snapshot.md): reproducible Git-tree *file/byte* snapshot of selected EndstoneMC repositories; **not** a prescriptive baseline or coverage measurement.
- [Official guidance](../../comparators/maintainable-testing/official-guidance.md): project-authored testing practices from Google, LLVM, Go, CPython, Linux kernel, PostgreSQL and SQLite.
- **26 previously diff-checked historical implementation decisions**: [Linux](../../comparators/maintainable-testing/linux.md), [Go](../../comparators/maintainable-testing/go.md), [LLVM](../../comparators/maintainable-testing/llvm.md), [PostgreSQL](../../comparators/maintainable-testing/postgresql.md), [SQLite](../../comparators/maintainable-testing/sqlite.md), [CPython](../../comparators/maintainable-testing/cpython.md). These are a separately graded supplement, not a claim of runtime verification.
- [Testing](../judgment/testing.md): the concise conditional test-design rule.

## Evidence grading {#method}

**Observed** = primary source commit diff/PR discussion or preserved audited historical analysis. **Reported** = maintainers' own build, benchmark, or test assertions. **Inferred** = proposed transfer for AI agents. Those categories must not be collapsed. Lines added/deleted count changed lines, not maintained source lines or reliability. We did not execute original projects. These cases cover only the named repositories and do not change other bundled analyses.
