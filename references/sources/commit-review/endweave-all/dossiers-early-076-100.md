<!-- retrieval: {"source_ids":["public:commit:1259aa912031a94b3a5ae4fd20a3761e8ffb939e","public:commit:1800838bf18ae0bf11864d3ff14b11c1fe9c93ad","public:commit:198ee0c3ec5a9d731717271b2c7f485cef94831b","public:commit:1e38cb83739d515d1dbfb9aec8a7c641b63d4bef","public:commit:24631fbd24fbacb9f593f1adecb3783be0f2c7ed","public:commit:3589ac5dde062888601f2f0b9ca0da24b623639f","public:commit:41a45e916d25173c10ddde6f8b165d67f2d6836e","public:commit:450237d77a73296b4e0b4ecb5565a9ee9eba32bf","public:commit:4f133e86b919a20b460275cccf4f62c7c875666b","public:commit:5bc2ab2c01200593a088889b3907b4085937b470","public:commit:646899945abd71630fe3e5e91665ee87794ef2d1","public:commit:6761a89d2f8cd31634a71f0054a48c7f82e1e88e","public:commit:6b0d8e52e69a434de7eb7527a5dd977957c776e8","public:commit:82001578c3026058ee41439e6e3ca61fb8958d1f","public:commit:996b6de9b8bc1a058f570b5198347e8111f28f7d","public:commit:9dc1c1573e29494d4cedb7993854811697cbcd11","public:commit:a72f99705dd77f6a2f1a9058a2b9dc366d82028e","public:commit:a79e8b5759ea731bd3a07a44bc626e885d419c29","public:commit:afbe3bbae3f8a59103a2f2d62dc1a7fc8fcf66c8","public:commit:d2514fa239d97895b1eb474955a69d952de1e154","public:commit:db1319057c883ddd6c640631a9979d6d9d923bcf","public:commit:ee8dae61bf3cbb03a8116a4afda97bc00eceb334","public:commit:f55a7983fb603faa5782ce673378d7c8c43242c1","public:commit:f6dabe32905aa7e73beed36d87a5b2a7252f4df2","public:commit:fdbe8bd746b854ffd9406cd454ede36c8274b1fd"],"source_type":"public","date":"2026-03-25..2026-03-29","topics":["lifetime","concurrency","testing","api","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endweave-commit-dossiers-assignment-ordinals-76-100"></a>
# Endweave commit dossiers: assignment ordinals 76–100 {#endweave-commit-dossiers-assignment-ordinals-76-100}

Static source review. Assignment ordinals are identifiers, not a topological ordering. Exact parents below define ancestry. Acquired but unread entries remain open. No upstream code, tests or workflows executed. Generated data must receive a separate structural audit before closure.

## 76. fix: correct inline comments and use OptionalType in UI handlers {#76-fix-correct-inline-comments-and-use-optionaltype-in-ui-handlers}
- Commit: [6b0d8e52e69a434de7eb7527a5dd977957c776e8](https://github.com/EndstoneMC/endweave/commit/6b0d8e52e69a434de7eb7527a5dd977957c776e8)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-25T21:32:19Z; committed: 2026-03-25T21:32:19Z
- Parents: ed1d81b2e0e30c35f847f5840c1e721e3294e914
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/v924_to_v898/handlers/text.py, src/endstone_endweave/protocol/v924_to_v944/handlers/data_driven_ui.py, src/endstone_endweave/protocol/v944_to_v924/handlers/data_driven_ui.py, src/endstone_endweave/protocol/v944_to_v924/handlers/sound_event.py, src/endstone_endweave/protocol/v944_to_v924/handlers/start_game.py, src/endstone_endweave/protocol/v944_to_v924/handlers/voxel_shapes.py

Title emphasizes comments/UI OptionalType, but StartGame944-to924 field sequence also changes: removes a third post-experiments BOOL and reduces force-experimental section from a BOOL plus conditional BOOL pair to one BOOL. These are substantive cursor/framing changes, not comment-only. Vectors replace equivalent float sequences; UI absence maps to OptionalType(None). Reverse voxel code still discards first ushort although new comment calls it custom-shape count; this is the unresolved PR4 end-of-payload discrepancy. No tests added; claimed validation against official definitions remains commit-author rationale, not independent runtime verification.

### Evidence limits {#source-acquisition-evidence}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 77. feat: add missing v898<->v924 handlers {#77-feat-add-missing-v898---v924-handlers}
- Commit: [646899945abd71630fe3e5e91665ee87794ef2d1](https://github.com/EndstoneMC/endweave/commit/646899945abd71630fe3e5e91665ee87794ef2d1)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-25T21:50:57Z; committed: 2026-03-25T21:50:57Z
- Parents: 6b0d8e52e69a434de7eb7527a5dd977957c776e8
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/camera.py, src/endstone_endweave/protocol/v898_to_v924/handlers/book_edit.py, src/endstone_endweave/protocol/v898_to_v924/handlers/camera.py, src/endstone_endweave/protocol/v898_to_v924/handlers/gameplay.py, src/endstone_endweave/protocol/v898_to_v924/protocol.py, src/endstone_endweave/protocol/v924_to_v898/handlers/book_edit.py, src/endstone_endweave/protocol/v924_to_v898/handlers/camera.py, src/endstone_endweave/protocol/v924_to_v898/protocol.py

Adds bidirectional BookEdit field-order and byte/varint page-index conversion, explicit unknown-action ValueError, with narrowed-byte range behavior delegated to writer. Extends shared spline representation with898 encoding that injects linear easing0 or drops easing; replaces CameraInstruction cancellation with conditional traversal/map in924-to898 and adds reverse handler. GraphicsParameterOverride upgrade writes two absent optionals after existing value list. This is lossy downgrade/default synthesis, not universal invertibility. No tests accompany newly supported actions, populated spline branches or graphics options.

### Evidence limits {#source-acquisition-evidence-2}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 78. refactor: replace _passthrough_ helpers with compound Types {#78-refactor-replace-passthrough-helpers-with-compound-types}
- Commit: [afbe3bbae3f8a59103a2f2d62dc1a7fc8fcf66c8](https://github.com/EndstoneMC/endweave/commit/afbe3bbae3f8a59103a2f2d62dc1a7fc8fcf66c8)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-25T22:02:06Z; committed: 2026-03-25T22:02:06Z
- Parents: 646899945abd71630fe3e5e91665ee87794ef2d1
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/data_store.py, src/endstone_endweave/codec/types/gameplay.py, src/endstone_endweave/protocol/v860_to_v898/handlers/gameplay.py, src/endstone_endweave/protocol/v898_to_v860/handlers/gameplay.py, src/endstone_endweave/protocol/v898_to_v924/handlers/data_store.py, src/endstone_endweave/protocol/v898_to_v924/handlers/gameplay.py, src/endstone_endweave/protocol/v924_to_v898/handlers/data_store.py, src/endstone_endweave/protocol/v924_to_v898/handlers/gameplay.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v944_to_v924/handlers/start_game.py, tests/test_start_game.py

Centralizes repeated sequences into Priority/ItemSetting/BlockProperty pairs, GameRules discriminated values, signed-versus-unsigned Experiments counts and recursive ChangeValue. Experiments codec deliberately excludes ever_toggled, which handlers/tests now copy separately. Recursive data-store maps preserve ordered duplicate keys as entry lists, unlike NBT dicts; no depth/resource guard is introduced. Dispatch rejects unknown value kinds. Existing tests migrate helper calls; no new recursive-boundary cases. Important inherited defect remains:898-to860 aim-assist reads/drops block-tag count but passthroughs its entries, leaving unframed data; refactor preserves that behavior rather than fixing it.

### Evidence limits {#source-acquisition-evidence-3}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 79. refactor: extract biome_definition_list helpers into compound Types {#79-refactor-extract-biomedefinitionlist-helpers-into-compound-types}
- Commit: [f6dabe32905aa7e73beed36d87a5b2a7252f4df2](https://github.com/EndstoneMC/endweave/commit/f6dabe32905aa7e73beed36d87a5b2a7252f4df2)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-25T22:12:07Z; committed: 2026-03-25T22:12:07Z
- Parents: afbe3bbae3f8a59103a2f2d62dc1a7fc8fcf66c8
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/biome.py, src/endstone_endweave/protocol/v924_to_v898/handlers/biome_definition_list.py

Reifies deeply nested biome generation wire structures into paired read/write dataclasses: climate, weighted rules, coordinates/scatter/features, surface/mountain/capped/mesa parameters, replacements and chunk generation. Carefully preserves distinction between absent optional arrays and present empty lists.924 variant alone reads/writes trailing optional village_type;898 serializer drops it. Handler maps each definition while retaining biome-name ushort index and trailing string table. This reconstructs objects instead of22 streaming helpers and supplies future reverse capability, but no reverse handler or new tests is added here. Generic placeholder field names remain evidence of incomplete semantic naming, not a new specification.

### Evidence limits {#source-acquisition-evidence-4}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 80. refactor: align dataclass names with official DOT/BDS names {#80-refactor-align-dataclass-names-with-official-dot-bds-names}
- Commit: [1800838bf18ae0bf11864d3ff14b11c1fe9c93ad](https://github.com/EndstoneMC/endweave/commit/1800838bf18ae0bf11864d3ff14b11c1fe9c93ad)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-25T22:48:56Z; committed: 2026-03-25T22:48:56Z
- Parents: f6dabe32905aa7e73beed36d87a5b2a7252f4df2
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/actor_data.py, src/endstone_endweave/codec/types/biome.py, src/endstone_endweave/codec/types/item.py, src/endstone_endweave/protocol/v924_to_v898/handlers/sound_event.py, tests/test_codec.py

Systematically renames biome dataclasses/type classes to DOT/BDS-derived Biome*Data names and ActorDataEntry to ActorDataItem; ItemInstance public name remains, private codec becomes _ItemInstanceType. Full diff retains field types/order and dispatch. Test class alone changes to TestNetworkItemInstanceDescriptor despite unchanged public ItemInstance, a naming inconsistency rather than behavior change. Names express source-alignment rationale, not independently validated equivalence to official implementations.

### Evidence limits {#source-acquisition-evidence-5}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 81. refactor: replace _ActorDataListType with ArrayType(ACTOR_DATA_ITEM) {#81-refactor-replace-actordatalisttype-with-arraytype-actordataitem}
- Commit: [6761a89d2f8cd31634a71f0054a48c7f82e1e88e](https://github.com/EndstoneMC/endweave/commit/6761a89d2f8cd31634a71f0054a48c7f82e1e88e)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-25T22:50:41Z; committed: 2026-03-25T22:50:41Z
- Parents: 1800838bf18ae0bf11864d3ff14b11c1fe9c93ad
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/actor_data.py

Extracts standalone ACTOR_DATA_ITEM key/type/value dispatch and defines ACTOR_DATA_LIST as ArrayType(ACTOR_DATA_ITEM). Preserves unsigned count and unknown-type lookup error while eliminating bespoke list loop. Reusable scalar codec is the concrete abstraction gain; no test changes or new behavior demonstrated.

### Evidence limits {#source-acquisition-evidence-6}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 82. refactor: inline Priority, ItemSetting, BlockProperty types {#82-refactor-inline-priority-itemsetting-blockproperty-types}
- Commit: [fdbe8bd746b854ffd9406cd454ede36c8274b1fd](https://github.com/EndstoneMC/endweave/commit/fdbe8bd746b854ffd9406cd454ede36c8274b1fd)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-25T22:58:34Z; committed: 2026-03-25T22:58:34Z
- Parents: 6761a89d2f8cd31634a71f0054a48c7f82e1e88e
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/gameplay.py, src/endstone_endweave/protocol/v860_to_v898/handlers/gameplay.py, src/endstone_endweave/protocol/v898_to_v860/handlers/gameplay.py, src/endstone_endweave/protocol/v898_to_v924/handlers/gameplay.py, src/endstone_endweave/protocol/v924_to_v898/handlers/gameplay.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v944_to_v924/handlers/start_game.py

Reverses part of78: removes Priority, ItemSetting and BlockProperty dataclasses/codecs because they lack standalone DOT/BDS counterparts, inlining pair sequences and counts in handlers. Keeps official GameRule/Experiment/ChangeValue types. Thus extraction is governed by domain fidelity, not deduplication alone. Preserves correct read-only dropping of924-to898 entity-family priorities and the distinct inherited898-to860 dropped-count/passthrough-entry defect. No new tests or wire-fix claim warranted.

### Evidence limits {#source-acquisition-evidence-7}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 83. refactor: centralize sound/ActorData remapping with SoundRewriter {#83-refactor-centralize-sound-actordata-remapping-with-soundrewriter}
- Commit: [f55a7983fb603faa5782ce673378d7c8c43242c1](https://github.com/EndstoneMC/endweave/commit/f55a7983fb603faa5782ce673378d7c8c43242c1)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-25T23:12:49Z; committed: 2026-03-25T23:12:49Z
- Parents: fdbe8bd746b854ffd9406cd454ede36c8274b1fd
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/sound_rewriter.py, src/endstone_endweave/protocol/v860_to_v898/handlers/gameplay.py, src/endstone_endweave/protocol/v860_to_v898/handlers/sound_event.py, src/endstone_endweave/protocol/v860_to_v898/protocol.py, src/endstone_endweave/protocol/v898_to_v860/handlers/gameplay.py, src/endstone_endweave/protocol/v898_to_v860/handlers/sound_event.py, src/endstone_endweave/protocol/v898_to_v860/protocol.py, src/endstone_endweave/protocol/v924_to_v898/handlers/sound_event.py, src/endstone_endweave/protocol/v924_to_v898/protocol.py, src/endstone_endweave/protocol/v924_to_v944/handlers/sound_event.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, src/endstone_endweave/protocol/v944_to_v924/handlers/sound_event.py, src/endstone_endweave/protocol/v944_to_v924/protocol.py

Centralizes five repeated sound/spawn/ActorData handler sets into configurable SoundRewriter, filtering dropped metadata before applying type2/type7 integer remappers. Registers five clientbound packet handlers per configured protocol, with bound methods retaining configuration object. Moves860/898 ActorEvent shifting/cancellation into gameplay. Version constants/functions remain in factories:566+12, reverse inserted-range fallback578,924-to898 cap578/drop136–138,924/944597+2 and inverse. Refactor retains inconsistent heartbeat key127 in older pairs versus126 in924/944 and suspect fallback boundaries later corrected121; centralization alone does not validate constants. Full deletions/additions read; no tests added.

### Evidence limits {#source-acquisition-evidence-8}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 84. fix: rewrite serverbound BlockActorData position for v944 clients {#84-fix-rewrite-serverbound-blockactordata-position-for-v944-clients}
- Commit: [ee8dae61bf3cbb03a8116a4afda97bc00eceb334](https://github.com/EndstoneMC/endweave/commit/ee8dae61bf3cbb03a8116a4afda97bc00eceb334)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-26T12:23:09Z; committed: 2026-03-26T12:23:09Z
- Parents: f55a7983fb603faa5782ce673378d7c8c43242c1
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, CLAUDE.md, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, tests/test_block_pos.py

Adds missing serverbound BlockActorData reverse position transform for newer clients, keeping NBT tail unchanged with test. Changelog replaces internal refactoring detail with user-visible sign-edit/dye failure and adds historical guidance for admin audience. Reverse older-client scenario still missing until115.

### Evidence limits {#source-acquisition-evidence-9}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 85. refactor: restructure tests to align with ViaVersion philosophy {#85-refactor-restructure-tests-to-align-with-viaversion-philosophy}
- Commit: [db1319057c883ddd6c640631a9979d6d9d923bcf](https://github.com/EndstoneMC/endweave/commit/db1319057c883ddd6c640631a9979d6d9d923bcf)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-26T12:49:11Z; committed: 2026-03-26T12:49:11Z
- Parents: ee8dae61bf3cbb03a8116a4afda97bc00eceb334
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tests/helpers.py, tests/test_block_pos.py, tests/test_codec.py, tests/test_login_rewriter.py, tests/test_sound_rewriter.py, tests/test_start_game.py, tests/test_v924_to_v944.py, tests/test_wrapper.py

Explicit type-centric testing policy: consolidate primitive/compound roundtrips and negative-Y conversions in test_codec, wrapper mechanics in test_wrapper, login/StartGame/complex handlers in one protocol suite; shared packet builders eliminate duplication. All full additions/deletions read. New branch tests cover note-block threshold16+4, map creation/decorations, UseItem negativeY/cooldown removal, legacy slots, optional camera sections and nonempty spline defaults; SoundRewriter covers597 threshold and heartbeat126 versus unrelated key. Deletes direct tests for simple positional handlers including ContainerOpen negativeY, trusting framework/type tests instead; that loses proof of each handler choosing correct offset/direction even when the type is correct. Synthetic fixture limits persist: structure verifier stops before rotation pivot/trailing fields; camera spline presence sometimes checked only by length/consumption; StartGame validates initial spawn and substring tails rather than fully parsing output. No multi-hop or actual-client interoperability proof, and no tests executed here. Policy is explicitly stated in this commit, scoped to this project/time rather than universal author preference.

### Evidence limits {#source-acquisition-evidence-10}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 86. Rewrite protocol diff tools with Pydantic models and pydot {#86-rewrite-protocol-diff-tools-with-pydantic-models-and-pydot}
- Commit: [4f133e86b919a20b460275cccf4f62c7c875666b](https://github.com/EndstoneMC/endweave/commit/4f133e86b919a20b460275cccf4f62c7c875666b)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-27T15:12:44Z; committed: 2026-03-27T15:12:44Z
- Parents: 706d055406b63234396bb0e7a2dd655782d4e16f
- Reading: non-generated diffs read; generated lock artifacts structurally audited
- Changed files: pyproject.toml, tools/generate_diff.py, tools/models.py, tools/parse_protocol_docs.py, uv.lock

Replaces regex DOT graph parsing with pydot, adds typed Pydantic Field/PacketDefinition/ProtocolDiff models, explicit packet IDs/direction and separate packet versus subtype additions/removals. Two-pass registry expands opaque referenced types so nested BlockPos changes can surface in StartGame/MapItemData/PlayerAuthInput. Graph root is inferred from edges or numeric fallback rather than requiring node0; reference resolution has a visited-type guard, but initial graph-tree recursion and JSON reference recursion remain unguarded. Broad DOT parse exceptions silently skip files. Node-ID noise filtering suppresses any added/removed dotted path containing node_NNN, which can hide descendants as well as harmless numbering. Flattened comparison still ignores ordering/attributes and packet ID/direction changes; JSON overwrites same-name DOT definitions. Adds tools-only pydot4.0.1/Pydantic2.12.5 plus dependencies; lock literals structurally checked, all non-artifact lines and code diffs read. No parser fixtures/tests or execution demonstrate claimed reliability.

### Evidence limits {#source-acquisition-evidence-11}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 87. Rename output files and separate changed types from changed packets {#87-rename-output-files-and-separate-changed-types-from-changed-packets}
- Commit: [996b6de9b8bc1a058f570b5198347e8111f28f7d](https://github.com/EndstoneMC/endweave/commit/996b6de9b8bc1a058f570b5198347e8111f28f7d)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-27T15:17:15Z; committed: 2026-03-27T15:17:15Z
- Parents: 4f133e86b919a20b460275cccf4f62c7c875666b
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/generate_diff.py, tools/models.py, tools/parse_protocol_docs.py

Separates changed packets (packet_id present) from subtype changes and renames JSON outputs consistently in parser/diff CLI. Data schema changes are consumer-facing; no generated output validation included.

### Evidence limits {#source-acquisition-evidence-12}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 88. Add changelog parsing to protocol diff output {#88-add-changelog-parsing-to-protocol-diff-output}
- Commit: [198ee0c3ec5a9d731717271b2c7f485cef94831b](https://github.com/EndstoneMC/endweave/commit/198ee0c3ec5a9d731717271b2c7f485cef94831b)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-27T15:27:35Z; committed: 2026-03-27T15:27:35Z
- Parents: 996b6de9b8bc1a058f570b5198347e8111f28f7d
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/generate_diff.py, tools/models.py

Adds typed EnumEntry/EnumChange/ChangelogEntry outputs and parses Modified Enums plus raw protocol-step changelogs, subtracting names/categories already present in old docs and filtering raw entries above old protocol. Missing old docs yields all new enum entries; missing new docs yields none. Important heuristic limits: clean_line strips indentation before the not-indented section test, added entries compare only names (ID changes can be missed), Changed discards old/new numeric detail, composite flags become None, first globbed changelog is unsorted, and raw entries have no target upper bound. This enriches handler-generation context but the title claim of sufficient context is not proof of correct mappings. No tests accompany this parser.

### Evidence limits {#source-acquisition-evidence-13}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 89. Detect enum renames in changelog diff (same ID, different name) {#89-detect-enum-renames-in-changelog-diff-same-id-different-name}
- Commit: [1259aa912031a94b3a5ae4fd20a3761e8ffb939e](https://github.com/EndstoneMC/endweave/commit/1259aa912031a94b3a5ae4fd20a3761e8ffb939e)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-27T15:29:56Z; committed: 2026-03-27T15:29:56Z
- Parents: 198ee0c3ec5a9d731717271b2c7f485cef94831b
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/generate_diff.py

Infers enum rename from equal numeric ID across old-only/new-only added lists, reports changed string instead of new addition. Equality of ID is heuristic dependent on registry stability; no test added.

### Evidence limits {#source-acquisition-evidence-14}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 90. Promote add+remove leaf pairs to type_changes in diff {#90-promote-add-remove-leaf-pairs-to-typechanges-in-diff}
- Commit: [9dc1c1573e29494d4cedb7993854811697cbcd11](https://github.com/EndstoneMC/endweave/commit/9dc1c1573e29494d4cedb7993854811697cbcd11)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-27T15:32:30Z; committed: 2026-03-27T15:32:30Z
- Parents: 1259aa912031a94b3a5ae4fd20a3761e8ffb939e
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/generate_diff.py

Promotes singleton add/remove siblings under same parent to type change, compensating DOT leaf names encoding types. Narrow one-to-one condition reduces ambiguity but still assumes a type swap; root promotion can remove pair without recording nonempty-parent type change, a review caveat.

### Evidence limits {#source-acquisition-evidence-15}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 91. Filter descendant fields of type_changes from added/removed {#91-filter-descendant-fields-of-typechanges-from-added-removed}
- Commit: [3589ac5dde062888601f2f0b9ca0da24b623639f](https://github.com/EndstoneMC/endweave/commit/3589ac5dde062888601f2f0b9ca0da24b623639f)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-27T15:34:02Z; committed: 2026-03-27T15:34:02Z
- Parents: 9dc1c1573e29494d4cedb7993854811697cbcd11
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/generate_diff.py

Suppresses descendants of already-changed type paths from add/remove to reduce repeated field noise. Maintains boundary with dot prefix; can conceal details if consumer fails to inspect referenced type.

### Evidence limits {#source-acquisition-evidence-16}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 92. Filter leaf type children from added/removed field lists {#92-filter-leaf-type-children-from-added-removed-field-lists}
- Commit: [1e38cb83739d515d1dbfb9aec8a7c641b63d4bef](https://github.com/EndstoneMC/endweave/commit/1e38cb83739d515d1dbfb9aec8a7c641b63d4bef)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-27T15:36:42Z; committed: 2026-03-27T15:36:42Z
- Parents: 3589ac5dde062888601f2f0b9ca0da24b623639f
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/generate_diff.py

Extracts sorted-path descendant filter using retained ancestor prefixes and explicit type-change prefixes. Parent-first lexical ordering is an assumption documented by function. No tests added; static algorithm read.

### Evidence limits {#source-acquisition-evidence-17}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 93. Deduplicate sub-type changes from parent entries in diff {#93-deduplicate-sub-type-changes-from-parent-entries-in-diff}
- Commit: [a79e8b5759ea731bd3a07a44bc626e885d419c29](https://github.com/EndstoneMC/endweave/commit/a79e8b5759ea731bd3a07a44bc626e885d419c29)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-27T15:39:23Z; committed: 2026-03-27T15:39:23Z
- Parents: 1e38cb83739d515d1dbfb9aec8a7c641b63d4bef
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/generate_diff.py

Suffix-deduplicates subtype field changes from enclosing entries and prunes now-empty packets/types. Suffix matching is not type-identity proof and may collide; pruning packets loses handler-discovery signal, directly corrected94.

### Evidence limits {#source-acquisition-evidence-18}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 94. Keep all changed_packets entries after sub-type dedup {#94-keep-all-changedpackets-entries-after-sub-type-dedup}
- Commit: [82001578c3026058ee41439e6e3ca61fb8958d1f](https://github.com/EndstoneMC/endweave/commit/82001578c3026058ee41439e6e3ca61fb8958d1f)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-27T15:42:18Z; committed: 2026-03-27T15:42:18Z
- Parents: a79e8b5759ea731bd3a07a44bc626e885d419c29
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/generate_diff.py

Retains empty changed packet entries because handler generation starts there, while still pruning empty subtypes. Explicit tradeoff: compactness must not erase impact/reachability. Message explicitly mentions LLM consumers; no generalized agent policy inferred.

### Evidence limits {#source-acquisition-evidence-19}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 95. Replace changed_sub_types with unified type_changes entries {#95-replace-changedsubtypes-with-unified-typechanges-entries}
- Commit: [41a45e916d25173c10ddde6f8b165d67f2d6836e](https://github.com/EndstoneMC/endweave/commit/41a45e916d25173c10ddde6f8b165d67f2d6836e)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-27T15:51:30Z; committed: 2026-03-27T15:51:30Z
- Parents: 82001578c3026058ee41439e6e3ca61fb8958d1f
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/generate_diff.py, tools/models.py

Records removed duplicated subtype changes as same-name old/new TypeChange references, distinguishing internal structural change from replacement. A suffix→single-name dictionary can collapse collisions; consumers must interpret old==new as non-no-op. Comment still names changed_sub_types although implementation unifies type_changes.

### Evidence limits {#source-acquisition-evidence-20}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 96. Add renamed packet detection and embedded type scanning {#96-add-renamed-packet-detection-and-embedded-type-scanning}
- Commit: [a72f99705dd77f6a2f1a9058a2b9dc366d82028e](https://github.com/EndstoneMC/endweave/commit/a72f99705dd77f6a2f1a9058a2b9dc366d82028e)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-27T15:59:59Z; committed: 2026-03-27T15:59:59Z
- Parents: 41a45e916d25173c10ddde6f8b165d67f2d6836e
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/generate_diff.py, tools/models.py

Recursively scans field trees for changed subtype dependencies and promotes impacted packets; detects packet renames from enum changelog strings. Also treats new packets containing changed types as changed rather than new, a heuristic that can conflate genuine new packet with renamed/changed one. Existing changed packet entries are skipped, so dependency completeness is not proven. No tests added.

### Evidence limits {#source-acquisition-evidence-21}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 97. Add manual packet-to-subtype overrides for schema gaps {#97-add-manual-packet-to-subtype-overrides-for-schema-gaps}
- Commit: [5bc2ab2c01200593a088889b3907b4085937b470](https://github.com/EndstoneMC/endweave/commit/5bc2ab2c01200593a088889b3907b4085937b470)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-27T16:18:13Z; committed: 2026-03-27T16:18:13Z
- Parents: a72f99705dd77f6a2f1a9058a2b9dc366d82028e
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/generate_diff.py

Adds explicit schema-gap overrides connecting InventoryTransaction and CameraSpline to known actual subtypes; bridges naming mismatch that recursion misses. Applies only when packet not already changed, retaining incomplete-reference caveat. Overrides are local knowledge requiring maintenance as schema changes.

### Evidence limits {#source-acquisition-evidence-22}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 98. Use protocol numbers for folder names and CLI args {#98-use-protocol-numbers-for-folder-names-and-cli-args}
- Commit: [450237d77a73296b4e0b4ecb5565a9ee9eba32bf](https://github.com/EndstoneMC/endweave/commit/450237d77a73296b4e0b4ecb5565a9ee9eba32bf)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-27T16:26:38Z; committed: 2026-03-27T16:26:38Z
- Parents: 5bc2ab2c01200593a088889b3907b4085937b470
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CLAUDE.md, tools/fetch_protocol_docs.py, tools/generate_diff.py, tools/parse_protocol_docs.py

Moves local docs lookup convention from release tags to v<protocol> and changes fetch/parse CLI validation to known integer protocols; branch derivation still uses registry release tags. Diff changelog lookup follows numeric directories and generated output is documented as data/vN.json. No existing directory migration is implemented in the patch, so old caches need refetch/relocation. Generate-diff argument resolver itself is not changed here despite title saying all three tools. No parser semantic change or tests.

### Evidence limits {#source-acquisition-evidence-23}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 99. Filter mPayload wrapper noise from diff output {#99-filter-mpayload-wrapper-noise-from-diff-output}
- Commit: [d2514fa239d97895b1eb474955a69d952de1e154](https://github.com/EndstoneMC/endweave/commit/d2514fa239d97895b1eb474955a69d952de1e154)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-27T17:23:49Z; committed: 2026-03-27T17:23:49Z
- Parents: 450237d77a73296b4e0b4ecb5565a9ee9eba32bf
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/generate_diff.py

Suppresses mPayload wrapper-only removals unless common non-wrapper field changes type. Reports169→16 changed packets in message, not reproduced. Heuristic does not compare all added semantic fields and can mask genuine additions; normalization with tests would offer stronger evidence.

### Evidence limits {#source-acquisition-evidence-24}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 100. Refactor diff and parse tools for reusability and concise logic: {#100-refactor-diff-and-parse-tools-for-reusability-and-concise-logic}
- Commit: [24631fbd24fbacb9f593f1adecb3783be0f2c7ed](https://github.com/EndstoneMC/endweave/commit/24631fbd24fbacb9f593f1adecb3783be0f2c7ed)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-29T16:05:08Z; committed: 2026-03-29T16:05:20Z
- Parents: 8b37c9dfb28181eb3a6e82e6557ea06cb760e46d
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/diff.py, tools/parse.py

Extracts _diff_definition, _dedup_subtypes, _changes_from_type_refs, _group_by_parent, _promote_leaf_renames, changelog/rename processors and lowest-numeric DOT-root selector from the large tool functions. Compared all removed/additions: intended algorithm preserved, including earliest nonnumeric fallback and no-op enum special-case removal. Existing heuristic hazards persist: one add/remove top-level pair is marked promoted even when empty parent prevents recording a type change; mPayload removal suppression can discard real additions; suffix matching can associate unrelated same-named fields. New-packet subtype references still reclassify genuinely new packets as changed. No regression tests accompany decomposition.

### Evidence limits {#source-acquisition-evidence-25}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.
