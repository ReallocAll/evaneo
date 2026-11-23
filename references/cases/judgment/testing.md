<!-- retrieval: {"source_ids":[],"source_type":"judgment_synthesis","date":"2026-10-30","topics":["engineering-judgment","testing","maintainability","complexity","review"],"limitations":"Conditional synthesis with preserved safety exceptions; references public historical cases. This is not authorization to remove tests or override current project requirements."} -->
# Test contracts with the lowest sustainable maintenance cost {#overview}

## Decision rule {#rule}

**Default during a consequential implementation or test-design decision:** Choose verification according to the externally meaningful failure risk and expected maintenance cost. Reuse existing tests and harnesses before adding new layers. Preserve tests for real compatibility, persistence, ownership, security, concurrency and protocol contracts. Do not target a test-count, test-to-production-code ratio, or coverage percentage as an objective.

**Before adding a separate harness, embedded runtime, mock framework, multi-platform matrix, or generated test layer,** establish what observable defect it would detect that the existing facility cannot, and why a smaller targeted test or real integration check would be insufficient. This is an engineering decision, not a mandatory form or approval ceremony.

**Before deleting or consolidating tests,** identify the distinct contract each removed test protected and either show retained evidence of that contract or explicitly disclose the lost guarantee. A shorter suite is not automatically better; more assertions do not automatically make a suite stronger.

## What counts as a good test {#oracles}

A useful test names an observable contract, uses an oracle that can reject a plausible wrong implementation, is understandable and deterministic enough to diagnose failures, and does not couple unnecessarily to private implementation details. Prefer adding a case to a coherent existing test file. For performance, do not treat unrelated workload captures as comparable A/B measurements.

## Primary cases and counterexamples {#evidence}

- [Endstone: thread state](../maintainable-testing/endstone-thread-state.md): custom C++ wrapper and embedded test infrastructure removed when existing pybind11 guards suffice.
- [Endstone: metrics](../maintainable-testing/endstone-metrics.md): custom service hierarchy and duplicate C++/Python chart logic removed; three test facilities deleted with explicitly noted coverage losses.
- [Endstone: network cache](../maintainable-testing/endstone-network-cache.md): a broad proposed caching layer narrowed to a verified player lookup.
- [Endstone: test package](../maintainable-testing/endstone-test-package.md), [Endstone: mocks](../maintainable-testing/endstone-mocks.md): duplicated test package and mock boilerplate reduced.
- [Endstone: async counterexample](../maintainable-testing/endstone-async-counterexample.md): async task lifetime genuinely warrants cross-thread regression tests.
- [Bedrock: protocol compiler](../maintainable-testing/bedrock-protocol-compiler.md): unsupported generality removed and later reintroduced when needed by real consumers.
- [Official guidance](../../comparators/maintainable-testing/official-guidance.md): official guidance from Google, LLVM, Go, CPython, Linux kernel, PostgreSQL and SQLite, with non-transferable extremes identified.

## Applicability and limits {#limits}

These are default engineering constraints, **not** authority to ignore current project contracts, remove necessary validation, or weaken user requirements. Historical commit statistics are descriptive, not correctness proofs. When a proposed test is costly but addresses a serious native ABI, data-loss, crash-recovery or concurrency boundary, keep the test if it offers distinct assurance. Use available real-runtime evidence where the behavior cannot be validated by a mock. No upstream code was executed to prepare this supplement.
