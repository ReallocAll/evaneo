<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:352"],"source_type":"public","date":"2026-03-21","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-352-playerportalevent-cannot-be-canceled-when-triggered-in-the-end"></a>
# EndstoneMC/endstone #352: PlayerPortalEvent cannot be canceled when triggered in the end {#endstonemc-endstone-352-playerportalevent-cannot-be-canceled-when-triggered-in-the-end}

Source: https://github.com/EndstoneMC/endstone/issues/352

## Evidence and attribution {#evidence-and-attribution}

Primary author: kleines-L. Created 2026-03-21T12:03:45Z; recorded state closed; merged not applicable.

## Semantics and follow-up {#semantics-and-follow-up}

kleines-L could cancel entering the End and Nether transitions, but not returning through an End exit. wu-vincent traced ServerPlayer::changeDimensionWithCredits→respawn and compared Bukkit/Paper: the return is a respawn, not a portal teleport. PlayerRespawnEvent fires and is not cancellable, so PlayerPortalEvent cannot block it.

He then added a RespawnReason distinguishing DEATH from END_PORTAL so plugins can detect and react to the transition (for example choosing a destination), without claiming the event became cancellable. References include SPIGOT-4770, Bukkit RespawnReason and Paper #5494; these are mature-project precedents cited in the discussion, not separately reviewed here.

Reusable rule: classify by actual lifecycle semantics, not visual entry point. Expose missing observational information without pretending an uninterruptible lifecycle operation supports cancellation. No patch/test output is included in this record.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/352
- https://github.com/EndstoneMC/endstone/issues/352#issuecomment-4604629531
- https://github.com/EndstoneMC/endstone/issues/352#issuecomment-4604862199
