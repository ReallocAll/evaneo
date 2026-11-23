<!-- retrieval: {"source_ids":["public:commit:0203f460a680c95573d70d22bd12bb22bc65b119","public:commit:155b58615e1f3ffba3ef3285889e68b0bf07f656","public:commit:2fc46abf22152fb5351ce4cc6c7ee3e7a9b0ab9e","public:commit:5e8bcaaab195abd661f38fce655ca1e8ffc50551","public:commit:64792e55c7177a3a991aba458701518bb066b864","public:commit:66118d80b3d363eccc16e0bc95e75564b573c0f6","public:commit:6f5e7beecb96095c5282370f06da1e6eaa660d7b","public:commit:8399ebac127b2074591e548a6e1c092df8cae79d","public:commit:9743cdccf357fa021c8ba2e4d18a41b6c74564d7","public:commit:9baae63854f2be912625891517644b90648f8434","public:commit:c60e145814d2e60b7479276391871893626798de","public:commit:db169eb60bad37e3b4b4c607dc8f60a6641936e5","public:commit:e293e49a10029f229b7cdd8c94d4f2c59c3ee72a","public:commit:ff8886b01bd5b97edf3e46049e300cda7b99dd4e"],"source_type":"public","date":"2024-04-10..2024-04-18","topics":["lifetime","ffi","testing","api","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Python surface: flatter imports, borrowed event objects, uneven migration coverage {#python-surface-flatter-imports-borrowed-event-objects-uneven-migration-coverage}

## Result and scope {#result-and-scope}

The Python API becomes flatter at the same time actor/player functionality expands. Public C++ header paths and constant spellings also change. The sequence demonstrates that “refactor” and “style” are insufficient semantic categories: import paths, C++ source compatibility and one native spawn cancellation repair change under those titles. Conversely, large binding-body moves are often behavior-preserving and should not receive invented rationale. [commit 644](https://github.com/EndstoneMC/endstone/commit/db169eb60bad37e3b4b4c607dc8f60a6641936e5) [commit 646](https://github.com/EndstoneMC/endstone/commit/6f5e7beecb96095c5282370f06da1e6eaa660d7b) [commit 650](https://github.com/EndstoneMC/endstone/commit/2fc46abf22152fb5351ce4cc6c7ee3e7a9b0ab9e) [commit 652](https://github.com/EndstoneMC/endstone/commit/9743cdccf357fa021c8ba2e4d18a41b6c74564d7) [commit 686](https://github.com/EndstoneMC/endstone/commit/a468885ff723625c2e288349815c6630be4489e8) [commit 697](https://github.com/EndstoneMC/endstone/commit/8399ebac127b2074591e548a6e1c092df8cae79d)

All changes in this family are Vincent-authored and Vincent-committed in the source metadata. There is no independently read PR-review rationale in this workunit. Generated `.pyi` changes were read as changed declarations and docs, not treated as proof of runtime execution or as separate original API design.

## 1. A flatter module surface, with consumer repairs {#1-a-flatter-module-surface-with-consumer-repairs}

ColorFormat, GameMode, Player and Level C++ headers move toward root include paths. Player's redundant `getName` declaration disappears while inherited behavior remains; GameMode and message methods gain documentation. Moving a public include path is source compatibility work even when function behavior is unchanged. [commit 644](https://github.com/EndstoneMC/endstone/commit/db169eb60bad37e3b4b4c607dc8f60a6641936e5) [commit 649](https://github.com/EndstoneMC/endstone/commit/0203f460a680c95573d70d22bd12bb22bc65b119)

Inside the extension, ColorFormat/GameMode registrations move out of `util.cpp` and the property macro is expanded into equivalent explicit registrations. Both old and new routines register on the same extension module, so that change alone does not move the public Python facade. The next commit moves facade exports from `endstone.util` to `endstone`, updates the color import test, and renames the misspelled Minecraft-version attribute. Bootstrap still refers to the old spelling until its immediate fix. [commit 645](https://github.com/EndstoneMC/endstone/commit/64792e55c7177a3a991aba458701518bb066b864) [commit 646](https://github.com/EndstoneMC/endstone/commit/6f5e7beecb96095c5282370f06da1e6eaa660d7b) [commit 648](https://github.com/EndstoneMC/endstone/commit/c60e145814d2e60b7479276391871893626798de)

Level, Logger and Server similarly move to root facade exports and their old modules are deleted without compatibility aliases. Import tests follow the new paths, then plugin_loader's Server import is repaired. The source demonstrates a simplification choice and its migration cost, but no policy statement about preserving or deliberately breaking third-party plugins. Do not infer a general compatibility philosophy from this pre-release-era local change. [commit 650](https://github.com/EndstoneMC/endstone/commit/2fc46abf22152fb5351ce4cc6c7ee3e7a9b0ab9e) [commit 651](https://github.com/EndstoneMC/endstone/commit/e293e49a10029f229b7cdd8c94d4f2c59c3ee72a)

Consolidating Level/Logger/Server registration into the main extension source keeps their bodies and return policies. It also preserves the existing Server.name→getVersion binding, confirmed in endpoint context. Moving code is not evidence that old mistakes were reviewed or repaired. The root facade at ordinal 720 still exports ColorFormat/GameMode/Level/Logger/Server, not Player; Actor/HumanActor have a separate actor facade and event modules expose player events. Internal binding existence and convenient public import availability are different milestones. [commit 652](https://github.com/EndstoneMC/endstone/commit/9743cdccf357fa021c8ba2e4d18a41b6c74564d7) [commit 666](https://github.com/EndstoneMC/endstone/commit/66118d80b3d363eccc16e0bc95e75564b573c0f6) [commit 668](https://github.com/EndstoneMC/endstone/commit/155b58615e1f3ffba3ef3285889e68b0bf07f656)

## 2. Borrowed actor/player events {#2-borrowed-actor-player-events}

Actor→HumanActor→Player is bound in the extension, and Player exposes UUID plus raw/popup/tip messages. Join/quit events expose their player, while actor spawn/removal expose their actor. The explicit reference policies are important: these are host-owned objects, not ownership transfers into Python. But reference borrowing does not extend native lifetime. At the first quit implementation, the wrapper is erased right after callback; after the ECS migration, destruction follows the native entity. Neither stage makes indefinite Python retention safe. [commit 666](https://github.com/EndstoneMC/endstone/commit/66118d80b3d363eccc16e0bc95e75564b573c0f6) [commit 667](https://github.com/EndstoneMC/endstone/commit/5e8bcaaab195abd661f38fce655ca1e8ffc50551) [commit 686](https://github.com/EndstoneMC/endstone/commit/a468885ff723625c2e288349815c6630be4489e8) [commit 687](https://github.com/EndstoneMC/endstone/commit/de5ee93545b7cc240cdc9233a4deab0b09aa605c) [commit 710](https://github.com/EndstoneMC/endstone/commit/90c597f1043f0c037257e6c94fc608fcb329acd6)

The event binding revision also adds reference policies for plugin and weather-level properties. A potentially suspicious `WeatherChangeEvent::getLevel` spelling in the thunder binding was checked against full class context: both derive from WeatherEvent, which actually declares the inherited getter. That spelling alone is not a demonstrated sibling-type error. This is a useful counterexample to turning a superficial diff observation into a bug claim. [commit 667](https://github.com/EndstoneMC/endstone/commit/5e8bcaaab195abd661f38fce655ca1e8ffc50551)

The spawn binding commit does more than register a class and update stubs: it removes the preceding unconditional cancellation. Popup/tip descriptions are corrected in the same commit. The generated stub is supporting evidence of the exposed signatures and text, while the native diff is the evidence that spawn behavior changes. [commit 685](https://github.com/EndstoneMC/endstone/commit/c6bbd884dd7861d9f704027dca263b0c09a9e3c2) [commit 686](https://github.com/EndstoneMC/endstone/commit/a468885ff723625c2e288349815c6630be4489e8)

## 3. UUID conversion is not proven bidirectional {#3-uuid-conversion-is-not-proven-bidirectional}

The manual caster names its Python type `uuid.UUID`, constructs an outbound object from a 16-byte array and attempts an inbound conversion using CPython calls. Several source-level limitations remain at the endpoint: inbound code invokes `bytes` as a method, intermediate objects are used without comprehensive null/error checks, and the final success return is `PyErr_Occurred() != nullptr`. Even a hypothetical clean conversion would return false. There is no round-trip test in these patches. [commit 665](https://github.com/EndstoneMC/endstone/commit/ff8886b01bd5b97edf3e46049e300cda7b99dd4e)

The public native UUID utility itself overlays two signed halves with bytes. Player identity copies native halves, while Python construction uses bytes. Neither the local 16-byte assertion nor the outbound stub proves canonical ordering or inbound correctness. The current binding consumers mainly expose a read-only player UUID property; no Server.get_player binding is added here to exercise the inbound route. This narrower observed usage should be retained rather than claiming all Python UUID operations fail or all work. [commit 617](https://github.com/EndstoneMC/endstone/commit/ef233a797c6249730ddbecfee1f73b4f2cbe06d2) [commit 666](https://github.com/EndstoneMC/endstone/commit/66118d80b3d363eccc16e0bc95e75564b573c0f6) [commit 717](https://github.com/EndstoneMC/endstone/commit/c3a9098b3c676ca9a0bde2c388d8cd4c612c979b)

The caster imports the UUID module/class each time and decrements several temporaries, but the constructor call creates an empty tuple inline without a matching owned reference cleanup in this source. This is a bounded ownership observation, not a runtime leak measurement. The external CPython/pybind implementation was not executed or audited as part of this unit.

## 4. Language-specific naming, not one universal spelling {#4-language-specific-naming-not-one-universal-spelling}

The broad style commit changes C++ ColorFormat constants and Permission's default constant to CamelCase, renames native command constants, and moves command-flag definitions from inline header definitions into the runtime translation unit. Numeric values remain identical. Python property names deliberately remain uppercase strings, so C++ source consumers and Python callers see different compatibility effects. A global “mechanical rename only” label would hide that distinction. [commit 697](https://github.com/EndstoneMC/endstone/commit/8399ebac127b2074591e548a6e1c092df8cae79d)

The same change tightens free-function naming in clang-tidy and then a later one-line commit reverts that constraint. Other constant naming choices remain. The available evidence supports a specific revision of lint scope, not a reason why the author changed their mind. [commit 699](https://github.com/EndstoneMC/endstone/commit/9baae63854f2be912625891517644b90648f8434)

## Tests and boundaries {#tests-and-boundaries}

Changed import/color tests verify the intended new module access at source level; no execution or CI result is claimed. Stubs and docstrings are not substitutes for lifetime, UUID round-trip, event cancellation or actual native-host tests. Existing PluginLoader.disable_plugin still binds enablePlugin in endpoint context, and Server.name still binds getVersion; these carry-forward observations prevent overstating API coherence but are not new defects attributed to the source-consolidation commit.

Per-SHA entries below cover the distinct deltas; native event timing and ECS ownership are developed in the lifecycle dossier. Exact source identities, contexts and patch hashes allow later reconciliation with PR review evidence without asserting a whole PR range is covered here.

## Per-commit dispositions {#per-commit-dispositions}

<a id="commit-644"></a>
### 644. refactor: move headers around {#commit-644}

Source: [db169eb60bad37e3b4b4c607dc8f60a6641936e5](https://github.com/EndstoneMC/endstone/commit/db169eb60bad37e3b4b4c607dc8f60a6641936e5); parent `bf9fd5c982d94020ef9e51ad7e2645b11f80ddc1`. Authored 2024-04-10T10:25:26Z. Disposition: small-semantic.

Moves public Player, ColorFormat, GameMode and concrete player headers/source toward root paths, updates includes and adds API comments. Removes redundant Player name redeclaration inherited from HumanActor. No message/UUID behavior change, but public include-path compatibility changes.

<a id="commit-645"></a>
### 645. refactor: move python bindings {#commit-645}

Source: [64792e55c7177a3a991aba458701518bb066b864](https://github.com/EndstoneMC/endstone/commit/64792e55c7177a3a991aba458701518bb066b864); parent `db169eb60bad37e3b4b4c607dc8f60a6641936e5`. Authored 2024-04-10T10:31:58Z. Disposition: mechanical.

Moves identical ColorFormat/GameMode registrations from util initializer to root initializer, expanding macro properties into explicit equivalent calls. Both already register on same extension module; Python facade moves separately646.

<a id="commit-646"></a>
### 646. refactor(python): move ColorFormat and GameMode to the root module {#commit-646}

Source: [6f5e7beecb96095c5282370f06da1e6eaa660d7b](https://github.com/EndstoneMC/endstone/commit/6f5e7beecb96095c5282370f06da1e6eaa660d7b); parent `64792e55c7177a3a991aba458701518bb066b864`. Authored 2024-04-10T10:36:27Z. Disposition: small-semantic.

Moves ColorFormat/GameMode facade exports to endstone root and updates color import test. Renames misspelled __minecraft__version__ to __minecraft_version__, leaving bootstrap consumer broken until648. No compatibility alias retained.

<a id="commit-648"></a>
### 648. fix: import statements in bootstrap module {#commit-648}

Source: [c60e145814d2e60b7479276391871893626798de](https://github.com/EndstoneMC/endstone/commit/c60e145814d2e60b7479276391871893626798de); parent `d63dcbeff6f5081b8fc2838f94c5355d1188896c`. Authored 2024-04-10T11:07:37Z. Disposition: small-semantic.

Repairs bootstrap import after646 version-attribute rename and removes unused version tuple import. Consumer repair rather than a separate version policy.

<a id="commit-649"></a>
### 649. refactor: move endstone/level/level.h to endstone/level.h {#commit-649}

Source: [0203f460a680c95573d70d22bd12bb22bc65b119](https://github.com/EndstoneMC/endstone/commit/0203f460a680c95573d70d22bd12bb22bc65b119); parent `c60e145814d2e60b7479276391871893626798de`. Authored 2024-04-10T11:18:01Z. Disposition: small-semantic.

Moves Level public/detail/source paths to root and updates all displayed includes. Public Level content exact rename; include-path compatibility changes without runtime semantic change.

<a id="commit-650"></a>
### 650. refactor: remove level, logger, server modules {#commit-650}

Source: [2fc46abf22152fb5351ce4cc6c7ee3e7a9b0ab9e](https://github.com/EndstoneMC/endstone/commit/2fc46abf22152fb5351ce4cc6c7ee3e7a9b0ab9e); parent `0203f460a680c95573d70d22bd12bb22bc65b119`. Authored 2024-04-10T11:21:58Z. Disposition: small-semantic.

Removes level/logger/server Python facade modules and exports types at root; import tests switch paths. Deliberate surface simplification has breaking import consequences; plugin-loader consumer follows651.

<a id="commit-651"></a>
### 651. fix: import in plugin_loader.py {#commit-651}

Source: [e293e49a10029f229b7cdd8c94d4f2c59c3ee72a](https://github.com/EndstoneMC/endstone/commit/e293e49a10029f229b7cdd8c94d4f2c59c3ee72a); parent `2fc46abf22152fb5351ce4cc6c7ee3e7a9b0ab9e`. Authored 2024-04-10T11:24:15Z. Disposition: small-semantic.

Updates plugin-loader Server import to root after650 module removal.

<a id="commit-652"></a>
### 652. refactor: simplify pybind11 python bindings {#commit-652}

Source: [9743cdccf357fa021c8ba2e4d18a41b6c74564d7](https://github.com/EndstoneMC/endstone/commit/9743cdccf357fa021c8ba2e4d18a41b6c74564d7); parent `e293e49a10029f229b7cdd8c94d4f2c59c3ee72a`. Authored 2024-04-10T11:47:50Z. Disposition: mechanical.

Consolidates Level/Logger/Server binding bodies into main extension file and splits color/game initializers. Existing return policies and Server.name mistakenly bound to getVersion survive unchanged; source consolidation is not evidence of a behavioral repair.

<a id="commit-665"></a>
### 665. feat(python): add type_caster for cast between endstone::UUID and uuid.UUID {#commit-665}

Source: [ff8886b01bd5b97edf3e46049e300cda7b99dd4e](https://github.com/EndstoneMC/endstone/commit/ff8886b01bd5b97edf3e46049e300cda7b99dd4e); parent `f313a5bbbf4dacc61f1eef9109b3699aeb71aa6c`. Authored 2024-04-11T16:39:34Z. Disposition: meaningful.

Introduces manual Python UUID caster over16 raw bytes. C++→Python constructs uuid.UUID(bytes=...); inbound calls bytes as method and returns PyErr_Occurred()!=nullptr, inverted relative to success, with unchecked intermediate C-API results. Explicit counterexample to assuming bidirectional conversion works; no round-trip tests accompany it. Header lacks an include guard in this change.

<a id="commit-666"></a>
### 666. feat(python): add basic bindings for Player, HumanActor and Actor {#commit-666}

Source: [66118d80b3d363eccc16e0bc95e75564b573c0f6](https://github.com/EndstoneMC/endstone/commit/66118d80b3d363eccc16e0bc95e75564b573c0f6); parent `ff8886b01bd5b97edf3e46049e300cda7b99dd4e`. Authored 2024-04-11T16:39:52Z. Disposition: meaningful.

Binds Actor→HumanActor→Player hierarchy and UUID/message access; generated stub records actual Python signatures. Popup/tip descriptions incorrectly repeat raw-message text. No new Python facade Player export here and no inbound UUID caller proves665 functional.

<a id="commit-667"></a>
### 667. feat(python): add PlayerJoinEvent and PlayerQuitEvent bindings {#commit-667}

Source: [5e8bcaaab195abd661f38fce655ca1e8ffc50551](https://github.com/EndstoneMC/endstone/commit/5e8bcaaab195abd661f38fce655ca1e8ffc50551); parent `66118d80b3d363eccc16e0bc95e75564b573c0f6`. Authored 2024-04-11T16:44:59Z. Disposition: meaningful.

Adds join/quit event bindings and explicitly reference-borrows player/plugin/level properties. Reference policy avoids ownership transfer but does not extend native wrapper lifetime after quit erase. Stub updated; the weather getter spelling uses WeatherChangeEvent::getLevel, but context confirms this is inherited from common WeatherEvent, so that spelling alone is not a demonstrated mismatch.

<a id="commit-668"></a>
### 668. feat(python): add endstone.actor module, add PlayerJoinEvent and PlayerQuitEvent to endstone.event module {#commit-668}

Source: [155b58615e1f3ffba3ef3285889e68b0bf07f656](https://github.com/EndstoneMC/endstone/commit/155b58615e1f3ffba3ef3285889e68b0bf07f656); parent `5e8bcaaab195abd661f38fce655ca1e8ffc50551`. Authored 2024-04-11T16:48:01Z. Disposition: small-semantic.

Adds endstone.actor facade for Actor/HumanActor and exports join/quit through event module. Internal Player class exists but this patch does not add root Player facade.

<a id="commit-697"></a>
### 697. style: update .clang-tidy and rename variables {#commit-697}

Source: [8399ebac127b2074591e548a6e1c092df8cae79d](https://github.com/EndstoneMC/endstone/commit/8399ebac127b2074591e548a6e1c092df8cae79d); parent `8bbe06ca3232706ae48e8ed54e4e47de6e446bcd`. Authored 2024-04-18T11:55:11Z. Disposition: meaningful.

Renames C++ constants to CamelCase and moves command-flag definitions from inline header to runtime magic.cpp, preserving values and Python uppercase names. Public C++ ColorFormat/Permission spellings break while Python facade remains stable. Dimension constants move to VanillaDimensions; removes unused parser declaration. Lint function-case rule temporarily tightened then699 reverts. Not pure formatting: linkage and source API change.

<a id="commit-699"></a>
### 699. style: update .clang-tidy {#commit-699}

Source: [9baae63854f2be912625891517644b90648f8434](https://github.com/EndstoneMC/endstone/commit/9baae63854f2be912625891517644b90648f8434); parent `0845b9f06f8972a71eeb91cbcb411167d948e02f`. Authored 2024-04-18T13:21:01Z. Disposition: mechanical.

Reverts free-function naming rule lower_case→aNy_CasE from697; other constant naming choices stay. No runtime change.
