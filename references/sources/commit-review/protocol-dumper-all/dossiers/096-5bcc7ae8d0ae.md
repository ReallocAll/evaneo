<!-- retrieval: {"source_ids":["public:commit:5bcc7ae8d0aeabcd7c4929eb562ddfb0060d8972"],"source_type":"public","date":"2026-08-05","topics":["ffi","build","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="096-match-the-entt-that-bds-1-26-50-was-built-against"></a>
# 096. Match the EnTT that BDS 1.26.50 was built against {#096-match-the-entt-that-bds-1-26-50-was-built-against}

Source: [5bcc7ae8d0aeabcd7c4929eb562ddfb0060d8972](https://github.com/EndstoneMC/protocol-dumper/commit/5bcc7ae8d0aeabcd7c4929eb562ddfb0060d8972)  
Date: 2026-08-05T17:07:38Z  
Causal parent: b80de45fd42dc496151363d05e594155df15c7ea

## Change, rationale, and limits {#change-rationale-and-limits}

Matches1.26.50 EnTT meta_data_node/container ABI revision and adapts id/alias API with requires shim. Reports942/991 failed types with nonsense data size. Dependency pin is host ABI contract, not merely upgrade. Exact upstream source equivalence not independently audited here.

This finding comes from the actual message and all meaningful patch changes in causal order. Explicit reasons are marked as message/author statements; implementation observations do not establish hidden intent. A terse title is not expanded into invented alternatives or outcomes. Read the [cross-commit synthesis](../ENGINEERING_SYNTHESIS.md) for reversals, final-state differences and applicable task families.

## Changed surfaces {#changed-surfaces}

- src/visitor.cpp
- third_party/entt/CMakeLists.txt

## Attribution {#attribution}

GitHub author: wu-vincent; Git author name Vincent. Original external mechanisms and mirrored BDS types remain credited separately.

## Evidence limits {#local-evidence-and-review-status}

No upstream execution, binary/ABI measurement, generated-tree recount, CI success or runtime equivalence is claimed. The patch contains no repository-owned automated test addition; operational CI and reported manual checks are distinguished in the analysis.
