<!-- retrieval: {"source_ids":["public:commit:53c9dc16ecc7885ea5ff1eb1a9b0faf05b96b27d","public:commit:53e6cfb2531a08d30a7587c36f9ad07a55200ffc","public:commit:5fa458dd362873bbd1948194fcd88b5ec3f575cb","public:commit:635376effe8e74a9ba8213d0aa8d69ca3e137727","public:commit:6a109e67f243d83e5f07649435adc29834776ed1","public:commit:7da175ca46bd5b20c4a5fa9ea0218a401951ac7c","public:commit:82c624050933cb358a0bf2805046eef1dd0e45f4","public:commit:86bf982173694d00da7f940bb4ad78984d60d6ca","public:commit:87346ffdeed101a4f9fa557c3d07791e89835411","public:commit:8ef787b74104d0141b97464cd00e8ca6e9abca90","public:commit:93c1560f49fda668d11ace645e726ddcebe870b7","public:commit:9444a576d3c4ef414a7c137e220df08828adf718","public:commit:aa6914541f2a41e1b88ae0c36613fa7440b6e1c4","public:commit:b284ec186a7f27b4c84b2cb4b7d9647506ca2cc5","public:commit:ba774f32fcec0dc5c65984da36db2c641b1a2d94","public:commit:c3ed44b3f39b8c1ce681ba09d8c76880946901d8","public:commit:d9ddafb5f8babfb23e0caa5f245169ac26ff5594","public:commit:f909f6205edff4971b4d6a6ec93a9defacb94fb0"],"source_type":"public","date":"2024-10-09..2024-10-17","topics":["lifetime","concurrency","ffi","testing","build","api","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Resource-pack integration and lifecycle {#resource-pack-integration-and-lifecycle}

Scope: Endstone commits 1801–1920, September 14–October 22, 2024. These notes follow related implementation areas during this period.

## Integration stages and explicit choices {#integration-stages-and-explicit-choices}

Resource-pack support is built in observable stages: recover native identity/path/report/repository interfaces (1876–1881), install a pass-through initialization hook (1882), register a source (1883), delegate pack construction to the engine (1884), discover files (1887), align source lifetime with server lifetime (1888), obtain and install a client stack (1889–1892), reject null pack construction (1893), and supply optional client content keys (1896). Declaration-only steps receive credit for recovered interfaces, not finished loading behavior. The archive parser, manifest factory and encryption implementation remain native dependencies.

Two motives are explicit. The source must not outlive the server, replacing a function/static lifetime with server-owned unique_ptr storage. The ADDON client stack is chosen because a comment says BDS does not otherwise use it and it is sent to clients, avoiding conflicts. This makes the integration strategy intelligible without claiming it was independently tested. Splitting early server construction from init permits pack discovery to obtain a logger/source earlier, but creates a phase contract around the native server pointer. Level/scoreboard initialization also moves earlier in the thread-start sequence before PostWorld plugins.

Negative examples qualify reuse. Pack equality ignores build metadata while hashing includes the full version string, violating equal-key hash expectations for that case. Initial loading retains null packs until 1893. getStack assumes non-null selected stacks; setStack mutates before rejecting unsupported compose=true; the actual caller uses false. SemVersion does not insert separators into supplied prerelease/build strings. These are bounded source observations, not an exhaustive archive/security audit or proof every typical pack fails.

Sidecar key handling validates a trimmed 32-byte value and inserts it into the network content-key map, without logging the value or replacing existing entries. No keys or archives were acquired/executed during review, and no secret content is reproduced. Exact maps, full pack source/level/lifecycle files and canonical patch hashes preserve the boundary between authored integration and native delegated behavior. There are no pack-loading behavior tests in this assigned patch set.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1876"></a>
### Commit 1876 · feat: add PackIdVersion and SemVersion {#commit-1876}

Source: [53e6cfb2531a08d30a7587c36f9ad07a55200ffc](https://github.com/EndstoneMC/endstone/commit/53e6cfb2531a08d30a7587c36f9ad07a55200ffc). Authored 2024-10-09T12:28:23Z; committed 2024-10-09T12:28:23Z. Git author: Vincent; committer: Vincent.


Introduces PackIdVersion, SemVersion and UUID serialization alongside pack-request identity fields. A static inconsistency matters downstream: equality ignores build metadata and pack_type, while the hash includes the full version string, so equal versions with different build metadata can hash differently. UUID high-word serialization also lacks the later mask repaired in 1887. These are limits on reusing the model, not claims that every normal release-version pack fails.

Changed-source navigation: `include/bedrock/core/resource/pack_id_version.h`, `include/bedrock/core/resource/pack_type.h`, `include/bedrock/core/sem_ver/sem_version.h`, `include/bedrock/network/server_network_handler.h`, `include/bedrock/platform/uuid.h`, `src/endstone_runtime/bedrock/core/sem_ver/sem_version.cpp`, `src/endstone_runtime/bedrock/network/server_network_handler.cpp`; plus 1 paths not listed here.

<a id="commit-1877"></a>
### Commit 1877 · feat: add more resource pack-related classes {#commit-1877}

Source: [9444a576d3c4ef414a7c137e220df08828adf718](https://github.com/EndstoneMC/endstone/commit/9444a576d3c4ef414a7c137e220df08828adf718). Authored 2024-10-09T13:59:01Z; committed 2024-10-09T13:59:01Z. Git author: Vincent; committer: Vincent.


Adds native path, resource filesystem, pack strategy, report, settings, preload and signature declarations. This is substantial ABI groundwork but not yet a functioning Endstone pack loader. NonOwnerPointer free comparison functions reach a private get(), a compile-oriented issue later removed by member comparisons. Native archive parsing and signature behavior remain delegated/unreviewed rather than authored or validated here.

Changed-source navigation: `include/bedrock/core/file/path.h`, `include/bedrock/core/resource/pack_type.h`, `include/bedrock/core/resource/resource_helper.h`, `include/bedrock/core/resource/resource_util.h`, `include/bedrock/core/utility/non_owner_pointer.h`, `include/bedrock/forward.h`, `include/bedrock/locale/i18n.h`; plus 9 paths not listed here.

<a id="commit-1880"></a>
### Commit 1880 · feat: add PackSource, PackManifestFactory, ContentIdentity and ContentKeyProvider {#commit-1880}

Source: [aa6914541f2a41e1b88ae0c36613fa7440b6e1c4](https://github.com/EndstoneMC/endstone/commit/aa6914541f2a41e1b88ae0c36613fa7440b6e1c4). Authored 2024-10-14T18:01:43Z; committed 2024-10-14T18:01:43Z. Git author: Vincent; committer: Vincent.


Adds content identity, key-provider, manifest-factory and PackSource interfaces. The declarations expose the native encrypted-content plumbing needed by later integration, without supplying secret material or bypassing access controls. The loader still lacks discovery and stack installation at this stage.

Changed-source navigation: `include/bedrock/core/resource/content_identity.h`, `include/bedrock/core/resource/resource_helper.h`, `include/bedrock/resources/content_key_provider.h`, `include/bedrock/resources/pack_manifest_factory.h`, `include/bedrock/resources/pack_source.h`, `include/bedrock/resources/resource_pack_stack.h`.

<a id="commit-1881"></a>
### Commit 1881 · feat: add ResourcePackRepository and ResourcePackStack {#commit-1881}

Source: [c3ed44b3f39b8c1ce681ba09d8c76880946901d8](https://github.com/EndstoneMC/endstone/commit/c3ed44b3f39b8c1ce681ba09d8c76880946901d8). Authored 2024-10-14T18:58:12Z; committed 2024-10-14T18:58:12Z. Git author: Vincent; committer: Vincent.


Models ResourcePackRepository's virtual interface, stack ownership and CompositePackSource's borrowed source list. The accompanying shim remains empty. This establishes the ownership vocabulary and native call surface; pack discovery and concrete registration arrive later, so it is not recorded as complete resource-pack support.

Changed-source navigation: `include/bedrock/core/resource/resource_helper.h`, `include/bedrock/forward.h`, `include/bedrock/resources/invalid_packs_filter_group.h`, `include/bedrock/resources/pack_manifest_factory.h`, `include/bedrock/resources/pack_source.h`, `include/bedrock/resources/resource_pack_repository.h`, `include/bedrock/resources/resource_pack_repository_interface.h`; plus 2 paths not listed here.

<a id="commit-1882"></a>
### Commit 1882 · feat: hook ResourcePackRepository::_initializePackSource {#commit-1882}

Source: [93c1560f49fda668d11ace645e726ddcebe870b7](https://github.com/EndstoneMC/endstone/commit/93c1560f49fda668d11ace645e726ddcebe870b7). Authored 2024-10-14T19:59:45Z; committed 2024-10-14T19:59:45Z. Git author: Vincent; committer: Vincent.


Adds the repository's _initializePackSource hook and Windows/Linux symbol addresses while still passing through to the original. CompositePackSource receives append, clear and source-list operations over borrowed pointers. The interception point is ready, but no Endstone source is installed until 1883.

Changed-source navigation: `include/bedrock/resources/pack_source.h`, `include/bedrock/resources/resource_pack_repository.h`, `python/src/endstone/_internal/symbols.toml`, `src/endstone_runtime/bedrock/resources/pack_source.cpp`, `src/endstone_runtime/bedrock/resources/resource_pack_repository.cpp`.

<a id="commit-1883"></a>
### Commit 1883 · feat: add EndstonePackSource {#commit-1883}

Source: [b284ec186a7f27b4c84b2cb4b7d9647506ca2cc5](https://github.com/EndstoneMC/endstone/commit/b284ec186a7f27b4c84b2cb4b7d9647506ca2cc5). Authored 2024-10-14T23:22:15Z; committed 2024-10-14T23:22:15Z. Git author: Vincent; committer: Vincent.


Registers a static EndstonePackSource after the native repository's original initialization. It owns Pack unique_ptrs, identifies user/resource origin, and leaves load unimplemented. The static lifetime is later explicitly rejected in 1888 because it can outlast the server. This first step should not be presented as the final ownership design or as successful file loading.

Changed-source navigation: `include/bedrock/resources/pack.h`, `include/bedrock/resources/pack_source.h`, `include/endstone/detail/packs/endstone_pack_source.h`, `src/endstone_core/packs/endstone_pack_source.cpp`, `src/endstone_runtime/bedrock/resources/resource_pack_repository.cpp`.

<a id="commit-1884"></a>
### Commit 1884 · feat: add Pack::createPack {#commit-1884}

Source: [5fa458dd362873bbd1948194fcd88b5ec3f575cb](https://github.com/EndstoneMC/endstone/commit/5fa458dd362873bbd1948194fcd88b5ec3f575cb). Authored 2024-10-15T00:05:28Z; committed 2024-10-15T00:05:28Z. Git author: Vincent; committer: Vincent.


Adds Pack::createPack as a trampoline to the native engine with corresponding symbols. It passes resource location, manifest factory, key provider, reports and subdirectory to the existing engine implementation. Endstone is integrating that parser, not implementing archive decoding in this patch.

Changed-source navigation: `include/bedrock/resources/pack.h`, `python/src/endstone/_internal/symbols.toml`, `src/endstone_runtime/bedrock/resources/pack.cpp`.

<a id="commit-1885"></a>
### Commit 1885 · feat: add constructors for PackReport and SemVersion {#commit-1885}

Source: [7da175ca46bd5b20c4a5fa9ea0218a401951ac7c](https://github.com/EndstoneMC/endstone/commit/7da175ca46bd5b20c4a5fa9ea0218a401951ac7c). Authored 2024-10-15T00:06:10Z; committed 2024-10-15T00:06:10Z. Git author: Vincent; committer: Vincent.


Implements version/report helpers and discovery-state scaffolding. A default SemVersion is 0.0.0 but invalid; wildcard state is valid. The constructor concatenates prerelease/build strings without adding separators, so callers must not assume general SemVer normalization. Pack report aggregation is implemented while loading is still incomplete. These source-level details qualify later use of version strings as identities.

Changed-source navigation: `include/bedrock/core/sem_ver/sem_version.h`, `include/bedrock/resources/content_key_provider.h`, `include/bedrock/resources/pack_error.h`, `include/bedrock/resources/pack_manifest_factory.h`, `include/bedrock/resources/pack_source.h`, `include/endstone/detail/packs/endstone_pack_source.h`, `src/endstone_core/packs/endstone_pack_source.cpp`; plus 3 paths not listed here.

<a id="commit-1886"></a>
### Commit 1886 · feat: add member variables for ResourcePackRepository {#commit-1886}

Source: [f909f6205edff4971b4d6a6ec93a9defacb94fb0](https://github.com/EndstoneMC/endstone/commit/f909f6205edff4971b4d6a6ec93a9defacb94fb0). Authored 2024-10-15T00:53:19Z; committed 2024-10-15T00:53:19Z. Git author: Vincent; committer: Vincent.


Expands repository ownership members and network content-key state, replacing more opaque layout placeholders. Some references are later changed to pointers for Clang compatibility in 1895. This is typed native representation, not a new pack-discovery algorithm or evidence of validated offsets.

Changed-source navigation: `include/bedrock/forward.h`, `include/bedrock/network/server_network_handler.h`, `include/bedrock/resources/content_key_provider.h`, `include/bedrock/resources/resource_pack_repository.h`, `include/bedrock/world/minecraft.h`.

<a id="commit-1887"></a>
### Commit 1887 · feat(pack): add support for loading zipped resource packs (.mcpack, .zip) on server startup {#commit-1887}

Source: [8ef787b74104d0141b97464cd00e8ca6e9abca90](https://github.com/EndstoneMC/endstone/commit/8ef787b74104d0141b97464cd00e8ca6e9abca90). Authored 2024-10-15T13:27:00Z; committed 2024-10-15T13:27:00Z. Git author: Vincent; committer: Vincent.


Discovers regular files with case-sensitive .zip/.mcpack extensions and delegates construction to native Pack::createPack using a Raw filesystem location. Native reports are logged. Initially all returned pointers are retained, including null; 1893 adds the required skip. A direct LoggerFactory path is explicitly used because the Endstone server may not yet be initialized. Path utilities, hashing and UUID high-word masking are also implemented. Static source/path capture is revised in 1888. No archive contents or external pack code were executed during review.

Changed-source navigation: `include/bedrock/core/file/path.h`, `include/bedrock/core/resource/resource_helper.h`, `include/bedrock/resources/pack_error.h`, `include/bedrock/resources/pack_source.h`, `include/endstone/detail/packs/endstone_pack_source.h`, `src/endstone_core/packs/endstone_pack_source.cpp`, `src/endstone_runtime/bedrock/core/file/path.cpp`; plus 5 paths not listed here.

<a id="commit-1888"></a>
### Commit 1888 · fix: ensure the lifecycle of pack sources does not exceed the server instance {#commit-1888}

Source: [635376effe8e74a9ba8213d0aa8d69ca3e137727](https://github.com/EndstoneMC/endstone/commit/635376effe8e74a9ba8213d0aa8d69ca3e137727). Authored 2024-10-15T16:26:51Z; committed 2024-10-15T16:26:51Z. Git author: Vincent; committer: Vincent.


The message explicitly requires the pack source not to outlive the Endstone server. Static storage becomes a server-owned unique_ptr, while default construction is split from init(ServerInstance&) so the locator can provide an early server during pack discovery. This improves ownership alignment but creates a meaningful phase distinction: the native server pointer is not usable until init. The composite repository still borrows the source; shutdown ordering and early consumers must respect that relationship.

Changed-source navigation: `include/endstone/detail/server.h`, `src/endstone_core/packs/endstone_pack_source.cpp`, `src/endstone_core/server.cpp`, `src/endstone_runtime/bedrock/resources/resource_pack_repository.cpp`, `src/endstone_runtime/bedrock/world/events/server_instance_event_coordinator.cpp`.

<a id="commit-1889"></a>
### Commit 1889 · feat: add ResourcePackManager {#commit-1889}

Source: [87346ffdeed101a4f9fa557c3d07791e89835411](https://github.com/EndstoneMC/endstone/commit/87346ffdeed101a4f9fa557c3d07791e89835411). Authored 2024-10-16T10:29:01Z; committed 2024-10-16T10:29:01Z. Git author: Vincent; committer: Vincent.


Models ResourcePackManager and represents the repository through NonOwnerPointer, with non-const get-or-create access. Null comparisons become members, resolving private-get access from the earlier free functions. This clarifies weak/borrowed native state without turning it into owned state; subsequent getStack still assumes selected pointers are present.

Changed-source navigation: `include/bedrock/core/resource/resource_helper.h`, `include/bedrock/core/utility/non_owner_pointer.h`, `include/bedrock/forward.h`, `include/bedrock/locale/i18n.h`, `include/bedrock/resources/resource_pack_manager.h`, `include/bedrock/world/minecraft.h`, `include/endstone/detail/server.h`; plus 3 paths not listed here.

<a id="commit-1890"></a>
### Commit 1890 · feat: add ResourcePackManager::getStack {#commit-1890}

Source: [6a109e67f243d83e5f07649435adc29834776ed1](https://github.com/EndstoneMC/endstone/commit/6a109e67f243d83e5f07649435adc29834776ed1). Authored 2024-10-16T14:46:11Z; committed 2024-10-16T14:46:11Z. Git author: Vincent; committer: Vincent.


Implements getStack selection across five stack types, throws for an invalid selector, and types Level's resource-pack manager accessors. It does not validate a selected null stack before dereferencing. PackInstance construction also leaves the is_dependent parameter unused. These concrete limits are preserved without extending into an unbounded audit of the engine's stack invariants.

Changed-source navigation: `include/bedrock/core/resource/resource_helper.h`, `include/bedrock/resources/resource_pack_manager.h`, `include/bedrock/resources/resource_pack_stack.h`, `include/bedrock/world/level/level_interface.h`, `include/bedrock/world/minecraft.h`, `src/endstone_runtime/bedrock/resources/resource_pack_manager.cpp`, `src/endstone_runtime/bedrock/resources/resource_pack_stack.cpp`; plus 1 paths not listed here.

<a id="commit-1891"></a>
### Commit 1891 · refactor: remove hook for sendServerLevelInitialized and associated symbols {#commit-1891}

Source: [d9ddafb5f8babfb23e0caa5f245169ac26ff5594](https://github.com/EndstoneMC/endstone/commit/d9ddafb5f8babfb23e0caa5f245169ac26ff5594). Authored 2024-10-16T15:21:13Z; committed 2024-10-16T15:21:13Z. Git author: Vincent; committer: Vincent.


Moves EndstoneLevel/scoreboard creation from the level-initialized hook into server thread startup before command-map initialization and PostWorld plugins. GameSession level retrieval validates the owner entity/weak level, and native stack deserialization becomes callable. The order makes resource-pack installation available at level construction, but returned native pointers remain borrowed. Removed hook addresses and new call sites are covered, not assumed equivalent solely from similar names.

Changed-source navigation: `include/bedrock/core/utility/non_owner_pointer.h`, `include/bedrock/entity/gamerefs_entity/owner_storage_entity.h`, `include/bedrock/network/client_or_server_network_system.h`, `include/bedrock/resources/resource_pack_stack.h`, `include/bedrock/world/game_session.h`, `include/bedrock/world/minecraft.h`, `python/src/endstone/_internal/symbols.toml`; plus 4 paths not listed here.

<a id="commit-1892"></a>
### Commit 1892 · feat: automatically send resource packs loaded from .mcpack and .zip to clients {#commit-1892}

Source: [82c624050933cb358a0bf2805046eef1dd0e45f4](https://github.com/EndstoneMC/endstone/commit/82c624050933cb358a0bf2805046eef1dd0e45f4). Authored 2024-10-16T16:38:24Z; committed 2024-10-16T16:38:24Z. Git author: Vincent; committer: Vincent.


Serializes discovered pack IDs and numeric versions, asks the native engine to deserialize a stack, and installs it in the client manager's ADDON slot. A comment explicitly says this slot is unused by BDS yet sent to clients, motivating conflict avoidance. setStack replaces ownership before its unsupported compose=true branch throws; the actual caller uses false and requests a later restack. Empty discovery leaves JSON null rather than an explicit array. Client delivery and engine acceptance were not run, so these are observed contracts and limits rather than proven end-to-end outcomes.

Changed-source navigation: `include/bedrock/core/sem_ver/sem_version.h`, `include/bedrock/resources/pack.h`, `include/bedrock/resources/pack_manifest.h`, `include/bedrock/resources/pack_manifest_factory.h`, `include/bedrock/resources/pack_source.h`, `include/bedrock/resources/resource_pack_manager.h`, `include/bedrock/resources/resource_pack_stack.h`; plus 9 paths not listed here.

<a id="commit-1893"></a>
### Commit 1893 · feat: output names of loaded resource packs {#commit-1893}

Source: [86bf982173694d00da7f940bb4ad78984d60d6ca](https://github.com/EndstoneMC/endstone/commit/86bf982173694d00da7f940bb4ad78984d60d6ca). Authored 2024-10-16T17:10:27Z; committed 2024-10-16T17:10:27Z. Git author: Vincent; committer: Vincent.


Skips a null Pack::createPack result before storing or dereferencing it, repairing the invalid-pack path introduced in 1887. Adds name/version/ID logging and more manifest/error metadata. This is a concrete validation boundary: construction failure is logged and omitted from later enumeration. It does not imply that every malformed archive error is caught by Endstone itself.

Changed-source navigation: `include/bedrock/resources/min_engine_version.h`, `include/bedrock/resources/pack_capabililty.h`, `include/bedrock/resources/pack_error.h`, `include/bedrock/resources/pack_manifest.h`, `include/bedrock/shared_types/molang/molang_version.h`, `src/endstone_core/packs/endstone_pack_source.cpp`, `src/endstone_runtime/bedrock/resources/pack_error.cpp`; plus 1 paths not listed here.

<a id="commit-1895"></a>
### Commit 1895 · ci: fix errors to make clang compiler happy again {#commit-1895}

Source: [ba774f32fcec0dc5c65984da36db2c641b1a2d94](https://github.com/EndstoneMC/endstone/commit/ba774f32fcec0dc5c65984da36db2c641b1a2d94). Authored 2024-10-16T17:40:15Z; committed 2024-10-16T17:40:15Z. Git author: Vincent; committer: Vincent.


Addresses Clang compilation through include-cycle/forward-declaration changes, pointer representation in repository members, and opaque unique_ptr placeholders for incompletely modeled native types. The explicit server destructor is removed. These edits are evidence of toolchain feedback and a compatibility repair, not proof that opaque deletion or native ABI behavior is generally safe. No compiler was executed here.

Changed-source navigation: `include/bedrock/resources/pack.h`, `include/bedrock/resources/resource_pack_repository.h`, `include/endstone/detail/level/level.h`, `include/endstone/detail/server.h`, `src/endstone_core/command/command_wrapper.cpp`.

<a id="commit-1896"></a>
### Commit 1896 · feat: add support for encrypted resource packs {#commit-1896}

Source: [53c9dc16ecc7885ea5ff1eb1a9b0faf05b96b27d](https://github.com/EndstoneMC/endstone/commit/53c9dc16ecc7885ea5ff1eb1a9b0faf05b96b27d). Authored 2024-10-17T11:45:52Z; committed 2024-10-17T11:45:52Z. Git author: Vincent; committer: Vincent.


Reads an optional adjacent .key file, trims it, requires exactly 32 bytes, and skips that pack on unreadable/invalid key input. Keys are stored by manifest identity and inserted into the network content-key map during PostWorld initialization; insert does not overwrite an existing entry. The key is not passed as a new argument to Pack::createPack, so the observed role is client content-key delivery rather than a newly authored archive decryptor. Source logs identify packs/paths, not key values. No credential value was printed, stored in the dossier or tested; the identity hash/equality limit from 1876 remains relevant.

Changed-source navigation: `include/endstone/detail/packs/endstone_pack_source.h`, `src/endstone_core/packs/endstone_pack_source.cpp`, `src/endstone_core/server.cpp`.
