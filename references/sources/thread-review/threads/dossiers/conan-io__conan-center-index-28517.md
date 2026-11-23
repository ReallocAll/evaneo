<!-- retrieval: {"source_ids":["public:thread:conan-io/conan-center-index:28517"],"source_type":"public","date":"2025-10-04","topics":["concurrency","testing","build","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="conan-io-conan-center-index-28517-llvm-core-add-version-20-1-6"></a>
# conan-io/conan-center-index#28517: llvm-core: add version `20.1.6` {#conan-io-conan-center-index-28517-llvm-core-add-version-20-1-6}

Source: https://github.com/conan-io/conan-center-index/pull/28517

Thread state: open; merged: False.

## Problem and constraints {#problem-and-constraints}
llvm-openmp/20.1.6 with build_libomptarget=True requires a missing llvm-core/20.1.6 package.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
The body claims no functional changes beyond adding a version. Actual patch also changes target selection and includes LLVM-20-specific dependency adaptation; this mismatch is preserved rather than adopting the summary. No reviews/comments are captured.

## Implementation and attribution {#implementation-and-attribution}
Full four-file patch pins LLVM and CMake archives/hashes, registers 20.1.6, adds SPIRV, and ports patches for zlib variable naming, editline package/target names, and zstd/libxml2 library resolution. At exact head 3708289b301e7febd7ff47e7fdd3c3dbf15ac1e4, the module-level LLVM_TARGETS is a mutable set. _all_targets assigns that same set then uses -= to remove SPIRV for <20 and LoongArch/VE for <14. Unlike the old non-mutating set subtraction, this mutates global state and can contaminate later recipe instances/properties in the same process. Relevant declaration/helper were inspected at the named PR head; the rest of that acquired full recipe is not claimed fully reviewed.

Diff evidence (patch inspected, not bundled): [public PR files-changed view](https://github.com/conan-io/conan-center-index/pull/28517/files) (live upstream diff, not the captured immutable patch). Declared changed files: 4.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Open and unmerged in captured state; only a local-test checklist claim. No automated evidence in discussion. The state contamination is a static code finding, not a reproduced runtime failure.

## Reusable decision and costs {#reusable-decision-and-costs}
Version additions can require real compatibility logic. Copy mutable global capability sets before filtering; review behavior separately from a no-functional-change description.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
