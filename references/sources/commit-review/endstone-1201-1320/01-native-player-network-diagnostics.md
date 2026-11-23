<!-- retrieval: {"source_ids":["public:commit:0deec7b7ffe8100ad4fe5c388c1da999b4eb4e68","public:commit:1038964bc47fbabf03a8c38fb7473cde2023167b","public:commit:11bf6d4fe6be264fc68e3eeda1830b1fabd3ca7a","public:commit:19361e6ebc6ae6f90f27a6813a6e46b80e177b53","public:commit:26b4e0bc20d7a49be5ee297e4160374ac59a417b","public:commit:33eb22ca4c6afe97e067ba124aef146c0965a202","public:commit:3646eaf0ae941e86fe8e82f5e22fa5ddd9df5d52","public:commit:4f110c844c3f412992d4d333d15f57e4c15ed22a","public:commit:4f742681dc131dd3afcfa885dc2d5eacded94fe3","public:commit:76ec634339d9200c28cb2240981eb7e870699262","public:commit:8136bb2d10c2131bca7b7c232d868b30f84d1fe0","public:commit:8c860e7abe23be40550c04827bc598e69d2dbf5f","public:commit:986a56ba53699926df8abb5dd287bec77c17d4f1","public:commit:98d173b78f67767723b2622065d1df991a15e51a","public:commit:a45be5d97df5c6b3c3e282e25a03c1992be6d0b3","public:commit:c1e33ac74955d4f1993326324e02d8fe1fb4eb76","public:commit:ced870bf9624b2d73f6b40ff599e26d1ac9ec253","public:commit:d0969bf401782b649f676331382ee39458c8630a","public:commit:da289d085d571e4608b940416c843b72c4abcbee","public:commit:ed5fbc8fe16a2ab1c0521b9766872e89d4aafba5"],"source_type":"public","date":"2024-06-18..2024-06-24","topics":["lifetime","concurrency","ffi","testing","api","diagnosis","documentation","review","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native ABI, player APIs, networking and diagnosis {#native-abi-player-apis-networking-and-diagnosis}

## What this sequence establishes {#what-this-sequence-establishes}

This unit starts immediately after the prior experience/attribute scaffolding. The first correction is below the plugin API: a native BaseAttributeMap has the wrong layout, and the claimed getExp crash is addressed by adding its missing vector. The very next patch revises the Linux size again (1201–1202). The useful sequence is observation, a platform-specific model, then correction; a size assertion constrains the declared C++ representation, not the truth of every host field. The 1.21.1 port at 1210 changes the whole address map without changing its keys. Earlier manifest lookup already lacked a live version/address validation contract; this unit does not supply one.

The experience API then matures through calculation, mutation and binding changes (1211–1215). The initially added resetPlayerLevel hook is never the implemented setter route and is removed as unused at 1220. The final setters adjust deltas, reject negative level/out-of-range progress and expose a breaking exp to exp_progress rename. The total value is reconstructed from current state. It is therefore unsafe to lift the documentation's lifetime-total wording into a stronger guarantee than the code. Conversely, speed setters (1218–1219) reuse ability synchronization but do not add bounds checks. Together these commits support case-specific API reasoning, not an unqualified preference that all inputs are validated.

The networking chain is more consequential than its warning-suppression purpose might imply. A forwarding hook and native models (1205) enable a whole receive-loop replacement (1208). Positive datagrams are timestamped and dispatched; zero/error results are deallocated without the former warning path. The new loop owns termination/accounting and host callback interaction. The original proprietary loop was not available as source in this review, so parity for every error, retry and shutdown condition is unknown. The time helper uses QPC on Windows and relative wall time on Linux (1206), with neither monotonicity nor concurrency established for the latter. The later include moves at 1224 do not change that reasoning.

## Diagnostic evidence and its limits {#diagnostic-evidence-and-its-limits}

Crash reports gain environment/version context, source snippets and object-relative addresses (1203–1204), followed by Windows virtual-terminal setup (1217). Those are concrete aids for linking a user's report to a native port. The short-lived SIGSEGV registration is removed in the next patch; no motivation beyond source evolution is available. The output path uses library formatting, streams, symbol resolution and snippet retrieval, so this static reading is not proof of asynchronous signal safety. No crash was triggered, server started, ABI assertion compiled or packet captured by this review.

## Reuse guidance {#reuse-guidance}

Use this case when deciding whether a crash belongs to public API logic, native layout, symbol mapping or observability; when changing a cross-language property name; and when replacing a host hook body for a narrow behavior fix. Keep the cost of taking over a complete loop visible. The code supports explicit local mechanisms and dated revisions, not a promise that every intermediate commit builds or that the final host behavior was measured. All target commits here are attributed to Vincent by GitHub and git; imported/runtime dependency internals are not thereby his implementation.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1201"></a>
### 1201: fix: calling getExp no longer crashes {#commit-1201}

Source: [c1e33ac74955d4f1993326324e02d8fe1fb4eb76](https://github.com/EndstoneMC/endstone/commit/c1e33ac74955d4f1993326324e02d8fe1fb4eb76), 2024-06-18T16:08:07Z; git author Vincent. Disposition: corrective.

Addresses the stated getExp crash by completing BaseAttributeMap with a dirty-attribute vector and adding Windows/Linux size assertions of 88/80 bytes. This is a native-layout repair beneath the public experience getter, not a changed experience formula. The Linux estimate is corrected again immediately at 1202; the commit message reports the fix, while this review supplies no runtime reproduction.

<a id="commit-1202"></a>
### 1202: refactor: move getAttribute from Player to Actor {#commit-1202}

Source: [ed5fbc8fe16a2ab1c0521b9766872e89d4aafba5](https://github.com/EndstoneMC/endstone/commit/ed5fbc8fe16a2ab1c0521b9766872e89d4aafba5), 2024-06-18T16:32:47Z; git author Vincent. Disposition: mixed_change.

Moves getAttribute from native Player to Actor so the accessor belongs to the common actor interface. Also changes the Linux BaseAttributeMap size from 80 to 64 and the dirty vector offset from 56 to 40. These ABI corrections are behaviorally significant despite the relocation title. Windows remains 88 bytes; the final header confirms the platform-specific map layouts.

<a id="commit-1203"></a>
### 1203: feat: improve crash dump {#commit-1203}

Source: [8c860e7abe23be40550c04827bc598e69d2dbf5f](https://github.com/EndstoneMC/endstone/commit/8c860e7abe23be40550c04827bc598e69d2dbf5f), 2024-06-18T21:50:49Z; git author Vincent. Disposition: diagnostics.

Adds operating-system, Endstone/API version and description fields to crash output, plus stack source snippets. Fixes the API-version macro's trailing semicolon and initially adds Windows SIGSEGV handling. This improves the evidence available to issue reports, but no captured crash output or signal-safety validation accompanies the patch. The Windows signal choice changes again at 1204.

<a id="commit-1204"></a>
### 1204: feat: print object address in crash dump {#commit-1204}

Source: [ced870bf9624b2d73f6b40ff599e26d1ac9ec253](https://github.com/EndstoneMC/endstone/commit/ced870bf9624b2d73f6b40ff599e26d1ac9ec253), 2024-06-18T22:58:43Z; git author Vincent. Disposition: diagnostics.

Replaces default stack rendering with numbered frames containing raw and object-relative addresses, symbols, file/line/column and inline-frame markers. Color depends on stderr being a terminal; empty traces have an explicit message. Windows exception codes become hexadecimal and SIGSEGV registration from 1203 is removed. Keep that reversal separate from the stable diagnostic-format change; its reason is unstated.

<a id="commit-1205"></a>
### 1205: feat: hook RNS2_Berkley::RecvFromLoopInt {#commit-1205}

Source: [76ec634339d9200c28cb2240981eb7e870699262](https://github.com/EndstoneMC/endstone/commit/76ec634339d9200c28cb2240981eb7e870699262), 2024-06-19T09:32:14Z; git author Vincent. Disposition: staging.

Introduces a forwarding RecvFromLoopInt hook and the native socket, receive-buffer, event-handler and atomic-counter models it needs. The first hook still delegates to the original; the replacement loop arrives at 1208. Counter operations use Interlocked on Windows and GCC/Clang builtins on Linux. The Linux member-name error is repaired at 1209, so this staging commit is not asserted independently buildable.

<a id="commit-1206"></a>
### 1206: feat: add RakNet::GetTime {#commit-1206}

Source: [1038964bc47fbabf03a8c38fb7473cde2023167b](https://github.com/EndstoneMC/endstone/commit/1038964bc47fbabf03a8c38fb7473cde2023167b), 2024-06-19T10:39:37Z; git author Vincent. Disposition: substantive.

Adds microsecond timing support: Windows uses QueryPerformanceFrequency/Counter with quotient/remainder scaling, while Linux subtracts a first-call gettimeofday baseline. These are different clock semantics, and the shared initialization flag is unsynchronized. The code supports receive timestamps; it does not demonstrate monotonic Linux behavior, concurrent initialization safety or benchmarked accuracy.

<a id="commit-1207"></a>
### 1207: refactor: rename types.h to raknet_types.h {#commit-1207}

Source: [26b4e0bc20d7a49be5ee297e4160374ac59a417b](https://github.com/EndstoneMC/endstone/commit/26b4e0bc20d7a49be5ee297e4160374ac59a417b), 2024-06-19T10:40:19Z; git author Vincent. Disposition: mixed_change.

Renames the RakNet types header and updates consumers, but also adds explicit Time/TimeUS 64-bit and TimeMS 32-bit aliases. The include relocation is mechanical; the time-width declarations support 1206/1208 and are retained as a real interface change rather than hidden under the rename title.

<a id="commit-1208"></a>
### 1208: feat: reimplement RNS2_Berkley::RecvFromLoopInt to avoid printing empty packet warning {#commit-1208}

Source: [4f110c844c3f412992d4d333d15f57e4c15ed22a](https://github.com/EndstoneMC/endstone/commit/4f110c844c3f412992d4d333d15f57e4c15ed22a), 2024-06-19T10:42:19Z; git author Vincent. Disposition: substantive.

The message explicitly aims to avoid empty-packet warnings. Replaces original receive-loop execution with allocation, recvfrom, timestamp/address population, event delivery for positive byte counts, and deallocation for zero/error results. It tracks loop activity and end_threads. IPv4 and IPv6 paths are modeled. This suppresses the unwanted path by owning the loop, which also means parity with undocumented original error/backoff/shutdown behavior is not proven.

<a id="commit-1209"></a>
### 1209: fix: LocklessUint32_t {#commit-1209}

Source: [11bf6d4fe6be264fc68e3eeda1830b1fabd3ca7a](https://github.com/EndstoneMC/endstone/commit/11bf6d4fe6be264fc68e3eeda1830b1fabd3ca7a), 2024-06-19T11:30:19Z; git author Vincent. Disposition: corrective.

Repairs Linux LocklessUint32_t's use of value instead of value_. The actual increment/decrement return conventions still differ between the platform implementations, but RecvFromLoopInt ignores those return values. This is a bounded compilation repair, not evidence of a general cross-platform atomic abstraction audit.

<a id="commit-1210"></a>
### 1210: chore: support version v1.21.1 {#commit-1210}

Source: [19361e6ebc6ae6f90f27a6813a6e46b80e177b53](https://github.com/EndstoneMC/endstone/commit/19361e6ebc6ae6f90f27a6813a6e46b80e177b53), 2024-06-20T11:51:16Z; git author Vincent. Disposition: version_port.

Ports the advertised Minecraft version and symbol manifest from 1.21.0 to 1.21.1. Parsed TOML comparison verifies the identical function-key set, all 92 platform offsets changed, plus timestamp and version: 94 changed leaf values in total. Addresses and source diff were read; correctness against the proprietary server binary remains unverified.

<a id="commit-1211"></a>
### 1211: feat: add Player::resetPlayerLevel {#commit-1211}

Source: [4f742681dc131dd3afcfa885dc2d5eacded94fe3](https://github.com/EndstoneMC/endstone/commit/4f742681dc131dd3afcfa885dc2d5eacded94fe3), 2024-06-21T08:58:20Z; git author Vincent. Disposition: staging.

Adds native Player::resetPlayerLevel forwarding and one hook address per platform. The manifest otherwise changes only its timestamp. No public caller is introduced in this patch; 1220 explicitly removes the unused route. Preserve it as an observed trial, rather than claiming the eventual setters use resetPlayerLevel.

<a id="commit-1212"></a>
### 1212: feat: add Player::getXpNeededForLevelRange {#commit-1212}

Source: [98d173b78f67767723b2622065d1df991a15e51a](https://github.com/EndstoneMC/endstone/commit/98d173b78f67767723b2622065d1df991a15e51a), 2024-06-21T10:10:38Z; git author Vincent. Disposition: substantive.

Adds the piecewise experience-total helper for a level range, complementing the existing per-level experience calculation. This provides the arithmetic needed for getTotalExp at 1215. The helper is implementation groundwork rather than a change in how the host awards or persists experience; no numerical boundary tests are added here.

<a id="commit-1213"></a>
### 1213: feat: add Player::setExpProgress and Player::setExpLevel {#commit-1213}

Source: [0deec7b7ffe8100ad4fe5c388c1da999b4eb4e68](https://github.com/EndstoneMC/endstone/commit/0deec7b7ffe8100ad4fe5c388c1da999b4eb4e68), 2024-06-21T10:20:59Z; git author Vincent. Disposition: api_change.

Adds setExpProgress and setExpLevel, rejecting progress outside 0..1 and negative levels. Progress is changed through a rounded delta in experience points; levels use the native level-adjustment route. Renames getExp/exp to getExpProgress/exp_progress across the C++ API, binding and Python stub, without a compatibility alias. Initial invalid-value messages incorrectly use percent placeholders with fmt, fixed next.

<a id="commit-1214"></a>
### 1214: fix: error message for invalid values {#commit-1214}

Source: [8136bb2d10c2131bca7b7c232d868b30f84d1fe0](https://github.com/EndstoneMC/endstone/commit/8136bb2d10c2131bca7b7c232d868b30f84d1fe0), 2024-06-21T10:22:30Z; git author Vincent. Disposition: corrective.

Changes the two invalid-experience diagnostics to fmt brace placeholders so the actual rejected progress/level appears. Validation and mutation behavior from 1213 are unchanged. The repair matters to diagnosis but supplies no evidence that invalid-value paths were exercised in tests.

<a id="commit-1215"></a>
### 1215: feat: add Player::getTotalExp {#commit-1215}

Source: [da289d085d571e4608b940416c843b72c4abcbee](https://github.com/EndstoneMC/endstone/commit/da289d085d571e4608b940416c843b72c4abcbee), 2024-06-21T11:25:02Z; git author Vincent. Disposition: substantive.

Adds total-experience access by summing the level-based formula and the current progress contribution, with C++/Python exposure. Documentation calls this total experience collected over time, but the implementation derives it from present level/progress and cannot independently account for experience already spent or lost. Retain that distinction when reusing the API contract; no lifetime counter is introduced.

<a id="commit-1217"></a>
### 1217: feat: enable virtual terminal processing on Windows {#commit-1217}

Source: [986a56ba53699926df8abb5dd287bec77c17d4f1](https://github.com/EndstoneMC/endstone/commit/986a56ba53699926df8abb5dd287bec77c17d4f1), 2024-06-21T14:07:02Z; git author Vincent. Disposition: diagnostics.

Enables Windows console virtual-terminal processing before setting UTF-8 output. This supports the newly colored diagnostic/logger output. The console API return values are not checked, so the patch expresses intended terminal support rather than guaranteeing color capability for every host or redirected stream.

<a id="commit-1218"></a>
### 1218: feat: add Player::getWalkSpeed and Player::getFlySpeed {#commit-1218}

Source: [3646eaf0ae941e86fe8e82f5e22fa5ddd9df5d52](https://github.com/EndstoneMC/endstone/commit/3646eaf0ae941e86fe8e82f5e22fa5ddd9df5d52), 2024-06-21T16:21:17Z; git author Vincent. Disposition: api_change.

Adds read-only flight and walking speed accessors backed by native abilities, with C++/Python exposure. The initial default values in documentation are reversed. Treat the implementation and prose separately: 1219 corrects the defaults while adding mutation, rather than changing these getter calculations.

<a id="commit-1219"></a>
### 1219: feat: add Player::setWalkSpeed and Player::setFlySpeed {#commit-1219}

Source: [33eb22ca4c6afe97e067ba124aef146c0965a202](https://github.com/EndstoneMC/endstone/commit/33eb22ca4c6afe97e067ba124aef146c0965a202), 2024-06-21T22:53:36Z; git author Vincent. Disposition: api_change.

Adds flight/walking speed setters through base abilities and updateAbilities, reusing the earlier ability synchronization route. Corrects documented defaults to flight 0.05 and walking 0.10. The setters do not add range checks, unlike the experience setters in the same unit; this is a useful boundary against inferring a universal validation policy from 1213.

<a id="commit-1220"></a>
### 1220: refactor: remove unused Player::resetPlayerLevel {#commit-1220}

Source: [a45be5d97df5c6b3c3e282e25a03c1992be6d0b3](https://github.com/EndstoneMC/endstone/commit/a45be5d97df5c6b3c3e282e25a03c1992be6d0b3), 2024-06-23T10:32:07Z; git author Vincent. Disposition: reversal.

Removes resetPlayerLevel's declaration, forwarding implementation and two manifest entries as unused. The rest of the manifest is unchanged. This closes the 1211 trial while leaving the delta-based progress and level APIs in place. The source supports removal of unused integration; it does not disclose an external review objection or failed experiment.

<a id="commit-1224"></a>
### 1224: refactor: move RakNet headers to bedrock/deps/raknet {#commit-1224}

Source: [d0969bf401782b649f676331382ee39458c8630a](https://github.com/EndstoneMC/endstone/commit/d0969bf401782b649f676331382ee39458c8630a), 2024-06-24T08:56:50Z; git author Vincent. Disposition: verified_relocation.

Moves RakNet headers/sources into bedrock/deps/raknet and RakPeerHelper into the network area, updating dependent include paths and case. Rename-aware patches were read and old/new blob identities retained in rename-coverage.json. Nonidentical moves are limited to the observed include/layout changes; no receive-loop behavior is deliberately revised here.
