<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:97"],"source_type":"public","date":"2024-11-29","topics":["concurrency","testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-97-feature-nbt-api-for-itemstack"></a>
# EndstoneMC/endstone #97: [feature] NBT API for ItemStack {#endstonemc-endstone-97-feature-nbt-api-for-itemstack}

Source: https://github.com/EndstoneMC/endstone/issues/97

## Review scope and state {#review-scope-and-state}

- Thread author: ye111566; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

ye111566 observes enchantment NBT survives ItemStack copying despite omission from repr. Wu explains internal handle preservation and initially plans a basic direct NBT API. Atrium asks for broader entity/block NBT; programminglaboratorys later asks about serialization implementation. Wu then revises direction: ItemMeta already covers common metadata, PDC/custom-data dicts would be safer and avoid wrappers for every NBT tag, and direct binary access is then excluded because endianness, varints and malformed payloads risk corruption. The Python dict versus explicit CompoundTag/IntTag/ByteTag example concretely separates user intent from wire representation. Mih4n prefers dictionaries. In November 2025 wu changes the announced interface again: ItemStack::fromNbt and toNbt will arrive in v0.11. This final update prevents treating the earlier avoidance of binary NBT as a timeless rule. The thread does not provide code, encoding contract or tests for those final methods. Preserve the full evolution: opaque copying → planned tags → safer semantic APIs under evaluation → later NBT conversion methods.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/97
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-2507274254
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-2507280875
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-2560504615
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-2564676829
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-2689108044
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-2689814269
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-2899237478
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-2903328147
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-2968388992
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-2971043269
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-2971647245
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-3181021082
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-3186918674
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-3403611814
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-3403621128
- https://github.com/EndstoneMC/endstone/issues/97#issuecomment-3544105688
