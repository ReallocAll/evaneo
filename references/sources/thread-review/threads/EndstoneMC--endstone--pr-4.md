<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:4"],"source_type":"public","date":"2024-01-30","topics":["testing","build","api","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-4-refactor-project-structure"></a>
# EndstoneMC/endstone #4: refactor: project structure {#endstonemc-endstone-4-refactor-project-structure}

Source: https://github.com/EndstoneMC/endstone/pull/4

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (196 additions, 205 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu's merged project-layout refactor has no body, comments, or reviews. The full exact base/head diff was inspected, including the deleted component CMake files; byte-identical renames are explicitly identified by Git rather than treated as newly authored implementations. Headers move to include/, native code to src/, Python to python/src with python/tests, and C++ tests to tests/. The public CMake/Conan component changes from endstone::api to endstone::headers, requiring downstream target-name updates; the test-package change demonstrates that migration.

The root CMake file consolidates package discovery, header/interface target, Python module, core, runtime and test target. Python Development replaces separately requested Module/Embed components. Runtime still links embedded Python and platform hooking dependencies; UNIX hidden visibility/exclude-libs options remain. Python module installation is now only the optional wheel-component destination, whereas its previous general library installation is removed. GTest remains required even when BUILD_TESTING is OFF. The old configure-time version guard is replaced with a source preprocessor check, but CMake still always defines ENDSTONE_VERSION, so this does not itself reject an empty version value. Conan removes explicit headers dependencies from core/runtime component metadata even though root CMake links core publicly to headers; consumers of exported metadata deserve separate validation.

CI moves from next to main, splits Linux build and coverage, updates wheel test locations, and labels workflows more simply. Docker builds default branch rather than explicitly cloning next; latest tags use default-branch metadata. Wheel and setuptools-scm source paths follow the new layout. This is packaging/API-consumer surface work, not merely folder cosmetics. No tests were run and no reviewer rationale is invented. Exact inspected base/head: 1556f4c0b6d505b9966e84ad7c57b4c5c73f18d4…eb3e71991df4dad4d5c25b3f421443b756e5ff13.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/4
