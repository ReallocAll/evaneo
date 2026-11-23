<!-- retrieval: {"source_ids":["public:commit:0f1016541e898cd0817b08f3467d0354ef845156","public:commit:14a9b260dab5705f66396be3aca59c8635f2b994","public:commit:20cad3f0e5457134cae226a1fda7514a437a5e2e","public:commit:2261260ef25643418f475ec8ace2d5134c8358a0","public:commit:2ae1c53f0c562463ae85b069d825b38b9ec353bc","public:commit:30e79fe4b7a39cbd609a2a35cea43828df958b73","public:commit:3f07676cdea28492094a78182c19557dc898491d","public:commit:4af561f294c6c5d0f625d795fcee26042545985c","public:commit:50b59cad5c240344a33c88bc7b1176496c7acaed","public:commit:5301e273925bdf3fb7e2eacf50f8991ce899e931","public:commit:5fb2ac40da4cf243300076f82af701dee6963173","public:commit:64c6c4e6642b9741e246cf9e0f9f25e9a2b37470","public:commit:701b522c948a923024efa105ebc35db78f80d8d3","public:commit:965d04575b2ab2143100da12588a0800605fb65a","public:commit:aaa661e289e3403cdec5538a772f984d2d624799","public:commit:b9e0bbf62a567d6dd90efce46f8e27ba8fb9773e","public:commit:c32add9b60a221fbbaf8a3b549820c90cb68db58","public:commit:d52abb9720b7dd304709f5c04cb0011f71246d22","public:commit:d98cbab85295a93cc5318c875b66631d9f557a9b","public:commit:e376a6ec8ce795f6b23c7a559923c81f90b2f876","public:commit:e4b66563ae755a6d245fbfbe72eb66b58a8b3e01","public:commit:e7308528da3eef006d170f5f7ba35484d66bdfc3","public:commit:edf8151de7602fbf19b129192bc7df1883ef48a4","public:commit:f35849e5242d0a097f5e71bb7c971097f1a1a313","public:commit:f440c2ea1a579c1963cc177f39ae34ab11185587"],"source_type":"public","date":"2024-09-03..2024-09-12","topics":["lifetime","ffi","testing","api","diagnosis","documentation","review","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Event interception, localization and item-presence semantics {#event-interception-localization-and-item-presence-semantics}


Endstone commits 1681–1800, dated August 29–September 14, 2024.

## Intercepting an engine operation is not necessarily undoing it {#intercepting-an-engine-operation-is-not-necessarily-undoing-it}

Knockback calls the original operation first, then measures and edits its velocity effect. The initial editable absolute velocity becomes an editable delta at 1727. Cancellation restores the prior velocity, but does not undo unrelated native side effects. That distinction is a concrete way to reason about the scope of a cancellable adapter event without assuming the engine operation is transactional.

Death-message delivery changes more substantially. The first wrapper-based attempt modifies the damage source's reported message, initially failing to honor an empty override. After extraction and that condition repair, 1747 abandons the wrapper, clears the engine death manager's packet sender and takes over DeathInfo/chat delivery. The event moves after the original native death operation. The source explicitly describes preventing duplicate native delivery; it does not document why the earlier wrapper design was rejected. Global sender takeover and the native preference check are part of the resulting contract.

A brief Message-typed death-event experiment loses the original localization key when initialized from server-rendered text. The selective revert restores string event editing while preserving original key/parameters if untouched. This consequence is observable in source; it is not presented as a quoted motive for the revert. The broader Message-based CommandSender API survives. Different destinations still differ: player packets can localize client-side, console output renders server-side, and BroadcastMessageEvent flattens messages to strings. Join/quit follows the preserve-original-unless-edited approach, but the prepared original-preference query has no caller at the reviewed endpoint.

## API presence, native lookup and narrow repairs {#api-presence-native-lookup-and-narrow-repairs}

Kick handling progresses from an assumed native virtual lookup to adapter-registry lookup after a reported Linux crash, then changes missing-player behavior from throw to return. These are different failure policies, not merely equivalent refactors. Retaining filtered-message/skip flags and suppressing disconnect when no wrapper exists bounds what can be inferred about all native disconnection paths.

The empty-item sequence is another useful negative example. First add null guards; accidentally leave a raw handle uninitialized on the empty branch; repair initialization; then separately represent absence with no event item wrapper so hasItem is false. Memory initialization and API presence are distinct requirements. The prior owned-wrapper/borrowed-item distinction remains, and replacing a wrapper's type still does not imply an inventory writeback. XP progress similarly switches from an integer-derived adjustment to direct attribute assignment, with dirty notification but no general native setter-equivalence proof.

No runtime server, packet client, event callback or crash reproduction was executed. Existing source tests do not add regression assertions for these event or message chains. Native definitions are locally modeled interfaces; their correctness and the reported outcomes remain statically assessed only.

## Individual commit dispositions {#individual-commit-dispositions}

<a id="commit-1723"></a>
### Commit 1723 {#commit-1723}

2024-09-03T16:24:02Z · `c32add9b60a221fbbaf8a3b549820c90cb68db58` · feat: add Actor::applyImpulse

Adds applyImpulse, initially assigning the supplied vector to velocity. That behavior conflates an impulse with replacement velocity. The next commit changes it to addition and introduces a distinct assignment helper; this is a useful negative example of a short-lived semantic mismatch.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/c32add9b60a221fbbaf8a3b549820c90cb68db58). Classification: intermediate_behavior.

<a id="commit-1724"></a>
### Commit 1724 {#commit-1724}

2024-09-03T19:54:54Z · `5fb2ac40da4cf243300076f82af701dee6963173` · feat: add Actor::setPosDelta, fix Actor::applyImpulse

Changes applyImpulse to add the vector and introduces setPosDelta for replacement. This separates additive impulse from absolute velocity assignment. Vec3's += operator is supplied by 1725, so this intermediate source is not assumed independently buildable. No behavioral test accompanies the correction.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/5fb2ac40da4cf243300076f82af701dee6963173). Classification: behavior_correction.

<a id="commit-1725"></a>
### Commit 1725 {#commit-1725}

2024-09-03T19:55:14Z · `64c6c4e6642b9741e246cf9e0f9f25e9a2b37470` · feat: add ActorKnockbackEvent

Adds a native knockback hook that records velocity, calls the original engine function, then raises ActorKnockbackEvent. Its first interface exposes raw delta separately from editable absolute resulting velocity. Cancellation restores only the prior velocity; it does not undo other native side effects. The source actor can be absent. Vec3 += is also added here.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/64c6c4e6642b9741e246cf9e0f9f25e9a2b37470). Classification: event_hook.

