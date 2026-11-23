<!-- retrieval: {"source_ids":["public:commit:04284b19d39d2d3bca9557db58bce7fa7fbb23a6","public:commit:0f26a54e08bdb8da80aae78660bd6499807f8776","public:commit:1115d40660719b59682e56035be304a8f583ab31","public:commit:1255f6d6cb5e1c8e788b4628e2c2808872a94d51","public:commit:157f9c003bca423f09d0b2013e242ad7873e310e","public:commit:15c1ad1c4f1058909416354693a7c0f56e71f169","public:commit:1d60496efdccd17f08a3e6f8aeab1f0cffd7f26e","public:commit:1f7a48003f5d36bab1e81f61b30c62499b881e9d","public:commit:26d35af5f66c6e2cf12d0a5fcd0c8a4ab463af74","public:commit:35b01988266720b6e6acbebcc161d2ab4d957f21","public:commit:3b9610ec752e1f4dc1478656fe09da5eae45253e","public:commit:3fda97f670e704dcde16862fc20d07ea0adc62c6","public:commit:64206db0488f503d8a475bfa6bb39560d56b4d2c","public:commit:65b9a227f197b727e1fcd1d1706704a55c34795b","public:commit:733f09aa3bfc03dfe3bec0405c8084b2c8d9599b","public:commit:747e3372f2b68aeaee2a4d55f4371407ade68564","public:commit:7902769ad1604877dd3407291c133d53b07c1ab0","public:commit:7d942e1a437662f6eba25d7a7487ad03eb51031d","public:commit:8376e0bed07c83d41948f0a5b43fc4bceec063a4","public:commit:86f72dba0eb0e7821aea5aa3d392aef0975a2e35","public:commit:8b3b757575e09a9fa429018a6d9320e3bdeaaaf0","public:commit:8bf54893ad6dc53d9db9ca79593f739a047c7417","public:commit:8c9f7e9dfe2fa8e9a8df481541e38ffa226e73e0","public:commit:8f87f0dbfee3bf8ff21cbbb1131cc357dc25e2f6","public:commit:96416061e8770d0ae0056194a57d273a0bb6bd48","public:commit:96f657aad6806e5addca3d886531cd99364c4fd7","public:commit:97db96fd8a8233ae62bb716bef348d277418bc42","public:commit:9af6251702e3c3413e6ba0b3779f7fff3905febc","public:commit:9c0e1c579dd9596fd5614367c546e416e3b1258b","public:commit:9cf94b27af9b1c0383ecb8cc6466ab69d20d56e2","public:commit:9db2de085d19750738b1e678d7550434525c04e6","public:commit:a6bcee8f03ca4410d50b87f88e86d538feadf508","public:commit:aae8bde0c7dc8236f969d4174119b9618cf57f7e","public:commit:b19f531d0ab2b9dad9c0d91db27ba72f97dcff73","public:commit:b1c188d2c2903d9464dec2760299c28a31deec46","public:commit:c2476486f293bb9a4242234e821a9a96cce6a520","public:commit:cb6af2ff0803f1029acc9e3d3018df342bc04c82","public:commit:dc6a8427de85e7b00c59451af9379e91595f8c64","public:commit:e65a25b17c96424de8df8f07aa4aef009e46a3ba","public:commit:ea95d2f7b78d0ceaec60daa7b6463f4558e11271","public:commit:edb53e6cf66f6682fc9daf69e1fedef74e782679","public:commit:f7cf1388333ad371395e21c156c9b8c4e174a845","public:commit:fa159c8dd32f325ab6109637ec7d00704d9ab3e7"],"source_type":"public","date":"2024-03-05..2024-03-13","topics":["lifetime","concurrency","ffi","testing","api","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Plugin APIs, Python wrappers and shutdown ownership {#plugin-apis-python-wrappers-and-shutdown-ownership}

## Result: native ownership and Python wrapper lifetime are separate {#result-native-ownership-and-python-wrapper-lifetime-are-separate}

This unit exposes command registration and callbacks to Python while repeatedly refining native holders, binding aliases and wrapper retention. A shared C++ object does not automatically preserve every Python override object. The implementation first fixes callback routing and keep-alive cardinality, then addresses shutdown lifetime. Source comments and titles report concrete problems, but this review does not claim a reproduced failure or passing runtime test.

## Command construction, ownership and dispatch {#command-construction-ownership-and-dispatch}

267–269 add plugin command lookup and registration. The initial template constructs a custom CommandType, then wraps its metadata in a PluginCommand with a borrowed Plugin owner. Custom execute code is not retained in that wrapping step; actual execution goes to an executor or owner callback. 271 makes base Command executable with a default false result, allowing it to act as metadata. 313–314 eventually replace template metadata construction with direct name, description, usages and aliases and make the base constructor protected. This is a concrete movement toward separating metadata from execution, not proof that subclassing is generally rejected.

The server initially takes unique ownership into a map that uses shared pointers. 298 changes the public input and pybind holders to shared ownership so Python-created commands can be registered. 299 adds a Python PluginCommand facade and virtual executor accessors, retaining a custom executor in Python. Plugin initially retains only one command wrapper. 301 replaces that slot with a list because registering a second command must not release the first wrapper. The list is appended before registration succeeds, so failed registrations are also retained. 303 aligns executor and plugin holders and represents the default executor as a fallback to the owner rather than storing an explicit owner executor.

The native PluginCommand continues to borrow its Plugin owner. Plugin lookup lowercases a name but does not check that the returned command belongs to that plugin, despite its documentation. Native shared ownership, Python retention, owner lifetime and namespace/authorization rules are therefore different contracts. The endpoint's manager clear now destroys loaders as well as clearing borrowed plugin entries; command-map lifetime must be considered alongside that change rather than reasoning about the manager in isolation.

## Python inheritance is not a C++ trampoline {#python-inheritance-is-not-a-c-trampoline}

292 creates an executor binding but initially looks up `onCommand` instead of Python's `on_command`; 297 corrects the mapping. 293 declares Plugin as a Python subclass of CommandExecutor, yet 305 still needs an explicit onCommand override in PyPlugin. Python type inheritance did not install the missing C++ virtual override. 315 similarly fixes a factory to return the PyPluginCommand alias rather than a plain PluginCommand, ensuring the constructed C++ object has the trampoline.

302 passes callback arguments using reference wrappers to avoid unintended value conversion. This does not extend the underlying sender/command/argument lifetime beyond the callback. The temporary sender used for nonserver origins later reinforces that limit. A Python consumer retaining a borrowed sender requires a separate lifetime contract; stubs and reference-return policies alone do not establish it.

Tests in this range mostly restore synthetic TestServer conformance when signatures change. Null-returning fixture implementations do not validate registration or callback dispatch. No callback success log or automated lifetime test accompanies the reported repairs. Preserve the distinction between implementation intent, reported bug title and verified source change.

## Binding initialization: static caches are tried and removed {#binding-initialization-static-caches-are-tried-and-removed}

286 consolidates plugin binding translation units and introduces a templated static py::class_ cache so types can be forward-created and enriched later. 287 applies it broadly, and 288 retracts its generic Extra-argument forwarding. 304 temporarily suppresses pybind's GIL-held refcount assertions after a reported shutdown crash. 306 explicitly attributes the issue to cached class wrappers being destroyed without the GIL, removes the static helper and reenables assertions.

307 retains forward type availability by creating class wrappers as ordinary local module-initialization objects and passing references to them. This preserves the ordering goal without process-static Python handle ownership. The causal statement about static-wrapper refcounting is in the source title; external pybind documentation linked in a comment was not independently read here. The retained lesson is to include wrapper lifetime and destruction context in binding initialization design, not to suppress assertions as a correctness fix.

## Teardown chain across the preceding unit {#teardown-chain-across-the-preceding-unit}

The preceding unit documents the ownership reversals: interpreter/GIL guards move from server members to globals, into the Python loader, then back to globals. At ordinal 204 the loader manually decrements its object under the GIL but leaves the handle populated, so member destruction decrements again. 308 repairs this with release after dec_ref, mirroring the earlier repair at 115. It is an explicit reported shutdown double-delete fix with an evident source mechanism.

309 identifies a GIL deadlock during server destruction and adds an explicit singleton reset inside the server-thread-stopped hook while holding the GIL. Its comment states that command-map/manager ownership reaches Python objects. It removes scoped global interpreter/release guards, explicitly initializes Python, imports threading, releases/disarms the guard and no longer finalizes through those global destructors. The original host stopped callback runs after disabling plugins and resetting Endstone while the acquire scope remains active. Startup exception handling also changes to throw the caught exception object, a distinct native-entry/exception-slicing concern rather than part of the intended ownership repair.

309 removes the older Windows detach `exit(0)` workaround. Ordinal 137's source explicitly said the cause of Windows not exiting was unknown. The later deadlock diagnosis should be retained as a later diagnosis, without retroactively claiming a captured trace established that every earlier nonexit symptom had the same cause. No host shutdown or process-lifetime test was executed in this review.

357 further changes Python initialization to avoid installing signal handlers. It starts from isolated configuration defaults but then sets isolated to zero and enables environment use. Calling the resulting runtime an isolated environment would be inaccurate. The reliable claim is explicit signal-handler suppression while allowing ambient environment configuration. Host signal ownership, Python object cleanup and interpreter finalization are distinct lifecycle concerns.

## API normalization and known endpoint mismatches {#api-normalization-and-known-endpoint-mismatches}

275 changes optional metadata outputs into empty strings/vectors; 276 updates tests and fixes its inverted author-output guard; 277 restores acceptance of None at Python input while normalizing outputs. This is compatible input adaptation around a simpler native model, rather than a complete reversal. Metadata extraction in 261 switches to summary/author_email; an absent author can still become a one-element list containing None, and distribution lookup still assumes the entry-point name identifies the distribution.

Generated stubs are fully read but not treated as execution evidence. At the endpoint, PluginLoader.disable_plugin still points to enablePlugin, while the manager's disable method is correct. Server.name still points to getVersion. Nullable plugin/command lookups are represented too strongly in some stubs. These concrete binding-pointer mismatches survive extensive docstring work. 347 replaces RTTI lookup with virtual asPluginCommand, satisfying an earlier comment's stated alternative, but loses null safety by dereferencing an absent map result. The historical endpoint records these counterexamples without claiming present-day defects.

Use this evidence for API migrations, factory alias checks, callback reachability, keep-alive graphs and shutdown ordering. Do not reduce it to a preferred smart-pointer type: responsibility repeatedly changes and each representation solves only part of the cross-runtime problem.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-258"></a>
### 258. feat: add 'name' property to Plugin class {#commit-258}

[86f72dba0eb0e7821aea5aa3d392aef0975a2e35](https://github.com/EndstoneMC/endstone/commit/86f72dba0eb0e7821aea5aa3d392aef0975a2e35) · 2024-03-05T05:01:40Z · small-semantic

Author: Vincent. Actual parent: `53797269da12bdbc0e41160ccbe470eab4759ad3`. Full individual diff read; static evidence only.

Adds Plugin::getName forwarding description's bare name and exposes matching Python property/stub. Completes 256 call dependency and centralizes identity access without changing naming policy.

Changed paths: `include/endstone/plugin/plugin.h`, `python/src/endstone/plugin.pyi`, `src/endstone_python/plugin/plugin.cpp`.

<a id="commit-261"></a>
### 261. fix: Python plugin loader now retrieves the correct metadata {#commit-261}

[04284b19d39d2d3bca9557db58bce7fa7fbb23a6](https://github.com/EndstoneMC/endstone/commit/04284b19d39d2d3bca9557db58bce7fa7fbb23a6) · 2024-03-05T13:16:55Z · meaningful

Author: Vincent. Actual parent: `31fcd9ffbee28485d52dfc7aa124bbdf19d91c74`. Full individual diff read; static evidence only.

Corrects installed package metadata keys to summary and author_email instead of description and structured authors. Authors becomes a one-element list even when the key is missing, potentially containing None; distribution association still uses entry-point name. This narrows earlier assumptions but adds no metadata-variation tests.

Changed paths: `python/src/endstone/_internal/plugin_loader.py`.

<a id="commit-267"></a>
### 267. feat: add `getCommand` to plugin interface {#commit-267}

[157f9c003bca423f09d0b2013e242ad7873e310e](https://github.com/EndstoneMC/endstone/commit/157f9c003bca423f09d0b2013e242ad7873e310e) · 2024-03-05T17:03:32Z · meaningful

Author: Vincent. Actual parent: `f9aaa855a98e46d3d0e6910fbeb92457be9201bd`. Full individual diff read; static evidence only.

Adds plugin/server command lookup interfaces and completes executor/PluginCommand vector-argument migration. Concrete lookup is initially nullptr. Plugin helper lowercases but does not verify returned command belongs to this plugin despite documentation saying specific to this plugin; ownership policy remains incomplete.

Changed paths: `include/endstone/command/command_executor.h`, `include/endstone/command/plugin_command.h`, `include/endstone/detail/server.h`, `include/endstone/plugin/plugin.h`, `include/endstone/server.h`, `src/endstone_core/server.cpp`.

<a id="commit-268"></a>
### 268. feat: add interface functions to register plugin commands {#commit-268}

[dc6a8427de85e7b00c59451af9379e91595f8c64](https://github.com/EndstoneMC/endstone/commit/dc6a8427de85e7b00c59451af9379e91595f8c64) · 2024-03-05T17:16:51Z · meaningful

Author: Vincent. Actual parent: `157f9c003bca423f09d0b2013e242ad7873e310e`. Full individual diff read; static evidence only.

Implements server lookup via dynamic_cast of map entries and command registration transferring unique ownership into the shared map. Comment explicitly references a desire to avoid RTTI under Google guidance, but uses it now. Plugin template initially creates CommandType directly where PluginCommand is required, fixed 269. Failure returns nullptr; no registration rollback tests.

Changed paths: `include/endstone/detail/server.h`, `include/endstone/plugin/plugin.h`, `include/endstone/server.h`, `src/endstone_core/server.cpp`.

<a id="commit-269"></a>
### 269. fix: command should be wrapped inside PluginCommand {#commit-269}

[9db2de085d19750738b1e678d7550434525c04e6](https://github.com/EndstoneMC/endstone/commit/9db2de085d19750738b1e678d7550434525c04e6) · 2024-03-05T22:30:51Z · meaningful

Author: Vincent. Actual parent: `dc6a8427de85e7b00c59451af9379e91595f8c64`. Full individual diff read; static evidence only.

Constructs a temporary custom CommandType then wraps copied Command metadata in PluginCommand bound to this owner. Repairs type mismatch but custom execute implementation is not retained: execution goes through owner/executor callback. This is metadata-definition versus executor separation, with the existing registration-pointer copy caveat.

Changed paths: `include/endstone/plugin/plugin.h`.

<a id="commit-270"></a>
### 270. fix: ENDSTONE_PLUGIN macro to include endstone namespace {#commit-270}

[ea95d2f7b78d0ceaec60daa7b6463f4558e11271](https://github.com/EndstoneMC/endstone/commit/ea95d2f7b78d0ceaec60daa7b6463f4558e11271) · 2024-03-05T22:32:58Z · small-semantic

Author: Vincent. Actual parent: `9db2de085d19750738b1e678d7550434525c04e6`. Full individual diff read; static evidence only.

Fully qualifies endstone::Plugin in exported factory macro for both platforms, repairing 187 namespace migration for downstream users without using directives. Factory C linkage still does not erase C++ ABI constraints.

Changed paths: `include/endstone/plugin/plugin.h`.

<a id="commit-275"></a>
### 275. refactor: remove the use of optional for PluginDescription {#commit-275}

[9af6251702e3c3413e6ba0b3779f7fff3905febc](https://github.com/EndstoneMC/endstone/commit/9af6251702e3c3413e6ba0b3779f7fff3905febc) · 2024-03-06T11:25:08Z · meaningful

Author: Vincent. Actual parent: `53de1d91ffcd2dcfca1789c63c8ab74e9b69d824`. Full individual diff read; static evidence only.

Simplifies PluginDescription C++ fields/getters from optional values to empty strings/vectors. Binding factory initially changes to nonoptional arguments, but defaults still None until 276. Version output mistakenly tests authors.empty() positively, suppressing actual authors;276 repairs. This is a cross-language contract migration, not just type cleanup.

Changed paths: `include/endstone/plugin/plugin_description.h`, `src/endstone_core/command/defaults/version_command.cpp`, `src/endstone_python/plugin/plugin_description.cpp`.

<a id="commit-276"></a>
### 276. test(python): fix tests {#commit-276}

[3b9610ec752e1f4dc1478656fe09da5eae45253e](https://github.com/EndstoneMC/endstone/commit/3b9610ec752e1f4dc1478656fe09da5eae45253e) · 2024-03-06T11:54:20Z · meaningful

Author: Vincent. Actual parent: `9af6251702e3c3413e6ba0b3779f7fff3905febc`. Full individual diff read; static evidence only.

Updates Python description tests to falsy-empty rather than None semantics and binding defaults to empty values. Repairs 275 inverted authors guard. Also changes author joining based on total size rather than position, yielding comma for two names and and at every separator otherwise; no output tests establish intent. Title understates production changes.

Changed paths: `python/tests/test_plugin_description.py`, `src/endstone_core/command/defaults/version_command.cpp`, `src/endstone_python/plugin/plugin_description.cpp`.

<a id="commit-277"></a>
### 277. feat: update python stubs {#commit-277}

[8c9f7e9dfe2fa8e9a8df481541e38ffa226e73e0](https://github.com/EndstoneMC/endstone/commit/8c9f7e9dfe2fa8e9a8df481541e38ffa226e73e0) · 2024-03-06T12:04:59Z · meaningful

Author: Vincent. Actual parent: `3b9610ec752e1f4dc1478656fe09da5eae45253e`. Full individual diff read; static evidence only.

Keeps nonoptional return stubs but restores Python constructor acceptance of None through optional adapter arguments normalized to empty C++ values. This explicitly separates permissive input compatibility from normalized output representation; differs from simply reverting 275.

Changed paths: `python/src/endstone/plugin.pyi`, `src/endstone_python/plugin/plugin_description.cpp`.

<a id="commit-280"></a>
### 280. feat: add getName to Server interface {#commit-280}

[f7cf1388333ad371395e21c156c9b8c4e174a845](https://github.com/EndstoneMC/endstone/commit/f7cf1388333ad371395e21c156c9b8c4e174a845) · 2024-03-06T12:47:46Z · meaningful

Author: Vincent. Actual parent: `79b7386f7a8c48524247cdce21d2e662a718d3e6`. Full individual diff read; static evidence only.

Adds server implementation name, changes getVersion from borrowed string_view to owned string and updates synthetic implementation. Startup/version output now reports implementation plus Minecraft version with colors; logger name becomes Server and native log-area label is renamed. Public virtual API/return ABI changes require consumer rebuilds; Python exposure follows 286.

Changed paths: `include/bedrock/bedrock_log.h`, `include/endstone/detail/server.h`, `include/endstone/server.h`, `src/endstone_core/command/defaults/version_command.cpp`, `src/endstone_core/server.cpp`, `src/endstone_runtime/bedrock/server_instance.cpp`, `test_package/src/test_server.cpp`.

<a id="commit-282"></a>
### 282. refactor: move class `PluginCommand` to `plugin.h` {#commit-282}

[7d942e1a437662f6eba25d7a7487ad03eb51031d](https://github.com/EndstoneMC/endstone/commit/7d942e1a437662f6eba25d7a7487ad03eb51031d) · 2024-03-06T14:00:27Z · meaningful

Author: Vincent. Actual parent: `014cfb9fc5ee8d60b7a44d510e9338372cc1dd60`. Full individual diff read; static evidence only.

Relocates PluginCommand definition unchanged into plugin.h after Plugin, reducing the mutual definition problem. It accidentally includes the now-deleted header and leaves external includes until 283. Existing callback/borrowed-owner/shared-executor semantics are preserved; relocation is not new ownership design.

Changed paths: `include/endstone/command/plugin_command.h`, `include/endstone/plugin/plugin.h`.

<a id="commit-283"></a>
### 283. fix: remove invalid includes {#commit-283}

[fa159c8dd32f325ab6109637ec7d00704d9ab3e7](https://github.com/EndstoneMC/endstone/commit/fa159c8dd32f325ab6109637ec7d00704d9ab3e7) · 2024-03-06T14:02:30Z · mechanical

Author: Vincent. Actual parent: `7d942e1a437662f6eba25d7a7487ad03eb51031d`. Full individual diff read; static evidence only.

Removes stale deleted PluginCommand header includes and uses plugin.h in core. Completes 282 relocation across production and package fixture.

Changed paths: `include/endstone/plugin/plugin.h`, `src/endstone_core/server.cpp`, `test_package/src/test_server.cpp`.

<a id="commit-286"></a>
### 286. refactor: python bindings {#commit-286}

[9cf94b27af9b1c0383ecb8cc6466ab69d20d56e2](https://github.com/EndstoneMC/endstone/commit/9cf94b27af9b1c0383ecb8cc6466ab69d20d56e2) · 2024-03-06T15:45:32Z · meaningful

Author: Vincent. Actual parent: `783d1a8cb9eec8a49b0a97d8bf1ff8176ddff210`. Full individual diff read; static evidence only.

Consolidates plugin binding translation units and changes module init phases. Adds templated py_class helper caching a static py::class_ so forward creation and later method definition share one type wrapper. This solves ordering structurally but gives Python refcounts static C++ lifetime, later diagnosed 306. Server name property is mistakenly bound to getVersion and loader disable misbinding persists. Full 623-line patch read including removed/recombined code; do not count moved implementations as newly invented.

Changed paths: `include/endstone/detail/python.h`, `src/endstone_python/color_format.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/forward.h`, `src/endstone_python/logger.cpp`, `src/endstone_python/plugin.cpp`, `src/endstone_python/plugin/plugin.cpp`, `src/endstone_python/plugin/plugin_description.cpp`, `src/endstone_python/plugin/plugin_loader.cpp`, `src/endstone_python/plugin/plugin_manager.cpp`, `src/endstone_python/server.cpp`, `src/endstone_python/util.cpp`.

<a id="commit-287"></a>
### 287. feat: replace py::class_ with py_class helper function {#commit-287}

[9c0e1c579dd9596fd5614367c546e416e3b1258b](https://github.com/EndstoneMC/endstone/commit/9c0e1c579dd9596fd5614367c546e416e3b1258b) · 2024-03-06T15:56:53Z · meaningful

Author: Vincent. Actual parent: `9cf94b27af9b1c0383ecb8cc6466ab69d20d56e2`. Full individual diff read; static evidence only.

Applies cached py_class broadly and moves helper back to detail header, adding forwarded Extra constructor arguments. Module util init moves last. Broadens the same static-wrapper lifetime assumption;288 immediately removes Extra support, showing a short-lived generalization.

Changed paths: `include/endstone/detail/python.h`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/forward.h`, `src/endstone_python/logger.cpp`, `src/endstone_python/plugin.cpp`, `src/endstone_python/server.cpp`, `src/endstone_python/util.cpp`.

<a id="commit-288"></a>
### 288. docs: add documents for endstone headers {#commit-288}

[64206db0488f503d8a475bfa6bb39560d56b4d2c](https://github.com/EndstoneMC/endstone/commit/64206db0488f503d8a475bfa6bb39560d56b4d2c) · 2024-03-06T16:40:40Z · meaningful

Author: Vincent. Actual parent: `9c0e1c579dd9596fd5614367c546e416e3b1258b`. Full individual diff read; static evidence only.

Adds API documentation for logger, plugin metadata and manager idempotence/case sensitivity, but also removes PluginLoader::getServer, exposes server_ to subclasses and reverts py_class Extra support. Consumers still call getServer until 289. Some docstrings retain null wording although 275 normalized empty values; docs express intended contracts, not independent implementation proof.

Changed paths: `include/endstone/detail/python.h`, `include/endstone/logger.h`, `include/endstone/plugin/plugin.h`, `include/endstone/plugin/plugin_description.h`, `include/endstone/plugin/plugin_loader.h`, `include/endstone/plugin/plugin_manager.h`, `include/endstone/util/color_format.h`.

<a id="commit-289"></a>
### 289. docs: add documentations for python bindings {#commit-289}

[7902769ad1604877dd3407291c133d53b07c1ab0](https://github.com/EndstoneMC/endstone/commit/7902769ad1604877dd3407291c133d53b07c1ab0) · 2024-03-06T16:41:07Z · meaningful

Author: Vincent. Actual parent: `64206db0488f503d8a475bfa6bb39560d56b4d2c`. Full individual diff read; static evidence only.

Adds binding docstrings, removes handwritten facade stubs ahead of generated replacement 290, and updates loader consumers after getServer removal. Replaces optimized-away assert type check with explicit TypeError, but misses f-string interpolation in the new error. Loader disable documentation now says disables while pointer still targets enable; server name likewise still targets version. Functional changes hide under documentation title.

Changed paths: `python/src/endstone/_internal/plugin_loader.py`, `python/src/endstone/logger.pyi`, `python/src/endstone/plugin.py`, `python/src/endstone/plugin.pyi`, `python/src/endstone/server.pyi`, `python/src/endstone/util.pyi`, `src/endstone_core/plugin/cpp_plugin_loader.cpp`, `src/endstone_python/logger.cpp`, `src/endstone_python/plugin.cpp`, `src/endstone_python/server.cpp`.

<a id="commit-290"></a>
### 290. docs: add stubs for python bindings generated from pybind11-stubgen {#commit-290}

[b19f531d0ab2b9dad9c0d91db27ba72f97dcff73](https://github.com/EndstoneMC/endstone/commit/b19f531d0ab2b9dad9c0d91db27ba72f97dcff73) · 2024-03-06T16:41:32Z · generated-verified

Author: Vincent. Actual parent: `7902769ad1604877dd3407291c133d53b07c1ab0`. Full individual diff read; static evidence only.

Adds 288-line stubgen output for seven extension classes. Entire generated file read and compared conceptually to bindings: includes enum machinery/docstrings, normalized metadata output and optional inputs. get_plugin is typed nonnullable despite nullable native return; generated method names cannot reveal loader-disable/server-name pointer mistakes. Generated evidence supports tooling surface, not runtime correctness or original algorithm credit.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`.

<a id="commit-291"></a>
### 291. feat: add python binding for class `CommandSender` {#commit-291}

[cb6af2ff0803f1029acc9e3d3018df342bc04c82](https://github.com/EndstoneMC/endstone/commit/cb6af2ff0803f1029acc9e3d3018df342bc04c82) · 2024-03-06T17:41:53Z · meaningful

Author: Vincent. Actual parent: `b19f531d0ab2b9dad9c0d91db27ba72f97dcff73`. Full individual diff read; static evidence only.

Binds CommandSender send_message/name/borrowed server, adds virtual destructor to public sender interface and initializes command bindings first using forward-created Server class. Changes logger Python keyword from msg to message and regenerates corresponding stubs; this keyword rename can affect callers. Error-message method not yet exposed. No callback integration tests.

Changed paths: `include/endstone/command/command_sender.h`, `include/endstone/plugin/plugin.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/command.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/logger.cpp`, `src/endstone_python/plugin.cpp`.

<a id="commit-292"></a>
### 292. feat: add python binding for class `CommandExecutor` {#commit-292}

[65b9a227f197b727e1fcd1d1706704a55c34795b](https://github.com/EndstoneMC/endstone/commit/65b9a227f197b727e1fcd1d1706704a55c34795b) · 2024-03-06T17:51:01Z · meaningful

Author: Vincent. Actual parent: `cb6af2ff0803f1029acc9e3d3018df342bc04c82`. Full individual diff read; static evidence only.

Adds CommandExecutor trampoline and Python facade with on_command callback, but trampoline macro initially searches onCommand rather than snake_case, repaired 297. Stub contains unresolved command type until 294. Corrects older executor success docstring. Binding surface exists before all dispatch dependencies are complete.

Changed paths: `include/endstone/command/command_executor.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/command.py`, `src/endstone_python/command.cpp`.

<a id="commit-293"></a>
### 293. feat: add `CommandExecutor` as the base class of `Plugin` in the binding code {#commit-293}

[edb53e6cf66f6682fc9daf69e1fedef74e782679](https://github.com/EndstoneMC/endstone/commit/edb53e6cf66f6682fc9daf69e1fedef74e782679) · 2024-03-06T17:54:50Z · meaningful

Author: Vincent. Actual parent: `65b9a227f197b727e1fcd1d1706704a55c34795b`. Full individual diff read; static evidence only.

Declares CommandExecutor base in Plugin binding and stub, aligning Python inheritance with C++. This alone does not install an override in PyPlugin;305 later repairs that missing callback path.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/plugin.cpp`.

<a id="commit-294"></a>
### 294. feat: add python binding for class `Command` {#commit-294}

[8f87f0dbfee3bf8ff21cbbb1131cc357dc25e2f6](https://github.com/EndstoneMC/endstone/commit/8f87f0dbfee3bf8ff21cbbb1131cc357dc25e2f6) · 2024-03-06T18:14:42Z · meaningful

Author: Vincent. Actual parent: `edb53e6cf66f6682fc9daf69e1fedef74e782679`. Full individual diff read; static evidence only.

Binds constructible Command metadata, mutable properties, execute and registration-state helpers, accepting None as normalized empty inputs. No Command trampoline is provided here, so exposing execute does not establish Python subclass virtual dispatch. register_to/unregister_from mention unbound CommandMap in generated stubs;295 removes those methods rather than exposing the map.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/command.cpp`.

<a id="commit-295"></a>
### 295. refactor: remove python bindings related to CommandMap {#commit-295}

[8b3b757575e09a9fa429018a6d9320e3bdeaaaf0](https://github.com/EndstoneMC/endstone/commit/8b3b757575e09a9fa429018a6d9320e3bdeaaaf0) · 2024-03-06T18:21:01Z · meaningful

Author: Vincent. Actual parent: `8f87f0dbfee3bf8ff21cbbb1131cc357dc25e2f6`. Full individual diff read; static evidence only.

Removes Python methods requiring unavailable CommandMap and switches Command to cached py_class helper. Narrows Python API to meaningful supported boundary; C++ registration methods remain.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/command.cpp`.

<a id="commit-296"></a>
### 296. feat: update imports in endstone.command {#commit-296}

[15c1ad1c4f1058909416354693a7c0f56e71f169](https://github.com/EndstoneMC/endstone/commit/15c1ad1c4f1058909416354693a7c0f56e71f169) · 2024-03-06T18:22:23Z · small-semantic

Author: Vincent. Actual parent: `8b3b757575e09a9fa429018a6d9320e3bdeaaaf0`. Full individual diff read; static evidence only.

Re-exports Command from public endstone.command facade. Completes discoverability for 294 binding without changing native behavior.

Changed paths: `python/src/endstone/command.py`.

<a id="commit-297"></a>
### 297. feat: add python binding for class `PluginCommand` {#commit-297}

[c2476486f293bb9a4242234e821a9a96cce6a520](https://github.com/EndstoneMC/endstone/commit/c2476486f293bb9a4242234e821a9a96cce6a520) · 2024-03-06T23:40:58Z · meaningful

Author: Vincent. Actual parent: `15c1ad1c4f1058909416354693a7c0f56e71f169`. Full individual diff read; static evidence only.

Adds PluginCommand binding, owner/executor properties and Plugin.get_command, and explicitly maps CommandExecutor trampoline to on_command. Getter reference/lifetime policies and owner retention are not comprehensively solved;299 adds a dedicated retained executor strategy. Stubs again do not express nullable get_command result.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/command.cpp`, `src/endstone_python/plugin.cpp`.

<a id="commit-298"></a>
### 298. feat: add bindings for plugin registration {#commit-298}

[35b01988266720b6e6acbebcc161d2ab4d957f21](https://github.com/EndstoneMC/endstone/commit/35b01988266720b6e6acbebcc161d2ab4d957f21) · 2024-03-06T23:49:19Z · meaningful

Author: Vincent. Actual parent: `c2476486f293bb9a4242234e821a9a96cce6a520`. Full individual diff read; static evidence only.

Changes server plugin-command input from unique_ptr to shared_ptr and aligns Command/PluginCommand pybind holders, enabling Python registration without transferring exclusive native ownership. Adds server command lookup/registration bindings and stubs. Shared native ownership still does not itself keep Python override wrapper alive, motivating 299/301. Fixture signature updated 300.

Changed paths: `include/endstone/detail/server.h`, `include/endstone/server.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_core/server.cpp`, `src/endstone_python/command.cpp`, `src/endstone_python/plugin.cpp`, `src/endstone_python/server.cpp`.

<a id="commit-299"></a>
### 299. feat: add trampoline class for `PluginCommand` in order to keep executor alive {#commit-299}

[e65a25b17c96424de8df8f07aa4aef009e46a3ba](https://github.com/EndstoneMC/endstone/commit/e65a25b17c96424de8df8f07aa4aef009e46a3ba) · 2024-03-07T00:32:49Z · meaningful

Author: Vincent. Actual parent: `35b01988266720b6e6acbebcc161d2ab4d957f21`. Full individual diff read; static evidence only.

Makes executor access virtual and adds PyPluginCommand trampoline plus Python subclass storing executor to keep its Python wrapper alive. Plugin retains one registered wrapper and constructs commands from metadata types;301 expands this to many. Changes binding initialization order to satisfy dependencies. This is explicit cross-runtime keep-alive design, distinct from native shared_ptr ownership. Owner initially serves as retained executor, creating potential reference cycles considered by 303 fallback change.

Changed paths: `include/endstone/plugin/plugin.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/plugin.py`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/plugin.cpp`, `src/endstone_python/server.cpp`.

<a id="commit-301"></a>
### 301. fix: allow plugin to manage the lifecycle of multiple commands {#commit-301}

[3fda97f670e704dcde16862fc20d07ea0adc62c6](https://github.com/EndstoneMC/endstone/commit/3fda97f670e704dcde16862fc20d07ea0adc62c6) · 2024-03-07T00:54:30Z · meaningful

Author: Vincent. Actual parent: `5c89e7266bd3f8388621b5be8d1df8ba8b19619a`. Full individual diff read; static evidence only.

Replaces one retained Python command slot with a list, so registering a later command no longer drops the earlier Python wrapper. Appends before registration result, retaining even failed requests. This explicitly fixes ownership cardinality rather than changing native map ownership.

Changed paths: `python/src/endstone/plugin.py`.

<a id="commit-302"></a>
### 302. fix: pass arguments by reference for override functions {#commit-302}

[8376e0bed07c83d41948f0a5b43fc4bceec063a4](https://github.com/EndstoneMC/endstone/commit/8376e0bed07c83d41948f0a5b43fc4bceec063a4) · 2024-03-07T01:03:54Z · meaningful

Author: Vincent. Actual parent: `3fda97f670e704dcde16862fc20d07ea0adc62c6`. Full individual diff read; static evidence only.

Passes sender, command and args into Python override through std::ref wrappers to preserve reference conversion rather than unintended copies. Does not itself extend borrowed native lifetimes beyond the callback; no retention/mutation tests supplied.

Changed paths: `src/endstone_python/command.cpp`.

<a id="commit-303"></a>
### 303. feat: use shared_ptr as the holder of CommandExecutor {#commit-303}

[0f26a54e08bdb8da80aae78660bd6499807f8776](https://github.com/EndstoneMC/endstone/commit/0f26a54e08bdb8da80aae78660bd6499807f8776) · 2024-03-07T10:27:38Z · meaningful

Author: Vincent. Actual parent: `8376e0bed07c83d41948f0a5b43fc4bceec063a4`. Full individual diff read; static evidence only.

Uses shared_ptr holders for CommandExecutor and derived Plugin, aligning holder compatibility. Python PluginCommand starts with no explicit executor and falls back to plugin property, avoiding the initially stored owner executor. This retains custom executors while separating default-owner lookup; cross-runtime cycles/lifetime still need shutdown tests.

Changed paths: `python/src/endstone/plugin.py`, `src/endstone_python/command.cpp`, `src/endstone_python/plugin.cpp`.

<a id="commit-304"></a>
### 304. fix: temporarily disable GIL_CHECK to avoid crash on shutdown {#commit-304}

[a6bcee8f03ca4410d50b87f88e86d538feadf508](https://github.com/EndstoneMC/endstone/commit/a6bcee8f03ca4410d50b87f88e86d538feadf508) · 2024-03-07T11:39:33Z · meaningful

Author: Vincent. Actual parent: `0f26a54e08bdb8da80aae78660bd6499807f8776`. Full individual diff read; static evidence only.

Temporarily disables pybind GIL-held INCREF/DECREF assertions globally to avoid reported shutdown crash, repeating an earlier workaround pattern. Suppressing an assertion is not proof refcount operations are safe;306 removes the underlying cached-wrapper strategy and reenables the checks.

Changed paths: `CMakeLists.txt`.

<a id="commit-305"></a>
### 305. fix: python plugin's on_command not getting called {#commit-305}

[96f657aad6806e5addca3d886531cd99364c4fd7](https://github.com/EndstoneMC/endstone/commit/96f657aad6806e5addca3d886531cd99364c4fd7) · 2024-03-07T11:39:56Z · meaningful

Author: Vincent. Actual parent: `a6bcee8f03ca4410d50b87f88e86d538feadf508`. Full individual diff read; static evidence only.

Adds explicit onCommand trampoline override to PyPlugin, fixing the reported Python plugin callback not being called despite 293 Python inheritance. Improves exception logs with command/plugin context and separate exception text. Distinguishes Python type inheritance from C++ virtual dispatch; no captured run or regression test accompanies the fix.

Changed paths: `include/endstone/plugin/plugin.h`, `src/endstone_python/command.cpp`, `src/endstone_python/plugin.cpp`.

<a id="commit-306"></a>
### 306. fix: dec_ref being called without GIL due to singletons of py::class_ {#commit-306}

[733f09aa3bfc03dfe3bec0405c8084b2c8d9599b](https://github.com/EndstoneMC/endstone/commit/733f09aa3bfc03dfe3bec0405c8084b2c8d9599b) · 2024-03-07T14:32:57Z · meaningful

Author: Vincent. Actual parent: `96f657aad6806e5addca3d886531cd99364c4fd7`. Full individual diff read; static evidence only.

Commit explicitly attributes dec_ref-without-GIL to static py::class_ singletons. Removes cached helper/forward creation, uses ordinary local py::class_ wrappers and reenables GIL assertions. This is an observed reversal of 286/287, solving Python-reference teardown ownership instead of permanently suppressing checks. No captured shutdown test proves all lifetime problems resolved;308/309 address separate layers.

Changed paths: `CMakeLists.txt`, `include/endstone/detail/python.h`, `src/endstone_python/command.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/logger.cpp`, `src/endstone_python/plugin.cpp`, `src/endstone_python/server.cpp`, `src/endstone_python/util.cpp`.

<a id="commit-307"></a>
### 307. docs: add docstring for plugin.register_command {#commit-307}

[aae8bde0c7dc8236f969d4174119b9618cf57f7e](https://github.com/EndstoneMC/endstone/commit/aae8bde0c7dc8236f969d4174119b9618cf57f7e) · 2024-03-07T16:30:50Z · meaningful

Author: Vincent. Actual parent: `733f09aa3bfc03dfe3bec0405c8084b2c8d9599b`. Full individual diff read; static evidence only.

Documentation title hides replacement forward-declaration design: create Server/PluginCommand/PluginLoader py::class_ wrappers as local module-init objects and pass/reuse references, with a pybind documentation link explaining docstring type names. Retains forward type availability without static wrappers. Adds plugin registration docstring; external documentation itself not read in this unit.

Changed paths: `python/src/endstone/plugin.py`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/plugin.cpp`, `src/endstone_python/server.cpp`.

<a id="commit-308"></a>
### 308. fix: crash on shutdown due to double delete {#commit-308}

[747e3372f2b68aeaee2a4d55f4371407ade68564](https://github.com/EndstoneMC/endstone/commit/747e3372f2b68aeaee2a4d55f4371407ade68564) · 2024-03-07T23:36:19Z · meaningful

Author: Vincent. Actual parent: `aae8bde0c7dc8236f969d4174119b9618cf57f7e`. Full individual diff read; static evidence only.

Explicitly fixes reported shutdown double delete by release() after manually dec_ref() under acquired GIL. Clears handle so ordinary py::object member destruction does not decrement again. Repairs 204 regression using the same mechanism as prior 115; local lifetime repair is distinct from global interpreter/server teardown handled 309.

Changed paths: `src/endstone_runtime/plugin/python_plugin_loader.cpp`.

<a id="commit-309"></a>
### 309. fix: GIL deadlock during the destruction of EndstoneServer {#commit-309}

[26d35af5f66c6e2cf12d0a5fcd0c8a4ab463af74](https://github.com/EndstoneMC/endstone/commit/26d35af5f66c6e2cf12d0a5fcd0c8a4ab463af74) · 2024-03-08T11:54:59Z · meaningful

Author: Vincent. Actual parent: `747e3372f2b68aeaee2a4d55f4371407ade68564`. Full individual diff read; static evidence only.

Title identifies GIL deadlock during EndstoneServer destruction. Adds Singleton::reset and acquires GIL in host stopped hook before disabling plugins and destroying server, with explicit comment that map/manager hold shared_ptrs to Python objects. Replaces global interpreter/release guards with explicit initialize_interpreter, imports threading citing pybind issue 2197, releases/disarms GIL guard and no longer finalizes through scoped globals. Removes Windows detach exit workaround. Startup catch now throws e rather than terminate, risking slicing/exception escape at native entry. The source establishes chosen shutdown ownership and attributed diagnosis, not a captured deadlock trace or proof that every earlier unexplained symptom shares one cause.

Changed paths: `include/endstone/detail/singleton.h`, `src/endstone_runtime/bedrock/server_instance.cpp`, `src/endstone_runtime/main.cpp`.

<a id="commit-312"></a>
### 312. refactor: remove noexcept {#commit-312}

[1d60496efdccd17f08a3e6f8aeab1f0cffd7f26e](https://github.com/EndstoneMC/endstone/commit/1d60496efdccd17f08a3e6f8aeab1f0cffd7f26e) · 2024-03-08T16:59:48Z · meaningful

Author: Vincent. Actual parent: `1ea6e9d29f343ca40a90b078733ed543bcec4b14`. Full individual diff read; static evidence only.

Removes remaining noexcept from command construction, allocating metadata setters, registration-state helpers and concrete map accessor. This avoids forced termination for ordinary allocation exceptions in setters but also relaxes trivially nonthrowing helpers. It continues 192 exception-policy revision rather than proving a universal anti-noexcept preference; no failure-injection test.

Changed paths: `include/endstone/command/command.h`, `include/endstone/command/command_executor.h`, `include/endstone/detail/command/command_adapter.h`, `include/endstone/detail/server.h`, `src/endstone_core/server.cpp`.

<a id="commit-313"></a>
### 313. refactor: registerCommand function in Plugin class {#commit-313}

[96416061e8770d0ae0056194a57d273a0bb6bd48](https://github.com/EndstoneMC/endstone/commit/96416061e8770d0ae0056194a57d273a0bb6bd48) · 2024-03-08T17:04:01Z · meaningful

Author: Vincent. Actual parent: `1d60496efdccd17f08a3e6f8aeab1f0cffd7f26e`. Full individual diff read; static evidence only.

Changes plugin command registration from templated metadata subclass construction to direct name/description/usages/aliases values and moves aliases into Command. Makes API simpler for data-defined commands; it still temporarily constructs/copies base Command until 314.

Changed paths: `include/endstone/command/command.h`, `include/endstone/plugin/plugin.h`.

<a id="commit-314"></a>
### 314. refactor: update python interface {#commit-314}

[8bf54893ad6dc53d9db9ca79593f739a047c7417](https://github.com/EndstoneMC/endstone/commit/8bf54893ad6dc53d9db9ca79593f739a047c7417) · 2024-03-08T17:40:44Z · meaningful

Author: Vincent. Actual parent: `96416061e8770d0ae0056194a57d273a0bb6bd48`. Full individual diff read; static evidence only.

Makes Command constructor protected, constructs PluginCommand directly from owner plus metadata and aligns Python registration/facade/stubs. Removes public Python Command constructor and metadata-type registration requirement, avoiding copying an existing registration pointer. Factory initially returns base PluginCommand, potentially bypassing trampoline construction;315 explicitly returns alias. Python signature union annotations introduce 3.9 import incompatibility fixed 316.

Changed paths: `include/endstone/command/command.h`, `include/endstone/detail/command/command_view.h`, `include/endstone/plugin/plugin.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/plugin.py`, `src/endstone_python/command.cpp`, `src/endstone_python/plugin.cpp`.

<a id="commit-315"></a>
### 315. fix: always return an alias for PluginCommand trampoline class {#commit-315}

[97db96fd8a8233ae62bb716bef348d277418bc42](https://github.com/EndstoneMC/endstone/commit/97db96fd8a8233ae62bb716bef348d277418bc42) · 2024-03-08T17:55:18Z · meaningful

Author: Vincent. Actual parent: `8bf54893ad6dc53d9db9ca79593f739a047c7417`. Full individual diff read; static evidence only.

Changes Python PluginCommand factory return to PyPluginCommand alias, ensuring executor virtual overrides exist even with factory construction. Concrete C++ object type, Python subclass and binding alias must agree; no ownership fix can compensate for a missing trampoline.

Changed paths: `src/endstone_python/plugin.cpp`.

<a id="commit-316"></a>
### 316. fix: unsupported operand type(s) for |: 'type' and 'NoneType' on Python 3.9 {#commit-316}

[b1c188d2c2903d9464dec2760299c28a31deec46](https://github.com/EndstoneMC/endstone/commit/b1c188d2c2903d9464dec2760299c28a31deec46) · 2024-03-08T18:01:52Z · meaningful

Author: Vincent. Actual parent: `97db96fd8a8233ae62bb716bef348d277418bc42`. Full individual diff read; static evidence only.

Replaces evaluated function annotations using type|None with Optional/list annotations compatible with supported Python 3.9. Local variable annotations are left, and generated stub uses future annotations; distinguish runtime module import from stub syntax. Title supplies concrete reported TypeError, but no run log was read.

Changed paths: `python/src/endstone/plugin.py`.

<a id="commit-347"></a>
### 347. feat: finish todo, clean up code {#commit-347}

[1f7a48003f5d36bab1e81f61b30c62499b881e9d](https://github.com/EndstoneMC/endstone/commit/1f7a48003f5d36bab1e81f61b30c62499b881e9d) · 2024-03-12T16:46:31Z · meaningful

Author: Vincent. Actual parent: `24ed96cb1de0d7439a010f93888655a8479cf16b`. Full individual diff read; static evidence only.

Replaces dynamic_cast in server plugin-command lookup with virtual Command::asPluginCommand returning null by default and this for PluginCommand, fulfilling 268 explicit TODO to avoid RTTI. New call dereferences getCommand without checking null, unlike dynamic_cast on a null pointer. This is a meaningful design alternative with a new absent-command counterexample, not pure cleanup. Other changes are formatting or equivalent null-operator branch order.

Changed paths: `include/endstone/command/command.h`, `include/endstone/detail/command/command_map.h`, `include/endstone/permissions/permissible.h`, `include/endstone/plugin/plugin.h`, `src/endstone_core/permissions/permissible_base.cpp`, `src/endstone_core/server.cpp`.

<a id="commit-353"></a>
### 353. refactor: remove unused function {#commit-353}

[1115d40660719b59682e56035be304a8f583ab31](https://github.com/EndstoneMC/endstone/commit/1115d40660719b59682e56035be304a8f583ab31) · 2024-03-13T11:17:39Z · mechanical

Author: Vincent. Actual parent: `84e5357d992ac29abbaa2e62bf16f013217caf3a`. Full individual diff read; static evidence only.

Removes unused private EndstoneServer::enablePlugin forwarding helper. Bulk enablePlugins and manager enablePlugin remain. This does not remove the unrelated stale customParseRule declaration, which remains at 360.

Changed paths: `include/endstone/detail/server.h`, `src/endstone_core/server.cpp`.

<a id="commit-357"></a>
### 357. fix: use isolated python env to avoid installing signal handlers {#commit-357}

[1255f6d6cb5e1c8e788b4628e2c2808872a94d51](https://github.com/EndstoneMC/endstone/commit/1255f6d6cb5e1c8e788b4628e2c2808872a94d51) · 2024-03-13T15:45:56Z · meaningful

Author: Vincent. Actual parent: `071b788b51610c9ac0ae1adb2259c05b108feb36`. Full individual diff read; static evidence only.

Title/comment identify avoiding Python-installed signal handlers. Initializes PyConfig with isolated defaults but explicitly resets isolated=0 and use_environment=1, while install_signal_handlers=0. The resulting configuration is therefore not a promise of isolation from ambient environment. Preserves threading import and disarmed release from 309. Correct lesson is coexistence with host signal handling plus deliberate configuration overrides; no runtime signal test or external docs content read.

Changed paths: `src/endstone_runtime/main.cpp`.
