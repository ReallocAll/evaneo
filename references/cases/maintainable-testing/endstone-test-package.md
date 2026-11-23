<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2024-04-06","topics":["testing","maintainability","complexity","review","duplicate-tests","build","test-harness"],"limitations":"Static review of linked primary sources and bundled historical analyses; upstream tests were not executed. Historical claims and code changes are distinguished from proven runtime outcomes."} -->
# Endstone historical test_package: delete a duplicate GTest facility {#case}

## Observed change {#changes}

Maintainer wu-vincent's [commit 3496014c](https://github.com/EndstoneMC/endstone/commit/3496014cbcf787e1c589f6bd274ea63f74bd2647) removed the standalone `test_package_` directory. Its commit subject explicitly says the checks were already covered by GTest. Five paths disappeared, including Conan/CMake setup and sample plugin/server programs, for **317 deleted lines and no additions** in the patch.

## Judgment {#reading}

Two independently maintained test packages that protect the same contract create duplicate compilation paths, tooling and update obligations. Prefer the smallest existing authoritative test facility. If the packaging tool must additionally prove real downstream installation, preserve one distinct consumer smoke test rather than treating all duplication as harmless.

## Limit {#limits}

The commit explains its reason but does not include a complete coverage mapping of every deleted check. It proves removal of a test package, not that equivalent coverage was independently verified here.
