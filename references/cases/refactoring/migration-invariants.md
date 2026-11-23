<!-- retrieval: {"source_type":"static_review","topics":["C++","refactoring","containers","lifecycle","invariants","termination","code-review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="preserve-progress-identity-and-polarity-during-mechanical-looking-migrations"></a>

# Preserve progress, identity and polarity during mechanical-looking migrations {#preserve-progress-identity-and-polarity-during-mechanical-looking-migrations}

## Problem {#problem}

Replacing a custom container or renaming a lifecycle flag can look syntactic while changing the behavior that callers rely on. Similar method names do not establish equivalent contracts.

## Inspected contrasting changes {#inspected-contrasting-changes}

One queue migration correctly replaced a consuming read with a peek followed by removal. Another migration replaced a consuming read with a peek alone inside a loop whose condition was the source queue's size. The destination grew while the source did not shrink. Latest observed context still contained that shape.

A lifecycle flag was also renamed from a negative condition to its positive counterpart. Some guards retained their old comparison, so the newly active state still selected an early-return path. These are static findings, not executed failures or measured user impact.

A separate map migration made identity explicit in the key instead of deriving ordering from the first element of a mutable payload. That avoided requiring a partially constructed payload to already contain an element before it could participate in lookup.

Together these changes show why container and naming migrations deserve invariant-level review even when the intended feature set is unchanged.

## Review checklist {#review-checklist}

For each replaced operation, compare consumption, ownership transfer, invalidation, ordering, allocation and failure behavior. Check the old API contract directly; a method named “pop” may return and remove, while the replacement separates those operations.

For every loop, identify a progress measure. If termination depends on a collection becoming empty, show exactly which operation reduces it on every continuing path. A changing destination is not evidence that the source is being drained.

For a polarity-changing rename, write a truth table for old and new states. Review initialization, transitions and every read. A project-wide textual rename cannot prove the comparisons still mean the same thing.

For identity changes, separate a stable key from mutable payload where appropriate. Verify insertion, empty construction, lookup and deletion, including transient states between those steps.

## Verification and tradeoffs {#verification-and-tradeoffs}

Use empty, single-element and multi-element queue cases; a bounded-step check can expose non-progress without hanging an entire test suite. Exercise operations before initialization, while active and after shutdown. Add transitions rather than only testing the final state.

Explicit keys may duplicate data, and standard containers can change invalidation or performance characteristics. Neither migration establishes that one container is always faster or preferable.

No upstream tests or builds were run. The case preserves generic invariants and source-level counterexamples; it does not establish a repository-wide defect audit.
