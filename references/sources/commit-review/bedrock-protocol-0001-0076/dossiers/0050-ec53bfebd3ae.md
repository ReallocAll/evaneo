<!-- retrieval: {"source_ids":["public:commit:ec53bfebd3ae05d6f273d9ea3a51d03eaefce45d"],"source_type":"public","date":"2026-07-21","topics":["testing","build","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="0050-feat-model-mobarmorequipmentpacket-id-32-at-both-eras"></a>
# 0050 · feat: model MobArmorEquipmentPacket (id 32) at both eras {#0050-feat-model-mobarmorequipmentpacket-id-32-at-both-eras}

SHA: `ec53bfebd3ae05d6f273d9ea3a51d03eaefce45d`  
Source: [EndstoneMC/bedrock-protocol commit](https://github.com/EndstoneMC/bedrock-protocol/commit/ec53bfebd3ae05d6f273d9ea3a51d03eaefce45d)  
Authored: 2026-07-21T12:40:24Z · Committed: 2026-07-21T12:40:24Z  
Parent(s): `938186519b4dbbf829706eec67fd469ff994ef67`  
Attribution: exact GitHub-linked author wu-vincent; raw author Vincent. See the attribution limits below.

## Decision and context {#decision-and-context}

Reuse the versioned item codec in armor packet32 and let dependency versioning split its C++ shapes.

## Observed implementation, tests, and changes {#observed-implementation-tests-and-changes}

One declaration contains runtime ID and five ordered item slots. Tests cover all-air and helmet-with-net-ID in both eras, checking exact fixtures and full decode consumption. Old air is one byte per slot, new air eight: complete packets6 versus41bytes. The helmet's plain old network ID becomes a tagged variant in the new item.

## Rationale and alternatives {#rationale-and-alternatives}

Explicit: packet cerealization does not imply its own order changed; the real delta is the item type underneath. Avoid redundant outer gates.

## Constraints, revisions, and uncertainty {#constraints-revisions-and-uncertainty}

Two representative item states cover propagation, not every item blob or armor combination. No fresh runtime execution.

Related reviewed units: [42](0042-8d2f9cac8e91.md), [43](0043-c212c536866c.md), [45](0045-6b35b4685a2d.md), [46](0046-a2ff3606c5ba.md), [48](0048-de9f236a844e.md), [58](0058-81085b1d8eca.md), [64](0064-eb761a0aca0f.md), [65](0065-203095993612.md), [67](0067-202857a9c1c7.md), [68](0068-10d3ab1ced05.md), [70](0070-a0b1a16480d9.md), [76](0076-e38efb023954.md).

## Attribution and execution limits {#attribution-and-execution-limits}

Imported runtime code, architectural analogies, reference fixtures, and agent-facing guidance retain their separate provenance as described in the synthesis.

- No upstream code, compiler, tests, reference codecs, BDS binaries, or benchmarks were executed by the reviewer.
- Historical test/CI/output-equivalence/disassembly reports remain attributed reports; static source checks do not reproduce them.
- No independent acquisition/review of external PR or review discussion is claimed by this commit slice.
- New expansion evidence has not been validated by the preserved frozen v1 evaluations.

Review index · [Detailed cross-commit synthesis](../SYNTHESIS.md)
