<!-- retrieval: {"source_type":"public","date":"2025-06-29","topics":["ffi","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="context-commit-ea5e0bfbc7274ea5a9f0c3d0e6fbcfb759bc7ee7"></a>
# Context commit ea5e0bfbc7274ea5a9f0c3d0e6fbcfb759bc7ee7 {#context-commit-ea5e0bfbc7274ea5a9f0c3d0e6fbcfb759bc7ee7}

<a id="context-provenance"></a>
## Provenance {#context-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/ea5e0bfbc7274ea5a9f0c3d0e6fbcfb759bc7ee7

This is historical integration/dependency context. A net branch delta, generated structure, or bounded review does not establish coverage of every intermediate implementation; reported outcomes were not independently reproduced.

<a id="source-analysis"></a>
## Source analysis {#source-analysis}

Summary: killcerr authors squash PR209, GitHub commits it; explicit trailers credit killcerr under another email and Vincent. Adds cancellable LeavesDecayEvent and native LeavesBlock::_die pre-operation hook, current block wrapper, platform symbols, Python surface and runtime build entry. Cancel returns before original decay. No tests; no guarantee every visual leaf disappearance uses this hook. Main branch adds these symbols after the v0.9 version branch fork, so later symbol-table merges require preserving and updating them.

Attribution: Actual Git author/committer and all explicit credit trailers retained; review and merge are not blanket implementation authorship.

Explicit credit lines: Co-authored-by: killcerr

Explicit credit lines: Co-authored-by: Vincent

Author: killcerr

[Associated detailed analysis](../sources/commit-review/endstone-2025-0801-0900/03-native-block-events.md#context-ea5e0bfbc7274ea5a9f0c3d0e6fbcfb759bc7ee7)
