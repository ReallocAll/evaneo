<!-- retrieval: {"source_ids":["public:commit:26b4ba59a45c7ffec9ab09e88a4dbe06a03545e6","public:commit:2d8c3d6aa488bb93ca5afea24f03b971674d517e","public:commit:32479ac9e7951887df01f4f6438b5db1d7650741","public:commit:32d455f95b75fc6f44b5e6bc5ed4155c51a3dfa1","public:commit:41c65340830b0e36996d25d3acb8979f0a56fe40","public:commit:4ef78ca8da3c575777b9545c49c8ce6f9a1674ee","public:commit:4ff750578783eedaab48739b7b99d437f69c2117","public:commit:6e924cb6560d973bf743368904636d157d53fff1","public:commit:785f4f8f1975dc12b638197dcd65c958d3698bcb","public:commit:801f9ed64b203b620284f6f65452087b53711177","public:commit:8788793417a2eb2dcd96b87b626bbffc7438b1ad","public:commit:9ec6374625003d2df4cde8dacf82d06294bb3392","public:commit:a7be72ec46b66c4906b720e599a34d0cb794e462","public:commit:a9076c15192ae814a489de9b64f77071a6e5ff45","public:commit:c06839824348c98137a0b194ce904410e2cc0725","public:commit:ce0dca4d09ea5cbe3c76e5a9e2d488b21c9183ff","public:commit:df774a50a3b864bda88e6a8e8952ebe2f8aeeef6","public:commit:e6bc2663bdb82a50200ad29926dad16944bafa13","public:commit:f16dd3a996a67271a4cfe421ff520dfab45e423e","public:commit:f42166f5d91ed9f73f17b4f9a9a8f0302d215418","public:commit:f9ae7a1f0351bfe4a1c1f60d285991ad2c3433ca"],"source_type":"public","date":"2024-01-19..2024-03-03","topics":["lifetime","ffi","testing","build","recovery","api","diagnosis","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Plugin ownership, Python lifetime and host lifecycle {#plugin-ownership-python-lifetime-and-host-lifecycle}

## Result: ownership is redistributed, then redistributed again {#result-ownership-is-redistributed-then-redistributed-again}

The previous unit ended with shared holders, borrowed server/loader relationships and a Python loader object.132 replaces manager-owned plugins and filename-filter associations with bulk loader APIs. The manager uniquely owns loaders and stores borrowed Plugin pointers; CppPluginLoader uniquely owns native plugin objects; PythonPluginLoader retains Python instances in a list. This removes the earlier multiple-filter unique_ptr problem by changing responsibility, rather than permanently standardizing on shared_ptr. Discovery, object ownership, manager lookup and callback execution are now distinct layers.

Clearing the manager disables and clears borrowed lookup/vector entries while loaders and their owned objects remain. Invalid-name objects can remain loader-owned after manager rejection. Duplicate names overwrite name lookup while all accepted pointers remain in the vector. Repeated load calls can append more objects. Native successful library handles are not represented by explicit unload owners; failure branches close handles when no export/instance is obtained. These are observed lifecycle properties, not proof that unloading should be added or that a production leak occurred. Keeping code loaded may be necessary while plugin virtual objects survive, but the design does not document a complete unloading contract here.

## Distribution entry points replace source loading {#distribution-entry-points-replace-source-loading}

133 removes TOML/source-directory loading and uses installed-distribution entry points in group endstone. This deliberately changes discovery scope: the directory argument is ignored by the Python loader, so installed packages in the environment are candidates.141 normalizes entry-point names for metadata lookup, but still assumes that an entry-point name identifies its distribution. That is a narrower workaround than associating metadata with the actual owning distribution. Metadata authors are treated as structured name/email objects; missing/variant metadata and failed entry-point imports are not covered by tests.

The Python loop retains every created plugin. Its trampoline catches a propagated std::exception and returns an empty result for the bulk call. Thus a later failing entry can leave earlier Python objects retained while no batch results reach the manager. A transaction or per-entry isolation policy is not demonstrated. At the endpoint the concrete server invokes all loaders only if its plugins directory already exists; otherwise it merely creates the directory. Installed Python entry points can consequently be skipped on that initial absent-directory path even though their own loader ignores the directory. This follows the inspected endpoint control flow, not an observed runtime incident.

## The dated interpreter/GIL chain matters {#the-dated-interpreter-gil-chain-matters}

135 fixes server member order: declaring the GIL-release guard after the manager means reverse destruction first reacquires the GIL, then destroys manager-owned objects, then finalizes the interpreter. It removes the previous manual refcount workaround and restores initPlugin after bulk Python loading.139 relocates Python embedding from core to runtime globals, reducing core linkage dependencies but losing that local aggregate lifetime.140 then localizes interpreter, Python object and release guard in PythonPluginLoader, in precisely that declaration order, making their reverse destruction relation explicit.

204 reverses140: interpreter/release return to runtime globals while the loader owns only its py::object. Its destructor manually acquires the GIL and calls dec_ref without release. Ordinary member destruction will still decrement the handle, after the local GIL guard is destroyed. This recreates the exact class of manual-refcount problem that prior114/115 had already addressed. The endpoint still contains that implementation. This is a strong static lifetime risk, not a reproduced shutdown crash or proof that it caused the separate Windows hang.

137 adds std::exit(0) in DLL_PROCESS_DETACH with an explicit TODO saying the server otherwise does not exit on Windows for an unknown reason. The statement of unknown cause must survive synthesis. Calling exit in detach has loader-context, shutdown reentrancy and exit-status implications; it is an acknowledged workaround, not evidence of diagnosed root cause. The later ownership changes do not remove it. Global interpreter guards and singleton storage across translation units leave ordering questions that cannot be settled from names alone.

## Native lifecycle and public API boundaries {#native-lifecycle-and-public-api-boundaries}

138 starts loading, enabling and disabling on host lifecycle hooks, before forwarding the respective original calls.204 installs a set-once generic singleton around DedicatedServer at its run loop;206 moves that installation to ServerInstance::startServerThread. The singleton rejects a second set but assumes get is called after initialization and supplies no synchronization. Host startup timing, repeat startup and failure unwinding need explicit tests. No host run is claimed here.

222 moves load callbacks into the manager after all loaders have finished and all accepted pointers are recorded. This supports the documented all-loads-before-enables ordering and removes duplicated server/TestServer loops. It also changes direct callers' behavior: loadPlugins now runs onLoad and can throw after manager state is already populated. enablePlugins uses the existing per-plugin enabled guard. Callback failure handling/rollback is not added. PluginCommand's later command ownership is separately discussed in the command dossier because it borrows plugin lifetime.

The Python API has a concrete unresolved mismatch: PluginLoader.disable_plugin is bound to PluginLoader::enablePlugin, inherited from prior31 and still present at240. PluginManager.disable_plugin is correctly bound; do not conflate those two APIs.223 adds manager enable_plugins and simplifies facade imports, but does not repair the loader binding. Stub/method names alone are not behavioral evidence.

## Validation, attribution and use {#validation-attribution-and-use}

131 removes the Python package lifecycle fixture.221's interface-based TestServer exercises only C++ plugin behavior; imports/color constants test different boundaries. None of the changed tests covers interpreter teardown, all entry-point metadata shapes, partial bulk failures, duplicate plugin names, reloading, borrowed pointers after clear, or host shutdown. The broad noexcept removal192 changes exception propagation but later command metadata setters add narrower noexcept contracts again; textual removal is not a universal ban and defaulted destructors still have implicit exception rules.

Use the chain for cross-runtime ownership reviews: draw actual owners and borrowed edges, include member/global destruction order, distinguish GIL acquisition from object lifetime, and test callback exceptions at the state-mutation boundary. These are evidence-based questions, not claims of one universally preferred holder type. All implementation attribution remains tied to individual commits; external pybind behavior and PR discussions were not comprehensively researched in this unit.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-129"></a>
### 129. refactor: move bedrock headers into endstone_api {#commit-129}

[32d455f95b75fc6f44b5e6bc5ed4155c51a3dfa1](https://github.com/EndstoneMC/endstone/commit/32d455f95b75fc6f44b5e6bc5ed4155c51a3dfa1) · 2024-01-19T03:06:26Z · meaningful

Moves Bedrock headers into the API include tree, removes their standalone interface target and relaxes namespace naming lint for host conventions. Four headers are exact renames; core.h loses only lint suppression. This expands public header exposure and prepares build simplification, but dependent targets still name the deleted alias until130.

Changed paths: `.clang-tidy`, `CMakeLists.txt`, `bedrock_internals/CMakeLists.txt`, `bedrock_internals/include/bedrock/bedrock.h`, `bedrock_internals/include/bedrock/bedrock_log.h`, `bedrock_internals/include/bedrock/common.h`, `bedrock_internals/include/bedrock/core.h`, `bedrock_internals/include/bedrock/dedicated_server.h`, `endstone_api/include/bedrock/bedrock.h`, `endstone_api/include/bedrock/bedrock_log.h`, `endstone_api/include/bedrock/common.h`, `endstone_api/include/bedrock/core.h`, `endstone_api/include/bedrock/dedicated_server.h`.

<a id="commit-130"></a>
### 130. refactor: move bedrock headers into endstone_api {#commit-130}

[f42166f5d91ed9f73f17b4f9a9a8f0302d215418](https://github.com/EndstoneMC/endstone/commit/f42166f5d91ed9f73f17b4f9a9a8f0302d215418) · 2024-01-19T09:44:35Z · small-semantic

Removes obsolete bedrock_internals source export and target links from core/runtime, completing129's header relocation. Small but build-relevant dependency repair, not proof129 built independently.

Changed paths: `conanfile.py`, `endstone_core/CMakeLists.txt`, `endstone_runtime/CMakeLists.txt`.

<a id="commit-131"></a>
### 131. refactor: remove the loading of python plugins from test_package {#commit-131}

[e6bc2663bdb82a50200ad29926dad16944bafa13](https://github.com/EndstoneMC/endstone/commit/e6bc2663bdb82a50200ad29926dad16944bafa13) · 2024-01-19T10:03:03Z · meaningful

Deletes source Python test plugin and its copy/setup/lifecycle assertions; synthetic package host now expects only one C++ plugin. Python binding/import tests are distinct and do not replace this removed lifecycle coverage. No reason or replacement integration result is supplied.

Changed paths: `test_package/conanfile.py`, `test_package/src/test_plugin_python/plugin.toml`, `test_package/src/test_plugin_python/src/test_plugin.py`, `test_package/src/test_server.cpp`.

<a id="commit-132"></a>
### 132. refactor: generalise the plugin loader interface {#commit-132}

[c06839824348c98137a0b194ce904410e2cc0725](https://github.com/EndstoneMC/endstone/commit/c06839824348c98137a0b194ce904410e2cc0725) · 2024-01-19T10:50:47Z · meaningful

Generalizes loader contract to bulk loadPlugins(directory) returning borrowed Plugin pointers. Manager owns unique loaders and borrows plugins; CppPluginLoader now owns unique plugin objects and handles discovery/filtering. This removes shared ownership/filter associations rather than endorsing shared_ptr permanently. Python registration is temporarily commented, manager single-file API/binding removed, and Python holders return to defaults. Linux single-file definition mistakenly remains shared_ptr until133. noexcept directory traversal/regex/allocation can throw; invalid-name plugins remain loader-owned, and clearPlugins clears manager views without necessarily deleting loader-owned objects. disable_plugin misbinding persists.

Changed paths: `endstone_api/include/endstone/plugin/plugin_loader.h`, `endstone_api/include/endstone/plugin/plugin_manager.h`, `endstone_core/include/endstone_core/plugin/cpp_plugin_loader.h`, `endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h`, `endstone_core/include/endstone_core/plugin/python_plugin_loader.h`, `endstone_core/src/endstone_core/endstone_server.cpp`, `endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp`, `endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp`, `endstone_core/src/endstone_core/plugin/python_plugin_loader.cpp`, `endstone_python/python/endstone/plugin.pyi`, `endstone_python/src/endstone_python/plugin/plugin.cpp`, `endstone_python/src/endstone_python/plugin/plugin_loader.cpp`, `endstone_python/src/endstone_python/plugin/plugin_manager.cpp`.

<a id="commit-133"></a>
### 133. feat: implement new python plugin loader {#commit-133}

[4ef78ca8da3c575777b9545c49c8ce6f9a1674ee](https://github.com/EndstoneMC/endstone/commit/4ef78ca8da3c575777b9545c49c8ce6f9a1674ee) · 2024-01-19T11:19:29Z · meaningful

Replaces bespoke TOML/src/sys.modules loader with installed-distribution entry points in group endstone, retaining plugin instances on the Python loader. Directory parameter is unused: discovery is environment-wide. Entry-point name is initially treated as distribution name, author metadata shape is assumed, and one failed entry aborts the whole call. Removes earlier cache/parser implementation and repairs Linux unique_ptr signature. Re-enables loader registration; constructor catches then throw e, potentially slicing exceptions. Plugin context initialization missing from132 is restored135.

Changed paths: `endstone_core/include/endstone_core/plugin/python_plugin_loader.h`, `endstone_core/src/endstone_core/endstone_server.cpp`, `endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp`, `endstone_core/src/endstone_core/plugin/python_plugin_loader.cpp`, `endstone_python/python/endstone/_internal/plugin_description_file.py`, `endstone_python/python/endstone/_internal/plugin_loader.py`.

<a id="commit-134"></a>
### 134. fix: bad cast from raw pointer to shared_ptr {#commit-134}

[32479ac9e7951887df01f4f6438b5db1d7650741](https://github.com/EndstoneMC/endstone/commit/32479ac9e7951887df01f4f6438b5db1d7650741) · 2024-01-19T11:29:08Z · small-semantic

Changes Python adapter cast from shared_ptr<PluginLoader> to raw borrowed pointer to match default pybind holder introduced132. Explicitly repairs bad ownership conversion; py::object continues to own the Python wrapper, so raw pointer alone is not the lifetime owner.

Changed paths: `endstone_core/include/endstone_core/plugin/python_plugin_loader.h`, `endstone_core/src/endstone_core/plugin/python_plugin_loader.cpp`.

<a id="commit-135"></a>
### 135. refactor: remove custom destructor in PythonPluginLoader {#commit-135}

[26b4ba59a45c7ffec9ab09e88a4dbe06a03545e6](https://github.com/EndstoneMC/endstone/commit/26b4ba59a45c7ffec9ab09e88a4dbe06a03545e6) · 2024-01-19T12:02:31Z · meaningful

Moves GIL-release member after manager so reverse destruction reacquires GIL before manager-owned Python objects are destroyed, then removes manual dec_ref/release destructor. This directly addresses the prior lifetime ordering concern using declaration order. Also restores per-plugin initPlugin/logger/context after bulk Python loading. No shutdown test result supplied; later140 localizes this ordering in the Python loader.

Changed paths: `endstone_core/include/endstone_core/endstone_server.h`, `endstone_core/include/endstone_core/plugin/python_plugin_loader.h`, `endstone_core/src/endstone_core/plugin/python_plugin_loader.cpp`.

<a id="commit-137"></a>
### 137. fix: server not exiting on Windows {#commit-137}

[4ff750578783eedaab48739b7b99d437f69c2117](https://github.com/EndstoneMC/endstone/commit/4ff750578783eedaab48739b7b99d437f69c2117) · 2024-01-19T14:30:08Z · meaningful

Calls std::exit(0) from Windows DLL_PROCESS_DETACH with a TODO explicitly saying server otherwise fails to exit for unknown reason. Treat as an acknowledged workaround with loader-context/reentrancy and exit-code consequences, not a diagnosed shutdown fix. No evidence of root cause or regression coverage.

Changed paths: `endstone_runtime/src/endstone_runtime/main.cpp`.

<a id="commit-138"></a>
### 138. feat: add hooks to load and unload plugins {#commit-138}

[41c65340830b0e36996d25d3acb8979f0a56fe40](https://github.com/EndstoneMC/endstone/commit/41c65340830b0e36996d25d3acb8979f0a56fe40) · 2024-01-19T14:38:41Z · meaningful

Hooks host startServerThread to load plugins and event-coordinator started/stopped callbacks to enable/disable them, each before forwarding original. Connects previously synthetic lifecycle to native host timing. Callback ordering is observable; no exception isolation or actual-host startup/shutdown test is added.

Changed paths: `endstone_api/include/bedrock/server_instance.h`, `endstone_runtime/src/bedrock/server_instance.cpp`.

<a id="commit-139"></a>
### 139. feat: remove endstone_core's dependency on pybind11 {#commit-139}

[801f9ed64b203b620284f6f65452087b53711177](https://github.com/EndstoneMC/endstone/commit/801f9ed64b203b620284f6f65452087b53711177) · 2024-01-19T15:27:21Z · meaningful

Moves Python adapter and embed dependency from core to runtime, removes core interpreter state and direct Python test, and introduces global interpreter/release owners in runtime main. Reduces core dependency surface but temporarily relies on cross-object/global lifetime ordering. Conan runtime gains pybind dependency while stale core smart_holder define remains. Runtime links become PRIVATE; moved header is exact content reuse.

Changed paths: `README.md`, `conanfile.py`, `endstone_core/CMakeLists.txt`, `endstone_core/include/endstone_core/endstone_server.h`, `endstone_core/include/endstone_core/plugin/python_plugin_loader.h`, `endstone_core/src/endstone_core/endstone_server.cpp`, `endstone_core/src/endstone_core/plugin/python_plugin_loader.cpp`, `endstone_runtime/CMakeLists.txt`, `endstone_runtime/include/endstone_runtime/python_plugin_loader.h`, `endstone_runtime/src/endstone_runtime/main.cpp`, `endstone_runtime/src/endstone_runtime/python/python_plugin_loader.cpp`, `test_package/src/test_server.cpp`.

<a id="commit-140"></a>
### 140. refactor: have the lifecycle of python interpret to be managed by PythonPluginLoader {#commit-140}

[f16dd3a996a67271a4cfe421ff520dfab45e423e](https://github.com/EndstoneMC/endstone/commit/f16dd3a996a67271a4cfe421ff520dfab45e423e) · 2024-01-21T23:57:36Z · meaningful

Moves interpreter ownership from runtime globals into PythonPluginLoader members ordered interpreter, object, GIL-release guard. Reverse destruction reacquires GIL, destroys object, then finalizes interpreter; constructor acquires GIL while creating Python loader after release guard initialization. Encapsulates runtime lifetime with its owner, but assumes a single suitable interpreter-owning loader and does not establish arbitrary subinterpreter/thread safety. Unknown Windows detach exit workaround remains.

Changed paths: `endstone_runtime/include/endstone_runtime/python_plugin_loader.h`, `endstone_runtime/src/endstone_runtime/main.cpp`, `endstone_runtime/src/endstone_runtime/python/python_plugin_loader.cpp`.

<a id="commit-141"></a>
### 141. feat: improve plugin metadata lookup {#commit-141}

[f9ae7a1f0351bfe4a1c1f60d285991ad2c3433ca](https://github.com/EndstoneMC/endstone/commit/f9ae7a1f0351bfe4a1c1f60d285991ad2c3433ca) · 2024-01-21T23:57:58Z · small-semantic

Normalizes hyphens to underscores before distribution metadata lookup. Still assumes entry-point name identifies the owning distribution; this is a narrow workaround, not a complete entry-point/distribution association model. No metadata variation test added.

Changed paths: `endstone_python/python/endstone/_internal/plugin_loader.py`.

<a id="commit-145"></a>
### 145. feat: add endstone server unit test {#commit-145}

[9ec6374625003d2df4cde8dacf82d06294bb3392](https://github.com/EndstoneMC/endstone/commit/9ec6374625003d2df4cde8dacf82d06294bb3392) · 2024-01-27T03:46:51Z · meaningful

Adds GoogleTest checks for singleton identity/no-throw construction and Minecraft version forwarding using a locally defined Common::getGameVersionString returning a fixture string. This proves intended seam and source coverage, not live host symbol/ABI validity; test was not executed.

Changed paths: `endstone_core/test/test_endstone_server.cpp`.

<a id="commit-171"></a>
### 171. refactor: getGameVersionString {#commit-171}

[6e924cb6560d973bf743368904636d157d53fff1](https://github.com/EndstoneMC/endstone/commit/6e924cb6560d973bf743368904636d157d53fff1) · 2024-01-31T16:54:04Z · mechanical_scope

Changes synthetic host game-version string to an explicitly dummy label. Fixture clarity only; no production host lookup change.

Changed paths: `test_package/src/dummy_bedrock.cpp`.

<a id="commit-186"></a>
### 186. fix: compile error due to renaming {#commit-186}

[2d8c3d6aa488bb93ca5afea24f03b971674d517e](https://github.com/EndstoneMC/endstone/commit/2d8c3d6aa488bb93ca5afea24f03b971674d517e) · 2024-02-01T17:28:24Z · small-semantic

Repairs manager reference to renamed PluginDescription::VALID_NAME after185. Narrow compile correction; earlier style title hid a coordinated API rename requirement.

Changed paths: `src/endstone_core/plugin/endstone_plugin_manager.cpp`.

<a id="commit-187"></a>
### 187. refactor: project code structure {#commit-187}

[a9076c15192ae814a489de9b64f77071a6e5ff45](https://github.com/EndstoneMC/endstone/commit/a9076c15192ae814a489de9b64f77071a6e5ff45) · 2024-02-05T11:55:04Z · meaningful

Moves implementation headers into endstone/detail and puts public API in endstone namespace, implementation/bindings in endstone::detail, with hook/os namespace changes across all consumers/tests. This is an ABI/source-compatibility change beyond relocation. Linux os.cpp mistakenly uses endstone::os instead of declared endstone::detail::os until208. ENDSTONE_PLUGIN macro still returns unqualified Plugin outside namespace; test plugin's using directive masks that consumer assumption. Includes one double-slash path later cleaned198. Full1,241-line rename-aware patch read in contiguous display ranges; no omitted changes.

Changed paths: `include/endstone/detail/endstone_server.h`, `include/endstone/detail/hook.h`, `include/endstone/detail/logger_factory.h`, `include/endstone/detail/os.h`, `include/endstone/detail/plugin/cpp_plugin_loader.h`, `include/endstone/detail/plugin/endstone_plugin_manager.h`, `include/endstone/detail/plugin/python_plugin_loader.h`, `include/endstone/detail/python.h`, `include/endstone/detail/spdlog/bedrock_level_formatter.h`, `include/endstone/detail/spdlog/bedrock_log_sink.h`, `include/endstone/detail/spdlog/bedrock_text_formatter.h`, `include/endstone/detail/spdlog/spdlog_adapter.h`, `include/endstone/logger.h`, `include/endstone/plugin/plugin.h`, `include/endstone/plugin/plugin_description.h`, `include/endstone/plugin/plugin_loader.h`, `include/endstone/plugin/plugin_manager.h`, `include/endstone/server.h`, `include/endstone/util/color_format.h`, `include/endstone_core/endstone_server.h`, `include/endstone_core/logger_factory.h`, `include/endstone_core/plugin/cpp_plugin_loader.h`, `include/endstone_core/plugin/endstone_plugin_manager.h`, `include/endstone_core/spdlog/bedrock_level_formatter.h`, `include/endstone_core/spdlog/bedrock_log_sink.h`, `include/endstone_core/spdlog/bedrock_text_formatter.h`, `include/endstone_core/spdlog/spdlog_adapter.h`, `include/endstone_python/endstone_python.h`, `include/endstone_runtime/hook.h`, `include/endstone_runtime/platform.h`, `include/endstone_runtime/python_plugin_loader.h`, `src/endstone_core/endstone_server.cpp`, `src/endstone_core/logger_factory.cpp`, `src/endstone_core/plugin/cpp_plugin_loader.cpp`, `src/endstone_core/plugin/endstone_plugin_manager.cpp`, `src/endstone_core/spdlog/bedrock_level_formatter.cpp`, `src/endstone_core/spdlog/bedrock_log_sink.cpp`, `src/endstone_core/spdlog/bedrock_text_formatter.cpp`, `src/endstone_core/spdlog/spdlog_adapter.cpp`, `src/endstone_python/color_format.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/logger.cpp`, `src/endstone_python/plugin/plugin.cpp`, `src/endstone_python/plugin/plugin_description.cpp`, `src/endstone_python/plugin/plugin_loader.cpp`, `src/endstone_python/plugin/plugin_manager.cpp`, `src/endstone_python/server.cpp`, `src/endstone_runtime/bedrock/bedrock_log.cpp`, `src/endstone_runtime/bedrock/command_registry.cpp`, `src/endstone_runtime/bedrock/common.cpp`, `src/endstone_runtime/bedrock/dedicated_server.cpp`, `src/endstone_runtime/bedrock/server_instance.cpp`, `src/endstone_runtime/linux/hook.cpp`, `src/endstone_runtime/linux/os.cpp`, `src/endstone_runtime/linux/platform.cpp`, `src/endstone_runtime/main.cpp`, `src/endstone_runtime/plugin/python_plugin_loader.cpp`, `src/endstone_runtime/python/python_plugin_loader.cpp`, `src/endstone_runtime/windows/hook.cpp`, `src/endstone_runtime/windows/os.cpp`, `src/endstone_runtime/windows/platform.cpp`, `test_package/src/test_plugin.cpp`, `test_package/src/test_server.cpp`, `tests/test_endstone_server.cpp`, `tests/test_logger.cpp`.

<a id="commit-204"></a>
### 204. refactor: add Singleton<T> for singleton pattern {#commit-204}

[df774a50a3b864bda88e6a8e8952ebe2f8aeeef6](https://github.com/EndstoneMC/endstone/commit/df774a50a3b864bda88e6a8e8952ebe2f8aeeef6) · 2024-03-03T15:55:49Z · meaningful

Introduces a generic set-once Singleton with unique_ptr storage, throwing on replacement but dereferencing without an initialization check. EndstoneServer becomes publicly constructible around DedicatedServer and is installed at the run-loop hook; Python loader registration follows. Interpreter/GIL-release ownership moves back from loader members to runtime globals. The loader again manually dec_ref()s its py::object without release(), recreating the prior114/115 double-decrement risk, now with a GIL guard ending before ordinary member destruction. Replaces the server GTest with VersionCommand code rather than preserving host lifecycle coverage; package tests temporarily use a dummy host. Adds a command-map skeleton with locked clearing and unlocked lookup, default version registration still stubbed.

Changed paths: `include/bedrock/command/command_registry.h`, `include/endstone/command/command_map.h`, `include/endstone/detail/command/command_map.h`, `include/endstone/detail/command/defaults/version_command.h`, `include/endstone/detail/plugin/python_plugin_loader.h`, `include/endstone/detail/server.h`, `include/endstone/detail/singleton.h`, `src/endstone_core/command/command_map.cpp`, `src/endstone_core/command/defaults/version_command.cpp`, `src/endstone_core/server.cpp`, `src/endstone_runtime/bedrock/dedicated_server.cpp`, `src/endstone_runtime/bedrock/server_instance.cpp`, `src/endstone_runtime/main.cpp`, `src/endstone_runtime/plugin/python_plugin_loader.cpp`, `test_package/src/test_server.cpp`, `tests/test_endstone_server.cpp`.

<a id="commit-205"></a>
### 205. refactor: use direct instance reference {#commit-205}

[a7be72ec46b66c4906b720e599a34d0cb794e462](https://github.com/EndstoneMC/endstone/commit/a7be72ec46b66c4906b720e599a34d0cb794e462) · 2024-03-03T16:44:00Z · mechanical

Simplifies Singleton getInstance from *pointer.get() to *pointer. Null initialization and synchronization behavior are unchanged.

Changed paths: `include/endstone/detail/singleton.h`.

<a id="commit-206"></a>
### 206. refactor: pass ServerInstance ref to EndstoneServer constructor {#commit-206}

[ce0dca4d09ea5cbe3c76e5a9e2d488b21c9183ff](https://github.com/EndstoneMC/endstone/commit/ce0dca4d09ea5cbe3c76e5a9e2d488b21c9183ff) · 2024-03-03T16:44:48Z · meaningful

Moves EndstoneServer construction and Python-loader registration from DedicatedServer run loop to ServerInstance::startServerThread, before the original host call. Removes the DedicatedServer shim and changes the stored borrowed host reference. This changes lifecycle timing and host dependency, not merely naming; package fixture is updated separately at209. No proof is supplied that all referenced host subsystems are initialized at this point.

Changed paths: `include/endstone/detail/server.h`, `src/endstone_core/server.cpp`, `src/endstone_runtime/bedrock/dedicated_server.cpp`, `src/endstone_runtime/bedrock/server_instance.cpp`.

<a id="commit-222"></a>
### 222. refactor: move plugin loading and enabling codes to PluginManager {#commit-222}

[8788793417a2eb2dcd96b87b626bbffc7438b1ad](https://github.com/EndstoneMC/endstone/commit/8788793417a2eb2dcd96b87b626bbffc7438b1ad) · 2024-03-03T23:29:22Z · meaningful

Moves onLoad callbacks/logging into PluginManager::loadPlugins after all loaders finish and accepted plugins have been recorded; adds enablePlugins to the abstract manager and core implementation. Server and TestServer delegate instead of duplicating loops, with existing enablePlugin guard retaining idempotence. This changes loadPlugins contract for direct callers and callback exception boundary: objects are already registered if onLoad throws, and remaining callbacks may not run. Public virtual-table/API shape changes; no rollback test is added.

Changed paths: `include/endstone/detail/plugin/plugin_manager.h`, `include/endstone/plugin/plugin_manager.h`, `src/endstone_core/plugin/plugin_manager.cpp`, `src/endstone_core/server.cpp`, `test_package/src/test_server.cpp`.

<a id="commit-223"></a>
### 223. refactor: python bindings {#commit-223}

[785f4f8f1975dc12b638197dcd65c958d3698bcb](https://github.com/EndstoneMC/endstone/commit/785f4f8f1975dc12b638197dcd65c958d3698bcb) · 2024-03-03T23:42:36Z · meaningful

Replaces dynamic import loops in Python facade modules with direct extension imports while preserving exported names and Python Plugin subclass. Adds enable_plugins binding and stub corresponding to222; ignores generated stubs directory. Bootstrap changes are formatting only. Import ordering and module export behavior remain source-reviewed, not runtime-tested; this does not repair the older PluginLoader disable_plugin binding mismatch.

Changed paths: `.gitignore`, `python/src/endstone/_internal/bootstrap/base.py`, `python/src/endstone/logger.py`, `python/src/endstone/plugin.py`, `python/src/endstone/plugin.pyi`, `python/src/endstone/server.py`, `python/src/endstone/util.py`, `src/endstone_python/plugin/plugin_manager.cpp`.
