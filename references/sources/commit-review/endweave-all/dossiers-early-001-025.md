<!-- retrieval: {"source_ids":["public:commit:00ef13c3acadce65b7ee70139e87942d00a021af","public:commit:03eec39346f1047e338bfaa4e9c72a3dd87600ac","public:commit:1501feeb4d34d1b5ab5c5a36fe7389facf0efc70","public:commit:206fa03acec626b815c707a92181e802f691b613","public:commit:2aff6e5ba7e1aa453741540e863412bb89fc17fc","public:commit:2fe8c33bba57c680dfc0c990a93b7edb71583a5c","public:commit:3162246091d0dfad84076f91630860fedd43db0b","public:commit:3e3bedff61365427a4d408de9fa24db1128511bd","public:commit:4398bbc5264a470b210585032f6da582d6dd2d3c","public:commit:65aa4f91faeae447c4646864cf2ba71524ae9cc4","public:commit:80064fb7439ae80faad5694da111e8191f5f2a71","public:commit:89f8f39ea11dc4b62e37f5237ac9aa69aacd5e87","public:commit:8b9e45175231f3f659fc3b40062f38ed3566893a","public:commit:9ebbbd75d62476f45c7129c89d126e7211250355","public:commit:b397ef252176d68f27ca3e7b10a0dcae89d29e37","public:commit:b92348aa5c2345a21c6d431c41b8c8c55f6ade7e","public:commit:bc8df50830acd4511e63692a7cab12b9fabe2ada","public:commit:c423aefbac6862b530e4f5128f41358c7fe861ab","public:commit:cd8966b747d0ef5b9e824c4457e88af8ca3cc0b6","public:commit:d688a68e18cb30f56938b3d92bd382bda6fcfa1d","public:commit:da4a166f971128aeb40e5cd9b283a467c0f7fe0d","public:commit:dd565e489ac7c604305f56aa5fcb38fb4a0a7f22","public:commit:ebf9f5f0ce091c5d6078772b2b165b13db764c19","public:commit:f566c680f827bc2a4cc8f80bd4d61a48e4f4dc7a","public:commit:f9810def2a166a4c6404d665391e91b29d13e37f"],"source_type":"public","date":"2026-03-17..2026-03-19","topics":["lifetime","concurrency","testing","build","performance","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endweave-commit-dossiers-assignment-ordinals-1-25"></a>
# Endweave commit dossiers: assignment ordinals 1–25 {#endweave-commit-dossiers-assignment-ordinals-1-25}

Static source review. Assignment ordinals are identifiers, not a topological ordering. Exact parents below define ancestry. Acquired but unread entries remain open. No upstream code, tests or workflows executed. Generated data must receive a separate structural audit before closure.

## 1. Initial commit {#1-initial-commit}
- Commit: [f9810def2a166a4c6404d665391e91b29d13e37f](https://github.com/EndstoneMC/endweave/commit/f9810def2a166a4c6404d665391e91b29d13e37f)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-17T13:40:56Z; committed: 2026-03-17T13:40:56Z
- Parents: root
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: .github/workflows/build.yml, .github/workflows/publish.yml, .gitignore, LICENSE, README.md, pyproject.toml, src/endstone_example/__init__.py, src/endstone_example/example_listener.py, src/endstone_example/example_plugin.py, src/endstone_example/python_command.py

Template bootstrap imports an Endstone example plugin, not the finished translator: lifecycle/event listeners, scheduler popup, permissions and command executor illustrate framework wiring. Build CI installs only despite its tests comment; publish remains gated to the template repository. Python 3.9 matrix conflicts with match syntax in example_plugin. Root MIT notice credits Endstone. No tests run and no target-exclusive authorship inferred from imported template.

### Evidence limits {#source-acquisition-evidence}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 2. Implement Endweave protocol translation plugin (v944 -> v924) {#2-implement-endweave-protocol-translation-plugin-v944---v924}
- Commit: [9ebbbd75d62476f45c7129c89d126e7211250355](https://github.com/EndstoneMC/endweave/commit/9ebbbd75d62476f45c7129c89d126e7211250355)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-17T17:01:32Z; committed: 2026-03-17T17:01:32Z
- Parents: f9810def2a166a4c6404d665391e91b29d13e37f
- Reading: non-generated diffs read; generated JSON exact-blob reconstruction and structural audit
- Changed files: .gitignore, CLAUDE.md, pyproject.toml, src/endstone_endweave/__init__.py, src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/nbt.py, src/endstone_endweave/codec/reader.py, src/endstone_endweave/codec/writer.py, src/endstone_endweave/data/.gitkeep, src/endstone_endweave/data/v924_packets.json, src/endstone_endweave/data/v924_v944_diff.json, src/endstone_endweave/data/v944_packets.json, src/endstone_endweave/pipeline.py, src/endstone_endweave/player_state.py, src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/__init__.py, src/endstone_endweave/protocol/base.py, src/endstone_endweave/protocol/registry.py, src/endstone_endweave/protocol/v924_to_v944/__init__.py, src/endstone_endweave/protocol/v924_to_v944/block_position.py, src/endstone_endweave/protocol/v924_to_v944/enum_map.py, src/endstone_endweave/protocol/v924_to_v944/handlers/__init__.py, src/endstone_endweave/protocol/v924_to_v944/handlers/auth_input.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/command_block.py, src/endstone_endweave/protocol/v924_to_v944/handlers/login.py, src/endstone_endweave/protocol/v924_to_v944/handlers/map_item_data.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v944/handlers/structure_block.py, src/endstone_endweave/protocol/v924_to_v944/handlers/sub_chunk.py, src/endstone_endweave/protocol/v924_to_v944/packet_ids.py, src/endstone_endweave/protocol/v924_to_v944/packets/__init__.py, src/endstone_endweave/protocol/v924_to_v944/packets/add_volume_entity.py, src/endstone_endweave/protocol/v924_to_v944/packets/anvil_damage.py, src/endstone_endweave/protocol/v924_to_v944/packets/block_actor_data.py, src/endstone_endweave/protocol/v924_to_v944/packets/block_event.py, src/endstone_endweave/protocol/v924_to_v944/packets/container_open.py, src/endstone_endweave/protocol/v924_to_v944/packets/lectern_update.py, src/endstone_endweave/protocol/v924_to_v944/packets/open_sign.py, src/endstone_endweave/protocol/v924_to_v944/packets/play_sound.py, src/endstone_endweave/protocol/v924_to_v944/packets/player_action.py, src/endstone_endweave/protocol/v924_to_v944/packets/set_spawn_position.py, src/endstone_endweave/protocol/v924_to_v944/packets/structure_template_data_request.py, src/endstone_endweave/protocol/v924_to_v944/packets/update_block.py, src/endstone_endweave/protocol/v924_to_v944/packets/update_block_synced.py, src/endstone_endweave/protocol/v924_to_v944/translator.py, src/endstone_example/__init__.py, src/endstone_example/example_listener.py, src/endstone_example/example_plugin.py, src/endstone_example/python_command.py, tests/test_block_pos_packets.py, tests/test_codec.py, tests/test_enum_map.py, tests/test_gameplay_rewriter.py, tests/test_login_rewriter.py, tests/test_nbt_skip.py, tests/test_pipeline.py, tools/fetch_protocol_docs.py, tools/generate_diff.py, tools/parse_dot_files.py, uv.lock

Initial plugin replaces Endstone example template with session-address tracking, exact version-pair translator registry, typed packet dataclasses/position-codec closures, low-priority event interception, binary reader/writer and offline document pipeline. Co-authored-by Claude Opus4.6 trailer retained; Git author identity does not imply sole manual authorship. Important delivered-state mismatch: factory enables only login and StartGame while most gameplay registrations/cancellations are commented out, although message advertises98 tests and broad support. Pipeline cancellation branches only log rather than call event.cancel; exceptions fail open with original incompatible payload. Tests for disabled registrations/cancellations contradict factory state, so claimed count is not a pass result. StartGame has incomplete spawn-settings offsets; MapData flags are2/4/8 in wrong categories; AuthInput bails out at first inventory action, leaving later coordinates unchanged, and65-bit input is serialized through64-bit writer. Position conversion incorrectly multiplies/divides8, supported by matching synthetic tests rather than captured wire data; later17 removes this assumption. NBT skipper uses fixed-width LE/string-short format, unbounded recursion and unchecked skip lengths; later network-NBT rewrite replaces it. Reader short slices advance beyond input, position/skip unrestricted, varint terminal high bits unbounded; writer masks bytes and32/64bit unsigned. Most dataclasses fully deserialize fixed fields and discard unknown tails, versus explicit trailing fields for selected packets. BlockEvent instrument remap helper exists but is not wired. Session cleanup only player quit; no prelogin timeout. Login preserves opaque chain bytes and short payload passthrough. Tests cover synthetic roundtrips/thresholds/session routing, sometimes call a one-way transform roundtrip without validating inverse. Tool clones are existence-cached, regex DOT assumes root0, ignores reference expansion and yields blank type values throughout both generated snapshots; diff compares path/type but not ordering/attributes. Generated JSON reconstructed and exact blobs verified:160/187 definitions,3201/3621 field type strings all empty, so apparent type changes appear as path renames. Full generated diff summary read; repetitive snapshots received exhaustive structural audit rather than literal-by-literal reasoning. No upstream code/tests run.

### Evidence limits {#source-acquisition-evidence-2}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 3. Add full PacketId enum, debug logging, and fix cancel list {#3-add-full-packetid-enum-debug-logging-and-fix-cancel-list}
- Commit: [03eec39346f1047e338bfaa4e9c72a3dd87600ac](https://github.com/EndstoneMC/endweave/commit/03eec39346f1047e338bfaa4e9c72a3dd87600ac)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-17T17:08:39Z; committed: 2026-03-17T17:08:39Z
- Parents: 9ebbbd75d62476f45c7129c89d126e7211250355
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/pipeline.py, src/endstone_endweave/protocol/v924_to_v944/packet_ids.py, src/endstone_endweave/protocol/v924_to_v944/translator.py, tests/test_login_rewriter.py

Re-enables previously commented complex and block-position handlers, corrects cancellation to genuinely new serverbound packet 343 rather than existing 306/318, and changes regression expectation accordingly. Expands packet enum and readable logging with numeric fallback. Message credits Claude Opus 4.6. Message mentions removal of future annotations and new exception handling, but actual diff only changes existing exception log labels and does not change plugin.py: message is broader than this patch. Errors still return rather than cancel at this point.

### Evidence limits {#source-acquisition-evidence-3}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 4. Add JSON Schema parsing to protocol docs pipeline {#4-add-json-schema-parsing-to-protocol-docs-pipeline}
- Commit: [b397ef252176d68f27ca3e7b10a0dcae89d29e37](https://github.com/EndstoneMC/endweave/commit/b397ef252176d68f27ca3e7b10a0dcae89d29e37)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-17T17:29:28Z; committed: 2026-03-17T17:29:28Z
- Parents: 03eec39346f1047e338bfaa4e9c72a3dd87600ac
- Reading: non-generated diffs read; generated JSON exact-blob reconstruction and structural audit
- Changed files: CLAUDE.md, src/endstone_endweave/data/v924_packets.json, src/endstone_endweave/data/v924_v944_diff.json, src/endstone_endweave/data/v944_packets.json, src/endstone_endweave/protocol/v924_to_v944/translator.py, tools/fetch_protocol_docs.py, tools/generate_diff.py, tools/parse_dot_files.py, tools/parse_protocol_docs.py

Adds JSON Schema alongside DOT acquisition/parsing, sorting properties by x-ordinal-index, mapping compressed integer underlyings and recursively expanding local definitions/array items; JSON overrides same-name DOT definitions. Keeps regex DOT/root0 limitations, no recursive-cycle protection, ignores schema optionality/enum numeric values, and flattening still misses order/attributes. Full non-generated code and generated diff summary read. Exhaustive reconstructed JSON/blob audit confirms924160→333 and944187→366 definitions, unique names throughout. New JSON definitions introduce concrete types where original DOT field types are all empty; only existing924 EditorNetwork and944 EditorNetwork/PlayerSkin definitions are overwritten. Generated differences now expose positional Y encoding changes, camera spline additions, UI fields, voxel trailing CustomShapeCount and input-lock server-position removal, while PlayerAuthInput node-number noise persists. Broad new-type labels still mix packet and subtype additions, resolved much later86. Separate executable change expands serverbound cancellation from one ID to inclusive range340–345 (per enum endpoints), despite documentation-focused title. These generated documents aid hypothesis discovery, not proof of wire behavior. Co-authored-by Claude trailer retained. No parser/test execution.

### Evidence limits {#source-acquisition-evidence-4}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 5. Add git conventions to CLAUDE.md {#5-add-git-conventions-to-claude-md}
- Commit: [c423aefbac6862b530e4f5128f41358c7fe861ab](https://github.com/EndstoneMC/endweave/commit/c423aefbac6862b530e4f5128f41358c7fe861ab)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-17T17:31:36Z; committed: 2026-03-17T17:31:36Z
- Parents: b397ef252176d68f27ca3e7b10a0dcae89d29e37
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CLAUDE.md

Repository-specific contributor guidance prohibits Claude co-author trailers. This is historical repository content, not current instructions; commit trailers remain the evidence for declared coauthorship.

### Evidence limits {#source-acquisition-evidence-5}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 6. Update README with actual project documentation {#6-update-readme-with-actual-project-documentation}
- Commit: [cd8966b747d0ef5b9e824c4457e88af8ca3cc0b6](https://github.com/EndstoneMC/endweave/commit/cd8966b747d0ef5b9e824c4457e88af8ca3cc0b6)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-17T22:13:42Z; committed: 2026-03-17T22:13:42Z
- Parents: c423aefbac6862b530e4f5128f41358c7fe861ab
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: README.md

Replaces inherited example README with translator purpose, selective rewrite and matching-version fast path, architecture and development workflow. Documentation promises zero deserialization rather than measured zero total cost; no execution evidence. Identifies ViaVersion inspiration and Endstone hosting.

### Evidence limits {#source-acquisition-evidence-6}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 7. Generalize protocol translation for arbitrary version pairs {#7-generalize-protocol-translation-for-arbitrary-version-pairs}
- Commit: [1501feeb4d34d1b5ab5c5a36fe7389facf0efc70](https://github.com/EndstoneMC/endweave/commit/1501feeb4d34d1b5ab5c5a36fe7389facf0efc70)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-18T00:28:16Z; committed: 2026-03-18T00:28:16Z
- Parents: cd8966b747d0ef5b9e824c4457e88af8ca3cc0b6
- Reading: non-generated diffs read; generated JSON exact-blob reconstruction and structural audit
- Changed files: .gitignore, CLAUDE.md, README.md, data/v924_packets.json, data/v924_v944_diff.json, data/v944_packets.json, src/endstone_endweave/data/.gitkeep, src/endstone_endweave/data/v924_packets.json, src/endstone_endweave/data/v924_v944_diff.json, src/endstone_endweave/data/v944_packets.json, src/endstone_endweave/pipeline.py, src/endstone_endweave/player_state.py, src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/base.py, src/endstone_endweave/protocol/packet_ids.py, src/endstone_endweave/protocol/registry.py, src/endstone_endweave/protocol/v924_to_v944/__init__.py, src/endstone_endweave/protocol/v924_to_v944/handlers/auth_input.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/command_block.py, src/endstone_endweave/protocol/v924_to_v944/handlers/login.py, src/endstone_endweave/protocol/v924_to_v944/handlers/map_item_data.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v944/handlers/structure_block.py, src/endstone_endweave/protocol/v924_to_v944/handlers/sub_chunk.py, src/endstone_endweave/protocol/v924_to_v944/packet_ids.py, src/endstone_endweave/protocol/v924_to_v944/translator.py, src/endstone_endweave/protocol/versions.py, src/endstone_endweave/session.py, tests/test_block_pos_packets.py, tests/test_gameplay_rewriter.py, tests/test_login_rewriter.py, tests/test_pipeline.py, tools/fetch_protocol_docs.py, tools/generate_diff.py, tools/parse_protocol_docs.py

Generalizes exact-pair registry into direct-first BFS over client→server edges, reverses chain clientbound, caches both reachable/unreachable paths globally and successful chains per session. Registration invalidates registry cache but existing session chains remain stale; repeated handshake can change client_protocol without invalidating session chain. Pipeline now actually calls event.cancel on either direction, fixing original log-only cancellation. It assigns event.payload after every hop: a later exception fails open with partially translated bytes. Login uses final session.server_protocol in each hop and overwrites session.client_protocol from current payload, so repeated login rewriting can lose original-client identity in multi-hop chains. Central version records drive tooling and server string detection, with lowest-known fallback for unmatched version strings; max-client advertisement depends only on graph reachability. Shared PacketId full class is byte-identical to removed version-specific class, with compatibility reexport and factory alias. Three generated JSON files are exact blob-equivalent moves from package to root; adding data/ ignore does not untrack them, hence deletion28. CLI gains known-tag/numeric diff args, min/max defaults, version-registry imports; package import still depends on runtime entrypoint. Tests only adjust imports/session constructor, adding no BFS/cancellation/multi-hop regression. Claims of arbitrary version support/stable IDs are scoped architectural intent, not compatibility evidence. This bytes-per-hop pipeline initially composes outputs; later wrapper rewrite10 introduces shared-cursor issue, repaired in collaborator PR4 context.

### Evidence limits {#source-acquisition-evidence-7}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 8. Add version range detection, cancel clientbound packets, and fix mypy errors {#8-add-version-range-detection-cancel-clientbound-packets-and-fix-mypy-errors}
- Commit: [2fe8c33bba57c680dfc0c990a93b7edb71583a5c](https://github.com/EndstoneMC/endweave/commit/2fe8c33bba57c680dfc0c990a93b7edb71583a5c)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-18T01:06:50Z; committed: 2026-03-18T01:06:50Z
- Parents: 1501feeb4d34d1b5ab5c5a36fe7389facf0efc70
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/pipeline.py, src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/base.py, src/endstone_endweave/protocol/registry.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/client_input_locks.py, src/endstone_endweave/protocol/v924_to_v944/translator.py, src/endstone_endweave/protocol/versions.py, tests/test_cancel_and_input_locks.py, tests/test_pipeline.py, uv.lock

Adds version aliases and short-name normalization, retains unsafe-to-generalize fallback to minimum registered protocol when unknown. Adds clientbound cancellation with priority over handlers, cancels incompatible editor/UI/voxel packets and serverbound skin pending implementation. Client input lock handler emits only unsigned flags, deliberately discarding old trailing Vec3. Tests cover cancellation priority and full output consumption, large flags and aliases. Fixes has_remaining method invocation and logger/type mismatches. Lock still requires Python >=3.13 here despite later package metadata broadening.

### Evidence limits {#source-acquisition-evidence-8}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 9. Remove dead code and backwards compatibility shims {#9-remove-dead-code-and-backwards-compatibility-shims}
- Commit: [89f8f39ea11dc4b62e37f5237ac9aa69aacd5e87](https://github.com/EndstoneMC/endweave/commit/89f8f39ea11dc4b62e37f5237ac9aa69aacd5e87)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-18T01:12:34Z; committed: 2026-03-18T01:12:34Z
- Parents: 2fe8c33bba57c680dfc0c990a93b7edb71583a5c
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/v924_to_v944/__init__.py, src/endstone_endweave/protocol/v924_to_v944/block_position.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/packet_ids.py, src/endstone_endweave/protocol/v924_to_v944/translator.py, src/endstone_endweave/session.py, tests/test_block_pos_packets.py, tests/test_login_rewriter.py

Removes compatibility reexports/factory alias and unused varint/string helpers, updating internal/test imports to canonical paths. This is an API cleanup in early history, not proof external users were unaffected. Actual deleted helpers inspected; no independent algorithmic innovation.

### Evidence limits {#source-acquisition-evidence-9}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 10. Refactor to ViaVersion-aligned architecture {#10-refactor-to-viaversion-aligned-architecture}
- Commit: [2aff6e5ba7e1aa453741540e863412bb89fc17fc](https://github.com/EndstoneMC/endweave/commit/2aff6e5ba7e1aa453741540e863412bb89fc17fc)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T17:36:44Z; committed: 2026-03-19T17:36:44Z
- Parents: 89f8f39ea11dc4b62e37f5237ac9aa69aacd5e87
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CLAUDE.md, src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types.py, src/endstone_endweave/codec/wrapper.py, src/endstone_endweave/config.toml, src/endstone_endweave/connection.py, src/endstone_endweave/pipeline.py, src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/base.py, src/endstone_endweave/protocol/base_protocol.py, src/endstone_endweave/protocol/manager.py, src/endstone_endweave/protocol/registry.py, src/endstone_endweave/protocol/v924_to_v944/__init__.py, src/endstone_endweave/protocol/v924_to_v944/handlers/login.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, src/endstone_endweave/protocol/v924_to_v944/translator.py, src/endstone_endweave/session.py, tests/test_base_protocol.py, tests/test_login_rewriter.py, tests/test_pipeline.py, tests/test_wrapper.py

Major ViaVersion-inspired migration: renames session/translator/registry/pipeline to connection/protocol/manager/pipeline, introduces typed read/write/passthrough wrapper with separate input/output and automatic unread tail, extracts base version-detection/disconnect logic, and retains directed BFS with direct-path cache and invalidation on register. Crucially new protocol factory only registers login and new-packet cancellation: prior gameplay handlers disappear from registration rather than being behavior-preserving renames. Old handler modules remain until12 cleanup. Single wrapper shared across chain consumes its input;11 repairs base/version boundary but not every multi-step boundary. Tests verify primitive roundtrips, manipulation and synthetic routing, not actual multi-step rewrite composition; short malformed base test catches all exceptions without requiring a precise error. Base clientbound is skipped for matching versions, contrary to always-on description. Logger config toggles debug level; no benchmark/run.

### Evidence limits {#source-acquisition-evidence-10}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 11. Fix wrapper reuse between base and version protocols {#11-fix-wrapper-reuse-between-base-and-version-protocols}
- Commit: [ebf9f5f0ce091c5d6078772b2b165b13db764c19](https://github.com/EndstoneMC/endweave/commit/ebf9f5f0ce091c5d6078772b2b165b13db764c19)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T17:37:41Z; committed: 2026-03-19T17:37:41Z
- Parents: 2aff6e5ba7e1aa453741540e863412bb89fc17fc
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/pipeline.py

Fixes consumed-cursor reuse between base and version protocol stages: serialize wrapper output, instantiate a fresh wrapper, and compare final bytes against original event payload. Serverbound base output is preserved even without translation/chain; clientbound finalization happens before base transforms. Explicit rationale is cursor consumption. No new regression test in patch; cannot claim runtime fix verified.

### Evidence limits {#source-acquisition-evidence-11}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 12. Remove dead code and rename varint/varlong methods {#12-remove-dead-code-and-rename-varint-varlong-methods}
- Commit: [00ef13c3acadce65b7ee70139e87942d00a021af](https://github.com/EndstoneMC/endweave/commit/00ef13c3acadce65b7ee70139e87942d00a021af)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T17:39:07Z; committed: 2026-03-19T17:39:07Z
- Parents: ebf9f5f0ce091c5d6078772b2b165b13db764c19
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/nbt.py, src/endstone_endweave/codec/reader.py, src/endstone_endweave/codec/writer.py, src/endstone_endweave/protocol/v924_to_v944/block_position.py, src/endstone_endweave/protocol/v924_to_v944/enum_map.py, src/endstone_endweave/protocol/v924_to_v944/handlers/auth_input.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/client_input_locks.py, src/endstone_endweave/protocol/v924_to_v944/handlers/command_block.py, src/endstone_endweave/protocol/v924_to_v944/handlers/map_item_data.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v944/handlers/structure_block.py, src/endstone_endweave/protocol/v924_to_v944/handlers/sub_chunk.py, src/endstone_endweave/protocol/v924_to_v944/packets/__init__.py, src/endstone_endweave/protocol/v924_to_v944/packets/add_volume_entity.py, src/endstone_endweave/protocol/v924_to_v944/packets/anvil_damage.py, src/endstone_endweave/protocol/v924_to_v944/packets/block_actor_data.py, src/endstone_endweave/protocol/v924_to_v944/packets/block_event.py, src/endstone_endweave/protocol/v924_to_v944/packets/container_open.py, src/endstone_endweave/protocol/v924_to_v944/packets/lectern_update.py, src/endstone_endweave/protocol/v924_to_v944/packets/open_sign.py, src/endstone_endweave/protocol/v924_to_v944/packets/play_sound.py, src/endstone_endweave/protocol/v924_to_v944/packets/player_action.py, src/endstone_endweave/protocol/v924_to_v944/packets/set_spawn_position.py, src/endstone_endweave/protocol/v924_to_v944/packets/structure_template_data_request.py, src/endstone_endweave/protocol/v924_to_v944/packets/update_block.py, src/endstone_endweave/protocol/v924_to_v944/packets/update_block_synced.py, tests/test_block_pos_packets.py, tests/test_cancel_and_input_locks.py, tests/test_codec.py, tests/test_enum_map.py, tests/test_gameplay_rewriter.py, tests/test_nbt_skip.py

Removes now-disconnected pre-wrapper handlers, typed packet dataclasses, fixed-little-endian NBT skipper and their tests after architecture replacement10. Deleted code embodied coordinate-times-eight assumption and incomplete nonempty-inventory-action handling; removed roundtrip tests sometimes asserted only non-null output, not actual roundtrip identity. Renames unsigned read/write_varint to uvarint and signed methods to varint, likewise unsigned64, adds signed64 zigzag. Existing codec tests migrate names; no new signed64 boundary tests. This is removal of obsolete implementation and test coverage, not proof gameplay behavior was preserved.

### Evidence limits {#source-acquisition-evidence-12}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 13. Add Direction enum, wrapper.user(), and single transform() method {#13-add-direction-enum-wrapper-user-and-single-transform-method}
- Commit: [bc8df50830acd4511e63692a7cab12b9fabe2ada](https://github.com/EndstoneMC/endweave/commit/bc8df50830acd4511e63692a7cab12b9fabe2ada)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T17:47:08Z; committed: 2026-03-19T17:47:08Z
- Parents: 00ef13c3acadce65b7ee70139e87942d00a021af
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/wrapper.py, src/endstone_endweave/pipeline.py, src/endstone_endweave/protocol/base.py, src/endstone_endweave/protocol/base_protocol.py, src/endstone_endweave/protocol/direction.py, src/endstone_endweave/protocol/v924_to_v944/handlers/login.py, tests/test_base_protocol.py, tests/test_login_rewriter.py, tests/test_pipeline.py, tests/test_wrapper.py

Consolidates direction methods into transform(Direction,id,wrapper), injects connection into wrapper.user and changes handlers to one argument; passthrough_remaining renamed passthrough_all. All associated tests/imports migrated. Missing-user check initially assert and thus removable under optimization, fixed31. No wire semantics intentionally changed; return typing remains object until47.

### Evidence limits {#source-acquisition-evidence-13}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 14. Merge base_protocol.py into base.py {#14-merge-baseprotocol-py-into-base-py}
- Commit: [8b9e45175231f3f659fc3b40062f38ed3566893a](https://github.com/EndstoneMC/endweave/commit/8b9e45175231f3f659fc3b40062f38ed3566893a)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T17:55:34Z; committed: 2026-03-19T17:55:34Z
- Parents: bc8df50830acd4511e63692a7cab12b9fabe2ada
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/base.py, src/endstone_endweave/protocol/base_protocol.py, tests/test_base_protocol.py, tests/test_pipeline.py

Combines always-on base handlers with framework Protocol in base.py to resolve confusing base/base_protocol names, updating factory imports/tests. No changed transform algorithm. Naming simplification is transitional, not final design:15 separates abstract infrastructure from concrete base behavior again.

### Evidence limits {#source-acquisition-evidence-14}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 15. Move Protocol class to protocol/__init__.py, keep base protocol in base.py {#15-move-protocol-class-to-protocol-init-py-keep-base-protocol-in-base-py}
- Commit: [80064fb7439ae80faad5694da111e8191f5f2a71](https://github.com/EndstoneMC/endweave/commit/80064fb7439ae80faad5694da111e8191f5f2a71)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T17:59:18Z; committed: 2026-03-19T17:59:18Z
- Parents: 8b9e45175231f3f659fc3b40062f38ed3566893a
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/connection.py, src/endstone_endweave/pipeline.py, src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/__init__.py, src/endstone_endweave/protocol/base.py, src/endstone_endweave/protocol/manager.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, tests/test_base_protocol.py, tests/test_pipeline.py, tests/test_wrapper.py

Moves framework Protocol/PacketHandler into protocol package root while keeping concrete initial-base handlers in base.py; restores explicit create_base_protocol factory name. Full old/new class inspected: transformation/cancellation logic retained, consumers updated. Stated rationale mirrors ViaVersion API versus concrete-protocol separation.

### Evidence limits {#source-acquisition-evidence-15}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 16. Add full StartGamePacket handler, COMPOUND_TAG type, and NBT skip {#16-add-full-startgamepacket-handler-compoundtag-type-and-nbt-skip}
- Commit: [b92348aa5c2345a21c6d431c41b8c8c55f6ade7e](https://github.com/EndstoneMC/endweave/commit/b92348aa5c2345a21c6d431c41b8c8c55f6ade7e)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T21:40:34Z; committed: 2026-03-19T21:40:34Z
- Parents: 80064fb7439ae80faad5694da111e8191f5f2a71
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/reader.py, src/endstone_endweave/codec/types.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v944/handlers/voxel_shapes.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, tests/test_start_game.py

Restores full StartGame and VoxelShapes clientbound handlers on wrapper architecture: spawn Y re-encoding, parsed intervening fields, raw network-NBT slices, conditional gathering removal and zero custom-shape count append. NBT uses explicit stack/depth512, network varint lengths/int values, but title claiming all12 tags exceeds implementation (no tag12 branch); direct cursor increments and negative lengths remain unchecked until later safety work. Experiments prints names. Crucial comment/test contradiction: join-info outer flag is passed through; when true handler writes three false subflags, whereas two new tests expect identical bytes to outer-false packet. Static inspection establishes disagreement, not observed test-run results. Other tests verify consumed-input and substring presence rather than fully parsing output. Coordinate-times-eight assumption from removed implementation is no longer used.

### Evidence limits {#source-acquisition-evidence-16}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 17. Add BlockPos handlers for all v924-to-v944 affected packets {#17-add-blockpos-handlers-for-all-v924-to-v944-affected-packets}
- Commit: [3e3bedff61365427a4d408de9fa24db1128511bd](https://github.com/EndstoneMC/endweave/commit/3e3bedff61365427a4d408de9fa24db1128511bd)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T22:26:40Z; committed: 2026-03-19T22:26:40Z
- Parents: b92348aa5c2345a21c6d431c41b8c8c55f6ade7e
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos_packets.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, tests/test_block_pos.py

Rebuilds gameplay coverage after12 with NetworkBlockPos unsigned Y and BlockPos zigzag Y codecs, explicitly without old times-eight scaling. Registers first-field and nested-position transforms, input-lock Vec3 stripping and CameraSpline whole-payload false/false suffix (later repaired68). ContainerOpen is incorrectly registered serverbound, fixed64; subchunk entries omit syncedUpdateType until26; structure settings remain opaque until23. Tests encode the same assumptions, including fake spline bytes and nonnegative Y only, demonstrating why self-generated fixtures missed framing/direction defects. Narrows new-packet cancellation to343;23 restores340/342.

### Evidence limits {#source-acquisition-evidence-17}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 18. Apply linter formatting {#18-apply-linter-formatting}
- Commit: [d688a68e18cb30f56938b3d92bd382bda6fcfa1d](https://github.com/EndstoneMC/endweave/commit/d688a68e18cb30f56938b3d92bd382bda6fcfa1d)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T22:27:32Z; committed: 2026-03-19T22:27:32Z
- Parents: 3e3bedff61365427a4d408de9fa24db1128511bd
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/reader.py, src/endstone_endweave/connection.py, src/endstone_endweave/pipeline.py, src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/manager.py, src/endstone_endweave/protocol/versions.py, tests/test_base_protocol.py, tests/test_codec.py, tests/test_login_rewriter.py, tests/test_pipeline.py, tests/test_start_game.py, tests/test_wrapper.py, tools/fetch_protocol_docs.py, tools/generate_diff.py, tools/parse_protocol_docs.py

Mostly formatter and unused-import cleanup, but the pipeline debug message switches from len(payload) to len(event.payload) in both directions. This fixes a clientbound reference to an unavailable local in the shown context and makes log sizing use original event input. Thus the formatting title conceals an executable change. Tests only reformatted; inherited StartGame nine-boolean fixture and contradictory join-info expectation remain.

### Evidence limits {#source-acquisition-evidence-18}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 19. Remove from __future__ import annotations from all files {#19-remove-from-future-import-annotations-from-all-files}
- Commit: [da4a166f971128aeb40e5cd9b283a467c0f7fe0d](https://github.com/EndstoneMC/endweave/commit/da4a166f971128aeb40e5cd9b283a467c0f7fe0d)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T22:29:44Z; committed: 2026-03-19T22:29:44Z
- Parents: d688a68e18cb30f56938b3d92bd382bda6fcfa1d
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CLAUDE.md, src/endstone_endweave/codec/reader.py, src/endstone_endweave/codec/types.py, src/endstone_endweave/codec/wrapper.py, src/endstone_endweave/codec/writer.py, src/endstone_endweave/connection.py, src/endstone_endweave/pipeline.py, src/endstone_endweave/protocol/__init__.py, src/endstone_endweave/protocol/base.py, src/endstone_endweave/protocol/manager.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos_packets.py, src/endstone_endweave/protocol/v924_to_v944/handlers/login.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v944/handlers/voxel_shapes.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, src/endstone_endweave/protocol/versions.py, tests/test_base_protocol.py, tests/test_block_pos.py, tests/test_codec.py, tests/test_login_rewriter.py, tests/test_pipeline.py, tests/test_start_game.py, tests/test_wrapper.py

Removes postponed annotations throughout source/tests and records a repository instruction against the future import. TYPE_CHECKING-only UserConnection and Protocol references are explicitly quoted to avoid eager name resolution. No rationale beyond the style directive and no compatibility validation supplied; this is repository-local guidance, not a universal Python recommendation.

### Evidence limits {#source-acquisition-evidence-19}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 20. Remove __slots__ from all classes {#20-remove-slots-from-all-classes}
- Commit: [206fa03acec626b815c707a92181e802f691b613](https://github.com/EndstoneMC/endweave/commit/206fa03acec626b815c707a92181e802f691b613)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T22:30:21Z; committed: 2026-03-19T22:30:21Z
- Parents: da4a166f971128aeb40e5cd9b283a467c0f7fe0d
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CLAUDE.md, src/endstone_endweave/codec/reader.py, src/endstone_endweave/codec/types.py, src/endstone_endweave/codec/wrapper.py, src/endstone_endweave/codec/writer.py

Removes __slots__ from reader, writer, wrapper, generic Type and primitive/composite codec classes, and adds an explicit repository rule against slots. Wire behavior is unchanged, but instance layout, dynamic-attribute allowance and allocation costs can change; no measurement or stated motivation supports a performance conclusion.

### Evidence limits {#source-acquisition-evidence-20}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 21. style: remove unnecessary blank lines across all files {#21-style-remove-unnecessary-blank-lines-across-all-files}
- Commit: [65aa4f91faeae447c4646864cf2ba71524ae9cc4](https://github.com/EndstoneMC/endweave/commit/65aa4f91faeae447c4646864cf2ba71524ae9cc4)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T22:31:16Z; committed: 2026-03-19T22:31:16Z
- Parents: 206fa03acec626b815c707a92181e802f691b613
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/reader.py, src/endstone_endweave/codec/types.py, src/endstone_endweave/codec/wrapper.py, src/endstone_endweave/codec/writer.py, src/endstone_endweave/connection.py, src/endstone_endweave/pipeline.py, src/endstone_endweave/protocol/__init__.py, src/endstone_endweave/protocol/base.py, src/endstone_endweave/protocol/manager.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos_packets.py, src/endstone_endweave/protocol/v924_to_v944/handlers/login.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v944/handlers/voxel_shapes.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, src/endstone_endweave/protocol/versions.py, tests/test_base_protocol.py, tests/test_block_pos.py, tests/test_codec.py, tests/test_login_rewriter.py, tests/test_pipeline.py, tests/test_start_game.py, tests/test_wrapper.py

Verified whitespace-only removal of blank lines left by annotation/slots cleanup in source and tests. No independent engineering lesson or behavior change.

### Evidence limits {#source-acquisition-evidence-21}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 22. Fix ruff lint errors {#22-fix-ruff-lint-errors}
- Commit: [3162246091d0dfad84076f91630860fedd43db0b](https://github.com/EndstoneMC/endweave/commit/3162246091d0dfad84076f91630860fedd43db0b)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T22:33:11Z; committed: 2026-03-19T22:33:11Z
- Parents: 65aa4f91faeae447c4646864cf2ba71524ae9cc4
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, tests/test_start_game.py, tests/test_wrapper.py, tools/generate_diff.py, tools/parse_protocol_docs.py

Removes unused local bindings without removing reads/passthrough calls; cleans misleading unused reader in trailing-string test, and permits E402 for deliberate sys.path setup in tools. Small lint disposition; test still checks string presence rather than complete packet structure.

### Evidence limits {#source-acquisition-evidence-22}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 23. Refactor BlockPos handlers {#23-refactor-blockpos-handlers}
- Commit: [f566c680f827bc2a4cc8f80bd4d61a48e4f4dc7a](https://github.com/EndstoneMC/endweave/commit/f566c680f827bc2a4cc8f80bd4d61a48e4f4dc7a)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T23:04:24Z; committed: 2026-03-19T23:04:24Z
- Parents: 3162246091d0dfad84076f91630860fedd43db0b
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos_packets.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, tests/test_block_pos.py

A refactor title includes real coverage additions: PlaySound registration/conversion, full nested StructureSettings size/offset rewriting in both structure update/request handlers, and cancellation340/342 alongside343. Renames block_pos module and drops _sb suffixes. Tests now build real nested structure fields instead of fake tails, but verifier stops at integrity seed and does not assert pivot/trailing consumption. ContainerOpen wrong-direction assumption persists.

### Evidence limits {#source-acquisition-evidence-23}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 24. Zero block registry checksum in StartGame for v944 clients {#24-zero-block-registry-checksum-in-startgame-for-v944-clients}
- Commit: [dd565e489ac7c604305f56aa5fcb38fb4a0a7f22](https://github.com/EndstoneMC/endweave/commit/dd565e489ac7c604305f56aa5fcb38fb4a0a7f22)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T23:18:35Z; committed: 2026-03-19T23:18:35Z
- Parents: f566c680f827bc2a4cc8f80bd4d61a48e4f4dc7a
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py

Reads but discards old LONG_LE block registry checksum, emits zero. Commit explains different registries caused a client rejection and says hash-based block IDs remain functional. This is validation bypass for interoperability, not proof registry equivalence; later block mapping work must be evaluated separately. No test added here.

### Evidence limits {#source-acquisition-evidence-24}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 25. Add MapItemData handler for tracked block object UBlockPos conversion {#25-add-mapitemdata-handler-for-tracked-block-object-ublockpos-conversion}
- Commit: [4398bbc5264a470b210585032f6da582d6dd2d3c](https://github.com/EndstoneMC/endweave/commit/4398bbc5264a470b210585032f6da582d6dd2d3c)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-19T23:28:36Z; committed: 2026-03-19T23:28:36Z
- Parents: dd565e489ac7c604305f56aa5fcb38fb4a0a7f22
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py

Adds MapItemData tracked-block position conversion gated by Decoration bit and Block object discriminant. Preserves map header, optional creation IDs, scale, entity IDs; converts only block object positions from NetworkBlockPos to BlockPos. Origin is already signed and left alone. Relies on trailing auto-copy; no patch tests. Correctness depends on field flags and discriminants, not blanket conversion of every position.

### Evidence limits {#source-acquisition-evidence-25}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.
