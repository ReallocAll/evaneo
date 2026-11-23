<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:471"],"source_type":"public","date":"2026-08-09","topics":["testing","build","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-471-replace-fetchcontentdeclare-with-plain-findpackage-for-expected-lite"></a>
# EndstoneMC/endstone #471: Replace `FetchContent_Declare()` with plain `find_package()` for `expected-lite`. {#endstonemc-endstone-471-replace-fetchcontentdeclare-with-plain-findpackage-for-expected-lite}

Source: https://github.com/EndstoneMC/endstone/pull/471

## Evidence and attribution {#evidence-and-attribution}

Primary author: micich. Created 2026-08-09T08:19:24Z; recorded state closed; merged False.

micich proposes mandatory find_package(expected-lite), partly from a larger fmt/spdlog upgrade effort. Wu rejects it because public header-only CMake consumers need a QUIET lookup plus FetchContent fallback without Conan; moving REQUIRED before the subproject return would break the plugin template, while the complete Conan build already finds the package. micich accepts the overlooked consumer path. Dependency discovery must cover embedders, not just the project's own full build.

## Direct patch findings {#direct-patch-findings}

Moves expected-lite REQUIRED before add_subdirectory(include)/subproject early-return and deletes QUIET+FetchContent v0.8.0 fallback. Confirms reviewer consumer-build objection.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (973 characters; SHA-256 fb17dabc46e962f81347a68540d2a5351b7ae252c0935a91c2bbe8b32fc9d9ea), head 643feccd5d94db294dd98d1a9c81527b4eef6794. This covers the supplied PR patch, not unrelated commits or historical intermediate revisions. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/471
- https://github.com/EndstoneMC/endstone/pull/471#issuecomment-5231361662
- https://github.com/EndstoneMC/endstone/pull/471#issuecomment-5233271268
