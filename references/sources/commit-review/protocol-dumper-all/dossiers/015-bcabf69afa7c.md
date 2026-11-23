<!-- retrieval: {"source_ids":["public:commit:bcabf69afa7c948fce2ce39c01da7a63611ad55e"],"source_type":"public","date":"2026-04-11","topics":["ffi","build","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="015-replace-funchook-config-driven-sigscan-with-inline-libhat-pattern-scanning"></a>
# 015. Replace funchook/config-driven sigscan with inline libhat pattern scanning {#015-replace-funchook-config-driven-sigscan-with-inline-libhat-pattern-scanning}

Source: [bcabf69afa7c948fce2ce39c01da7a63611ad55e](https://github.com/EndstoneMC/protocol-dumper/commit/bcabf69afa7c948fce2ce39c01da7a63611ad55e)  
Date: 2026-04-11T21:12:05Z  
Causal parent: 6d4deb762a6f86a540fc4f083439a16915150aaf

## Change, rationale, and limits {#change-rationale-and-limits}

Removes funchook/runtime config resolver in favor of inline cached libhat call-site patterns, reimplements BasicSchema lookup using EnTT custom data and virtual makeDescription, adds service-locator/ownership/layout mirrors. Broad clang-format changes verified separately from semantic work. Extraction again commented while ABI access is reconstructed; hard terminate on lookup later becomes exception. Not a proven simpler working replacement at this point.

This finding comes from the actual message and all meaningful patch changes in causal order. Explicit reasons are marked as message/author statements; implementation observations do not establish hidden intent. A terse title is not expanded into invented alternatives or outcomes. Read the [cross-commit synthesis](../ENGINEERING_SYNTHESIS.md) for reversals, final-state differences and applicable task families.

## Changed surfaces {#changed-surfaces}

- .clang-format
- .gitignore
- CMakeLists.txt
- config.json
- src/cereal/Context.h
- src/cereal/schema/BasicSchema.cpp
- src/cereal/schema/BasicSchema.h
- src/cereal/schema/DynamicValue.h
- src/cereal/schema/SchemaDescription.h
- src/common/Bedrock.h
- src/common/EnableNonOwnerReferences.h
- src/common/NetworkSystem.cpp
- src/common/NetworkSystem.h
- src/common/NonOwnerPointer.h
- src/common/Packet.cpp
- src/common/Packet.h
- src/common/PrioritySharedMutex.h
- src/common/ServerInstance.h
- src/common/ServiceLocator.h
- src/config.cpp
- src/config.h
- src/generator.cpp
- src/generator.h
- src/injector.cpp
- src/main.cpp
- src/reader.cpp
- src/reader.h
- src/symbol.cpp
- src/symbol.h

## Attribution {#attribution}

GitHub author: wu-vincent; Git author name Vincent. Original external mechanisms and mirrored BDS types remain credited separately.

- Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

## Evidence limits {#local-evidence-and-review-status}

No upstream execution, binary/ABI measurement, generated-tree recount, CI success or runtime equivalence is claimed. The patch contains no repository-owned automated test addition; operational CI and reported manual checks are distinguished in the analysis.
