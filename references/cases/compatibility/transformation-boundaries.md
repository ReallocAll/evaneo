<!-- retrieval: {"source_type":"static_review","topics":["numeric-conversion","C++","boundaries","compatibility","testing","proof","self-correction"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="check-the-value-at-the-transformation-boundary"></a>

# Check the value at the transformation boundary {#check-the-value-at-the-transformation-boundary}

## Problem {#problem}

A numeric conversion can have several stages: receive a floating-point input, transform it, check whether an integer representation is valid, then choose an output format. Testing the wrong intermediate value can reject an input whose transformed value is representable.

## Inspected change {#inspected-change}

An implementation checked the raw input against an integer range even though the intended behavior depended on the value after truncation. A correction moved the range decision to the transformed value. Tests exercised representable floating-point neighbors immediately outside the integer endpoints, where a small fractional excess disappears under truncation.

An earlier audit had described the range guard as already sufficient. The later implementation and adjacent-value tests narrowed that claim. This is a concrete example of a plausible proof skipping a transformation step, rather than evidence that every range check should move after conversion.

Exact product outputs, proprietary reference details and original constants are unnecessary for the general lesson and are omitted.

## Review method {#review-method}

Write the stages in their actual order. Give each stage its own domain and failure conditions. Ask whether the guard protects the original input, the transformed mathematical value, or the machine conversion itself.

Do not perform a potentially invalid machine cast merely to discover whether the cast is valid. Establish a safe predicate in a representation that can express the relevant conditions first.

Test:

- Values on each boundary
- The next representable floating-point value on both sides
- Fractional values that transform onto the boundary
- Values that remain outside after transformation
- Non-finite values and signed zero when the contract distinguishes them

The last two categories are proposed coverage questions, not claims that the inspected patch tested every one.

## Applicability and limits {#applicability-and-limits}

This matters in serialization, numeric formatting, language bridges and compatibility work. It also applies to normalization, rounding and unit conversion when validation and transformation do not commute.

Sometimes the contract intentionally rejects the original input even if a later transformation would make it valid. Then moving the guard changes the contract. First establish the observable rule, then place the predicate.

The patch and tests were read but not run. Reported reference behavior remains source-reported. A handful of adjacent cases improves the proof but does not prove every floating-point path or platform correct.
