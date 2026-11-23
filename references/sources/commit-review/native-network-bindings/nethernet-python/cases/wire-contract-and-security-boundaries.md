<!-- retrieval: {"source_ids":["public:commit:009e5b3d2c6abc5e712b4fa2b1a932b6cb7b692d","public:commit:1b82cf111b4e3ec22056d2b6271f61176545ba1b","public:commit:1bfb9e7b5936515735f1a4bb6ac68e03a9b267be","public:commit:1ea609a793d7db2d39ab3222e45549a55cf4b783","public:commit:21c7cc1cef47573dcd4b10751a284aa731a71db6","public:commit:37532379296a38351e5c272e163a2c87a80835d4","public:commit:6ea0cbfa6fe42d1d373940b492a207c9228c0a7f","public:commit:7e55d04977b0f5fe9e519038ba85cacdbc4bc411","public:commit:83e732e10d12faffd27dba33ef7b8c291ca9a29e","public:commit:91e211cba34ed82df349389c566842690d2c769d","public:commit:fa383012b8db4f6f070a99292995335ee91636a1"],"source_type":"public","date":"2026-06-14..2026-07-27","topics":["testing","api","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="nn02-preserve-exact-wire-behavior-without-inheriting-every-security-assumption"></a>
# Preserve exact wire behavior without inheriting every security assumption {#nn02-preserve-exact-wire-behavior-without-inheriting-every-security-assumption}

## The contract is smaller than the reference implementation {#the-contract-is-smaller-than-the-reference-implementation}

Identifiers, text signaling, discovery packets and fragmentation are implemented as small independent components. NetworkID distinguishes decimal unsigned64-bit peer IDs, UUID identities and an unset value; session IDs use a separate random64-bit space. The signaling parser splits only the first two spaces, preserving embedded spaces and line breaks in SDP. It rejects malformed IDs and unknown message verbs while retaining unknown numeric error codes as integers. The representation supports forward compatibility at the parser layer, but later public exceptions assume an enum with a .name attribute. End-to-end error tolerance therefore needs a check across layers, not just a permissive parser test.

Packed discovery uses explicit little-endian structures: a20-byte base header,24-byte Response prefix and32-byte Message prefix. These sizes are calculated independently of native C struct alignment. Serializers cap payloads at1,148 and1,140 bytes respectively. Tests exercise exact offsets, short buffers, unknown packet kinds and truncation. The decoder reads the advertised packet-length field but does not validate it against the entire buffer; payload extent checks should not be described as full validation of every header invariant.

The optional first-discovery probe has sender ID zero and empty data. The specification separates accepting this probe from electing to emit it. LAN handling avoids caching or answering it as an ordinary peer message, preventing an unnecessary response loop and bogus zero identity. This is a small receiver-tolerance contract with observable consequences, not merely a comment change.

## Compatibility encryption is not a new security design {#compatibility-encryption-is-not-a-new-security-design}

The required discovery envelope derives a key from SHA-256 of the little-endian application ID, uses AES-256 ECB with PKCS7 padding, and authenticates plaintext with HMAC using the same key. The implementation checks MAC values in constant time after decrypting and rejects malformed block size, padding and MAC. Tests include a vector attributed to an OpenSSL3.2.3 implementation and tamper cases.

The source explicitly retains ECB for interoperability. The default application ID is public; deriving its key does not establish a secret or authenticated peer identity. These facts limit the meaning of the MAC: it can enforce envelope consistency for the compatibility protocol, but it is not evidence that a hostile LAN peer cannot forge traffic. The review does not recommend this construction for a new protocol and did not reproduce a cryptographic attack or external vector-generation run.

## Framing and its preconditions {#framing-and-its-preconditions}

PacketQueue is independent of aiortc through injected send callbacks. Reliable application packets are split into fragments of at most0x3FFFF bytes, with a one-byte countdown. The maximum application size0x3FBFF01 follows the finite fragment-count space. Unreliable traffic cannot span multiple fragments. FIFO and partial reads are explicit, and an empty application packet is distinguishable from an empty data-channel input that is ignored.

The implementation relies on reliable ordered SCTP. It does not validate a hostile countdown sequence or enforce a total receive reassembly budget. Those omissions matter when choosing a reuse boundary: lifting this code unchanged into an unordered datagram receiver would lose a premise on which it relies. The high-level send method also discards the underlying false return for an oversized packet; applications are not promised an exception for every silent protocol drop.

## Names, numbers and source equivalence {#names-numbers-and-source-equivalence}

Two naming migrations occur independently of the wire constants. Commit006 adopts UPPER_SNAKE_CASE enum members with the source names retained in comments, explicitly in response to a requested Python convention. Commit032 removes the C++ E prefix from enum class names. The latter is supported by an exact finite substitution audit: normalize only the three old class names, compare each changed file, then read the residual imports/comments/grammar. Numeric values do not change. Python import compatibility nevertheless changes, so “wire-compatible” is not synonymous with “API-compatible.” Commit012 is only the equivalent decimal-to-hex fragment-size literal and merits no independent design credit.

## What to carry forward {#what-to-carry-forward}

Use explicit byte layouts and immutable value objects where the wire grammar is fixed. State tolerant input rules precisely, and test that later presentation/error layers preserve them. Keep compatibility algorithms, their threat assumptions and their authorship distinct from the port author's choices. Name-only and literal-only patches can share reasoning once their equivalence is proven, while retaining each commit identity. The byte constants and crypto construction in this case are protocol-specific, not universal defaults.

Sources: bundled dossiers 004–012, 016–018, 020, 024 and [032](../dossiers/032-91e211cba34e.md), with pinned public commits below. The enum-rename comparison files and final source snapshots are not bundled; the equivalence finding is from the recorded static review, not a fresh reproduction. The fixture and OpenSSL results are source-reported. No upstream execution, live peer exchange, fuzzing or security assessment was performed.

## Exact commit navigation {#exact-commit-navigation}

- [004 7e55d04977b0: feat(network-id): NetworkID parsing and ConnectionId minting](../dossiers/004-7e55d04977b0.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/7e55d04977b0f5fe9e519038ba85cacdbc4bc411)
- [005 1b82cf111b4e: feat(signaling): message codec and shared error enums](../dossiers/005-1b82cf111b4e.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/1b82cf111b4e3ec22056d2b6271f61176545ba1b)
- [006 6ea0cbfa6fe4: chore: enforce PEP8 naming with ruff; rename enum members](../dossiers/006-6ea0cbfa6fe4.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/6ea0cbfa6fe42d1d373940b492a207c9228c0a7f)
- [007 21c7cc1cef47: feat(discovery): packet codec for Request/Response/Message](../dossiers/007-21c7cc1cef47.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/21c7cc1cef47573dcd4b10751a284aa731a71db6)
- [008 009e5b3d2c6a: feat(discovery): AES-256-ECB + HMAC-SHA256 crypto envelope](../dossiers/008-009e5b3d2c6a.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/009e5b3d2c6abc5e712b4fa2b1a932b6cb7b692d)
- [009 1bfb9e7b5936: docs(spec): add optional LAN first-discovery probe note; plan Task 12](../dossiers/009-1bfb9e7b5936.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/1bfb9e7b5936515735f1a4bb6ac68e03a9b267be)
- [010 1ea609a793d7: feat(transport): packet framing and fragmentation (PacketQueue)](../dossiers/010-1ea609a793d7.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/1ea609a793d7db2d39ab3222e45549a55cf4b783)
- [012 83e732e10d12: style(framing): use hex literal for FRAGMENT_SIZE](../dossiers/012-83e732e10d12.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/83e732e10d12faffd27dba33ef7b8c291ca9a29e)
- [017 37532379296a: feat(discovery): LAN discovery + signaling UDP transport](../dossiers/017-37532379296a.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/37532379296a38351e5c272e163a2c87a80835d4)
- [020 fa383012b8db: test(conformance): SPEC s11 byte-vector + fragmentation suite](../dossiers/020-fa383012b8db.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/fa383012b8db4f6f070a99292995335ee91636a1)
- [032 91e211cba34e: refactor: drop the C++ E prefix from enum class names](../dossiers/032-91e211cba34e.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/91e211cba34ed82df349389c566842690d2c769d)
