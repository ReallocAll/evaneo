<!-- retrieval: {"source_ids":["public:commit:12c0c062e32803cbcfed911c81c409077d598270","public:commit:221c28cbd6dc436381f895b3e5cb1ad02bd4b47d","public:commit:5416b404990ab70006e9b77ceacb7f9890442ad3","public:commit:640c5624436def25da2072ae93ae8330e4f57ef7","public:commit:779affa8eb2e977221a540f00bd86d51aa16bb80","public:commit:b9971184a54dcc68e29ef42b31ebefc2f1ad949d","public:commit:c80e3ddfff7df2eecb167b7ad4e6a9a5b3c397fa","public:commit:c84d9e703f7ae9aacf77ae1791981a36d6684576"],"source_type":"public","date":"2024-05-14..2024-05-18","topics":["lifetime","concurrency","ffi","testing","diagnosis","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native hook selection and command ownership require separate proofs {#native-hook-selection-and-command-ownership-require-separate-proofs}

## The scheduler correction changes its clock and injection point {#the-scheduler-correction-changes-its-clock-and-injection-point}

[947](#commit-947) explicitly reports Linux scheduler functionality after moving heartbeat injection from Minecraft::tickSimtime to Level::tick. It uses the native server-tick value and removes the EndstoneServer counter introduced in793 without initialization. The original function name is supplied explicitly for the platform-specific lookup.948 is an exact source relocation, not another scheduler behavior change.

The existing scheduler, task and hook implementations were read in full at960. The change does not replace the concurrent pending queue, heap/active-task bookkeeping, cancellation flag or repeat scheduling algorithm. Earlier concerns about cancellation bookkeeping and borrowed Plugin lifetime are not resolved by choosing a better hook. Conversely, the removed counter's initialization concern should no longer be reported as present at960. The Linux success statement is the author's commit claim; no live host execution in this unit proves which prior mechanism caused the failure. The causal conclusion supported by code is the changed hook/clock, not an invented root-cause diagnosis.

## Constructing a native origin is not the same as transferring it safely {#constructing-a-native-origin-is-not-the-same-as-transferring-it-safely}

954 gives CommandContext an explicitly owning unique_ptr constructor.955 makes the free-function hook helper accept a name, and956 wraps a static native factory returning unique_ptr<CommandOrigin> with the appropriate return convention.958 supplies a hardcoded command version38.959 reconstructs enough ServerNetworkHandler structure to obtain the native Level and calls an init method completed in960.

960 initializes a player's retained command origin from native network/player/level data and exposes performCommand. The intended path is coherent at a high level: prepare an origin representing the player, construct context, execute through native MinecraftCommands and return is_success. But the ownership transfer is not coherent. The code obtains the raw pointer from the retained unique_ptr, constructs a second unique_ptr from it, and gives the second owner to the owning CommandContext. Nothing releases or clones the first owner. When the context is destroyed, the player's stored owner can point at freed storage and later delete it again.

This is a concrete static ownership counterexample supported by both954 and960 plus final full-file context. It is not an observed crash, and a proposed repair was not implemented here. The useful review question is whether a context needs a fresh origin, a real transfer, or a borrowed representation; the historical code does not document a choice resolving that conflict. Do not attribute any proposed alternative to Vincent without later evidence.

## Event semantics and verification boundaries {#event-semantics-and-verification-boundaries}

The existing native command hook dispatches a cancellable ServerCommandEvent, but final context still does not copy a listener-modified command string back into CommandContext. Adding performCommand therefore does not automatically implement command rewriting. Returning the host's success result is a separate feature from mutation/cancellation propagation. No Python binding for performCommand appears in this unit.

The source includes platform-specific name/return-convention handling and reconstructed native declarations, but there is no new host command execution test or ownership regression test. Existing scheduler tests are source-read evidence from the previous unit, not live platform verification. All assigned changes are attributed to Vincent; no PR review, collaborator endorsement or current-version correctness is assumed. Retrieve this dossier for hook relocation, use of native clocks, explicit original-symbol lookup, owning-context APIs and checking raw-pointer escape/re-adoption across wrappers.

## Per-commit source dispositions {#per-commit-source-dispositions}

<a id="commit-947"></a>
### 947 · fix: scheduler now works on Linux {#commit-947}

[Full commit 12c0c062e32803cbcfed911c81c409077d598270](https://github.com/EndstoneMC/endstone/commit/12c0c062e32803cbcfed911c81c409077d598270) · 2024-05-14T14:03:08Z · parent `9cefce226c2ead60e57a36a20227c660559e3252` · corrective_hook_revision.

Explicitly reports that the scheduler now works on Linux and moves heartbeat injection from Minecraft::tickSimtime to Level::tick, using the native current-server tick value. The old server-owned counter, introduced without initialization in793, is removed. Original-function resolution is made explicit for the platform hook name. The commit changes the timing source and hook boundary, not the scheduler's queue/cancellation algorithms; existing tests do not independently establish live Linux host behavior.

Changed paths: `include/bedrock/common/minecraft.h`, `include/bedrock/world/level/level.h`, `include/bedrock/world/level/tick.h`, `include/endstone/detail/server.h`, `src/endstone_core/level/level.cpp`, `src/endstone_core/server.cpp`, `src/endstone_runtime/bedrock/common/minecraft.cpp`, `src/endstone_runtime/bedrock/server/level/level.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-948"></a>
### 948 · refactor: move level.cpp to bedrock/world/level {#commit-948}

[Full commit 779affa8eb2e977221a540f00bd86d51aa16bb80](https://github.com/EndstoneMC/endstone/commit/779affa8eb2e977221a540f00bd86d51aa16bb80) · 2024-05-14T14:04:46Z · parent `12c0c062e32803cbcfed911c81c409077d598270` · mechanical.

Moves the Level hook source into bedrock/world/level without changing its bytes. Exact blob identity is retained in rename coverage. It adds no second scheduler fix or new runtime behavior beyond947.

Changed paths: `src/endstone_runtime/bedrock/world/level/level.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-954"></a>
### 954 · fix: add missing headers {#commit-954}

[Full commit c80e3ddfff7df2eecb167b7ad4e6a9a5b3c397fa](https://github.com/EndstoneMC/endstone/commit/c80e3ddfff7df2eecb167b7ad4e6a9a5b3c397fa) · 2024-05-18T13:47:33Z · parent `55c7f785dd4161625ba9ed370587d2489e914129` · ownership_api_preparation.

Alongside missing-header fixes, adds CommandContext construction taking a unique_ptr<CommandOrigin> by value and moving it into the context, and renames the version member. This establishes an owning command-context contract used by960; treating the commit as include-only would miss the later double-ownership issue. UUID gains the appropriate string include.

Changed paths: `include/bedrock/command/command_context.h`, `include/bedrock/command/command_registry.h`, `include/endstone/util/uuid.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-955"></a>
### 955 · feat: allow get_original to accept an optional name {#commit-955}

[Full commit 5416b404990ab70006e9b77ceacb7f9890442ad3](https://github.com/EndstoneMC/endstone/commit/5416b404990ab70006e9b77ceacb7f9890442ad3) · 2024-05-18T13:48:16Z · parent `c80e3ddfff7df2eecb167b7ad4e6a9a5b3c397fa` · hook_api_extension.

Extends the free-function get_original helper to accept an optional explicit name, matching existing member-function overloads while retaining address-based fallback. This supports native static/free hooks such as956. It adds lookup flexibility, not verification that every supplied mangled name or calling convention matches the host.

Changed paths: `include/endstone/detail/hook.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-956"></a>
### 956 · feat: add CommandOrigin::fromCommandOriginData {#commit-956}

[Full commit 640c5624436def25da2072ae93ae8330e4f57ef7](https://github.com/EndstoneMC/endstone/commit/640c5624436def25da2072ae93ae8330e4f57ef7) · 2024-05-18T15:28:16Z · parent `5416b404990ab70006e9b77ceacb7f9890442ad3` · native_factory.

Introduces CommandOriginData, extracts the existing origin-type enum without changing its values, and wraps the host's fromCommandOriginData factory returning unique_ptr. The static-function return-value convention is handled separately from member 'this' calls on the two platforms. The data carries type, UUID, request ID and player ID; actual player initialization consuming it arrives in960. No host factory test is added.

Changed paths: `include/bedrock/command/command_origin.h`, `include/bedrock/command/command_origin_data.h`, `include/bedrock/command/command_origin_type.h`, `src/endstone_runtime/bedrock/command/command_origin.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-958"></a>
### 958 · feat: add CommandVersion::CurrentVersion {#commit-958}

[Full commit 221c28cbd6dc436381f895b3e5cb1ad02bd4b47d](https://github.com/EndstoneMC/endstone/commit/221c28cbd6dc436381f895b3e5cb1ad02bd4b47d) · 2024-05-18T16:10:45Z · parent `8097f798a2aa694a8d8723a5ee56825db7e4d2fb` · native_version_constant.

Adds CommandVersion::CurrentVersion as the literal38. This selects a known command protocol/version value for subsequent execution; it is not queried from the host and no cross-version negotiation is implemented.

Changed paths: `include/bedrock/command/command_version.h`, `src/endstone_runtime/magic.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-959"></a>
### 959 · feat: add members of ServerNetworkHandler {#commit-959}

[Full commit c84d9e703f7ae9aacf77ae1791981a36d6684576](https://github.com/EndstoneMC/endstone/commit/c84d9e703f7ae9aacf77ae1791981a36d6684576) · 2024-05-18T16:11:31Z · parent `221c28cbd6dc436381f895b3e5cb1ad02bd4b47d` · native_network_mapping.

Expands ServerNetworkHandler's native inheritance and members, including thread queue, non-owning references, observers and LevelListener state, and adds getLevel. The new-player hook now invokes EndstonePlayer::init, whose implementation/declaration arrives in960, so this intermediate tree is incomplete. These reconstructed fields enable the command-origin factory; no full native-layout or networking test is added.

Changed paths: `include/bedrock/network/protocol/net_event_callback.h`, `include/bedrock/server/network/server_network_handler.h`, `include/bedrock/social.h`, `include/bedrock/threading.h`, `src/endstone_runtime/bedrock/server/network/server_network_handler.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-960"></a>
### 960 · feat: add Player::performCommand {#commit-960}

[Full commit b9971184a54dcc68e29ef42b31ebefc2f1ad949d](https://github.com/EndstoneMC/endstone/commit/b9971184a54dcc68e29ef42b31ebefc2f1ad949d) · 2024-05-18T16:11:53Z · parent `c84d9e703f7ae9aacf77ae1791981a36d6684576` · feature_with_ownership_counterexample.

Adds Player::performCommand and initializes a retained unique_ptr command origin from native player/network/level data. The call creates another unique_ptr from command_origin_.get() and moves that new owner into CommandContext; both now claim the same origin. Context destruction can delete the object while the member remains dangling, creating a static double-ownership/use-after-free path. This conclusion follows the owning constructor added in954, not a runtime experiment. Execution returns the host result's is_success; no Python binding or regression test is added. The existing command hook still does not propagate a listener's modified command text back into the context.

Changed paths: `include/endstone/detail/player.h`, `include/endstone/player.h`, `src/endstone_core/player.cpp`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.
