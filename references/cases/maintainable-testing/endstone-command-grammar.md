<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2026-10-17","topics":["testing","maintainability","complexity","review","api","protocol","regression"],"limitations":"Static review of linked primary sources and bundled historical analyses; upstream tests were not executed. Historical claims and code changes are distinguished from proven runtime outcomes."} -->
# Endstone #554: use the existing command grammar and remove an unnecessary test detour {#case}

## Mechanism {#changes}

Contributor FETXU's [PR #554](https://github.com/EndstoneMC/endstone/pull/554) diagnosed a client command-parser collision for `/ban` and `/ban-ip`. The initial patch changed the target/reason argument shape, and provided live and C++ regression tests. Maintainer wu-vincent observed that native `message` arguments already match empty input and should be registered as required, analogous to the vanilla `/kick` command. The [second commit](https://github.com/EndstoneMC/endstone/commit/1a3040e1317d) restored the multiword `message` semantics rather than changing the reason to `str`.

Comparing PR revisions to the same first-commit parent, the initial change was **+48/−11**; after the second commit, **+37/−11**. The new C++ command-usage parser test is no longer in the revised patch, while the relevant Python command test remains. [Maintainer discussion](https://github.com/EndstoneMC/endstone/pull/554#issuecomment-6243144964).

## Judgment {#reading}

When an existing parser's semantics are misunderstood, a local compatibility workaround can induce extra tests for an invented behavior. Correct the common protocol boundary first; preserve regression checks for the observable client crash and command behavior, rather than a test of the abandoned workaround.

## Limit {#limits}

PR final-base comparisons can shift with merges; figures here compare the early two revisions to a fixed parent. The C++ test's removal is a diff observation, not proof that all possible command grammars are covered.
