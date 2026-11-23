<!-- retrieval: {"source_ids":["public:thread:wu-vincent/scikit-build-core-conan:11"],"source_type":"public","date":"2026-01-31","topics":["concurrency","testing","build","api","documentation","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="wu-vincent-scikit-build-core-conan-11-v0-9-1-breaks-with-typeerror-cannot-create-types-uniontype-instances"></a>
# wu-vincent/scikit-build-core-conan#11: v0.9.1 breaks with TypeError: cannot create 'types.UnionType' instances {#wu-vincent-scikit-build-core-conan-11-v0-9-1-breaks-with-typeerror-cannot-create-types-uniontype-instances}

Source: https://github.com/wu-vincent/scikit-build-core-conan/issues/11

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
With 0.9.x, explicitly setting build=missing causes types.UnionType instantiation failure; leaving the field unset or using 0.8.0 avoids it.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
martinezlc99 identifies UnionType versus typing.Union and contributes an upstream fix (#1214, reported merged). mreininghaus confirms the configuration sensitivity. Vincent chooses a local backward-compatible Union[A,B] spelling rather than waiting for users to upgrade scikit-build-core.

## Implementation and attribution {#implementation-and-attribution}
Full a1e79964eb6a87ba8e046a762e175d98aa0b8c7d patch read: imports List/Union, changes build to Union[List[str], str], documents the older-parser reason, bumps version 0.9.2 and updates changelog. Commit date is February 2026; changelog says 2025, a documentation inconsistency, not a reliable release date.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Closed with release-fix announcement. Upstream #1214 is a collaborator-reported separate solution not independently reviewed here; local compatibility mechanism is verified. No test or reporter retest after 0.9.2 appears.

## Reusable decision and costs {#reusable-decision-and-costs}
When upstream adds support for a newer runtime type, a downstream compatibility spelling can preserve the broader supported version range. Validate both default and explicitly supplied settings, because default values may bypass converter failures.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [mreininghaus · 2026-02-02T13:23:58Z](https://github.com/wu-vincent/scikit-build-core-conan/issues/11#issuecomment-3835103063).
- [martinezlc99 · 2026-02-03T04:20:51Z](https://github.com/wu-vincent/scikit-build-core-conan/issues/11#issuecomment-3838967160).
- [wu-vincent · 2026-02-04T12:59:17Z](https://github.com/wu-vincent/scikit-build-core-conan/issues/11#issuecomment-3847307666).
