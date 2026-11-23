<!-- retrieval: {"source_ids":["public:commit:0cdc730f7d2dbb9e4221e2f3f2e4abcc11674ae0","public:commit:0ce5261e6befb28adfdaeb60d13f53bc2ce23d64","public:commit:0e40f3dce5442fc239f2be57924f03d244450de9","public:commit:18ab3c33a98079d51e2bdd1314015c888d956695","public:commit:2e55636f369cb4e2ff5f0ff7682b5d53e70325c4","public:commit:366bdb9f4fd2f1eae9095c217367f7e1f03190da","public:commit:4a1a7210c17735a5fe740555f890fdec6be8081e","public:commit:4adadc3f6828357fec6b8fd1e2e25a95257853c3","public:commit:747637a70dfafd2a128081b95731197fb140d884","public:commit:7c7ab80905b0650f603fd1cc081129df9721da6e","public:commit:912262c926d895d54727c51517c22dcf908826b2","public:commit:a7d190dee36bdf122b699feeea97adedae21e725","public:commit:b146f89a7f407cdecac13e86925a0e58f7300c82","public:commit:b5e0dcb06cc12d426028a1bc3386fd6a9ef0b83a","public:commit:be599b38b6286c06c33138b5777cdba147251c84","public:commit:c0fe8887b86fef548f24b9a889c784a27e148055","public:commit:df567c97eec113538e1f94285b223e5aa15076cc","public:commit:e219eae358211300ef574e4fc97b8be58e345bd3","public:commit:f40f8800e2e23ddb4efb2dfaea5c7ea7eec7413e"],"source_type":"public","date":"2025-02-10..2025-02-23","topics":["lifetime","concurrency","ffi","testing","api","diagnosis","documentation","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Commands, packet policy and lifecycle ordering {#commands-packet-policy-and-lifecycle-ordering}

## Commands: preserve source and revise incorrect proxies {#commands-preserve-source-and-revise-incorrect-proxies}

221 explicitly fixes issue131's inserted spaces around punctuation. It reconstructs compound parameters from the original contiguous source span instead of joining parse-tree leaves with synthetic separators; leaf IDs have surrounding quotes removed. This preserves source spelling while relying on token pointers delimiting the same live input buffer. The issue author Mih4n's reproduction and Wu's response supply problem context; no parser regression test is added here.

216–218 map VirtualCommandOrigin to a ProxiedCommandSender with caller/output-receiver and callee/underlying-origin wrappers, add polymorphic casting and Python exports.269 later marks the conversion incorrect and disables it; the API itself remains. The valid lesson is to track the reversal, not to infer the original mapping as a permanent preference.273/274 place the associated crash-fix claim under0.6.1.

PR133 explicitly lists client command refresh after operator change as broken because setPermissions became inlined/unhookable.288 implements the setter locally: update abilities, recalculate plugin permissions, then resend available commands. This supports calls through Endstone's setter; it does not prove interception of every inlined native write. Likewise285's active-player lower clamp is disabled as TODO in287 despite the latter's reorder-only title. At300 the public maximum-player API rejects negative/above200 but can request fewer than the current population.

## Initialization order and teardown {#initialization-order-and-teardown}

228 moves server/level setup to ServerScriptManager execution groups after former hooks became inlined. Static once_flags register each stage once per process; native reset destroys the locator before forwarding to the native script manager.254 moves the original runPlugins call ahead of setup, explicitly reporting a post-startup crash fix. The order is now native initialization first, Endstone listener setup second. Reinitialization after locator reset remains a boundary because the once_flags do not reset with it. This evidence supports ordering/ownership checks, not a claim that every reload lifecycle is solved.

251 fixes emote/respawn dispatch by moving those cases to the actual void-event variant visitor. The initially unknown variant slot is identified as weak ClientJoinedEventData268. The public join event is not moved in this range.300 instead replaces network/kick lookup through Endstone's online-player map with native level-user lookup, a prerequisite for reasoning about events earlier than public registration.

## Packet cancellation contracts {#packet-cancellation-contracts}

291/293 first call the original native incoming/outgoing filters and preserve any rejection. Only allowed packets reach plugin callbacks, and a native player lookup is required. Receive cancellation returns silent rejection. Send dispatch loops all recipients but immediately rejects the entire native batch when any event is cancelled, so this is not per-recipient filtering and later recipients receive no callback after that cancellation.

Both event objects hold Player& and borrowed std::string_view into shared network storage. Python data getters copy bytes, but retained C++ views or nested sends can outlive/invalidate the storage. No payload rewrite is implemented. Packet sizes, pre-login coverage, network thread affinity and reentrancy are not independently verified.300 changes lookup to native users, checking entity/component presence before converting to ServerPlayer; it does not independently make the event object owning.

294 suppresses Sentry transmission for Windows STATUS_FATAL_APP_EXIT. The endpoint handler still prints the crash message and stack first, then drops the report. This is a reporting policy, not crash prevention or complete telemetry validation. The reason is the stated category exclusion; no unrecorded incident rationale is invented.


<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}


<a id="commit-216"></a>
### 216. feat: implement `ProxiedCommandSender` {#commit-216}

[df567c97eec113538e1f94285b223e5aa15076cc](https://github.com/EndstoneMC/endstone/commit/df567c97eec113538e1f94285b223e5aa15076cc) · 2025-02-10T23:19:39Z · author Vincent.

Parents: `3b5a0c42d518c6dfa04d49258269f1425801cea0`. Full message and sources: parent 1.

Implements VirtualCommandOrigin→ProxiedCommandSender with caller from output receiver and callee from underlying origin; wrappers now own shared pointers, getters expose references. Adds native command-position/origin layouts and Python reference bindings, separates include cycles. Null nested senders are not checked before getters dereference. Existing proxy forwarding policies require full context; later269 removes this Virtual-origin mapping as incorrect, so not a final endorsed model.

Coverage: 8 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-217"></a>
### 217. feat: add ProxiedCommandSender in type caster {#commit-217}

[747637a70dfafd2a128081b95731197fb140d884](https://github.com/EndstoneMC/endstone/commit/747637a70dfafd2a128081b95731197fb140d884) · 2025-02-10T23:23:07Z · author Vincent.

Parents: `df567c97eec113538e1f94285b223e5aa15076cc`. Full message and sources: parent 1.

Adds public virtual asProxiedCommandSender and override, then extends Python polymorphic CommandSender caster. This exposes216's subtype correctly across bindings while changing public virtual interface. const accessor returns a mutable pointer via const_cast as existing API pattern; no lifetime extension.

Coverage: 3 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-218"></a>
### 218. feat: add python bindings for `ProxiedCommandSender` {#commit-218}

[f40f8800e2e23ddb4efb2dfaea5c7ea7eec7413e](https://github.com/EndstoneMC/endstone/commit/f40f8800e2e23ddb4efb2dfaea5c7ea7eec7413e) · 2025-02-10T23:26:13Z · author Vincent.

Parents: `747637a70dfafd2a128081b95731197fb140d884`. Full message and sources: parent 1.

Adds ProxiedCommandSender to public Python module export and generated-style stub with caller/callee properties. Actual pybind class landed216 and polymorphic recognition217. Full export-list change inspected; no runtime binding test.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-221"></a>
### 221. fix: correct the logic of parsing command parameters {#commit-221}

[0cdc730f7d2dbb9e4221e2f3f2e4abcc11674ae0](https://github.com/EndstoneMC/endstone/commit/0cdc730f7d2dbb9e4221e2f3f2e4abcc11674ae0) · 2025-02-12T18:47:50Z · author Vincent.

Parents: `789099ec07a12c8114fd30daec3999d5f8acd5a1`. Full message and sources: parent 1.

Explicitly fixes issue131 by replacing DFS token concatenation with source-span reconstruction: leaf ID tokens lose surrounding quotes, compound parameters copy contiguous text between first/last located leaves. This preserves original separators instead of injecting spaces; assumes token pointers delimit one valid source buffer. Adds exact Symbol equality and returns false for null output storage. No parsing test added in this commit; error/origin/version arguments remain unused.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-222"></a>
### 222. refactor: remove unused header includes {#commit-222}

[be599b38b6286c06c33138b5777cdba147251c84](https://github.com/EndstoneMC/endstone/commit/be599b38b6286c06c33138b5777cdba147251c84) · 2025-02-12T18:49:25Z · author Vincent.

Parents: `0cdc730f7d2dbb9e4221e2f3f2e4abcc11674ae0`. Full message and sources: parent 1.

Removes unused stack, Boost join, fmt/ranges and spdlog includes left by221. Complete small diff inspected; no independent behavior or engineering preference inferred.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-228"></a>
### 228. feat: replace invalid hooks due to function inlining with new ones {#commit-228}

[0ce5261e6befb28adfdaeb60d13f53bc2ce23d64](https://github.com/EndstoneMC/endstone/commit/0ce5261e6befb28adfdaeb60d13f53bc2ce23d64) · 2025-02-13T23:54:30Z · author Vincent.

Parents: `182e81aedf1e9d9aca042a1c7c28679f4a31453d`. Full message and sources: parent 1.

Explicitly replaces hooks invalidated by inlining. Verified PR133 file reuse covers server initialization through ServerScriptManager::_runPlugins execution groups, once_flags and locator reset before native script-manager reset, plus target wiring and removed coordinator detours. Residual Windows offsets fill loader/player creation targets. Player::setPermissions loses hook marker with an alternative-hook TODO; the PR records command-refresh breakage. Once_flags persist after locator destruction, so repeated in-process initialization remains a lifecycle boundary.

Coverage: 11 all-parent changed-file occurrences; 9 exact prior PR133 file-patch occurrences reused.


<a id="commit-251"></a>
### 251. fix: ensure proper firing of `PlayerRespawnEvent` and `PlayerEmoteEvent` {#commit-251}

[c0fe8887b86fef548f24b9a889c784a27e148055](https://github.com/EndstoneMC/endstone/commit/c0fe8887b86fef548f24b9a889c784a27e148055) · 2025-02-16T16:50:03Z · author Vincent.

Parents: `9eda28c67b6ed1c31fef01ad2293e1f9d7059adc`. Full message and sources: parent 1.

Moves respawn/emote handling from CoordinatorResult visitor to the void-event visitor, which actually contains those variants. Also inserts still-unknown PlayerEvent26 into the native variant sequence. Both files exactly reuse PR133; the two specific hunks were additionally inspected to establish the causal repair to the prior slice.

Coverage: 2 all-parent changed-file occurrences; 2 exact prior PR133 file-patch occurrences reused.


<a id="commit-252"></a>
### 252. chore: improve TODO comments {#commit-252}

[7c7ab80905b0650f603fd1cc081129df9721da6e](https://github.com/EndstoneMC/endstone/commit/7c7ab80905b0650f603fd1cc081129df9721da6e) · 2025-02-16T16:55:55Z · author Vincent.

Parents: `c0fe8887b86fef548f24b9a889c784a27e148055`. Full message and sources: parent 1.

Four TODOs are relabelled TODO(fixme), explicitly preserving unresolved I18n initialization, Level listener names and PlayerUI/SimpleContainer structure questions. No behavior changes or independent technique claim.

Coverage: 4 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-253"></a>
### 253. [feat] 1.21.60 support for Windows (WIP) (#133) {#commit-253}

[4adadc3f6828357fec6b8fd1e2e25a95257853c3](https://github.com/EndstoneMC/endstone/commit/4adadc3f6828357fec6b8fd1e2e25a95257853c3) · 2025-02-16T16:57:53Z · author Vincent.

Parents: `be599b38b6286c06c33138b5777cdba147251c84`, `7c7ab80905b0650f603fd1cc081129df9721da6e`. Full message and sources: parent 1, parent 2.

Merge PR133 imports the already-read Windows 1.21.60 chain 223–252. Tree equals second parent, whose delta is empty; all 103 first-parent file patches exactly equal the completed PR base/head patch. Full merge message states command permissions do not update client commands as a known issue. Vincent author and GitHub committer are preserved, with imported copyable_function external attribution separate.

Coverage: 103 all-parent changed-file occurrences; 103 exact prior PR133 file-patch occurrences reused.


<a id="commit-254"></a>
### 254. fix: prevent crashes by reinitializing event listeners after the scripting engine startup {#commit-254}

[366bdb9f4fd2f1eae9095c217367f7e1f03190da](https://github.com/EndstoneMC/endstone/commit/366bdb9f4fd2f1eae9095c217367f7e1f03190da) · 2025-02-16T20:25:44Z · author Vincent.

Parents: `4adadc3f6828357fec6b8fd1e2e25a95257853c3`. Full message and sources: parent 1.

Moves original ServerScriptManager::_runPlugins before the once-only Endstone registration block rather than after it. Message explicitly calls this a post-startup crash fix; static ordering now lets native initialization precede decorating gameplay listeners. Process-lifetime once_flags remain. No crash reproduction was run.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-269"></a>
### 269. fix: remove incorrect handling for VirtualCommandOrigin {#commit-269}

[2e55636f369cb4e2ff5f0ff7682b5d53e70325c4](https://github.com/EndstoneMC/endstone/commit/2e55636f369cb4e2ff5f0ff7682b5d53e70325c4) · 2025-02-20T00:25:16Z · author Vincent.

Parents: `abe8ff0304b0a63ca8aad4ddfc30d9d283ea27f8`. Full message and sources: parent 1.

Comments out the Virtual command-origin proxy conversion introduced216 as incorrect, so it now reaches default nullptr. ProxiedCommandSender API remains available; removing this mapping is not removing the API. Adds joined-event header dependencies. Later changelog associates this with a crash fix.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-285"></a>
### 285. refactor:`Server::setMaxPlayers` {#commit-285}

[4a1a7210c17735a5fe740555f890fdec6be8081e](https://github.com/EndstoneMC/endstone/commit/4a1a7210c17735a5fe740555f890fdec6be8081e) · 2025-02-21T10:52:29Z · author Vincent.

Parents: `c7b48fa1637106027866d78255d7688904d5d08e`. Full message and sources: parent 1.

Centralizes connection cap200 across RakPeer startup and server setters. Native setter clamps below active/in-progress count, notifies announcements and application callback on change; public setter validates negative/above-cap but ignores native clamp result. Method declarations and UUIDEMPTY arrive later286–287; intermediate state is incomplete.

Coverage: 4 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-287"></a>
### 287. refactor: reorder methods in `ServerNetworkHandler` {#commit-287}

[e219eae358211300ef574e4fc97b8be58e345bd3](https://github.com/EndstoneMC/endstone/commit/e219eae358211300ef574e4fc97b8be58e345bd3) · 2025-02-21T11:16:10Z · author Vincent.

Parents: `8f93bfc7850e21466d8ea5647bc64a15e2339400`. Full message and sources: parent 1.

Nominal method reorder also comments out active/in-progress-player lower-bound clamp as TODO. Adds actual getter/setter declarations and connection token getter, removes unused getLevel. At boundary300 max players can therefore be set below current population through valid public range; do not preserve285's temporary clamp as final behavior.

Coverage: 4 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-288"></a>
### 288. fix: fix the implementation of `Player::setPermissions` {#commit-288}

[18ab3c33a98079d51e2bdd1314015c888d956695](https://github.com/EndstoneMC/endstone/commit/18ab3c33a98079d51e2bdd1314015c888d956695) · 2025-02-21T11:51:02Z · author Vincent.

Parents: `e219eae358211300ef574e4fc97b8be58e345bd3`. Full message and sources: parent 1.

Replaces unhookable Player::setPermissions original-call path with explicit AbilitiesComponent command-permission update, then recalculates plugin permissions and resends commands. This addresses the PR133 stated client command refresh gap. It does not prove all native inlined permission writes are intercepted, and existing EndstonePlayer::setOp mapping is outside this patch.

Coverage: 5 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-291"></a>
### 291. feat(event): add DataPacketReceiveEvent {#commit-291}

[0e40f3dce5442fc239f2be57924f03d244450de9](https://github.com/EndstoneMC/endstone/commit/0e40f3dce5442fc239f2be57924f03d244450de9) · 2025-02-21T17:51:21Z · author Vincent.

Parents: `0f0de32dfb43747e8e8b2cbf36b038d8a1c80ce3`. Full message and sources: parent 1.

Introduces cancellable receive event after original native filter allows packet. Known connected player is required, data borrows receive_buffer as string_view, and cancellation returns RejectedSilently. C++ view lifetime is synchronous callback-bound; Python getter copies bytes. No packet rewrite, prelogin event guarantee, buffer-length slicing or thread-affinity validation is established. Player property documentation initially copied from block event, fixed292.

Coverage: 6 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-292"></a>
### 292. docs: fix the docs for `DataPacketReceiveEvent` {#commit-292}

[b146f89a7f407cdecac13e86925a0e58f7300c82](https://github.com/EndstoneMC/endstone/commit/b146f89a7f407cdecac13e86925a0e58f7300c82) · 2025-02-21T17:54:35Z · author Vincent.

Parents: `0e40f3dce5442fc239f2be57924f03d244450de9`. Full message and sources: parent 1.

Corrects receive-event player documentation in bindings/stub only. No runtime behavior change or second event implementation credit.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-293"></a>
### 293. feat: add `DataPacketSendEvent` {#commit-293}

[912262c926d895d54727c51517c22dcf908826b2](https://github.com/EndstoneMC/endstone/commit/912262c926d895d54727c51517c22dcf908826b2) · 2025-02-21T23:09:20Z · author Vincent.

Parents: `b146f89a7f407cdecac13e86925a0e58f7300c82`. Full message and sources: parent 1.

Adds send event after native filter accepts, iterates recipients and passes borrowed send_stream view. Cancellation at any recipient immediately rejects the entire batch and prevents callbacks to remaining recipients, not selective removal of one recipient. Python copies bytes; C++ view can be invalidated by reentrant sends. No network/reentrancy regression tests accompany event introduction.

Coverage: 6 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-294"></a>
### 294. feat: skip reporting `STATUS_FATAL_APP_EXIT` crashes on Windows {#commit-294}

[a7d190dee36bdf122b699feeea97adedae21e725](https://github.com/EndstoneMC/endstone/commit/a7d190dee36bdf122b699feeea97adedae21e725) · 2025-02-22T17:16:59Z · author Vincent.

Parents: `912262c926d895d54727c51517c22dcf908826b2`. Full message and sources: parent 1.

Extends crash-report predicate with Windows exception context and drops STATUS_FATAL_APP_EXIT from Sentry submission by releasing event and returning null. Other reports still return true. The patch suppresses a report category; it does not prevent application exit or demonstrate less crashing.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-300"></a>
### 300. feat: implement ServerNetworkHandler::_getServerPlayer {#commit-300}

[b5e0dcb06cc12d426028a1bc3386fd6a9ef0b83a](https://github.com/EndstoneMC/endstone/commit/b5e0dcb06cc12d426028a1bc3386fd6a9ef0b83a) · 2025-02-23T17:25:08Z · author Vincent.

Parents: `e115658d4237673aa9002f033debd8882452b2ec`. Full message and sources: parent 1.

Replaces Endstone player-map scan with ServerNetworkHandler::_getServerPlayer scanning native level users, checking entity/value and UserEntityIdentifierComponent then converting Actor pointer. Packet and kick hooks now use native lookup, enabling them independently of public online-player map timing. Wrong/missing native actor returns no event; conversion assumes users are ServerPlayer. No join-event timing change is implemented in this target itself.

Coverage: 4 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.
