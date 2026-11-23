<!-- retrieval: {"source_ids":["public:commit:007f3f83aa2d67f0839fe3da09ef1ddfedbb7ef9","public:commit:1c6ce2e75ccb6c9baa7e7a966a0658ec419ccfb2","public:commit:1c71334c18bea89446b76ae7087b4276a5cb66cd","public:commit:202157c76b587dc04fc2ec6f1b05ec2d46a313c7","public:commit:26a4950ea9f1b4ed076b5b16d55d60e4031a1102","public:commit:2b912b0484e7f9ad903f57073ced386f6a359a1d","public:commit:2f6229368cf1b8592dc82245b75a42471411cb7a","public:commit:40e685133e1450bfe0b572f097cf08ca10e8ad6b","public:commit:5fca1a41ddacf387d64b83e0587d5fdb2e402dbe","public:commit:636b32bba4c92e3994216f2ea3b9977b93971d13","public:commit:7bc0cbc78bf3d2625363dcf86df47bd6c610b712","public:commit:7edb52b4d444789cad0ee3c91f4c08594148f7e2","public:commit:9cee026e9b22d045d0114302ab40b5956ce447cb","public:commit:add4d85225b4d7ddbaf15186d908dcd2cd74c065","public:commit:b01480dbce0fc68b7417c68230257377d541e458","public:commit:b5e33d30c64df06c6734882cc5c9c07a86516ced","public:commit:bfcb5bf7db1c3221d122d6aa136f33f442890f6e","public:commit:c4e455cd6a5d24a52f7d4eee30a6002b08532b1f","public:commit:cb408753eab01268d0b746b1299372cf401e39f1","public:commit:df3ef46a35be49e498dd4a4a6a31c32b4186f1b9","public:commit:e257eadfe76fc3c11a26264f1fcf8ab736f04860","public:commit:e913a03f94e0fdbadec4688c85bd52b2d84f461f","public:commit:ec23ae2e2c3336a46f474450bb11a69cc42e81d5","public:commit:ee013d7875c417964731a8436bc04c9bcd0691c9","public:commit:f2dcf756e756cca4382843bb4d5e82877b39c01a"],"source_type":"public","date":"2026-03-20..2026-03-21","topics":["lifetime","concurrency","ffi","testing","build","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endweave-commit-dossiers-assignment-ordinals-26-50"></a>
# Endweave commit dossiers: assignment ordinals 26–50 {#endweave-commit-dossiers-assignment-ordinals-26-50}

Static source review. Assignment ordinals are identifiers, not a topological ordering. Exact parents below define ancestry. Acquired but unread entries remain open. No upstream code, tests or workflows executed. Generated data must receive a separate structural audit before closure.

## 26. Add ITEM_INSTANCE type, InventoryTransaction handler, and fixes {#26-add-iteminstance-type-inventorytransaction-handler-and-fixes}
- Commit: [9cee026e9b22d045d0114302ab40b5956ce447cb](https://github.com/EndstoneMC/endweave/commit/9cee026e9b22d045d0114302ab40b5956ce447cb)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-20T02:01:43Z; committed: 2026-03-20T02:01:43Z
- Parents: 4398bbc5264a470b210585032f6da582d6dd2d3c
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, tests/test_block_pos.py, tests/test_wrapper.py

Opaque ITEM_INSTANCE codec locates stack boundaries through network ID, count, metadata, optional stack-net ID, block runtime ID and byte-slice extra data, enabling inventory actions without decoding NBT. New InventoryTransaction handler traverses legacy slots and source-specific actions, converts UseItem position and strips cooldown byte only for transaction type2; other transaction payloads remain tail-copied. Restores missing syncedUpdateType in both subchunk arrays and updates fixtures. VAR_LONG becomes VAR_INT64 naming. Claimed340/342 cancellation already existed in parent; changed lines only formatting. No new item/inventory tests here.

### Evidence limits {#source-acquisition-evidence}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 27. Add NoteBlockInstrument remapping to TILE_EVENT handler {#27-add-noteblockinstrument-remapping-to-tileevent-handler}
- Commit: [add4d85225b4d7ddbaf15186d908dcd2cd74c065](https://github.com/EndstoneMC/endweave/commit/add4d85225b4d7ddbaf15186d908dcd2cd74c065)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-20T02:30:52Z; committed: 2026-03-20T02:30:52Z
- Parents: 9cee026e9b22d045d0114302ab40b5956ce447cb
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py

Dedicated TileEvent rewriter replaces generic first-position rewrite. Preserves position conversion and remaps note-block instrument IDs >=16 by +4 only for event_type==0, accounting for inserted trumpet variants. Other event types remain unchanged; no added test or observed client run.

### Evidence limits {#source-acquisition-evidence-2}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 28. Remove data/ folder from tracking {#28-remove-data-folder-from-tracking}
- Commit: [7bc0cbc78bf3d2625363dcf86df47bd6c610b712](https://github.com/EndstoneMC/endweave/commit/7bc0cbc78bf3d2625363dcf86df47bd6c610b712)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-20T14:00:38Z; committed: 2026-03-20T14:00:38Z
- Parents: add4d85225b4d7ddbaf15186d908dcd2cd74c065
- Reading: non-generated diffs read; generated JSON exact-blob reconstruction and structural audit
- Changed files: data/v924_packets.json, data/v924_v944_diff.json, data/v944_packets.json

Deletes the three generated root data JSON files only. Exhaustive static reconstruction parses every deleted byte and verifies exact Git blob hashes against unchanged files moved in7 and produced in4. No new implementation semantics or independent author preference; generator/source remain separate evidence. Repetitive literals were content-equivalence/structurally verified, not individually reasoned about.

### Evidence limits {#source-acquisition-evidence-3}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 29. Rewrite README for clarity and brevity {#29-rewrite-readme-for-clarity-and-brevity}
- Commit: [df3ef46a35be49e498dd4a4a6a31c32b4186f1b9](https://github.com/EndstoneMC/endweave/commit/df3ef46a35be49e498dd4a4a6a31c32b4186f1b9)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-20T14:09:07Z; committed: 2026-03-20T14:09:07Z
- Parents: 7bc0cbc78bf3d2625363dcf86df47bd6c610b712
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: README.md

README compresses architecture/developer detail into supported-version table, wheel installation and conceptual chaining/selective rewrite. Claims zero overhead are documentation language, not measurements. Public installation path now foregrounds releases instead of pip/source setup.

### Evidence limits {#source-acquisition-evidence-4}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 30. Add author, classifiers, and dependencies to pyproject.toml {#30-add-author-classifiers-and-dependencies-to-pyproject-toml}
- Commit: [1c71334c18bea89446b76ae7087b4276a5cb66cd](https://github.com/EndstoneMC/endweave/commit/1c71334c18bea89446b76ae7087b4276a5cb66cd)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-20T14:11:55Z; committed: 2026-03-20T14:11:55Z
- Parents: df3ef46a35be49e498dd4a4a6a31c32b4186f1b9
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: pyproject.toml

Declares endstone>=0.11 and Python>=3.10, dev pytest extra, alpha status and supported interpreter classifiers 3.10–3.14. Adds repository/issues metadata and author attribution. Declared classifiers are not evidence all versions were tested.

### Evidence limits {#source-acquisition-evidence-5}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 31. Fix debug print, harden assert, add docstrings, and clean up code quality {#31-fix-debug-print-harden-assert-add-docstrings-and-clean-up-code-quality}
- Commit: [26a4950ea9f1b4ed076b5b16d55d60e4031a1102](https://github.com/EndstoneMC/endweave/commit/26a4950ea9f1b4ed076b5b16d55d60e4031a1102)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-20T14:29:49Z; committed: 2026-03-20T14:29:49Z
- Parents: 1c71334c18bea89446b76ae7087b4276a5cb66cd
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: .github/workflows/build.yml, src/endstone_endweave/codec/reader.py, src/endstone_endweave/codec/types.py, src/endstone_endweave/codec/wrapper.py, src/endstone_endweave/codec/writer.py, src/endstone_endweave/connection.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, tools/fetch_protocol_docs.py, tools/generate_diff.py, tools/parse_protocol_docs.py

Adds actual pytest CI step and aligns matrix to >=3.10, replacing install-only root workflow. RuntimeError replaces optimizable assert in PacketWrapper.user; removes stray experiment-name print while retaining parsing; extracts direction helpers/constants without changing their transforms, adds codec docstrings and removes future imports in tools. This does not yet repair incorrect ContainerOpen direction (64).

### Evidence limits {#source-acquisition-evidence-6}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 32. Update publish workflow repo, LICENSE year, CLAUDE.md tooling, and uv.lock {#32-update-publish-workflow-repo-license-year-claude-md-tooling-and-uv-lock}
- Commit: [bfcb5bf7db1c3221d122d6aa136f33f442890f6e](https://github.com/EndstoneMC/endweave/commit/bfcb5bf7db1c3221d122d6aa136f33f442890f6e)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-20T14:30:32Z; committed: 2026-03-20T14:30:32Z
- Parents: 26a4950ea9f1b4ed076b5b16d55d60e4031a1102
- Reading: non-generated diffs read; generated lock artifacts structurally audited
- Changed files: .github/workflows/publish.yml, CLAUDE.md, LICENSE, uv.lock

Corrects inherited publish repository gate from python-plugin-template to EndstoneMC/endweave, updates license year2023→2025 and adds uv run guidance. Regenerates minimal Python>=3.13 lock for >=3.10 with actual Endstone0.11.2 and pytest9.0.2 dependency graph; numpy resolves2.2.6 below3.11 and2.4.3 above, with other compatibility markers. All non-artifact lock entries read; exhaustive static scan of1008 artifact URL/hash records confirms files.pythonhosted.org and valid SHA256 lexical forms. Repetitive distribution literals were structurally audited, not individually reasoned about or downloaded/hash-verified. No install/publish execution.

### Evidence limits {#source-acquisition-evidence-7}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 33. Replace raw-byte ItemInstance passthrough with structured dataclass {#33-replace-raw-byte-iteminstance-passthrough-with-structured-dataclass}
- Commit: [7edb52b4d444789cad0ee3c91f4c08594148f7e2](https://github.com/EndstoneMC/endweave/commit/7edb52b4d444789cad0ee3c91f4c08594148f7e2)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-20T14:43:02Z; committed: 2026-03-20T14:43:02Z
- Parents: bfcb5bf7db1c3221d122d6aa136f33f442890f6e
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types.py, tests/test_codec.py

Replaces opaque ItemInstance byte slicing with dataclass fields and symmetric codecs so later ID remapping can mutate values. Air short-circuits, optional stack net ID conditional, user data length-prefixed. Tests cover air, full/no-net-ID roundtrips, complete consumption and byte identity for writer-generated canonical values. Does not prove preservation of noncanonical varint or boolean encodings.

### Evidence limits {#source-acquisition-evidence-8}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 34. Add Google-style docstrings project-wide and update CLAUDE.md {#34-add-google-style-docstrings-project-wide-and-update-claude-md}
- Commit: [f2dcf756e756cca4382843bb4d5e82877b39c01a](https://github.com/EndstoneMC/endweave/commit/f2dcf756e756cca4382843bb4d5e82877b39c01a)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-20T14:54:12Z; committed: 2026-03-20T14:54:12Z
- Parents: 7edb52b4d444789cad0ee3c91f4c08594148f7e2
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CLAUDE.md, src/endstone_endweave/codec/reader.py, src/endstone_endweave/codec/types.py, src/endstone_endweave/codec/wrapper.py, src/endstone_endweave/codec/writer.py, src/endstone_endweave/connection.py, src/endstone_endweave/pipeline.py, src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/__init__.py, src/endstone_endweave/protocol/base.py, src/endstone_endweave/protocol/manager.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/login.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v944/handlers/voxel_shapes.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, src/endstone_endweave/protocol/versions.py, tools/fetch_protocol_docs.py, tools/generate_diff.py, tools/parse_protocol_docs.py

Project-wide Google-style Args/Returns/Attributes/Raises documentation and an explicit ViaVersion reference directive, with trivial one-line docstrings exempted. Full diff inspected: runtime statements unchanged apart from expansion of abstract method stubs to host docstrings. Useful contracts include wrapper read-removes/write-inserts, unread-tail forwarding, BFS shortest route and registration cache invalidation. Documentation is not independent correctness evidence: single-wrapper chaining, exact-length read claims without bounds enforcement, incorrect ContainerOpen direction and camera-spline append assumptions remain inherited implementation problems. No added tests or runtime results.

### Evidence limits {#source-acquisition-evidence-9}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 35. Align NBT types with ViaVersion design and make COMPOUND_TAG parsed {#35-align-nbt-types-with-viaversion-design-and-make-compoundtag-parsed}
- Commit: [007f3f83aa2d67f0839fe3da09ef1ddfedbb7ef9](https://github.com/EndstoneMC/endweave/commit/007f3f83aa2d67f0839fe3da09ef1ddfedbb7ef9)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-20T16:07:51Z; committed: 2026-03-20T16:07:51Z
- Parents: f2dcf756e756cca4382843bb4d5e82877b39c01a
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/reader.py, src/endstone_endweave/codec/types.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/item.py, src/endstone_endweave/codec/types/nbt.py, src/endstone_endweave/codec/types/primitives.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, tests/test_start_game.py

Replaces raw NBT slicing with parsed dataclass tag hierarchy, named/nameless root codecs and None-for-End semantics; splits primitive/item/NBT package. Adds actual LongArray tag12 support. Named read discards root name and writer emits empty name; duplicate compound names collapse in dict, so arbitrary byte preservation is lost even though canonical empty-root fixture roundtrips. Nameless codec retains Bedrock numeric/string encodings despite Java-format wording: naming convention inspiration is not full Java NBT compatibility. Read recursion guards depth512 but write has no depth guard; list element types are not validated against child tags. Fixes the16 fixture from9 to10 booleans and revises join-info assertions to compare gathering/non-gathering under outer true, resolving earlier test mismatch. No runtime tests executed.

### Evidence limits {#source-acquisition-evidence-10}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 36. Add PacketReader bounds checks and cancel packets on handler exceptions {#36-add-packetreader-bounds-checks-and-cancel-packets-on-handler-exceptions}
- Commit: [c4e455cd6a5d24a52f7d4eee30a6002b08532b1f](https://github.com/EndstoneMC/endweave/commit/c4e455cd6a5d24a52f7d4eee30a6002b08532b1f)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-20T16:31:21Z; committed: 2026-03-20T16:31:21Z
- Parents: 007f3f83aa2d67f0839fe3da09ef1ddfedbb7ef9
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/reader.py, src/endstone_endweave/pipeline.py, tests/test_codec.py, tests/test_pipeline.py

Hardens read_bytes/skip against negative and over-remaining lengths, and string reads against >131068 byte lengths, with explicit ValueError and tests. Handler exceptions now cancel both directions instead of allowing untranslated original bytes through. Tests install failing handlers and assert cancellation. Safety is local to handled translation; no demonstrated peer disconnect yet. String limit borrowed from ViaVersion, not independently validated as every Bedrock field's limit.

### Evidence limits {#source-acquisition-evidence-11}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 37. Add hatch-vcs dynamic versioning and modernize CI with uv {#37-add-hatch-vcs-dynamic-versioning-and-modernize-ci-with-uv}
- Commit: [ee013d7875c417964731a8436bc04c9bcd0691c9](https://github.com/EndstoneMC/endweave/commit/ee013d7875c417964731a8436bc04c9bcd0691c9)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-20T17:10:01Z; committed: 2026-03-20T17:10:01Z
- Parents: c4e455cd6a5d24a52f7d4eee30a6002b08532b1f
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: .github/workflows/build.yml, .github/workflows/publish.yml, .gitignore, pyproject.toml, uv.lock

Moves static package version to hatch-vcs generated _version.py; fetch-depth 0 preserves tags, uv standardizes installs/builds, matrix adds 3.14. Release publish depends on test job, uploads wheel to GitHub after PyPI. uv.lock dependency marker narrows typing-extensions from <3.13 to <3.11. Configuration read, not executed; GitHub-release event means a release can preexist failed tests despite publication gate.

### Evidence limits {#source-acquisition-evidence-12}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 38. Add rewriters for Data-Driven UI packets (333, 334) {#38-add-rewriters-for-data-driven-ui-packets-333-334}
- Commit: [5fca1a41ddacf387d64b83e0587d5fdb2e402dbe](https://github.com/EndstoneMC/endweave/commit/5fca1a41ddacf387d64b83e0587d5fdb2e402dbe)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T12:19:51Z; committed: 2026-03-21T12:20:12Z
- Parents: ee013d7875c417964731a8436bc04c9bcd0691c9
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/v924_to_v944/handlers/data_driven_ui.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py

Replaces prior cancellation for two UI packets with rewriters appending default zero uint32 FormID and DataInstanceID; close packet appends zero FormID. Code comments assert zero means close all, but no evidence/test establishes semantic equivalence here. Whole prior payload is copied before defaults; later optional-field corrections matter.

### Evidence limits {#source-acquisition-evidence-13}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 39. Add ConnectionState, type-keyed storage, and active flag to UserConnection {#39-add-connectionstate-type-keyed-storage-and-active-flag-to-userconnection}
- Commit: [ec23ae2e2c3336a46f474450bb11a69cc42e81d5](https://github.com/EndstoneMC/endweave/commit/ec23ae2e2c3336a46f474450bb11a69cc42e81d5)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T12:42:09Z; committed: 2026-03-21T12:42:09Z
- Parents: 5fca1a41ddacf387d64b83e0587d5fdb2e402dbe
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/connection.py, tests/test_connection.py

Adds HANDSHAKE/LOGIN/PLAY metadata, active/pending_disconnect flags and exact-type keyed connection storage with overwrite/get/remove semantics. Removal clears storage even if external references retain connection; tests exercise this explicit cleanup. State assignment tests do not prove correct event transition order, and flags are declarations here, not yet enforced lifecycle gates. ViaVersion attribution explicit.

### Evidence limits {#source-acquisition-evidence-14}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 40. Add Protocol.init/name and base protocol state transitions {#40-add-protocol-init-name-and-base-protocol-state-transitions}
- Commit: [1c6ce2e75ccb6c9baa7e7a966a0658ec419ccfb2](https://github.com/EndstoneMC/endweave/commit/1c6ce2e75ccb6c9baa7e7a966a0658ec419ccfb2)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T12:42:14Z; committed: 2026-03-21T12:42:14Z
- Parents: ec23ae2e2c3336a46f474450bb11a69cc42e81d5
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/__init__.py, src/endstone_endweave/protocol/base.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, tests/test_base_protocol.py

Adds protocol name for diagnostics and init hook declaration; base RequestNetworkSettings sets LOGIN, StartGame idempotently sets PLAY, Disconnect marks pending before attempted parse and lowers log severity. Tests exercise transitions and malformed disconnect flag. Message says init called once but actual invocation arrives42; this patch only defines hook. No guards enforce legal state transitions or prevent future processing solely from pending flag.

### Evidence limits {#source-acquisition-evidence-15}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 41. Add DebugHandler and InformativeException {#41-add-debughandler-and-informativeexception}
- Commit: [636b32bba4c92e3994216f2ea3b9977b93971d13](https://github.com/EndstoneMC/endweave/commit/636b32bba4c92e3994216f2ea3b9977b93971d13)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T12:42:21Z; committed: 2026-03-21T12:42:21Z
- Parents: 1c6ce2e75ccb6c9baa7e7a966a0658ec419ccfb2
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/debug.py, src/endstone_endweave/exception.py, tests/test_error_scenarios.py

Introduces enabled/filterable DebugHandler: empty packet-ID filter means all; pre defaults on and post off; structured name/decimal/hex IDs and unknown fallback. InformativeException retains ordered duplicate entries, bounded individual values (256 characters), numbered source names and causal chaining; cause text itself is unbounded. Tests cover filtering/config/error formatting and malformed packet cancellation. Pipeline context expectation anticipates the integration in 42, so this intermediate commit is not independently established passing.

### Evidence limits {#source-acquisition-evidence-16}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 42. Align pipeline with ViaVersion's ProtocolPipelineImpl {#42-align-pipeline-with-viaversion-s-protocolpipelineimpl}
- Commit: [40e685133e1450bfe0b572f097cf08ca10e8ad6b](https://github.com/EndstoneMC/endweave/commit/40e685133e1450bfe0b572f097cf08ca10e8ad6b)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T12:42:27Z; committed: 2026-03-21T12:42:27Z
- Parents: 636b32bba4c92e3994216f2ea3b9977b93971d13
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/config.toml, src/endstone_endweave/pipeline.py, src/endstone_endweave/plugin.py, tests/test_chain.py, tests/test_pipeline.py

Wires init hooks on chain resolution, caches chain then marks active; clientbound fast path now active-dependent. Adds filtered pre/post debug context and InformativeException fields (direction,packet,protocol,address,state), preserving fail-closed packet cancellation. Tests verify BFS order, init once and append-only multi-step handlers; they deliberately share wrapper and therefore do not prove downstream stages can reread upstream transformed fields. Matching connections still bypass clientbound base lifecycle in this version. Startup endpoints range is presentation, not proof every intermediate version supported.

### Evidence limits {#source-acquisition-evidence-17}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 43. Extract shared rewriter helpers to protocol/rewriter.py {#43-extract-shared-rewriter-helpers-to-protocol-rewriter-py}
- Commit: [2f6229368cf1b8592dc82245b75a42471411cb7a](https://github.com/EndstoneMC/endweave/commit/2f6229368cf1b8592dc82245b75a42471411cb7a)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T12:42:32Z; committed: 2026-03-21T12:42:32Z
- Parents: 40e685133e1450bfe0b572f097cf08ca10e8ad6b
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/reader.py, src/endstone_endweave/protocol/rewriter.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, tests/test_start_game.py

Moves position/inventory/structure helpers into shared protocol.rewriter without changing their field sequences; imports alias existing private names to minimize handler edits. Structure helper still embodies one conversion direction despite generic passthrough name. Remaining edits are formatting. This centralization enables later shared codecs; no independent wire change or test extension.

### Evidence limits {#source-acquisition-evidence-18}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 44. Add LevelSoundEvent remapping for v924 to v944 {#44-add-levelsoundevent-remapping-for-v924-to-v944}
- Commit: [e257eadfe76fc3c11a26264f1fcf8ab736f04860](https://github.com/EndstoneMC/endweave/commit/e257eadfe76fc3c11a26264f1fcf8ab736f04860)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T13:12:47Z; committed: 2026-03-21T13:12:47Z
- Parents: 2f6229368cf1b8592dc82245b75a42471411cb7a
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/rewriter.py, src/endstone_endweave/protocol/v924_to_v944/handlers/sound_event.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py

Introduces sound-ID shift at597 by2, including heartbeat metadata key126 in AddActor/AddItemActor/AddPlayer/SetActorData plus LevelSoundEvent. Shared ActorData dispatcher handles types0–8 and selectively remaps Int type2 only. Unknown metadata types silently consume no value, risking cursor desynchronization; type5 uses unnamed COMPOUND_TAG and type7 is not remapped until59 correction. Handlers manually walk spawn prefixes to reach metadata. No tests added. Removes explicit protocol name so default diagnostic naming applies.

### Evidence limits {#source-acquisition-evidence-19}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 45. Replace bytes_type with UUID constant {#45-replace-bytestype-with-uuid-constant}
- Commit: [cb408753eab01268d0b746b1299372cf401e39f1](https://github.com/EndstoneMC/endweave/commit/cb408753eab01268d0b746b1299372cf401e39f1)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T13:16:45Z; committed: 2026-03-21T13:16:45Z
- Parents: e257eadfe76fc3c11a26264f1fcf8ab736f04860
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/primitives.py, src/endstone_endweave/protocol/v924_to_v944/handlers/sound_event.py, tests/test_wrapper.py

Replaces generic bytes_type factory with named UUID singleton of 16 raw bytes and updates reexports, AddPlayer field use and roundtrip test. Narrows API to actual need without yet modelling UUID component endianness; later MceUUID change should not be mistaken as identical representation policy.

### Evidence limits {#source-acquisition-evidence-20}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 46. Standardize field comments to match v924_packets.json {#46-standardize-field-comments-to-match-v924packets-json}
- Commit: [e913a03f94e0fdbadec4688c85bd52b2d84f461f](https://github.com/EndstoneMC/endweave/commit/e913a03f94e0fdbadec4688c85bd52b2d84f461f)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T13:56:27Z; committed: 2026-03-21T13:56:27Z
- Parents: cb408753eab01268d0b746b1299372cf401e39f1
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CLAUDE.md, src/endstone_endweave/protocol/rewriter.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/data_driven_ui.py, src/endstone_endweave/protocol/v924_to_v944/handlers/login.py, src/endstone_endweave/protocol/v924_to_v944/handlers/sound_event.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v944/handlers/voxel_shapes.py

Comment and docstring standardization ties wrapper field names to generated v924 schema, using v944 for added fields. All hunks inspected: callable order and wire types unchanged. Removes redundant layout prose, preserves meaningful field-level provenance, but incorrect inherited ContainerOpen direction, camera suffix and StartGame outer-join prose remain; schema-consistent names do not validate framing.

### Evidence limits {#source-acquisition-evidence-21}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 47. Fix generic type hints in PacketWrapper and standardize TypeVar naming {#47-fix-generic-type-hints-in-packetwrapper-and-standardize-typevar-naming}
- Commit: [202157c76b587dc04fc2ec6f1b05ec2d46a313c7](https://github.com/EndstoneMC/endweave/commit/202157c76b587dc04fc2ec6f1b05ec2d46a313c7)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T14:04:13Z; committed: 2026-03-21T14:04:13Z
- Parents: e913a03f94e0fdbadec4688c85bd52b2d84f461f
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/codec/types/primitives.py, src/endstone_endweave/codec/wrapper.py, src/endstone_endweave/connection.py, src/endstone_endweave/protocol/rewriter.py

Propagates Type[T] through wrapper read/write/passthrough, changes heterogeneous actor types to Type[Any] and remapper input to Mapping for variance. Static typing improvement preserves runtime operations; no evidence of type checker execution.

### Evidence limits {#source-acquisition-evidence-22}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 48. Add bStats metrics integration and changelog rule {#48-add-bstats-metrics-integration-and-changelog-rule}
- Commit: [2b912b0484e7f9ad903f57073ced386f6a359a1d](https://github.com/EndstoneMC/endweave/commit/2b912b0484e7f9ad903f57073ced386f6a359a1d)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T14:08:44Z; committed: 2026-03-21T14:08:44Z
- Parents: 202157c76b587dc04fc2ec6f1b05ec2d46a313c7
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CLAUDE.md, src/endstone_endweave/plugin.py

Initializes bStats service30345 and introduces changelog convention in historical guidance. Runtime telemetry behavior added, not mere docs; no network calls executed in review.

### Evidence limits {#source-acquisition-evidence-23}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 49. Store Metrics instance on plugin for lifecycle management {#49-store-metrics-instance-on-plugin-for-lifecycle-management}
- Commit: [b5e33d30c64df06c6734882cc5c9c07a86516ced](https://github.com/EndstoneMC/endweave/commit/b5e33d30c64df06c6734882cc5c9c07a86516ced)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T14:09:14Z; committed: 2026-03-21T14:09:14Z
- Parents: 2b912b0484e7f9ad903f57073ced386f6a359a1d
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/plugin.py

Retains Metrics object as plugin field rather than discarded constructor result. Intent says lifecycle management, but this patch alone adds no shutdown. Use as ownership prerequisite, not completed cleanup.

### Evidence limits {#source-acquisition-evidence-24}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 50. Add CHANGELOG.md and rewrite README for clarity {#50-add-changelog-md-and-rewrite-readme-for-clarity}
- Commit: [b01480dbce0fc68b7417c68230257377d541e458](https://github.com/EndstoneMC/endweave/commit/b01480dbce0fc68b7417c68230257377d541e458)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T15:28:48Z; committed: 2026-03-21T15:28:48Z
- Parents: b5e33d30c64df06c6734882cc5c9c07a86516ced
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, README.md

Introduces Keep a Changelog history and simplifies README for users. Separates unreleased sound/UI/metrics/debug changes from initial0.1.0 feature claims; later55 corrects date. No runtime evidence from release-note assertions.

### Evidence limits {#source-acquisition-evidence-25}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.
