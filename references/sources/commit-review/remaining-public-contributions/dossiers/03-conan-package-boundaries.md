<!-- retrieval: {"source_ids":["public:commit:de1245ece15923a411e345c15a26b563fae863af","public:commit:ac95f1a5bbb3384fc291e81e12dfc4e903549985","public:commit:73e6a68d9a2e82e06b206a067d37609c05710547"],"source_type":"public","date":"2024-07-29..2025-04-09","topics":["ffi","testing","build","api","diagnosis","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="conan-package-boundaries-upstream-review-and-collateral-compatibility"></a>
# Conan: package boundaries, upstream review and collateral compatibility {#conan-package-boundaries-upstream-review-and-collateral-compatibility}

## Problem and final artifact {#problem-and-final-artifact}

[MinHook commit de1245](34-de1245ece15923a411e345c15a26b563fae863af.md) packages a Windows x86/x64 C hooking library for Conan. It adds six final files, not the library’s hooking implementation. The PR title still names cci.20240114, but both source metadata and config map use 1.3.3.cci.20240629 and pin upstream commit 91cc9466e383d13a43d7cf33c7c8fdccb27095d3 with SHA256. For exact reconstruction, final tree content outranks a stale title.

The [completed PR #22165 review](../../../thread-review/threads/dossiers/conan-io__conan-center-index-22165.md) preserves the longer decision chain: Vincent proposes packaging and explicitly disclaims original MinHook authorship; AbrilRBS asks about a fresh release; Vincent suggests a dated snapshot after an unanswered upstream request; valgur asks for CMake compatibility changes; memsharded later supplies a future-proof versioning revision. Final commit trailers explicitly credit Martin Valgur and memsharded. Their review/version decisions must stay attached to the case. An earlier CMake patch discussed in review is absent from the final six-file result; do not invent it into the final recipe.

## Boundary choices visible in code {#boundary-choices-visible-in-code}

The recipe removes compiler.cppstd/libcxx because the library is C, rejects non-Windows and non-x86-family targets, supports static/shared options, uses CMake layout/toolchain generation, installs the upstream license and removes upstream CMake package metadata under lib/minhook. It selects actual library names with x32/x64 and Debug suffixes. These operations describe dependency/package integration; they do not establish native hook correctness across every compiler or Windows version.

The consumer test is stronger than a header-only compile probe: CMake resolves minhook::minhook, Conan supplies VirtualRunEnv, and can_run avoids blindly executing a cross-built target. A dummy MessageBox-style function permits nonmodal hook lifecycle exercise: initialize, create disabled hook, enable, invoke trampoline-backed detour, disable, invoke again, uninitialize. Every API status can fail the process. The strings expected on stdout are comments rather than assertions, so the test does not prove the hooked/unhooked output. The dummy’s fixed-width formatting is suitable only for the short test strings; it is not a general renderer. These limits were found by source reading, not running the binary.

Captured Conan bots report success and maintainers approve/merge. That is source-reported CI evidence; this review did not reproduce it. Preserve the distinction among added test design, reported test results and independently measured outcomes.

## Two small changes with different evidential weight {#two-small-changes-with-different-evidential-weight}

[EnTT ac95f1](35-ac95f1a5bbb3384fc291e81e12dfc4e903549985.md) registers version 3.14.0 URL/hash and existing recipe-folder mapping. It has a concise no-independent-lesson disposition; commit authored no EnTT algorithm. Bots mention subsets of builds, which must not become an exhaustive matrix claim.

[GLEW 73e6a6](36-73e6a68d9a2e82e06b206a067d37609c05710547.md) raises both maintained upstream CMake-patch minima from 2.8.12 to 3.5 for CMake 4 compatibility. It also raises required_conan_version from 1.53 to 2.1. That support drop is substantive despite the short compatibility title. [PR #27188](https://github.com/conan-io/conan-center-index/pull/27188) supplies approval and a local-test checklist, not an attached detailed regression matrix.

## Transfer and counterconditions {#transfer-and-counterconditions}

Use this case when adding a dependency recipe or reviewing a compatibility fix: establish the true source/version identity, supported OS/architecture/client matrix, link target, debug naming, runtime environment and test oracle. Preserve upstream authorship and maintainer changes. A minimal version bump is not an architecture lesson; a seemingly tiny minimum-version fix may materially narrow consumers. No artifact download/hash recomputation, package build, native execution or publishing occurred here.
