<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:133"],"source_type":"public","date":"2025-02-13","topics":["lifetime","concurrency","ffi","testing","api","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-133-feat-1-21-60-support-for-windows-wip"></a>
# EndstoneMC/endstone #133: [feat] 1.21.60 support for Windows (WIP) {#endstonemc-endstone-133-feat-1-21-60-support-for-windows-wip}

Source: https://github.com/EndstoneMC/endstone/pull/133

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (3611 additions, 629 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu’s merged Windows 1.21.60 WIP explicitly records a known defect: operator-status changes do not refresh client commands. There are no captured comments or reviews. The patch is a working-in-progress compatibility port, not a harmless version-label update or a claim of cross-platform completeness.

### Complete patch inspection {#complete-patch-inspection}

The full 103-file port was read, including utility implementations, imported-reference function wrapper, both removed/added layouts, lifecycle hooks and all new tests. It targets Windows: symbol offsets update only the Windows table; getI18n becomes a hardcoded Windows executable-base offset with a TODO and no non-Windows return. Known operator command-refresh breakage is reflected by setPermissions losing its hook marker after inlining, with an explicit alternative-hook TODO.

ABI migration is substantial: SemVersion shrinks to 24 bytes through an 8-byte packed StaticOptimizedString; CommandRegistry allocator becomes a 64-byte brstd::copyable_function; AppPlatformListener acquires a subscription; serialized abilities gain vertical fly speed; mutable attributes carry modification context separately and dispatch dirty notifications through a stored member callback. Player name/inventory become direct member access, requiring expanded Actor/Mob/Player/container/inventory declarations. Biome uses a flat set and opaque 32-byte category entries with TODO; unknown virtual slots/event 26 remain explicitly unresolved. BlockDescriptor resolves deferred state under a lock. Native virtual ordering changes across Actor, BlockSource, ILevel/Level and BlockLegacy; assertions alone cannot validate every field.

Server setup moves from event-coordinator hooks to ServerScriptManager::_runPlugins execution groups, with once_flags for server/level initialization. ServerInstance::_resetServerScriptManager destroys the Endstone server before forwarding native reset. The comments identify safe server-thread shutdown/destruction and suggest ScriptModuleShutdownEvent as an alternative, not an implemented solution. Once_flags persist for the process; resetting the locator does not reset those flags, relevant if initialization can repeat in-process.

Utility counterexamples are important. SpinLockImpl checks atomic owner against empty and then stores ownership in separate operations, so two contenders can both acquire it; atomic storage does not make check-and-set atomic. Its contention test increments an atomic counter, which can remain correct even if the lock fails mutual exclusion. Other tests verify recursion/wrong-owner failures but do not deterministically force simultaneous entry. StaticOptimizedString copies based on length, so a short dynamically owned source becomes a borrowed copy that can dangle after source destruction; reset and assignment overwrite owned pointers without release. Tests use literals, a live short backing string, one long construction, and empty assignment destinations, leaving those ownership cases uncovered. SemVersion adds numeric/alphabetic prerelease ordering and correct '-'/'+' formatting, but uses stoi for arbitrarily long numeric components and tests ordinary ordering only.

brstd/copyable_function and its 610-line implementation explicitly reference LiteLDev/LeviLamina at fbb3c97; this is a separate project precedent, not wholly original Wu code. It models inline/heap targets and cv/ref/noexcept-qualified invocation. Static issues in this snapshot include missing returns from nullptr/copy assignment and array-pointer arithmetic in embedded_target_ptr when an alignment offset is nonzero. No execution or current-release allegation follows from these historical findings. Reuse the boundary lessons: ABI-shaped utilities need ownership, contention and alignment tests in addition to size checks.

Exact inspected base/head: be599b38b6286c06c33138b5777cdba147251c84…7c7ab80905b0650f603fd1cc081129df9721da6e. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/133
