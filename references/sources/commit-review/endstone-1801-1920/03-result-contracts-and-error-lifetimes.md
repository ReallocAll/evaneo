<!-- retrieval: {"source_ids":["public:commit:22e3a7401d11f0beaa108955421f41445ab2650a","public:commit:37bb0efcd62b6a15b236407bafb9257bc4b8ba29","public:commit:3de6c8ead087921cff29e0e5106a6424f886595b","public:commit:41b59147a6fb40b2fd7ffbd33940c38f7649c0a6","public:commit:7855335bdf219bee4d7070a4aa5483d16c1dbeee","public:commit:78d56e127cd3c4ba07a2e1ae4ef0ace91f6e4d7b","public:commit:85f2422120bf71fafb8572f8e600737a1c0839ca","public:commit:9514e7cf891b64980e043cc29479b4bdc78acd40","public:commit:9dc8d9e7a486bc8db96c4fb6bf8fba19233e68d4","public:commit:bca990465df5aa92194679f0229c6824eba1fe3a","public:commit:dde4d6f7a112462777a8c242513540efa1f08d9a","public:commit:e492667201feb7b96e4e64f4f52b3c20d0f9c61c"],"source_type":"public","date":"2024-09-29..2024-09-30","topics":["lifetime","ffi","testing","build","api","diagnosis","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Result contracts across C++ and Python {#result-contracts-across-c-and-python}

Scope: Endstone commits 1801–1920, September 14–October 22, 2024. These notes follow related implementation areas during this period.

## Causal reading and applicability {#causal-reading-and-applicability}

The September 29–30 chain introduces expected-lite and a common Result/Error channel, then migrates scoreboards, permissions, events, blocks and other APIs. The later changelog (1917) explicitly describes the intended language boundary: C++ returns a Result, Python unwraps success and raises on failure. This is supported intent, not inferred solely from naming. Python conversion preserves the message but not a structured trace; successful void maps to None.

The implementation contains important counterevidence to an unqualified “prefer Result” rule. Error stores string_views to temporary formatted messages and temporary trace strings. Several consumers discard a Result or convert it to a boolean/absence: scheduler validation loses its diagnostic, attachment removal hides the error detail, Objective display queries can suppress an invalid-state error, and BlockState update ignores its inner set-data failure. Native throws and invalid casts are not automatically caught by changing a return type. Whole relevant files and exact endpoint equality confirm these limits remain at 1920; no later repair outside this assignment is presumed.

Block hooks show a separate integration decision: when wrapper construction fails, log and execute the original native operation; when an event is delivered and cancelled, prevent the operation. This fail-open behavior is observed in code, not generalized into a universal safety preference. It preserves native execution availability at the cost of missing plugin intervention on a wrapper failure. The no-physics flags also change during the migration and are not dismissed as mechanical Result plumbing.

Use the family as evidence for explicit, cross-language error contracts only together with ownership of diagnostic storage, complete propagation at call sites and consistent exception policy. The errors identified here are static source counterexamples, not reproduced crashes. expected-lite/cpptrace internals and native implementation behavior were not exhaustively audited or executed. Changes in tests are mock-interface adaptations, with unchanged assertion lines; artifact validation must never be described as passing upstream tests.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1841"></a>
### Commit 1841 · chore(deps): update cpptrace and expected-lite libraries {#commit-1841}

Source: [3de6c8ead087921cff29e0e5106a6424f886595b](https://github.com/EndstoneMC/endstone/commit/3de6c8ead087921cff29e0e5106a6424f886595b). Authored 2024-09-29T16:27:45Z; committed 2024-09-29T16:27:45Z. Git author: Vincent; committer: Vincent.


Adds expected-lite 0.8 as a public/header dependency and moves cpptrace to 0.7.1 through CMake and Conan. This establishes the build surface for Result and richer errors rather than independently justifying expected-lite over all alternatives. A later collaborator fixes the expected-lite fetch tag spelling in 1862. Dependency code itself was not executed or exhaustively reviewed.

Changed-source navigation: `CMakeLists.txt`, `conanfile.py`.

<a id="commit-1842"></a>
### Commit 1842 · feat: introduce endstone::Error for improved error handling {#commit-1842}

Source: [78d56e127cd3c4ba07a2e1ae4ef0ace91f6e4d7b](https://github.com/EndstoneMC/endstone/commit/78d56e127cd3c4ba07a2e1ae4ef0ace91f6e4d7b). Authored 2024-09-29T16:40:20Z; committed 2024-09-29T16:40:20Z. Git author: Vincent; committer: Vincent.


Introduces Error carrying message and stack-trace string_views, with trace capture implemented through cpptrace. The trace view is built from a temporary generated string, so ownership is not retained. This directly undercuts the intended durable error object even before broader Result adoption. It is a static lifetime observation, not a measured crash. The public Error implementation is proven unchanged through ordinal 1920.

Changed-source navigation: `CMakeLists.txt`, `conanfile.py`, `include/endstone/detail/util/error.h`, `include/endstone/util/error.h`, `src/endstone_core/util/error.cpp`.

<a id="commit-1843"></a>
### Commit 1843 · feat: introduce endstone::Result {#commit-1843}

Source: [85f2422120bf71fafb8572f8e600737a1c0839ca](https://github.com/EndstoneMC/endstone/commit/85f2422120bf71fafb8572f8e600737a1c0839ca). Authored 2024-09-29T16:49:26Z; committed 2024-09-29T16:49:26Z. Git author: Vincent; committer: Vincent.


Defines Result as an expected-style value/error channel and supplies formatted make_error helpers. The formatting helper returns an Error referring to a temporary formatted message, adding a second non-owning lifetime problem to 1842's trace. The intended distinction between values and explicit failures is clear, but the storage choice prevents treating this implementation as a safe reusable error-value recipe. Full Error/Result/helper context was read.

Changed-source navigation: `include/endstone/detail/util/error.h`, `include/endstone/util/result.h`.

<a id="commit-1844"></a>
### Commit 1844 · feat: use endstone::Result for Objective class functions {#commit-1844}

Source: [dde4d6f7a112462777a8c242513540efa1f08d9a](https://github.com/EndstoneMC/endstone/commit/dde4d6f7a112462777a8c242513540efa1f08d9a). Authored 2024-09-29T18:25:47Z; committed 2024-09-29T18:25:47Z. Git author: Vincent; committer: Vincent.


Objective operations begin returning Result and check whether an objective is still registered rather than silently doing nothing. Removal, display and rendering operations can now communicate failures. The validity check uses name existence, not identity of the original native objective, so unregister/recreate scenarios are not fully characterized by the check. This is a breaking C++ contract migration; Python adaptation follows rather than being assumed simultaneous.

Changed-source navigation: `include/endstone/detail/scoreboard/objective.h`, `include/endstone/scoreboard/objective.h`, `src/endstone_core/scoreboard/objective.cpp`, `src/endstone_core/scoreboard/score.cpp`.

<a id="commit-1845"></a>
### Commit 1845 · feat: add type caster for endstone::Result {#commit-1845}

Source: [9dc8d9e7a486bc8db96c4fb6bf8fba19233e68d4](https://github.com/EndstoneMC/endstone/commit/9dc8d9e7a486bc8db96c4fb6bf8fba19233e68d4). Authored 2024-09-29T19:06:30Z; committed 2024-09-29T19:06:30Z. Git author: Vincent; committer: Vincent.


The Result pybind caster unwraps successful values, maps successful void to None, and raises RuntimeError with the message on failure. It does not expose the captured trace as a structured Python error. Objective bindings and stubs stop representing these failure cases as optional successful results. This is the concrete C++/Python boundary policy later explained in release notes, with the underlying Error lifetime caveat still applicable.

Changed-source navigation: `include/endstone/detail/pybind_type_caster.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_core/scoreboard/objective.cpp`, `src/endstone_python/scoreboard.cpp`.

<a id="commit-1846"></a>
### Commit 1846 · feat(scoreboard): Add Objective::isDisplayed method {#commit-1846}

Source: [bca990465df5aa92194679f0229c6824eba1fe3a](https://github.com/EndstoneMC/endstone/commit/bca990465df5aa92194679f0229c6824eba1fe3a). Authored 2024-09-29T22:35:13Z; committed 2024-09-29T22:35:13Z. Git author: Vincent; committer: Vincent.


Objective isDisplayed now returns Result<bool>, extending state validation to a predicate. The Python display-slot path uses value_or(false), however, so an invalid-state error can still collapse into a normal absent-slot result there. This local exception to the new error policy is preserved instead of declaring every migrated call uniformly exception-raising.

Changed-source navigation: `include/endstone/detail/scoreboard/objective.h`, `include/endstone/scoreboard/objective.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_core/scoreboard/objective.cpp`, `src/endstone_python/scoreboard.cpp`.

<a id="commit-1847"></a>
### Commit 1847 · refactor(scoreboard): update methods in Score class to return Result {#commit-1847}

Source: [9514e7cf891b64980e043cc29479b4bdc78acd40](https://github.com/EndstoneMC/endstone/commit/9514e7cf891b64980e043cc29479b4bdc78acd40). Authored 2024-09-29T23:05:21Z; committed 2024-09-29T23:05:21Z. Git author: Vincent; committer: Vincent.


Score getters and mutations adopt Result and report invalid/read-only cases. An unset score still reads as zero; that prior convention is not converted into an error. The older invalid scoreboard-ID check is removed. The distinction matters when migrating callers: the new type signals specific state failures, not every absence or zero value.

Changed-source navigation: `include/endstone/detail/scoreboard/score.h`, `include/endstone/scoreboard/score.h`, `src/endstone_core/scoreboard/score.cpp`.

<a id="commit-1848"></a>
### Commit 1848 · refactor: update various methods to return Result type {#commit-1848}

Source: [e492667201feb7b96e4e64f4f52b3c20d0f9c61c](https://github.com/EndstoneMC/endstone/commit/e492667201feb7b96e4e64f4f52b3c20d0f9c61c). Authored 2024-09-29T23:30:03Z; committed 2024-09-29T23:30:03Z. Git author: Vincent; committer: Vincent.


Scoreboard addObjective now returns Result for duplicate names, and redundant local error callbacks are removed. Unknown criteria can still throw through a different path; existing ignored display-name/render-type arguments are not repaired by this type migration. Scheduler validation also returns Result, but the caller discards it and returns nullptr without the former diagnostic. Thus an explicit error type can still lose information if consumers do not propagate it. Full scoreboard and scheduler context informed this limited claim.

Changed-source navigation: `include/endstone/detail/scoreboard/scoreboard.h`, `include/endstone/permissions/permissible.h`, `include/endstone/scoreboard/scoreboard.h`, `src/endstone_core/scheduler/scheduler.cpp`, `src/endstone_core/scoreboard/objective.cpp`, `src/endstone_core/scoreboard/scoreboard.cpp`.

<a id="commit-1849"></a>
### Commit 1849 · refactor: update more methods to return Result type {#commit-1849}

Source: [22e3a7401d11f0beaa108955421f41445ab2650a](https://github.com/EndstoneMC/endstone/commit/22e3a7401d11f0beaa108955421f41445ab2650a). Authored 2024-09-30T00:43:25Z; committed 2024-09-30T00:43:25Z. Git author: Vincent; committer: Vincent.


Propagates Result across permissions, event registration, boss progress, experience/flying controls, server/block-data creation and corresponding interfaces. Empty permission names receive validation. Convenience plugin calls still return void and log errors, while attachment removal exposes only has_value(), hiding error detail. The null-handler diagnostic has a format/argument-count mismatch visible in the patch; it is a compile-risk observation, not a reproduced build failure. PythonPluginLoader changes throw e to bare throw, preserving exception type. Test changes adapt mock signatures only, without new behavioral assertions. The full 865-line patch was read in two pages.

Changed-source navigation: `include/endstone/boss/boss_bar.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/mob.h`, `include/endstone/detail/boss/boss_bar.h`, `include/endstone/detail/command/console_command_sender.h`, `include/endstone/detail/command/proxied_command_sender.h`, `include/endstone/detail/command/server_command_sender.h`; plus 24 paths not listed here.

<a id="commit-1850"></a>
### Commit 1850 · feat(python): update python bindings {#commit-1850}

Source: [41b59147a6fb40b2fd7ffbd33940c38f7649c0a6](https://github.com/EndstoneMC/endstone/commit/41b59147a6fb40b2fd7ffbd33940c38f7649c0a6). Authored 2024-09-30T00:55:41Z; committed 2024-09-30T00:55:41Z. Git author: Vincent; committer: Vincent.


Adds the Result caster includes to the affected Python binding units and changes remove_attachment's stub return to None. This aligns language bindings with 1849; it does not resolve the error-storage or error-consumption limits.

Changed-source navigation: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/boss.cpp`, `src/endstone_python/permissions.cpp`.

<a id="commit-1851"></a>
### Commit 1851 · refactor: update block-related methods to return Result type {#commit-1851}

Source: [37bb0efcd62b6a15b236407bafb9257bc4b8ba29](https://github.com/EndstoneMC/endstone/commit/37bb0efcd62b6a15b236407bafb9257bc4b8ba29). Authored 2024-09-30T13:11:58Z; committed 2024-09-30T13:11:58Z. Git author: Vincent; committer: Vincent.


Block creation/access validates height, chunk availability and ticking state and returns Result; invalid formatting gets an explicit INVALID representation. Hooks that cannot form the wrapper log and fall through to the original native operation, whereas a successfully delivered cancelled event still prevents it. This is an observed fail-open integration choice. Block setting also changes no-physics flags from 2|16|1024 to 2, while physics uses 3. Native set results remain ignored. BlockState::update discards the inner set-data Result and can report true despite that failure; comparing an edited snapshot's type is another narrower semantic issue. The full 777-line patch and whole block/state context were read, without claiming exhaustive foreign-implementation cast safety.

Changed-source navigation: `cmake/EndstoneHeaders.cmake`, `include/endstone/block/block.h`, `include/endstone/block/block_state.h`, `include/endstone/detail/block/block.h`, `include/endstone/detail/block/block_state.h`, `include/endstone/detail/level/dimension.h`, `include/endstone/level/dimension.h`; plus 9 paths not listed here.

<a id="commit-1853"></a>
### Commit 1853 · fix: compilation errors on Linux {#commit-1853}

Source: [7855335bdf219bee4d7070a4aa5483d16c1dbeee](https://github.com/EndstoneMC/endstone/commit/7855335bdf219bee4d7070a4aa5483d16c1dbeee). Authored 2024-09-30T13:38:26Z; committed 2024-09-30T13:38:26Z. Git author: Vincent; committer: Vincent.


Repairs Linux compilation by adjusting the block callback/local Result handling and BlockState's value access. It is a concrete follow-up to the broad Result migration, not proof of a cross-platform successful build in this review. The still-ignored inner BlockState update failure remains unchanged through 1920, verified by full-blob equality.

Changed-source navigation: `src/endstone_core/block/block.cpp`, `src/endstone_core/block/block_state.cpp`.
