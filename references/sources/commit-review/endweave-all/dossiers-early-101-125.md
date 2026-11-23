<!-- retrieval: {"source_ids":["public:commit:06c74119b30f5a5f8bc5ca3186406ae67b35588f","public:commit:093f0c859dbf10cffa8fda9a1498f0d2e7a74b33","public:commit:0c382636886e35339710bfdb2a0e88fe3ec15941","public:commit:168ab9b4ef87905e41c5980e4a1b184903cd8c03","public:commit:3167e0789c605c77a9f4a9a86ce64dad4a296fd0","public:commit:495d9cbd54ec2589cc091800fba5ad8cfbc0f98f","public:commit:6347a12ef1b82d591d86c7d12932700ea362ce38","public:commit:6bbccce2782be6a473ae122ceda7f3366d95a8cd","public:commit:739fa2061a23e71aedcec4ed4eefa3be14036713","public:commit:79fb0f47e45541b72329ff520385b767c5326e85","public:commit:7d586cc74462b5f53fd829489e3874b909e5743b","public:commit:841b45aeba63f0dcfebcf955b12f09239129be03","public:commit:85e9853f2d997975c1e64a2dfb028773a7ecf8b9","public:commit:8839f074a3036467b5a8db7677b4bcc95a6ca8aa","public:commit:8a1e7dae23bdee948939e95b553c0f0fecabb231","public:commit:8b37c9dfb28181eb3a6e82e6557ea06cb760e46d","public:commit:a4e38d2866e4042a4def110a62cd58b70cd3ab70","public:commit:a8a54062073c2a8f400188cb8b18983e7af05cc8","public:commit:b1f648e6b05bc09af12b1f9fd2882a3496732577","public:commit:cbe7cb96e1975deba70a1f1628f9a8b33f732d78","public:commit:d1c1f56f854d15da841b0713d1ea2d0fedaad79d","public:commit:d4f6321ece0f2784a0f6bc97ca9998976e4e8a4e","public:commit:dc950ef4036dcb2f962a3ce54b797c78ea5ea64a","public:commit:f9db901907faef47e7459cfc4db1017985aa57a6","public:commit:fd203552681f7857db49f129712f69d8a0252f6a"],"source_type":"public","date":"2026-03-29..2026-04-04","topics":["lifetime","testing","performance","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endweave-commit-dossiers-assignment-ordinals-101-125"></a>
# Endweave commit dossiers: assignment ordinals 101–125 {#endweave-commit-dossiers-assignment-ordinals-101-125}

Static source review. Assignment ordinals are identifiers, not a topological ordering. Exact parents below define ancestry. Acquired but unread entries remain open. No upstream code, tests or workflows executed. Generated data must receive a separate structural audit before closure.

## 101. Consolidate tools/ scripts with shorter names and single entry point {#101-consolidate-tools-scripts-with-shorter-names-and-single-entry-point}
- Commit: [8b37c9dfb28181eb3a6e82e6557ea06cb760e46d](https://github.com/EndstoneMC/endweave/commit/8b37c9dfb28181eb3a6e82e6557ea06cb760e46d)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-29T15:49:13Z; committed: 2026-03-29T16:05:20Z
- Parents: 6879a198c962f4c121903ea292a4eb104c05b937
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CLAUDE.md, tools/diff.py, tools/fetch.py, tools/fetch_protocol_docs.py, tools/generate_diff.py, tools/models.py, tools/parse.py, tools/parse_protocol_docs.py

Consolidates tooling into fetch.py/parse.py/diff.py and automatically fetches/parses prerequisites from diff CLI. Full new implementations read; complete deleted versions compared against new in the static comparison, with every residual change read, avoiding duplicate unchanged prose. Adds callable fetch_if_missing, parse_version, ensure_parsed; cache validity is existence-only, so partial docs or stale generated schemas can suppress rebuild. Main parse CLI now list rather than dict, so repeated numeric args may repeat work. Retains regex changelog heuristics, type-reference propagation, mPayload suppression and suffix deduplication limitations. Fetch retries any clone error as uppercase branch variant, potentially masking a different failure. No upstream tooling executed. DAG order: this commit is parent of ordinal100 despite assignment numbering.

### Evidence limits {#source-acquisition-evidence}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 102. Refactor tools to improve field handling and protocol diffing: {#102-refactor-tools-to-improve-field-handling-and-protocol-diffing}
- Commit: [a4e38d2866e4042a4def110a62cd58b70cd3ab70](https://github.com/EndstoneMC/endweave/commit/a4e38d2866e4042a4def110a62cd58b70cd3ab70)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-29T17:15:15Z; committed: 2026-03-29T17:15:15Z
- Parents: 24631fbd24fbacb9f593f1adecb3783be0f2c7ed
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/diff.py, tools/models.py, tools/parse.py

Changes tooling output schema from children/attributes to fields/list/type with internal attributes excluded; _to_output folds first list-element child into parent. Adds typed FieldChange records for add/remove paths and inline added/removed subtype details to same-name TypeChange, with fallback direction inference. This is a data-format migration, not merely cleanup. Existing existence-only ensure_parsed can reuse old children-format caches; model validation/defaults can then lose nested information without automatic regeneration. Diff flattening still records only type, ignoring list flags and serialization ordering; folding assumes one correctly marked element and drops other list children. Descendant type changes are removed under parent changes; inline details omit nested type-change details. No new tests or runtime evidence.

### Evidence limits {#source-acquisition-evidence-2}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 103. Remove trailing passthroughs from handlers, rely on auto-copy {#103-remove-trailing-passthroughs-from-handlers-rely-on-auto-copy}
- Commit: [6347a12ef1b82d591d86c7d12932700ea362ce38](https://github.com/EndstoneMC/endweave/commit/6347a12ef1b82d591d86c7d12932700ea362ce38)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-29T17:48:41Z; committed: 2026-03-29T17:48:41Z
- Parents: a4e38d2866e4042a4def110a62cd58b70cd3ab70
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/v860_to_v898/handlers/commands.py, src/endstone_endweave/protocol/v860_to_v898/handlers/gameplay.py, src/endstone_endweave/protocol/v898_to_v860/handlers/commands.py, src/endstone_endweave/protocol/v898_to_v860/handlers/gameplay.py, src/endstone_endweave/protocol/v898_to_v924/handlers/book_edit.py, src/endstone_endweave/protocol/v898_to_v924/handlers/camera.py, src/endstone_endweave/protocol/v898_to_v924/handlers/gameplay.py, src/endstone_endweave/protocol/v924_to_v898/handlers/biome_definition_list.py, src/endstone_endweave/protocol/v924_to_v898/handlers/book_edit.py, src/endstone_endweave/protocol/v924_to_v898/handlers/camera.py, src/endstone_endweave/protocol/v924_to_v898/handlers/gameplay.py, src/endstone_endweave/protocol/v924_to_v898/handlers/text.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/camera.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v944_to_v924/handlers/block_pos.py, src/endstone_endweave/protocol/v944_to_v924/handlers/camera.py, src/endstone_endweave/protocol/v944_to_v924/handlers/start_game.py, tests/test_v924_to_v944.py

Stops handlers at their last changed field and relies on PacketWrapper.to_bytes to append unread tail across18 handler files: book text, camera suffixes, telemetry, biome string table, actor event data, command data and resource-pack tail no longer decode/re-encode. Valid canonical payloads should preserve those bytes while reducing work, but malformed tail validation and normalization are also removed. Changes are scoped to trailing identical sections; needed insertion/removal flags remain. Tests shift from full consumption toward output assertions, yet all-variants StartGame now checks only nonempty output and camera all-present checks only larger length, weak evidence of valid framing. No measured performance or runtime compatibility result.

### Evidence limits {#source-acquisition-evidence-3}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 104. Refactor protocol handlers: BDS enums, per-packet files, field comments {#104-refactor-protocol-handlers-bds-enums-per-packet-files-field-comments}
- Commit: [dc950ef4036dcb2f962a3ce54b797c78ea5ea64a](https://github.com/EndstoneMC/endweave/commit/dc950ef4036dcb2f962a3ce54b797c78ea5ea64a)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-29T21:37:36Z; committed: 2026-03-29T21:37:36Z
- Parents: 6347a12ef1b82d591d86c7d12932700ea362ce38
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/enums.py, src/endstone_endweave/codec/types/inventory.py, src/endstone_endweave/protocol/base.py, src/endstone_endweave/protocol/sound_rewriter.py, src/endstone_endweave/protocol/v860_to_v898/handlers/actor_event.py, src/endstone_endweave/protocol/v860_to_v898/handlers/animate.py, src/endstone_endweave/protocol/v860_to_v898/handlers/camera_aim_assist.py, src/endstone_endweave/protocol/v860_to_v898/handlers/commands.py, src/endstone_endweave/protocol/v860_to_v898/handlers/event.py, src/endstone_endweave/protocol/v860_to_v898/handlers/gameplay.py, src/endstone_endweave/protocol/v860_to_v898/handlers/interact.py, src/endstone_endweave/protocol/v860_to_v898/handlers/mob_effect.py, src/endstone_endweave/protocol/v860_to_v898/handlers/resource_pack_stack.py, src/endstone_endweave/protocol/v860_to_v898/handlers/start_game.py, src/endstone_endweave/protocol/v860_to_v898/handlers/text.py, src/endstone_endweave/protocol/v860_to_v898/protocol.py, src/endstone_endweave/protocol/v898_to_v860/handlers/actor_event.py, src/endstone_endweave/protocol/v898_to_v860/handlers/camera_aim_assist.py, src/endstone_endweave/protocol/v898_to_v860/handlers/commands.py, src/endstone_endweave/protocol/v898_to_v860/handlers/event.py, src/endstone_endweave/protocol/v898_to_v860/handlers/gameplay.py, src/endstone_endweave/protocol/v898_to_v860/handlers/interact.py, src/endstone_endweave/protocol/v898_to_v860/handlers/mob_effect.py, src/endstone_endweave/protocol/v898_to_v860/handlers/resource_pack_stack.py, src/endstone_endweave/protocol/v898_to_v860/handlers/start_game.py, src/endstone_endweave/protocol/v898_to_v860/handlers/text.py, src/endstone_endweave/protocol/v898_to_v860/protocol.py, src/endstone_endweave/protocol/v898_to_v924/handlers/camera_aim_assist.py, src/endstone_endweave/protocol/v898_to_v924/handlers/data_store.py, src/endstone_endweave/protocol/v898_to_v924/handlers/gameplay.py, src/endstone_endweave/protocol/v898_to_v924/handlers/graphics_parameter_override.py, src/endstone_endweave/protocol/v898_to_v924/handlers/start_game.py, src/endstone_endweave/protocol/v898_to_v924/protocol.py, src/endstone_endweave/protocol/v924_to_v898/handlers/biome_definition_list.py, src/endstone_endweave/protocol/v924_to_v898/handlers/camera_aim_assist.py, src/endstone_endweave/protocol/v924_to_v898/handlers/data_store.py, src/endstone_endweave/protocol/v924_to_v898/handlers/gameplay.py, src/endstone_endweave/protocol/v924_to_v898/handlers/graphics_parameter_override.py, src/endstone_endweave/protocol/v924_to_v898/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v898/protocol.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, src/endstone_endweave/protocol/v944_to_v924/handlers/block_pos.py, src/endstone_endweave/protocol/v944_to_v924/protocol.py

Adds named BDS-oriented enums and splits gameplay/command handlers into per-packet files, with all removed and added bodies read. Most inventory/source/sound/map checks simply replace numeric literals. Substantive exceptions: CommandRequest default version48 becomes45; Animate860-to898 now passes entire payload unchanged and appends absent SwingSource, deleting VAR_INT-to-BYTE conversion and rowing handling, while reverse assumes BYTE then runtime ID/FLOAT and optional string. This is an assumption change concealed by the refactor title; ordinal111 later restores action-width conversion and handles rowing float removal. The claim of BDS fidelity is not independent wire validation. Event still injects/removes UsePlayerID until118. Aim-assist dropped-count/preserved-entry issue and partial StartGame gather-flag handling remain inherited. New enums cover command origin/output/version, map flags, inventory and interaction categories; declared values were read but not independently validated against a running BDS. No tests or measurements accompany the reorganization.

### Evidence limits {#source-acquisition-evidence-4}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 105. Enforce BDS headers as sole protocol reference {#105-enforce-bds-headers-as-sole-protocol-reference}
- Commit: [7d586cc74462b5f53fd829489e3874b909e5743b](https://github.com/EndstoneMC/endweave/commit/7d586cc74462b5f53fd829489e3874b909e5743b)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-29T22:24:07Z; committed: 2026-03-29T22:24:07Z
- Parents: dc950ef4036dcb2f962a3ce54b797c78ea5ea64a
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CLAUDE.md

Historical contributor guidance prioritizes BDS headers, IntEnum names and version-specific string-label codecs over third-party implementation assumptions. Message alleges specific Cloudburst inaccuracies; treat as author's stated rationale, not independent blanket assessment. No code change or external source verification here.

### Evidence limits {#source-acquisition-evidence-5}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 106. Extract command types, add BDS enums, detect optional fields in parser {#106-extract-command-types-add-bds-enums-detect-optional-fields-in-parser}
- Commit: [495d9cbd54ec2589cc091800fba5ad8cfbc0f98f](https://github.com/EndstoneMC/endweave/commit/495d9cbd54ec2589cc091800fba5ad8cfbc0f98f)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-29T22:33:31Z; committed: 2026-03-29T22:33:31Z
- Parents: 7d586cc74462b5f53fd829489e3874b909e5743b
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/commands.py, src/endstone_endweave/codec/types/enums.py, src/endstone_endweave/protocol/v860_to_v898/handlers/animate.py, src/endstone_endweave/protocol/v860_to_v898/handlers/commands.py, src/endstone_endweave/protocol/v860_to_v898/handlers/text.py, src/endstone_endweave/protocol/v898_to_v860/handlers/commands.py, src/endstone_endweave/protocol/v898_to_v924/handlers/book_edit.py, src/endstone_endweave/protocol/v898_to_v924/handlers/graphics_parameter_override.py, src/endstone_endweave/protocol/v924_to_v898/handlers/book_edit.py, src/endstone_endweave/protocol/v924_to_v898/handlers/graphics_parameter_override.py, src/endstone_endweave/protocol/v924_to_v898/handlers/text.py, tools/models.py, tools/parse.py

Extracts command dataclasses and versioned codecs:860 enum index width depends on total values (<=256 BYTE, <=65536 USHORT, otherwise INT);898 uses INT, subcommand pair widths and command permission labels differ. ArrayType/map replaces handwritten loops, preserving most layout. Meaningful change: command outputs and old-to-new requests now retain origin type/player ID rather than coercing every origin to player; newer-to-old request still explicitly coerces player. Unknown898 origin labels default0, unlike permission/output mappings that raise. Programmatic enum labels remove underscores and lowercase all letters: text labels formerly systemMessage/textObjectWhisper/jukeboxPopup become systemmessage/textobjectwhisper/jukeboxpopup, a concrete wire-string change requiring evidence, not a mechanically equivalent refactor. OptionalType replacements retain absent versus present-string logic (empty filtered text maps absent). Parser adds optional metadata through JSON required arrays but treats absent or empty required as None, so those cases leave all fields nonoptional contrary to general JSON Schema semantics. Existing diff flattening still ignores optional metadata and existence-only caches are not invalidated. Message claims reparsed versions, but captured diff contains no generated data files. All full changed/deleted command helpers read; no new tests or upstream execution.

### Evidence limits {#source-acquisition-evidence-6}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 107. Fix handler bugs found by cross-referencing data/*.json {#107-fix-handler-bugs-found-by-cross-referencing-data-json}
- Commit: [a8a54062073c2a8f400188cb8b18983e7af05cc8](https://github.com/EndstoneMC/endweave/commit/a8a54062073c2a8f400188cb8b18983e7af05cc8)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-29T23:18:47Z; committed: 2026-03-29T23:18:47Z
- Parents: 495d9cbd54ec2589cc091800fba5ad8cfbc0f98f
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/v860_to_v898/handlers/interact.py, src/endstone_endweave/protocol/v898_to_v860/handlers/camera_aim_assist.py, src/endstone_endweave/protocol/v898_to_v860/handlers/interact.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, src/endstone_endweave/protocol/v944_to_v924/handlers/block_pos.py, src/endstone_endweave/protocol/v944_to_v924/handlers/voxel_shapes.py, src/endstone_endweave/protocol/v944_to_v924/protocol.py

Cross-schema audit repairs four field-level bugs: trailing rather than leading VoxelShapes count, two-byte prefix before lectern position, StopRiding position discriminant, and read/discard rather than passthrough for unsupported camera block-tag priorities. Both direction variants updated where present. VoxelShapes data[:-2] lacks explicit short-payload guard and assumes custom-shape representation can be removed as two bytes; no new tests.

### Evidence limits {#source-acquisition-evidence-7}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 108. Fix LecternUpdate serverbound and log version range {#108-fix-lecternupdate-serverbound-and-log-version-range}
- Commit: [8839f074a3036467b5a8db7677b4bcc95a6ca8aa](https://github.com/EndstoneMC/endweave/commit/8839f074a3036467b5a8db7677b4bcc95a6ca8aa)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-29T23:29:07Z; committed: 2026-03-29T23:29:07Z
- Parents: a8a54062073c2a8f400188cb8b18983e7af05cc8
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, src/endstone_endweave/protocol/v944_to_v924/handlers/block_pos.py, src/endstone_endweave/protocol/v944_to_v924/protocol.py

Adds reverse serverbound LecternUpdate after clientbound-only fix, with correct two BYTE prefix in both version-pair modules; startup supported list becomes endpoints range. Range may conceal holes absent a separately verified contiguous support invariant. No tests added.

### Evidence limits {#source-acquisition-evidence-8}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 109. Update CHANGELOG for unreleased fixes {#109-update-changelog-for-unreleased-fixes}
- Commit: [f9db901907faef47e7459cfc4db1017985aa57a6](https://github.com/EndstoneMC/endweave/commit/f9db901907faef47e7459cfc4db1017985aa57a6)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-29T23:30:12Z; committed: 2026-03-29T23:30:12Z
- Parents: 8839f074a3036467b5a8db7677b4bcc95a6ca8aa
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md

Changelog records recent packet corrections but drops sign fix entry, which112 restores. Small documentation evolution; release notes are lossy summaries rather than exhaustive proof.

### Evidence limits {#source-acquisition-evidence-9}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 110. Fix v860 StartGame: use GAME_RULES passthrough and zero block checksum {#110-fix-v860-startgame-use-gamerules-passthrough-and-zero-block-checksum}
- Commit: [841b45aeba63f0dcfebcf955b12f09239129be03](https://github.com/EndstoneMC/endweave/commit/841b45aeba63f0dcfebcf955b12f09239129be03)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-29T23:55:49Z; committed: 2026-03-29T23:55:49Z
- Parents: f9db901907faef47e7459cfc4db1017985aa57a6
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/v860_to_v898/handlers/start_game.py, src/endstone_endweave/protocol/v898_to_v860/handlers/start_game.py

Uses shared GAME_RULES codec instead of duplicated inline loop, correcting unsigned integer wire parsing in860→898; reverse loop was already signed. Zeroes checksum in898→860;860→898 already zeroed and only gains comments. Message overstates symmetry of missing checksum fix. No tests added; validation bypass does not prove block palette compatibility.

### Evidence limits {#source-acquisition-evidence-10}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 111. Fix AnimatePacket v860 wire format and alias cross-imports {#111-fix-animatepacket-v860-wire-format-and-alias-cross-imports}
- Commit: [fd203552681f7857db49f129712f69d8a0252f6a](https://github.com/EndstoneMC/endweave/commit/fd203552681f7857db49f129712f69d8a0252f6a)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-30T00:20:44Z; committed: 2026-03-30T00:20:44Z
- Parents: 841b45aeba63f0dcfebcf955b12f09239129be03
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, src/endstone_endweave/protocol/v860_to_v898/handlers/animate.py, src/endstone_endweave/protocol/v898_to_v860/protocol.py

Animate conversion now reads860 action zigzag varint and emits898 byte, preserving actor ID/data, removing conditional rowing time and appending absent swing-source option. Reverse converts byte→varint and discards option, but does not synthesize rowing float if0x80 set, so symmetry is conditional. Aliases handlers by explicit version direction to avoid clientbound/serverbound naming ambiguity when reused across reverse protocol. No tests in patch.

### Evidence limits {#source-acquisition-evidence-11}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 112. Rewrite CHANGELOG entries in plain language {#112-rewrite-changelog-entries-in-plain-language}
- Commit: [b1f648e6b05bc09af12b1f9fd2882a3496732577](https://github.com/EndstoneMC/endweave/commit/b1f648e6b05bc09af12b1f9fd2882a3496732577)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-30T00:21:19Z; committed: 2026-03-30T00:21:19Z
- Parents: fd203552681f7857db49f129712f69d8a0252f6a
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md

Rewrites changelog from protocol/internal terms to user symptoms and restores sign-edit fix. Documentation-only; technical detail belongs in source dossiers rather than discarded from knowledge.

### Evidence limits {#source-acquisition-evidence-12}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 113. Improve codec efficiency {#113-improve-codec-efficiency}
- Commit: [6bbccce2782be6a473ae122ceda7f3366d95a8cd](https://github.com/EndstoneMC/endweave/commit/6bbccce2782be6a473ae122ceda7f3366d95a8cd)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-30T00:37:55Z; committed: 2026-03-30T00:37:55Z
- Parents: b1f648e6b05bc09af12b1f9fd2882a3496732577
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/reader.py, src/endstone_endweave/codec/writer.py, src/endstone_endweave/connection.py, src/endstone_endweave/pipeline.py, src/endstone_endweave/protocol/__init__.py

Optimizes interpreted hot path by precompiled struct.Struct objects, one-byte LEB128 read/write fast paths, handler-or-cancel membership check before wrapper allocation, and cached base+reversed-chain clientbound order. Existing mask normalization retained before writer fast path; lengths/overflow behavior outside changed lines not independently benchmarked. No tests or timings added, so infer reduced operations rather than measured speedup. Demonstrates later architecture already uses fresh wrapper per protocol step, unlike42; trace intervening72 before generalizing.

### Evidence limits {#source-acquisition-evidence-13}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 114. Revise README.md for improved clarity {#114-revise-readme-md-for-improved-clarity}
- Commit: [168ab9b4ef87905e41c5980e4a1b184903cd8c03](https://github.com/EndstoneMC/endweave/commit/168ab9b4ef87905e41c5980e4a1b184903cd8c03)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-30T00:42:38Z; committed: 2026-03-30T00:42:38Z
- Parents: 6bbccce2782be6a473ae122ceda7f3366d95a8cd
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: README.md

README broadens positioning to both client/server version directions, maintaining ViaVersion attribution. Assertions of zero processing and chaining remain unmeasured docs claims.

### Evidence limits {#source-acquisition-evidence-14}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 115. Fix v944_to_v924 missing serverbound BlockActorData handler {#115-fix-v944tov924-missing-serverbound-blockactordata-handler}
- Commit: [79fb0f47e45541b72329ff520385b767c5326e85](https://github.com/EndstoneMC/endweave/commit/79fb0f47e45541b72329ff520385b767c5326e85)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-30T14:00:52Z; committed: 2026-03-30T14:00:52Z
- Parents: 22bcb5767d22c1c427695dc875f2669b1e10930c
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, src/endstone_endweave/protocol/v944_to_v924/handlers/block_pos.py, src/endstone_endweave/protocol/v944_to_v924/protocol.py

Completes missing serverbound BlockActorData conversion in reverse version pair, addressing older clients editing newer servers' command blocks. Complements84; tests not added, so both directions require integration coverage.

### Evidence limits {#source-acquisition-evidence-15}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 116. Handle DebugDrawer and ServerboundDiagnostics across v898/v924 {#116-handle-debugdrawer-and-serverbounddiagnostics-across-v898-v924}
- Commit: [093f0c859dbf10cffa8fda9a1498f0d2e7a74b33](https://github.com/EndstoneMC/endweave/commit/093f0c859dbf10cffa8fda9a1498f0d2e7a74b33)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-30T14:54:30Z; committed: 2026-03-30T14:54:30Z
- Parents: 79fb0f47e45541b72329ff520385b767c5326e85
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, src/endstone_endweave/protocol/v898_to_v924/handlers/debug_drawer.py, src/endstone_endweave/protocol/v898_to_v924/handlers/diagnostics.py, src/endstone_endweave/protocol/v898_to_v924/protocol.py, src/endstone_endweave/protocol/v924_to_v898/handlers/debug_drawer.py, src/endstone_endweave/protocol/v924_to_v898/handlers/diagnostics.py, src/endstone_endweave/protocol/v924_to_v898/protocol.py

Replaces DebugDrawer cancellation with bidirectional per-shape transformation: optional attached entity is stripped or synthesized absent between common fields and discriminated Arrow/Text/Box/Line/Sphere payload. Unknown variant indices have no explicit rejection, so payload can desynchronize subsequent shapes. Shared helper doc incorrectly says it handles extra-shape field although caller does. Diagnostics downgrade retains exactly nine floats then discards all tail, upgrade appends zero list count after nine floats. Tail discard intentionally loses newer metrics and skips their structural validation. Both protocol directions registered; no regression tests added.

### Evidence limits {#source-acquisition-evidence-16}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 117. Improve codec efficiency {#117-improve-codec-efficiency}
- Commit: [d4f6321ece0f2784a0f6bc97ca9998976e4e8a4e](https://github.com/EndstoneMC/endweave/commit/d4f6321ece0f2784a0f6bc97ca9998976e4e8a4e)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-30T15:01:06Z; committed: 2026-03-30T15:01:06Z
- Parents: 093f0c859dbf10cffa8fda9a1498f0d2e7a74b33
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/v898_to_v860/handlers/event.py

Title/message repeat broad optimization description, but actual patch solely removes invalid assertion that event-data discriminant duplicates event type, still stripping UsePlayerID. No codec optimization in this SHA.118 then corrects that remaining shared-field mistake.

### Evidence limits {#source-acquisition-evidence-17}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 118. Fix LegacyTelemetryEvent: Use Player ID exists in both v860 and v898 {#118-fix-legacytelemetryevent-use-player-id-exists-in-both-v860-and-v898}
- Commit: [06c74119b30f5a5f8bc5ca3186406ae67b35588f](https://github.com/EndstoneMC/endweave/commit/06c74119b30f5a5f8bc5ca3186406ae67b35588f)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-30T15:04:35Z; committed: 2026-03-30T15:04:35Z
- Parents: d4f6321ece0f2784a0f6bc97ca9998976e4e8a4e
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/v860_to_v898/handlers/event.py, src/endstone_endweave/protocol/v898_to_v860/handlers/event.py

Preserves UsePlayerID BOOL in both directions because both versions carry it; only EventData is inserted/removed. Explicit reported symptom is /list disconnecting860 clients. Upgrade still writes event_type as EventData; no new execution or test evidence proves all payload variants.

### Evidence limits {#source-acquisition-evidence-18}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 119. Add /list disconnect fix to CHANGELOG {#119-add-list-disconnect-fix-to-changelog}
- Commit: [8a1e7dae23bdee948939e95b553c0f0fecabb231](https://github.com/EndstoneMC/endweave/commit/8a1e7dae23bdee948939e95b553c0f0fecabb231)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-30T15:06:06Z; committed: 2026-03-30T15:06:06Z
- Parents: 06c74119b30f5a5f8bc5ca3186406ae67b35588f
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md

Adds plain-language command-disconnect changelog item for118. No independent implementation content.

### Evidence limits {#source-acquisition-evidence-19}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 120. Use server.protocol_version for direct protocol detection {#120-use-server-protocolversion-for-direct-protocol-detection}
- Commit: [0c382636886e35339710bfdb2a0e88fe3ec15941](https://github.com/EndstoneMC/endweave/commit/0c382636886e35339710bfdb2a0e88fe3ec15941)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-30T21:15:45Z; committed: 2026-03-30T21:15:45Z
- Parents: 76ae098030d44b7301685f32a2904c83b84f24a9
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, src/endstone_endweave/metrics.py, src/endstone_endweave/plugin.py, tests/test_pipeline.py

Server protocol_version becomes the authoritative integer, replacing Minecraft-version normalization, lookup and fallback-to-minimum logic that mishandled unknown hotfix versions. Deletes normalization tests without adding a new protocol-detection regression test. Moves platform metrics handling to its own module; extraction is organizational rather than evidence that metrics serialization changed.

### Evidence limits {#source-acquisition-evidence-20}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 121. Add LevelSoundEvent and ActorDataIDs enums, fix sound remapping bugs {#121-add-levelsoundevent-and-actordataids-enums-fix-sound-remapping-bugs}
- Commit: [cbe7cb96e1975deba70a1f1628f9a8b33f732d78](https://github.com/EndstoneMC/endweave/commit/cbe7cb96e1975deba70a1f1628f9a8b33f732d78)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-31T13:42:19Z; committed: 2026-03-31T13:42:19Z
- Parents: 2b987023756527a056c1af14db77b4475124a1bb
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/biome.py, src/endstone_endweave/codec/types/camera.py, src/endstone_endweave/codec/types/commands.py, src/endstone_endweave/codec/types/enums.py, src/endstone_endweave/codec/types/inventory.py, src/endstone_endweave/pipeline.py, src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/v860_to_v898/handlers/text.py, src/endstone_endweave/protocol/v860_to_v898/protocol.py, src/endstone_endweave/protocol/v898_to_v860/protocol.py, src/endstone_endweave/protocol/v898_to_v924/handlers/biome_definition_list.py, src/endstone_endweave/protocol/v898_to_v924/protocol.py, src/endstone_endweave/protocol/v924_to_v898/handlers/text.py, src/endstone_endweave/protocol/v924_to_v898/protocol.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, src/endstone_endweave/protocol/v944_to_v924/handlers/start_game.py, src/endstone_endweave/protocol/v944_to_v924/protocol.py, tests/helpers.py, tests/test_sound_rewriter.py, tools/diff.py, tools/fetch.py, tools/parse.py

Adds explicit ActorDataIDs and broad LevelSoundEvent enum with historical Undefined aliases566/578/597/599. Corrects older-pair heartbeat key127 (last death position) to126; fixes898-to860 inserted sounds collapsing to566 rather than out-of-range578; adds missing898-to924 sound/ActorData registration and shift19 so old Undefined does not play SaddleInWater. All six mapping directions gain boundary/range tests, including intentionally extrapolated above-Undefined IDs; tests do not prove real-client validity of those extrapolations. Source enum includes intentional historical alias collisions and gaps, so cannot assume contiguous IDs or unique names. Full literal diff read as source declarations, not independently cross-validated against every upstream BDS enum. Other broad formatting hunks preserve parser and pipeline behavior.

### Evidence limits {#source-acquisition-evidence-21}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 122. Add LevelSettings type to replace StartGame boilerplate {#122-add-levelsettings-type-to-replace-startgame-boilerplate}
- Commit: [3167e0789c605c77a9f4a9a86ce64dad4a296fd0](https://github.com/EndstoneMC/endweave/commit/3167e0789c605c77a9f4a9a86ce64dad4a296fd0)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-31T21:40:07Z; committed: 2026-03-31T21:40:07Z
- Parents: cbe7cb96e1975deba70a1f1628f9a8b33f732d78
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/level_settings.py, src/endstone_endweave/protocol/v860_to_v898/handlers/start_game.py, src/endstone_endweave/protocol/v898_to_v860/handlers/start_game.py, src/endstone_endweave/protocol/v898_to_v924/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v898/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v944_to_v924/handlers/start_game.py

Extracts the full ordered LevelSettings wire structure into a typed dataclass and shared reader/writer, replacing six duplicated StartGame traversals with version-selected codecs. V860 uses unsigned-varint spawn Y and signed fixed-width experiment count; V924 changes count to unsigned; V944 changes spawn Y to signed varint. The surrounding telemetry locations and world/scenario ordering remain direction-specific. Override-force-experimental becomes OptionalType(BOOL), preserving both presence and value rather than a single flag; its Any annotation is tightened next. The cross-924/944 path still directly maps the unsigned numeric Y value to signed varint and vice versa; unlike NetworkBlockPos fixed at70, it does not reinterpret the 32-bit sign bit. This is inherited from the removed StartGame handler rather than a newly introduced regression, and negative-height behavior remains a static concern. Consolidation makes schema differences explicit but no new tests accompany the extensive replacement; no runtime validation.

### Evidence limits {#source-acquisition-evidence-22}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 123. Code quality improvements from audit {#123-code-quality-improvements-from-audit}
- Commit: [d1c1f56f854d15da841b0713d1ea2d0fedaad79d](https://github.com/EndstoneMC/endweave/commit/d1c1f56f854d15da841b0713d1ea2d0fedaad79d)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-31T22:19:04Z; committed: 2026-03-31T22:19:04Z
- Parents: 3167e0789c605c77a9f4a9a86ce64dad4a296fd0
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: pyproject.toml, src/endstone_endweave/codec/types/enums.py, src/endstone_endweave/codec/types/gameplay.py, src/endstone_endweave/codec/types/level_settings.py, src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/v860_to_v898/protocol.py, src/endstone_endweave/protocol/v898_to_v860/handlers/text.py, src/endstone_endweave/protocol/v898_to_v860/protocol.py, src/endstone_endweave/protocol/v898_to_v924/protocol.py, src/endstone_endweave/protocol/v924_to_v898/protocol.py, src/endstone_endweave/protocol/v944_to_v924/protocol.py, tests/conftest.py

Audit refactor removes generic enum aliases, dispatches GameRules codecs through type-ID lookup1 BOOL/2 VAR_INT/3 FLOAT with explicit unknown-type ValueError on read and write, and parameterizes Experiments count codec INT_LE versus UINT_LE. LevelSettings shares constants and narrows Any to bool-or-None; plugin factory loop preserves order. Adds shared reader/writer fixtures, test path configuration and Ruff W rules. Comments/documentation cleanup is not wire-compatibility proof; no upstream tests executed.

### Evidence limits {#source-acquisition-evidence-23}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 124. Add MappingData model and declarative mapping files per version pair {#124-add-mappingdata-model-and-declarative-mapping-files-per-version-pair}
- Commit: [85e9853f2d997975c1e64a2dfb028773a7ecf8b9](https://github.com/EndstoneMC/endweave/commit/85e9853f2d997975c1e64a2dfb028773a7ecf8b9)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-04-04T14:06:59Z; committed: 2026-04-04T14:07:13Z
- Parents: c030450bcaed25d8b1c436d2c500d31005c7d476
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CLAUDE.md, src/endstone_endweave/protocol/mapping_data.py, src/endstone_endweave/protocol/mappings/__init__.py, src/endstone_endweave/protocol/mappings/v860_v898.py, src/endstone_endweave/protocol/mappings/v898_v924.py, src/endstone_endweave/protocol/mappings/v924_v944.py, src/endstone_endweave/protocol/v860_to_v898/protocol.py, src/endstone_endweave/protocol/v898_to_v860/protocol.py, src/endstone_endweave/protocol/v898_to_v924/handlers/start_game.py, src/endstone_endweave/protocol/v898_to_v924/protocol.py, src/endstone_endweave/protocol/v924_to_v898/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v898/protocol.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, src/endstone_endweave/protocol/v944_to_v924/handlers/start_game.py, src/endstone_endweave/protocol/v944_to_v924/protocol.py, tests/test_sound_rewriter.py

Adds frozen IdShift insertion/count abstraction with shift_up, shift_down (inserted interval collapses to insertion ID), and cap (all IDs at/above threshold collapse). MappingData centralizes optional sound/actor/note shifts and dropped-ID frozensets. Paired modules share mappings across six directions, preserving the special924-to898 cap behavior instead of replacing it with shift_down. Actor/note metadata is not yet fully integrated into rewriting. Also zeroes StartGame checksum in898-to924,924-to898 and944-to924 where missing. Tests import shared mapping methods but add no cases. Expanded contributor guide teaches bidirectional registration and typed/compound operations; its broad always-handler rule needs contextual exceptions.

### Evidence limits {#source-acquisition-evidence-24}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 125. Update CHANGELOG with block registry checksum fix {#125-update-changelog-with-block-registry-checksum-fix}
- Commit: [739fa2061a23e71aedcec4ed4eefa3be14036713](https://github.com/EndstoneMC/endweave/commit/739fa2061a23e71aedcec4ed4eefa3be14036713)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-04-04T15:19:25Z; committed: 2026-04-04T15:19:25Z
- Parents: 85e9853f2d997975c1e64a2dfb028773a7ecf8b9
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md

Records missing checksum zeroing across some version pairs; doc-only claim linked to prior implementations, no independent validation.

### Evidence limits {#source-acquisition-evidence-25}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.