<a id="commit-1726"></a>
### Commit 1726 {#commit-1726}

2024-09-03T20:04:49Z · `f440c2ea1a579c1963cc177f39ae34ab11185587` · feat: add python binding for ActorKnockbackEvent

Adds Python knockback-event properties and includes the Mob definition needed by the event. Returned actor/source objects are borrowed references, and source may be null even though the stub does not mark it optional. The binding exposes the initial absolute/raw split, which is immediately revised at 1727.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/f440c2ea1a579c1963cc177f39ae34ab11185587). Classification: binding_completion.

<a id="commit-1727"></a>
### Commit 1727 {#commit-1727}

2024-09-03T20:44:18Z · `50b59cad5c240344a33c88bc7b1176496c7acaed` · refactor: rename raw knockback to knockback in ActorKnockbackEvent

Despite a rename-oriented title, changes the editable knockback value from absolute velocity to delta and removes the public raw-knockback property. The hook now applies before+edited_delta or before on cancellation. This is a substantive event contract change, not just spelling. The already executed native operation's nonvelocity side effects remain outside cancellation.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/50b59cad5c240344a33c88bc7b1176496c7acaed). Classification: event_contract_revision.

<a id="commit-1728"></a>
### Commit 1728 {#commit-1728}

2024-09-03T22:40:29Z · `14a9b260dab5705f66396be3aca59c8635f2b994` · feat: add PlayerKickEvent

Adds cancellable PlayerKickEvent around disconnectClient and allows reason editing. It obtains the player through an assumed native virtual method, passes through when no player is found, and retains filtered_message and skip_message. Linux crashes later motivate replacement of that lookup at 1774. A changed event reason is not by itself proof that the final client sees it under every retained native flag.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/14a9b260dab5705f66396be3aca59c8635f2b994). Classification: kick_event_introduction.

