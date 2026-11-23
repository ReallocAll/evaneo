<!-- retrieval: {"source_ids":["public:commit:0556ab1813b6fa0539c4d66ba5188989b10265e5","public:commit:0723795ea1ebae1fce3bf21584580803a54a3970","public:commit:1e1611fb56dd9eaf6ba2008e534838a5c9c8a1ff","public:commit:1f9d4241258d41de4b623bcd36871ce5804c7b6d","public:commit:21b92a1dc875e9f5adb96c7b3d1690c454d5d2fb","public:commit:451d1db1ad29c3aefe58a93dfe101bb78246fb5f","public:commit:4a02faae1ab46f8ed10baea398a954f195be43d4","public:commit:4c1da829e0b876fa7bfb3a0a6100ed5a00537ed6","public:commit:4efc9981882d961f1dd67aa576eb999aed70b3c7","public:commit:6448b62dec61a6ea15039ffb5e0fc98375044a9a","public:commit:9a9dd217f2430fe53f5e66da3ad308beaa2fcc13","public:commit:9f2b850ef49a755cd3e43d8c458a85063aa927df","public:commit:a898b20559169a05f9e4ae1037272a6c524317ea","public:commit:ab4cc56d457e55933792dfd446b966d353bd3c97","public:commit:b81ac29b729abd70288e2b98c2f8af104d89ae08","public:commit:c04708c5ab31bf6ccb0e394bcad0c647fd0681ce","public:commit:de7c11b291ee8a2778d2b1fd07163110f061604e","public:commit:f4b3df7cbfdb1ca19c4ed9cf8e2b8678a09248a3","public:commit:fc22331a0cd5e4449ec420f6230901d9171b76f5","public:commit:fee756e3c65d0ba1ec667fd6b68d6af4ddf4af6c"],"source_type":"public","date":"2024-05-04..2024-05-06","topics":["lifetime","ffi","testing","build","performance","api","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Spatial APIs expose three different kinds of lifetime {#spatial-apis-expose-three-different-kinds-of-lifetime}

## A value model grows around a native object model {#a-value-model-grows-around-a-native-object-model}

[880](#commit-880) adds a small arithmetic Vector and14 concrete GoogleTest cases. The tests cover coordinate access, arithmetic, norms and distances. They were fully read and are discovered by the root CMake tests glob; packaged wheel builds set BUILD_TESTING off. No tests were run. Generic vector arithmetic is distinct from the host Actor reconstruction that follows:883 replaces opaque storage with components and native fields, and later fixes revise pointer forms and offsets. A public coordinate result depends on both the value type and the correctness of that ABI access path.

The value API itself evolves. Vector moves into the intended namespace; Position/Location initially inherit privately and lack construction;888 makes inheritance public.885 changes squared arithmetic from pow to direct multiplication while being titled as documentation.894 changes the public/bound specialization to float and norm/distance results to T. Those details prevent a misleading 'documentation-only' or 'pure rename' disposition. Existing tests remain double-based and do not establish precision requirements for the new float API or integral-instantiation behavior.

Eigen is briefly introduced and then replaced by glm in883. The code shows which dependency is used for native matrix representation, but no explicit comparison, benchmark or rejected-library discussion is present. It would be unsupported to generalize this into a durable preference for one math library.

## The ownership chain must be read in causal order {#the-ownership-chain-must-be-read-in-causal-order}

The sequence is unusually informative because all120 assignment commits form an actual direct parent chain, not merely a date-sorted list.884 gives EndstoneLevel enable_shared_from_this while server storage is still unique_ptr; weak_from_this therefore has no shared owner to observe.888 calls shared_from_this before the owner is changed, introducing a static bad_weak_ptr path.889 experiments with optional weak references to distinguish never-set from expired.891 finally changes the server map and returned Level handles to shared_ptr, removes the enable_shared_from_this dependency, and reduces Position to ordinary weak references returning null when locking fails.

891 explicitly says the intent is preventing dangling pointers to unloaded levels. The achieved change has to be separated into three layers:

1. The server and callers can share ownership of the EndstoneLevel wrapper.
2. Position/Location do not prolong wrapper lifetime; their weak locks may return null.
3. EndstoneLevel still stores references to native Level and EndstoneServer. Keeping the wrapper alive does not, by itself, keep either referent alive or invalidate access after native unloading.

Final960 full-file context confirms that third-layer limitation. It is not proof of an observed unload crash, but it limits the stated lifetime guarantee. Python shared holders align with shared wrapper handles; explicit reference policy on a shared return is not an additional native-world lifetime protocol. This is a useful case for tracking ownership by object, not by the presence of a smart-pointer spelling.

## Domain semantics are corrected separately from ownership {#domain-semantics-are-corrected-separately-from-ownership}

892 changes location from eyes to the native Feet attachment, using the platform-specific native return convention.895 starts velocity as the native position delta.899 zeroes its vertical component when grounded, and900 exposes the ground flag. The new previous-position helper is not used to derive velocity and no per-second conversion is introduced. A consumer should not silently infer a conventional physics unit from the name alone.

901 adds water/lava flags throughout the layers, but the wrapper's lava method calls the water query. This survives through960 and has no matching test in the changed source. The native flag implementations are distinct, so the issue is specifically delegation, not evidence that the host represents lava as water. This bounded negative example complements the14 arithmetic tests: tests exist for pure values, while the newer native semantic mappings remain unverified here.

## Applicability and attribution {#applicability-and-attribution}

Retrieve this family for native-to-public coordinate semantics, language binding holder consistency, weak versus shared handles, incremental ABI mapping, and testing the last delegation layer. All assigned authorship is Vincent; the native engine and dependencies are separately authored systems. There is no reviewer rationale, runtime validation, benchmark or present-day correctness claim. Intermediate broken states are preserved as chronology, not used to infer personal carelessness or to erase the eventual wrapper-ownership repair.

## Per-commit source dispositions {#per-commit-source-dispositions}

<a id="commit-880"></a>
### 880 · feat: add basic `endstone::Vector` {#commit-880}

[Full commit 0556ab1813b6fa0539c4d66ba5188989b10265e5](https://github.com/EndstoneMC/endstone/commit/0556ab1813b6fa0539c4d66ba5188989b10265e5) · 2024-05-04T17:10:07Z · parent `95deab5285df0b51982bffee06d43646f9198b01` · feature_with_tests.

Adds a templated component-wise Vector with arithmetic, length and distance, initially outside the intended endstone namespace, plus14 GoogleTest cases for accessors/arithmetic/norm/distance. The same commit adds Boost and Eigen dependencies, though this Vector uses its own scalar arithmetic rather than those libraries. Tests are substantive source evidence but were not executed; they do not cover division by zero, integer overflow or native lifetime behavior.

Changed paths: `CMakeLists.txt`, `conanfile.py`, `include/endstone/util/vector.h`, `tests/util/test_vector.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-881"></a>
### 881 · feat: add dependencies to requires in conanfile.py {#commit-881}

[Full commit 4efc9981882d961f1dd67aa576eb999aed70b3c7](https://github.com/EndstoneMC/endstone/commit/4efc9981882d961f1dd67aa576eb999aed70b3c7) · 2024-05-04T17:19:24Z · parent `0556ab1813b6fa0539c4d66ba5188989b10265e5` · build_integration.

Updates Conan's core component requirements to reflect the newly linked dependencies. This is necessary package metadata alignment, not a separate library-selection rationale or proof that downstream linking was exercised.

Changed paths: `conanfile.py`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-882"></a>
### 882 · feat: add basic Position and Location {#commit-882}

[Full commit ab4cc56d457e55933792dfd446b966d353bd3c97](https://github.com/EndstoneMC/endstone/commit/ab4cc56d457e55933792dfd446b966d353bd3c97) · 2024-05-04T17:42:32Z · parent `4efc9981882d961f1dd67aa576eb999aed70b3c7` · incremental_api.

Moves Vector into namespace endstone and updates tests, then introduces Position and Location using weak references to Level/Dimension. At this point inheritance is private and constructors are absent, while pitch/yaw are not initialized; the types are an incomplete scaffold. Later888/889/891 revisions supply usable inheritance, construction and lifetime semantics, so the first weak_ptr appearance should not be presented as the finished design.

Changed paths: `include/endstone/level/location.h`, `include/endstone/level/position.h`, `include/endstone/util/vector.h`, `tests/util/test_vector.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-883"></a>
### 883 · feat: add members variables in `Actor` class {#commit-883}

[Full commit c04708c5ab31bf6ccb0e394bcad0c647fd0681ce](https://github.com/EndstoneMC/endstone/commit/c04708c5ab31bf6ccb0e394bcad0c647fd0681ce) · 2024-05-05T13:38:13Z · parent `ab4cc56d457e55933792dfd446b966d353bd3c97` · native_abi_mapping.

Replaces large opaque Actor storage with named fields and component pointers, including state-vector/AABB/rotation data, hashed strings, maps and matrix storage. Position access now follows the native StateVectorComponent pointer. Build dependencies switch Eigen to glm across CMake/Conan. The field comments and partial size checks express a reconstructed native layout, not proof of every offset or vtable slot; no explicit comparative library rationale or performance result accompanies the switch.

Changed paths: `CMakeLists.txt`, `conanfile.py`, `include/bedrock/forward.h`, `include/bedrock/hashed_string.h`, `include/bedrock/network/syncher/move_actor_absolute_data.h`, `include/bedrock/network/syncher/spatial_actor_network_data.h`, `include/bedrock/network/syncher/synched_actor_data_entity_wrapper.h`, `include/bedrock/world/actor/actor.h`, `include/bedrock/world/actor/components/built_in_actor_components.h`, `include/bedrock/world/math/vec2.h`, `include/bedrock/world/math/vec3.h`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-884"></a>
### 884 · feat: add `Actor::getLocation` and `Actor::getLevel` {#commit-884}

[Full commit 9a9dd217f2430fe53f5e66da3ad308beaa2fcc13](https://github.com/EndstoneMC/endstone/commit/9a9dd217f2430fe53f5e66da3ad308beaa2fcc13) · 2024-05-05T15:37:55Z · parent `c04708c5ab31bf6ccb0e394bcad0c647fd0681ce` · feature_then_corrected.

Adds Actor getLocation/getLevel through human/player wrappers, using component position/rotation and a Level wrapper lookup. EndstoneLevel gains enable_shared_from_this and Location receives a weak level reference via weak_from_this, but the server still owns levels through unique_ptr, so this does not yet create a valid shared ownership group. Dimension is absent.888's later shared_from_this call makes this mismatch more explicit until891 changes the owner.

Changed paths: `include/bedrock/world/actor/actor.h`, `include/bedrock/world/math/vec2.h`, `include/endstone/actor/actor.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/human.h`, `include/endstone/detail/level/level.h`, `include/endstone/detail/player.h`, `include/endstone/level/level.h`, `include/endstone/level/location.h`, `include/endstone/level/position.h`, `src/endstone_core/actor/actor.cpp`, `src/endstone_core/actor/human.cpp`, `src/endstone_core/player.cpp`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-885"></a>
### 885 · docs: add doxygen documentations for Vector, Position and Location {#commit-885}

[Full commit de7c11b291ee8a2778d2b1fd07163110f061604e](https://github.com/EndstoneMC/endstone/commit/de7c11b291ee8a2778d2b1fd07163110f061604e) · 2024-05-05T15:48:10Z · parent `9a9dd217f2430fe53f5e66da3ad308beaa2fcc13` · documentation_with_semantics.

Documents axes, yaw/pitch degrees and vector methods, adds zero construction, and replaces pow-based squared arithmetic with component multiplication. The arithmetic change affects intermediate types and overflow behavior, especially for integral instantiations; it is not merely Doxygen. constexpr declarations involving sqrt do not make every call a C++17 constant expression. Some setter return prose remains inconsistent with void signatures.

Changed paths: `include/endstone/level/location.h`, `include/endstone/level/position.h`, `include/endstone/util/vector.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-886"></a>
### 886 · feat: add python bindings for endstone::Vector<double> {#commit-886}

[Full commit 451d1db1ad29c3aefe58a93dfe101bb78246fb5f](https://github.com/EndstoneMC/endstone/commit/451d1db1ad29c3aefe58a93dfe101bb78246fb5f) · 2024-05-05T16:20:30Z · parent `de7c11b291ee8a2778d2b1fd07163110f061604e` · binding_feature.

Adds compound vector operations and scalar multiplication on either side, then binds Vector<double> operators, repr/str and stub exports to Python. In-place bindings cover vector operands rather than every scalar form. Python squared-length/distance names initially retain camelCase and are corrected in887. This is a coordinated native/binding API addition, without Python execution tests in this commit.

Changed paths: `include/endstone/util/vector.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/util.py`, `src/endstone_python/util.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-887"></a>
### 887 · refactor: fix function naming style {#commit-887}

[Full commit b81ac29b729abd70288e2b98c2f8af104d89ae08](https://github.com/EndstoneMC/endstone/commit/b81ac29b729abd70288e2b98c2f8af104d89ae08) · 2024-05-05T16:29:39Z · parent `451d1db1ad29c3aefe58a93dfe101bb78246fb5f` · api_naming_correction.

Renames the Python methods to length_squared and distance_squared and adds named arguments. The C++ method names remain unchanged. This is a small Python compatibility change and evidence of per-language naming adaptation, not a wholesale native API rename.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/util.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-888"></a>
### 888 · feat: add python bindings for `endstone::Position` {#commit-888}

[Full commit 4a02faae1ab46f8ed10baea398a954f195be43d4](https://github.com/EndstoneMC/endstone/commit/4a02faae1ab46f8ed10baea398a954f195be43d4) · 2024-05-05T16:51:47Z · parent `b81ac29b729abd70288e2b98c2f8af104d89ae08` · ownership_transition.

Makes Position/Location inheritance public, accepts shared_ptr construction while storing weak references, introduces Python shared holders for Level/Dimension, and adds Vector string conversion. Getters temporarily throw for expired weak references and return references; Actor now calls shared_from_this while server ownership remains unique_ptr, a static bad_weak_ptr path corrected in891. This intermediate commit must not be credited with the final safe ownership protocol.

Changed paths: `include/endstone/level/location.h`, `include/endstone/level/position.h`, `include/endstone/util/vector.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/level.py`, `src/endstone_core/actor/actor.cpp`, `src/endstone_python/level.cpp`, `src/endstone_python/util.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-889"></a>
### 889 · feat: add python bindings for `endstone::Location` {#commit-889}

[Full commit 1f9d4241258d41de4b623bcd36871ce5804c7b6d](https://github.com/EndstoneMC/endstone/commit/1f9d4241258d41de4b623bcd36871ce5804c7b6d) · 2024-05-05T17:09:08Z · parent `4a02faae1ab46f8ed10baea398a954f195be43d4` · ownership_transition.

Uses optional weak references to distinguish an unassigned null level/dimension from an expired owner, returns shared_ptr from getters and exposes Location/yaw/pitch in Python. The setter's engaged weak pointer after null assignment differs from the constructor's absent optional state, so the distinction is not uniform. Actor explicitly passes no Dimension.891 simplifies this exceptional state model to nullable weak locking.

Changed paths: `include/endstone/level/location.h`, `include/endstone/level/position.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/level.py`, `src/endstone_core/actor/actor.cpp`, `src/endstone_python/level.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-890"></a>
### 890 · feat: add python bindings for `Actor::getLocation` and `Actor::getLevel` {#commit-890}

[Full commit 0723795ea1ebae1fce3bf21584580803a54a3970](https://github.com/EndstoneMC/endstone/commit/0723795ea1ebae1fce3bf21584580803a54a3970) · 2024-05-05T17:15:31Z · parent `1f9d4241258d41de4b623bcd36871ce5804c7b6d` · binding.

Adds Actor.location and Actor.level bindings and stubs, preregistering Actor before initializing level-related types to resolve cross-references. It exposes the current transition state from888/889; registration ordering does not repair the unique/shared ownership mismatch. The level property initially lacks the later explicit return-policy annotation.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/actor.cpp`, `src/endstone_python/endstone_python.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-891"></a>
### 891 · feat: use std::shared_ptr instead of raw pointers to prevent dangling pointers of unloaded levels {#commit-891}

[Full commit f4b3df7cbfdb1ca19c4ed9cf8e2b8678a09248a3](https://github.com/EndstoneMC/endstone/commit/f4b3df7cbfdb1ca19c4ed9cf8e2b8678a09248a3) · 2024-05-05T21:39:04Z · parent `0723795ea1ebae1fce3bf21584580803a54a3970` · corrective_ownership.

Explicitly claims prevention of dangling pointers to unloaded levels and changes server storage plus getLevels/getLevel and actor-level APIs to shared_ptr. Position keeps ordinary weak references whose lock returns null for both unset and expired owners, removing the optional/exception design; enable_shared_from_this is no longer needed. Mocks and weather consumers are adapted. This repairs the wrapper ownership group, but EndstoneLevel still borrows native Level and server references, so retaining a wrapper does not prove native-world validity. Event/scheduler exception logging also drops from critical to error.

Changed paths: `include/endstone/actor/actor.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/human.h`, `include/endstone/detail/level/level.h`, `include/endstone/detail/player.h`, `include/endstone/detail/server.h`, `include/endstone/level/position.h`, `include/endstone/server.h`, `src/endstone_core/actor/actor.cpp`, `src/endstone_core/actor/human.cpp`, `src/endstone_core/player.cpp`, `src/endstone_core/plugin/plugin_manager.cpp`, `src/endstone_core/scheduler/scheduler.cpp`, `src/endstone_core/server.cpp`, `src/endstone_runtime/bedrock/world/level/event/gameplay_handler.cpp`, `tests/plugin/test_cpp_plugin_loader.cpp`, `tests/scheduler/test_scheduler.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-892"></a>
### 892 · fix: `Player::getLocation` now returns the location of feet instead of eyes {#commit-892}

[Full commit fc22331a0cd5e4449ec420f6230901d9171b76f5](https://github.com/EndstoneMC/endstone/commit/fc22331a0cd5e4449ec420f6230901d9171b76f5) · 2024-05-05T22:47:28Z · parent `f4b3df7cbfdb1ca19c4ed9cf8e2b8678a09248a3` · semantic_coordinate_fix.

Changes reported locations from the actor's eye position to the native Feet attachment position, explicitly fixing Player::getLocation semantics. The hook has platform-specific return conventions; StateVector previous/delta field order is adjusted and an offsets component is added. This is a domain-coordinate and ABI correction, not a numeric precision change. No live-coordinate comparison was performed by this review.

Changed paths: `include/bedrock/world/actor/actor.h`, `include/bedrock/world/actor/actor_location.h`, `include/bedrock/world/actor/components/built_in_actor_components.h`, `include/bedrock/world/actor/components/offsets_component.h`, `src/endstone_core/actor/actor.cpp`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-893"></a>
### 893 · fix: members in class `Actor` {#commit-893}

[Full commit 9f2b850ef49a755cd3e43d8c458a85063aa927df](https://github.com/EndstoneMC/endstone/commit/9f2b850ef49a755cd3e43d8c458a85063aa927df) · 2024-05-06T11:23:17Z · parent `fc22331a0cd5e4449ec420f6230901d9171b76f5` · native_abi_correction.

Revises Actor reconstruction again: synched data uses WeakRef<EntityContext>, spatial data becomes a unique_ptr with accompanying padding, and renderer/category/offset fields are clarified. A prior size assertion is commented out. The changes show iterative native-layout discovery; they do not establish a validated universal actor layout across server versions.

Changed paths: `include/bedrock/forward.h`, `include/bedrock/network/syncher/synched_actor_data_entity_wrapper.h`, `include/bedrock/world/actor/actor.h`, `include/bedrock/world/actor/components/offsets_component.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-894"></a>
### 894 · refactor: use Vector<float> instead of Vector<double> for Locations {#commit-894}

[Full commit 21b92a1dc875e9f5adb96c7b3d1690c454d5d2fb](https://github.com/EndstoneMC/endstone/commit/21b92a1dc875e9f5adb96c7b3d1690c454d5d2fb) · 2024-05-06T16:44:07Z · parent `9f2b850ef49a755cd3e43d8c458a85063aa927df` · precision_revision.

Switches public Position/Location and the bound Vector specialization from double to float, while Vector length/distance now return T. Alignment with native float coordinates is a plausible reading of adjacent code, not an explicit stated reason. Returning T also changes generic integral instantiations to truncated results. Existing double-oriented vector tests are not expanded into precision or host-coordinate tests.

Changed paths: `include/endstone/level/location.h`, `include/endstone/level/position.h`, `include/endstone/util/vector.h`, `src/endstone_python/level.cpp`, `src/endstone_python/util.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-895"></a>
### 895 · feat: add Actor::getVelocity {#commit-895}

[Full commit a898b20559169a05f9e4ae1037272a6c524317ea](https://github.com/EndstoneMC/endstone/commit/a898b20559169a05f9e4ae1037272a6c524317ea) · 2024-05-06T21:22:27Z · parent `21b92a1dc875e9f5adb96c7b3d1690c454d5d2fb` · api_feature.

Adds velocity by reading the native state-vector position_delta and delegates through Actor/HumanActor/Player wrappers. It does not derive velocity by subtracting the newly exposed positions or define a seconds-based unit.899 subsequently suppresses the vertical component while grounded, indicating the initial raw field is not treated as the complete public semantic contract.

Changed paths: `include/bedrock/world/actor/actor.h`, `include/endstone/actor/actor.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/human.h`, `include/endstone/detail/player.h`, `src/endstone_core/actor/actor.cpp`, `src/endstone_core/actor/human.cpp`, `src/endstone_core/player.cpp`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-898"></a>
### 898 · feat: add python bindings for `Actor::getVelocity` {#commit-898}

[Full commit 4c1da829e0b876fa7bfb3a0a6100ed5a00537ed6](https://github.com/EndstoneMC/endstone/commit/4c1da829e0b876fa7bfb3a0a6100ed5a00537ed6) · 2024-05-06T22:01:24Z · parent `8fd0fd5c92f0f11e0c0fc43a15f424c14a45559a` · binding.

Adds the Python velocity property and stub, delegating to the native wrapper introduced in895. It adds no unit conversion or independent velocity calculation and no execution test.

Changed paths: `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_python/actor.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-899"></a>
### 899 · feat: improve `Actor::getVelocity` when actor is on ground {#commit-899}

[Full commit 6448b62dec61a6ea15039ffb5e0fc98375044a9a](https://github.com/EndstoneMC/endstone/commit/6448b62dec61a6ea15039ffb5e0fc98375044a9a) · 2024-05-06T23:20:36Z · parent `4c1da829e0b876fa7bfb3a0a6100ed5a00537ed6` · semantic_velocity_fix.

Zeros the vertical velocity component when the ECS OnGround flag is set. Adds WasOnGround access, previous-position access and native Vec3 arithmetic, but those helpers are not used to calculate this public velocity. The public result remains the native delta with a grounded correction; no per-second scaling or general physics guarantee is established.

Changed paths: `CHANGELOG.md`, `include/bedrock/world/actor/actor.h`, `include/bedrock/world/actor/actor_collision.h`, `include/bedrock/world/actor/components/flag_component.h`, `include/bedrock/world/math/vec3.h`, `src/endstone_core/actor/actor.cpp`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`, `src/endstone_runtime/bedrock/world/actor/actor_collision.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-900"></a>
### 900 · feat: add `Actor::isOnGround` and its python bindings {#commit-900}

[Full commit fee756e3c65d0ba1ec667fd6b68d6af4ddf4af6c](https://github.com/EndstoneMC/endstone/commit/fee756e3c65d0ba1ec667fd6b68d6af4ddf4af6c) · 2024-05-06T23:26:26Z · parent `6448b62dec61a6ea15039ffb5e0fc98375044a9a` · api_feature.

Exposes isOnGround and its Python property through all wrapper layers, and adds explicit reference policy to the level property whose C++ return is now shared_ptr. This policy annotation does not supply a separate native-level lifetime mechanism. No grounded-transition test accompanies the new API.

Changed paths: `include/endstone/actor/actor.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/human.h`, `include/endstone/detail/player.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_core/actor/actor.cpp`, `src/endstone_core/actor/human.cpp`, `src/endstone_core/player.cpp`, `src/endstone_python/actor.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-901"></a>
### 901 · feat: add `Actor::isInWater`, `Actor::isInLava` and their python bindings {#commit-901}

[Full commit 1e1611fb56dd9eaf6ba2008e534838a5c9c8a1ff](https://github.com/EndstoneMC/endstone/commit/1e1611fb56dd9eaf6ba2008e534838a5c9c8a1ff) · 2024-05-06T23:44:52Z · parent `fee756e3c65d0ba1ec667fd6b68d6af4ddf4af6c` · feature_with_negative_example.

Adds native water/lava ECS flag queries, wrapper methods and Python properties. The native queries are distinct, but EndstoneActor::isInLava delegates to isInWater, and final960 context confirms that wrong delegation persists. Python prose also says java instead of lava. This is a bounded copy/delegation counterexample: symmetry across many wrappers can spread a single wrong method call, and no corresponding behavior test was added.

Changed paths: `include/bedrock/world/actor/actor.h`, `include/bedrock/world/actor/actor_environment.h`, `include/bedrock/world/actor/components/flag_component.h`, `include/endstone/actor/actor.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/human.h`, `include/endstone/detail/player.h`, `python/src/endstone/_internal/endstone_python.pyi`, `src/endstone_core/actor/actor.cpp`, `src/endstone_core/actor/human.cpp`, `src/endstone_core/player.cpp`, `src/endstone_python/actor.cpp`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`, `src/endstone_runtime/bedrock/world/actor/actor_environment.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.
