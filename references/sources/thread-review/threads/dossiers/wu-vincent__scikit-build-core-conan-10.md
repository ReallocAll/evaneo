<!-- retrieval: {"source_ids":["public:thread:wu-vincent/scikit-build-core-conan:10"],"source_type":"public","date":"2026-01-27","topics":["concurrency","testing","build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="wu-vincent-scikit-build-core-conan-10-remove-future-annotations-from-settings-py"></a>
# wu-vincent/scikit-build-core-conan#10: Remove __future__ annotations from settings.py {#wu-vincent-scikit-build-core-conan-10-remove-future-annotations-from-settings-py}

Source: https://github.com/wu-vincent/scikit-build-core-conan/pull/10

Thread state: closed; merged: True.

## Problem and constraints {#problem-and-constraints}
After settings changes, scikit-build-core 0.11.6 cannot convert the build field’s deferred string annotation list[str] | str.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
deivse diagnoses postponed annotation evaluation, proposes removing the future import, and Vincent confirms the same failure.

## Implementation and attribution {#implementation-and-attribution}
Complete two-line removal patch deletes from __future__ import annotations from settings.py, letting dataclass field.type hold evaluated runtime types. It does not change the union spelling.

Diff evidence (patch inspected, not bundled): [pinned public three-dot comparison](https://github.com/wu-vincent/scikit-build-core-conan/compare/acfd2fdab5613890de7903d7004acb8569435e62...02167be91d8ddce44cf58f955b23d334800b3e9b). Declared changed files: 1.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Merged with no added tests. This resolves one layer but #11 documents another: an evaluated types.UnionType is still unsupported by older conversion logic.

## Reusable decision and costs {#reusable-decision-and-costs}
Runtime schema introspection makes annotation representation observable behavior. Postponed evaluation and union-object compatibility are separate contracts.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2026-01-30T13:48:11Z](https://github.com/wu-vincent/scikit-build-core-conan/pull/10#issuecomment-3823856159).