<a id="commit-1729"></a>
### Commit 1729 {#commit-1729}

2024-09-03T22:55:51Z · `30e79fe4b7a39cbd609a2a35cea43828df958b73` · docs: update the docstring of PlayerKickEvent

Corrects the PlayerKickEvent reason property's documentation in the binding and generated stub. The native disconnect behavior is unchanged. No independent design lesson is inferred from the wording correction.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/30e79fe4b7a39cbd609a2a35cea43828df958b73). Classification: verified_mechanical.

<a id="commit-1730"></a>
### Commit 1730 {#commit-1730}

2024-09-04T12:08:15Z · `b9e0bbf62a567d6dd90efce46f8e27ba8fb9773e` · feat: add methods to AttributeInstance and BaseAttributeMap

Adds direct current-value assignment followed by dirty-map notification, mutable attribute lookup and a typed 16-byte dirty handle. Getter bodies move out of line. This creates the write path used by the following XP fix. The adapter does not reproduce every native clamp, callback or deduplication rule, so its scope is narrower than a fully equivalent engine setter.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/b9e0bbf62a567d6dd90efce46f8e27ba8fb9773e). Classification: attribute_write_path.

<a id="commit-1731"></a>
### Commit 1731 {#commit-1731}

2024-09-04T12:18:06Z · `f35849e5242d0a097f5e71bb7c971097f1a1a313` · fix: Player::setExpProgress

Replaces rounded XP-delta/giveExperience adjustment with direct assignment to the experience attribute, preserving the existing 0–1 range check and marking the attribute dirty. Release notes explicitly describe precision loss as the problem. This avoids quantization through integer experience, but does not establish all other XP-related state is synchronized or cover NaN input with tests.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/f35849e5242d0a097f5e71bb7c971097f1a1a313). Classification: precision_correction.

<a id="commit-1740"></a>
### Commit 1740 {#commit-1740}

2024-09-05T23:42:12Z · `e376a6ec8ce795f6b23c7a559923c81f90b2f876` · fix: duplicate death message

Replaces direct rebroadcast with an ActorDamageSource wrapper carrying a customized death message while delegating the other virtual operations. This aims to avoid duplicate native/manual messages. The override branch is initially nested under a nonempty check, so an empty event message falls back to the original source instead of suppressing it. The wrapper clone still borrows the original source. Both limitations matter before the later replacement.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/e376a6ec8ce795f6b23c7a559923c81f90b2f876). Classification: death_message_experiment.

<a id="commit-1741"></a>
### Commit 1741 {#commit-1741}

2024-09-05T23:46:24Z · `2261260ef25643418f475ec8ace2d5134c8358a0` · refactor: move ActorDamageSourceWrapper to separate header file

Extracts the same damage-source wrapper into a dedicated header and detail namespace, marks it final and qualifies the native Actor type. The delegation and borrowed-source clone semantics remain. This is organizational work on a short-lived implementation, not a new ownership solution.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/2261260ef25643418f475ec8ace2d5134c8358a0). Classification: structural_extraction.

<a id="commit-1745"></a>
### Commit 1745 {#commit-1745}

2024-09-07T17:10:25Z · `965d04575b2ab2143100da12588a0800605fb65a` · refactor: remove unnecessary forward declarations

Cleans forward declarations and includes, simplifies nested ItemDescriptor type names and introduces an empty GameRules placeholder. Crucially, it also moves custom-death-message substitution outside the nonempty logging branch, allowing an empty override to reach the wrapper. The title understates this behavior change; it must not be discarded as include-only cleanup.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/965d04575b2ab2143100da12588a0800605fb65a). Classification: mixed_refactor_and_fix.

<a id="commit-1746"></a>
### Commit 1746 {#commit-1746}

2024-09-07T18:04:59Z · `4af561f294c6c5d0f625d795fcee26042545985c` · feat: add PlayerDeathManager

