<!-- retrieval: {"source_type":"public","topics":["build","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="context-commit-fbe2d4d46b5d4f8cf54add19d1c03e27a30db7dd"></a>
# Context commit fbe2d4d46b5d4f8cf54add19d1c03e27a30db7dd {#context-commit-fbe2d4d46b5d4f8cf54add19d1c03e27a30db7dd}

<a id="context-provenance"></a>
## Provenance {#context-provenance}

Public source: https://github.com/EndstoneMC/endstone/commit/fbe2d4d46b5d4f8cf54add19d1c03e27a30db7dd

This is historical integration/dependency context. A net branch delta, generated structure, or bounded review does not establish coverage of every intermediate implementation; reported outcomes were not independently reproduced.

<a id="source-analysis"></a>
## Source analysis {#source-analysis}

Summary: Bumps download-artifact 6 to 7 in wheel and Windows-portable publication jobs. Existing artifact patterns and dist paths are unchanged; whole final workflow context retains merge-multiple and release-published gating.

Limits: Verified version-substitution-only disposition; no download, publish, or runner compatibility was tested.

Limits: Whole final workflow context is a later descendant read, not claimed to be byte-identical at every earlier context commit.

Limits: No source dependency audit, workflow execution, download, installation, build or upstream mutation.

Authorship / git author name: dependabot[bot]

Review scope: Static review of the linked commit and its parent diff; no workflow execution is claimed.
Changed workflow paths and inspected hunks:
- `.github/workflows/wheel.yml` — `@@ -86,7 +86,7 @@ jobs:`
- `.github/workflows/windows-portable.yml` — `@@ -97,7 +97,7 @@ jobs:`
Later workflow context consulted: `545efac3af53b201b4cb1b4fa072684f7a3e9c63`, `9c16f1239c6f5cbb30923cbe7da0115d4e29327e` (not a byte-identical snapshot of every earlier revision).

[Associated detailed analysis](../sources/commit-review/endstone-2026-merge-closure/dossiers.md#context-fbe2d4d46b5d4f8cf54add19d1c03e27a30db7dd)
