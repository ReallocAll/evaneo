<!-- retrieval: {"source_ids":["public:commit:2f6ceaf4ef3f237210e4b8c0f7130aa80ff33697"],"source_type":"public","date":"2026-05-02","topics":["build","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="060-drop-unused-minecraftpackets-createpacket-and-remove-empty-source-files"></a>
# 060. Drop unused `MinecraftPackets::createPacket` and remove empty source files {#060-drop-unused-minecraftpackets-createpacket-and-remove-empty-source-files}

Source: [2f6ceaf4ef3f237210e4b8c0f7130aa80ff33697](https://github.com/EndstoneMC/protocol-dumper/commit/2f6ceaf4ef3f237210e4b8c0f7130aa80ff33697)  
Date: 2026-05-02T15:54:25Z  
Causal parent: 3e7b224d4863e60b873a6da25638e9ade572ec6c

## Change, rationale, and limits {#change-rationale-and-limits}

Removes unused createPacket wrapper and BasicSchema lookup/description implementations plus CMake source references. Message calls files empty but they contained unused implementations; deletion follows direct-meta traversal, not new runtime behavior.

This finding comes from the actual message and all meaningful patch changes in causal order. Explicit reasons are marked as message/author statements; implementation observations do not establish hidden intent. A terse title is not expanded into invented alternatives or outcomes. Read the [cross-commit synthesis](../ENGINEERING_SYNTHESIS.md) for reversals, final-state differences and applicable task families.

## Changed surfaces {#changed-surfaces}

- CMakeLists.txt
- src/cereal/schema/BasicSchema.cpp
- src/common/Packet.cpp
- src/common/Packet.h
- src/symbol.h

## Attribution {#attribution}

GitHub author: wu-vincent; Git author name Vincent. Original external mechanisms and mirrored BDS types remain credited separately.

- Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>

## Evidence limits {#local-evidence-and-review-status}

No upstream execution, binary/ABI measurement, generated-tree recount, CI success or runtime equivalence is claimed. The patch contains no repository-owned automated test addition; operational CI and reported manual checks are distinguished in the analysis.
