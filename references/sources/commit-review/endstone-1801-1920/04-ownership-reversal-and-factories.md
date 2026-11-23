<!-- retrieval: {"source_ids":["public:commit:08d4260244daa49a87f39c6caba79a250e6f1493","public:commit:3ab80d24ef2833de4f576717cf87ba887aed7b6f","public:commit:54ee86872a2626e94f1d9f62fb432436f4bc54e1","public:commit:60b6c2e425a555829683f0e8f0a839e9331bfc49","public:commit:6e459287b017b766eb1d6e8d2f71270c4747d5e9","public:commit:93c96a079ea65bf3250bc8a948a8682bea1a705b","public:commit:9b320267da94f6a18633ae1887cbe6fee03f829f","public:commit:ce97d272fa65699669b712292413e0503786e043","public:commit:df80c125507afd5ed98983fcb869df7fae85ce33","public:commit:e2a6ad9449a2f290629cd08d567964e95b04a44a","public:commit:e848e6f1f7d0b59eae8677ca9784b00193cf069f"],"source_type":"public","date":"2024-09-30..2024-10-01","topics":["lifetime","ffi","testing","recovery","api","diagnosis","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# The September–October ownership reversal {#the-september-october-ownership-reversal}

Scope: Endstone commits 1801–1920, September 14–October 22, 2024. These notes follow related implementation areas during this period.

## Dated reversal, not a timeless pointer preference {#dated-reversal-not-a-timeless-pointer-preference}

The September 30 commits expose shared ownership across Permissible, actor access, console access and Python holders. By October 1, public APIs return to references/raw pointers, Python shared holders are removed, and enable_shared_from_this is placed on concrete implementation classes. The explicit 1861 message reports crashes caused by the recent refactoring. Internal shared wrapper caches and factories survive. This is a selective rollback followed by narrower construction discipline, not a complete rejection or universal endorsement of shared_ptr.

The observed alternatives are all local and concrete: public-base enable_shared_from_this versus concrete implementation ownership; immediate permission recalculation versus post-construction Normal/Lazy factories; public shared_ptr-returning APIs versus borrowed-facing APIs backed by shared internal storage. The source supports an inference that construction order and multiply inherited interfaces complicate shared_from_this initialization and virtual callbacks. It does not supply a crash trace that isolates one exact runtime cause, and it does not establish what unobserved reviewers argued.

The ECS component owns an Endstone wrapper, but the wrapper still refers to a native actor. Shared wrapper lifetime does not keep the engine entity alive. The explicit asPlayer override repairs type dispatch across multiple inheritance; it is distinct from ownership. This distinction is useful when reviewing C++/Python bindings or decorators: ask separately who owns the wrapper, who owns the represented object, when virtual initialization is safe, and whether a cast/holder arrangement matches the actual inheritance graph.

Full factory, permission-base and hierarchy context was read. Tests only adjust interfaces elsewhere; no upstream construction test, Python lifetime test, native session or crash reproduction was run. The dated API reversals should remain visible in any future synthesis rather than being flattened into “always use smart pointers” or “always use references.”

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1854"></a>
### Commit 1854 · refactor: enable shared ownership for Permissible {#commit-1854}

Source: [ce97d272fa65699669b712292413e0503786e043](https://github.com/EndstoneMC/endstone/commit/ce97d272fa65699669b712292413e0503786e043). Authored 2024-09-30T20:45:48Z; committed 2024-09-30T20:45:48Z. Git author: Vincent; committer: Vincent.


Begins the shared-ownership experiment by placing enable_shared_from_this on public Permissible and switching actor/command/permission Python holders to shared_ptr. This changes construction and binding contracts across a multiply inherited family. It must be read with the October 1 reversal, not extracted as a lasting preference for shared_ptr-based public APIs.

Changed-source navigation: `include/endstone/permissions/permissible.h`, `src/endstone_core/server.cpp`, `src/endstone_python/actor.cpp`, `src/endstone_python/command.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_python/permissions.cpp`.

<a id="commit-1855"></a>
### Commit 1855 · refactor: ensure the use of factory class for Permissible objects {#commit-1855}

Source: [3ab80d24ef2833de4f576717cf87ba887aed7b6f](https://github.com/EndstoneMC/endstone/commit/3ab80d24ef2833de4f576717cf87ba887aed7b6f). Authored 2024-09-30T21:38:39Z; committed 2024-09-30T21:38:39Z. Git author: Vincent; committer: Vincent.


Adds a protected construction token/factory and shared PermissibleBase ownership. Permission recalculation initially happens immediately, including while a larger owning object can still be constructing. Deleted copy/move declarations are removed from some interfaces as constructors change; inherited/noncopyable members may still restrict copying, so no blanket claim of newly copyable actors is made. The construction-order issue motivates reading the subsequent staged repairs rather than treating this point as final.

Changed-source navigation: `include/endstone/actor/actor.h`, `include/endstone/actor/mob.h`, `include/endstone/command/command_sender.h`, `include/endstone/command/proxied_command_sender.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/mob.h`, `include/endstone/detail/command/command_adapter.h`; plus 13 paths not listed here.

<a id="commit-1856"></a>
### Commit 1856 · refactor: use factory methods for command senders {#commit-1856}

Source: [93c96a079ea65bf3250bc8a948a8682bea1a705b](https://github.com/EndstoneMC/endstone/commit/93c96a079ea65bf3250bc8a948a8682bea1a705b). Authored 2024-09-30T22:28:33Z; committed 2024-09-30T22:28:33Z. Git author: Vincent; committer: Vincent.


Replaces the token design with protected constructors and a derived enabler factory, recalculating after shared allocation. Server console access becomes shared_ptr, command origins recover ownership with shared_from_base, and command adapters move to heap-created instances. This attempts to align factory completion with shared ownership initialization, but the actor migration and multiple-inheritance behavior are still evolving.

Changed-source navigation: `include/bedrock/server/commands/command_origin.h`, `include/endstone/actor/actor.h`, `include/endstone/actor/mob.h`, `include/endstone/command/command_sender.h`, `include/endstone/command/proxied_command_sender.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/mob.h`; plus 23 paths not listed here.

<a id="commit-1857"></a>
### Commit 1857 · feat: add EndstoneActorComponent {#commit-1857}

Source: [60b6c2e425a555829683f0e8f0a839e9331bfc49](https://github.com/EndstoneMC/endstone/commit/60b6c2e425a555829683f0e8f0a839e9331bfc49). Authored 2024-09-30T22:47:39Z; committed 2024-09-30T22:47:39Z. Git author: Vincent; committer: Vincent.


Caches shared_ptr wrappers in the ECS EndstoneActorComponent and uses factories for Actor/Mob/Player. The stored wrapper can have shared lifetime, while its native Actor remains borrowed. That distinction prevents a false guarantee that keeping a wrapper alive also keeps the native entity valid. Template casting helpers are introduced for access to the cached concrete wrapper.

Changed-source navigation: `include/bedrock/world/actor/actor.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/actor/mob.h`, `include/endstone/detail/player.h`, `src/endstone_core/actor/actor.cpp`, `src/endstone_core/actor/mob.cpp`, `src/endstone_core/player.cpp`; plus 1 paths not listed here.

<a id="commit-1858"></a>
### Commit 1858 · refactor: Actor::getEndstoneActor now returns a shared_ptr<Actor> instead of Actor& {#commit-1858}

Source: [6e459287b017b766eb1d6e8d2f71270c4747d5e9](https://github.com/EndstoneMC/endstone/commit/6e459287b017b766eb1d6e8d2f71270c4747d5e9). Authored 2024-09-30T23:22:10Z; committed 2024-09-30T23:22:10Z. Git author: Vincent; committer: Vincent.


Converts native getEndstoneActor and the public level actor list to shared_ptr, with dereferences added throughout callers. The cache stores a concrete EndstoneActor pointer to navigate multiple Actor bases. ScoreEntry still keeps a raw actor pointer, demonstrating incomplete uniformity even within this experiment. No new tests establish native-object lifetime extension.

Changed-source navigation: `include/bedrock/world/actor/actor.h`, `include/bedrock/world/actor/mob.h`, `include/bedrock/world/actor/player/player.h`, `include/endstone/detail/actor/actor.h`, `include/endstone/detail/level/level.h`, `include/endstone/level/level.h`, `src/endstone_core/level/level.cpp`; plus 11 paths not listed here.

<a id="commit-1859"></a>
### Commit 1859 · fix: factory function for PermissibleBase {#commit-1859}

Source: [54ee86872a2626e94f1d9f62fb432436f4bc54e1](https://github.com/EndstoneMC/endstone/commit/54ee86872a2626e94f1d9f62fb432436f4bc54e1). Authored 2024-09-30T23:51:12Z; committed 2024-09-30T23:51:12Z. Git author: Vincent; committer: Vincent.


PermissibleBase gains its own private-token make_shared construction and stops eagerly recalculating through the generic factory. This is consistent with avoiding callbacks into a partially constructed outer permissible, although the precise crash mechanism is not explicitly demonstrated. The later Normal/Lazy factory makes that staging clearer.

Changed-source navigation: `include/endstone/detail/permissions/permissible_base.h`, `src/endstone_core/permissions/permissible_base.cpp`.

<a id="commit-1860"></a>
### Commit 1860 · refactor: Actor::getEndstoneActor returns reference {#commit-1860}

Source: [df80c125507afd5ed98983fcb869df7fae85ce33](https://github.com/EndstoneMC/endstone/commit/df80c125507afd5ed98983fcb869df7fae85ce33). Authored 2024-10-01T00:33:01Z; committed 2024-10-01T00:33:01Z. Git author: Vincent; committer: Vincent.


Restores reference/raw-pointer-facing console and level APIs and restores reference-returning native actor access, while keeping shared internal wrapper storage. Native-origin paths can still recover shared ownership internally. This is a selective rollback of exposed ownership, not abandonment of all shared_ptr use; downstream compatibility and internal retention are deliberately distinguished in the record.

Changed-source navigation: `include/bedrock/world/actor/actor.h`, `include/endstone/detail/level/level.h`, `include/endstone/detail/server.h`, `include/endstone/level/level.h`, `include/endstone/server.h`, `src/endstone_core/level/level.cpp`, `src/endstone_core/scoreboard/scoreboard.cpp`; plus 13 paths not listed here.

<a id="commit-1861"></a>
### Commit 1861 · fix: Resolve crashes caused by recent refactoring efforts {#commit-1861}

Source: [e2a6ad9449a2f290629cd08d567964e95b04a44a](https://github.com/EndstoneMC/endstone/commit/e2a6ad9449a2f290629cd08d567964e95b04a44a). Authored 2024-10-01T11:57:34Z; committed 2024-10-01T11:57:34Z. Git author: Vincent; committer: Vincent.


The message explicitly says it fixes crashes caused by the recent refactoring. enable_shared_from_this moves off the multiply inherited public Permissible onto concrete EndstoneActor and EndstoneConsoleCommandSender, and Python shared holders are removed. Factories and the shared ECS cache remain. Multiple-inheritance/shared_from_this interaction is a plausible explanatory mechanism visible in the changes, but no crash trace or runtime reproduction identifies it conclusively. The dated reversal is stronger evidence than a simplified smart-pointer rule.

Changed-source navigation: `include/endstone/detail/actor/actor.h`, `include/endstone/detail/command/console_command_sender.h`, `include/endstone/detail/permissions/permissible_base.h`, `include/endstone/permissions/permissible.h`, `src/endstone_python/actor.cpp`, `src/endstone_python/command.cpp`, `src/endstone_python/endstone_python.cpp`; plus 2 paths not listed here.

<a id="commit-1863"></a>
### Commit 1863 · feat: add PermissibleFactory {#commit-1863}

Source: [e848e6f1f7d0b59eae8677ca9784b00193cf069f](https://github.com/EndstoneMC/endstone/commit/e848e6f1f7d0b59eae8677ca9784b00193cf069f). Authored 2024-10-01T12:35:15Z; committed 2024-10-01T12:35:15Z. Git author: Vincent; committer: Vincent.


Moves construction helpers from the public Permissible API into detail::PermissibleFactory, with Normal and Lazy modes. PermissibleBase uses Lazy so permission recalculation can wait until the concrete owner is fully constructed; normal factories complete it afterward. This retains internal shared ownership while reducing public construction machinery. The native actor is still borrowed, and the change does not solve stale entity access by itself.

Changed-source navigation: `include/endstone/detail/permissions/permissible.h`, `include/endstone/detail/permissions/permissible_base.h`, `include/endstone/permissions/permissible.h`, `src/endstone_core/actor/actor.cpp`, `src/endstone_core/actor/mob.cpp`, `src/endstone_core/command/command_adapter.cpp`, `src/endstone_core/command/console_command_sender.cpp`; plus 2 paths not listed here.

<a id="commit-1864"></a>
### Commit 1864 · refactor: simplify getEndstoneActor by adding a default type to template {#commit-1864}

Source: [08d4260244daa49a87f39c6caba79a250e6f1493](https://github.com/EndstoneMC/endstone/commit/08d4260244daa49a87f39c6caba79a250e6f1493). Authored 2024-10-01T12:55:37Z; committed 2024-10-01T12:55:37Z. Git author: Vincent; committer: Vincent.


Makes EndstoneActor the default getter template argument and removes repetitive explicit type arguments. The console constructor becomes protected, enforcing the factory path rather than permitting direct construction. Most call-site changes are mechanical, but this construction restriction is a real invariant improvement within the revised ownership design.

Changed-source navigation: `include/bedrock/world/actor/actor.h`, `include/endstone/detail/command/console_command_sender.h`, `src/endstone_core/level/level.cpp`, `src/endstone_runtime/bedrock/server/commands/command_origin.cpp`, `src/endstone_runtime/bedrock/server/server_level.cpp`, `src/endstone_runtime/bedrock/world/actor/actor.cpp`, `src/endstone_runtime/bedrock/world/actor/mob.cpp`; plus 1 paths not listed here.

<a id="commit-1865"></a>
### Commit 1865 · fix: add the missing asPlayer override in EndstonePlayer {#commit-1865}

Source: [9b320267da94f6a18633ae1887cbe6fee03f829f](https://github.com/EndstoneMC/endstone/commit/9b320267da94f6a18633ae1887cbe6fee03f829f). Authored 2024-10-01T13:25:42Z; committed 2024-10-01T13:25:42Z. Git author: Vincent; committer: Vincent.


Adds EndstonePlayer::asPlayer explicitly to route to Player's implementation across the multiple-inheritance branches. UUID qualification is incidental. Full Actor/Mob/Console and permission-factory context was read to retain the hierarchy rather than diagnosing every cast from a one-line override alone.

Changed-source navigation: `include/endstone/detail/player.h`, `include/endstone/player.h`, `src/endstone_core/player.cpp`.
