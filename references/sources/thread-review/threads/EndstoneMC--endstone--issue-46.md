<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:46"],"source_type":"public","date":"2024-09-04","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-46-publish-vanilla-bedrock-data-blobs-in-a-separate-repository"></a>
# EndstoneMC/endstone #46: Publish vanilla bedrock data blobs in a separate repository {#endstonemc-endstone-46-publish-vanilla-bedrock-data-blobs-in-a-separate-repository}

Source: https://github.com/EndstoneMC/endstone/issues/46

## Review scope and state {#review-scope-and-state}

- Thread author: IvanCraft623; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

IvanCraft623 requests separately published data blobs to avoid each consumer regenerating them, citing PocketMine and Cloudburst repositories. smartcmd points to AllayMC/BedrockData. Wu agrees in principle but assigns low priority and confirms Allay’s data comes from Endstone while explicitly noting independent maintenance. Stale-bot closure later is not implementation evidence. This preserves the tradeoff between reusable generated artifacts and maintenance ownership; consumers should not infer Endstone release guarantees for the third-party mirror.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/46
- https://github.com/EndstoneMC/endstone/issues/46#issuecomment-2327806384
- https://github.com/EndstoneMC/endstone/issues/46#issuecomment-2394603471
- https://github.com/EndstoneMC/endstone/issues/46#issuecomment-2397290419
- https://github.com/EndstoneMC/endstone/issues/46#issuecomment-2524172191
- https://github.com/EndstoneMC/endstone/issues/46#issuecomment-2558598998
