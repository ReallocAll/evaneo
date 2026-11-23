<!-- retrieval: {"source_ids":["public:commit:492f3175cd410e72b4baba16e0f60e971f556e08","public:commit:a27b61cb7d05ce10725865c5820903be18a813be","public:commit:eb6d9450259a7c0bc3cf41522275ab3577590fca"],"source_type":"public","date":"2024-09-05","topics":["lifetime","concurrency","testing","api","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Reload cleanup and public API changes {#reload-cleanup-and-public-api-changes}


Endstone commits 1681–1800, dated August 29–September 14, 2024.

## Dated repair, not retroactive safety {#dated-repair-not-retroactive-safety}

The previous August endpoint clears plugin loaders and reloads packages without invoking scheduler cancellation for each plugin. On September 5, 1734 explicitly adds task cancellation and event-handler removal after disabling an enabled plugin, with an issue-48 fix claim. This is a meaningful repair of that earlier gap. The later in-game reload expansion should be interpreted at its September point in the chain, not retroactively applied to the earlier console restriction.

The full cancellation path limits the claim. cancelTasks holds a nonrecursive tasks_mtx while calling task->doCancel. An idle async task's doCancel calls removeTask, which attempts the same mutex again. This is a concrete static deadlock path, not a reproduced runtime failure. Active async work also is not joined before plugin destruction; EndstoneServer::reload still contains an explicit TODO to wait up to 2.5 seconds. Task ownership remains a raw plugin pointer. HandlerList returns a vector of raw handler pointers, while unregister destroys handlers under its own lock, so retaining a dispatch snapshot is not protected by that lock. These observations explain why adding cleanup is necessary without calling the whole reload lifecycle safe.

The default PluginLoader catches exceptions from disabling and returns; manager cleanup follows that return. Custom loaders can have different behavior, so an exception escaping a loader remains outside a guaranteed finally-style cleanup path. Dependency ordering is still TODO. Python loader replacement also constructs/destructs the new metrics object, creating another lifecycle dependency not solved by per-plugin task cancellation.

## Public API tradeoff {#public-api-tradeoff}

The scoreboard factory rename is behavior-preserving internally but source-breaking publicly, with no alias. Release notes explicitly name consistency with other create* factories. Broader Message virtual-method changes occur in the event dossier. The patch release keeps API version 0.5, while the C++ loader checks that coarse version string. This is evidence of the limits of the current compatibility gate, not proof of deliberate acceptance of every binary break.

Use this case for cleanup ordering, ownership, callback reentrancy, cancellation versus completion, and migration-documentation decisions. No scheduler tests or plugin reload were run; changed test files only update mock interfaces. Earlier shutdown-crash causes that were not established remain unknown and are not explained away by these later findings.

## Individual commit dispositions {#individual-commit-dispositions}

<a id="commit-1733"></a>
### Commit 1733 {#commit-1733}

2024-09-05T11:17:33Z · `a27b61cb7d05ce10725865c5820903be18a813be` · refactor(scoreboard)!: rename `getNewScoreboard` to `createScoreboard`

Renames getNewScoreboard to createScoreboard across C++, Python and test mocks without a compatibility alias. The body is unchanged. Later release notes explicitly give consistency with createBossBar/createBlockData as the reason. This is an observed willingness to make a documented breaking rename; it is not evidence that API compatibility is always unimportant.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/a27b61cb7d05ce10725865c5820903be18a813be). Classification: breaking_api_rename.

<a id="commit-1734"></a>
### Commit 1734 {#commit-1734}

2024-09-05T16:07:55Z · `492f3175cd410e72b4baba16e0f60e971f556e08` · fix: remove plugin tasks and event handlers on disable, fix #48

On disabling an enabled plugin, calls its loader, cancels owned scheduler tasks, then unregisters its event handlers. The title explicitly associates the fix with issue 48. This repairs missing cleanup in the earlier reload path but does not add an async completion barrier. Full scheduler context reveals that idle async cancellation can call removeTask while tasks_mtx is already held, and HandlerList snapshots contain raw pointers. These static limits prevent a blanket safe-reload claim.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/492f3175cd410e72b4baba16e0f60e971f556e08). Classification: lifecycle_cleanup.

<a id="commit-1737"></a>
### Commit 1737 {#commit-1737}

2024-09-05T17:33:45Z · `eb6d9450259a7c0bc3cf41522275ab3577590fca` · feat(command): /reload command can now be executed in-game

Removes the console-only restriction on /reload while retaining permission checking. Chronologically this follows the task/handler cleanup, which makes the expansion intelligible, but the source does not state that cleanup proves concurrency safety. The September behavior must not be projected backward into the console-restricted August implementation.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/eb6d9450259a7c0bc3cf41522275ab3577590fca). Classification: policy_expansion.

## Coverage boundary {#coverage-boundary}

Findings rely on the linked public sources; external PR/issue discussions, dependencies, and native engine internals are outside the cited evidence. Runtime and current-release behavior were not tested.
