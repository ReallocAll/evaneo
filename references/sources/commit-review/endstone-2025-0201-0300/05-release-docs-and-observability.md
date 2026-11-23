<!-- retrieval: {"source_ids":["public:commit:2b88490577173ea28fe00b8aabb1098b9b55d2af","public:commit:4a071232a3bfca72001f350a09a4b6c1ae86bc65","public:commit:58440c88206ed74b225a3ca1374375a89c278ed3","public:commit:e7faf73810ab36589cb16e12b6ceda1723e21c2c","public:commit:f3730aa2758c3498a99a3e3c5b788571f202f086","public:commit:fc8bace5e2f6f53e5f008841b284dabbb0fe3f97"],"source_type":"public","date":"2025-02-19..2025-02-20","topics":["ffi","testing","build","performance","api","diagnosis","documentation"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Release metadata, documentation and observability {#release-metadata-documentation-and-observability}

265 adds API0.6 to Python's compatibility list and restores Release wheel configuration after260 temporarily selected RelWithDebInfo.266 advances the source patch version and README Bedrock badge. These are inspectable distribution inputs; this review does not claim a package was published or installed. BUILD_TESTING remains disabled in wheel configuration, so test-source presence does not prove release-build test execution.

273 writes0.6.0 and0.6.1 release notes and a prospective0.6.2 section. It credits smartcmd and killcerr contributions separately and describes the native compatibility/API work.274 removes a duplicated proxied-command crash fix from the earlier release, preserving the corrected chronology.275 documents damage/explosion cancellation, rather than introducing hooks. Doc claims about block behavior in unloaded chunks are reported behavior and cannot substitute for native runtime checks after the API validation removal.

281 multiplies fractional tick usage by100 in current/average percent-labelled status text. It repairs display units without changing measurements or supporting a performance claim. Small mechanical/documentation edits are individually represented below but do not each support an independent style preference.

No package publication, benchmark, build, server run, crash reproduction or frozen evaluation was performed. The larger research remains incomplete outside this bounded100-target unit.


<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}


<a id="commit-265"></a>
### 265. chore: release v0.6.0 {#commit-265}

[f3730aa2758c3498a99a3e3c5b788571f202f086](https://github.com/EndstoneMC/endstone/commit/f3730aa2758c3498a99a3e3c5b788571f202f086) · 2025-02-19T20:47:53Z · author Vincent.

Parents: `f49b4a70a155827e58602b5211e184f198062896`. Full message and sources: parent 1.

Releases source version0.6.0 support by adding Python API0.6 compatibility and restoring Release wheel build type after260. Build testing remains off in the wheel configuration. No package publication or runtime compatibility was verified.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-266"></a>
### 266. chore: v0.6.1 is next {#commit-266}

[2b88490577173ea28fe00b8aabb1098b9b55d2af](https://github.com/EndstoneMC/endstone/commit/2b88490577173ea28fe00b8aabb1098b9b55d2af) · 2025-02-19T21:08:32Z · author Vincent.

Parents: `f3730aa2758c3498a99a3e3c5b788571f202f086`. Full message and sources: parent 1.

Updates README Bedrock compatibility badge to1.21.60 and advances header patch version to0.6.1. Release metadata only, not an observed test result.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-273"></a>
### 273. docs: update CHANGELOG.md {#commit-273}

[4a071232a3bfca72001f350a09a4b6c1ae86bc65](https://github.com/EndstoneMC/endstone/commit/4a071232a3bfca72001f350a09a4b6c1ae86bc65) · 2025-02-20T11:50:17Z · author Vincent.

Parents: `92cc35a47e600ec41b6990b8c6cd65f5b1621b9a`. Full message and sources: parent 1.

Writes0.6.0/0.6.1 changelog and upcoming0.6.2 section, describing API additions and native compatibility. Credits smartcmd PR113/132 and killcerr PR114 separately. Initially duplicates proxied-command crash fix under both releases;274 removes old entry. Documentation claims about empty blocks in unloaded chunks are not independently verified native outcomes.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-274"></a>
### 274. docs: update CHANGELOG.md {#commit-274}

[e7faf73810ab36589cb16e12b6ceda1723e21c2c](https://github.com/EndstoneMC/endstone/commit/e7faf73810ab36589cb16e12b6ceda1723e21c2c) · 2025-02-20T11:56:26Z · author Vincent.

Parents: `4a071232a3bfca72001f350a09a4b6c1ae86bc65`. Full message and sources: parent 1.

Removes duplicate proxied-command crash fix from0.6.0, retaining0.6.1 chronology. A documentation correction, not a second implementation repair.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-275"></a>
### 275. docs: update CHANGELOG.md {#commit-275}

[58440c88206ed74b225a3ca1374375a89c278ed3](https://github.com/EndstoneMC/endstone/commit/58440c88206ed74b225a3ca1374375a89c278ed3) · 2025-02-20T12:02:51Z · author Vincent.

Parents: `e7faf73810ab36589cb16e12b6ceda1723e21c2c`. Full message and sources: parent 1.

Adds ActorDamageEvent and ActorExplodeEvent event documentation and cancellation descriptions. No new executable hook or cancellation implementation.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-281"></a>
### 281. fix: display usage in percentage in status command outputs {#commit-281}

[fc8bace5e2f6f53e5f008841b284dabbb0fe3f97](https://github.com/EndstoneMC/endstone/commit/fc8bace5e2f6f53e5f008841b284dabbb0fe3f97) · 2025-02-20T21:17:08Z · author Vincent.

Parents: `b0cf8458da86714cc0e2c6ec2f1d072eb58de60b`. Full message and sources: parent 1.

Multiplies current and average tick-usage fractions by100 for percent-labelled status output. This is a unit-format correction, not changed timing collection or a performance improvement.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.
