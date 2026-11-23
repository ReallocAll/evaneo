<!-- retrieval: {"source_ids":["public:commit:02325754285fd9677789065c9acd7daf223f9d86","public:commit:0499a1cd28b76e15ca8c52edda9f196f6da7bf65","public:commit:0637efabbc4e884d19c6dabad2b6b7512d6bd247","public:commit:16f5c467dc74f63d2d01a6fd9bfc06ae03b7761f","public:commit:243de3210080267157ddb6beba11f3edfaa1d800","public:commit:2711ea9ed5e59b7cb2095779640f1ee6bceb1c2b","public:commit:39c9aa048212845d7a32785cf7dbed11485b7123","public:commit:4443170369ffa8f008ba3e4c7e5eca92fc0f21dd","public:commit:5112b81e011cb0485b2450ee06cb12e8121c6726","public:commit:54cd471871f606ebec5cc98d2ed7a6e4493c9d8c","public:commit:5d334542569155483fcc1eb2bd9b7e9d2f17ed3e","public:commit:5d7e029c218d7ca004268b13c081bd2ac854799f","public:commit:6101f5de64d8a9d5e08cc9d8153ef467314df4cc","public:commit:7294b5c03c161683c1740f791f57f9cb5a8b79d0","public:commit:738ef6cb197cd0aa090dddcab3468436a1c4e501","public:commit:7bd19f862a8c2e3ce582ac3a3e096c190b872be6","public:commit:be899b9e4d6e17ffb3a6653cd082717df28508bf","public:commit:bf38fb78315279926f3bce4848b26f7fcee67f4f","public:commit:c3353a134aaabbb87339253e77ef4e643eeb35a0","public:commit:d2d90d2e9a2c6eed5261ed413f97bfcc29c12ff7","public:commit:d7f614d9d91129a33ae7a1ce3d99cd649a119c1a","public:commit:d97478442dda52d39d5cc64f3d0c0d7918ed062c","public:commit:d9a79b21a731887df7f63808d52ef2a38cd43bc9","public:commit:e28db2bd904d9400e1b2572b535e47a2ee42d7fc","public:commit:fd542c6585a82a4a34974f82a03e4cec8b4420ea","public:commit:fdd317988593d3178bccd526bd315213544e757b"],"source_type":"public","date":"2024-05-18..2024-06-04","topics":["lifetime","ffi","testing","build","performance","review","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native mirrors: collaborator knowledge, semantic corrections and verified file movement {#native-mirrors-collaborator-knowledge-semantic-corrections-and-verified-file-movement}

## Types and names carry ABI claims {#types-and-names-carry-abi-claims}

This family contains both genuine organization-only work and substantive reconstruction hidden under refactor/style titles. Native Dimension removes enable_shared_from_this in967 and restores it in1050. ActorOwnerComponent changes from raw pointer to unique_ptr in1050, while its accessor changes to get(). CommandRegistry gains typed vectors, function objects, enum kinds and named fields in1048. ServerInstance gains a chrono type in1049; LevelSettings needs a Linux size correction in1054. These are native representation assumptions, not cosmetic naming choices, and no native host execution validates them in this review.

NonOwnerPointer is a cautionary naming example. Its local reference constructor initializes shared_ptr from a raw address using the default deleter; EnableNonOwnerReferences uses that constructor on itself. The aliasing cast preserves a control block but does not change its deletion policy. A native object whose control block is constructed by the host may have different semantics, so the evidence supports a bounded concern about local construction, not a claim that every existing server object is double-deleted. The full final header was inspected.

There are several intentionally staged interfaces: AABB access precedes filling its component, an ability include is corrected in the following commit, and1065 adds a MapDataManager header that1066 replaces with a forward declaration. These should remain chronological integration facts rather than being interpreted as successful compile/test outcomes. Removing a size assertion in1050 also reduces one source-level check; it does not prove either incompatibility or correctness.

## Collaborator attribution is recoverable from the DAG {#collaborator-attribution-is-recoverable-from-the-dag}

1040 merges PR11 from Duckos-Mods. Five branch commits independently name HashedString's cached match, observer subjects and CommandOrigin identity, then map Packet fields and fix include separators. The NetworkPeer comment explicitly says its class form preserves name mangling. Packet priority/reliability/compressibility and receive time become meaningful types; default initializers from the opaque fields disappear. This is collaborator-supplied host knowledge, with integration naming/moves by Vincent in1041. Changelog1045 explicitly credits Duckos.

At1040 the branches are disjoint: the second parent contributes1039's Python resource-anchor fix, while the first parent imports the native structure work.1043 reproduces its second parent without additional resolution changes. Duckos' six branch commits retain their own source history, including the include-path repair, rather than being reduced to the merged net change.

The log switch preserves the1/2/4/8 mapping and Critical fallback, with no benchmark.1044's style pass narrows to uint8_t, so unusual high-bit values can differ from the original uint32_t interpretation;1065 subsequently takes an explicit uint32_t priority and removes that narrowing. This is a small but useful counterexample to title-based noise filtering and to treating a contributor's implementation as frozen after merge.

## Semantic discriminators and native hooks {#semantic-discriminators-and-native-hooks}

1079 replaces the heuristic max_num_players>0 with PeerPurpose::Gameplay when selecting the started RakNet peer. The duplicate-peer check and startup-success requirement remain. This is a concrete move from a proxy signal to an explicit host discriminator, not a general assertion that heuristics are always wrong. StartGamePacket layout and Linux repairs support the seed-hiding hook discussed in the deployment dossier; these files are not independent evidence of a complete packet implementation.1047's listed virtual methods are commented, so they do not change the compiled vtable.

## Relocation is verified without erasing source identity {#relocation-is-verified-without-erasing-source-identity}

1059–1064 reorganize command, packet, server, entity, core, locale and world paths. Exact moved blobs receive identity-based reuse; nonidentical files' include and declaration differences were read. Public native include paths still change, even if execution bodies do not. Tests receive an include update for the UUID relocation rather than new behavioral assertions.

1064 is particularly unsuitable for trusting Git similarity alone: it reports a rename from IDataOutput to Color because shared header material dominates a small file. Actual reading shows Color extracted from mce.h, IDataInput and IDataOutput merged into data_io.h, and ownership helpers split between memory and non_owner_pointer. The cross-file-body artifact verifies those actual origins. All1301 raw display lines were read in three complete pages. Canonical no-renames hashes preserve every path/blob/hunk, while rename-aware reading avoids pretending a large copied block is new behavior. A hash match proves identity, not independent engineering authorship or an aggregate PR-range match.

## Applicability and limits {#applicability-and-limits}

Use this family to audit mixed refactors, reconstruct native ABI assumptions, credit outside layout discoveries, compare semantic and heuristic selectors, or verify large reorganizations without rereading identical content. The scope is historical source inspection. No binary reverse-engineering session, build, native hook execution or performance measurement occurred. Assertions and comments are evidence of the encoded assumptions; runtime truth remains unverified.


## Individual commit dispositions {#individual-commit-dispositions}


<a id="commit-963"></a>
### 963: feat: add CommandOriginIdentity {#commit-963}

Source: [e28db2bd904d9400e1b2572b535e47a2ee42d7fc](https://github.com/EndstoneMC/endstone/commit/e28db2bd904d9400e1b2572b535e47a2ee42d7fc). Authored 2024-05-18T23:24:17Z; Git author Vincent. Disposition: abi_scaffold.

Models CommandOriginIdentity as two strings still called unknown1/unknown2. The size/shape is useful before semantic names are known; Duckos-Mods supplies XUID/platform identity names in1040. Do not attribute those later names to this initial scaffold.


<a id="commit-967"></a>
### 967: fix: Dimension base classes {#commit-967}

Source: [0637efabbc4e884d19c6dabad2b6b7512d6bd247](https://github.com/EndstoneMC/endstone/commit/0637efabbc4e884d19c6dabad2b6b7512d6bd247). Authored 2024-05-19T03:34:06Z; Git author Vincent. Disposition: abi_revision.

Removes native Dimension’s enable_shared_from_this base and adds a WeakRef member. This changes reconstructed layout/ownership representation, not just formatting.1050 explicitly restores the base and removes the member; no reason for either layout reversal is stated beyond the changed declarations.


<a id="commit-968"></a>
### 968: fix: ILevel should inherit from Bedrock::EnableNonOwnerReferences {#commit-968}

Source: [738ef6cb197cd0aa090dddcab3468436a1c4e501](https://github.com/EndstoneMC/endstone/commit/738ef6cb197cd0aa090dddcab3468436a1c4e501). Authored 2024-05-19T03:34:31Z; Git author Vincent. Disposition: abi_revision.

Makes ILevel derive from EnableNonOwnerReferences and marks its destructor override. This aligns the non-owner pointer path used by the command factory. It does not establish native Level ownership or justify deleting a host-owned object.


<a id="commit-969"></a>
### 969: feat: add AABB and Actor::getAABB {#commit-969}

Source: [243de3210080267157ddb6beba11f3edfaa1d800](https://github.com/EndstoneMC/endstone/commit/243de3210080267157ddb6beba11f3edfaa1d800). Authored 2024-05-19T04:02:54Z; Git author Vincent. Disposition: incremental_scaffold.

Adds AABB min/max and Actor::getAABB through its built-in AABB component. The component is still empty in this intermediate snapshot;973 completes its AABB member. A commit’s feature title does not prove that the isolated snapshot compiles.


<a id="commit-970"></a>
### 970: feat: add BlockPos constructors {#commit-970}

Source: [39c9aa048212845d7a32785cf7dbed11485b7123](https://github.com/EndstoneMC/endstone/commit/39c9aa048212845d7a32785cf7dbed11485b7123). Authored 2024-05-19T04:03:08Z; Git author Vincent. Disposition: implementation.

Adds BlockPos construction from double/float coordinates by flooring each component. Negative fractional positions therefore round downward rather than toward zero. This is a deliberate conversion semantic visible in code; no boundary tests are added.


<a id="commit-971"></a>
### 971: feat: improve Bedrock::EnableNonOwnerReferences and Bedrock::NonOwnerPointer {#commit-971}

Source: [4443170369ffa8f008ba3e4c7e5eca92fc0f21dd](https://github.com/EndstoneMC/endstone/commit/4443170369ffa8f008ba3e4c7e5eca92fc0f21dd). Authored 2024-05-19T04:03:29Z; Git author Vincent. Disposition: ownership_boundary.

Adds NonOwnerPointer construction from a reference and an aliasing static_pointer_cast; EnableNonOwnerReferences initializes its pointer from itself. The local constructor uses shared_ptr(&obj) with its default deleter, despite the non-owner name. Existing native objects may have different host-created control blocks, so the bounded concern is local construction/destruction semantics, not a demonstrated server lifetime failure.


<a id="commit-973"></a>
### 973: feat: improve AABBShapeComponent {#commit-973}

Source: [02325754285fd9677789065c9acd7daf223f9d86](https://github.com/EndstoneMC/endstone/commit/02325754285fd9677789065c9acd7daf223f9d86). Authored 2024-05-19T04:04:44Z; Git author Vincent. Disposition: scaffold_completion.

Fills AABBShapeComponent with its AABB field, completing969’s accessor assumption. No new collision algorithm or bounding-box mutation is implemented.


<a id="commit-1040"></a>
### 1040: Merge pull request #11 from Duckos-Mods/StructFixing {#commit-1040}

Source: [d97478442dda52d39d5cc64f3d0c0d7918ed062c](https://github.com/EndstoneMC/endstone/commit/d97478442dda52d39d5cc64f3d0c0d7918ed062c). Authored 2024-05-24T14:25:19Z; Git author Vincent (Zhengyu) Wu. Disposition: collaborative_merge.

Merges PR11 from Duckos-Mods: names HashedString’s cached match and CommandOrigin identity strings, documents observer subject pointers, defines packet priority/reliability/compressibility and maps Packet fields. The branch explicitly preserves class-based name mangling and repairs Windows-style include separators before merge. Packet default initializers are removed in the reconstruction. Both parents and all five branch commits are read; disjoint-path tree proof establishes no extra conflict-resolution code. Credit belongs to the contributor for the mapped structures.


<a id="commit-1041"></a>
### 1041: style: code formatting {#commit-1041}

Source: [0499a1cd28b76e15ca8c52edda9f196f6da7bf65](https://github.com/EndstoneMC/endstone/commit/0499a1cd28b76e15ca8c52edda9f196f6da7bf65). Authored 2024-05-24T14:35:26Z; Git author Vincent. Disposition: integration_style.

Normalizes the contributed member names to snake_case, moves enum headers to protocol/raknet, fixes includes and cleans formatting/comments. These are project integration conventions applied to Duckos-Mods’ work, not evidence Vincent independently discovered the layouts. Public native-header paths/member names do change, even without a new runtime algorithm.


<a id="commit-1043"></a>
### 1043: Merge pull request #12 from Duckos-Mods/main {#commit-1043}

Source: [2711ea9ed5e59b7cb2095779640f1ee6bceb1c2b](https://github.com/EndstoneMC/endstone/commit/2711ea9ed5e59b7cb2095779640f1ee6bceb1c2b). Authored 2024-05-25T16:09:03Z; Git author Vincent (Zhengyu) Wu. Disposition: collaborative_merge.

Merges PR12 from Duckos-Mods, replacing a four-entry static logging hashmap with a switch over1/2/4/8 and Critical fallback. The merge tree is exactly the contributor’s parent tree; no independent resolution delta exists. No performance measurement accompanies this observed alternative.


<a id="commit-1044"></a>
### 1044: style: code formatting {#commit-1044}

Source: [c3353a134aaabbb87339253e77ef4e643eeb35a0](https://github.com/EndstoneMC/endstone/commit/c3353a134aaabbb87339253e77ef4e643eeb35a0). Authored 2024-05-26T00:59:33Z; Git author Vincent. Disposition: integration_revision.

Restyles the contributed switch, puts Critical in default and casts to uint8_t rather than uint32_t. For the four recognized values behavior is unchanged, but high bits of other priorities can be truncated, so this is not completely semantics-free formatting.1065 later takes uint32_t priority directly and removes this narrowing.


<a id="commit-1046"></a>
### 1046: feat: add LevelSettings and LevelSeed64 {#commit-1046}

Source: [5d7e029c218d7ca004268b13c081bd2ac854799f](https://github.com/EndstoneMC/endstone/commit/5d7e029c218d7ca004268b13c081bd2ac854799f). Authored 2024-05-26T03:05:25Z; Git author Vincent. Disposition: abi_prerequisite.

Adds a64-bit LevelSeed and minimal LevelSettings seed get/set representation. This becomes the StartGamePacket seed-redaction hook’s target in1051. It is not a world-generation algorithm.


<a id="commit-1047"></a>
### 1047: refactor: move MinecraftPacketIds into minecraft_packet_ids.h {#commit-1047}

Source: [5d334542569155483fcc1eb2bd9b7e9d2f17ed3e](https://github.com/EndstoneMC/endstone/commit/5d334542569155483fcc1eb2bd9b7e9d2f17ed3e). Authored 2024-05-26T03:05:51Z; Git author Vincent. Disposition: abi_scaffold.

Separates packet IDs and declares Text=9; adds commented-out packet virtual signatures and BinaryStream forwarding. Commented declarations do not modify the actual vtable. Later packet relocation preserves these distinctions.


<a id="commit-1048"></a>
### 1048: refactor: members in CommandRegistry {#commit-1048}

Source: [7bd19f862a8c2e3ce582ac3a3e096c190b872be6](https://github.com/EndstoneMC/endstone/commit/7bd19f862a8c2e3ce582ac3a3e096c190b872be6). Authored 2024-05-26T03:52:32Z; Git author Vincent. Disposition: abi_reconstruction.

Replaces several opaque command-registry fields with typed containers/functions, gives overload/version/signature fields names, adds runnable state, and replaces parameter-kind integers with an enum propagated into command registration. Registry size assertions remain. This is substantive native layout/type work despite the broad refactor label, not just a local variable rename.


<a id="commit-1049"></a>
### 1049: refactor: rename members {#commit-1049}

Source: [d2d90d2e9a2c6eed5261ed413f97bfcc29c12ff7](https://github.com/EndstoneMC/endstone/commit/d2d90d2e9a2c6eed5261ed413f97bfcc29c12ff7). Authored 2024-05-26T04:08:35Z; Git author Vincent. Disposition: mixed_refactor.

Renames connection/chat/event/saved-data fields and updates consumers; ServerInstance’s opaque slot becomes a chrono time_point. Most control flow is unchanged, but type reconstruction and field meanings carry ABI assumptions beyond formatting.


<a id="commit-1050"></a>
### 1050: refactor: rename members {#commit-1050}

Source: [fdd317988593d3178bccd526bd315213544e757b](https://github.com/EndstoneMC/endstone/commit/fdd317988593d3178bccd526bd315213544e757b). Authored 2024-05-26T05:09:09Z; Git author Vincent. Disposition: mixed_ownership_refactor.

Renames command context/version/output, actor/network/tick fields and rewires consumers, while also changing ActorOwnerComponent from raw Actor* to unique_ptr, restoring Dimension’s enable_shared_from_this base and removing its WeakRef member, and changing several opaque types. Removes a MinecraftCommands size assertion. These ownership/layout changes make the commit substantive even though its title emphasizes member renaming; no host binary validation accompanies it.


<a id="commit-1053"></a>
### 1053: fix: compilation error on Linux {#commit-1053}

Source: [6101f5de64d8a9d5e08cc9d8153ef467314df4cc](https://github.com/EndstoneMC/endstone/commit/6101f5de64d8a9d5e08cc9d8153ef467314df4cc). Authored 2024-05-26T14:15:47Z; Git author Vincent. Disposition: platform_fix.

Repairs Linux compilation of StartGamePacket’s reconstructed item-data region by using vector<void*> instead of an incomplete ItemData type. This is an opaque layout placeholder, not a complete inventory model or evidence of native payload validation.


<a id="commit-1054"></a>
### 1054: fix: correct LevelSetting size for Linux {#commit-1054}

Source: [54cd471871f606ebec5cc98d2ed7a6e4493c9d8c](https://github.com/EndstoneMC/endstone/commit/54cd471871f606ebec5cc98d2ed7a6e4493c9d8c). Authored 2024-05-26T14:45:49Z; Git author Vincent. Disposition: layout_correction.

Corrects Linux LevelSettings padding/size from1072 to1024 and updates offset comments; Windows remains1248. Also replaces an unnecessary move of a trivial seed value with a copy. Platform-specific layout correction is substantive; no runtime layout test is executed.


<a id="commit-1059"></a>
### 1059: refactor: move command headers to bedrock/server/commands {#commit-1059}

Source: [be899b9e4d6e17ffb3a6653cd082717df28508bf](https://github.com/EndstoneMC/endstone/commit/be899b9e4d6e17ffb3a6653cd082717df28508bf). Authored 2024-05-27T08:20:56Z; Git author Vincent. Disposition: verified_relocation.

Moves command interfaces/runtime implementations under server/commands and standard command paths, updates all includes and adds the missing CommandPermission include. Exact unchanged file moves are blob-verified; include-only edits are read separately. No new command execution algorithm is introduced, but native include consumers must follow the new paths.


<a id="commit-1060"></a>
### 1060: refactor: move minecraft.h to bedrock/world {#commit-1060}

Source: [7294b5c03c161683c1740f791f57f9cb5a8b79d0](https://github.com/EndstoneMC/endstone/commit/7294b5c03c161683c1740f791f57f9cb5a8b79d0). Authored 2024-05-27T08:25:21Z; Git author Vincent. Disposition: verified_relocation.

Moves Minecraft to the world path and rewires its includes/runtime location. The full diff was reread after an initially truncated combined display. Exact blob moves and include edits are distinguished; no runtime behavior change is inferred.


<a id="commit-1061"></a>
### 1061: refactor: move network packets to bedrock/network/packet {#commit-1061}

Source: [d9a79b21a731887df7f63808d52ef2a38cd43bc9](https://github.com/EndstoneMC/endstone/commit/d9a79b21a731887df7f63808d52ef2a38cd43bc9). Authored 2024-05-27T08:27:14Z; Git author Vincent. Disposition: verified_relocation.

Moves packet headers and runtime files into network/packet and changes includes. The full diff was reread after truncation. Relocation does not independently strengthen packet correctness or seed-hiding behavior.


<a id="commit-1062"></a>
### 1062: refactor: move network headers to bedrock/network {#commit-1062}

Source: [16f5c467dc74f63d2d01a6fd9bfc06ae03b7761f](https://github.com/EndstoneMC/endstone/commit/16f5c467dc74f63d2d01a6fd9bfc06ae03b7761f). Authored 2024-05-27T08:35:59Z; Git author Vincent. Disposition: verified_relocation.

Flattens protocol/network locations, moves certificate and inventory-network types and updates includes, with a packet-ID final newline. Exact moves and include-only differences are verified; no new authentication/network behavior follows from directory names.


<a id="commit-1063"></a>
### 1063: refactor: move ServerLevel and ServerPlayer to bedrock/server {#commit-1063}

Source: [bf38fb78315279926f3bce4848b26f7fcee67f4f](https://github.com/EndstoneMC/endstone/commit/bf38fb78315279926f3bce4848b26f7fcee67f4f). Authored 2024-05-27T08:39:15Z; Git author Vincent. Disposition: verified_relocation.

Flattens ServerLevel/ServerPlayer and moves movement/syncher headers under actor with include updates. The underlying definitions are preserved where blobs match; this is structural organization with source-include compatibility implications.


<a id="commit-1064"></a>
### 1064: refactor: move headers {#commit-1064}

Source: [d7f614d9d91129a33ae7a1ce3d99cd649a119c1a](https://github.com/EndstoneMC/endstone/commit/d7f614d9d91129a33ae7a1ce3d99cd649a119c1a). Authored 2024-05-27T09:33:01Z; Git author Vincent. Disposition: structural_reorganization.

Reorganizes core memory/math/utility, entity, locale, events and world headers and all consumers/tests. Splits mce into UUID and Color, merges IDataInput/Output into data_io and separates non-owner pointers from memory. Git’s rename heuristic falsely pairs old IDataOutput with new Color; manual content reading and cross-file body proofs identify the real origins. Full1301-line display read in three pages; no semantics are inferred from similarity scores alone.


<a id="commit-1065"></a>
### 1065: refactor: rename parameters {#commit-1065}

Source: [5112b81e011cb0485b2450ee06cb12e8121c6726](https://github.com/EndstoneMC/endstone/commit/5112b81e011cb0485b2450ee06cb12e8121c6726). Authored 2024-05-28T12:18:58Z; Git author Vincent. Disposition: mixed_refactor.

Names command suppression and Xbox-live parameters, expands SubClientId values and changes logging to an explicit uint32_t priority, eliminating1044’s narrow cast. Also types ILevel’s MapDataManager accessor but adds a header not present in the tree;1066 replaces it with a forward declaration. This is more than parameter renaming and contains an intermediate compile-surface gap.


<a id="commit-1079"></a>
### 1079: feat: add enum PakPeerHelper::PeerPurpose {#commit-1079}

Source: [fd542c6585a82a4a34974f82a03e4cec8b4420ea](https://github.com/EndstoneMC/endstone/commit/fd542c6585a82a4a34974f82a03e4cec8b4420ea). Authored 2024-06-04T05:09:56Z; Git author Vincent. Disposition: semantic_discriminator.

Defines RakPeerHelper::PeerPurpose and selects the gameplay peer using purpose==Gameplay instead of max_num_players>0. This replaces an indirect capacity heuristic with the host’s explicit semantic discriminator while retaining startup success and duplicate-registration checks. No network test is run.
