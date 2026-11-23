<!-- retrieval: {"source_ids":["public:commit:01745a6b13b1fa64c3606d1ce2fe40631ff866f9","public:commit:0ce5ea4f68be72b7e16b1201951154a2482003ef","public:commit:11438391fae019dab41b42b962c846e7f0efd5bf","public:commit:14200cbbdebe488eaf07d8e3c130fc896f74247b","public:commit:18f5a453d6f18c40355a324d68ef364568521cc2","public:commit:3c9907c50e45b6916c31254e62bc37b2928f1cd6","public:commit:4a9d708d6bd34851ab4e67b1f9d7a4376d53f905","public:commit:4e7d65fe642ec81557f1ad84b1a448fd7f625c77","public:commit:59c7ca2db2967c29479d44f6302e6fd64116e7d6","public:commit:63d14f129c1565783664abc92542b8252a616949","public:commit:6ca042ce64a140e38df743fb24a9ba90646f2f2c","public:commit:721ad79b846d1c6695dc264f2e4ab0b039742a86","public:commit:94366c1a01f523bde2b9441d24edbe8c2303b313","public:commit:96266f4345d08b4a7a1ba2db0a1abb0a51b21597","public:commit:9995e17700d2619584b0e6c6921792c9885d72e3","public:commit:ed328702a6ffb282919244b17c6c5f035a4071fd","public:commit:f38b81d0921937af96109ec1456b6d994af3727e"],"source_type":"public","date":"2024-10-11..2024-10-22","topics":["ffi","testing","api","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Language, actor tags, health and particle APIs {#language-actor-tags-health-and-particle-apis}

Scope: Endstone commits 1801–1920, September 14–October 22, 2024. These notes follow related implementation areas during this period.

## Cross-language contracts and mutable native state {#cross-language-contracts-and-mutable-native-state}

Language support evolves from a breaking Translatable accessor/import move to native I18n delegation and an owned Server language service. The serialized translate/with keys stay stable while C++ headers and Python imports/properties change. Unknown locales fall back through current localization and then en_US. This is useful migration evidence, not a custom translation-dictionary implementation or an observed benchmark.

Actor tags expose a richer corrective chain. Read access arrives first, then add/remove mutate an interned IndexSet while failing to retain the new set ID. The later repair copies the set and assigns the resulting ID, keeping other actors' interned membership independent. A separate sparse-index removal defect remains in the unchanged helper. The explicit [10,20] counterexample in 1914 is hand-derived from source, not an executed test. IDType wraps an optional integer, so present zero is valid; conflating optional presence with integer truthiness would produce a false diagnosis.

Health reads round native floating values upward into integers and return zero when a component is absent. The setter validates against max health and uses Result, but persistent-component mutation has stronger prerequisites than the read fallback. Particle spawning then demonstrates another narrow API/packet mismatch: the initial actor ID makes supplied positions relative to the player; removing it relies on the packet's verified -1 default for world coordinates. Recipient dimension remains separate from the Location argument's dimension.

Use these cases to check language binding/stub/export agreement, value-versus-presence semantics, interned/shared state mutation, native-object prerequisites and packet coordinate conventions. The evidence does not support a broad claim that these APIs were fully tested. Mock changes for language service contain no added assertions, and no native translation, tag mutation, health update or client rendering was run.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1878"></a>
### Commit 1878 · feat: add Actor::getScoreboardTags {#commit-1878}

Source: [9995e17700d2619584b0e6c6921792c9885d72e3](https://github.com/EndstoneMC/endstone/commit/9995e17700d2619584b0e6c6921792c9885d72e3). Authored 2024-10-11T12:49:31Z; committed 2024-10-11T12:49:31Z. Git author: Vincent; committer: Vincent.


Adds scoreboard-tag reads through a typed native TagRegistry/IndexSet and exposes them through Actor/Mob/Player and Python. Missing tag components produce an empty vector; TagSystem::hasTag is still incomplete at this point. The first parent is daoge's separately authored defaultBlockStateHash export commit. Later tag mutation needs both set interning and per-actor ID updates, not merely this read API.

Changed-source navigation: `include/bedrock/entity/components/tags_component.h`, `include/bedrock/entity/systems/tag_system.h`, `include/bedrock/forward.h`, `include/bedrock/util/biome_tag_registry_types.h`, `include/bedrock/util/index_set.h`, `include/bedrock/util/level_tag_registry_types.h`, `include/bedrock/util/tag_registry.h`; plus 13 paths not listed here.

<a id="commit-1902"></a>
### Commit 1902 · refactor: rename variables in Translatable {#commit-1902}

Source: [4e7d65fe642ec81557f1ad84b1a448fd7f625c77](https://github.com/EndstoneMC/endstone/commit/4e7d65fe642ec81557f1ad84b1a448fd7f625c77). Authored 2024-10-19T18:03:09Z; committed 2024-10-19T18:03:09Z. Git author: Vincent; committer: Vincent.


Renames Translatable's C++ accessors to getText/getParameters and Python properties to text/params, updating callers. JSON wire keys remain translate/with. This separates source API compatibility from serialized protocol compatibility: existing Python/C++ consumers need migration even though the message wire shape is unchanged. No legacy aliases are introduced in the reviewed patch.

Changed-source navigation: `include/endstone/translatable.h`, `src/endstone_core/command/command_origin_wrapper.cpp`, `src/endstone_core/form/form_codec.cpp`, `src/endstone_core/message.cpp`, `src/endstone_core/player.cpp`, `src/endstone_python/endstone_python.cpp`.

<a id="commit-1904"></a>
### Commit 1904 · refactor: move translatable.h to lang folder {#commit-1904}

Source: [f38b81d0921937af96109ec1456b6d994af3727e](https://github.com/EndstoneMC/endstone/commit/f38b81d0921937af96109ec1456b6d994af3727e). Authored 2024-10-20T10:34:53Z; committed 2024-10-20T10:34:53Z. Git author: Vincent; committer: Vincent.


Moves Translatable into the lang include hierarchy with unchanged body and adds Language/EndstoneLanguage placeholders. The include path is a compatibility change even though the moved implementation is identical. Actual translation behavior is supplied in 1906, avoiding premature credit for the scaffold.

Changed-source navigation: `include/endstone/detail/lang/language.h`, `include/endstone/lang/language.h`, `include/endstone/lang/translatable.h`, `include/endstone/message.h`, `include/endstone/translatable.h`, `src/endstone_core/lang/language.cpp`.

<a id="commit-1905"></a>
### Commit 1905 · feat: add optional_ref wrapper class {#commit-1905}

Source: [11438391fae019dab41b42b962c846e7f0efd5bf](https://github.com/EndstoneMC/endstone/commit/11438391fae019dab41b42b962c846e7f0efd5bf). Authored 2024-10-20T10:44:05Z; committed 2024-10-20T10:44:05Z. Git author: Vincent; committer: Vincent.


Changes optional_ref from a T* alias into a one-pointer wrapper with null construction and unwrap. It models a native interface more explicitly but adds no automatic null validation. Related forward declarations and the remaining Translatable include are aligned with the new layout.

Changed-source navigation: `include/bedrock/core/utility/optional_ref.h`, `include/bedrock/forward.h`, `include/bedrock/locale/i18n.h`, `include/bedrock/world/level/block/block_legacy.h`, `src/endstone_runtime/bedrock/server/server_player.cpp`.

<a id="commit-1906"></a>
### Commit 1906 · feat: implement endstone::Language {#commit-1906}

Source: [6ca042ce64a140e38df743fb24a9ba90646f2f2c](https://github.com/EndstoneMC/endstone/commit/6ca042ce64a140e38df743fb24a9ba90646f2f2c). Authored 2024-10-20T13:07:33Z; committed 2024-10-20T13:07:33Z. Git author: Vincent; committer: Vincent.


Implements translation overloads through the native I18n/Localization service. An unknown requested locale falls back to the current localization; absent current localization falls back to en_US. It does not create an independent plugin translation store. Public virtual declarations initially lack pure-virtual markers/definitions and are corrected in 1907. The native fallback policy is observed in full source, not tested against installed language resources.

Changed-source navigation: `include/bedrock/core/utility/optional_ref.h`, `include/bedrock/forward.h`, `include/bedrock/locale/i18n.h`, `include/bedrock/locale/localization.h`, `include/endstone/detail/lang/language.h`, `include/endstone/lang/language.h`, `src/endstone_core/lang/language.cpp`; plus 1 paths not listed here.

<a id="commit-1907"></a>
### Commit 1907 · feat: add Server::getLanguage {#commit-1907}

Source: [18f5a453d6f18c40355a324d68ef364568521cc2](https://github.com/EndstoneMC/endstone/commit/18f5a453d6f18c40355a324d68ef364568521cc2). Authored 2024-10-20T13:25:12Z; committed 2024-10-20T13:25:12Z. Git author: Vincent; committer: Vincent.


Makes the Language interface pure virtual and gives Server an owned EndstoneLanguage/getLanguage service. Test mocks adapt to the new Server API but add no behavioral assertions. This completes the construction/access contract missing from the preceding scaffold, not proof of translation output across locales.

Changed-source navigation: `include/endstone/detail/server.h`, `include/endstone/lang/language.h`, `include/endstone/server.h`, `src/endstone_core/server.cpp`, `tests/plugin/test_cpp_plugin_loader.cpp`, `tests/scheduler/test_scheduler.cpp`.

<a id="commit-1908"></a>
### Commit 1908 · feat: add python bindings for language {#commit-1908}

Source: [94366c1a01f523bde2b9441d24edbe8c2303b313](https://github.com/EndstoneMC/endstone/commit/94366c1a01f523bde2b9441d24edbe8c2303b313). Authored 2024-10-20T13:43:26Z; committed 2024-10-20T13:43:26Z. Git author: Vincent; committer: Vincent.


Exposes endstone.lang, server.language and translation overloads with optional parameters/locale, updates references/tutorials and removes the old root-level Translatable export. No compatibility alias is retained. This is a coordinated documentation, runtime binding and stub migration; users must change imports as well as the properties renamed in 1902.

Changed-source navigation: `docs/reference/python/lang.md`, `docs/tutorials/register-commands.md`, `include/endstone/lang/language.h`, `mkdocs.yml`, `python/src/endstone/__init__.py`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/lang.py`; plus 2 paths not listed here.

<a id="commit-1909"></a>
### Commit 1909 · feat: add python bindings for the overloaded method of Language::translate {#commit-1909}

Source: [14200cbbdebe488eaf07d8e3c130fc896f74247b](https://github.com/EndstoneMC/endstone/commit/14200cbbdebe488eaf07d8e3c130fc896f74247b). Authored 2024-10-20T14:01:00Z; committed 2024-10-20T14:01:00Z. Git author: Vincent; committer: Vincent.


Adds Python translation directly from a Translatable object and cleans up the obsolete miscellaneous reference entry. This completes an overload omitted in 1908 rather than changing the native localization algorithm or fallback order.

Changed-source navigation: `docs/reference/python/misc.md`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/lang.cpp`.

<a id="commit-1910"></a>
### Commit 1910 · feat: implement Actor::addTag {#commit-1910}

Source: [63d14f129c1565783664abc92542b8252a616949](https://github.com/EndstoneMC/endstone/commit/63d14f129c1565783664abc92542b8252a616949). Authored 2024-10-21T17:16:18Z; committed 2024-10-21T17:16:18Z. Git author: Vincent; committer: Vincent.


Implements native tag addition, IndexSet membership/insertion and TagSystem::hasTag. The first TagRegistry implementation mutates an interned set in place and discards a newly interned set ID at the actor call site, creating problems for shared sets and changed membership. IDType holds an optional integer: zero is a valid present ID, so the truth check must not be misreported as rejecting zero. Native cache accounting happens before the set update. These details lead to 1914's copy-on-write repair.

Changed-source navigation: `include/bedrock/entity/systems/tag_system.h`, `include/bedrock/util/index_set.h`, `include/bedrock/util/tag_registry.h`, `include/bedrock/world/actor/actor.h`, `src/endstone_runtime/bedrock/util/index_set.cpp`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`.

<a id="commit-1911"></a>
### Commit 1911 · feat: add Actor::addScoreboardTag {#commit-1911}

Source: [0ce5ea4f68be72b7e16b1201951154a2482003ef](https://github.com/EndstoneMC/endstone/commit/0ce5ea4f68be72b7e16b1201951154a2482003ef). Authored 2024-10-21T20:44:17Z; committed 2024-10-21T20:44:17Z. Git author: Vincent; committer: Vincent.


Exposes addScoreboardTag through Actor/Mob/Player and Python, returning whether a tag was newly added. Const wrapper methods still mutate the underlying native entity. The forwarding API does not fix the initial registry/ID behavior from 1910 and has no new test assertions.

Changed-source navigation: `include/endstone/actor/actor.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/mob.h`, `include/endstone/detail/player.h`, `src/endstone_core/actor/actor.cpp`, `src/endstone_core/actor/mob.cpp`, `src/endstone_core/player.cpp`; plus 1 paths not listed here.

<a id="commit-1912"></a>
### Commit 1912 · feat: implement Actor::removeTag {#commit-1912}

Source: [ed328702a6ffb282919244b17c6c5f035a4071fd](https://github.com/EndstoneMC/endstone/commit/ed328702a6ffb282919244b17c6c5f035a4071fd). Authored 2024-10-21T21:22:34Z; committed 2024-10-21T21:22:34Z. Git author: Vincent; committer: Vincent.


Implements native tag removal and IndexSet::remove, while still discarding the replacement set ID. The sparse-index repair loop writes sparse_[i] rather than sparse_[packed_[i]], so removing an item can invalidate membership for retained nontrivial IDs. Python's add-tag stub is also caught up. The set-ID problem is addressed in 1914; the sparse-index defect is not, and these two failures must not be conflated.

Changed-source navigation: `include/bedrock/entity/systems/tag_system.h`, `include/bedrock/util/index_set.h`, `include/bedrock/util/tag_registry.h`, `include/bedrock/world/actor/actor.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_runtime/bedrock/util/index_set.cpp`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`.

<a id="commit-1913"></a>
### Commit 1913 · feat: add Actor::removeScoreboardTag {#commit-1913}

Source: [01745a6b13b1fa64c3606d1ce2fe40631ff866f9](https://github.com/EndstoneMC/endstone/commit/01745a6b13b1fa64c3606d1ce2fe40631ff866f9). Authored 2024-10-21T21:28:22Z; committed 2024-10-21T21:28:22Z. Git author: Vincent; committer: Vincent.


Adds removeScoreboardTag forwarding and the corresponding Python method/stub. This exposes the current native removal semantics; it is not separate evidence that IndexSet removal or registry ID reassignment is correct.

Changed-source navigation: `include/endstone/actor/actor.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/mob.h`, `include/endstone/detail/player.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_core/actor/actor.cpp`, `src/endstone_core/actor/mob.cpp`; plus 2 paths not listed here.

<a id="commit-1914"></a>
### Commit 1914 · fix: Actor::removeScoreboardTag now functions correctly {#commit-1914}

Source: [721ad79b846d1c6695dc264f2e4ab0b039742a86](https://github.com/EndstoneMC/endstone/commit/721ad79b846d1c6695dc264f2e4ab0b039742a86). Authored 2024-10-22T12:33:11Z; committed 2024-10-22T12:33:11Z. Git author: Vincent; committer: Vincent.


Copies interned tag sets before mutation and assigns the returned tag_set_id for both add and remove, repairing shared-set mutation and discarded-ID errors. _getSet changes from checked at() to unchecked indexing, leaving bounds as an invariant. The unchanged IndexSet::remove still has its sparse-index bug: packed IDs [10,20] map to positions [0,1]; removing 10 moves 20 to position 0 but updates sparse_[0], not sparse_[20], so contains(20) can fail. This is a static counterexample, not an executed test, and the exact helper is proven unchanged through 1920.

Changed-source navigation: `include/bedrock/entity/systems/tag_system.h`, `include/bedrock/util/tag_registry.h`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`.

<a id="commit-1915"></a>
### Commit 1915 · feat: add Actor::getHealth and Actor::getMaxHealth {#commit-1915}

Source: [4a9d708d6bd34851ab4e67b1f9d7a4376d53f905](https://github.com/EndstoneMC/endstone/commit/4a9d708d6bd34851ab4e67b1f9d7a4376d53f905). Authored 2024-10-22T13:11:15Z; committed 2024-10-22T13:11:15Z. Git author: Vincent; committer: Vincent.


Adds health/max-health reads through native attributes and exposes them in C++ and Python. Float values are rounded upward to integers; absence of the attributes component returns zero. This is an integer API rather than general fractional-health support. The mutable path added next has different missing-component assumptions, so zero-read fallback is not a universal mutation guarantee.

Changed-source navigation: `include/bedrock/world/actor/actor.h`, `include/bedrock/world/attribute/attribute_instance.h`, `include/endstone/actor/actor.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/mob.h`, `include/endstone/detail/player.h`, `python/src/endstone/_internal/endstone_python.pyi`; plus 6 paths not listed here.

<a id="commit-1916"></a>
### Commit 1916 · feat: add Actor:setHealth {#commit-1916}

Source: [59c7ca2db2967c29479d44f6302e6fd64116e7d6](https://github.com/EndstoneMC/endstone/commit/59c7ca2db2967c29479d44f6302e6fd64116e7d6). Authored 2024-10-22T13:37:45Z; committed 2024-10-22T13:37:45Z. Git author: Vincent; committer: Vincent.


setHealth returns Result and validates the inclusive range zero through max health before updating the native attribute. Python reuses the Result-to-exception caster. Full native context shows getMutableAttribute requires the persistent attributes component; the zero fallback from reads does not establish a safe setter on entities without that component. No native attribute mutation or resulting gameplay was executed.

Changed-source navigation: `include/endstone/actor/actor.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/mob.h`, `include/endstone/detail/player.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_core/actor/actor.cpp`, `src/endstone_core/actor/mob.cpp`; plus 2 paths not listed here.

<a id="commit-1919"></a>
### Commit 1919 · feat: add Player::spawnParticle {#commit-1919}

Source: [96266f4345d08b4a7a1ba2db0a1abb0a51b21597](https://github.com/EndstoneMC/endstone/commit/96266f4345d08b4a7a1ba2db0a1abb0a51b21597). Authored 2024-10-22T15:21:15Z; committed 2024-10-22T15:21:15Z. Git author: Vincent; committer: Vincent.


Adds four C++ and two Python particle-spawn overloads plus release/stub updates. Packet delivery uses the recipient player's dimension; the Location overload does not select a different dimension from its argument. The initial packet also sets the player's actor ID, making the position actor-relative under the reported behavior; 1920 removes that. sendPacket becomes const, and the health setter stub is corrected to None. No client rendering was executed.

Changed-source navigation: `CHANGELOG.md`, `include/endstone/detail/player.h`, `include/endstone/player.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_core/player.cpp`, `src/endstone_python/endstone_python.cpp`.

<a id="commit-1920"></a>
### Commit 1920 · fix: use world position in Player::spawnParticle {#commit-1920}

Source: [3c9907c50e45b6916c31254e62bc37b2928f1cd6](https://github.com/EndstoneMC/endstone/commit/3c9907c50e45b6916c31254e62bc37b2928f1cd6). Authored 2024-10-22T15:44:49Z; committed 2024-10-22T15:44:49Z. Git author: Vincent; committer: Vincent.


Removes the player actor ID from SpawnParticleEffectPacket so supplied coordinates are world-relative. Full packet context confirms the default actor ID is -1, rather than leaving an uninitialized field. This is a small, causally clear repair immediately after 1919. It does not change the recipient-dimension behavior or establish cross-dimension particle delivery.

Changed-source navigation: `src/endstone_core/player.cpp`.
