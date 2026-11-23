<!-- retrieval: {"source_ids":["public:commit:caf77eaeacdf6d1d5e65cfaf47020580bcfdcdb3"],"source_type":"public","date":"2026-02-24","topics":["testing","build","review","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="008-refactor-update-cmake-paths-for-new-directory-layout"></a>
# 008. refactor: update CMake paths for new directory layout {#008-refactor-update-cmake-paths-for-new-directory-layout}

Repository: wu-vincent/RakNet

SHA: `caf77eaeacdf6d1d5e65cfaf47020580bcfdcdb3`

[Public commit](https://github.com/wu-vincent/RakNet/commit/caf77eaeacdf6d1d5e65cfaf47020580bcfdcdb3) | [Detailed case RN01](../cases/build-modernization-and-reversals.md)

## Engineering finding {#engineering-finding}

Updates root subdirectories, source/header globs, build include path and Irrlicht cross-reference; adds RAKNET_ENABLE_TESTS and removes redundant generated-header-copy option. Install path now derives from include/RakNet. Separate commit repairs references after007; neither tree was built here.

## Causal and attribution context {#causal-and-attribution-context}

Author identity comes from the exact GitHub-linked target occurrence, not from committer or repository ownership. Authored 2026-02-24T15:05:13Z; committed 2026-02-24T15:05:13Z. Parents: 7ff77454194958eaa8091c9f78dd619af6ae00a8. DAG rank 7; display index is not a topological claim. The linked case traces initial choices, later changes, final state and applicability.

- Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

### Commit message {#complete-guarded-message}

> refactor: update CMake paths for new directory layout
> 
> Update glob paths in src/CMakeLists.txt, subdirectory references in
> root CMakeLists.txt, cross-references in IrrlichtDemo, and tests
> CMakeLists.txt to match the restructured directory layout.
> 
> Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

## Reviewed surfaces {#reviewed-surfaces}

- CMakeLists.txt
- DependentExtensions/IrrlichtDemo/CMakeLists.txt
- src/CMakeLists.txt
- tests/CMakeLists.txt

Review scope: The commit message and meaningful residual changes were reviewed after exact-blob and line-ending accounting. Structural matches do not establish semantic review of inherited code.

## Limits {#limits}

- No upstream build, tests, binaries, package installation, platform execution, workflow run or live peer exchange was performed.
- Commit messages and source comments establish declared rationale; code-derived risks are static inferences.
