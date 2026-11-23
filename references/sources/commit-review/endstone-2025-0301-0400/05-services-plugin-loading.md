<!-- retrieval: {"source_ids":["public:commit:34d4c09ac29842fcc5c5733882534e3c79388cde","public:commit:78d0ff3e3e243f78b845d639b2c497f247965796","public:commit:7ba59e9dfb9a263b3b1228c7029e771b4e13b69a","public:commit:955941682473f3da527b407b7732d4efcedc5b7a","public:commit:957d2afbdbc47aac52d8030f416a1d8b88381473","public:commit:9e1ac6a312bc2100fe6ab6fd9c3b7992b55dbee0","public:commit:af1a4acad11203d6b1b3df02cfa229327d49b478","public:commit:e0883e79cbb1c7923b9fd7998fb992252ed65811","public:commit:e30be899588b3362ea4e1e8d9b4db18e2f9af48b","public:commit:fd2e23fb610ddef85daa44502478ccdc83f80903"],"source_type":"public","date":"2025-03-13..2025-03-17","topics":["lifetime","concurrency","ffi","testing","api","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Service provider ownership and staged plugin loading {#service-provider-ownership-and-staged-plugin-loading}

## Service semantics {#service-semantics}

384–388 add Service, ServiceManager, five priorities, C++ and Python interfaces, implementation, eight tests and Server ownership. The registry locks a name→vector map, sorts descending priority and returns shared_ptr. Equal priorities insert before existing providers, so newest wins by implementation; the API does not document a tie rule. C++ load<T> statically casts based on the name convention. The provider is shared-owned but the Plugin is a borrowed reference.

Shared ownership and a mutex do not complete lifecycle safety. Erasure can run provider destruction under the nonrecursive lock. Python register’s keep_alive<1,3> attaches provider lifetime to the manager rather than individual registration. At400 disablePlugin cancels tasks and unregisters handlers but never calls service unregisterAll; clearPlugins clears loaders without clearing the service registry. These source-visible gaps motivate unload, GC, reentrancy and lifetime tests. The supplied tests establish intended priority/fallback and several unregister cases only; they were not run and do not exercise concurrent access or Python destruction.

## Plugin initialization revisions {#plugin-initialization-revisions}

395 rejects missing hard dependency names.396 resolves the first matching loader and registers a plugin only after successful onLoad, making failure an admission barrier but changing fallback among overlapping loaders.397 then splits metadata initialization from dependency check/onLoad and bulk-initializes all candidate names first. That reduces filesystem-order false negatives, but it also reintroduces lookup visibility for failed onLoad plugins. Dependency checks verify presence rather than successful readiness, and the explicit TODO still covers ordering, soft_depend, load_before and provides. Bulk initialization is preparation for dependency resolution, not the completed resolver.

400 reserves platform/vendor names. Because lowercase validation and the endstone-prefix rule already precede the case-insensitive equality checks, part of the final condition is redundant.394 removes an include-only unused builder scaffold; this is mechanical cleanup, not a design principle.

## Use and limits {#use-and-limits}

Useful for plugin extension registries, priority semantics, lifecycle cleanup, staged admission and failure recovery. Tests or analyses needed before reuse include equal-priority registration, null providers, unregister(provider), service retention across reload, destructor reentrancy, plugin dependency cycles/order and exceptions. No source was run or modified upstream; these are historical source interpretations with explicit uncertainty.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-384"></a>
### Commit 384 {#commit-384}

fd2e23fb610ddef85daa44502478ccdc83f80903 · 2025-03-13T17:03:35Z

[feat: add `Service` and `ServiceManager`](https://github.com/EndstoneMC/endstone/commit/fd2e23fb610ddef85daa44502478ccdc83f80903)

**Observed change.** Adds polymorphic shared-owning Service marker and abstract ServiceManager register/unregister API.

**Causal interpretation.** Introduces a cross-plugin provider seam, separating service interface identity from implementation provider.

**Limits.** Service initially global namespace, fixed387; no implementation until387, typed load not yet present.

<a id="commit-385"></a>
### Commit 385 {#commit-385}

78d0ff3e3e243f78b845d639b2c497f247965796 · 2025-03-13T17:14:37Z

[feat: add python binding for `Service` and `ServiceManager`](https://github.com/EndstoneMC/endstone/commit/78d0ff3e3e243f78b845d639b2c497f247965796)

**Observed change.** Adds Service shared_ptr binding, ServiceManager methods and stubs; register keep_alive<1,3> keeps provider alive with manager.

**Causal interpretation.** Python subclass identity/lifetime needs extra retention beyond C++ ownership.

**Limits.** Keep-alive lifetime is manager-wide rather than registration-wide and unregister does not explicitly remove it; no Python GC/unload test.

<a id="commit-386"></a>
### Commit 386 {#commit-386}

7ba59e9dfb9a263b3b1228c7029e771b4e13b69a · 2025-03-13T17:36:19Z

[feat: add `ServicePriority`](https://github.com/EndstoneMC/endstone/commit/7ba59e9dfb9a263b3b1228c7029e771b4e13b69a)

**Observed change.** Adds five service priorities, highest-provider get, unchecked templated static_pointer_cast load; exposes Python register priority/load and exports. CMake adds implementation path before file arrives387.

**Causal interpretation.** Service selection becomes ordered fallback, while type safety rests on name/interface convention.

**Limits.** Null provider, duplicate registrations and equal-priority policy unspecified in API; Python load stub omits possible None.

<a id="commit-387"></a>
### Commit 387 {#commit-387}

955941682473f3da527b407b7732d4efcedc5b7a · 2025-03-13T18:13:58Z

[test: add tests for `ServiceManager`](https://github.com/EndstoneMC/endstone/commit/955941682473f3da527b407b7732d4efcedc5b7a)

**Observed change.** Implements mutex-protected name→sorted provider vectors; lower_bound greater inserts equal priorities before existing providers; erase variants clean empty buckets. Moves Service into namespace and adds eight tests.

**Causal interpretation.** Highest priority wins, equal priority is newest first by implementation; shared_ptr return permits provider survival after unregister while plugin is a borrowed reference.

**Limits.** Tests cover register, priority fallback, per-name and per-plugin unregister, missing names. No equal-priority, null, provider-only unregister, concurrency, reentrant destruction, Python or plugin-unload tests. Erase can destroy providers under nonrecursive mutex.

<a id="commit-388"></a>
### Commit 388 {#commit-388}

e0883e79cbb1c7923b9fd7998fb992252ed65811 · 2025-03-14T00:46:12Z

[feat: add `Server::getServiceManager`](https://github.com/EndstoneMC/endstone/commit/e0883e79cbb1c7923b9fd7998fb992252ed65811)

**Observed change.** Server constructs/owns ServiceManager and exposes reference getter/Python property; mocks updated. ServiceManager header forwards Plugin to reduce include coupling.

**Causal interpretation.** Makes registry available through central lifecycle owner rather than requiring plugins to construct one.

**Limits.** No disablePlugin unregisterAll integration in this commit or400; stored Plugin& lifetime therefore needs separate cleanup discipline.

<a id="commit-394"></a>
### Commit 394 {#commit-394}

af1a4acad11203d6b1b3df02cfa229327d49b478 · 2025-03-16T21:51:25Z

[refactor: remove unused header file](https://github.com/EndstoneMC/endstone/commit/af1a4acad11203d6b1b3df02cfa229327d49b478)

**Observed change.** Deletes unused header containing includes only and no builder declarations.

**Causal interpretation.** Mechanical dead include scaffold removal verified from full content.

**Limits.** No independent design lesson; no compilation run.

<a id="commit-395"></a>
### Commit 395 {#commit-395}

34d4c09ac29842fcc5c5733882534e3c79388cde · 2025-03-16T22:19:06Z

[feat: add dependency checks for plugins](https://github.com/EndstoneMC/endstone/commit/34d4c09ac29842fcc5c5733882534e3c79388cde)

**Observed change.** Checks hard dependency names through plugin lookup before initialization; replaces prefix test spelling with starts_with.

**Causal interpretation.** Fails missing dependencies explicitly, but this initial approach is load-order dependent.

**Limits.** No topological sort/soft dependency/provides handling; moved397 into later load phase.

<a id="commit-396"></a>
### Commit 396 {#commit-396}

957d2afbdbc47aac52d8030f416a1d8b88381473 · 2025-03-16T22:33:04Z

[feat: add `resolvePluginLoader` method to `PluginManager`](https://github.com/EndstoneMC/endstone/commit/957d2afbdbc47aac52d8030f416a1d8b88381473)

**Observed change.** Adds first-matching loader resolver; load failure no longer falls through to other matching loaders. Registers plugin only after onLoad succeeds and returns failure on exception.

**Causal interpretation.** Creates a clearer admission point and avoids reporting failed onLoad as loaded at this intermediate step.

**Limits.** Changes loader fallback semantics; plugin object cleanup depends on loader. Reversed registration timing397; no failure-path tests.

<a id="commit-397"></a>
### Commit 397 {#commit-397}

e30be899588b3362ea4e1e8d9b4db18e2f9af48b · 2025-03-16T22:57:12Z

[refactor: decouple plugin loading from plugin initialization](https://github.com/EndstoneMC/endstone/commit/e30be899588b3362ea4e1e8d9b4db18e2f9af48b)

**Observed change.** Separates initialization (metadata fields and registry insertion) from dependency check/onLoad. Bulk paths initialize all candidates before loading; retains snapshot of loaders against onLoad mutation.

**Causal interpretation.** Avoids missing-name lookup merely because dependency is later in filesystem order and prepares future dependency ordering.

**Limits.** No topological ordering implemented. Failed onLoad plugin remains lookup-visible; dependency check tests presence, not successful load. Single-file flow likewise registers before onLoad. TODO explicitly retains depend/soft_depend/load_before/provides.

<a id="commit-400"></a>
### Commit 400 {#commit-400}

9e1ac6a312bc2100fe6ab6fd9c3b7992b55dbee0 · 2025-03-17T16:16:42Z

[feat: add checks for restricted names in plugin manager](https://github.com/EndstoneMC/endstone/commit/9e1ac6a312bc2100fe6ab6fd9c3b7992b55dbee0)

**Observed change.** Rejects endstone/minecraft/mojang plugin names case-insensitively after lowercase regex and endstone-prefix check.

**Causal interpretation.** Reserves vendor/platform names; endstone equality is redundant because prefix rule already rejects it.

**Limits.** No name-validation tests. Latest chronological main commit is not a merge of beta1.21.70 branch.
