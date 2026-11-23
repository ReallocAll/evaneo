<!-- retrieval: {"source_ids":["public:thread:wu-vincent/scikit-build-core-conan:9"],"source_type":"public","date":"2025-10-17","topics":["concurrency","testing","build","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="wu-vincent-scikit-build-core-conan-9-specifying-multiple-values-for-build"></a>
# wu-vincent/scikit-build-core-conan#9: Specifying multiple values for `build` {#wu-vincent-scikit-build-core-conan-9-specifying-multiple-values-for-build}

Source: https://github.com/wu-vincent/scikit-build-core-conan/issues/9

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
A single string build option cannot express Conan policies such as force-building a named pattern while also building missing packages.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent confirms limitation and promises next-version changes. Supplementary repository history establishes the actual implementation and later annotation regressions, rather than treating the promise as completion.

## Implementation and attribution {#implementation-and-attribution}
Full commits 39aa2fa31693151ce411edda7bc2192ea67eb94c and 6cc6a01573136bb9786c2bb364027e2b67fe7414 read. Settings accepts list[str] | str; _normalize_build_policy wraps a nonempty string, preserves nonempty list, defaults empty values to [missing], and passes the result directly to analyze_binaries. The same extension adds deployer/reference/update/lockfile settings, with normalized paths and explicit graph/install forwarding. Those additions are not all caused by this issue.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Feature is implemented in subsequent history; no test in the two commits. #10/#11 reveal parser compatibility regressions from the new union annotation.

## Reusable decision and costs {#reusable-decision-and-costs}
Preserve CLI multiplicity in configuration schemas and normalize once at the API boundary. Test schema conversion across supported parser versions as well as policy forwarding.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2025-10-20T23:16:39Z](https://github.com/wu-vincent/scikit-build-core-conan/issues/9#issuecomment-3424066346).
