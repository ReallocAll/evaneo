<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:162"],"source_type":"public","date":"2025-03-21","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-162-feature-resource-pack-event"></a>
# EndstoneMC/endstone #162: [feature] Resource Pack Event {#endstonemc-endstone-162-feature-resource-pack-event}

Source: https://github.com/EndstoneMC/endstone/issues/162

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat wants server packs required while preserving client-owned packs. Wu first implements that as the unconditional 0.7.0 default, citing PocketMine's policy. Arduinonk counters that their server intentionally excludes custom packs because of x-ray/ESP concerns and reports behavior resembling optional downloads; PrimeStrat initially reports the opposite but identifies an old dev build and confirms the new behavior after updating. Wu separates two independent controls: requiring server-pack download versus allowing client-owned packs. He then promises, and reports completed in 0.7.1, an opt-in client-pack setting defaulting false, restoring vanilla-like exclusion unless enabled; Arduinonk confirms the result. The conflict is a real policy/default regression, not merely user confusion.

Full relevant local patches inspected: 5d78c0fe3649292e2982de00c852b4676c08be88 forces ResourcePackStackPacket.texture_pack_required false and cites PocketMine; 5a0a1829862deca2e8b5992e1aefa5a2c45ad1d8 reads settings.allow-client-packs from endstone.toml with false fallback, gates that packet mutation, and adds tomlplusplus linkage. The latter also removes cached StartGame level-state lookup and checks level before reading it. Nukkit's forceResourcesAllowOwnPacks is a referenced mature-project precedent, not Wu-authored evidence, and its independent source was not audited. Pack acceptance does not establish cheat prevention guarantees.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/162
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2744397360
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2745544018
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2757735681
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758193375
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758242272
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758261484
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758292432
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758314337
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758326299
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758327847
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758337274
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758344699
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758348314
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758354503
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758357142
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758367800
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758374826
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2758377667
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2759085948
- https://github.com/EndstoneMC/endstone/issues/162#issuecomment-2759543242
