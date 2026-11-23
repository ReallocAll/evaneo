<!-- retrieval: {"source_ids":["public:commit:1f5b2f40d4646ec6cf334bef4831776b5a20b2ba","public:commit:5a02eeb2b1387b20a9e35b0cede031e9502ac4b5","public:commit:84327b08f67205946d5ce8d56e3f0eae53886740","public:commit:e0fed8fb22384251676c6477751304719d65a41d","public:commit:fa33de07c476b06b9ad52a694b1b0545d246a931","public:context-commit:207f439c599a589485218f34af61caa7c9e1ddf3","public:context-commit:4abf54a10805c484086637870546b0483fad687e","public:context-commit:5969cb5fc9fb4008e19e1a20c468ede6d7eb4a06","public:context-commit:8046b602d2c0c93ff1f4951b7f42de341364bdbf","public:context-commit:8aeb44d05385daf9e760e627be7ddd354a352434","public:thread:EndstoneMC/endstone:174"],"source_type":"public","date":"2025-03-18..2025-04-16","topics":["ffi","testing","build","documentation","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="merge-integration-collaborator-credit-and-review-limits"></a>
# Merge integration, collaborator credit and review limits {#merge-integration-collaborator-credit-and-review-limits}

<a id="exact-coverage-and-causal-reuse"></a>
## Exact coverage and causal reuse {#exact-coverage-and-causal-reuse}

This 2025 history covers changes around commits 401–500, including branch merges at 408, 418, 419, 421 and 446. The merge entries distinguish original contributors from integration changes.

Merges 419 and 446 have no content difference from their second-parent trees. Other integrations combine branch changes described below.

PR149 and PR174 provide context for changes imported by these branches. Apache notices retain their source text and copyright lines. Symbol-table changes do not establish compatibility with a running server.

## Collaborators and public discussion {#collaborators-and-public-discussion}

421 imports four daoge/smartcmd commits: 8046b602 introduces a tint enum; 5969cb5 revises it; 207f439 adopts TintMethod, including DryFoliage and JSON tintMethod; 8aeb44d removes header-only CMake registration after Wu review.

446 imports killcerr's --recurse-submodule README change. PR163 has no description or human review; its Codecov report is an automated claim, not a verified test result.

Issue159 records MipaSenpai's report and Wu's response; commit 455 contains the code fix. PR149 reports preliminary Windows/Linux testing to reduce later port work; this remains author-reported. Commit 453 cites PocketMine-MP for client-pack flag reasoning.

## Static limits and reproducibility {#static-limits-and-reproducibility}

No upstream source, tests, generators, builds or native executables were run. The linked public commits document historical source changes, not current upstream status or runtime ABI behavior.

Intermediate repairs and intentionally changed contracts are distinguished from limitations that persist in the reviewed source. Runtime crashes, ABI correctness and present-day support were not independently verified.

<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}


<a id="commit-408"></a>
### 408. Merge remote-tracking branch 'origin/main' into feat/1.21.70-support {#commit-408}

[1f5b2f40d4646ec6cf334bef4831776b5a20b2ba](https://github.com/EndstoneMC/endstone/commit/1f5b2f40d4646ec6cf334bef4831776b5a20b2ba) · 2025-03-18T17:43:48Z · author Vincent.

Parents: `0d05e555d44e05e7e997ee8c3b03904b20619cde`, `56b514781cb89a0a42fc17b51435dfdd61bc8cb3`. Read displays: parent 1, parent 2.

Merges main through407 into the1.21.70-support branch rooted at prior393. Both parent messages/deltas accounted for:53 exact prior PR149 file occurrences and12 exact merge-base/other-parent full-file blob+hunk matches avoid repeated implementation reading; all residual headers/deletions read. Imports plugin/parser/build work while preserving preview-only ABI state. This is integration of already-reviewed ancestry, not an additional new resolver or port implementation.

All-parent changed-file occurrences: 68. Exact prior PR reuse: 53; exact reviewed-ancestry file reuse: 12.


<a id="commit-418"></a>
### 418. Merge remote-tracking branch 'origin/main' into feat/1.21.70-support {#commit-418}

[5a02eeb2b1387b20a9e35b0cede031e9502ac4b5](https://github.com/EndstoneMC/endstone/commit/5a02eeb2b1387b20a9e35b0cede031e9502ac4b5) · 2025-03-20T18:20:46Z · author Vincent.

Parents: `05ddc5ea259cb7df846d4718f84f6349e38eb2eb`, `491f13a67ef01a56f7357ed62d87200963f9511d`. Read displays: parent 1, parent 2.

Merges main409–416 into preview. Both parent deltas and meaningful residuals read; exact PR149/branch full-file identities account for repeated implementations. Integrates new map/meta/server accessor with preview ABI state.

All-parent changed-file occurrences: 83. Exact prior PR reuse: 57; exact reviewed-ancestry file reuse: 16.


<a id="commit-419"></a>
### 419. [feature] 1.21.70 support (#149) {#commit-419}

[fa33de07c476b06b9ad52a694b1b0545d246a931](https://github.com/EndstoneMC/endstone/commit/fa33de07c476b06b9ad52a694b1b0545d246a931) · 2025-03-21T13:19:34Z · author Vincent.

Parents: `491f13a67ef01a56f7357ed62d87200963f9511d`, `5a02eeb2b1387b20a9e35b0cede031e9502ac4b5`. Read displays: parent 1, parent 2.

Merges PR149 preview support. Full message reports preliminary preview beta26 Windows/Linux testing and goal of reducing final-release work; those are author-reported historical claims, not independently verified runtime results. Prior verified PR149 patch identities reused, residual header deletion/addition read; second-parent diff empty.

All-parent changed-file occurrences: 59. Exact prior PR reuse: 57; exact reviewed-ancestry file reuse: 0.


<a id="commit-421"></a>
### 421. feat(devtools): dump tint type for blocks (#161) {#commit-421}

[84327b08f67205946d5ce8d56e3f0eae53886740](https://github.com/EndstoneMC/endstone/commit/84327b08f67205946d5ce8d56e3f0eae53886740) · 2025-03-21T15:32:30Z · author Vincent.

Parents: `b59a30edc28743d3d874ff9987ce2495357c38bb`, `8aeb44d05385daf9e760e627be7ddd354a352434`. Read displays: parent 1, parent 2.

Merges daoge/smartcmd PR161 tintMethod feature after four full context commits. Final uint8 enum has None0, DefaultFoliage1, Birch2, Evergreen3, DryFoliage4, Grass5, Water6, Stem7, Redstone8, Size9; getter/export uses tintMethod. Intermediate wrong enum layouts were corrected before merge. Both parent deltas verified; preserve collaborator authorship.

All-parent changed-file occurrences: 7. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 6.


<a id="commit-446"></a>
### 446. docs: add --recurse-submodule to build instructions (#163) {#commit-446}

[e0fed8fb22384251676c6477751304719d65a41d](https://github.com/EndstoneMC/endstone/commit/e0fed8fb22384251676c6477751304719d65a41d) · 2025-03-22T12:45:15Z · author Vincent.

Parents: `19ab9039c2779d4c06dd3b0470630d87180b4e39`, `4abf54a10805c484086637870546b0483fad687e`. Read displays: parent 1, parent 2.

Integrates killcerr README clone --recurse-submodule change via PR163, preserving collaborator patch credit. Both parents read/proven; second-parent tree diff empty. Public PR163 has null body, no reviews/inline comments, one Codecov bot coverage report read as reported output, not executed proof.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 1.
