<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:25"],"source_type":"public","date":"2024-07-08","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-25-bug-duplicate-furnace-aux-recipes"></a>
# EndstoneMC/endstone #25: [bug] Duplicate furnace aux recipes {#endstonemc-endstone-25-bug-duplicate-furnace-aux-recipes}

Source: https://github.com/EndstoneMC/endstone/issues/25

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

The initial report calls furnace auxiliary recipes duplicates. KoshakMineDEV asks progress; smartcmd suggests manual removal. Wu corrects the premise: outputs have differing NBT hidden by the display. He questions whether that NBT is needed, recommends downstream filtering because few recipes are affected and upstream filtering saves little size, then closes wont-fix. Preserve semantic difference and marginal-benefit reasoning; this does not authorize generally discarding NBT or deduplicating by appearance.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/25
- https://github.com/EndstoneMC/endstone/issues/25#issuecomment-2227227543
- https://github.com/EndstoneMC/endstone/issues/25#issuecomment-2227236546
- https://github.com/EndstoneMC/endstone/issues/25#issuecomment-2227306968
