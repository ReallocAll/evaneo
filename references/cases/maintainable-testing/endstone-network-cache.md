<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2026-10-18","topics":["testing","maintainability","complexity","review","performance","scope","caching"],"limitations":"Static review of linked primary sources and bundled historical analyses; upstream tests were not executed. Historical claims and code changes are distinguished from proven runtime outcomes."} -->
# Endstone #548: narrow a speculative network cache to an observed lookup {#case}

## Two designs {#changes}

[PR #548](https://github.com/EndstoneMC/endstone/pull/548), by wu-vincent, proposed caching both a peer/connection lookup and per-subclient player lookup on high-volume packet-event paths. Its final patch added 67 and deleted 31 lines across four files. The PR was **closed without merge**; the maintainer said it was superseded by [c2c778ad](https://github.com/EndstoneMC/endstone/commit/c2c778adf07cab6204cd7a2f3c0004eda9731c77) on the maintained branch.

The replacement commit changed three files (**+31/−13 lines**) and addressed the player lookup only by caching a weak entity reference, falling back to the existing scan after invalidation. The commit reports that the original reported severe slowdown did not reproduce in its 40-bot test; measured per-call timing changed from roughly 1.2 microseconds to 1.07 microseconds under its specified workload. These figures are commit-reported, not independently rebenchmarked here.

## Judgment {#reading}

An optimization may address a real asymptotic concern while expanding invalidation and ownership state beyond what measured data supports. Prefer the narrowest confirmed expensive path. Record non-reproduced performance claims explicitly rather than treating them as a mandate for a larger caching subsystem.

## Limit {#limits}

The two patches are not functionally identical; their line counts are descriptive scope evidence, not proof that the replacement achieves every original goal. The replacement maintains a cache and requires careful entity lifetime behavior.
