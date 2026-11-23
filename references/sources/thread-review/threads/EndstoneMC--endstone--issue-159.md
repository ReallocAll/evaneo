<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:159"],"source_type":"public","date":"2025-03-19","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-159-bug-the-item-is-not-given-to-the-player"></a>
# EndstoneMC/endstone #159: [bug] The item is not given to the player. {#endstonemc-endstone-159-bug-the-item-is-not-given-to-the-player}

Source: https://github.com/EndstoneMC/endstone/issues/159

## Review scope and state {#review-scope-and-state}

- Thread author: MipaSenpai; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

MipaSenpai reports add_item failing with an empty inventory, suggests set_item as a workaround, and Wu reproduces and recognizes it as unintended. The reproduction itself is an image/video not independently inspected, but the full linked fix e277d632064fbb4dcdaa92607ca567e1be6b25ad reveals the narrower mechanism: after an uncancelled BlockBreakEvent, refresh event.item_used from the player's selected inventory slot because plugin handlers may have modified it. This is a stale event snapshot overwriting/ignoring an inventory mutation, not proof that all empty-inventory insertion paths were broken. The commit specifically fixes selected-slot changes during BlockBreakEvent; the maintainer supplies a demonstration link but no independent execution was performed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/159
- https://github.com/EndstoneMC/endstone/issues/159#issuecomment-2736836893
- https://github.com/EndstoneMC/endstone/issues/159#issuecomment-2737546634
- https://github.com/EndstoneMC/endstone/issues/159#issuecomment-2737556271
- https://github.com/EndstoneMC/endstone/issues/159#issuecomment-2738526005
- https://github.com/EndstoneMC/endstone/issues/159#issuecomment-2745897739
- https://github.com/EndstoneMC/endstone/commit/e277d632064fbb4dcdaa92607ca567e1be6b25ad
