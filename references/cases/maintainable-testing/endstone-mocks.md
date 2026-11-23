<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2025-05-05","topics":["testing","maintainability","complexity","review","mocks","duplicate-tests"],"limitations":"Static review of linked primary sources and bundled historical analyses; upstream tests were not executed. Historical claims and code changes are distinguished from proven runtime outcomes."} -->
# Endstone historical mocks: remove two files of boilerplate without inflating fixtures {#case}

## Observed change {#changes}

Maintainer wu-vincent's [commit 47ea0cc6](https://github.com/EndstoneMC/endstone/commit/47ea0cc640cbd208c0197a88cfa6924a612523b2) simplified tests by deriving fixture mocks directly from `EndstoneServer`. Two test files changed, **+4/−98 lines**, deleting repeated mock method declarations.

The related longitudinal review ([03-enchantment-registry.md](../../sources/commit-review/endstone-2025-0501-0600/03-enchantment-registry.md)) notes that this direct-inheritance approach was **temporary**. A subsequent revision centralized the abstract mock methods, adopted more appropriate GMock fixtures and removed a brittle exact logger-call count without losing the plugin/scheduler behavior assertions. Do not describe the intermediate direct-inheritance shape as the final permanent design.

## Judgment {#reading}

Fixtures and mocks are production-maintenance obligations in disguise. Remove repeating declarations and assertions that encode incidental logging or private call counts. Prefer tests of behavior and reusable narrow fixtures, but do not equate shortest intermediate diff with stable final design.

## Limit {#limits}

The later trajectory is sourced from the bundled historical review; the intermediate patch alone cannot prove final mock structure. No tests were executed.
