<!-- retrieval: {"source_ids":["public:commit:8b9173691659e15cdd9dd2b4cf628081029d09cf"],"source_type":"public","date":"2026-10-12","topics":["testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="bedrock-bench-fake-system-and-integration-contract-review"></a>
# bedrock-bench fake-system and integration-contract review {#bedrock-bench-fake-system-and-integration-contract-review}

## Result {#result}

The complete change in [8b9173691659e15cdd9dd2b4cf628081029d09cf](https://github.com/EndstoneMC/bedrock-bench/commit/8b9173691659e15cdd9dd2b4cf628081029d09cf), ordinal 13 of the main review, has been substantively read: 32 new files, 5,090 source lines, 5,282 full diff lines. The reduced view has 5,218 logical lines; its only omissions are 64 file-mode/blob-identity header lines, also inspected. All 32 reconstructed additions match their Git blob identities. This is a source review, not a test run.

The useful mechanism is a substitute system behind the same adapter, command-line, process, console, artifact and event interfaces. It supports short, intentionally faulty executions without installing a game server. Its strongest limits are equally important:

- The network is a private JSON-lines TCP protocol, not Bedrock/RakNet. Chunk, packet-byte and RTT telemetry is simulated.
- Generated output and fake parsing patterns share definitions. This prevents internal drift but is not independent evidence of real-server fidelity.
- `runner.py`, `phases.py` and `results.py` do not exist at this commit. Integration tests are conditionally strict xfail until their entry points exist. Test source cannot be treated as a successful end-to-end result.
- Fake control operations implement less than the real bot contract, especially index addressing, reconnect timing, global radius and jitter.
- Initial tests classify a bad stop as server failure. Later examined history deliberately changes post-measurement stop failures into an `unclean_stop` flag.
- The commit declares Claude Opus 5.5 coauthorship. The GitHub-linked Vincent attribution is preserved without assigning every design decision exclusively to him.

## Offline navigation {#offline-navigation}

- [Detailed dossier](dossier.md): mechanism, constraints, alternatives, lifecycle, fidelity, limitations and reusable decisions.
- [Test claims and boundaries](test-coverage.md): every test module and the assertions it contributes.

This is static analysis of the cited upstream commit, not an upstream code change or a benchmark run. Nukkit here names contemporary fake adapters; unrelated historical Nukkit implementation choices were not examined.
