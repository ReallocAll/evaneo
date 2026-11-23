<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:69"],"source_type":"public","date":"2024-10-01","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-69-feature-add-inventory-item-manipulation"></a>
# EndstoneMC/endstone #69: [feature] Add inventory/item manipulation. {#endstonemc-endstone-69-feature-add-inventory-item-manipulation}

Source: https://github.com/EndstoneMC/endstone/issues/69

## Review scope and state {#review-scope-and-state}

- Thread author: palmmc; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

palmmc requests item/NBT manipulation beyond ScriptAPI restrictions. xXLarryTFVWXx proposes a Python dictionary with hotbar, armor, selected hand, offhand and general slots, explicitly lacking implementation knowledge. Wu later reports concrete PlayerInventory accessors for armor/main/off-hand in a dev build and splits NBT (#97) and enchantments (#103), with lore work ongoing. Do not claim the dictionary design was adopted or that slot access implements arbitrary NBT. The useful decision is phased capability delivery and separate tracking of semantically different item APIs.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/69
- https://github.com/EndstoneMC/endstone/issues/69#issuecomment-2450813520
- https://github.com/EndstoneMC/endstone/issues/69#issuecomment-2487443923
- https://github.com/EndstoneMC/endstone/issues/69#issuecomment-2601020983
- https://github.com/EndstoneMC/endstone/issues/69#issuecomment-2745405573
