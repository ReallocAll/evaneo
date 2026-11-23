<!-- retrieval: {"source_ids":["public:thread:Bedrock-OSS/bedrock-wiki:834"],"source_type":"public","date":"2024-04-07","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="bedrock-oss-bedrock-wiki-834-update-server-software-md"></a>
# Bedrock-OSS/bedrock-wiki #834: Update server-software.md {#bedrock-oss-bedrock-wiki-834-update-server-software-md}

Source: https://github.com/Bedrock-OSS/bedrock-wiki/pull/834

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (5 additions, 2 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu describes the 2024 architecture as a high-level Bukkit/Spigot-like plugin API that hides hooks, embeds Python, and permits C++ or Python plugins distributed through a Python package. Those are author claims in the proposal, not independently tested capabilities. The merged patch is documentation only: add Endstone under C++ and Python and update both language counts. The dual listing follows supported plugin languages rather than asserting two independent server implementations. No reviewer discussion appears; merge status establishes acceptance of the listing, not a review of runtime correctness.



## Source index {#source-index}

- https://github.com/Bedrock-OSS/bedrock-wiki/pull/834
