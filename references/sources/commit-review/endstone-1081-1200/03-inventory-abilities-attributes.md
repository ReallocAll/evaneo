<!-- retrieval: {"source_ids":["public:commit:10eb28f05f70194fa7cc1b520089d2853e375684","public:commit:1ba324c7d8f100812002029611a4c8c3b21684be","public:commit:1c4a6d1ebbf26624edfd240edd6f906aab50295e","public:commit:21503748a9c0bae879f5327b77eefbd817620197","public:commit:2cd6cedd74b3347dbd5cd63866421941df495ab5","public:commit:3280891a28602c09d5c05173b7f476288660622b","public:commit:335141b0b3dbcaf4f472bfd7a686efcbc4069b33","public:commit:3ffde7d36e45f1363fb5a5650733353e569016cc","public:commit:44ff6c3883840e3f61927652e25a368e381e33b1","public:commit:465505e74633435c786b9491b70ce4632472e2ae","public:commit:576ca1dac57dbbee29fea8aabc2986d349ed8d48","public:commit:656b996078fee9ad2f0e17f178c3a9e18ce23ed9","public:commit:7edfa7479263bdd9bc4e0618b1ba8cae374f9f44","public:commit:82994a3a8d42945b63810e93d4e1bf776aefbd0b","public:commit:89b7cb47306b7cd830daf0c25ff299d5e38db60a","public:commit:978f34e4c092799cfcb7f14a3ac2ca72f431215f","public:commit:980552f19309ea0b2f0cabfd535bffb03810e191","public:commit:9c81b5ca12ba3dd8816b668e53550742d7ea04f6","public:commit:a7f9c79003d4e6194488aa60d2fa956ed97baa0b","public:commit:a97078944b37c72d71c26abf94135ad5f822dcac","public:commit:b20a9f9e9952c0c23c241a269f5509ad18a86058","public:commit:b570154d8edc80d57cadec7aa039a5eaee284fd2","public:commit:b94b6d3f4382854450af4e9929edce58afb48763","public:commit:c096b5d8e43b6b9f0a7a3e30f26035190b0a1181","public:commit:c5ed6a3e7d374fc1d19671fa3f52a0fd15a03134","public:commit:c8ca5d700475ad2d590b991eb9e2e1bf63097c30","public:commit:cbea2be3e83ee9ac49eb3db720c5338e9cfb1ea1","public:commit:cf93bac5b48e784b2750fbba190a8fbbb226155e","public:commit:d774af2a6152bc141246ef2ed15f9f4d3985a32d","public:commit:da1707f3ea54e06c07583c390055e29897d5072c","public:commit:e80452ed02c5452a2772c5be019becc86a8ceeb1","public:commit:e9aeeeae953b126d6a09966cc761406801c85ea8","public:commit:fe38940ab84a9524837df131c716736d1478343d"],"source_type":"public","date":"2024-06-08..2024-06-17","topics":["lifetime","ffi","testing","performance","api","review","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Inventory adapters, flight synchronization and attribute interoperability {#inventory-adapters-flight-synchronization-and-attribute-interoperability}

## An API can be staged before it is usable {#an-api-can-be-staged-before-it-is-usable}

Inventory grows through several intentionally small changes: abstract size/max-stack interfaces, namespace/access corrections, implementation wrappers, native getInventory/Container modeling, constructor initialization and Python exposure. The historical intermediate states include TODO zero results, an uninitialized unique_ptr and an invalid extra class qualification. The final basic adapter uniquely belongs to EndstonePlayer and borrows the native Container by reference. Multiple inheritance from EndstoneInventory and PlayerInventory is resolved with explicit forwarding overrides. A virtual public destructor follows. Python returns a reference; this review does not infer automatic player/container lifetime extension. The advertised inventory scope mentions armor/extra slots, but this chunk exposes only size and max-stack-size, not item access, mutation, transactions or validation.

That chain is useful for distinguishing interface availability from completed behavior and for tracking ownership separately for wrapper and host object. It does not prove every intermediate commit builds. The native Container vtable is updated again during the 1.21 port; a wrapper can be logically correct and still dispatch through the wrong native slot if the representation is stale.

## Flight spans representation, layered policy and client state {#flight-spans-representation-layered-policy-and-client-state}

The initial isFlying correction makes the Ability tag/options enums byte-sized and removes type guards from raw union access. AbilitiesIndex/Layer widths are corrected separately. Actual flight and permission-to-fly are distinct indices. Layer resolution scans descending priority until a set value; setters write the Base layer. Thus changing Base need not override Spectator/Commands/Editor layers. This is a visible constraint of the implementation, not an inferred promise that plugins always win over native state.

Public flight setters first mutate host abilities with TODO synchronization. The sequence then adds packet IDs, layer iteration, the UpdateAbilitiesPacket representation and SerializedAbilitiesData. Serialization copies player identity and permissions, skips empty layers and preserves set/value bitmasks and float speeds. All 19 current indices fit the 32-bit masks. Two immediate corrections are essential: creating an UpdateAbilitiesPacket rather than a Text packet before casting, and clearing Flying only when a currently flying player loses MayFly. The final code resends full layered state after each accepted change; it logs/returns when trying to set Flying while flight is not allowed. Even setting false goes through that allow-flight check. There is no measured client synchronization or higher-layer test here.

The documented chronological sequence has temporary missing declarations/headers. These do not justify collapsing the commits into a fictional atomic implementation. Every SHA retains a disposition, while the family explains the coherent final path and what the fixes corrected. No source title is treated as proof of success.

## Experience bridges an existing native attribute registry {#experience-bridges-an-existing-native-attribute-registry}

Giving experience/levels initially delegates to host virtuals rather than reimplementing leveling arithmetic. Reading them later requires AttributesComponent, host Attribute metadata/instances, a singleton AttributeCollection and map lookups. Public exp means fractional progress toward the next level, not total accumulated points. Native getters cache pointers to two named attributes and read current-value fields. They rely on registry availability and do not guard a failed name lookup before dereference; BaseAttributeMap's later explicit invalid-ID error occurs after that boundary. The pointer is borrowed from the host, not allocated by the plugin-facing getter.

HashedString demonstrates the hidden interoperability requirement. Using std::hash<string> for a structurally correct key fails to establish equivalence with an existing native unordered_map. 1199 replaces it with explicit multiply-then-XOR 64-bit hashing and known attribute-name outputs. The algorithm's multiply-before-XOR order matters. The five GoogleTest assertions are concrete test-source evidence, not a claim tests ran. Empty input returns zero. Equality first compares the stored hash then text, with a reciprocal cached match optimization. Copy/move/assignment reset this object's cache, but ordinary constructors leave the pointer without a default initializer and the shown assignment does not invalidate another object's reciprocal pointer. These visible limits prevent turning the fix into a blanket recommendation to copy this value type. Further audit is outside this assignment.

AttributeInstance evolves from empty scaffold to abstract layout model to concrete default-destructor representation; BaseAttributeMap changes at() to an explicit find/error message. Windows component hash checks are retained. No general public attribute registry API is delivered in this scope, and no current native ABI was tested.

## Evidence and applicability {#evidence-and-applicability}

Useful demand families include staged API design, borrowed lifetimes across pybind, native type-size/identity invariants, layered permission/state mutation, serialization synchronization and hash compatibility with externally owned containers. Alternatives are the actual preceding code: zero stub vs native forwarding, local-only state vs packet resend, aggregate sentinel construction vs explicit constructors (ABI dossier), standard hash vs explicit host-compatible hash, generic at() error vs explicit message. Reasons not stated in source stay unknown. No unit/build/native tests or upstream code were run.

## Commit-by-commit dispositions {#commit-by-commit-dispositions}

<a id="commit-1110"></a>
### 1110: feat: add basic inventory interface {#commit-1110}

Source: [e9aeeeae953b126d6a09966cc761406801c85ea8](https://github.com/EndstoneMC/endstone/commit/e9aeeeae953b126d6a09966cc761406801c85ea8) · 2024-06-08T20:44:44Z · staging

Adds the first Inventory/PlayerInventory interfaces with size and max-stack getters and a Player inventory contract. Initial classes are outside endstone and lack public access specifiers; this is incomplete scaffolding, not a ready item-management API.

<a id="commit-1111"></a>
### 1111: feat: add Player::getInventory {#commit-1111}

Source: [1c4a6d1ebbf26624edfd240edd6f906aab50295e](https://github.com/EndstoneMC/endstone/commit/1c4a6d1ebbf26624edfd240edd6f906aab50295e) · 2024-06-08T20:59:14Z · staging

Moves inventory interfaces into endstone and creates EndstoneInventory/EndstonePlayerInventory wrappers with multiple inheritance and a unique_ptr member on EndstonePlayer. At this stage getters return TODO zeros and the player inventory pointer is not initialized. The following native Container/accessor work completes only these basic reads.

<a id="commit-1112"></a>
### 1112: feat: add Player::getInventory {#commit-1112}

Source: [44ff6c3883840e3f61927652e25a368e381e33b1](https://github.com/EndstoneMC/endstone/commit/44ff6c3883840e3f61927652e25a368e381e33b1) · 2024-06-08T21:08:55Z · staging

Adds a native Player::getInventory detour, empty Container declaration and matching manifest offsets. The in-class declaration has an extra Player:: qualification, corrected by 1118. No item mutation implementation is present.

<a id="commit-1113"></a>
### 1113: feat: add Container {#commit-1113}

Source: [fe38940ab84a9524837df131c716736d1478343d](https://github.com/EndstoneMC/endstone/commit/fe38940ab84a9524837df131c716736d1478343d) · 2024-06-08T21:22:38Z · substantive

Models the initial Container virtual interface through size and max-stack-size, including listener, add/remove/drop operations needed to keep vtable positions. The trailing model is deliberately incomplete. These native declarations support wrapper calls rather than exposing all operations to plugins.

<a id="commit-1114"></a>
### 1114: feat: add basic implementation of Inventory {#commit-1114}

Source: [2cd6cedd74b3347dbd5cd63866421941df495ab5](https://github.com/EndstoneMC/endstone/commit/2cd6cedd74b3347dbd5cd63866421941df495ab5) · 2024-06-08T21:23:29Z · substantive

Makes inventory methods public, borrows Container by reference, forwards size/max-stack values and initializes a uniquely owned EndstonePlayerInventory wrapper in the player constructor. Explicit overrides resolve the two inventory inheritance routes. Ownership is of the adapter, not the native inventory; the host container must outlive it.

<a id="commit-1115"></a>
### 1115: feat: add python bindings for inventory {#commit-1115}

Source: [d774af2a6152bc141246ef2ed15f9f4d3985a32d](https://github.com/EndstoneMC/endstone/commit/d774af2a6152bc141246ef2ed15f9f4d3985a32d) · 2024-06-08T21:40:19Z · api_change

Adds Inventory's virtual destructor, Inventory/PlayerInventory Python classes and Player.inventory with reference return policy, plus public module exports/stubs. The exposed surface still consists only of size and max_stack_size. A Python reference is not made an independent owner or lifetime keeper of the player/container.

<a id="commit-1118"></a>
### 1118: fix: compilation error due to extra qualification {#commit-1118}

Source: [576ca1dac57dbbee29fea8aabc2986d349ed8d48](https://github.com/EndstoneMC/endstone/commit/576ca1dac57dbbee29fea8aabc2986d349ed8d48) · 2024-06-08T21:51:28Z · corrective

Removes the extra Player:: qualification from the in-class getInventory declaration, explicitly fixing a compile error. This closes the syntax defect introduced in 1112; no runtime behavior changes.

<a id="commit-1147"></a>
### 1147: refactor: Ability::Type and Ability::Options {#commit-1147}

Source: [335141b0b3dbcaf4f472bfd7a686efcbc4069b33](https://github.com/EndstoneMC/endstone/commit/335141b0b3dbcaf4f472bfd7a686efcbc4069b33) · 2024-06-14T22:09:36Z · mechanical

Renames Ability enum labels NotSet to Unset and Options::Default to None, adjusting the layered lookup comparison. Values and lookup strategy are unchanged; width corrections follow separately.

<a id="commit-1148"></a>
### 1148: fix: Player::isFlying sometimes always returns false due to the incorrect base type of Ability::Type {#commit-1148}

Source: [7edfa7479263bdd9bc4e0618b1ba8cae374f9f44](https://github.com/EndstoneMC/endstone/commit/7edfa7479263bdd9bc4e0618b1ba8cae374f9f44) · 2024-06-14T22:39:46Z · corrective

Fixes the explicitly reported isFlying false result by making Ability::Type and Options uint8_t rather than default-width enums. It also removes getBool/getFloat type checks, returning the union field directly. Thus this is not only a layout change: callers now rely more heavily on the established type/index contract.

<a id="commit-1149"></a>
### 1149: fix: base types of AbilitiesLayer and AbilitiesIndex {#commit-1149}

Source: [da1707f3ea54e06c07583c390055e29897d5072c](https://github.com/EndstoneMC/endstone/commit/da1707f3ea54e06c07583c390055e29897d5072c) · 2024-06-14T22:54:42Z · corrective

Makes AbilitiesIndex int16_t and AbilitiesLayer uint16_t. These widths are part of the native ABI, separate from the public Python/C++ logical values; no tests of host compatibility accompany the patch.

<a id="commit-1162"></a>
### 1162: feat: add Player::giveExp and Player::giveExpLevels {#commit-1162}

Source: [cf93bac5b48e784b2750fbba190a8fbbb226155e](https://github.com/EndstoneMC/endstone/commit/cf93bac5b48e784b2750fbba190a8fbbb226155e) · 2024-06-16T22:26:27Z · substantive

Adds public giveExp/giveExpLevels and Python bindings/stubs by delegating to native addExperience/addLevels. Refactors nearby accesses through getHandle without altering those algorithms. A pre-existing reversed setOp ternary is still visible in unchanged behavior; this patch does not claim to fix it.

<a id="commit-1163"></a>
### 1163: feat: add Player::getAllowFlight {#commit-1163}

Source: [c8ca5d700475ad2d590b991eb9e2e1bf63097c30](https://github.com/EndstoneMC/endstone/commit/c8ca5d700475ad2d590b991eb9e2e1bf63097c30) · 2024-06-16T22:49:51Z · substantive

Exposes getAllowFlight and read-only Python allow_flight by reading AbilitiesComponent MayFly. It distinguishes permission to double-tap fly from actual Flying state; mutation and synchronization follow at 1168–1175.

<a id="commit-1165"></a>
### 1165: feat: add ability setters {#commit-1165}

Source: [9c81b5ca12ba3dd8816b668e53550742d7ea04f6](https://github.com/EndstoneMC/endstone/commit/9c81b5ca12ba3dd8816b668e53550742d7ea04f6) · 2024-06-16T23:03:26Z · substantive

Adds bool/float ability setters. Ability converts Unset to the requested type and zeroes union storage before writing; other existing types are not re-tagged. LayeredAbilities setters deliberately write the Base layer, while getters resolve highest set layer. Therefore a write need not override a higher active layer.

<a id="commit-1166"></a>
### 1166: feat: add Player::getAbilities {#commit-1166}

Source: [978f34e4c092799cfcb7f14a3ac2ca72f431215f](https://github.com/EndstoneMC/endstone/commit/978f34e4c092799cfcb7f14a3ac2ca72f431215f) · 2024-06-16T23:09:17Z · substantive

Adds const native Player::getAbilities returning the persistent component's layered ability reference and routes isFlying through it. This reduces repeated component plumbing without transferring ownership.

<a id="commit-1167"></a>
### 1167: feat: add non-const Player::getAbilities {#commit-1167}

Source: [1ba324c7d8f100812002029611a4c8c3b21684be](https://github.com/EndstoneMC/endstone/commit/1ba324c7d8f100812002029611a4c8c3b21684be) · 2024-06-16T23:27:36Z · staging

Adds non-const getAbilities implementation and mutable ability lookups; the Player header declaration arrives at 1168. Mutable layered lookup scans highest-to-lowest just like const lookup, distinct from the Base-only setters.

<a id="commit-1168"></a>
### 1168: feat: add Player::setAllowFlight and Player::setFlying {#commit-1168}

Source: [3ffde7d36e45f1363fb5a5650733353e569016cc](https://github.com/EndstoneMC/endstone/commit/3ffde7d36e45f1363fb5a5650733353e569016cc) · 2024-06-16T23:32:40Z · substantive

Adds public/Python setAllowFlight and setFlying plus the missing native mutable-access declaration. Setting flying requires allow-flight and logs/returns otherwise. Initial allow-flight disable condition is inverted and synchronization remains TODO; 1170/1174/1175 complete the intended operation in separate steps.

<a id="commit-1170"></a>
### 1170: feat: add EndstonePlayer::updateAbilities {#commit-1170}

Source: [e80452ed02c5452a2772c5be019becc86a8ceeb1](https://github.com/EndstoneMC/endstone/commit/e80452ed02c5452a2772c5be019becc86a8ceeb1) · 2024-06-17T00:00:58Z · staging

Adds permission-handler/layer iteration and updateAbilities calls after the flight setters. Constructs serialized data from player ID and layered state, but mistakenly creates a Text packet before casting to UpdateAbilitiesPacket. The new packet/data headers are staged in 1171/1173, and the wrong packet ID is repaired at 1174.

<a id="commit-1171"></a>
### 1171: feat: add UpdateAbilitiesPacket {#commit-1171}

Source: [c5ed6a3e7d374fc1d19671fa3f52a0fd15a03134](https://github.com/EndstoneMC/endstone/commit/c5ed6a3e7d374fc1d19671fa3f52a0fd15a03134) · 2024-06-17T00:01:13Z · staging

Adds UpdateAbilitiesPacket containing SerializedAbilitiesData. It depends on the data header supplied at 1173; this is a representation declaration rather than a standalone completed synchronization path.

<a id="commit-1172"></a>
### 1172: feat: add more ability-related methods {#commit-1172}

Source: [980552f19309ea0b2f0cabfd535bffb03810e191](https://github.com/EndstoneMC/endstone/commit/980552f19309ea0b2f0cabfd535bffb03810e191) · 2024-06-17T00:54:42Z · substantive

Adds per-layer typed reads, any-set detection and option-filtered iteration. Ability options become EnTT bit flags and isSet means type is not Unset; getBool/getFloat return defaults only for unset at Abilities level. These helpers support serializing only relevant layers while retaining raw union reads for set entries.

<a id="commit-1173"></a>
### 1173: feat: add SerializedAbilitiesData {#commit-1173}

Source: [a97078944b37c72d71c26abf94135ad5f822dcac](https://github.com/EndstoneMC/endstone/commit/a97078944b37c72d71c26abf94135ad5f822dcac) · 2024-06-17T00:54:53Z · substantive

Builds SerializedAbilitiesData from a player ID, permission handler and nonempty layers in descending order. Each serialized layer records type, set/value bitsets and fly/walk speeds; value-initialized records start masks at zero. Nineteen current ability indices fit the 32-bit masks. This reconstructs host packet data rather than sending only the one changed flag.

<a id="commit-1174"></a>
### 1174: fix: EndstonePlayer::updateAbilities {#commit-1174}

Source: [b20a9f9e9952c0c23c241a269f5509ad18a86058](https://github.com/EndstoneMC/endstone/commit/b20a9f9e9952c0c23c241a269f5509ad18a86058) · 2024-06-17T00:55:10Z · corrective

Changes updateAbilities packet factory ID from Text to UpdateAbilitiesPacket before the static cast. This repairs the representation mismatch introduced at 1170; it is stronger evidence of incremental correction than a claim every feature commit was independently safe.

<a id="commit-1175"></a>
### 1175: fix: Player::setAllowFlight {#commit-1175}

Source: [a7f9c79003d4e6194488aa60d2fa956ed97baa0b](https://github.com/EndstoneMC/endstone/commit/a7f9c79003d4e6194488aa60d2fa956ed97baa0b) · 2024-06-17T00:56:59Z · corrective

Corrects disabling-flight logic to clear Flying when currently flying and permission is being disabled. Then MayFly is updated and abilities resent. Higher-layer precedence and setter rejection rules remain; no live client test was run.

<a id="commit-1190"></a>
### 1190: feat: add attribute-related stuff {#commit-1190}

Source: [b94b6d3f4382854450af4e9929edce58afb48763](https://github.com/EndstoneMC/endstone/commit/b94b6d3f4382854450af4e9929edce58afb48763) · 2024-06-17T19:44:28Z · staging

Introduces AttributesComponent, Attribute metadata, a placeholder AttributeInstance, BaseAttributeMap declaration and byte-sized RedefinitionMode. This models native attributes for upcoming experience getters; no public general-purpose attribute API or completed instance access exists yet.

<a id="commit-1191"></a>
### 1191: feat: add constructors for HashedString {#commit-1191}

Source: [465505e74633435c786b9491b70ce4632472e2ae](https://github.com/EndstoneMC/endstone/commit/465505e74633435c786b9491b70ce4632472e2ae) · 2024-06-17T20:31:55Z · staging

Adds HashedString constructors/private fields, initially computing std::hash<string>. That implementation is later replaced at 1199 to match host hash constants. The cached last_match pointer lacks default initialization in these ordinary constructors; this chunk does not claim to settle all cache lifetime invariants.

<a id="commit-1192"></a>
### 1192: feat: add operators for HashedString class {#commit-1192}

Source: [89b7cb47306b7cd830daf0c25ff299d5e38db60a](https://github.com/EndstoneMC/endstone/commit/89b7cb47306b7cd830daf0c25ff299d5e38db60a) · 2024-06-17T20:52:21Z · substantive

Adds hash accessor/equality, cached reciprocal last-match shortcut and std::hash<HashedString>. Equality compares stored hash then actual text before caching a match. It is host-container interoperability work; the initial standard-library string hash still makes lookups incompatible until 1199's explicit algorithm.

<a id="commit-1193"></a>
### 1193: feat: add AttributeCollection {#commit-1193}

Source: [656b996078fee9ad2f0e17f178c3a9e18ce23ed9](https://github.com/EndstoneMC/endstone/commit/656b996078fee9ad2f0e17f178c3a9e18ce23ed9) · 2024-06-17T20:56:36Z · staging

Adds native AttributeCollection singleton hook and map from HashedString to Attribute pointers, plus one manifest function per platform while preserving prior offsets. Collection ownership remains with the host; this declaration does not expose a populated local registry.

<a id="commit-1194"></a>
### 1194: feat: add 'getAttribute' and 'hasAttribute' methods to AttributeCollection class {#commit-1194}

Source: [10eb28f05f70194fa7cc1b520089d2853e375684](https://github.com/EndstoneMC/endstone/commit/10eb28f05f70194fa7cc1b520089d2853e375684) · 2024-06-17T21:08:43Z · substantive

Adds collection lookup returning nullptr for absent names and a presence query. These are initially instance methods while the native singleton accessor is private; 1195 turns them into practical static convenience methods through instance().

<a id="commit-1195"></a>
### 1195: feat: add more attribute-related stuff {#commit-1195}

Source: [3280891a28602c09d5c05173b7f476288660622b](https://github.com/EndstoneMC/endstone/commit/3280891a28602c09d5c05173b7f476288660622b) · 2024-06-17T21:39:23Z · substantive

Makes collection lookup/presence static through the native singleton, enables implicit HashedString construction, models AttributeInstance's host layout/current value and implements BaseAttributeMap by numeric attribute ID. The instance is initially abstract because of pure virtual destructor/tick declarations; 1198 adjusts that representation. Map lookup initially uses at().

<a id="commit-1196"></a>
### 1196: feat: add Player::getAttribute and Player::getPlayerLevel {#commit-1196}

Source: [21503748a9c0bae879f5327b77eefbd817620197](https://github.com/EndstoneMC/endstone/commit/21503748a9c0bae879f5327b77eefbd817620197) · 2024-06-17T21:39:57Z · substantive

Adds native player attribute access from persistent AttributesComponent and a level getter using a cached pointer to minecraft:player.level. Missing-name null is dereferenced without a new guard, relying on the native registry contract; later hash repair is essential for lookup, not merely a performance change.

<a id="commit-1197"></a>
### 1197: feat: add Player::getLevelProgress {#commit-1197}

Source: [cbea2be3e83ee9ac49eb3db720c5338e9cfb1ea1](https://github.com/EndstoneMC/endstone/commit/cbea2be3e83ee9ac49eb3db720c5338e9cfb1ea1) · 2024-06-17T21:43:44Z · substantive

Adds level-progress reading through cached minecraft:player.experience Attribute. It exposes a host current-value field, not a locally calculated experience formula; absence/lifetime assumptions match the level getter.

<a id="commit-1198"></a>
### 1198: feat: add Player::getExp and Player::getExpLevel {#commit-1198}

Source: [b570154d8edc80d57cadec7aa039a5eaee284fd2](https://github.com/EndstoneMC/endstone/commit/b570154d8edc80d57cadec7aa039a5eaee284fd2) · 2024-06-17T21:57:05Z · api_change

Adds public/Python exp and exp_level getters, documenting exp as progress 0..1 toward the next level rather than total points. Makes AttributeInstance's destructor default and comments out pure tick, enabling a concrete representation in the map. No new experience mutation/validation algorithm or runtime test is included.

<a id="commit-1199"></a>
### 1199: fix: hash computation in class HashedString {#commit-1199}

Source: [82994a3a8d42945b63810e93d4e1bf776aefbd0b](https://github.com/EndstoneMC/endstone/commit/82994a3a8d42945b63810e93d4e1bf776aefbd0b) · 2024-06-17T23:09:17Z · corrective

Replaces std::hash with explicit 64-bit multiply-then-XOR hashing, empty-input result zero, overloads for string/C-string and five known Minecraft attribute hash assertions. Adds copy/move/assignment that clear the match cache and text accessors. Test source was read, not executed; ordinary constructor cache initialization and reciprocal cache invalidation on mutation remain unproven, so this is not a blanket value-type safety endorsement.

<a id="commit-1200"></a>
### 1200: feat: improve BaseAttributeMap {#commit-1200}

Source: [c096b5d8e43b6b9f0a7a3e30f26035190b0a1181](https://github.com/EndstoneMC/endstone/commit/c096b5d8e43b6b9f0a7a3e30f26035190b0a1181) · 2024-06-17T23:37:59Z · substantive

Adds Windows AttributesComponent type-hash assertion and replaces map.at with find plus explicit runtime_error for an invalid ID. This improves the error message/type contract at the map boundary; it does not guard a missing cached Attribute pointer before ID lookup. Native host validation remains outstanding outside this static review.
