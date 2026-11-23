<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/bedrock-server-data:3"],"source_type":"public","date":"2026-02-11","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-bedrock-server-data-3-added-missing-1-26-10-22-linux-server-metadata"></a>
# EndstoneMC/bedrock-server-data #3: Added missing 1.26.10.22 Linux server metadata. {#endstonemc-bedrock-server-data-3-added-missing-1-26-10-22-linux-server-metadata}

Source: https://github.com/EndstoneMC/bedrock-server-data/pull/3

## Review scope and state {#review-scope-and-state}

- Thread author: purple-blog; state at review: closed; merged: False.
- Evidence: Public PR and patch reviewed statically (4 additions, 0 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

purple-blog submitted missing Linux preview metadata after a previously unavailable server build appeared. Wu requested changes because the proposed Linux digest was copied from Windows. He reports downloading the actual Linux archive and gives both the independently computed SHA256 and a reproducible PowerShell verification command. The inspected submitted patch still contains the duplicate Windows value; it is not the corrected implementation. Wu then closed the PR to apply the correction directly, so closed/unmerged is intentional supersession, not rejection of adding Linux support. The decisive engineering distinction is platform-specific artifact identity: a plausible URL plus a copied checksum is insufficient. The follow-on direct commit is not linked in this thread and has not been inspected here.



## Source index {#source-index}

- https://github.com/EndstoneMC/bedrock-server-data/pull/3
- https://github.com/EndstoneMC/bedrock-server-data/pull/3#issuecomment-4112429866
- https://github.com/EndstoneMC/bedrock-server-data/pull/3#pullrequestreview-3993408436
