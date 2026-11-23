<!-- retrieval: {"source_ids":["public:commit:09e532cf6e95a910fad867a881b08cc012eb0f89","public:commit:0f4b6b2e39d7372e7b20127fed9ed74192e2ec72","public:commit:10d3ab1ced055fa80ac5752427665a141583c248","public:commit:19e9203b3eb2d17c51837e12cc94688190d7163e","public:commit:202857a9c1c7e1866db22b655813063a0ae36888","public:commit:39637ffc6f754b5692f5ab9728df7ab455eae7c6","public:commit:3ddd4d80092450b68787de8f3743dda9a82d0871","public:commit:4326417f7cacd1fd5cd77534b20eab77e7bafc25","public:commit:44040ecb86a8b61dd6eba7411cc04d50c82d5316","public:commit:4b190c22a2e256db2e7b04ab5c977a2f9cf51116","public:commit:5114938dfaf6bb6806fd7cd5338e0bfc2471188f","public:commit:5aa7780d6ccd2b85268aea1f5714997a54a9b239","public:commit:6b35b4685a2d2b4008fd455e07ca004ec50c504c","public:commit:84bdb837c1a15673fb06c11280c0c5f1d6b28338","public:commit:867ff6590321f62d7ee27e0b8689632a9e6e3c8b","public:commit:89a9452ce7e29358356eb3684bfcd3b9d7ceaf4a","public:commit:8d2f9cac8e916dce4dc325850386588bec8f4c68","public:commit:9fe937885b294502954981e4d098acbf1caadc2a","public:commit:a0b1a16480d96e0103170a50e84ec1d3ca998981","public:commit:a300a054db52817a42c6221651c46c00b4bf796f","public:commit:a9226f4f2333c2e10824c957bf35f3c7fec62874","public:commit:ad2d546e094453f2f4247cf1552ee447220246af","public:commit:ba508b42b7cce2428f85f0b451a329e4fe8a3156","public:commit:bc6cf7102eff43d5c1e3627ee3d793d5c16674a2","public:commit:c212c536866c969a2d15de5c81989b59616ffd16","public:commit:c7ef6a7d1eac803569312911986d859a3a2ec1ce","public:commit:d43065cf3882d625d1f7ee8cbad53566915846f8","public:commit:d9d5d378ad0bffd24875d6bbff5fb6a68969a9cc","public:commit:eb761a0aca0f4aa689f29da6636f863fc2bbaf5c","public:commit:f1de73e2e2f346d925990f805d3e4d1d87970c5c","public:commit:f3c4e704ed4ca9638b9f7067f38bdf43210635df","public:commit:f88ee6a03763f0eb7185b04a801ac495e467d86d"],"source_type":"public","date":"2026-07-11..2026-07-28","topics":["lifetime","ffi","testing","build","diagnosis","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Additional per-source analysis and source qualifications {#additional-per-source-causal-analysis}

These supplemental notes record commit-specific engineering observations and evidence limits alongside the main source analyses. Public commit links identify the inspected revisions; no runtime result is independently verified here. A repeated review-scope qualification describes a limit of the analysis, not necessarily a change made by every listed commit.

<a id="commit-3ddd4d80092450b68787de8f3743dda9a82d0871"></a>
## Rewrite the compiler from scratch, protoc-faithful and minimal {#commit-3ddd4d80092450b68787de8f3743dda9a82d0871}

Semantic synthesis / alternatives: The removed broad framework is the actual prior alternative. #32/#33/#34 refine ownership and boundaries further; #34 reverses the terminology change in #4.

### Provenance {#commit-3ddd4d80092450b68787de8f3743dda9a82d0871-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/3ddd4d80092450b68787de8f3743dda9a82d0871

Source date: 2026-07-11T16:11:12Z


<a id="commit-89a9452ce7e29358356eb3684bfcd3b9d7ceaf4a"></a>
## refactor(cpp): rename MessageGenerator -> ClassGenerator {#commit-89a9452ce7e29358356eb3684bfcd3b9d7ceaf4a}

Semantic synthesis / rationale: Message says class is domain-faithful; #34 later explicitly chooses protoc correspondence instead. Preserve reversal, not a universal naming preference.

### Provenance {#commit-89a9452ce7e29358356eb3684bfcd3b9d7ceaf4a-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/89a9452ce7e29358356eb3684bfcd3b9d7ceaf4a

Source date: 2026-07-11T16:21:39Z


<a id="commit-a9226f4f2333c2e10824c957bf35f3c7fec62874"></a>
## feat(cpp): compute includes on demand from generated types {#commit-a9226f4f2333c2e10824c957bf35f3c7fec62874}

Semantic synthesis / limits: This is the intermediate include architecture; #6 splits body-only dependencies and #7 moves ownership to emission sites.

Limits: This is the intermediate include architecture; #6 splits body-only dependencies and #7 moves ownership to emission sites.

### Provenance {#commit-a9226f4f2333c2e10824c957bf35f3c7fec62874-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/a9226f4f2333c2e10824c957bf35f3c7fec62874

Source date: 2026-07-11T16:24:42Z


<a id="commit-4b190c22a2e256db2e7b04ab5c977a2f9cf51116"></a>
## ci: build on GCC, Clang, and MSVC with native stdlibs (not just libc++) {#commit-4b190c22a2e256db2e7b04ab5c977a2f9cf51116}

Semantic synthesis / observed: Adds GCC Linux libstdc++, Clang Linux libstdc++ and Windows2022 cl, fail-fast false, MSVC environment setup and shared Ninja configure. #13 immediately corrects Clang library pairing.

### Provenance {#commit-4b190c22a2e256db2e7b04ab5c977a2f9cf51116-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/4b190c22a2e256db2e7b04ab5c977a2f9cf51116

Source date: 2026-07-11T17:12:13Z


<a id="commit-19e9203b3eb2d17c51837e12cc94688190d7163e"></a>
## ci: pair Clang with libc++ (libstdc++ <expected> is incompatible with Clang; still covered by the GCC job) {#commit-19e9203b3eb2d17c51837e12cc94688190d7163e}

Semantic synthesis / rationale: Specific documented toolchain constraint revises #12's native-library simplification. Three compiler/library combinations remain.

### Provenance {#commit-19e9203b3eb2d17c51837e12cc94688190d7163e-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/19e9203b3eb2d17c51837e12cc94688190d7163e

Source date: 2026-07-11T17:17:33Z


<a id="commit-09e532cf6e95a910fad867a881b08cc012eb0f89"></a>
## feat: add ClientboundUpdateSoundDataPacket (id 348) {#commit-09e532cf6e95a910fad867a881b08cc012eb0f89}

Semantic synthesis / limits: Despite wording not hand-derivation, this initial test guidance says read Marshal and encode fields; #30/#35 later require actually executing reference code. CLAUDE.md is analyzed as source evidence, never followed as task instructions. Its existence indicates agent-facing coordination, not proof an AI authored every change.

Limits: Despite wording not hand-derivation, this initial test guidance says read Marshal and encode fields; #30/#35 later require actually executing reference code. CLAUDE.md is analyzed as source evidence, never followed as task instructions. Its existence indicates agent-facing coordination, not proof an AI authored every change.

### Provenance {#commit-09e532cf6e95a910fad867a881b08cc012eb0f89-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/09e532cf6e95a910fad867a881b08cc012eb0f89

Source date: 2026-07-15T15:03:41Z


<a id="commit-f88ee6a03763f0eb7185b04a801ac495e467d86d"></a>
## feat(compiler): take an enum's underlying type from a second base {#commit-f88ee6a03763f0eb7185b04a801ac495e467d86d}

Semantic synthesis / rationale: Message warns uint8/uvarint32 coincide below128, so passing small goldens cannot establish width. Default is convenience rather than cereal's intrinsic rules. #29 flags its limitations and later cereal context changes supersede it.

### Provenance {#commit-f88ee6a03763f0eb7185b04a801ac495e467d86d-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/f88ee6a03763f0eb7185b04a801ac495e467d86d

Source date: 2026-07-16T10:28:26Z


<a id="commit-84bdb837c1a15673fb06c11280c0c5f1d6b28338"></a>
## feat: model MemoryCategory in full {#commit-84bdb837c1a15673fb06c11280c0c5f1d6b28338}

Semantic synthesis / rationale: Message reports exact header/dump agreement, no gates needed. #37/#38 later make auto version-aware.

### Provenance {#commit-84bdb837c1a15673fb06c11280c0c5f1d6b28338-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/84bdb837c1a15673fb06c11280c0c5f1d6b28338

Source date: 2026-07-16T10:35:53Z


<a id="commit-ad2d546e094453f2f4247cf1552ee447220246af"></a>
## feat: model BiomeNoiseGradientSurfaceData, reshaped at 981 {#commit-ad2d546e094453f2f4247cf1552ee447220246af}

Semantic synthesis / limits: Explicit historical naming TODO later closed #69; isolation limitation later corrected by whole-packet path tests #51.

Limits: Explicit historical naming TODO later closed #69; isolation limitation later corrected by whole-packet path tests #51.

### Provenance {#commit-ad2d546e094453f2f4247cf1552ee447220246af-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/ad2d546e094453f2f4247cf1552ee447220246af

Source date: 2026-07-16T13:34:17Z


<a id="commit-0f4b6b2e39d7372e7b20127fed9ed74192e2ec72"></a>
## feat: add StartGamePacket (id 11) {#commit-0f4b6b2e39d7372e7b20127fed9ed74192e2ec72}

Semantic synthesis / rationale: Dump branch r26_u3 lacks this not-yet-cereal packet; r26_u4 is protocol2168 rather than a small successor. Message explicitly rejects then-main's unsigned game_type because refs diverge for nonzero enum. #30 improves oracle execution; committed #27 already has three-byte empty CompoundTag, so #30's narrative of prior four-byte error is development history rather than a four-to-three change visible in this commit.

### Provenance {#commit-0f4b6b2e39d7372e7b20127fed9ed74192e2ec72-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/0f4b6b2e39d7372e7b20127fed9ed74192e2ec72

Source date: 2026-07-16T16:07:22Z


<a id="commit-39637ffc6f754b5692f5ab9728df7ab455eae7c6"></a>
## refactor: drop the enum wire types the underlying already derives {#commit-39637ffc6f754b5692f5ab9728df7ab455eae7c6}

Semantic synthesis / limits: #29 immediately documents cereal counterexamples; #41 temporarily tolerates byte-equivalent small-enum mismatches. Later independent cereal controls supersede width-derived policy.

Limits: #29 immediately documents cereal counterexamples; #41 temporarily tolerates byte-equivalent small-enum mismatches. Later independent cereal controls supersede width-derived policy.

### Provenance {#commit-39637ffc6f754b5692f5ab9728df7ab455eae7c6-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/39637ffc6f754b5692f5ab9728df7ab455eae7c6

Source date: 2026-07-16T16:14:41Z


<a id="commit-f1de73e2e2f346d925990f805d3e4d1d87970c5c"></a>
## docs: record the deferred hole in the enum wire default {#commit-f1de73e2e2f346d925990f805d3e4d1d87970c5c}

Semantic synthesis / limits: The categorical guidance is itself revised by #41 and corrected further by #70–71. Preserve it as an intermediate diagnosis, not final authority.

Limits: The categorical guidance is itself revised by #41 and corrected further by #70–71. Preserve it as an intermediate diagnosis, not final authority.

### Provenance {#commit-f1de73e2e2f346d925990f805d3e4d1d87970c5c-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/f1de73e2e2f346d925990f805d3e4d1d87970c5c

Source date: 2026-07-16T16:23:46Z


<a id="commit-9fe937885b294502954981e4d098acbf1caadc2a"></a>
## test: regenerate the StartGame golden from a live gophertunnel {#commit-9fe937885b294502954981e4d098acbf1caadc2a}

Semantic synthesis / limits: The committed parent already has a three-byte empty CompoundTag. Do not fabricate a visible four-to-three-byte diff: that error is reported development history. This reviewer did not run either implementation. The structural old-version test is weaker than an independently produced old golden, later reference re-execution is reported at #66, but no independent old StartGame literal is committed there.

Limits: The committed parent already has a three-byte empty CompoundTag. Do not fabricate a visible four-to-three-byte diff: that error is reported development history. This reviewer did not run either implementation. The structural old-version test is weaker than an independently produced old golden, later reference re-execution is reported at #66, but no independent old StartGame literal is committed there.

### Provenance {#commit-9fe937885b294502954981e4d098acbf1caadc2a-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/9fe937885b294502954981e4d098acbf1caadc2a

Source date: 2026-07-16T16:29:36Z


<a id="commit-a300a054db52817a42c6221651c46c00b4bf796f"></a>
## refactor(cpp): name the backend after protoc's, and give fields a real map {#commit-a300a054db52817a42c6221651c46c00b4bf796f}

Semantic synthesis / limits: This reverses #4's terminology without reversing the wire model. The new constructor asserts all field types resolved earlier; malformed/unresolved paths may fail sooner, so broad behavior identity is stronger than the observed existing-schema claim.

Limits: This reverses #4's terminology without reversing the wire model. The new constructor asserts all field types resolved earlier; malformed/unresolved paths may fail sooner, so broad behavior identity is stronger than the observed existing-schema claim.

### Provenance {#commit-a300a054db52817a42c6221651c46c00b4bf796f-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/a300a054db52817a42c6221651c46c00b4bf796f

Source date: 2026-07-16T20:54:35Z


<a id="commit-44040ecb86a8b61dd6eba7411cc04d50c82d5316"></a>
## docs: consolidate CLAUDE.md down to the rules that bite {#commit-44040ecb86a8b61dd6eba7411cc04d50c82d5316}

Semantic synthesis / limits: Document is evidence of agent coordination and project policy, not proof that every commit used AI or followed every rule. Its claims about external consumers are author reports here. #39 immediately includes a derived golden, and #66 later audits them, demonstrating a gap between stated process and recorded practice.

Limits: Document is evidence of agent coordination and project policy, not proof that every commit used AI or followed every rule. Its claims about external consumers are author reports here. #39 immediately includes a derived golden, and #66 later audits them, demonstrating a gap between stated process and recorded practice.

### Provenance {#commit-44040ecb86a8b61dd6eba7411cc04d50c82d5316-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/44040ecb86a8b61dd6eba7411cc04d50c82d5316

Source date: 2026-07-20T19:04:50Z


<a id="commit-5aa7780d6ccd2b85268aea1f5714997a54a9b239"></a>
## feat: model LevelSoundEvent, adding the 983 sound events {#commit-5aa7780d6ccd2b85268aea1f5714997a54a9b239}

Semantic synthesis / limits: At this commit late members and the moving sentinel are not snapshot-correct. #37 gates ten additions and #38 fixes the sentinel. Individual sound names are data transcription, not573 independent engineering lessons. Full mapping was read; structural inventory is also retained.

Limits: At this commit late members and the moving sentinel are not snapshot-correct. #37 gates ten additions and #38 fixes the sentinel. Individual sound names are data transcription, not573 independent engineering lessons. Full mapping was read; structural inventory is also retained.

### Provenance {#commit-5aa7780d6ccd2b85268aea1f5714997a54a9b239-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/5aa7780d6ccd2b85268aea1f5714997a54a9b239

Source date: 2026-07-20T19:16:20Z


<a id="commit-d9d5d378ad0bffd24875d6bbff5fb6a68969a9cc"></a>
## feat(compiler): version-gate enum members, and gate the 983..1000 sound events {#commit-d9d5d378ad0bffd24875d6bbff5fb6a68969a9cc}

Semantic synthesis / limits: No new tests in this patch; generated-output claims belong to the message. The sentinel limitation is not permanent: #38 solves it.

Limits: No new tests in this patch; generated-output claims belong to the message. The sentinel limitation is not permanent: #38 solves it.

### Provenance {#commit-d9d5d378ad0bffd24875d6bbff5fb6a68969a9cc-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/d9d5d378ad0bffd24875d6bbff5fb6a68969a9cc

Source date: 2026-07-20T19:20:58Z


<a id="commit-4326417f7cacd1fd5cd77534b20eab77e7bafc25"></a>
## feat: model BiomeDefinitionListPacket (id 122) {#commit-4326417f7cacd1fd5cd77534b20eab77e7bafc25}

Semantic synthesis / limits: The basic golden is still described as derived, conflicting with #35's newly stated execute-first policy; #66 later regenerates it. Several enum overrides and comments are temporary and cleaned later. Map order test covers deterministic output, not duplicate input keys or resource limits.

Limits: The basic golden is still described as derived, conflicting with #35's newly stated execute-first policy; #66 later regenerates it. Several enum overrides and comments are temporary and cleaned later. Map order test covers deterministic output, not duplicate input keys or resource limits.

### Provenance {#commit-4326417f7cacd1fd5cd77534b20eab77e7bafc25-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/4326417f7cacd1fd5cd77534b20eab77e7bafc25

Source date: 2026-07-20T19:26:48Z


<a id="commit-ba508b42b7cce2428f85f0b451a329e4fe8a3156"></a>
## feat: model BossEventPacket (id 74) at both eras {#commit-ba508b42b7cce2428f85f0b451a329e4fe8a3156}

Semantic synthesis / limits: The small-value-equivalence policy relaxes #29's width-fidelity rule and should be retained as a transient tradeoff, not evidence that uint8 equals uvarint32 generally. The test name 'every gated shape' loops four fixtures, not all nine event IDs. All reported execution remains historical.

Limits: The small-value-equivalence policy relaxes #29's width-fidelity rule and should be retained as a transient tradeoff, not evidence that uint8 equals uvarint32 generally. The test name 'every gated shape' loops four fixtures, not all nine event IDs. All reported execution remains historical.

### Provenance {#commit-ba508b42b7cce2428f85f0b451a329e4fe8a3156-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/ba508b42b7cce2428f85f0b451a329e4fe8a3156

Source date: 2026-07-20T19:58:23Z


<a id="commit-8d2f9cac8e916dce4dc325850386588bec8f4c68"></a>
## feat(compiler): Optional[] spelling and the cereal presence-wrapper collapse {#commit-8d2f9cac8e916dce4dc325850386588bec8f4c68}

Semantic synthesis / limits: False marker is not rejected and may cause remaining bytes to be misinterpreted. #76 replaces this special case with explicit Literal[True], removes nested-optional syntax and validates the marker. Do not teach this intermediate encoding as the final design.

Limits: False marker is not rejected and may cause remaining bytes to be misinterpreted. #76 replaces this special case with explicit Literal[True], removes nested-optional syntax and validates the marker. Do not teach this intermediate encoding as the final design.

### Provenance {#commit-8d2f9cac8e916dce4dc325850386588bec8f4c68-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/8d2f9cac8e916dce4dc325850386588bec8f4c68

Source date: 2026-07-20T22:21:21Z


<a id="commit-c212c536866c969a2d15de5c81989b59616ffd16"></a>
## feat: model InventoryTransactionPacket (id 30) cerealised form {#commit-c212c536866c969a2d15de5c81989b59616ffd16}

Semantic synthesis / limits: The packet is1001-only here; pre-cereal support is added #48. ContainerID starts as primitive alias, becomes typed #68 and its temporary encoding change is reversed #70. Fixtures cover three of five variants and narrow happy-path values, not exhaustive validity. Historical source/test reports are not independently executed.

Limits: The packet is1001-only here; pre-cereal support is added #48. ContainerID starts as primitive alias, becomes typed #68 and its temporary encoding change is reversed #70. Fixtures cover three of five variants and narrow happy-path values, not exhaustive validity. Historical source/test reports are not independently executed.

### Provenance {#commit-c212c536866c969a2d15de5c81989b59616ffd16-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/c212c536866c969a2d15de5c81989b59616ffd16

Source date: 2026-07-20T22:21:21Z


<a id="commit-6b35b4685a2d2b4008fd455e07ca004ec50c504c"></a>
## feat(compiler): version a type alias over versioned types {#commit-6b35b4685a2d2b4008fd455e07ca004ec50c504c}

Semantic synthesis / limits: Alias planning lives in the C++ backend rather than DescriptorPool. The last alias selector has no computed disappearance bound. A local reused variable triggers mypy failure later repaired in #60; reported generated C++ preservation does not establish full toolchain CI health.

Limits: Alias planning lives in the C++ backend rather than DescriptorPool. The last alias selector has no computed disappearance bound. A local reused variable triggers mypy failure later repaired in #60; reported generated C++ preservation does not establish full toolchain CI health.

### Provenance {#commit-6b35b4685a2d2b4008fd455e07ca004ec50c504c-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/6b35b4685a2d2b4008fd455e07ca004ec50c504c

Source date: 2026-07-21T10:30:30Z


<a id="commit-867ff6590321f62d7ee27e0b8689632a9e6e3c8b"></a>
## feat: add MinecraftEventing::InteractionType with 986's Equipping {#commit-867ff6590321f62d7ee27e0b8689632a9e6e3c8b}

Semantic synthesis / limits: No packet or runtime test is added. The name is a temporary flattening pending support; #64 enables nesting, but #65 does not modify telemetry.py, so no telemetry rename is claimed within this range.

Limits: No packet or runtime test is added. The name is a temporary flattening pending support; #64 enables nesting, but #65 does not modify telemetry.py, so no telemetry rename is claimed within this range.

### Provenance {#commit-867ff6590321f62d7ee27e0b8689632a9e6e3c8b-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/867ff6590321f62d7ee27e0b8689632a9e6e3c8b

Source date: 2026-07-21T10:30:47Z


<a id="commit-5114938dfaf6bb6806fd7cd5338e0bfc2471188f"></a>
## feat: model PrimitiveShapesPacket (id 328) at both eras {#commit-5114938dfaf6bb6806fd7cd5338e0bfc2471188f}

Semantic synthesis / limits: Keep the cylinder source disagreement and provenance, not an unqualified assertion that headers always determine shape. Ellipsoid and cone are modeled but unexercised in these fixtures. Composition of a reported oracle is visible and later #66 compares it, rather than pretending every literal was an untouched independent dump.

Limits: Keep the cylinder source disagreement and provenance, not an unqualified assertion that headers always determine shape. Ellipsoid and cone are modeled but unexercised in these fixtures. Composition of a reported oracle is visible and later #66 compares it, rather than pretending every literal was an untouched independent dump.

### Provenance {#commit-5114938dfaf6bb6806fd7cd5338e0bfc2471188f-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/5114938dfaf6bb6806fd7cd5338e0bfc2471188f

Source date: 2026-07-21T12:40:47Z


<a id="commit-c7ef6a7d1eac803569312911986d859a3a2ec1ce"></a>
## feat: add MovementEffectType with 998's GEYSER_BOOST {#commit-c7ef6a7d1eac803569312911986d859a3a2ec1ce}

Semantic synthesis / limits: No packet or dedicated test here. #63 later tests its reflected membership/sentinel. The source warning is unresolved at this point and should not become an inferred encoding rule.

Limits: No packet or dedicated test here. #63 later tests its reflected membership/sentinel. The source warning is unresolved at this point and should not become an inferred encoding rule.

### Provenance {#commit-c7ef6a7d1eac803569312911986d859a3a2ec1ce-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/c7ef6a7d1eac803569312911986d859a3a2ec1ce

Source date: 2026-07-21T15:32:11Z


<a id="commit-bc6cf7102eff43d5c1e3627ee3d793d5c16674a2"></a>
## fix(compiler): give the alias view its own name {#commit-bc6cf7102eff43d5c1e3627ee3d793d5c16674a2}

Semantic synthesis / rationale: Message explicitly reports CI had been red since #45 because mypy inferred the original local type. Generated C++ is reported unchanged.

### Provenance {#commit-bc6cf7102eff43d5c1e3627ee3d793d5c16674a2-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/bc6cf7102eff43d5c1e3627ee3d793d5c16674a2

Source date: 2026-07-21T16:05:36Z


<a id="commit-d43065cf3882d625d1f7ee8cbad53566915846f8"></a>
## docs: add a README {#commit-d43065cf3882d625d1f7ee8cbad53566915846f8}

Semantic synthesis / limits: Historical example validation is not this review's run and not actual Codex/Windows proof. #62 changes version selector syntax immediately afterward, so preserve both chronology and current-context qualifier.

Limits: Historical example validation is not this review's run and not actual Codex/Windows proof. #62 changes version selector syntax immediately afterward, so preserve both chronology and current-context qualifier.

### Provenance {#commit-d43065cf3882d625d1f7ee8cbad53566915846f8-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/d43065cf3882d625d1f7ee8cbad53566915846f8

Source date: 2026-07-21T16:10:34Z


<a id="commit-f3c4e704ed4ca9638b9f7067f38bdf43210635df"></a>
## feat: gate versions on raw protocol numbers {#commit-f3c4e704ed4ca9638b9f7067f38bdf43210635df}

Semantic synthesis / rationale: Message explicitly removes artificial DSL enum coupling and documents raw selector API. Gate guidance still requires modeled boundaries. Handshake fields concretely need endian. The biome change is stated but rationale becomes explicit at #65: old dumper falsely marked enum signedness unsigned.

### Provenance {#commit-f3c4e704ed4ca9638b9f7067f38bdf43210635df-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/f3c4e704ed4ca9638b9f7067f38bdf43210635df

Source date: 2026-07-28T13:49:04Z


<a id="commit-eb761a0aca0f4aa689f29da6636f863fc2bbaf5c"></a>
## feat(compiler): support nested types {#commit-eb761a0aca0f4aa689f29da6636f863fc2bbaf5c}

Semantic synthesis / limits: No new tests in this compiler patch; schema/test exercise follows #65. The implementation's anchoring groups all nested children based on whether any changes, which is a conservative strategy, not minimal dedup per child. Recursive names do not prove every alias cycle or redeclaration-inside-one-body case works.

Limits: No new tests in this compiler patch; schema/test exercise follows #65. The implementation's anchoring groups all nested children based on whether any changes, which is a conservative strategy, not minimal dedup per child. Recursive names do not prove every alias cycle or redeclaration-inside-one-body case works.

### Provenance {#commit-eb761a0aca0f4aa689f29da6636f863fc2bbaf5c-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/eb761a0aca0f4aa689f29da6636f863fc2bbaf5c

Source date: 2026-07-28T14:51:42Z


<a id="commit-202857a9c1c7e1866db22b655813063a0ae36888"></a>
## docs: name the open wire question after BDS, not gophertunnel {#commit-202857a9c1c7e1866db22b655813063a0ae36888}

Semantic synthesis / limits: No wire change or resolution here; #68 experiments and #70 closes it.

Limits: No wire change or resolution here; #68 experiments and #70 closes it.

### Provenance {#commit-202857a9c1c7e1866db22b655813063a0ae36888-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/202857a9c1c7e1866db22b655813063a0ae36888

Source date: 2026-07-28T15:06:43Z


<a id="commit-10d3ab1ced055fa80ac5752427665a141583c248"></a>
## feat(protocol): model ContainerID as the enum BDS declares {#commit-10d3ab1ced055fa80ac5752427665a141583c248}

Semantic synthesis / limits: This encoding decision is reversed at #70. Keep the valuable typed enum addition separate from the failed trait inference. A passing patched golden only demonstrates agreement with the chosen schema, not external correctness.

Limits: This encoding decision is reversed at #70. Keep the valuable typed enum addition separate from the failed trait inference. A passing patched golden only demonstrates agreement with the chosen schema, not external correctness.

### Provenance {#commit-10d3ab1ced055fa80ac5752427665a141583c248-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/10d3ab1ced055fa80ac5752427665a141583c248

Source date: 2026-07-28T15:38:43Z


<a id="commit-a0b1a16480d96e0103170a50e84ec1d3ca998981"></a>
## fix(protocol): read InventorySource's container id as a plain int8 {#commit-a0b1a16480d96e0103170a50e84ec1d3ca998981}

Semantic synthesis / observed: Removes only the1001varint override, restores fixture byte18 to0c, removes its TODO and explanation. The entire test file returns exactly to its pre-#68 blob; the new ContainerID enum remains. Docs say the dump is not an automatic tiebreaker and the trait was misread.

### Provenance {#commit-a0b1a16480d96e0103170a50e84ec1d3ca998981-provenance}

Public source: https://github.com/EndstoneMC/bedrock-protocol/commit/a0b1a16480d96e0103170a50e84ec1d3ca998981

Source date: 2026-07-28T15:56:54Z
