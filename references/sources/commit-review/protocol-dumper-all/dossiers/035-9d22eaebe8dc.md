<!-- retrieval: {"source_ids":["public:commit:9d22eaebe8dc5d0c8aed5d8927bee01a8b9077e0"],"source_type":"public","date":"2026-04-18","topics":["testing","build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="035-add-github-actions-ci-cd-workflow"></a>
# 035. Add GitHub Actions CI/CD workflow {#035-add-github-actions-ci-cd-workflow}

Source: [9d22eaebe8dc5d0c8aed5d8927bee01a8b9077e0](https://github.com/EndstoneMC/protocol-dumper/commit/9d22eaebe8dc5d0c8aed5d8927bee01a8b9077e0)  
Date: 2026-04-18T20:48:24Z  
Causal parent: c161dc1cd14314d9761aedbeb0a828b51f62fcd9

## Change, rationale, and limits {#change-rationale-and-limits}

Adds Windows push/PR master and v-tag build/artifact/release workflows using LLVM, Ninja and presets. No automated test added. Release artifacts and master trigger are source configuration, not confirmed successful runs. Claude Opus 4.6 credit.

This finding comes from the actual message and all meaningful patch changes in causal order. Explicit reasons are marked as message/author statements; implementation observations do not establish hidden intent. A terse title is not expanded into invented alternatives or outcomes. Read the [cross-commit synthesis](../ENGINEERING_SYNTHESIS.md) for reversals, final-state differences and applicable task families.

## Changed surfaces {#changed-surfaces}

- .github/workflows/build.yml

## Attribution {#attribution}

GitHub author: wu-vincent; Git author name Vincent. Original external mechanisms and mirrored BDS types remain credited separately.

- Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

## Evidence limits {#local-evidence-and-review-status}

No upstream execution, binary/ABI measurement, generated-tree recount, CI success or runtime equivalence is claimed. The patch contains no repository-owned automated test addition; operational CI and reported manual checks are distinguished in the analysis.
