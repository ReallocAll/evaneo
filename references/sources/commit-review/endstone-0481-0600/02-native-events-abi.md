<!-- retrieval: {"source_ids":["public:commit:05aa90a0a64893926fc0f2c3b3f67e130215f308","public:commit:0b77c9e9c3910499af0e48e101b91cf9466e473e","public:commit:0f9980e6be96a61bb2525328dd2370ac701e267f","public:commit:1bcf473cdf283f99fc99d249526f32a07fab841c","public:commit:230509d8b9720609df1943b26a6d7205816b989e","public:commit:2be59a15ee88af988361b47a3d2e6ce5328380bb","public:commit:46392b2f801079f22bbb32a5b360229e9a8d0717","public:commit:4b848df877d377b5f0d13b3ac834ed31b205340d","public:commit:57f5bef7d40cbb70602f3e8bb69a235488015f55","public:commit:588b22a142f23a15add7b80c09d6b5a971db8cc2","public:commit:5c8573ce71d4f94e55f5f13eb7d5fe6b564626e8","public:commit:5e0053aeffd79b73aac4eaf08788bf7294dd2d1e","public:commit:63f3a786fb6cfa892d8c4571acf778068b041ac0","public:commit:6b08811f855ecc6c8c18f8efbd35f2b002e52a47","public:commit:6fe42f2481a75a4894224a0024a9e544bbfd1372","public:commit:7b9e8d5abd0fcd2d4bc6d53163986856f6fbf51e","public:commit:7e1b34196700082cdbd91a93aea7bd3f90af9531","public:commit:8323efd3ad368db77bfced842037aba3e070cbd0","public:commit:8ace9966d1f82d3492e6ba2a0022ada3efb9352c","public:commit:91ef3f897832d8fa944f1892a02ca6bca9b4630f","public:commit:9b72254a7c27b7a95178c0f76a64d21bbc9678ad","public:commit:9c15b796423d1d72db56de325389326d4b4b1364","public:commit:9ddf0668d1d0a97685020d1392428185306d9a67","public:commit:a32757a56c9210ed859b446d763546206a05b7b5","public:commit:a3c579ac4300fcb13766737be5efb4a4299b2ff9","public:commit:a9f30d23933d92ad61a3abc3ca797192b2fbe0fd","public:commit:aadad562933654f6c8a086fb86860bbe415bc179","public:commit:b31ec55b2d91b64547d495919648503b37780eee","public:commit:b7f34022c199b4a8d4e5afe1cd4976d63698b57c","public:commit:c62e80e2f7cf5d89298b8bbe36525b8e32579b56","public:commit:cb4e2e12526baf5210d40be75fdec0bea070daae","public:commit:d08c0cdf9338718ed5db8dab8f66650b1b1aebd5","public:commit:d68c146c9ebb076184b8f251058a7d2304370e66","public:commit:da6d0faff93615b0c9d7016c463d91668ee90c44","public:commit:dfa0699c068a7d59a3b6dedc794b6ce409904e04","public:commit:e0807862709fcd57fcdd317000b8fdac9cc4298f","public:commit:e6d0159353ea92c96dd4b1c037e3ebe4c9c66975","public:commit:ecebce5a5aea58cb3ec6d5f2101b53aa3525de31","public:commit:f7315c2786ed0adae4d4eba3803ae4e9d689eb43","public:commit:f9296c3cea4be40182a5185f97ee32433e6aec78","public:commit:fd0c8c64d2efd224dd5ae5ed0c101a6cb9015c1c","public:commit:fd4276b4cb92f464112125f385c851a31b7bb032"],"source_type":"public","date":"2024-03-25..2024-04-04","topics":["lifetime","ffi","testing","build","recovery","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native event adapters, packet mutation and ABI uncertainty {#native-event-adapters-packet-mutation-and-abi-uncertainty}

## Result: useful adapters amid deliberately provisional native models {#result-useful-adapters-amid-deliberately-provisional-native-models}

The March–April sequence adds three different event bridges: an outgoing server-list response can be rewritten, a dedicated-console command can be cancelled, and rain/thunder proposals can be vetoed. These bridges do not share an identical mutation mechanism. Much of the surrounding actor/player/block/item/server event work is native layout scaffolding and temporary diagnostic interception, later removed at 578. A declared event type, a std::variant alternative, an installed native hook and a public Endstone callback are four different levels of implementation.

The prior unit established command visibility and native actor/player virtual interfaces. This unit extends that reverse-engineering approach but also shows several corrections and retreats. The useful result is a dated decision history with explicit assumptions, rather than an assertion that every named game event was supported or that the source mirrors are authoritative host specifications.

## Server-list ping: advertised state is a projection {#server-list-ping-advertised-state-is-a-projection}

511 introduces GameMode and 512 uses it to interpret an outgoing unconnected-pong response. The hook checks the first packet byte, extracts a length after a fixed header, reads a semicolon-separated response and creates an asynchronous noncancellable ServerListPingEvent. The remote address and port come from the native send parameters. If parsing fails, it logs and forwards the original packet. If parsing succeeds, plugins can alter selected fields; the hook serializes them into a new local vector, points the native send parameters at that vector and calls the original send routine before returning.

This placement is outbound interception even though the public event comment speaks of a ping coming in. The mutable fields describe what the server advertises: message of the day, counts/capacity, reported version, level name and game mode. Changing max_players here does not change the host's actual admission policy, and changing game_mode does not update world state. The distinction is directly visible because the only writeback is packet construction. Python property descriptions and names should not be read as evidence of another runtime state mutation.

515 improves parser structure by collecting fields and checking there are at least twelve before indexed access. Numeric conversion and enum-name validation can reject malformed values; exceptions return false. It remains a partial format parser: it does not validate every textual prefix, complete numeric consumption, delimiter escaping or preservation of extra fields. Serialization writes fixed marker/unknown values and a trailing field rather than round-tripping the entire input. Unknown later protocol extensions therefore are not automatically preserved merely because parsing succeeds.

The native packet boundary is a separate concern. Header/length access occurs before parsing and has no explicit send-buffer bounds validation in the observed code. The length expression shifts char values, and the reconstructed data pointer refers to local vector storage, so the forwarding contract assumes the native send routine consumes it synchronously rather than retaining it. These are source-level constraints, not a demonstrated exploit or measured failure. No packet fixtures, malformed-length tests, delimiter cases or asynchronous-buffer-retention tests are added in this unit.

513 exposes these properties to Python and removes unused GameMode aliases. 559 changes Spectator from 6 to 3, while 588 updates generated stubs. The ping serializer uses enum names, so the numeric correction has different implications for integer consumers than for this particular string field. The selected Minecraft version advances to 1.20.73 at 558, but a version literal and badge are not an ABI compatibility test.

## Console cancellation and command rewriting diverge {#console-cancellation-and-command-rewriting-diverge}

516 defines the native CommandContext view: a command string, an owned origin and version, with documented offsets but a commented size assertion. It exposes getters, not a command setter. 517 hooks MinecraftCommands::executeCommand and only creates ServerCommandEvent for DedicatedServer origin. Player and other command origins are forwarded without this event. Cancellation returns the native CommandsDisabled result and skips the original execution call.

The allowed path forwards the original CommandContext unchanged. ServerCommandEvent stores a mutable copy of the command string and Python exposes a setter, but there is no copy-back or replacement context before execution. Consequently cancellation is implemented while rewriting the event's command does not alter the native execution input at this endpoint. This distinction is a strong reason to trace mutation from public API through the hook, instead of treating a setter or documentation sentence as proof of effect. It is retained as an observed code discrepancy without claiming a reproduced host result.

517 initially uses the explicit return-buffer helper on both platforms. 525 changes Linux to an ordinary aggregate return and retains the Windows hidden-buffer path. 527–528 repeat the same correction for weather handler results. The source messages report crashes; the diffs show a calling-convention correction for specific aggregate return types. They do not establish that every aggregate, compiler version or platform should use the same rule. In particular the helper's name RVO should not obscure that this code is manually matching a native ABI, not merely asking a compiler to optimize a C++ copy.

518 removes live diagnostic output from console interception. 519 adds Python sender/command access. A live printf removal affects operational noise, whereas 553 later deletes already-commented print statements and is genuinely mechanical. The individual ledger preserves that distinction.

## Original-function lookup is centralized, with platform enumeration retained {#original-function-lookup-is-centralized-with-platform-enumeration-retained}

523 moves common hook installation and original-function maps out of platform-specific implementations. Platform code still discovers detours and native targets through its own symbol mechanisms. The common installer matches names, prepares and installs funchook detours, and records originals by both detour address and symbol name. 524 repairs stale declarations/uses left during that split. 526 adds optional named lookup to member normal/RVO and free RVO adapters, enabling explicit native symbol selection for ambiguous or differently declared functions.

Endpoint context shows missing originals are fatal with diagnostics, and missing target/preparation/install failures throw. Installation occurs one function at a time, with no rollback protocol shown for an error after earlier hooks were installed. This is the observed failure model; centralizing the code does not newly prove transactionality. No rollback or native symbol enumeration test was added. The project is using funchook through its API, but the external library implementation was not read or executed in this assignment.

The shared pointer-casting helper moves again at 561 to serve vtable work. Its union-based member/function pointer conversion is ABI-sensitive; a relocation does not make it a portable standard representation guarantee. Named originals and detour-address originals solve lookup convenience, not correctness of every function signature or hidden return convention.

## Weather is an actual native writeback path {#weather-is-an-actual-native-writeback-path}

529 supplies previous/proposed rain and lightning booleans plus durations. 530 creates separate cancellable WeatherChangeEvent and ThunderChangeEvent only when the corresponding state changes. Initially callbacks run before the original native handler; cancellation restores the proposed boolean to its previous value. Duration fields are left intact. Rain cancellation and thunder cancellation are independent, so one can proceed while the other is reset.

This differs from console rewriting: cancellation modifies the native input reference that the original handler receives. 565 later moves original execution first and honors native Deny before invoking Endstone listeners. The later vtable dossier traces that ordering reversal and its implications. Neither form is equivalent to undoing arbitrary native side effects already performed elsewhere. At first WeatherEvent has no level reference; 587 resolves that TODO by associating the native handler with the owning EndstoneLevel.

532 binds weather observations but removes constructors from previously constructible server/plugin event classes. That removal belongs to the Python API history, not only to the native weather bridge. The binding hierarchy directly lists Event for concrete weather classes, while the C++ classes derive through WeatherEvent. Later level getters use the inherited base member. A spelling that names WeatherChangeEvent for the inherited getter is not by itself proof of a sibling-object cast defect; the declaring member and binding machinery matter.

## Variant reconstruction evolves toward narrower claims {#variant-reconstruction-evolves-toward-narrower-claims}

533 introduces ValueOrRef as variant<T*,T>, then 538 wraps it with get() returning either inline data or a dereferenced stored pointer. This models a host event envelope with owned/borrowed representation alternatives. The wrapper does not prove the pointer is non-null or that foreign memory contains a valid instance of the expected standard-library variant. The noexcept accessor assumes those conditions. The relevant compatibility constraint includes standard-library ABI and alternative order, not just sizeof.

534–535 define level and player event unions with guessed opaque payload sizes. 537 adds a Windows-only level game-rule alternative, changing indices as well as storage. 540 replaces many guessed payload sizes with empty named types and a final size-forcing placeholder. That preserves the intended known alternative indices while making the storage-extent assumption explicit. It reduces false confidence about individual fields, but still assumes the host discriminator layout and object representation match the local variant model.

The corrections are platform-specific rather than monotonic toward one common number: player Windows padding becomes 368 at 541; level Linux becomes 56 at 542; player Linux becomes 368 at 543; actor Linux later remains 320 versus Windows 304 at 549. Block variants also have distinct platform sizes, and the item variant explicitly leaves one Windows size unchecked. The numbers are historical observations, not reusable constants for a current game version.

537 temporarily asserts the full level event size, then 540 removes that assertion. 541 adds bad_variant_access handling and a memory dump that reads beyond the nominal object size; 543 removes the catch paths while retaining simple visitation. A diagnostic exception handler cannot validate arbitrary foreign memory, and the dump is not a safe general introspection primitive. 546 lowers logs to debug; 548 replaces visitor bodies with TODOs. None of those changes implements public actor/player/block callbacks merely because a native interception exists.

544, 548, 550–552 add overloaded native coordinator entry points and explicitly select the member-pointer overloads before forwarding. 545 adds mutable player-event declarations without hooking that path. 554–555 add item/server envelopes without corresponding public events. Finally 578 removes the provisional coordinator sendEvent hooks, experimental visitation and dump helper, retaining the server lifecycle bridge and shifting toward focused gameplay-handler vtable interception. This removal is an important negative example: a growing list of declarations was exploratory work, not a completed general event product.

## Outcome types and limits {#outcome-types-and-limits}

522 initially represents GameplayHandlerResult with a boolean success and a typed result. 556 revises it to a typed value plus EventResult and introduces Deny/Default terminology distinct from CoordinatorResult. Total object size can remain similar while field semantics and interpretation change. 536's earlier Failed/Success→Reject/Default rename preserves numeric values and is smaller; conflating both as cosmetic would lose the ABI correction.

The engineering pattern supported here is to trace the whole bridge: native trigger, argument/return layout, public event identity, callback eligibility, mutation writeback and original-call order. Several changes improve one link while another remains provisional. Claims of successful crash fixes remain author reports; static source supports the changed mechanism but not measured runtime success. External RakNet/Mojang references identify provenance for borrowed concepts, not independent reading or authorship of the underlying game implementation. No upstream code was executed.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-511"></a>
### 511. faet: add GameMode enum class {#commit-511}

Source: [8323efd3ad368db77bfced842037aba3e070cbd0](https://github.com/EndstoneMC/endstone/commit/8323efd3ad368db77bfced842037aba3e070cbd0) · authored 2024-03-25T11:34:39Z. Actual parent(s): `c5c5fc37f76273539f1574a31a5793c974bfec7d`.

Author: **Vincent**.

Introduces GameMode values including Undefined/Default/WorldDefault aliases and Spectator=6. Values are API/host mapping evidence, not independently verified protocol truth; 513 removes unused values and 559 later corrects Spectator.

First-parent changed paths: `include/endstone/util/game_mode.h`.

Coverage: 35 canonical first-parent patch lines; 35 across all actual parents.

<a id="commit-512"></a>
### 512. feat: add ServerListPingEvent to enable users to customize the information displayed when a server ping is initiated {#commit-512}

Source: [2be59a15ee88af988361b47a3d2e6ce5328380bb](https://github.com/EndstoneMC/endstone/commit/2be59a15ee88af988361b47a3d2e6ce5328380bb) · authored 2024-03-25T12:09:18Z. Actual parent(s): `8323efd3ad368db77bfced842037aba3e070cbd0`.

Author: **Vincent**.

Intercepts outbound unconnected pong, parses semicolon-separated advertised server data into an asynchronous noncancellable event, runs plugins and rebuilds packet before original send. Failure to parse falls back to original response. Mutations alter advertised values, not actual player capacity/game mode. RakNet declarations cite its source, with opaque address padding; external source not read here. Packet length extraction initially uses signed char shifts and lacks length/bounds checks; local buffer lifetime assumes original send consumes synchronously. Parser accepts numeric prefixes and serialization hardcodes unknown fields, with no delimiter escaping or round-trip tests. Keep these bounded format/lifetime constraints rather than claiming a validated network codec.

First-parent changed paths: `include/bedrock/raknet/socket2.h`, `include/bedrock/raknet/types.h`, `include/endstone/event/server/server_list_ping_event.h`, `src/endstone_core/event/server/server_list_ping_event.cpp`, `src/endstone_runtime/bedrock/raknet/socket2.cpp`, `src/endstone_runtime/bedrock/raknet/types.cpp`.

Coverage: 537 canonical first-parent patch lines; 537 across all actual parents.

<a id="commit-513"></a>
### 513. feat(python): add bindings for ServerListPingEvent {#commit-513}

Source: [8ace9966d1f82d3492e6ba2a0022ada3efb9352c](https://github.com/EndstoneMC/endstone/commit/8ace9966d1f82d3492e6ba2a0022ada3efb9352c) · authored 2024-03-25T12:21:00Z. Actual parent(s): `2be59a15ee88af988361b47a3d2e6ce5328380bb`.

Author: **Vincent**.

Adds Python ping-event read/write properties and GameMode enum, pluralizes max_players, removes undefined/default native enum values and initializes utility bindings before dependent event signatures. No Python constructor is exposed for ping event. Documentation now says players allowed, but mutation still changes discovery response only; no server-capacity enforcement added.

First-parent changed paths: `include/endstone/event/server/server_list_ping_event.h`, `include/endstone/util/game_mode.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/event.py`, `python/src/endstone/util.py`, `src/endstone_core/event/server/server_list_ping_event.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/event.cpp`, `src/endstone_python/util.cpp`.

Coverage: 385 canonical first-parent patch lines; 385 across all actual parents.

<a id="commit-515"></a>
### 515. refactor: improve ping response parsing {#commit-515}

Source: [5c8573ce71d4f94e55f5f13eb7d5fe6b564626e8](https://github.com/EndstoneMC/endstone/commit/5c8573ce71d4f94e55f5f13eb7d5fe6b564626e8) · authored 2024-03-25T16:37:31Z. Actual parent(s): `a7cb51fc2d7f5b5b0a553840cf95238c3f0833a6`.

Author: **Vincent**.

Replaces sequential field extraction with split-vector indexing guarded by at least twelve fields. Numeric conversions and enum validation remain; malformed short records fail before indexing. Does not validate prefix, all numeric text, delimiters or unknown fields, and serialized output still normalizes/hardcodes portions. No parser tests accompany this revision.

First-parent changed paths: `src/endstone_core/event/server/server_list_ping_event.cpp`.

Coverage: 56 canonical first-parent patch lines; 56 across all actual parents.

<a id="commit-516"></a>
### 516. feat: add CommandContext class {#commit-516}

Source: [dfa0699c068a7d59a3b6dedc794b6ce409904e04](https://github.com/EndstoneMC/endstone/commit/dfa0699c068a7d59a3b6dedc794b6ce409904e04) · authored 2024-03-25T18:12:58Z. Actual parent(s): `5c8573ce71d4f94e55f5f13eb7d5fe6b564626e8`.

Author: **Vincent**.

Adds native CommandContext view containing command string, owned origin and version. Exposes read-only command/origin access; layout offsets are comments and size assertion is commented out. Prepares console interception but does not yet provide a setter for event command rewriting.

First-parent changed paths: `include/bedrock/command/command_context.h`.

Coverage: 45 canonical first-parent patch lines; 45 across all actual parents.

<a id="commit-517"></a>
### 517. feat: implement ServerCommandEvent {#commit-517}

Source: [5e0053aeffd79b73aac4eaf08788bf7294dd2d1e](https://github.com/EndstoneMC/endstone/commit/5e0053aeffd79b73aac4eaf08788bf7294dd2d1e) · authored 2024-03-25T18:13:38Z. Actual parent(s): `dfa0699c068a7d59a3b6dedc794b6ce409904e04`.

Author: **Vincent**.

Hooks native command execution for DedicatedServer origin, dispatches cancellable ServerCommandEvent and returns CommandsDisabled on cancellation. Other origins bypass event. Allowed path still passes original CommandContext unchanged, so event.setCommand does not rewrite execution despite mutable event API. Also normalizes static NAME and defines result layout; all platforms initially use explicit return-buffer helper, corrected for Linux in 525.

First-parent changed paths: `include/bedrock/command/command_origin.h`, `include/bedrock/command/minecraft_commands.h`, `include/endstone/event/server/server_command_event.h`, `src/endstone_runtime/bedrock/command/minecraft_commands.cpp`.

Coverage: 119 canonical first-parent patch lines; 119 across all actual parents.

<a id="commit-518"></a>
### 518. fix: remove debug printf {#commit-518}

Source: [6fe42f2481a75a4894224a0024a9e544bbfd1372](https://github.com/EndstoneMC/endstone/commit/6fe42f2481a75a4894224a0024a9e544bbfd1372) · authored 2024-03-25T18:15:06Z. Actual parent(s): `5e0053aeffd79b73aac4eaf08788bf7294dd2d1e`.

Author: **Vincent**.

Removes command-event debug printf. Eliminates unsolicited console output, including command contents, without changing dispatch/cancellation or the unchanged-context behavior.

First-parent changed paths: `src/endstone_runtime/bedrock/command/minecraft_commands.cpp`.

Coverage: 12 canonical first-parent patch lines; 12 across all actual parents.

<a id="commit-519"></a>
### 519. feat(python): add bindings for ServerCommandEvent {#commit-519}

Source: [fd0c8c64d2efd224dd5ae5ed0c101a6cb9015c1c](https://github.com/EndstoneMC/endstone/commit/fd0c8c64d2efd224dd5ae5ed0c101a6cb9015c1c) · authored 2024-03-25T18:46:05Z. Actual parent(s): `6fe42f2481a75a4894224a0024a9e544bbfd1372`.

Author: **Vincent**.

Exposes Python ServerCommandEvent, borrowed sender and mutable command property; changes native getter to value and setter to move input. Docs recommend limited interception uses and say leading slash. No host context writeback is added, so documented modifiers remain unsupported by observed execution path.

First-parent changed paths: `include/endstone/event/server/server_command_event.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/event.py`, `src/endstone_python/event.cpp`.

Coverage: 128 canonical first-parent patch lines; 128 across all actual parents.

<a id="commit-520"></a>
### 520. refactor: rename CommandFlag members {#commit-520}

Source: [e6d0159353ea92c96dd4b1c037e3ebe4c9c66975](https://github.com/EndstoneMC/endstone/commit/e6d0159353ea92c96dd4b1c037e3ebe4c9c66975) · authored 2024-03-25T21:44:28Z. Actual parent(s): `fd0c8c64d2efd224dd5ae5ed0c101a6cb9015c1c`.

Author: **Vincent**.

Renames NOT_REQUIRE_CHEAT to WITHOUT_CHEATS_ENABLED and updates registration reference, preserving bit 7. Unlike earlier ordinal 368, this named-flag edit keeps the actual value and default unchanged.

First-parent changed paths: `include/bedrock/command/command_flag.h`, `src/endstone_core/command/command_map.cpp`.

Coverage: 39 canonical first-parent patch lines; 39 across all actual parents.

<a id="commit-521"></a>
### 521. refactor: move files around {#commit-521}

Source: [cb4e2e12526baf5210d40be75fdec0bea070daae](https://github.com/EndstoneMC/endstone/commit/cb4e2e12526baf5210d40be75fdec0bea070daae) · authored 2024-03-26T11:29:59Z. Actual parent(s): `e6d0159353ea92c96dd4b1c037e3ebe4c9c66975`.

Author: **Vincent**.

Relocates actor/player/server-player headers and runtime files; exact unchanged Actor blob and include-only modifications verified. No virtual ordering, layout or behavior change; historical ABI content is reused, not reattributed as new implementation.

First-parent changed paths: `include/bedrock/level/actor/actor.h`, `include/bedrock/level/actor/mob.h`, `include/bedrock/level/actor/player.h`, `include/bedrock/server/level/player.h`, `include/bedrock/server/level/server_player.h`, `include/bedrock/server/server_player.h`, `include/bedrock/world/actor/actor.h`, `include/bedrock/world/actor/mob.h`, `src/endstone_runtime/bedrock/level/actor/player.cpp`, `src/endstone_runtime/bedrock/server/level/player.cpp`, `src/endstone_runtime/bedrock/server/level/server_player.cpp`, `src/endstone_runtime/bedrock/server/server_player.cpp`.

Coverage: 1092 canonical first-parent patch lines; 1092 across all actual parents.

<a id="commit-522"></a>
### 522. feat: add gameplay handler {#commit-522}

Source: [9b72254a7c27b7a95178c0f76a64d21bbc9678ad](https://github.com/EndstoneMC/endstone/commit/9b72254a7c27b7a95178c0f76a64d21bbc9678ad) · authored 2024-03-26T12:23:20Z. Actual parent(s): `cb4e2e12526baf5210d40be75fdec0bea070daae`.

Author: **Vincent**.

Introduces CoordinatorResult, GameplayHandlerResult and placeholder weather event plus a virtual ScriptLevelGameplayHandler declaration. This is native ABI scaffolding with provisional result field meanings; no emission yet. Later result/layout corrections must be retained rather than treating these initial names as settled semantics.

First-parent changed paths: `include/bedrock/event/gameplay_handler.h`, `include/bedrock/event/level/weather_changed_event.h`, `include/bedrock/event/script_gameplay_handler.h`.

Coverage: 85 canonical first-parent patch lines; 85 across all actual parents.

<a id="commit-525"></a>
### 525. fix: crash when invoking MinecraftCommands::executeCommand on Linux {#commit-525}

Source: [d08c0cdf9338718ed5db8dab8f66650b1b1aebd5](https://github.com/EndstoneMC/endstone/commit/d08c0cdf9338718ed5db8dab8f66650b1b1aebd5) · authored 2024-03-26T13:51:31Z. Actual parent(s): `8964d34b5cabce1274fe1537664da3b9a44df21e`.

Author: **Vincent**.

Reported Linux executeCommand crash is addressed by normal return-value call on Linux while Windows retains explicit hidden-result-buffer helper. Demonstrates platform/return-type calling-convention distinction, not proof every aggregate-return hook needs the same treatment. Both console and bypass paths change; no native test included.

First-parent changed paths: `src/endstone_runtime/bedrock/command/minecraft_commands.cpp`.

Coverage: 28 canonical first-parent patch lines; 28 across all actual parents.

<a id="commit-527"></a>
### 527. feat: hook ScriptLevelGameplayHandler::handleEvent(LevelWeatherChangedEvent &event) {#commit-527}

Source: [aadad562933654f6c8a086fb86860bbe415bc179](https://github.com/EndstoneMC/endstone/commit/aadad562933654f6c8a086fb86860bbe415bc179) · authored 2024-03-26T14:01:16Z. Actual parent(s): `5cecbfe64834cf325d3ebafb096a1752a920956e`.

Author: **Vincent**.

Adds named-original weather handler hook, using Windows decorated function macro and explicit Linux mangled name. Event dispatch is still TODO. Both platforms initially use explicit hidden return-buffer helper; 528 repairs Linux as in prior command-result correction.

First-parent changed paths: `src/endstone_runtime/bedrock/event/level/script_gameplay_handler.cpp`.

Coverage: 37 canonical first-parent patch lines; 37 across all actual parents.

<a id="commit-528"></a>
### 528. fix: crash when ScriptLevelGameplayHandler::handleEvent gets invoked on Linux {#commit-528}

Source: [46392b2f801079f22bbb32a5b360229e9a8d0717](https://github.com/EndstoneMC/endstone/commit/46392b2f801079f22bbb32a5b360229e9a8d0717) · authored 2024-03-26T14:31:20Z. Actual parent(s): `aadad562933654f6c8a086fb86860bbe415bc179`.

Author: **Vincent**.

Reported Linux weather-handler crash is repaired by normal aggregate return rather than RVO buffer helper. Windows remains unchanged. This repeats 525 calling-convention lesson for a different return type; no measured host test is present.

First-parent changed paths: `src/endstone_runtime/bedrock/event/level/script_gameplay_handler.cpp`.

Coverage: 17 canonical first-parent patch lines; 17 across all actual parents.

<a id="commit-529"></a>
### 529. feat: update LevelWeatherChangedEvent structure {#commit-529}

Source: [da6d0faff93615b0c9d7016c463d91668ee90c44](https://github.com/EndstoneMC/endstone/commit/da6d0faff93615b0c9d7016c463d91668ee90c44) · authored 2024-03-26T14:50:32Z. Actual parent(s): `46392b2f801079f22bbb32a5b360229e9a8d0717`.

Author: **Vincent**.

Replaces empty native weather event with previous/next rain and lightning booleans plus duration fields. Supplies the state necessary for selective interception, while layout remains reverse-engineered declaration evidence.

First-parent changed paths: `include/bedrock/event/level/weather_changed_event.h`.

Coverage: 17 canonical first-parent patch lines; 17 across all actual parents.

<a id="commit-530"></a>
### 530. feat: implement WeatherChangeEvent and ThunderChangeEvent {#commit-530}

Source: [63f3a786fb6cfa892d8c4571acf778068b041ac0](https://github.com/EndstoneMC/endstone/commit/63f3a786fb6cfa892d8c4571acf778068b041ac0) · authored 2024-03-26T15:32:15Z. Actual parent(s): `da6d0faff93615b0c9d7016c463d91668ee90c44`.

Author: **Vincent**.

Creates cancellable rain/thunder events, dispatches only when each state changes, and on cancellation restores that native target boolean before calling original handler. Rain and thunder are independent decisions; duration fields remain unchanged. Unlike console string mutation, this path actually writes event changes back into the native input. WeatherEvent lacks world/level identity and explicitly leaves it TODO until later level support.

First-parent changed paths: `include/endstone/event/weather/thunder_change_event.h`, `include/endstone/event/weather/weather_change_event.h`, `include/endstone/event/weather/weather_event.h`, `src/endstone_runtime/bedrock/event/level/script_gameplay_handler.cpp`.

Coverage: 194 canonical first-parent patch lines; 194 across all actual parents.

<a id="commit-531"></a>
### 531. style: format code {#commit-531}

Source: [588b22a142f23a15add7b80c09d6b5a971db8cc2](https://github.com/EndstoneMC/endstone/commit/588b22a142f23a15add7b80c09d6b5a971db8cc2) · authored 2024-03-26T15:33:29Z. Actual parent(s): `63f3a786fb6cfa892d8c4571acf778068b041ac0`.

Author: **Vincent**.

Reorders two includes in Player header; actual declarations and virtual ordering unchanged.

First-parent changed paths: `include/bedrock/level/actor/player.h`.

Coverage: 14 canonical first-parent patch lines; 14 across all actual parents.

<a id="commit-533"></a>
### 533. feat: add Details::ValueOrRef {#commit-533}

Source: [fd4276b4cb92f464112125f385c851a31b7bb032](https://github.com/EndstoneMC/endstone/commit/fd4276b4cb92f464112125f385c851a31b7bb032) · authored 2024-03-26T22:01:14Z. Actual parent(s): `f0f653a50b9d649f52816e9f589bfc8aa680468f`.

Author: **Vincent**.

Introduces Details::ValueOrRef as variant<T*, T>, representing native events either borrowed or inline. This is an ABI mirror, not evidence the host uses a standard portable serialized format; alternative order and storage layout matter.

First-parent changed paths: `include/bedrock/details.h`.

Coverage: 30 canonical first-parent patch lines; 30 across all actual parents.

<a id="commit-534"></a>
### 534. refactor: level events {#commit-534}

Source: [9c15b796423d1d72db56de325389326d4b4b1364](https://github.com/EndstoneMC/endstone/commit/9c15b796423d1d72db56de325389326d4b4b1364) · authored 2024-03-26T22:52:19Z. Actual parent(s): `fd4276b4cb92f464112125f385c851a31b7bb032`.

Author: **Vincent**.

Groups level events into variant envelopes, separates EventRef and CoordinatorResult, relocates weather handler declarations and adds provisional opaque event sizes. Immutable events use ValueOrRef<const T>; mutable weather uses nonconst T. Gameplay header references player_events before 535 supplies it. Rename similarity pairs unrelated small headers, so actual removed/added semantics were read rather than trusted as relocation.

First-parent changed paths: `include/bedrock/event/coordinator_result.h`, `include/bedrock/event/event_ref.h`, `include/bedrock/event/gameplay_handler.h`, `include/bedrock/event/level/weather_changed_event.h`, `include/bedrock/event/level_events.h`, `include/bedrock/event/script_gameplay_handler.h`, `src/endstone_runtime/bedrock/event/level/script_gameplay_handler.cpp`.

Coverage: 235 canonical first-parent patch lines; 235 across all actual parents.

<a id="commit-535"></a>
### 535. feat: add player events {#commit-535}

Source: [6b08811f855ecc6c8c18f8efbd35f2b002e52a47](https://github.com/EndstoneMC/endstone/commit/6b08811f855ecc6c8c18f8efbd35f2b002e52a47) · authored 2024-03-26T22:52:27Z. Actual parent(s): `9c15b796423d1d72db56de325389326d4b4b1364`.

Author: **Vincent**.

Adds twenty-four named player-event alternatives with guessed padding and explicit size-verification TODO. Declared event names do not yet become public Endstone events or behavioral handlers; this establishes native variant ordering and storage assumptions that 540 revises.

First-parent changed paths: `include/bedrock/event/player_events.h`.

Coverage: 123 canonical first-parent patch lines; 123 across all actual parents.

<a id="commit-536"></a>
### 536. refactor: rename enum values in CoordinatorResult {#commit-536}

Source: [57f5bef7d40cbb70602f3e8bb69a235488015f55](https://github.com/EndstoneMC/endstone/commit/57f5bef7d40cbb70602f3e8bb69a235488015f55) · authored 2024-03-26T23:09:55Z. Actual parent(s): `6b08811f855ecc6c8c18f8efbd35f2b002e52a47`.

Author: **Vincent**.

Renames CoordinatorResult Failed/Success to Reject/Default with values 0/1 preserved. Clarifies interpretation of native outcome; no host behavior change.

First-parent changed paths: `include/bedrock/event/coordinator_result.h`.

Coverage: 13 canonical first-parent patch lines; 13 across all actual parents.

<a id="commit-537"></a>
### 537. feat: hook LevelEventCoordinator::sendEvent {#commit-537}

Source: [7e1b34196700082cdbd91a93aea7bd3f90af9531](https://github.com/EndstoneMC/endstone/commit/7e1b34196700082cdbd91a93aea7bd3f90af9531) · authored 2024-03-27T00:48:30Z. Actual parent(s): `57f5bef7d40cbb70602f3e8bb69a235488015f55`.

Author: **Vincent**.

Hooks level coordinator sendEvent with temporary diagnostics, refines opaque event structures and makes game-rule-change alternative Windows-only. Adds active sizeof(LevelGameplayEvent<void>) assertion at 72, then removes it in 540. Platform-specific alternative membership affects discriminant indices as well as size; diagnostics are not proof all layouts are correct.

First-parent changed paths: `include/bedrock/event/event_coordinator.h`, `include/bedrock/event/event_ref.h`, `include/bedrock/event/level_events.h`, `include/bedrock/forward.h`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`, `src/endstone_runtime/bedrock/event/gameplay_handler.cpp`, `src/endstone_runtime/bedrock/event/level/script_gameplay_handler.cpp`.

Coverage: 294 canonical first-parent patch lines; 294 across all actual parents.

<a id="commit-538"></a>
### 538. feat: add helper function to get reference from ValueOrRef {#commit-538}

Source: [91ef3f897832d8fa944f1892a02ca6bca9b4630f](https://github.com/EndstoneMC/endstone/commit/91ef3f897832d8fa944f1892a02ca6bca9b4630f) · authored 2024-03-27T16:35:08Z. Actual parent(s): `7e1b34196700082cdbd91a93aea7bd3f90af9531`.

Author: **Vincent**.

Replaces ValueOrRef alias with wrapper exposing get(): returns inline value or dereferenced stored pointer. Default variant still permits a null pointer and noexcept assumes valid variant/pointer state. Wrapper preserves intended storage shape but no layout or lifetime tests establish host equivalence.

First-parent changed paths: `include/bedrock/details.h`.

Coverage: 25 canonical first-parent patch lines; 25 across all actual parents.

<a id="commit-539"></a>
### 539. refactor: remove debug printf {#commit-539}

Source: [a3c579ac4300fcb13766737be5efb4a4299b2ff9](https://github.com/EndstoneMC/endstone/commit/a3c579ac4300fcb13766737be5efb4a4299b2ff9) · authored 2024-03-27T16:38:14Z. Actual parent(s): `91ef3f897832d8fa944f1892a02ca6bca9b4630f`.

Author: **Vincent**.

Removes level coordinator debug printf before/after original. Native forwarding remains; new diagnostics return in 540.

First-parent changed paths: `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 12 canonical first-parent patch lines; 12 across all actual parents.

<a id="commit-540"></a>
### 540. feat: add placeholder events to ensure the correct storage size for std::variant {#commit-540}

Source: [230509d8b9720609df1943b26a6d7205816b989e](https://github.com/EndstoneMC/endstone/commit/230509d8b9720609df1943b26a6d7205816b989e) · authored 2024-03-27T16:59:18Z. Actual parent(s): `a3c579ac4300fcb13766737be5efb4a4299b2ff9`.

Author: **Vincent**.

Replaces guessed per-event payload sizes with empty named types plus a final size-forcing placeholder alternative for level/player variants. Retains known alternative indices while modeling only storage extent; Linux/Windows placeholders initially differ. Removes prior size assertion and adds std::visit logging. This narrows payload claims but still relies on matching standard-library variant layout, discriminator position and host object lifetime.

First-parent changed paths: `include/bedrock/event/level_events.h`, `include/bedrock/event/player_events.h`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 255 canonical first-parent patch lines; 255 across all actual parents.

<a id="commit-541"></a>
### 541. fix: PlayerEventPlaceHolder size {#commit-541}

Source: [b31ec55b2d91b64547d495919648503b37780eee](https://github.com/EndstoneMC/endstone/commit/b31ec55b2d91b64547d495919648503b37780eee) · authored 2024-03-27T17:36:14Z. Actual parent(s): `230509d8b9720609df1943b26a6d7205816b989e`.

Author: **Vincent**.

Increases Windows player placeholder 352→368, adds player coordinator interception and bad_variant_access diagnostics with memory dump. Dump deliberately reads sixteen bytes beyond nominal object size, a bounded diagnostic risk rather than a safe ABI validator. Catching bad_variant_access does not prove all corrupt-layout cases become exceptions. Titles understate new hook/diagnostic behavior.

First-parent changed paths: `include/bedrock/event/event_coordinator.h`, `include/bedrock/event/level_events.h`, `include/bedrock/event/player_events.h`, `include/bedrock/forward.h`, `include/bedrock/level/actor/player.h`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 155 canonical first-parent patch lines; 155 across all actual parents.

<a id="commit-542"></a>
### 542. fix: LevelEventPlaceHolder size for Linux {#commit-542}

Source: [1bcf473cdf283f99fc99d249526f32a07fab841c](https://github.com/EndstoneMC/endstone/commit/1bcf473cdf283f99fc99d249526f32a07fab841c) · authored 2024-03-27T17:43:09Z. Actual parent(s): `b31ec55b2d91b64547d495919648503b37780eee`.

Author: **Vincent**.

Corrects Linux level placeholder 64→56, aligning platform storage size, and fixes GitHub capitalization in diagnostics. Does not remove the Windows-only game-rule alternative or make variant indices identical.

First-parent changed paths: `include/bedrock/event/level_events.h`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 38 canonical first-parent patch lines; 38 across all actual parents.

<a id="commit-543"></a>
### 543. fix: PlayerEventPlaceHolder size for Linux {#commit-543}

Source: [7b9e8d5abd0fcd2d4bc6d53163986856f6fbf51e](https://github.com/EndstoneMC/endstone/commit/7b9e8d5abd0fcd2d4bc6d53163986856f6fbf51e) · authored 2024-03-27T18:05:39Z. Actual parent(s): `1bcf473cdf283f99fc99d249526f32a07fab841c`.

Author: **Vincent**.

Corrects Linux player placeholder 376→368 and removes bad_variant_access catch/report paths from both level/player hooks. std::visit now propagates its failures; unused dump helper remains. Size correction and error-handling removal are separate changes, not merely a constant update.

First-parent changed paths: `include/bedrock/event/player_events.h`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 50 canonical first-parent patch lines; 50 across all actual parents.

<a id="commit-544"></a>
### 544. feat: add more built-in events for players {#commit-544}

Source: [0f9980e6be96a61bb2525328dd2370ac701e267f](https://github.com/EndstoneMC/endstone/commit/0f9980e6be96a61bb2525328dd2370ac701e267f) · authored 2024-03-27T18:20:53Z. Actual parent(s): `7b9e8d5abd0fcd2d4bc6d53163986856f6fbf51e`.

Author: **Vincent**.

Adds result-bearing player event variant and coordinator overload, disambiguating overloaded native function pointers explicitly. New alternatives cover say/experience/interactions with placeholder216; hooks only inspect/log then forward original, without public event translation or cancellation implementation.

First-parent changed paths: `include/bedrock/event/event_coordinator.h`, `include/bedrock/event/player_events.h`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 92 canonical first-parent patch lines; 92 across all actual parents.

<a id="commit-545"></a>
### 545. feat: add mutable player event (i.e. PlayerGameModeChangeEvent) {#commit-545}

Source: [9ddf0668d1d0a97685020d1392428185306d9a67](https://github.com/EndstoneMC/endstone/commit/9ddf0668d1d0a97685020d1392428185306d9a67) · authored 2024-03-27T18:29:14Z. Actual parent(s): `0f9980e6be96a61bb2525328dd2370ac701e267f`.

Author: **Vincent**.

Adds mutable player game-mode-change envelope with opaque32 payload, and changes unspecialized PlayerGameplayEvent from empty definition to forward declaration. No coordinator emission/translation added for mutable path.

First-parent changed paths: `include/bedrock/event/player_events.h`.

Coverage: 65 canonical first-parent patch lines; 65 across all actual parents.

<a id="commit-546"></a>
### 546. refactor: suppress event debug message {#commit-546}

Source: [0b77c9e9c3910499af0e48e101b91cf9466e473e](https://github.com/EndstoneMC/endstone/commit/0b77c9e9c3910499af0e48e101b91cf9466e473e) · authored 2024-03-27T18:33:56Z. Actual parent(s): `9ddf0668d1d0a97685020d1392428185306d9a67`.

Author: **Vincent**.

Lowers coordinator diagnostic logging from info to debug, preserving visitation and native forwarding. This affects operational noise, not event availability.

First-parent changed paths: `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 30 canonical first-parent patch lines; 30 across all actual parents.

<a id="commit-547"></a>
### 547. refactor: use template for PlayerEventPlaceHolder {#commit-547}

Source: [f9296c3cea4be40182a5185f97ee32433e6aec78](https://github.com/EndstoneMC/endstone/commit/f9296c3cea4be40182a5185f97ee32433e6aec78) · authored 2024-03-27T18:56:24Z. Actual parent(s): `0b77c9e9c3910499af0e48e101b91cf9466e473e`.

Author: **Vincent**.

Replaces result-type-specific player padding specializations with size-parameterized placeholder template, retaining368/216 byte arrays. Reorders level placeholder declaration. Source representation simplification only; not new ABI validation.

First-parent changed paths: `include/bedrock/event/level_events.h`, `include/bedrock/event/player_events.h`.

Coverage: 76 canonical first-parent patch lines; 76 across all actual parents.

<a id="commit-548"></a>
### 548. feat: add ActorGameplayEvent<void> {#commit-548}

Source: [f7315c2786ed0adae4d4eba3803ae4e9d689eb43](https://github.com/EndstoneMC/endstone/commit/f7315c2786ed0adae4d4eba3803ae4e9d689eb43) · authored 2024-03-27T22:02:24Z. Actual parent(s): `f9296c3cea4be40182a5185f97ee32433e6aec78`.

Author: **Vincent**.

Adds actor event variants, provisional block envelope and actor-void interception; relocates server coordinator declarations/implementations into common event files. Existing startup/PostWorld/server-load/GIL-reset sequence is preserved. Level/player diagnostic lambdas become TODO bodies while still visiting. Added actor names are native scaffolding, not functional public callbacks; unchanged renamed level/player headers retain prior provenance.

First-parent changed paths: `include/bedrock/event/actor_event.h`, `include/bedrock/event/block_event.h`, `include/bedrock/event/event_coordinator.h`, `include/bedrock/event/gameplay_handler.h`, `include/bedrock/event/level_event.h`, `include/bedrock/event/level_events.h`, `include/bedrock/event/player_event.h`, `include/bedrock/event/player_events.h`, `include/bedrock/server/server_instance.h`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`, `src/endstone_runtime/bedrock/event/gameplay_handler.cpp`, `src/endstone_runtime/bedrock/server/server_instance.cpp`.

Coverage: 765 canonical first-parent patch lines; 765 across all actual parents.

<a id="commit-549"></a>
### 549. fix: ActorEventPlaceHolder size for Linux {#commit-549}

Source: [c62e80e2f7cf5d89298b8bbe36525b8e32579b56](https://github.com/EndstoneMC/endstone/commit/c62e80e2f7cf5d89298b8bbe36525b8e32579b56) · authored 2024-03-27T22:14:36Z. Actual parent(s): `f7315c2786ed0adae4d4eba3803ae4e9d689eb43`.

Author: **Vincent**.

Changes Linux actor placeholder304→320 while Windows stays304 and enables placeholder visitation instead of commented diagnostics. Platform size difference is explicit, contrary to earlier player/level convergence; no universal padding rule is inferred.

First-parent changed paths: `include/bedrock/event/actor_event.h`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 35 canonical first-parent patch lines; 35 across all actual parents.

<a id="commit-550"></a>
### 550. feat: add coordinator actor events {#commit-550}

Source: [ecebce5a5aea58cb3ec6d5f2101b53aa3525de31](https://github.com/EndstoneMC/endstone/commit/ecebce5a5aea58cb3ec6d5f2101b53aa3525de31) · authored 2024-03-27T22:21:19Z. Actual parent(s): `c62e80e2f7cf5d89298b8bbe36525b8e32579b56`.

Author: **Vincent**.

Adds actor result-bearing coordinator export/hook with exact overload pointer and TODO visitation, forwarding original result. Extends interception surface without public event policy.

First-parent changed paths: `include/bedrock/event/event_coordinator.h`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 37 canonical first-parent patch lines; 37 across all actual parents.

<a id="commit-551"></a>
### 551. feat: add coordinator block events {#commit-551}

Source: [05aa90a0a64893926fc0f2c3b3f67e130215f308](https://github.com/EndstoneMC/endstone/commit/05aa90a0a64893926fc0f2c3b3f67e130215f308) · authored 2024-03-27T22:42:19Z. Actual parent(s): `ecebce5a5aea58cb3ec6d5f2101b53aa3525de31`.

Author: **Vincent**.

Adds block variants with platform-specific placeholders and hooks result-bearing coordinator. Temporary type comparison uses wrapper type against underlying BlockRandomTickEvent but body contains only commented debug output, so it implements no event filtering behavior. Size/order assumptions remain native ABI declarations.

First-parent changed paths: `include/bedrock/event/block_event.h`, `include/bedrock/event/event_coordinator.h`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 101 canonical first-parent patch lines; 101 across all actual parents.

<a id="commit-552"></a>
### 552. feat: add block pattern event {#commit-552}

Source: [4b848df877d377b5f0d13b3ac834ed31b205340d](https://github.com/EndstoneMC/endstone/commit/4b848df877d377b5f0d13b3ac834ed31b205340d) · authored 2024-03-27T22:51:25Z. Actual parent(s): `05aa90a0a64893926fc0f2c3b3f67e130215f308`.

Author: **Vincent**.

Adds void block coordinator interception and removes the ineffective/commented temporary filter from result-bearing hook. Both visit with TODO bodies and forward original, not completed block pattern Endstone events.

First-parent changed paths: `include/bedrock/event/event_coordinator.h`, `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 63 canonical first-parent patch lines; 63 across all actual parents.

<a id="commit-553"></a>
### 553. refactor: remove debug prints {#commit-553}

Source: [b7f34022c199b4a8d4e5afe1cd4976d63698b57c](https://github.com/EndstoneMC/endstone/commit/b7f34022c199b4a8d4e5afe1cd4976d63698b57c) · authored 2024-03-27T22:58:22Z. Actual parent(s): `4b848df877d377b5f0d13b3ac834ed31b205340d`.

Author: **Vincent**.

Deletes already-commented debug print lines only. No runtime output or control-flow change, unlike earlier live printf removals.

First-parent changed paths: `src/endstone_runtime/bedrock/event/event_coordinator.cpp`.

Coverage: 16 canonical first-parent patch lines; 16 across all actual parents.

<a id="commit-554"></a>
### 554. feat: add item events {#commit-554}

Source: [e0807862709fcd57fcdd317000b8fdac9cc4298f](https://github.com/EndstoneMC/endstone/commit/e0807862709fcd57fcdd317000b8fdac9cc4298f) · authored 2024-03-27T23:14:39Z. Actual parent(s): `b7f34022c199b4a8d4e5afe1cd4976d63698b57c`.

Author: **Vincent**.

Defines immutable recipe/client and mutable item-use event envelopes with storage placeholders160/328. Windows size for first explicitly unchecked. Inclusion in coordinator header is not a new item coordinator hook; fields remain opaque.

First-parent changed paths: `include/bedrock/event/event_coordinator.h`, `include/bedrock/event/item_event.h`.

Coverage: 85 canonical first-parent patch lines; 85 across all actual parents.

<a id="commit-555"></a>
### 555. feat: add server events {#commit-555}

Source: [d68c146c9ebb076184b8f251058a7d2304370e66](https://github.com/EndstoneMC/endstone/commit/d68c146c9ebb076184b8f251058a7d2304370e66) · authored 2024-03-27T23:25:01Z. Actual parent(s): `e0807862709fcd57fcdd317000b8fdac9cc4298f`.

Author: **Vincent**.

Defines server leave/reload and mutable network chat event envelopes with placeholder16/chat128. Reuses ItemEventPlaceHolder and transitive includes; no native interception or public chat event behavior yet.

First-parent changed paths: `include/bedrock/event/event_coordinator.h`, `include/bedrock/event/server_event.h`.

Coverage: 60 canonical first-parent patch lines; 60 across all actual parents.

<a id="commit-556"></a>
### 556. fix: GameplayHandlerResult member variables {#commit-556}

Source: [a9f30d23933d92ad61a3abc3ca797192b2fbe0fd](https://github.com/EndstoneMC/endstone/commit/a9f30d23933d92ad61a3abc3ca797192b2fbe0fd) · authored 2024-03-27T23:37:04Z. Actual parent(s): `d68c146c9ebb076184b8f251058a7d2304370e66`.

Author: **Vincent**.

Corrects GameplayHandlerResult from bool-success plus result to typed value plus EventResult; also renames CoordinatorResult Reject→Deny and introduces separate EventResult. For CoordinatorResult, two enum-width fields replace bool-plus-enum semantics even if total size can remain eight. Layout/meaning correction must be distinguished from cosmetic naming; previous platform return-path fixes remain relevant.

First-parent changed paths: `include/bedrock/event/coordinator_result.h`, `include/bedrock/event/event_result.h`, `include/bedrock/event/gameplay_handler.h`.

Coverage: 58 canonical first-parent patch lines; 58 across all actual parents.

<a id="commit-559"></a>
### 559. refactor Spectator mode value in enum GameMode {#commit-559}

Source: [a32757a56c9210ed859b446d763546206a05b7b5](https://github.com/EndstoneMC/endstone/commit/a32757a56c9210ed859b446d763546206a05b7b5) · authored 2024-04-04T22:19:14Z. Actual parent(s): `13934efa0b3b1b39e10dd32ab9d3a01f2114c53d`.

Author: **Vincent**.

Changes public GameMode Spectator from6 to3. Numeric contract changes despite refactor title; ping enum serialization by name is separate from consumers relying on integer value. No rationale or regression test beyond source claim.

First-parent changed paths: `include/endstone/util/game_mode.h`.

Coverage: 13 canonical first-parent patch lines; 13 across all actual parents.
