<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:354"],"source_type":"public","date":"2026-03-30","topics":["lifetime","ffi","testing","api","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-354-feat-add-support-for-26-10"></a>
# EndstoneMC/endstone #354: feat: add support for 26.10 {#endstonemc-endstone-354-feat-add-support-for-26-10}

Source: https://github.com/EndstoneMC/endstone/pull/354

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-03-30T22:34:54Z; recorded state closed; merged True.

## Discussion disposition {#discussion-disposition}

Version 26.10 support port; no primary discussion, but #344 links it to command-message packet compatibility.

The full associated patch was subsequently inspected; test execution is not independently verified.

## Complete port and boundary relocations {#complete-port-and-boundary-relocations}

All160294characters of the final patch were inspected. The title says26.10; final constants/stubs are26.11/protocol944. Both platform tables and native declarations change, but the decisive behavior is moving interception to narrower/native-owned boundaries. TextPacket and InventorySlotPacket handwritten constructors/writers/readers are removed; API send methods allocate via MinecraftPackets and populate native payloads. This avoids maintaining copied serializers that previously drifted in#309/#327. Translatable messages now build JSON rawtext with translate and text parameters and send TextObject, while raw/chat/popup/tip choose native variant bodies. No packet-byte/client-rendering oracle accompanies this change.

Packet events move from NetworkSystem send/NetworkConnection receive into BatchedNetworkPeer raw send/_receivePacket. Send preserves the parsed header, emits the event and re-encodes only replaced payload; receive loops over cancelled packets and replaces bytes for the original native pipeline to decode. This removes manual size/decode/dispatch and timestamp duplication for edited receives. Malformed outgoing headers are logged critical and dropped; malformed incoming headers return BrokenData rather than the former skip/continue. However, old StartGame/resource-pack/map patchPacket invocations are left commented with TODO, so moving the hook drops those patch behaviors at this revision. Peer identity walks peer_ until the last node then static_casts it to RakNetNetworkPeer, assuming nonnull/acylcic RakNet chain; no alternate transport handling exists here. Receive now chooses recipient sub-ID while the removed path decoded sender bits, and send chooses sender sub-ID; split-screen routing requires explicit fixtures instead of assuming these names agree.

Drop cancellation narrows from a partial copied executeFull implementation (exact two-source/one-action shape and custom inventory validation) to the native world-interaction lambda, named executeWorldInteraction for mapping convenience. For drop slot0 it returns success only when Player::drop succeeds, so native transaction handling can restore the inventory after event cancellation; pickup slot1 succeeds and other shapes return Unknown. Upstream remains responsible for surrounding verification and execution. This is a reusable example of hooking the smallest decision point rather than reimplementing a full transaction, with native lambda ABI as the new maintenance cost.

## Leaves, registry, ownership and tests {#leaves-registry-ownership-and-tests}

Leaves decay goes the opposite way: the optimized/inlined _die hook is replaced with a copied randomTick algorithm and local _die. It scans a9×9×9 neighborhood in an11³ stack buffer, marks wood roots and leaf candidates, and propagates six-neighbor distance through four rounds. Only update_bit and nonpersistent leaves participate. If required chunks are absent, the zero-initialized center is treated nonnegative and the update bit is cleared; this deserves parity testing against native chunk-boundary behavior. Cancellation leaves the block and update bit unchanged, allowing repeated future events. Decay spawns native resources then sets air, recognizing a fixed list of vanilla logs/woods; custom supporting blocks and future wood types need coverage. Native spawnResources is mapped instead of copying loot rules, while popResource uses random offsets and a10-tick throw time. No decay/parity/performance fixture is added.

A public BlockType registry is added with ID/equality/translation/item-presence/default BlockData, eagerly populated from native registry. BlockData creation wraps native default state by const_cast, so its wrapper's later mutation semantics are critical. Python create_block_data stub incorrectly declares None and generic args despite an actual BlockData result. The backing cache uses owning string keys; enchantment metadata also changes from nonowning Identifier keys to owning strings and resolves through public registry for writing. The new buildEnchantments dereferences Enchant::getEnchant(type) before testing the public registry result, removing the earlier native-null guard: malformed/unrecognized enchant IDs need a defensive-path test. Tests only strengthen add/set-meta assertions, widen version regex, and compare naive start times using local time rather than pretending UTC.

ActorHurtResult replaces bool on attack/fire/_hurt, player furnace option fields and gameplay variant entries change, block fields move without overall size growth, Dimension gains registry ID, and world-clock/tick manager virtuals are inserted. These coordinated ABI changes cannot be verified by offsets alone. Formatting/license changes and the repository's requested omission of Claude co-author trailers are source content, not an instruction to this review or proof of human-only authorship.


## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (160294 characters; SHA-256 099295a06d4758600587800b3186bd1c9dfc51e13adb10cfcbab99bfbfb793ea), head 9b5e60e71fd8032636b1327916ef40f9e56aa93d. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/354
