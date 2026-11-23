<!-- retrieval: {"source_ids":["public:commit:3f0bd9e650f8c7544ff331428929dddb68758400","public:commit:804087ce224d2960bb059fcaec25b8def44c8940","public:commit:a472961a35d386ce016b0939dc3847f13c2f5255","public:commit:b474f869ccd9d94f2f3fd04159555302dd74252a","public:commit:f54a813bebbbc99617f57261ac9900a12c357892"],"source_type":"public","date":"2026-08-24","topics":["testing","build","diagnosis","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="specialized-build-images-shared-python-provenance-and-false-capability-failures"></a>
# Specialized build images: shared Python, provenance and false capability failures {#specialized-build-images-shared-python-provenance-and-false-capability-failures}

## Mechanism and attribution {#mechanism-and-attribution}
This is five changes attributed to the commit author on an existing PyPA manylinux codebase. Inherited architecture selection, verified CPython download flow, hardening logic, pre-commit and all-green workflow structure belong to upstream unless the target diff actually changes them. Parent identity is 8413de204fa10bf0414dc88df12b1535768bacca (Matthieu Darbois). The target switches CPython to a shared build and adds patchelf plus an origin-relative interpreter RPATH, making the interpreter find its adjacent library without a global absolute installation path. The message states shared-build intent; a particular embedding consumer is not named.

Publication moves from upstream Quay to EndstoneMC GHCR and the maintained matrix is explicitly reduced to manylinux_2_31 x86_64. deploy.sh computes a UTC date plus first-parent daily build count, keeps latest, and has a dry-run mode. That naming is inherited context, not invented target provenance work. A version-like tag improves traceability compared with latest but is not an immutable digest or tested rollback mechanism. The final build workflow still carries a pypa-only cache-login condition and a quay-only multiarch branch; those differ from the active fork deployment gate. No claim that either breaks the actual service is made without execution.

The derivative LLVM20 image moves LLVM/libc++ apt work out of every downstream build. Its main workflow depends on successful base builds; a standalone manual workflow route also exists. It SHA-pins actions and disables persisted checkout credentials, while base/output latest tags and apt packages remain mutable. Pinning an action does not prove full build reproducibility.

## Diagnostic case {#diagnostic-case}
The final one-line package fix has unusually strong explicit rationale: CMake's Ninja C++20 module dependency scanner invokes clang-scan-deps. Without clang-tools the executable is missing; try_compile exits 127, which upstream feature detection can present as the platform lacking the tested capability. Check process launch failure and required tools before accepting a negative compile probe. This preserves the reported causal mechanism without claiming a reproduced compiler run or extrapolating to every probe failure.

## Practical limits {#practical-limits}
Source/CMake/build-image review is static. No source signature verification was actually run, no Docker image built, no package publishing attempted and no downstream runtime validated. The copied final files are context for the five changes, not evidence that all PyPA history was reviewed. No excluded Nukkit history is involved.

## Complete per-SHA navigation {#complete-per-sha-navigation}

- [01 a472961a35d3 — feat: build python with `--enable-shared`](dossiers/01-a472961a35d386ce016b0939dc3847f13c2f5255.md)
- [02 b474f869ccd9 — refactor: change registry from `quay.io` to `ghcr.io`](dossiers/02-b474f869ccd9d94f2f3fd04159555302dd74252a.md)
- [03 f54a813bebbb — ci: build only manylinux_2_31_x86_64](dossiers/03-f54a813bebbbc99617f57261ac9900a12c357892.md)
- [04 3f0bd9e650f8 — ci: publish a manylinux image with LLVM preinstalled](dossiers/04-3f0bd9e650f8c7544ff331428929dddb68758400.md)
- [05 804087ce224d — fix: install clang-tools for clang-scan-deps](dossiers/05-804087ce224d2960bb059fcaec25b8def44c8940.md)
