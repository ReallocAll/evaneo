<!-- retrieval: {"source_ids":["public:commit:0458d3d58298af12d39ad91ed0e0b88a52ba3a92","public:commit:38075fa193442b037653779c15da5b833186f933","public:commit:407f8dc1a6c03c4ef8dcaa6fa05e1ff2f62b1816","public:commit:491194b40a00c63f3695dc6287176f27e17dfbca","public:commit:52a2b71b89883e5d365b0c8838d1b0198c4f669a","public:commit:656d3da4eab900a56617c6c6d7d7555e3fdda010","public:commit:791b86576c9feeb87c0d9310a31d24b61ecbbac0","public:commit:7b9a646e00b1c5f8fa3abe82e2bd1db330f426d8","public:commit:7d2c905346c2047f9e6f4834abecaf6964a7ee0a","public:commit:8c14033cd9bbc78224f166d62f929a28e9d62438","public:commit:a04b6678f8b295b581e8160ba3f357db41ed14fb","public:commit:a1ba0edc825db7bd5d5c74b77f9c0bb160109529","public:commit:a3de2f4f42acb12a0a2f1944b282dde66b1c0f65","public:commit:aa1c104bb5544c0701302e0e769832bc4e48971d","public:commit:adae43fc6a7b791f15196cf3acafb500362a1d1c","public:commit:b28c3fa7388b2a595cc9b3f040e4afdcac4c2ac6","public:commit:ca8236fe60c0d02466b767e41c82c5290e54a735","public:commit:cb526a474be544c874206beaeff471b46a9ea52f","public:commit:d736fb2a8b3a13b55586179b80a0fcbc8333ea82","public:commit:d96203599ba6b8ec995eef8f7febe85478688346","public:commit:e6e175894ee894536acc64bd6ada6d279100c4cc"],"source_type":"public","date":"2025-03-12..2025-03-16","topics":["lifetime","ffi","testing","build","api","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="papi01-replace-plugin-downcasts-with-a-shared-c-python-service"></a>
# Replace plugin downcasts with a shared C++/Python service {#papi01-replace-plugin-downcasts-with-a-shared-c-python-service}

## Problem, scope and attribution {#problem-scope-and-attribution}

The March 2025 PAPI work aims to let C++ and Python Endstone plugins replace placeholders through the same provider. This case concerns architectural evolution; intermediate revisions were not all runnable. The root `e6e1758` is an exact tree copy of cpp-example-plugin `d6cb3c29539dc7e02a3cb1d340c12eefe97dc827`, so the example framework is shared starting context rather than a new PAPI design.

Vincent authored the interface, binding, consumer and build evolution. daoge_cmd supplied the later real parser, registry, default processors and command implementation; those are separate context, analyzed in PAPI02. Comments credit the Java PlaceholderAPI project as inspiration.

## Initial alternatives and concrete revisions {#initial-alternatives-and-concrete-revisions}

1. `b28c3fa7` establishes an empty public interface and `Plugin + PlaceholderAPI` multiple-inheritance implementation. `a1ba0edc` adds a pure virtual single-text translator and moves implementation details out of the public header. The stub merely returns the input. The documented syntax therefore precedes a working parser.
2. `656d3da4` exports a CMake INTERFACE library and stops full builds when used as a subproject. `d9620359` confines that target to dependency consumption and adds opt-in examples. This separates the consumer header dependency from the implementation artifact.
3. `a3de2f4f` makes a C++ join-event consumer fetch the plugin and cast it to the interface. With sibling bases this relationship is awkward; `7b9a646e` makes the public interface itself derive from `Plugin`, providing a direct downcast relationship. The commit also appends the player's name in a demonstration stub, later removed by `0458d3d5`.
4. `a04b6678` tries nanobind and a wheel. `491194b4` adds a Python consumer calling `PlaceholderAPI(self)` before the matching constructor exists. `cb526a47` replaces nanobind with pybind11 and a native wrapper that performs the downcast. Its comment explicitly explains that C++ downcasting is easier than doing it from Python and that this wrapper should remain until a cleaner approach is found. The wrapper initializes a raw PAPI pointer only if enabled and throws when unset; it does not track later provider disable/unload.
5. `52a2b71b` replaces plugin inheritance with `endstone::Service`, a virtual C++ interface, pybind11 trampoline and shared-pointer holder. It removes the native plugin implementation and builds the Python extension as the principal artifact. The comment explicitly says the interface is shared so C++ and Python know how to interoperate. This is the demonstrated alternative to the temporary raw-pointer wrapper.
6. `407f8dc1`, `adae43fc`, and `ca8236fe` migrate consumers to named service lookup, implement the provider in Python, register it during `on_load` at highest priority, and unregister the provider's services in `on_disable`. `38075fa1` fixes omitted `player, text` arguments in the trampoline macro. README examples follow in `d736fb2a`.
7. `7d2c9053` changes consumer checks from “plugin enabled” to “plugin exists.” Since service registration is in `on_load`, the change is consistent with discovery before enable; that explanation is inference, not a stated rationale.

## Contract and lifetime analysis {#contract-and-lifetime-analysis}

The final public C++ interface remains separately consumable. A C++ client retains `shared_ptr<PlaceholderAPI>`; Python implementation inherits the native interface, and the binding imports Endstone modules before registering the base type. This avoids making every consumer know the concrete Python implementation.

Shared ownership is not a complete availability or type-safety policy. The captured Endstone v0.7.0 ServiceManager contract says lookup may return null and selects the highest-priority provider. Its templated `load<T>` uses `static_pointer_cast`. Both examples first check plugin presence and then dereference the loaded service without an explicit null check. Presence alone does not establish that a named provider was registered successfully or has the requested interface. This is a static integration risk, not a reproduced failure.

Provider unregister on disable removes discovery entries but does not automatically prove all retained client references have become unusable. Likewise the Python registry later retains callbacks without an owner-specific removal operation. Service lifetime, Python override lifetime and plugin lifetime should be tested together instead of treating `shared_ptr` as an unload protocol. These are review questions, not evidence the target solved them.

## Evidence, outcomes and limits {#evidence-outcomes-and-limits}

The source shows a completed architectural migration and a specific argument-forwarding fix. The screenshot added in `02c31fd8` visibly shows a join message containing a name and `GameMode.SURVIVAL`; it is author-supplied illustrative evidence only. No runtime, build or wheel import was executed in this review. The selected history has no automated cross-language behavior tests. No performance superiority of services over wrappers was measured.

## Scoped use {#scoped-use}

Retrieve this case when exposing an extensible Python implementation to native plugin clients, designing header-only consumer dependencies, or reviewing plugin-unload lifetime. Preserve the explicit rationale for a shared interface and the temporary nature of the wrapper. Do not generalize it into “always use services” or “raw pointers are never appropriate.” Validate provider absence, wrong interface name, registration order, cross-language calls with real arguments, disable/reload with a client retaining the service, and interpreter shutdown before recommending the design for production.

## Source navigation and provenance {#local-navigation-and-provenance}

- [Per-commit source index](../repositories/papi-source-index.md) links the public revisions; the local patch text is unavailable.
- Key public sources: https://github.com/EndstoneMC/papi/commit/cb526a474be544c874206beaeff471b46a9ea52f and https://github.com/EndstoneMC/papi/commit/52a2b71b89883e5d365b0c8838d1b0198c4f669a .
