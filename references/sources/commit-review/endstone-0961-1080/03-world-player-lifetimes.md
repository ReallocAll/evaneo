<!-- retrieval: {"source_ids":["public:commit:00ef74052692284af8825440e39cf8b0e268995a","public:commit:113c4b5c0eec805bb95dabe35b5ca9500d3ec094","public:commit:13f27338ca20be74a813aea331b054e74959e522","public:commit:1409bf27defc9eb97be6d2bbbb64658563756fb9","public:commit:1bd7938871af021859c6abc27c9f7e110d48affb","public:commit:26785a4e78e08ddf42b99cfc26c610898590c104","public:commit:2bcd98a07695470138689da14027db7a45086e52","public:commit:3638f6e510708beacc7076cb701ed4071d611866","public:commit:3caf42a6d17d0d735c14bc661bead947d804638d","public:commit:498583d0996166cda96948077d889a77c0162939","public:commit:5cb5bb8b6fc24050fb46fcc7efec90d0380d8c39","public:commit:5fc71f1cd3801a8bb3c729d5df2908a4a2617cab","public:commit:69f8d35e612b510494d929a3ed8bb0496ea292be","public:commit:7fdd2bc77736b87c50b430e1719c5fe56b8197fb","public:commit:8ccd5d8518fa588b4e29b906a3c3a78ca0b75301","public:commit:96f194b76ea7276ea141eae112bb2728cda5e307","public:commit:a9373eba513d845155d52a0f31ec3216e1ea1624","public:commit:b08c2f925b7dea5b533645cc858ad30337d715bd","public:commit:b9745716a5355434b515271b98707d6233ab57b0","public:commit:bbdef7a1c0a5d5d4a3027e95296d0c0c645139f0","public:commit:c01d1a05da169a5765439af7286d1bcf56fbbf75","public:commit:c5c1e0c42c39759f1deda4c935f0b3ff6ab830a7","public:commit:cb89562ec67b93fe6252eab6686aae6364509ef9","public:commit:d3f70300ae40a19ab07fbf4a14bc08baf344d8db","public:commit:e04ae71d1f125ebf815e613116c5dc94f4ac01c3","public:commit:e1563d3e5ef8b83bca1d88996ad4b37df65edd31","public:commit:e27ac3d1f0cf76db8304bb5c509b24cf1b81f6d4","public:commit:e9012aa42511f8868775f1b12b40a02cb100ca47","public:commit:f63988c41678e69f489bfc20257c1254fd350138","public:commit:f8f8dafeb66f6abd2b2982f916f5f96f0effa47e"],"source_type":"public","date":"2024-05-21..2024-06-03","topics":["lifetime","ffi","testing","performance","api","documentation","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Dimension ownership, actor observations and the Python boundary evolve together {#dimension-ownership-actor-observations-and-the-python-boundary-evolve-together}

## The public identity and lifetime contract change again {#the-public-identity-and-lifetime-contract-change-again}

The previous unit had already separated native Level identity from dimensions, then used shared Level wrappers and weak references in Position to address a stated dangling-pointer concern at891. This unit adds the actual Dimension interface and implementation, initially exposes a shared-pointer dimension map, and then changes direction at1013–1017. Server owns Level wrappers uniquely; each Level owns Dimension wrappers uniquely; API calls return references or raw pointers; Position stores a nullable raw Dimension pointer instead of a weak Level handle. Dimension supplies its parent Level reference.

This is not a single ownership simplification hidden behind equivalent interfaces. Public constructors, getters, Python holders and documentation change. The prior unloaded-level wording disappears. The new model relies on server/wrapper lifecycle invariants and no longer supplies weak expiration detection. No commit message explains why the earlier concern was resolved or traded off, so a universal preference for either shared ownership or raw pointers would be unsupported. Native Level/Dimension objects are still borrowed by their wrappers, which is a separate lifetime layer from ownership of the wrapper itself.

1009's dimension map exists before it is populated.1015 eagerly requests the three vanilla dimensions when a Level wrapper is constructed, registers wrappers by case-insensitive name and rejects duplicates. A Custom enum case does not mean custom dimensions are automatically discovered.1016 actor lookup assumes its Level and named Dimension are registered and dereferences the results. Those assumptions connect initialization order directly to apparently simple getters.

## Python reference policies do not erase native lifetime assumptions {#python-reference-policies-do-not-erase-native-lifetime-assumptions}

1025 exposes Dimension name/type/level and Level dimensions/lookup using reference or reference_internal policies. Position and Location accept raw Dimension pointers. The bindings avoid transferring C++ ownership to Python, but an owner-wrapper relationship in Python is not proof that the host's native world remains alive. The lookup's generated stub does not mark the nullable C++ result optional. These are useful API review distinctions, not evidence of a reproduced dangling reference. The final binding and wrapper files were read in full.

1018 also removes the HumanActor intermediate interface and moves per-player permission state into EndstonePlayer, which derives directly from Actor at the public boundary. The history supports removing this particular intermediate abstraction, including its unused op field; it does not support a rule against inheritance. Generated stubs lag the implementation until1023, illustrating why a native API review must check both runtime bindings and typing output.

## Actor state comes from different host observations {#actor-state-comes-from-different-host-observations}

1002 replaces the feet-position native hook with position minus the persistent height offset.1003–1006 model passenger/category state and use the vehicle's post-tick displacement for riding Mob/Ridable velocity, falling back to the actor's own displacement. This also removes899's blanket ground-Y zeroing. These are concrete changes to the definition of a reported observation. A physically intuitive result must still match the host component and tick semantics; no benchmark or simulation test establishes that here.

Game modes narrow host values to four public modes, resolve native Default through Level and map unrecognized values to Survival. Flight is another read-only host observation: five ability layers are searched from highest to lowest for a non-NotSet entry, and typed accessors return defaults on mismatched tags. Gliding, emoting and jumping use flags/components; they are not all derived from velocity. The unit adds no generic movement controller, account permission model or flight setter.

1073 repairs the earlier901 public lava getter, which had delegated to water; its Python typo is corrected at the same time and the stub catches up in1077. This closes a specific negative example with a dated fix. Retaining only the bug would be as misleading as retaining only the final clean getter. There is no new lava/water regression test in the diff.

## Limits and uses {#limits-and-uses}

Size assertions, enum values, component offsets and get_or_emplace wrappers were inspected as source. They do not establish compatibility with a currently running Bedrock binary. The not-null persistent-component accessor requires an invariant; its presence is not a runtime check that every component exists. The unique-ID fallback asks for a new ID and calls getOrAdd on a possibly existing sentinel component, without explicitly replacing that existing value. Host invariants remain unknown. Relevant use cases are ownership migration review, wrapper/native lifetime separation, C++/Python API consistency, and deciding which host state is the correct observation for a user-facing property. No old Nukkit material is used as precedent.


## Individual commit dispositions {#individual-commit-dispositions}


<a id="commit-1002"></a>
### 1002: refactor: Actor::getLocation {#commit-1002}

Source: [2bcd98a07695470138689da14027db7a45086e52](https://github.com/EndstoneMC/endstone/commit/2bcd98a07695470138689da14027db7a45086e52). Authored 2024-05-21T10:44:18Z; Git author Vincent. Disposition: implementation_revision.

Replaces the native feet-location hook with local position minus OffsetsComponent.height_offset and expands the reconstructed offsets component. This retains a feet-based public location while changing the integration mechanism. Native offset correctness is assumed from the declarations; no measured accuracy comparison is given.


<a id="commit-1003"></a>
### 1003: feat: add StrictEntityContext and PassengerComponent {#commit-1003}

Source: [e04ae71d1f125ebf815e613116c5dc94f4ac01c3](https://github.com/EndstoneMC/endstone/commit/e04ae71d1f125ebf815e613116c5dc94f4ac01c3). Authored 2024-05-21T11:28:07Z; Git author Vincent. Disposition: abi_prerequisite.

Adds StrictEntityContext::isNull using the lower18-bit entity mask and models PassengerComponent as a strict context plus vehicle ID. This supports vehicle lookup but relies on the host’s entity representation; no broad ECS invariant is established.


<a id="commit-1004"></a>
### 1004: feat: add ActorCategory {#commit-1004}

Source: [e27ac3d1f0cf76db8304bb5c509b24cf1b81f6d4](https://github.com/EndstoneMC/endstone/commit/e27ac3d1f0cf76db8304bb5c509b24cf1b81f6d4). Authored 2024-05-21T11:28:26Z; Git author Vincent. Disposition: abi_prerequisite.

Adds ActorCategory bit flags and combinations, with the native entityCategoryFromString source noted in comments. The enum enables later Mob/Ridable selection. It is reconstructed host knowledge rather than a new gameplay categorization policy.


<a id="commit-1005"></a>
### 1005: feat: add Actor::getVehicle, Actor::isRiding and Actor::hasCategory {#commit-1005}

Source: [d3f70300ae40a19ab07fbf4a14bc08baf344d8db](https://github.com/EndstoneMC/endstone/commit/d3f70300ae40a19ab07fbf4a14bc08baf344d8db). Authored 2024-05-21T11:28:48Z; Git author Vincent. Disposition: implementation.

Adds Actor vehicle lookup via a non-null PassengerComponent’s vehicle ID, isRiding as successful lookup and bitmask hasCategory. Missing passenger or failed lookup returns null. The public velocity correction in1006 uses these helpers rather than making every actor’s velocity its vehicle’s velocity.


<a id="commit-1006"></a>
### 1006: fix: Actor::getVelocity when the actor is riding {#commit-1006}

Source: [498583d0996166cda96948077d889a77c0162939](https://github.com/EndstoneMC/endstone/commit/498583d0996166cda96948077d889a77c0162939). Authored 2024-05-21T11:39:28Z; Git author Vincent. Disposition: corrective_revision.

Fixes riding velocity by using PostTickPositionDeltaComponent from a Mob/Ridable actor’s vehicle, or the actor itself when there is no vehicle, falling back to the state-vector delta. Removes899’s forced zero Y velocity on ground. This is a change in which simulation observation defines velocity, not merely a variable rename or a benchmarked performance improvement.


<a id="commit-1007"></a>
### 1007: feat: basic interface for Dimension {#commit-1007}

Source: [b9745716a5355434b515271b98707d6233ab57b0](https://github.com/EndstoneMC/endstone/commit/b9745716a5355434b515271b98707d6233ab57b0). Authored 2024-05-21T14:58:11Z; Git author Vincent. Disposition: public_api.

Defines Dimension’s name/type/Level interface. It gives plugin-facing dimension identity separate from Level and prepares the subsequent ownership changes. Implementation and Python exposure arrive later; this commit alone is the contract.


<a id="commit-1009"></a>
### 1009: feat: add Level::getDimension and Level::getDimensions {#commit-1009}

Source: [5fc71f1cd3801a8bb3c729d5df2908a4a2617cab](https://github.com/EndstoneMC/endstone/commit/5fc71f1cd3801a8bb3c729d5df2908a4a2617cab). Authored 2024-05-21T15:22:02Z; Git author Vincent. Disposition: incremental_api.

Adds Level dimension listing and case-insensitive lookup backed initially by shared_ptr values, plus API documentation. The map is not populated until1015. A declared public lookup and its eventual usable initialization must be distinguished.


<a id="commit-1010"></a>
### 1010: refactor: make VanillaDimensions constexpr {#commit-1010}

Source: [26785a4e78e08ddf42b99cfc26c610898590c104](https://github.com/EndstoneMC/endstone/commit/26785a4e78e08ddf42b99cfc26c610898590c104). Authored 2024-05-21T16:12:36Z; Git author Vincent. Disposition: abi_constants.

Defines vanilla dimension IDs0/1/2 as constexpr and removes the out-of-line toString declaration.1012 removes its implementation. This simplifies known host constants without adding custom-dimension discovery.


<a id="commit-1011"></a>
### 1011: feat: add members of Dimension {#commit-1011}

Source: [e1563d3e5ef8b83bca1d88996ad4b37df65edd31](https://github.com/EndstoneMC/endstone/commit/e1563d3e5ef8b83bca1d88996ad4b37df65edd31). Authored 2024-05-21T16:12:55Z; Git author Vincent. Disposition: abi_reconstruction.

Names native Dimension fields, including its queue, name and ID, and provides getName. Layout comments document offsets but are not runtime validation. This representation underlies1012’s public wrapper mapping.


<a id="commit-1012"></a>
### 1012: feat: add EndstoneDimension {#commit-1012}

Source: [cb89562ec67b93fe6252eab6686aae6364509ef9](https://github.com/EndstoneMC/endstone/commit/cb89562ec67b93fe6252eab6686aae6364509ef9). Authored 2024-05-21T16:13:24Z; Git author Vincent. Disposition: wrapper_implementation.

Adds EndstoneDimension borrowing native Dimension and public Level references, maps vanilla IDs to Overworld/Nether/TheEnd and otherwise Custom, and removes the old native toString hook. The wrapper owns neither native object. A public virtual destructor enables ownership through the interface.


<a id="commit-1013"></a>
### 1013: feat: replace std::shared_ptr<Level> with Level& {#commit-1013}

Source: [a9373eba513d845155d52a0f31ec3216e1ea1624](https://github.com/EndstoneMC/endstone/commit/a9373eba513d845155d52a0f31ec3216e1ea1624). Authored 2024-05-21T16:25:43Z; Git author Vincent. Disposition: ownership_reversal.

Replaces shared Level returns/registry ownership with server-owned unique_ptr and raw pointer/reference APIs, changes Position from weak_ptr to raw Level*, removes unloaded-level documentation and updates Python holders/mocks. This reverses891’s explicit dangling-pointer rationale without a new stated motive. It establishes a different lifetime contract, not proof raw pointers became inherently safe.


<a id="commit-1014"></a>
### 1014: style: clean up codes {#commit-1014}

Source: [f8f8dafeb66f6abd2b2982f916f5f96f0effa47e](https://github.com/EndstoneMC/endstone/commit/f8f8dafeb66f6abd2b2982f916f5f96f0effa47e). Authored 2024-05-21T16:26:24Z; Git author Vincent. Disposition: mechanical.

Only include order and comment spacing change. The actual diff is verified; no additional lifetime or behavior policy is inferred.


<a id="commit-1015"></a>
### 1015: feat: add dimensions on level load {#commit-1015}

Source: [7fdd2bc77736b87c50b430e1719c5fe56b8197fb](https://github.com/EndstoneMC/endstone/commit/7fdd2bc77736b87c50b430e1719c5fe56b8197fb). Authored 2024-05-22T02:45:40Z; Git author Vincent. Disposition: ownership_completion.

Loads the three vanilla native dimensions when EndstoneLevel is constructed, wraps them in unique_ptr, returns borrowed raw pointers and rejects duplicate case-insensitive names with a log. This completes1009’s empty map and changes its shared ownership to unique ownership. Custom enum support does not imply automatic custom dimension enumeration.


<a id="commit-1016"></a>
### 1016: feat: add Actor::getDimension {#commit-1016}

Source: [5cb5bb8b6fc24050fb46fcc7efec90d0380d8c39](https://github.com/EndstoneMC/endstone/commit/5cb5bb8b6fc24050fb46fcc7efec90d0380d8c39). Authored 2024-05-22T03:10:11Z; Git author Vincent. Disposition: api_integration.

Adds Actor::getDimension via its Level’s name lookup and makes Location use Dimension rather than Level. The pointer result is dereferenced under the registration invariant; missing registration has no local fallback. Position/Location constructor compatibility is completed by1017 and player forwarding by1018.


<a id="commit-1017"></a>
### 1017: refactor: Position and Location no longer holds reference to Level {#commit-1017}

Source: [13f27338ca20be74a813aea331b054e74959e522](https://github.com/EndstoneMC/endstone/commit/13f27338ca20be74a813aea331b054e74959e522). Authored 2024-05-22T03:13:15Z; Git author Vincent. Disposition: public_api_revision.

Removes the Level member entirely from Position/Location and stores a nullable raw Dimension*. The setter accepts a reference; expiry detection from the former weak Level model is gone. Dimension itself provides Level navigation. This is a public constructor/property migration, not simply an ownership implementation detail.


<a id="commit-1018"></a>
### 1018: refactor: Player now inherits directly from Actor {#commit-1018}

Source: [69f8d35e612b510494d929a3ed8bb0496ea292be](https://github.com/EndstoneMC/endstone/commit/69f8d35e612b510494d929a3ed8bb0496ea292be). Authored 2024-05-22T03:14:20Z; Git author Vincent. Disposition: hierarchy_revision.

Removes HumanActor and has Player derive directly from Actor, moving the permission base/delegations into EndstonePlayer and updating Python inheritance/position constructors. It also removes unused HumanActor op storage. This is a concrete simplification of an unused intermediate layer; it does not support a general rejection of inheritance. Stubs catch up in1023.


<a id="commit-1019"></a>
### 1019: fix: compilation errors due to missing includes {#commit-1019}

Source: [96f194b76ea7276ea141eae112bb2728cda5e307](https://github.com/EndstoneMC/endstone/commit/96f194b76ea7276ea141eae112bb2728cda5e307). Authored 2024-05-22T03:20:16Z; Git author Vincent. Disposition: build_fix.

Adds the missing Dimension include needed by the changed actor/location interfaces. This is a compile-surface repair, with no build execution in this review.


<a id="commit-1021"></a>
### 1021: feat: add GameType {#commit-1021}

Source: [00ef74052692284af8825440e39cf8b0e268995a](https://github.com/EndstoneMC/endstone/commit/00ef74052692284af8825440e39cf8b0e268995a). Authored 2024-05-22T03:58:46Z; Git author Vincent. Disposition: abi_enum.

Defines native GameType IDs including Undefined=-1, Default=5 and Spectator=6. These are host protocol/model constants used by the next mapping; no new game-mode behavior is implemented yet.


<a id="commit-1022"></a>
### 1022: feat: add Player::getGameMode and Player::setGameMode {#commit-1022}

Source: [bbdef7a1c0a5d5d4a3027e95296d0c0c645139f0](https://github.com/EndstoneMC/endstone/commit/bbdef7a1c0a5d5d4a3027e95296d0c0c645139f0). Authored 2024-05-22T04:14:15Z; Git author Vincent. Disposition: public_api.

Adds get/set game mode: reads the ECS component, resolves Default through Level, maps four exposed modes and falls back to public Survival for other values; setting calls the native virtual setter. This intentionally narrows the public model relative to native sentinel values. No mode-transition tests are added.


<a id="commit-1023"></a>
### 1023: feat: add python bindings for `game_mode` property {#commit-1023}

Source: [f63988c41678e69f489bfc20257c1254fd350138](https://github.com/EndstoneMC/endstone/commit/f63988c41678e69f489bfc20257c1254fd350138). Authored 2024-05-22T04:19:21Z; Git author Vincent. Disposition: python_api.

Exposes game_mode and refreshes stubs for game modes, removal of HumanActor and dimension-based Position/Location. The generated surface is verified against the API change; it is not independent runtime evidence.


<a id="commit-1025"></a>
### 1025: feat: add python bindings for Dimension {#commit-1025}

Source: [e9012aa42511f8868775f1b12b40a02cb100ca47](https://github.com/EndstoneMC/endstone/commit/e9012aa42511f8868775f1b12b40a02cb100ca47). Authored 2024-05-22T04:40:41Z; Git author Vincent. Disposition: python_lifetime_boundary.

Adds Dimension type/name/level and Level dimensions/get_dimension Python bindings and return policies, with stub updates. reference/reference_internal exposes borrowed C++ objects; it cannot by itself keep the underlying native Level alive after server teardown. The lookup stub is non-optional although C++ can return null.


<a id="commit-1029"></a>
### 1029: feat: add AbilitiesIndex and ActorFlags {#commit-1029}

Source: [1bd7938871af021859c6abc27c9f7e110d48affb](https://github.com/EndstoneMC/endstone/commit/1bd7938871af021859c6abc27c9f7e110d48affb). Authored 2024-05-23T07:44:39Z; Git author Vincent. Disposition: abi_enum.

Expands ActorFlags and AbilitiesIndex and makes the native status-flag getter const-correct. The enumerations support later gliding/emoting/flying access, not permission enforcement by themselves.


<a id="commit-1030"></a>
### 1030: feat: add Mob::isGliding {#commit-1030}

Source: [3638f6e510708beacc7076cb701ed4071d611866](https://github.com/EndstoneMC/endstone/commit/3638f6e510708beacc7076cb701ed4071d611866). Authored 2024-05-23T07:44:50Z; Git author Vincent. Disposition: implementation.

Adds native Mob::isGliding from the relevant actor flag. It is a small read adapter; it does not add a public flight controller or state mutation.


<a id="commit-1031"></a>
### 1031: feat: add Player::isEmoting {#commit-1031}

Source: [1409bf27defc9eb97be6d2bbbb64658563756fb9](https://github.com/EndstoneMC/endstone/commit/1409bf27defc9eb97be6d2bbbb64658563756fb9). Authored 2024-05-23T07:45:01Z; Git author Vincent. Disposition: implementation.

Adds native Player::isEmoting from its actor flag. No event or setter is introduced.


<a id="commit-1032"></a>
### 1032: refactor: inline ActorCollision and ActorEnvironment functions {#commit-1032}

Source: [c5c1e0c42c39759f1deda4c935f0b3ff6ab830a7](https://github.com/EndstoneMC/endstone/commit/c5c1e0c42c39759f1deda4c935f0b3ff6ab830a7). Authored 2024-05-23T07:51:10Z; Git author Vincent. Disposition: verified_relocation.

Moves four ground/water/lava ECS-flag helpers inline with their existing bodies. Reading verifies equivalent predicates; there is no measured performance result and no repair to the separate public lava delegation until1073.


<a id="commit-1033"></a>
### 1033: feat: add Actor::isJumping {#commit-1033}

Source: [113c4b5c0eec805bb95dabe35b5ca9500d3ec094](https://github.com/EndstoneMC/endstone/commit/113c4b5c0eec805bb95dabe35b5ca9500d3ec094). Authored 2024-05-23T08:02:11Z; Git author Vincent. Disposition: implementation.

Adds native jump state using MobIsJumpingFlag and an inline MobJump helper. This reads the host’s component state instead of deriving jumping from Y velocity.


<a id="commit-1034"></a>
### 1034: feat: add ability classes {#commit-1034}

Source: [b08c2f925b7dea5b533645cc858ad30337d715bd](https://github.com/EndstoneMC/endstone/commit/b08c2f925b7dea5b533645cc858ad30337d715bd). Authored 2024-05-24T02:59:36Z; Git author Vincent. Disposition: abi_scaffold.

Models Ability’s tagged value/options, the19-entry Abilities array and five-layer LayeredAbilities with permissions; moves AbilitiesIndex. Size assertions encode the assumed host shape. One CommandOrigin include points to the wrong actor path until1035, so the scaffold is not proof of a buildable isolated commit.


<a id="commit-1035"></a>
### 1035: feat: add Player::isFlying {#commit-1035}

Source: [8ccd5d8518fa588b4e29b906a3c3a78ca0b75301](https://github.com/EndstoneMC/endstone/commit/8ccd5d8518fa588b4e29b906a3c3a78ca0b75301). Authored 2024-05-24T03:39:11Z; Git author Vincent. Disposition: implementation.

Resolves abilities by searching layers from Editor downward for the first non-NotSet value, then returns typed bool/float defaults on mismatch; adds native Player flying access and corrects the include. This models precedence explicitly, but it is not a general account permission system or a flight setter.


<a id="commit-1036"></a>
### 1036: feat: add python binding for Player::isFlying {#commit-1036}

Source: [c01d1a05da169a5765439af7286d1bcf56fbbf75](https://github.com/EndstoneMC/endstone/commit/c01d1a05da169a5765439af7286d1bcf56fbbf75). Authored 2024-05-24T03:53:12Z; Git author Vincent. Disposition: public_api.

Exposes isFlying through EndstonePlayer and Python, moves init/disconnect without changing their bodies and adds nodiscard annotations. The read-only property reports layered native ability state. Mechanical relocation is not counted as another lifecycle redesign.


<a id="commit-1073"></a>
### 1073: fix: Actor::isInLava {#commit-1073}

Source: [3caf42a6d17d0d735c14bc661bead947d804638d](https://github.com/EndstoneMC/endstone/commit/3caf42a6d17d0d735c14bc661bead947d804638d). Authored 2024-06-03T16:23:21Z; Git author Vincent. Disposition: corrective_revision.

Fixes public EndstoneActor::isInLava to call native lava rather than water and corrects Python’s java typo to lava. This closes the exact901 defect observed in the previous unit, rather than supporting a claim that the bug persisted indefinitely. No lava/water regression test is added.