Introduces a skeletal PlayerDeathManager and publisher layout plus a method to reset its packet sender. NonOwnerPointer's boolean conversion becomes isValid. The next commit adds a missing polymorphic base and shifts the death-manager offsets/size. These declarations model engine memory rather than implement a complete independent publisher system.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/4af561f294c6c5d0f625d795fcee26042545985c). Classification: native_support_model.

<a id="commit-1747"></a>
### Commit 1747 {#commit-1747}

2024-09-07T22:19:08Z · `701b522c948a923024efa105ebc35db78f80d8d3` · refactor: improve handling of custom death message

Deletes the wrapper approach. The hook clears the native death manager's sender, invokes the original death operation, fires the event afterwards, sends DeathInfo to the dead player, logs nonempty text and broadcasts only when the native death-message preference permits. Clearing the sender is not locally restored: the comment explicitly describes taking over delivery. The corrected 160/120-byte layout is an assertion/model, not reviewer-run ABI validation.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/701b522c948a923024efa105ebc35db78f80d8d3). Classification: death_message_redesign.

<a id="commit-1748"></a>
### Commit 1748 {#commit-1748}

2024-09-07T22:45:48Z · `5301e273925bdf3fb7e2eacf50f8991ce899e931` · feat: add hooks for ServerNetworkHandler::_isServerTextEnabled

Hooks _isServerTextEnabled to suppress native connection messages and reserves a special ConnectionOriginal value for querying the original setting. This prepares custom join/quit delivery. At the reviewed endpoint, a complete source search finds no caller using that reserved query, so the existence of the hook branch does not prove join/quit preference preservation.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/5301e273925bdf3fb7e2eacf50f8991ce899e931). Classification: native_message_suppression.

<a id="commit-1749"></a>
### Commit 1749 {#commit-1749}

2024-09-07T23:07:20Z · `e4b66563ae755a6d245fbfbe72eb66b58a8b3e01` · feat: add EndstoneMessage helper class

Adds common Message visitors for server-side string rendering and conversion to Translatable. Raw strings become translation strings with no parameters in the latter path, which depends on the native translation contract for passthrough. This reduces duplicated conversion logic but does not make all message destinations behave identically.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/e4b66563ae755a6d245fbfbe72eb66b58a8b3e01). Classification: message_adapter.

<a id="commit-1750"></a>
### Commit 1750 {#commit-1750}

2024-09-07T23:08:16Z · `aaa661e289e3403cdec5538a772f984d2d624799` · refactor: change the type of death message to Message

Changes death_message from string to Message and makes Translatable construction explicit. The death event is still initialized from a server-translated string, and its output unconditionally replaces the original key/parameters. Therefore unchanged messages lose their original localization representation. Commit 1752 reverts this specific API within minutes; the source does not explicitly state the reason, so the localization consequence remains an observed explanation candidate.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/aaa661e289e3403cdec5538a772f984d2d624799). Classification: reverted_api_experiment.

<a id="commit-1751"></a>
### Commit 1751 {#commit-1751}

2024-09-07T23:22:17Z · `d52abb9720b7dd304709f5c04cb0011f71246d22` · refactor: use Message instead of std::string and Translatable wherever possible

Collapses CommandSender's string and Translatable virtual overloads into Message and updates concrete senders and Python unions. Player delivery still distinguishes raw packets from localized translation packets; console delivery renders server-side. This simplifies call surfaces but changes C++ subclass/vtable requirements. The death-message experiment is adjusted again here and then reverted, while the broader Message API survives.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/d52abb9720b7dd304709f5c04cb0011f71246d22). Classification: message_api_unification.

<a id="commit-1752"></a>
### Commit 1752 {#commit-1752}

2024-09-07T23:31:57Z · `edf8151de7602fbf19b129192bc7df1883ef48a4` · revert: change the type of death message to Message

Restores death_message to string and preserves the original native translation key/parameters when the event's rendered text was not changed. Modified text clears parameters; empty text suppresses console/broadcast after DeathInfo delivery. Only the death-event experiment is reverted, not Message-based CommandSender APIs. The Python stub catches up at 1753. No explicit rationale beyond the revert title is invented.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/edf8151de7602fbf19b129192bc7df1883ef48a4). Classification: selective_reversal.

<a id="commit-1753"></a>
### Commit 1753 {#commit-1753}

