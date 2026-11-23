<!-- retrieval: {"source_ids":["public:commit:9fd0aaecaca40f60efad074b1b570b1b1ce74d55"],"source_type":"public","date":"2026-08-25","topics":["testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="217-feat-protocol-model-scriptmessagepacket"></a>
# 217. feat(protocol): model ScriptMessagePacket {#217-feat-protocol-model-scriptmessagepacket}

Source: [9fd0aaecaca40f60efad074b1b570b1b1ce74d55](https://github.com/EndstoneMC/bedrock-protocol/commit/9fd0aaecaca40f60efad074b1b570b1b1ce74d55)
Authored: 2026-08-25T18:16:20Z  
Causal parent: 55337540f0947742eb5f4b5291929de07a118b7c

## Implementation and reasoning {#implementation-and-reasoning}

ScriptMessage id177 since2168 represents identifier and opaque string payload. Schema does not parse payload or implement script delivery.

## Tests and outcome boundary {#tests-and-outcome-boundary}

endstone:ping/hello fixture and empty identifier plus200-byte value c801,203 total; gates.

The tests above were read, not executed. Passing assertions and interoperable runtime behavior are not claimed. Test values establish codec representation intent; they do not validate gameplay semantics or all wire constraints.

## Attribution and source coverage {#attribution-and-source-coverage}

GitHub-linked author: wu-vincent; Git name Vincent. External codec/BDS mechanisms are credited in the analysis; no review endorsement is inferred.

Full commit message and all meaningful first-parent diff content read. Every changed file is covered; git blob-index headers were only mechanically verified. No binary changes or credential redactions in this unit.

Changed files: `protocol/script.py`, `tests/test_177_script_message.cpp`.

- message: 4 source lines; SHA256 `fa8492621dbe12e8924970469742ab345587e3a925d6b57fe46a8fb7af6fb7bf`, reverified against the mirror.
- diff: 71 source lines; SHA256 `4df25dd5b12e498fb8edc9bc3e9a73e09769def51f6de4218e132b92d999e444`, reverified against the mirror.

See [engineering synthesis](../ENGINEERING_SYNTHESIS.md) for shared encoding rules, producer-oracle limitations, version-gate policy and later-history integration. No actual compilation, tests, BDS execution, upstream changes or frozen-evaluation changes were made.
