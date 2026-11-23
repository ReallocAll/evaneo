<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2024-05-14","topics":["testing","maintainability","complexity","review","python","dependency","api"],"limitations":"Static review of linked primary sources and bundled historical analyses; upstream tests were not executed. Historical claims and code changes are distinguished from proven runtime outcomes."} -->
# Endstone historical loader: custom import fallback gives way to standard entry points {#case}

## Historical revision chain {#changes}

The bundled code review [05-build-bootstrap-plugins.md](../../sources/commit-review/endstone-0841-0960/05-build-bootstrap-plugins.md) documents an import mechanism that became more complex before it simplified. Commit [7e4541c8](https://github.com/EndstoneMC/endstone/commit/7e4541c8817179be6d04c05db33ea93faf4701c6) added a hand-built Python module import-by-spec loader for wheel plugins and plugin dependency installation. It broke editable installs. Commit [cf44942e](https://github.com/EndstoneMC/endstone/commit/cf44942e1362caf9e8a6818f0a6f182a4e24e7bc) first tried the standard entry point and then a custom fallback, increasing paths and making missing-plugin versus missing-dependency errors ambiguous. Commit [712c80fc](https://github.com/EndstoneMC/endstone/commit/712c80fcaf7248e803a7c36c39998f4566a9970a) removed the custom loader and derived the Python user site using the standard API.

## Judgment {#reading}

Interoperability with a mature runtime rarely justifies a parallel loader merely to anticipate corner cases. Prefer standard import and entry-point contracts. A compatibility fallback must have a demonstrated consumer and an unambiguous error predicate, or it becomes a permanent second subsystem to maintain and test.

## Limit {#limits}

This is retrospective code review, not a package installation reproduced today. Shared dependency state and installer error handling are separate unresolved design topics.
