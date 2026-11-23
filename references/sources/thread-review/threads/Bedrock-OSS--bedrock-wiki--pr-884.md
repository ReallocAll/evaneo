<!-- retrieval: {"source_ids":["public:thread:Bedrock-OSS/bedrock-wiki:884"],"source_type":"public","date":"2024-07-18","topics":["review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="bedrock-oss-bedrock-wiki-884-update-server-software-md"></a>
# Bedrock-OSS/bedrock-wiki #884: Update server-software.md {#bedrock-oss-bedrock-wiki-884-update-server-software-md}

Source: https://github.com/Bedrock-OSS/bedrock-wiki/pull/884

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (12 additions, 19 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu proposes three documentation maintenance operations: rename LiteLoader to LeviLamina, alphabetize listings, and move inactive projects. The merged diff moves GreenFrogMCBE, PowerAllay, SynapseNet, PieMC and Netrex to discontinued lists and updates language counts/anchors when active categories become empty. The code-level artifact is a catalog migration, not runtime engineering. The body supplies no per-project evidence or inactivity threshold, so the moves cannot support a general policy beyond this change. Maintaining counts and anchors alongside entries is the reusable consistency check.



## Source index {#source-index}

- https://github.com/Bedrock-OSS/bedrock-wiki/pull/884
