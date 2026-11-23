<!-- retrieval: {"source_type":"static_review","topics":["testing","golden-files","portability","differential-testing","normalization","C++","JavaScript"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="normalize-only-observations-outside-the-contract"></a>

# Normalize only observations outside the contract {#normalize-only-observations-outside-the-contract}

## Problem {#problem}

A golden output can accidentally specify the iteration order of an unordered container. Different operating systems, standard libraries or library versions may produce different text while preserving the intended mapping. Conversely, normalizing all differences can hide a real compatibility defect.

## Inspected change {#inspected-change}

The examined test infrastructure had recorded incidental member order and sometimes reported the first of several rejected fields. The correction sorted diagnostic keys, narrowed the misleading test claim from ordering to membership, and made an error fixture expose one relevant invalid field. Some test-owned dictionaries were changed to containers with a defined iteration order.

These are different interventions:

- Sorting a diagnostic representation removes an irrelevant presentation difference.
- Renaming or narrowing an assertion stops claiming a contract that was never established.
- Making a failure fixture unambiguous isolates the behavior being tested.
- Choosing deterministic test data removes nondeterminism from the harness itself.

The source reports rerecording the oracle output and perturbing member order to check that the updated suite remained stable. Those runs were not repeated here. All meaningful changed golden lines and the normalization and fixture patches were read; unchanged detailed golden context was not exhaustively read or independently re-derived.

## Applying the lesson {#applying-the-lesson}

Before changing a golden, classify each difference as semantic, explicitly permitted, diagnostic or unexplained. State why the contract permits the normalization. Preserve an unnormalized observation for diagnosis when useful.

Keep separate tests when ordering itself matters. Property enumeration, serialization, error precedence or stable iteration can be observable API behavior even if an internal container is unordered. A sorted representation is appropriate only when the assertion is about membership or values rather than order.

Use perturbation as a check: change insertion order or the relevant test environment and verify that the invariant still holds. This is stronger than rerecording expected output from the candidate alone.

## Costs and counterexamples {#costs-and-counterexamples}

Changing a fixture's container may stop testing the unordered-container path. Moving to deterministic data is useful for one test but may require separate coverage of that production behavior.

Sorting can conceal duplicate, omission or precedence bugs if the comparison is poorly designed. Identical normalized results do not prove identical semantics. Treat unexplained differences as failures or unresolved evidence rather than expanding normalization until the suite is green.

This case establishes a bounded test-contract correction. It does not establish that every original difference was independently verified as harmless, or that every platform passed.
