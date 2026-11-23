<!-- retrieval: {"source_ids":["public:thread:conan-io/conan-center-index:22224"],"source_type":"public","date":"2024-01-09","topics":["concurrency","testing","build","diagnosis","documentation","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="conan-io-conan-center-index-22224-funchook-add-funchook-1-1-3-recipe"></a>
# conan-io/conan-center-index#22224: funchook: add funchook/1.1.3 recipe {#conan-io-conan-center-index-22224-funchook-add-funchook-1-1-3-recipe}

Source: https://github.com/conan-io/conan-center-index/pull/22224

Thread state: closed; merged: False.

## Problem and constraints {#problem-and-constraints}
Package funchook 1.1.3 with a reproducible Conan dependency instead of upstream-discovered/downloaded disassemblers. Windows and Linux are supported; macOS is explicitly rejected by the recipe although imported test conditionals mention it.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
The first PR #22200 was stopped by scope gates: it changed another library and later mixed recipe/configuration changes. #22224 resubmitted the recipe but its Linux GCC 11 consumer execution failed after successful compilation: get_val_in_exe could not be found through runtime symbol lookup. Both Conan 1 Debug and Conan 2 Release logs show the same first-test failure. No human review diagnoses it in the captured conversation; the second PR eventually went stale and closed unmerged. The two final patches were found byte-identical in the source review, so implementation analysis is shared without dropping either thread.

## Implementation and attribution {#implementation-and-attribution}
All semantic hunks of the 47,016-character patch were read; the exact mechanical S(1)..S(600) sequence was verified algorithmically. Recipe pins source archive/hash, exports/applies a CMake patch, removes C++ ABI settings for C, sets static/shared/fPIC rules, and requires capstone/4.0.2. Patch forces Capstone on all platforms, replaces nested download/build with find_package(capstone CONFIG REQUIRED), links capstone::capstone and disables distorm/Zydis paths. It disables upstream build tests but imports an extensive consumer suite: DLL/executable hooks, assembly relative branches and PC thunks, ARM64 ADR/literal loads/conditional branches, file-opening redirection, 600 functions each in DLL/executable, install/uninstall restoration and expected error cases. CMake selects GAS/MASM/noasm per CPU/compiler; recipe links psapi on Windows or dl on Linux and exports modern plus legacy Conan CMake names. The failure path uses dlopen(NULL, RTLD_LAZY|RTLD_NOLOAD) then dlsym; consumer CMake does not enable executable exports or an export-dynamic flag. Missing export configuration is therefore a code-grounded likely explanation, not a recorded confirmed fix. Tests and library mechanisms must not all be credited as newly invented by the recipe submitter.

Diff evidence (patch inspected, not bundled): [public PR files-changed view](https://github.com/conan-io/conan-center-index/pull/22224/files) (live upstream diff, not the captured immutable patch). Declared changed files: 16.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Full semantic read includes assembly and C test harness; no upstream source was executed. The public CI failures are runtime, not compiler failures, and cannot support cross-platform package success. No fix/retest appears. Test code also has early-return cleanup gaps and the uint64 helper omits destroy on its success path, so copied test harness code should not be treated as production lifecycle guidance.

## Reusable decision and costs {#reusable-decision-and-costs}
A package recipe can compile successfully yet fail its consumer contract because symbol visibility, runtime loader paths or assembly selection differ from upstream’s test build. Preserve external dependency provenance, scope one library per contribution, and test actual exported interfaces before claiming distribution support.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [conan-center-bot · 2024-01-09T14:14:37Z](https://github.com/conan-io/conan-center-index/pull/22224#issuecomment-1883125225).
- [github-actions[bot] · 2025-02-17T06:40:51Z](https://github.com/conan-io/conan-center-index/pull/22224#issuecomment-2662191597).
- [github-actions[bot] · 2025-03-19T06:41:59Z](https://github.com/conan-io/conan-center-index/pull/22224#issuecomment-2735502339).
