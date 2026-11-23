<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:3"],"source_type":"public","date":"2023-09-08","topics":["ffi","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-3-new-command-system"></a>
# EndstoneMC/endstone #3: New command system {#endstonemc-endstone-3-new-command-system}

Source: https://github.com/EndstoneMC/endstone/pull/3

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (218 additions, 109 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu's merged command-bridge refactor has no explanatory body or review discussion. The exact base/head patch was read, with surrounding symbol search. It replaces a fixed console sender with a Bedrock-origin adapter, changes names from borrowed string views to owning strings, and routes command execution through Endstone's dispatcher. Only the Server origin is implemented; other origins throw. Usage and unknown-command messages now use consistent red formatting rather than separate console-only error logging.

The native interop layer adds vtable-call and hidden return-value helpers, obtains command origin type from slot 23 and name from slot 2, and introduces CommandContext construction with owned origin. These are ABI assumptions in code, not portable C++ contracts. The non-const return-value helper's function-pointer cast omits the output argument that its lambda supplies; its impact depends on instantiation, which was not compiled here.

The replacement of a Bedrock placeholder with BedrockCommand leaves execute() throwing. The newly retained original_executor captures the first command context by reference and ignores its supplied command-line argument in favor of that captured context; this creates stale/dangling-context risk if called later. Whole-tree search at head finds only its declaration and assignment, no use that resolves native forwarding. The hook calls getCommonOrigin(), while the changed CommandContext declares getSender(); this snapshot should not be represented as a demonstrated working bridge. These static inconsistencies are reviewer findings, not explanations attributed to Wu. Merge state alone is no runtime or build validation.

Reusable boundary: wrapping a native command origin requires ownership and supported-origin policies, and retaining callbacks requires copying durable context rather than a request-scoped reference. Exact inspected base/head: 5770431987f9e99f6c8fc7d26c76e291820517e9…ca4f4373f0a542ecc7b5b9444d7c6541b7d6227f.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/3
