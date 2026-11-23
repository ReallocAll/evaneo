<!-- retrieval: {"source_ids":["public:context-commit:1c6b6785e40930f224a18650be3477b2d8c13406","public:context-commit:2591031eccc0618da853872a0d72f0c7688ec881","public:context-commit:2f66fb0347a3c81e70e33af7c3627c6f0a0e4cdb","public:context-commit:6e06c413edb1cc352dbd52ca893cce7f9cf0fcc1","public:context-commit:d839b8ac7b37d5f6e024635686349f6bec86e74a","public:context-commit:fe98430eece665704d743d27ef8464847aff60ae"],"source_type":"public","topics":["testing","build","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Context commit reading and synthesis mappings {#context-commit-reading-and-synthesis-mappings}

Six contextual commits were examined in the original static review: six commit messages and seven direct-parent deltas. The earlier internal JSON reports, extracted diff files and their hashes are not distributed, so those pointers cannot be independently checked by Evaneo readers. The public commits and parent comparisons below provide accessible revision evidence; no new target scope or independent execution is claimed.

These six contextual commits are not part of the 95 commits reviewed in the main sequence. No work from them is credited to the principal commit author. Complete parent-delta review does not imply review of every ancestor or execution of any dependency/vendor binary.

<a id="context-d839b8ac7b37d5f6e024635686349f6bec86e74a"></a>

## Context d839b8ac7b37d5f6e024635686349f6bec86e74a {#context-d839b8ac7b37d5f6e024635686349f6bec86e74a}

### Automated 1.21.31 metadata entering the origin/main merge {#automated-1-21-31-metadata-entering-the-origin-main-merge}

[Public source](https://github.com/EndstoneMC/bedrock-server-data/commit/d839b8ac7b37d5f6e024635686349f6bec86e74a)

Adds one Windows/Linux pair for Bedrock 1.21.31.04 under aggregate key 1.21.31. The complete 22-line parent delta contains the two distinct digests and platform-specific minecraft.net URLs, with no updater-code change. The later target merge a0d53fa8ac0033ed57e75a4881d6e431365ef647 preserves this record alongside the local 1.21.40 record; existing parsed proof establishes the resulting mapping is exactly the union of both target parents.

Attribution: The verified Git author header says wu-vincent and the committer is github-actions[bot]. That literal identity plus automated data role is retained; this context is not added to the set of GitHub-attributed commits, and no independent human implementation preference is inferred from the generated record.

### Public revision evidence {#exact-reading-components}

- Commit message and recorded authorship: [public commit](https://github.com/EndstoneMC/bedrock-server-data/commit/d839b8ac7b37d5f6e024635686349f6bec86e74a).

- Parent 1 (`ee9a3056ecae`): [public parent-to-commit comparison](https://github.com/EndstoneMC/bedrock-server-data/compare/ee9a3056ecae3d7b18e486cc8af621b9e27c028b...d839b8ac7b37d5f6e024635686349f6bec86e74a) (reported 22-line delta).

### Synthesis and limits {#synthesis-and-limits}

Existing consuming analysis: [bedrock-server-data-review.md](bedrock-server-data-review.md), lines 117–130; target integration: [a0d53fa8ac00](https://github.com/EndstoneMC/bedrock-server-data/commit/a0d53fa8ac0033ed57e75a4881d6e431365ef647).

Knowledge: [cases/bedrock-server-data-schema-platform-migrations.md](cases/bedrock-server-data-schema-platform-migrations.md).

- The supplied hashes were not recomputed from vendor binaries.

- The commit message supplies no further rationale; generated metadata is not authored vendor binary code.

- Static source/context review only; no upstream execution or artifact download.

- Scope: complete message and every parent delta; no credit to the principal author, no additional commit added to the review, no upstream execution.

<a id="context-2591031eccc0618da853872a0d72f0c7688ec881"></a>

## Context 2591031eccc0618da853872a0d72f0c7688ec881 {#context-2591031eccc0618da853872a0d72f0c7688ec881}

### Purple synchronizes the contribution branch with v2 {#purple-synchronizes-the-contribution-branch-with-v2}

[Public source](https://github.com/EndstoneMC/bedrock-server-data/commit/2591031eccc0618da853872a0d72f0c7688ec881)

This is a two-parent contributor merge. Relative to fe98430eece665704d743d27ef8464847aff60ae, its 34-line delta imports release 1.21.131 metadata and advances that release registry entry. Relative to d3f8e7518e42482c8015774e330373b332d97787, its 32-line delta retains Purple's historical preview 1.26.0-preview.23 and inserts it below newer previews without changing preview latest. Both full parent deltas were already read. The later target integration fa099cd4539c705897cd8fccef4440128102906a additionally retains main's newer preview .26; the existing proof verifies contributor metadata equality and preservation of prior preview order/latest.

Attribution: Purple is the Git author and GitHub is the committer. Synchronizing upstream release data into a contributor branch does not make Purple or the target the author of vendor binaries or all upstream metadata. The target receives only the separately documented later integration credit.

### Public revision evidence {#exact-reading-components-2}

- Commit message and recorded authorship: [public commit](https://github.com/EndstoneMC/bedrock-server-data/commit/2591031eccc0618da853872a0d72f0c7688ec881).

- Parent 1 (`fe98430eece6`): [public parent-to-commit comparison](https://github.com/EndstoneMC/bedrock-server-data/compare/fe98430eece665704d743d27ef8464847aff60ae...2591031eccc0618da853872a0d72f0c7688ec881) (reported 34-line delta).

- Parent 2 (`d3f8e7518e42`): [public parent-to-commit comparison](https://github.com/EndstoneMC/bedrock-server-data/compare/d3f8e7518e42482c8015774e330373b332d97787...2591031eccc0618da853872a0d72f0c7688ec881) (reported 32-line delta).

### Synthesis and limits {#synthesis-and-limits-2}

Existing consuming analysis: [bedrock-server-data-review.md](bedrock-server-data-review.md), lines 383–396; target integration: [fa099cd4539c](https://github.com/EndstoneMC/bedrock-server-data/commit/fa099cd4539c705897cd8fccef4440128102906a).

Knowledge: [cases/bedrock-server-data-schema-platform-migrations.md](cases/bedrock-server-data-schema-platform-migrations.md), [cases/bedrock-server-data-download-provenance-and-backfill.md](cases/bedrock-server-data-download-provenance-and-backfill.md).

- No archive download/hash recomputation or runtime validation.

- This is complete message/all-parent-delta context review, not a new independent review of every historical ancestor of either branch.

- Static source/context review only; no upstream execution or artifact download.

- Scope: complete message and every parent delta; no credit to the principal author, no additional commit added to the review, no upstream execution.

<a id="context-fe98430eece665704d743d27ef8464847aff60ae"></a>

## Context fe98430eece665704d743d27ef8464847aff60ae {#context-fe98430eece665704d743d27ef8464847aff60ae}

### Purple adds the historical preview .23 record {#purple-adds-the-historical-preview-23-record}

[Public source](https://github.com/EndstoneMC/bedrock-server-data/commit/fe98430eece665704d743d27ef8464847aff60ae)

Adds preview/1.26.0-preview.23/metadata.json with version, two platform URLs and distinct SHA256 fields, plus one insertion in versions.json between preview .24 and the older 1.21.130 series. The 32-line delta does not move latest back to the historical discovery. Its metadata blob is preserved through contributor synchronization 2591031eccc0618da853872a0d72f0c7688ec881 and target integration fa099cd4539c705897cd8fccef4440128102906a. This is a concrete contrast to the updater's generic arrival-at-head registry behavior, not a new algorithm implementation in this data commit.

Attribution: Purple is both Git author and committer. Purple/purple-blog receives the contributed metadata credit; the target's later merge does not establish commit authorship of this patch.

### Public revision evidence {#exact-reading-components-3}

- Commit message and recorded authorship: [public commit](https://github.com/EndstoneMC/bedrock-server-data/commit/fe98430eece665704d743d27ef8464847aff60ae).

- Parent 1 (`7469a9e45c48`): [public parent-to-commit comparison](https://github.com/EndstoneMC/bedrock-server-data/compare/7469a9e45c48148110bbc5170f9ab78f645ac99c...fe98430eece665704d743d27ef8464847aff60ae) (reported 32-line delta).

### Synthesis and limits {#synthesis-and-limits-3}

Existing consuming analysis: [bedrock-server-data-review.md](bedrock-server-data-review.md), lines 383–396; target integration: [fa099cd4539c](https://github.com/EndstoneMC/bedrock-server-data/commit/fa099cd4539c705897cd8fccef4440128102906a).

Knowledge: [cases/bedrock-server-data-schema-platform-migrations.md](cases/bedrock-server-data-schema-platform-migrations.md), [cases/bedrock-server-data-download-provenance-and-backfill.md](cases/bedrock-server-data-download-provenance-and-backfill.md).

- Message is a one-line metadata description, without an independently documented discovery or hashing method.

- Digest shape and source identity were checked; artifact authenticity and availability were not tested.

- Static source/context review only; no upstream execution or artifact download.

- Scope: complete message and every parent delta; no credit to the principal author, no additional commit added to the review, no upstream execution.

<a id="context-1c6b6785e40930f224a18650be3477b2d8c13406"></a>

## Context 1c6b6785e40930f224a18650be3477b2d8c13406 {#context-1c6b6785e40930f224a18650be3477b2d8c13406}

### Purple completes the preview .21 Windows metadata {#purple-completes-the-preview-21-windows-metadata}

[Public source](https://github.com/EndstoneMC/bedrock-server-data/commit/1c6b6785e40930f224a18650be3477b2d8c13406)

Adds the missing Windows URL and SHA256 for 1.26.10-preview.21 while keeping the existing Linux record. The complete 15-line parent delta contains only that two-leaf metadata addition. Merge 46cdb71d73a6e05ebafbc779494094b25cd922fb has the exact incoming tree and an empty second-parent delta, proving unchanged integration with no merge resolution by the commit author.

Attribution: Purple is both Git author and committer. A later commit merged the contribution unchanged; no content is credited to its author.

### Public revision evidence {#exact-reading-components-4}

- Commit message and recorded authorship: [public commit](https://github.com/EndstoneMC/bedrock-server-data/commit/1c6b6785e40930f224a18650be3477b2d8c13406).

- Parent 1 (`f0c116ba261a`): [public parent-to-commit comparison](https://github.com/EndstoneMC/bedrock-server-data/compare/f0c116ba261a62c124ae83fd7fc81216b4c62c45...1c6b6785e40930f224a18650be3477b2d8c13406) (reported 15-line delta).

### Synthesis and limits {#synthesis-and-limits-4}

Existing consuming analysis: [bedrock-server-data-review.md](bedrock-server-data-review.md), lines 397–410; target integration: [46cdb71d73a6](https://github.com/EndstoneMC/bedrock-server-data/commit/46cdb71d73a6e05ebafbc779494094b25cd922fb).

Knowledge: [cases/bedrock-server-data-schema-platform-migrations.md](cases/bedrock-server-data-schema-platform-migrations.md), [cases/bedrock-server-data-download-provenance-and-backfill.md](cases/bedrock-server-data-download-provenance-and-backfill.md).

- The two platform hashes are distinct but were not verified by redownloading binaries.

- This record does not establish why the upstream endpoint previously omitted the platform or when the artifact became available.

- Static source/context review only; no upstream execution or artifact download.

- Scope: complete message and every parent delta; no credit to the principal author, no additional commit added to the review, no upstream execution.

<a id="context-6e06c413edb1cc352dbd52ca893cce7f9cf0fcc1"></a>

## Context 6e06c413edb1cc352dbd52ca893cce7f9cf0fcc1 {#context-6e06c413edb1cc352dbd52ca893cce7f9cf0fcc1}

### Dependabot proposes setup-python 5 to 6 {#dependabot-proposes-setup-python-5-to-6}

[Public source](https://github.com/EndstoneMC/bedrock-server-data/commit/6e06c413edb1cc352dbd52ca893cce7f9cf0fcc1)

The complete 13-line delta changes only actions/setup-python@v5 to @v6 in the updater workflow, retaining Python 3.11 configuration. The full 15-line bot message identifies a semver-major direct production dependency update, links release notes/commits and includes its sign-off. Target merge 5fca64d517d949dffaf6099cbf0bb2bbccf6e476 exactly equals the incoming tree; no target-specific patch is introduced.

Attribution: Dependabot is the Git author and GitHub the committer. The bot owns the proposal; the target's role is the separately recorded integration. Inheriting the changed workflow does not make the target its sole author.

### Public revision evidence {#exact-reading-components-5}

- Commit message and recorded authorship: [public commit](https://github.com/EndstoneMC/bedrock-server-data/commit/6e06c413edb1cc352dbd52ca893cce7f9cf0fcc1).

- Parent 1 (`c0f78d2f9ebd`): [public parent-to-commit comparison](https://github.com/EndstoneMC/bedrock-server-data/compare/c0f78d2f9ebd6ca5db2149b86e6077a0053e61f6...6e06c413edb1cc352dbd52ca893cce7f9cf0fcc1) (reported 13-line delta).

### Synthesis and limits {#synthesis-and-limits-5}

Existing consuming analysis: [bedrock-server-data-review.md](bedrock-server-data-review.md), lines 453–466; target integration: [5fca64d517d9](https://github.com/EndstoneMC/bedrock-server-data/commit/5fca64d517d949dffaf6099cbf0bb2bbccf6e476).

Knowledge: [cases/bedrock-server-data-generated-data-publication.md](cases/bedrock-server-data-generated-data-publication.md).

- The linked action upstream implementation/release notes were not independently reviewed in this bounded context.

- The workflow/action was not executed; no successful compatibility/security test is claimed.

- Static source/context review only; no upstream execution or artifact download.

- Scope: complete message and every parent delta; no credit to the principal author, no additional commit added to the review, no upstream execution.

<a id="context-2f66fb0347a3c81e70e33af7c3627c6f0a0e4cdb"></a>

## Context 2f66fb0347a3c81e70e33af7c3627c6f0a0e4cdb {#context-2f66fb0347a3c81e70e33af7c3627c6f0a0e4cdb}

### Dependabot widens the uv_build build requirement {#dependabot-widens-the-uvbuild-build-requirement}

[Public source](https://github.com/EndstoneMC/stubgen/commit/2f66fb0347a3c81e70e33af7c3627c6f0a0e4cdb)

The complete 13-line pyproject delta changes the uv_build upper bound from <0.9.0 to <0.11.0 while preserving >=0.8.17 and the uv_build backend. Its merge-style subject does not imply a two-parent merge: the verified object has one parent, a21d550b4d85fb8ab77f9b43985bf18a9984c87f. This explains the build requirement inherited by target a2ef084254a96268385536f5c27c614a2156eb2d; the later extension split did not author this requirement widening.

Attribution: Dependabot is the Git author and GitHub the committer. This is dependency-maintenance context; it does not establish the principal author’s preference or add a commit to the review.

### Public revision evidence {#exact-reading-components-6}

- Commit message and recorded authorship: [public commit](https://github.com/EndstoneMC/stubgen/commit/2f66fb0347a3c81e70e33af7c3627c6f0a0e4cdb).

- Parent 1 (`a21d550b4d85`): [public parent-to-commit comparison](https://github.com/EndstoneMC/stubgen/compare/a21d550b4d85fb8ab77f9b43985bf18a9984c87f...2f66fb0347a3c81e70e33af7c3627c6f0a0e4cdb) (reported 13-line delta).

### Synthesis and limits {#synthesis-and-limits-6}

Existing consuming analysis: [stubgen-review.md](stubgen-review.md), lines 257–270; target integration: [a2ef084254a9](https://github.com/EndstoneMC/stubgen/commit/a2ef084254a96268385536f5c27c614a2156eb2d).

Knowledge: [cases/stubgen-release-provenance.md](cases/stubgen-release-provenance.md).

- The uv_build implementation and newly allowed releases were not audited or executed.

- A widened constraint expresses allowed resolution range, not proof every newly allowed version builds this package successfully.

- Static source/context review only; no upstream execution or artifact download.

- Scope: complete message and every parent delta; no credit to the principal author, no additional commit added to the review, no upstream execution.
