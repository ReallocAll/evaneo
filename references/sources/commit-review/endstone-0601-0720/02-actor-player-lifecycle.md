<!-- retrieval: {"source_ids":["public:commit:088bb4c915ee4504ccf1d41d86154fea38a57cb8","public:commit:0dc710ff797d247150e21c9827b8fa4d2fa5c365","public:commit:0e2a2006c5ff0ff3668bb34fc641ee332d6d7b43","public:commit:131c83baba7e100447c6974739a561142b4218b8","public:commit:15f7228222927341594145fd97f2af0846e2a622","public:commit:1b2797dd2c42627219902efb351dbd1ffb47434e","public:commit:23c6a56c43afaac621d52342f060c859a8fc10b4","public:commit:303c5406aa96444e9154c9b3c9d985715386d946","public:commit:309bb3cbcd60624078327be8f5e4e7afb0ecd75e","public:commit:30d6fc343ac75403684d66ceeddf583c04ecbd86","public:commit:3bd8be23fcd31f8cdd4d6c4b5b747c36e790c25e","public:commit:3ecfe61b8fa22fad454b0b7b8ec9f7670891e2f5","public:commit:3fd9a44c269542ba91bcf7b7eb4fc11b6c566283","public:commit:51976a722a4a2a383c88c98b5819ad5c15aa40c6","public:commit:546da3ac29b87ba7b1a670a46f15b8db22485448","public:commit:583cf0cbf23a4d74fe571f786a777d44d6e5b495","public:commit:5cab8984dc8331eb3c6b76f17cead77c569df14a","public:commit:5f10eeb972c2695e7d455a54442b646e710dde2c","public:commit:6177fbbd8fac2e57bec6c02dc71c628f73d790a3","public:commit:63da543e1ccfc7163b43a408335a04718d75e9a6","public:commit:6b02d5666674e3e716b0669cf064567ab1f025f3","public:commit:6be7069c2c3a8375f1531b0c81d38db4d11d6c51","public:commit:776e1735e16ff0e6994dcfd71aefdf487e864315","public:commit:79574bd51de6659fc256fba7fa7ac81d0cc985fc","public:commit:7cd2c8dab18ba2c6e29ac9aeabba06d938926be1","public:commit:7e3cbf5fb5063fb344c8f1caab04427a3f284cbd","public:commit:8766f58fa2f554be2a4a8c6f79207941e585ff79","public:commit:8bbe06ca3232706ae48e8ed54e4e47de6e446bcd","public:commit:90c597f1043f0c037257e6c94fc608fcb329acd6","public:commit:a2f0280fb26aeb54c8c80e06c586eb7d907edc40","public:commit:a467c37559cd241aa851721910edc1f26005c573","public:commit:a468885ff723625c2e288349815c6630be4489e8","public:commit:aa5e6e0ba918047c8ca2f9f9ebbc10493672b52c","public:commit:b8533fe5421649ba43ce4baac38c91fecec4fc97","public:commit:b8fb5c16fc7bd4b72ae934b9c8a760ad3b49a4ef","public:commit:bb666a70a4508fdfa6d62024aba51a1e49457b6e","public:commit:bf9fd5c982d94020ef9e51ad7e2645b11f80ddc1","public:commit:c0b7e205119114dcc6c961f2a5ab414d91953819","public:commit:c0b8a343abe8628ea291fc558d8a94b9fb92bbf5","public:commit:c3a9098b3c676ca9a0bde2c388d8cd4c612c979b","public:commit:c3e4f15c23e1c2834ee2bc3f62ffb3b08b5c27d8","public:commit:c6bbd884dd7861d9f704027dca263b0c09a9e3c2","public:commit:cbb780a813a939b2d1b60795783017e6887b7732","public:commit:ce531876be166ed7473a7574650ff33964caf783","public:commit:d409f286032043ae53e6e079995444191e5fa34a","public:commit:d63dcbeff6f5081b8fc2838f94c5355d1188896c","public:commit:d645fe918a8dfc70aac08f4ab0d197615d2b6ab8","public:commit:dc582260523468c735245e011b6bd6db449557a6","public:commit:de5ee93545b7cc240cdc9233a4deab0b09aa605c","public:commit:eae6c6bdb2aab339969dab4e4abbb63d81cb528b","public:commit:ecfa0f5d92779ef1d77983c83c3bf64b5e076f8a","public:commit:ee85cebd6ff028cfb8d54997ca4b61735a2a1288","public:commit:f2bca73f6fa6b1197dea1ce09ef924ffdf941561","public:commit:f5dda3a275e47fef9df6c5abd37bf7ce2f7dca25","public:commit:f9830549d6c52994eafc926e36a0cfb24cbab06f"],"source_type":"public","date":"2024-04-08..2024-04-19","topics":["lifetime","ffi","testing","api","diagnosis","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Actor and player lifecycle: maps, dimensions, ECS ownership, event timing {#actor-and-player-lifecycle-maps-dimensions-ecs-ownership-event-timing}

## Result and scope {#result-and-scope}

This range moves from empty public actor/player types to functioning borrowed wrappers, commands, messages and lifecycle events. Its central design change is explicit: EndstoneActor becomes a native ECS component “to simplify lifecycle management”; player ownership follows. That is a dated reversal of the level-owned actor map and server-owned player map introduced only days earlier. The final API reads native state instead of maintaining those parallel ownership collections. [commit 604](https://github.com/EndstoneMC/endstone/commit/0dc710ff797d247150e21c9827b8fa4d2fa5c365) [commit 605](https://github.com/EndstoneMC/endstone/commit/eae6c6bdb2aab339969dab4e4abbb63d81cb528b) [commit 623](https://github.com/EndstoneMC/endstone/commit/ce531876be166ed7473a7574650ff33964caf783) [commit 679](https://github.com/EndstoneMC/endstone/commit/cbb780a813a939b2d1b60795783017e6887b7732) [commit 705](https://github.com/EndstoneMC/endstone/commit/30d6fc343ac75403684d66ceeddf583c04ecbd86) [commit 711](https://github.com/EndstoneMC/endstone/commit/f9830549d6c52994eafc926e36a0cfb24cbab06f) [commit 717](https://github.com/EndstoneMC/endstone/commit/c3a9098b3c676ca9a0bde2c388d8cd4c612c979b)

The chain is verified causally, not just sorted by timestamps: each of the 120 commits directly parents the next. This matters because several commits are intermediate migration states with broken declarations, TODO lookup implementations or temporary forced cancellation. It would be misleading to treat every historical SHA as a polished release. All author/committer metadata in this range identifies Vincent; outside review participation is unknown, not inferred absent.

## 1. Public interfaces before concrete lifecycle {#1-public-interfaces-before-concrete-lifecycle}

The public sequence starts with Player and a borrowing PlayerEvent, then Actor→HumanActor→Player. Native lifecycle hooks initially only forward and carry TODOs. A temporary public Player directly references the native ServerPlayer; the concrete EndstonePlayer later moves that host coupling into implementation details. This separates the intended plugin surface from native representation, while all wrappers continue borrowing native objects. [commit 604](https://github.com/EndstoneMC/endstone/commit/0dc710ff797d247150e21c9827b8fa4d2fa5c365) [commit 605](https://github.com/EndstoneMC/endstone/commit/eae6c6bdb2aab339969dab4e4abbb63d81cb528b) [commit 608](https://github.com/EndstoneMC/endstone/commit/79574bd51de6659fc256fba7fa7ac81d0cc985fc) [commit 609](https://github.com/EndstoneMC/endstone/commit/309bb3cbcd60624078327be8f5e4e7afb0ecd75e) [commit 623](https://github.com/EndstoneMC/endstone/commit/ce531876be166ed7473a7574650ff33964caf783)

Server UUID lookup is initially a stub, then a map lookup, then receives duplicate-rejecting insertion and erasure. The concrete player caches UUID from the identity component and delegates its name. Registration occurs before native `_loadNewPlayer` returns; this version has no explicit rollback when native loading fails. That is an observed lifecycle gap, not evidence that the author intended failed logins to remain registered. At this stage both server lookup and events depend on the side map staying synchronized with native state. [commit 611](https://github.com/EndstoneMC/endstone/commit/ecfa0f5d92779ef1d77983c83c3bf64b5e076f8a) [commit 612](https://github.com/EndstoneMC/endstone/commit/5cab8984dc8331eb3c6b76f17cead77c569df14a) [commit 613](https://github.com/EndstoneMC/endstone/commit/f5dda3a275e47fef9df6c5abd37bf7ce2f7dca25) [commit 623](https://github.com/EndstoneMC/endstone/commit/ce531876be166ed7473a7574650ff33964caf783)

The first real join/quit behavior is clear about order. Native initial spawn completes before join dispatch, then available commands are sent. Quit dispatch occurs before server-map erase and native disconnect. The borrowed wrapper is usable during synchronous callback execution but is destroyed by erase immediately afterward. The event is noncancellable and carries no mutable join/quit message. Login remains TODO even after later ownership changes. [commit 625](https://github.com/EndstoneMC/endstone/commit/6be7069c2c3a8375f1531b0c81d38db4d11d6c51) [commit 710](https://github.com/EndstoneMC/endstone/commit/90c597f1043f0c037257e6c94fc608fcb329acd6)

## 2. CommandSender and permissions become real player behavior {#2-commandsender-and-permissions-become-real-player-behavior}

Actor gains CommandSender behavior. Generic actors initially have no-op message methods, a placeholder name, and one static permission base shared across all generic actor wrappers. Human actors gain a per-instance permission base; multiple inheritance is bridged by explicit overrides. Deleting ServerOperator and moving its methods to Permissible simplifies the interface graph, but one following commit repairs the now-stale actor operator helper. These are small steps in the same causal change, not separate complete permission systems. [commit 626](https://github.com/EndstoneMC/endstone/commit/7cd2c8dab18ba2c6e29ac9aeabba06d938926be1) [commit 627](https://github.com/EndstoneMC/endstone/commit/3ecfe61b8fa22fad454b0b7b8ec9f7670891e2f5) [commit 628](https://github.com/EndstoneMC/endstone/commit/b8533fe5421649ba43ce4baac38c91fecec4fc97) [commit 629](https://github.com/EndstoneMC/endstone/commit/303c5406aa96444e9154c9b3c9d985715386d946)

The endpoint still contains useful counterexamples. Generic actor permission attachments share the static base. Its null operator context means false `isOp` and no-op `setOp`; this is verified from full context. Human `op_` is not initialized in its constructor. Concrete players override operator queries using native command permission and map `setOp(true)` to Any while `isOp` treats Any as false. That inversion persists through ordinal 720. These facts limit claims of a coherent completed permission API; they are not promoted into a broad security audit. [commit 630](https://github.com/EndstoneMC/endstone/commit/a467c37559cd241aa851721910edc1f26005c573) [commit 633](https://github.com/EndstoneMC/endstone/commit/0e2a2006c5ff0ff3668bb34fc641ee332d6d7b43)

The command execution path first begins using the actual wrapper, then repairs the wrong UUID source. Later the client-visible available-command filtering replaces `DummyPlayerSender` with that same real player object. This is a meaningful progression from a snapshot of operator status toward plugin attachment-aware checks. The source still resends commands on native permission changes without explicitly recalculating the player's cached permission map in that hook. Existing default-before-attachment insertion semantics also persist in the permission base. Thus “uses real Player” is supported; “all permission changes are fully synchronized” is not. [commit 637](https://github.com/EndstoneMC/endstone/commit/51976a722a4a2a383c88c98b5819ad5c15aa40c6) [commit 638](https://github.com/EndstoneMC/endstone/commit/ee85cebd6ff028cfb8d54997ca4b61735a2a1288) [commit 647](https://github.com/EndstoneMC/endstone/commit/d63dcbeff6f5081b8fc2838f94c5355d1188896c) [commit 708](https://github.com/EndstoneMC/endstone/commit/7e3cbf5fb5063fb344c8f1caab04427a3f284cbd)

Messaging moves from TODO through native packet-factory construction to raw/popup/tip methods. Names also move from a generic placeholder to native CommandUtils and later make HumanActor use Actor naming rather than a separate native Player reference. The refactor removes redundant stored native references without making generic actor messaging functional. [commit 639](https://github.com/EndstoneMC/endstone/commit/6b02d5666674e3e716b0669cf064567ab1f025f3) [commit 641](https://github.com/EndstoneMC/endstone/commit/63da543e1ccfc7163b43a408335a04718d75e9a6) [commit 643](https://github.com/EndstoneMC/endstone/commit/bf9fd5c982d94020ef9e51ad7e2645b11f80ddc1) [commit 706](https://github.com/EndstoneMC/endstone/commit/776e1735e16ff0e6994dcfd71aefdf487e864315)

## 3. Actor ownership starts in level maps {#3-actor-ownership-starts-in-level-maps}

ActorManager insertion and Actor::remove are explored as lifecycle boundaries. The removal hook briefly moves to ActorManager's deletion-reference method, then returns to Actor::remove. The patches provide no detailed explanation for this selection, so the report preserves the alternatives without inventing a reason. Public runtime-ID queries and native owner/identity components support the initial tracking strategy. [commit 672](https://github.com/EndstoneMC/endstone/commit/23c6a56c43afaac621d52342f060c859a8fc10b4) [commit 674](https://github.com/EndstoneMC/endstone/commit/3bd8be23fcd31f8cdd4d6c4b5b747c36e790c25e) [commit 676](https://github.com/EndstoneMC/endstone/commit/c0b8a343abe8628ea291fc558d8a94b9fb92bbf5) [commit 679](https://github.com/EndstoneMC/endstone/commit/cbb780a813a939b2d1b60795783017e6887b7732)

Level owns unique_ptr wrappers indexed by runtime ID and returns borrowed pointers. After native insertion succeeds, a nonplayer actor is associated with a level identified by the native level ID; removal erases its wrapper before forwarding. Players remain in the server map, so the initial level actor list excludes them. This design creates at least two synchronization obligations: match native spawn/removal, and move wrappers when actors change dimensions. The code later explicitly leaves the latter as TODO. [commit 679](https://github.com/EndstoneMC/endstone/commit/cbb780a813a939b2d1b60795783017e6887b7732) [commit 680](https://github.com/EndstoneMC/endstone/commit/546da3ac29b87ba7b1a670a46f15b8db22485448) [commit 701](https://github.com/EndstoneMC/endstone/commit/15f7228222927341594145fd97f2af0846e2a622)

The separate actor owner-component lookup first handles absent components but assumes a nonnull owner, and uses `isAlive` as an acknowledged approximation of “not removed.” A later helper named `isRemoved` still returns `!isAlive`; renaming does not resolve the approximation. The new null-owner check is real progress, but no source evidence justifies equating all dead and removed host states. [commit 682](https://github.com/EndstoneMC/endstone/commit/131c83baba7e100447c6974739a561142b4218b8) [commit 683](https://github.com/EndstoneMC/endstone/commit/6177fbbd8fac2e57bec6c02dc71c628f73d790a3) [commit 705](https://github.com/EndstoneMC/endstone/commit/30d6fc343ac75403684d66ceeddf583c04ecbd86)

## 4. Spawn cancellation changes from prevention to compensation {#4-spawn-cancellation-changes-from-prevention-to-compensation}

The first implemented cancellable spawn event runs before native insertion. It creates a temporary EndstoneActor wrapper for the callback, returns nullptr if cancelled, and creates a different wrapper for the level map after successful insertion. Therefore a callback's wrapper identity is not the same persistent object stored afterward. The following revision moves native insertion first, dispatches against one wrapper and either despawns on cancellation or transfers that same wrapper into the map. This repairs identity continuity on the success path at the cost of making cancellation compensating rather than preemptive. [commit 684](https://github.com/EndstoneMC/endstone/commit/1b2797dd2c42627219902efb351dbd1ffb47434e) [commit 685](https://github.com/EndstoneMC/endstone/commit/c6bbd884dd7861d9f704027dca263b0c09a9e3c2)

The intermediate revision also unconditionally sets the event cancelled after dispatch, forcing every handled spawn to despawn. The Python-binding commit removes that line. Its title alone would hide the native behavioral repair; the actual diff shows it. The docs continue saying a cancelled actor will not spawn, whereas implementation now lets native insertion happen before despawn. No test or discussion in this range establishes that those observable effects are equivalent. [commit 685](https://github.com/EndstoneMC/endstone/commit/c6bbd884dd7861d9f704027dca263b0c09a9e3c2) [commit 686](https://github.com/EndstoneMC/endstone/commit/a468885ff723625c2e288349815c6630be4489e8)

Removal events have an explicit narrower contract: monitoring only, noncancellable, no actor modification during/after the event, and not for players. Initially the callback precedes wrapper erase and native removal. After ECS ownership, it precedes native removal but wrapper destruction is delegated to the component lifecycle. Python properties use borrowed references; those policies do not authorize retention after native destruction. [commit 687](https://github.com/EndstoneMC/endstone/commit/de5ee93545b7cc240cdc9233a4deab0b09aa605c) [commit 705](https://github.com/EndstoneMC/endstone/commit/30d6fc343ac75403684d66ceeddf583c04ecbd86)

At the endpoint, spawn moves again from ActorManager insertion to `ServerLevel::_postReloadActorAdded`. Native original executes first, players are skipped, nonplayer callbacks run, and cancellation calls `despawn`. The new initialization-reason enum names loaded/spawned/born/transformed/updated/event/legacy states, but the hook simply forwards the reason and does not filter or expose a spawn cause. The transition is observed; no claim is made that all creation paths are covered or that reload is intentionally equivalent to a fresh spawn. [commit 719](https://github.com/EndstoneMC/endstone/commit/bb666a70a4508fdfa6d62024aba51a1e49457b6e) [commit 720](https://github.com/EndstoneMC/endstone/commit/d645fe918a8dfc70aac08f4ab0d197615d2b6ab8)

## 5. Dimensions make parallel bookkeeping more expensive {#5-dimensions-make-parallel-bookkeeping-more-expensive}

EndstoneLevel initially wraps a native Level. It becomes a wrapper for a native Level plus a specific Dimension; startup gets or creates all three vanilla dimensions and adds each wrapper before forwarding the level-initialized notification. Overworld uses the original name, while other names initially have hardcoded suffixes and later use native `VanillaDimensions::toString`. Time still delegates to the shared native Level, so this is not three independent world clocks. [commit 696](https://github.com/EndstoneMC/endstone/commit/8bbe06ca3232706ae48e8ed54e4e47de6e446bcd) [commit 703](https://github.com/EndstoneMC/endstone/commit/d409f286032043ae53e6e079995444191e5fa34a)

The actor-map code at first continues looking up the unsuffixed native level name and explicitly marks dimension matching unfinished. Actor::setDimension carries a map-transfer TODO. These are concrete costs of maintaining a parallel per-dimension collection. The next ownership redesign removes the map and that transfer obligation. Connecting those facts as an explanation is an inference supported by adjacent code; the author's only explicit reason is simplifying lifecycle management. [commit 696](https://github.com/EndstoneMC/endstone/commit/8bbe06ca3232706ae48e8ed54e4e47de6e446bcd) [commit 701](https://github.com/EndstoneMC/endstone/commit/15f7228222927341594145fd97f2af0846e2a622) [commit 705](https://github.com/EndstoneMC/endstone/commit/30d6fc343ac75403684d66ceeddf583c04ecbd86)

## 6. ECS ownership, temporary regressions, restored read APIs {#6-ecs-ownership-temporary-regressions-restored-read-apis}

`getOrAddComponent` allows a wrapper to be lazily attached to the native entity. In 705 generic actor wrappers move there; level maps and add/remove methods disappear. `getActors` becomes an empty TODO temporarily. This is not an uninterrupted monotonic feature addition. Actor removal can now obtain a wrapper on demand without a previously tracked map entry. [commit 704](https://github.com/EndstoneMC/endstone/commit/da999e5a4aa24599f2f8d57ae19ed234f50ecf0a) [commit 705](https://github.com/EndstoneMC/endstone/commit/30d6fc343ac75403684d66ceeddf583c04ecbd86)

Players follow in 708–711. Getter implementation, declaration, lifecycle callers and server ownership removal land in separate commits. The intermediate implementation references a private Actor context and a constructor restricted to ServerPlayer; cleanup in 712 exposes context to derived Player, broadens the concrete constructor to native Player, disambiguates native/public classes and deletes wrapper copying/moving. Server `getPlayer` temporarily returns nullptr. These repairs are causally linked, and static source evidence is enough to mark intermediate incompleteness without claiming a build was run. [commit 708](https://github.com/EndstoneMC/endstone/commit/7e3cbf5fb5063fb344c8f1caab04427a3f284cbd) [commit 709](https://github.com/EndstoneMC/endstone/commit/5f10eeb972c2695e7d455a54442b646e710dde2c) [commit 710](https://github.com/EndstoneMC/endstone/commit/90c597f1043f0c037257e6c94fc608fcb329acd6) [commit 711](https://github.com/EndstoneMC/endstone/commit/f9830549d6c52994eafc926e36a0cfb24cbab06f) [commit 712](https://github.com/EndstoneMC/endstone/commit/3fd9a44c269542ba91bcf7b7eb4fc11b6c566283)

Read APIs then recover by consulting native state. `getActors` enumerates native entities, filters absent/removed contexts and dimension identity, and lazily returns component wrappers. Its first revision still rejects player entities through the generic getter; the next unifies dispatch to EndstonePlayer for players and generic EndstoneActor otherwise. Server UUID lookup calls native Level::getPlayer and returns the component wrapper. Three dimension wrappers can query the same underlying native Level more than once, but ownership is no longer duplicated in the server. [commit 714](https://github.com/EndstoneMC/endstone/commit/3e1d05c68ebddeabaea484a66b811429d654019f) [commit 715](https://github.com/EndstoneMC/endstone/commit/dc582260523468c735245e011b6bd6db449557a6) [commit 716](https://github.com/EndstoneMC/endstone/commit/8766f58fa2f554be2a4a8c6f79207941e585ff79) [commit 717](https://github.com/EndstoneMC/endstone/commit/c3a9098b3c676ca9a0bde2c388d8cd4c612c979b)

The design gain is specific: entity lifecycle owns wrapper identity, and enumeration derives from native state instead of synchronized side maps. The boundary remains borrowed native references, foreign registry ABI, server-service availability during component lifetime, and synchronous callback contracts. No destruction-order test, retained-Python-reference test, cancellation integration test or dimensional-transfer test is added in this range. Existing normal server shutdown still resets the server under the GIL; the new component ownership does not by itself prove ordering against that teardown.

## Evidence discipline {#evidence-discipline}

The direct motive is lifecycle simplification. Other explanations above are labeled inference or observed sequence. Negative examples are retained because they prevent overstating completeness, not to infer negligence or enduring preference. Per-commit entries preserve every distinct change, including mechanical path moves, temporary regressions and their repairs. Endpoint contexts and canonical hashes are separately audited; no native host or upstream tests were executed.

## Per-commit dispositions {#per-commit-dispositions}

<a id="commit-604"></a>
### 604. feat: add headers for Player and PlayerEvent {#commit-604}

Source: [0dc710ff797d247150e21c9827b8fa4d2fa5c365](https://github.com/EndstoneMC/endstone/commit/0dc710ff797d247150e21c9827b8fa4d2fa5c365); parent `ea94c5d3efdec0bf090d6a060aaa27a13e179277`. Authored 2024-04-08T12:45:07Z. Disposition: small-semantic.

Introduces empty public Player and abstract PlayerEvent borrowing Player reference. No join/quit emission or lifetime ownership yet.

<a id="commit-605"></a>
### 605. feat: add base class Actor {#commit-605}

Source: [eae6c6bdb2aab339969dab4e4abbb63d81cb528b](https://github.com/EndstoneMC/endstone/commit/eae6c6bdb2aab339969dab4e4abbb63d81cb528b); parent `0dc710ff797d247150e21c9827b8fa4d2fa5c365`. Authored 2024-04-08T13:00:11Z. Disposition: small-semantic.

Introduces polymorphic Actor→HumanActor→Player public hierarchy with name query on human/player. Native player-event header receives missing result include. This defines API scaffolding, not concrete wrapper behavior.

<a id="commit-608"></a>
### 608. feat: add and hook ServerPlayer::disconnect {#commit-608}

Source: [79574bd51de6659fc256fba7fa7ac81d0cc985fc](https://github.com/EndstoneMC/endstone/commit/79574bd51de6659fc256fba7fa7ac81d0cc985fc); parent `ccd3201e883cfa2b3d8e71eaaaafd451e905fd63`. Authored 2024-04-08T15:12:05Z. Disposition: meaningful.

Hooks disconnect and relocates native ServerPlayer header. Adds borrowed native ServerPlayer into public Player temporarily, coupling public API to host declaration. Join/quit remain TODO in native lifecycle hooks; coordinator branches become empty. Concrete events and wrapper separation follow623/625.

<a id="commit-609"></a>
### 609. feat: hook ServerNetworkHandler::_loadNewPlayer {#commit-609}

Source: [309bb3cbcd60624078327be8f5e4e7afb0ecd75e](https://github.com/EndstoneMC/endstone/commit/309bb3cbcd60624078327be8f5e4e7afb0ecd75e); parent `79574bd51de6659fc256fba7fa7ac81d0cc985fc`. Authored 2024-04-08T15:30:16Z. Disposition: small-semantic.

Adds ServerNetworkHandler::_loadNewPlayer hook forwarding original with player/login TODOs, while reorganizing actor headers and includes. Merely acquiring server does not create a wrapper or login event.

<a id="commit-611"></a>
### 611. feat: add getPlayer method to Server {#commit-611}

Source: [ecfa0f5d92779ef1d77983c83c3bf64b5e076f8a](https://github.com/EndstoneMC/endstone/commit/ecfa0f5d92779ef1d77983c83c3bf64b5e076f8a); parent `bc550407258cd9d1905e852e6e93d6615e9c04cc`. Authored 2024-04-08T16:00:58Z. Disposition: small-semantic.

Adds public Server UUID lookup and matching mock method, but EndstoneServer implementation returns nullptr TODO. Also repairs stale native player include from relocation. API declaration and functional lookup are separate milestones.

<a id="commit-612"></a>
### 612. feat: implement getPlayer in class `EndstoneServer` {#commit-612}

Source: [5cab8984dc8331eb3c6b76f17cead77c569df14a](https://github.com/EndstoneMC/endstone/commit/5cab8984dc8331eb3c6b76f17cead77c569df14a); parent `ecfa0f5d92779ef1d77983c83c3bf64b5e076f8a`. Authored 2024-04-08T16:09:45Z. Disposition: meaningful.

Implements player lookup through UUID-keyed unique_ptr map; adds bytewise UUID equality needed for unordered_map and simplifies utility names/types. Map owns wrappers and returns borrowed pointers, but insertion/removal arrive613.

<a id="commit-613"></a>
### 613. feat: add addPlayer and removePlayer method {#commit-613}

Source: [f5dda3a275e47fef9df6c5abd37bf7ce2f7dca25](https://github.com/EndstoneMC/endstone/commit/f5dda3a275e47fef9df6c5abd37bf7ce2f7dca25); parent `5cab8984dc8331eb3c6b76f17cead77c569df14a`. Authored 2024-04-08T16:20:30Z. Disposition: meaningful.

Adds duplicate-rejecting player insertion and erase-by-UUID, plus public unique ID query. UUID gains two signed64-bit parts overlay and sizeof16 assertion. This verifies local size only, not byte-order correspondence or safe host-object ownership.

<a id="commit-623"></a>
### 623. feat: player creation and removal {#commit-623}

Source: [ce531876be166ed7473a7574650ff33964caf783](https://github.com/EndstoneMC/endstone/commit/ce531876be166ed7473a7574650ff33964caf783); parent `32583cf734e46750d9ee0cceac69ba0095102b77`. Authored 2024-04-09T13:19:29Z. Disposition: meaningful.

Creates concrete EndstonePlayer borrowing ServerPlayer, moving host details out of public Player interface. Constructor requires identity component and terminates if absent; caches UUID and delegates name. Network load hook inserts wrapper before original returns and does not roll back on false; disconnect erases wrapper before original. Spawn/disconnect lookup assumes identity and wrapper exist; join/quit still TODO. This establishes server-map ownership, later replaced by ECS ownership in705/711.

<a id="commit-625"></a>
### 625. feat: add PlayerJoinEvent and PlayerQuitEvent {#commit-625}

Source: [6be7069c2c3a8375f1531b0c81d38db4d11d6c51](https://github.com/EndstoneMC/endstone/commit/6be7069c2c3a8375f1531b0c81d38db4d11d6c51); parent `a20c7d8c5ce788743d091030f4b98e93f1f9d8c6`. Authored 2024-04-09T13:57:18Z. Disposition: meaningful.

Adds noncancellable PlayerJoin/Quit events borrowing Player. Initial spawn calls native original before join dispatch and command resend; disconnect dispatches quit before server-map erase and native original. Wrapper is valid during synchronous quit dispatch, destroyed immediately afterward; no mutable join/quit messages or general retained-reference lifetime guarantee.

<a id="commit-626"></a>
### 626. feat: add EndstoneActor which implements CommandSender {#commit-626}

Source: [7cd2c8dab18ba2c6e29ac9aeabba06d938926be1](https://github.com/EndstoneMC/endstone/commit/7cd2c8dab18ba2c6e29ac9aeabba06d938926be1); parent `6be7069c2c3a8375f1531b0c81d38db4d11d6c51`. Authored 2024-04-09T14:24:50Z. Disposition: meaningful.

Actor becomes CommandSender. EndstoneActor borrows server/native actor, initially no-op messaging and placeholder name. All nonhuman actors share one static PermissibleBase and a false/no-op operator provider. Shared attachment/permission state is a scoped counterexample to per-actor isolation, not evidence of an intentional policy rationale.

<a id="commit-627"></a>
### 627. refactor: merge ServerOperator class methods into Permissible, delete ServerOperator class {#commit-627}

Source: [3ecfe61b8fa22fad454b0b7b8ec9f7670891e2f5](https://github.com/EndstoneMC/endstone/commit/3ecfe61b8fa22fad454b0b7b8ec9f7670891e2f5); parent `7cd2c8dab18ba2c6e29ac9aeabba06d938926be1`. Authored 2024-04-09T15:32:22Z. Disposition: meaningful.

Moves operator methods into Permissible and deletes ServerOperator. PermissibleBase now accepts Permissible pointer as operator/parent context, falling back to itself for parent. This simplifies interface graph but temporarily leaves EndstoneActor referring to removed ServerOperator until628.

<a id="commit-628"></a>
### 628. refactor: actor classes and remove ActorServerOperator {#commit-628}

Source: [b8533fe5421649ba43ce4baac38c91fecec4fc97](https://github.com/EndstoneMC/endstone/commit/b8533fe5421649ba43ce4baac38c91fecec4fc97); parent `3ecfe61b8fa22fad454b0b7b8ec9f7670891e2f5`. Authored 2024-04-09T15:39:07Z. Disposition: small-semantic.

Repairs preceding interface deletion by removing ActorServerOperator and constructing shared actor PermissibleBase with null operator context. Permission-state sharing remains; this is not per-actor permission ownership. Endpoint context verifies null isOp returns false and setOp is a no-op.

<a id="commit-629"></a>
### 629. feat: add HumanActor class {#commit-629}

Source: [303c5406aa96444e9154c9b3c9d985715386d946](https://github.com/EndstoneMC/endstone/commit/303c5406aa96444e9154c9b3c9d985715386d946); parent `b8533fe5421649ba43ce4baac38c91fecec4fc97`. Authored 2024-04-09T15:39:51Z. Disposition: meaningful.

Introduces EndstoneHumanActor with multiple inheritance and explicit forwarding bridges, borrowed native player and per-instance PermissibleBase. Name delegates native player; local op_ is not initialized in this change. setOp stores/recalculates human permissions, but concrete player later overrides operator policy. Message forwarding still reaches actor no-op.

<a id="commit-630"></a>
### 630. feat: implement permission-related methods in Player class {#commit-630}

Source: [a467c37559cd241aa851721910edc1f26005c573](https://github.com/EndstoneMC/endstone/commit/a467c37559cd241aa851721910edc1f26005c573); parent `303c5406aa96444e9154c9b3c9d985715386d946`. Authored 2024-04-09T15:56:16Z. Disposition: meaningful.

Concrete player adopts EndstoneHumanActor and explicit forwarding bridges across duplicate public inheritance paths. Player isOp remains false TODO; setOp maps true to Any and false to GameDirectors, opposite expected operator meaning. Native permission hook resends commands, without an explicit permission-cache recalculation in this patch. This is an incomplete stage, not a polished policy design.

<a id="commit-631"></a>
### 631. refactor: improve TODO notes {#commit-631}

Source: [aa5e6e0ba918047c8ca2f9f9ebbc10493672b52c](https://github.com/EndstoneMC/endstone/commit/aa5e6e0ba918047c8ca2f9f9ebbc10493672b52c); parent `a467c37559cd241aa851721910edc1f26005c573`. Authored 2024-04-09T15:58:05Z. Disposition: mechanical.

Adds TODO labels to existing empty messaging/dependency placeholders; no executable change.

<a id="commit-633"></a>
### 633. feat: implement EndstonePlayer::isOp {#commit-633}

Source: [0e2a2006c5ff0ff3668bb34fc641ee332d6d7b43](https://github.com/EndstoneMC/endstone/commit/0e2a2006c5ff0ff3668bb34fc641ee332d6d7b43); parent `13cae071330a65124a21a0c7e920ae1d7dd7f5b1`. Authored 2024-04-09T16:19:08Z. Disposition: meaningful.

Adds abilities/permission-handler native declarations, but actual player isOp queries command permission level and treats any non-Any as operator. Prior setOp mapping remains inverted. Abilities structure addition is not used to prove policy semantics or a fix to setter behavior.

<a id="commit-636"></a>
### 636. feat: add header for TextPacket in player.cpp {#commit-636}

Source: [a2f0280fb26aeb54c8c80e06c586eb7d907edc40](https://github.com/EndstoneMC/endstone/commit/a2f0280fb26aeb54c8c80e06c586eb7d907edc40); parent `3fcc871e2bc4de5ac73dbc2d4b24e8d1d6f2d418`. Authored 2024-04-09T16:30:26Z. Disposition: small-semantic.

Includes TextPacket in player implementation in preparation for messaging; sendMessage remains TODO.

<a id="commit-637"></a>
### 637. feat: use Player instance as the CommandSender for CommandOriginType::Player {#commit-637}

Source: [51976a722a4a2a383c88c98b5819ad5c15aa40c6](https://github.com/EndstoneMC/endstone/commit/51976a722a4a2a383c88c98b5819ad5c15aa40c6); parent `a2f0280fb26aeb54c8c80e06c586eb7d907edc40`. Authored 2024-04-09T16:37:06Z. Disposition: meaningful.

Player-origin commands now resolve real EndstonePlayer by origin UUID and execute against its permissions/attachments; unknown players log and stop, while nonplayer origins retain adapter. Fixes error-log argument order. Origin UUID is the wrong identity domain for this lookup, corrected immediately638.

<a id="commit-638"></a>
### 638. fix: command cannot be executed with Player being the sender {#commit-638}

Source: [ee85cebd6ff028cfb8d54997ca4b61735a2a1288](https://github.com/EndstoneMC/endstone/commit/ee85cebd6ff028cfb8d54997ca4b61735a2a1288); parent `51976a722a4a2a383c88c98b5819ad5c15aa40c6`. Authored 2024-04-09T22:51:31Z. Disposition: meaningful.

Explicit command-execution failure fix changes lookup key from command-origin UUID to entity user-identity component UUID. Wrapper-missing guard remains, but entity/component are dereferenced without null checks. This shows identity-domain correction, not merely an interchangeable UUID API choice.

<a id="commit-639"></a>
### 639. feat: implement EndstonePlayer::sendMessage {#commit-639}

Source: [6b02d5666674e3e716b0669cf064567ab1f025f3](https://github.com/EndstoneMC/endstone/commit/6b02d5666674e3e716b0669cf064567ab1f025f3); parent `ee85cebd6ff028cfb8d54997ca4b61735a2a1288`. Authored 2024-04-10T00:08:23Z. Disposition: meaningful.

Implements sendMessage via native MinecraftPackets factory, explicit shared_ptr RVO forwarding, TextPacket SystemMessage and network send. Using host factory avoids constructing an incomplete local native virtual object. Names packet fields and default markers; no network integration test establishes layout at runtime.

<a id="commit-640"></a>
### 640. refactor: clean up code {#commit-640}

Source: [b8fb5c16fc7bd4b72ae934b9c8a760ad3b49a4ef](https://github.com/EndstoneMC/endstone/commit/b8fb5c16fc7bd4b72ae934b9c8a760ad3b49a4ef); parent `6b02d5666674e3e716b0669cf064567ab1f025f3`. Authored 2024-04-10T00:18:07Z. Disposition: mechanical.

Adds nodiscard to name override and clarifies sendCommands comment; executable behavior unchanged.

<a id="commit-641"></a>
### 641. feat: add sendPopup and sendTip to Player {#commit-641}

Source: [63da543e1ccfc7163b43a408335a04718d75e9a6](https://github.com/EndstoneMC/endstone/commit/63da543e1ccfc7163b43a408335a04718d75e9a6); parent `b8fb5c16fc7bd4b72ae934b9c8a760ad3b49a4ef`. Authored 2024-04-10T08:46:11Z. Disposition: meaningful.

Adds raw-message, popup and tip methods using native packet factory. Existing sendMessage delegates raw-message, changing its packet type from SystemMessage to Raw as well as extending API. No translation/formatting layer introduced.

<a id="commit-643"></a>
### 643. feat: add CommandUtils and implement EndstoneActor::getName {#commit-643}

Source: [bf9fd5c982d94020ef9e51ad7e2645b11f80ddc1](https://github.com/EndstoneMC/endstone/commit/bf9fd5c982d94020ef9e51ad7e2645b11f80ddc1); parent `3a3c1d71a6a0d20b962ce3033d099b30ad06a72f`. Authored 2024-04-10T08:57:56Z. Disposition: small-semantic.

Adds native CommandUtils actor-name forwarding with explicit string return convention; EndstoneActor name changes from placeholder to native-derived. Actor messaging remains no-op.

<a id="commit-647"></a>
### 647. refactor: add getEndstonePlayer and simplify codes {#commit-647}

Source: [d63dcbeff6f5081b8fc2838f94c5355d1188896c](https://github.com/EndstoneMC/endstone/commit/d63dcbeff6f5081b8fc2838f94c5355d1188896c); parent `6f5e7beecb96095c5282370f06da1e6eaa660d7b`. Authored 2024-04-10T11:01:46Z. Disposition: meaningful.

Centralizes native Player→wrapper UUID lookup; command path now checks entity isPlayer before cast but still assumes entity/component nonnull. Lifecycle hooks reuse helper, with server-map ownership unchanged. Adds const component access that still returns mutable pointer.

<a id="commit-672"></a>
### 672. feat: hook ActorManager::addActorEntity for ActorSpawnEvent {#commit-672}

Source: [23c6a56c43afaac621d52342f060c859a8fc10b4](https://github.com/EndstoneMC/endstone/commit/23c6a56c43afaac621d52342f060c859a8fc10b4); parent `2a69c9d289df638477182df97ef74f2dc2b8da3e`. Authored 2024-04-13T01:19:57Z. Disposition: small-semantic.

Adds ActorManager addActorEntity hook and owner/context layout mirrors, but spawn cancellation/wrapper insertion remain TODO and original receives context by value. Comments propose returning nullptr on cancellation, an alternative later replaced by post-add despawn compensation. Coordinator diagnostic visitors remain commented.

<a id="commit-674"></a>
### 674. feat: add hook for Actor::remove {#commit-674}

Source: [3bd8be23fcd31f8cdd4d6c4b5b747c36e790c25e](https://github.com/EndstoneMC/endstone/commit/3bd8be23fcd31f8cdd4d6c4b5b747c36e790c25e); parent `4ad9e3883e42abb6ebbbbb0caecd09c65acc081c`. Authored 2024-04-13T17:12:01Z. Disposition: small-semantic.

Adds native virtual Actor::remove hook forwarding by explicit decorated symbol; public remove event remains TODO. First removal interception candidate, replaced676 then restored679.

<a id="commit-675"></a>
### 675. refactor: update ActorGameplayEvent and OwnerStorageEntity {#commit-675}

Source: [088bb4c915ee4504ccf1d41d86154fea38a57cb8](https://github.com/EndstoneMC/endstone/commit/088bb4c915ee4504ccf1d41d86154fea38a57cb8); parent `3bd8be23fcd31f8cdd4d6c4b5b747c36e790c25e`. Authored 2024-04-15T09:56:01Z. Disposition: mechanical.

Renames OwnerStorageEntity context field and corrects variant-index comments from1-based to0-based; variant alternatives/layout unchanged.

<a id="commit-676"></a>
### 676. feat: add RuntimeIDComponent and ActorUniqueIDComponent {#commit-676}

Source: [c0b8a343abe8628ea291fc558d8a94b9fb92bbf5](https://github.com/EndstoneMC/endstone/commit/c0b8a343abe8628ea291fc558d8a94b9fb92bbf5); parent `088bb4c915ee4504ccf1d41d86154fea38a57cb8`. Authored 2024-04-15T11:25:43Z. Disposition: meaningful.

Adds runtime/unique ID components and temporarily replaces Actor::remove interception with ActorManager removal-reference hook. Spawn hook now calls original first but comments still describe pre-spawn cancellation; neither event actually emitted. Hook-point selection remains exploratory.

<a id="commit-677"></a>
### 677. feat: add Actor::getRuntimeID {#commit-677}

Source: [c3e4f15c23e1c2834ee2bc3f62ffb3b08b5c27d8](https://github.com/EndstoneMC/endstone/commit/c3e4f15c23e1c2834ee2bc3f62ffb3b08b5c27d8); parent `c0b8a343abe8628ea291fc558d8a94b9fb92bbf5`. Authored 2024-04-15T11:33:30Z. Disposition: small-semantic.

Native runtime-ID query dereferences RuntimeIDComponent without absence guard; component existence is assumed.

<a id="commit-678"></a>
### 678. feat: add getRuntimeId to endstone::Actor {#commit-678}

Source: [583cf0cbf23a4d74fe571f786a777d44d6e5b495](https://github.com/EndstoneMC/endstone/commit/583cf0cbf23a4d74fe571f786a777d44d6e5b495); parent `c3e4f15c23e1c2834ee2bc3f62ffb3b08b5c27d8`. Authored 2024-04-15T11:39:06Z. Disposition: small-semantic.

Adds public signed runtime-ID query and forwards through actor/human/player concrete inheritance paths. Public pure-virtual interface expands; no Python binding here.

<a id="commit-679"></a>
### 679. feat: extend EndstoneLevel with actor management methods {#commit-679}

Source: [cbb780a813a939b2d1b60795783017e6887b7732](https://github.com/EndstoneMC/endstone/commit/cbb780a813a939b2d1b60795783017e6887b7732); parent `583cf0cbf23a4d74fe571f786a777d44d6e5b495`. Authored 2024-04-15T13:43:08Z. Disposition: meaningful.

Creates level-owned unique_ptr actor map with duplicate/missing-ID logging and borrowed list/query outputs. Restores Actor::remove hook and deletes manager-removal hook, reversing676. Actual insertion/removal still TODO until680; ownership design should not be inferred from declarations alone.

<a id="commit-680"></a>
### 680. feat: associate actors with levels {#commit-680}

Source: [546da3ac29b87ba7b1a670a46f15b8db22485448](https://github.com/EndstoneMC/endstone/commit/546da3ac29b87ba7b1a670a46f15b8db22485448); parent `cbb780a813a939b2d1b60795783017e6887b7732`. Authored 2024-04-15T14:45:23Z. Disposition: meaningful.

Adds mirrored native level pointer at stated Actor offset600. After successful original add, nonplayers get level-owned wrappers; removal erases wrapper before original. Players remain server-owned, so level actor enumeration initially excludes them. Level lookup uses native level ID and throws if missing. No evidence establishes the offset beyond source comments.

<a id="commit-681"></a>
### 681. refactor: use std::uint64_t for actor's runtime id {#commit-681}

Source: [c0b7e205119114dcc6c961f2a5ab414d91953819](https://github.com/EndstoneMC/endstone/commit/c0b7e205119114dcc6c961f2a5ab414d91953819); parent `546da3ac29b87ba7b1a670a46f15b8db22485448`. Authored 2024-04-15T15:30:40Z. Disposition: small-semantic.

Changes public actor IDs and level-map keys from signed to uint64_t consistently; native runtime-ID field remains signed until682. API type compatibility change with stable width.

<a id="commit-682"></a>
### 682. feat: add Actor::tryGetFromEntity {#commit-682}

Source: [131c83baba7e100447c6974739a561142b4218b8](https://github.com/EndstoneMC/endstone/commit/131c83baba7e100447c6974739a561142b4218b8); parent `c0b7e205119114dcc6c961f2a5ab414d91953819`. Authored 2024-04-15T15:31:23Z. Disposition: meaningful.

Adds context→Actor lookup via ActorOwnerComponent and uses isAlive as acknowledged temporary substitute for !isRemoved. Component absence handled, owner null not yet checked. Also initializes unique ID to-1/runtime ID to0 and makes native runtime ID unsigned; missing component header follows683.

<a id="commit-683"></a>
### 683. feat: add ActorOwnerComponent {#commit-683}

Source: [6177fbbd8fac2e57bec6c02dc71c628f73d790a3](https://github.com/EndstoneMC/endstone/commit/6177fbbd8fac2e57bec6c02dc71c628f73d790a3); parent `131c83baba7e100447c6974739a561142b4218b8`. Authored 2024-04-15T15:31:38Z. Disposition: small-semantic.

Adds ActorOwnerComponent raw pointer declaration used by682; illustrative type-hash assertion remains commented, not verified.

<a id="commit-684"></a>
### 684. feat: add ActorSpawnEvent {#commit-684}

Source: [1b2797dd2c42627219902efb351dbd1ffb47434e](https://github.com/EndstoneMC/endstone/commit/1b2797dd2c42627219902efb351dbd1ffb47434e); parent `6177fbbd8fac2e57bec6c02dc71c628f73d790a3`. Authored 2024-04-15T15:34:54Z. Disposition: meaningful.

Implements cancellable pre-original ActorSpawnEvent for nonplayers using owner context. Cancellation returns nullptr without native add; success creates a second wrapper for level map, distinct from temporary event wrapper. Event-borrow identity therefore does not persist across successful insertion. Missing context returnsnullptr. This is superseded685.

<a id="commit-685"></a>
### 685. feat: improve ActorSpawnEvent {#commit-685}

Source: [c6bbd884dd7861d9f704027dca263b0c09a9e3c2](https://github.com/EndstoneMC/endstone/commit/c6bbd884dd7861d9f704027dca263b0c09a9e3c2); parent `1b2797dd2c42627219902efb351dbd1ffb47434e`. Authored 2024-04-15T16:24:33Z. Disposition: meaningful.

Moves spawn event after original addition and changes cancellation from preventing insertion to despawn compensation. Reuses event wrapper in level map on success, fixing684 duplicate-wrapper identity. However an unconditional e.setCancelled(true) forces every handled spawn to despawn in this intermediate commit;686 removes it. Removal now checks tracked wrapper before erasing.

<a id="commit-686"></a>
### 686. feat(python): add ActorSpawnEvent binding {#commit-686}

Source: [a468885ff723625c2e288349815c6630be4489e8](https://github.com/EndstoneMC/endstone/commit/a468885ff723625c2e288349815c6630be4489e8); parent `c6bbd884dd7861d9f704027dca263b0c09a9e3c2`. Authored 2024-04-15T16:31:39Z. Disposition: meaningful.

Adds Python spawn-event binding/facade/stub with borrowed actor and fixes popup/tip docstrings; also removes unconditional cancellation introduced685. Despite Python-focused title, this repairs native spawning. Plugin cancellation remains post-add despawn, so docs saying will not spawn are stronger than actual timing.

<a id="commit-687"></a>
### 687. feat: add ActorRemoveEvent and its python binding {#commit-687}

Source: [de5ee93545b7cc240cdc9233a4deab0b09aa605c](https://github.com/EndstoneMC/endstone/commit/de5ee93545b7cc240cdc9233a4deab0b09aa605c); parent `a468885ff723625c2e288349815c6630be4489e8`. Authored 2024-04-15T16:45:02Z. Disposition: meaningful.

Adds noncancellable ActorRemoveEvent with explicit monitoring-only/no-modification/no-player contract, Python borrowed binding and stub. Event fires before level-map wrapper deletion and before native removal. Lifetime discipline is documented, but no asynchronous retention protection or removal-cause field implemented.

<a id="commit-696"></a>
### 696. feat: add EndstoneLevel based on Dimension instead of Level {#commit-696}

Source: [8bbe06ca3232706ae48e8ed54e4e47de6e446bcd](https://github.com/EndstoneMC/endstone/commit/8bbe06ca3232706ae48e8ed54e4e47de6e446bcd); parent `39d54adc6fcde95d55c890cff47f162bc753550f`. Authored 2024-04-18T00:28:52Z. Disposition: meaningful.

Changes EndstoneLevel from one wrapper per native level to one per native dimension, retaining shared native Level for time. Initialization eagerly gets/creates three vanilla dimensions before original notification; names gain suffixes, unknown IDs throw. Actor tracking still finds plain level name and explicitly TODOs dimension matching, exposing synchronization burden later removed705.

<a id="commit-701"></a>
### 701. feat: hook Actor::setDimension for dimension change {#commit-701}

Source: [15f7228222927341594145fd97f2af0846e2a622](https://github.com/EndstoneMC/endstone/commit/15f7228222927341594145fd97f2af0846e2a622); parent `ddd59165782e6e24d3de5f03e7c1d83c3d7b3659`. Authored 2024-04-18T13:22:03Z. Disposition: small-semantic.

Adds Actor setDimension forward hook with TODO for moving level-map ownership. No transfer bookkeeping implemented; this burden becomes unnecessary under705 ECS ownership.

<a id="commit-703"></a>
### 703. feat: add VanillaDimensions::toString and improve EndstoneLevel::getName {#commit-703}

Source: [d409f286032043ae53e6e079995444191e5fa34a](https://github.com/EndstoneMC/endstone/commit/d409f286032043ae53e6e079995444191e5fa34a); parent `c8de424ab692e1dfb7c31cbeaf727eed6be16013`. Authored 2024-04-18T14:05:40Z. Disposition: meaningful.

Reintroduces VanillaDimensions::toString as native-forwarded RVO string function, replacing hardcoded Nether/TheEnd suffixes and unknown-dimension throw with native naming. Supports whatever native name conversion handles, not evidence arbitrary dimensions are registered by three-ID bootstrap.

<a id="commit-705"></a>
### 705. feat: make EndstoneActor one of the actor components to simplify lifecycle management {#commit-705}

Source: [30d6fc343ac75403684d66ceeddf583c04ecbd86](https://github.com/EndstoneMC/endstone/commit/30d6fc343ac75403684d66ceeddf583c04ecbd86); parent `da999e5a4aa24599f2f8d57ae19ed234f50ecf0a`. Authored 2024-04-18T15:27:07Z. Disposition: meaningful.

Explicit rationale: make EndstoneActor an ECS component to simplify lifecycle management. Deletes level wrapper map/insertion/removal, lazy getOrAdd owns wrapper with entity; removal event accesses component before native original. Dimension-change map-transfer TODO disappears; getActors temporarily returns empty. Adds owner-null check; isRemoved still merely !isAlive. Player getter initially rejected, unified716. This is a real ownership reversal with temporary API regression.

<a id="commit-706"></a>
### 706. feat: update EndstoneHuman class {#commit-706}

Source: [776e1735e16ff0e6994dcfd71aefdf487e864315](https://github.com/EndstoneMC/endstone/commit/776e1735e16ff0e6994dcfd71aefdf487e864315); parent `30d6fc343ac75403684d66ceeddf583c04ecbd86`. Authored 2024-04-18T15:52:22Z. Disposition: small-semantic.

Generalizes EndstoneHumanActor from native Player to native Actor, removes duplicate player reference and delegates name to Actor naming. Local op_ remains uninitialized; concrete player overrides still apply.

<a id="commit-708"></a>
### 708. feat: use endstone::Player for command permission testing instead of DummyPlayerSender {#commit-708}

Source: [7e3cbf5fb5063fb344c8f1caab04427a3f284cbd](https://github.com/EndstoneMC/endstone/commit/7e3cbf5fb5063fb344c8f1caab04427a3f284cbd); parent `13a2d1d6329f1ec62259271b663bddc0b3b73c42`. Authored 2024-04-18T16:30:43Z. Disposition: meaningful.

Replaces DummyPlayerSender operator snapshot with real EndstonePlayer for advertised command permission filtering, bringing attachments into visibility checks. Also switches getEndstonePlayer implementation from UUID map pointer to lazy ECS component reference. Header/constructor/access updates arrive709/712, so this is an intermediate uncompilable migration stage, not a standalone finished feature.

<a id="commit-709"></a>
### 709. feat: add Player::getEndstonePlayer {#commit-709}

Source: [5f10eeb972c2695e7d455a54442b646e710dde2c](https://github.com/EndstoneMC/endstone/commit/5f10eeb972c2695e7d455a54442b646e710dde2c); parent `7e3cbf5fb5063fb344c8f1caab04427a3f284cbd`. Authored 2024-04-18T16:31:33Z. Disposition: small-semantic.

Updates native Player getter declaration to mutable concrete reference matching708 and adds detail include. Does not itself fix private Actor context access or ServerPlayer-only constructor mismatch;712 handles those.

<a id="commit-710"></a>
### 710. feat: use Player::getEndstonePlayer for related events {#commit-710}

Source: [90c597f1043f0c037257e6c94fc608fcb329acd6](https://github.com/EndstoneMC/endstone/commit/90c597f1043f0c037257e6c94fc608fcb329acd6); parent `5f10eeb972c2695e7d455a54442b646e710dde2c`. Authored 2024-04-18T16:31:53Z. Disposition: meaningful.

Join/quit/login hooks use component-backed player reference; removes server-map insertion and quit erasure. Events still borrow wrapper, but destruction now follows entity-component lifecycle rather than immediate server-map erase. Login event remains TODO.

<a id="commit-711"></a>
### 711. feat: endstone::Server no longer manage the lifecycle of Players {#commit-711}

Source: [f9830549d6c52994eafc926e36a0cfb24cbab06f](https://github.com/EndstoneMC/endstone/commit/f9830549d6c52994eafc926e36a0cfb24cbab06f); parent `90c597f1043f0c037257e6c94fc608fcb329acd6`. Authored 2024-04-18T16:32:19Z. Disposition: meaningful.

Explicitly removes server player-lifecycle map and add/remove methods. Public getPlayer temporarily becomes nullptr TODO, preserving signature but regressing functional lookup until717. Completes ownership transfer only when read with708–712.

<a id="commit-712"></a>
### 712. feat: clean up codes {#commit-712}

Source: [3fd9a44c269542ba91bcf7b7eb4fc11b6c566283](https://github.com/EndstoneMC/endstone/commit/3fd9a44c269542ba91bcf7b7eb4fc11b6c566283); parent `f9830549d6c52994eafc926e36a0cfb24cbab06f`. Authored 2024-04-18T16:33:29Z. Disposition: meaningful.

Cleanup title hides semantic migration repairs: exposes native context to derived Player, changes concrete player constructor from ServerPlayer to Player, deletes public actor/human/player copy and move operations, removes include cycles/ambiguous aliases, and updates command adapter to component reference. Nonplayer origin now throws instead of logging/returning. Nonmovable wrappers reinforce stable ECS identity; native lifetime remains borrowed.

<a id="commit-713"></a>
### 713. style: format codes {#commit-713}

Source: [f2bca73f6fa6b1197dea1ce09ef924ffdf941561](https://github.com/EndstoneMC/endstone/commit/f2bca73f6fa6b1197dea1ce09ef924ffdf941561); parent `3fd9a44c269542ba91bcf7b7eb4fc11b6c566283`. Authored 2024-04-18T16:34:10Z. Disposition: mechanical.

Reflows removal-event monitoring warning and reorders includes. No runtime change.

<a id="commit-715"></a>
### 715. feat: reimplement EndstoneLevel::getActors() {#commit-715}

Source: [dc582260523468c735245e011b6bd6db449557a6](https://github.com/EndstoneMC/endstone/commit/dc582260523468c735245e011b6bd6db449557a6); parent `3e1d05c68ebddeabaea484a66b811429d654019f`. Authored 2024-04-18T16:46:02Z. Disposition: meaningful.

Restores getActors by enumerating native Level entities, skipping absent context/removed actors and filtering actual dimension pointer identity. Lazily gets component wrapper. At this commit player actors still trigger getEndstoneActor rejection, resolved716; shared native level enumeration avoids manual per-dimension synchronization.

<a id="commit-716"></a>
### 716. refactor: improve Actor::getEndstoneActor and simplify Player::getEndstonePlayer {#commit-716}

Source: [8766f58fa2f554be2a4a8c6f79207941e585ff79](https://github.com/EndstoneMC/endstone/commit/8766f58fa2f554be2a4a8c6f79207941e585ff79); parent `dc582260523468c735245e011b6bd6db449557a6`. Authored 2024-04-18T16:49:44Z. Disposition: meaningful.

Unifies Actor getter to create EndstonePlayer component for native players and generic EndstoneActor otherwise; Player getter casts that result. Resolves715 mixed-entity traversal and avoids duplicate wrapper systems. Other actor subclasses remain factory TODO; correctness depends native isPlayer/type consistency.

<a id="commit-717"></a>
### 717. feat: reimplement Server::getPlayer {#commit-717}

Source: [c3a9098b3c676ca9a0bde2c388d8cd4c612c979b](https://github.com/EndstoneMC/endstone/commit/c3a9098b3c676ca9a0bde2c388d8cd4c612c979b); parent `8766f58fa2f554be2a4a8c6f79207941e585ff79`. Authored 2024-04-18T17:05:37Z. Disposition: meaningful.

Restores Server UUID lookup through each registered EndstoneLevel native Level getPlayer, reconstructing native UUID halves then returning component wrapper. Three dimension wrappers can repeat lookup on same native Level; functional behavior no longer depends server-owned map. No Python get_player binding added here.

<a id="commit-719"></a>
### 719. refactor: use ServerLevel::_postReloadActorAdded for actor initialization {#commit-719}

Source: [bb666a70a4508fdfa6d62024aba51a1e49457b6e](https://github.com/EndstoneMC/endstone/commit/bb666a70a4508fdfa6d62024aba51a1e49457b6e); parent `9f131591fa1b062c88872bf054f10be9496f03f1`. Authored 2024-04-19T00:18:46Z. Disposition: meaningful.

Replaces ActorManager insertion hook with ServerLevel postReloadActorAdded, calls original then nonplayer spawn event/despawn-on-cancel. Adds temporary name debug print before original, which forces wrapper creation even for players;720 removes it. Initialization reason parameter forwarded but not used to classify spawn causes. No explicit rationale beyond initialization hook selection.

<a id="commit-720"></a>
### 720. feat: add ActorInitializationMethod {#commit-720}

Source: [d645fe918a8dfc70aac08f4ab0d197615d2b6ab8](https://github.com/EndstoneMC/endstone/commit/d645fe918a8dfc70aac08f4ab0d197615d2b6ab8); parent `bb666a70a4508fdfa6d62024aba51a1e49457b6e`. Authored 2024-04-19T00:26:52Z. Disposition: small-semantic.

Defines ActorInitializationMethod enum values Invalid/Loaded/Spawned/Born/Transformed/Updated/Event/Legacy, updates includes and removes pre-original debug print719. Spawn hook remains post-original, nonplayer, cancellable via despawn; reason enum is not yet exposed or filtered.
