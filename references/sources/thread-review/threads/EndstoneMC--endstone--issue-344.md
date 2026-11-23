<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:344"],"source_type":"public","date":"2026-03-07","topics":["testing","diagnosis","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-344-replaceitem-command-leads-to-kick-of-a-player-crash"></a>
# EndstoneMC/endstone #344: /replaceitem command leads to kick of a player/crash {#endstonemc-endstone-344-replaceitem-command-leads-to-kick-of-a-player-crash}

Source: https://github.com/EndstoneMC/endstone/issues/344

## Evidence and attribution {#evidence-and-attribution}

Primary author: kleines-L. Created 2026-03-07T22:40:33Z; recorded state closed; merged not applicable.

## Root cause claim {#root-cause-claim}

kleines-L showed /replaceitem entity @s slot.hotbar 1 nether_star kicking the client while plain BDS worked. wu-vincent explained that its success message has five parameters but Endstone's packet type allowed only four, causing client rejection. The chosen correction was the unlimited-parameter message representation used internally by vanilla, scheduled with #354.

Reuse native protocol representations when bounded convenience formats cannot preserve valid command outputs. The sporadic crash suspicion was not reproduced and should remain separate from the demonstrated disconnect. This thread has no patch or successful retest.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/344
- https://github.com/EndstoneMC/endstone/issues/344#issuecomment-4159257134
