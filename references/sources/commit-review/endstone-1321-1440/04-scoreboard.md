<!-- retrieval: {"source_ids":["public:commit:0681cdf182ae40af1573bcb48d8d2aa0dfeda368","public:commit:072631ba06e3d06045dafab7d3ae99d18ee69927","public:commit:1212f83ab3cef787ea460de310169a81d6951cf8","public:commit:2b5b56142a4cab3959baea1c0290ddca1ae53635","public:commit:2e5d056f73743bd179db738864036832eebf4ba8","public:commit:3623534043a702d242bd6a5b66f0f50071f449de","public:commit:3712cdc91c3751d57188336a135e2108fa6e856c","public:commit:51720715cc6c8e0038ee6d9050392ab4769d5559","public:commit:52d521f94247c1fdef6827f7e1f57e83f0a84302","public:commit:5d3aa39f3d0923822fceb71524bee74f3ed11240","public:commit:6bb9fe82222b5233f2618c1b26414d80fbbac165","public:commit:77f1d0b68fd68cab8bfc06b2880f7cc382594256","public:commit:79688737f9e42538a57e3683e3cd683ca1a99b9d","public:commit:7a58866b3e3887b35514a9156d66ee3aba4fb0ad","public:commit:81b77c9d262a166e1f4c0b0143d46e84ca61b403","public:commit:881ee5c27a068aaf3467cdfb54dc35903fade9d0","public:commit:9fd9b690ed340a43d27a328f4acb9d033675805c","public:commit:b80621ec1eaa2fcb7f918e047b56932bcb19f242","public:commit:c4b9392db41720fa3419b8eeea30041d0bd4b4be","public:commit:c96d508bdbe6de0e9ca5668dac92d3ee2cb0523a","public:commit:c9869470cd72f60e598ddb86f6d112e2def8021c","public:commit:d25ff99d0c31a524775ab318822154805198329e","public:commit:daa56de4adb9ef4493255fe40e444874fa80423d","public:commit:dade75aeca238c82de25704001fea2913f904399","public:commit:ed478178a0b8e6f17a7fe8f2e9ddfceb30f49e92","public:commit:f4df80a551761cac2a1c08fdd267387112a486ab"],"source_type":"public","date":"2024-07-18..2024-07-20","topics":["lifetime","ffi","testing","recovery","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Scoreboard construction: contracts before implementation, ownership before lifetime safety {#scoreboard-construction-contracts-before-implementation-ownership-before-lifetime-safety}


## Observable development order {#observable-development-order}

1413–1422 build display slots, Objective, Criteria, Score and Scoreboard interfaces and Python exposure before usable core operations exist. Sets become vectors and entries become Player/Actor/string variants. Type registration and initialization ordering change alongside forward declarations. Criteria evolves from an enum to a borrowed native adapter with nested Type; an exported Python alias preserves Criteria.DUMMY while the C++ contract changes. Native layout declarations include explicit offsets, but there are no runtime layout tests here.

1431 attaches an owned EndstoneScoreboard to the server on level initialization. Most methods still throw; through 1440 the public Server interface has no scoreboard getter. Therefore a title claiming a class was added or all Objective methods implemented must not be expanded into a complete available scoreboard feature. The final core board file was read to establish this boundary, including the registration overload that drops its supplied display name. Python's registration lambda also drops the returned object from its first introduction onward. Stubs correctly reflect that lambda's None result, which is weaker than the C++ contract.

## Three distinct ownership layers {#three-distinct-ownership-layers}

The engine owns native Objective objects. EndstoneObjective is an adapter which stores a name and criteria adapter but borrows the board and native Objective. EndstoneScore in turn borrows the EndstoneObjective wrapper and carries raw actor/player entries or a string. These layers remain distinct across raw pointer/reference interfaces, shared_ptr in 1433, unique Score wrappers in 1437, and unique Objective/collection returns in 1439. A unique wrapper per lookup can simplify ownership of the adapter; it does not extend engine or parent-wrapper lifetime. No explicit reason for the shared-to-unique reversal is supplied, so a universal preference claim would overreach.

Invalid state changes from an abstract isValid promise, to logged/default-valued checks, to optional name/display/render/slot/order getters. Yet checkState tests only whether the old name is currently present. If an Objective is removed and a different one is registered under that name, the check does not compare the retained native object's identity. Likewise owning a Score wrapper does not own its Objective wrapper. These are source-level counterexamples to inferring lifetime safety from smart-pointer vocabulary. No actual use-after-free was reproduced.

## Mutation, identity and notification {#mutation-identity-and-notification}

Duplicate registration changes from returning an existing Objective to a nullable failure at 1432, before the operation is implemented. Identity lookups distinguish player/entity/fake-string paths; a fake-string miss falls back to stoll, accepting a numeric prefix unless later processing rejects it. Score reads distinguish absent state through isScoreSet while getScore returns zero. Setting checks existing identity and read-only criteria, then changes the native map directly. It does not create the missing identity or call the declared scoreboard notification hook in this unit. Display-name mutation retains a dirty-state TODO. Client synchronization and persistence effects remain unknown rather than assumed from local map mutation.

1440 combines slot and order mutation into setDisplay, clears former display slots and applies an ascending default. C++ None supports clearing, but the Python enum export is not updated here; numeric enum values also shift. Render mutation is a logged unsupported operation despite a writable API property. Getter optionals, name-only validation and outstanding board TODOs give the exact endpoint, which later history must update rather than perpetuate unexamined.

## Evidence and practical use {#evidence-and-practical-use}

All 26 scoreboard-family commits are authored/committed by Vincent in a direct parent chain. No separate reviewer discussion or rationale was read; native declarations are adaptation, not authorship of Bedrock's design. There are no scoreboard behavioral tests in these patches and none were executed. This family is useful for reviewing staged public APIs, wrapper/pointee lifetime distinctions, invalid-state semantics, binding return ownership, and the separate obligations of local mutation versus engine notification. It provides evolving choices and counterexamples, not a finished architecture to copy uncritically.

## Individual commit dispositions {#individual-commit-dispositions}

<a id="commit-1413"></a>
### 1413 · feat(scoreboard): add DisplaySlot {#commit-1413}

[Commit 2b5b56142a4c](https://github.com/EndstoneMC/endstone/commit/2b5b56142a4cab3959baea1c0290ddca1ae53635) · 2024-07-18T16:17:20Z · Git author/committer: Vincent.

Starts the public scoreboard surface with three display slots and Python exports/stubs. The binding file initially has the scordboard typo, corrected at 1433. There is no core scoreboard implementation yet; the enum and module are the first API scaffold.

Source paths: `include/endstone/scoreboard/display_slot.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/scoreboard.py`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/scordboard.cpp`.

<a id="commit-1414"></a>
### 1414 · feat(scoreboard): add Objective {#commit-1414}

[Commit 072631ba06e3](https://github.com/EndstoneMC/endstone/commit/072631ba06e3d06045dafab7d3ae99d18ee69927) · 2024-07-18T16:28:26Z · Git author/committer: Vincent.

Adds Objective name/display-name/isValid contracts and Python properties. Validity is only an abstract interface here, removed at 1420 and later represented through optional getters and logged checks. Do not interpret this initial name as evidence of an implemented lifetime-safe validity mechanism.

Source paths: `include/endstone/scoreboard/objective.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/scoreboard.py`, `src/endstone_python/scordboard.cpp`.

<a id="commit-1415"></a>
### 1415 · feat(scoreboard): add Criteria {#commit-1415}

[Commit c96d508bdbe6](https://github.com/EndstoneMC/endstone/commit/c96d508bdbe6de0e9ca5668dac92d3ee2cb0523a) · 2024-07-18T16:37:01Z · Git author/committer: Vincent.

Adds the initial Dummy criteria enum with Python exports. The binding includes the scoreboard header before it is added at 1416, illustrating staged source construction. Criteria later becomes an object with a nested type enum; this early representation is not the final API.

Source paths: `include/endstone/scoreboard/criteria.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/scoreboard.py`, `src/endstone_python/scordboard.cpp`.

<a id="commit-1416"></a>
### 1416 · feat(scoreboard): add Scoreboard {#commit-1416}

[Commit b80621ec1eaa](https://github.com/EndstoneMC/endstone/commit/b80621ec1eaa2fcb7f918e047b56932bcb19f242) · 2024-07-18T17:02:59Z · Git author/committer: Vincent.

Defines registration, name/slot lookup, objective/entry collection and clear-slot contracts. Duplicate registration initially promises the existing Objective reference. Python's add_objective lambda discards that return and consequently advertises None in the stub. No core implementation exists yet. This mismatch persists through the unit even as C++ ownership changes.

Source paths: `include/endstone/scoreboard/scoreboard.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/scoreboard.py`, `src/endstone_python/scordboard.cpp`.

<a id="commit-1417"></a>
### 1417 · docs: add reference for endstone.scoreboard {#commit-1417}

[Commit 6bb9fe82222b](https://github.com/EndstoneMC/endstone/commit/6bb9fe82222b5233f2618c1b26414d80fbbac165) · 2024-07-18T17:04:09Z · Git author/committer: Vincent.

Adds the endstone.scoreboard API-reference page and navigation. It documents the newly exposed module; it does not make the native implementation complete or provide a usage test.

Source paths: `docs/reference/python/scoreboard.md`, `mkdocs.yml`.

<a id="commit-1418"></a>
### 1418 · feat(scoreboard): update return value policies in scoreboard bindings {#commit-1418}

[Commit 7a58866b3e38](https://github.com/EndstoneMC/endstone/commit/7a58866b3e3887b35514a9156d66ee3aba4fb0ad) · 2024-07-18T21:07:05Z · Git author/committer: Vincent.

Changes sets to vectors, introduces Player/Actor/string entries and adds reference/reference_internal return policies. The forward declarations initially resolve to native global types rather than Endstone types, fixed at 1437. Module initialization is reordered, then revised again at 1419. Return policies cannot repair the still-void registration lambda or prove pointee lifetime ownership.

Source paths: `include/endstone/scoreboard/scoreboard.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/scordboard.cpp`.

<a id="commit-1419"></a>
### 1419 · feat(scoreboard): add getScores and resetScores {#commit-1419}

[Commit 79688737f9e4](https://github.com/EndstoneMC/endstone/commit/79688737f9e42538a57e3683e3cd683ca1a99b9d) · 2024-07-18T21:27:57Z · Git author/committer: Vincent.

Extracts ScoreEntry, adds the initial Score interface and getScores/resetScores contracts, and exposes them in Python. Runtime initialization order is restored with Actor/Player before Scoreboard while declarations are organized separately. This is staged API and dependency-order work, still preceding real score operations.

Source paths: `include/endstone/scoreboard/score.h`, `include/endstone/scoreboard/score_entry.h`, `include/endstone/scoreboard/scoreboard.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/scordboard.cpp`.

<a id="commit-1420"></a>
### 1420 · feat(scoreboard): expand Objective class {#commit-1420}

[Commit 52d521f94247](https://github.com/EndstoneMC/endstone/commit/52d521f94247c1fdef6827f7e1f57e83f0a84302) · 2024-07-18T22:01:37Z · Git author/committer: Vincent.

Expands Objective with display name, criteria, modifiability, scoreboard, slot, sort order and score access. It removes isValid and adds ObjectiveSortOrder. Python class objects are declared before attaching cross-referencing methods. These contracts initially use raw references and nonoptional getters; the later ownership and invalid-state revisions are essential context.

Source paths: `include/endstone/scoreboard/objective.h`, `include/endstone/scoreboard/objective_sort_order.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/scordboard.cpp`.

<a id="commit-1421"></a>
### 1421 · feat(scoreboard): expand Score class {#commit-1421}

[Commit d25ff99d0c31](https://github.com/EndstoneMC/endstone/commit/d25ff99d0c31a524775ab318822154805198329e) · 2024-07-18T22:10:57Z · Git author/committer: Vincent.

Expands Score with entry/value mutation, isScoreSet and Objective/Scoreboard access, mirrored by Python properties. The distinction between zero and never-set becomes part of the contract. At this point it remains an interface with raw parent references, not an implemented identity lookup or storage mutation.

Source paths: `include/endstone/scoreboard/score.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/scordboard.cpp`.

<a id="commit-1422"></a>
### 1422 · feat(scoreboard): add ObjectiveSortOrder and Score to endstone.scoreboard module {#commit-1422}

[Commit 3712cdc91c37](https://github.com/EndstoneMC/endstone/commit/3712cdc91c3751d57188336a135e2108fa6e856c) · 2024-07-18T22:20:13Z · Git author/committer: Vincent.

Exports Score and ObjectiveSortOrder from the public Python scoreboard module after their bindings already exist. This closes a discoverability gap without adding behavior or test evidence.

Source paths: `python/src/endstone/scoreboard.py`.

<a id="commit-1423"></a>
### 1423 · feat(scoreboard): add ObjectiveCriteria and ObjectiveRenderType {#commit-1423}

[Commit ed478178a0b8](https://github.com/EndstoneMC/endstone/commit/ed478178a0b8e6f17a7fe8f2e9ddfceb30f49e92) · 2024-07-19T08:55:14Z · Git author/committer: Vincent.

Models native ObjectiveCriteria name/read-only/render fields and an 8-bit integer render enum. The getters expose engine state for the adapter. This is a reverse-engineered/native layout declaration, not new criteria computation or proof of a verified binary offset.

Source paths: `include/bedrock/world/scores/objective_criteria.h`, `include/bedrock/world/scores/objective_render_type.h`.

<a id="commit-1424"></a>
### 1424 · feat(scoreboard): add RenderType and Criteria::Type {#commit-1424}

[Commit 77f1d0b68fd6](https://github.com/EndstoneMC/endstone/commit/77f1d0b68fd68cab8bfc06b2880f7cc382594256) · 2024-07-19T09:11:17Z · Git author/committer: Vincent.

Replaces Criteria's enum with an abstract object plus nested Type::Dummy and introduces public RenderType. Python export_values retains Criteria.DUMMY as an alias while adding object properties. Objective now returns a criteria reference. The pure virtual destructor lacks a definition here and is changed to default at 1435; intermediate buildability is not assumed.

Source paths: `include/endstone/scoreboard/criteria.h`, `include/endstone/scoreboard/objective.h`, `include/endstone/scoreboard/render_type.h`, `include/endstone/scoreboard/scoreboard.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/scordboard.cpp`.

<a id="commit-1425"></a>
### 1425 · feat(scoreboard): add EndstoneCriteria {#commit-1425}

[Commit 5d3aa39f3d09](https://github.com/EndstoneMC/endstone/commit/5d3aa39f3d0923822fceb71524bee74f3ed11240) · 2024-07-19T09:23:25Z · Git author/committer: Vincent.

Adds EndstoneCriteria as a borrowed adapter over native ObjectiveCriteria, forwarding name/read-only and casting the render enum. Public RenderType becomes uint8_t to align the modeled representation. This does not transfer ownership or make the underlying criteria independent of the engine.

Source paths: `include/endstone/detail/scoreboard/criteria.h`, `include/endstone/scoreboard/render_type.h`, `src/endstone_core/scoreboard/criteria.cpp`.

<a id="commit-1426"></a>
### 1426 · feat(scoreboard): add an overload of Scoreboard::addObjective {#commit-1426}

[Commit 1212f83ab3ce](https://github.com/EndstoneMC/endstone/commit/1212f83ab3cef787ea460de310169a81d6951cf8) · 2024-07-19T09:38:53Z · Git author/committer: Vincent.

Adds registration with explicit render type and Objective render accessors, plus Python's Integer default. The registration lambda still discards the result. Later 1440 explicitly reports render mutation unsupported, so the writable-looking early API is a promise under development rather than evidence of an implemented capability.

Source paths: `include/endstone/scoreboard/objective.h`, `include/endstone/scoreboard/scoreboard.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/scordboard.cpp`.

<a id="commit-1428"></a>
### 1428 · feat(scoreboard): add Objective, ObjectiveSortOrder and ScoreboardId {#commit-1428}

[Commit c9869470cd72](https://github.com/EndstoneMC/endstone/commit/c9869470cd72f60e598ddb86f6d112e2def8021c) · 2024-07-19T10:20:52Z · Git author/committer: Vincent.

Models native Scoreboard virtuals, Objective fields and ScoreboardId, including annotated platform offsets. These declarations establish prerequisites for the adapter; they do not implement Endstone registration or validate the commented offsets. The native Objective's map and borrowed criteria are distinct from the public wrapper ownership introduced later.

Source paths: `include/bedrock/forward.h`, `include/bedrock/world/level/level_interface.h`, `include/bedrock/world/scores/objective.h`, `include/bedrock/world/scores/objective_sort_order.h`, `include/bedrock/world/scores/scoreboard.h`, `include/bedrock/world/scores/scoreboard_id.h`.

<a id="commit-1430"></a>
### 1430 · feat(scoreboard): add Scoreboard members {#commit-1430}

[Commit 881ee5c27a06](https://github.com/EndstoneMC/endstone/commit/881ee5c27a068aaf3467cdfb54dc35903fade9d0) · 2024-07-19T11:23:54Z · Git author/committer: Vincent.

Adds native scoreboard maps for identities, objectives, criteria and display state, plus event-coordinator fields and a command soft-enum registry. Some formerly unknown thread-related fields receive names. This is layout reconstruction, not a new synchronization algorithm or a guarantee that all referenced types are complete at the intermediate revision.

Source paths: `include/bedrock/server/commands/command_soft_enum_registry.h`, `include/bedrock/world/events/event_coordinator.h`, `include/bedrock/world/scores/scoreboard.h`, `include/bedrock/world/scores/scoreboard_identity_ref.h`.

<a id="commit-1431"></a>
### 1431 · feat(scoreboard): add EndstoneScoreboard {#commit-1431}

[Commit daa56de4adb9](https://github.com/EndstoneMC/endstone/commit/daa56de4adb9ef4493255fe40e444874fa80423d) · 2024-07-19T11:30:33Z · Git author/committer: Vincent.

Creates EndstoneScoreboard, owned by EndstoneServer and initialized from the engine level before the original level-initialized callback. Most methods throw Not implemented; the three-argument registration overload also forwards name instead of the supplied display name. The server stores the wrapper but its public getter is absent through 1440. These scaffolds must not be presented as a shipped usable scoreboard feature.

Source paths: `include/endstone/detail/scoreboard/scoreboard.h`, `include/endstone/detail/server.h`, `src/endstone_core/scoreboard/scoreboard.cpp`, `src/endstone_core/server.cpp`, `src/endstone_runtime/bedrock/world/events/event_coordinator.cpp`.

<a id="commit-1432"></a>
### 1432 · feat(scoreboard): Scoreboard::addObjective now returns nullptr if an objective with the given name already exists {#commit-1432}

[Commit 81b77c9d262a](https://github.com/EndstoneMC/endstone/commit/81b77c9d262a166e1f4c0b0143d46e84ca61b403) · 2024-07-19T11:40:03Z · Git author/committer: Vincent.

Changes duplicate-registration semantics from returning the existing Objective to rejecting with nullptr, and adjusts pointer signatures/docs. The core operation still throws, so this is an explicit API-policy revision preceding implementation. Python's void-return lambda is unchanged.

Source paths: `include/endstone/detail/scoreboard/scoreboard.h`, `include/endstone/scoreboard/scoreboard.h`, `src/endstone_core/scoreboard/scoreboard.cpp`.

<a id="commit-1433"></a>
### 1433 · feat(scoreboard): use std::share_ptr as the holder for Objective and Score {#commit-1433}

[Commit 51720715cc6c](https://github.com/EndstoneMC/endstone/commit/51720715cc6c8e0038ee6d9050392ab4769d5559) · 2024-07-19T12:56:18Z · Git author/committer: Vincent.

Changes Objective and Score returns/collections to shared_ptr with matching Python holders, and fixes the binding filename. Native name lookup is implemented against the map, while the Endstone wrapper lookup remains TODO until 1434. This records an observed shared-ownership design stage; no explicit rationale or benchmark supports a broader preference.

Source paths: `include/bedrock/world/scores/scoreboard.h`, `include/endstone/detail/scoreboard/scoreboard.h`, `include/endstone/scoreboard/objective.h`, `include/endstone/scoreboard/scoreboard.h`, `src/endstone_core/scoreboard/scoreboard.cpp`, `src/endstone_python/scordboard.cpp`, `src/endstone_python/scoreboard.cpp`, `src/endstone_runtime/bedrock/world/scores/scoreboard.cpp`.

<a id="commit-1434"></a>
### 1434 · feat(scoreboard): add DisplayObjective {#commit-1434}

[Commit 9fd9b690ed34](https://github.com/EndstoneMC/endstone/commit/9fd9b690ed340a43d27a328f4acb9d033675805c) · 2024-07-19T14:18:12Z · Git author/committer: Vincent.

Adds DisplayObjective, native Objective accessors and a fresh shared EndstoneObjective wrapper for each name lookup. The wrapper owns a copied name and criteria adapter but borrows the board/native Objective. checkState only checks whether that name exists, returning defaults/logging otherwise; it does not compare identity after unregister/recreate. Criteria becomes a nullable pointer, and the Python is_modifiable spelling changes.

Source paths: `include/bedrock/forward.h`, `include/bedrock/world/scores/display_objective.h`, `include/bedrock/world/scores/objective.h`, `include/bedrock/world/scores/scoreboard.h`, `include/endstone/detail/scoreboard/criteria.h`, `include/endstone/detail/scoreboard/objective.h`, `include/endstone/detail/scoreboard/scoreboard.h`, `include/endstone/scoreboard/objective.h`, `src/endstone_core/scoreboard/criteria.cpp`, `src/endstone_core/scoreboard/objective.cpp`, `src/endstone_core/scoreboard/scoreboard.cpp`, `src/endstone_python/scoreboard.cpp`, `src/endstone_runtime/bedrock/world/scores/objective.cpp`, `src/endstone_runtime/bedrock/world/scores/scoreboard.cpp`.

<a id="commit-1435"></a>
### 1435 · feat(scoreboard): basic implementation of EndstoneObjective {#commit-1435}

[Commit 2e5d056f7374](https://github.com/EndstoneMC/endstone/commit/2e5d056f73743bd179db738864036832eebf4ba8) · 2024-07-19T15:30:35Z · Git author/committer: Vincent.

Makes invalid names/display names/render/slot/order optional rather than conflating absence with empty strings/default enums. Slot and order getters search native display slots. Display-name mutation still carries an explicit dirty-notification TODO, and setters remain incomplete. The Criteria destructor is defaulted; ScoreboardId gets a -1 invalid sentinel. These are distinct state-model repairs within the scaffold.

Source paths: `include/bedrock/world/scores/scoreboard_id.h`, `include/endstone/detail/scoreboard/objective.h`, `include/endstone/scoreboard/criteria.h`, `include/endstone/scoreboard/display_slot.h`, `include/endstone/scoreboard/objective.h`, `include/endstone/scoreboard/objective_sort_order.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_core/scoreboard/objective.cpp`.

<a id="commit-1436"></a>
### 1436 · feat(scoreboard): add functions to Scoreboard and IdentityDictionary {#commit-1436}

[Commit f4df80a55176](https://github.com/EndstoneMC/endstone/commit/f4df80a551761cac2a1c08fdd267387112a486ab) · 2024-07-19T16:19:13Z · Git author/committer: Vincent.

Groups four identity maps into IdentityDictionary and adds ID equality/hash and native lookup helpers. String lookup first tries fake-player names, then parses an entity ID with stoll; no full-consumption check is made. hasScore distinguishes absence from getPlayerScore's zero fallback. The method names describe lookup, not automatic identity creation or player lifetime retention.

Source paths: `include/bedrock/forward.h`, `include/bedrock/world/actor/actor_unique_id.h`, `include/bedrock/world/scores/identity_dictionary.h`, `include/bedrock/world/scores/objective.h`, `include/bedrock/world/scores/player_scoreboard_id.h`, `include/bedrock/world/scores/scoreboard.h`, `include/bedrock/world/scores/scoreboard_id.h`, `include/bedrock/world/scores/scoreboard_identity_ref.h`, `src/endstone_runtime/bedrock/world/scores/objective.cpp`, `src/endstone_runtime/bedrock/world/scores/scoreboard.cpp`.

<a id="commit-1437"></a>
### 1437 · feat(scoreboard): add EndstoneScore {#commit-1437}

[Commit dade75aeca23](https://github.com/EndstoneMC/endstone/commit/dade75aeca238c82de25704001fea2913f904399) · 2024-07-20T15:00:15Z · Git author/committer: Vincent.

Fixes ScoreEntry forward declarations into the Endstone namespace and implements EndstoneScore with borrowed Objective and raw actor/player entries. Reads return zero/false for absent scores; mutation is still TODO. Objective::getScore switches from shared_ptr to unique_ptr, with Python's default holder. Ownership of the new wrapper does not extend the borrowed parent's lifetime.

Source paths: `include/bedrock/world/scores/scoreboard_id.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/scoreboard/objective.h`, `include/endstone/detail/scoreboard/score.h`, `include/endstone/detail/scoreboard/scoreboard.h`, `include/endstone/scoreboard/objective.h`, `include/endstone/scoreboard/score_entry.h`, `src/endstone_core/actor/actor.cpp`, `src/endstone_core/scoreboard/objective.cpp`, `src/endstone_core/scoreboard/score.cpp`, `src/endstone_python/scoreboard.cpp`.

<a id="commit-1438"></a>
### 1438 · feat(scoreboard): implement Score::setScore {#commit-1438}

[Commit 0681cdf182ae](https://github.com/EndstoneMC/endstone/commit/0681cdf182ae40af1573bcb48d8d2aa0dfeda368) · 2024-07-20T15:22:30Z · Git author/committer: Vincent.

Implements setting a score only for an existing valid identity and a modifiable objective. The native helper directly changes the scores map and supports Set/Add/Subtract, checking read-only state again. It does not call scoreboard change notification or create identities. Invalid-ID return occurs before the later error path, so missing-entry diagnostics are not uniformly emitted. Client/persistence effects remain untested.

Source paths: `include/bedrock/world/scores/objective.h`, `include/bedrock/world/scores/player_score_set_function.h`, `src/endstone_core/scoreboard/score.cpp`, `src/endstone_runtime/bedrock/world/scores/objective.cpp`.

<a id="commit-1439"></a>
### 1439 · refactor(scoreboard): use unique_ptr instead of shared_ptr for Objective {#commit-1439}

[Commit c4b9392db417](https://github.com/EndstoneMC/endstone/commit/c4b9392db41720fa3419b8eeea30041d0bd4b4be) · 2024-07-20T15:28:26Z · Git author/committer: Vincent.

Replaces shared_ptr with unique_ptr for Objective returns and Score/Objective collections, using a fresh unique wrapper per name lookup and default Python holders. Borrowed native Objective/board references and Score's borrowed wrapper parent remain unchanged. This reverses the 1433 ownership experiment without a stated reason; it is not evidence that shared_ptr is categorically disfavored.

Source paths: `include/endstone/detail/scoreboard/scoreboard.h`, `include/endstone/scoreboard/scoreboard.h`, `src/endstone_core/scoreboard/scoreboard.cpp`, `src/endstone_python/scoreboard.cpp`.

<a id="commit-1440"></a>
### 1440 · feat(scoreboard): implement all methods in EndstoneObjective {#commit-1440}

[Commit 3623534043a7](https://github.com/EndstoneMC/endstone/commit/3623534043a702d242bd6a5b66f0f50071f449de) · 2024-07-20T22:42:58Z · Git author/committer: Vincent.

Consolidates display slot/order mutation into setDisplay, clearing previous slots and optionally assigning a new one with ascending default. C++ DisplaySlot::None shifts enum values but is not exported in Python here. Render mutation only logs unsupported despite the all-methods title; board registration/enumeration still throw. Name-only validity, borrowed parent lifetime and notification gaps remain explicit endpoint limitations.

Source paths: `include/endstone/detail/scoreboard/objective.h`, `include/endstone/scoreboard/display_slot.h`, `include/endstone/scoreboard/objective.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_core/scoreboard/objective.cpp`, `src/endstone_python/scoreboard.cpp`.
