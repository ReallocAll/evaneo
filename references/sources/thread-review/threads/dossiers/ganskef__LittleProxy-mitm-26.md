<!-- retrieval: {"source_ids":["public:thread:ganskef/LittleProxy-mitm:26"],"source_type":"public","date":"2017-03-05","topics":["concurrency","testing","api","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="ganskef-littleproxy-mitm-26-use-guava-instead-of-common-io"></a>
# ganskef/LittleProxy-mitm#26: Use Guava instead of Common-IO {#ganskef-littleproxy-mitm-26-use-guava-instead-of-common-io}

Source: https://github.com/ganskef/LittleProxy-mitm/issues/26

Thread state: open; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
LittleProxy 1.1.1 removed the transitive Commons-IO dependency, requiring consumers of littleproxy-mitm to add it explicitly.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent proposes using already-present Guava instead; no reply, benchmark or accepted implementation.

## Implementation and attribution {#implementation-and-attribution}
No code patch is supplied. This is a dependency-contract proposal, not proof that all used Commons-IO methods have equivalent Guava replacements.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Open in captured state; migration not verified.

## Reusable decision and costs {#reusable-decision-and-costs}
Declare direct runtime dependencies instead of relying on another library’s incidental transitive graph; replacement requires API/behavior checking.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
