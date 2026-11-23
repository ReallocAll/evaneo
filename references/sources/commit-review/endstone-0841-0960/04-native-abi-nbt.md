<!-- retrieval: {"source_ids":["public:commit:113e7b589c2b802e1860dfbadcc128329aeb3ea1","public:commit:12bc154566f005b221fa579b1e33f16685a18c25","public:commit:1a1646de507519e1fe29082b426f480c176804b9","public:commit:2468f9752baec492cc05c017329fca9018b924d6","public:commit:331748e2746b4559b517234900fd85f5c45c459f","public:commit:48a540950a3e735eac466d18249b5d1b4b7cc92a","public:commit:4a035a7b1d70a8c61077ce20c4a795ca7a11b994","public:commit:60c3c9aa345d72a2c409e34de54c80478edd08a5","public:commit:6b19e05c6e703b238017380e42fedd79d92197e5","public:commit:71044e071437f2a0f4c1c63aca2555a65a4b4440","public:commit:78097708d97c64cb6c21393e71fbf65074410d17","public:commit:8097f798a2aa694a8d8723a5ee56825db7e4d2fb","public:commit:88a34a9af89b2c372ae03cc08c564d5967fb1a0b","public:commit:8d8f6ca3d9ce3f6916692abf0722e319790a65b2","public:commit:8e5ac0e5ca9767e3281c12f6846660fff70420cb","public:commit:8fd7d0d8f3c289f0169a276d7209e47b35b35606","public:commit:ac82785cff63c721feb6fcbdb7c269de9ac0cb90","public:commit:dd18094d47ab5a712074992aad394826c9df9cfc","public:commit:fd775b9a49ee96eaa8efce4c01326744ec9b9629","public:commit:ff2f6713f35b79ae25b9ff981e44969c51f845de"],"source_type":"public","date":"2024-05-07..2024-05-18","topics":["lifetime","ffi","testing","api","diagnosis","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native declarations become host-facing views rather than a local NBT implementation {#native-declarations-become-host-facing-views-rather-than-a-local-nbt-implementation}

## Representation work is substantive but not complete functionality {#representation-work-is-substantive-but-not-complete-functionality}

ItemStackBase, ItemStack, MaterialType, Tick and network-ID declarations in903–905 describe native storage and virtual interfaces. They are necessary groundwork for later wrappers, but they do not yet deliver a user-facing inventory or serializer.906 centralizes platform-specific total-size assertions and deliberately gates them on NDEBUG. This catches selected release-layout mismatches while leaving debug builds unchecked by that macro. A correct total size alone cannot establish field offsets, vtable order, construction rules or native ownership.

The NBT chain begins with type IDs, abstract I/O and an expected-style Result representation. Expected-lite is introduced as a dependency, while ErrorInfo and its frame/context types arrive in later commits. This is mapping a host ABI, not sufficient evidence of a general preference to replace exceptions with expected everywhere. Some declarations are temporarily incomplete between commits; the final source imports the missing error representation.

## Two observed approaches and a substantial reversal {#two-observed-approaches-and-a-substantial-reversal}

917 creates the tag hierarchy and variant-based compound representation, with abstract operations and storage layouts.918 adds local printing behavior.920 implements EndTag, including an empty copy result, and923 supplies base type-ID equality.925 adds mostly empty translation units plus meaningful include-cycle repairs. These are not13 independent implementations merely because many files were added.

[928](#commit-928) is the decision-changing patch. Its title mentions put methods, but the full diff removes the local Tag/EndTag/PrintStream implementations and empty source files, changes the variant inheritance structure, deletes default constructors and supplies throwing virtual stubs instead of pure virtual declarations. The five CompoundTag mutation methods call through native hooks. The observed endpoint is best explained as a C++ representation used to view/call host objects rather than an independently complete NBT implementation. This explanation is an inference from the code; no accompanying discussion explicitly states the entire tradeoff.

That direction avoids claiming local implementations for all native behavior, but it adds constraints. A host object must have the right layout and dispatch; default construction is intentionally unavailable for central types; copying a representation is not automatically proof of safe host virtual behavior. Final960 Tag/CompoundTag/CompoundTagVariant files were read in full. The deleted EndTag copy implementation is not credited as a tested fix: it disappears with the approach that contained it.

## Small repairs preserve the chronology {#small-repairs-preserve-the-chronology}

926 changes reconstructed native reference members to pointers to address initialization warnings;927 repairs the getter to dereference the new pointer.924 moves LogLevel into its native namespace.957 makes CompoundTag declarations available where complete types are needed. These source-level integration repairs are worth retaining but do not each require an invented architectural principle. They also show why a commit title such as 'missing headers' cannot be assumed to describe every semantic change elsewhere in this unit.

## What can be reused {#what-can-be-reused}

Use this case when deciding how much of an external native object to implement locally, how to distinguish an ABI view from an owning domain object, and how to document which invariants size checks actually cover. No NBT read/write round-trip, malformed-data test, native inventory exercise or host invocation was run or added in these patches. Boilerplate and exact relocations are accounted for in per-SHA hashes. All changed declarations are attributed to Vincent's commits; Bedrock, expected-lite and standard-library algorithms are not attributed to him. No external review or alternative library discussion is inferred.

## Per-commit source dispositions {#per-commit-source-dispositions}

<a id="commit-903"></a>
### 903 · feat: add ItemStackBase {#commit-903}

[Full commit 48a540950a3e735eac466d18249b5d1b4b7cc92a](https://github.com/EndstoneMC/endstone/commit/48a540950a3e735eac466d18249b5d1b4b7cc92a) · 2024-05-07T22:48:28Z · parent `d96b05deed9bf0b1d73cfafe09d5f1c4e2cb368f` · native_abi_scaffold.

Adds native ItemStackBase layout and virtual operations, weak-pointer representation, Tick storage and an initial ItemStack declaration. Counts, raw Block pointer and unique CompoundTag storage describe host representation. This is groundwork for later inventory access, not a completed public inventory API or independently implemented item serialization.

Changed paths: `include/bedrock/forward.h`, `include/bedrock/memory.h`, `include/bedrock/world/actor/actor.h`, `include/bedrock/world/item/item_stack.h`, `include/bedrock/world/item/item_stack_base.h`, `include/bedrock/world/level/tick.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-904"></a>
### 904 · feat: add ItemStack {#commit-904}

[Full commit 8e5ac0e5ca9767e3281c12f6846660fff70420cb](https://github.com/EndstoneMC/endstone/commit/8e5ac0e5ca9767e3281c12f6846660fff70420cb) · 2024-05-07T23:14:09Z · parent `48a540950a3e735eac466d18249b5d1b4b7cc92a` · native_abi_scaffold.

Expands ItemStack with network-ID variants and polymorphic typed server/client IDs, with declared sizes for the variant, ItemStackBase and ItemStack. These are ABI constraints on the selected native version. They do not validate every member offset, ownership rule or network operation, and no round-trip item test is added.

Changed paths: `include/bedrock/network/item/item_stack_net_id_variant.h`, `include/bedrock/world/item/item_stack.h`, `include/bedrock/world/item/item_stack_base.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-905"></a>
### 905 · feat: add MaterialType {#commit-905}

[Full commit 113e7b589c2b802e1860dfbadcc128329aeb3ea1](https://github.com/EndstoneMC/endstone/commit/113e7b589c2b802e1860dfbadcc128329aeb3ea1) · 2024-05-07T23:36:21Z · parent `8e5ac0e5ca9767e3281c12f6846660fff70420cb` · native_enum_mapping.

Adds the native MaterialType values0–54 with mapping-origin commentary and marks string helpers nodiscard. The enum is a reconstruction of domain identifiers; this commit provides no independent material conversion implementation or rationale favoring a broader enum style.

Changed paths: `include/bedrock/forward.h`, `include/bedrock/world/actor/actor.h`, `include/bedrock/world/item/item_stack_base.h`, `include/bedrock/world/material/material_type.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-906"></a>
### 906 · feat: add macro BEDROCK_STATIC_ASSERT_SIZE for size checks {#commit-906}

[Full commit ac82785cff63c721feb6fcbdb7c269de9ac0cb90](https://github.com/EndstoneMC/endstone/commit/ac82785cff63c721feb6fcbdb7c269de9ac0cb90) · 2024-05-08T14:55:13Z · parent `113e7b589c2b802e1860dfbadcc128329aeb3ea1` · abi_check_policy.

Introduces BEDROCK_STATIC_ASSERT_SIZE with Windows/Linux sizes and migrates existing assertions, but enables the macro only under NDEBUG. Debug builds therefore lose these size checks rather than gaining universal checking. Renames the platform-selection macro without changing its selected values and removes an export-macro override guard. The useful evidence is explicit platform-layout enforcement in release-style builds, bounded by the fact that total size alone does not prove offsets, vtables or ownership.

Changed paths: `include/bedrock/bedrock.h`, `include/bedrock/command/command.h`, `include/bedrock/command/command_registry.h`, `include/bedrock/command/minecraft_commands.h`, `include/bedrock/common/app_platform_listener.h`, `include/bedrock/common/game_callbacks.h`, `include/bedrock/mce.h`, `include/bedrock/network/item/item_stack_net_id_variant.h`, `include/bedrock/network/network_identifier.h`, `include/bedrock/network/protocol/packet.h`, `include/bedrock/network/raknet/types.h`, `include/bedrock/network/syncher/move_actor_absolute_data.h`, `include/bedrock/server/player_list_entry.h`, `include/bedrock/world/actor/actor_collision.h`, `include/bedrock/world/actor/actor_environment.h`, `include/bedrock/world/actor/components/built_in_actor_components.h`, `include/bedrock/world/actor/registry/entity_context.h`, `include/bedrock/world/item/item_stack.h`, `include/bedrock/world/item/item_stack_base.h`, `include/bedrock/world/level/event/actor_event.h`, `include/bedrock/world/level/event/block_event.h`, `include/bedrock/world/math/vec2.h`, `include/bedrock/world/math/vec3.h`, `include/endstone/endstone.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-913"></a>
### 913 · feat: add Tag::Type {#commit-913}

[Full commit 60c3c9aa345d72a2c409e34de54c80478edd08a5](https://github.com/EndstoneMC/endstone/commit/60c3c9aa345d72a2c409e34de54c80478edd08a5) · 2024-05-09T16:22:34Z · parent `3da0bb49a0226b1f11b24ed2b3d299b3a1506b6e` · native_enum_mapping.

Introduces Tag::Type with End through IntArray and the count sentinel. This is the first NBT type vocabulary in the chain; actual tag layouts, I/O results and behavior arrive incrementally afterward.

Changed paths: `include/bedrock/nbt/tag.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-914"></a>
### 914 · refactor: replace forward declarations with imports {#commit-914}

[Full commit fd775b9a49ee96eaa8efce4c01326744ec9b9629](https://github.com/EndstoneMC/endstone/commit/fd775b9a49ee96eaa8efce4c01326744ec9b9629) · 2024-05-09T16:22:57Z · parent `60c3c9aa345d72a2c409e34de54c80478edd08a5` · declaration_integration.

Replaces selected forward declarations with includes and marks Minecraft's destructor override. The inspected change tightens declaration consistency; it does not add destruction behavior or complete the emerging NBT implementation.

Changed paths: `include/bedrock/command/command_origin.h`, `include/bedrock/common/minecraft.h`, `include/bedrock/forward.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-915"></a>
### 915 · feat: add IDataInput and IDataOutput {#commit-915}

[Full commit dd18094d47ab5a712074992aad394826c9df9cfc](https://github.com/EndstoneMC/endstone/commit/dd18094d47ab5a712074992aad394826c9df9cfc) · 2024-05-09T16:42:44Z · parent `fd775b9a49ee96eaa8efce4c01326744ec9b9629` · native_io_scaffold.

Adds abstract IDataInput/IDataOutput operations with typed primitive/string reads and writes. Reads refer to Bedrock::Result before its definition arrives in916, showing an incremental native-interface reconstruction. The declarations provide neither byte-order implementation nor evidence that malformed input handling has been tested.

Changed paths: `include/bedrock/nbt/io/data_input.h`, `include/bedrock/nbt/io/data_output.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-916"></a>
### 916 · feat: add Bedrock::Result {#commit-916}

[Full commit 71044e071437f2a0f4c1c63aca2555a65a4b4440](https://github.com/EndstoneMC/endstone/commit/71044e071437f2a0f4c1c63aca2555a65a4b4440) · 2024-05-09T22:31:13Z · parent `dd18094d47ab5a712074992aad394826c9df9cfc` · result_model.

Adds expected-lite0.6.3 to dependency/build metadata and defines Bedrock::Result over expected<T,ErrorInfo<E>>; ErrorInfo remains forward-declared until922 and properly included later. I/O primitive signatures move to fixed-width signed forms. This mirrors the host's error/value representation, not evidence that Endstone invented or benchmarked a new error-handling policy.

Changed paths: `CMakeLists.txt`, `conanfile.py`, `include/bedrock/forward.h`, `include/bedrock/nbt/io/data_input.h`, `include/bedrock/nbt/io/data_output.h`, `include/bedrock/result.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-917"></a>
### 917 · feat: add headers for nbt tags {#commit-917}

[Full commit 6b19e05c6e703b238017380e42fedd79d92197e5](https://github.com/EndstoneMC/endstone/commit/6b19e05c6e703b238017380e42fedd79d92197e5) · 2024-05-10T09:50:14Z · parent `71044e071437f2a0f4c1c63aca2555a65a4b4440` · native_abi_scaffold.

Adds13 NBT tag layouts with scalar, array, list and compound-map storage, abstract Tag operations and a PrintStream interface. CompoundTagVariant initially inherits EndTag and contains a variant of still-abstract tag alternatives, an incomplete construction model later replaced in928. IDataInput byte signedness and I/O file locations also change. Size assertions express platform expectations but no serialization, parsing or interoperability tests accompany the large header addition.

Changed paths: `include/bedrock/io/data_input.h`, `include/bedrock/io/data_output.h`, `include/bedrock/io/print_stream.h`, `include/bedrock/nbt/byte_array_tag.h`, `include/bedrock/nbt/byte_tag.h`, `include/bedrock/nbt/compound_tag.h`, `include/bedrock/nbt/compound_tag_variant.h`, `include/bedrock/nbt/double_tag.h`, `include/bedrock/nbt/end_tag.h`, `include/bedrock/nbt/float_tag.h`, `include/bedrock/nbt/int64_tag.h`, `include/bedrock/nbt/int_array_tag.h`, `include/bedrock/nbt/int_tag.h`, `include/bedrock/nbt/list_tag.h`, `include/bedrock/nbt/short_tag.h`, `include/bedrock/nbt/string_tag.h`, `include/bedrock/nbt/tag.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-918"></a>
### 918 · feat: add implementations for PrintStream and Tag {#commit-918}

[Full commit 12bc154566f005b221fa579b1e33f16685a18c25](https://github.com/EndstoneMC/endstone/commit/12bc154566f005b221fa579b1e33f16685a18c25) · 2024-05-10T10:26:14Z · parent `6b19e05c6e703b238017380e42fedd79d92197e5` · local_implementation_attempt.

Implements PrintStream println and basic Tag printing, tag-name mapping and no-op child deletion. The print overload does not use its prefix parameter. This is an actual attempt at local behavior beyond ABI declarations, later removed in928; it should not be silently treated as the final host-delegating design.

Changed paths: `include/bedrock/io/print_stream.h`, `include/bedrock/nbt/tag.h`, `src/endstone_runtime/bedrock/io/print_stream.cpp`, `src/endstone_runtime/bedrock/nbt/tag.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-920"></a>
### 920 · feat: implement EndTag {#commit-920}

[Full commit 1a1646de507519e1fe29082b426f480c176804b9](https://github.com/EndstoneMC/endstone/commit/1a1646de507519e1fe29082b426f480c176804b9) · 2024-05-10T15:57:38Z · parent `44fcaa6d1ea333dcc00e77d21abeca0e30f47bf1` · local_implementation_attempt.

Implements EndTag's no-payload write/load, End identity, END text and zero hash; equals relies on the Tag base implementation supplied in923. copy returns an empty unique_ptr rather than a cloned tag. These incomplete semantics are removed with the local implementations in928, not specifically repaired and tested here.

Changed paths: `include/bedrock/nbt/end_tag.h`, `src/endstone_runtime/bedrock/nbt/end_tag.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-921"></a>
### 921 · feat: add Bedrock::CallStack {#commit-921}

[Full commit 8fd7d0d8f3c289f0169a276d7209e47b35b35606](https://github.com/EndstoneMC/endstone/commit/8fd7d0d8f3c289f0169a276d7209e47b35b35606) · 2024-05-10T16:17:41Z · parent `1a1646de507519e1fe29082b426f480c176804b9` · native_error_scaffold.

Adds CallStack with32 frame slots and message/logging context, plus platform-sized FrameWithContext. These declarations establish storage for native error information. The LogLevel namespace mismatch is corrected in924; there is no new stack-capture implementation or diagnostics experiment in this commit.

Changed paths: `include/bedrock/callstack.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-922"></a>
### 922 · feat: add Bedrock::ErrorInfo {#commit-922}

[Full commit 331748e2746b4559b517234900fd85f5c45c459f](https://github.com/EndstoneMC/endstone/commit/331748e2746b4559b517234900fd85f5c45c459f) · 2024-05-10T16:26:49Z · parent `8fd7d0d8f3c289f0169a276d7209e47b35b35606` · native_error_scaffold.

Defines ErrorInfo with an error value, frame context and recursively stored frame errors, completing a type referenced by916's Result. The recursive vectors and declared64-byte size describe native representation; the commit does not establish allocation strategy, failure behavior or an independently tested error-reporting pipeline.

Changed paths: `include/bedrock/error_info.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-923"></a>
### 923 · feat: implement Tag::equals {#commit-923}

[Full commit ff2f6713f35b79ae25b9ff981e44969c51f845de](https://github.com/EndstoneMC/endstone/commit/ff2f6713f35b79ae25b9ff981e44969c51f845de) · 2024-05-10T16:27:02Z · parent `331748e2746b4559b517234900fd85f5c45c459f` · local_implementation_attempt.

Provides Tag's destructor and equals based on matching type IDs, and imports the I/O/Result declarations used by the interface. Type equality is only a base-level comparison, not value equality for compounds or scalars. The concrete tag classes remain incomplete until928 changes the virtual-method design.

Changed paths: `include/bedrock/nbt/tag.h`, `src/endstone_runtime/bedrock/nbt/tag.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-924"></a>
### 924 · fix: LogLevel should be under namespace Bedrock {#commit-924}

[Full commit 8d8f6ca3d9ce3f6916692abf0722e319790a65b2](https://github.com/EndstoneMC/endstone/commit/8d8f6ca3d9ce3f6916692abf0722e319790a65b2) · 2024-05-10T16:27:38Z · parent `ff2f6713f35b79ae25b9ff981e44969c51f845de` · abi_declaration_correction.

Moves LogLevel under namespace Bedrock and adjusts aliases/signatures/maps using its uint32 representation. This repairs the declaration relation used by921's context types without changing the numeric logging thresholds or establishing a new runtime logging policy.

Changed paths: `include/bedrock/bedrock_log.h`, `src/endstone_runtime/bedrock/bedrock_log.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-925"></a>
### 925 · feat: add sources for nbt tags {#commit-925}

[Full commit 78097708d97c64cb6c21393e71fbf65074410d17](https://github.com/EndstoneMC/endstone/commit/78097708d97c64cb6c21393e71fbf65074410d17) · 2024-05-10T16:28:14Z · parent `8d8f6ca3d9ce3f6916692abf0722e319790a65b2` · scaffold_and_dependency_repair.

Adds11 mostly header-only NBT translation-unit scaffolds, which warrant brief treatment rather than11 invented implementations. Meaningful accompanying repairs break the CompoundTag/variant include cycle and include ErrorInfo from Result, with a Result<uint8_t> size assertion. All changed source was read;928 later deletes these empty units as part of a different representation approach.

Changed paths: `include/bedrock/forward.h`, `include/bedrock/nbt/compound_tag.h`, `include/bedrock/nbt/compound_tag_variant.h`, `include/bedrock/result.h`, `src/endstone_runtime/bedrock/nbt/byte_array_tag.cpp`, `src/endstone_runtime/bedrock/nbt/byte_tag.cpp`, `src/endstone_runtime/bedrock/nbt/compound_tag.cpp`, `src/endstone_runtime/bedrock/nbt/double_tag.cpp`, `src/endstone_runtime/bedrock/nbt/float_tag.cpp`, `src/endstone_runtime/bedrock/nbt/int64_tag.cpp`, `src/endstone_runtime/bedrock/nbt/int_array_tag.cpp`, `src/endstone_runtime/bedrock/nbt/int_tag.cpp`, `src/endstone_runtime/bedrock/nbt/list_tag.cpp`, `src/endstone_runtime/bedrock/nbt/short_tag.cpp`, `src/endstone_runtime/bedrock/nbt/string_tag.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-926"></a>
### 926 · fix: warning due to reference never being initialised {#commit-926}

[Full commit 88a34a9af89b2c372ae03cc08c564d5967fb1a0b](https://github.com/EndstoneMC/endstone/commit/88a34a9af89b2c372ae03cc08c564d5967fb1a0b) · 2024-05-10T16:34:33Z · parent `78097708d97c64cb6c21393e71fbf65074410d17` · abi_declaration_correction.

Changes native ServerInstance's app and Dimension's level members from references to pointers, explicitly addressing never-initialized-reference warnings in these reconstructed layouts. The Dimension getter is not adjusted until927. This is evidence about native declaration modeling, not ownership transfer or a blanket preference for pointers over references.

Changed paths: `include/bedrock/server/server_instance.h`, `include/bedrock/world/level/dimension/dimension.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-927"></a>
### 927 · fix: compilation error due to the change of member variable {#commit-927}

[Full commit 4a035a7b1d70a8c61077ce20c4a795ca7a11b994](https://github.com/EndstoneMC/endstone/commit/4a035a7b1d70a8c61077ce20c4a795ca7a11b994) · 2024-05-10T16:38:04Z · parent `88a34a9af89b2c372ae03cc08c564d5967fb1a0b` · corrective_followup.

Dereferences the changed Dimension level pointer in getLevel, repairing926's compilation mismatch. This small follow-up demonstrates that the representation change needed a caller adjustment; no nullability guard or lifetime extension is introduced.

Changed paths: `src/endstone_runtime/bedrock/world/level/dimension/dimension.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-928"></a>
### 928 · fix: add put methods for CompoundTag {#commit-928}

[Full commit 2468f9752baec492cc05c017329fca9018b924d6](https://github.com/EndstoneMC/endstone/commit/2468f9752baec492cc05c017329fca9018b924d6) · 2024-05-11T00:02:24Z · parent `4a035a7b1d70a8c61077ce20c4a795ca7a11b994` · architecture_revision.

Adds five CompoundTag put operations delegated to native hooks and simultaneously replaces the local NBT implementation approach. Tag's default constructor is deleted, formerly pure virtual operations become throwing stubs, its type enum uses char representation, and CompoundTagVariant becomes a std::variant-derived view with visitation rather than EndTag plus a member. Deletes Tag/EndTag/PrintStream implementations and empty tag sources. The observed direction is a host-object ABI view rather than a complete local serializer; that rationale is inferred from code, not explicitly argued in the title. No round-trip tests or proof that copied native views preserve valid virtual behavior are added.

Changed paths: `include/bedrock/io/data_output.h`, `include/bedrock/io/print_stream.h`, `include/bedrock/nbt/byte_tag.h`, `include/bedrock/nbt/compound_tag.h`, `include/bedrock/nbt/compound_tag_variant.h`, `include/bedrock/nbt/end_tag.h`, `include/bedrock/nbt/list_tag.h`, `include/bedrock/nbt/tag.h`, `src/endstone_runtime/bedrock/io/print_stream.cpp`, `src/endstone_runtime/bedrock/nbt/byte_array_tag.cpp`, `src/endstone_runtime/bedrock/nbt/byte_tag.cpp`, `src/endstone_runtime/bedrock/nbt/compound_tag.cpp`, `src/endstone_runtime/bedrock/nbt/double_tag.cpp`, `src/endstone_runtime/bedrock/nbt/end_tag.cpp`, `src/endstone_runtime/bedrock/nbt/float_tag.cpp`, `src/endstone_runtime/bedrock/nbt/int64_tag.cpp`, `src/endstone_runtime/bedrock/nbt/int_array_tag.cpp`, `src/endstone_runtime/bedrock/nbt/int_tag.cpp`, `src/endstone_runtime/bedrock/nbt/list_tag.cpp`, `src/endstone_runtime/bedrock/nbt/short_tag.cpp`, `src/endstone_runtime/bedrock/nbt/string_tag.cpp`, `src/endstone_runtime/bedrock/nbt/tag.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-957"></a>
### 957 · refactor: remove unnecessary forward declaration {#commit-957}

[Full commit 8097f798a2aa694a8d8723a5ee56825db7e4d2fb](https://github.com/EndstoneMC/endstone/commit/8097f798a2aa694a8d8723a5ee56825db7e4d2fb) · 2024-05-18T15:28:46Z · parent `640c5624436def25da2072ae93ae8330e4f57ef7` · declaration_integration.

Removes redundant forward declarations/namespace wrapping and includes CompoundTag for item/saved-data declarations. This is a dependency completeness repair in the evolving native headers, without new serialization behavior or ownership transfer.

Changed paths: `include/bedrock/forward.h`, `include/bedrock/world/item/item_stack_base.h`, `include/bedrock/world/level/storage/saved_data.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.
