<!-- retrieval: {"source_ids":["public:commit:12a2b2ecabf769da307ef16a959b71c7760e24ec","public:commit:2cb821eb6433ff27892ed19be7e9758c42c336dc","public:commit:2ed0c8e3c6d4537b394edebe280501589dcff9bd","public:commit:305a79765b794bd9e5defae02963154f9e337cda","public:commit:45ab85e759bf5e91dff950d3bc25a3c69e570cb5","public:commit:564f72311a863205d26f41ab1cfe19600cb5ec5b","public:commit:5b9cb93f940d8aab357d6139c2b5c35498f78120","public:commit:5e62c4afe7bd79410bf068b0611932f75977661d","public:commit:683ae09b40c79bcfe9bd66480b16c0ef79cf433d","public:commit:6d3304e533a9fb0ca5942bea0d3a18ea3f38b872","public:commit:6d7c74e9c5017df98787a49e86cde7a6dee8e7bb","public:commit:7da084e915cd4f9e9fe9192a7a6eae6957c96a11","public:commit:8813bfacf6b2b129818c019f7e5a19330dfadda3","public:commit:9e003fe800ca5da1695f79919fc93154add50dad","public:commit:b184c0667d2f904a71d749564c1fa4ed86b94daf","public:commit:b6b016e36afdba402d3d39b74d4be0bdf813862b","public:commit:c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37","public:commit:ce97489b9f40e3779ebf82cdc6c3b1a2b7cda3b9","public:commit:d1d75524d8edbedac293a6d4f09d19ae4974bd59","public:commit:d72bc80e8a61350212e09fc40e8c22f99e464df0","public:commit:e752bc3ced6dae3607d71b08fdcf9b76ea304b46","public:commit:e762c60865cd64093828c9fa7947e04bfb3f3126","public:commit:f7f438ab559bdb6d5765ab94107e1ce7a9c7c2f8","public:commit:ff92b7f5d9ad1ec766b8d62b3201966d8128ea84"],"source_type":"public","date":"2024-01-01..2024-01-11","topics":["lifetime","concurrency","ffi","testing","build","performance","recovery","api","diagnosis","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native host hooks, symbol matching and ABI assumptions {#native-host-hooks-symbol-matching-and-abi-assumptions}

## Architecture and initialization {#architecture-and-initialization}

The runtime begins as dependency preparation and a shared-library placeholder, then interposes compiled Endstone shims on host functions. At80 it enumerates shim symbols, finds corresponding host addresses, installs MinHook detours and preserves original trampolines for forwarding. At84 the server/interpreter is constructed during native attach/constructor startup.88 obtains the actual game version through a forwarding shim;90 redirects host log_va into Endstone's logger by area. That host integration is broader than merely loading a DLL: ABI, symbol visibility, initialization context and shutdown order all matter.

A C++ member-function pointer is not generally equivalent to a void pointer; return-value conventions can insert hidden arguments. This implementation uses casts and special RVO adapters to bridge those conventions.98's RVO macro points to the ordinary get_original path, illustrating why the adapter cannot be assumed correct from its name. No real-host ABI probe or architecture matrix was executed here. Exported C names at the plugin entry point do not remove these C++ calling-convention concerns.

## Backend and resource management revisions {#backend-and-resource-management-revisions}

62 imports MinHook packaging, including an official CMake patch by Mikhail Paulyshka that credits Tsuda Kageyu.65 repairs WINAPI matching in the sample.95 adds funchook packaging and broad dependency fixtures;98 switches runtime installation from MinHook to funchook and changes original lookup from symbol name to detour pointer.99 simplifies SymbolHandler into platform functions;106/107 split platform hooking implementations explicitly. These are actual alternatives seen in the code, not hypothetical designs.

The earlier SymbolManager attempts RAII but its move constructor omits the handle, a per-instance mutex cannot serialize independent users of global DbgHelp state, and a noexcept lookup invokes throwing operations. The later manual SymInitialize/SymCleanup flow loses automatic cleanup on exceptions. Funchook objects are allocated and installed per function without being retained for symmetric destruction; a failure can leave earlier hooks installed. DLL detach no longer undoes them. Source does not establish whether process-lifetime-only hooks are deliberate. Any future design decision should distinguish a documented process-lifetime strategy from an accidental leak or unsafe partial initialization.

## Linux symbol and toolchain chain {#linux-symbol-and-toolchain-chain}

102 parses /proc/self/maps to find module base/path and LIEF ELF symbols. An unmatched name can leave an uninitialized base;106's ModuleInfo early return fixes that. The parser still uses unbounded whitespace-delimited pathname parsing and first-match base assumptions; file offsets, spaces, deleted mappings, PIE/shared objects and absence of symbols warrant tests. Linux detours use exported global static symbols, while target lookup changes at106 to local-binding entries from the executable's _symbols.debug companion. That difference is meaningful evidence: identical filter rules for both sides were insufficient.

Native LIEF is replaced with Python LIEF under the GIL at105, then restored at110. CMake target casing, dependency placement, Windows guards and visibility are corrected along the way. Windows107 explicitly separates host executable and injected module APIs and keeps decorated symbol names for exact matching. The companion debug file, exported shim symbols and stripped-wheel settings must all agree with packaging. There is no measured performance comparison or proof of successful symbol discovery in this workunit.

## Log interception and diagnostics {#log-interception-and-diagnostics}

90 maps host bit-valued levels1/2/4/8 to standard levels, defaults unknown values to Critical, renders a copied va_list with vsnprintf and trims trailing whitespace. It replaces rather than forwards original logging. A negative vsnprintf result needs handling before size conversion, and va_end on caller-supplied arguments requires an ownership convention. Unknown areas/levels and varargs ABI are not covered by new tests.88's debug format has two placeholders but one argument;107 repairs Windows diagnostics and111 repairs Linux separately. Logging changes can therefore be correctness fixes, not only verbosity preferences.

## Dependency audit, tests and attribution {#dependency-audit-tests-and-attribution}

The funchook fixture suite exercises direct/call/jump hooks, restoration, file-function redirection,600 repeated exported functions and architecture-specific instruction patterns. All substantive fixture changes were read; the repetitive suffix file was exhaustively verified as S(1)..S(600). These are dependency-level fixtures, not Bedrock integration results. Imported-style tests and upstream patch bodies must not be credited wholesale to the commit author merely because they enter the repository in that SHA.

MinHook recipe declares BSD-2-Clause and funchook GPL-2.0-or-later. This is a verified metadata change that calls for distribution/license review; it is not a legal conclusion about the resulting application.69 fixes a packaged license filename.113 removes the unused MinHook recipe/tests after the migration.

## Application and limits {#application-and-limits}

Use this chain for symbol-resolution audits, native ABI reviews, transactional hook installation, platform resource cleanup, diagnostics and third-party intake. Synthetic dummy-host tests establish only the provided seam. No native hooks, assembly fixtures, downloaded software or upstream build scripts were executed during review, and no runtime safety, benchmark or current-version compatibility is asserted.

## Individual commit evidence {#individual-commit-evidence}



<a id="commit-62"></a>
### 62. feat: add conan recipe for minhook {#commit-62}

- Source: [2ed0c8e3c6d4537b394edebe280501589dcff9bd](https://github.com/EndstoneMC/endstone/commit/2ed0c8e3c6d4537b394edebe280501589dcff9bd)
- Authored: 2024-01-01T17:18:37Z; parent: `1c6fefa3b8bd63f60fced477ea1b920c97789911`
- Disposition: meaningful; full actual diff statically reviewed.

Adds MinHook Conan recipe restricted to Windows x86/x64 with shared/static naming, official CMake patch by Mikhail Paulyshka and separate minimum-CMake patch. Imported patch credits Tsuda Kageyu; do not attribute its entire implementation to Vincent. Test exercises create/enable/disable on dummy MessageBox with status checks but prints expected text rather than asserting it. Source initially points at Endstone fork, corrected next.

Changed-path evidence: [endstone_core/src/endstone_core/endstone_server.cpp](https://github.com/EndstoneMC/endstone/blob/2ed0c8e3c6d4537b394edebe280501589dcff9bd/endstone_core/src/endstone_core/endstone_server.cpp) (+1/−1); [third_party/minhook/conandata.yml](https://github.com/EndstoneMC/endstone/blob/2ed0c8e3c6d4537b394edebe280501589dcff9bd/third_party/minhook/conandata.yml) (+13/−0); [third_party/minhook/conanfile.py](https://github.com/EndstoneMC/endstone/blob/2ed0c8e3c6d4537b394edebe280501589dcff9bd/third_party/minhook/conanfile.py) (+95/−0); [third_party/minhook/patches/0001-add-cmake-support.patch](https://github.com/EndstoneMC/endstone/blob/2ed0c8e3c6d4537b394edebe280501589dcff9bd/third_party/minhook/patches/0001-add-cmake-support.patch) (+204/−0); [third_party/minhook/patches/0002-increase-cmake-min-version.patch](https://github.com/EndstoneMC/endstone/blob/2ed0c8e3c6d4537b394edebe280501589dcff9bd/third_party/minhook/patches/0002-increase-cmake-min-version.patch) (+13/−0); [third_party/minhook/test_package/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/2ed0c8e3c6d4537b394edebe280501589dcff9bd/third_party/minhook/test_package/CMakeLists.txt) (+8/−0); [third_party/minhook/test_package/conanfile.py](https://github.com/EndstoneMC/endstone/blob/2ed0c8e3c6d4537b394edebe280501589dcff9bd/third_party/minhook/test_package/conanfile.py) (+27/−0); [third_party/minhook/test_package/test_package.cpp](https://github.com/EndstoneMC/endstone/blob/2ed0c8e3c6d4537b394edebe280501589dcff9bd/third_party/minhook/test_package/test_package.cpp) (+60/−0)



<a id="commit-63"></a>
### 63. feat: add minhook to requirements on Windows {#commit-63}

- Source: [9e003fe800ca5da1695f79919fc93154add50dad](https://github.com/EndstoneMC/endstone/commit/9e003fe800ca5da1695f79919fc93154add50dad)
- Authored: 2024-01-01T17:27:25Z; parent: `2ed0c8e3c6d4537b394edebe280501589dcff9bd`
- Disposition: meaningful; full actual diff statically reviewed.

Wires Windows-only MinHook requirement into CI/wheel export and placeholder runtime Conan component, adding default recipe version. Runtime component has no binary yet. This is dependency preparation, not completed hooking support.

Changed-path evidence: [.github/workflows/ci-windows.yml](https://github.com/EndstoneMC/endstone/blob/9e003fe800ca5da1695f79919fc93154add50dad/.github/workflows/ci-windows.yml) (+1/−0); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/9e003fe800ca5da1695f79919fc93154add50dad/conanfile.py) (+9/−0); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/9e003fe800ca5da1695f79919fc93154add50dad/pyproject.toml) (+1/−0); [third_party/minhook/conanfile.py](https://github.com/EndstoneMC/endstone/blob/9e003fe800ca5da1695f79919fc93154add50dad/third_party/minhook/conanfile.py) (+3/−0)



<a id="commit-64"></a>
### 64. fix: conandata sources for package minhook {#commit-64}

- Source: [6d3304e533a9fb0ca5942bea0d3a18ea3f38b872](https://github.com/EndstoneMC/endstone/commit/6d3304e533a9fb0ca5942bea0d3a18ea3f38b872)
- Authored: 2024-01-01T17:31:18Z; parent: `9e003fe800ca5da1695f79919fc93154add50dad`
- Disposition: small-semantic; full actual diff statically reviewed.

Corrects MinHook source URL from Endstone fork to TsudaKageyu upstream at same version/digest. Read-only provenance correction; digest unchanged does not itself prove both archives are equivalent without acquisition.

Changed-path evidence: [third_party/minhook/conandata.yml](https://github.com/EndstoneMC/endstone/blob/6d3304e533a9fb0ca5942bea0d3a18ea3f38b872/third_party/minhook/conandata.yml) (+1/−1)



<a id="commit-65"></a>
### 65. feat: update conanfile.py and test_package.cpp {#commit-65}

- Source: [e752bc3ced6dae3607d71b08fdcf9b76ea304b46](https://github.com/EndstoneMC/endstone/commit/e752bc3ced6dae3607d71b08fdcf9b76ea304b46)
- Authored: 2024-01-01T17:53:15Z; parent: `6d3304e533a9fb0ca5942bea0d3a18ea3f38b872`
- Disposition: small-semantic; full actual diff statically reviewed.

Adds WINAPI to dummy detour target so calling convention matches pointer type, expands decorative sample output and marks recipe preparation TODOs for Conan Center. Calling-convention repair matters on affected architectures; printed output remains a demonstration rather than asserted semantic verification.

Changed-path evidence: [third_party/minhook/conanfile.py](https://github.com/EndstoneMC/endstone/blob/e752bc3ced6dae3607d71b08fdcf9b76ea304b46/third_party/minhook/conanfile.py) (+2/−5); [third_party/minhook/test_package/test_package.cpp](https://github.com/EndstoneMC/endstone/blob/e752bc3ced6dae3607d71b08fdcf9b76ea304b46/third_party/minhook/test_package/test_package.cpp) (+18/−3)



<a id="commit-69"></a>
### 69. fix: copy LICENSE.txt to conan package {#commit-69}

- Source: [5b9cb93f940d8aab357d6139c2b5c35498f78120](https://github.com/EndstoneMC/endstone/commit/5b9cb93f940d8aab357d6139c2b5c35498f78120)
- Authored: 2024-01-02T23:41:18Z; parent: `0822628f479461a19644cbc5e518b5d5ad941ef1`
- Disposition: small-semantic; full actual diff statically reviewed.

Corrects packaged MinHook license filename to LICENSE.txt. Compliance artifact repair is real although only one line; does not establish broader license audit.

Changed-path evidence: [third_party/minhook/conanfile.py](https://github.com/EndstoneMC/endstone/blob/5b9cb93f940d8aab357d6139c2b5c35498f78120/third_party/minhook/conanfile.py) (+1/−1)



<a id="commit-76"></a>
### 76. feat: add 'endstone_runtime' library and related dependencies {#commit-76}

- Source: [45ab85e759bf5e91dff950d3bc25a3c69e570cb5](https://github.com/EndstoneMC/endstone/commit/45ab85e759bf5e91dff950d3bc25a3c69e570cb5)
- Authored: 2024-01-03T16:41:27Z; parent: `f666f998d4a7cf9e35ee7d877959ed1c2fc66f89`
- Disposition: meaningful; full actual diff statically reviewed.

Creates shared endstone_runtime target installed into wheel internals with Windows MinHook/dbghelp links and placeholder process attach/Linux constructor logging. Adds runtime component dependencies and loosens fmt pin to >=10.1.1. Conan runtime libs remains empty, and hook APIs are not implemented yet. DLL attach currently runs logging under loader context; no shutdown tests.

Changed-path evidence: [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/45ab85e759bf5e91dff950d3bc25a3c69e570cb5/CMakeLists.txt) (+1/−0); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/45ab85e759bf5e91dff950d3bc25a3c69e570cb5/conanfile.py) (+12/−4); [endstone_runtime/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/45ab85e759bf5e91dff950d3bc25a3c69e570cb5/endstone_runtime/CMakeLists.txt) (+26/−0); [endstone_runtime/include/endstone_runtime/hook.h](https://github.com/EndstoneMC/endstone/blob/45ab85e759bf5e91dff950d3bc25a3c69e570cb5/endstone_runtime/include/endstone_runtime/hook.h) (+15/−0); [endstone_runtime/src/endstone_runtime/dllmain.cpp](https://github.com/EndstoneMC/endstone/blob/45ab85e759bf5e91dff950d3bc25a3c69e570cb5/endstone_runtime/src/endstone_runtime/dllmain.cpp) (+75/−0)



<a id="commit-80"></a>
### 80. feat: implement hooking on Windows {#commit-80}

- Source: [d72bc80e8a61350212e09fc40e8c22f99e464df0](https://github.com/EndstoneMC/endstone/commit/d72bc80e8a61350212e09fc40e8c22f99e464df0)
- Authored: 2024-01-04T17:40:25Z; parent: `196e39ef1f2d442cee659f393302da75758a5304`
- Disposition: meaningful; full actual diff statically reviewed.

Adds bedrock internal declaration target, exported runDedicatedServerLoop shim, function/member/RVO adapters, DbgHelp SymbolManager and MinHook installation. Enumerates local shim symbols, resolves host targets and replaces lookup entries with original trampolines before enabling all hooks. SymbolManager owns cleanup but move constructor fails to transfer handle; mutex is per instance despite global DbgHelp state. symbol is noexcept yet calls throwing operations; hook failures lack transactional rollback, cleanup can throw from DllMain, and global symbol map is unsynchronized. Initial shim only prints then forwards; host lifecycle integration comes later. These are source-derived risks, not reproduced crashes.

Changed-path evidence: [.clang-tidy](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/.clang-tidy) (+1/−1); [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/CMakeLists.txt) (+1/−1); [bedrock_internals/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/bedrock_internals/CMakeLists.txt) (+8/−0); [bedrock_internals/include/bedrock/bedrock.h](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/bedrock_internals/include/bedrock/bedrock.h) (+21/−0); [bedrock_internals/include/bedrock/core.h](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/bedrock_internals/include/bedrock/core.h) (+19/−0); [bedrock_internals/include/bedrock/dedicated_server.h](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/bedrock_internals/include/bedrock/dedicated_server.h) (+30/−0); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/conanfile.py) (+7/−2); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/endstone_core/CMakeLists.txt) (+1/−1); [endstone_python/python/endstone/_internal/bootstrap/base.py](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/endstone_python/python/endstone/_internal/bootstrap/base.py) (+3/−0); [endstone_runtime/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/endstone_runtime/CMakeLists.txt) (+1/−1); [endstone_runtime/include/endstone_runtime/hook.h](https://github.com/EndstoneMC/endstone/blob/196e39ef1f2d442cee659f393302da75758a5304/endstone_runtime/include/endstone_runtime/hook.h) (+0/−15); [endstone_runtime/include/endstone_runtime/internals.h](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/endstone_runtime/include/endstone_runtime/internals.h) (+113/−0); [endstone_runtime/include/endstone_runtime/windows/hook.h](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/endstone_runtime/include/endstone_runtime/windows/hook.h) (+26/−0); [endstone_runtime/include/endstone_runtime/windows/symbol_manager.h](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/endstone_runtime/include/endstone_runtime/windows/symbol_manager.h) (+63/−0); [endstone_runtime/src/bedrock/dedicated_server.cpp](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/endstone_runtime/src/bedrock/dedicated_server.cpp) (+15/−0); [endstone_runtime/src/endstone_runtime/dllmain.cpp](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/endstone_runtime/src/endstone_runtime/dllmain.cpp) (+9/−16); [endstone_runtime/src/endstone_runtime/windows/hook.cpp](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/endstone_runtime/src/endstone_runtime/windows/hook.cpp) (+166/−0); [endstone_runtime/src/endstone_runtime/windows/symbol_manager.cpp](https://github.com/EndstoneMC/endstone/blob/d72bc80e8a61350212e09fc40e8c22f99e464df0/endstone_runtime/src/endstone_runtime/windows/symbol_manager.cpp) (+92/−0)



<a id="commit-84"></a>
### 84. refactor: rename dllmain.cpp to main.cpp and update log messages {#commit-84}

- Source: [b184c0667d2f904a71d749564c1fa4ed86b94daf](https://github.com/EndstoneMC/endstone/commit/b184c0667d2f904a71d749564c1fa4ed86b94daf)
- Authored: 2024-01-05T01:13:39Z; parent: `46beb17a5342b9a707bf82fba52c562e33b999e6`
- Disposition: meaningful; full actual diff statically reviewed.

Renames dllmain.cpp to main.cpp, constructs singleton server during native runtime attach/constructor and emits startup version, adds explicit break after detach cleanup. Brief Python print acquires GIL. This changes initialization timing and brings interpreter/plugin-loader setup into DLL attach, carrying loader-context risks beyond the title's logging cleanup.

Changed-path evidence: [endstone_core/src/endstone_core/endstone_server.cpp](https://github.com/EndstoneMC/endstone/blob/b184c0667d2f904a71d749564c1fa4ed86b94daf/endstone_core/src/endstone_core/endstone_server.cpp) (+4/−0); [endstone_runtime/src/endstone_runtime/dllmain.cpp](https://github.com/EndstoneMC/endstone/blob/46beb17a5342b9a707bf82fba52c562e33b999e6/endstone_runtime/src/endstone_runtime/dllmain.cpp) (+0/−68); [endstone_runtime/src/endstone_runtime/main.cpp](https://github.com/EndstoneMC/endstone/blob/b184c0667d2f904a71d749564c1fa4ed86b94daf/endstone_runtime/src/endstone_runtime/main.cpp) (+75/−0)



<a id="commit-88"></a>
### 88. feat: add Common::getGameVersionString and improve logging {#commit-88}

- Source: [b6b016e36afdba402d3d39b74d4be0bdf813862b](https://github.com/EndstoneMC/endstone/commit/b6b016e36afdba402d3d39b74d4be0bdf813862b)
- Authored: 2024-01-05T15:14:20Z; parent: `aee2f62ad6540fe3330bbacd53d12faf37854ec1`
- Disposition: meaningful; full actual diff statically reviewed.

Adds Common::getGameVersionString forwarding shim and changes Server Minecraft-version return from string_view to owned string, replacing Unknown with runtime host query. Startup/loop logs use host version and hooks switch printf to spdlog debug. One debug format has two placeholders but only original pointer argument, a source-visible formatting defect later corrected. Stubbed package tests must now supply host function.

Changed-path evidence: [bedrock_internals/include/bedrock/common.h](https://github.com/EndstoneMC/endstone/blob/b6b016e36afdba402d3d39b74d4be0bdf813862b/bedrock_internals/include/bedrock/common.h) (+23/−0); [endstone_api/include/endstone/server.h](https://github.com/EndstoneMC/endstone/blob/b6b016e36afdba402d3d39b74d4be0bdf813862b/endstone_api/include/endstone/server.h) (+1/−1); [endstone_core/include/endstone_core/endstone_server.h](https://github.com/EndstoneMC/endstone/blob/b6b016e36afdba402d3d39b74d4be0bdf813862b/endstone_core/include/endstone_core/endstone_server.h) (+1/−1); [endstone_core/src/endstone_core/endstone_server.cpp](https://github.com/EndstoneMC/endstone/blob/b6b016e36afdba402d3d39b74d4be0bdf813862b/endstone_core/src/endstone_core/endstone_server.cpp) (+4/−7); [endstone_runtime/src/bedrock/common.cpp](https://github.com/EndstoneMC/endstone/blob/b6b016e36afdba402d3d39b74d4be0bdf813862b/endstone_runtime/src/bedrock/common.cpp) (+22/−0); [endstone_runtime/src/bedrock/dedicated_server.cpp](https://github.com/EndstoneMC/endstone/blob/b6b016e36afdba402d3d39b74d4be0bdf813862b/endstone_runtime/src/bedrock/dedicated_server.cpp) (+2/−1); [endstone_runtime/src/endstone_runtime/main.cpp](https://github.com/EndstoneMC/endstone/blob/b6b016e36afdba402d3d39b74d4be0bdf813862b/endstone_runtime/src/endstone_runtime/main.cpp) (+1/−1); [endstone_runtime/src/endstone_runtime/windows/hook.cpp](https://github.com/EndstoneMC/endstone/blob/b6b016e36afdba402d3d39b74d4be0bdf813862b/endstone_runtime/src/endstone_runtime/windows/hook.cpp) (+4/−2)



<a id="commit-89"></a>
### 89. feat: add magic_enum package dependency {#commit-89}

- Source: [ce97489b9f40e3779ebf82cdc6c3b1a2b7cda3b9](https://github.com/EndstoneMC/endstone/commit/ce97489b9f40e3779ebf82cdc6c3b1a2b7cda3b9)
- Authored: 2024-01-05T16:37:00Z; parent: `b6b016e36afdba402d3d39b74d4be0bdf813862b`
- Disposition: small-semantic; full actual diff statically reviewed.

Adds magic_enum0.9.5 requirement and runtime component dependency, preparing log-area names. No runtime use in this commit alone.

Changed-path evidence: [conanfile.py](https://github.com/EndstoneMC/endstone/blob/ce97489b9f40e3779ebf82cdc6c3b1a2b7cda3b9/conanfile.py) (+2/−1)



<a id="commit-90"></a>
### 90. feat: hook 'BedrockLog::log_va' and redirect message to endstone logger {#commit-90}

- Source: [d1d75524d8edbedac293a6d4f09d19ae4974bd59](https://github.com/EndstoneMC/endstone/commit/d1d75524d8edbedac293a6d4f09d19ae4974bd59)
- Authored: 2024-01-05T16:38:41Z; parent: `ce97489b9f40e3779ebf82cdc6c3b1a2b7cda3b9`
- Disposition: meaningful; full actual diff statically reviewed.

Adds Bedrock log signature/area enum and replaces log_va with Endstone logging by area; maps bit-valued levels1/2/4/8 and defaults unknown values to Critical. Copies va_list, sizes with vsnprintf, renders, trims trailing whitespace and uses literal '{}' logging. Needs negative vsnprintf-result handling and careful caller-owned va_list lifecycle (calls va_end on incoming args); no tests cover formatting failures, unknown areas or varargs ABI. Suppresses original logger entirely.

Changed-path evidence: [bedrock_internals/include/bedrock/bedrock_log.h](https://github.com/EndstoneMC/endstone/blob/d1d75524d8edbedac293a6d4f09d19ae4974bd59/bedrock_internals/include/bedrock/bedrock_log.h) (+83/−0); [bedrock_internals/include/bedrock/common.h](https://github.com/EndstoneMC/endstone/blob/d1d75524d8edbedac293a6d4f09d19ae4974bd59/bedrock_internals/include/bedrock/common.h) (+1/−1); [endstone_runtime/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/d1d75524d8edbedac293a6d4f09d19ae4974bd59/endstone_runtime/CMakeLists.txt) (+2/−1); [endstone_runtime/src/bedrock/bedrock_log.cpp](https://github.com/EndstoneMC/endstone/blob/d1d75524d8edbedac293a6d4f09d19ae4974bd59/endstone_runtime/src/bedrock/bedrock_log.cpp) (+59/−0)



<a id="commit-92"></a>
### 92. fix: test_package by adding dummy bedrock internal functions {#commit-92}

- Source: [5e62c4afe7bd79410bf068b0611932f75977661d](https://github.com/EndstoneMC/endstone/commit/5e62c4afe7bd79410bf068b0611932f75977661d)
- Authored: 2024-01-05T16:56:40Z; parent: `62c2e5d7e25a4032992b9e48ea9a7112d1336951`
- Disposition: meaningful; full actual diff statically reviewed.

Adds dummy Common::getGameVersionString for package test and adjusts log prefixes. Establishes host-symbol seam for tests, but passing against dummy cannot verify actual Bedrock symbol resolution or ABI.

Changed-path evidence: [test_package/src/dummy_bedrock.cpp](https://github.com/EndstoneMC/endstone/blob/5e62c4afe7bd79410bf068b0611932f75977661d/test_package/src/dummy_bedrock.cpp) (+20/−0); [test_package/src/test_server.cpp](https://github.com/EndstoneMC/endstone/blob/5e62c4afe7bd79410bf068b0611932f75977661d/test_package/src/test_server.cpp) (+1/−2)



<a id="commit-95"></a>
### 95. feat: add funchook/1.1.3 recipe {#commit-95}

- Source: [c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37](https://github.com/EndstoneMC/endstone/commit/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37)
- Authored: 2024-01-07T23:53:56Z; parent: `cf1a3e83d67c5168ebf1c65e5c6350b526cbe744`
- Disposition: meaningful; full actual diff statically reviewed.

Adds funchook1.1.3 recipe/digest and forces CCI capstone across platforms instead of vendored disassemblers. Imported-style test suite covers executable/DLL direct/call/jump hooks, restore semantics, open/fopen redirection, 600 DLL and executable functions, ARM64 PC-relative/branch/literal instructions and x86 thunk/back-jump cases; 600 suffix entries verified exactly S(1)..S(600). Tests are dependency tests, not Bedrock integration; no execution claimed. Recipe declares GPL-2.0-or-later unlike MinHook BSD; retain license-review need, not a legal conclusion. Test fixture authorship is not established merely by this commit's author.

Changed-path evidence: [third_party/funchook/conandata.yml](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/conandata.yml) (+9/−0); [third_party/funchook/conanfile.py](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/conanfile.py) (+93/−0); [third_party/funchook/patches/1.1.3-0001-cmake-use-cci-capstone.patch](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/patches/1.1.3-0001-cmake-use-cci-capstone.patch) (+69/−0); [third_party/funchook/test_package/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/test_package/CMakeLists.txt) (+56/−0); [third_party/funchook/test_package/conanfile.py](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/test_package/conanfile.py) (+27/−0); [third_party/funchook/test_package/libfunchook_test.c](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/test_package/libfunchook_test.c) (+21/−0); [third_party/funchook/test_package/libfunchook_test_aarch64_gas.S](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/test_package/libfunchook_test_aarch64_gas.S) (+139/−0); [third_party/funchook/test_package/libfunchook_test_noasm.c](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/test_package/libfunchook_test_noasm.c) (+19/−0); [third_party/funchook/test_package/libfunchook_test_x86_64_gas.S](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/test_package/libfunchook_test_x86_64_gas.S) (+38/−0); [third_party/funchook/test_package/libfunchook_test_x86_64_masm.asm](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/test_package/libfunchook_test_x86_64_masm.asm) (+18/−0); [third_party/funchook/test_package/libfunchook_test_x86_gas.S](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/test_package/libfunchook_test_x86_gas.S) (+68/−0); [third_party/funchook/test_package/libfunchook_test_x86_masm.asm](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/test_package/libfunchook_test_x86_masm.asm) (+26/−0); [third_party/funchook/test_package/suffix.list](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/test_package/suffix.list) (+600/−0); [third_party/funchook/test_package/test_main.c](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/test_package/test_main.c) (+634/−0); [third_party/funchook/test_package/x86_test.S](https://github.com/EndstoneMC/endstone/blob/c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37/third_party/funchook/test_package/x86_test.S) (+326/−0)



<a id="commit-96"></a>
### 96. refactor: remove "macos" from topics in funchook/1.1.3 recipe {#commit-96}

- Source: [f7f438ab559bdb6d5765ab94107e1ce7a9c7c2f8](https://github.com/EndstoneMC/endstone/commit/f7f438ab559bdb6d5765ab94107e1ce7a9c7c2f8)
- Authored: 2024-01-07T23:57:22Z; parent: `c3f0ba51209f9d3eb34d02915e99e4c12ac9dd37`
- Disposition: mechanical; full actual diff statically reviewed.

Removes macos topic from funchook recipe to match Windows/Linux validation. Metadata-only source change, fully inspected; no independent engineering principle.

Changed-path evidence: [third_party/funchook/conanfile.py](https://github.com/EndstoneMC/endstone/blob/f7f438ab559bdb6d5765ab94107e1ce7a9c7c2f8/third_party/funchook/conanfile.py) (+1/−1)



<a id="commit-97"></a>
### 97. fix: validation error message in funchook/1.1.3 recipe {#commit-97}

- Source: [683ae09b40c79bcfe9bd66480b16c0ef79cf433d](https://github.com/EndstoneMC/endstone/commit/683ae09b40c79bcfe9bd66480b16c0ef79cf433d)
- Authored: 2024-01-07T23:58:10Z; parent: `f7f438ab559bdb6d5765ab94107e1ce7a9c7c2f8`
- Disposition: small-semantic; full actual diff statically reviewed.

Corrects unsupported-platform error message by removing inaccurate shared-only qualifier; validation condition is unchanged. User-facing diagnostic correction.

Changed-path evidence: [third_party/funchook/conanfile.py](https://github.com/EndstoneMC/endstone/blob/683ae09b40c79bcfe9bd66480b16c0ef79cf433d/third_party/funchook/conanfile.py) (+1/−1)



<a id="commit-98"></a>
### 98. feat: replace minhook with funchook {#commit-98}

- Source: [e762c60865cd64093828c9fa7947e04bfb3f3126](https://github.com/EndstoneMC/endstone/commit/e762c60865cd64093828c9fa7947e04bfb3f3126)
- Authored: 2024-01-08T13:23:05Z; parent: `683ae09b40c79bcfe9bd66480b16c0ef79cf433d`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces runtime MinHook dependency/install path with funchook, maps original trampolines by detour pointer rather than symbol name, introduces SymbolHandler interface and platform-independent main. Hooks are prepared/installed individually and no longer uninstalled on DLL detach; allocated hook handles are not retained for cleanup. RVO macro accidentally calls ordinary get_original, and member-pointer casting assumes representation compatible with extracted void pointer. Failed target lookup throws after potential partial installation. Existing MinHook recipe remains in tree; no deletion was assumed.

Changed-path evidence: [conanfile.py](https://github.com/EndstoneMC/endstone/blob/e762c60865cd64093828c9fa7947e04bfb3f3126/conanfile.py) (+4/−5); [endstone_runtime/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/e762c60865cd64093828c9fa7947e04bfb3f3126/endstone_runtime/CMakeLists.txt) (+3/−6); [endstone_runtime/include/endstone_runtime/hook.h](https://github.com/EndstoneMC/endstone/blob/e762c60865cd64093828c9fa7947e04bfb3f3126/endstone_runtime/include/endstone_runtime/hook.h) (+106/−0); [endstone_runtime/include/endstone_runtime/internals.h](https://github.com/EndstoneMC/endstone/blob/683ae09b40c79bcfe9bd66480b16c0ef79cf433d/endstone_runtime/include/endstone_runtime/internals.h) (+0/−113); [endstone_runtime/include/endstone_runtime/symbol_handler.h](https://github.com/EndstoneMC/endstone/blob/e762c60865cd64093828c9fa7947e04bfb3f3126/endstone_runtime/include/endstone_runtime/symbol_handler.h) (+43/−0); [endstone_runtime/include/endstone_runtime/windows/hook.h](https://github.com/EndstoneMC/endstone/blob/683ae09b40c79bcfe9bd66480b16c0ef79cf433d/endstone_runtime/include/endstone_runtime/windows/hook.h) (+0/−26); [endstone_runtime/include/endstone_runtime/windows/symbol_manager.h](https://github.com/EndstoneMC/endstone/blob/683ae09b40c79bcfe9bd66480b16c0ef79cf433d/endstone_runtime/include/endstone_runtime/windows/symbol_manager.h) (+0/−63); [endstone_runtime/src/bedrock/common.cpp](https://github.com/EndstoneMC/endstone/blob/e762c60865cd64093828c9fa7947e04bfb3f3126/endstone_runtime/src/bedrock/common.cpp) (+2/−2); [endstone_runtime/src/bedrock/dedicated_server.cpp](https://github.com/EndstoneMC/endstone/blob/e762c60865cd64093828c9fa7947e04bfb3f3126/endstone_runtime/src/bedrock/dedicated_server.cpp) (+3/−3); [endstone_runtime/src/endstone_runtime/hook_error.cpp](https://github.com/EndstoneMC/endstone/blob/e762c60865cd64093828c9fa7947e04bfb3f3126/endstone_runtime/src/endstone_runtime/hook_error.cpp) (+65/−0); [endstone_runtime/src/endstone_runtime/main.cpp](https://github.com/EndstoneMC/endstone/blob/e762c60865cd64093828c9fa7947e04bfb3f3126/endstone_runtime/src/endstone_runtime/main.cpp) (+31/−46); [endstone_runtime/src/endstone_runtime/windows/hook.cpp](https://github.com/EndstoneMC/endstone/blob/e762c60865cd64093828c9fa7947e04bfb3f3126/endstone_runtime/src/endstone_runtime/windows/hook.cpp) (+72/−107); [endstone_runtime/src/endstone_runtime/windows/symbol_handler.cpp](https://github.com/EndstoneMC/endstone/blob/e762c60865cd64093828c9fa7947e04bfb3f3126/endstone_runtime/src/endstone_runtime/windows/symbol_handler.cpp) (+87/−0); [endstone_runtime/src/endstone_runtime/windows/symbol_manager.cpp](https://github.com/EndstoneMC/endstone/blob/683ae09b40c79bcfe9bd66480b16c0ef79cf433d/endstone_runtime/src/endstone_runtime/windows/symbol_manager.cpp) (+0/−92)



<a id="commit-99"></a>
### 99. refactor: move platform-specific code to platform_x.cpp {#commit-99}

- Source: [12a2b2ecabf769da307ef16a959b71c7760e24ec](https://github.com/EndstoneMC/endstone/commit/12a2b2ecabf769da307ef16a959b71c7760e24ec)
- Authored: 2024-01-08T15:29:40Z; parent: `e762c60865cd64093828c9fa7947e04bfb3f3126`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces SymbolHandler abstraction with narrow platform functions for base/path/symbol enumeration and moves installation to common hook.cpp. Windows enumeration cleanup is now manual and no per-instance mutex remains; exceptions before SymCleanup leak session state. Adds Linux LIEF0.13.1 dependency but mistakenly puts lief::lief into system_libs, repaired next. This simplifies layering while altering resource safety.

Changed-path evidence: [Dockerfile](https://github.com/EndstoneMC/endstone/blob/12a2b2ecabf769da307ef16a959b71c7760e24ec/Dockerfile) (+1/−0); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/12a2b2ecabf769da307ef16a959b71c7760e24ec/conanfile.py) (+4/−0); [endstone_runtime/include/endstone_runtime/platform.h](https://github.com/EndstoneMC/endstone/blob/12a2b2ecabf769da307ef16a959b71c7760e24ec/endstone_runtime/include/endstone_runtime/platform.h) (+26/−0); [endstone_runtime/include/endstone_runtime/symbol_handler.h](https://github.com/EndstoneMC/endstone/blob/e762c60865cd64093828c9fa7947e04bfb3f3126/endstone_runtime/include/endstone_runtime/symbol_handler.h) (+0/−43); [endstone_runtime/src/endstone_runtime/hook.cpp](https://github.com/EndstoneMC/endstone/blob/12a2b2ecabf769da307ef16a959b71c7760e24ec/endstone_runtime/src/endstone_runtime/hook.cpp) (+146/−0); [endstone_runtime/src/endstone_runtime/hook_error.cpp](https://github.com/EndstoneMC/endstone/blob/e762c60865cd64093828c9fa7947e04bfb3f3126/endstone_runtime/src/endstone_runtime/hook_error.cpp) (+0/−65); [endstone_runtime/src/endstone_runtime/platform_windows.cpp](https://github.com/EndstoneMC/endstone/blob/12a2b2ecabf769da307ef16a959b71c7760e24ec/endstone_runtime/src/endstone_runtime/platform_windows.cpp) (+96/−0); [endstone_runtime/src/endstone_runtime/windows/hook.cpp](https://github.com/EndstoneMC/endstone/blob/e762c60865cd64093828c9fa7947e04bfb3f3126/endstone_runtime/src/endstone_runtime/windows/hook.cpp) (+0/−133); [endstone_runtime/src/endstone_runtime/windows/symbol_handler.cpp](https://github.com/EndstoneMC/endstone/blob/e762c60865cd64093828c9fa7947e04bfb3f3126/endstone_runtime/src/endstone_runtime/windows/symbol_handler.cpp) (+0/−87)



<a id="commit-102"></a>
### 102. feat(endstone_runtime): add Linux platform support {#commit-102}

- Source: [6d7c74e9c5017df98787a49e86cde7a6dee8e7bb](https://github.com/EndstoneMC/endstone/commit/6d7c74e9c5017df98787a49e86cde7a6dee8e7bb)
- Authored: 2024-01-10T11:01:07Z; parent: `e832f0d67356fcd4fc7efd9269d773858f686592`
- Disposition: meaningful; full actual diff statically reviewed.

Implements Linux platform discovery through /proc/self/maps and native LIEF ELF static-symbol enumeration. An unmatched requested path leaves module_base uninitialized; null path picks the first mapping. sscanf uses an unbounded %s for the pathname, cannot represent spaces, and base ignores mapping file offset. Exported STB_GLOBAL filter suits detours but not necessarily target symbols. No malformed-map, stripped-binary or missing-module test is added; some issues are revised at106.

Changed-path evidence: [endstone_runtime/src/endstone_runtime/platform_linux.cpp](https://github.com/EndstoneMC/endstone/blob/6d7c74e9c5017df98787a49e86cde7a6dee8e7bb/endstone_runtime/src/endstone_runtime/platform_linux.cpp) (+125/−0)



<a id="commit-103"></a>
### 103. feat(endstone_runtime): add lief package for parsing symbols {#commit-103}

- Source: [ff92b7f5d9ad1ec766b8d62b3201966d8128ea84](https://github.com/EndstoneMC/endstone/commit/ff92b7f5d9ad1ec766b8d62b3201966d8128ea84)
- Authored: 2024-01-10T11:30:38Z; parent: `6d7c74e9c5017df98787a49e86cde7a6dee8e7bb`
- Disposition: meaningful; full actual diff statically reviewed.

Corrects LIEF CMake target case, hides GNU runtime symbols and excludes archive exports, selects DLL/SO filenames by platform, and uses the executable's _symbols.debug companion on Linux. Adds instrumentation while retaining a debug format string with two placeholders but one argument. Removes scikit-build build-dir. Changes couple packaging, symbol availability and loader behavior; no successful runtime result is recorded.

Changed-path evidence: [endstone_runtime/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/ff92b7f5d9ad1ec766b8d62b3201966d8128ea84/endstone_runtime/CMakeLists.txt) (+9/−3); [endstone_runtime/include/endstone_runtime/platform.h](https://github.com/EndstoneMC/endstone/blob/ff92b7f5d9ad1ec766b8d62b3201966d8128ea84/endstone_runtime/include/endstone_runtime/platform.h) (+1/−1); [endstone_runtime/src/endstone_runtime/hook.cpp](https://github.com/EndstoneMC/endstone/blob/ff92b7f5d9ad1ec766b8d62b3201966d8128ea84/endstone_runtime/src/endstone_runtime/hook.cpp) (+17/−5); [endstone_runtime/src/endstone_runtime/platform_windows.cpp](https://github.com/EndstoneMC/endstone/blob/ff92b7f5d9ad1ec766b8d62b3201966d8128ea84/endstone_runtime/src/endstone_runtime/platform_windows.cpp) (+7/−4); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/6d7c74e9c5017df98787a49e86cde7a6dee8e7bb/pyproject.toml) (+0/−1)



<a id="commit-105"></a>
### 105. refactor(endstone_runtime): replace conan package lief/0.10.1 with pypi package lief==0.13.2 {#commit-105}

- Source: [8813bfacf6b2b129818c019f7e5a19330dfadda3](https://github.com/EndstoneMC/endstone/commit/8813bfacf6b2b129818c019f7e5a19330dfadda3)
- Authored: 2024-01-10T12:38:33Z; parent: `ca74d16252eba9118a0eb61b42b58841b09ca223`
- Disposition: meaningful; full actual diff statically reviewed.

Removes Conan/native LIEF and implements Linux symbol enumeration by importing Python lief under gil_scoped_acquire, parsing the file and iterating static_symbols with exported/global checks. This chooses Python as an integration boundary while requiring an initialized interpreter and Python dependency at startup. No timing data or discussion proves a performance tradeoff; native LIEF returns at110.

Changed-path evidence: [conanfile.py](https://github.com/EndstoneMC/endstone/blob/ca74d16252eba9118a0eb61b42b58841b09ca223/conanfile.py) (+0/−4); [endstone_runtime/src/endstone_runtime/hook.cpp](https://github.com/EndstoneMC/endstone/blob/8813bfacf6b2b129818c019f7e5a19330dfadda3/endstone_runtime/src/endstone_runtime/hook.cpp) (+1/−1); [endstone_runtime/src/endstone_runtime/platform_linux.cpp](https://github.com/EndstoneMC/endstone/blob/8813bfacf6b2b129818c019f7e5a19330dfadda3/endstone_runtime/src/endstone_runtime/platform_linux.cpp) (+14/−8)



<a id="commit-106"></a>
### 106. fix(endstone_runtime): hooking functions on Linux {#commit-106}

- Source: [7da084e915cd4f9e9fe9192a7a6eae6957c96a11](https://github.com/EndstoneMC/endstone/commit/7da084e915cd4f9e9fe9192a7a6eae6957c96a11)
- Authored: 2024-01-10T13:38:45Z; parent: `8813bfacf6b2b129818c019f7e5a19330dfadda3`
- Disposition: meaningful; full actual diff statically reviewed.

Splits common hooking into Linux and Windows implementations with separate module/executable platform APIs. Linux detours remain exported global static symbols; targets now use local-binding symbols from the executable debug companion. ModuleInfo early return eliminates the uninitialized base variable while retaining first-map/offset assumptions. Initialization errors now terminate. Windows extraction is temporarily inconsistent: executable base still uses module API and pathname call has stale nullptr argument;107 repairs these. Funchook's public header moves into an include namespace.

Changed-path evidence: [endstone_runtime/include/endstone_runtime/platform.h](https://github.com/EndstoneMC/endstone/blob/7da084e915cd4f9e9fe9192a7a6eae6957c96a11/endstone_runtime/include/endstone_runtime/platform.h) (+4/−3); [endstone_runtime/src/endstone_runtime/hook.cpp](https://github.com/EndstoneMC/endstone/blob/8813bfacf6b2b129818c019f7e5a19330dfadda3/endstone_runtime/src/endstone_runtime/hook.cpp) (+0/−158); [endstone_runtime/src/endstone_runtime/linux/hook.cpp](https://github.com/EndstoneMC/endstone/blob/7da084e915cd4f9e9fe9192a7a6eae6957c96a11/endstone_runtime/src/endstone_runtime/linux/hook.cpp) (+196/−0); [endstone_runtime/src/endstone_runtime/linux/platform.cpp](https://github.com/EndstoneMC/endstone/blob/7da084e915cd4f9e9fe9192a7a6eae6957c96a11/endstone_runtime/src/endstone_runtime/linux/platform.cpp) (+98/−0); [endstone_runtime/src/endstone_runtime/main.cpp](https://github.com/EndstoneMC/endstone/blob/7da084e915cd4f9e9fe9192a7a6eae6957c96a11/endstone_runtime/src/endstone_runtime/main.cpp) (+1/−2); [endstone_runtime/src/endstone_runtime/platform_linux.cpp](https://github.com/EndstoneMC/endstone/blob/8813bfacf6b2b129818c019f7e5a19330dfadda3/endstone_runtime/src/endstone_runtime/platform_linux.cpp) (+0/−131); [endstone_runtime/src/endstone_runtime/platform_windows.cpp](https://github.com/EndstoneMC/endstone/blob/8813bfacf6b2b129818c019f7e5a19330dfadda3/endstone_runtime/src/endstone_runtime/platform_windows.cpp) (+0/−99); [endstone_runtime/src/endstone_runtime/windows/hook.cpp](https://github.com/EndstoneMC/endstone/blob/7da084e915cd4f9e9fe9192a7a6eae6957c96a11/endstone_runtime/src/endstone_runtime/windows/hook.cpp) (+162/−0); [endstone_runtime/src/endstone_runtime/windows/platform_windows.cpp](https://github.com/EndstoneMC/endstone/blob/7da084e915cd4f9e9fe9192a7a6eae6957c96a11/endstone_runtime/src/endstone_runtime/windows/platform_windows.cpp) (+99/−0); [third_party/funchook/conanfile.py](https://github.com/EndstoneMC/endstone/blob/7da084e915cd4f9e9fe9192a7a6eae6957c96a11/third_party/funchook/conanfile.py) (+5/−0)



<a id="commit-107"></a>
### 107. fix(endstone_runtime): hooking functions on Windows {#commit-107}

- Source: [564f72311a863205d26f41ab1cfe19600cb5ec5b](https://github.com/EndstoneMC/endstone/commit/564f72311a863205d26f41ab1cfe19600cb5ec5b)
- Authored: 2024-01-10T14:11:18Z; parent: `7da084e915cd4f9e9fe9192a7a6eae6957c96a11`
- Disposition: meaningful; full actual diff statically reviewed.

Finishes Windows separation: explicit executable base/path versus injected module base/path, DbgHelp enumeration inside hook.cpp, and SymSetOptions(NULL) to preserve decorated names (do not undecorate) for exact matching. Fixes hook diagnostics into separate target/detour/original entries and uses funchook/funchook.h. Manual SymCleanup remains vulnerable to exceptions and installed hooks lack transactional rollback; this is a substantial platform repair rather than a file move alone.

Changed-path evidence: [endstone_runtime/src/endstone_runtime/windows/hook.cpp](https://github.com/EndstoneMC/endstone/blob/564f72311a863205d26f41ab1cfe19600cb5ec5b/endstone_runtime/src/endstone_runtime/windows/hook.cpp) (+56/−18); [endstone_runtime/src/endstone_runtime/windows/platform.cpp](https://github.com/EndstoneMC/endstone/blob/564f72311a863205d26f41ab1cfe19600cb5ec5b/endstone_runtime/src/endstone_runtime/windows/platform.cpp) (+83/−0); [endstone_runtime/src/endstone_runtime/windows/platform_windows.cpp](https://github.com/EndstoneMC/endstone/blob/7da084e915cd4f9e9fe9192a7a6eae6957c96a11/endstone_runtime/src/endstone_runtime/windows/platform_windows.cpp) (+0/−99)



<a id="commit-110"></a>
### 110. fix(endstone_runtime): add conan package lief/0.10.1 {#commit-110}

- Source: [2cb821eb6433ff27892ed19be7e9758c42c336dc](https://github.com/EndstoneMC/endstone/commit/2cb821eb6433ff27892ed19be7e9758c42c336dc)
- Authored: 2024-01-11T17:16:48Z; parent: `9815f26009d1b1912d385672713fb7db54fbd6e3`
- Disposition: meaningful; full actual diff statically reviewed.

Reverts Python LIEF integration to native Conan LIEF0.10.1, preserving the global-exported detour/local-target split. Removes pip LIEF and GIL acquisition from native symbol enumeration. Adds global hidden visibility and extension dynamic-list-cpp-typeinfo, plus unconditional find_package(LIEF), which would request a Linux-only dependency on Windows.112 narrows these choices. Motive beyond refactor title and performance outcome are unknown.

Changed-path evidence: [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/2cb821eb6433ff27892ed19be7e9758c42c336dc/CMakeLists.txt) (+1/−0); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/2cb821eb6433ff27892ed19be7e9758c42c336dc/conanfile.py) (+4/−0); [endstone_python/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/2cb821eb6433ff27892ed19be7e9758c42c336dc/endstone_python/CMakeLists.txt) (+3/−0); [endstone_runtime/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/2cb821eb6433ff27892ed19be7e9758c42c336dc/endstone_runtime/CMakeLists.txt) (+2/−0); [endstone_runtime/src/endstone_runtime/linux/hook.cpp](https://github.com/EndstoneMC/endstone/blob/2cb821eb6433ff27892ed19be7e9758c42c336dc/endstone_runtime/src/endstone_runtime/linux/hook.cpp) (+22/−46); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/2cb821eb6433ff27892ed19be7e9758c42c336dc/pyproject.toml) (+1/−1)



<a id="commit-111"></a>
### 111. refactor: set logging level from info to debug in hook.cpp {#commit-111}

- Source: [305a79765b794bd9e5defae02963154f9e337cda](https://github.com/EndstoneMC/endstone/commit/305a79765b794bd9e5defae02963154f9e337cda)
- Authored: 2024-01-11T18:06:55Z; parent: `2cb821eb6433ff27892ed19be7e9758c42c336dc`
- Disposition: meaningful; full actual diff statically reviewed.

Demotes Linux startup diagnostics to debug, reports module pathname, and gives target/detour/original pointers explicit name/value arguments, repairing the earlier format arity defect on this platform. Small patch with concrete diagnostic correctness, not just logging taste.

Changed-path evidence: [endstone_runtime/src/endstone_runtime/linux/hook.cpp](https://github.com/EndstoneMC/endstone/blob/305a79765b794bd9e5defae02963154f9e337cda/endstone_runtime/src/endstone_runtime/linux/hook.cpp) (+6/−4)
