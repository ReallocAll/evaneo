<!-- retrieval: {"source_ids":["public:thread:wu-vincent/scikit-build-core-conan:8"],"source_type":"public","date":"2025-06-04","topics":["concurrency","ffi","testing","build","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="wu-vincent-scikit-build-core-conan-8-building-wheels-fails-since-scikit-build-core-v0-11-4"></a>
# wu-vincent/scikit-build-core-conan#8: Building wheels fails since scikit-build-core v0.11.4 {#wu-vincent-scikit-build-core-conan-8-building-wheels-fails-since-scikit-build-core-v0-11-4}

Source: https://github.com/wu-vincent/scikit-build-core-conan/issues/8

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Minimal wheel project fails to import the build backend with scikit-build-core 0.11.4; pinning 0.11.3 works. Reproducer supplies pyproject, Conan pybind11 dependency, CMake and a one-function binding.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent acknowledges and announces fix in 0.7.1; reporter thanks. The exact linked historical implementation was located by the issue-closing commit.

## Implementation and attribution {#implementation-and-attribution}
Full commit 29f76292233018266091461210f66bd38e5846f8 read: import correctly spelled process_overrides first, fall back on ImportError to older misspelled process_overides aliased to the new spelling, and call the unified name. SettingsReader import remains direct.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Static change matches the backend-import version boundary; no test added in this commit. Thanks is not an explicit independent successful build log.

## Reusable decision and costs {#reusable-decision-and-costs}
Compatibility adapters around upstream internal APIs should normalize spelling/version differences at one boundary; keep a minimal build-backend import reproducer separate from native compilation.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2025-06-05T00:16:24Z](https://github.com/wu-vincent/scikit-build-core-conan/issues/8#issuecomment-2942136577).
- [wu-vincent · 2025-06-05T12:30:28Z](https://github.com/wu-vincent/scikit-build-core-conan/issues/8#issuecomment-2944054658).
- [mreininghaus · 2025-06-05T14:10:42Z](https://github.com/wu-vincent/scikit-build-core-conan/issues/8#issuecomment-2944616411).
