<!-- retrieval: {"source_ids":["public:thread:Bedrock-OSS/bedrock-wiki:1079"],"source_type":"public","date":"2025-07-30","topics":["review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="bedrock-oss-bedrock-wiki-1079-docs-update-active-server-softwares"></a>
# Bedrock-OSS/bedrock-wiki #1079: docs: update active server softwares {#bedrock-oss-bedrock-wiki-1079-docs-update-active-server-softwares}

Source: https://github.com/Bedrock-OSS/bedrock-wiki/pull/1079

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (24 additions, 24 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu explicitly separates two inactivity criteria: six months without activity for JukeBoxMC, RAstra and Sculk, versus missing latest-game support and no substantive feature work beyond dependency bumps for JSPrismarine. The merged two-file patch moves all four entries from active to discontinued while preserving their descriptions, languages and implementation type. This is a concrete maintenance decision where dependency churn alone does not establish feature maintenance. Historical criteria should not be presented as a current assessment of these projects; repository activity was not independently rechecked here.



## Source index {#source-index}

- https://github.com/Bedrock-OSS/bedrock-wiki/pull/1079
