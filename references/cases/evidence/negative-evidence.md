<!-- retrieval: {"source_type":"static_review","topics":["research","audit","evidence","code-review","search","testing","self-correction"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="bound-negative-claims-by-the-search-that-produced-them"></a>

# Bound negative claims by the search that produced them {#bound-negative-claims-by-the-search-that-produced-them}

## Problem {#problem}

“No caller uses this,” “all variants behave alike,” and “the implementation already matches” sound stronger than a partial search supports. A truncated result set can hide the only relevant caller. Several similar examples can all exercise the same branch.

## Inspected correction chain {#inspected-correction-chain}

One audit initially treated a limited cross-reference listing as evidence that an ownership operation was absent. A later note examined additional callers and described separate copy, move and reference-transfer paths. The useful correction was methodological: absence in the displayed subset did not establish absence in the relevant program.

A separate audit generalized from several string-valued examples to all enumeration objects. Revisiting the dispatch branches exposed a distinct numeric-valued case. Focused tests were added for forward and reverse lookup and property attributes. The inspected notes continued to report a mismatch for that branch; the presence of tests did not establish a completed implementation fix.

Another correction distinguished registration order from the order a consumer actually tries alternatives. A surprising producer representation was not, by itself, evidence of incorrect consumer behavior.

These are documented audits and inspected test changes. The underlying reference executable was not independently analyzed or executed in this review.

## A usable negative-evidence record {#a-usable-negative-evidence-record}

For each absence claim, record:

- The source revision and subsystem searched
- Query, result cap, pagination and filtering
- Whether wrappers, templates, inlining or alternate dispatch branches can hide uses
- Which caller categories and behavior variants were actually checked
- What observation would falsify the conclusion

“None in the inspected callers” is a useful bounded result. Promote it to a broader claim only after closing the relevant coverage gaps.

For heterogeneous behavior, construct a small branch matrix before choosing examples. Vary representation, valid and invalid inputs, ownership mode and exceptional paths where they matter. More examples from one branch do not cover another branch.

## Costs and limits {#costs-and-limits}

Exhaustive whole-program searching can be expensive and unnecessary. Scope the claim to the decision being made; stop when the missing cases cannot change that decision, and explain why. A source-level search can still miss dynamically selected behavior.

Preserve the correction and its counterexample together. Removing an old conclusion without recording why it failed loses the most reusable lesson. No personal preference or universal audit quality is inferred from this chain.