2024-09-08T00:11:35Z · `d98cbab85295a93cc5318c875b66631d9f557a9b` · feat: implement join and quit messages for respective events

Implements mutable string join/quit messages while preserving Translatable originals for untouched messages and suppressing empty ones. Native connection messages were already disabled, but the original preference query is not consulted here. Broadcast APIs accept Message yet convert through string-valued BroadcastMessageEvent and send its string, so per-client localization is not preserved through that route. Also renames Translatable C++ accessors and colors translated errors. Test changes are mock signatures only.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/d98cbab85295a93cc5318c875b66631d9f557a9b). Classification: join_quit_and_broadcast_api.

<a id="commit-1762"></a>
### Commit 1762 {#commit-1762}

2024-09-09T17:35:52Z · `20cad3f0e5457134cae226a1fda7514a437a5e2e` · fix(item): check for empty item in item stack before invoking methods

Adds a native isNull interpretation and guards item operations. However, the new constructor assigns handle_ only for nonempty items, leaving the raw member uninitialized for empty items. Commit 1775 repairs this exact path. Also, isNull is richer than a bare item-pointer check, so its false result should not be generalized to every possible native-pointer invariant.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/20cad3f0e5457134cae226a1fda7514a437a5e2e). Classification: incomplete_empty_item_fix.

<a id="commit-1774"></a>
### Commit 1774 {#commit-1774}

2024-09-11T19:33:21Z · `0f1016541e898cd0817b08f3467d0354ef845156` · fix: resolve crash on Linux when ServerNetworkHandler::disconnectClient is called

The title reports a Linux disconnect crash. The patch removes assumed native virtual handshake/player-lookup slots and finds players by matching network/subclient identifiers in Endstone's registry. This trades ABI dependence for a linear adapter-owned lookup. Missing players now throw instead of passing through; 1779 changes that to return. The code still assumes a persistent identifier component for registered players, and no crash trace or runtime reproduction is included.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/0f1016541e898cd0817b08f3467d0354ef845156). Classification: disconnect_lookup_redesign.

<a id="commit-1775"></a>
### Commit 1775 {#commit-1775}

2024-09-11T22:16:54Z · `e7308528da3eef006d170f5f7ba35484d66bdfc3` · fix: resolve crash occurring when players interact with blocks without items in hand

Always initializes the borrowed item handle with either null or the native item address. This fixes 1762's empty-item branch leaving handle_ indeterminate and is explicitly associated with bare-hand interaction crashes. The source correction is direct; the reviewer did not reproduce the reported crash or run the fix.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/e7308528da3eef006d170f5f7ba35484d66bdfc3). Classification: initialization_repair.

<a id="commit-1776"></a>
### Commit 1776 {#commit-1776}

2024-09-11T22:28:08Z · `3f07676cdea28492094a78182c19557dc898491d` · fix: InteractEvent::hasItem now correctly returns false when player interacts with a block without an item

Passes no ItemStack wrapper to PlayerInteractEvent for an empty native stack, allowing hasItem to return false rather than seeing an air-like wrapper. This is a distinct API-presence correction after the constructor repair. It also adds ItemStack formatting and enable_shared_from_this to BlockState. No new behavior assertions accompany these changes.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/3f07676cdea28492094a78182c19557dc898491d). Classification: empty_value_contract_fix.

<a id="commit-1779"></a>
### Commit 1779 {#commit-1779}

2024-09-12T08:54:05Z · `2ae1c53f0c562463ae85b069d825b38b9ec353bc` · feat: improve player kick messaging and handling

Plugin kick uses the Kicked reason and does not suppress the message merely because its input is empty. The hook presents server-translated text to the event while preserving the original key when untouched. Missing-player handling changes from exception to return without calling the original disconnect, which is a meaningful behavioral tradeoff. filtered_message and incoming skip_message remain otherwise unchanged, so this is not complete normalization of every native kick path.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/2ae1c53f0c562463ae85b069d825b38b9ec353bc). Classification: kick_message_revision.

## Coverage boundary {#coverage-boundary}

Findings rely on the linked public sources; external PR/issue discussions, dependencies, and native engine internals are outside the cited evidence. Runtime and current-release behavior were not tested.
