<!-- retrieval: {"source_ids":["public:commit:1841a88a5fda378e8524b97a277b4d182ed06871","public:commit:28ba71750246e378d0f583cb0a365f9c4b27d542","public:commit:469c32717bf0113089c16db2bd220c15eff6489c","public:commit:577e472c2b6e399ca346cf4b0564162875f5c6af","public:commit:70ec2e3e11bf5c2c5375d1587a7680e33e844853","public:commit:71371baf85ad4dd260d3fd0ec6217c057427eea7","public:commit:823dc2388a832cca92462f7f8af189c7b201edd9","public:commit:91064e5fa25c4416f5f8782d7ba6004251a723bf","public:commit:911c1fef6bf1539d06c2b69f545cdaaa1111e10b","public:commit:937c70a5ac804567576ce3a5fbe6ecbaf2f66804","public:commit:989771ee0388376e7d2d428360361f94ef82bf63","public:commit:a78b39c147581fc31aa88e2bd95f80b1d9d730c7","public:commit:c7a25f0e6accd03a3a6964c7f643d4fcfcc77d0d","public:commit:d379fa5dfef0046faa8983fd55e67d1a4b1d00c0","public:commit:dd7736a5ff03deb59dde5653a1ecf909c5b25f2e","public:commit:e1db80635f8e0731595139b27fedae237db05e70","public:commit:ef36db7c2b6460580fa5d88ce63473a0d5b4e4d0","public:commit:fce3b8e4b280df7cf2f6b0b3c483861c8bc0b73b","public:context-commit:5dfcb9c87d9c95b964b6c3506e92887720cce850","public:context-commit:72e85161e6c0dd643af8080155283d262f4f1654","public:context-commit:747115ad3dae5ad86b03350d29990f3a04d968a8","public:context-commit:84cff37a7ea3f745ed2cd78c097233bd0666b175","public:context-commit:9c58bfcc0ee61cbd6ffb157ec5933b69499d4e99","public:context-commit:aa2fe8a2d05ae2f419a6ccea0a6fac60e505b723","public:context-commit:b56974a8b7a2d979427ac5bf6ed5f45a8dd4ce37","public:context-commit:bc9ba6bc5bdb9ec1e333c2d994412087ac1d15e0","public:context-commit:bf939797587115ca5054eb9a44980b0861c5b3d1","public:context-commit:e44194138c9279ffe45cddce1d3e89e623fd15c8","public:context-commit:f00efc635bb349244a2d4c350e129e06cf952088"],"source_type":"public","date":"2025-08-27..2025-12-14","topics":["concurrency","ffi","testing","build","api","diagnosis","documentation","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Branches, releases, build changes and context {#branches-releases-build-changes-and-context}

## Exact chronology is not a single linear product state {#exact-chronology-is-not-a-single-linear-product-state}

Main reaches 1352 with the November updates; stable continues to 1363 with separate December changes. The branches share earlier history but have distinct release and feature endpoints, so stable-only changes must not be folded into main's 1352 state.

The merge history includes two follow-up repairs: 1315 needs 1316's syntax and symbol fix, and 1336's main address selection is refreshed by 1337. A merge's recorded conflict list does not by itself establish correct integration.

## Build, documentation and release costs {#build-documentation-and-release-costs}

Most native declarations are reconstructed compatibility scaffolding, not independently invented algorithms. Symbol tables receive proportional full-key/value, duplicate-address and nonnumeric residual checks rather than meaningless line-by-line recitation of hundreds of integers. Dependency major-version bot bumps preserve workflow configuration and need separate action/runtime compatibility validation; this review does not execute CI.

The contributing document moves into the docs tree, retaining Conan/C++20/Ninja and MkDocs steps while changing Windows tab indentation. Empty .gitmodules removal has no substantive lesson. Release labels are recorded precisely: 0.10.17 prose appears while the macro remains16; 1362 jumps it to18 and uses a December11 changelog date despite the December14 commit. Such details prevent release documentation from being misused as a runtime test record.

Test changes outside imported histories are a renamed Identifier type in an existing assertion and mock signature updates. No removed test is automatically labelled a defect; no absent regression suite is silently treated as passing. The useful cost/coverage question is which contract changes need expensive native validation versus cheap source/unit checks, not maximizing test count.

## Captured issue312 {#captured-issue312}

The local primary report by pgrd1 describes Windows Endstone0.10.16 access violation, uncertain new-item reproduction, and a stack through ItemStackBase::deserializeComponents and Item::readUserData. Vincent confirms a bug and says work on a fix is underway. pgrd1 expresses thanks, which is not a retest. Commit1357 closes the issue and changes one Windows loader address. Full captured three-unit thread context, source hash and links are in thread-context-index.json and context/thread-312-read.txt.

PR301 and PR302 discussions are absent from the canonical captured thread inventory. Their actual bot commit messages and complete diffs are available and read below. This absence limits discussion coverage only; it is not represented as a denied request or an unread available patch.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1303"></a>
## Commit 1303 {#commit-1303}

d379fa5dfef0046faa8983fd55e67d1a4b1d00c0 · 2025-11-17T16:41:27Z

[chore: update BDS to v1.21.123.2](https://github.com/EndstoneMC/endstone/commit/d379fa5dfef0046faa8983fd55e67d1a4b1d00c0)

**Change and causal context.** Stable BDS 1.21.123 address refresh changes all 65 Windows and 65 Linux symbol values; version and timestamp advance. Parsed full-key/value proof finds no key changes or duplicate addresses.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Only symbol-table content is verified. Title names binary version 1.21.123.2; table stores 1.21.123. No binary disassembly or invocation validates addresses.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1304"></a>
## Commit 1304 {#commit-1304}

937c70a5ac804567576ce3a5fbe6ecbaf2f66804 · 2025-11-17T16:46:56Z

[Merge remote-tracking branch 'origin/v0.10' into v0.10](https://github.com/EndstoneMC/endstone/commit/937c70a5ac804567576ce3a5fbe6ecbaf2f66804)

**Change and causal context.** Merges the remote v0.10 branch into local v0.10 after the address update; message records symbols.toml conflict. Every resulting changed file is exactly one parent blob/mode, with no novel mixed file. Both directional histories are retained in merge-reuse.json.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Parent identity and completed semantic ancestry establish reuse, not an inference that a merge endorses every imported behavior.

Offline full message: message. Full deltas: parent 1, parent 2.
Author: Vincent; committer: Vincent.

<a id="commit-1314"></a>
## Commit 1314 {#commit-1314}

dd7736a5ff03deb59dde5653a1ecf909c5b25f2e · 2025-11-18T01:57:53Z

[chore: bump version to 0.10.12](https://github.com/EndstoneMC/endstone/commit/dd7736a5ff03deb59dde5653a1ecf909c5b25f2e)

**Change and causal context.** Publishes 0.10.12 constants/changelog and README BDS badge; corrects the old 0.10.11 release link. Changelog groups map retention, certificate/item malformed-input defenses, custom dimension fixes and early IP bans.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Release prose is author-reported outcome, not runtime verification. It does not establish that all preceding staged implementations are complete.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1315"></a>
## Commit 1315 {#commit-1315}

911c1fef6bf1539d06c2b69f545cdaaa1111e10b · 2025-11-18T13:25:58Z

[Merge remote-tracking branch 'origin/v0.10'](https://github.com/EndstoneMC/endstone/commit/911c1fef6bf1539d06c2b69f545cdaaa1111e10b)

**Change and causal context.** Merges stable 0.10.12 into main. Seven mixed paths are read against both parents: CMake composes native input and runtime hooks, item/compound code combines main additions with stable parser changes, and server setup retains main metrics/console/map event behavior. The server conflict resolution adds a stray duplicate ConnectPosition statement.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** The duplicate is repaired in 1316. Parent-equal symbol selection omits the new three detour/loader symbols until 1316. All other parent-equal files are exact identity-backed ancestry reuse.

Offline full message: message. Full deltas: parent 1, parent 2.
Author: Vincent; committer: Vincent.

<a id="commit-1316"></a>
## Commit 1316 {#commit-1316}

1841a88a5fda378e8524b97a277b4d182ed06871 · 2025-11-18T13:32:45Z

[feat: update symbols.toml](https://github.com/EndstoneMC/endstone/commit/1841a88a5fda378e8524b97a277b4d182ed06871)

**Change and causal context.** Repairs the stray ConnectPosition statement left by 1315 and adds the certificate, Item::readUserData and can-place/can-destroy loader symbols to main. Main has 67 symbols per platform, retaining its own symbol set.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** A symbols-only title hides a syntax repair. Address values remain static evidence only; this bridges the integration gap, not a demonstrated build pass.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1318"></a>
## Commit 1318 {#commit-1318}

ef36db7c2b6460580fa5d88ce63473a0d5b4e4d0 · 2025-11-18T14:36:46Z

[chore: bump version to 0.10.13](https://github.com/EndstoneMC/endstone/commit/ef36db7c2b6460580fa5d88ce63473a0d5b4e4d0)

**Change and causal context.** Bumps stable to 0.10.13 and records a certain-world crash fix, following dimension enumeration.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** The changelog is a release assertion; no captured reporter confirmation or test is added in this commit.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1321"></a>
## Commit 1321 {#commit-1321}

91064e5fa25c4416f5f8782d7ba6004251a723bf · 2025-11-18T22:46:15Z

[chore: bump version to 0.10.14](https://github.com/EndstoneMC/endstone/commit/91064e5fa25c4416f5f8782d7ba6004251a723bf)

**Change and causal context.** Bumps 0.10.14, records packet limiting/disconnected-client defense, and logs a connection-closed message when there is no associated player.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** The logging branch is later removed in 1331. Compare-link label mistakenly says 0.10.12 while URL compares 0.10.13; 1327 corrects it. No packet-flood benchmark is supplied.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1324"></a>
## Commit 1324 {#commit-1324}

989771ee0388376e7d2d428360361f94ef82bf63 · 2025-11-18T23:12:06Z

[Merge remote-tracking branch 'origin/v0.10'](https://github.com/EndstoneMC/endstone/commit/989771ee0388376e7d2d428360361f94ef82bf63)

**Change and causal context.** Merges the additional stable dimension/network changes into main. server.cpp is the only mixed file and both deltas are read; it combines limiter startup with existing metrics, map events, registries and console setup. Portal-header conflict is resolved to an exact parent blob.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Preserve branch provenance and imported prior caveats. A merge title is not new independent support for every imported implementation.

Offline full message: message. Full deltas: parent 1, parent 2.
Author: Vincent; committer: Vincent.

<a id="commit-1325"></a>
## Commit 1325 {#commit-1325}

c7a25f0e6accd03a3a6964c7f643d4fcfcc77d0d · 2025-11-21T17:59:31Z

[feat: add support for v1.21.124.2](https://github.com/EndstoneMC/endstone/commit/c7a25f0e6accd03a3a6964c7f643d4fcfcc77d0d)

**Change and causal context.** Stable advances to BDS 1.21.124.2, protocol 860 and patch 15, with Python Minecraft label 1.21.124. Symbol proof finds 16 Windows and all 68 Linux values changed, with stable keys unchanged.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** No native address or protocol interaction is tested. Main gets its separate matching table in 1337.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1327"></a>
## Commit 1327 {#commit-1327}

28ba71750246e378d0f583cb0a365f9c4b27d542 · 2025-11-21T18:44:19Z

[docs: update README.md and CHANGELOG.md](https://github.com/EndstoneMC/endstone/commit/28ba71750246e378d0f583cb0a365f9c4b27d542)

**Change and causal context.** Documents 0.10.15/BDS 1.21.124.2 and updates README. Corrects the preceding compare label but introduces a truncated 0.10.1 label for the new entry, fixed by 1354.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Documentation only; no new behavioral proof.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1335"></a>
## Commit 1335 {#commit-1335}

823dc2388a832cca92462f7f8af189c7b201edd9 · 2025-11-24T22:32:55Z

[Merge remote-tracking branch 'origin/main'](https://github.com/EndstoneMC/endstone/commit/823dc2388a832cca92462f7f8af189c7b201edd9)

**Change and causal context.** Merges remote main, importing the two November 24 bot upgrades plus main feature work in the opposite direction. No mixed result file differs from both parents.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Dependabot authored the workflow update; GitHub is the committer. The change is not a runtime or compatibility result.

Offline full message: message. Full deltas: parent 1, parent 2.
Author: Vincent; committer: Vincent.

<a id="commit-1336"></a>
## Commit 1336 {#commit-1336}

469c32717bf0113089c16db2bd220c15eff6489c · 2025-11-24T22:33:46Z

[Merge remote-tracking branch 'origin/v0.10'](https://github.com/EndstoneMC/endstone/commit/469c32717bf0113089c16db2bd220c15eff6489c)

**Change and causal context.** Merges stable 0.10.15 into main. Sole mixed file combines main lazy Python exports with stable Minecraft 1.21.124 label; both-parent deltas read. Other conflicts, including network_system and symbols, select exact parent blobs.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Selected main symbol version remains 1.21.123 until 1337 despite advertised version advance. An exact parent selection may still leave an integration gap; no compile/runtime pass inferred.

Offline full message: message. Full deltas: parent 1, parent 2.
Author: Vincent; committer: Vincent.

<a id="commit-1337"></a>
## Commit 1337 {#commit-1337}

e1db80635f8e0731595139b27fedae237db05e70 · 2025-11-25T16:43:06Z

[chore: update symbol to 1.21.124](https://github.com/EndstoneMC/endstone/commit/e1db80635f8e0731595139b27fedae237db05e70)

**Change and causal context.** Updates main symbol table to 1.21.124: 67 keys per platform, 16 Windows and 67 Linux address changes, no key addition/removal or duplicates.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Main and stable have different key sets, so this cannot be treated as blindly identical to 1325. Tables are fully parsed and key changes checked, but addresses not binary-verified.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1341"></a>
## Commit 1341 {#commit-1341}

577e472c2b6e399ca346cf4b0564162875f5c6af · 2025-11-25T19:01:46Z

[chore: remove `.gitmodules` file](https://github.com/EndstoneMC/endstone/commit/577e472c2b6e399ca346cf4b0564162875f5c6af)

**Change and causal context.** Deletes the zero-byte .gitmodules blob; no submodule contents or dependency versions change.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Verified empty-object deletion is mechanical and supports no independent design preference.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1342"></a>
## Commit 1342 {#commit-1342}

a78b39c147581fc31aa88e2bd95f80b1d9d730c7 · 2025-11-25T19:02:25Z

[chore: move contributing guide to docs directory](https://github.com/EndstoneMC/endstone/commit/a78b39c147581fc31aa88e2bd95f80b1d9d730c7)

**Change and causal context.** Moves contributing prose into docs/getting-started/contributing.md, replacing its include directive and deleting root CONTRIBUTING.md. Clone, Conan >=2, C++20/Ninja, activation/build/install and MkDocs instructions remain.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Windows tab code fences lose indentation while Linux fences retain it, which may affect tab rendering. Commands were read as documentation, never executed. No justification to infer a preferred package manager beyond this project.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1354"></a>
## Commit 1354 {#commit-1354}

fce3b8e4b280df7cf2f6b0b3c483861c8bc0b73b · 2025-12-11T00:05:46Z

[docs: update README.md and CHANGELOG.md](https://github.com/EndstoneMC/endstone/commit/fce3b8e4b280df7cf2f6b0b3c483861c8bc0b73b)

**Change and causal context.** Documents 0.10.16/BDS 1.21.130.4, updates README and fixes the previous truncated compare label.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Only release documentation; the port’s native correctness is not demonstrated by this entry.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1358"></a>
## Commit 1358 {#commit-1358}

70ec2e3e11bf5c2c5375d1587a7680e33e844853 · 2025-12-11T19:40:25Z

[docs: update CHANGELOG.md](https://github.com/EndstoneMC/endstone/commit/70ec2e3e11bf5c2c5375d1587a7680e33e844853)

**Change and causal context.** Adds a 0.10.17 changelog section saying crashes fixed and verbose content logs suppressed.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** This commit changes no version macro: stable remains patch16 until 1362 jumps to18. Preserve release prose versus code constants instead of inferring synchronized release metadata.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

<a id="commit-1362"></a>
## Commit 1362 {#commit-1362}

71371baf85ad4dd260d3fd0ec6217c057427eea7 · 2025-12-14T18:23:11Z

[chore: bump version to 0.10.18](https://github.com/EndstoneMC/endstone/commit/71371baf85ad4dd260d3fd0ec6217c057427eea7)

**Change and causal context.** Advances patch constant 16→18 and adds 0.10.18 malformed-login crash-fix release prose. Existing bullet markers are normalized in historical entries.

**Rationale and attribution.** Commit message states the intent; further rationale is inferred only where explicitly labelled.

**Limits and counterexamples.** Changelog date remains December11 although commit is December14. No need to reread unrelated history as new evidence: exact marker-normalization proof accounts for unchanged prose; new entry is read.

Offline full message: message. Full deltas: parent 1.
Author: Vincent; committer: Vincent.

## Context-only bot ancestry {#context-only-bot-ancestry}

The following Dependabot commits update build workflows; each source link preserves its author and committer.

<a id="context-5dfcb9c87d9c95b964b6c3506e92887720cce850"></a>

## Context 5dfcb9c87d9c95b964b6c3506e92887720cce850 {#context-5dfcb9c87d9c95b964b6c3506e92887720cce850}

Dependabot upgrades actions/checkout v5→v6 in six workflows/seven occurrences, preserving existing fetch-depth/submodule options. Docker has two jobs. No permissions or secret values change. Linked PR discussion was not inspected; dependency internals and CI outcomes are not audited.

Author: dependabot[bot]; committer: GitHub. [Commit](https://github.com/EndstoneMC/endstone/commit/5dfcb9c87d9c95b964b6c3506e92887720cce850).

<a id="context-72e85161e6c0dd643af8080155283d262f4f1654"></a>

## Context 72e85161e6c0dd643af8080155283d262f4f1654 {#context-72e85161e6c0dd643af8080155283d262f4f1654}

Dependabot updates cibuildwheel3.2.0→3.2.1 in two workflow files. Full message, bot signoff/coauthor and patch read. Merge1051 imports this exact change; no independent build/release behavior claim.

Author: dependabot[bot]; committer: GitHub. [Commit](https://github.com/EndstoneMC/endstone/commit/72e85161e6c0dd643af8080155283d262f4f1654).

<a id="context-747115ad3dae5ad86b03350d29990f3a04d968a8"></a>

## Context 747115ad3dae5ad86b03350d29990f3a04d968a8 {#context-747115ad3dae5ad86b03350d29990f3a04d968a8}

dependabot updates checkout4 to5 in seven occurrences across six workflows; bot signoff/coauthor retained.

Author: dependabot[bot]; committer: GitHub. [Commit](https://github.com/EndstoneMC/endstone/commit/747115ad3dae5ad86b03350d29990f3a04d968a8).

<a id="context-84cff37a7ea3f745ed2cd78c097233bd0666b175"></a>

## Context 84cff37a7ea3f745ed2cd78c097233bd0666b175 {#context-84cff37a7ea3f745ed2cd78c097233bd0666b175}

Dependabot changes two workflow action references: download-artifact5→6. Full title-only message and patch read; no workflow or action internals run.

Author: dependabot[bot]; committer: GitHub. [Commit](https://github.com/EndstoneMC/endstone/commit/84cff37a7ea3f745ed2cd78c097233bd0666b175).

<a id="context-9c58bfcc0ee61cbd6ffb157ec5933b69499d4e99"></a>

## Context 9c58bfcc0ee61cbd6ffb157ec5933b69499d4e99 {#context-9c58bfcc0ee61cbd6ffb157ec5933b69499d4e99}

Dependabot upgrades pypa/cibuildwheel v3.2.1→v3.3.0 in wheel and Windows-portable workflows, preserving matrix/environment configuration. Linked PR discussion was not inspected; dependency internals and CI outcomes are not audited.

Author: dependabot[bot]; committer: GitHub. [Commit](https://github.com/EndstoneMC/endstone/commit/9c58bfcc0ee61cbd6ffb157ec5933b69499d4e99).

<a id="context-aa2fe8a2d05ae2f419a6ccea0a6fac60e505b723"></a>

## Context aa2fe8a2d05ae2f419a6ccea0a6fac60e505b723 {#context-aa2fe8a2d05ae2f419a6ccea0a6fac60e505b723}

dependabot updates download-artifact4 to5 in two workflows; bot signoff/coauthor retained.

Author: dependabot[bot]; committer: GitHub. [Commit](https://github.com/EndstoneMC/endstone/commit/aa2fe8a2d05ae2f419a6ccea0a6fac60e505b723).

<a id="context-b56974a8b7a2d979427ac5bf6ed5f45a8dd4ce37"></a>

## Context b56974a8b7a2d979427ac5bf6ed5f45a8dd4ce37 {#context-b56974a8b7a2d979427ac5bf6ed5f45a8dd4ce37}

Dependabot updates actions/stale9→10. The60-day stale and15-day close policy remains unchanged. Full workflow delta and title-only message read; no workflow executed.

Author: dependabot[bot]; committer: GitHub. [Commit](https://github.com/EndstoneMC/endstone/commit/b56974a8b7a2d979427ac5bf6ed5f45a8dd4ce37).

<a id="context-bc9ba6bc5bdb9ec1e333c2d994412087ac1d15e0"></a>

## Context bc9ba6bc5bdb9ec1e333c2d994412087ac1d15e0 {#context-bc9ba6bc5bdb9ec1e333c2d994412087ac1d15e0}

Dependabot updates cibuildwheel3.1.4→3.2.0 in two workflows. Full patch/title-only message read. This ancestor connects main1032 to later history; do not mistake target-only parent gaps for disconnected branches.

Author: dependabot[bot]; committer: GitHub. [Commit](https://github.com/EndstoneMC/endstone/commit/bc9ba6bc5bdb9ec1e333c2d994412087ac1d15e0).

<a id="context-bf939797587115ca5054eb9a44980b0861c5b3d1"></a>

## Context bf939797587115ca5054eb9a44980b0861c5b3d1 {#context-bf939797587115ca5054eb9a44980b0861c5b3d1}

Dependabot changes two workflow action references: upload-artifact4→5. Full title-only message and patch read; no workflow or action internals run.

Author: dependabot[bot]; committer: GitHub. [Commit](https://github.com/EndstoneMC/endstone/commit/bf939797587115ca5054eb9a44980b0861c5b3d1).

<a id="context-e44194138c9279ffe45cddce1d3e89e623fd15c8"></a>

## Context e44194138c9279ffe45cddce1d3e89e623fd15c8 {#context-e44194138c9279ffe45cddce1d3e89e623fd15c8}

Dependabot updates cibuildwheel3.1.3→3.1.4 in two workflow files. Full bump message and explicit bot signoff/coauthor read; declared wheel workflows are not observed successful builds.

Author: dependabot[bot]; committer: GitHub. [Commit](https://github.com/EndstoneMC/endstone/commit/e44194138c9279ffe45cddce1d3e89e623fd15c8).

<a id="context-f00efc635bb349244a2d4c350e129e06cf952088"></a>

## Context f00efc635bb349244a2d4c350e129e06cf952088 {#context-f00efc635bb349244a2d4c350e129e06cf952088}

Dependabot updates actions/setup-python5→6 in CI, coverage and docs. Python3.12/3.11/3.x selections remain. Full patch/title-only message read; dependency internals and workflow outcomes unvalidated.

Author: dependabot[bot]; committer: GitHub. [Commit](https://github.com/EndstoneMC/endstone/commit/f00efc635bb349244a2d4c350e129e06cf952088).
