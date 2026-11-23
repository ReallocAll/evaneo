<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:539"],"source_type":"public","date":"2026-09-19","topics":["lifetime","testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-539-intermittent-exceptionaccessviolation-inside-vanilla-level-tick-4-ticks-after-a-player-s-natural-disconnec"></a>
# EndstoneMC/endstone #539: Intermittent EXCEPTION_ACCESS_VIOLATION inside vanilla Level::tick, ~4 ticks after a player's natural disconnect {#endstonemc-endstone-539-intermittent-exceptionaccessviolation-inside-vanilla-level-tick-4-ticks-after-a-player-s-natural-disconnec}

Source: https://github.com/EndstoneMC/endstone/issues/539

## Evidence and attribution {#evidence-and-attribution}

Primary author: nikastro-w. Created 2026-09-19T22:02:30Z; recorded state closed; merged not applicable.

## Delayed crash reveals earlier lifetime corruption {#delayed-crash-reveals-earlier-lifetime-corruption}
nikastro-w supplies seven matching outer stacks over two versions, tick-precise disconnect timing, stale-reference auditing and careful limits: scheduled tasks returned, but earlier plugin actions could still corrupt state. Generic crashpad nearest-symbol frames and Level::tick wrappers are not the real cause; similarity to #451 is only triage context. #395's synchronous double-close is already fixed and has a different path.
Wu resolves Objective::serialize → ServerScoreboard::writeToLevelStorage → ServerLevel::_subTick: removeFromObjective frees IdentityDefinition before removing its score entry, and later persistence dereferences the dangling identity. Disconnect precedes failure because save discovers earlier damage. 4be6a165f reportedly fixes this plus three adjacent BDS mismatches. Scope is plugin scoreboard APIs such as reset_scores/player.scoreboard, not vanilla /scoreboard. Wu explicitly offers to reopen if no plugin touches that API; that unresolved applicability caveat matters.

## Additional source and attachment inspection {#additional-source-and-attachment-inspection}

Five supplied crash files were acquired; SHA-256 equality proves three 0.11.10 reports are byte-identical and two 0.11.11 reports are byte-identical. Both distinct reports were read fully. They show Windows access violations, generic nearest crashpad symbols and unknown Bedrock frames, followed by EndstoneServer::tick at line 827 or 843 and Level::tick line 33. They do not expose the freed scoreboard identity directly and must not be read as crashpad destructor causality.

The full six-file fix 4be6a165f90d193d164674c6fb55876485c52b61 was inspected. removeFromObjective now checks hasScore, copies the ID, erases the objective score, decrements reference count, and clears identity only after the last reference. This ordering removes the stale key before identity destruction. removeObjective removes display entries and the hashed lookup before destroying the objective; resetPlayerScore copies an ID that may alias freed storage before looping; IdentityDictionary::clearIdentity copies its erase key. Add/subtract promotes to int64, detects an out-of-int32 result and returns IntegerOverflow without changing the score. The commit message cites BDS 1.26.51 disassembly; no new tests accompany this patch. These changes verify implementation, not the reporter's plugin-specific trigger or the claim that every similar Level::tick crash shares this cause.

## Code and verification boundary {#code-and-verification-boundary}

All distinct supplied diagnostic evidence and complete relevant follow-up commit patches/messages were inspected. Public sources are linked under Traceability; the original acquisition, hashes, and per-file inspection inventories are not distributed. No runtime reproduction. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Attachment coverage: Five attachments reduce to two distinct complete crash reports by exact SHA-256; both were read.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/539
- https://github.com/EndstoneMC/endstone/issues/539#issuecomment-5750243593
- https://github.com/user-attachments/files/32424668/crash-2026-09-13-14.36.47-server.txt
- https://github.com/user-attachments/files/32424670/crash-2026-09-13-16.28.19-server.txt
- https://github.com/user-attachments/files/32424669/crash-2026-09-15-13.46.10-server.txt
- https://github.com/user-attachments/files/32424672/crash-2026-09-18-03.46.43-server.txt
- https://github.com/user-attachments/files/32424671/crash-2026-09-19-11.10.35-server.txt
- https://github.com/EndstoneMC/endstone/commit/4be6a165f90d193d164674c6fb55876485c52b61
