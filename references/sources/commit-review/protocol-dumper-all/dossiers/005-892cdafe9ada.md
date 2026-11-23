<!-- retrieval: {"source_ids":["public:commit:892cdafe9ada26c0cbaf17328b49cf0ab2601bfd"],"source_type":"public","date":"2026-04-11","topics":["ffi","build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="005-pin-entt-to-latest-commit-1333fa5"></a>
# 005. Pin entt to latest commit (1333fa5) {#005-pin-entt-to-latest-commit-1333fa5}

Source: [892cdafe9ada26c0cbaf17328b49cf0ab2601bfd](https://github.com/EndstoneMC/protocol-dumper/commit/892cdafe9ada26c0cbaf17328b49cf0ab2601bfd)  
Date: 2026-04-11T15:46:39Z  
Causal parent: bf543b49e2ed1cf3ded6fc9f3fded81949659c51

## Change, rationale, and limits {#change-rationale-and-limits}

Replaces EnTT release tag with exact 1333fa5 commit and updated archive hash. Message declares latest commit; does not itself establish ABI compatibility reason. Later documents explicitly tie EnTT choice to BDS ABI.

This finding comes from the actual message and all meaningful patch changes in causal order. Explicit reasons are marked as message/author statements; implementation observations do not establish hidden intent. A terse title is not expanded into invented alternatives or outcomes. Read the [cross-commit synthesis](../ENGINEERING_SYNTHESIS.md) for reversals, final-state differences and applicable task families.

## Changed surfaces {#changed-surfaces}

- CMakeLists.txt

## Attribution {#attribution}

GitHub author: wu-vincent; Git author name Vincent. Original external mechanisms and mirrored BDS types remain credited separately.

- Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

## Evidence limits {#local-evidence-and-review-status}

No upstream execution, binary/ABI measurement, generated-tree recount, CI success or runtime equivalence is claimed. The patch contains no repository-owned automated test addition; operational CI and reported manual checks are distinguished in the analysis.
