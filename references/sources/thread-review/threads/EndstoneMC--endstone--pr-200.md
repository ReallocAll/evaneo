<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:200"],"source_type":"public","date":"2025-06-15","topics":["ffi","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-200-feat-add-playerpickupitemevent-chunkunloadevent-and-chunkloadevent-wip"></a>
# EndstoneMC/endstone #200: feat: add `PlayerPickupItemEvent`, `ChunkUnloadEvent` and `ChunkLoadEvent` (WIP) {#endstonemc-endstone-200-feat-add-playerpickupitemevent-chunkunloadevent-and-chunkloadevent-wip}

Source: https://github.com/EndstoneMC/endstone/pull/200

## Review scope and state {#review-scope-and-state}

- Thread author: dreamguxiang; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (376 additions, 9 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

dreamguxiang authors this merged 18-file PR. Wu's sole comment approves and thanks the contributor; it supplies no technical rationale. The full final patch was inspected, preserving the distinction between implemented pickup dispatch and disabled chunk hooks.

### Complete patch inspection {#complete-patch-inspection}

The final patch implements PlayerPickupItemEvent at native Player::take. It immediately rejects client-side calls or players unable to interact; for item-category actors it creates an Endstone item view, uses the existing player wrapper, fires the cancellable event, and returns false on cancellation before native take. Other eligible actors go through the original method. Thus this is a pre-operation hook, not proof that an eventual inventory insertion succeeded. Its ItemStack reference and Python reference-policy getter borrow a locally owned wrapper alive only through synchronous dispatch; listeners should copy required data rather than retain the event/item wrapper.

LevelEvent, DimensionEvent and ChunkEvent provide borrowed references and Python properties. ChunkLoadEvent and ChunkUnloadEvent classes are exposed, but both hook declarations and complete dispatch implementations are commented out in the final patch. Therefore this PR does not establish active chunk lifecycle notifications despite its title and exported types. This is the key implementation-versus-surface distinction. The patch also removes an unused ItemActor throw-time setter and adds a generated build-provider ignore rule. No new tests or human technical explanation accompany the code.

Exact inspected base/head: b9b405f75f559f2b3ffcb98b67f51edba5af7c45…2260736aaa212ea5d619314f69e16212238dbf4b. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/200
- https://github.com/EndstoneMC/endstone/pull/200#issuecomment-2988691138
