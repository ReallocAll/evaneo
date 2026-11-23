<!-- retrieval: {"source_ids":["public:commit:0b8127287fb334264f2bd4268e822a77fa0c7d82","public:commit:0da0315a5cbec35a2ce496a5a2046e2912cf8048","public:commit:12ca822416cb62539b147d95e6ce9ffc2bb2fe6f","public:commit:144778827a676ea68067f65221c4b0153645c62a","public:commit:16a1a1856a1ab6de37aeff59fcf968849953afdd","public:commit:17f0f15f1a59d7633248ad510a263b042f659e6e","public:commit:18c83baecbfa2b1a94be1d6bc018954345107b86","public:commit:21b2b902a41b656c1e3eba9fb02d6ad9ec86d5eb","public:commit:23eaf19aff66854e2d01c7722de03ba8c5de19f5","public:commit:24881e235ed01dd09b853ed3ca7c7d0ae6529c00","public:commit:2b4fa21574fe4a095c2221873d51df6fd1d7919d","public:commit:472562fe93cb7ff9fe8425e0cec6fff963255353","public:commit:4925a8b6afb6b7b379cf2c3aa21028bf9938f765","public:commit:52c7ed2aa41f392500c60d79542cd7a4d5bc30c7","public:commit:5dadcc04645c11875caa592c30e7188aba70bec3","public:commit:765ba002f5987c96a8ad4e91b177e638251772e2","public:commit:8f9cdebf513af49c5af39fe1f62ccba7a7871415","public:commit:943306adb6de47bdd356d394ba08d9bf77475414","public:commit:af0784d8edd9de328aafd98d0e727f11c44ffd66","public:commit:c98f8a6cddbc298fa74bb7638458daffa6c44887","public:commit:d322fb6bfd35b63b413e78cbadede849faa502fa","public:commit:d5b996e9725217f1c91f48a62e9e61fcd4021fe1","public:commit:ddb4ed65d20c79ee36dc312081e496aa25c08cde","public:commit:de8bdd0f34cdea984f581cff12ad786a9160814b","public:commit:e1a62bb226534265e82c278e8382017af15946e5","public:commit:e3f40a8d003fd80521a809b93d6499fce4de41d3","public:commit:ea398d24ad56b19f6eb04c7ebad805ba52e39de7","public:commit:eb3aa3e6900a922207b0f4e71a7995b2ba1380b8","public:commit:ee346d335c2c8185455a0b08a89ea03a09c046ff","public:commit:ee3c704494ab9da503660b16139acabf470c29ba"],"source_type":"public","date":"2025-01-05..2025-01-11","topics":["lifetime","concurrency","ffi","testing","build","api","diagnosis","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native ABI models and inventory reconstruction {#native-abi-models-and-inventory-reconstruction}

## Representation is a compatibility claim {#representation-is-a-compatibility-claim}

The first native changes reconstruct Bedrock structures and virtual interfaces in stages.27 adds an Explosion layout and forwarding hook without an API event.30 removes fields and changes Scoreboard/ServerScoreboard size assertions.31 models gameplay-handler overloads and mutable block event variants.40 corrects a native virtual return type from a void placeholder to RedactableString.45 removes Json allocation/type bitfields, and75 changes the enum's underlying type to char while total Json::Value size stays16. These are examples of why sizeof alone cannot establish field, vtable or calling-convention compatibility. Addresses, offsets and static assertions were read but never tested against a running Bedrock binary.

C++/Python API models and native ABI models have different ownership. InternalItemDescriptor stores a raw item pointer obtained from a WeakPtr; it does not extend item-registry lifetime. The native shared/weak pointer implementation uses a custom counter.74 initializes null counters and repairs WeakPtr assignment ordering, but also removes SharedPtr's explicit assignment/move operations; the final type still has an implicitly generated shallow pointer assignment. That is a static ownership hazard if such assignment is used, not an observed crash. The implicit conversion to raw T* does not create an ownership guarantee.

## Item construction is not completed in one refactor {#item-construction-is-not-completed-in-one-refactor}

32–51 move declaration bodies into sources while adding descriptors, serialization, constructors, copy/assignment, registry lookup and diagnostics. Several intermediate commits leave declarations undefined.48 replaces an artificial native factory mechanism with ordinary ItemStack constructors and value conversion, with the author explicitly describing the old factory as ugly. Native calls receive stable local values rather than temporary pointers. This does not mean all item behavior has been reimplemented correctly:51's copy constructor initializes with its own count_, and77 explicitly fixes it to rhs.count_. User-data assignment only copies when the source has a tag, so removal of an old tag is not demonstrated by that branch.

69 implements ItemStackBase initialization using item/block IDs, legacy block permutations, wildcard aux and cloned NBT;71 delegates its low-level integer init back to the native binary.85 similarly replaces local user-data/charged-item reconstruction with a native call and removes ItemInstance::fromTag. This is a useful engineering trade-off: reconstruct direct field operations where understood, but return to native behavior for complex invariant maintenance. The code sequence demonstrates that trade-off; no explicit author statement explains every delegation decision.

70 introduces a compatibility mutex guard and BaseGameVersion/SemVersion logic. The guard owns a shared mutex pointer and manually locks/unlocks; it has no explicit copy prohibition in the final header. For unequal core versions, SemVersion::< compares its own major/minor/patch tuple to itself and therefore returns false, rather than ordering against rhs. It also still throws for equal core versions with the same prerelease-presence state, despite a commit subject claiming all undefined methods. Its <= short-circuits equality, so exact equal versions avoid that throw through <=, while distinct prereleases do not. > and >= are declared without definitions in the inspected endpoint. Preserve the exact reachable condition rather than saying every equal-version compatibility check fails.

## Serialization and algorithm edges {#serialization-and-algorithm-edges}

34's ADL JSON conversion does not initialize empty arrays/objects in a fresh JSON destination and does not reset an existing destination when input is null.36 uses descriptor serialization to extract recipe tags;75 repairs the object-versus-item branch.41 writes native bool, short and float representations into a binary stream. The project restricts itself to x86_64 in16, but that restriction alone is not an endian/protocol fixture test.44/46 descriptor matching includes wildcard aux and block canonicalization, yet sameItems ignores its supplied comparison operand in this intermediate implementation.47's cache has an iterator-member typo and performs insertion/factory work under a mutex after an earlier lookup; an initial miss can still create duplicate work. These are boundaries for reuse, not polished examples to copy unquestioningly.

97 supplies BlockPos equality/hash in preparation for mutable explosion block sets. Its arithmetic/hash mechanism is visible and unbenchmarked. All tests changed in this unit were read, but no item ABI, NBT roundtrip, JSON empty-container, ownership, or native-calling-convention test outcome was observed.


<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}



<a id="commit-027"></a>
### 027. feat: hook `Explosion::explode` for explosion events {#commit-027}

Commit: [d5b996e9725217f1c91f48a62e9e61fcd4021fe1](https://github.com/EndstoneMC/endstone/commit/d5b996e9725217f1c91f48a62e9e61fcd4021fe1) · committed 2025-01-05T00:07:27Z · author Vincent.

Actual parent: `f9f0b6bfc5b82eee302479fa7a1c649de08498c8`. Full message and parent-relative patch: local source.

Adds Explosion layout and both platform explode symbol offsets, with a forwarding hook and fire accessors. No Endstone explosion event is emitted yet. ActorUniqueID invalid sentinel declaration is corrected in28; native structure fields/symbol addresses are compatibility assertions, not validated runtime facts.

Changed-file coverage: 7 paths. `include/bedrock/forward.h`; `include/bedrock/world/actor/actor_unique_id.h`; `include/bedrock/world/level/explosion.h`; `include/bedrock/world/level/level_interface.h`; `python/src/endstone/_internal/symbols.toml`; `src/endstone_runtime/CMakeLists.txt`; `src/endstone_runtime/bedrock/world/level/explosion.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-030"></a>
### 030. fix: ServerScoreboard structure {#commit-030}

Commit: [eb3aa3e6900a922207b0f4e71a7995b2ba1380b8](https://github.com/EndstoneMC/endstone/commit/eb3aa3e6900a922207b0f4e71a7995b2ba1380b8) · committed 2025-01-05T17:48:04Z · author Vincent.

Actual parent: `d5009b564b7f40edc8d17c832f3fcc718205ae90`. Full message and parent-relative patch: local source.

Corrects reconstructed Scoreboard/ServerScoreboard layouts by removing event tracker specialization and trailing ImGui member; size assertions change 792/560→784/552 and968/736→944/712. Introduces generic EventCoordinator deriving Pimpl and ActorUniqueID validity helpers. Assertions are compile-time expectations, not proof of Bedrock ABI.

Changed-file coverage: 6 paths. `include/bedrock/world/actor/actor_unique_id.h`; `include/bedrock/world/events/block_event_coordinator.h`; `include/bedrock/world/events/event_coordinator.h`; `include/bedrock/world/events/scoreboard_event_coordinator.h`; `include/bedrock/world/scores/scoreboard.h`; `include/bedrock/world/scores/server_scoreboard.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-031"></a>
### 031. feat: add BlockGameplayHandler {#commit-031}

Commit: [943306adb6de47bdd356d394ba08d9bf77475414](https://github.com/EndstoneMC/endstone/commit/943306adb6de47bdd356d394ba08d9bf77475414) · committed 2025-01-05T18:05:46Z · author Vincent.

Actual parent: `eb3aa3e6900a922207b0f4e71a7995b2ba1380b8`. Full message and parent-relative patch: local source.

Models block/scripting handler virtual overloads, block coordinator handler ownership, mutable ExplosionStarted/BlockTryDestroy events and watchdog event lifetime scope. Preserves variant ordering/padding per platform. This prepares event interception through handlers; no implementation is attached yet. Missing explicit template specialization marker is repaired in33.

Changed-file coverage: 8 paths. `include/bedrock/forward.h`; `include/bedrock/gameplayhandlers/scripting_event_handler.h → include/bedrock/gameplayhandlers/block_gameplay_handler.h`; `include/bedrock/gameplayhandlers/scripting_event_handler.h`; `include/bedrock/gameplayhandlers/scripting_event_handler.h → include/bedrock/scripting/lifetime_registry/lifetime_scope.h`; `include/bedrock/world/events/block_event_coordinator.h`; `include/bedrock/world/events/block_events.h`; `include/bedrock/world/events/scripting_event_coordinator.h`; `include/bedrock/world/events/scripting_events.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-032"></a>
### 032. refactor: separate definitions from declarations {#commit-032}

Commit: [18c83baecbfa2b1a94be1d6bc018954345107b86](https://github.com/EndstoneMC/endstone/commit/18c83baecbfa2b1a94be1d6bc018954345107b86) · committed 2025-01-05T22:21:38Z · author Vincent.

Actual parent: `943306adb6de47bdd356d394ba08d9bf77475414`. Full message and parent-relative patch: local source.

Separates Block and ItemDescriptor bodies into sources while preserving direct-data/delegation behavior, but also adds descriptor binary/JSON serialization, lazy resolve, private impl_, constructors and debug name output. Renames getLiquidClipShape to getLiquidClipVolume. Constructors are only declared at this stage; sources enter build in33.

Changed-file coverage: 4 paths. `include/bedrock/world/item/item_descriptor.h`; `include/bedrock/world/level/block/block.h`; `src/endstone_runtime/bedrock/world/item/item_descriptor.cpp`; `src/endstone_runtime/bedrock/world/level/block/block.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-033"></a>
### 033. feat: implement ItemStackBase {#commit-033}

Commit: [5dadcc04645c11875caa592c30e7188aba70bec3](https://github.com/EndstoneMC/endstone/commit/5dadcc04645c11875caa592c30e7188aba70bec3) · committed 2025-01-05T22:22:15Z · author Vincent.

Actual parent: `18c83baecbfa2b1a94be1d6bc018954345107b86`. Full message and parent-relative patch: local source.

Begins native ItemStackBase implementation: initializes fields, reset logic, textual diagnostics, descriptor construction and ID/count methods; registers new block/descriptor sources and fixes31 specialization. reinit overloads remain empty. set() currently clears when !isNull(), an observed surprising branch requiring later-history checks; no tests validate behavior. Several native size/offset annotations are still provisional.

Changed-file coverage: 4 paths. `include/bedrock/world/events/block_events.h`; `include/bedrock/world/item/item_stack_base.h`; `src/endstone_runtime/CMakeLists.txt`; `src/endstone_runtime/bedrock/world/item/item_stack_base.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-034"></a>
### 034. refactor: rework the conversion from Json::Value to nlohmann::json {#commit-034}

Commit: [e3f40a8d003fd80521a809b93d6499fce4de41d3](https://github.com/EndstoneMC/endstone/commit/e3f40a8d003fd80521a809b93d6499fce4de41d3) · committed 2025-01-05T22:23:07Z · author Vincent.

Actual parent: `5dadcc04645c11875caa592c30e7188aba70bec3`. Full message and parent-relative patch: local source.

Replaces standalone recursive Json::to_nlohmann helper with ADL to_json and noexcept swap. Conversion now relies on implicit recursion at assignments; absent explicit initialization means empty arrays/objects remain null in a fresh destination and null conversion does not reset an existing destination. Removes default invalid-type exception. These are observable edge semantics, not established intentional changes.

Changed-file coverage: 3 paths. `include/bedrock/deps/json/nlohmann_json.h`; `include/bedrock/deps/json/value.h`; `src/endstone_runtime/bedrock/deps/json/value.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-035"></a>
### 035. feat: add constructors for Tick {#commit-035}

Commit: [ee346d335c2c8185455a0b08a89ea03a09c046ff](https://github.com/EndstoneMC/endstone/commit/ee346d335c2c8185455a0b08a89ea03a09c046ff) · committed 2025-01-05T22:23:31Z · author Vincent.

Actual parent: `e3f40a8d003fd80521a809b93d6499fce4de41d3`. Full message and parent-relative patch: local source.

Adds explicit uint64 Tick constructor and default constructor supporting the prior reset code; no independent larger design claim.

Changed-file coverage: 1 paths. `include/bedrock/world/level/tick.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-036"></a>
### 036. refactor: use `ItemDescriptor::ANY_AUX_VALUE` instead of the hardcoded 0x7fff {#commit-036}

Commit: [765ba002f5987c96a8ad4e91b177e638251772e2](https://github.com/EndstoneMC/endstone/commit/765ba002f5987c96a8ad4e91b177e638251772e2) · committed 2025-01-05T22:24:04Z · author Vincent.

Actual parent: `ee346d335c2c8185455a0b08a89ea03a09c046ff`. Full message and parent-relative patch: local source.

Beyond replacing magic aux constants, moves recipe ingredient inspection from public descriptor internals to serialize(Json::Value) plus ADL conversion, distinguishing string item names from item_tag objects. Updates renamed liquid clip API and explicit ItemDescriptor construction. This follows encapsulation in32/34.

Changed-file coverage: 1 paths. `src/endstone_devtools/vanilla_data.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-037"></a>
### 037. refactor: clean up headers {#commit-037}

Commit: [0b8127287fb334264f2bd4268e822a77fa0c7d82](https://github.com/EndstoneMC/endstone/commit/0b8127287fb334264f2bd4268e822a77fa0c7d82) · committed 2025-01-05T22:24:15Z · author Vincent.

Actual parent: `765ba002f5987c96a8ad4e91b177e638251772e2`. Full message and parent-relative patch: local source.

Fixes required scripting handler include, declares Item::buildDescriptor, removes deleted JSON conversion headers and lets form response ADL conversion happen at the call boundary. Existing dead-player/null guard is retained.

Changed-file coverage: 4 paths. `include/bedrock/gameplayhandlers/scripting_event_handler.h`; `include/bedrock/world/item/item.h`; `src/endstone_core/player.cpp`; `src/endstone_runtime/bedrock/world/events/player_event_coordinator.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-038"></a>
### 038. feat: implement `CompoundTag::remove` {#commit-038}

Commit: [ddb4ed65d20c79ee36dc312081e496aa25c08cde](https://github.com/EndstoneMC/endstone/commit/ddb4ed65d20c79ee36dc312081e496aa25c08cde) · committed 2025-01-05T22:26:25Z · author Vincent.

Actual parent: `0b8127287fb334264f2bd4268e822a77fa0c7d82`. Full message and parent-relative patch: local source.

Implements CompoundTag::remove as lookup, false when missing, erase and true when present; supplies reset path used by ItemStackBase.

Changed-file coverage: 1 paths. `src/endstone_runtime/bedrock/nbt/compound_tag.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-039"></a>
### 039. feat: implement `ItemDescriptor::getId` {#commit-039}

Commit: [8f9cdebf513af49c5af39fe1f62ccba7a7871415](https://github.com/EndstoneMC/endstone/commit/8f9cdebf513af49c5af39fe1f62ccba7a7871415) · committed 2025-01-05T22:29:41Z · author Vincent.

Actual parent: `ddb4ed65d20c79ee36dc312081e496aa25c08cde`. Full message and parent-relative patch: local source.

Implements ItemDescriptor ID with -1 for no impl, lazy resolution, native item ID or0 for missing item. This distinguishes invalid descriptor from empty item.

Changed-file coverage: 1 paths. `src/endstone_runtime/bedrock/world/item/item_descriptor.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-040"></a>
### 040. refactor: separate definitions from declarations for `Item` class {#commit-040}

Commit: [0da0315a5cbec35a2ce496a5a2046e2912cf8048](https://github.com/EndstoneMC/endstone/commit/0da0315a5cbec35a2ce496a5a2046e2912cf8048) · committed 2025-01-05T22:38:08Z · author Vincent.

Actual parent: `8f9cdebf513af49c5af39fe1f62ccba7a7871415`. Full message and parent-relative patch: local source.

Moves Item getters out of header, introduces real RedactableString return type instead of void placeholder in a virtual method, makes low-level permission hooks private, and builds descriptor from item/aux while ignoring supplied tag. Native vtable signature correction matters more than source organization.

Changed-file coverage: 4 paths. `include/bedrock/safety/redactable_string.h`; `include/bedrock/world/item/item.h`; `include/bedrock/world/item/item_descriptor.h`; `src/endstone_runtime/bedrock/world/item/item.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-041"></a>
### 041. feat: add `BinaryStream::writeSignedShort` {#commit-041}

Commit: [d322fb6bfd35b63b413e78cbadede849faa502fa](https://github.com/EndstoneMC/endstone/commit/d322fb6bfd35b63b413e78cbadede849faa502fa) · committed 2025-01-05T23:37:18Z · author Vincent.

Actual parent: `0da0315a5cbec35a2ce496a5a2046e2912cf8048`. Full message and parent-relative patch: local source.

Adds signed/unsigned16-bit writes, makes raw write private, renames byte API at particle codec caller and reorders methods. Boolean changes from explicit0/1 byte to native bool storage; short/float writes use native representations. Scope is x86_64 per16; no portable-endian or wire-fixture evidence.

Changed-file coverage: 3 paths. `include/bedrock/core/utility/binary_stream.h`; `src/endstone_core/network/spawn_particle_effect_packet_codec.cpp`; `src/endstone_runtime/bedrock/core/utility/binary_stream.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-042"></a>
### 042. feat: add `BlockLegacy::getBlockItemId` {#commit-042}

Commit: [12ca822416cb62539b147d95e6ce9ffc2bb2fe6f](https://github.com/EndstoneMC/endstone/commit/12ca822416cb62539b147d95e6ce9ffc2bb2fe6f) · committed 2025-01-05T23:37:42Z · author Vincent.

Actual parent: `d322fb6bfd35b63b413e78cbadede849faa502fa`. Full message and parent-relative patch: local source.

Computes block item IDs below256 directly and above the threshold through255-id, changes default block state pointer return to reference, and grants ItemDescriptor friendship for block data. Header declarations catch up in43/44.

Changed-file coverage: 2 paths. `include/bedrock/world/level/block/block.h`; `src/endstone_runtime/bedrock/world/level/block/block_legacy.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-043"></a>
### 043. feat: add `Item::getFullNameHash` {#commit-043}

Commit: [472562fe93cb7ff9fe8425e0cec6fff963255353](https://github.com/EndstoneMC/endstone/commit/472562fe93cb7ff9fe8425e0cec6fff963255353) · committed 2025-01-05T23:37:56Z · author Vincent.

Actual parent: `12ca822416cb62539b147d95e6ce9ffc2bb2fe6f`. Full message and parent-relative patch: local source.

Adds hashed full item name accessor and synchronizes BlockLegacy default-state/reference and ID declarations, adding legacy-data state lookup declaration. Bridges the intermediate source/header mismatch.

Changed-file coverage: 3 paths. `include/bedrock/world/item/item.h`; `include/bedrock/world/level/block/block_legacy.h`; `src/endstone_runtime/bedrock/world/item/item.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-044"></a>
### 044. feat: add `InternalItemDescriptor` {#commit-044}

Commit: [144778827a676ea68067f65221c4b0153645c62a](https://github.com/EndstoneMC/endstone/commit/144778827a676ea68067f65221c4b0153645c62a) · committed 2025-01-05T23:38:14Z · author Vincent.

Actual parent: `472562fe93cb7ff9fe8425e0cec6fff963255353`. Full message and parent-relative patch: local source.

Adds InternalItemDescriptor with24-byte size assertion, clone/matching, wildcard aux, block-state canonical comparison, name/NBT/binary serialization and hash composition. ItemEntry holds a raw item pointer extracted from WeakPtr; registry lifetime is assumed, not extended. Adds block constructor and named constants; constructor/getFullName validity assumptions remain.

Changed-file coverage: 4 paths. `include/bedrock/world/item/item_descriptor.h`; `include/bedrock/world/item/registry/item_registry.h`; `src/endstone_devtools/vanilla_data.cpp`; `src/endstone_runtime/bedrock/world/item/item_descriptor.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-045"></a>
### 045. fix: remove incorrect fields in `Json::Value` {#commit-045}

Commit: [24881e235ed01dd09b853ed3ca7c7d0ae6529c00](https://github.com/EndstoneMC/endstone/commit/24881e235ed01dd09b853ed3ca7c7d0ae6529c00) · committed 2025-01-06T00:14:35Z · author Vincent.

Actual parent: `144778827a676ea68067f65221c4b0153645c62a`. Full message and parent-relative patch: local source.

Removes incorrect Json::Value allocation bit and bitfield type, treating all stored CZString objects as owned; simplifies copy/destruction/swap and adds std::string constructor. Size stays16 while internal field representation changes. Further enum-width correction arrives75, showing size alone is insufficient ABI validation.

Changed-file coverage: 2 paths. `include/bedrock/deps/json/value.h`; `src/endstone_runtime/bedrock/deps/json/value.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-046"></a>
### 046. feat: implement ItemDescriptor {#commit-046}

Commit: [23eaf19aff66854e2d01c7722de03ba8c5de19f5](https://github.com/EndstoneMC/endstone/commit/23eaf19aff66854e2d01c7722de03ba8c5de19f5) · committed 2025-01-06T00:14:52Z · author Vincent.

Actual parent: `24881e235ed01dd09b853ed3ca7c7d0ae6529c00`. Full message and parent-relative patch: local source.

Adds descriptor default virtual implementations, Aux NBT persistence and ItemEntry block resolution; exposes ItemStackBase state to subclasses and updates hashes on reset. sameItems ignores its argument and compares against its own getItem(), an observed interim implementation limitation. Several defaults are placeholders (isValid true, resolve null).

Changed-file coverage: 4 paths. `include/bedrock/world/item/item_descriptor.h`; `include/bedrock/world/item/item_stack_base.h`; `src/endstone_runtime/bedrock/world/item/item_descriptor.cpp`; `src/endstone_runtime/bedrock/world/item/item_stack_base.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-047"></a>
### 047. feat: implement `ItemStackBase::_updateCompareHashes` {#commit-047}

Commit: [17f0f15f1a59d7633248ad510a263b042f659e6e](https://github.com/EndstoneMC/endstone/commit/17f0f15f1a59d7633248ad510a263b042f659e6e) · committed 2025-01-06T00:55:58Z · author Vincent.

Actual parent: `23eaf19aff66854e2d01c7722de03ba8c5de19f5`. Full message and parent-relative patch: local source.

Sorts placement/destruction block vectors before hash combining, adds descriptor constructors and default destructor/name, implements registry-based block-state call. Also introduces Cache::get with lock-separated lookup and insertion; source has emplace(...).first.second instead of iterator dereference, so this stage cannot be treated as tested cache code. Factory executes under insertion lock and duplicate misses can still build redundant values.

Changed-file coverage: 5 paths. `include/bedrock/core/container/cache.h`; `include/bedrock/world/item/item_descriptor.h`; `src/endstone_runtime/bedrock/world/item/item_descriptor.cpp`; `src/endstone_runtime/bedrock/world/item/item_stack_base.cpp`; `src/endstone_runtime/bedrock/world/level/block/block_legacy.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-048"></a>
### 048. refactor: use constructors instead of 'ugly' factory method for ItemStack {#commit-048}

Commit: [ea398d24ad56b19f6eb04c7ebad805ba52e39de7](https://github.com/EndstoneMC/endstone/commit/ea398d24ad56b19f6eb04c7ebad805ba52e39de7) · committed 2025-01-06T01:07:16Z · author Vincent.

Actual parent: `17f0f15f1a59d7633248ad510a263b042f659e6e`. Full message and parent-relative patch: local source.

Replaces native ItemStack factory thunks with normal constructors and value-returning conversion, adapting inventory calls to stable locals. Explicit subject calls old factory ugly. Endstone wrapper still owns unique_ptr where needed, while conversion clones by value; non-native item conversion still lacks NBT support. Constructor definitions are intentionally incomplete until subsequent commits.

Changed-file coverage: 6 paths. `include/bedrock/world/item/item_stack.h`; `include/endstone/detail/inventory/item_stack.h`; `src/endstone_core/inventory/inventory.cpp`; `src/endstone_core/inventory/item_stack.cpp`; `src/endstone_devtools/vanilla_data.cpp`; `src/endstone_runtime/bedrock/world/item/item_stack.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-049"></a>
### 049. feat: implement ItemStackNetIdVariant::toString {#commit-049}

Commit: [4925a8b6afb6b7b379cf2c3aa21028bf9938f765](https://github.com/EndstoneMC/endstone/commit/4925a8b6afb6b7b379cf2c3aa21028bf9938f765) · committed 2025-01-06T01:49:12Z · author Vincent.

Actual parent: `ea398d24ad56b19f6eb04c7ebad805ba52e39de7`. Full message and parent-relative patch: local source.

Adds typed server/client network-ID diagnostics and variant visitor naming all three alternatives; variant storage becomes private. Preserves24-byte static size constraint. No runtime protocol behavior change is claimed.

Changed-file coverage: 3 paths. `include/bedrock/world/inventory/network/item_stack_net_id_variant.h`; `src/endstone_runtime/CMakeLists.txt`; `src/endstone_runtime/bedrock/world/inventory/network/item_stack_net_id_variant.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-050"></a>
### 050. feat: implement ItemStack virtual methods {#commit-050}

Commit: [21b2b902a41b656c1e3eba9fb02d6ad9ec86d5eb](https://github.com/EndstoneMC/endstone/commit/21b2b902a41b656c1e3eba9fb02d6ad9ec86d5eb) · committed 2025-01-06T01:49:28Z · author Vincent.

Actual parent: `4925a8b6afb6b7b379cf2c3aa21028bf9938f765`. Full message and parent-relative patch: local source.

Adds ItemStack reinit implementations via temporary/copy assignment, reset of network ID and appended network diagnostics; declares base constructors/copy assignment and defines base destructor. Missing constructor/initialization bodies continue to51/69/70.

Changed-file coverage: 5 paths. `include/bedrock/world/item/item_stack.h`; `include/bedrock/world/item/item_stack_base.h`; `src/endstone_core/inventory/item_stack.cpp`; `src/endstone_runtime/bedrock/world/item/item_stack.cpp`; `src/endstone_runtime/bedrock/world/item/item_stack_base.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-051"></a>
### 051. feat: implement more methods in ItemStackBase {#commit-051}

Commit: [e1a62bb226534265e82c278e8382017af15946e5](https://github.com/EndstoneMC/endstone/commit/e1a62bb226534265e82c278e8382017af15946e5) · committed 2025-01-06T15:51:34Z · author Vincent.

Actual parent: `21b2b902a41b656c1e3eba9fb02d6ad9ec86d5eb`. Full message and parent-relative patch: local source.

Implements native ItemStack constructors and base copy/assignment with cloned user data, placement/destruction hashes and compatibility hook calls; adds charged-item extraction and registry lookup delegation. Copy constructor uses its own count_ instead of rhs.count_, fixed explicitly in77. Assignment only overwrites user_data when rhs has it, so clearing an old tag is not demonstrated. init/compatibility/ItemInstance::fromTag remain undefined here.

Changed-file coverage: 12 paths. `include/bedrock/world/item/item.h`; `include/bedrock/world/item/item_instance.h`; `include/bedrock/world/item/item_stack.h`; `include/bedrock/world/item/item_stack_base.h`; `include/bedrock/world/item/registry/item_registry.h`; `include/bedrock/world/item/registry/item_registry_ref.h`; `src/endstone_runtime/CMakeLists.txt`; `src/endstone_runtime/bedrock/world/item/item_descriptor.cpp`; `include/bedrock/world/item/item_instance.h → src/endstone_runtime/bedrock/world/item/item_instance.cpp`; `src/endstone_runtime/bedrock/world/item/item_stack.cpp`; `src/endstone_runtime/bedrock/world/item/item_stack_base.cpp`; `src/endstone_runtime/bedrock/world/item/registry/item_registry_ref.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-069"></a>
### 069. feat: implement more methods in `ItemStackBase` {#commit-069}

Commit: [af0784d8edd9de328aafd98d0e727f11c44ffd66](https://github.com/EndstoneMC/endstone/commit/af0784d8edd9de328aafd98d0e727f11c44ffd66) · committed 2025-01-08T00:25:31Z · author Vincent.

Actual parent: `32f570321aef1426283b065ae305f78ffd136883`. Full message and parent-relative patch: local source.

Implements ItemStackBase init overloads resolving BlockLegacy permutations, ANY_AUX wildcard, user-data clone, integer ID/count initialization and native _setItem. Required BaseGameVersion copied from block when item requirement EMPTY; BaseGameVersion constructors/equality added. Negative count clamps but uint8 assignment permits positive narrowing. Adds ItemInstance::fromTag native wrapper; Windows symbols. Copy self-test simplified but existing count_ instead rhs.count_ persists until77. Equal-version compatibility implementation follows70.

Changed-file coverage: 13 paths. `src/bedrock/CMakeLists.txt`; `src/bedrock/core/sem_ver/sem_version.h`; `src/bedrock/resources/base_game_version.h → src/bedrock/resources/base_game_version.cpp`; `src/bedrock/resources/base_game_version.h`; `src/bedrock/symbol_generator/symbols.toml`; `src/bedrock/world/item/item.cpp`; `src/bedrock/world/item/item.h`; `src/bedrock/world/item/item_instance.cpp`; `src/bedrock/world/item/item_stack_base.cpp`; `src/bedrock/world/item/item_stack_base.h`; `src/bedrock/world/level/block/block_legacy.cpp`; `src/bedrock/world/level/block/block_legacy.h`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-070"></a>
### 070. feat: implement all undefined methods {#commit-070}

Commit: [2b4fa21574fe4a095c2221873d51df6fd1d7919d](https://github.com/EndstoneMC/endstone/commit/2b4fa21574fe4a095c2221873d51df6fd1d7919d) · committed 2025-01-08T19:00:22Z · author Vincent.

Actual parent: `af0784d8edd9de328aafd98d0e727f11c44ffd66`. Full message and parent-relative patch: local source.

Adds compatibility lock guard and check that nulls incompatible item; mutex optional shared_ptr manually lock/unlock, no explicit copy deletion seen. BaseGameVersion compatibility and SemVersion comparisons/getters added. Despite title all undefined methods, SemVersion::< throws Not implemented when same core version and same prerelease-presence; >/>= declarations no definitions here. Native ServerScoreboard factory temporarily restored; platform constexpr removed but Linux still get_name mismatch. Full diff read; no complete semantic-version compliance claim. Additional exact algorithm boundary: for unequal core versions, operator< compares std::tie(major_, minor_, patch_) to the identical same-object tuple, so that branch returns false rather than ordering against rhs. This is a static code consequence, not a measured runtime failure.

Changed-file coverage: 13 paths. `include/endstone/detail/platform.h`; `src/bedrock/core/sem_ver/sem_version.cpp`; `src/bedrock/core/sem_ver/sem_version.h`; `src/bedrock/resources/base_game_version.cpp`; `src/bedrock/resources/base_game_version.h`; `src/bedrock/symbol.h`; `src/bedrock/world/item/item_stack_base.cpp`; `src/bedrock/world/item/registry/item_registry_ref.cpp`; `src/bedrock/world/item/registry/item_registry_ref.h`; `src/bedrock/world/scores/server_scoreboard.cpp`; `src/endstone/core/crash_handler.cpp`; `src/endstone/core/platform_linux.cpp`. The complete path/object disposition ledger is not distributed; the linked public commit provides the inspectable changed-file history.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-074"></a>
### 074. fix: initialize member variable in `ItemStackBase` {#commit-074}

Commit: [ee3c704494ab9da503660b16139acabf470c29ba](https://github.com/EndstoneMC/endstone/commit/ee3c704494ab9da503660b16139acabf470c29ba) · committed 2025-01-08T23:48:07Z · author Vincent.

Actual parent: `e202af151f11d0d9afdb2ce1a5521c935801dcfd`. Full message and parent-relative patch: local source.

Initializes ItemStackBase item/userdata/block/charged-item pointers and WeakPtr counter to null; restructures weak copy assignment to increment before resetting old ownership and guards self-assignment. SharedPtr reset/destructor now centralize decrement/delete. Broader than title: removes SharedPtr move/copy assignments/reset(ptr)/swap and bool conversion, introduces implicit T* conversion. Implicit generated SharedPtr assignment is a potential shallow-counter hazard; no usage failure proven. Removes obsolete resetPlayerScore export-hook marker.

Changed-file coverage: 4 paths. `src/bedrock/shared_ptr.h`; `src/bedrock/world/item/item_stack_base.cpp`; `src/bedrock/world/item/item_stack_base.h`; `src/bedrock/world/scores/scoreboard.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-075"></a>
### 075. fix: underlying type for Json::ValueType enum should be `char` {#commit-075}

Commit: [52c7ed2aa41f392500c60d79542cd7a4d5bc30c7](https://github.com/EndstoneMC/endstone/commit/52c7ed2aa41f392500c60d79542cd7a4d5bc30c7) · committed 2025-01-09T01:03:27Z · author Vincent.

Actual parent: `ee3c704494ab9da503660b16139acabf470c29ba`. Full message and parent-relative patch: local source.

Explicitly corrects Json::ValueType underlying type to char and numeric enum codes, after45 removed bitfields; total-size alone could not show field ABI correctness. Copy dispatch now switches source type. Devtool recipe extraction tests object for item_tag and otherwise gets full item name, replacing incorrect string-vs-tag branching. No native layout run.

Changed-file coverage: 3 paths. `src/bedrock/deps/json/value.cpp`; `src/bedrock/deps/json/value.h`; `src/endstone/core/devtools/vanilla_data.cpp`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-076"></a>
### 076. fix: correct default locale format in player settings {#commit-076}

Commit: [c98f8a6cddbc298fa74bb7638458daffa6c44887](https://github.com/EndstoneMC/endstone/commit/c98f8a6cddbc298fa74bb7638458daffa6c44887) · committed 2025-01-09T01:08:43Z · author Vincent.

Actual parent: `52c7ed2aa41f392500c60d79542cd7a4d5bc30c7`. Full message and parent-relative patch: local source.

Player settings default locale en-US→en_US. Explicit correctness claim limited to spelling; no locale negotiation or translation test changed.

Changed-file coverage: 1 paths. `src/endstone/core/player.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-077"></a>
### 077. fix: fix `ItemStack` copy constructor with corrected count {#commit-077}

Commit: [de8bdd0f34cdea984f581cff12ad786a9160814b](https://github.com/EndstoneMC/endstone/commit/de8bdd0f34cdea984f581cff12ad786a9160814b) · committed 2025-01-09T01:37:53Z · author Vincent.

Actual parent: `c98f8a6cddbc298fa74bb7638458daffa6c44887`. Full message and parent-relative patch: local source.

Fixes native stack copy constructor using rhs.count_ instead of own initially-zero count_. Separates invalid-deprecated (-1) from valid-but-no-item (0). Public adapter toMinecraft shared_ptr argument becomes const-reference. Repair confirms risk in51/69 rather than claiming original refactor preserved behavior.

Changed-file coverage: 4 paths. `src/bedrock/world/item/item_stack.cpp`; `src/bedrock/world/item/item_stack_base.cpp`; `src/endstone/core/inventory/item_stack.cpp`; `src/endstone/core/inventory/item_stack.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.


<a id="commit-097"></a>
### 097. feat: add comparison operators and hash specialization for BlockPos {#commit-097}

Commit: [16a1a1856a1ab6de37aeff59fcf968849953afdd](https://github.com/EndstoneMC/endstone/commit/16a1a1856a1ab6de37aeff59fcf968849953afdd) · committed 2025-01-11T21:55:08Z · author Vincent.

Actual parent: `90b65613f83b3d2ae0be35971840140b642d4229`. Full message and parent-relative patch: local source.

BlockPos equality/inequality compare three coordinates; hash combines per-axis int hashes using standard boost-like mix. Supports unordered_set use for explosion positions. Constructor reorder and ZERO location mechanical. No collision/performance test.

Changed-file coverage: 1 paths. `src/bedrock/world/level/block_pos.h`.

Evidence boundary: the commit message above supplies the explicit stated goal; additional rationale in the review is inference unless identified as a source comment. No upstream execution or runtime result is claimed.
