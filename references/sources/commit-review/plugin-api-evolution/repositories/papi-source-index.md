<!-- retrieval: {"source_ids":["public:commit:02c31fd8863c1cce37aa3ff6e334e81097e48377","public:commit:044cb128d138e3d51422c128e1e3b1b64384e202","public:commit:0458d3d58298af12d39ad91ed0e0b88a52ba3a92","public:commit:070be6ee8ebc960c52361a981e556a17088c883a","public:commit:0cbb0b4b6b0e5963ea1f1179936a78cd489aa022","public:commit:0fdd2497e61ccfcffe67bf1292ef946fd659ce28","public:commit:117d8780bb1603c446cd4141cec6e59d9391f037","public:commit:173bf02fa2e5f7b0cba6014b140b73e7e7bc8a80","public:commit:1a47a108e8a3a84690ce151986e64ad9c46d5168","public:commit:1a5f721b4b15b783faf8f8cd540dad57c4c8962b","public:commit:1d45e10bfa5266ba0799130a9daa2c815a6c13e6","public:commit:38075fa193442b037653779c15da5b833186f933","public:commit:407f8dc1a6c03c4ef8dcaa6fa05e1ff2f62b1816","public:commit:488c9688300fc47890b747711c93d3a70cd3d56f","public:commit:491194b40a00c63f3695dc6287176f27e17dfbca","public:commit:4b978694f00dc5e50d97ca4eebda6cbfea8cc8bf","public:commit:52a2b71b89883e5d365b0c8838d1b0198c4f669a","public:commit:656d3da4eab900a56617c6c6d7d7555e3fdda010","public:commit:68f566436258abecc75db3f0521cdbef6909f79b","public:commit:6d88f1e65629d8008e3cfe06b219f4c703e445da","public:commit:70fe10660887abc218fc7166a66956e566747e8a","public:commit:791b86576c9feeb87c0d9310a31d24b61ecbbac0","public:commit:7b9a646e00b1c5f8fa3abe82e2bd1db330f426d8","public:commit:7d2c905346c2047f9e6f4834abecaf6964a7ee0a","public:commit:8c14033cd9bbc78224f166d62f929a28e9d62438","public:commit:8c7e4c21155b2f333a9ce47283f235f462f82f50","public:commit:a018919d80f8fe0849e8c78bb85f232ab193b482","public:commit:a04b6678f8b295b581e8160ba3f357db41ed14fb","public:commit:a18015c4df2ad9c3e8edfb91ae59c66b67c6e121","public:commit:a1ba0edc825db7bd5d5c74b77f9c0bb160109529","public:commit:a3de2f4f42acb12a0a2f1944b282dde66b1c0f65","public:commit:aa1c104bb5544c0701302e0e769832bc4e48971d","public:commit:adae43fc6a7b791f15196cf3acafb500362a1d1c","public:commit:b28c3fa7388b2a595cc9b3f040e4afdcac4c2ac6","public:commit:b8b2e1441a36c14ecb22614a1b42038820217c8e","public:commit:c3a4289ea1d09e5eb57d8424d175e1767d3c5259","public:commit:ca8236fe60c0d02466b767e41c82c5290e54a735","public:commit:cb526a474be544c874206beaeff471b46a9ea52f","public:commit:d6281a3b1c51f477bb0f97497173b82385c70754","public:commit:d736fb2a8b3a13b55586179b80a0fcbc8333ea82","public:commit:d96203599ba6b8ec995eef8f7febe85478688346","public:commit:dae929b39bcf4c544cbe6e5e1d972e06fc80092c","public:commit:de0aa81266af0d11032c87b4b50bf1c3703dfbae","public:commit:e51990bbf51fb600a31ef8df74a15f7fe790c09c","public:commit:e6e175894ee894536acc64bd6ada6d279100c4cc","public:commit:fd3aad5c9f814513bed63d93c6561c011f81cdd9"],"source_type":"public","date":"2024-05-24..2026-07-12","topics":["ffi","testing","build","api","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-papi-source-index"></a>
# EndstoneMC/papi source index {#endstonemc-papi-source-index}

Each entry links to a public commit. Read the linked case before applying a change elsewhere.

<a id="1-e6e175894ee894536acc64bd6ada6d279100c4cc"></a>
## 1. e6e175894ee894536acc64bd6ada6d279100c4cc {#1-e6e175894ee894536acc64bd6ada6d279100c4cc}

[Initial commit](https://github.com/EndstoneMC/papi/commit/e6e175894ee894536acc64bd6ada6d279100c4cc)

Disposition: duplicate_scaffold.

Exact whole-tree copy of cpp-example-plugin d6cb3c29539dc7e02a3cb1d340c12eefe97dc827, verified by tree hash. CMake/native plugin skeleton, listener/command examples, CI and MIT license are copied scaffolding; not a fresh PAPI design decision.

Case: PAPI01.

<a id="2-b28c3fa7388b2a595cc9b3f040e4afdcac4c2ac6"></a>
## 2. b28c3fa7388b2a595cc9b3f040e4afdcac4c2ac6 {#2-b28c3fa7388b2a595cc9b3f040e4afdcac4c2ac6}

[feat: add basic plugin codes](https://github.com/EndstoneMC/papi/commit/b28c3fa7388b2a595cc9b3f040e4afdcac4c2ac6)

Disposition: substantive.

Replaces example namespace, files, metadata and README with a PAPI project; introduces separate PlaceholderAPI and multiply inherited PlaceholderAPIPlugin, initially without functionality. Endstone pin moves v0.6.1 to v0.6.2.

Case: PAPI01.

<a id="3-a1ba0edc825db7bd5d5c74b77f9c0bb160109529"></a>
## 3. a1ba0edc825db7bd5d5c74b77f9c0bb160109529 {#3-a1ba0edc825db7bd5d5c74b77f9c0bb160109529}

[feat: add `PlaceholderAPI::setPlaceholder`](https://github.com/EndstoneMC/papi/commit/a1ba0edc825db7bd5d5c74b77f9c0bb160109529)

Disposition: substantive.

Introduces abstract setPlaceholder(Player const&, string_view), separates details/plugin.h from public header and implements a no-op return-text stub. Header describes placeholder syntax but implementation does not parse yet.

Case: PAPI01.

<a id="4-8c14033cd9bbc78224f166d62f929a28e9d62438"></a>
## 4. 8c14033cd9bbc78224f166d62f929a28e9d62438 {#4-8c14033cd9bbc78224f166d62f929a28e9d62438}

[feat: add command](https://github.com/EndstoneMC/papi/commit/8c14033cd9bbc78224f166d62f929a28e9d62438)

Disposition: substantive.

Registers placeholderapi command metadata with papi alias, but no command execution implementation is added at this stage.

Case: PAPI01.

<a id="5-656d3da4eab900a56617c6c6d7d7555e3fdda010"></a>
## 5. 656d3da4eab900a56617c6c6d7d7555e3fdda010 {#5-656d3da4eab900a56617c6c6d7d7555e3fdda010}

[feat: add endstone_papi interface library](https://github.com/EndstoneMC/papi/commit/656d3da4eab900a56617c6c6d7d7555e3fdda010)

Disposition: substantive.

Adds INTERFACE target and alias exporting headers, and returns early for subproject consumption so a dependent plugin need not build the implementation.

Case: PAPI01.

<a id="6-d96203599ba6b8ec995eef8f7febe85478688346"></a>
## 6. d96203599ba6b8ec995eef8f7febe85478688346 {#6-d96203599ba6b8ec995eef8f7febe85478688346}

[chore: update CMakeLists.txt](https://github.com/EndstoneMC/papi/commit/d96203599ba6b8ec995eef8f7febe85478688346)

Disposition: substantive.

Moves INTERFACE target creation into subproject branch, removes alias, adds opt-in C++ example directory. Build-consumer topology changes despite chore title.

Case: PAPI01.

<a id="7-a3de2f4f42acb12a0a2f1944b282dde66b1c0f65"></a>
## 7. a3de2f4f42acb12a0a2f1944b282dde66b1c0f65 {#7-a3de2f4f42acb12a0a2f1944b282dde66b1c0f65}

[feat: add C++ example plugin](https://github.com/EndstoneMC/papi/commit/a3de2f4f42acb12a0a2f1944b282dde66b1c0f65)

Disposition: substantive.

Adds C++ consumer that soft-depends on papi, disables itself if plugin unavailable, and casts Plugin* to PlaceholderAPI* before rewriting join text. At this commit interface is a sibling base, so the downcast arrangement is revised next.

Case: PAPI01.

<a id="8-7b9a646e00b1c5f8fa3abe82e2bd1db330f426d8"></a>
## 8. 7b9a646e00b1c5f8fa3abe82e2bd1db330f426d8 {#8-7b9a646e00b1c5f8fa3abe82e2bd1db330f426d8}

[refactor: make PlaceholderAPI derive from `endstone::Plugin`](https://github.com/EndstoneMC/papi/commit/7b9a646e00b1c5f8fa3abe82e2bd1db330f426d8)

Disposition: substantive.

Makes PlaceholderAPI derive from Plugin, with implementation deriving only from PlaceholderAPI. Also changes the stub to append player name. Inheritance makes the consumer downcast structurally available; this design is later replaced by services.

Case: PAPI01.

<a id="9-a04b6678f8b295b581e8160ba3f357db41ed14fb"></a>
## 9. a04b6678f8b295b581e8160ba3f357db41ed14fb {#9-a04b6678f8b295b581e8160ba3f357db41ed14fb}

[feat: add python binding](https://github.com/EndstoneMC/papi/commit/a04b6678f8b295b581e8160ba3f357db41ed14fb)

Disposition: substantive.

Adds nanobind extension, Python package and scikit-build metadata; build switches on SKBUILD and propagates endstone::endstone through the C++ interface target. Binding exposes abstract interface without constructor or Plugin base, so this is intermediate integration rather than complete Python API.

Case: PAPI01.

<a id="10-491194b40a00c63f3695dc6287176f27e17dfbca"></a>
## 10. 491194b40a00c63f3695dc6287176f27e17dfbca {#10-491194b40a00c63f3695dc6287176f27e17dfbca}

[feat: add python example plugin](https://github.com/EndstoneMC/papi/commit/491194b40a00c63f3695dc6287176f27e17dfbca)

Disposition: substantive.

Adds Python join-event example and wheel entry point; it calls PlaceholderAPI(self), a constructor supplied by the following wrapper revision. The soft dependency and missing-plugin disable path are explicit.

Case: PAPI01.

<a id="11-cb526a474be544c874206beaeff471b46a9ea52f"></a>
## 11. cb526a474be544c874206beaeff471b46a9ea52f {#11-cb526a474be544c874206beaeff471b46a9ea52f}

[feat: use pybind11 for python bindings](https://github.com/EndstoneMC/papi/commit/cb526a474be544c874206beaeff471b46a9ea52f)

Disposition: substantive.

Switches nanobind to pybind11 and introduces a native wrapper obtaining the PAPI plugin pointer from an owning plugin. Explicit comment says C++ downcasting is easier than Python and calls wrapper temporary. It throws if pointer was not initialized, but retains a raw pointer without unload invalidation.

Case: PAPI01.

<a id="12-aa1c104bb5544c0701302e0e769832bc4e48971d"></a>
## 12. aa1c104bb5544c0701302e0e769832bc4e48971d {#12-aa1c104bb5544c0701302e0e769832bc4e48971d}

[chore: add todo notes](https://github.com/EndstoneMC/papi/commit/aa1c104bb5544c0701302e0e769832bc4e48971d)

Disposition: planning.

Adds TODOs directed to daoge for registration/query/pattern APIs and explicitly proposes braces rather than percentage delimiters, referencing Java PlaceholderAPI as inspiration. Requested work is not implemented here.

Case: PAPI01.

<a id="13-d6281a3b1c51f477bb0f97497173b82385c70754"></a>
## 13. d6281a3b1c51f477bb0f97497173b82385c70754 {#13-d6281a3b1c51f477bb0f97497173b82385c70754}

[ci: update workflows](https://github.com/EndstoneMC/papi/commit/d6281a3b1c51f477bb0f97497173b82385c70754)

Disposition: substantive.

Refactors native CI into OS matrix and adds cp39-cp313 Linux/Windows wheel matrix. Linux custom manylinux image installs Clang/libc++16; native jobs use Clang15. These are build definitions, not evidence of successful runs.

Case: PAPI03.

<a id="14-791b86576c9feeb87c0d9310a31d24b61ecbbac0"></a>
## 14. 791b86576c9feeb87c0d9310a31d24b61ecbbac0 {#14-791b86576c9feeb87c0d9310a31d24b61ecbbac0}

[docs: update README.md](https://github.com/EndstoneMC/papi/commit/791b86576c9feeb87c0d9310a31d24b61ecbbac0)

Disposition: documentation.

README introduces C++ and Python integration examples, credits Spigot PAPI inspiration, and still describes native implementation plus Python wrapper topology. Later service changes supersede these examples.

Case: PAPI01.

<a id="15-0458d3d58298af12d39ad91ed0e0b88a52ba3a92"></a>
## 15. 0458d3d58298af12d39ad91ed0e0b88a52ba3a92 {#15-0458d3d58298af12d39ad91ed0e0b88a52ba3a92}

[refactor: mark `PlaceholderAPI::setPlaceholder` as const](https://github.com/EndstoneMC/papi/commit/0458d3d58298af12d39ad91ed0e0b88a52ba3a92)

Disposition: substantive.

Adds const and nodiscard to C++ translation contract and wrapper; removes temporary appended player name, restoring no-op stub. Not just qualifiers: observable stub output changes.

Case: PAPI01.

<a id="16-52a2b71b89883e5d365b0c8838d1b0198c4f669a"></a>
## 16. 52a2b71b89883e5d365b0c8838d1b0198c4f669a {#16-52a2b71b89883e5d365b0c8838d1b0198c4f669a}

[feat: `PlaceholderAPI` as a service](https://github.com/EndstoneMC/papi/commit/52a2b71b89883e5d365b0c8838d1b0198c4f669a)

Disposition: substantive.

Replaces plugin inheritance/raw-pointer wrapper with Service interface and pybind11 shared_ptr holder plus virtual trampoline. Deletes native implementation target; wheel becomes implementation carrier. Explicit comment defines the common C++/Python interop interface. Trampoline initially omits forwarded arguments.

Case: PAPI01.

<a id="17-407f8dc1a6c03c4ef8dcaa6fa05e1ff2f62b1816"></a>
## 17. 407f8dc1a6c03c4ef8dcaa6fa05e1ff2f62b1816 {#17-407f8dc1a6c03c4ef8dcaa6fa05e1ff2f62b1816}

[feat: update c++ example plugin](https://github.com/EndstoneMC/papi/commit/407f8dc1a6c03c4ef8dcaa6fa05e1ff2f62b1816)

Disposition: substantive.

C++ example now retains shared_ptr obtained by service-manager load. Example is opt-in. Checking plugin enabled still does not verify a non-null named service result.

Case: PAPI01.

<a id="18-adae43fc6a7b791f15196cf3acafb500362a1d1c"></a>
## 18. adae43fc6a7b791f15196cf3acafb500362a1d1c {#18-adae43fc6a7b791f15196cf3acafb500362a1d1c}

[feat: add dummy implementation of PlaceholderAPI](https://github.com/EndstoneMC/papi/commit/adae43fc6a7b791f15196cf3acafb500362a1d1c)

Disposition: substantive.

Adds Python concrete service, registers it at highest priority in on_load and unregisters plugin services on_disable; pybind11 imports/registers Service base. Demonstration uses str.format for two player fields, not general registry parsing.

Case: PAPI01.

<a id="19-ca8236fe60c0d02466b767e41c82c5290e54a735"></a>
## 19. ca8236fe60c0d02466b767e41c82c5290e54a735 {#19-ca8236fe60c0d02466b767e41c82c5290e54a735}

[feat: update python example plugin](https://github.com/EndstoneMC/papi/commit/ca8236fe60c0d02466b767e41c82c5290e54a735)

Disposition: substantive.

Python example now resolves named service and annotates optional stored API, matching the service redesign instead of constructing a wrapper.

Case: PAPI01.

<a id="20-38075fa193442b037653779c15da5b833186f933"></a>
## 20. 38075fa193442b037653779c15da5b833186f933 {#20-38075fa193442b037653779c15da5b833186f933}

[fix: add missing parameters to trampoline functions](https://github.com/EndstoneMC/papi/commit/38075fa193442b037653779c15da5b833186f933)

Disposition: substantive.

Fixes virtual trampoline by forwarding player and text to PYBIND11_OVERRIDE_PURE_NAME. This is a concrete cross-language call-shape repair with no test result attached.

Case: PAPI01.

<a id="21-d736fb2a8b3a13b55586179b80a0fcbc8333ea82"></a>
## 21. d736fb2a8b3a13b55586179b80a0fcbc8333ea82 {#21-d736fb2a8b3a13b55586179b80a0fcbc8333ea82}

[docs: update examples in README.md](https://github.com/EndstoneMC/papi/commit/d736fb2a8b3a13b55586179b80a0fcbc8333ea82)

Disposition: documentation.

README examples move both languages from plugin downcast/wrapper construction to named shared service lookup. This follows code changes, preserving consumer migration guidance.

Case: PAPI01.

<a id="22-e51990bbf51fb600a31ef8df74a15f7fe790c09c"></a>
## 22. e51990bbf51fb600a31ef8df74a15f7fe790c09c {#22-e51990bbf51fb600a31ef8df74a15f7fe790c09c}

[ci: update github action workflow](https://github.com/EndstoneMC/papi/commit/e51990bbf51fb600a31ef8df74a15f7fe790c09c)

Disposition: substantive.

Removes native-plugin CI job after implementation becomes a wheel; retains CPython wheel matrix and renames artifacts. No test invocation is added.

Case: PAPI03.

<a id="23-1a5f721b4b15b783faf8f8cd540dad57c4c8962b"></a>
## 23. 1a5f721b4b15b783faf8f8cd540dad57c4c8962b {#23-1a5f721b4b15b783faf8f8cd540dad57c4c8962b}

[feat: add headers to wheels](https://github.com/EndstoneMC/papi/commit/1a5f721b4b15b783faf8f8cd540dad57c4c8962b)

Disposition: substantive.

Installs public include directory inside endstone_papi wheel so C++ consumers can obtain headers with the distributed Python service.

Case: PAPI03.

<a id="24-6d88f1e65629d8008e3cfe06b219f4c703e445da"></a>
## 24. 6d88f1e65629d8008e3cfe06b219f4c703e445da {#24-6d88f1e65629d8008e3cfe06b219f4c703e445da}

[docs: update README.md](https://github.com/EndstoneMC/papi/commit/6d88f1e65629d8008e3cfe06b219f4c703e445da)

Disposition: documentation.

Updates tree documentation to distinguish Python package and C++ headers and removes obsolete native src entry.

Case: PAPI03.

<a id="25-1d45e10bfa5266ba0799130a9daa2c815a6c13e6"></a>
## 25. 1d45e10bfa5266ba0799130a9daa2c815a6c13e6 {#25-1d45e10bfa5266ba0799130a9daa2c815a6c13e6}

[feat: add stubs](https://github.com/EndstoneMC/papi/commit/1d45e10bfa5266ba0799130a9daa2c815a6c13e6)

Disposition: substantive.

Adds Python type stub for the service and changes concrete implementation import to relative. Stub documents old colon delimiter, later corrected by collaborator documentation.

Case: PAPI02.

<a id="26-b8b2e1441a36c14ecb22614a1b42038820217c8e"></a>
## 26. b8b2e1441a36c14ecb22614a1b42038820217c8e {#26-b8b2e1441a36c14ecb22614a1b42038820217c8e}

[style: format code](https://github.com/EndstoneMC/papi/commit/b8b2e1441a36c14ecb22614a1b42038820217c8e)

Disposition: mechanical.

Only quote style and blank-line formatting in .pyi. Diff read; no independent behavioral lesson.

Case: PAPI03.

<a id="27-02c31fd8863c1cce37aa3ff6e334e81097e48377"></a>
## 27. 02c31fd8863c1cce37aa3ff6e334e81097e48377 {#27-02c31fd8863c1cce37aa3ff6e334e81097e48377}

[docs: add screenshot to README.md](https://github.com/EndstoneMC/papi/commit/02c31fd8863c1cce37aa3ff6e334e81097e48377)

Disposition: documentation_with_binary.

README marks plugin unreleased and points to CI artifacts/header-in-wheel distribution. Added JPEG inspected: one join message with player name and GameMode.SURVIVAL. Screenshot is an illustrative author-supplied outcome, not reproduced runtime validation.

Case: PAPI03.

<a id="28-c3a4289ea1d09e5eb57d8424d175e1767d3c5259"></a>
## 28. c3a4289ea1d09e5eb57d8424d175e1767d3c5259 {#28-c3a4289ea1d09e5eb57d8424d175e1767d3c5259}

[style: code formatting](https://github.com/EndstoneMC/papi/commit/c3a4289ea1d09e5eb57d8424d175e1767d3c5259)

Disposition: mechanical.

Reformats collaborator parser, registry, command and examples plus C++ signatures. Four changed Python ASTs are equal before/after; C++ changes inspected as whitespace/layout only. New-looking registry bulk originated in daoge_cmd context commits, not this target formatting commit.

Case: PAPI02.

<a id="29-4b978694f00dc5e50d97ca4eebda6cbfea8cc8bf"></a>
## 29. 4b978694f00dc5e50d97ca4eebda6cbfea8cc8bf {#29-4b978694f00dc5e50d97ca4eebda6cbfea8cc8bf}

[refactor: update `registerPlaceholder` function signature](https://github.com/EndstoneMC/papi/commit/4b978694f00dc5e50d97ca4eebda6cbfea8cc8bf)

Disposition: substantive.

Renames translation to plural setPlaceholders across interface/implementation/binding/stub/C++ example and replaces optional-reference callback signature with named Processor alias (Player const&, string). Removes invalid std::optional<Player&> design, but Python example and command call sites are repaired in subsequent commits.

Case: PAPI02.

<a id="30-dae929b39bcf4c544cbe6e5e1d972e06fc80092c"></a>
## 30. dae929b39bcf4c544cbe6e5e1d972e06fc80092c {#30-dae929b39bcf4c544cbe6e5e1d972e06fc80092c}

[refactor: rename python binding to `_papi`](https://github.com/EndstoneMC/papi/commit/dae929b39bcf4c544cbe6e5e1d972e06fc80092c)

Disposition: substantive.

Renames native binding and stub to _papi, concrete module to papi; fixes import/class names and CMake paths, but native PYBIND11_MODULE name remains pypapi until 68f5664. Module rename is a multi-surface migration.

Case: PAPI02.

<a id="31-1a47a108e8a3a84690ce151986e64ad9c46d5168"></a>
## 31. 1a47a108e8a3a84690ce151986e64ad9c46d5168 {#31-1a47a108e8a3a84690ce151986e64ad9c46d5168}

[chore: lower Python version requirement to 3.9](https://github.com/EndstoneMC/papi/commit/1a47a108e8a3a84690ce151986e64ad9c46d5168)

Disposition: compatibility_claim.

Lowers requires-python from 3.10 to 3.9 without removing match syntax in plugin.py or runtime union annotations in chars_replacer.py. Metadata alone is not verified compatibility; static grammar check rejects plugin.py under Python 3.9.

Case: PAPI03.

<a id="32-070be6ee8ebc960c52361a981e556a17088c883a"></a>
## 32. 070be6ee8ebc960c52361a981e556a17088c883a {#32-070be6ee8ebc960c52361a981e556a17088c883a}

[chore: code clean up, add review notes](https://github.com/EndstoneMC/papi/commit/070be6ee8ebc960c52361a981e556a17088c883a)

Disposition: substantive.

Registry typing and parser lookup change to dictionary/get; pattern API returns regex source text. Adds explicit review questions about inconsistent delimiter reconstruction and namespace fallback. The later daoge fix resolves reconstruction to pipe.

Case: PAPI02.

<a id="33-044cb128d138e3d51422c128e1e3b1b64384e202"></a>
## 33. 044cb128d138e3d51422c128e1e3b1b64384e202 {#33-044cb128d138e3d51422c128e1e3b1b64384e202}

[feat: add `PlaceholderAPI::getPlaceholderPattern`](https://github.com/EndstoneMC/papi/commit/044cb128d138e3d51422c128e1e3b1b64384e202)

Disposition: substantive.

Exposes getPlaceholderPattern as string across C++ and trampoline; Python properties delegate to underscored override hooks for identifiers and pattern. Public regex representation is portable text rather than Python re.Pattern.

Case: PAPI02.

<a id="34-68f566436258abecc75db3f0521cdbef6909f79b"></a>
## 34. 68f566436258abecc75db3f0521cdbef6909f79b {#34-68f566436258abecc75db3f0521cdbef6909f79b}

[feat: update stubs](https://github.com/EndstoneMC/papi/commit/68f566436258abecc75db3f0521cdbef6909f79b)

Disposition: substantive.

Expands all service stubs and adds pybind11/functional.h for std::function callbacks. Corrects native module init name to _papi and plugin import to .papi, so feat-stubs title understates functional binding repairs.

Case: PAPI02.

<a id="35-a18015c4df2ad9c3e8edfb91ae59c66b67c6e121"></a>
## 35. a18015c4df2ad9c3e8edfb91ae59c66b67c6e121 {#35-a18015c4df2ad9c3e8edfb91ae59c66b67c6e121}

[feat: update python example plugin](https://github.com/EndstoneMC/papi/commit/a18015c4df2ad9c3e8edfb91ae59c66b67c6e121)

Disposition: substantive.

Python example imports future annotations and calls plural set_placeholders, completing one renamed consumer path.

Case: PAPI02.

<a id="36-de0aa81266af0d11032c87b4b50bf1c3703dfbae"></a>
## 36. de0aa81266af0d11032c87b4b50bf1c3703dfbae {#36-de0aa81266af0d11032c87b4b50bf1c3703dfbae}

[fix: pass plugin instance to constructor](https://github.com/EndstoneMC/papi/commit/de0aa81266af0d11032c87b4b50bf1c3703dfbae)

Disposition: substantive.

Passes owning plugin into PlaceholderAPI constructor, repairs command translation name and identifiers-property access. Concrete service needs plugin during default-provider registration.

Case: PAPI02.

<a id="37-70fe10660887abc218fc7166a66956e566747e8a"></a>
## 37. 70fe10660887abc218fc7166a66956e566747e8a {#37-70fe10660887abc218fc7166a66956e566747e8a}

[fix: correct command argument type](https://github.com/EndstoneMC/papi/commit/70fe10660887abc218fc7166a66956e566747e8a)

Disposition: substantive.

Changes command usage text to <text: message> and retains optional player afterward. Argument schema correction is incomplete until later ordering fix.

Case: PAPI02.

<a id="38-a018919d80f8fe0849e8c78bb85f232ab193b482"></a>
## 38. a018919d80f8fe0849e8c78bb85f232ab193b482 {#38-a018919d80f8fe0849e8c78bb85f232ab193b482}

[refactor: make player nullable](https://github.com/EndstoneMC/papi/commit/a018919d80f8fe0849e8c78bb85f232ab193b482)

Disposition: substantive.

Makes C++ Player input and Processor pointer nullable; Python service/stub annotate None. However C++ trampoline passes *player, contradicting nullable API. Namespace-fallback comments become explicit; no owner-unregister API for processors is added.

Case: PAPI02.

<a id="39-0cbb0b4b6b0e5963ea1f1179936a78cd489aa022"></a>
## 39. 0cbb0b4b6b0e5963ea1f1179936a78cd489aa022 {#39-0cbb0b4b6b0e5963ea1f1179936a78cd489aa022}

[Merge remote-tracking branch 'origin/main'](https://github.com/EndstoneMC/papi/commit/0cbb0b4b6b0e5963ea1f1179936a78cd489aa022)

Disposition: merge_integration.

Two-parent merge imports daoge_cmd pipe-delimiter reconstruction fix. Remerge diff shows conflict resolved by retaining target nullable signature and docstring in papi.py rather than collaborator docstring deletion. Both parent diffs and remerge inspected; parser fix remains collaborator-authored.

Case: PAPI02.

<a id="40-117d8780bb1603c446cd4141cec6e59d9391f037"></a>
## 40. 117d8780bb1603c446cd4141cec6e59d9391f037 {#40-117d8780bb1603c446cd4141cec6e59d9391f037}

[chore: change build backend to `scikit-build-core-conan`](https://github.com/EndstoneMC/papi/commit/117d8780bb1603c446cd4141cec6e59d9391f037)

Disposition: substantive.

Switches build backend to scikit-build-core-conan and adds dependency-free Conan CMakeDeps/CMakeToolchain layout. No explicit why beyond commit title.

Case: PAPI03.

<a id="41-8c7e4c21155b2f333a9ce47283f235f462f82f50"></a>
## 41. 8c7e4c21155b2f333a9ce47283f235f462f82f50 {#41-8c7e4c21155b2f333a9ce47283f235f462f82f50}

[feat: configure to use Ninja generator](https://github.com/EndstoneMC/papi/commit/8c7e4c21155b2f333a9ce47283f235f462f82f50)

Disposition: substantive.

Sets Conan toolchain generator to Ninja, aligning backend-generated toolchain with existing scikit-build Ninja selection. No build output is present.

Case: PAPI03.

<a id="42-7d2c905346c2047f9e6f4834abecaf6964a7ee0a"></a>
## 42. 7d2c905346c2047f9e6f4834abecaf6964a7ee0a {#42-7d2c905346c2047f9e6f4834abecaf6964a7ee0a}

[feat: update examples](https://github.com/EndstoneMC/papi/commit/7d2c905346c2047f9e6f4834abecaf6964a7ee0a)

Disposition: substantive.

Both examples and README check plugin presence rather than enabled state before named service load. This is consistent with provider registration during on_load, but no explicit rationale is recorded and service-null result remains unchecked.

Case: PAPI01.

<a id="43-fd3aad5c9f814513bed63d93c6561c011f81cdd9"></a>
## 43. fd3aad5c9f814513bed63d93c6561c011f81cdd9 {#43-fd3aad5c9f814513bed63d93c6561c011f81cdd9}

[Merge remote-tracking branch 'origin/main'](https://github.com/EndstoneMC/papi/commit/fd3aad5c9f814513bed63d93c6561c011f81cdd9)

Disposition: merge_integration.

Clean two-parent merge imports daoge_cmd usage-to-usages fix; second-parent diff carries target example presence-check changes. No additional conflict-resolution code and no blanket authorship credit.

Case: PAPI02.

<a id="44-0fdd2497e61ccfcffe67bf1292ef946fd659ce28"></a>
## 44. 0fdd2497e61ccfcffe67bf1292ef946fd659ce28 {#44-0fdd2497e61ccfcffe67bf1292ef946fd659ce28}

[feat: use simplified syntax for command usages](https://github.com/EndstoneMC/papi/commit/0fdd2497e61ccfcffe67bf1292ef946fd659ce28)

Disposition: substantive.

Simplifies parse/list usage strings from explicit enum notation to literal subcommands. Permissions list repair was collaborator context, not this target delta.

Case: PAPI02.

<a id="45-488c9688300fc47890b747711c93d3a70cd3d56f"></a>
## 45. 488c9688300fc47890b747711c93d3a70cd3d56f {#45-488c9688300fc47890b747711c93d3a70cd3d56f}

[fix: correct parameters of `parse` subcommand](https://github.com/EndstoneMC/papi/commit/488c9688300fc47890b747711c93d3a70cd3d56f)

Disposition: substantive.

Moves player before greedy message argument and requires exactly three parsed tokens. Adds me (player-only), --null and named-player branches; handled errors return True. Assertion guards arity, but special targets remain declared as player-typed and need parser validation.

Case: PAPI02.

<a id="46-173bf02fa2e5f7b0cba6014b140b73e7e7bc8a80"></a>
## 46. 173bf02fa2e5f7b0cba6014b140b73e7e7bc8a80 {#46-173bf02fa2e5f7b0cba6014b140b73e7e7bc8a80}

[feat: add support for endstone v0.7.0](https://github.com/EndstoneMC/papi/commit/173bf02fa2e5f7b0cba6014b140b73e7e7bc8a80)

Disposition: substantive.

Pins Endstone dependency from floating main to v0.7.0. This identifies intended API version, not evidence that wheels/tests ran successfully.

Case: PAPI03.
