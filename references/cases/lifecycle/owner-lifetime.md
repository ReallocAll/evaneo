<!-- retrieval: {"source_type":"static_review","topics":["C++","lifecycle","ownership","reload","plugin-boundary","behavior-preservation","regression-testing"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="align-replacement-lifetime-with-the-real-owner"></a>

# Align replacement lifetime with the real owner {#align-replacement-lifetime-with-the-real-owner}

## Problem and constraint {#problem-and-constraint}

A replacement component can imitate an interface yet still violate its lifetime contract. A short-lived context may release its last local reference while the host continues to retain and call a longer-lived service. Reload is particularly revealing: contexts disappear and return, while controller state may intentionally survive.

## Observed decision chain {#observed-decision-chain}

The inspected correction distinguished the host-owned service from the contexts using it. The earlier replacement died with the last context. The source reports that a host-held controller reference then became invalid during reload and a later operation crashed.

The implementation change added a strong lifetime relationship anchored to the host-owned object. Tests changed accordingly: releasing local context-side references should not destroy the replacement while the host owner remains; destroying the host owner should release it; subsequent creation should produce a new valid instance.

A related test change exercised state continuity across context destruction and recreation. It also exercised overlapping diagnostics and callback-driven operations. These tests make transitions observable rather than relying solely on a happy-path construction test.

## Transferable method {#transferable-method}

Draw separate ownership graphs for the host and the replacement. Include raw references, callbacks, caches and retained service handles. For each edge, record whether it is owning or observing and the event that removes it.

Build a transition matrix covering normal use, last-context removal, reload, last-host-owner removal, shutdown and recreation. Verify both necessary survival and eventual release. A weak reference or other observable lifetime probe can help test those two sides without confusing a successful use with proof that cleanup occurs.

## What must not be generalized {#what-must-not-be-generalized}

The concrete anchoring technique in the inspected implementation depended on version-specific host internals. It is deliberately omitted. Reusing an apparently spare callback or storage field in another system could violate unrelated behavior, ownership or binary assumptions.

The general lesson is to establish the actual ownership contract and choose an explicit, justified lifetime anchor. It is not to extend every object to process lifetime or add global strong references. Either can hide the original crash while creating leaks, stale state or shutdown cycles.

## Evidence boundaries {#evidence-boundaries}

The fix and its test patches were read. The external host's ownership claims were described by the source but were not independently reconstructed or executed here. The report of a live failure is evidence of the author's diagnosis, not a new measured result. This case supports a concrete ownership investigation and test strategy, not universal compatibility.
