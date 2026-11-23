<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:510"],"source_type":"public","date":"2026-08-22","topics":["lifetime","concurrency","ffi","testing","build","api","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-510-feat-add-public-c-metrics-service-api"></a>
# EndstoneMC/endstone #510: feat: add public C++ metrics service API {#endstonemc-endstone-510-feat-add-public-c-metrics-service-api}

Source: https://github.com/EndstoneMC/endstone/pull/510

## Evidence and attribution {#evidence-and-attribution}

Primary author: ReallocAll. Created 2026-08-22T04:00:58Z; recorded state closed; merged True.

## Metrics lifetime was revised during review {#metrics-lifetime-was-revised-during-review}
ReallocAll initially offers a public C++ MetricsService plus registration handles owning charts, callback shutdown, seven chart types and custom charts, reusing Python's transport. Callback execution is primary-thread/GIL-aware; failures are isolated; public headers should not leak implementation types. CI wheel coverage across Windows/Linux and CPython3.11–3.14 is reported.
Wu changes ownership: a local Metrics handle can die at the end of onEnable while the server retains registration, like scheduled tasks; there is one reporter per service ID. Native plugin unload must synchronously discard chart callbacks before loaders unload their modules, rather than waiting for bStats's roughly30-minute collection interval. Python's caller-facing API remains familiar while chart implementations move to C++ and custom charts remain subclassable. The initial body's ownership model must not be presented as the final accepted API.

## Direct patch findings {#direct-patch-findings}

Final diff exposes nlohmann_json shapes publicly, vendors pybind11_json d0bf434 separately credited to MartinRenou/pybind (stated reason: Conan recipe pins older conflicting dependency versions), and ports seven bStats chart filters into C++. SimpleBar keeps zero, line/advancedpie omit zero, drilldown omits empty groups, advancedbar omits empty vectors. JSON caster handles recursive structures with cycle detection, signed/unsigned integer fit and base64 bytes; its stale comment says Any while stubgen now rewrites JsonValue/Object/Array. ModalForm callback changes from serialized string to parsed array; spawn_particle argument name/type changes to JsonObject and dumps only at wire boundary. These are explicit breaking changes beyond metrics.

Server caches one shared backend per service ID globally, so duplicate IDs from different plugins reuse the first plugin association. A short-lived Metrics handle can safely disappear while server owns backend. C++ addCustomChart acquires GIL and transfers chart to Python; shutdown calls Python shutdown then drops its object. Reload merely clears server's shared-handle map before plugin clear; a retained Metrics/NotNull keeps backend alive, so unconditional callback retirement is not established. Exact-head NotNull owns shared_ptr. Exact-head endstone/metrics/_base.py and __init__.py were fully inspected: shutdown cancels only its periodic future, does not explicitly clear charts or track in-flight send futures; callbacks/log closures can retain reporter. Most importantly, initial submission uses submit_task (plugin scheduler), but recurring while-loop directly calls _submit_data from the async coroutine, violating the new primary-thread callback promise after the first submission. Build success cannot validate that delayed path.

Added Python tests cover16 chart filter cases, IDs/emptyIDs, callback exceptions, custom subclass output, envelope/filtering/error isolation and plugin-description version retrieval, with transport monkeypatched. They do not test delayed thread affinity, retained handles during reload, duplicate service-ID ownership, actual native-module unload, JSON/form/particle integration or network submission. Existing C++ mock only gains createMetrics declaration. Preserve reviewer lifecycle goal as a requirement, not proof final patch meets it.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (85793 characters; SHA-256 a6dbeae762735ac16928a79bcd3d8b6bf4795af1c18d2c5036177c1104c89edc), head 230e808f087804548aa3970dacfdd04afe655407. Additional exact-head context:24 core/inventory/item_stack.cpp setters;102 endstone/metrics/_base.py, __init__.py and util/pointers.h shared ownership. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/510
- https://github.com/EndstoneMC/endstone/pull/510#issuecomment-5383152554
