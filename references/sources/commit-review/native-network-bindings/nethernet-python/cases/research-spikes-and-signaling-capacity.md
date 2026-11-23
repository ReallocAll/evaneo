<!-- retrieval: {"source_ids":["public:commit:0692dec196a01544c2078293564af1801f3e87bf","public:commit:1705348ebf10a54a9c5dbf8b2f17f72d6d51c6fd","public:commit:8b0211839b340525827abfca9c4b32ce0c160e3d","public:commit:c9b86cc5d8a19c4a2d1b19bc0641256d7ce855ee","public:commit:deb486236c4386bef92b7316fc0504dd9816c19e","public:commit:e7a05314974718d72e13040fb8aaa7e481cf9444","public:commit:f7431a5f337571b50144d588373cfcbfa503b31f"],"source_type":"public","date":"2026-06-14","topics":["ffi","testing","documentation","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="nn01-a-protocol-port-changes-direction-when-the-enclosing-transport-disagrees"></a>
# A protocol port changes direction when the enclosing transport disagrees {#nn01-a-protocol-port-changes-direction-when-the-enclosing-transport-disagrees}

## Problem and evidence chain {#problem-and-evidence-chain}

The project starts with a wire specification and a phased Python implementation plan, not a literal translation of the reference C++ object graph. Commit001 separates observable network behavior from implementation details such as C++ threads. The planned order is identifiers and signaling, packed discovery and cryptographic envelope, fragmentation, aiortc adaptation, session state, LAN integration and a public facade. That order makes each layer inspectable before integration depends on it.

The plan identifies unusually large WebRTC messages and ICE candidate representation as risks. Commit003 builds a small aiortc experiment before the session stack. The recorded environment is aiortc1.14.0: the normal SDP advertises a65,536-byte maximum, whereas a rewritten max-message-size permits a262,144-byte frame. The experiment also exercises channel opening and candidate parsing. This is more specific than saying “test the dependency”: it asks whether the dependency can support the largest protocol fragment plus its one-byte header.

The source records successful upstream runs. This review read the experiment, assertions and findings but did not run aiortc, contact a remote peer or independently verify the reported transfer. The candidate parser accepts a prefixed string without necessarily interpreting it correctly, so the later foundation=='1' assertion is a materially stronger check than absence of an exception. A test requiring the default maximum to remain below the required frame size could itself fail if a later aiortc release improves the default; preserve the capability requirement separately from the observed old default.

## Initial implementation and reversal {#initial-implementation-and-reversal}

The first PeerConnection adapter creates/adopts two precisely named data channels, rewrites the SDP maximum, buffers sends until open and candidates until a remote description exists. Session readiness requires both channels. The initial plan favors non-trickle ICE: gather candidates and exchange a complete SDP. That simplifies sequencing at the WebRTC layer.

The containing LAN protocol has a different bound. Its Message packet has a32-byte header and at most1,140 bytes of signal payload. Serialization deliberately truncates overlong payloads. At018, a complete SDP exceeds that capacity. The described symptom is silent truncation, rather than an aiortc failure to generate an offer. The correction strips candidate/end-of-candidates lines out of the initial offer/answer and sends candidates as separate CANDIDATEADD messages. UDP can reorder these messages, so SessionManager retains up to64 candidates for an as-yet unknown connection ID and flushes them once CONNECTREQUEST creates the listener.

This is a genuine reversal supported by a changed constraint. It is not evidence that trickle ICE is always preferable. The final HTTP signaling path deliberately sends a full-ICE offer in one HTTP request because the LAN datagram cap is absent. The architecture retains one transport/session engine while allowing the signaling channel to determine its exchange strategy.

## Boundaries the implementation does not establish {#boundaries-the-implementation-does-not-establish}

The64-candidate cap applies to each dictionary entry. Neither a total number of pending connection IDs nor expiry/eviction of old entries is enforced in the inspected final SessionManager. It is therefore inaccurate to generalize that local list cap into bounded aggregate memory under unsolicited traffic.

The relay-only option is another dependency boundary. The adapter filters advertised candidates because the documented aiortc interface lacks the desired enforced transport policy. Advertising only relay candidates is not independently demonstrated to prevent all non-relay connectivity or local information use. The final enum documentation still uses stronger “forces relay-only” language; the adapter limitation should govern any privacy-sensitive use.

## Verification and interoperability {#verification-and-interoperability}

The repository distinguishes several useful kinds of evidence:
- Byte-layout and envelope golden fixtures check the implementation against the written contract.
- In-process aiortc peers check adapter/session behavior.
- UDP loopback exercises the signaling path, but seeded addresses do not establish real broadcast discovery across interfaces or operating systems.
- A live C++/Bedrock interoperability step is explicitly PENDING in the recorded checklist because the reference build is a static library without a runnable peer.

One documentation claim says the public transport integration includes a large payload. The inspected facade test uses short reliable/unreliable messages; fragmentation is covered in separate wrapper/manager tests. This is a scope mismatch to preserve, not a reason to discard those tests.

## Reusable decision {#reusable-decision}

Before porting a protocol, write down both the inner protocol requirement and the enclosing transport budget. Prove uncertain library capabilities with the smallest vertical experiment, retain the exact tested version, and allow integration evidence to revise a convenient initial design. Keep byte conformance, local integration and external interoperability as separate claims. Apply this case to a new port or dependency selection; do not copy its particular UDP limits, candidate policy or old aiortc assumptions into unrelated transports.

Sources: per-SHA dossiers001–003,011,014,018–021 and030. Relevant files include SPEC.md, tasks/plan.md, tasks/spike-aiortc.md, tests/test_aiortc_spike.py, transport/peer_connection.py and the final SessionManager snapshot. Explicit reasons come from those messages and documents; aggregate-memory and relay-policy limits are static inferences from the code, not reproduced attacks.

## Exact commit navigation {#exact-commit-navigation}

- [001 deb486236c43: docs: add NetherNet SPEC and implementation plan](../dossiers/001-deb486236c43.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/deb486236c4386bef92b7316fc0504dd9816c19e)
- [002 f7431a5f3375: chore: scaffold uv project with aiortc + cryptography](../dossiers/002-f7431a5f3375.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/f7431a5f337571b50144d588373cfcbfa503b31f)
- [003 0692dec196a0: spike(aiortc): de-risk large messages, non-trickle ICE, candidate format](../dossiers/003-0692dec196a0.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/0692dec196a01544c2078293564af1801f3e87bf)
- [011 8b0211839b34: feat(transport): aiortc PeerConnection wrapper with framing](../dossiers/011-8b0211839b34.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/8b0211839b340525827abfca9c4b32ce0c160e3d)
- [014 c9b86cc5d8a1: test: run the suite in parallel with pytest-xdist (-n auto)](../dossiers/014-c9b86cc5d8a1.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/c9b86cc5d8a19c4a2d1b19bc0641256d7ce855ee)
- [018 1705348ebf10: fix(session): trickle ICE candidates to fit the LAN message cap](../dossiers/018-1705348ebf10.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/1705348ebf10a54a9c5dbf8b2f17f72d6d51c6fd)
- [021 e7a053149747: docs(interop): document Task 15 live-interop harness and blocker](../dossiers/021-e7a053149747.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/e7a05314974718d72e13040fb8aaa7e481cf9444)
