<!-- retrieval: {"source_ids":["public:commit:0d05e555d44e05e7e997ee8c3b03904b20619cde","public:commit:3b96783c05a60055a73a4507e24fb6d814b62f9d","public:commit:4f744c76eef74fda490db2e2dd44b1cf7323899f","public:commit:5899d8ab6693d2352bd2b4355f67629254db0ddd","public:commit:653d3fab2cfb3c69d91d0462067f91c39a62a729","public:commit:687875f039fed28a3f6256c132325b2e50fc93f4","public:commit:6a7c2941c0d27dd020ffecec32d30810a8f2a4d9","public:commit:757feb6890e2be2c19c559d041b7ae26ecab7769","public:commit:8653ddabd63d4f48c7699bcc2d1cde5b73068951","public:commit:8b8cdc5c021ff989ed7b50190c3807e20ad92446","public:commit:8e79803ee6d88d46328f65f38c9e8a5321b3a2cb","public:commit:8f2ba83078cdcdef790fd954d58b0ddb149efe61","public:commit:9a9c0933a0b8e111d62eb50b848af278399a7a4c","public:commit:9f6630675fd7421caa5fa5e4458035c81e7e35a2","public:commit:a7dbb2812e8add92fcbeffceb0a823838d82015a","public:commit:ada20bf0c6f88254c255bb4c548dd503da14a2c8","public:commit:bf16a826c62ce026993609e180389f3053d9b956","public:commit:eab250240a211cafaffeedc01995b38901be7d71","public:commit:eae2fa3a7dac8279c977be43bcf2446a7c4a3c10","public:commit:ed03eb02298773565e338618aa9a193214609a1d","public:commit:ed9f9304047fe5d58fe8c93c155408f7c52cae18","public:commit:fa38205e8172226deba344774eb226d60c7dc0e7"],"source_type":"public","date":"2025-03-05..2025-03-14","topics":["lifetime","concurrency","ffi","testing","api","diagnosis","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native ABI version migration and branch-aware conclusions {#native-abi-version-migration-and-branch-aware-conclusions}

## Two concurrent histories {#two-concurrent-histories}

These are2025-only committed-time/SHA ordinals, not a linear native-version timeline.334–361 belong to1.21.70-support.383 and392 merge main into that branch;393 removes a modeled factory there.400 is main and does not contain those beta-only commits. Both tips393 and400 are required to represent the read slice. A conclusion such as “the factory was removed by400” would be wrong even though393 has an earlier timestamp. The merge/branch audit JSON files are not distributed; the linked public commits and both branch tips provide accessible ancestry evidence, not a replacement for the historical per-file comparisons.

## Schema and repair chain {#schema-and-repair-chain}

332 updates the main1.21.62 target, hardcoded Windows I18n location and symbol table.334–346 reshape identity, native events, packet/actor flags, pack objects, timers and broad virtual/member layouts for beta1.21.70. Identity access moves behind component getters, XUID validation retains the self-signed restriction, and getAddress changes to value-returning live lookup rather than constructor-time caching/mutation.

336 initially models GameServerToken as polymorphic, but357 removes the virtuals and restores certificate offset0.355 corrects BlockLegacy virtual slots,356 adds EntityRegistry state,358 restores a missing Mob field and downstream offsets,359 supplies complete container element types and opaque-pointer stand-ins for Linux.360 corrects Level::tick by two bytes. These reversals make “all support added in one broad patch” an inaccurate account. Source declarations, comments and size assertions are constraints or hypotheses; no native executable was used to establish layout truth.

332 and349 each contain95 existing numeric address substitutions. Structural TOML audit proves the platform key sets, numeric types, old/new values and scalar version/timestamp changes; Windows gI18n is added332 then removed349. All nonnumeric residuals were read. Address values are not semantically validated by counting, hashing or parsing them. No hidden address-validation claim is made.

391 expands main NetworkSystem’s tail including incoming queues and an aligned factory member;393 removes the factory only on beta after392 imports main changes. The author reports a Linux crash fix, but the source review establishes only the revised model and branch relationship.

## Use and limits {#use-and-limits}

Useful for API/ABI migration planning, spotting provisional offsets, maintaining separate stable/preview histories, and avoiding false conclusions from chronological inventories. Exact symbols and architecture-specific sizes must still be checked against the relevant vendor binary. No source from excluded old Nukkit was used.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-332"></a>
### Commit 332 {#commit-332}

4f744c76eef74fda490db2e2dd44b1cf7323899f · 2025-03-09T00:46:55Z

[feat: support game version v1.21.62](https://github.com/EndstoneMC/endstone/commit/4f744c76eef74fda490db2e2dd44b1cf7323899f)

**Observed change.** Declares1.21.62 support, adjusts Windows I18n hardcoded address and regenerates version/timestamp/platform symbol addresses, including gI18n entry.

**Causal interpretation.** Version support couples Python advertised target, native object location and symbol table. Numeric bulk receives exact structural key/type/address audit; semantic non-symbol hunks read.

**Limits.** No disassembly/address verification or native run. Windows gI18n key is added here and removed349 on beta; numeric address substitution is not verified compatibility.

<a id="commit-334"></a>
### Commit 334 {#commit-334}

5899d8ab6693d2352bd2b4355f67629254db0ddd · 2025-03-09T15:29:11Z

[feat: update `UserEntityIdentifierComponent`](https://github.com/EndstoneMC/endstone/commit/5899d8ab6693d2352bd2b4355f67629254db0ddd)

**Observed change.** Replaces public UserEntityIdentifierComponent fields/certificate with private reordered network/subclient/playfab/UUID/GameServerToken members and accessors/identity queries.

**Causal interpretation.** Native1.21.70 branch changes identity layout and moves call sites toward a semantic facade rather than certificate member peeking.

**Limits.** Implementation arrives346; intermediate states may not compile. Authored March5 but committed March9; ordering is by committed time/SHA, not strict ancestry.

<a id="commit-335"></a>
### Commit 335 {#commit-335}

653d3fab2cfb3c69d91d0462067f91c39a62a729 · 2025-03-09T15:29:11Z

[refactor: move `HashType64` to a separate header](https://github.com/EndstoneMC/endstone/commit/653d3fab2cfb3c69d91d0462067f91c39a62a729)

**Observed change.** Moves HashType64 into dedicated header and adds32-bit HashType alias; string_hash includes it.

**Causal interpretation.** Small shared-type extraction supporting native layout updates.

**Limits.** Mechanical content read; no performance or ABI change claim beyond identical existing uint64 alias.

<a id="commit-336"></a>
### Commit 336 {#commit-336}

9a9c0933a0b8e111d62eb50b848af278399a7a4c · 2025-03-09T15:29:11Z

[feat: update `GameServerToken` class](https://github.com/EndstoneMC/endstone/commit/9a9c0933a0b8e111d62eb50b848af278399a7a4c)

**Observed change.** Adds virtual destructor/toString/isValid to GameServerToken, moving certificate offset comment0→8.

**Causal interpretation.** An initial polymorphic ABI model later corrected357 by removing virtuals, so this is provisional reverse engineering rather than final design.

**Limits.** No native vtable evidence or test; later correction is essential context.

<a id="commit-337"></a>
### Commit 337 {#commit-337}

ada20bf0c6f88254c255bb4c548dd503da14a2c8 · 2025-03-09T15:29:11Z

[refactor: remove `ExtendedCertificate`](https://github.com/EndstoneMC/endstone/commit/ada20bf0c6f88254c255bb4c548dd503da14a2c8)

**Observed change.** Deletes ExtendedCertificate XUID helper, including its reject-self-signed-unless-trusted condition.

**Causal interpretation.** Responsibility migrates into GameServerToken/UserEntityIdentifierComponent; must preserve authentication policy, not merely delete a header.

**Limits.** Replacement call sites342 and implementation346 complete the chain; no authentication tests.

<a id="commit-338"></a>
### Commit 338 {#commit-338}

687875f039fed28a3f6256c132325b2e50fc93f4 · 2025-03-09T15:29:12Z

[feat: add new actor events](https://github.com/EndstoneMC/endstone/commit/687875f039fed28a3f6256c132325b2e50fc93f4)

**Observed change.** Adds before/after dropped-item native payloads with damage source/items, adds MutableActorGameplayEvent<void> and corresponding virtual slot/decorator forwarding, appends after-event to void variant.

**Causal interpretation.** Preserves native handler vtable and variant schema for new vendor events without claiming a public Endstone event API.

**Limits.** Forwarding only, no public dispatch/test; ABI sizes/order unvalidated against binary.

<a id="commit-339"></a>
### Commit 339 {#commit-339}

6a7c2941c0d27dd020ffecec32d30810a8f2a4d9 · 2025-03-09T15:29:12Z

[feat: add new packet ids](https://github.com/EndstoneMC/endstone/commit/6a7c2941c0d27dd020ffecec32d30810a8f2a4d9)

**Observed change.** Renames two old sound packet constants DEPRECATED and appends update client options/video capture/entity override packet IDs323–325, EndId326.

**Causal interpretation.** Protocol enum compatibility maintenance, not implementation of those packet behaviors.

**Limits.** No wire-schema or traffic validation.

<a id="commit-340"></a>
### Commit 340 {#commit-340}

8e79803ee6d88d46328f65f38c9e8a5321b3a2cb · 2025-03-09T15:29:12Z

[feat: add new actor flags](https://github.com/EndstoneMC/endstone/commit/8e79803ee6d88d46328f65f38c9e8a5321b3a2cb)

**Observed change.** Appends BODY_ROTATION_AXIS_ALIGNED, COLLIDABLE and WASD_AIR_CONTROLLED actor flags120–122 before Count.

**Causal interpretation.** Native flag-index model expands without reordering older values.

**Limits.** No simulation behavior or bitset-size verification.

<a id="commit-341"></a>
### Commit 341 {#commit-341}

a7dbb2812e8add92fcbeffceb0a823838d82015a · 2025-03-09T15:29:12Z

[feat: update classes](https://github.com/EndstoneMC/endstone/commit/a7dbb2812e8add92fcbeffceb0a823838d82015a)

**Observed change.** Broad1.21.70 ABI update: pack IO/dependency objects, registry validator, new level/block-source virtuals, ActorSoundIdentifier parameters, ServerPlayer constructor/options, removed Mob/Player fields, float timer stepping, network receipt-event flag, biome field removal. Also removes obsolete ExtendedCertificate build entry.

**Causal interpretation.** Data members and virtual interfaces co-evolve; large formatting portions hide real offset/slot changes. Follow-on355–359 repairs show provisional nature.

**Limits.** All meaningful full hunks read. No vendor binary/layout parity; native offsets/comments and declarations are hypotheses, not a tested ABI contract.

<a id="commit-342"></a>
### Commit 342 {#commit-342}

bf16a826c62ce026993609e180389f3053d9b956 · 2025-03-09T15:29:12Z

[feat: update implementations](https://github.com/EndstoneMC/endstone/commit/bf16a826c62ce026993609e180389f3053d9b956)

**Observed change.** Updates player, scoreboard and runtime identity call sites to334 accessors; XUID now from component; preserves RakNet socket/address mutation and name/UUID behavior. Cleans includes/blank lines.

**Causal interpretation.** Completes facade adoption but still depends on346 accessor definitions and corrected GameServerToken layout357.

**Limits.** No authentication/address behavior tests or compile run; no independent lesson for formatting-only pieces.

<a id="commit-344"></a>
### Commit 344 {#commit-344}

ed9f9304047fe5d58fe8c93c155408f7c52cae18 · 2025-03-09T22:19:54Z

[refactor: update methods in `NetworkIdentifier`](https://github.com/EndstoneMC/endstone/commit/ed9f9304047fe5d58fe8c93c155408f7c52cae18)

**Observed change.** NetworkIdentifier address/port conversion switches on transport type, handles IPv4/IPv6 with inet_ntop and appropriate buffers, returns empty/zero for other types.

**Causal interpretation.** Avoids interpreting every union as a socket and supports IPv6 text width.

**Limits.** No socket/endianness/platform tests; native representation remains assumed.

<a id="commit-345"></a>
### Commit 345 {#commit-345}

eae2fa3a7dac8279c977be43bcf2446a7c4a3c10 · 2025-03-09T22:35:14Z

[refactor: update `getAddress` implementation in `EndstonePlayer`](https://github.com/EndstoneMC/endstone/commit/eae2fa3a7dac8279c977be43bcf2446a7c4a3c10)

**Observed change.** Player.getAddress returns a value, resolves current RakNet peer address or socket identifier dynamically, removes cached address and constructor socket mutation; skin is value-initialized.

**Causal interpretation.** Avoids freezing or mutating connection address state during wrapper creation. Constructor now assumes persistent identity component rather than checking optional lookup.

**Limits.** Breaking C++ return signature; native lookup lifetime and unsupported NetherNet fallback are untested.

<a id="commit-346"></a>
### Commit 346 {#commit-346}

3b96783c05a60055a73a4507e24fb6d814b62f9d · 2025-03-09T22:43:14Z

[feat: implement methods in `UserEntityIdentifierComponent`](https://github.com/EndstoneMC/endstone/commit/3b96783c05a60055a73a4507e24fb6d814b62f9d)

**Observed change.** Implements GameServerToken XUID access with validity and self-signed restrictions, and component UUID/XUID/network/subclient getters.

**Causal interpretation.** Restores the certificate policy displaced337 while encapsulating revised identity representation.

**Limits.** Other declared identity queries remain declarations; no authentication or signed-token test.

<a id="commit-348"></a>
### Commit 348 {#commit-348}

8f2ba83078cdcdef790fd954d58b0ddb149efe61 · 2025-03-09T22:54:42Z

[feat: update offset for `getI18n`](https://github.com/EndstoneMC/endstone/commit/8f2ba83078cdcdef790fd954d58b0ddb149efe61)

**Observed change.** Updates hardcoded Windows I18n location to0x60BBF20.

**Causal interpretation.** One-address native version maintenance, with no independently generalizable preference.

**Limits.** No binary/disassembly validation; the symbol generator table is separate.

<a id="commit-349"></a>
### Commit 349 {#commit-349}

757feb6890e2be2c19c559d041b7ae26ecab7769 · 2025-03-09T23:30:54Z

[feat: update symbols.toml (1.21.70-beta.26)](https://github.com/EndstoneMC/endstone/commit/757feb6890e2be2c19c559d041b7ae26ecab7769)

**Observed change.** Updates symbol version/timestamp to1.21.70-beta.26 and all95 existing platform numeric addresses; removes Windows gI18n key and ignores preview server folder.

**Causal interpretation.** Exact TOML structural comparison verifies48 Linux and47 Windows retained numeric keys; all nonnumeric changes and removed key inspected.

**Limits.** Numeric values structurally audited, not semantically validated against binaries.360 corrects Linux Level::tick by two bytes.

<a id="commit-355"></a>
### Commit 355 {#commit-355}

9f6630675fd7421caa5fa5e4458035c81e7e35a2 · 2025-03-10T18:24:31Z

[fix: correct the virtual table of `BlockLegacy` class](https://github.com/EndstoneMC/endstone/commit/9f6630675fd7421caa5fa5e4458035c81e7e35a2)

**Observed change.** Changes BlockLegacy canBeBuiltOver virtual signature and removes obsolete use-related virtual slots; updates flag comment.

**Causal interpretation.** Native vtable repair after broad341 model, showing version support is iterative.

**Limits.** No ABI slot/offset validation against native executable.

<a id="commit-356"></a>
### Commit 356 {#commit-356}

eab250240a211cafaffeedc01995b38901be7d71 · 2025-03-10T21:07:18Z

[fix: add missing member to `EntityRegistry`](https://github.com/EndstoneMC/endstone/commit/eab250240a211cafaffeedc01995b38901be7d71)

**Observed change.** Adds EntityRegistry is_viewing bool before debug name and removes obsolete offset comments.

**Causal interpretation.** Restores a modeled member that changes subsequent layout.

**Limits.** No native construction/offset tests.

<a id="commit-357"></a>
### Commit 357 {#commit-357}

fa38205e8172226deba344774eb226d60c7dc0e7 · 2025-03-10T21:13:24Z

[fix: remove virtual methods in `GameServerToken`](https://github.com/EndstoneMC/endstone/commit/fa38205e8172226deba344774eb226d60c7dc0e7)

**Observed change.** Removes GameServerToken virtual destructor/toString/virtual isValid and restores certificate offset0.

**Causal interpretation.** Reverses336's polymorphic model; earlier intermediate ABI is not a final contract.

**Limits.** No binary vtable proof or integration test.

<a id="commit-358"></a>
### Commit 358 {#commit-358}

8b8cdc5c021ff989ed7b50190c3807e20ad92446 · 2025-03-10T21:45:15Z

[fix: add missing member in `Mob` class](https://github.com/EndstoneMC/endstone/commit/8b8cdc5c021ff989ed7b50190c3807e20ad92446)

**Observed change.** Adds Mob attack_anim float and updates Player inventory/name and ServerPlayer initialized offsets.

**Causal interpretation.** Repairs a missing native field rather than papering over only downstream offsets.

**Limits.** Offset comments/static assertions remain source hypotheses without native runtime validation.

<a id="commit-359"></a>
### Commit 359 {#commit-359}

8653ddabd63d4f48c7699bcc2d1cde5b73068951 · 2025-03-10T21:56:40Z

[fix: resolve compilation errors on Linux](https://github.com/EndstoneMC/endstone/commit/8653ddabd63d4f48c7699bcc2d1cde5b73068951)

**Observed change.** Completes vector element type for LegacyDependenciesUpgrade; replaces unavailable subpack/metadata pointed-to types with void* stand-ins.

**Causal interpretation.** Linux compilation repair uses full types where containers need them and opaque pointers where only pointer layout matters.

**Limits.** Reduces static type information; compile success is author-reported by title, not verified.

<a id="commit-391"></a>
### Commit 391 {#commit-391}

ed03eb02298773565e338618aa9a193214609a1d · 2025-03-14T21:23:10Z

[fix: resolve a crash on Linux](https://github.com/EndstoneMC/endstone/commit/ed03eb02298773565e338618aa9a193214609a1d)

**Observed change.** Models NetworkSystem tail: four incoming queues with callback/mutex, network flags/ports/stats and aligned PacketSecurityControllerFactory.

**Causal interpretation.** Author reports Linux crash repair through fuller layout/alignment model; sizeof/alignment affects enclosing native network owner.

**Limits.** No crash reproduced or native sizeof verified. Factory removed only on beta branch393, while400 main retains it.

<a id="commit-393"></a>
### Commit 393 {#commit-393}

0d05e555d44e05e7e997ee8c3b03904b20619cde · 2025-03-14T21:32:45Z

[feat: remove `PacketSecurityControllerFactory` from `NetworkSystem`](https://github.com/EndstoneMC/endstone/commit/0d05e555d44e05e7e997ee8c3b03904b20619cde)

**Observed change.** Removes nested security-controller/factory alias and aligned factory member from beta NetworkSystem.

**Causal interpretation.** Corrects native-version-specific tail model while retaining incoming queues/ports/stats.

**Limits.** This is beta-branch-only relative to400; cannot report removal as main endpoint behavior.
