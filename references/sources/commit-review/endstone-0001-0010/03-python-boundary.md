<!-- retrieval: {"source_ids":["public:commit:00c1cfc24c53d52f81208ff19f35eacbf175884f","public:commit:02a0767e6da397cb05ce86ee0d11548826312c3d","public:commit:156c6f0b3f8a2c3ef26137cdd79ee870a7c6343c","public:commit:1d6fdbcf24079a85798a1b94a6c1a81e97a563ac","public:commit:2ad0ddf075fb4a96cf54889d6759398d89e0ef54","public:commit:2ae7edd69ab9d3a1748a304947cbbbdafd75a19f","public:commit:35b4c6b749f0f88a5893fb8b7d2d82558aab8383","public:commit:3fe97573961882a9ec0b7776af1f673caa00a1de","public:commit:49aa72e2461e6e745c495f2fbaca860afc9a425e","public:commit:4c9b1a67c9eb95e2e796fcaa24dc55985e808fbc","public:commit:5fdcf09a2bc9d2354e14d7cb6dd7dca4c9651bb0","public:commit:62c2e5d7e25a4032992b9e48ea9a7112d1336951","public:commit:6f09f142e69c0b0d70c31331f7a4f481496f327a","public:commit:6f67d47312602ceb4b522a1ba8dd8741b80a5159","public:commit:8038a11021b170cbba46c567928c03bce3dc7a05","public:commit:81b14246e96e0c02d18806ff664147d4e1a69220","public:commit:8c8bf1f8e8a9139319ea8e43be4da55976e38289","public:commit:8e3c3d35b4390a117661c7121d6a5451bb464d24","public:commit:906bfcc4197703414dce28518fad4a67876e63ad","public:commit:992206db916dacf366c9df37a7b7eb9abb2f435d","public:commit:9a6f84919661cd1cf304ea755aaedb38c243a8b7","public:commit:a88ffaf1b2c39761e68d429a00aa7c14596099d6","public:commit:aee2f62ad6540fe3330bbacd53d12faf37854ec1","public:commit:af1e7516dd8c4e01ad6a2217118ec5aaaa7d7950","public:commit:af50240910edd59f7baebce8efee37e9379d3805","public:commit:b5e0521adbef83dc99335d123683dd6fdad8de2c","public:commit:b6d265f68dac73b4bcbcc2a9c3a8294e971c0edc","public:commit:be5b7ab43ca20e93f8a43f67efea4fe796ce974d","public:commit:cc1fd33789a1fd676372902cc5b360e6b67c107b","public:commit:cdb7a4c5d3e9651bc3a3906e2cefb86b01a7f03d","public:commit:cdebe1d5c732c99b0822af251dd1a55370947c09","public:commit:cfe0e0a8c236e0742b48eba9beec364d112f718d","public:commit:d08f4430f83b30568e942e29464a27f3f19d27ee","public:commit:d4db6fdaa616c8a55b5327922c82ac6bf0560efa","public:commit:e0ef42a510b682ba34021a3b928e5093b5acedbc","public:commit:e73d7a11f6e74e6746b3d3587d9a0d2f79d5555b","public:commit:f592559df3932d2e6cdbca2f475f79e52713538e"],"source_type":"public","date":"2023-12-19..2024-01-12","topics":["lifetime","ffi","testing","build","recovery","api","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Python/C++ boundary, lifetime and API evolution {#python-c-boundary-lifetime-and-api-evolution}

## The central problem is ownership in two runtimes {#the-central-problem-is-ownership-in-two-runtimes}

The bindings expand from an empty Server class at15 to Plugin/Loader/Manager/Logger metadata, lifecycle and source loading. Returning a C++ pointer to Python combines three separate questions: who deletes the C++ object, what keeps the Python override object alive, and whether Python refcount work happens while the interpreter and GIL are valid. A reference return policy addresses borrowing; it does not independently solve ownership conversion or trampoline lifetime.

The observed ownership chain is unusually informative.25 starts Plugin with nodelete.30 wraps a Python-returned raw Plugin pointer in unique_ptr.41 adds reference policies.42 tries a shared_ptr loader adapter.43/46 adopt a pinned smart_holder branch and direct unique_ptr transfer;49 adds trampoline_self_life_support.48 temporarily creates the interpreter in test main, while the host is static.50 moves the interpreter into the server so it can outlive manager-owned Python objects.87 globally suppresses pybind GIL refcount assertions with an explicit comment that the Windows shutdown cause is unknown. This is a documented workaround, not a proved repair.

113 returns to standard ConanCenter pybind11 and removes trampoline support.114/115 switch loader and plugin ownership to shared_ptr, retaining the Python loader as py::object and Python-created plugin wrappers in a _keep_alive list.114 temporarily returns nullptr from Python loadPlugin while conversion is being changed;115 restores forwarding. The manager's multi-filter unique_ptr defect is fixed by the shared loader association at114. Its explicit dec_ref initially leaves ordinary object destruction to decrement again;115 adds release() to clear that handle after the GIL-protected decrement.115 disables assertion suppression and117 removes the obsolete comment. None of these patches alone supplies an observed shutdown regression-test result.

## Remaining lifecycle questions at this endpoint {#remaining-lifecycle-questions-at-this-endpoint}

Server members are declared logger, interpreter, GIL-release guard, then manager. Reverse destruction destroys manager before the guard reacquires the GIL and before interpreter finalization. Holders/destructors must therefore acquire the GIL where necessary; declaration order alone is not sufficient. The new Python loader destructor explicitly does this, but pimpl() calls obj_.cast without a local GIL guard, and native entry paths need scrutiny. The retained source-plugin list has no demonstrated pruning on manager clear. Shared owners can defer deletion beyond the manager and do not extend borrowed server/loader lifetimes automatically. These are static audit concerns, not claims of reproduced crashes.

The noexcept load contract at115 also needs care: allocation, Python casts and callbacks can throw. The trampoline catches std::exception and returns null, but other surrounding native operations must fit the same contract or terminate.117 repairs a missing Linux definition qualifier; it does not add all failure-path tests.

## Configuration, validation and API behavior {#configuration-validation-and-api-behavior}

The source loader parses TOML, resolves module:class, loads a package or module from src, checks subclassing and installs metadata.39 contains several independent initial defects: it validates name as though it were main, does not store main, and calls a nonexistent instance helper.45 and49 repair them. Input checks use assert, so optimized Python changes the validation contract. Modules are inserted into sys.modules before execution; execution failures can leave partial cache entries, and name collisions can reuse unrelated modules. These are concrete reasons to test isolation and retry behavior.

31 binds disable_plugin to enablePlugin by mistake. This remains in the inspected endpoint unless a later unassigned change repairs it; API names/stubs must not substitute for source inspection.35 converts description from polymorphic interface to copyable value, simplifying conversion but breaking virtual-extension shape. Its internal Python getter initially warns on required internal calls;56 removes that warning for this explicit reason. A failed description override logs and terminates rather than returning an error value.

Exports and typing also change repeatedly: explicit imports replace wholesale module-global copying, public classes move to dedicated modules, then dynamic aliases are used.58 adds manager APIs, but nullable C++ lookups do not match non-optional stub types, list-of-pointer return ownership lacks targeted evidence, and keyword names drift. These are contract-level changes even when titles describe stubs or cleanup.

## Tests, attribution and applicable lessons {#tests-attribution-and-applicable-lessons}

Pytest covers import surfaces, value constructor forms, normalized names and full-name formatting.49 adds synthetic C++/Python lifecycle integration. These tests do not establish callback failure rollback, cross-runtime destruction safety, refcount correctness, cache isolation, unknown plugin handling or actual Bedrock compatibility. No test was executed during this review. The smart_holder/pybind11 implementation belongs to its upstream contributors; this unit studies Endstone's integration and reversals, not authorship of the dependency.

Use this dossier for holder selection, Python override lifetime, interpreter shutdown design, API/stub consistency and plugin configuration recovery. It supports concrete audit questions and revision patterns, not a universal recommendation to suppress GIL checks, choose shared_ptr, or avoid smart_holder.

## Individual commit evidence {#individual-commit-evidence}



<a id="commit-15"></a>
### 15. feat: add endstone_python module {#commit-15}

- Source: [cc1fd33789a1fd676372902cc5b360e6b67c107b](https://github.com/EndstoneMC/endstone/commit/cc1fd33789a1fd676372902cc5b360e6b67c107b)
- Authored: 2023-12-19T18:30:42Z; parent: `5610297207487b3bef39827f74c0f40e2340ad7d`
- Disposition: meaningful; full actual diff statically reviewed.

Adds pybind11 2.11.1 dependency, a Python extension target exposing an otherwise empty Server class, include install rules and GNU filesystem linkage. Conan core dependency includes pybind11::embed ahead of actual embedding. This establishes packaging/build wiring rather than an implemented Python server API.

Changed-path evidence: [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/cc1fd33789a1fd676372902cc5b360e6b67c107b/CMakeLists.txt) (+1/−0); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/cc1fd33789a1fd676372902cc5b360e6b67c107b/conanfile.py) (+3/−2); [endstone_python/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/cc1fd33789a1fd676372902cc5b360e6b67c107b/endstone_python/CMakeLists.txt) (+21/−0); [endstone_python/include/endstone_python/endstone_python.h](https://github.com/EndstoneMC/endstone/blob/cc1fd33789a1fd676372902cc5b360e6b67c107b/endstone_python/include/endstone_python/endstone_python.h) (+15/−0); [endstone_python/src/endstone_python/endstone_python.cpp](https://github.com/EndstoneMC/endstone/blob/cc1fd33789a1fd676372902cc5b360e6b67c107b/endstone_python/src/endstone_python/endstone_python.cpp) (+26/−0); [endstone_python/src/endstone_python/server.cpp](https://github.com/EndstoneMC/endstone/blob/cc1fd33789a1fd676372902cc5b360e6b67c107b/endstone_python/src/endstone_python/server.cpp) (+13/−0)



<a id="commit-22"></a>
### 22. feat: move the stubs for class Server to __init__.pyi {#commit-22}

- Source: [d4db6fdaa616c8a55b5327922c82ac6bf0560efa](https://github.com/EndstoneMC/endstone/commit/d4db6fdaa616c8a55b5327922c82ac6bf0560efa)
- Authored: 2023-12-21T11:08:44Z; parent: `757a44d820d55159964ad9ecf09746b2b9a51f0e`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces wholesale module-global copying with explicit Server/version imports and __all__, moves Server stub to package __init__.pyi, and corrects the Minecraft-version attribute spelling. Removes exported version tuple and adjusts tests accordingly. Public import surface becomes explicit; this is observable API change.

Changed-path evidence: [endstone_python/python/endstone/__init__.py](https://github.com/EndstoneMC/endstone/blob/d4db6fdaa616c8a55b5327922c82ac6bf0560efa/endstone_python/python/endstone/__init__.py) (+8/−8); [endstone_python/python/endstone/__init__.pyi](https://github.com/EndstoneMC/endstone/blob/d4db6fdaa616c8a55b5327922c82ac6bf0560efa/endstone_python/python/endstone/__init__.pyi) (+9/−0); [endstone_python/python/endstone/server.pyi](https://github.com/EndstoneMC/endstone/blob/757a44d820d55159964ad9ecf09746b2b9a51f0e/endstone_python/python/endstone/server.pyi) (+0/−6); [endstone_python/test/test_endstone.py](https://github.com/EndstoneMC/endstone/blob/d4db6fdaa616c8a55b5327922c82ac6bf0560efa/endstone_python/test/test_endstone.py) (+1/−1)



<a id="commit-25"></a>
### 25. feat: add python binding for Plugin class {#commit-25}

- Source: [b5e0521adbef83dc99335d123683dd6fdad8de2c](https://github.com/EndstoneMC/endstone/commit/b5e0521adbef83dc99335d123683dd6fdad8de2c)
- Authored: 2023-12-21T12:37:21Z; parent: `3c96463d94da99a5b0cf142f900e5943b689bd1e`
- Disposition: meaningful; full actual diff statically reviewed.

Adds Python Plugin trampoline and wrapper, lifecycle callback forwarding with exception logging, borrowed logger/loader/server properties and a nodelete holder. Description initially returns a dummy static value. Callback exceptions are swallowed and logged while plugin enabled state already changed in C++; no rollback is implemented. Uninitialized logger access before loader initialization is not tested.

Changed-path evidence: [endstone_python/include/endstone_python/endstone_python.h](https://github.com/EndstoneMC/endstone/blob/b5e0521adbef83dc99335d123683dd6fdad8de2c/endstone_python/include/endstone_python/endstone_python.h) (+8/−0); [endstone_python/python/endstone/plugin/__init__.py](https://github.com/EndstoneMC/endstone/blob/b5e0521adbef83dc99335d123683dd6fdad8de2c/endstone_python/python/endstone/plugin/__init__.py) (+3/−0); [endstone_python/python/endstone/plugin/__init__.pyi](https://github.com/EndstoneMC/endstone/blob/b5e0521adbef83dc99335d123683dd6fdad8de2c/endstone_python/python/endstone/plugin/__init__.pyi) (+1/−0); [endstone_python/python/endstone/plugin/_plugin.py](https://github.com/EndstoneMC/endstone/blob/b5e0521adbef83dc99335d123683dd6fdad8de2c/endstone_python/python/endstone/plugin/_plugin.py) (+11/−0); [endstone_python/src/endstone_python/endstone_python.cpp](https://github.com/EndstoneMC/endstone/blob/b5e0521adbef83dc99335d123683dd6fdad8de2c/endstone_python/src/endstone_python/endstone_python.cpp) (+3/−3); [endstone_python/src/endstone_python/logger.cpp](https://github.com/EndstoneMC/endstone/blob/b5e0521adbef83dc99335d123683dd6fdad8de2c/endstone_python/src/endstone_python/logger.cpp) (+26/−0); [endstone_python/src/endstone_python/plugin/plugin.cpp](https://github.com/EndstoneMC/endstone/blob/b5e0521adbef83dc99335d123683dd6fdad8de2c/endstone_python/src/endstone_python/plugin/plugin.cpp) (+83/−0); [endstone_python/src/endstone_python/server.cpp](https://github.com/EndstoneMC/endstone/blob/b5e0521adbef83dc99335d123683dd6fdad8de2c/endstone_python/src/endstone_python/server.cpp) (+13/−0)



<a id="commit-26"></a>
### 26. feat: add stubs for Logger and Plugin {#commit-26}

- Source: [49aa72e2461e6e745c495f2fbaca860afc9a425e](https://github.com/EndstoneMC/endstone/commit/49aa72e2461e6e745c495f2fbaca860afc9a425e)
- Authored: 2023-12-21T16:39:30Z; parent: `b5e0521adbef83dc99335d123683dd6fdad8de2c`
- Disposition: meaningful; full actual diff statically reviewed.

Flattens Python plugin package to plugin.py and plugin.pyi, exports Logger and types plugin properties. Expands import-surface tests but weakens version checks from non-None assertions to attribute existence only. Stubs describe APIs ahead of fuller implementations.

Changed-path evidence: [endstone_python/python/endstone/__init__.py](https://github.com/EndstoneMC/endstone/blob/49aa72e2461e6e745c495f2fbaca860afc9a425e/endstone_python/python/endstone/__init__.py) (+2/−1); [endstone_python/python/endstone/__init__.pyi](https://github.com/EndstoneMC/endstone/blob/49aa72e2461e6e745c495f2fbaca860afc9a425e/endstone_python/python/endstone/__init__.pyi) (+2/−0); [endstone_python/python/endstone/plugin.py](https://github.com/EndstoneMC/endstone/blob/49aa72e2461e6e745c495f2fbaca860afc9a425e/endstone_python/python/endstone/plugin.py) (+13/−0); [endstone_python/python/endstone/plugin.pyi](https://github.com/EndstoneMC/endstone/blob/49aa72e2461e6e745c495f2fbaca860afc9a425e/endstone_python/python/endstone/plugin.pyi) (+17/−0); [endstone_python/python/endstone/plugin/__init__.py](https://github.com/EndstoneMC/endstone/blob/b5e0521adbef83dc99335d123683dd6fdad8de2c/endstone_python/python/endstone/plugin/__init__.py) (+0/−3); [endstone_python/python/endstone/plugin/__init__.pyi](https://github.com/EndstoneMC/endstone/blob/b5e0521adbef83dc99335d123683dd6fdad8de2c/endstone_python/python/endstone/plugin/__init__.pyi) (+0/−1); [endstone_python/python/endstone/plugin/_plugin.py](https://github.com/EndstoneMC/endstone/blob/b5e0521adbef83dc99335d123683dd6fdad8de2c/endstone_python/python/endstone/plugin/_plugin.py) (+0/−11); [endstone_python/test/test_endstone.py](https://github.com/EndstoneMC/endstone/blob/49aa72e2461e6e745c495f2fbaca860afc9a425e/endstone_python/test/test_endstone.py) (+12/−5)



<a id="commit-27"></a>
### 27. feat: add python bindings for Logger class {#commit-27}

- Source: [cfe0e0a8c236e0742b48eba9beec364d112f718d](https://github.com/EndstoneMC/endstone/commit/cfe0e0a8c236e0742b48eba9beec364d112f718d)
- Authored: 2023-12-21T17:17:07Z; parent: `49aa72e2461e6e745c495f2fbaca860afc9a425e`
- Disposition: meaningful; full actual diff statically reviewed.

Adds C++ trace helper and Python logger methods/enum constants plus descriptive stubs. Python strings are passed into fmt-format helpers rather than an explicit literal-message log overload, an important formatting-boundary concern to test. Enum runtime representation and int stubs are not demonstrated identical by these tests.

Changed-path evidence: [endstone_api/include/endstone/logger.h](https://github.com/EndstoneMC/endstone/blob/cfe0e0a8c236e0742b48eba9beec364d112f718d/endstone_api/include/endstone/logger.h) (+6/−1); [endstone_python/python/endstone/__init__.pyi](https://github.com/EndstoneMC/endstone/blob/cfe0e0a8c236e0742b48eba9beec364d112f718d/endstone_python/python/endstone/__init__.pyi) (+80/−1); [endstone_python/src/endstone_python/logger.cpp](https://github.com/EndstoneMC/endstone/blob/cfe0e0a8c236e0742b48eba9beec364d112f718d/endstone_python/src/endstone_python/logger.cpp) (+50/−1)



<a id="commit-28"></a>
### 28. feat: add python source plugin to test_package {#commit-28}

- Source: [d08f4430f83b30568e942e29464a27f3f19d27ee](https://github.com/EndstoneMC/endstone/commit/d08f4430f83b30568e942e29464a27f3f19d27ee)
- Authored: 2023-12-21T17:17:53Z; parent: `cfe0e0a8c236e0742b48eba9beec364d112f718d`
- Disposition: small-semantic; full actual diff statically reviewed.

Adds a Python sample plugin with lifecycle log methods and TOML metadata using dotted module/class main. It is a fixture, not yet wired into the package test; the main grammar changes next.

Changed-path evidence: [test_package/src/test_plugin_python/plugin.toml](https://github.com/EndstoneMC/endstone/blob/d08f4430f83b30568e942e29464a27f3f19d27ee/test_package/src/test_plugin_python/plugin.toml) (+3/−0); [test_package/src/test_plugin_python/src/test_plugin.py](https://github.com/EndstoneMC/endstone/blob/d08f4430f83b30568e942e29464a27f3f19d27ee/test_package/src/test_plugin_python/src/test_plugin.py) (+12/−0)



<a id="commit-30"></a>
### 30. feat: add python binding for PluginLoader {#commit-30}

- Source: [8e3c3d35b4390a117661c7121d6a5451bb464d24](https://github.com/EndstoneMC/endstone/commit/8e3c3d35b4390a117661c7121d6a5451bb464d24)
- Authored: 2023-12-21T23:43:43Z; parent: `39ac169793b9b6fb0e5150934b8d0378b0203a76`
- Disposition: meaningful; full actual diff statically reviewed.

Moves shared lifecycle/server/init implementation back from core PluginLoaderBase into public PluginLoader while adding Python loader trampoline. Python-returned raw Plugin* becomes a unique_ptr, so cross-language transfer/lifetime is central; exceptions log and return nullptr/empty filters. Windows init call is updated but Linux is missed until commit 36. This reverses the earlier interface-only design, showing adaptation rather than a fixed abstraction preference.

Changed-path evidence: [endstone_api/include/endstone/plugin/plugin_loader.h](https://github.com/EndstoneMC/endstone/blob/8e3c3d35b4390a117661c7121d6a5451bb464d24/endstone_api/include/endstone/plugin/plugin_loader.h) (+37/−3); [endstone_core/include/endstone_core/plugin/cpp_plugin_loader.h](https://github.com/EndstoneMC/endstone/blob/8e3c3d35b4390a117661c7121d6a5451bb464d24/endstone_core/include/endstone_core/plugin/cpp_plugin_loader.h) (+3/−3); [endstone_core/include/endstone_core/plugin/plugin_loader_base.h](https://github.com/EndstoneMC/endstone/blob/39ac169793b9b6fb0e5150934b8d0378b0203a76/endstone_core/include/endstone_core/plugin/plugin_loader_base.h) (+0/−37); [endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/8e3c3d35b4390a117661c7121d6a5451bb464d24/endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp) (+2/−1); [endstone_core/src/endstone_core/plugin/plugin_loader_base.cpp](https://github.com/EndstoneMC/endstone/blob/39ac169793b9b6fb0e5150934b8d0378b0203a76/endstone_core/src/endstone_core/plugin/plugin_loader_base.cpp) (+0/−45); [endstone_python/include/endstone_python/endstone_python.h](https://github.com/EndstoneMC/endstone/blob/8e3c3d35b4390a117661c7121d6a5451bb464d24/endstone_python/include/endstone_python/endstone_python.h) (+1/−0); [endstone_python/src/endstone_python/endstone_python.cpp](https://github.com/EndstoneMC/endstone/blob/8e3c3d35b4390a117661c7121d6a5451bb464d24/endstone_python/src/endstone_python/endstone_python.cpp) (+1/−0); [endstone_python/src/endstone_python/plugin/plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/8e3c3d35b4390a117661c7121d6a5451bb464d24/endstone_python/src/endstone_python/plugin/plugin_loader.cpp) (+64/−0); [test_package/src/test_plugin.cpp](https://github.com/EndstoneMC/endstone/blob/8e3c3d35b4390a117661c7121d6a5451bb464d24/test_package/src/test_plugin.cpp) (+1/−1); [test_package/src/test_server.cpp](https://github.com/EndstoneMC/endstone/blob/8e3c3d35b4390a117661c7121d6a5451bb464d24/test_package/src/test_server.cpp) (+6/−6)



<a id="commit-31"></a>
### 31. feat: add stubs for PluginLoader {#commit-31}

- Source: [81b14246e96e0c02d18806ff664147d4e1a69220](https://github.com/EndstoneMC/endstone/commit/81b14246e96e0c02d18806ff664147d4e1a69220)
- Authored: 2023-12-22T00:17:49Z; parent: `8e3c3d35b4390a117661c7121d6a5451bb464d24`
- Disposition: meaningful; full actual diff statically reviewed.

Adds loader stubs and public exports; renames get_plugin_file_filters override and exposes enable/disable/server. Source mistakenly binds disable_plugin to enablePlugin, not disablePlugin. The newly declared Python API therefore cannot be assumed to satisfy its names; no callback behavior tests accompany it.

Changed-path evidence: [endstone_python/python/endstone/plugin.py](https://github.com/EndstoneMC/endstone/blob/81b14246e96e0c02d18806ff664147d4e1a69220/endstone_python/python/endstone/plugin.py) (+2/−1); [endstone_python/python/endstone/plugin.pyi](https://github.com/EndstoneMC/endstone/blob/81b14246e96e0c02d18806ff664147d4e1a69220/endstone_python/python/endstone/plugin.pyi) (+8/−1); [endstone_python/src/endstone_python/plugin/plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/81b14246e96e0c02d18806ff664147d4e1a69220/endstone_python/src/endstone_python/plugin/plugin_loader.cpp) (+5/−2)



<a id="commit-33"></a>
### 33. refactor: plugin.toml now uses format module_name:class_name for main {#commit-33}

- Source: [9a6f84919661cd1cf304ea755aaedb38c243a8b7](https://github.com/EndstoneMC/endstone/commit/9a6f84919661cd1cf304ea755aaedb38c243a8b7)
- Authored: 2023-12-22T00:19:31Z; parent: `713c1dca0c26153853faeb84b79df4e62db90aed`
- Disposition: small-semantic; full actual diff statically reviewed.

Changes sample main from dotted test_plugin.TestPlugin to explicit module:class grammar. This is a configuration contract revision, not merely formatting; parser implementation follows later.

Changed-path evidence: [test_package/src/test_plugin_python/plugin.toml](https://github.com/EndstoneMC/endstone/blob/9a6f84919661cd1cf304ea755aaedb38c243a8b7/test_package/src/test_plugin_python/plugin.toml) (+1/−1)



<a id="commit-35"></a>
### 35. feat: add python binding and stubs for PluginDescription {#commit-35}

- Source: [2ad0ddf075fb4a96cf54889d6759398d89e0ef54](https://github.com/EndstoneMC/endstone/commit/2ad0ddf075fb4a96cf54889d6759398d89e0ef54)
- Authored: 2023-12-22T02:06:00Z; parent: `9f8bbe26f854799157925cdf39921b305f65d818`
- Disposition: meaningful; full actual diff statically reviewed.

Turns PluginDescription from noncopyable polymorphic interface into copyable stored metadata value, exposes Python constructor/properties with ignored extra args/kwargs, and replaces dummy description with Python _get_description override. Constructor tests cover positional/keyword/dictionary/optional values. Description callback failure logs then terminates; Python wrapper's internal getter emits a deprecation warning even when legitimately called. Value conversion simplifies metadata but removes custom C++ virtual getters and changes ABI.

Changed-path evidence: [endstone_api/include/endstone/plugin/plugin_description.h](https://github.com/EndstoneMC/endstone/blob/2ad0ddf075fb4a96cf54889d6759398d89e0ef54/endstone_api/include/endstone/plugin/plugin_description.h) (+21/−14); [endstone_python/include/endstone_python/endstone_python.h](https://github.com/EndstoneMC/endstone/blob/2ad0ddf075fb4a96cf54889d6759398d89e0ef54/endstone_python/include/endstone_python/endstone_python.h) (+1/−0); [endstone_python/python/endstone/plugin.py](https://github.com/EndstoneMC/endstone/blob/2ad0ddf075fb4a96cf54889d6759398d89e0ef54/endstone_python/python/endstone/plugin.py) (+18/−5); [endstone_python/python/endstone/plugin.pyi](https://github.com/EndstoneMC/endstone/blob/2ad0ddf075fb4a96cf54889d6759398d89e0ef54/endstone_python/python/endstone/plugin.pyi) (+29/−0); [endstone_python/src/endstone_python/endstone_python.cpp](https://github.com/EndstoneMC/endstone/blob/2ad0ddf075fb4a96cf54889d6759398d89e0ef54/endstone_python/src/endstone_python/endstone_python.cpp) (+1/−0); [endstone_python/src/endstone_python/plugin/plugin.cpp](https://github.com/EndstoneMC/endstone/blob/2ad0ddf075fb4a96cf54889d6759398d89e0ef54/endstone_python/src/endstone_python/plugin/plugin.cpp) (+8/−4); [endstone_python/src/endstone_python/plugin/plugin_description.cpp](https://github.com/EndstoneMC/endstone/blob/2ad0ddf075fb4a96cf54889d6759398d89e0ef54/endstone_python/src/endstone_python/plugin/plugin_description.cpp) (+48/−0); [endstone_python/test/test_endstone.py](https://github.com/EndstoneMC/endstone/blob/2ad0ddf075fb4a96cf54889d6759398d89e0ef54/endstone_python/test/test_endstone.py) (+58/−1)



<a id="commit-36"></a>
### 36. fix: CppPluginLoader not working on Linux {#commit-36}

- Source: [906bfcc4197703414dce28518fad4a67876e63ad](https://github.com/EndstoneMC/endstone/commit/906bfcc4197703414dce28518fad4a67876e63ad)
- Authored: 2023-12-22T02:07:17Z; parent: `2ad0ddf075fb4a96cf54889d6759398d89e0ef54`
- Disposition: small-semantic; full actual diff statically reviewed.

Updates Linux loader initPlugin call to pass factory logger, completing the signature migration missed in commit 30. Narrow cross-platform build correction; Windows-only changes must be checked against both platform branches.

Changed-path evidence: [endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/906bfcc4197703414dce28518fad4a67876e63ad/endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp) (+1/−1)



<a id="commit-38"></a>
### 38. refactor: separate tests into multiple files {#commit-38}

- Source: [3fe97573961882a9ec0b7776af1f673caa00a1de](https://github.com/EndstoneMC/endstone/commit/3fe97573961882a9ec0b7776af1f673caa00a1de)
- Authored: 2023-12-22T02:31:47Z; parent: `753433be03f2d3a357f1440b8d2121b4920d5379`
- Disposition: small-semantic; full actual diff statically reviewed.

Splits import checks and PluginDescription constructor scenarios into separate pytest files/tests with shared class fixture. Existing assertion content is preserved while failures become individually attributable; no new production behavior.

Changed-path evidence: [endstone_python/test/test_endstone.py](https://github.com/EndstoneMC/endstone/blob/753433be03f2d3a357f1440b8d2121b4920d5379/endstone_python/test/test_endstone.py) (+0/−77); [endstone_python/test/test_imports.py](https://github.com/EndstoneMC/endstone/blob/3fe97573961882a9ec0b7776af1f673caa00a1de/endstone_python/test/test_imports.py) (+22/−0); [endstone_python/test/test_plugin_description.py](https://github.com/EndstoneMC/endstone/blob/3fe97573961882a9ec0b7776af1f673caa00a1de/endstone_python/test/test_plugin_description.py) (+69/−0)



<a id="commit-39"></a>
### 39. feat: add plugin loader for loading from source {#commit-39}

- Source: [af50240910edd59f7baebce8efee37e9379d3805](https://github.com/EndstoneMC/endstone/commit/af50240910edd59f7baebce8efee37e9379d3805)
- Authored: 2023-12-22T02:32:16Z; parent: `3fe97573961882a9ec0b7776af1f673caa00a1de`
- Disposition: meaningful; full actual diff statically reviewed.

Adds TOML description reader, explicit source module/package spec discovery and sys.modules caching, plugin subclass check and metadata attachment. Initial code checks name for module:class syntax instead of main, never assigns description.main, and calls self._create_plugin although helper is module-level. Loader's nodelete holder is dropped. Assertions are input validation and disappear under Python optimization; cache insertion before exec leaves partial modules on failure and name collisions reuse existing modules. These are static risks, not reproduced failures.

Changed-path evidence: [endstone_python/python/endstone/_internal/plugin_description_file.py](https://github.com/EndstoneMC/endstone/blob/af50240910edd59f7baebce8efee37e9379d3805/endstone_python/python/endstone/_internal/plugin_description_file.py) (+24/−0); [endstone_python/python/endstone/_internal/plugin_loader.py](https://github.com/EndstoneMC/endstone/blob/af50240910edd59f7baebce8efee37e9379d3805/endstone_python/python/endstone/_internal/plugin_loader.py) (+67/−0); [endstone_python/src/endstone_python/plugin/plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/af50240910edd59f7baebce8efee37e9379d3805/endstone_python/src/endstone_python/plugin/plugin_loader.cpp) (+1/−1)



<a id="commit-40"></a>
### 40. feat: add tests for property full_name of PluginDescription {#commit-40}

- Source: [af1e7516dd8c4e01ad6a2217118ec5aaaa7d7950](https://github.com/EndstoneMC/endstone/commit/af1e7516dd8c4e01ad6a2217118ec5aaaa7d7950)
- Authored: 2023-12-22T02:37:56Z; parent: `af50240910edd59f7baebce8efee37e9379d3805`
- Disposition: meaningful; full actual diff statically reviewed.

Expands description tests to normalized spaces and full_name formatting across constructor styles, plus negative author membership. Establishes explicit normalization expectations; invalid names, malformed versions and loader integration remain outside these tests.

Changed-path evidence: [endstone_python/test/test_plugin_description.py](https://github.com/EndstoneMC/endstone/blob/af1e7516dd8c4e01ad6a2217118ec5aaaa7d7950/endstone_python/test/test_plugin_description.py) (+8/−2)



<a id="commit-41"></a>
### 41. fix: add return_value_policy that is missing {#commit-41}

- Source: [02a0767e6da397cb05ce86ee0d11548826312c3d](https://github.com/EndstoneMC/endstone/commit/02a0767e6da397cb05ce86ee0d11548826312c3d)
- Authored: 2023-12-22T02:51:25Z; parent: `af1e7516dd8c4e01ad6a2217118ec5aaaa7d7950`
- Disposition: meaningful; full actual diff statically reviewed.

Adds reference return policies for load_plugin and server. This documents an attempted borrowing fix, but loadPlugin still returns unique_ptr and requires deeper holder/lifetime reasoning; policy alone does not establish safe ownership. The disable_plugin→enablePlugin mistake remains unchanged.

Changed-path evidence: [endstone_python/src/endstone_python/plugin/plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/02a0767e6da397cb05ce86ee0d11548826312c3d/endstone_python/src/endstone_python/plugin/plugin_loader.cpp) (+2/−2); [endstone_python/test/test_imports.py](https://github.com/EndstoneMC/endstone/blob/02a0767e6da397cb05ce86ee0d11548826312c3d/endstone_python/test/test_imports.py) (+2/−0)



<a id="commit-42"></a>
### 42. feat: add python interpreter to endstone::core {#commit-42}

- Source: [f592559df3932d2e6cdbca2f475f79e52713538e](https://github.com/EndstoneMC/endstone/commit/f592559df3932d2e6cdbca2f475f79e52713538e)
- Authored: 2023-12-22T12:25:14Z; parent: `02a0767e6da397cb05ce86ee0d11548826312c3d`
- Disposition: meaningful; full actual diff statically reviewed.

Adds C++ PythonPluginLoader adapter holding shared_ptr<PluginLoader>, importing/constructing Python loader under GIL, delegating filters/lifecycle and initializing returned plugin logger. Core now links pybind11::embed and transitive headers, loader enable/disable become virtual and Python binding uses shared_ptr. Test environment adds Python home/path information. Interpreter lifetime itself is not established here despite title; scope-based interpreter appears later.

Changed-path evidence: [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/f592559df3932d2e6cdbca2f475f79e52713538e/CMakeLists.txt) (+1/−1); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/f592559df3932d2e6cdbca2f475f79e52713538e/conanfile.py) (+1/−1); [endstone_api/include/endstone/plugin/plugin_loader.h](https://github.com/EndstoneMC/endstone/blob/f592559df3932d2e6cdbca2f475f79e52713538e/endstone_api/include/endstone/plugin/plugin_loader.h) (+2/−2); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/f592559df3932d2e6cdbca2f475f79e52713538e/endstone_core/CMakeLists.txt) (+2/−1); [endstone_core/include/endstone_core/plugin/python_plugin_loader.h](https://github.com/EndstoneMC/endstone/blob/f592559df3932d2e6cdbca2f475f79e52713538e/endstone_core/include/endstone_core/plugin/python_plugin_loader.h) (+34/−0); [endstone_core/src/endstone_core/plugin/python_plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/f592559df3932d2e6cdbca2f475f79e52713538e/endstone_core/src/endstone_core/plugin/python_plugin_loader.cpp) (+57/−0); [endstone_python/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/f592559df3932d2e6cdbca2f475f79e52713538e/endstone_python/CMakeLists.txt) (+3/−1); [endstone_python/src/endstone_python/plugin/plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/f592559df3932d2e6cdbca2f475f79e52713538e/endstone_python/src/endstone_python/plugin/plugin_loader.cpp) (+1/−1); [test_package/conanfile.py](https://github.com/EndstoneMC/endstone/blob/f592559df3932d2e6cdbca2f475f79e52713538e/test_package/conanfile.py) (+13/−0)



<a id="commit-43"></a>
### 43. feat: use smart_holder branch of pybind11 {#commit-43}

- Source: [8038a11021b170cbba46c567928c03bce3dc7a05](https://github.com/EndstoneMC/endstone/commit/8038a11021b170cbba46c567928c03bce3dc7a05)
- Authored: 2023-12-23T02:17:53Z; parent: `f592559df3932d2e6cdbca2f475f79e52713538e`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces Conan pybind11 dependency with CMake FetchContent pinned to smart_holder-branch commit b6444460, requiring CMake 3.24 and OVERRIDE_FIND_PACKAGE. Removes embed component from exported Conan requirements while resolving it in the build via fetched source. Exact revision is pinned but no archive digest is provided. This is a temporary dependency mechanism, later packaged in Conan.

Changed-path evidence: [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/8038a11021b170cbba46c567928c03bce3dc7a05/CMakeLists.txt) (+11/−1); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/8038a11021b170cbba46c567928c03bce3dc7a05/conanfile.py) (+1/−2); [endstone_api/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/f592559df3932d2e6cdbca2f475f79e52713538e/endstone_api/CMakeLists.txt) (+0/−1); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/f592559df3932d2e6cdbca2f475f79e52713538e/endstone_core/CMakeLists.txt) (+0/−1); [endstone_python/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/f592559df3932d2e6cdbca2f475f79e52713538e/endstone_python/CMakeLists.txt) (+0/−1)



<a id="commit-45"></a>
### 45. fix: typo in plugin_description_file.py {#commit-45}

- Source: [4c9b1a67c9eb95e2e796fcaa24dc55985e808fbc](https://github.com/EndstoneMC/endstone/commit/4c9b1a67c9eb95e2e796fcaa24dc55985e808fbc)
- Authored: 2023-12-23T02:36:23Z; parent: `583c6d60c56259bdaabcbf84ee21be25b93aa731`
- Disposition: small-semantic; full actual diff statically reviewed.

Fixes TOML main grammar validation to inspect main rather than name; still does not store main until commit 49. Also condenses FetchContent formatting with identical pinned URL. A narrow parser repair, not evidence the source loader is complete.

Changed-path evidence: [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/4c9b1a67c9eb95e2e796fcaa24dc55985e808fbc/CMakeLists.txt) (+1/−5); [endstone_python/python/endstone/_internal/plugin_description_file.py](https://github.com/EndstoneMC/endstone/blob/4c9b1a67c9eb95e2e796fcaa24dc55985e808fbc/endstone_python/python/endstone/_internal/plugin_description_file.py) (+2/−2)



<a id="commit-46"></a>
### 46. feat: enable progressive mode for pybind11's smart holder {#commit-46}

- Source: [e73d7a11f6e74e6746b3d3587d9a0d2f79d5555b](https://github.com/EndstoneMC/endstone/commit/e73d7a11f6e74e6746b3d3587d9a0d2f79d5555b)
- Authored: 2023-12-24T10:31:27Z; parent: `4c9b1a67c9eb95e2e796fcaa24dc55985e808fbc`
- Disposition: meaningful; full actual diff statically reviewed.

Enables smart_holder as default, changes Python loader implementation ownership shared_ptr→unique_ptr, removes explicit nodelete/shared holders and returns unique_ptr directly from the Python trampoline. Eliminates raw-pointer rewrapping. Correctness depends on all participating pybind translation units agreeing on holder mode, explored in subsequent packaging/definition fixes.

Changed-path evidence: [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/e73d7a11f6e74e6746b3d3587d9a0d2f79d5555b/CMakeLists.txt) (+1/−1); [endstone_core/include/endstone_core/plugin/python_plugin_loader.h](https://github.com/EndstoneMC/endstone/blob/e73d7a11f6e74e6746b3d3587d9a0d2f79d5555b/endstone_core/include/endstone_core/plugin/python_plugin_loader.h) (+1/−1); [endstone_core/src/endstone_core/plugin/python_plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/e73d7a11f6e74e6746b3d3587d9a0d2f79d5555b/endstone_core/src/endstone_core/plugin/python_plugin_loader.cpp) (+1/−1); [endstone_python/src/endstone_python/plugin/plugin.cpp](https://github.com/EndstoneMC/endstone/blob/e73d7a11f6e74e6746b3d3587d9a0d2f79d5555b/endstone_python/src/endstone_python/plugin/plugin.cpp) (+1/−1); [endstone_python/src/endstone_python/plugin/plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/e73d7a11f6e74e6746b3d3587d9a0d2f79d5555b/endstone_python/src/endstone_python/plugin/plugin_loader.cpp) (+2/−5)



<a id="commit-48"></a>
### 48. feat: use pybind11 recipe instead of FetchContent {#commit-48}

- Source: [00c1cfc24c53d52f81208ff19f35eacbf175884f](https://github.com/EndstoneMC/endstone/commit/00c1cfc24c53d52f81208ff19f35eacbf175884f)
- Authored: 2023-12-25T23:24:25Z; parent: `32684966003e7b1d429ae85686d0d78b30baaa7b`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces FetchContent with custom Conan smart_holder recipe pinned to the same upstream commit; CI and wheel hooks export it first. Moves version functions out of headers so private target definitions suffice, scopes holder definitions to core/extension/test, and creates scoped_interpreter in test main. Dependency source loses the imported release SHA256 map in favor of a commit archive without hash. Interpreter destruction before static server destruction becomes the next lifecycle issue.

Changed-path evidence: [.github/workflows/ci-linux.yml](https://github.com/EndstoneMC/endstone/blob/00c1cfc24c53d52f81208ff19f35eacbf175884f/.github/workflows/ci-linux.yml) (+2/−0); [.github/workflows/ci-windows.yml](https://github.com/EndstoneMC/endstone/blob/00c1cfc24c53d52f81208ff19f35eacbf175884f/.github/workflows/ci-windows.yml) (+1/−0); [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/32684966003e7b1d429ae85686d0d78b30baaa7b/CMakeLists.txt) (+0/−6); [conanfile.py](https://github.com/EndstoneMC/endstone/blob/00c1cfc24c53d52f81208ff19f35eacbf175884f/conanfile.py) (+2/−1); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/00c1cfc24c53d52f81208ff19f35eacbf175884f/endstone_core/CMakeLists.txt) (+3/−2); [endstone_core/include/endstone_core/endstone_server.h](https://github.com/EndstoneMC/endstone/blob/00c1cfc24c53d52f81208ff19f35eacbf175884f/endstone_core/include/endstone_core/endstone_server.h) (+2/−19); [endstone_core/src/endstone_core/endstone_server.cpp](https://github.com/EndstoneMC/endstone/blob/00c1cfc24c53d52f81208ff19f35eacbf175884f/endstone_core/src/endstone_core/endstone_server.cpp) (+10/−0); [endstone_python/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/00c1cfc24c53d52f81208ff19f35eacbf175884f/endstone_python/CMakeLists.txt) (+1/−0); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/00c1cfc24c53d52f81208ff19f35eacbf175884f/pyproject.toml) (+2/−0); [test_package/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/00c1cfc24c53d52f81208ff19f35eacbf175884f/test_package/CMakeLists.txt) (+3/−0); [test_package/src/test_server.cpp](https://github.com/EndstoneMC/endstone/blob/00c1cfc24c53d52f81208ff19f35eacbf175884f/test_package/src/test_server.cpp) (+6/−0); [third_party/pybind11/conandata.yml](https://github.com/EndstoneMC/endstone/blob/32684966003e7b1d429ae85686d0d78b30baaa7b/third_party/pybind11/conandata.yml) (+0/−25); [third_party/pybind11/conanfile.py](https://github.com/EndstoneMC/endstone/blob/00c1cfc24c53d52f81208ff19f35eacbf175884f/third_party/pybind11/conanfile.py) (+25/−10)



<a id="commit-49"></a>
### 49. feat: add python plugin loader to test_package {#commit-49}

- Source: [be5b7ab43ca20e93f8a43f67efea4fe796ce974d](https://github.com/EndstoneMC/endstone/commit/be5b7ab43ca20e93f8a43f67efea4fe796ce974d)
- Authored: 2023-12-27T02:15:59Z; parent: `00c1cfc24c53d52f81208ff19f35eacbf175884f`
- Disposition: meaningful; full actual diff statically reviewed.

Registers Python SourcePluginLoader and extends package test to C++ plus Python plugins, fixes main storage/source src directory/helper call, and adds trampoline_self_life_support to plugin and loader. Copies package source/bindings/fixture into test runtime and asserts both plugins' state transitions. Loader registration exceptions are logged, leaving C++ support available; no test outcome proves all shutdown paths.

Changed-path evidence: [endstone_core/src/endstone_core/endstone_server.cpp](https://github.com/EndstoneMC/endstone/blob/be5b7ab43ca20e93f8a43f67efea4fe796ce974d/endstone_core/src/endstone_core/endstone_server.cpp) (+10/−4); [endstone_python/python/endstone/_internal/plugin_description_file.py](https://github.com/EndstoneMC/endstone/blob/be5b7ab43ca20e93f8a43f67efea4fe796ce974d/endstone_python/python/endstone/_internal/plugin_description_file.py) (+1/−0); [endstone_python/python/endstone/_internal/plugin_loader.py](https://github.com/EndstoneMC/endstone/blob/be5b7ab43ca20e93f8a43f67efea4fe796ce974d/endstone_python/python/endstone/_internal/plugin_loader.py) (+5/−4); [endstone_python/src/endstone_python/plugin/plugin.cpp](https://github.com/EndstoneMC/endstone/blob/be5b7ab43ca20e93f8a43f67efea4fe796ce974d/endstone_python/src/endstone_python/plugin/plugin.cpp) (+1/−1); [endstone_python/src/endstone_python/plugin/plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/be5b7ab43ca20e93f8a43f67efea4fe796ce974d/endstone_python/src/endstone_python/plugin/plugin_loader.cpp) (+6/−4); [test_package/conanfile.py](https://github.com/EndstoneMC/endstone/blob/be5b7ab43ca20e93f8a43f67efea4fe796ce974d/test_package/conanfile.py) (+37/−12); [test_package/src/test_plugin_python/plugin.toml](https://github.com/EndstoneMC/endstone/blob/be5b7ab43ca20e93f8a43f67efea4fe796ce974d/test_package/src/test_plugin_python/plugin.toml) (+1/−1); [test_package/src/test_server.cpp](https://github.com/EndstoneMC/endstone/blob/be5b7ab43ca20e93f8a43f67efea4fe796ce974d/test_package/src/test_server.cpp) (+18/−6)



<a id="commit-50"></a>
### 50. fix: python interpreter to have the same lifecycle as the EndstoneServer {#commit-50}

- Source: [a88ffaf1b2c39761e68d429a00aa7c14596099d6](https://github.com/EndstoneMC/endstone/commit/a88ffaf1b2c39761e68d429a00aa7c14596099d6)
- Authored: 2023-12-28T00:11:12Z; parent: `be5b7ab43ca20e93f8a43f67efea4fe796ce974d`
- Disposition: meaningful; full actual diff statically reviewed.

Moves scoped_interpreter and gil_scoped_release into EndstoneServer members before plugin_manager, tying Python runtime to host lifetime. Reverse member destruction places manager destruction before GIL-release object's reacquisition and interpreter finalization; exact safety also depends on holders' GIL handling. Refactors test stages and acquires GIL explicitly for direct Python call. This corrects local interpreter/static host lifetime mismatch rather than merely reorganizing tests.

Changed-path evidence: [endstone_core/include/endstone_core/endstone_server.h](https://github.com/EndstoneMC/endstone/blob/a88ffaf1b2c39761e68d429a00aa7c14596099d6/endstone_core/include/endstone_core/endstone_server.h) (+5/−0); [test_package/src/test_server.cpp](https://github.com/EndstoneMC/endstone/blob/a88ffaf1b2c39761e68d429a00aa7c14596099d6/test_package/src/test_server.cpp) (+43/−13)



<a id="commit-51"></a>
### 51. refactor: remove __version__ and __minecraft_version__ from package `endstone` {#commit-51}

- Source: [5fdcf09a2bc9d2354e14d7cb6dd7dca4c9651bb0](https://github.com/EndstoneMC/endstone/commit/5fdcf09a2bc9d2354e14d7cb6dd7dca4c9651bb0)
- Authored: 2023-12-28T00:30:39Z; parent: `a88ffaf1b2c39761e68d429a00aa7c14596099d6`
- Disposition: small-semantic; full actual diff statically reviewed.

Removes public package __version__/__minecraft_version__ and matching tests/stubs. Eliminates import-time four-component parsing; source does not state a broader version-policy preference. Internal generated version remains for CLI later.

Changed-path evidence: [endstone_python/python/endstone/__init__.py](https://github.com/EndstoneMC/endstone/blob/a88ffaf1b2c39761e68d429a00aa7c14596099d6/endstone_python/python/endstone/__init__.py) (+0/−6); [endstone_python/python/endstone/__init__.pyi](https://github.com/EndstoneMC/endstone/blob/a88ffaf1b2c39761e68d429a00aa7c14596099d6/endstone_python/python/endstone/__init__.pyi) (+0/−3); [endstone_python/test/test_imports.py](https://github.com/EndstoneMC/endstone/blob/a88ffaf1b2c39761e68d429a00aa7c14596099d6/endstone_python/test/test_imports.py) (+0/−4)



<a id="commit-52"></a>
### 52. refactor: move Server and Logger to separate modules {#commit-52}

- Source: [1d6fdbcf24079a85798a1b94a6c1a81e97a563ac](https://github.com/EndstoneMC/endstone/commit/1d6fdbcf24079a85798a1b94a6c1a81e97a563ac)
- Authored: 2023-12-28T00:40:50Z; parent: `5fdcf09a2bc9d2354e14d7cb6dd7dca4c9651bb0`
- Disposition: meaningful; full actual diff statically reviewed.

Moves Logger/Server into dedicated public modules with matching stubs/import tests, leaving package root empty and updating plugin type imports. Breaking import-layout migration is coordinated across code and tests; preserve module names by historical version.

Changed-path evidence: [endstone_python/python/endstone/__init__.py](https://github.com/EndstoneMC/endstone/blob/5fdcf09a2bc9d2354e14d7cb6dd7dca4c9651bb0/endstone_python/python/endstone/__init__.py) (+0/−6); [endstone_python/python/endstone/__init__.pyi](https://github.com/EndstoneMC/endstone/blob/5fdcf09a2bc9d2354e14d7cb6dd7dca4c9651bb0/endstone_python/python/endstone/__init__.pyi) (+0/−87); [endstone_python/python/endstone/logger.py](https://github.com/EndstoneMC/endstone/blob/1d6fdbcf24079a85798a1b94a6c1a81e97a563ac/endstone_python/python/endstone/logger.py) (+3/−0); [endstone_python/python/endstone/logger.pyi](https://github.com/EndstoneMC/endstone/blob/1d6fdbcf24079a85798a1b94a6c1a81e97a563ac/endstone_python/python/endstone/logger.pyi) (+80/−0); [endstone_python/python/endstone/plugin.pyi](https://github.com/EndstoneMC/endstone/blob/1d6fdbcf24079a85798a1b94a6c1a81e97a563ac/endstone_python/python/endstone/plugin.pyi) (+2/−1); [endstone_python/python/endstone/server.py](https://github.com/EndstoneMC/endstone/blob/1d6fdbcf24079a85798a1b94a6c1a81e97a563ac/endstone_python/python/endstone/server.py) (+3/−0); [endstone_python/python/endstone/server.pyi](https://github.com/EndstoneMC/endstone/blob/1d6fdbcf24079a85798a1b94a6c1a81e97a563ac/endstone_python/python/endstone/server.pyi) (+6/−0); [endstone_python/test/test_imports.py](https://github.com/EndstoneMC/endstone/blob/1d6fdbcf24079a85798a1b94a6c1a81e97a563ac/endstone_python/test/test_imports.py) (+7/−5)



<a id="commit-54"></a>
### 54. feat: improve python api stubs {#commit-54}

- Source: [b6d265f68dac73b4bcbcc2a9c3a8294e971c0edc](https://github.com/EndstoneMC/endstone/commit/b6d265f68dac73b4bcbcc2a9c3a8294e971c0edc)
- Authored: 2023-12-28T01:38:54Z; parent: `c7579a84b1180c375da08f000a154ec365375ad0`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces direct extension imports in public wrappers with import_module plus controlled globals aliases, adds typed source-loader helper and imports public API classes. Commit title says stubs but change is runtime facade construction. No explicit explanation establishes why dynamic indirection helps tooling; record that motive as unknown.

Changed-path evidence: [endstone_python/python/endstone/_internal/plugin_loader.py](https://github.com/EndstoneMC/endstone/blob/b6d265f68dac73b4bcbcc2a9c3a8294e971c0edc/endstone_python/python/endstone/_internal/plugin_loader.py) (+3/−5); [endstone_python/python/endstone/logger.py](https://github.com/EndstoneMC/endstone/blob/b6d265f68dac73b4bcbcc2a9c3a8294e971c0edc/endstone_python/python/endstone/logger.py) (+7/−2); [endstone_python/python/endstone/plugin.py](https://github.com/EndstoneMC/endstone/blob/b6d265f68dac73b4bcbcc2a9c3a8294e971c0edc/endstone_python/python/endstone/plugin.py) (+9/−3); [endstone_python/python/endstone/server.py](https://github.com/EndstoneMC/endstone/blob/b6d265f68dac73b4bcbcc2a9c3a8294e971c0edc/endstone_python/python/endstone/server.py) (+7/−2); [endstone_python/python/endstone/server.pyi](https://github.com/EndstoneMC/endstone/blob/b6d265f68dac73b4bcbcc2a9c3a8294e971c0edc/endstone_python/python/endstone/server.pyi) (+1/−1)



<a id="commit-55"></a>
### 55. feat: add more methods for Server's python binding {#commit-55}

- Source: [6f09f142e69c0b0d70c31331f7a4f481496f327a](https://github.com/EndstoneMC/endstone/commit/6f09f142e69c0b0d70c31331f7a4f481496f327a)
- Authored: 2023-12-28T01:47:44Z; parent: `b6d265f68dac73b4bcbcc2a9c3a8294e971c0edc`
- Disposition: meaningful; full actual diff statically reviewed.

Exposes Server.logger using reference policy and version/minecraft_version properties with stubs; plugin_manager remains commented. Borrowed logger lifetime still follows server/factory, while strings convert as values. No new behavioral tests accompany these properties.

Changed-path evidence: [endstone_python/python/endstone/server.pyi](https://github.com/EndstoneMC/endstone/blob/6f09f142e69c0b0d70c31331f7a4f481496f327a/endstone_python/python/endstone/server.pyi) (+23/−1); [endstone_python/src/endstone_python/server.cpp](https://github.com/EndstoneMC/endstone/blob/6f09f142e69c0b0d70c31331f7a4f481496f327a/endstone_python/src/endstone_python/server.cpp) (+8/−1)



<a id="commit-56"></a>
### 56. fix: remove warnings as it will also be triggered by internal calls {#commit-56}

- Source: [8c8bf1f8e8a9139319ea8e43be4da55976e38289](https://github.com/EndstoneMC/endstone/commit/8c8bf1f8e8a9139319ea8e43be4da55976e38289)
- Authored: 2023-12-28T02:12:45Z; parent: `6f09f142e69c0b0d70c31331f7a4f481496f327a`
- Disposition: small-semantic; full actual diff statically reviewed.

Removes deprecated warning from internal description getter and warnings import. Title explicitly explains internal calls also trigger it. This is evidence for avoiding noisy warnings in required internal paths, not for avoiding deprecation warnings generally.

Changed-path evidence: [endstone_python/python/endstone/plugin.py](https://github.com/EndstoneMC/endstone/blob/6f09f142e69c0b0d70c31331f7a4f481496f327a/endstone_python/python/endstone/plugin.py) (+0/−9)



<a id="commit-57"></a>
### 57. feat: improve python api stubs {#commit-57}

- Source: [2ae7edd69ab9d3a1748a304947cbbbdafd75a19f](https://github.com/EndstoneMC/endstone/commit/2ae7edd69ab9d3a1748a304947cbbbdafd75a19f)
- Authored: 2023-12-28T02:17:34Z; parent: `8c8bf1f8e8a9139319ea8e43be4da55976e38289`
- Disposition: mechanical; full actual diff statically reviewed.

Splits __all__ assignment from iteration and relocates import_module inside loop in three facades; reorders PluginDescription import after tomllib/tomli selection. Exported names and conversions remain the same; no independent architectural preference inferred.

Changed-path evidence: [endstone_python/python/endstone/_internal/plugin_description_file.py](https://github.com/EndstoneMC/endstone/blob/2ae7edd69ab9d3a1748a304947cbbbdafd75a19f/endstone_python/python/endstone/_internal/plugin_description_file.py) (+2/−2); [endstone_python/python/endstone/logger.py](https://github.com/EndstoneMC/endstone/blob/2ae7edd69ab9d3a1748a304947cbbbdafd75a19f/endstone_python/python/endstone/logger.py) (+4/−2); [endstone_python/python/endstone/plugin.py](https://github.com/EndstoneMC/endstone/blob/2ae7edd69ab9d3a1748a304947cbbbdafd75a19f/endstone_python/python/endstone/plugin.py) (+4/−2); [endstone_python/python/endstone/server.py](https://github.com/EndstoneMC/endstone/blob/2ae7edd69ab9d3a1748a304947cbbbdafd75a19f/endstone_python/python/endstone/server.py) (+4/−2)



<a id="commit-58"></a>
### 58. feat: add python binding and stubs for `PluginManager` {#commit-58}

- Source: [992206db916dacf366c9df37a7b7eb9abb2f435d](https://github.com/EndstoneMC/endstone/commit/992206db916dacf366c9df37a7b7eb9abb2f435d)
- Authored: 2023-12-28T09:28:21Z; parent: `2ae7edd69ab9d3a1748a304947cbbbdafd75a19f`
- Disposition: meaningful; full actual diff statically reviewed.

Adds PluginManager binding/stubs, overloads name/object enabled checks, references for individual get/load calls and lifecycle controls. List-of-pointer properties/load results lack explicit reference policy, while stubs promise Plugin despite nullable lookup/load results; these need targeted ownership/None tests. load_plugin keyword is named plugin rather than file in C++, unlike the stub.

Changed-path evidence: [endstone_python/include/endstone_python/endstone_python.h](https://github.com/EndstoneMC/endstone/blob/992206db916dacf366c9df37a7b7eb9abb2f435d/endstone_python/include/endstone_python/endstone_python.h) (+1/−0); [endstone_python/python/endstone/plugin.py](https://github.com/EndstoneMC/endstone/blob/992206db916dacf366c9df37a7b7eb9abb2f435d/endstone_python/python/endstone/plugin.py) (+8/−2); [endstone_python/python/endstone/plugin.pyi](https://github.com/EndstoneMC/endstone/blob/992206db916dacf366c9df37a7b7eb9abb2f435d/endstone_python/python/endstone/plugin.pyi) (+23/−10); [endstone_python/src/endstone_python/endstone_python.cpp](https://github.com/EndstoneMC/endstone/blob/992206db916dacf366c9df37a7b7eb9abb2f435d/endstone_python/src/endstone_python/endstone_python.cpp) (+1/−0); [endstone_python/src/endstone_python/plugin/plugin_manager.cpp](https://github.com/EndstoneMC/endstone/blob/992206db916dacf366c9df37a7b7eb9abb2f435d/endstone_python/src/endstone_python/plugin/plugin_manager.cpp) (+43/−0)



<a id="commit-59"></a>
### 59. feat: add property 'plugin_manager' to the python binding for class `Server` {#commit-59}

- Source: [e0ef42a510b682ba34021a3b928e5093b5acedbc](https://github.com/EndstoneMC/endstone/commit/e0ef42a510b682ba34021a3b928e5093b5acedbc)
- Authored: 2023-12-28T09:34:07Z; parent: `992206db916dacf366c9df37a7b7eb9abb2f435d`
- Disposition: meaningful; full actual diff statically reviewed.

Enables borrowed Server.plugin_manager property and performs small test cleanup. Does not add corresponding Server stub here or behavioral test; API discovery and typing can drift even when binding compiles.

Changed-path evidence: [endstone_python/src/endstone_python/server.cpp](https://github.com/EndstoneMC/endstone/blob/e0ef42a510b682ba34021a3b928e5093b5acedbc/endstone_python/src/endstone_python/server.cpp) (+1/−1); [test_package/src/test_plugin.cpp](https://github.com/EndstoneMC/endstone/blob/e0ef42a510b682ba34021a3b928e5093b5acedbc/test_package/src/test_plugin.cpp) (+1/−1); [test_package/src/test_server.cpp](https://github.com/EndstoneMC/endstone/blob/e0ef42a510b682ba34021a3b928e5093b5acedbc/test_package/src/test_server.cpp) (+2/−3)



<a id="commit-70"></a>
### 70. feat: update CMakeLists.txt (endstone_core) {#commit-70}

- Source: [156c6f0b3f8a2c3ef26137cdd79ee870a7c6343c](https://github.com/EndstoneMC/endstone/commit/156c6f0b3f8a2c3ef26137cdd79ee870a7c6343c)
- Authored: 2024-01-02T23:42:22Z; parent: `5b9cb93f940d8aab357d6139c2b5c35498f78120`
- Disposition: meaningful; full actual diff statically reviewed.

Makes core's dl/stdc++fs links and smart_holder/version definitions PUBLIC in CMake, propagating compile/link assumptions to dependent targets. This repairs consumer consistency after private-scoping changes; version definition may be broader than needed, and Conan consumers need matching metadata separately.

Changed-path evidence: [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/156c6f0b3f8a2c3ef26137cdd79ee870a7c6343c/endstone_core/CMakeLists.txt) (+3/−3)



<a id="commit-87"></a>
### 87. fix: add compile definitions to fix pybind11 errors on Windows {#commit-87}

- Source: [aee2f62ad6540fe3330bbacd53d12faf37854ec1](https://github.com/EndstoneMC/endstone/commit/aee2f62ad6540fe3330bbacd53d12faf37854ec1)
- Authored: 2024-01-05T14:22:17Z; parent: `c4795ad263165de632820a69e1eaa5860e1cf993`
- Disposition: meaningful; full actual diff statically reviewed.

Globally enables smart_holder, detailed errors and PYBIND11_NO_ASSERT_GIL_HELD_INCREF_DECREF, updates smart_holder pin and removes per-target definitions. Comment explicitly calls assertion suppression a temporary Windows shutdown workaround whose cause is undetermined, linked to pybind11 issue4748. Do not record this as a solved GIL bug or recommend suppressing safety checks generally.

Changed-path evidence: [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/aee2f62ad6540fe3330bbacd53d12faf37854ec1/CMakeLists.txt) (+10/−0); [endstone_core/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/c4795ad263165de632820a69e1eaa5860e1cf993/endstone_core/CMakeLists.txt) (+0/−1); [endstone_python/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/c4795ad263165de632820a69e1eaa5860e1cf993/endstone_python/CMakeLists.txt) (+0/−5); [third_party/pybind11/conanfile.py](https://github.com/EndstoneMC/endstone/blob/aee2f62ad6540fe3330bbacd53d12faf37854ec1/third_party/pybind11/conanfile.py) (+2/−2)



<a id="commit-91"></a>
### 91. feat: add PYBIND11_USE_SMART_HOLDER_AS_DEFAULT to endstone_core components in conanfile.py {#commit-91}

- Source: [62c2e5d7e25a4032992b9e48ea9a7112d1336951](https://github.com/EndstoneMC/endstone/commit/62c2e5d7e25a4032992b9e48ea9a7112d1336951)
- Authored: 2024-01-05T16:53:49Z; parent: `d1d75524d8edbedac293a6d4f09d19ae4974bd59`
- Disposition: meaningful; full actual diff statically reviewed.

Exports smart_holder define through Conan core metadata and removes consumer's manual test definition, demonstrating CMake PUBLIC settings alone were insufficient for packaged consumers. Adds dummy_bedrock.cpp to test build before the file lands in following commit, so this intermediate revision may not configure independently.

Changed-path evidence: [conanfile.py](https://github.com/EndstoneMC/endstone/blob/62c2e5d7e25a4032992b9e48ea9a7112d1336951/conanfile.py) (+1/−0); [test_package/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/62c2e5d7e25a4032992b9e48ea9a7112d1336951/test_package/CMakeLists.txt) (+1/−2)



<a id="commit-113"></a>
### 113. refactor(endstone_runtime): use cci package pybind11 instead of pybind11 smart_holder branch {#commit-113}

- Source: [cdb7a4c5d3e9651bc3a3906e2cefb86b01a7f03d](https://github.com/EndstoneMC/endstone/commit/cdb7a4c5d3e9651bc3a3906e2cefb86b01a7f03d)
- Authored: 2024-01-12T14:36:59Z; parent: `9c439fb33def7000c99f707782b07c55be2763aa`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces custom smart_holder pybind11 with ConanCenter pybind11/2.11.1 and removes trampoline_self_life_support inheritance. Deletes the complete custom pybind11 recipe/tests and the now-unused MinHook recipe, upstream CMake patches and tests. This is an ownership strategy change plus dependency cleanup; holder and workflow follow-through arrives at114–117. Imported MinHook/ConanCenter material is not original Endstone implementation.

Changed-path evidence: [conanfile.py](https://github.com/EndstoneMC/endstone/blob/cdb7a4c5d3e9651bc3a3906e2cefb86b01a7f03d/conanfile.py) (+1/−1); [endstone_python/src/endstone_python/plugin/plugin.cpp](https://github.com/EndstoneMC/endstone/blob/cdb7a4c5d3e9651bc3a3906e2cefb86b01a7f03d/endstone_python/src/endstone_python/plugin/plugin.cpp) (+1/−1); [endstone_python/src/endstone_python/plugin/plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/cdb7a4c5d3e9651bc3a3906e2cefb86b01a7f03d/endstone_python/src/endstone_python/plugin/plugin_loader.cpp) (+1/−1); [third_party/minhook/conandata.yml](https://github.com/EndstoneMC/endstone/blob/9c439fb33def7000c99f707782b07c55be2763aa/third_party/minhook/conandata.yml) (+0/−13); [third_party/minhook/conanfile.py](https://github.com/EndstoneMC/endstone/blob/9c439fb33def7000c99f707782b07c55be2763aa/third_party/minhook/conanfile.py) (+0/−95); [third_party/minhook/patches/0001-add-cmake-support.patch](https://github.com/EndstoneMC/endstone/blob/9c439fb33def7000c99f707782b07c55be2763aa/third_party/minhook/patches/0001-add-cmake-support.patch) (+0/−204); [third_party/minhook/patches/0002-increase-cmake-min-version.patch](https://github.com/EndstoneMC/endstone/blob/9c439fb33def7000c99f707782b07c55be2763aa/third_party/minhook/patches/0002-increase-cmake-min-version.patch) (+0/−13); [third_party/minhook/test_package/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/9c439fb33def7000c99f707782b07c55be2763aa/third_party/minhook/test_package/CMakeLists.txt) (+0/−8); [third_party/minhook/test_package/conanfile.py](https://github.com/EndstoneMC/endstone/blob/9c439fb33def7000c99f707782b07c55be2763aa/third_party/minhook/test_package/conanfile.py) (+0/−27); [third_party/minhook/test_package/test_package.cpp](https://github.com/EndstoneMC/endstone/blob/9c439fb33def7000c99f707782b07c55be2763aa/third_party/minhook/test_package/test_package.cpp) (+0/−75); [third_party/pybind11/conanfile.py](https://github.com/EndstoneMC/endstone/blob/9c439fb33def7000c99f707782b07c55be2763aa/third_party/pybind11/conanfile.py) (+0/−95); [third_party/pybind11/test_package/CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/9c439fb33def7000c99f707782b07c55be2763aa/third_party/pybind11/test_package/CMakeLists.txt) (+0/−5); [third_party/pybind11/test_package/conanfile.py](https://github.com/EndstoneMC/endstone/blob/9c439fb33def7000c99f707782b07c55be2763aa/third_party/pybind11/test_package/conanfile.py) (+0/−53); [third_party/pybind11/test_package/test.py](https://github.com/EndstoneMC/endstone/blob/9c439fb33def7000c99f707782b07c55be2763aa/third_party/pybind11/test_package/test.py) (+0/−5); [third_party/pybind11/test_package/test_package.cpp](https://github.com/EndstoneMC/endstone/blob/9c439fb33def7000c99f707782b07c55be2763aa/third_party/pybind11/test_package/test_package.cpp) (+0/−16)



<a id="commit-114"></a>
### 114. refactor: use shared_ptr as the holder for PluginLoader {#commit-114}

- Source: [6f67d47312602ceb4b522a1ba8dd8741b80a5159](https://github.com/EndstoneMC/endstone/commit/6f67d47312602ceb4b522a1ba8dd8741b80a5159)
- Authored: 2024-01-12T15:01:13Z; parent: `cdb7a4c5d3e9651bc3a3906e2cefb86b01a7f03d`
- Disposition: meaningful; full actual diff statically reviewed.

Changes loader registration, associations and pybind holder to shared_ptr; storing a copy for every filter fixes moving the sole unique_ptr into the first filter. Python adapter retains py::object and casts shared_ptr on demand; destructor explicitly dec_refs under GIL but does not clear ownership, risking a second automatic decrement until115 adds release(). The Python load trampoline is temporarily replaced by unconditional nullptr, an explicit functionality gap despite refactor title. No new multi-filter or destruction regression test is included.

Changed-path evidence: [endstone_api/include/endstone/plugin/plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/6f67d47312602ceb4b522a1ba8dd8741b80a5159/endstone_api/include/endstone/plugin/plugin_manager.h) (+1/−1); [endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/6f67d47312602ceb4b522a1ba8dd8741b80a5159/endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h) (+2/−2); [endstone_core/include/endstone_core/plugin/python_plugin_loader.h](https://github.com/EndstoneMC/endstone/blob/6f67d47312602ceb4b522a1ba8dd8741b80a5159/endstone_core/include/endstone_core/plugin/python_plugin_loader.h) (+4/−1); [endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp](https://github.com/EndstoneMC/endstone/blob/6f67d47312602ceb4b522a1ba8dd8741b80a5159/endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp) (+2/−2); [endstone_core/src/endstone_core/plugin/python_plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/6f67d47312602ceb4b522a1ba8dd8741b80a5159/endstone_core/src/endstone_core/plugin/python_plugin_loader.cpp) (+16/−6); [endstone_python/src/endstone_python/plugin/plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/6f67d47312602ceb4b522a1ba8dd8741b80a5159/endstone_python/src/endstone_python/plugin/plugin_loader.cpp) (+11/−10)



<a id="commit-115"></a>
### 115. refactor: use shared_ptr as the holder for Plugin {#commit-115}

- Source: [cdebe1d5c732c99b0822af251dd1a55370947c09](https://github.com/EndstoneMC/endstone/commit/cdebe1d5c732c99b0822af251dd1a55370947c09)
- Authored: 2024-01-12T16:00:49Z; parent: `6f67d47312602ceb4b522a1ba8dd8741b80a5159`
- Disposition: meaningful; full actual diff statically reviewed.

Changes Plugin load and manager storage to shared_ptr, restores Python load trampoline, and keeps Python-created plugins alive in SourcePluginLoader._keep_alive. Adds release() after explicit dec_ref under GIL in the loader destructor and disables smart-holder/GIL-assert suppression macros. Native loadPlugin becomes noexcept, but Linux definition initially omits it until117. Retained list is not pruned on manager clear; shared ownership does not by itself solve borrowed server/loader lifetimes or GIL safety of pimpl()->cast, which has no local acquire. These are source-level concerns, not observed crashes.

Changed-path evidence: [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/CMakeLists.txt) (+2/−2); [endstone_api/include/endstone/plugin/plugin_loader.h](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/endstone_api/include/endstone/plugin/plugin_loader.h) (+1/−1); [endstone_core/include/endstone_core/plugin/cpp_plugin_loader.h](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/endstone_core/include/endstone_core/plugin/cpp_plugin_loader.h) (+1/−1); [endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/endstone_core/include/endstone_core/plugin/endstone_plugin_manager.h) (+1/−1); [endstone_core/include/endstone_core/plugin/python_plugin_loader.h](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/endstone_core/include/endstone_core/plugin/python_plugin_loader.h) (+1/−1); [endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp) (+4/−4); [endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/endstone_core/src/endstone_core/plugin/endstone_plugin_manager.cpp) (+3/−4); [endstone_core/src/endstone_core/plugin/python_plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/endstone_core/src/endstone_core/plugin/python_plugin_loader.cpp) (+2/−1); [endstone_python/python/endstone/_internal/plugin_loader.py](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/endstone_python/python/endstone/_internal/plugin_loader.py) (+9/−1); [endstone_python/src/endstone_python/plugin/plugin.cpp](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/endstone_python/src/endstone_python/plugin/plugin.cpp) (+1/−1); [endstone_python/src/endstone_python/plugin/plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/cdebe1d5c732c99b0822af251dd1a55370947c09/endstone_python/src/endstone_python/plugin/plugin_loader.cpp) (+10/−11)



<a id="commit-117"></a>
### 117. refactor: include a missing `noexcept`, remove uncessary compile definitions {#commit-117}

- Source: [35b4c6b749f0f88a5893fb8b7d2d82558aab8383](https://github.com/EndstoneMC/endstone/commit/35b4c6b749f0f88a5893fb8b7d2d82558aab8383)
- Authored: 2024-01-12T16:13:03Z; parent: `e93668c70c8642dce65f116aa084dce97587b9a9`
- Disposition: meaningful; full actual diff statically reviewed.

Adds missing noexcept to Linux CppPluginLoader definition, matching changed declaration115. Removes commented-out smart-holder and GIL assertion suppression definitions plus the documented unresolved Windows shutdown warning. Deleting the workaround comment does not prove the root cause resolved; the ownership rewrite is the nearby concrete change.

Changed-path evidence: [CMakeLists.txt](https://github.com/EndstoneMC/endstone/blob/e93668c70c8642dce65f116aa084dce97587b9a9/CMakeLists.txt) (+0/−6); [endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp](https://github.com/EndstoneMC/endstone/blob/35b4c6b749f0f88a5893fb8b7d2d82558aab8383/endstone_core/src/endstone_core/plugin/cpp_plugin_loader.cpp) (+1/−1)
