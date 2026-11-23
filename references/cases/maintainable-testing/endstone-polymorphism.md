<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2026-04-05","topics":["testing","maintainability","complexity","review","api","refactor","abstraction"],"limitations":"Static review of linked primary sources and bundled historical analyses; upstream tests were not executed. Historical claims and code changes are distinguished from proven runtime outcomes."} -->
# Endstone #357: replace repeated type-specific branches with one justified generic hook {#case}

## Observed change {#changes}

[PR #357](https://github.com/EndstoneMC/endstone/pull/357), by wu-vincent, replaced numerous hand-maintained `asXxx()` virtual-type methods with `Object::as<T>()`/`is<T>()`, backed by existing EnTT type metadata. The former structure required touching base classes, concrete overrides and Python dispatch lists when a type was added.

A follow-up [9f129e45](https://github.com/EndstoneMC/endstone/commit/9f129e45789ecc0f04833e17e3c15d79dc0afb14) replaced the `poly_dispatch` infrastructure with one generic polymorphic type hook and changed two paths (**+18/−79 lines**).

## Judgment {#reading}

Avoid both indiscriminate abstractions and mechanical duplication. A shared abstraction is justified when several real consumers already duplicate the same mechanism, when it reduces future edits, and when its implementation burden is smaller than the alternatives. This is a **counterexample to an unconditional 'no abstraction' rule**.

## Limit {#limits}

The complete PR adds types and supporting code; 61 fewer lines in one follow-up commit does not establish a PR-wide reduction or runtime equivalence. No build or test run is claimed here.
