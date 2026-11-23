<!-- retrieval: {"source_ids":["public:thread:wu-vincent/scikit-build-core-conan:6"],"source_type":"public","date":"2025-01-10","topics":["concurrency","testing","build","performance","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="wu-vincent-scikit-build-core-conan-6-splitting-profiles-for-host-and-build-once-again"></a>
# wu-vincent/scikit-build-core-conan#6: Splitting profiles for host and build once again {#wu-vincent-scikit-build-core-conan-6-splitting-profiles-for-host-and-build-once-again}

Source: https://github.com/wu-vincent/scikit-build-core-conan/pull/6

Thread state: closed; merged: True.

## Problem and constraints {#problem-and-constraints}
Conan API migration in 0.5.2 unexpectedly applies host overrides to build tools, causing prebuilt binaries in another remote not to match.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
mijoku explains that <=0.5.1 CLI only modified host profile, requests restoration and gives the missed-binary symptom. Vincent acknowledges missed review and approves.

## Implementation and attribution {#implementation-and-attribution}
Full one-file patch creates host profile with wheel build_type and user overrides, creates build profile from selected/default base without overrides, prints both before graph calculation and passes separate objects to load_graph_consumer. It also removes a stray conan_api.install expression.

Diff evidence (patch inspected, not bundled): [pinned public three-dot comparison](https://github.com/wu-vincent/scikit-build-core-conan/compare/99994f7cd75a53220a36ada6e295379de4780426...a15e56b7d65f691a6c634953d815be6f0d548910). Declared changed files: 1.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Merged. Clear before/after behavior explanation and concrete report, but no automated graph comparison included. Shared profile path remains a limitation; separate host/build profile-file settings arrive elsewhere.

## Reusable decision and costs {#reusable-decision-and-costs}
Compiler/build-tool execution context and output target context are distinct. Preserve native tool package identity when changing target settings and print resolved profiles before diagnosing missing binaries.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [mijoku · 2025-02-05T14:34:48Z](https://github.com/wu-vincent/scikit-build-core-conan/pull/6#issuecomment-2637022771).
- [wu-vincent · 2025-02-05T15:15:29Z](https://github.com/wu-vincent/scikit-build-core-conan/pull/6#issuecomment-2637194404).
