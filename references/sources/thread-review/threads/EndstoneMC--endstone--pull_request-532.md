<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:532"],"source_type":"public","date":"2026-09-15","topics":["testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-532-fix-boss-use-a-stable-id-for-each-boss-bar"></a>
# EndstoneMC/endstone #532: fix(boss): use a stable id for each boss bar {#endstonemc-endstone-532-fix-boss-use-a-stable-id-for-each-boss-bar}

Source: https://github.com/EndstoneMC/endstone/pull/532

## Evidence and attribution {#evidence-and-attribution}

Primary author: HP-network. Created 2026-09-15T15:52:52Z; recorded state closed; merged False.

HP-network correctly identifies recipient-ID collision but allocates a fresh level ID without spawning a client actor. Wu rejects: client BossEvent processing looks up boss_id in its level and discards unknown actors, so this would produce zero bars. Existing code borrows the player's actor because that actor is guaranteed known. Multiple bars require one fake actor each, lifecycle removal and respawn after dimension changes; Geyser's zero-scale creeper and PocketMine's slime are precedents cited by Wu, not independently audited here. Query handling currently resends only when ID matches the player, another broken invariant. Only diff --check is reported, not gameplay. Closed unmerged, correct diagnosis plus invalid fix.

## Direct patch findings {#direct-patch-findings}

Stores ActorUniqueID per bar, lazily gets level ID on first send, carries it in snapshots/resends, and substitutes it for player ID. Adds no AddActor/RemoveActor lifecycle or query correction, corroborating reviewer gap.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (2185 characters; SHA-256 9c39d8cfe7d8d39e9fe455429ac23ef038f24800badad6d219cd0ed32b2d65a8), head c020aad118ec3e3b58725d955e58169e12d72ffd. This covers the supplied PR patch, not unrelated commits or historical intermediate revisions. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/532
- https://github.com/EndstoneMC/endstone/pull/532#issuecomment-6019606012
