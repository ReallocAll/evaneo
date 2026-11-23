<!-- retrieval: {"source_ids":["public:commit:0dbae89c9032d7c7005c641d1f116d78db74ed81","public:commit:106d7e0571e115b740962dcb9c5c62c5ae6ecf37","public:commit:3136014571de24e463b43b5fa78453762ee64631","public:commit:31f98e4b004a8a848d2d1160eb3f0582b7fd3a69","public:commit:323b64b3ee3e0d77fa72a4983c1579c22ff9c76c","public:commit:400eaccf0ffc079228351066883f98a06b38c8a8","public:commit:42f0cb06e8d5e3dbea24127bbb1c03917e27290d","public:commit:43b5049758388673829b298f07508b99e35ad464","public:commit:479096bdca2434af4aa3c87e06a592aa127424a1","public:commit:4e4a52708cc3b162912d7b73dea33da41b60f541","public:commit:5059517425a1a74659c6f2c678ab32a62e463de9","public:commit:5170e0472da54f23bdd1110cebe3279547d9fef0","public:commit:5723474abd818fecd59636423e6362e947166730","public:commit:583683109140be2341de3b4355871e4a3455bfa6","public:commit:5a7f4a2b4136fb490b481fdcee065a37768917f5","public:commit:5ef723581b8202f4d81d96852b6af4d8dfda8b97","public:commit:65d51747dc1dd3a91769c32baa94e6dd4fb49a2f","public:commit:66a44d03a74dc0b5396a25e28a9463e1b071ae95","public:commit:69ca452daa37aad38629397e05e6f09a378895dd","public:commit:6bc4e9301289d4ed856a387444a9a79e0b3dcc4b","public:commit:820ff4a3a69d50c3d858e1d1867873a251908b6a","public:commit:84b664a602510b74587ea0edf851644ca2d80a32","public:commit:866d7ce6d19d3eecea4af027afe03aebed3188db","public:commit:9cea74aac4aff5748d58fa2c43b10dfcc4c069ac","public:commit:9f4a178936ebac9546e8aee7a57301b354e87dc5","public:commit:a4bd58fc0ece34ef1f4a368c53a0c335aa5f68b3","public:commit:a55d7bda2bd9df29fd21f0b0988d510a9cbb7938","public:commit:a880d65b53a0a778351cc2a0e87f2ca992a76cb7","public:commit:a8c971e280fc5dc2112b9eb1e7ff1959ae0f677d","public:commit:acd2ed78b482adaaa0abb5629d8f5cd22c184702","public:commit:aec7153c59de5fb9830e292f5f5673ff99d01585","public:commit:b59ed710d89fbdee5d0c02437d204a91a34babeb","public:commit:b86c8f2d8c3579bdfe35f5c32f3f9867e945b60e","public:commit:c3b5c8bd2854b07be5b604ec13cb2d7e8ecbfb44","public:commit:c70ca2c5c6f4c5c8a2ffc3c9a553ebfdc9bd18ea","public:commit:d4faa50098c38757b02e91f2f256c3afbc38dd28","public:commit:d7bad11ce16ab26664c8eb28804253835ba0b8e4","public:commit:d956e7d8fc5ab707d7fcfaa07f7ee304c9c70fae","public:commit:e21cae6c40e2043ac2b087b1f461f19d31dadcfa","public:commit:e3b9a28b785b096657277c402f9a1db5f98cc5ca","public:commit:ea9fd53270e8150ca17afdda92d6b5aac74d4ce6","public:commit:eaa528f7d0bb3a3655e34fd3a10358d85be7a53d","public:commit:edf705795c49a85db27fd74b4fc22accd9ee35ac","public:commit:f0e2bfe13e126c7a868967b249fce3bcacee837a","public:commit:f89f1ba097ec43bc13a6e8c3ea01583c17f0b951","public:commit:fc6cc150f05c65e73e09dd0dac841e86cb73e07f"],"source_type":"public","date":"2024-03-13..2024-03-21","topics":["lifetime","concurrency","ffi","testing","build","api","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Declarative plugin metadata, compatibility and Python ownership {#declarative-plugin-metadata-compatibility-and-python-ownership}

## Result: construction data and live plugin state separate {#result-construction-data-and-live-plugin-state-separate}

From 13–21 March 2024, Endstone replaces much of its imperative plugin registration surface with declarative command, permission and lifecycle metadata. The endpoint has a C++ builder producing a value PluginDescription, a Python class-attribute loader producing the same native description shape, and server-side phase-aware activation. These pieces arrive through several intermediate incompatible states. The full chain matters: a final header alone conceals the attempted static pointer, friendship, public-pointer and generated-subclass designs.

Every ordinal below is a verified actual-parent descendant, not merely a timestamp neighbor. The accompanying command dossier explains native registration and permission effects; this dossier concentrates on construction, lifecycle, API policy and wrapper ownership. The source provides no PR discussion establishing why every alternative was rejected. Where a rationale is inferred from a changed boundary rather than stated in a title/comment, it is presented as such.

## Native metadata construction alternatives {#native-metadata-construction-alternatives}

415 simplifies PluginDescription construction to name/version and moves optional values into a setup structure. 416 adds a macro-generated exported factory named init_endstone_plugin and a static description setup path. This replaces the earlier EndstonePluginInit symbol and changes how plugins supply their descriptions. The first attempt assigns a private base-class description pointer. 417 tries friendship, 418 exposes the pointer publicly and updates both platform loaders, and 420 abandons that pointer arrangement in favor of a macro-generated subclass overriding the pure virtual getDescription. 421 then gives each plugin instance an owned description snapshot and fully qualifies the generated return type.

These adjacent commits show concrete alternatives and source-compatibility repairs. They do not prove that all intermediate commits built successfully. The namespace/linkage/friendship arrangement and the unqualified generated return type are visible constraints. The final macro still imposes its own contract: the supplied main class must be derivable and default-constructible, and the generated implementation supplies description behavior.

426 separates PluginMetadata into its own header. 429 adds CommandBuilder and PermissionBuilder maps keyed by lowercased names. Repeated lookup returns the same builder rather than replacing the existing entry. 431 changes usages, aliases and permission lists from replaceable vectors to accumulating sorted sets. This is a meaningful semantic change: calls deduplicate and accumulate, but output ordering becomes lexical rather than insertion order. A convenience builder refactor can therefore affect help text or overload/alias ordering. No ordering-equivalence test accompanies it.

444–446 complete the separation. PluginDescription stores explicit values and returns snapshots instead of rebuilding builder maps on each query; PluginDescriptionBuilder constructs that value, and the Python adapter follows its new constructor ordering. The macro's static builder is initialized before constructing the generated plugin object. It is still process/static state reused if the factory is called repeatedly; accumulation can carry across repeated setup calls. The repository does not show a repeated-factory test or declare that repeated calls are supported.

The endpoint description and builder headers include one another. With the builder included first, the description definition is available before the builder's build function. With description included directly first, the builder reaches PluginDescription before it has been declared. This source-level include-order constraint limits any claim that the refactor produced independently includable public headers. No compiler was run to turn it into an observed diagnostic, and it is not a reason to expand this review into an unrelated include audit.

## Metadata fields are not all runtime policies {#metadata-fields-are-not-all-runtime-policies}

421 adds website and contributors, later displayed by the version command in 443. 422 introduces Startup and PostWorld metadata, with capitalization and aggregate-order repairs in 423–424. 432 adds provides, dependency lists and default_permission; 440 standardizes depend and soft_depend spelling. These API names and values are preserved individually, even when the behavior change is small.

The endpoint explicitly leaves dependency, soft dependency, load-before and provides resolution as a manager TODO. Phase selection does run, but it is not dependency-graph scheduling. Similarly, default_permission is stored in the description, while PermissionBuilder still uses its own default and Python permission construction uses its own fallback. There is no propagation of the plugin-level value to every permission in this range. Merely exposing a property and producing stubs does not implement the policy described by its name.

## Startup order is moved and then repaired {#startup-order-is-moved-and-then-repaired}

438 moves server construction, Python-loader registration and plugin loading from the earlier server-thread start location to initialize-start. It enables Startup plugins before forwarding that original host callback. At thread-started it enables PostWorld plugins. All loaded plugins receive onLoad before either phase-specific enable loop because loading collects plugins and then calls those load callbacks.

At first, command-map population is delayed until after PostWorld callbacks. 439 moves initialization and core permission setup before those callbacks, then registers each plugin's declared permissions immediately before enabling it. This is a causally linked availability repair, not simply two independent lifecycle refactors. Startup plugins remain earlier than command-map initialization, so the default phase and early phase have different available services. API documentation must be read in that temporal context.

The directory-absent path still only creates the directory and skips loader enumeration on that call. That inherited control-flow detail is not changed by adding lifecycle phases. Similarly, the manager retains loader-order iteration rather than dependency ordering. Registration errors are logged or returned in individual components; the new high-level lifecycle sequence does not provide an all-or-nothing activation transaction.

The previous GIL-aware explicit server reset remains in the thread-stopped callback. This range does not reestablish a different shutdown cause or supersede the earlier documented uncertainty about the original Windows exit problem. Object ownership and lifecycle phase changes should be analyzed alongside that existing teardown contract, rather than asserting a new measured shutdown result.

## API compatibility is a gate after some code has already run {#api-compatibility-is-a-gate-after-some-code-has-already-run}

433 adds a native plugin API major.minor equality check. 434 centralizes the literal in a macro, and 435 stores the API string in the description during construction instead of recomputing it in the getter. Storing plugin-created metadata better preserves the intended provenance of the reported version; it is not a comprehensive solution to cross-module C++ ABI or inline-definition issues. The macro contains a trailing semicolon at this point, which works at its current assignment sites but is not a general expression macro.

The check necessarily follows library loading and factory invocation in this implementation. It can reject the plugin before normal registration, but it cannot guarantee that no incompatible initializer/factory code has already run. 437 clarifies the diagnostic. These are concrete policy and placement facts, not evidence of malicious input or a recommendation to execute untrusted plugins.

441 deduplicates Windows and Linux loaders behind platform macros. The shared path extends prefix-based logger naming, previously added only in the Windows branch by 419, to Linux. It also moves the API check into loadPlugin before the raw factory result is wrapped in unique_ptr. The mismatch return therefore no longer benefits from the previous local smart-pointer destruction. The module and instance are not cleaned up on that branch. This narrowly demonstrates why reducing duplicated code must be checked against failure-path ownership, not just matching successful output.

462 adds a separate Python declared-api check. Missing api_version warns and proceeds; an unsupported value logs and skips instantiation. However, ep.load and distribution metadata retrieval already happened. The gate is before class construction, not before import. 463 changes the C++ header to API 0.3 while explicitly allowing Python plugins declaring 0.2 or 0.3. Native compatibility remains exact current major.minor. This asymmetry is a supported policy observation; a blanket claim that the project rejects every older plugin would be wrong.

The native PluginDescription created by Python records the runtime header's version, while the loader consumes the class's declared api_version separately. A later consumer of description.api_version therefore cannot assume it is the exact declaration used by that Python compatibility check. Source schemas and provenance of version fields matter as much as their spelling.

## Python metadata loading changes its fallback and inheritance contract {#python-metadata-loading-changes-its-fallback-and-inheritance-contract}

366 looks up distribution metadata using endstone_ plus a normalized entry-point name and derives a display name from that entry point. It assumes a packaging naming convention instead of obtaining the actual distribution owning the entry point. 459 moves most metadata to a shallow copy of the direct plugin class dictionary. Distribution metadata remains a name/version fallback; the old summary/authors fallback is no longer used.

Using cls.__dict__ captures direct declarations but not inherited custom metadata. Methods and other class attributes are passed through the description adapter's permissive extra-keyword path and ignored when unused. This makes direct declarative syntax convenient, but a misspelled supported key may also be ignored. Nested permission dictionaries are not deep-copied: normalization replaces their default values in the original nested mapping. These are observed implementation contracts, not inferred personal preferences about Python inheritance.

459 builds Command and Permission values before plugin instantiation, converts bool and string permission defaults, and normalizes load-order strings. 462 repairs None handling for optional fields and removes processed keys before constructing the description. A plugin whose direct name or version is explicitly None is still not necessarily the same as a missing attribute fallback; only the optional fields covered by the adapter receive its defaulting behavior. No loader test matrix for inheritance, unknown keys, repeated loads or invalid enum spellings is supplied here.

The loader's server property, removed earlier at 288, is restored in 462 because compatibility diagnostics need server logging. This is a concrete removal/restoration chain. PluginLoader.disable_plugin still binds enablePlugin in the endpoint binding source, an inherited mismatch not repaired by the property restoration. It should not disappear from historical caveats merely because the API facade becomes more complete.

## Wrapper lifetime remains separate from native ownership {#wrapper-lifetime-remains-separate-from-native-ownership}

411 removes direct Python PluginCommand construction and its trampoline as the imperative registration API goes away. 447 restores construction of plain Command values for metadata, with a factory returning the base type. This does not restore arbitrary Python virtual execute dispatch. 449 moves PluginCommand binding initialization back into the plugin module and forward-creates enum/class wrappers as ordinary local objects. That retains the earlier 307 approach rather than reinstating the static pybind wrapper cache that caused a reported shutdown problem.

455 supplies a Python PluginCommand facade around an already existing native command. It delegates methods and properties to the underlying object, retains a custom Python executor in a Python attribute, and caches wrappers by native command in each Plugin. This preserves repeated lookup identity and the Python executor object, revisiting the lifetime goal of 299–303 in the new declarative model. Native executor shared_ptr ownership alone had not been treated as enough to preserve every Python override wrapper.

The facade also constructs its own base Command subobject, then forwards Python-level operations to the separate native implementation. Passing the facade through a native base-class API is therefore not proven equivalent to passing the implementation: Python property forwarding and C++ base-object identity are different mechanisms. The source supplies no such conversion test. Plugin.getCommand also still delegates globally without checking owner identity, despite its plugin-specific wording. These limits prevent overstating the new cache as a complete ownership or namespace guarantee.

Borrowed server, logger, owner and command references retain their original lifetime boundaries. The added command_sender property in 448 exposes an existing server-owned object rather than transferring it to Python. Generated stubs can describe accessibility and annotations, but do not demonstrate successful teardown, callback retention or native lifetime safety.

## Testing, attribution and practical reuse {#testing-attribution-and-practical-reuse}

430's test-package edits show how to declare command usages, aliases, permission children and defaults. They are meaningful examples and source-compatibility scaffolding. They do not add assertions that the declarations register, dependencies order correctly, denial works, or repeated construction is safe. No upstream code was executed for this research.

The practical design questions are: which metadata is a stable value snapshot, which builder state is retained, what services exist in each lifecycle phase, what code executes before a compatibility gate, and which Python object must remain alive in addition to a native smart pointer? The observed sequence supports those questions while preserving the costs and counterexamples of the chosen implementations. It does not prove a permanent preference for macros, fluent builders or one ownership model in every project.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-366"></a>
### 366. feat: ensure plugin distribution names always start with the "endstone_" namespace {#commit-366}

Source: [d4faa50098c38757b02e91f2f256c3afbc38dd28](https://github.com/EndstoneMC/endstone/commit/d4faa50098c38757b02e91f2f256c3afbc38dd28) · authored 2024-03-13T22:45:03Z · parent `5dc491617359564fb932edcd83106331ef5f4149`.

Author: **Vincent**.

Requires metadata lookup under endstone_ plus normalized entry-point name, while display plugin name is derived from entry-point name rather than distribution metadata name. Establishes a packaging naming convention but still infers distribution association instead of using actual entry-point owner. Existing unexpanded TypeError placeholder and absent-author None behavior remain. Website metadata is expressly TODO.

Changed paths: `python/src/endstone/_internal/plugin_loader.py`.

Coverage: 23 canonical patch lines; 1 changed paths.

<a id="commit-409"></a>
### 409. refactor: move PluginCommand to separate header file {#commit-409}

Source: [fc6cc150f05c65e73e09dd0dac841e86cb73e07f](https://github.com/EndstoneMC/endstone/commit/fc6cc150f05c65e73e09dd0dac841e86cb73e07f) · authored 2024-03-19T23:23:00Z · parent `d788a0b730dbc5c896d1b8850b2924712392870a`.

Author: **Vincent**.

Moves PluginCommand back into separate command header, reversing 282 placement, while removing Plugin::registerCommand/registerPermission helpers. Command execution/owner/executor code is relocated unchanged apart from context. This prepares metadata-driven registration and breaks previous imperative helper API; title understates removals.

Changed paths: `include/endstone/command/plugin_command.h`, `include/endstone/plugin/plugin.h`.

Coverage: 259 canonical patch lines; 2 changed paths.

<a id="commit-410"></a>
### 410. refactor: remove registerPluginCommand from Server class {#commit-410}

Source: [a880d65b53a0a778351cc2a0e87f2ca992a76cb7](https://github.com/EndstoneMC/endstone/commit/a880d65b53a0a778351cc2a0e87f2ca992a76cb7) · authored 2024-03-19T23:23:24Z · parent `fc6cc150f05c65e73e09dd0dac841e86cb73e07f`.

Author: **Vincent**.

Removes server registerPluginCommand public/concrete/test interface, leaving lookup and internal map registration. Completes withdrawal of imperative construction path. Python registration binding remains briefly stale until 411; metadata registration arrives 439.

Changed paths: `include/endstone/detail/server.h`, `include/endstone/server.h`, `src/endstone_core/server.cpp`, `test_package/src/test_server.cpp`.

Coverage: 74 canonical patch lines; 4 changed paths.

<a id="commit-411"></a>
### 411. fix: python bindings due to the change in PluginCommand {#commit-411}

Source: [479096bdca2434af4aa3c87e06a592aa127424a1](https://github.com/EndstoneMC/endstone/commit/479096bdca2434af4aa3c87e06a592aa127424a1) · authored 2024-03-19T23:24:09Z · parent `a880d65b53a0a778351cc2a0e87f2ca992a76cb7`.

Author: **Vincent**.

Moves PluginCommand binding into command module without constructor/trampoline, exposing executor property directly and removing server registration binding. This removes earlier retained-wrapper strategy while Python facade still expects old methods until later rewrite.455 restores explicit executor retention through a wrapper adapted to metadata-created commands. Known server-name misbinding remains.

Changed paths: `src/endstone_python/command.cpp`, `src/endstone_python/plugin.cpp`, `src/endstone_python/server.cpp`.

Coverage: 112 canonical patch lines; 3 changed paths.

<a id="commit-412"></a>
### 412. feat: add endstone export header file {#commit-412}

Source: [106d7e0571e115b740962dcb9c5c62c5ae6ecf37](https://github.com/EndstoneMC/endstone/commit/106d7e0571e115b740962dcb9c5c62c5ae6ecf37) · authored 2024-03-19T23:45:51Z · parent `479096bdca2434af4aa3c87e06a592aa127424a1`.

Author: **Vincent**.

Adds shared export macro for Windows or default ELF visibility, guarded for override. Centralizes platform export spelling; exported C entry still returns a C++ object and does not make plugin ABI portable.

Changed paths: `include/endstone/endstone.h`.

Coverage: 29 canonical patch lines; 1 changed paths.

<a id="commit-414"></a>
### 414. feat: add version and stringify macro in endstone.h {#commit-414}

Source: [400eaccf0ffc079228351066883f98a06b38c8a8](https://github.com/EndstoneMC/endstone/commit/400eaccf0ffc079228351066883f98a06b38c8a8) · authored 2024-03-19T23:58:04Z · parent `a1bfae25c3fe35e9d871a79b2c92c63ecbe65fc1`.

Author: **Vincent**.

Introduces header major/minor/patch0.2.0 plus two-stage stringify macros. Supports compile-time API identity used by subsequent plugin description; no compatibility enforcement yet.

Changed paths: `include/endstone/endstone.h`.

Coverage: 18 canonical patch lines; 1 changed paths.

<a id="commit-415"></a>
### 415. refactor: plugin description {#commit-415}

Source: [3136014571de24e463b43b5fa78453762ee64631](https://github.com/EndstoneMC/endstone/commit/3136014571de24e463b43b5fa78453762ee64631) · authored 2024-03-19T23:58:51Z · parent `400eaccf0ffc079228351066883f98a06b38c8a8`.

Author: **Vincent**.

Reduces description constructor to name/version, returns identity strings by value, exposes optional metadata as public fields and adds API version from header major/minor. Removes Python optional constructor adapter temporarily, so existing loader/tests still passing metadata keywords require later repair. Evolves metadata representation, not only naming.

Changed paths: `include/endstone/plugin/plugin_description.h`, `src/endstone_python/plugin.cpp`.

Coverage: 142 canonical patch lines; 2 changed paths.

<a id="commit-416"></a>
### 416. refactor: ENDSTONE_PLUGIN macro {#commit-416}

Source: [5059517425a1a74659c6f2c678ab32a62e463de9](https://github.com/EndstoneMC/endstone/commit/5059517425a1a74659c6f2c678ab32a62e463de9) · authored 2024-03-20T00:11:15Z · parent `3136014571de24e463b43b5fa78453762ee64631`.

Author: **Vincent**.

Changes plugin export to init_endstone_plugin and expands macro to create static description plus initialization function, making Plugin getDescription dereference a new pointer instead of abstract override. Macro writes private field without access until 417, and loader symbol migration follows 418. Static metadata lifetime is distinct from plugin object lifetime and repeated initializer calls can mutate it.

Changed paths: `include/endstone/plugin/plugin.h`.

Coverage: 59 canonical patch lines; 1 changed paths.

<a id="commit-417"></a>
### 417. Add friend function to set plugin description in ENDSTONE_PLUGIN macro {#commit-417}

Source: [583683109140be2341de3b4355871e4a3455bfa6](https://github.com/EndstoneMC/endstone/commit/583683109140be2341de3b4355871e4a3455bfa6) · authored 2024-03-20T00:12:41Z · parent `5059517425a1a74659c6f2c678ab32a62e463de9`.

Author: **Vincent**.

Adds friend declaration intended to allow macro entry function to set private description. Namespace/C-linkage correspondence remains delicate;418 abandons this attempt by exposing the pointer, then 420 restores abstract override design. Preserve as short-lived access-control alternative, not a settled pattern.

Changed paths: `include/endstone/plugin/plugin.h`.

Coverage: 12 canonical patch lines; 1 changed paths.

<a id="commit-418"></a>
### 418. fix: cpp_plugin_loader {#commit-418}

Source: [f0e2bfe13e126c7a868967b249fce3bcacee837a](https://github.com/EndstoneMC/endstone/commit/f0e2bfe13e126c7a868967b249fce3bcacee837a) · authored 2024-03-20T00:27:22Z · parent `583683109140be2341de3b4355871e4a3455bfa6`.

Author: **Vincent**.

Moves description pointer public, adds macro body variable parameter, updates both platform loaders to new init_endstone_plugin export, and migrates package fixture to metadata macro. Removes earlier friend workaround. Entry-point and macro contract must change together; existing binary plugins with old export fail discovery.

Changed paths: `include/endstone/plugin/plugin.h`, `src/endstone_core/plugin/cpp_plugin_loader.cpp`, `test_package/src/test_plugin.cpp`.

Coverage: 128 canonical patch lines; 3 changed paths.

<a id="commit-419"></a>
### 419. fix: c++ plugin logger now respect prefix property {#commit-419}

Source: [d956e7d8fc5ab707d7fcfaa07f7ee304c9c70fae](https://github.com/EndstoneMC/endstone/commit/d956e7d8fc5ab707d7fcfaa07f7ee304c9c70fae) · authored 2024-03-20T00:30:45Z · parent `f0e2bfe13e126c7a868967b249fce3bcacee837a`.

Author: **Vincent**.

Uses description prefix with name fallback for C++ plugin logger in the Windows loader branch. Linux duplicate branch is not changed here; later 441 consolidation carries common implementation across both. Source title is broader than immediate platform coverage; no logging test run.

Changed paths: `src/endstone_core/plugin/cpp_plugin_loader.cpp`.

Coverage: 17 canonical patch lines; 1 changed paths.

<a id="commit-420"></a>
### 420. refactor: improve ENDSTONE_PLUGIN macro {#commit-420}

Source: [b59ed710d89fbdee5d0c02437d204a91a34babeb](https://github.com/EndstoneMC/endstone/commit/b59ed710d89fbdee5d0c02437d204a91a34babeb) · authored 2024-03-20T01:02:21Z · parent `d956e7d8fc5ab707d7fcfaa07f7ee304c9c70fae`.

Author: **Vincent**.

Restores pure virtual getDescription and removes exposed pointer. Macro instead generates a subclass of user MainClass that returns static description, eliminating the private-field/friend/public-pointer workaround. API now requires derivable/default-constructible MainClass; namespace qualification of returned PluginDescription corrected 421. Fixture updated to three-argument macro.

Changed paths: `include/endstone/plugin/plugin.h`, `test_package/src/test_plugin.cpp`.

Coverage: 80 canonical patch lines; 2 changed paths.

<a id="commit-421"></a>
### 421. refactor: `ENDSTONE_PLUGIN` macro to use `PluginDetail` {#commit-421}

Source: [42f0cb06e8d5e3dbea24127bbb1c03917e27290d](https://github.com/EndstoneMC/endstone/commit/42f0cb06e8d5e3dbea24127bbb1c03917e27290d) · authored 2024-03-20T10:07:02Z · parent `b59ed710d89fbdee5d0c02437d204a91a34babeb`.

Author: **Vincent**.

Introduces PluginDetail data aggregate and changes generated subclass to own its description value copied from initialized static detail. Makes metadata encapsulated/read-only through getters, adds contributors/website and moves name regex into manager. This separates mutable setup aggregate from per-plugin snapshot; macro return type fully qualified, fixture namespace dependence later tested 426.

Changed paths: `include/endstone/plugin/plugin.h`, `include/endstone/plugin/plugin_description.h`, `src/endstone_core/plugin/cpp_plugin_loader.cpp`, `src/endstone_core/plugin/plugin_manager.cpp`.

Coverage: 181 canonical patch lines; 4 changed paths.

<a id="commit-422"></a>
### 422. feat: add getLoad method to PluginDescription {#commit-422}

Source: [a4bd58fc0ece34ef1f4a368c53a0c335aa5f68b3](https://github.com/EndstoneMC/endstone/commit/a4bd58fc0ece34ef1f4a368c53a0c335aa5f68b3) · authored 2024-03-20T10:14:31Z · parent `42f0cb06e8d5e3dbea24127bbb1c03917e27290d`.

Author: **Vincent**.

Adds Startup/PostWorld phase enum, metadata load default PostWorld and getter, with fixture demonstrating description/website/authors/load/prefix. Only metadata exists here; actual phase-aware enable behavior arrives 438. Initial spelling StartUp is changed 424.

Changed paths: `include/endstone/plugin/plugin.h`, `include/endstone/plugin/plugin_description.h`, `include/endstone/plugin/plugin_load_order.h`, `test_package/src/test_plugin.cpp`.

Coverage: 104 canonical patch lines; 4 changed paths.

<a id="commit-423"></a>
### 423. feat: extend PluginDescription with additional fields and createPluginDescription method {#commit-423}

Source: [31f98e4b004a8a848d2d1160eb3f0582b7fd3a69](https://github.com/EndstoneMC/endstone/commit/31f98e4b004a8a848d2d1160eb3f0582b7fd3a69) · authored 2024-03-20T10:27:27Z · parent `a4bd58fc0ece34ef1f4a368c53a0c335aa5f68b3`.

Author: **Vincent**.

Restores optional Python metadata adapter with contributors/website/load and binds phase enum. Uses Startup before 424 renames C++ enum and aggregate initialization order disagrees with current PluginDetail field order until 424 moves load. This is a staged cross-language migration, not a fully consistent independent commit.

Changed paths: `src/endstone_python/plugin.cpp`.

Coverage: 41 canonical patch lines; 1 changed paths.

<a id="commit-424"></a>
### 424. refactor: rename enum names {#commit-424}

Source: [e3b9a28b785b096657277c402f9a1db5f98cc5ca](https://github.com/EndstoneMC/endstone/commit/e3b9a28b785b096657277c402f9a1db5f98cc5ca) · authored 2024-03-20T10:27:39Z · parent `31f98e4b004a8a848d2d1160eb3f0582b7fd3a69`.

Author: **Vincent**.

Renames StartUp to Startup and moves load field to aggregate end, matching 423 Python initializer. Title only mentions enum spelling but layout/aggregate order repair is substantive; no output behavior test.

Changed paths: `include/endstone/plugin/plugin_description.h`, `include/endstone/plugin/plugin_load_order.h`.

Coverage: 30 canonical patch lines; 2 changed paths.

<a id="commit-426"></a>
### 426. refactor: rename detail::PluginDetail to detail::PluginMetadata {#commit-426}

Source: [323b64b3ee3e0d77fa72a4983c1579c22ff9c76c](https://github.com/EndstoneMC/endstone/commit/323b64b3ee3e0d77fa72a4983c1579c22ff9c76c) · authored 2024-03-20T10:46:09Z · parent `be0f1fd001fb19563367d0fdbe19d0844d853ceb`.

Author: **Vincent**.

Extracts PluginMetadata to detail header, renames macro/setup functions and stores const-reference input by copy. Adds dependency/load-before lists plus private command/permission vectors before APIs expose them. Fixture removes using-namespace and explicitly qualifies public names, useful downstream macro/header self-sufficiency coverage. Python aggregate construction temporarily cannot match private fields until later adapter rewrite.

Changed paths: `include/endstone/detail/plugin/plugin_metadata.h`, `include/endstone/plugin/plugin.h`, `include/endstone/plugin/plugin_description.h`, `test_package/src/test_plugin.cpp`.

Coverage: 234 canonical patch lines; 4 changed paths.

<a id="commit-428"></a>
### 428. refactor: rename method 'setPermission' to 'setPermissions' {#commit-428}

Source: [43b5049758388673829b298f07508b99e35ad464](https://github.com/EndstoneMC/endstone/commit/43b5049758388673829b298f07508b99e35ad464) · authored 2024-03-20T11:43:23Z · parent `48d9572c7b7887044e763a351041f42bb6547b19`.

Author: **Vincent**.

Pluralizes command permission setter and updates consumers, but also makes Command/EndstoneCommand constructors public again and inherits constructors for BedrockCommand. Reverses 314 protected-base choice to support metadata command values. Adds nodiscard to silent permission predicate; no enforcement-policy change.

Changed paths: `include/endstone/command/command.h`, `include/endstone/detail/command/bedrock_command.h`, `include/endstone/detail/command/endstone_command.h`, `src/endstone_core/command/defaults/plugins_command.cpp`, `src/endstone_core/command/defaults/version_command.cpp`, `src/endstone_python/command.cpp`.

Coverage: 112 canonical patch lines; 6 changed paths.

<a id="commit-429"></a>
### 429. feat: extend plugin metadata with additional parameters {#commit-429}

Source: [b86c8f2d8c3579bdfe35f5c32f3f9867e945b60e](https://github.com/EndstoneMC/endstone/commit/b86c8f2d8c3579bdfe35f5c32f3f9867e945b60e) · authored 2024-03-20T11:45:34Z · parent `43b5049758388673829b298f07508b99e35ad464`.

Author: **Vincent**.

Adds fluent CommandBuilder/PermissionBuilder and lowercase-keyed metadata maps with on-demand value construction; repeated lookup returns existing builder. Exposes dependency metadata to Python constructor. This creates a declarative registration model replacing removed imperative helpers, but no runtime registration until 438/439. Initial builder list setters replace prior values;431 changes them to accumulating sets.

Changed paths: `include/endstone/detail/plugin/plugin_metadata.h`, `src/endstone_python/plugin.cpp`.

Coverage: 183 canonical patch lines; 2 changed paths.

<a id="commit-430"></a>
### 430. test: register permissions and commands for the test plugin {#commit-430}

Source: [aec7153c59de5fb9830e292f5f5673ff99d01585](https://github.com/EndstoneMC/endstone/commit/aec7153c59de5fb9830e292f5f5673ff99d01585) · authored 2024-03-20T11:46:05Z · parent `b86c8f2d8c3579bdfe35f5c32f3f9867e945b60e`.

Author: **Vincent**.

Adds test-plugin permission hierarchy and command usage/alias/permission metadata examples. Exercises construction/source compatibility but adds no assertions about runtime registration, authorization or dependency ordering. Preserve fixture as usage evidence rather than a passed integration test.

Changed paths: `test_package/src/test_plugin.cpp`.

Coverage: 21 canonical patch lines; 1 changed paths.

<a id="commit-431"></a>
### 431. refactor: replace vectors with sets for storing plugin usages, aliases and permissions {#commit-431}

Source: [9cea74aac4aff5748d58fa2c43b10dfcc4c069ac](https://github.com/EndstoneMC/endstone/commit/9cea74aac4aff5748d58fa2c43b10dfcc4c069ac) · authored 2024-03-20T12:13:45Z · parent `aec7153c59de5fb9830e292f5f5673ff99d01585`.

Author: **Vincent**.

Changes builder usages/aliases/permissions to sorted sets and fold-expression insertion. Repeated setter calls now accumulate and deduplicate instead of replace, and built vectors use lexical rather than insertion order. This affects overload/help/alias ordering as well as duplicate handling; no equivalence test proves order irrelevant.

Changed paths: `include/endstone/detail/plugin/plugin_metadata.h`.

Coverage: 57 canonical patch lines; 1 changed paths.

<a id="commit-432"></a>
### 432. feat: add additional properties in plugin description {#commit-432}

Source: [ea9fd53270e8150ca17afdda92d6b5aac74d4ce6](https://github.com/EndstoneMC/endstone/commit/ea9fd53270e8150ca17afdda92d6b5aac74d4ce6) · authored 2024-03-20T12:29:25Z · parent `9cea74aac4aff5748d58fa2c43b10dfcc4c069ac`.

Author: **Vincent**.

Adds provides/default_permission and getter surfaces for dependency lists, commands and permissions; makes builder conversion const. Python adapter accepts new metadata. These are declarations of intent: default_permission is not propagated into individual PermissionBuilder defaults here, and dependency resolution remains unimplemented, explicitly noted 442.

Changed paths: `include/endstone/detail/plugin/plugin_metadata.h`, `include/endstone/plugin/plugin_description.h`, `src/endstone_python/plugin.cpp`.

Coverage: 179 canonical patch lines; 3 changed paths.

<a id="commit-433"></a>
### 433. feat: add API version check in C++ plugin loading {#commit-433}

Source: [edf705795c49a85db27fd74b4fc22accd9ee35ac](https://github.com/EndstoneMC/endstone/commit/edf705795c49a85db27fd74b4fc22accd9ee35ac) · authored 2024-03-20T12:46:24Z · parent `ea9fd53270e8150ca17afdda92d6b5aac74d4ce6`.

Author: **Vincent**.

Rejects C++ plugins whose reported API major.minor differs from runtime before adding to loader-owned collection. Check occurs after library load and plugin factory execution, so it cannot prevent all incompatible-binary interaction. Getter initially computes compile-time literal at call site;435 stores per-description value. No mismatch integration test.

Changed paths: `src/endstone_core/plugin/cpp_plugin_loader.cpp`.

Coverage: 26 canonical patch lines; 1 changed paths.

<a id="commit-434"></a>
### 434. feat: add `ENDSTONE_API_VERSION` macro {#commit-434}

Source: [866d7ce6d19d3eecea4af027afe03aebed3188db](https://github.com/EndstoneMC/endstone/commit/866d7ce6d19d3eecea4af027afe03aebed3188db) · authored 2024-03-20T12:49:17Z · parent `edf705795c49a85db27fd74b4fc22accd9ee35ac`.

Author: **Vincent**.

Centralizes major.minor API string in ENDSTONE_API_VERSION macro for loader/description. Macro includes trailing semicolon, acceptable at these statement sites but unsuitable as arbitrary expression; later code must respect that limitation. No compatibility-policy change.

Changed paths: `include/endstone/endstone.h`, `include/endstone/plugin/plugin_description.h`, `src/endstone_core/plugin/cpp_plugin_loader.cpp`.

Coverage: 48 canonical patch lines; 3 changed paths.

<a id="commit-435"></a>
### 435. feat: improve api version check error message {#commit-435}

Source: [4e4a52708cc3b162912d7b73dea33da41b60f541](https://github.com/EndstoneMC/endstone/commit/4e4a52708cc3b162912d7b73dea33da41b60f541) · authored 2024-03-20T13:53:37Z · parent `866d7ce6d19d3eecea4af027afe03aebed3188db`.

Author: **Vincent**.

Error-message title also stores API version in description during construction instead of recomputing getter literal, preserving plugin-created metadata across runtime call sites. Restores clang-tidy member-to-static rule disabled 413. Diagnostic now names plugin; no evidence all cross-library ABI or inline-definition issues are solved.

Changed paths: `.clang-tidy`, `include/endstone/plugin/plugin_description.h`, `src/endstone_core/plugin/cpp_plugin_loader.cpp`.

Coverage: 60 canonical patch lines; 3 changed paths.

<a id="commit-436"></a>
### 436. fix: getPluginCommand method {#commit-436}

Source: [5ef723581b8202f4d81d96852b6af4d8dfda8b97](https://github.com/EndstoneMC/endstone/commit/5ef723581b8202f4d81d96852b6af4d8dfda8b97) · authored 2024-03-20T14:07:58Z · parent `4e4a52708cc3b162912d7b73dea33da41b60f541`.

Author: **Vincent**.

Checks command lookup before virtual asPluginCommand call and returns nullptr when absent, repairing null-dereference regression introduced 347. Retains RTTI-free lookup alternative. No new regression test, but exact source control-flow repair is clear.

Changed paths: `src/endstone_core/server.cpp`.

Coverage: 16 canonical patch lines; 1 changed paths.

<a id="commit-437"></a>
### 437. refactor: refine error messaging for incompatible plugins. {#commit-437}

Source: [5723474abd818fecd59636423e6362e947166730](https://github.com/EndstoneMC/endstone/commit/5723474abd818fecd59636423e6362e947166730) · authored 2024-03-20T14:08:13Z · parent `5ef723581b8202f4d81d96852b6af4d8dfda8b97`.

Author: **Vincent**.

Clarifies incompatible-plugin message as API version rather than framework version and removes v prefix. Same exact equality check and failure path.

Changed paths: `src/endstone_core/plugin/cpp_plugin_loader.cpp`.

Coverage: 20 canonical patch lines; 1 changed paths.

<a id="commit-438"></a>
### 438. feat: implement plugin load order {#commit-438}

Source: [acd2ed78b482adaaa0abb5629d8f5cd22c184702](https://github.com/EndstoneMC/endstone/commit/acd2ed78b482adaaa0abb5629d8f5cd22c184702) · authored 2024-03-20T15:13:06Z · parent `5723474abd818fecd59636423e6362e947166730`.

Author: **Vincent**.

Moves server setup/loading from startServerThread to initialize-start coordinator, enables Startup plugins there and PostWorld plugins at thread-started callback. Registers declared permissions before enabling each plugin, then dirties default subscribers. Delays command-map population from constructor to PostWorld; initial placement is after plugin callbacks, revised 439. Phase selection is implemented, dependency ordering is not. Directory-absent path still creates directory without loading.

Changed paths: `include/bedrock/server/server_instance.h`, `include/endstone/command/command_map.h`, `include/endstone/detail/command/command_map.h`, `include/endstone/detail/plugin/plugin_manager.h`, `include/endstone/detail/server.h`, `src/endstone_core/command/command_map.cpp`, `src/endstone_core/command/server_command_sender.cpp`, `src/endstone_core/server.cpp`, `src/endstone_runtime/bedrock/server/server_instance.cpp`.

Coverage: 218 canonical patch lines; 9 changed paths.

<a id="commit-439"></a>
### 439. feat: implement plugin command registration from plugin description {#commit-439}

Source: [a55d7bda2bd9df29fd21f0b0988d510a9cbb7938](https://github.com/EndstoneMC/endstone/commit/a55d7bda2bd9df29fd21f0b0988d510a9cbb7938) · authored 2024-03-20T15:43:05Z · parent `acd2ed78b482adaaa0abb5629d8f5cd22c184702`.

Author: **Vincent**.

Adds command-map initialise to import native/built-in commands, populate plugin-name enums and wrap each description Command in PluginCommand. Runs it and core-permission registration before PostWorld enable callbacks, repairing 438 command-availability order for that phase. Startup callbacks still occur before map initialization. Registration iterates all loaded plugins and ignores boolean failures; no transaction/repeated-init tests. Constructor copies metadata Command, preserving earlier separation from custom execute logic.

Changed paths: `include/endstone/command/plugin_command.h`, `include/endstone/detail/command/command_map.h`, `src/endstone_core/command/command_map.cpp`, `src/endstone_core/server.cpp`.

Coverage: 102 canonical patch lines; 4 changed paths.

<a id="commit-440"></a>
### 440. refactor: renaming of methods getDepends and getSoftDepends to getDepend and getSoftDepend respectively {#commit-440}

Source: [c70ca2c5c6f4c5c8a2ffc3c9a553ebfdc9bd18ea](https://github.com/EndstoneMC/endstone/commit/c70ca2c5c6f4c5c8a2ffc3c9a553ebfdc9bd18ea) · authored 2024-03-20T15:45:51Z · parent `a55d7bda2bd9df29fd21f0b0988d510a9cbb7938`.

Author: **Vincent**.

Renames dependency fields/getters/Python keywords from plural depends/soft_depends to depend/soft_depend. Source API migration only; values and still-unimplemented dependency scheduling unchanged.

Changed paths: `include/endstone/detail/plugin/plugin_metadata.h`, `include/endstone/plugin/plugin_description.h`, `src/endstone_python/plugin.cpp`.

Coverage: 76 canonical patch lines; 3 changed paths.

<a id="commit-441"></a>
### 441. feat: add macros to simplify the call to load C++ plugins on different platforms {#commit-441}

Source: [65d51747dc1dd3a91769c32baa94e6dd4fb49a2f](https://github.com/EndstoneMC/endstone/commit/65d51747dc1dd3a91769c32baa94e6dd4fb49a2f) · authored 2024-03-20T16:02:53Z · parent `c70ca2c5c6f4c5c8a2ffc3c9a553ebfdc9bd18ea`.

Author: **Vincent**.

Consolidates Windows/Linux library-load implementations behind four platform macros, removes duplicate branch and undefines macros afterward. Prefix logger behavior now reaches Linux too. Moves API check into loadPlugin before wrapping raw plugin pointer in unique_ptr, so rejection no longer gets previous local unique_ptr destruction; module/instance cleanup remains incomplete. Deduplication reduces platform drift but must preserve failure ownership, not just happy-path code.

Changed paths: `src/endstone_core/plugin/cpp_plugin_loader.cpp`.

Coverage: 152 canonical patch lines; 1 changed paths.

<a id="commit-443"></a>
### 443. feat: display website and contributors in version command {#commit-443}

Source: [e21cae6c40e2043ac2b087b1f461f19d31dadcfa](https://github.com/EndstoneMC/endstone/commit/e21cae6c40e2043ac2b087b1f461f19d31dadcfa) · authored 2024-03-20T23:31:04Z · parent `c22850004f2bbfa43e5218ad32d74f7efa4371fa`.

Author: **Vincent**.

Displays website and contributors in version output when nonempty, replacing long-standing TODOs. Uses existing name-list helper and formatting, whose earlier separator behavior remains; no output snapshot test.

Changed paths: `src/endstone_core/command/defaults/version_command.cpp`.

Coverage: 32 canonical patch lines; 1 changed paths.

<a id="commit-444"></a>
### 444. refactor PluginDescription class constructor. {#commit-444}

Source: [6bc4e9301289d4ed856a387444a9a79e0b3dcc4b](https://github.com/EndstoneMC/endstone/commit/6bc4e9301289d4ed856a387444a9a79e0b3dcc4b) · authored 2024-03-20T23:56:41Z · parent `e21cae6c40e2043ac2b087b1f461f19d31dadcfa`.

Author: **Vincent**.

Replaces embedded PluginMetadata with explicit description fields and long constructor including command/permission vectors. Getter results are stored snapshots instead of rebuilding builders each call. References builder header that arrives 445; circular include ordering between description and builder needs care, not evidence of standalone-header validation.

Changed paths: `include/endstone/plugin/plugin_description.h`.

Coverage: 184 canonical patch lines; 1 changed paths.

<a id="commit-445"></a>
### 445. refactor: add PluginDescriptionBuilder, remove PluginMetadata {#commit-445}

Source: [0dbae89c9032d7c7005c641d1f116d78db74ed81](https://github.com/EndstoneMC/endstone/commit/0dbae89c9032d7c7005c641d1f116d78db74ed81) · authored 2024-03-20T23:57:15Z · parent `6bc4e9301289d4ed856a387444a9a79e0b3dcc4b`.

Author: **Vincent**.

Renames setup aggregate PluginDescriptionBuilder and adds build(name, version) producing plain PluginDescription; macro owns a description snapshot built after setup. Command and permission conversion helpers become private. Separates construction DSL from runtime metadata. The endpoint description and builder headers include each other: builder-first include order permits description definition before build, whereas direct description-first inclusion reaches an undeclared PluginDescription in builder. Static builder persists across factory calls and accumulating setters can retain state. These are source-level constraints, not executed compiler or repeated-factory tests.

Changed paths: `include/endstone/detail/plugin/plugin_description_builder.h`, `include/endstone/detail/plugin/plugin_metadata.h`, `include/endstone/plugin/plugin.h`.

Coverage: 411 canonical patch lines; 3 changed paths.

<a id="commit-446"></a>
### 446. refactor: update python bindings for PluginDescription constructor {#commit-446}

Source: [f89f1ba097ec43bc13a6e8c3ea01583c17f0b951](https://github.com/EndstoneMC/endstone/commit/f89f1ba097ec43bc13a6e8c3ea01583c17f0b951) · authored 2024-03-20T23:57:31Z · parent `0dbae89c9032d7c7005c641d1f116d78db74ed81`.

Author: **Vincent**.

Aligns Python optional adapter with expanded plain description constructor, reorders load position and adds commands/permissions vectors. Inputs None normalize to empty/default values. Restores cross-language construction after 444/445; source alone does not establish all overload/default combinations work.

Changed paths: `src/endstone_python/plugin.cpp`.

Coverage: 65 canonical patch lines; 1 changed paths.

<a id="commit-447"></a>
### 447. feat(python): add constructor for Command class {#commit-447}

Source: [eaa528f7d0bb3a3655e34fd3a10358d85be7a53d](https://github.com/EndstoneMC/endstone/commit/eaa528f7d0bb3a3655e34fd3a10358d85be7a53d) · authored 2024-03-21T00:04:40Z · parent `f89f1ba097ec43bc13a6e8c3ea01583c17f0b951`.

Author: **Vincent**.

Restores public Python Command constructor for metadata values, normalizing optional fields and accepting extra args/kwargs. Factory returns base Command with no trampoline, consistent with declarative metadata rather than Python virtual execute subclassing. Unknown kwargs are ignored by adapter, allowing broad class metadata dictionaries later 459.

Changed paths: `src/endstone_python/command.cpp`.

Coverage: 41 canonical patch lines; 1 changed paths.

<a id="commit-448"></a>
### 448. feat(python): add CommandSender property in Server class. {#commit-448}

Source: [69ca452daa37aad38629397e05e6f09a378895dd](https://github.com/EndstoneMC/endstone/commit/69ca452daa37aad38629397e05e6f09a378895dd) · authored 2024-03-21T00:04:52Z · parent `eaa528f7d0bb3a3655e34fd3a10358d85be7a53d`.

Author: **Vincent**.

Exposes borrowed Server.command_sender property, making native server sender available in Python. Lifetime still follows server; no ownership transfer or shutdown keep-alive guarantee.

Changed paths: `src/endstone_python/server.cpp`.

Coverage: 13 canonical patch lines; 1 changed paths.

<a id="commit-449"></a>
### 449. feat(python): add necessary forward declaration to avoid cpp types in docstrings {#commit-449}

Source: [5170e0472da54f23bdd1110cebe3279547d9fef0](https://github.com/EndstoneMC/endstone/commit/5170e0472da54f23bdd1110cebe3279547d9fef0) · authored 2024-03-21T00:18:04Z · parent `69ca452daa37aad38629397e05e6f09a378895dd`.

Author: **Vincent**.

Forward-creates permission enum and relocates PluginCommand binding back to plugin initialization so type names exist before signatures/docstrings use them. Retains ordinary local wrappers rather than static cache from prior 286. Generated stubs catch up constructor/removal/property changes but still show unbound Permission placeholders until 453.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/command.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/permissions.cpp`, `src/endstone_python/plugin.cpp`.

Coverage: 208 canonical patch lines; 5 changed paths.

<a id="commit-450"></a>
### 450. feat(python): expand PluginDescription properties {#commit-450}

Source: [84b664a602510b74587ea0edf851644ca2d80a32](https://github.com/EndstoneMC/endstone/commit/84b664a602510b74587ea0edf851644ca2d80a32) · authored 2024-03-21T00:23:38Z · parent `5170e0472da54f23bdd1110cebe3279547d9fef0`.

Author: **Vincent**.

Exposes all expanded description fields in Python and updates stubs. Removes incorrect command timing phrase from C++ doc, matching 439 registration separate from per-plugin enabling. Dependency/default-policy metadata exposure is not implementation of dependency/default propagation.

Changed paths: `include/endstone/plugin/plugin_description.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/plugin.cpp`.

Coverage: 146 canonical patch lines; 3 changed paths.

<a id="commit-454"></a>
### 454. refactor: update command setters to not return any value {#commit-454}

Source: [9f4a178936ebac9546e8aee7a57301b354e87dc5](https://github.com/EndstoneMC/endstone/commit/9f4a178936ebac9546e8aee7a57301b354e87dc5) · authored 2024-03-21T01:28:52Z · parent `153a83b7218b08d5f12eb2080a8c1015ced2dcef`.

Author: **Vincent**.

Makes command setters void, removing chaining/success return and moving temporary list construction inside unregistered guard. Registered mutations remain silently ignored except permission setter, which is unchanged. Simplifies value-style API but removes caller feedback; no justification beyond refactor title or test evidence supplied.

Changed paths: `include/endstone/command/command.h`.

Coverage: 86 canonical patch lines; 1 changed paths.

<a id="commit-455"></a>
### 455. feat: add PluginCommand wrapper to keep the executor alive {#commit-455}

Source: [66a44d03a74dc0b5396a25e28a9463e1b071ae95](https://github.com/EndstoneMC/endstone/commit/66a44d03a74dc0b5396a25e28a9463e1b071ae95) · authored 2024-03-21T01:35:59Z · parent `9f4a178936ebac9546e8aee7a57301b354e87dc5`.

Author: **Vincent**.

Replaces constructible PluginCommand subclass facade with delegating wrapper around existing native command and retains custom Python executor explicitly. Plugin caches wrappers keyed by native command identity, preserving repeated get_command object and executor lifetime. Removes obsolete register_command path and exposes class-level metadata fields. Wrapper has its own base Command storage but delegates Python methods/properties to implementation; passing wrapper through native base APIs is not proven equivalent by this source.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/plugin.py`.

Coverage: 214 canonical patch lines; 2 changed paths.

<a id="commit-457"></a>
### 457. feat(python): import PluginLoadOrder into plugin module {#commit-457}

Source: [820ff4a3a69d50c3d858e1d1867873a251908b6a](https://github.com/EndstoneMC/endstone/commit/820ff4a3a69d50c3d858e1d1867873a251908b6a) · authored 2024-03-21T02:09:36Z · parent `d7e8726e35dd5601b0e67a2a4ee379aff98e0056`.

Author: **Vincent**.

Re-exports PluginLoadOrder in public plugin module. Completes public configuration ergonomics without changing lifecycle timing.

Changed paths: `python/src/endstone/plugin.py`.

Coverage: 28 canonical patch lines; 1 changed paths.

<a id="commit-459"></a>
### 459. feat: implement python plugin loader for the refactored plugin description {#commit-459}

Source: [d7bad11ce16ab26664c8eb28804253835ba0b8e4](https://github.com/EndstoneMC/endstone/commit/d7bad11ce16ab26664c8eb28804253835ba0b8e4) · authored 2024-03-21T02:17:15Z · parent `9346b850c46bb8daaaaabe42e6bd5b99edee2ef1`.

Author: **Vincent**.

Builds command and permission objects from direct plugin class attributes before instantiation; normalizes bool/string permission defaults and load-order strings, uses distribution metadata only for name/version fallback, and fixes missing f-string in type error. Shallow cls.__dict__ omits inherited custom metadata and nested permission normalization mutates original dictionaries. Does not carry old distribution summary/authors fallback forward. Explicit None handling is incomplete until 462; no loader tests.

Changed paths: `python/src/endstone/_internal/plugin_loader.py`.

Coverage: 93 canonical patch lines; 1 changed paths.

<a id="commit-460"></a>
### 460. feat: update python stubs {#commit-460}

Source: [a8c971e280fc5dc2112b9eb1e7ff1959ae0f677d](https://github.com/EndstoneMC/endstone/commit/a8c971e280fc5dc2112b9eb1e7ff1959ae0f677d) · authored 2024-03-21T02:18:39Z · parent `d7bad11ce16ab26664c8eb28804253835ba0b8e4`.

Author: **Vincent**.

Updates generated Permission stub keyword/property to default, matching 458. Entire changed generated diff read; no independent runtime design or validation claim.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`.

Coverage: 29 canonical patch lines; 1 changed paths.

<a id="commit-462"></a>
### 462. feat: add api version check when loading python plugins {#commit-462}

Source: [c3b5c8bd2854b07be5b604ec13cb2d7e8ecbfb44](https://github.com/EndstoneMC/endstone/commit/c3b5c8bd2854b07be5b604ec13cb2d7e8ecbfb44) · authored 2024-03-21T11:44:04Z · parent `4b41d9d19fdfeb6e50fcd32be82930a2378797dd`.

Author: **Vincent**.

Checks declared Python api_version against supported list before constructing plugin instance; missing version warns and continues, incompatible version logs/skips. ep.load and distribution metadata retrieval already occurred, so import side effects precede compatibility check. Restores loader getServer/server binding removed 288, handles None optional metadata, and pops normalized keys before description construction. Native descriptor API version still records runtime header version, distinct from Python declared compatibility claim.

Changed paths: `include/endstone/plugin/plugin_loader.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/_internal/plugin_loader.py`, `python/src/endstone/plugin.py`, `src/endstone_python/plugin.cpp`.

Coverage: 170 canonical patch lines; 5 changed paths.

<a id="commit-463"></a>
### 463. release: version 0.3.0 {#commit-463}

Source: [5a7f4a2b4136fb490b481fdcee065a37768917f5](https://github.com/EndstoneMC/endstone/commit/5a7f4a2b4136fb490b481fdcee065a37768917f5) · authored 2024-03-21T11:56:45Z · parent `c3b5c8bd2854b07be5b604ec13cb2d7e8ecbfb44`.

Author: **Vincent**.

Releases header API 0.3 and documents milestone versions; Python supported list now accepts 0.2 and 0.3 while C++ loader still requires exact current major.minor. This is explicit compatibility-policy asymmetry rather than uniform version bump noise. No release publication/runtime compatibility proof observed.

Changed paths: `README.md`, `include/endstone/endstone.h`, `python/src/endstone/_internal/plugin_loader.py`.

Coverage: 59 canonical patch lines; 3 changed paths.
