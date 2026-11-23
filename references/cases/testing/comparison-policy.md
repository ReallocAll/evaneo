<!-- retrieval: {"source_type":"static_review","topics":["compatibility","differential-testing","test-oracle","skips","validation","Python","evidence"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="keep-comparison-policy-independent-of-test-output"></a>

# Keep comparison policy independent of test output {#keep-comparison-policy-independent-of-test-output}

## Failure mode {#failure-mode}

A differential suite can appear healthier simply because its own output declares more tests inapplicable. If the comparator accepts any emitted skip classification as permission to omit a case, a test-side change can shrink the evidence without failing the build.

## Observed correction {#observed-correction}

The inspected comparator originally learned permitted engine-specific exceptions from emitted results. The correction introduced an independent allowed-topic policy and rejected any mismatch between that policy and the declared exception set. A case applicable to only one side still had to pass on that side.

The complete surrounding script was read. It also checked that completion output appeared in the expected place, reconciled totals with observed result lines, checked which implementation actually ran, retained comparison output and distinguished infrastructure failure from disagreement.

These checks improve the meaning of a green result: the suite must reach a verdict under a known exception policy, rather than merely emit some reassuring text.

## Essential distinction {#essential-distinction}

Agreement is not correctness. Two implementations can fail the same assertion, share an incorrect assumption, or be observed through a faulty harness. An equal failure can support behavioral agreement while still requiring investigation of the test expectation and both implementations.

Do not convert “both sides failed similarly” into proof that the test is wrong. Nor should an unavailable reference, wrong runtime or incomplete run become a pass.

## A stronger comparison contract {#a-stronger-comparison-contract}

For a new suite, define in advance:

1. The expected case identities and applicability
2. The allowed normalization and exception policy
3. The required observations, including failures
4. The criteria for complete execution
5. Separate outcomes for disagreement, invalid evidence and agreement

Reject duplicate or missing case identities instead of silently overwriting them in a dictionary. Compare against an independently established case manifest when coverage matters. These are analyst extensions: the inspected script's counters and result map do not by themselves prove those stronger properties were implemented.

## Costs and limits {#costs-and-limits}

An independent policy needs deliberate maintenance when legitimate applicability changes. It should be narrow enough to detect accidental coverage loss without freezing the suite forever.

The policy patch and comparator were read; no comparison run was performed. The source's association with the changes supports a bounded engineering example, not a universal personal preference or a claim of oracle independence for every test.
