<!-- retrieval: {"source_ids":["public:thread:conan-io/conan-center-index:27188"],"source_type":"public","date":"2025-04-08","topics":["concurrency","testing","build","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="conan-io-conan-center-index-27188-glew-cmake-4-support"></a>
# conan-io/conan-center-index#27188: glew: CMake 4 support {#conan-io-conan-center-index-27188-glew-cmake-4-support}

Source: https://github.com/conan-io/conan-center-index/pull/27188

Thread state: closed; merged: True.

## Problem and constraints {#problem-and-constraints}
GLEW builds fail under CMake 4 because the existing project minimum falls below supported policy compatibility.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent proposes raising the minimum to 3.5; perseoGI approves.

## Implementation and attribution {#implementation-and-attribution}
Full three-file patch updates two shipped CMake patches from minimum 2.8.12 to 3.5, and also raises required_conan_version from >=1.53.0 to >=2.1. This latter client-support change is real despite not being called out in the short motivation.

Diff evidence (patch inspected, not bundled): [public PR files-changed view](https://github.com/conan-io/conan-center-index/pull/27188/files) (live upstream diff, not the captured immutable patch). Declared changed files: 3.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Merged; local test is asserted in checklist, no detailed matrix or regression test appears.

## Reusable decision and costs {#reusable-decision-and-costs}
Check compatibility-repair diffs for collateral toolchain support drops; increasing one minimum can make the package unavailable to previously supported clients.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [perseoGI · 2025-04-09T11:05:02Z](https://github.com/conan-io/conan-center-index/pull/27188#pullrequestreview-2753086617).
