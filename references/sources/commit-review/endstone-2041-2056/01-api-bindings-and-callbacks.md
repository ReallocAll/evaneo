<!-- retrieval: {"source_ids":["public:commit:0719ae587b5be796fca25881d395242054854c35","public:commit:075364bc61392859787a56cec7a7448d65ad31ce","public:commit:1e984d43284933cf830522ce6ace613997dfdb2c","public:commit:3b4ce8b80415913df20b55637d7ca0fcd812af05","public:commit:3dba2c6175dd2404486b303da4138de8c27c1787","public:commit:4495a76fdb59146e5792489b7a9cbb22b5c8c413","public:commit:4af63b58afd3d081d30c2459cf22b5cb4c43ddc5","public:commit:4fb4c9a2cd15ed5bbd46a18a685071d510ab39b9","public:commit:5310484c580f9077b436a58c8f90905f3ddff2c4","public:commit:6ffc92e603cbfa29724bf55a4e2516c30af80996","public:commit:7a0b01a5ea4d6efae2af50e77cc55743adcbf5b0","public:commit:a3a86c3333e802f41822131aaaaf7956f1ee3b6a","public:commit:bf40fd129f2405d51e27fc53369622c7cd617914","public:commit:ceff698de67ad5d5a8a349b68117cebb5f653e06"],"source_type":"public","date":"2024-12-23..2024-12-24","topics":["lifetime","ffi","testing","recovery","api","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Completing public surfaces without overstating lifetime safety {#completing-public-surfaces-without-overstating-lifetime-safety}

## Actor identity and form callbacks {#actor-identity-and-form-callbacks}

2041 adds canonical actor type retrieval through ActorDefinitionIdentifierComponent, the native wrapper, public Actor/Mob/Player delegates and Python property. If the component is absent, a static empty identifier is returned. This is a safe fallback by source inspection, not proof that all native actor layouts or components have the modeled ABI.

2042 repairs the reported crash when a form callback kills the player. It moves the form variant into a local value and erases the map entry before invoking user code. The callback can then invalidate the player/map without leaving a post-callback forms_.erase(iterator). The moved form also survives callbacks, so reading its buttons after an ActionForm submit no longer depends on the original forms_ storage.

The endpoint still passes this to a later ActionForm button callback after onSubmit, and its catch path calls getServer through this. If an earlier callback invalidates the player, those uses remain a review concern. The source therefore establishes a bounded iterator/form-storage fix, not universal lifetime safety or a retained Player handle. The full relevant close/submit functions were read at2056; no death/callback test was executed. Issue111 is only linked by the source message in this unit.

## Ban bindings expose the storage contract {#ban-bindings-expose-the-storage-contract}

2044 adds mutable BanEntry metadata and concrete entry constructors.2045 exposes lists and server properties with reference returns and entries using reference_internal. The preceding owner [ban dossier](../endstone-1921-2040/03-ban-model-and-persistence.md) establishes vector-backed storage, erase/reinsert upsert, expiry removal and load invalidation. A Python reference policy does not stabilize addresses after those mutations, and setters on an entry do not invoke persistence themselves. A source-level public API can be complete yet still impose lifetime and durability constraints.

Stubs say get_ban_entry returns an entry rather than possibly None, even though C++ returns nullptr. Binding documentation describes name/UUID/orXUID lookup, while the matcher is a conjunction with missing-value wildcards. Expiration-date overloads are bound; duration overloads are not.2046 adds endstone.ban and documentation navigation but reexports only concrete entries/lists, not the base BanEntry. Stub files are interface artifacts; they receive no independent generated-code authorship assumption.

## Boolean property migration and a hotfix {#boolean-property-migration-and-a-hotfix}

2047 renames several Python Boolean properties to is_ names. It preserves only cancelled as a deprecated read/write alias, while its recommended replacement is_cancelled is readonly. Existing Python Plugin.register_events still reads enabled until2048 switches it to is_enabled.2048 also uses FutureWarning and an always filter, making notices visible process-wide. PyErr_WarnEx return handling is not added, so warning-as-error behavior is not established.

2050 records0.5.7,2051 advances the development macro, and2055 finally adds the missing setter to is_cancelled.2056 records0.5.7.1 with that repair and the logging change below, reverting the C++ patch macro8→7; it does not encode a fourth component. The source does not establish tag publication or binary compatibility merely from these changelog entries.

2054 moves player command logging after dispatching PlayerCommandEvent, the cancellation return and possible command rewrite. Cancelled commands are not printed by this path; allowed commands log the effective command. At2056 supported player/console senders dispatch through the server, while unsupported sender kinds forward to the original native route. This is a narrow privacy/control-flow improvement, not a global secret-redaction policy.

## Attribution and test boundary {#attribution-and-test-boundary}

2043's changelog credits ping setters to theaddonn, devtool cleanup to smartcmd and plugin loader selection to engsr6982.2049 still revises native container/skin/cereal signatures near release, showing that API surface completion and native compatibility verification are different dimensions. All observations here are static; no Python import, compiler, server, UI or network test was run.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-2041"></a>
### Commit 2041 {#commit-2041}

3b4ce8b80415913df20b55637d7ca0fcd812af05 · 2024-12-23T14:35:00Z

[feat: add `Actor::getType` function to retrieve actor types (e.g., minecraft:pig)](https://github.com/EndstoneMC/endstone/commit/3b4ce8b80415913df20b55637d7ca0fcd812af05)


Adds ActorDefinitionIdentifier component and canonical string type across public Actor/Mob/Player/Python. Missing component returns static empty identifier, avoiding dereference. Native getEntityTypeId still requires persistent component; no runtime native-layout proof.

Static review only; no upstream execution.

<a id="commit-2042"></a>
### Commit 2042 {#commit-2042}

7a0b01a5ea4d6efae2af50e77cc55743adcbf5b0 · 2024-12-23T14:55:05Z

[fix: prevent crash caused by killing a player in a form callback, which invalidates the player object](https://github.com/EndstoneMC/endstone/commit/7a0b01a5ea4d6efae2af50e77cc55743adcbf5b0)


Moves form variant out of forms_ and erases map entry before invoking close/submit callback, so callback-triggered player death cannot invalidate the map iterator used afterward. Local moved form survives callback. ActionForm can pass this to a second button callback after submit, and exception path still calls getServer through this after potential invalidation; repair is bounded, not general callback lifetime safety. Issue111 is source-linked, not fetched evidence.

Static review only; no upstream execution.

<a id="commit-2043"></a>
### Commit 2043 {#commit-2043}

4495a76fdb59146e5792489b7a9cbb22b5c8c413 · 2024-12-23T15:07:25Z

[docs: update CHANGELOG.md](https://github.com/EndstoneMC/endstone/commit/4495a76fdb59146e5792489b7a9cbb22b5c8c413)


Changelog summarizes actor/IPban/form/inventory/resource repairs and explicitly credits ping setters to theaddonn, devtool deletion to smartcmd, and loader selection to engsr6982.

Static review only; no upstream execution.

<a id="commit-2044"></a>
### Commit 2044 {#commit-2044}

a3a86c3333e802f41822131aaaaf7956f1ee3b6a · 2024-12-23T17:23:12Z

[feat: add python bindings for ban entries](https://github.com/EndstoneMC/endstone/commit/a3a86c3333e802f41822131aaaaf7956f1ee3b6a)


Registers BanEntry mutable metadata and concrete IP/player entries with chrono/UUID conversions; removes unused include. Entry mutation does not itself persist through a list hook. Stubs mirror binding surface; no Python execution.

Static review only; no upstream execution.

<a id="commit-2045"></a>
### Commit 2045 {#commit-2045}

1e984d43284933cf830522ce6ace613997dfdb2c · 2024-12-23T17:52:32Z

[feat: add python bindings for ban lists](https://github.com/EndstoneMC/endstone/commit/1e984d43284933cf830522ce6ace613997dfdb2c)


Adds list get/add/reference returns, entries reference_internal and server list references. Raw entries are vector-backed and invalidated by add/remove/expiration/load; keeping parent alive does not stabilize addresses. Stub get_ban_entry omits possible None, and docs say name/UUID/orXUID though matcher is conjunction-with-wildcards. Duration overload not exposed.

Static review only; no upstream execution.

<a id="commit-2046"></a>
### Commit 2046 {#commit-2046}

4af63b58afd3d081d30c2459cf22b5cb4c43ddc5 · 2024-12-23T17:56:41Z

[docs: add python module `endstone.ban`](https://github.com/EndstoneMC/endstone/commit/4af63b58afd3d081d30c2459cf22b5cb4c43ddc5)


Adds endstone.ban reexports and docs nav plus Server ban properties in stub; BanEntry base itself is not reexported. Surface completion, no new enforcement.

Static review only; no upstream execution.

<a id="commit-2047"></a>
### Commit 2047 {#commit-2047}

6ffc92e603cbfa29724bf55a4e2516c30af80996 · 2024-12-23T19:54:22Z

[BREAKING CHANGE: replace boolean property names with an "is_" prefix for consistency](https://github.com/EndstoneMC/endstone/commit/6ffc92e603cbfa29724bf55a4e2516c30af80996)


Renames Python visible/registered/enabled/cancellable/asynchronous to is_ names; only cancelled retains deprecated read/write compatibility alias. New is_cancelled is accidentally readonly, so recommended migration cannot cancel until2055. Plugin wrapper still used enabled until2048.

Static review only; no upstream execution.

<a id="commit-2048"></a>
### Commit 2048 {#commit-2048}

3dba2c6175dd2404486b303da4138de8c27c1787 · 2024-12-23T20:22:04Z

[feat: add FutureWarning for deprecated methods and properties](https://github.com/EndstoneMC/endstone/commit/3dba2c6175dd2404486b303da4138de8c27c1787)


Updates register_events to is_enabled and switches cancelled alias warning to FutureWarning with always filter in loader. This makes warnings visible globally, but ignores PyErr_WarnEx return if warnings are escalated; no test executed.

Static review only; no upstream execution.

<a id="commit-2049"></a>
### Commit 2049 {#commit-2049}

075364bc61392859787a56cec7a7448d65ad31ce · 2024-12-23T21:11:28Z

[fix: correct headers](https://github.com/EndstoneMC/endstone/commit/075364bc61392859787a56cec7a7448d65ad31ce)


Replaces container removed-listener virtuals with connector/subscriber queries, corrects block lava/nameinstrument field semantics and skin/cerealContext signatures. Native ABI assumptions only, no binary execution.

Static review only; no upstream execution.

<a id="commit-2050"></a>
### Commit 2050 {#commit-2050}

bf40fd129f2405d51e27fc53369622c7cd617914 · 2024-12-23T21:13:28Z

[chore: release v0.5.7](https://github.com/EndstoneMC/endstone/commit/bf40fd129f2405d51e27fc53369622c7cd617914)


Marks0.5.7 released2024-12-23 and opens0.5.8 changelog; macro patch6→7. Changelog success claims remain source-reported; does not fix2040 bounds regression or2047 readonly migration.

Static review only; no upstream execution.

<a id="commit-2051"></a>
### Commit 2051 {#commit-2051}

ceff698de67ad5d5a8a349b68117cebb5f653e06 · 2024-12-23T21:50:23Z

[chore: v0.5.8 is next](https://github.com/EndstoneMC/endstone/commit/ceff698de67ad5d5a8a349b68117cebb5f653e06)


Advances macro patch7→8 for next development release; API version stays0.5. Reversed at2056 hotfix endpoint.

Static review only; no upstream execution.

<a id="commit-2054"></a>
### Commit 2054 {#commit-2054}

0719ae587b5be796fca25881d395242054854c35 · 2024-12-24T13:13:24Z

[fix: prevent commands from logging if PlayerCommandEvent is cancelled.](https://github.com/EndstoneMC/endstone/commit/0719ae587b5be796fca25881d395242054854c35)


Moves player-command log after cancellation check and event command rewrite, so cancelled commands do not log and permitted commands log effective command. Native execution forwarding context checked; not blanket secret-redaction policy.

Static review only; no upstream execution.

<a id="commit-2055"></a>
### Commit 2055 {#commit-2055}

4fb4c9a2cd15ed5bbd46a18a685071d510ab39b9 · 2024-12-24T13:38:56Z

[fix: `event.is_cancelled` property should be writable](https://github.com/EndstoneMC/endstone/commit/4fb4c9a2cd15ed5bbd46a18a685071d510ab39b9)


Makes is_cancelled writable through Event::setCancelled and matching stub, closing2047 migration break while deprecated alias remains.

Static review only; no upstream execution.

<a id="commit-2056"></a>
### Commit 2056 {#commit-2056}

5310484c580f9077b436a58c8f90905f3ddff2c4 · 2024-12-24T13:46:33Z

[chore: release v0.5.7.1](https://github.com/EndstoneMC/endstone/commit/5310484c580f9077b436a58c8f90905f3ddff2c4)


Records0.5.7.1 hotfix for writable cancellation and cancelled-command logging; macro8→7 does not encode fourth component. Final2024target; neither tagpublication nor runtime tests established.2025excluded.

Static review only; no upstream execution.
