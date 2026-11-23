<!-- retrieval: {"source_ids":["public:commit:7abb21fbb9adca2505dbc176c025beff85c5d6d4"],"source_type":"public","date":"2026-04-21","topics":["build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="044-order-type-fields-by-ordinal-index-refine-typeref-and-json-output"></a>
# 044. Order type fields by ordinal index; refine TypeRef and JSON output {#044-order-type-fields-by-ordinal-index-refine-typeref-and-json-output}

Source: [7abb21fbb9adca2505dbc176c025beff85c5d6d4](https://github.com/EndstoneMC/protocol-dumper/commit/7abb21fbb9adca2505dbc176c025beff85c5d6d4)  
Date: 2026-04-21T16:24:29Z  
Causal parent: f22f8c7e27ea348d83d5bf8cc6ba3508fb2f52e8

## Change, rationale, and limits {#change-rationale-and-limits}

Validates absent/duplicate member ordinals and sorts fields. Adds TypeRef alternatives, sanitized filenames, separate enum directory and stream error logs. Alias output is actually skipped despite message dedicated-path language; field resolution still incomplete. Claude Opus 4.7 credit.

This finding comes from the actual message and all meaningful patch changes in causal order. Explicit reasons are marked as message/author statements; implementation observations do not establish hidden intent. A terse title is not expanded into invented alternatives or outcomes. Read the [cross-commit synthesis](../ENGINEERING_SYNTHESIS.md) for reversals, final-state differences and applicable task families.

## Changed surfaces {#changed-surfaces}

- src/main.cpp
- src/models.h
- src/visitor.cpp

## Attribution {#attribution}

GitHub author: wu-vincent; Git author name Vincent. Original external mechanisms and mirrored BDS types remain credited separately.

- Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>

## Evidence limits {#local-evidence-and-review-status}

No upstream execution, binary/ABI measurement, generated-tree recount, CI success or runtime equivalence is claimed. The patch contains no repository-owned automated test addition; operational CI and reported manual checks are distinguished in the analysis.
