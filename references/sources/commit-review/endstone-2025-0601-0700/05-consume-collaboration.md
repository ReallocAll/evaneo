<!-- retrieval: {"source_ids":["public:commit:07f8cb26806e7db12c24a3d36b02b97d302587ee","public:commit:09680b318cdd675aeeaf05bafae617c30d88b30b","public:commit:114057c0a1a0401c30b90a67d4311591b951e04f","public:commit:16f7e8ca59dddddb3c76874a6ec43b7ed5c64a9c","public:commit:1dcbc0eddf2ecb95c15c107d6fe86e815b9a0ec6","public:commit:1ea7741a503d79fe6b4a09fcda15bf4d46612afd","public:commit:312be22a4a5107115f4585c2d529dba95c2b0def","public:commit:3939b6b0600400fdf8d6104e44c3404ff67da2fd","public:commit:4eecd7b9f021c965a43945b7aea134f117f7dcba","public:commit:5077851868a4c32d670a23b817198b6985e00d34","public:commit:61612019a49ddbcd880b7efa0d34cb3771c7874b","public:commit:7631896584a7fb800ef53504f65ebbc7e2ebd998","public:commit:7be45aff6ad535437008f6b2826ebf13ec919937","public:commit:8ef66a9e17f2256d5cf2509f6d4b531d14010bf2","public:commit:8f8927f7048b3b60b134bcd97da9acabdc729582","public:commit:bfd37ffb9c13f821395d7bd6dc57995da4c3335d","public:commit:ce0466603bfa48d4eb06368bd73e6a7510dd721e","public:commit:d712b476df507f2bc0086bf3602814ce1d2c1baa","public:commit:dde8b100563a6749ee6562cfcf3cc7e2154c41d9","public:commit:f05225e812f86f8dfb86495401914ff1cb196de4","public:commit:f0a60dc3bc48256449ff72e38ea8c12a9062f754","public:commit:f5b312e5f5f06df6ab0bed5f9aeca610fcdb5cef","public:commit:fba493a9ceb1d694a500dec637a38c9df04e6279","public:context-commit:0baeca9a1759c98b242a69f28bec5280f2aa79af","public:context-commit:2f9962e8b7f3b200dcc97631fe0719e37f050c66","public:context-commit:36de665683102a8a6458c29f6bfd8848fcdf237f","public:context-commit:51be3939c6d42fbcfaf9baaec0c4de16d5ca3cb1","public:context-commit:5b18840f7f604f0f027c544baad391f24ebb749a","public:context-commit:5c3b877dbf72d737e2b0a10f547c7c6cae95cb2e","public:thread:EndstoneMC/endstone:188"],"source_type":"public","date":"2025-05-23..2025-05-25","topics":["lifetime","ffi","testing","build","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Consume events: collaborator review, cancellation and withdrawn replacement {#consume-events-collaborator-review-cancellation-and-withdrawn-replacement}


<a id="actual-people-and-causal-order"></a>
## Actual people and causal order {#actual-people-and-causal-order}

668 is Vincent's item gameplay-event scaffolding, with a TODO naming killcerr. Six subsequent non-target commits are authored and committed by killcerr. They first propose a nullable item event in the script ItemCompleteUse path, guard player origin, then move dispatch to Player::completeUsingItem to support cancellation. The move preserves the food/potion/milk/medicine filter initially. This inference about cancellation follows the preceding TODO and code; the commit does not provide a broader design rationale.

PR188 contains four COMMENTED review envelopes and four inline comments from wu-vincent. They request ItemStack references in two locations, correct the Windows address to39210592, and reuse getEndstoneActor rather than manufacture a fresh player wrapper. killcerr's5c3b877 applies those requests;0baeca9 removes the now-unused helper. The reviews are not APPROVED states, and the implementation remains killcerr-authored even when incorporating Wu feedback. Vincent then authors669–688.689 merges without a new resolution: merge tree equals the second parent, and both parent deltas are accounted for.

The captured PR has no explanatory body. Do not infer intent from its final patch alone. The six public commits linked below provide inspectable author attribution, messages and diffs; the historical review-state snapshot is not distributed. No explicit AI credit appears in these inspected messages or review bodies. That observation cannot establish that no AI assistance occurred.

## Cancellation becomes native state cleanup {#cancellation-becomes-native-state-cleanup}

The direct native hook eventually drops the food/name filter and dispatches for the completeUsingItem path. It reuses the existing wrapper, derives Hand/OffHand from selected container state, and on cancellation clears USINGITEM, the item-in-use stack, selected slot and item-use/movement ECS components. Duration moves into an ECS component. Vanilla item tags and WeakPtr const conversion support the trident movement marker. These are native layout and lifecycle changes, not just a new public event class.

At700 the hook dereferences fromMinecraft's result without a local null guard. fromMinecraft returns null for a null stack; whether the hook can receive that state depends on native entry invariants not established here. No reproduced null dereference is claimed. Cancellation, hand selection, duration reset and native side effects have no regression test in this slice.

## Replacement is tried, then explicitly deferred {#replacement-is-tried-then-explicitly-deferred}

The event's item storage moves from borrowed pointer to cloned ownership, then back to a borrowed pointer, then finally a borrowed const reference. A setter briefly allows replacement.685 converts the event item back to a native stack and reinstalls it before original completion.687 removes the setter and that native reinstallation, explicitly saying there is no good way to implement replacement for now and leaving it for future improvement. This is a documented boundary reduction, not permission to claim replacement works because an earlier commit or stale note says so.

The final event getter calls clone and its documentation says modifying the returned item has no effect, but EndstoneItemStack's copy constructor copies handle_. Its clone therefore owns another wrapper, not another native item; metadata application and amount mutation can still reach shared native state. This qualifies the earlier completed PR dossier's snapshot description using endpoint source. Plain ItemStack copying is different. Lifetime after the original native stack disappears is also not extended by owning the wrapper.

Documentation lags the reversal: C++ still mentions the removed setter and changed-item effects; Python read-only item retains gets-or-sets wording. Stub688 removes the setter but retains the prose. The safe historical conclusion is that explicit replacement was intentionally deferred while wrapper-isolation and documentation contracts remained unresolved.

## Reuse and practical lesson {#reuse-and-practical-lesson}

Merge689 imports exactly six killcerr context commits and twenty Vincent target commits. Exact PR188 file pairs and full hunks are reused, while intermediate revisions, review context and merge boundaries are independently read. Scoreboard's unrelated stoi→from_chars change also appears here; it checks conversion error status rather than full consumption, so this is not evidence of stricter numeric suffix rejection.

Use this case for reviewing cancellation at the actual lifecycle boundary, respecting collaborator identity, checking whether clone deep-copies a resource or only its wrapper, and withdrawing unsupported mutability honestly. The result is static source evidence, with no native server, compiler, tests or hooks executed.

## Per-commit decisions and revisions {#per-commit-decisions-and-revisions}

<a id="commit-668"></a>
### Commit 668 {#commit-668}

[09680b318cdd](https://github.com/EndstoneMC/endstone/commit/09680b318cdd675aeeaf05bafae617c30d88b30b) · 2025-05-23T17:14:39Z · feat: add hook for item events

Adds native item gameplayeventlayouts/staticasserts and mutable/const variants, coordinatorhandler ownership field, vtablehookWindows1/Linux3 registeredafterplugins. ItemCompleteUse handlerTODO explicitlyassignedkillcerr, returns true; duplicate nested call onfalse is latent untilcollaboratorfix. This scaffolds itemevent support, not a consumeeventimplementation yet. NativeABI/staticasserts notrun.


<a id="commit-669"></a>
### Commit 669 {#commit-669}

[d712b476df50](https://github.com/EndstoneMC/endstone/commit/d712b476df507f2bc0086bf3602814ce1d2c1baa) · 2025-05-25T14:42:01Z · feat: add `EquipmentSlot` enum

Adds EquipmentSlot with Hand, OffHand, Feet, Legs, Chest, Head and Body values and umbrella inclusion. Exact PR188 file identities reuse the completed source reading. This supplies the consume event's hand contract; no behavior or test by itself.


<a id="commit-670"></a>
### Commit 670 {#commit-670}

[61612019a49d](https://github.com/EndstoneMC/endstone/commit/61612019a49ddbcd880b7efa0d34cb3771c7874b) · 2025-05-25T14:42:14Z · feat: add `ENDSTONE_EVENT` macro

Adds ENDSTONE_EVENT to centralize event name/override boilerplate; exact PR188 file identity. The next commit applies it to the consume event. This is API maintenance, not a new dispatch mechanism.


<a id="commit-671"></a>
### Commit 671 {#commit-671}

[1ea7741a503d](https://github.com/EndstoneMC/endstone/commit/1ea7741a503d79fe6b4a09fcda15bf4d46612afd) · 2025-05-25T14:42:51Z · refactor: use `ENDSTONE_EVENT` macro in `PlayerItemConsumeEvent` definition

Applies ENDSTONE_EVENT and inherited Cancellable constructor shorthand to PlayerItemConsumeEvent. Removes repeated naming boilerplate while preserving cancellable PlayerEvent inheritance.


<a id="commit-672"></a>
### Commit 672 {#commit-672}

[7be45aff6ad5](https://github.com/EndstoneMC/endstone/commit/7be45aff6ad535437008f6b2826ebf13ec919937) · 2025-05-25T15:19:30Z · feat: add `ItemStack::clone`

Adds ItemStack copy/clone paths. Plain ItemStack copies metadata through the factory; EndstoneItemStack copy copies the raw native handle and then reapplies metadata. Its clone therefore creates another wrapper over the same native stack, not an independent native snapshot. The initially private copy constructor is made public in677 to permit make_unique. No clone-isolation test.


<a id="commit-673"></a>
### Commit 673 {#commit-673}

[dde8b100563a](https://github.com/EndstoneMC/endstone/commit/dde8b100563a6749ee6562cfcf3cc7e2154c41d9) · 2025-05-25T15:19:43Z · refactor: update methods in `PlayerItemConsumeEvent`

Makes consume event final, adds hand, initially clones its input into unique ownership and returns clone from getItem. setItem accepts unique ownership with null mapped to air. Wrapper cloning still aliases native state, so unique wrapper ownership does not prove item isolation. Native replacement is not applied until685.


<a id="commit-674"></a>
### Commit 674 {#commit-674}

[8ef66a9e17f2](https://github.com/EndstoneMC/endstone/commit/8ef66a9e17f2256d5cf2509f6d4b531d14010bf2) · 2025-05-25T16:00:31Z · feat: implement methods in `PlayerItemInUse`

Encapsulates native PlayerItemInUse fields and adds clearItemInUse, which clears the item, removes ECS item-use/movement components and resets selected slot. Getter/setter/duration declarations stage subsequent implementation and depend on675/676 additions.


<a id="commit-675"></a>
### Commit 675 {#commit-675}

[ce0466603bfa](https://github.com/EndstoneMC/endstone/commit/ce0466603bfa48d4eb06368bd73e6a7510dd721e) · 2025-05-25T16:03:14Z · feat: add `EntityContext::removeComponent`

Adds EntityContext::removeComponent as an EnTT registry removal wrapper. Supports cancellation cleanup; no independent higher-level policy or tests.


<a id="commit-676"></a>
### Commit 676 {#commit-676}

[bfd37ffb9c13](https://github.com/EndstoneMC/endstone/commit/bfd37ffb9c13f821395d7bd6dc57995da4c3335d) · 2025-05-25T16:03:22Z · feat: add `ItemInUseComponent`

Models ItemInUseComponent as a weak native item plus duration, with an empty movement marker. This is native ECS layout scaffolding, not evidence of ABI correctness on a running server.


<a id="commit-677"></a>
### Commit 677 {#commit-677}

[7631896584a7](https://github.com/EndstoneMC/endstone/commit/7631896584a7fb800ef53504f65ebbc7e2ebd998) · 2025-05-25T16:07:26Z · feat: improve the implementation of `PlayerItemConsumeEvent`

Implements item-in-use access and selected-slot plumbing, exposes native wrapper copy constructor, and revises direct consume hook. Removes food/name filtering, reuses the existing EndstonePlayer, derives hand from selected container, and clears USINGITEM plus ECS state on cancellation. Teleport formatting leaves final-position behavior intact. The hook assumes a nonnull native item; fromMinecraft returns null for null stacks, with no local guard before dereference. Native entry invariants were not executed or established here.


<a id="commit-678"></a>
### Commit 678 {#commit-678}

[fba493a9ceb1](https://github.com/EndstoneMC/endstone/commit/fba493a9ceb1d694a500dec637a38c9df04e6279) · 2025-05-25T16:09:36Z · feat: add python binding for `EquipmentSlot`

Exposes EquipmentSlot in Python, reusing the exact completed PR188 patch. Enum binding alone does not validate consume cancellation.


<a id="commit-679"></a>
### Commit 679 {#commit-679}

[5077851868a4](https://github.com/EndstoneMC/endstone/commit/5077851868a4c32d670a23b817198b6985e00d34) · 2025-05-25T18:06:30Z · feat: add `VanillaItemTags`

Renames native ItemTag to VanillaItemTag, inherits constructors and introduces named vanilla tags/build source. Exact PR188 identities. The trident tag supports the movement-duration marker in681.


<a id="commit-680"></a>
### Commit 680 {#commit-680}

[f5b312e5f5f0](https://github.com/EndstoneMC/endstone/commit/f5b312e5f5f06df6ab0bed5f9aeca610fcdb5cef) · 2025-05-25T18:06:50Z · feat: add templated copy constructor to WeakPtr

Adds a templated WeakPtr converting copy constructor using a reinterpreted shared control block and cross-specialization friendship. Supports const item conversion in the ECS component; the template has no type-convertibility constraint. No generalized pointer-safety claim.


<a id="commit-681"></a>
### Commit 681 {#commit-681}

[4eecd7b9f021](https://github.com/EndstoneMC/endstone/commit/4eecd7b9f021c965a43945b7aea134f117f7dcba) · 2025-05-25T18:07:14Z · feat: implement `PlayerItemInUse::setItemInUse`

Reads use duration from ECS and implements setItemInUse: stores stack/slot, sets interaction state, writes weak item/duration component and adds movement ticking for tridents. Removes the old duration field. Setter assumes a nonnull item and does not remove a prior movement marker for nontridents. It is briefly used by685;687 removes that hook call.


<a id="commit-682"></a>
### Commit 682 {#commit-682}

[3939b6b06004](https://github.com/EndstoneMC/endstone/commit/3939b6b0600400fdf8d6104e44c3404ff67da2fd) · 2025-05-25T18:07:29Z · refactor: update `PlayerItemConsumeEvent` members

Changes event item storage from owned clone to borrowed pointer, makes setItem borrow a const pointer and returns an air clone for null. Newly supplied temporary pointers could outlive their object during use; the later687 reversal removes the setter. Documentation now promises changed-item effects before685 implements them.


<a id="commit-683"></a>
### Commit 683 {#commit-683}

[8f8927f7048b](https://github.com/EndstoneMC/endstone/commit/8f8927f7048b3b60b134bcd97da9acabdc729582) · 2025-05-25T18:08:10Z · refactor: reorder methods in `ItemStackBase`

Reorders native ItemStackBase helpers; exact PR188 reading verifies substantially relocated existing nulling behavior. No independent behavior change should be inferred from the refactor title.


<a id="commit-684"></a>
### Commit 684 {#commit-684}

[312be22a4a51](https://github.com/EndstoneMC/endstone/commit/312be22a4a5107115f4585c2d529dba95c2b0def) · 2025-05-25T18:09:39Z · feat: add `Item::hasTag`

Adds native Item::hasTag and required item/component includes. EntityContext::getOrAddComponent becomes nonconst decltype(auto), accommodating EnTT's actual return type including empty components. Supporting actor/item accessor and descriptor declarations are exact PR188 matches. No runtime tag or ECS test.


<a id="commit-685"></a>
### Commit 685 {#commit-685}

[16f7e8ca59dd](https://github.com/EndstoneMC/endstone/commit/16f7e8ca59dddddb3c76874a6ec43b7ed5c64a9c) · 2025-05-25T18:18:54Z · feat: add python binding for `PlayerItemConsumeEvent`

Adds Python consume-event item/hand binding, facade, stub and docs. On the uncancelled native path, converts the event item back and installs it with prior duration/current slot before original completion. This is the brief implementation of item replacement, removed in687. No replacement/cancellation regression test.


<a id="commit-686"></a>
### Commit 686 {#commit-686}

[07f8cb26806e](https://github.com/EndstoneMC/endstone/commit/07f8cb26806e7db12c24a3d36b02b97d302587ee) · 2025-05-25T18:19:21Z · feat: add `Player::completeUsingItem` to `symbols.toml`

Adds Linux completeUsingItem symbol126909760, retains corrected Windows39210592 and repositions its table entry. Platform symbol completeness is structural; numeric address correctness was not tested.


<a id="commit-687"></a>
### Commit 687 {#commit-687}

[f05225e812f8](https://github.com/EndstoneMC/endstone/commit/f05225e812f86f8dfb86495401914ff1cb196de4) · 2025-05-25T21:00:40Z · refactor: remove `PlayerItemConsumeEvent::setItem`

Explicit message says there is no good way to implement replacement for now and leaves it for future improvement. Removes setItem and the native reinstallation path, restores a borrowed const reference and makes Python item read-only. C++ notes still mention mutation and a removed setter; Python description still says gets or sets. Getter clone still aliases a native handle. Also replaces scoreboard stoi with from_chars; exact PR188 patch checks error status, not complete text consumption, so numeric prefixes remain accepted.


<a id="commit-688"></a>
### Commit 688 {#commit-688}

[f0a60dc3bc48](https://github.com/EndstoneMC/endstone/commit/f0a60dc3bc48256449ff72e38ea8c12a9062f754) · 2025-05-25T21:04:44Z · feat: update python bindings

Updates the Python stub to remove the consume item setter. The getter's inherited stale mutation prose remains. Documentation synchronization is partial, not evidence of replacement support.


<a id="commit-689"></a>
### Commit 689 {#commit-689}

[114057c0a1a0](https://github.com/EndstoneMC/endstone/commit/114057c0a1a0401c30b90a67d4311591b951e04f) · 2025-05-25T21:06:39Z · feat: add PlayerItemConsumeEvent (#188)

Merges PR188 with tree exactly equal to its second parent. Imports six killcerr commits and twenty Vincent target commits669–688, with both parent deltas inspected and no merge resolution. Preserve killcerr authorship and Wu's review/revision roles separately. Reuses only proven PR/branch identities.


<a id="commit-690"></a>
### Commit 690 {#commit-690}

[1dcbc0eddf2e](https://github.com/EndstoneMC/endstone/commit/1dcbc0eddf2ecb95c15c107d6fe86e815b9a0ec6) · 2025-05-25T21:17:42Z · fix: add <charconv> include to scoreboard.cpp

Adds the charconv header needed by687's scoreboard conversion. Narrow compile dependency repair; no new parser contract or test.


## Imported collaborator commits {#imported-collaborator-commits}

<a id="context-2f9962e8b7f3b200dcc97631fe0719e37f050c66"></a>

### Context 2f9962e8b7f3b200dcc97631fe0719e37f050c66 {#context-2f9962e8b7f3b200dcc97631fe0719e37f050c66}

[killcerr · 2f9962e8b7f3](https://github.com/EndstoneMC/endstone/commit/2f9962e8b7f3b200dcc97631fe0719e37f050c66) · 2025-05-24T01:47:45+08:00

killcerr introduces nullable ItemStack pointer consume event and ItemCompleteUse hook restricted to food/potion/milk/medicine. Reads item before null check, reinterprets ItemInstance as ItemStack and constructs fresh EndstonePlayer wrapper; synchronous borrowed event. Initial proposal, not Wu-authored final design.


<a id="context-5b18840f7f604f0f027c544baad391f24ebb749a"></a>

### Context 5b18840f7f604f0f027c544baad391f24ebb749a {#context-5b18840f7f604f0f027c544baad391f24ebb749a}

[killcerr · 5b18840f7f60](https://github.com/EndstoneMC/endstone/commit/5b18840f7f604f0f027c544baad391f24ebb749a) · 2025-05-24T19:38:45+08:00

killcerr first guards player origin, flattens filtering and event dispatch; explicitly TODO fix cancellation. Removes duplicate nested handleEvent call inherited668, so one event dispatch. Retains fresh wrapper/pointer/ItemInstance cast.


<a id="context-36de665683102a8a6458c29f6bfd8848fcdf237f"></a>

### Context 36de665683102a8a6458c29f6bfd8848fcdf237f {#context-36de665683102a8a6458c29f6bfd8848fcdf237f}

[killcerr · 36de66568310](https://github.com/EndstoneMC/endstone/commit/36de665683102a8a6458c29f6bfd8848fcdf237f) · 2025-05-24T20:43:29+08:00

killcerr moves dispatch from scripting ItemCompleteUse to direct Player::completeUsingItem hook, preserves food/name filtering. Cancellation calls newly added stopUsingItem clearingduration/item/slot/USINGITEM. Exposes nativeitem/slot fields; scripting visitor now forwards unchanged. No authored reason beyond implementation; connection to cancellationTODO inferred.


<a id="context-51be3939c6d42fbcfaf9baaec0c4de16d5ca3cb1"></a>

### Context 51be3939c6d42fbcfaf9baaec0c4de16d5ca3cb1 {#context-51be3939c6d42fbcfaf9baaec0c4de16d5ca3cb1}

[killcerr · 51be3939c6d4](https://github.com/EndstoneMC/endstone/commit/51be3939c6d42fbcfaf9baaec0c4de16d5ca3cb1) · 2025-05-24T21:48:58+08:00

killcerr supplies Windows completeUsingItem symbol39206496; laterreviewcorrects39210592. Numericnativeaddress neverexecutedhere.


<a id="context-5c3b877dbf72d737e2b0a10f547c7c6cae95cb2e"></a>

### Context 5c3b877dbf72d737e2b0a10f547c7c6cae95cb2e {#context-5c3b877dbf72d737e2b0a10f547c7c6cae95cb2e}

[killcerr · 5c3b877dbf72](https://github.com/EndstoneMC/endstone/commit/5c3b877dbf72d737e2b0a10f547c7c6cae95cb2e) · 2025-05-24T23:32:50+08:00

killcerr implements Wu reviewrequests: nonnullItemStackreference, correctedWindows39210592, existinggetEndstoneActor wrapperidentity. Inlinescancelcleanup andoriginalcall onuncancelledpath. Keep actualauthor despite reviewerinput.


<a id="context-0baeca9a1759c98b242a69f28bec5280f2aa79af"></a>

### Context 0baeca9a1759c98b242a69f28bec5280f2aa79af {#context-0baeca9a1759c98b242a69f28bec5280f2aa79af}

[killcerr · 0baeca9a1759](https://github.com/EndstoneMC/endstone/commit/0baeca9a1759c98b242a69f28bec5280f2aa79af) · 2025-05-24T23:35:25+08:00

killcerr deletes nowunused stopUsingItem declaration/definition afterinliningcleanup. This is scopedcleanup, not changed cancellationpolicy.
