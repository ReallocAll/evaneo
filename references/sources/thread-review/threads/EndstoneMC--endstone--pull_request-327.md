<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:327"],"source_type":"public","date":"2026-02-10","topics":["lifetime","ffi","testing","performance","api","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-327-feature-add-26-0-support-wip"></a>
# EndstoneMC/endstone #327: [feature] Add 26.0 support (WIP) {#endstonemc-endstone-327-feature-add-26-0-support-wip}

Source: https://github.com/EndstoneMC/endstone/pull/327

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-02-10T18:17:59Z; recorded state closed; merged True.

## Discussion disposition {#discussion-disposition}

Version 26.0 port with no primary reasoning or discussion.

The full associated patch was subsequently inspected; test execution is not independently verified.

## Exact-content reuse and full implementation findings {#exact-content-reuse-and-full-implementation-findings}

The recorded PR base matches the first parent of the squash commit, and the PR head and squash have identical trees. Their ordered additions and deletions also match (70,270 characters, SHA-256 72c8839260b0e97cceab69f85d2c04850c5cdc4f20a144caea76157102dac80f). Only the hunk grouping and function-context labels differ. The 2,821-line full-index squash diff with rename detection disabled has SHA-256 7a47e1efb4f158601b0172bd3833a116e612de3684b2ed27e2c83338285e66bc. [Squash commit 281604a08b6d](https://github.com/EndstoneMC/endstone/commit/281604a08b6d1211fab68c262aff8a95e9cbe0dc)

## Windows 26.0 port: coupled wire, ABI, event and test migration {#windows-26-port}

Source: `281604a08b6d1211fab68c262aff8a95e9cbe0dc` (#327), all 2,821 diff lines and 99 message lines read. This is a substantial squash, not an offset-only update. The version becomes 1.26.0/protocol 924; Windows offsets are refreshed while the Linux table remains old. Static declarations and size assertions constrain the reimplementation, but they do not establish runtime compatibility on either platform.

- **Wire and connection contracts.** `Packet::getName` and concrete overrides change from owned string to string_view. Text serialization finally removes the spurious type-name string lists flagged in January: it writes localize, variant index, one type byte, then that variant's author/message/parameters, XUID and platform ID. Filtered text is now an unconditional string, empty when absent, rather than presence-bool plus optional value. No round-trip or wire-byte test is added, and `_read` remains outside the implementation supplied here. The close callback receives an extra mutable message-body override; `NetworkSystem` supplies a static empty string, so callback mutation could persist between calls. Connector callback signatures and removed virtual slots must match the new server ABI; this is distinct from cosmetic renaming of `trytLoadPlayer` to `tryToLoadPlayer` across declaration, hook and symbol key.
- **Layout changes are coordinated, not independent guesses.** `NO_UNIQUE_ADDRESS` selects MSVC's spelling where necessary, compressing empty flat-set mapped containers/comparators. Block component padding becomes explicit flat_map/flat_set fields, with size 104→80; Block shrinks by 24 bytes. BlockActor adds filtered name storage and grows from Windows152/Linux136 to184/160, shifting piston offsets. Actor, Item, ILevel, resource packs and chunk sources gain/remove/change virtual signatures; permissions gain a shared single-threaded publisher; ServerInstance gains profiling ownership and service-registration token. Biome tag storage moves before the remaining registry fields and five tags are added; the old exact-size assertion is removed. These edits need a version-matched binary, not merely successful header compilation. ActorDamageSource additionally owns a death-message override string, and interaction results become two bitfields rather than an integer enum.
- **Damage interception moves to the upstream mutable event boundary.** The old HealthAttributeDelegate/Mob `_hurt` hook pair is commented out and unmarked. It had independently maintained last-hurt damage to avoid event-reduced damage bypassing an invulnerability window, and used a component flag to suppress knockback after cancellation. The replacement catches `ActorBeforeHurtEvent`, emits Endstone ActorDamageEvent, returns BypassListeners/Cancel when cancelled, otherwise writes `event.damage` back and invokes the original handler. Windows vtable slot1/Linux5 are installed. This makes cancellation earlier and removes bespoke last-hurt bookkeeping, but the diff supplies no invulnerability/knockback regression oracle proving equivalent outcomes; treating the removed comment's concern as automatically solved would overclaim. The conversion still requests EndstoneMob from the event's Actor; non-mob coverage is not shown. Before-heal/acquire events are declared, but healing is not exposed and pickup still uses its old hook with a TODO.
- **Portal semantics narrow.** The hook still computes a prospective destination and emits a cancellable PlayerPortalEvent, but after non-cancellation it calls original changeDimension with the original dimension ID. It no longer applies `e.getTo()` or submits the modified request. Thus observers can cancel, while edits to the event destination are ignored at this revision. Reading the full 50-line hook confirms that no later statement reapplies them. The changelog changes the claim to cancellation. Target-position state is reset in the separate transition-component helper.
- **Attribute and item details.** Dirty attributes now exclude non-client-syncable attributes. The removed callback-null guard is supported by the class's default member initializer pointing at `_onAttributeModified`, although other construction/overwrite paths are not proven. Identifier gets combined namespace/key hashing, allowing item-meta enchantment maps to use EnchantmentId instead of raw strings. There is no benchmark for these changes. Crash trace filename formatting and stale changelog claims also change; these are not independent architectural preferences.
- **Test collection repair and stronger runtime boundaries.** A collection hook marks modules under `endstone_test.tests.player.`; the ineffective conftest-level pytestmark is deleted. This makes automatic `not player` versus explicit player-command selection meaningful. Player tests add max-health write/restore, invalid health/max-health/experience ValueErrors, flight toggles, XUID/UUID/network/device smoke checks. Locale validation weakens from Babel parsing to nonempty string; version regex only checks a prefix. Successful mutable tests restore inline rather than in finally, so an assertion can leave live state changed. XUID nonempty assumes authenticated players; hardcoded default speeds and name-tag assumptions remain environment-sensitive. These tests still do not cover damage cancellation, portal edits, kick wire correctness, or client rendering.
- **NBT regression oracle.** Both native and Python tests assign a compound into its own child (`a["b"] = a`) and require a deep pre-insertion snapshot: outer keys a,b, inner only a=1. The inner size assertion distinguishes snapshot semantics from recursive aliasing or copying after insertion. The patch adds tests, not an implementation fix. Their execution is not evidenced here; C++ core tests and in-server Python tests remain different validation paths.

Costs and applicability: this port requires simultaneously correct virtual layouts, event variant order, packet encoding and offsets. It is a useful checklist for binary interop upgrades; copying only its numeric table would omit behavior changes and test-selection repair. No upstream code was run in this research.


## Code and verification boundary {#code-and-verification-boundary}

Inspected all primary/discussion text directly; full code review reused only after exact tree/base and ordered changed-line equivalence to commit281604a08b6d1211fab68c262aff8a95e9cbe0dc was verified. Captured PR diff SHA-256 379499c887034e2e817e80b4b2d30bd510b9376ec52529488c74aef271b76f9c. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/327
