<!-- retrieval: {"source_ids":["public:commit:02cffddd96243d33f532fec75a71d5da97894c17","public:commit:102a723fd8e8c03f72084fe31b549011486add79","public:commit:1039408c4e83670f34319680d5338a8bc8922a1f","public:commit:151f7d9f1e48703a3e843d30e41faa94c63c4900","public:commit:261d16294a115e2ca38b92c0f1ff2d95fc157343","public:commit:2a5f86d7696e57e438d0bb1472e306684cd37efb","public:commit:43ac355288ec51e965d5e50b50b92b81b90192c5","public:commit:4c6249a141794160b0c8659de9f4e2bfc27d87d6","public:commit:7166200b6748b4c1e4befa7839efba9de53b72fd","public:commit:787b3aafb468456b723998e6c0b02da1609d8753","public:commit:8d4a7c37f0b8e55c5d9dbf730dfeb98ca6194866","public:commit:9084e6430171006225edcf3d218a4713b901f7d2","public:commit:9f1a7bc69f4e2515293a9c5da2d15378e55b3355","public:commit:a54e3714a9fd16d7fb2bd30b4f307d2f3b9a810c","public:commit:a9566bd97239dd422636e4f17f668b8ef5e713e1","public:commit:af2b3fed58fb712de50d99c60f743a6691203352","public:commit:b9d8af397e271dc321af2ca49a71bca603ed8b2a","public:commit:c8f9ae2e524206a1ddd83fb8c4f932cd691ceadd","public:commit:d50d746fa509fa6423c70be216206db90f99658e","public:commit:d6bc91546f0a0f153ff8dd06f699774761946bc7","public:commit:d77c31829a6ea3ce2ebd595b14e0c086da507c93","public:commit:e23905f8f2389ab3675707da7e1d59d01b3f3d74","public:commit:ed1d81b2e0e30c35f847f5840c1e721e3294e914","public:commit:fcfe21e71ab1c72c34d7c20f1f5138e1d96a744e","public:commit:ff88bb8bf9403dc5ce5af066fded2901e983c9b3"],"source_type":"public","date":"2026-03-21..2026-03-25","topics":["lifetime","concurrency","testing","build","performance","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endweave-commit-dossiers-assignment-ordinals-51-75"></a>
# Endweave commit dossiers: assignment ordinals 51–75 {#endweave-commit-dossiers-assignment-ordinals-51-75}

Static source review. Assignment ordinals are identifiers, not a topological ordering. Exact parents below define ancestry. Acquired but unread entries remain open. No upstream code, tests or workflows executed. Generated data must receive a separate structural audit before closure.

## 51. Refactor docstrings to See Also references, add ruff config, lint {#51-refactor-docstrings-to-see-also-references-add-ruff-config-lint}
- Commit: [af2b3fed58fb712de50d99c60f743a6691203352](https://github.com/EndstoneMC/endweave/commit/af2b3fed58fb712de50d99c60f743a6691203352)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T15:39:04Z; committed: 2026-03-21T15:39:04Z
- Parents: b01480dbce0fc68b7417c68230257377d541e458
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: README.md, pyproject.toml, src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/reader.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/item.py, src/endstone_endweave/codec/types/nbt.py, src/endstone_endweave/codec/types/primitives.py, src/endstone_endweave/codec/wrapper.py, src/endstone_endweave/connection.py, src/endstone_endweave/debug.py, src/endstone_endweave/exception.py, src/endstone_endweave/pipeline.py, src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/__init__.py, src/endstone_endweave/protocol/base.py, src/endstone_endweave/protocol/direction.py, src/endstone_endweave/protocol/manager.py, src/endstone_endweave/protocol/rewriter.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/login.py, src/endstone_endweave/protocol/v924_to_v944/handlers/sound_event.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, src/endstone_endweave/protocol/versions.py, tests/test_base_protocol.py, tests/test_block_pos.py, tests/test_chain.py, tests/test_codec.py, tests/test_connection.py, tests/test_error_scenarios.py, tests/test_login_rewriter.py, tests/test_pipeline.py, tests/test_start_game.py, tests/test_wrapper.py, tools/fetch_protocol_docs.py, tools/generate_diff.py, tools/parse_protocol_docs.py

Adds Ruff I/E/F rules at line length120, reorganizes imports/formatting across source/tests/tools, and replaces broad ViaVersion-alignment prose with qualified Java See Also references. No wire-algorithm change found in full patch. References document inspiration rather than proven equivalence: wrapper points to api.type.Types and pipeline still describes single-wrapper composition. Test changes are mechanical, not new evidence of compatibility.

### Evidence limits {#source-acquisition-evidence}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 52. Pythonic refactoring: properties, type hints, and naming {#52-pythonic-refactoring-properties-type-hints-and-naming}
- Commit: [e23905f8f2389ab3675707da7e1d59d01b3f3d74](https://github.com/EndstoneMC/endweave/commit/e23905f8f2389ab3675707da7e1d59d01b3f3d74)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T15:58:42Z; committed: 2026-03-21T15:58:42Z
- Parents: af2b3fed58fb712de50d99c60f743a6691203352
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: pyproject.toml, src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/reader.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/primitives.py, src/endstone_endweave/codec/wrapper.py, src/endstone_endweave/codec/writer.py, src/endstone_endweave/debug.py, src/endstone_endweave/exception.py, src/endstone_endweave/pipeline.py, src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/__init__.py, src/endstone_endweave/protocol/base.py, src/endstone_endweave/protocol/manager.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/login.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, tests/test_block_pos.py, tests/test_codec.py, tests/test_error_scenarios.py, tests/test_start_game.py, tests/test_wrapper.py

Converts no-argument state getters to properties throughout source/tests, renames fixed signed64 codec LONG_LE/read_long_le/write_long_le to INT64_LE equivalents, and aligns the structure helper alias. Adds strict mypy with ignore_missing_imports; struct results receive explicit annotations, external decorators/config assignments retain targeted ignores, debug config flags now bool-coerced. These are API-breaking names without aliases, although wire encodings stay unchanged. get_max_client_version uses list/max and loses prior deduplication, potentially repeats cached lookups but preserves maximum semantics. Claimed strict-mode success is commit narrative only; no checker executed here.

### Evidence limits {#source-acquisition-evidence-2}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 53. Release v0.2.0 {#53-release-v0-2-0}
- Commit: [4c6249a141794160b0c8659de9f4e2bfc27d87d6](https://github.com/EndstoneMC/endweave/commit/4c6249a141794160b0c8659de9f4e2bfc27d87d6)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T15:59:59Z; committed: 2026-03-21T15:59:59Z
- Parents: e23905f8f2389ab3675707da7e1d59d01b3f3d74
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md

Adds0.2.0 dated release heading only; no independent implementation lesson.

### Evidence limits {#source-acquisition-evidence-3}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 54. Add Dependabot for GitHub Actions and uv {#54-add-dependabot-for-github-actions-and-uv}
- Commit: [a54e3714a9fd16d7fb2bd30b4f307d2f3b9a810c](https://github.com/EndstoneMC/endweave/commit/a54e3714a9fd16d7fb2bd30b4f307d2f3b9a810c)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T16:02:10Z; committed: 2026-03-21T16:02:10Z
- Parents: 4c6249a141794160b0c8659de9f4e2bfc27d87d6
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: .github/dependabot.yml

Adds weekly Dependabot updates for GitHub Actions and uv at repository root. Configuration does not show bots actually ran or updates were safe/merged.

### Evidence limits {#source-acquisition-evidence-4}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 55. Update CHANGELOG for corrected 0.1.0 release date {#55-update-changelog-for-corrected-0-1-0-release-date}
- Commit: [151f7d9f1e48703a3e843d30e41faa94c63c4900](https://github.com/EndstoneMC/endweave/commit/151f7d9f1e48703a3e843d30e41faa94c63c4900)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T16:05:33Z; committed: 2026-03-21T16:05:33Z
- Parents: a54e3714a9fd16d7fb2bd30b4f307d2f3b9a810c
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md

Corrects0.1.0 date March21→March20,2026; documentation correction only.

### Evidence limits {#source-acquisition-evidence-5}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 56. Production readiness: CI linting, py.typed, and CLAUDE.md overhaul {#56-production-readiness-ci-linting-py-typed-and-claude-md-overhaul}
- Commit: [ff88bb8bf9403dc5ce5af066fded2901e983c9b3](https://github.com/EndstoneMC/endweave/commit/ff88bb8bf9403dc5ce5af066fded2901e983c9b3)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T16:18:27Z; committed: 2026-03-21T16:18:27Z
- Parents: 779177c7bd0e13a00cbd4d35ff1f0b6d00358b63
- Reading: non-generated diffs read; generated lock artifacts structurally audited
- Changed files: .github/workflows/build.yml, CLAUDE.md, pyproject.toml, src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/protocol/__init__.py, src/endstone_endweave/protocol/manager.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/py.typed, tests/test_wrapper.py, uv.lock

Adds Ruff source/tests and strict mypy source checks after existing pytest CI, declares mypy/ruff dev extras, adds empty py.typed for PEP561 consumers, sorts exports and explicitly exports Protocol/PacketHandler. Beta classifier is a release claim rather than demonstrated production readiness. CLAUDE architecture/tooling guidance is updated, including properties, private TypeVars and precise ViaVersion references. All non-artifact lock edits read: adds mypy1.19.1, ruff0.15.7 and librt0.8.1/mypy-extensions1.1.0/pathspec1.0.4; 136 artifact URL/hash records were statically checked. Distribution literal integrity/authenticity not independently verified. No CI or type-check execution.

### Evidence limits {#source-acquisition-evidence-6}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 57. Exclude auto-generated _version.py from ruff {#57-exclude-auto-generated-version-py-from-ruff}
- Commit: [1039408c4e83670f34319680d5338a8bc8922a1f](https://github.com/EndstoneMC/endweave/commit/1039408c4e83670f34319680d5338a8bc8922a1f)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T16:21:51Z; committed: 2026-03-21T16:21:51Z
- Parents: ff88bb8bf9403dc5ce5af066fded2901e983c9b3
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: pyproject.toml

Excludes generated version module from Ruff. Generated-code exception is narrowly scoped; no broader lint preference inferred.

### Evidence limits {#source-acquisition-evidence-7}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 58. Change license from MIT to Apache 2.0 {#58-change-license-from-mit-to-apache-2-0}
- Commit: [261d16294a115e2ca38b92c0f1ff2d95fc157343](https://github.com/EndstoneMC/endweave/commit/261d16294a115e2ca38b92c0f1ff2d95fc157343)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T16:34:08Z; committed: 2026-03-21T16:34:08Z
- Parents: 1039408c4e83670f34319680d5338a8bc8922a1f
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: LICENSE, README.md, pyproject.toml

Replaces MIT license text with Apache2.0 terms and Endstone2025 notice, synchronizing README and package classifier. Full replacement read. No implementation change or stated rationale; preserve this licensing boundary when tracing earlier code, without treating the change as an engineering-performance preference or independently adjudicating contributor rights.

### Evidence limits {#source-acquisition-evidence-8}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 59. Fix ActorData CompoundTag parsing and Int64 remapping {#59-fix-actordata-compoundtag-parsing-and-int64-remapping}
- Commit: [c8f9ae2e524206a1ddd83fb8c4f932cd691ceadd](https://github.com/EndstoneMC/endweave/commit/c8f9ae2e524206a1ddd83fb8c4f932cd691ceadd)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T19:35:04Z; committed: 2026-03-21T19:35:04Z
- Parents: 261d16294a115e2ca38b92c0f1ff2d95fc157343
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/rewriter.py

Uses named rather than nameless NBT CompoundTag for ActorData type5; commit explains earlier parser desync obscured heartbeat sound entry. Remapping extends from Int to Int64 while selecting corresponding wire codec. Also adds Endstone<=0.11.2 metrics polyfill using private _description. No added regression test; upstream private attribute compatibility remains coupling.

### Evidence limits {#source-acquisition-evidence-9}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 60. Add docstring to EndweaveMetrics polyfill class {#60-add-docstring-to-endweavemetrics-polyfill-class}
- Commit: [d50d746fa509fa6423c70be216206db90f99658e](https://github.com/EndstoneMC/endweave/commit/d50d746fa509fa6423c70be216206db90f99658e)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T20:06:09Z; committed: 2026-03-21T20:06:09Z
- Parents: c8f9ae2e524206a1ddd83fb8c4f932cd691ceadd
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/plugin.py

Despite docstring-only title, adds platform-data override: invokes superclass, removes minecraftVersion, fills bukkitVersion/bukkitName when absent. Meaningful metrics schema compatibility change, not noise. Important counterexample to classifying by title.

### Evidence limits {#source-acquisition-evidence-10}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 61. Release 0.2.1 {#61-release-0-2-1}
- Commit: [43ac355288ec51e965d5e50b50b92b81b90192c5](https://github.com/EndstoneMC/endweave/commit/43ac355288ec51e965d5e50b50b92b81b90192c5)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T20:10:01Z; committed: 2026-03-21T20:10:01Z
- Parents: d50d746fa509fa6423c70be216206db90f99658e
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/rewriter.py

0.2.1 release notes cover NBT/int64, metrics, license; remaining code diff is import/blank-line formatting. Does not independently validate reported fixes.

### Evidence limits {#source-acquisition-evidence-11}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 62. Fix mypy strict error in EndweaveMetrics.append_service_data {#62-fix-mypy-strict-error-in-endweavemetrics-appendservicedata}
- Commit: [b9d8af397e271dc321af2ca49a71bca603ed8b2a](https://github.com/EndstoneMC/endweave/commit/b9d8af397e271dc321af2ca49a71bca603ed8b2a)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T20:12:18Z; committed: 2026-03-21T20:12:18Z
- Parents: 43ac355288ec51e965d5e50b50b92b81b90192c5
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/plugin.py

Guards optional plugin description before reporting version. Advertised strict-mypy repair also avoids runtime None dereference; absent description omits field.

### Evidence limits {#source-acquisition-evidence-12}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 63. Normalize bStats OS architecture across platforms {#63-normalize-bstats-os-architecture-across-platforms}
- Commit: [7166200b6748b4c1e4befa7839efba9de53b72fd](https://github.com/EndstoneMC/endweave/commit/7166200b6748b4c1e4befa7839efba9de53b72fd)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-21T21:20:24Z; committed: 2026-03-21T21:21:18Z
- Parents: b9d8af397e271dc321af2ca49a71bca603ed8b2a
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, src/endstone_endweave/plugin.py

Normalizes platform.machine lowercase and x86_64→amd64 in metrics; changelog records behavior. Other architectures passed through lowercase without new mapping.

### Evidence limits {#source-acquisition-evidence-13}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 64. Fix ContainerOpen registered as serverbound instead of clientbound {#64-fix-containeropen-registered-as-serverbound-instead-of-clientbound}
- Commit: [9f1a7bc69f4e2515293a9c5da2d15378e55b3355](https://github.com/EndstoneMC/endweave/commit/9f1a7bc69f4e2515293a9c5da2d15378e55b3355)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-23T14:45:02Z; committed: 2026-03-23T14:45:02Z
- Parents: 7166200b6748b4c1e4befa7839efba9de53b72fd
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, tests/test_block_pos.py

ContainerOpen was wrongly registered serverbound and converted in wrong direction. Moves to clientbound and NetworkBlockPos→BlockPos; relocates test and reverses fixture encoding while preserving trailing entity ID. Demonstrates unit test matching a wrong assumption does not verify packet direction; no registration-level regression added here.

### Evidence limits {#source-acquisition-evidence-14}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 65. Shorten dev version by dropping local segment {#65-shorten-dev-version-by-dropping-local-segment}
- Commit: [d77c31829a6ea3ce2ebd595b14e0c086da507c93](https://github.com/EndstoneMC/endweave/commit/d77c31829a6ea3ce2ebd595b14e0c086da507c93)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-23T14:47:55Z; committed: 2026-03-23T14:47:55Z
- Parents: 9f1a7bc69f4e2515293a9c5da2d15378e55b3355
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: pyproject.toml

Drops VCS local version segment via no-local-version, yielding shorter dev versions but losing hash/date in published display. No runtime translator change.

### Evidence limits {#source-acquisition-evidence-15}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 66. Add automated release workflow {#66-add-automated-release-workflow}
- Commit: [d6bc91546f0a0f153ff8dd06f699774761946bc7](https://github.com/EndstoneMC/endweave/commit/d6bc91546f0a0f153ff8dd06f699774761946bc7)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-23T14:59:25Z; committed: 2026-03-23T14:59:25Z
- Parents: d77c31829a6ea3ce2ebd595b14e0c086da507c93
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: .github/workflows/publish.yml, .github/workflows/release.yml, CHANGELOG.md

Introduces manually dispatched release version/dry-run workflow replacing release-event publication. Validates numeric X.Y.Z and existing tags, extracts Unreleased notes, commits changelog and lightweight tag, pushes main, creates GitHub release, then tests tagged source and publishes via OIDC environment plus wheel upload. Static defects/risks: --follow-tags does not normally push the lightweight git tag created here, and release creation precedes test/build validation so failures can leave public partial releases. Version is interpolated directly into shell before regex validation. Dry run only previews notes and skips downstream jobs; it is not a build rehearsal. No workflow run or release outcome verified.

### Evidence limits {#source-acquisition-evidence-16}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 67. Fix release workflow pushing lightweight tags {#67-fix-release-workflow-pushing-lightweight-tags}
- Commit: [2a5f86d7696e57e438d0bb1472e306684cd37efb](https://github.com/EndstoneMC/endweave/commit/2a5f86d7696e57e438d0bb1472e306684cd37efb)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-23T15:03:57Z; committed: 2026-03-23T15:03:57Z
- Parents: d6bc91546f0a0f153ff8dd06f699774761946bc7
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: .github/workflows/release.yml

Replaces follow-tags with explicit branch/tag pushes because created tags are lightweight and follow-tags only sends annotated tags. Both operations still non-atomic here; later220 changes that. No push executed.

### Evidence limits {#source-acquisition-evidence-17}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 68. Fix CameraSpline handler breaking login with experimental_creator_cameras {#68-fix-cameraspline-handler-breaking-login-with-experimentalcreatorcameras}
- Commit: [787b3aafb468456b723998e6c0b02da1609d8753](https://github.com/EndstoneMC/endweave/commit/787b3aafb468456b723998e6c0b02da1609d8753)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-24T19:05:56Z; committed: 2026-03-24T19:07:44Z
- Parents: fb1b4ca20ef845fee6a9a3862f69612b0e539e8a
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/camera.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py, tests/test_block_pos.py

Repairs CameraSpline framing by appending empty identifier and false loadFromJson to each spline, not to the entire payload. Moves camera rewriting into dedicated module. Zero-count regression fixture now uses actual empty-array framing and verifies no appended bytes. Populated spline coverage is absent; spline type/easing are still decoded as strings until 69. Cloudburst citation is historical rationale, not an independently verified specification.

### Evidence limits {#source-acquisition-evidence-18}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 69. Add CameraInstruction handler and VEC2/VEC3 codec types {#69-add-camerainstruction-handler-and-vec2-vec3-codec-types}
- Commit: [02cffddd96243d33f532fec75a71d5da97894c17](https://github.com/EndstoneMC/endweave/commit/02cffddd96243d33f532fec75a71d5da97894c17)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-24T19:52:10Z; committed: 2026-03-24T19:52:10Z
- Parents: 787b3aafb468456b723998e6c0b02da1609d8753
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/primitives.py, src/endstone_endweave/plugin.py, src/endstone_endweave/protocol/v924_to_v944/handlers/camera.py, src/endstone_endweave/protocol/v924_to_v944/protocol.py

Introduces reusable little-endian VEC2/VEC3 tuples and corrects CameraSpline spline-type to BYTE and easing to INT_LE. CameraInstruction conditionally parses Set, Clear, Fade, Target, RemoveTarget, FOV, Spline, Attach and Detach fields, preserves Set removeIgnoreStartingValuesComponent boolean and inserts identifier/loadFromJson within present Spline. Optional flags drive reads; absent fields must consume no payload. Registers the handler explicitly. Full diff inspected; no new populated-branch regression tests accompany this broad framing change.

### Evidence limits {#source-acquisition-evidence-19}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 70. Fix block interactions failing at Y < 0 (#3) {#70-fix-block-interactions-failing-at-y-0-3}
- Commit: [8d4a7c37f0b8e55c5d9dbf730dfeb98ca6194866](https://github.com/EndstoneMC/endweave/commit/8d4a7c37f0b8e55c5d9dbf730dfeb98ca6194866)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-25T16:35:51Z; committed: 2026-03-25T16:35:51Z
- Parents: 379dd73e0e52bdaa669f270095a1f741def3b196
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, src/endstone_endweave/codec/types/primitives.py, tests/test_block_pos.py

Fixes unsigned-wire/signed-domain distinction for NetworkBlockPos Y by subtracting2^32 when high bit set. Preserves same bytes on roundtrip; tests cover -1,-10,-64, both conversion directions and chest position with trailing entity ID. Links issue3 in message; peer discussion not read here. Claim all18 packets benefit follows shared primitive, not18 executed integration tests.

### Evidence limits {#source-acquisition-evidence-20}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 71. Add PacketWrapper.map() for cross-type field conversion {#71-add-packetwrapper-map-for-cross-type-field-conversion}
- Commit: [fcfe21e71ab1c72c34d7c20f1f5138e1d96a744e](https://github.com/EndstoneMC/endweave/commit/fcfe21e71ab1c72c34d7c20f1f5138e1d96a744e)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-25T16:50:28Z; committed: 2026-03-25T16:50:28Z
- Parents: a5e051a8ed4354e7b993d7f49cabcf5f9633cd0c
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, src/endstone_endweave/codec/wrapper.py, src/endstone_endweave/protocol/rewriter.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, tests/test_wrapper.py

Adds PacketWrapper.map(old_type,new_type), returning the decoded value after writing its new representation. Replaces local block-position helpers across ordinary, structure and inventory handlers. Unit test converts signed varint42 to little-endian int while retaining unread FF tail. Generic type parameter assumes the two codecs share a semantic value domain; map does not itself provide arbitrary value conversion.

### Evidence limits {#source-acquisition-evidence-21}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 72. Add compound Type objects and PacketWrapper.map() {#72-add-compound-type-objects-and-packetwrapper-map}
- Commit: [a9566bd97239dd422636e4f17f668b8ef5e713e1](https://github.com/EndstoneMC/endweave/commit/a9566bd97239dd422636e4f17f668b8ef5e713e1)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-25T17:32:38Z; committed: 2026-03-25T17:32:38Z
- Parents: fcfe21e71ab1c72c34d7c20f1f5138e1d96a744e
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/camera.py, src/endstone_endweave/codec/types/inventory.py, src/endstone_endweave/codec/types/structure.py, src/endstone_endweave/protocol/rewriter.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/camera.py

Despite repeating the preceding map feature in its title, actual change extracts shared semantic dataclasses/codecs for CameraSpline, InventoryAction and StructureSettings. Versioned codecs vary position encoding and append spline identifier/load flag while retaining common order. Inventory source IDs0/99999 carry window IDs and2 carries flags; required optional members are enforced by assertions. Handler helper duplication becomes compound map/passthrough operations. This centralizes layout knowledge but materializes objects/lists; no performance evidence or new tests. No pipeline cursor fix occurs here.

### Evidence limits {#source-acquisition-evidence-22}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 73. Add OptionalType, ActorData compound type, and simplify handlers {#73-add-optionaltype-actordata-compound-type-and-simplify-handlers}
- Commit: [9084e6430171006225edcf3d218a4713b901f7d2](https://github.com/EndstoneMC/endweave/commit/9084e6430171006225edcf3d218a4713b901f7d2)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-25T17:57:33Z; committed: 2026-03-25T17:57:33Z
- Parents: a9566bd97239dd422636e4f17f668b8ef5e713e1
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/actor_data.py, src/endstone_endweave/codec/types/primitives.py, src/endstone_endweave/codec/types/structure.py, src/endstone_endweave/protocol/rewriter.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/sound_event.py, src/endstone_endweave/protocol/v924_to_v944/handlers/start_game.py, src/endstone_endweave/protocol/versions.py

Introduces OptionalType with None as absence and bool prefix; false inner BOOL remains present, avoiding truthiness conflation. ActorData becomes materialized entries with type-dispatch read/write, preserving type2/type7 heartbeat remapping and namedNBT correction. Unknown type now raises KeyError rather than silently consuming nothing in old helper, a meaningful safety change. Removes shared rewriter after its responsibilities migrate, and replaces repeated float fields with VEC2/VEC3. No new tests.

### Evidence limits {#source-acquisition-evidence-23}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 74. Add ArrayType and use OptionalType/ArrayType in handlers {#74-add-arraytype-and-use-optionaltype-arraytype-in-handlers}
- Commit: [102a723fd8e8c03f72084fe31b549011486add79](https://github.com/EndstoneMC/endweave/commit/102a723fd8e8c03f72084fe31b549011486add79)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-25T18:09:34Z; committed: 2026-03-25T18:09:34Z
- Parents: 9084e6430171006225edcf3d218a4713b901f7d2
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: CHANGELOG.md, src/endstone_endweave/codec/__init__.py, src/endstone_endweave/codec/types/__init__.py, src/endstone_endweave/codec/types/primitives.py, src/endstone_endweave/protocol/v924_to_v944/handlers/block_pos.py, src/endstone_endweave/protocol/v924_to_v944/handlers/camera.py

Adds generic ArrayType with unsigned-varint count and no explicit resource/count ceiling, then applies it to Map IDs. Registers optional bool/vector singletons and simplifies11 camera optional fields while preserving presence versus false. Dynamic OptionalType(INT64_LE) remains created per invocation. Full diff shows no pipeline composition change and no new tests.

### Evidence limits {#source-acquisition-evidence-24}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.

## 75. fix: handle case-insensitive Mojang branch names in fetch script {#75-fix-handle-case-insensitive-mojang-branch-names-in-fetch-script}
- Commit: [ed1d81b2e0e30c35f847f5840c1e721e3294e914](https://github.com/EndstoneMC/endweave/commit/ed1d81b2e0e30c35f847f5840c1e721e3294e914)
- Author: Vincent; GitHub-linked attribution wu-vincent, not blanket ownership of imported code.
- Authored: 2026-03-25T21:16:03Z; committed: 2026-03-25T21:16:03Z
- Parents: b925a7f8efffdb1aadcbd9cf9ba3f56d5e4a4499
- Reading: complete captured message and all parent diffs read; static synthesis below
- Changed files: tools/fetch_protocol_docs.py

Fetch retries uppercase branch suffix after clone failure to accommodate Mojang casing. Same temp target and subprocess array used, shell-free. Any clone failure triggers retry, so message branch-not-found can misdiagnose transport failures; not full case-insensitive lookup. No network fetch executed.

### Evidence limits {#source-acquisition-evidence-25}
Surrounding unchanged source beyond visible diff context has not been universally read; findings are scoped to changed implementation and explicitly traced evolution. Runtime compatibility remains unverified.
