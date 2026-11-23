<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:254"],"source_type":"public","date":"2025-08-25","topics":["ffi","testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-254-feat-add-format-support-to-playerchatevent"></a>
# EndstoneMC/endstone #254: [feat] Add format support to `PlayerChatEvent {#endstonemc-endstone-254-feat-add-format-support-to-playerchatevent}

Source: https://github.com/EndstoneMC/endstone/pull/254

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (131 additions, 68 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu's merged chat-format PR has no prose/review, but its full5-file patch was read. PlayerChatEvent gains runtime format, replaceable displayed player via reference_wrapper, and optional recipients lazily populated from online players. The handler preserves explicit native targets, invokes plugins, honors cancellation, formats player/message with fmt and catches invalid format strings. If format changed, it sends ordinary messages to recipients and bypasses native chat; otherwise it updates native author/message and retains the native path. This makes transport semantics depend on format changes, not merely text appearance.

Limit: getRecipients returns a vector by value and Python exposes a read-only property; mutating that returned list is not a verified recipient-editor API. The patch also regenerates stubs removing NamespacedKey and changing registry/enchantment identifiers to strings, but contains no corresponding native implementation of those unrelated API changes, so they cannot be attributed as implemented by this PR alone. No tests executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/254
