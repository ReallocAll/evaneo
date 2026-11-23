<!-- retrieval: {"source_ids":["public:commit:effc8d8b9dd37a6b9a89b4db58a7873cf5a427d7"],"source_type":"public","date":"2026-05-04","topics":["build","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="081-publish-each-dump-to-endstonemc-protocol-docs-on-a-per-update-branch"></a>
# 081. Publish each dump to EndstoneMC/protocol-docs on a per-update branch {#081-publish-each-dump-to-endstonemc-protocol-docs-on-a-per-update-branch}

Source: [effc8d8b9dd37a6b9a89b4db58a7873cf5a427d7](https://github.com/EndstoneMC/protocol-dumper/commit/effc8d8b9dd37a6b9a89b4db58a7873cf5a427d7)  
Date: 2026-05-04T13:40:27Z  
Causal parent: 143c54a6adb26ae64ac151f5730c0744d107f61b

## Change, rationale, and limits {#change-rationale-and-limits}

Publishes dump snapshots to protocol-docs update branches, preserves branch history, avoids no-change commits, uses GitHub Actions identity and secret. Guard redacts one credential-bearing URL-expression line; neither inspected nor reconstructed. Publication config is studied, not executed or proof of actual publication.

This finding comes from the actual message and all meaningful patch changes in causal order. Explicit reasons are marked as message/author statements; implementation observations do not establish hidden intent. A terse title is not expanded into invented alternatives or outcomes. Read the [cross-commit synthesis](../ENGINEERING_SYNTHESIS.md) for reversals, final-state differences and applicable task families.

## Changed surfaces {#changed-surfaces}

- .github/workflows/dump.yml

## Attribution {#attribution}

GitHub author: wu-vincent; Git author name Vincent. Original external mechanisms and mirrored BDS types remain credited separately.

- Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>

## Evidence limits {#local-evidence-and-review-status}

Credential-like line(s) remain opaque under the extractor guard. No upstream execution, binary/ABI measurement, generated-tree recount, CI success or runtime equivalence is claimed. The patch contains no repository-owned automated test addition; operational CI and reported manual checks are distinguished in the analysis.
