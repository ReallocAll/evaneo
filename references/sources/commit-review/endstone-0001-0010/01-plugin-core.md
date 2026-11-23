<!-- retrieval: {"source_ids":["public:commit:1164f2efd4eb3318ea97df76e0bcfd72f66d7e01","public:commit:1226cb2d1393b4b7cc660561c67d88f9a557adf0","public:commit:2f576d357a2f40220d6e3229058a92d33f0c8199","public:commit:3883d65c03185804e3f4f02e483675fbea482912","public:commit:4076a53158fdde21fac1ba5d877073f5d9ccf9c8","public:commit:46beb17a5342b9a707bf82fba52c562e33b999e6","public:commit:713c1dca0c26153853faeb84b79df4e62db90aed","public:commit:8be7040cff93337159a45413ad39034f4fedf7f2","public:commit:9cfc1606a1c885f51a5d898005ae76de5214d2be","public:commit:a75dad798aff8883130437e429713fff1762cc27","public:commit:c4795ad263165de632820a69e1eaa5860e1cf993","public:commit:da1686aaa269ac018fad4262f7b21e9015edb978","public:commit:dcf65292843f0a68a063c656b783e25c4a621c71","public:commit:fe547816b27ad2de4c676f8da9e5567fcbd229d6"],"source_type":"public","date":"2023-12-17..2024-01-05","topics":["lifetime","concurrency","ffi","testing","build","api","diagnosis","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Plugin host, lifecycle and ownership {#plugin-host-lifecycle-and-ownership}

## Context and mechanism {#context-and-mechanism}

The root starts with a C++17 plugin contract, not a functioning Bedrock hook. The exported C factory creates a C++ Plugin whose virtual methods, strings and containers cross the library boundary. C linkage stabilizes the entry-point name; it does not erase compiler, standard-library, object-layout or allocator obligations. This distinction explains why compiler/ABI changes in [build history](02-build-release.md) matter to application architecture.

The implementation acquires concrete shape at commits6–9: a singleton server owns a manager; the manager owns loaded plugins and associates filename regular expressions with loaders; plugin objects borrow their server and loader. A separate name lookup stores raw pointers into the owned collection. Load, enable and disable are distinct phases. The loader installs context/logger before invoking plugin load callback, and enabled state changes precede callback dispatch. LoggerFactory interns loggers by name and protects that map with a mutex. This is specific synchronization for logger lookup/creation; there is no equivalent manager-wide lock or demonstrated thread-safety contract.

## Alternatives and revision chains actually present {#alternatives-and-revision-chains-actually-present}

- Shared loader behavior moves from public PluginLoader at1, to abstract-only interface at2, to core PluginLoaderBase at7, and back to the public loader at30. This is an observed design reversal while Python integration matures. No discussion here establishes a universal preference for header-only APIs or abstract interfaces.
- Manager loading arguments become strings at32 while filesystem work stays inside core. This reduces exposure to filesystem implementation differences; it does not make the remaining C++ ABI portable.
- Owned per-plugin logger wrappers at7 disappear at12 in favor of factory-owned named loggers and common formatting. Removing the wrapper also drops custom metadata prefix use, so it cannot be summarized as an entirely behavior-preserving refactor.
- The original loader association loop moves one unique_ptr once per filter. Subsequent filters can receive an empty pointer. The eventual shared_ptr change at114 copies the same owner into each association and directly fixes this edge case. This is a concrete reason to consider ownership cardinality, not general evidence that shared_ptr is preferable.
- CppPluginLoader initially logs through the global server;83 changes both OS branches to its associated server. That reduces hidden singleton coupling even though the concrete host itself remains singleton-based.

## Failure handling and costs {#failure-handling-and-costs}

Native loading has acquire-library, resolve-entry, call-factory and initialize-plugin phases.9 repairs Linux paths that accidentally used Windows error/cleanup APIs. Libraries are closed on the observed failure paths but successful handles are not represented by an unload owner. Keeping code loaded may protect live virtual objects, but the source does not document a deliberate unloading policy. Throwing factories and exception safety around registration are not tested here.

At the endpoint, duplicate names can replace name-map entries while leaving both objects in the owned collection; missing-file logging does not immediately stop search; regular-expression order comes from an unordered map. Those observations warrant explicit policy/tests, not a claim that a particular failure has occurred. Shared plugin ownership at115 changes deletion timing again. External owners can outlive the manager while borrowed server/loader relationships remain; clearPlugins is not equivalent to proving all plugin objects are destroyed.

## Validation and applicability {#validation-and-applicability}

The package test at8 executes a synthetic host/plugin lifecycle and keeps assertions active in Release.11 adds pointer-overload coverage;23 adds logger identity and threshold tests. Source tests establish intended contracts but were not run in this review. They do not exercise duplicate names, multi-filter loaders, failed exports/factories, callback exceptions, concurrent operations, unload or shutdown ordering. Native host tests later use a dummy Bedrock function, so their scope is deliberately narrower than real-host compatibility.

Use this history when designing plugin ownership, reviewing ABI boundaries, splitting public contracts from implementation, or deciding what a test genuinely proves. Treat the untested edges as questions to validate. The sources do not establish throughput, thread safety, safe unloading or present-day behavior.

## Individual commit evidence {#individual-commit-evidence}



<a id="commit-1"></a>
### 1. feat: add endstone_api and test_package {#commit-1}

- Source: [da1686aaa269ac018fad4262f7b21e9015edb978](https://github.com/EndstoneMC/endstone/commit/da1686aaa269ac018fad4262f7b21e9015edb978)
- Authored: 2023-12-17T23:42:46Z; parent: `empty tree (root)`
- Disposition: meaningful; full actual diff statically reviewed.

Root introduces header-only C++17 API (Server, Logger, Plugin, PluginDescription, PluginLoader, PluginManager), Conan/CMake package metadata, Apache-2.0 licensing and a dynamically exported test plugin. Plugin lifecycle toggles state before callbacks, loaders initialize borrowed server/loader pointers and an owned logger, and name normalization replaces spaces. Test recipe initially does nothing at runtime, so this proves API scaffolding rather than a working host. The public ABI includes STL strings, containers and filesystem; the exported C factory does not make the returned C++ object ABI-neutral. Prior project context is unavailable.

Changed-path evidence: [.clang-format](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/.clang-format) (+30/−0); [.clang-tidy](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/.clang-tidy) (+84/−0); [.git_archival.txt](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/.git_archival.txt) (+4/−0); [.gitignore](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/.gitignore) (+14/−0); [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/CMakeLists.txt) (+8/−0); [LICENSE](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/LICENSE) (+201/−0); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/conanfile.py) (+95/−0); [endstone_api/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/endstone_api/CMakeLists.txt) (+11/−0); [endstone_api/include/endstone/logger.h](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/endstone_api/include/endstone/logger.h) (+75/−0); [endstone_api/include/endstone/plugin/plugin.h](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/endstone_api/include/endstone/plugin/plugin.h) (+143/−0); [endstone_api/include/endstone/plugin/plugin_description.h](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/endstone_api/include/endstone/plugin/plugin_description.h) (+74/−0); [endstone_api/include/endstone/plugin/plugin_loader.h](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/endstone_api/include/endstone/plugin/plugin_loader.h) (+60/−0); [endstone_api/include/endstone/plugin/plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/endstone_api/include/endstone/plugin/plugin_manager.h) (+41/−0); [endstone_api/include/endstone/server.h](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/endstone_api/include/endstone/server.h) (+61/−0); [test_package/.gitignore](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/test_package/.gitignore) (+14/−0); [test_package/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/test_package/CMakeLists.txt) (+11/−0); [test_package/conanfile.py](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/test_package/conanfile.py) (+24/−0); [test_package/src/test_plugin.cpp](https://github.com/EndstoneMC/endstone/blob/da1686aaa269ac018fad4262f7b21e9015edb978/test_package/src/test_plugin.cpp) (+45/−0)



<a id="commit-2"></a>
### 2. feat: remove implementation of PluginLoader {#commit-2}

- Source: [8be7040cff93337159a45413ad39034f4fedf7f2](https://github.com/EndstoneMC/endstone/commit/8be7040cff93337159a45413ad39034f4fedf7f2)
- Authored: 2023-12-17T23:46:23Z; parent: `da1686aaa269ac018fad4262f7b21e9015edb978`
- Disposition: meaningful; full actual diff statically reviewed.

Removes PluginLoader's server storage, constructor, lifecycle implementations and init helper, leaving an abstract interface. This deliberately separates API from behavior but temporarily leaves getServer declared pure without virtual, repaired next. No test changes; do not infer a successful intermediate build.

Changed-path evidence: [endstone_api/include/endstone/plugin/plugin_loader.h](https://github.com/EndstoneMC/endstone/blob/8be7040cff93337159a45413ad39034f4fedf7f2/endstone_api/include/endstone/plugin/plugin_loader.h) (+3/−32)



<a id="commit-3"></a>
### 3. refactor: clean up includes {#commit-3}

- Source: [1226cb2d1393b4b7cc660561c67d88f9a557adf0](https://github.com/EndstoneMC/endstone/commit/1226cb2d1393b4b7cc660561c67d88f9a557adf0)
- Authored: 2023-12-17T23:53:53Z; parent: `8be7040cff93337159a45413ad39034f4fedf7f2`
- Disposition: meaningful; full actual diff statically reviewed.

Rearranges complete includes versus forward declarations across Plugin/Loader/Manager/Server and adds the missing virtual to pure getServer. Although titled include cleanup, the virtual correction is a compile-relevant semantic repair; later edits reverse part of the dependency direction.

Changed-path evidence: [endstone_api/include/endstone/plugin/plugin.h](https://github.com/EndstoneMC/endstone/blob/1226cb2d1393b4b7cc660561c67d88f9a557adf0/endstone_api/include/endstone/plugin/plugin.h) (+1/−4); [endstone_api/include/endstone/plugin/plugin_loader.h](https://github.com/EndstoneMC/endstone/blob/1226cb2d1393b4b7cc660561c67d88f9a557adf0/endstone_api/include/endstone/plugin/plugin_loader.h) (+4/−2); [endstone_api/include/endstone/plugin/plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/1226cb2d1393b4b7cc660561c67d88f9a557adf0/endstone_api/include/endstone/plugin/plugin_manager.h) (+2/−4); [endstone_api/include/endstone/server.h](https://github.com/EndstoneMC/endstone/blob/8be7040cff93337159a45413ad39034f4fedf7f2/endstone_api/include/endstone/server.h) (+0/−2)



<a id="commit-6"></a>
### 6. feat: add basic server, logger and plugin manager {#commit-6}

- Source: [a75dad798aff8883130437e429713fff1762cc27](https://github.com/EndstoneMC/endstone/commit/a75dad798aff8883130437e429713fff1762cc27)
- Authored: 2023-12-18T12:11:51Z; parent: `1954760eacb89dd8b7142dd15aae79fb24b71fcb`
- Disposition: meaningful; full actual diff statically reviewed.

Adds singleton EndstoneServer, spdlog adapter/factory and SimplePluginManager with owned plugins and filename-pattern loaders, borrowed lookup pointers, directory discovery and load/enable/disable phases. Logger factory serializes map lookup/creation with a mutex; manager operations have no corresponding concurrency guard. Source shows two hazards: registerLoader moves the same unique_ptr once per filter, and duplicate plugin names overwrite lookup while retaining earlier owned objects. Missing-file logging does not immediately return. Plugin loading remains unregistered at this stage.

Changed-path evidence: [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/CMakeLists.txt) (+1/−0); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/conanfile.py) (+6/−1); [endstone_api/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_api/CMakeLists.txt) (+1/−0); [endstone_api/include/endstone/logger.h](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_api/include/endstone/logger.h) (+6/−6); [endstone_api/include/endstone/server.h](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_api/include/endstone/server.h) (+3/−2); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_core/CMakeLists.txt) (+17/−0); [endstone_core/include/endstone/core/endstone_server.h](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_core/include/endstone/core/endstone_server.h) (+70/−0); [endstone_core/include/endstone/core/logger_factory.h](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_core/include/endstone/core/logger_factory.h) (+38/−0); [endstone_core/include/endstone/core/plugin/simple_plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_core/include/endstone/core/plugin/simple_plugin_manager.h) (+48/−0); [endstone_core/src/endstone/core/endstone_server.cpp](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_core/src/endstone/core/endstone_server.cpp) (+72/−0); [endstone_core/src/endstone/core/logger_factory.cpp](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_core/src/endstone/core/logger_factory.cpp) (+63/−0); [endstone_core/src/endstone/core/simple_plugin_manager.cpp](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_core/src/endstone/core/simple_plugin_manager.cpp) (+178/−0)



<a id="commit-7"></a>
### 7. feat: add cpp plugin loader {#commit-7}

- Source: [fe547816b27ad2de4c676f8da9e5567fcbd229d6](https://github.com/EndstoneMC/endstone/commit/fe547816b27ad2de4c676f8da9e5567fcbd229d6)
- Authored: 2023-12-19T00:26:17Z; parent: `a75dad798aff8883130437e429713fff1762cc27`
- Disposition: meaningful; full actual diff statically reviewed.

Registers CppPluginLoader, implements load/symbol lookup/create/init, renames exported factory to EndstonePluginInit, restores lifecycle implementation in PluginLoaderBase, and moves core include/source paths. PluginLogger adds prefixing over factory-owned loggers. Linux branches coexist with unconditional Windows diagnostics/cleanup, fixed in the next chain. Successful module handles are intentionally or accidentally left loaded; no unloading ownership is recorded. Exact moves and changed hunks were distinguished.

Changed-path evidence: [endstone_api/include/endstone/plugin/plugin.h](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_api/include/endstone/plugin/plugin.h) (+11/−9); [endstone_api/include/endstone/plugin/plugin_loader.h](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_api/include/endstone/plugin/plugin_loader.h) (+1/−2); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_core/CMakeLists.txt) (+1/−0); [endstone_core/include/endstone/core/endstone_server.h](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_core/include/endstone/core/endstone_server.h) (+0/−70); [endstone_core/include/endstone/core/logger_factory.h](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_core/include/endstone/core/logger_factory.h) (+0/−38); [endstone_core/include/endstone/core/plugin/simple_plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_core/include/endstone/core/plugin/simple_plugin_manager.h) (+0/−48); [endstone_core/include/endstone_core/endstone_server.h](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_core/include/endstone_core/endstone_server.h) (+70/−0); [endstone_core/include/endstone_core/logger_factory.h](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_core/include/endstone_core/logger_factory.h) (+38/−0); [endstone_core/include/endstone_core/plugin/cpp_plugin_loader.h](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_core/include/endstone_core/plugin/cpp_plugin_loader.h) (+29/−0); [endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h) (+48/−0); [endstone_core/include/endstone_core/plugin/plugin_loader_base.h](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_core/include/endstone_core/plugin/plugin_loader_base.h) (+37/−0); [endstone_core/include/endstone_core/plugin/plugin_logger.h](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_core/include/endstone_core/plugin/plugin_logger.h) (+34/−0); [endstone_core/src/endstone/core/endstone_server.cpp](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_core/src/endstone/core/endstone_server.cpp) (+0/−72); [endstone_core/src/endstone/core/logger_factory.cpp](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_core/src/endstone/core/logger_factory.cpp) (+0/−63); [endstone_core/src/endstone/core/simple_plugin_manager.cpp](https://github.com/EndstoneMC/endstone/blob/a75dad798aff8883130437e429713fff1762cc27/endstone_core/src/endstone/core/simple_plugin_manager.cpp) (+0/−178); [endstone_core/src/endstone_core/endstone_server.cpp](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_core/src/endstone_core/endstone_server.cpp) (+75/−0); [endstone_core/src/endstone_core/logger_factory.cpp](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_core/src/endstone_core/logger_factory.cpp) (+63/−0); [endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp) (+79/−0); [endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp) (+178/−0); [endstone_core/src/endstone_core/plugin/plugin_loader_base.cpp](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_core/src/endstone_core/plugin/plugin_loader_base.cpp) (+43/−0); [endstone_core/src/endstone_core/plugin/plugin_logger.cpp](https://github.com/EndstoneMC/endstone/blob/fe547816b27ad2de4c676f8da9e5567fcbd229d6/endstone_core/src/endstone_core/plugin/plugin_logger.cpp) (+44/−0)



<a id="commit-8"></a>
### 8. feat: add test_package for plugin loader {#commit-8}

- Source: [2f576d357a2f40220d6e3229058a92d33f0c8199](https://github.com/EndstoneMC/endstone/commit/2f576d357a2f40220d6e3229058a92d33f0c8199)
- Authored: 2023-12-19T10:13:11Z; parent: `fe547816b27ad2de4c676f8da9e5567fcbd229d6`
- Disposition: meaningful; full actual diff statically reviewed.

Turns test_package into an executable lifecycle test: builds shared plugin and host, copies OS-specific binary to plugins, then asserts empty→loaded→enabled→disabled through name lookup. Undefines NDEBUG so Release assertions remain live. It does not test invalid exports, failed factories, unload or multiple filters; runtime success is not supplied.

Changed-path evidence: [test_package/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/2f576d357a2f40220d6e3229058a92d33f0c8199/test_package/CMakeLists.txt) (+2/−3); [test_package/conanfile.py](https://github.com/EndstoneMC/endstone/blob/2f576d357a2f40220d6e3229058a92d33f0c8199/test_package/conanfile.py) (+16/−4); [test_package/src/test_server.cpp](https://github.com/EndstoneMC/endstone/blob/2f576d357a2f40220d6e3229058a92d33f0c8199/test_package/src/test_server.cpp) (+50/−0)



<a id="commit-9"></a>
### 9. fix: cpp plugin loader on Linux {#commit-9}

- Source: [1164f2efd4eb3318ea97df76e0bcfd72f66d7e01](https://github.com/EndstoneMC/endstone/commit/1164f2efd4eb3318ea97df76e0bcfd72f66d7e01)
- Authored: 2023-12-19T11:21:50Z; parent: `2f576d357a2f40220d6e3229058a92d33f0c8199`
- Disposition: meaningful; full actual diff statically reviewed.

Splits loader implementations by OS, replacing unguarded GetLastError/FreeLibrary in Linux paths with dlerror/dlclose while retaining Windows behavior. Both handle acquisition and factory failure paths are inspected. Successful-module lifetime remains unmanaged, and throwing factories are not handled.

Changed-path evidence: [endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/1164f2efd4eb3318ea97df76e0bcfd72f66d7e01/endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp) (+44/−24)



<a id="commit-11"></a>
### 11. feat: add more tests for test_server {#commit-11}

- Source: [dcf65292843f0a68a063c656b783e25c4a621c71](https://github.com/EndstoneMC/endstone/commit/dcf65292843f0a68a063c656b783e25c4a621c71)
- Authored: 2023-12-19T12:10:59Z; parent: `f68b84d741b8c6b2af13cf133e73a36f06ed74cc`
- Disposition: meaningful; full actual diff statically reviewed.

Extends existing lifecycle assertions to both plugin-pointer and name overloads at disabled/enabled/disabled states, and switches to cassert. Narrow coverage improvement; no claim of exercising unknown pointers or nullptr.

Changed-path evidence: [test_package/src/test_server.cpp](https://github.com/EndstoneMC/endstone/blob/dcf65292843f0a68a063c656b783e25c4a621c71/test_package/src/test_server.cpp) (+4/−2)



<a id="commit-12"></a>
### 12. feat: improve logging formatter, remove plugin logger {#commit-12}

- Source: [9cfc1606a1c885f51a5d898005ae76de5214d2be](https://github.com/EndstoneMC/endstone/commit/9cfc1606a1c885f51a5d898005ae76de5214d2be)
- Authored: 2023-12-19T13:35:58Z; parent: `dcf65292843f0a68a063c656b783e25c4a621c71`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces per-plugin owned PluginLogger wrappers with borrowed LoggerFactory loggers; formatter now supplies timestamp, level and logger name globally. Renames verbose helper to debug and adds critical; smoke test logs each level. Removing the wrapper also removes custom PluginDescription prefix use, a behavior change beyond simplification. Logger lifetime now relies on static factory storage.

Changed-path evidence: [endstone_api/include/endstone/logger.h](https://github.com/EndstoneMC/endstone/blob/9cfc1606a1c885f51a5d898005ae76de5214d2be/endstone_api/include/endstone/logger.h) (+7/−1); [endstone_api/include/endstone/plugin/plugin.h](https://github.com/EndstoneMC/endstone/blob/9cfc1606a1c885f51a5d898005ae76de5214d2be/endstone_api/include/endstone/plugin/plugin.h) (+1/−1); [endstone_core/include/endstone_core/plugin/plugin_loader_base.h](https://github.com/EndstoneMC/endstone/blob/9cfc1606a1c885f51a5d898005ae76de5214d2be/endstone_core/include/endstone_core/plugin/plugin_loader_base.h) (+1/−1); [endstone_core/include/endstone_core/plugin/plugin_logger.h](https://github.com/EndstoneMC/endstone/blob/dcf65292843f0a68a063c656b783e25c4a621c71/endstone_core/include/endstone_core/plugin/plugin_logger.h) (+0/−34); [endstone_core/src/endstone_core/logger_factory.cpp](https://github.com/EndstoneMC/endstone/blob/9cfc1606a1c885f51a5d898005ae76de5214d2be/endstone_core/src/endstone_core/logger_factory.cpp) (+35/−2); [endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/9cfc1606a1c885f51a5d898005ae76de5214d2be/endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp) (+2/−3); [endstone_core/src/endstone_core/plugin/plugin_loader_base.cpp](https://github.com/EndstoneMC/endstone/blob/9cfc1606a1c885f51a5d898005ae76de5214d2be/endstone_core/src/endstone_core/plugin/plugin_loader_base.cpp) (+4/−2); [endstone_core/src/endstone_core/plugin/plugin_logger.cpp](https://github.com/EndstoneMC/endstone/blob/dcf65292843f0a68a063c656b783e25c4a621c71/endstone_core/src/endstone_core/plugin/plugin_logger.cpp) (+0/−44); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/9cfc1606a1c885f51a5d898005ae76de5214d2be/pyproject.toml) (+1/−1); [test_package/src/test_server.cpp](https://github.com/EndstoneMC/endstone/blob/9cfc1606a1c885f51a5d898005ae76de5214d2be/test_package/src/test_server.cpp) (+7/−1)



<a id="commit-13"></a>
### 13. refactor: code clean up {#commit-13}

- Source: [4076a53158fdde21fac1ba5d877073f5d9ccf9c8](https://github.com/EndstoneMC/endstone/commit/4076a53158fdde21fac1ba5d877073f5d9ccf9c8)
- Authored: 2023-12-19T14:30:00Z; parent: `9cfc1606a1c885f51a5d898005ae76de5214d2be`
- Disposition: small-semantic; full actual diff statically reviewed.

Changes displayed WARN to WARNING, orders formatter construction before sink, and reverts a commented pyproject setting to cmake.verbose. Mostly cleanup but emitted log label is observable; no broad engineering inference supported.

Changed-path evidence: [endstone_core/src/endstone_core/logger_factory.cpp](https://github.com/EndstoneMC/endstone/blob/4076a53158fdde21fac1ba5d877073f5d9ccf9c8/endstone_core/src/endstone_core/logger_factory.cpp) (+3/−3); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/4076a53158fdde21fac1ba5d877073f5d9ccf9c8/pyproject.toml) (+1/−1)



<a id="commit-23"></a>
### 23. feat: add testing for logger and logger_factory {#commit-23}

- Source: [3883d65c03185804e3f4f02e483675fbea482912](https://github.com/EndstoneMC/endstone/commit/3883d65c03185804e3f4f02e483675fbea482912)
- Authored: 2023-12-21T11:55:36Z; parent: `d4db6fdaa616c8a55b5327922c82ac6bf0560efa`
- Disposition: meaningful; full actual diff statically reviewed.

Introduces GoogleTest logger checks for name, singleton-per-name identity and default/changed level thresholds, wiring enable_testing before subdirectories and gtest discovery. Makes spdlog public in CMake again. Tests do not assert formatted output or thread races; globally cached logger state can influence future tests using the same name.

Changed-path evidence: [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/3883d65c03185804e3f4f02e483675fbea482912/CMakeLists.txt) (+5/−5); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/3883d65c03185804e3f4f02e483675fbea482912/conanfile.py) (+1/−0); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/3883d65c03185804e3f4f02e483675fbea482912/endstone_core/CMakeLists.txt) (+16/−4); [endstone_core/src/endstone_core/logger_factory.cpp](https://github.com/EndstoneMC/endstone/blob/3883d65c03185804e3f4f02e483675fbea482912/endstone_core/src/endstone_core/logger_factory.cpp) (+1/−1); [endstone_core/test/test_logger.cpp](https://github.com/EndstoneMC/endstone/blob/3883d65c03185804e3f4f02e483675fbea482912/endstone_core/test/test_logger.cpp) (+60/−0)



<a id="commit-32"></a>
### 32. refactor: remove filesystem from endstone::api {#commit-32}

- Source: [713c1dca0c26153853faeb84b79df4e62db90aed](https://github.com/EndstoneMC/endstone/commit/713c1dca0c26153853faeb84b79df4e62db90aed)
- Authored: 2023-12-22T00:18:18Z; parent: `81b14246e96e0c02d18806ff664147d4e1a69220`
- Disposition: meaningful; full actual diff statically reviewed.

Changes PluginManager public loading signatures from filesystem::path to std::string while retaining filesystem conversion/discovery inside core. Removes filesystem from API header and adjusts all callers. This reduces type/toolchain coupling but is not a fully stable C ABI; std::string and ownership-sensitive pointers remain.

Changed-path evidence: [endstone_api/include/endstone/plugin/plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/713c1dca0c26153853faeb84b79df4e62db90aed/endstone_api/include/endstone/plugin/plugin_manager.h) (+2/−4); [endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/713c1dca0c26153853faeb84b79df4e62db90aed/endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h) (+2/−2); [endstone_core/src/endstone_core/endstone_server.cpp](https://github.com/EndstoneMC/endstone/blob/713c1dca0c26153853faeb84b79df4e62db90aed/endstone_core/src/endstone_core/endstone_server.cpp) (+7/−6); [endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp](https://github.com/EndstoneMC/endstone/blob/713c1dca0c26153853faeb84b79df4e62db90aed/endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp) (+15/−15)



<a id="commit-83"></a>
### 83. refactor: simplify getLogger in cpp_plugin_loader, streamline command in pyproject.toml {#commit-83}

- Source: [46beb17a5342b9a707bf82fba52c562e33b999e6](https://github.com/EndstoneMC/endstone/commit/46beb17a5342b9a707bf82fba52c562e33b999e6)
- Authored: 2024-01-05T01:12:44Z; parent: `5661427fb15bcf3b8cfbfb8e0c92f911430ba9d7`
- Disposition: meaningful; full actual diff statically reviewed.

Uses loader's associated Server logger rather than global EndstoneServer singleton in both OS paths, improving ownership/context consistency. Combines libpython extraction commands into one shell chain and cites manylinux PR1250. No behavior test for alternate Server implementations.

Changed-path evidence: [endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/46beb17a5342b9a707bf82fba52c562e33b999e6/endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp) (+2/−2); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/46beb17a5342b9a707bf82fba52c562e33b999e6/pyproject.toml) (+2/−4)



<a id="commit-86"></a>
### 86. refactor: update PluginManager constructors and clean up code {#commit-86}

- Source: [c4795ad263165de632820a69e1eaa5860e1cf993](https://github.com/EndstoneMC/endstone/commit/c4795ad263165de632820a69e1eaa5860e1cf993)
- Authored: 2024-01-05T11:54:00Z; parent: `0925ac771bd53fd1b0d94d5abf4cdd6c955ec025`
- Disposition: meaningful; full actual diff statically reviewed.

Makes PluginManager explicitly noncopyable, removes unused filesystem include/namespace alias from concrete header and normalizes CMake formatting. Ownership-bearing API now states copy restriction; no change to plugin loading logic.

Changed-path evidence: [endstone_api/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/c4795ad263165de632820a69e1eaa5860e1cf993/endstone_api/CMakeLists.txt) (+1/−2); [endstone_api/include/endstone/plugin/plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/c4795ad263165de632820a69e1eaa5860e1cf993/endstone_api/include/endstone/plugin/plugin_manager.h) (+3/−0); [endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/0925ac771bd53fd1b0d94d5abf4cdd6c955ec025/endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h) (+0/−2)
