<!-- retrieval: {"source_ids":["public:commit:017d38e6b1f63831d45a4383a8d8fcaa08fd9c7b","public:commit:0db23dc489835adae64dcf8e3231f32604269a11","public:commit:0e56f6bde10a3b13cb85eb4083ab300dc84f2af6","public:commit:18cb4252191b3f64d001191567a3fc06931f386f","public:commit:19ab9039c2779d4c06dd3b0470630d87180b4e39","public:commit:2479c6765024c48a9f7873da7a8f3e7a16a55125","public:commit:2b0367d4f7f24cdb292190241748f5462abea495","public:commit:2e66ae992a3e4536911655481c031c1ab816f795","public:commit:3ac37b3ab1a2a7fb53c0af232699ae6396ec40ef","public:commit:3c91bbaf0e3bf5b990b4c4501bc4c6d3afc8dceb","public:commit:4bccf57b5e673c62afaf1294c46a3b8175ce1085","public:commit:4e370151ac68ade11e62101a01867992917db79f","public:commit:5bb5b275cc713dbc9a8e1355f5e0a5fb000e0ff5","public:commit:60135b6a5b7379ad0cf492ec42d1deecb6201f5f","public:commit:6371006b9a861630559ecfd60b25bf0660f1a19e","public:commit:68c99ad0959db655423e2b5ae0ea8a415b04fc4d","public:commit:6c7a019d1f654325616e1f06d57763a6c7e113e2","public:commit:6e81f14d8423edef9a3a6d2adca571f757ef9d34","public:commit:6f3fa906fcbcddd10cad4fe2f2fe5dc38a5f36ee","public:commit:74e224c1e093a7b250546cebc4d6da76d05a7b68","public:commit:7d1ca3a064eef0239afdeec2255d6cd55cfcf41c","public:commit:7de911c74293976bcc32fc822a4e1ead676b3a8b","public:commit:96982ca7e1ae46b7d68e85713dd7fa21df5fd665","public:commit:982e89c3c3d4a2bcc3ca9ef6782965983082be3c","public:commit:98baeb4fa4726282d6db9e93bcf94df71b533ef4","public:commit:a3103aa06ddce48bf94240d9a8aaf3972b583c1e","public:commit:b40cfcab7993329e4f4f346d5996a75ec7312542","public:commit:c2746aeb0754aebfca6036d5e20ac960dc1f331a","public:commit:ce3437a9a15c992e8481a5de63dacdac5690a653","public:commit:cf431ca1007d0f334b798010857c84f80f8b33d6","public:commit:de5f3a499b81f2e0bca7b10e215cbf87dd96c6a4","public:commit:e6de388bd977177480e67e65f525e523be116cce","public:commit:efc09bb4c0c3bad2c46f67010fa945ad46fc7d39","public:commit:f0a7dde08a48f04fbe0fc9e39ab4733b7b5fadb7","public:commit:f807e7d65d1cf6698a2900dc3eafa7ad7ebe6762","public:commit:f9150fdc81321a7ce44aafdc8e744bc73ce1ef21","public:commit:fcd6e77a506066596392933caaa00f4a5e7e09ce"],"source_type":"public","date":"2025-03-18..2025-03-24","topics":["lifetime","ffi","testing","build","api","diagnosis","documentation","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Inventory metadata and ownership evolution {#inventory-metadata-and-ownership-evolution}

## From declared metadata to working NBT conversion {#from-declared-metadata-to-working-nbt-conversion}

410 provides map-native layouts;411–413 expose metadata before native getItemMeta is implemented.457 moves generic metadata to a public constructible class,458 adds item metadata storage,460–462 introduce a map discriminator/factory/clone, and465–467 connect native display/lore NBT. These are staged revisions:457's wrong setLore condition,462's reversed getItemMeta ternary,467's wrong setter argument and unmanaged shared_from_this clear path are repaired in468–469.472 adds actual native Lore removal and stops skipping empty metadata.473 then adds optional display names. A linear summary saying the initial API worked throughout would erase important development history.

At500 metadata getters return copies; setters copy/convert metadata and null clears the implemented display-name/lore fields. Empty strings/empty lore normalize to absence. MapMeta preserves its dynamic clone type, but map-specific NBT remains TODO. Arbitrary user NBT is not wholesale removed by clear; only implemented metadata fields are applied/removed. ItemMeta::isEmpty still checks lore alone, so a named-only native stack can report hasItemMeta=false; the pure API stack checks stored pointer presence instead. This bounded mismatch has no native regression test here.

469 adds three pure ItemStack tests for lore set, lore remove and null clear.475 changes construction/arguments to unique ownership while retaining assertions. These tests establish the intended copy/normalization contract in source, not native inventory synchronization or NBT integration. No test execution or AI authorship is inferred from verbose test comments.

## Equipment and stale event state {#equipment-and-stale-event-state}

422–425 and435 add main/offhand/armor reads.430 changes StringByteOutput to borrow its destination string, enabling431's descriptor serializer.434 validates native hotbar selection, creates an equipment packet and broadcasts it; the public setter ignores failure and keeps a precondition diagnostic TODO, so invalid slots silently do nothing.477 adds setters; armor contract explicitly accepts arbitrary item types. Missing armor-type checks are therefore intentional, not automatically defects.

[455](https://github.com/EndstoneMC/endstone/commit/e277d632064fbb4dcdaa92607ca567e1be6b25ad) addresses issue159 by refreshing item_used after uncancelled BlockBreakEvent callbacks. The user report described item insertion, but the code repair is narrower: a pre-callback native item snapshot must not overwrite/ignore a plugin's selected-slot mutation. The existing issue dossier preserves MipaSenpai's report, Wu's response and the limitation that linked image/video demonstrations were not independently executed or inspected here.

## Unique wrapper ownership is distinct from native storage ownership {#unique-wrapper-ownership-is-distinct-from-native-storage-ownership}

475,476,478 and480 systematically remove shared ownership from metadata, items, blocks and block data. Factory/getter results become unique_ptr; setters borrow const pointers/references; event fields borrow callback-local wrappers; Python holders/bindings and mocks are updated. This removes shared_from_this preconditions for stack API items. It is also a C++ source/ABI compatibility change, accompanying API0.7.

The native EndstoneItemStack created fromMinecraft still borrows the source ItemStack pointer through const_cast. Existing setType can switch it to separately owned replacement storage; reset clears its handle. Unique_ptr ownership of the wrapper alone does not pin inventory storage or its Player holder. Block clones copy position plus a borrowed BlockSource reference, not an independent world; old 'only one Block' documentation does not describe clone behavior.

478's Python explosion list setter first clears the event's owning unique_ptr list, then clones raw input pointers. If those inputs came from the current list getter, the sources can be invalidated before clone. The source-level order is definite; no Python crash was reproduced. Synchronous callEvent keeps local wrappers alive during dispatch, but retaining borrowed references beyond it is not established safe. These are bounded lifetime implications of the changed ownership contract, not a general lifetime audit.

Evidence: all per-commit diffs below; endpoint ItemMeta/ItemStack/native converter/event-binding snapshots in context manifest; issue159 is credited in discussion provenance.

<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}


<a id="commit-410"></a>
### 410. feat: add map-related classes {#commit-410}

[fcd6e77a506066596392933caaa00f4a5e7e09ce](https://github.com/EndstoneMC/endstone/commit/fcd6e77a506066596392933caaa00f4a5e7e09ce) · 2025-03-18T19:29:16Z · author Vincent.

Parents: `f639c27b288a086db972f6bba4a96b13ff30ab01`. Read displays: parent 1.

Adds native map saved-data/tracked-actor/decoration scaffolding, pixel and tracked-entity fields and size assertions. Include-only cpp plus declarations do not implement a public map rendering API.

All-parent changed-file occurrences: 5. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-411"></a>
### 411. feat(item): add `ItemMeta` base class {#commit-411}

[6371006b9a861630559ecfd60b25bf0660f1a19e](https://github.com/EndstoneMC/endstone/commit/6371006b9a861630559ecfd60b25bf0660f1a19e) · 2025-03-18T19:46:19Z · author Vincent.

Parents: `fcd6e77a506066596392933caaa00f4a5e7e09ce`. Read displays: parent 1.

Adds abstract public ItemMeta with optional lore, shared_from_this/shared Python holder and export/stub. Unrelated Python indentation cleanup has no behavior change.

All-parent changed-file occurrences: 6. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-412"></a>
### 412. feat(item): add `EndstoneItemMeta` {#commit-412}

[b40cfcab7993329e4f4f346d5996a75ec7312542](https://github.com/EndstoneMC/endstone/commit/b40cfcab7993329e4f4f346d5996a75ec7312542) · 2025-03-18T20:04:48Z · author Vincent.

Parents: `6371006b9a861630559ecfd60b25bf0660f1a19e`. Read displays: parent 1.

Implements Base/Map meta type discrimination and optional lore storage with empty lore normalized to nullopt and copies returned. Native item application remains pending.

All-parent changed-file occurrences: 4. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-413"></a>
### 413. feat(item): add `ItemStack::getItemMeta` {#commit-413}

[e6de388bd977177480e67e65f525e523be116cce](https://github.com/EndstoneMC/endstone/commit/e6de388bd977177480e67e65f525e523be116cce) · 2025-03-18T20:24:38Z · author Vincent.

Parents: `b40cfcab7993329e4f4f346d5996a75ec7312542`. Read displays: parent 1.

Adds getItemMeta API promising a copy, but both public/native implementation still return nullptr TODO. Moves native accessors; existing native item constructor retains borrowed const_cast wrapper. This is staged incomplete functionality.

All-parent changed-file occurrences: 3. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-422"></a>
### 422. feat(inventory): add `PlayerInventory::getItemInMainHand` {#commit-422}

[2b0367d4f7f24cdb292190241748f5462abea495](https://github.com/EndstoneMC/endstone/commit/2b0367d4f7f24cdb292190241748f5462abea495) · 2025-03-21T16:55:02Z · author Vincent.

Parents: `84327b08f67205946d5ce8d56e3f0eae53886740`. Read displays: parent 1.

Adds public/Python main-hand getter using native supplies' selected-slot index and existing getItem conversion. Container-id selection is not consulted; borrowed native-item ownership remains. Native hotbar/selected-slot scaffolding accompanies API.

All-parent changed-file occurrences: 10. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-423"></a>
### 423. feat(inventory): add `Actor::getOffhandSlot` {#commit-423}

[7de911c74293976bcc32fc822a4e1ead676b3a8b](https://github.com/EndstoneMC/endstone/commit/7de911c74293976bcc32fc822a4e1ead676b3a8b) · 2025-03-21T17:06:54Z · author Vincent.

Parents: `2b0367d4f7f24cdb292190241748f5462abea495`. Read displays: parent 1.

Adds equipment component with unique hand/armor containers and size16 assertion, native offhand getter and hotbar size getter. No public setter yet.

All-parent changed-file occurrences: 7. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-424"></a>
### 424. feat(inventory): add `PlayerInventory::getItemInOffHand` {#commit-424}

[cf431ca1007d0f334b798010857c84f80f8b33d6](https://github.com/EndstoneMC/endstone/commit/cf431ca1007d0f334b798010857c84f80f8b33d6) · 2025-03-21T17:11:32Z · author Vincent.

Parents: `7de911c74293976bcc32fc822a4e1ead676b3a8b`. Read displays: parent 1.

Adds public/Python offhand getter converting native item; removes redundant outer const_cast, while native item wrapper still contains its own const_cast, so not an immutability guarantee.

All-parent changed-file occurrences: 6. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-425"></a>
### 425. feat(inventory): add `Actor::getArmor` {#commit-425}

[ce3437a9a15c992e8481a5de63dacdac5690a653](https://github.com/EndstoneMC/endstone/commit/ce3437a9a15c992e8481a5de63dacdac5690a653) · 2025-03-21T17:26:57Z · author Vincent.

Parents: `cf431ca1007d0f334b798010857c84f80f8b33d6`. Read displays: parent 1.

Adds native armor slot enum and getArmor access through persistent component. Humanoid slot count4 differs from total5 including Body. Component presence is assumed.

All-parent changed-file occurrences: 6. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-429"></a>
### 429. feat: add `Actor::isClientSide` {#commit-429}

[0db23dc489835adae64dcf8e3231f32604269a11](https://github.com/EndstoneMC/endstone/commit/0db23dc489835adae64dcf8e3231f32604269a11) · 2025-03-21T22:36:08Z · author Vincent.

Parents: `33b939ce48da6d7a539bdc8c833b0dee82c6d745`. Read displays: parent 1.

Adds Actor::isClientSide: true when level pointer absent, otherwise delegates to Level. Provides later equipment synchronization guard.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-430"></a>
### 430. fix: correct member of `StringByteOutput` {#commit-430}

[68c99ad0959db655423e2b5ae0ea8a415b04fc4d](https://github.com/EndstoneMC/endstone/commit/68c99ad0959db655423e2b5ae0ea8a415b04fc4d) · 2025-03-21T22:36:36Z · author Vincent.

Parents: `0db23dc489835adae64dcf8e3231f32604269a11`. Read displays: parent 1.

Changes StringByteOutput from owned string to borrowed string reference, mandatory ctor and size16; BigEndian inherits constructors and callers supply local buffers. Native ABI/lifetime correction, not merely field rename. Callers' buffer lifetime remains responsibility of use sites.

All-parent changed-file occurrences: 4. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-431"></a>
### 431. feat: add constructors for `ItemDescriptor` and its derived classes {#commit-431}

[3c91bbaf0e3bf5b990b4c4501bc4c6d3afc8dceb](https://github.com/EndstoneMC/endstone/commit/3c91bbaf0e3bf5b990b4c4501bc4c6d3afc8dceb) · 2025-03-21T22:37:03Z · author Vincent.

Parents: `68c99ad0959db655423e2b5ae0ea8a415b04fc4d`. Read displays: parent 1.

Adds deep ItemDescriptor copy via impl_->clone, counted descriptor ctor and NetworkItemStackDescriptor from native item with net-id/block runtime id/user-data serialization into member-owned buffer through borrowed StringByteOutput. Defaults initialize absent IDs. This supplies equipment packet materialization rather than sharing descriptor implementation.

All-parent changed-file occurrences: 4. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-432"></a>
### 432. feat: add `MobEquipmentPacket` {#commit-432}

[2479c6765024c48a9f7873da7a8f3e7a16a55125](https://github.com/EndstoneMC/endstone/commit/2479c6765024c48a9f7873da7a8f3e7a16a55125) · 2025-03-21T22:37:11Z · author Vincent.

Parents: `3c91bbaf0e3bf5b990b4c4501bc4c6d3afc8dceb`. Read displays: parent 1.

Declares MobEquipmentPacket native field layout for runtime id, item, int and byte slots/container identifiers. Actual construction still uses MinecraftPackets native factory; no independent serialization implementation/test.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-433"></a>
### 433. feat: add `ItemStack::getItemStackNetIdVariant` {#commit-433}

[6f3fa906fcbcddd10cad4fe2f2fe5dc38a5f36ee](https://github.com/EndstoneMC/endstone/commit/6f3fa906fcbcddd10cad4fe2f2fe5dc38a5f36ee) · 2025-03-21T22:37:23Z · author Vincent.

Parents: `2479c6765024c48a9f7873da7a8f3e7a16a55125`. Read displays: parent 1.

Defines native EMPTY_ITEM and const-reference network-id variant accessor used by descriptor/equipment selection.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-434"></a>
### 434. feat(inventory): add ability to get and set held item slot {#commit-434}

[de5f3a499b81f2e0bca7b10e215cbf87dd96c6a4](https://github.com/EndstoneMC/endstone/commit/de5f3a499b81f2e0bca7b10e215cbf87dd96c6a4) · 2025-03-21T22:43:43Z · author Vincent.

Parents: `6f3fa906fcbcddd10cad4fe2f2fe5dc38a5f36ee`. Read displays: parent 1.

Adds held-slot public/Python property. Native selection rejects out-of-hotbar range and client-side calls, then constructs/broadcasts equipment packet to entity viewers. Public setter ignores returned EMPTY_ITEM and retains TODO precondition diagnostic, so invalid indices silently leave selection unchanged rather than throwing. Native validation supplies the documented0–8 range; no test/runtime verification.

All-parent changed-file occurrences: 10. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-435"></a>
### 435. feat(inventory): add ability to get item stack from armor slots {#commit-435}

[19ab9039c2779d4c06dd3b0470630d87180b4e39](https://github.com/EndstoneMC/endstone/commit/19ab9039c2779d4c06dd3b0470630d87180b4e39) · 2025-03-21T22:53:00Z · author Vincent.

Parents: `de5f3a499b81f2e0bca7b10e215cbf87dd96c6a4`. Read displays: parent 1.

Adds four armor getter APIs/Python properties, converting native Head/Torso/Legs/Feet slots into item wrappers. Native holder and underlying item storage remain borrowed.

All-parent changed-file occurrences: 5. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-457"></a>
### 457. refactor: move `ItemMeta` implementations into the header file {#commit-457}

[2e66ae992a3e4536911655481c031c1ab816f795](https://github.com/EndstoneMC/endstone/commit/2e66ae992a3e4536911655481c031c1ab816f795) · 2025-03-23T13:34:13Z · author Vincent.

Parents: `dd37325b9febd68cce4c8d0d94aec5dd6197dbe6`. Read displays: parent 1.

Moves ItemMeta implementation into public header and removes native subclass/cpp/CMake entry, making pure metadata constructible. Introduces wrong setLore condition reading old lore_.value() and negated emptiness;468 repairs it. Intermediate behavior cannot be treated as equivalent move.

All-parent changed-file occurrences: 4. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-458"></a>
### 458. feat: add `hasItemMeta` and `setItemMeta` method to `ItemStack` {#commit-458}

[f9150fdc81321a7ce44aafdc8e744bc73ce1ef21](https://github.com/EndstoneMC/endstone/commit/f9150fdc81321a7ce44aafdc8e744bc73ce1ef21) · 2025-03-23T18:08:37Z · author Vincent.

Parents: `2e66ae992a3e4536911655481c031c1ab816f795`. Read displays: parent 1.

Adds pure ItemStack has/set meta with defensive copies and nullable clear; initial clone slices specific metadata (TODO). Native implementation remains staged until467.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-459"></a>
### 459. refactor: replace `asEndstoneItemStack` with `isEndstoneItemStack` {#commit-459}

[96982ca7e1ae46b7d68e85713dd7fa21df5fd665](https://github.com/EndstoneMC/endstone/commit/96982ca7e1ae46b7d68e85713dd7fa21df5fd665) · 2025-03-23T18:20:24Z · author Vincent.

Parents: `f9150fdc81321a7ce44aafdc8e744bc73ce1ef21`. Read displays: parent 1.

Replaces native downcast helper with Boolean discriminator in public ItemStack, preceding concrete implementation update467. Intermediate override consistency unresolved until that update.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-460"></a>
### 460. feat: add `MapMeta` class {#commit-460}

[98baeb4fa4726282d6db9e93bcf94df71b533ef4](https://github.com/EndstoneMC/endstone/commit/98baeb4fa4726282d6db9e93bcf94df71b533ef4) · 2025-03-23T18:41:41Z · author Vincent.

Parents: `96982ca7e1ae46b7d68e85713dd7fa21df5fd665`. Read displays: parent 1.

Adds MapMeta discriminator and Python class/export include; no map-specific fields yet. This is specialization scaffold.

All-parent changed-file occurrences: 3. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-461"></a>
### 461. feat: add `ItemFactory` {#commit-461}

[5bb5b275cc713dbc9a8e1355f5e0a5fb000e0ff5](https://github.com/EndstoneMC/endstone/commit/5bb5b275cc713dbc9a8e1355f5e0a5fb000e0ff5) · 2025-03-23T18:58:23Z · author Vincent.

Parents: `98baeb4fa4726282d6db9e93bcf94df71b533ef4`. Read displays: parent 1.

Adds ItemFactory selecting filled-map meta versus generic meta and conversion helper. Pointer-copy constructors needed by factory arrive462, so this intermediate staged API is not independently established buildable.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-462"></a>
### 462. feat: add `ItemMeta::clone` {#commit-462}

[4bccf57b5e673c62afaf1294c46a3b8175ce1085](https://github.com/EndstoneMC/endstone/commit/4bccf57b5e673c62afaf1294c46a3b8175ce1085) · 2025-03-23T19:00:31Z · author Vincent.

Parents: `5bb5b275cc713dbc9a8e1355f5e0a5fb000e0ff5`. Read displays: parent 1.

Adds polymorphic clone, pointer-copy ctor, ItemMeta Base→Item type and factory application. getItemMeta ternary is reversed and null branch dereferences meta_;469 repairs. MapMeta clone initially inherits base implementation until465. Preserve intermediate faults rather than smoothing into final feature.

All-parent changed-file occurrences: 4. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-463"></a>
### 463. feat: update python bindings {#commit-463}

[efc09bb4c0c3bad2c46f67010fa945ad46fc7d39](https://github.com/EndstoneMC/endstone/commit/efc09bb4c0c3bad2c46f67010fa945ad46fc7d39) · 2025-03-23T19:04:29Z · author Vincent.

Parents: `4bccf57b5e673c62afaf1294c46a3b8175ce1085`. Read displays: parent 1.

Updates Python stub/facade with MapMeta and clone to match binding surface; repeated export line read and checked against actual bindings.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-464"></a>
### 464. feat: add `ItemStackBase::TAG_LORE` {#commit-464}

[0e56f6bde10a3b13cb85eb4083ab300dc84f2af6](https://github.com/EndstoneMC/endstone/commit/0e56f6bde10a3b13cb85eb4083ab300dc84f2af6) · 2025-03-23T19:47:23Z · author Vincent.

Parents: `efc09bb4c0c3bad2c46f67010fa945ad46fc7d39`. Read displays: parent 1.

Adds native Lore NBT tag constant used by forthcoming metadata converter.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-465"></a>
### 465. feat: add `EndstoneItemFactory` {#commit-465}

[f0a7dde08a48f04fbe0fc9e39ab4733b7b5fadb7](https://github.com/EndstoneMC/endstone/commit/f0a7dde08a48f04fbe0fc9e39ab4733b7b5fadb7) · 2025-03-23T19:47:53Z · author Vincent.

Parents: `0e56f6bde10a3b13cb85eb4083ab300dc84f2af6`. Read displays: parent 1.

Adds EndstoneItemFactory native lore loading and MapMeta clone override, preserving dynamic type. Initial loader omits empty lore lines;467 retains them. Map-specific NBT remains TODO. CMake links implementation.

All-parent changed-file occurrences: 4. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-466"></a>
### 466. feat: add `CompoundTag::getList` {#commit-466}

[4e370151ac68ade11e62101a01867992917db79f](https://github.com/EndstoneMC/endstone/commit/4e370151ac68ade11e62101a01867992917db79f) · 2025-03-23T20:26:13Z · author Vincent.

Parents: `f0a7dde08a48f04fbe0fc9e39ab4733b7b5fadb7`. Read displays: parent 1.

Implements const/mutable CompoundTag getList with runtime type check and null on absent/wrong type. Borrowed pointer into tag storage.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-467"></a>
### 467. feat: implement `EndstoneItemStack` {#commit-467}

[a3103aa06ddce48bf94240d9a8aaf3972b583c1e](https://github.com/EndstoneMC/endstone/commit/a3103aa06ddce48bf94240d9a8aaf3972b583c1e) · 2025-03-23T20:26:37Z · author Vincent.

Parents: `4e370151ac68ade11e62101a01867992917db79f`. Read displays: parent 1.

Implements native item metadata conversion/application, copies raw native stacks when converting wrappers and serializes pure API metadata. Introduces clear path through stack EMPTY.shared_from_this and mistaken meta_ member instead of parameter;468 repairs. Native metadata is fresh copy, native ItemStack wrapper still borrows item pointer; no materialized owner conversion. NBT application initially adds lore only and skips empty meta, preventing removal until472.

All-parent changed-file occurrences: 7. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-468"></a>
### 468. fix: `ItemMeta::setLore` now works as expected {#commit-468}

[6c7a019d1f654325616e1f06d57763a6c7e113e2](https://github.com/EndstoneMC/endstone/commit/6c7a019d1f654325616e1f06d57763a6c7e113e2) · 2025-03-23T21:35:50Z · author Vincent.

Parents: `a3103aa06ddce48bf94240d9a8aaf3972b583c1e`. Read displays: parent 1.

Repairs setLore to inspect supplied optional, passes actual setItemMeta parameter, uses owned shared empty-meta instead of unmanaged shared_from_this and keeps lore optional local during iteration. Adds Python meta property. Does not yet fix pure-stack reversed ternary or NBT removal;469/472 do that.

All-parent changed-file occurrences: 6. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-469"></a>
### 469. test: add tests for `ItemMeta` {#commit-469}

[982e89c3c3d4a2bcc3ca9ef6782965983082be3c](https://github.com/EndstoneMC/endstone/commit/982e89c3c3d4a2bcc3ca9ef6782965983082be3c) · 2025-03-23T23:02:59Z · author Vincent.

Parents: `6c7a019d1f654325616e1f06d57763a6c7e113e2`. Read displays: parent 1.

Adds three pure ItemStack lore/set/remove/null-clear tests and CMake registration, while fixing reversed getItemMeta null ternary. Tests validate API copies/normalization, not native NBT/inventory/lifetime paths. Tests read, not run; no AI authorship inference from comment style.

All-parent changed-file occurrences: 3. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-470"></a>
### 470. style: code clean up {#commit-470}

[6e81f14d8423edef9a3a6d2adca571f757ef9d34](https://github.com/EndstoneMC/endstone/commit/6e81f14d8423edef9a3a6d2adca571f757ef9d34) · 2025-03-23T23:06:10Z · author Vincent.

Parents: `982e89c3c3d4a2bcc3ca9ef6782965983082be3c`. Read displays: parent 1.

Uses returned putCompound pointer and scoped optional lore local; behavior-equivalent cleanup after468, retaining no-removal branch until472.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-471"></a>
### 471. feat(python): add explicit setter for `ItemMeta` in `ItemStack` {#commit-471}

[60135b6a5b7379ad0cf492ec42d1deecb6201f5f](https://github.com/EndstoneMC/endstone/commit/60135b6a5b7379ad0cf492ec42d1deecb6201f5f) · 2025-03-23T23:11:45Z · author Vincent.

Parents: `6e81f14d8423edef9a3a6d2adca571f757ef9d34`. Read displays: parent 1.

Makes Python item_meta read-only plus explicit Boolean-returning set_item_meta, aligning return-bearing mutation with set_type/set_data. Also removes Python Block type/data property setters, retaining explicit methods with physics argument. Compatibility shift; no C++ removal.

All-parent changed-file occurrences: 3. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-472"></a>
### 472. fix: lore can now be correctly removed {#commit-472}

[7d1ca3a064eef0239afdeec2255d6cd55cfcf41c](https://github.com/EndstoneMC/endstone/commit/7d1ca3a064eef0239afdeec2255d6cd55cfcf41c) · 2025-03-23T23:38:31Z · author Vincent.

Parents: `60135b6a5b7379ad0cf492ec42d1deecb6201f5f`. Read displays: parent 1.

Fixes native lore removal by deleting Lore when absent and applying even empty converted metadata. Null clear now reaches remover. No native regression test added here.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-473"></a>
### 473. feat: add `ItemMeta::getDisplayName` and `ItemMeta::setDisplayName` {#commit-473}

[017d38e6b1f63831d45a4383a8d8fcaa08fd9c7b](https://github.com/EndstoneMC/endstone/commit/017d38e6b1f63831d45a4383a8d8fcaa08fd9c7b) · 2025-03-23T23:57:34Z · author Vincent.

Parents: `7d1ca3a064eef0239afdeec2255d6cd55cfcf41c`. Read displays: parent 1.

Adds optional display-name public/Python/NBT read/write/removal, treating empty string as absent. ItemMeta::isEmpty still checks lore only through500, so named-only native hasItemMeta reports false despite present name metadata; pure ItemStack uses pointer-presence instead.

All-parent changed-file occurrences: 5. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-474"></a>
### 474. refactor: remove unused include {#commit-474}

[f807e7d65d1cf6698a2900dc3eafa7ad7ebe6762](https://github.com/EndstoneMC/endstone/commit/f807e7d65d1cf6698a2900dc3eafa7ad7ebe6762) · 2025-03-24T00:02:06Z · author Vincent.

Parents: `017d38e6b1f63831d45a4383a8d8fcaa08fd9c7b`. Read displays: parent 1.

Removes unused Boost MPL include added468; no behavior change.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-475"></a>
### 475. refactor: remove unnecessary use of shared_ptr for `ItemMeta` {#commit-475}

[74e224c1e093a7b250546cebc4d6da76d05a7b68](https://github.com/EndstoneMC/endstone/commit/74e224c1e093a7b250546cebc4d6da76d05a7b68) · 2025-03-24T19:20:43Z · author Vincent.

Parents: `f807e7d65d1cf6698a2900dc3eafa7ad7ebe6762`. Read displays: parent 1.

Replaces shared metadata with unique_ptr copies, raw borrowed setter inputs and reference-based native factory helpers; removes enable_shared_from_this and uses static EMPTY by const reference. Tests updated to stack ItemStack/unique meta without removing assertions. Unique ownership covers metadata, not underlying item storage; ItemStack implicit copyability also changes due unique member.

All-parent changed-file occurrences: 10. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-476"></a>
### 476. refactor: remove unnecessary use of shared_ptr for `ItemStack` {#commit-476}

[18cb4252191b3f64d001191567a3fc06931f386f](https://github.com/EndstoneMC/endstone/commit/18cb4252191b3f64d001191567a3fc06931f386f) · 2025-03-24T20:00:29Z · author Vincent.

Parents: `74e224c1e093a7b250546cebc4d6da76d05a7b68`. Read displays: parent 1.

Replaces shared ItemStack API results with unique_ptr, setter inputs const pointers and stack-safe add/first; removes shared_from_this dependency. Event item borrows callback-local wrapper pointer, Python default holder changes. Native fromMinecraft wrapper still borrows its source item; setType can switch it to owned replacement storage, an existing distinction. Unique wrapper ownership does not fix borrowed-source lifetime. Stub loses None annotation although native pointer clear path persists; __get_item__/__set_item__ names unchanged.

All-parent changed-file occurrences: 13. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-477"></a>
### 477. feat: add setters for armor slots and player's main/off-hand items {#commit-477}

[c2746aeb0754aebfca6036d5e20ac960dc1f331a](https://github.com/EndstoneMC/endstone/commit/c2746aeb0754aebfca6036d5e20ac960dc1f331a) · 2025-03-24T20:32:15Z · author Vincent.

Parents: `18cb4252191b3f64d001191567a3fc06931f386f`. Read displays: parent 1.

Adds armor/main/offhand public/Python setters using native virtual equipment operations; main hand uses inventory setter plus sendInventory, armor/offhand rely on native methods. Contract explicitly permits non-armor item types in armor slots, so absence of armor-type validation is intentional.

All-parent changed-file occurrences: 5. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-478"></a>
### 478. refactor: remove unnecessary use of shared_ptr for `Block` {#commit-478}

[3ac37b3ab1a2a7fb53c0af232699ae6396ec40ef](https://github.com/EndstoneMC/endstone/commit/3ac37b3ab1a2a7fb53c0af232699ae6396ec40ef) · 2025-03-24T21:27:45Z · author Vincent.

Parents: `c2746aeb0754aebfca6036d5e20ac960dc1f331a`. Read displays: parent 1.

Converts Block APIs and explosion lists to unique ownership, event fields to borrowed refs/pointers, adds clone and reference_wrapper for native BlockSource. Caller-local ownership spans synchronous dispatch. Python explosion setter clears owning list before cloning input raw pointers, so assigning pointers obtained from its current list can invalidate sources before clone. Clone duplicates location wrapper, not world ownership; existing 'only one Block' documentation is stale. Bounded lifetime finding, not runtime reproduction.

All-parent changed-file occurrences: 20. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.
