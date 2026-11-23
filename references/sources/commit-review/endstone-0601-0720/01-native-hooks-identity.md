<!-- retrieval: {"source_ids":["public:commit:01c0e013e5a4a01307da2ecf6b2eeefa1cf3eccf","public:commit:0845b9f06f8972a71eeb91cbcb411167d948e02f","public:commit:13cae071330a65124a21a0c7e920ae1d7dd7f5b1","public:commit:1b18b69c9da33bbc8b7058c1cb36b24ab9ab29e0","public:commit:1bed4b57a16221028b88d1dac19559e91c3f9393","public:commit:233922fb2bd46092d2fbceacbfbcf85341681bff","public:commit:282ad2467c4889be62beaf2741d7293a9300bc50","public:commit:32583cf734e46750d9ee0cceac69ba0095102b77","public:commit:34a9560f02de165cdbf3c9dcf99a0c84c854820d","public:commit:39d54adc6fcde95d55c890cff47f162bc753550f","public:commit:3a3c1d71a6a0d20b962ce3033d099b30ad06a72f","public:commit:3e1d05c68ebddeabaea484a66b811429d654019f","public:commit:3fcc871e2bc4de5ac73dbc2d4b24e8d1d6f2d418","public:commit:531b94a7b86b4d83d6af516b41baf89ace9dc9ad","public:commit:647e96a2272a64c4b1d9eb70625b01da654d41b6","public:commit:683cddc5137636a84d42076944b9a10bdb010c7d","public:commit:70688b1cb6a88557607b217ad017a2156328201d","public:commit:76018a8718dc968af860af531f2b41c6c0c052e7","public:commit:76f7cd0ca43cdb6b121adfbe7e4837fa9d7b6804","public:commit:97863e452b3c10656ba07d9dca0cf519658ee749","public:commit:9f131591fa1b062c88872bf054f10be9496f03f1","public:commit:a20c7d8c5ce788743d091030f4b98e93f1f9d8c6","public:commit:b884cda45e354f99024a9eb79d5613d93fc8b536","public:commit:bc550407258cd9d1905e852e6e93d6615e9c04cc","public:commit:c2da2ab785d101cf4f155f4483a4168b64b257da","public:commit:c8de424ab692e1dfb7c31cbeaf727eed6be16013","public:commit:ccd3201e883cfa2b3d8e71eaaaafd451e905fd63","public:commit:da999e5a4aa24599f2f8d57ae19ed234f50ecf0a","public:commit:ddd59165782e6e24d3de5f03e7c1d83c3d7b3659","public:commit:e677412825b7c3e5d0baadf3616aa7a282ef54d5","public:commit:ea94c5d3efdec0bf090d6a060aaa27a13e179277","public:commit:ef233a797c6249730ddbecfee1f73b4f2cbe06d2","public:commit:f3af07cf47f1aa5f2629ba1635620349ec573b68","public:commit:f4e8f2d789024d6e360692b039ce1172efc907bf"],"source_type":"public","date":"2024-04-08..2024-04-18","topics":["lifetime","concurrency","ffi","testing","build","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native integration: abandoning vtable hooks, exposing ECS identity {#native-integration-abandoning-vtable-hooks-exposing-ecs-identity}

## Result and scope {#result-and-scope}

The most explicit design judgment in this unit is a reversal: the vtable-hook experiment is abandoned for cross-platform maintainability. The project then invests in native ECS/type/layout mirrors, named function hooks, packet factories and host-derived identity. This is not evidence that ABI risk disappears. The replacement weather hook still needs a receiver-adjustment workaround, and the ECS integration depends on matching EnTT configuration and native component/type layout. The useful engineering lesson is local and dated: the author accepted a different compatibility burden after encountering maintainability costs in the first approach. [commit 606](https://github.com/EndstoneMC/endstone/commit/1bed4b57a16221028b88d1dac19559e91c3f9393) [commit 607](https://github.com/EndstoneMC/endstone/commit/ccd3201e883cfa2b3d8e71eaaaafd451e905fd63) [commit 619](https://github.com/EndstoneMC/endstone/commit/683cddc5137636a84d42076944b9a10bdb010c7d)

The linked commits form a first-parent chain. Vincent is the recorded author for this work. The UUID header explicitly credits an adaptation from Boost UUID; that upstream implementation was not independently examined. [Commit 610](https://github.com/EndstoneMC/endstone/commit/bc550407258cd9d1905e852e6e93d6615e9c04cc)

## 1. Vtable experiment → named hooks, with an unresolved receiver model {#1-vtable-experiment-named-hooks-with-an-unresolved-receiver-model}

The immediately preceding unit ended after several iterations of table-size/prefix arithmetic, detour bookkeeping and enable/disable behavior. Its endpoint was not a settled long-term preference. After whitespace and direct-include repairs, the explicit message in 606 rejects vtable hooks on cross-platform maintenance grounds. Per-level table installation disappears, coordinator `sendEvent` interception returns, and weather goes back to a named `ScriptLevelGameplayHandler::handleEvent` hook. The generic table helper remains in the tree, but remaining includes do not establish active use. [commit 601](https://github.com/EndstoneMC/endstone/commit/647e96a2272a64c4b1d9eb70625b01da654d41b6) [commit 602](https://github.com/EndstoneMC/endstone/commit/e677412825b7c3e5d0baadf3616aa7a282ef54d5) [commit 603](https://github.com/EndstoneMC/endstone/commit/ea94c5d3efdec0bf090d6a060aaa27a13e179277) [commit 606](https://github.com/EndstoneMC/endstone/commit/1bed4b57a16221028b88d1dac19559e91c3f9393)

This also changes event semantics. The prior original-first weather path, which suppressed plugin callbacks on native Deny, gives way to plugin callbacks first: compare old/new rain and lightning flags, dispatch their cancellable events, restore each previous flag if cancelled, then call native original. The returned native result still flows back to the caller. The explicit maintainability explanation covers the architecture reversal; it does not separately explain why the event order changed. Treat that order as observed behavior, not a documented philosophy about plugin priority. [commit 565](https://github.com/EndstoneMC/endstone/commit/f14cf337a40817583e793edd43910cbd0a5864d6) [commit 606](https://github.com/EndstoneMC/endstone/commit/1bed4b57a16221028b88d1dac19559e91c3f9393)

The next fix adds a virtual destructor to the modeled script handler and uses `this - 1` when finding the enclosing level handler. Its comment explicitly calls this hacky and asks for a better multiple-inheritance workaround. The local modeled class now has a vptr, so the subtraction is tied to its size and assumed host subobject arrangement. The method searches registered wrappers for a matching native gameplay-handler address. Neither the subtraction nor the existing pointer-slot lookup proves general ABI portability. [commit 607](https://github.com/EndstoneMC/endstone/commit/ccd3201e883cfa2b3d8e71eaaaafd451e905fd63)

A later interaction matters: after one native level gets three dimension-specific Endstone wrappers, all three wrappers still refer to the same native level/coordinator. The endpoint weather search returns the first matching wrapper from the server's unordered-map-derived list. Thus the dimensional redesign does not by itself establish an unambiguous weather-event dimension. This is a bounded integration consequence visible in the read endpoint contexts, not a claim of a reproduced host bug or an intentional choice. [commit 696](https://github.com/EndstoneMC/endstone/commit/8bbe06ca3232706ae48e8ed54e4e47de6e446bcd)

The restored actor/block/player/level coordinators mostly visit variants with empty lambdas and then forward. Commented diagnostic branches are not implemented public events. Join/quit and actor spawn/removal later use more specific lifecycle hooks. This distinction avoids converting scaffolding volume into a claim of event coverage. [commit 607](https://github.com/EndstoneMC/endstone/commit/ccd3201e883cfa2b3d8e71eaaaafd451e905fd63) [commit 625](https://github.com/EndstoneMC/endstone/commit/6be7069c2c3a8375f1531b0c81d38db4d11d6c51) [commit 672](https://github.com/EndstoneMC/endstone/commit/23c6a56c43afaac621d52342f060c859a8fc10b4) [commit 687](https://github.com/EndstoneMC/endstone/commit/de5ee93545b7cc240cdc9233a4deab0b09aa605c) [commit 719](https://github.com/EndstoneMC/endstone/commit/bb666a70a4508fdfa6d62024aba51a1e49457b6e)

## 2. Identity crosses several domains {#2-identity-crosses-several-domains}

UUID begins as a 16-byte utility with ordering, hashing, nil/version inspection and later equality, a two-half overlay, formatting and a zero-initializing default. `sizeof == 16` is a useful local invariant. It does not prove that the two native 64-bit halves have the same canonical byte order as an external textual UUID on every host. Formatting walks the raw byte array; lookup reconstructs native halves from that overlay. Those are different operations whose correspondence needs evidence beyond width. No round-trip test is added in this range. [commit 610](https://github.com/EndstoneMC/endstone/commit/bc550407258cd9d1905e852e6e93d6615e9c04cc) [commit 612](https://github.com/EndstoneMC/endstone/commit/5cab8984dc8331eb3c6b76f17cead77c569df14a) [commit 613](https://github.com/EndstoneMC/endstone/commit/f5dda3a275e47fef9df6c5abd37bf7ce2f7dca25) [commit 617](https://github.com/EndstoneMC/endstone/commit/ef233a797c6249730ddbecfee1f73b4f2cbe06d2) [commit 624](https://github.com/EndstoneMC/endstone/commit/a20c7d8c5ce788743d091030f4b98e93f1f9d8c6)

The command execution sequence gives a concrete identity-domain counterexample. A player command first looks up its wrapper with `CommandOrigin::getUUID`, then the next commit explicitly fixes command failure by using the origin entity's user-identity component UUID. A UUID-shaped value from the wrong subsystem was not interchangeable with player identity. A subsequent helper centralizes the mapping and checks that a player-origin entity is actually a player; entity and identity-component validity still remain assumptions at several sites. [commit 637](https://github.com/EndstoneMC/endstone/commit/51976a722a4a2a383c88c98b5819ad5c15aa40c6) [commit 638](https://github.com/EndstoneMC/endstone/commit/ee85cebd6ff028cfb8d54997ca4b61735a2a1288) [commit 647](https://github.com/EndstoneMC/endstone/commit/d63dcbeff6f5081b8fc2838f94c5355d1188896c)

Native actor IDs are kept distinct from player UUIDs. Runtime IDs are initially signed, become unsigned in the public API/map, and then become unsigned/default-zero in the native mirror; unique IDs default to -1. The component accessor dereferences the runtime-ID component directly. These revisions reveal type alignment in progress, not evidence that all native entities always satisfy the accessor precondition. [commit 676](https://github.com/EndstoneMC/endstone/commit/c0b8a343abe8628ea291fc558d8a94b9fb92bbf5) [commit 677](https://github.com/EndstoneMC/endstone/commit/c3e4f15c23e1c2834ee2bc3f62ffb3b08b5c27d8) [commit 678](https://github.com/EndstoneMC/endstone/commit/583cf0cbf23a4d74fe571f786a777d44d6e5b495) [commit 681](https://github.com/EndstoneMC/endstone/commit/c0b7e205119114dcc6c961f2a5ab414d91953819) [commit 682](https://github.com/EndstoneMC/endstone/commit/131c83baba7e100447c6974739a561142b4218b8)

## 3. ECS mirror and ownership implications {#3-ecs-mirror-and-ownership-implications}

`EntityContext` carries references to a mirrored registry and its EnTT registry plus an entity ID. `tryGetComponent` delegates into that registry. EnTT becomes a public-header dependency rather than only a core dependency because native declarations expose it. The configuration is then made explicit: sparse page size 2048, packed page size 128, and custom 18-bit entity/14-bit version traits. The static assertion checks the local selected page size, not the foreign process's registry implementation. The redundant masks removed in 621 were not the specialized trait values used by EnTT. [commit 614](https://github.com/EndstoneMC/endstone/commit/01c0e013e5a4a01307da2ecf6b2eeefa1cf3eccf) [commit 615](https://github.com/EndstoneMC/endstone/commit/34a9560f02de165cdbf3c9dcf99a0c84c854820d) [commit 619](https://github.com/EndstoneMC/endstone/commit/683cddc5137636a84d42076944b9a10bdb010c7d) [commit 621](https://github.com/EndstoneMC/endstone/commit/f4e8f2d789024d6e360692b039ce1172efc907bf)

This groundwork enables `getOrAddComponent`, which mutates the referenced registry even through a const context accessor. The later actor/player wrapper redesign deliberately relies on it for lazy, entity-bound identity. Public wrapper copy/move operations are deleted during the migration. That is a stronger local identity constraint than the earlier independent wrapper maps, but it still does not prove safe retention after the host destroys an entity. The external EnTT implementation and destruction ordering are outside this unit's reads. [commit 704](https://github.com/EndstoneMC/endstone/commit/da999e5a4aa24599f2f8d57ae19ed234f50ecf0a) [commit 705](https://github.com/EndstoneMC/endstone/commit/30d6fc343ac75403684d66ceeddf583c04ecbd86) [commit 712](https://github.com/EndstoneMC/endstone/commit/3fd9a44c269542ba91bcf7b7eb4fc11b6c566283)

The memory wrappers should be interpreted narrowly. `WeakRef` locks locally and returns a reference or raw pointer after the temporary lock is gone; it does not hand the caller a retained shared owner. `OwnerPtr<EntityContext>` later becomes noncopyable and move-constructible, with assignment deleted. Its stored context and generated move operations are only the modeled transfer surface, not a demonstrated general-purpose ownership implementation. The actor insertion hook switches to `std::move` and is replaced by another lifecycle hook the next day. [commit 695](https://github.com/EndstoneMC/endstone/commit/39d54adc6fcde95d55c890cff47f162bc753550f) [commit 718](https://github.com/EndstoneMC/endstone/commit/9f131591fa1b062c88872bf054f10be9496f03f1) [commit 719](https://github.com/EndstoneMC/endstone/commit/bb666a70a4508fdfa6d62024aba51a1e49457b6e)

## 4. Native packets and semantic names {#4-native-packets-and-semantic-names}

Packet scaffolding moves common opaque base fields out of `AvailableCommandsPacket` into `Packet`, then models text-packet fields. Actual player messaging uses the native factory to obtain a packet and fills the text type/message before native send. This avoids pretending the incomplete local abstract native class can be safely constructed as a real host packet. The initial `sendMessage` uses SystemMessage; the raw/popup/tip extension changes its delegation to Raw. That behavioral switch is preserved rather than calling the whole change additive. [commit 634](https://github.com/EndstoneMC/endstone/commit/c2da2ab785d101cf4f155f4483a4168b64b257da) [commit 635](https://github.com/EndstoneMC/endstone/commit/3fcc871e2bc4de5ac73dbc2d4b24e8d1d6f2d418) [commit 636](https://github.com/EndstoneMC/endstone/commit/a2f0280fb26aeb54c8c80e06c586eb7d907edc40) [commit 639](https://github.com/EndstoneMC/endstone/commit/6b02d5666674e3e716b0669cf064567ab1f025f3) [commit 641](https://github.com/EndstoneMC/endstone/commit/63da543e1ccfc7163b43a408335a04718d75e9a6)

Native Boolean command parsing similarly reuses an existing host enum symbol rather than creating a standalone boolean parser. Actor naming and dimension naming delegate to native helpers with explicit string-return forwarding. These choices keep game semantics in the host, while increasing dependence on precise symbols and return conventions. No network or native integration test is present in the relevant patches. [commit 642](https://github.com/EndstoneMC/endstone/commit/3a3c1d71a6a0d20b962ce3033d099b30ad06a72f) [commit 643](https://github.com/EndstoneMC/endstone/commit/bf9fd5c982d94020ef9e51ad7e2645b11f80ddc1) [commit 703](https://github.com/EndstoneMC/endstone/commit/d409f286032043ae53e6e079995444191e5fa34a)

## 5. What to retain, and what not to infer {#5-what-to-retain-and-what-not-to-infer}

Retain the documented rejection of vtable maintenance cost, the explicit receiver-layout uncertainty, the staged alignment of registry configuration, and the distinction between command-origin identity and player identity. Do not generalize them into “all direct-layout integration is preferred,” “all events are supported,” or “matching local sizeof proves compatibility.” The broad file moves and constant renames are separately covered per SHA; they are evidence of organization and API spelling changes, not independent architectural breakthroughs.

The public commit history documents weather handling, registry identity, UUID/caster and actor lifecycle changes. This is a static historical account, not verification of current upstream behavior or a runtime ABI guarantee.

## Per-commit dispositions {#per-commit-dispositions}

<a id="commit-601"></a>
### 601. style: code formatting {#commit-601}

Source: [647e96a2272a64c4b1d9eb70625b01da654d41b6](https://github.com/EndstoneMC/endstone/commit/647e96a2272a64c4b1d9eb70625b01da654d41b6); parent `3297d0e9177f4bd4e108931d21c3ad12e83fa67e`. Authored 2024-04-08T11:03:42Z. Disposition: mechanical.

Whitespace/template wrapping only across level, vtable and magic constants; actual values and control flow unchanged.

<a id="commit-602"></a>
### 602. fix: add missing include in virtual_table.h {#commit-602}

Source: [e677412825b7c3e5d0baadf3616aa7a282ef54d5](https://github.com/EndstoneMC/endstone/commit/e677412825b7c3e5d0baadf3616aa7a282ef54d5); parent `647e96a2272a64c4b1d9eb70625b01da654d41b6`. Authored 2024-04-08T11:07:58Z. Disposition: small-semantic.

Adds direct endstone macro header dependency to virtual_table.h. Repairs reliance on transitive includes; no table arithmetic change.

<a id="commit-603"></a>
### 603. fix: add missing 'entt/entt.hpp' include in 'virtual_table.h' {#commit-603}

Source: [ea94c5d3efdec0bf090d6a060aaa27a13e179277](https://github.com/EndstoneMC/endstone/commit/ea94c5d3efdec0bf090d6a060aaa27a13e179277); parent `e677412825b7c3e5d0baadf3616aa7a282ef54d5`. Authored 2024-04-08T12:15:44Z. Disposition: small-semantic.

Adds direct EnTT include to virtual_table.h, repairing another transitive dependency exposed by the previous refactor.

<a id="commit-606"></a>
### 606. refactor: revert back to old event hooks due to the maintainability of vmt hooks across different platforms {#commit-606}

Source: [1bed4b57a16221028b88d1dac19559e91c3f9393](https://github.com/EndstoneMC/endstone/commit/1bed4b57a16221028b88d1dac19559e91c3f9393); parent `eae6c6bdb2aab339969dab4e4abbb63d81cb528b`. Authored 2024-04-08T13:36:04Z. Disposition: meaningful.

Explicitly abandons vtable hooks because of cross-platform maintainability. Restores actor/block/player/level coordinator sendEvent interception with TODO visitors, removes per-level installation and table-size specialization, returns weather to named function hook. Also reverses original-first behavior from565: Endstone events now mutate native weather booleans before original; native Deny no longer gates callbacks. Removes leave/actor-added vtable diagnostics. VirtualTable header remains unused rather than being erased. This is a documented design reversal, not a lasting preference inferred from prior endpoint.

<a id="commit-607"></a>
### 607. fix: unable to get level from ScriptLevelGameplayHandler::handleEvent {#commit-607}

Source: [ccd3201e883cfa2b3d8e71eaaaafd451e905fd63](https://github.com/EndstoneMC/endstone/commit/ccd3201e883cfa2b3d8e71eaaaafd451e905fd63); parent `1bed4b57a16221028b88d1dac19559e91c3f9393`. Authored 2024-04-08T14:36:09Z. Disposition: meaningful.

Reported inability to map weather receiver to level leads to pure virtual destructor in ScriptLevelGameplayHandler and getLevel(this-1) workaround, explicitly marked hacky for multiple inheritance. Pointer arithmetic depends on the modeled class size and native subobject layout; no generalized ABI guarantee. Replaces TODO visitors with entt::overloaded and player-specific empty branches, still no public events. Removes unused HandlerResult/player-handler declarations.

<a id="commit-610"></a>
### 610. feat: add endstone::UUID {#commit-610}

Source: [bc550407258cd9d1905e852e6e93d6615e9c04cc](https://github.com/EndstoneMC/endstone/commit/bc550407258cd9d1905e852e6e93d6615e9c04cc); parent `309bb3cbcd60624078327be8f5e4e7afb0ecd75e`. Authored 2024-04-08T15:51:47Z. Disposition: meaningful.

Adds 16-byte UUID utility explicitly adapted from Boost UUID, with byte iteration, ordering, version1–5 detection and hash combiner. Credit belongs separately to cited Boost source; external implementation not independently read. No constructor/equality or parsing yet; raw data initially uninitialized on default construction. Do not attribute standard UUID design to this adapter author.

<a id="commit-614"></a>
### 614. feat: add headers of EntityContext and EntityRegistry {#commit-614}

Source: [01c0e013e5a4a01307da2ecf6b2eeefa1cf3eccf](https://github.com/EndstoneMC/endstone/commit/01c0e013e5a4a01307da2ecf6b2eeefa1cf3eccf); parent `f5dda3a275e47fef9df6c5abd37bf7ce2f7dca25`. Authored 2024-04-08T18:13:19Z. Disposition: small-semantic.

Defines EntityContext and EntityRegistry mirrors with EnTT registry reference/entity ID and storage specialization. Native object offsets are comments, not host-verified runtime layout. Enables later ECS component lookup, initially no methods beyond construction.

<a id="commit-615"></a>
### 615. feat: add tryGetComponent to Actor and EntityContext class {#commit-615}

Source: [34a9560f02de165cdbf3c9dcf99a0c84c854820d](https://github.com/EndstoneMC/endstone/commit/34a9560f02de165cdbf3c9dcf99a0c84c854820d); parent `01c0e013e5a4a01307da2ecf6b2eeefa1cf3eccf`. Authored 2024-04-08T22:05:51Z. Disposition: meaningful.

Adds Actor/EntityContext tryGetComponent forwarding into mirrored EnTT registry, and concrete Actor context/name fields. Moves EnTT dependency from core to public header target in CMake and Conan because exposed headers now use it. Correct registry layout, component type identity and library configuration become native compatibility requirements.

<a id="commit-616"></a>
### 616. feat: add UserEntityIdentifierComponent {#commit-616}

Source: [b884cda45e354f99024a9eb79d5613d93fc8b536](https://github.com/EndstoneMC/endstone/commit/b884cda45e354f99024a9eb79d5613d93fc8b536); parent `34a9560f02de165cdbf3c9dcf99a0c84c854820d`. Authored 2024-04-08T22:20:19Z. Disposition: small-semantic.

Defines user-identity component with network/subclient/UUID/platform/certificate fields, opaque160-byte NetworkIdentifier and empty Certificate. Login hook reads component but does not yet use it; these are ABI declarations, not authentication verification or handling of captured private data.

<a id="commit-617"></a>
### 617. feat: add str() method for endstone::UUID {#commit-617}

Source: [ef233a797c6249730ddbecfee1f73b4f2cbe06d2](https://github.com/EndstoneMC/endstone/commit/ef233a797c6249730ddbecfee1f73b4f2cbe06d2); parent `b884cda45e354f99024a9eb79d5613d93fc8b536`. Authored 2024-04-09T00:07:06Z. Disposition: meaningful.

Adds UUID construction by signed64-bit halves and hexadecimal/hyphen string formatting over raw byte order; native mce halves become signed. Memory-order formatting is not proven canonical across endianness, and no round-trip tests appear. Later Python UUID conversion needs to account for host halves separately.

<a id="commit-618"></a>
### 618. style: rename member variables {#commit-618}

Source: [282ad2467c4889be62beaf2741d7293a9300bc50](https://github.com/EndstoneMC/endstone/commit/282ad2467c4889be62beaf2741d7293a9300bc50); parent `ef233a797c6249730ddbecfee1f73b4f2cbe06d2`. Authored 2024-04-09T00:12:11Z. Disposition: mechanical.

Renames native Actor context field consistently and aligns comments. No offset, lookup or behavior change.

<a id="commit-619"></a>
### 619. feat: update entt config to align with Minecraft's {#commit-619}

Source: [683cddc5137636a84d42076944b9a10bdb010c7d](https://github.com/EndstoneMC/endstone/commit/683cddc5137636a84d42076944b9a10bdb010c7d); parent `282ad2467c4889be62beaf2741d7293a9300bc50`. Authored 2024-04-09T11:54:27Z. Disposition: meaningful.

Explicitly aligns EnTT configuration with game: sparse pages2048, packed pages128, custom EntityId/traits with18-bit entity and14-bit version masks. Local page-size assertion checks configuration, not foreign registry ABI. EntityId also redundantly carries11-bit version mask until621; specialized traits select a distinct14-bit value. No runtime registry interoperability test included.

<a id="commit-620"></a>
### 620. style: code clean up {#commit-620}

Source: [531b94a7b86b4d83d6af516b41baf89ace9dc9ad](https://github.com/EndstoneMC/endstone/commit/531b94a7b86b4d83d6af516b41baf89ace9dc9ad); parent `683cddc5137636a84d42076944b9a10bdb010c7d`. Authored 2024-04-09T11:54:41Z. Disposition: mechanical.

Exact component-header rename plus include/forward-declaration updates. Native component content unchanged; no new identity behavior.

<a id="commit-621"></a>
### 621. refactor: remove unnecessary constants (oops) {#commit-621}

Source: [f4e8f2d789024d6e360692b039ce1172efc907bf](https://github.com/EndstoneMC/endstone/commit/f4e8f2d789024d6e360692b039ce1172efc907bf); parent `531b94a7b86b4d83d6af516b41baf89ace9dc9ad`. Authored 2024-04-09T11:56:01Z. Disposition: small-semantic.

Removes redundant masks from EntityId, retaining specialized EntityTraits masks used by EnTT. Does not change the actual traits values.

<a id="commit-622"></a>
### 622. fix: add zero-length check for ping data {#commit-622}

Source: [32583cf734e46750d9ee0cceac69ba0095102b77](https://github.com/EndstoneMC/endstone/commit/32583cf734e46750d9ee0cceac69ba0095102b77); parent `f4e8f2d789024d6e360692b039ce1172efc907bf`. Authored 2024-04-09T12:38:23Z. Disposition: small-semantic.

Empty ping payload length now forwards original before event creation. Length bytes and first packet byte are still read before this guard, so it is not a general packet-bound validation fix.

<a id="commit-624"></a>
### 624. style: code clean up {#commit-624}

Source: [a20c7d8c5ce788743d091030f4b98e93f1f9d8c6](https://github.com/EndstoneMC/endstone/commit/a20c7d8c5ce788743d091030f4b98e93f1f9d8c6); parent `ce531876be166ed7473a7574650ff33964caf783`. Authored 2024-04-09T13:26:57Z. Disposition: small-semantic.

Adds zero-initializing UUID default constructor and removes explicit player UUID{0,0} initializer; surrounding include/spacing changes are mechanical. General default construction now has defined nil bytes, so style title understates semantic effect.

<a id="commit-632"></a>
### 632. feat: add PlayerPermissionLevel enum {#commit-632}

Source: [13cae071330a65124a21a0c7e920ae1d7dd7f5b1](https://github.com/EndstoneMC/endstone/commit/13cae071330a65124a21a0c7e920ae1d7dd7f5b1); parent `aa5e6e0ba918047c8ca2f9f9ebbc10493672b52c`. Authored 2024-04-09T16:06:02Z. Disposition: small-semantic.

Defines native PlayerPermissionLevel values Visitor, Member, Operator, Custom; no behavioral use yet.

<a id="commit-634"></a>
### 634. feat: add TextPacket {#commit-634}

Source: [c2da2ab785d101cf4f155f4483a4168b64b257da](https://github.com/EndstoneMC/endstone/commit/c2da2ab785d101cf4f155f4483a4168b64b257da); parent `0e2a2006c5ff0ff3668bb34fc641ee332d6d7b43`. Authored 2024-04-09T16:29:36Z. Disposition: small-semantic.

Adds TextPacket type enum and tentative field layout; size assertion remains commented. This is packet ABI scaffolding, not successful transmission.

<a id="commit-635"></a>
### 635. refactor: update structure of Packet {#commit-635}

Source: [3fcc871e2bc4de5ac73dbc2d4b24e8d1d6f2d418](https://github.com/EndstoneMC/endstone/commit/3fcc871e2bc4de5ac73dbc2d4b24e8d1d6f2d418); parent `c2da2ab785d101cf4f155f4483a4168b64b257da`. Authored 2024-04-09T16:29:50Z. Disposition: meaningful.

Moves common opaque fields from AvailableCommandsPacket into Packet base with active48-byte assertion, enabling shared derived-packet offsets. Local compile assertion is not proof of matching all native packet versions.

<a id="commit-642"></a>
### 642. feat: improve support for boolean command parameters {#commit-642}

Source: [3a3c1d71a6a0d20b962ce3033d099b30ad06a72f](https://github.com/EndstoneMC/endstone/commit/3a3c1d71a6a0d20b962ce3033d099b30ad06a72f); parent `63da543e1ccfc7163b43a408335a04718d75e9a6`. Authored 2024-04-10T08:50:55Z. Disposition: meaningful.

Command parameter bool now uses native Boolean enum symbol with Enum data type; debug command usage becomes <toggle: bool>. Empty addEnumValues payload relies on existing native Boolean values rather than defining true/false itself. Static symbol still assumes registry-lifetime compatibility.

<a id="commit-688"></a>
### 688. refactor: move bedrock header files {#commit-688}

Source: [f3af07cf47f1aa5f2629ba1635620349ec573b68](https://github.com/EndstoneMC/endstone/commit/f3af07cf47f1aa5f2629ba1635620349ec573b68); parent `de5ee93545b7cc240cdc9233a4deab0b09aa605c`. Authored 2024-04-15T22:06:00Z. Disposition: mechanical.

Reorganizes native headers into world/actor, world/level, server and protocol/raknet directories, splits runtime-ID component into its own file, updates includes and removes unused ones. No runtime algorithm change; exact renamed blobs recorded. Initial combined display truncated within688, fully reread separately.

<a id="commit-689"></a>
### 689. refactor: move OwnerPtr, NonOwnerPointer and EnableNonOwnerReferences to bedrock/memory.h {#commit-689}

Source: [233922fb2bd46092d2fbceacbfbcf85341681bff](https://github.com/EndstoneMC/endstone/commit/233922fb2bd46092d2fbceacbfbcf85341681bff); parent `f3af07cf47f1aa5f2629ba1635620349ec573b68`. Authored 2024-04-16T12:43:26Z. Disposition: mechanical.

Moves ownership/reference declarations into memory.h and EntityContext specialization into registry header. Class fields/ownership operations unchanged; dependency placement changes, with direct memory include added later719.

<a id="commit-690"></a>
### 690. refactor: move ActorManager and Player {#commit-690}

Source: [97863e452b3c10656ba07d9dca0cf519658ee749](https://github.com/EndstoneMC/endstone/commit/97863e452b3c10656ba07d9dca0cf519658ee749); parent `233922fb2bd46092d2fbceacbfbcf85341681bff`. Authored 2024-04-16T12:44:56Z. Disposition: mechanical.

Exact100% source renames for Player and ActorManager, no hunk changes.

<a id="commit-691"></a>
### 691. refactor: move classes {#commit-691}

Source: [76f7cd0ca43cdb6b121adfbe7e4837fa9d7b6804](https://github.com/EndstoneMC/endstone/commit/76f7cd0ca43cdb6b121adfbe7e4837fa9d7b6804); parent `97863e452b3c10656ba07d9dca0cf519658ee749`. Authored 2024-04-16T12:48:25Z. Disposition: mechanical.

Five exact100% source relocations for packets/RakNet/server player/network handler.

<a id="commit-692"></a>
### 692. feat: move event-related classes {#commit-692}

Source: [1b18b69c9da33bbc8b7058c1cb36b24ab9ab29e0](https://github.com/EndstoneMC/endstone/commit/1b18b69c9da33bbc8b7058c1cb36b24ab9ab29e0); parent `76f7cd0ca43cdb6b121adfbe7e4837fa9d7b6804`. Authored 2024-04-17T09:51:34Z. Disposition: mechanical.

Moves native event headers/sources under world/level/event, updates includes and placeholder template parameter case, removes unused magic.cpp includes. No variant alternatives or event dispatch behavior changes.

<a id="commit-693"></a>
### 693. feat: add Actor::getPosition {#commit-693}

Source: [70688b1cb6a88557607b217ad017a2156328201d](https://github.com/EndstoneMC/endstone/commit/70688b1cb6a88557607b217ad017a2156328201d); parent `1b18b69c9da33bbc8b7058c1cb36b24ab9ab29e0`. Authored 2024-04-17T10:29:27Z. Disposition: small-semantic.

Adds native Vec3 and borrowed Actor position getter at modeled offset664, after56-byte padding. No public position API or runtime offset verification in this commit.

<a id="commit-694"></a>
### 694. feat: add headers for Dimension and AutomaticID {#commit-694}

Source: [76018a8718dc968af860af531f2b41c6c0c052e7](https://github.com/EndstoneMC/endstone/commit/76018a8718dc968af860af531f2b41c6c0c052e7); parent `70688b1cb6a88557607b217ad017a2156328201d`. Authored 2024-04-17T23:40:13Z. Disposition: small-semantic.

Adds AutomaticID definition, empty native Dimension scaffold and public three-value Dimension enum; extracts runtime/unique ID classes into headers without value changes. Dimension behavior arrives696.

<a id="commit-695"></a>
### 695. feat: add WeakRef to memory.h {#commit-695}

Source: [39d54adc6fcde95d55c890cff47f162bc753550f](https://github.com/EndstoneMC/endstone/commit/39d54adc6fcde95d55c890cff47f162bc753550f); parent `76018a8718dc968af860af531f2b41c6c0c052e7`. Authored 2024-04-17T23:56:14Z. Disposition: meaningful.

Adds WeakRef convenience dereference/arrow/expired. Dereference locks only locally and returns borrowed reference after temporary lock dies; arrow similarly returns pointer without retained ownership. Safety therefore depends on external native ownership, not an enduring lease. Throws bad_weak_ptr only on reference dereference when expired.

<a id="commit-698"></a>
### 698. refactor: remove unused toString function from vanilla_dimensions.h {#commit-698}

Source: [0845b9f06f8972a71eeb91cbcb411167d948e02f](https://github.com/EndstoneMC/endstone/commit/0845b9f06f8972a71eeb91cbcb411167d948e02f); parent `8399ebac127b2074591e548a6e1c092df8cae79d`. Authored 2024-04-18T12:08:03Z. Disposition: small-semantic.

Removes unused extra-qualified VanillaDimensions::toString declaration introduced697. Reintroduced correctly with forwarding implementation703.

<a id="commit-700"></a>
### 700. feat: add base classes of Dimension {#commit-700}

Source: [ddd59165782e6e24d3de5f03e7c1d83c3d7b3659](https://github.com/EndstoneMC/endstone/commit/ddd59165782e6e24d3de5f03e7c1d83c3d7b3659); parent `9baae63854f2be912625891517644b90648f8434`. Authored 2024-04-18T13:21:38Z. Disposition: small-semantic.

Models Dimension multiple-inheritance bases IDimension, LevelListener, SavedData, EnableNonOwnerReferences. Adds minimal virtual/field declarations; native layout remains partial and no host validation supplied.

<a id="commit-702"></a>
### 702. feat: add member variables of Dimension {#commit-702}

Source: [c8de424ab692e1dfb7c31cbeaf727eed6be16013](https://github.com/EndstoneMC/endstone/commit/c8de424ab692e1dfb7c31cbeaf727eed6be16013); parent `15f7228222927341594145fd97f2af0846e2a622`. Authored 2024-04-18T13:51:28Z. Disposition: small-semantic.

Adds Dimension shared_from_this base, opaque transfer/vector fields, native Level reference and height range with platform-offset comments; getter simply returns borrowed level. Partial ABI mirror, not independent dimension ownership.

<a id="commit-704"></a>
### 704. feat: add EntityContext::getOrAddComponent {#commit-704}

Source: [da999e5a4aa24599f2f8d57ae19ed234f50ecf0a](https://github.com/EndstoneMC/endstone/commit/da999e5a4aa24599f2f8d57ae19ed234f50ecf0a); parent `d409f286032043ae53e6e079995444191e5fa34a`. Authored 2024-04-18T15:23:37Z. Disposition: small-semantic.

Adds const EntityContext getOrAddComponent forwarding EnTT get_or_emplace, enabling lazy wrapper allocation inside native registry. Const method can mutate referenced registry.

<a id="commit-714"></a>
### 714. feat: add Actor::getDimension {#commit-714}

Source: [3e1d05c68ebddeabaea484a66b811429d654019f](https://github.com/EndstoneMC/endstone/commit/3e1d05c68ebddeabaea484a66b811429d654019f); parent `f2bca73f6fa6b1197dea1ce09ef924ffdf941561`. Authored 2024-04-18T16:45:37Z. Disposition: small-semantic.

Replaces16 bytes of Actor padding with WeakRef<Dimension> at stated offset584 and adds borrowed dimension getter. Uses695 temporary-lock semantics.

<a id="commit-718"></a>
### 718. feat: make OwnerPtr only movable {#commit-718}

Source: [9f131591fa1b062c88872bf054f10be9496f03f1](https://github.com/EndstoneMC/endstone/commit/9f131591fa1b062c88872bf054f10be9496f03f1); parent `c3a9098b3c676ca9a0bde2c388d8cd4c612c979b`. Authored 2024-04-18T21:21:47Z. Disposition: meaningful.

Makes OwnerStorageEntity/OwnerPtr noncopyable and move-constructible, with move assignment deleted; forwards context via std::move into native add hook. This narrows transfer contract, not full generic smart-pointer destruction semantics. Hook replaced719.
