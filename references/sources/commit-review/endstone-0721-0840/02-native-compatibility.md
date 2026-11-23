<!-- retrieval: {"source_ids":["public:commit:156a2a2d712eea67df88f042cd9718de1c3241c6","public:commit:194741c286c2c64bbf230428230f777f386536c3","public:commit:20297a3a58f3746e6c224439f763cfeb49fe57ed","public:commit:2d4473ab94548ba9fd1b6535177e96aa0c101575","public:commit:2e29ff20854b05bfa64df474010d68ddea6a5c54","public:commit:353f3e3956d16a159cf8a4d9e844b448aecce0f2","public:commit:4b0ab4ae4272d20fa3ec8549de7c5c82f25c1d0f","public:commit:4b258a836da86a38f0bcb81bf552c3b3cd2fa7f3","public:commit:502ed0303ec7a05590f5196f104d5b905b8449b3","public:commit:51a4b930472d07ed3dfedb3a5243eaeca5f15248","public:commit:549116c4307c73e5ee9df3c0d85c94e21a18fad1","public:commit:6a2f9aa39153d9802d7aaa876db4600cda652e4e","public:commit:718997b3cc4fdf9dc3a99689d056606cae7546c6","public:commit:80589d1f5327c9539a1c9dd1a7a5a346114076c5","public:commit:8445778b8a17a127e804be18c50d85a03484da61","public:commit:8a6a83e299ef98988787815090895bada6001a9c","public:commit:8c1fe3ee10b20c3ce6c423215de61ae569938362","public:commit:8f45a4b98ff0d5909a92fbf54ebbe5f47a6678c7","public:commit:9c8b340969c0cd75e48ebefd9846efb36727e6be","public:commit:a4be5328e3f607bab9cf561ffe97524ca45bdd5a","public:commit:a5e1fb5dc648e3df8df98ca159c92c8f0b845f0a","public:commit:aec9e027f6fb8b62ab1783875dae9255274b37fc","public:commit:b308ee1d984aa15f3233f912b49fb042e814b877","public:commit:bcf77267074847470c16064c4421f2a898d34f47","public:commit:d38b09b0531da236005543d37c51fcc079567152","public:commit:da77f8b706311bb8af502aa9e485f8199a4d1a98","public:commit:e440b1fe6538ab6955705f2f0ee1fc7178885ea3","public:commit:f4e5c0c145ca1a6abc2b5f01fe75bebbe89e48cf","public:commit:fba00c8748d59a26458b26c6ca5a48efcec280c9","public:commit:fd3f0dfd2cf94e54adb63fa1749b3aa576e7404c"],"source_type":"public","date":"2024-04-19..2024-04-29","topics":["lifetime","concurrency","ffi","testing","build","api","diagnosis","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native ABI, UUID representation and player identity {#native-abi-uuid-representation-and-player-identity}

## Useful conclusion {#useful-conclusion}

The1.20.80 transition exposes two complementary approaches: keep native ABI mirrors aligned where virtual calls are necessary, and replace brittle access paths with more explicit representations where practical. This unit changes vtable ordering, models named fields instead of word offsets, uses ECS presence to identify players, converts UUID byte fields explicitly, and resolves network endpoints through the captured native peer. Each reduces one kind of ambiguity while retaining another host-version or lifetime dependency.

These changes are not evidence that declaration-only native mirrors are safe without validation. Some total-size assertions are introduced and then removed. Weather needs another Linux-specific repair after earlier generic-vtable abandonment606. The useful record is the sequence of hypotheses, repairs and limits, rather than an unconditional preference for either raw offsets or structural mirrors.

## Version markers versus actual ABI work {#version-markers-versus-actual-abi-work}

751 updates the advertised game to1.20.80.753 replaces the formerly static I18n::get hook with a getI18n accessor and a full modeled virtual interface, changing callers for descriptions and /say logging. GSL introduced752 is used in a nonnull/nonowner resource signature. The source establishes the new declarations and calls, not their agreement with every native build.

754's ILevel changes are substantive ABI edits: reordered overload families, removed obsolete event-coordinator setters and direct entity-tick entry, and a new sorted-position query all shift virtual slots.757 likewise removes Actor/Mob entries and changes equipment-death overload order. It would be wrong to classify these as cosmetic header sorting.755 explicitly disables broken actor/block/level/player coordinator export hooks while preserving server startup hooks, and moves fatal diagnostics earlier to initialization start. This is a scoped retreat from unstable hook coverage, not evidence that the event system was globally removed.

756 adds compiler-specific EnTT type-hash assertions for the player flag and user identity component.757 stops calling a virtual isPlayer and instead checks the player component.758 switches the presence predicate from try_get pointer comparison to registry all_of. Targeted757 context confirms both Actor and EntityContext already had const tryGetComponent overloads, so no constness repair is claimed. The precise failure behind the title 'fix Actor::hasComponent' remains unknown. We have not inspected EnTT internals or reproduced host component storage behavior.

## Make byte representation explicit, then test the external contract too {#make-byte-representation-explicit-then-test-the-external-contract-too}

Earlier player UUIDs copied native signed halves through a union directly into16 public bytes.759 introduces explicit reverse-copy mappings across six byte fields, in both directions, and uses them for cached player UUID plus native lookup input. The public UUID loses its half overlay and user constructors. Plain `UUID value;` is therefore no longer guaranteed initialized, while `UUID{}` aggregate initialization supplies zeroes; these are different call-site contracts.

The added test fills bytes0..15, converts public→native→public and checks each byte. That is valuable inverse-pair coverage, but two matching wrong conversions can still pass. There is no test with a known external UUID string/native pair in this commit. The change explicitly reports incorrect conversion, so intent is clear; canonical host correctness is reported rather than independently demonstrated. Source-attributed Boost adaptation belongs to the earlier public UUID implementation and must not be recast as entirely original algorithm authorship.

795 later exposes Server.get_player to Python. Endpoint caster context confirms the earlier handwritten input conversion still calls `bytes` as a method, accesses returned bytes without checking the failed call, and returns true when PyErr_Occurred is nonnull. That path was previously largely latent in the reviewed public API. The new binding makes input-direction tests necessary; the native roundtrip test759 does not cover it. Outbound conversion uses the public byte array and has separate C-API ownership/error concerns. No Python or upstream code was executed during this review.

## From magic offsets to readable but still ABI-dependent structures {#from-magic-offsets-to-readable-but-still-abi-dependent-structures}

762 replaces Minecraft's commands pointer arithmetic with named fields after EnableNonOwnerReferences, including callbacks, resource/structure managers, permissions, time state and commands_.763 similarly models ServerInstance's multiple bases and minecraft_ member instead of platform word indices. This makes the assumed layout reviewable and groups related concepts, but actual offsets still depend on compiler/base layout. Some asserted base sizes are local compile-time checks; the StorageAreaStateListener size assertion is commented.

764 models EventCoordinatorPimpl's listener/function vectors, flags and thread ID, then LevelEventCoordinator's handler/subscription fields. It replaces another word-offset getter.765 immediately adds a missing thread include and removes both total-size assertions. No rationale for removing those assertions is in the commit. Do not convert 'fix' into proof that all layout assumptions are validated. Named unique_ptr/shared_ptr members are mirrors of host storage, not permission for Endstone to independently destroy native objects.

The weather chain is especially instructive.606 abandoned generic virtual-table replacement for cross-platform maintainability, and607 used `this - 1` as an acknowledged receiver adjustment.722 temporarily removed the script handler destructor while adding chat.768 explicitly reports a Linux weather-change crash, restores an appropriate virtual destructor base/derived model and compares `this` directly to the level handler. It also selects only the Overworld wrapper, avoiding the three wrappers sharing one native Level/coordinator introduced696. These combined edits establish the intended correction, but no isolated test identifies which edit caused the observed crash. Plugin-first weather/thunder events still revert native target fields on cancellation, then invoke original.

766–768 also expose Dimension in the public Level API. The wrapper validates ID against exactly Overworld/Nether/TheEnd and names it via magic_enum; this narrows the native-name delegation added703.767 contains a member-using lambda without capture, removed768. The endpoint source confirms native-dimension pointer filtering for actor enumeration and native Level sharing for time. Python Level binding still only includes name/time, so C++ getDimension is not automatically cross-language complete.

## Resolve a transport endpoint through its actual identity form {#resolve-a-transport-endpoint-through-its-actual-identity-form}

770 models SystemAddress's IPv4/IPv6 union and RakNetGUID, with size assertions.771 models NetworkIdentifier's GUID/address/type fields.772 uses inet_ntop and ntohs rather than native GetPort forwarding, including Windows socket linkage;773 supplies Linux declarations. Conversion failure returns unspecified-looking zero addresses, and any non-IPv4 family follows the IPv6 path. These fallbacks are observed choices, not verified validation policy.

774 names transport variants.775 hooks successful peer startup and captures a raw pointer when incoming connections are allowed, rejecting another capture. It adds the partial RakPeer virtual surface needed to call GetSystemAddressFromGuid. The choice of incoming-count rather than PeerPurpose is visible; no explicit justification or reset lifecycle is given. A raw locator is not ownership.

776 resolves a RakNet player's address through that peer, writes the result into the native identity component, then intentionally falls through to direct address extraction. Address/Address6 are accepted; NetherNet/Generic throw.777 adds the cached public fields/getters and778 exposes them in Python. Thus wrapper construction now requires usable identity and peer state. The cache is not automatically refreshed as transport state changes.779 repairs a Windows-specific integer spelling for Linux. No network requests, runtime peer creation or sensitive live player data were collected by this research.

## Typed grammar data and declarations without independent preference credit {#typed-grammar-data-and-declarations-without-independent-preference-credit}

769 preserves numeric command-flag/symbol values while renaming them.798 replaces many static Symbol globals with HardNonTerminal enum values and a uint32 wrapper. Important aliases preserve their exact old values: public float selects Val0x100003, message selects MessageRoot0x100044, JSON selects JsonObject0x10004a. The generic default Symbol changes from signed-1 to0, while parameter sentinel fields explicitly retain UINT32_MAX. This is more than a textual rename but not a command parser rewrite.

797 ActorType and799 DisconnectFailReason are full mirrored enumeration additions. Their values were read, but there is no reason to infer a personal taxonomy preference or original authorship of native protocol concepts. The latter becomes public and used for login disconnect800.811 exposes runtime IDs through Python and improves inherited documentation, a small API-completeness step rather than new identity storage.

## Tests, collaborators and scope {#tests-collaborators-and-scope}

Only UUID roundtrip source provides a new native unit test in this family; no test execution, native disassembly, binary-vtable inspection or platform build occurred. All120 unit commits have Vincent as author and committer. Dependency authors retain credit for EnTT/GSL/RakNet/Boost concepts; no outside code was read as a personal-style precedent. Applicability is version-bound native integration and foreign-representation testing. The source does not warrant copying hardcoded offsets, enum tables or type hashes into a different host version without revalidation.

Prior reviewed context: [generic-vtable abandonment606 and receiver workaround607](../endstone-0601-0720/01-native-hooks-identity.md), [dimension-wrapper/ECS transition696–717](../endstone-0601-0720/02-actor-player-lifecycle.md), [initial UUID caster665](../endstone-0601-0720/03-python-surface.md).

## Individual source dispositions {#individual-source-dispositions}

<a id="commit-721"></a>
### 721 · feat: add WeakRef<EntityContext> {#commit-721}

[d38b09b0531da236005543d37c51fcc079567152](https://github.com/EndstoneMC/endstone/commit/d38b09b0531da236005543d37c51fcc079567152) · 2024-04-19T10:59:25Z · Vincent (author and committer).

Adds specialized weak EntityContext storage with registry weak reference and entity ID, size assertions24/32 bytes, replaces opaque ChatEvent bytes with candidate fields. Removes generic WeakRef call/expired helpers. Layout modeling only; no chat event dispatch yet.


<a id="commit-753"></a>
### 753 · feat: update I18n interface {#commit-753}

[da77f8b706311bb8af502aa9e485f8199a4d1a98](https://github.com/EndstoneMC/endstone/commit/da77f8b706311bb8af502aa9e485f8199a4d1a98) · 2024-04-24T12:29:14Z · Vincent (author and committer).

Replaces static native I18n::get hook with getI18n singleton accessor and modeled virtual interface; command descriptions and /say use instance get. Adds GSL nonowner resource signature and optional_ref alias. ABI maintenance response adjacent to game update; declarations do not independently prove slot alignment.


<a id="commit-754"></a>
### 754 · fix: virtual table for ILevel {#commit-754}

[8c1fe3ee10b20c3ce6c423215de61ae569938362](https://github.com/EndstoneMC/endstone/commit/8c1fe3ee10b20c3ce6c423215de61ae569938362) · 2024-04-24T12:58:47Z · Vincent (author and committer).

Repairs ILevel virtual order: player lookup, explosion/pathfinding/sound/event overloads reordered; obsolete direct-tick/coordinator setters removed; sorted-client-offset query added. These are ABI semantics, not harmless declaration sorting; matching native implementation is prerequisite for UUID lookup/weather and other virtual calls.


<a id="commit-755"></a>
### 755 · fix: disable broken hooks of EventCoordinator {#commit-755}

[8f45a4b98ff0d5909a92fbf54ebbe5f47a6678c7](https://github.com/EndstoneMC/endstone/commit/8f45a4b98ff0d5909a92fbf54ebbe5f47a6678c7) · 2024-04-24T12:59:10Z · Vincent (author and committer).

Explicitly disables broken actor/block/level/player EventCoordinator export hooks by removing BEDROCK_API, leaving bodies/source placeholders. Server initialization hooks remain. Moves signal handler registration earlier from thread-started to initialize-start, covering more startup failures. No rootcause/host test supplied.


<a id="commit-756"></a>
### 756 · feat: add FlagComponent {#commit-756}

[549116c4307c73e5ee9df3c0d85c94e21a18fad1](https://github.com/EndstoneMC/endstone/commit/549116c4307c73e5ee9df3c0d85c94e21a18fad1) · 2024-04-24T14:00:47Z · Vincent (author and committer).

Adds player flag component and compiler-specific EnTT type-hash static assertions for it and user identity component. These assert local type-hash contract when compiled, not proof runtime host component layout.


<a id="commit-757"></a>
### 757 · fix: virtual table for Actor and Mob {#commit-757}

[718997b3cc4fdf9dc3a99689d056606cae7546c6](https://github.com/EndstoneMC/endstone/commit/718997b3cc4fdf9dc3a99689d056606cae7546c6) · 2024-04-24T14:01:01Z · Vincent (author and committer).

Removes obsolete Actor/Mob virtual entries and reorders death-equipment overloads; isPlayer changes from native virtual call to presence of Player flag ECS component. Initial hasComponent tests try_get pointer, replaced758 with registry all_of. Context confirms const tryGetComponent already existed; no const-mismatch claim. ABI repair plus alternate identification mechanism.


<a id="commit-758"></a>
### 758 · fix: Actor::hasComponent {#commit-758}

[4b0ab4ae4272d20fa3ec8549de7c5c82f25c1d0f](https://github.com/EndstoneMC/endstone/commit/4b0ab4ae4272d20fa3ec8549de7c5c82f25c1d0f) · 2024-04-24T14:34:53Z · Vincent (author and committer).

Routes Actor::hasComponent to EntityContext::hasComponent using registry all_of rather than retrieving a pointer. Explicit presence query for757 flag check; exact reason previous pointer check failed is not stated. Const overloads already existed, so do not infer a constness repair.


<a id="commit-759"></a>
### 759 · fix: incorrect UUID conversion {#commit-759}

[fba00c8748d59a26458b26c6ca5a48efcec280c9](https://github.com/EndstoneMC/endstone/commit/fba00c8748d59a26458b26c6ca5a48efcec280c9) · 2024-04-24T16:03:05Z · Vincent (author and committer).

Fixes UUID conversion with explicit reversed byte-field mappings both directions, replacing direct union overlay/native-half constructor. Applies to player cached UUID and server lookup. Adds0..15-byte roundtrip test; roundtrip proves mutual inverse only, not externally canonical expected UUID. Removing default constructor leaves plain default initialization uninitialized, while UUID{} value initialization zeros aggregate.


<a id="commit-762"></a>
### 762 · refactor: Minecraft class {#commit-762}

[b308ee1d984aa15f3233f912b49fb042e814b877](https://github.com/EndstoneMC/endstone/commit/b308ee1d984aa15f3233f912b49fb042e814b877) · 2024-04-25T09:21:21Z · Vincent (author and committer).

Replaces Minecraft command-pointer word-offset cast with named modeled commands_ unique_ptr after nonowner base and detailed fields. Native object remains host-owned; offsets now depend C++ ABI/member layout rather than disappearing. No runtime validation included.


<a id="commit-763"></a>
### 763 · refactor: ServerInstance class {#commit-763}

[194741c286c2c64bbf230428230f777f386536c3](https://github.com/EndstoneMC/endstone/commit/194741c286c2c64bbf230428230f777f386536c3) · 2024-04-25T09:43:53Z · Vincent (author and committer).

Models ServerInstance four bases and fields, replaces Minecraft pointer word-offset cast with minecraft_ member, relocates common headers/sources. Adds AppPlatformListener/GameCallbacks size assertions, leaves StorageAreaStateListener size assertion commented. Typed structural modeling improves readability but still version/platform dependent.


<a id="commit-764"></a>
### 764 · refactor: LevelEventCoordinator class {#commit-764}

[a4be5328e3f607bab9cf561ffe97524ca45bdd5a](https://github.com/EndstoneMC/endstone/commit/a4be5328e3f607bab9cf561ffe97524ca45bdd5a) · 2024-04-25T10:36:42Z · Vincent (author and committer).

Models EventCoordinatorPimpl vector/thread/flag fields and LevelEventCoordinator unique handler/shared subscription, replaces magic-word pointer arithmetic. Compiler-specific total-size assertions introduced then removed765; source comments alone cannot validate offsets.


<a id="commit-765"></a>
### 765 · fix: LevelEventCoordinator class {#commit-765}

[f4e5c0c145ca1a6abc2b5f01fe75bebbe89e48cf](https://github.com/EndstoneMC/endstone/commit/f4e5c0c145ca1a6abc2b5f01fe75bebbe89e48cf) · 2024-04-25T10:52:01Z · Vincent (author and committer).

Adds required thread header and removes both coordinator size assertions introduced764. Correctness claim narrowed: no replacement invariant or stated reason for removal.


<a id="commit-766"></a>
### 766 · refactor: fix dimension enumeration naming {#commit-766}

[353f3e3956d16a159cf8a4d9e844b448aecce0f2](https://github.com/EndstoneMC/endstone/commit/353f3e3956d16a159cf8a4d9e844b448aecce0f2) · 2024-04-25T12:36:59Z · Vincent (author and committer).

Renames public Dimension enumerators uppercase→CamelCase, values unchanged. C++ source compatibility change completing697 naming direction; no Python enum binding in this diff.


<a id="commit-767"></a>
### 767 · feat: add Level::getDimension {#commit-767}

[80589d1f5327c9539a1c9dd1a7a5a346114076c5](https://github.com/EndstoneMC/endstone/commit/80589d1f5327c9539a1c9dd1a7a5a346114076c5) · 2024-04-25T12:38:13Z · Vincent (author and committer).

Adds public Level::getDimension, validates native ID against three-value enum and names dimensions via magic_enum rather than native VanillaDimensions conversion. Rejects other IDs, narrowing703 generality. Constructor lambda references member without capture, repaired768. Actor filtering still compares native dimension pointer.


<a id="commit-768"></a>
### 768 · fix: crash on Linux when weather is changed {#commit-768}

[a5e1fb5dc648e3df8df98ca159c92c8f0b845f0a](https://github.com/EndstoneMC/endstone/commit/a5e1fb5dc648e3df8df98ca159c92c8f0b845f0a) · 2024-04-25T12:43:57Z · Vincent (author and committer).

Explicit Linux weather-crash fix replaces this-1 handler adjustment with proper virtual destructor base/derived model and direct this comparison. Selects Overworld wrapper before matching shared native coordinator, resolving ambiguous dimension match from696. Also fixes767 constructor lambda. Multiple changes mean no isolated crash rootcause demonstrated; plugin-first weather cancellation remains.


<a id="commit-769"></a>
### 769 · refactor: rename command symbols and flags {#commit-769}

[51a4b930472d07ed3dfedb3a5243eaeca5f15248](https://github.com/EndstoneMC/endstone/commit/51a4b930472d07ed3dfedb3a5243eaeca5f15248) · 2024-04-25T14:34:48Z · Vincent (author and committer).

Renames WithoutCheatEnabled→NotCheat and WildcardActorSelector→WildcardSelector, preserving flagbit128/symbol0x10000a and registration. Native internal naming only; not permission behavior change.


<a id="commit-770"></a>
### 770 · feat: add members of SystemAddress {#commit-770}

[4b258a836da86a38f0bcb81bf552c3b3cd2fa7f3](https://github.com/EndstoneMC/endstone/commit/4b258a836da86a38f0bcb81bf552c3b3cd2fa7f3) · 2024-04-25T16:08:33Z · Vincent (author and committer).

Replaces opaque SystemAddress with socket storage IPv4/IPv6 union and debug port, adds RakNetGUID/system index plus136/16-byte size assertions and platform headers. Layout groundwork, no new public endpoint yet.


<a id="commit-771"></a>
### 771 · feat: update NetworkIdentifier class structure {#commit-771}

[156a2a2d712eea67df88f042cd9718de1c3241c6](https://github.com/EndstoneMC/endstone/commit/156a2a2d712eea67df88f042cd9718de1c3241c6) · 2024-04-25T16:35:57Z · Vincent (author and committer).

Models160-byte NetworkIdentifier nether ID/GUID/address/type offsets and reorders plugin-loader includes before Windows header. Native layout now explicit; include ordering does not change loader algorithms.


<a id="commit-772"></a>
### 772 · feat: implement getAddress and getPort in NetworkIdentifier class {#commit-772}

[aec9e027f6fb8b62ab1783875dae9255274b37fc](https://github.com/EndstoneMC/endstone/commit/aec9e027f6fb8b62ab1783875dae9255274b37fc) · 2024-04-25T16:48:52Z · Vincent (author and committer).

Implements IP text conversion with inet_ntop and network-order port extraction, replacing native GetPort hook; adds ws2_32 CMake/Conan linkage. Non-AF_INET assumes IPv6, errors return0.0.0.0/:: rather than explicit status. Linux include repaired773.


<a id="commit-773"></a>
### 773 · fix: add arpa/inet.h include to socket_includes.h {#commit-773}

[2e29ff20854b05bfa64df474010d68ddea6a5c54](https://github.com/EndstoneMC/endstone/commit/2e29ff20854b05bfa64df474010d68ddea6a5c54) · 2024-04-25T16:54:30Z · Vincent (author and committer).

Adds arpa/inet.h for Linux inet_ntop declarations used772.


<a id="commit-774"></a>
### 774 · feat: add NetworkIdentifier::getType {#commit-774}

[e440b1fe6538ab6955705f2f0ee1fc7178885ea3](https://github.com/EndstoneMC/endstone/commit/e440b1fe6538ab6955705f2f0ee1fc7178885ea3) · 2024-04-26T00:14:50Z · Vincent (author and committer).

Names NetworkIdentifier transport variants and exposes getType; no parsing or transport support added yet.


<a id="commit-775"></a>
### 775 · feat: hook RakPeerHelper::peerStartup for server RakPeer instance {#commit-775}

[20297a3a58f3746e6c224439f763cfeb49fe57ed](https://github.com/EndstoneMC/endstone/commit/20297a3a58f3746e6c224439f763cfeb49fe57ed) · 2024-04-26T00:16:22Z · Vincent (author and committer).

Captures successful RakPeer startup with incoming connections into global nonowning locator, rejects duplicate capture; adds partial virtual interface through GUID→address and related structs/enums. Ignores purpose enum and relies incoming-count heuristic. No reset/ownership shown; host lifecycle assumption explicit.


<a id="commit-776"></a>
### 776 · feat: retrieve Player's socket address and port from RakNetGUID {#commit-776}

[9c8b340969c0cd75e48ebefd9846efb36727e6be](https://github.com/EndstoneMC/endstone/commit/9c8b340969c0cd75e48ebefd9846efb36727e6be) · 2024-04-26T00:22:14Z · Vincent (author and committer).

Player wrapper constructor resolves RakNet GUID through captured peer, writes socket storage into native NetworkIdentifier, intentionally falls through to address/port extraction; Address/Address6 accepted, NetherNet/Generic throw. Cached fields only declared777, so intermediate source incomplete. No independent peer readiness/null fallback.


<a id="commit-777"></a>
### 777 · feat: add Player::getAddress and Player::getPort {#commit-777}

[2d4473ab94548ba9fd1b6535177e96aa0c101575](https://github.com/EndstoneMC/endstone/commit/2d4473ab94548ba9fd1b6535177e96aa0c101575) · 2024-04-26T00:24:34Z · Vincent (author and committer).

Adds public address string/uint32 port queries and storage, completing776 constructor assignments. Endpoint is cached at wrapper construction, not live transport query; public port width wider than native16bit.


<a id="commit-778"></a>
### 778 · feat(python): update python bindings for endstone::Player {#commit-778}

[502ed0303ec7a05590f5196f104d5b905b8449b3](https://github.com/EndstoneMC/endstone/commit/502ed0303ec7a05590f5196f104d5b905b8449b3) · 2024-04-26T00:27:45Z · Vincent (author and committer).

Adds Python readonly address/port properties and stubs matching C++ accessors; no independent validation or privacy policy inference.


<a id="commit-779"></a>
### 779 · fix: build on Linux {#commit-779}

[fd3f0dfd2cf94e54adb63fa1749b3aa576e7404c](https://github.com/EndstoneMC/endstone/commit/fd3f0dfd2cf94e54adb63fa1749b3aa576e7404c) · 2024-04-26T00:36:03Z · Vincent (author and committer).

Replaces MS-specific unsigned __int64 in RakPeer virtual signature with std::uint64_t to repair Linux compilation. Same intended64bit ABI width.


<a id="commit-797"></a>
### 797 · feat: add ActorType {#commit-797}

[8445778b8a17a127e804be18c50d85a03484da61](https://github.com/EndstoneMC/endstone/commit/8445778b8a17a127e804be18c50d85a03484da61) · 2024-04-29T14:09:50Z · Vincent (author and committer).

Adds ActorType bitmask/category/species enum table through current mobs; no use site or public behavior changed here. Full values read, no independent engineering preference from mirrored enumeration.


<a id="commit-798"></a>
### 798 · feat: add CommandRegistry::HardNonTerminal {#commit-798}

[8a6a83e299ef98988787815090895bada6001a9c](https://github.com/EndstoneMC/endstone/commit/8a6a83e299ef98988787815090895bada6001a9c) · 2024-04-29T14:35:54Z · Vincent (author and committer).

Replaces individual runtime Symbol globals with typed HardNonTerminal enum and uint32 Symbol wrapper/accessor. Existing user parameter mapping retains exact numeric IDs despite renamed Float→Val, String→Id, Message→MessageRoot, Json→JsonObject. Default Symbol becomes0 instead-1; parameter sentinels explicitly preserve UINT32_MAX. Native grammar table modeled, not parser validation.


<a id="commit-799"></a>
### 799 · feat: add Connection::DisconnectFailReason {#commit-799}

[bcf77267074847470c16064c4421f2a898d34f47](https://github.com/EndstoneMC/endstone/commit/bcf77267074847470c16064c4421f2a898d34f47) · 2024-04-29T14:40:45Z · Vincent (author and committer).

Adds native DisconnectFailReason0–115 enumeration, initially private; no disconnect behavior until800. Full declarations read, no inferred error taxonomy design authorship.


<a id="commit-811"></a>
### 811 · feat(python): add bindings for Actor::getRuntimeId {#commit-811}

[6a2f9aa39153d9802d7aaa876db4600cda652e4e](https://github.com/EndstoneMC/endstone/commit/6a2f9aa39153d9802d7aaa876db4600cda652e4e) · 2024-04-29T23:28:23Z · Vincent (author and committer).

Exposes existing Actor runtime ID through Python property/stub, documents C++ getter and enables inherited-member docs. Small cross-language completeness repair.
