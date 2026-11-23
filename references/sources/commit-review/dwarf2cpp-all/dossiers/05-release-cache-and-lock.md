<!-- retrieval: {"source_ids":["public:commit:154e45a835f3b9dc3964a12b36876b9e3598f02c","public:commit:1cc96f70f0030bb883ed2c1f626997085839c00e","public:commit:3bea9b4b83eb2faa9c5a4157b34dd4561cf8c2a3","public:commit:77d525823889d0fef38e556d1fb61d39d6cb826a","public:commit:85e8fd16bbf79edf571ab26b5754869de427078f"],"source_type":"public","date":"2026-05-16","topics":["lifetime","concurrency","build","diagnosis","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="dwarf2cpp-release-cache-and-lock"></a>
# Dwarf2cpp: release cache and lock {#dwarf2cpp-release-cache-and-lock}

Each dossier presents its commits in causal DAG order. The numbering is stable;94 precedes93 because93 is its child. Read the cross-cutting [engineering synthesis](../ENGINEERING_SYNTHESIS.md) for revision chains, applicability, counterexamples and validation limits.


<a id="commit-094"></a>
## 094. fix(build): bump Windows Conan compiler.version to 194 {#commit-094}

- Commit: [85e8fd16bbf79edf571ab26b5754869de427078f](https://github.com/EndstoneMC/dwarf2cpp/commit/85e8fd16bbf79edf571ab26b5754869de427078f)
- Date: 2026-05-16T16:19:43Z; parent(s): f96cfc99d1a0dae6ddd904d1b99752613adfaff3
- Exact reading: diff parent1 lines1–26; message parent1 lines1–7
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Changes Windows Conan compiler.version193 to194 in pyproject and agent guide. Message diagnoses windows-latest MSVC19.44 lacking toolset14.3, causing libiconv source build vcvars failure. This is a reported environment diagnosis, not a reproduced measurement. Parent of93 in the actual DAG.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-093"></a>
## 093. ci: cache Conan packages across wheel builds {#commit-093}

- Commit: [1cc96f70f0030bb883ed2c1f626997085839c00e](https://github.com/EndstoneMC/dwarf2cpp/commit/1cc96f70f0030bb883ed2c1f626997085839c00e)
- Date: 2026-05-16T16:19:43Z; parent(s): 85e8fd16bbf79edf571ab26b5754869de427078f
- Exact reading: diff parent1 lines1–49; message parent1 lines1–6
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Caches ~/.conan2 per runner OS and conanfile.txt hash in build/release and volume-mounts host cache into Linux container. Explicit goal is dependency reuse; no cache timing measurements. Commit94 is the causal parent despite93's earlier timestamp. After98 relocates Conan home, this mount becomes unused and109 repairs it.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-095"></a>
## 095. ci: reclaim Conan cache ownership after Linux container builds {#commit-095}

- Commit: [77d525823889d0fef38e556d1fb61d39d6cb826a](https://github.com/EndstoneMC/dwarf2cpp/commit/77d525823889d0fef38e556d1fb61d39d6cb826a)
- Date: 2026-05-16T17:27:48Z; parent(s): 1cc96f70f0030bb883ed2c1f626997085839c00e
- Exact reading: diff parent1 lines1–34; message parent1 lines1–6
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Adds always-on-Linux ownership reclamation after wheel builds in both workflows. Message explains Docker root-owned cache files prevent unprivileged actions/cache post-step tar. Scoped operational correction, not evidence that all cache errors are ownership errors or that builds passed.

The complete message source linked above records any explicit diagnosis. Behavioral explanation is static analysis; no successful execution is inferred.


<a id="commit-096"></a>
## 096. Merge branch 'main' of github.com:EndstoneMC/dwarf2cpp {#commit-096}

- Commit: [3bea9b4b83eb2faa9c5a4157b34dd4561cf8c2a3](https://github.com/EndstoneMC/dwarf2cpp/commit/3bea9b4b83eb2faa9c5a4157b34dd4561cf8c2a3)
- Date: 2026-05-16T17:28:11Z; parent(s): 77d525823889d0fef38e556d1fb61d39d6cb826a, db1577c499886530598e0cc663ddf44c30910dde
- Exact reading: diff parent1 lines1–13; diff parent2 lines1–34; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Two-parent merge composes95 cache ownership fix and github-actions bot release commitdb1577c. First-parent patch only adds dated0.1.0 heading; second-parent patch is byte-identical to95 verified full-index diff. No novel conflict-resolution algorithm. Preserve bot release authorship and do not count duplicated cache patch as another independent lesson.


<a id="commit-097"></a>
## 097. chore: track uv.lock, ignore .claude/ {#commit-097}

- Commit: [154e45a835f3b9dc3964a12b36876b9e3598f02c](https://github.com/EndstoneMC/dwarf2cpp/commit/154e45a835f3b9dc3964a12b36876b9e3598f02c)
- Date: 2026-05-16T17:37:58Z; parent(s): 3bea9b4b83eb2faa9c5a4157b34dd4561cf8c2a3
- Exact reading: diff parent1 lines1–193; message parent1 lines1–1
- Attribution: GitHub-linked wu-vincent author, not exclusive authorship of copied dependencies or merged work.

Tracks173-line uv.lock and ignores .claude/. Entire TOML parsed structurally:8 package records,90 artifact records, full dependency edges/markers/version/source/filename/size/timestamps and SHA256 shapes examined; digest literals are integrity metadata, not independent reasoning. Locks click8.3.3,colorama0.4.6,jinja2 3.1.6,lazy-loader0.5,markupsafe3.0.3,packaging26.2,tqdm4.67.3 plus editable project0.1.0. All artifact URLs point to HTTPS files.pythonhosted.org. No downloaded artifact hash/content verification. Lock requires-python>=3.10 remains unchanged after101 raises project>=3.12.
