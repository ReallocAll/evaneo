<!-- retrieval: {"source_type":"static_review","topics":["integration","build","linking","architecture","capability","testing","documentation","evidence"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="match-capability-claims-to-the-boundary-actually-exercised"></a>

# Match capability claims to the boundary actually exercised {#match-capability-claims-to-the-boundary-actually-exercised}

## Problem {#problem}

A component can compile without being linked into a runnable path. A service can announce a capability without implementing the full interaction. A synthetic test can validate an adapter while leaving the real host boundary untouched.

## Inspected chain {#inspected-chain}

A staged refactor removed an obsolete adapter and temporarily excluded an unfinished replacement from the build. A subsequent step compiled a library seam while some owner-side behavior was still being connected. A successful executable build did not alone establish that the new object was linked and exercised: unused archive members can remain outside the executable's reachable path.

Another change removed outward-facing capability surfaces that accepted or advertised behavior without completing it. That reduced the gap between what a client could infer and what the implementation actually supported. It was a scope correction, not evidence that the removed capability had become functional.

Elsewhere, loopback tests exercised lifecycle and callback transitions through a synthetic transport. Documentation separated those tests from a reported live-host check and separated one observed platform from another platform's inferred behavior. The review did not repeat those executions.

## An evidence ladder {#an-evidence-ladder}

Keep distinct statements for:

1. The declaration compiles.
2. The implementation compiles into an artifact.
3. The expected object and symbols are linked into the delivered program.
4. The relevant path is reached in a controlled test.
5. The real external boundary completes the intended interaction.
6. Failure, cancellation and repeated-operation behavior are covered.

A lower step can be valuable without implying the next one. Report the highest demonstrated step and the remaining assumptions.

For advertised capabilities, connect each signal to an end-to-end acceptance criterion. If the implementation is staged, suppress the signal, reject the operation explicitly, or mark the feature unavailable in a way the consumer understands.

## Costs and limits {#costs-and-limits}

Temporary exclusion makes incremental work easier but can hide missing integration if CI checks only the default build. Consider a dedicated compile target, a link-coverage check or a small boundary test. These are suggested safeguards, not features claimed present in the inspected project.

Synthetic tests remain useful because they control scheduling and failure injection. Pair them with a small real-boundary check rather than replacing them with a costly end-to-end suite.

This case supports honest capability and evidence reporting. It does not assert that every staged commit should be production-ready, that a source-reported live run was independently verified, or that all platforms behave alike.
