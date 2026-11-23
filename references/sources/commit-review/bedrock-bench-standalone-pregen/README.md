<!-- retrieval: {"source_ids":["public:commit:f3a696cc01d7438a7bcbab1c37a93df14dff4d35"],"source_type":"public","date":"2026-10-12","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="standalone-adapters-and-pre-generated-worlds"></a>
# Standalone adapters and pre-generated worlds {#standalone-adapters-and-pre-generated-worlds}

Source: [bedrock-bench commit f3a696cc](https://github.com/EndstoneMC/bedrock-bench/commit/f3a696cc01d7438a7bcbab1c37a93df14dff4d35), authored by Vincent with explicit coauthor credit to Claude Opus 5.5.

- [Detailed dossier](dossier.md): the problem, implementation, trade-offs, failure lifecycle, fidelity and limitations.
- [Tests and exact source navigation](test-coverage.md): 111 static test functions and what they exercise or simulate.
- Public commit source and bounded static coverage notes.

No upstream code was imported, compiled, run, or tested. Runtime claims below are source intentions, author-reported results, or limitations.

Use this case when adding a foreign-runtime adapter, keeping configuration changes auditable, distinguishing rescue variants from defaults, controlling world-state reuse, or asking whether a test proves persistence. The central caution is that a template tree hash preserves the state accepted by a validator; it cannot strengthen that validator's coverage or clean-save guarantees.
