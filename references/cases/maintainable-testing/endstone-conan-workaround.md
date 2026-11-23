<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2026-07-17","topics":["testing","maintainability","complexity","review","build","dependency","api"],"limitations":"Static review of linked primary sources and bundled historical analyses; upstream tests were not executed. Historical claims and code changes are distinguished from proven runtime outcomes."} -->
# Endstone #439: remove private Conan cache code after upstream takes ownership {#case}

## Observed change {#changes}

In [PR #439](https://github.com/EndstoneMC/endstone/pull/439), contributor czoido showed that `conan-py-build` v0.6 already cleaned the temporary export-package cache when copying the built wheel. Endstone's own override of a private Conan `export_pkg` implementation was therefore redundant and exposed the project to future internal API breakage. The patch deletes the **107-line** custom method and raises the build dependency floor to `conan-py-build>=0.6.0`. Maintainer wu-vincent supported the simplification. [Maintainer discussion](https://github.com/EndstoneMC/endstone/pull/439#issuecomment-5003514084).

## Judgment {#reading}

Before adding maintenance code that reaches into a dependency's private methods, check whether the dependency already provides the needed contract. Removing duplicated responsibility can be a stronger maintenance improvement than covering that private workaround with tests.

## Limit {#limits}

The related review at [EndstoneMC--endstone--pull_request-439.md](../../sources/thread-review/threads/EndstoneMC--endstone--pull_request-439.md) inspected the PR patch; the upstream build helper's implementation and real wheel lifecycle were not rerun for this supplement. Verify the dependency's promised version and cache behavior in the current build before deleting an equivalent workaround elsewhere.
