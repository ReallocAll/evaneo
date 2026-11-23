<!-- retrieval: {"source_ids":["public:commit:14a484627cd35321fdf266dc50ce743dc493b6e6","public:commit:1a32ec86416614d890245ac5ed697f2b80b3f20a","public:commit:1d2df090d0007fd651bd24005479d36453ea2e92","public:commit:23dc25e2d55a050fce9655dfbb4d24ebc45c67e9","public:commit:355fa02fa24f4f37d6511eca850888438a63b3ea","public:commit:408e17b705dd84a2b9115b7e61163f29fe0bad21","public:commit:4abe7d51ce0e2482a9fbd2e085933845a780047b","public:commit:4c98e1a6afbba5de002790d38152c80ec576b237","public:commit:6c2c8ff4bb976a12810cd995ff17feafd717df0f","public:commit:6d719a902dc681910b9c629635f4a0ae72b56594","public:commit:6f646e0a0cc86deaa40675451cb0e9f6c925d2e6","public:commit:7561b70c35218f2b146aaaf1079aa2accce762fe","public:commit:774620efd7e715bbaea8f717163c1235c236c9e2","public:commit:8b7b1fbe55ca4c3a7793c4ba957519fdf912d6bc","public:commit:99b3437118e5f6493b0bf12142bfa902403492d7","public:commit:a1c6b008253ccf89cbcacac20c538ac1dfe0312d","public:commit:a2fe96273b9f64dd1d739d894a5a0e3f0e1ff50e","public:commit:b010d55d23b69dcc0fac3e8ac0215653bd676882","public:commit:b05c77a44b6fcf432d85648d8f4fe49d6ca3b5c1","public:commit:b9501c69a6349cc0ccbf0d645639cb045f998452","public:commit:bc48bd362a9563dc94ba4969d9307cd5ed1fa7e8","public:commit:c2b0823270987dbef66ef8cd1a735bfc3e8c392e","public:commit:cb950eaa8bb3a31cc92544884bb9cebd7473b5bd","public:commit:ccd918ed6e5adee7b05925332458c388073af0dd","public:commit:e5bf28afca0c350ff8555217d53cec24926243a0","public:commit:e9491ff861b1b087a4662d3963c5ddd8f0dc45cc","public:commit:f04604bc8ab4a8e1882f1010886041c935f415ae","public:commit:f088952b8712d77d81f2ba91883feeddc568d1a9","public:commit:f76cf4ad2868f6f7e89e578a16fc224be7300fe4","public:commit:fa73288dfa3e053267c6573136ff3852b62d6e47","public:commit:facfb51aee008b5359316ad5346df79ad721b831"],"source_type":"public","date":"2024-10-24..2024-12-18","topics":["lifetime","ffi","testing","build","api","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native compatibility is a coordinated migration {#native-compatibility-is-a-coordinated-migration}

## Causal chain and endpoint {#causal-chain-and-endpoint}

The 1.21.41 work (1922–1929) changes several dependent contracts together: symbol names/addresses, native virtual slots, class field offsets, weak ownership representation, event variant ordering and hook arguments. The spawn hook moves from ServerLevel to LevelEventCoordinator and receives ActorInitializationMethod; useItemOn adds and forwards a Boolean argument. A symbol at the old address with a new signature is not behavior-preserving merely because resolution succeeds.

NonOwnerPointer is especially instructive. 1922 adds a typed pointer and shared control state; 1923 replaces the control state's object pointer with a validity Boolean invalidated by the owner. The implementation first had a validation-order error, then assigns the control block before checking validity. At the1927 context, however, a typed null pointer can bypass _setControlBlock and still dereference control_block_; reset throws if the owner is already invalid, and the destructor calls reset. The apparent ownership abstraction therefore needs null, owner-destruction and noexcept-boundary tests. This source review establishes those code paths, not their native lifetime compatibility.

The resource repository layout is revised and partly reversed: new test pack-source fields appear at1923, then are removed at1927; the Windows size returns from592 to576. This is not a monotonic expansion or a stable preference for extra abstraction. Keep both experiments and the endpoint.

The 1.21.50 migration starts with1990 explicitly labelled “not supported yet”, even while package metadata changes to1.21.50. Dimension's polymorphic IntProvider, block storage composition and104-byte opaque storage, Actor initialization parameters, binary-stream buffer/view representation, and command-registry data widths all then change. The Linux Block size assertion is corrected312→320 at2000 after an initial same-size assumption. Biome's former FIXME is replaced by a richer layout, but MobSpawnerData and portions of the native component storage are still opaque.

CommandRegistry2017 is more than renaming: enum value pairs narrow64→32 bits, Symbol's default becomes-1, SemanticConstraint changes width, and parameter symbols become typed fields. It also removes vanilla /reload before saving registry state, so restoring that snapshot does not resurrect the vanilla command. Header cleanup2015 temporarily leaves a broken WebToken accessor and stale Certificate field access;2017 fixes both. The intermediate is not independently build-verified.

## Event dispatch failure and repair {#event-dispatch-failure-and-repair}

Adding ScriptModuleStartupEvent/ShutdownEvent at1992 changes the native variant alternatives. The new generic forwarding visitor can be selected ahead of the const-specific script-message handler for mutable references, skipping the Endstone event.2007 uses a decayed alternative type and if constexpr to dispatch script messages explicitly, retaining the null scripting handler guard. Its nondependent false static_assert is then removed at2010 to repair compilation. The endpoint forwards other variants generically rather than claiming exhaustive static checking. A source claim of compilation repair is not a compiler run in this review.

## Evidence, attribution and applicability {#evidence-attribution-and-applicability}

Canonical all-parent diffs retain every numeric map update and vtable change. Context reads include the full NonOwnerPointer implementation and BEDROCK_STATIC_ASSERT_SIZE definition. The latter is enabled only under NDEBUG, with platform-selected sizes; Debug builds do not supply those assertions. Even an executed size assertion would not validate offsets, virtual ordering, semantic meaning, native allocator behavior or event discriminants. The native engine binaries, symbol-discovery process and external dependency implementations were not inspected or executed here.

Useful application: treat version support as a checklist of mutually dependent representations and test both supported platforms, native calls, null/expired references and event variants. Do not infer an author's universal design preference from reverse-engineered declarations, opaque padding, short-lived broken commits, or address tables.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-1922"></a>
### Commit 1922 {#commit-1922}

c2b0823270987dbef66ef8cd1a735bfc3e8c392e · 2024-10-24T16:10:06Z

[feat: support BDS v1.21.41 Windows (WIP)](https://github.com/EndstoneMC/endstone/commit/c2b0823270987dbef66ef8cd1a735bfc3e8c392e)


1.21.41 Windows WIP changes NonOwnerPointer to retain a typed raw pointer alongside shared control state; expands ILevel virtual slots, changes scoreboard constructor to NonOwnerPointer gameplay manager, replaces static creative-item hook with registry instance traversal, refreshes Windows addresses/version, and supplies Endstone/Minecraft User-Agent on downloads. Intermediate _setControlBlock checks validity before assignment and null pointer construction dereferences absent control; 1923 repairs ordering but retains the typed-null branch risk. Removed Windows resetPlayerScore address restored by1923. No native execution validates layouts/addresses.

Static review only; no upstream execution.

<a id="commit-1923"></a>
### Commit 1923 {#commit-1923}

6c2c8ff4bb976a12810cd995ff17feafd717df0f · 2024-10-24T18:20:39Z

[fix: NonOwnerPointer and ResourcePackRepository](https://github.com/EndstoneMC/endstone/commit/6c2c8ff4bb976a12810cd995ff17feafd717df0f)


Changes control block from object pointer to boolean validity; destructor invalidates it and NonOwnerPointer keeps typed address. Assigns control block before validity test, repairing1922 ordering. Constructor still tests control_block_->is_valid after if(ptr), so typed null pointer input remains unsafe (nullptr_t overload is distinct). Adds ResourcePackRepository test-source slots and missing virtual method; restores scoreboard symbol. Test-source slots are removed again1927, so not final layout.

Static review only; no upstream execution.

<a id="commit-1924"></a>
### Commit 1924 {#commit-1924}

f04604bc8ab4a8e1882f1010886041c935f415ae · 2024-10-24T21:24:07Z

[fix: BlockLegacy, Item, PacketSender, ServerNetworkHandler](https://github.com/EndstoneMC/endstone/commit/f04604bc8ab4a8e1882f1010886041c935f415ae)


Updates packet/disconnect enums, adds PacketSender::isInitialized and forwarding wrapper, repairs Item/BlockLegacy virtual declarations, item registry reverse-alias map, network-handler layout, Linux scoreboard sizes, and recipe user-data-shapeless names. Removes obsolete BlockLegacy virtuals/fields; exported recipe key changes while UI key still shulkerBox pending1925. Native mappings are source models, not verified engine ABI.

Static review only; no upstream execution.

<a id="commit-1925"></a>
### Commit 1925 {#commit-1925}

bc48bd362a9563dc94ba4969d9307cd5ed1fa7e8 · 2024-10-24T21:40:58Z

[fix: Biome class members](https://github.com/EndstoneMC/endstone/commit/bc48bd362a9563dc94ba4969d9307cd5ed1fa7e8)


Recalculates ResourcePackRepository offsets for expanded nonowner pointers and Linux size504; Biome removes fog weak ref and uses uint16 id; devtools label becomes User Data Shapeless. Follow-up1927 removes test pack sources and revises Windows size.

Static review only; no upstream execution.

<a id="commit-1926"></a>
### Commit 1926 {#commit-1926}

23dc25e2d55a050fce9655dfbb4d24ebc45c67e9 · 2024-10-24T22:40:58Z

[fix: Actor virtual functions](https://github.com/EndstoneMC/endstone/commit/23dc25e2d55a050fce9655dfbb4d24ebc45c67e9)


Removes obsolete Actor save, spin-attack and touch-autoattack virtual declarations plus commented slots, realigning native vtable assumptions without executed ABI verification.

Static review only; no upstream execution.

<a id="commit-1927"></a>
### Commit 1927 {#commit-1927}

355fa02fa24f4f37d6511eca850888438a63b3ea · 2024-10-25T09:45:35Z

[fix: ResourcePackRepository member variables](https://github.com/EndstoneMC/endstone/commit/355fa02fa24f4f37d6511eca850888438a63b3ea)


Removes test_behavior_pack_source_ and test_resource_pack_source_ added1923, shifts repository layout back and changes Windows size592 to576 while Linux stays504. Offset comments are partial and cannot substitute runtime ABI proof.

Static review only; no upstream execution.

<a id="commit-1928"></a>
### Commit 1928 {#commit-1928}

fa73288dfa3e053267c6573136ff3852b62d6e47 · 2024-10-25T10:32:37Z

[fix: update function signatures in GameMode, ServerLevel and LevelEventCoordinator](https://github.com/EndstoneMC/endstone/commit/fa73288dfa3e053267c6573136ff3852b62d6e47)


Moves postReloadActorAdded hook from ServerLevel to LevelEventCoordinator with ActorInitializationMethod, preserving nonplayer spawn event then cancellation/despawn; adds bool is_first_event to GameMode::useItemOn and forwards it. Changes corresponding Windows decorated signatures; same address can require a different callable signature.

Static review only; no upstream execution.

<a id="commit-1929"></a>
### Commit 1929 {#commit-1929}

4c98e1a6afbba5de002790d38152c80ec576b237 · 2024-10-25T10:52:20Z

[feat: support BDS v1.21.41 Linux (WIP)](https://github.com/EndstoneMC/endstone/commit/4c98e1a6afbba5de002790d38152c80ec576b237)


Refreshes Linux1.21.41 address map, removes static creative-item and Level gameplay-manager hooks, migrates spawn hook and useItemOn bool signature and ServerScoreboard NonOwnerPointer constructor. Numeric values read; their native correctness is not established.

Static review only; no upstream execution.

<a id="commit-1938"></a>
### Commit 1938 {#commit-1938}

a2fe96273b9f64dd1d739d894a5a0e3f0e1ff50e · 2024-10-27T17:36:32Z

[feat: add ContainerType](https://github.com/EndstoneMC/endstone/commit/a2fe96273b9f64dd1d739d894a5a0e3f0e1ff50e)


Adds int8 ContainerType values and expands native container virtual interface for slot copies/counts/transactions/names/save data. Declaration alignment is not native runtime validation.

Static review only; no upstream execution.

<a id="commit-1947"></a>
### Commit 1947 {#commit-1947}

774620efd7e715bbaea8f717163c1235c236c9e2 · 2024-11-04T17:21:42Z

[refactor: separate definitions from declarations](https://github.com/EndstoneMC/endstone/commit/774620efd7e715bbaea8f717163c1235c236c9e2)


Moves Ability/Abilities method bodies from header to source with same logic, removes unnecessary entt header dependencies and Windows AttributesComponent type_hash static_assert. Assertion removal is meaningful verification loss, so not wholly mechanical.

Static review only; no upstream execution.

<a id="commit-1967"></a>
### Commit 1967 {#commit-1967}

8b7b1fbe55ca4c3a7793c4ba957519fdf912d6bc · 2024-11-26T20:27:05Z

[feat: support BDS v1.21.44 Windows](https://github.com/EndstoneMC/endstone/commit/8b7b1fbe55ca4c3a7793c4ba957519fdf912d6bc)


Refreshes Windows addresses and both package/map version to1.21.44. Values vary by symbol; numeric map read but no native verification. Linux map not updated until1985.

Static review only; no upstream execution.

<a id="commit-1985"></a>
### Commit 1985 {#commit-1985}

b010d55d23b69dcc0fac3e8ac0215653bd676882 · 2024-12-02T13:44:06Z

[feat: support BDS v1.21.44 Linux](https://github.com/EndstoneMC/endstone/commit/b010d55d23b69dcc0fac3e8ac0215653bd676882)


Refreshes Linux1.21.44 symbol addresses; no native engine code or runtime checked.

Static review only; no upstream execution.

<a id="commit-1990"></a>
### Commit 1990 {#commit-1990}

e9491ff861b1b087a4662d3963c5ddd8f0dc45cc · 2024-12-04T18:56:44Z

[chore: update symbols.toml for BDS v1.21.50 Windows (not supported yet)](https://github.com/EndstoneMC/endstone/commit/e9491ff861b1b087a4662d3963c5ddd8f0dc45cc)


Refreshes Windows symbol addresses and declared Minecraft version to 1.21.50; commit explicitly says not supported yet. Version metadata is not evidence that layouts or runtime work.

Static review only; no upstream execution.

<a id="commit-1991"></a>
### Commit 1991 {#commit-1991}

99b3437118e5f6493b0bf12142bfa902403492d7 · 2024-12-05T09:25:12Z

[fix: add missing virtual functions in IResourcePackRepository](https://github.com/EndstoneMC/endstone/commit/99b3437118e5f6493b0bf12142bfa902403492d7)


Adds repository virtual addTempWorldTemplateResourcePacks, removes obsolete initialization hook declaration, and moves signal-handler registration into EndstoneServer construction. This changes installation timing rather than only names.

Static review only; no upstream execution.

<a id="commit-1992"></a>
### Commit 1992 {#commit-1992}

6d719a902dc681910b9c629635f4a0ae72b56594 · 2024-12-05T10:06:47Z

[fix: ScriptingGameplayEvent variants](https://github.com/EndstoneMC/endstone/commit/6d719a902dc681910b9c629635f4a0ae72b56594)


Adds startup/shutdown script event alternatives, moves Linux source-created/destroyed and protected level methods to Level, adds cerealContext slots, and uses each ScriptCommandMessageEvent level instead of dereferencing server level. Generic visitor can win overload resolution; corrected2007/2010. Redundant getLevel conditional later removed2003.

Static review only; no upstream execution.

<a id="commit-1993"></a>
### Commit 1993 {#commit-1993}

b05c77a44b6fcf432d85648d8f4fe49d6ca3b5c1 · 2024-12-05T10:31:42Z

[fix: Dimension class members](https://github.com/EndstoneMC/endstone/commit/b05c77a44b6fcf432d85648d8f4fe49d6ca3b5c1)


Completes IDimension virtual slots and inserts sea level, spawn light limit and polymorphic variant IntProvider before block_source; moves level/name/id offsets. New ConstantInt/UniformInt are native-layout declarations, not implemented generation algorithms.

Static review only; no upstream execution.

<a id="commit-1994"></a>
### Commit 1994 {#commit-1994}

f088952b8712d77d81f2ba91883feeddc568d1a9 · 2024-12-05T10:36:57Z

[fix: PlayerGameplayEvent variants](https://github.com/EndstoneMC/endstone/commit/f088952b8712d77d81f2ba91883feeddc568d1a9)


Inserts PlayerInputModeChangeEvent and PlayerScriptInputEvent at native variant positions. Ordering changes discriminant interpretation even though event bodies remain opaque.

Static review only; no upstream execution.

<a id="commit-1995"></a>
### Commit 1995 {#commit-1995}

1d2df090d0007fd651bd24005479d36453ea2e92 · 2024-12-05T10:43:30Z

[fix: update enums](https://github.com/EndstoneMC/endstone/commit/1d2df090d0007fd651bd24005479d36453ea2e92)


Renames deprecated disconnect/platform enum values without renumbering and adds camera presets packet320, EndId321 and Creaking actor146|Monster. Player OS switch follows renamed enum.

Static review only; no upstream execution.

<a id="commit-1996"></a>
### Commit 1996 {#commit-1996}

a1c6b008253ccf89cbcacac20c538ac1dfe0312d · 2024-12-05T12:05:05Z

[fix: Block and BlockLegacy](https://github.com/EndstoneMC/endstone/commit/a1c6b008253ccf89cbcacac20c538ac1dfe0312d)


Replaces inherited BlockComponentStorage with composed opaque104-byte storage, remaps Block network ID and BlockLegacy fields, adds liquid DetectionRule, and removes obsolete virtuals. Temporarily disables canContainLiquid devtool output. Getters move unchanged into source. Storage internals remain padding, so size assertions cannot prove behavior; Linux size corrected2000.

Static review only; no upstream execution.

<a id="commit-1997"></a>
### Commit 1997 {#commit-1997}

408e17b705dd84a2b9115b7e61163f29fe0bad21 · 2024-12-05T12:32:59Z

[fix: Item and ItemRegistry](https://github.com/EndstoneMC/endstone/commit/408e17b705dd84a2b9115b7e61163f29fe0bad21)


Adds redacted description virtual placeholder with intentionally approximate return type, narrows use_anim to uint8, inserts ItemRegistry cereal context and unique-owned publisher. ABI slot/layout compatibility, not new item functionality.

Static review only; no upstream execution.

<a id="commit-1998"></a>
### Commit 1998 {#commit-1998}

f76cf4ad2868f6f7e89e578a16fc224be7300fe4 · 2024-12-05T13:10:28Z

[fix: Actor class](https://github.com/EndstoneMC/endstone/commit/f76cf4ad2868f6f7e89e578a16fc224be7300fe4)


Replaces opaque Actor initialization array with nine-pointer VariantParameterList, expands formerly unknown fields, and shifts dimension/level offsets to456/472. Removes canAttack virtual slot; public field exposure enables later metadata access. Native correctness remains unexecuted.

Static review only; no upstream execution.

<a id="commit-1999"></a>
### Commit 1999 {#commit-1999}

1a32ec86416614d890245ac5ed697f2b80b3f20a · 2024-12-05T13:42:25Z

[fix: BlockSource and BinaryStream](https://github.com/EndstoneMC/endstone/commit/1a32ec86416614d890245ac5ed697f2b80b3f20a)


ReadOnlyBinaryStream now owns buffer plus string_view before cursor; BinaryStream removes duplicate ownedbuffer. Size assertions differ Windows/Linux. Moves mutable removeBlock/postGameEvent virtuals to IBlockSource and inserts seed/height slots.

Static review only; no upstream execution.

<a id="commit-2000"></a>
### Commit 2000 {#commit-2000}

facfb51aee008b5359316ad5346df79ad721b831 · 2024-12-05T13:56:02Z

[fix: correct size assertion for Block class](https://github.com/EndstoneMC/endstone/commit/facfb51aee008b5359316ad5346df79ad721b831)


Corrects Block Linux size312→320 while Windows312 stays; removes unused Boost includes in opaque storage. Demonstrates same apparent fields do not imply equal cross-platform layout.

Static review only; no upstream execution.

<a id="commit-2003"></a>
### Commit 2003 {#commit-2003}

b9501c69a6349cc0ccbf0d645639cb045f998452 · 2024-12-06T07:17:28Z

[chore: update symbols.toml for BDS v1.21.50 Linux](https://github.com/EndstoneMC/endstone/commit/b9501c69a6349cc0ccbf0d645639cb045f998452)


Refreshes full Linux1.21.50 symbol map and simplifies getLevel to unique_ptr.get. Symbol addresses remain opaque external-binary assumptions, not a validated runtime result.

Static review only; no upstream execution.

<a id="commit-2004"></a>
### Commit 2004 {#commit-2004}

cb950eaa8bb3a31cc92544884bb9cebd7473b5bd · 2024-12-06T07:29:40Z

[fix: make Level::_cerealContext() a pure virtual function.](https://github.com/EndstoneMC/endstone/commit/cb950eaa8bb3a31cc92544884bb9cebd7473b5bd)


Makes ILevel::_cerealContext pure virtual, resolving declaration semantics after1992; not proof of binary slot accuracy.

Static review only; no upstream execution.

<a id="commit-2007"></a>
### Commit 2007 {#commit-2007}

ccd918ed6e5adee7b05925332458c388073af0dd · 2024-12-06T15:41:08Z

[fix(event): ensure ScriptMessageEvent is invoked correctly](https://github.com/EndstoneMC/endstone/commit/ccd918ed6e5adee7b05925332458c388073af0dd)


Replaces overloaded const-specific plus forwarding visitor with if-constexpr on decayed variant alternative so mutable ValueOrRef cannot select generic path and skip ScriptMessageEvent. Adds startup/shutdown branches but nondependent static_assert false is compilation trouble removed2010. Null scripting handler guard preserved only for script messages.

Static review only; no upstream execution.

<a id="commit-2010"></a>
### Commit 2010 {#commit-2010}

4abe7d51ce0e2482a9fbd2e085933845a780047b · 2024-12-06T17:18:11Z

[fix: compilation error in ScriptingEventCoordinator](https://github.com/EndstoneMC/endstone/commit/4abe7d51ce0e2482a9fbd2e085933845a780047b)


Removes nondependent false static_assert and explicit alternative branches from2007, forwards every event after conditional ScriptMessageEvent dispatch. Exhaustiveness checking is abandoned to restore compile viability; no build run.

Static review only; no upstream execution.

<a id="commit-2012"></a>
### Commit 2012 {#commit-2012}

7561b70c35218f2b146aaaf1079aa2accce762fe · 2024-12-16T14:54:07Z

[fix: update Biome class members](https://github.com/EndstoneMC/endstone/commit/7561b70c35218f2b146aaaf1079aa2accce762fe)


Biome moves id to346 after eight-category mob maps, narrows return to BiomeIdType and adds componentstorage32-byte declaration. Replaces old FIXME layout, yet MobSpawnerData stays empty/opaque; static assertions are source checks, not runtime evidence.

Static review only; no upstream execution.

<a id="commit-2013"></a>
### Commit 2013 {#commit-2013}

6f646e0a0cc86deaa40675451cb0e9f6c925d2e6 · 2024-12-16T15:49:29Z

[ci: fix static_assert macros for class size checks](https://github.com/EndstoneMC/endstone/commit/6f646e0a0cc86deaa40675451cb0e9f6c925d2e6)


Uses BEDROCK_STATIC_ASSERT_SIZE for Biome component base/storage instead of unconditional assertions; exact assertion gate evaluated in context.

Static review only; no upstream execution.

<a id="commit-2015"></a>
### Commit 2015 {#commit-2015}

e5bf28afca0c350ff8555217d53cec24926243a0 · 2024-12-18T18:36:53Z

[refactor: correct headers](https://github.com/EndstoneMC/endstone/commit/e5bf28afca0c350ff8555217d53cec24926243a0)


Relocates identical AppPlatformListener header and encapsulates WebToken with getData. Getter mistakenly returns data_info rather than data_info_, and Certificate still uses old direct field, repaired2017. Not safe to label this isolated commit build-clean.

Static review only; no upstream execution.

<a id="commit-2017"></a>
### Commit 2017 {#commit-2017}

14a484627cd35321fdf266dc50ce743dc493b6e6 · 2024-12-18T20:57:17Z

[refactor: update members in CommandRegistry](https://github.com/EndstoneMC/endstone/commit/14a484627cd35321fdf266dc50ce743dc493b6e6)


CommandRegistry refactor changes enum value pair width64→32, default Symbol0→-1, semantic constraint width, adds stats pointer and typed parameter symbols; updates consumers. Moves vanilla reload removal before registry snapshot so restore no longer reintroduces it. Also fixes WebToken accessor and Certificate compile regressions2015. Native widths remain unverified.

Static review only; no upstream execution.
