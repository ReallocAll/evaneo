<!-- retrieval: {"source_ids":["public:commit:695095c7d853e56fd60076bfe6db9fab6714e88b","public:commit:a0e526ae5ee191c42745f8dce3425532947f4ec7","public:commit:d7d50c218b0100f0371ed70dd2966e0b9d11a899","public:commit:e98353be3b721be99ef95e3a83986573d93e5b8e","public:commit:ef3e80be5c25064cec172f39b08e018e968ea1b7"],"source_type":"public","date":"2026-07-27..2026-10-19","topics":["lifetime","testing","build","api","documentation","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="nn04-separate-protocol-identity-mechanics-trust-policy-and-application-rejection"></a>
# Separate protocol identity mechanics, trust policy and application rejection {#nn04-separate-protocol-identity-mechanics-trust-policy-and-application-rejection}

## A second signaling channel without a second connection API {#a-second-signaling-channel-without-a-second-connection-api}

Commit030 adds HTTP signaling over an optional aiohttp extra. The client performs a capability GET, then one offer POST, and consumes the answer. It does not retry a potentially stateful join automatically. HTTP carries full ICE in the SDP, whereas LAN signaling must split candidates to fit its datagram payload. Both routes produce the same Connection/session abstraction. The HTTP session has no LAN endpoint to own.

On the server, the raw network-ID URL segment is retained alongside a best-effort parsed value. IncomingOffer exposes the stripped SDP and optional identity envelope to validate_offer before a session is created. Malformed envelopes fail early; the application decides whether the supplied identity is authorized. This preserves a useful distinction between parseable identity material and permission to join.

## What cryptographic verification means here {#what-cryptographic-verification-means-here}

The identity component canonicalizes ordered SDP fingerprint entries into JSON, signs them using a detached JWS, and can produce a self-signed JWT containing the operator public key in cpk. It supports the corresponding EC signature encodings, including conversion between DER ECDSA and raw r||s form. ServerIdentity reports the key digest and claims after structural verification, fingerprint signature verification and an expiry check when an expiry is present.

A self-signed token binds the answer's fingerprint to the token's key; it does not establish that the key belongs to the desired operator. The API explicitly leaves TLS trust or TOFU/pinning to the caller's on_server_identity callback. When that callback is absent, identity assertions are stripped without verification. On the receiving side, validate_offer is likewise the application's authorization hook. Generated ephemeral keys and print-only example callbacks demonstrate mechanics, not persistent trust management or real-player authentication.

Tests inspect canonical payloads, valid/wrong-key/tampered signatures, envelope roundtrips, expiry, and local HTTP connection behavior. The source's reported23 new tests and aggregate147 passing tests are not rerun here. No auth service, real player token, Bedrock binary or remote trusted peer was exercised.

## Preserve protocol errors across abstraction layers {#preserve-protocol-errors-across-abstraction-layers}

Commit034 identifies a concrete boundary failure. A successful HTTP status with content type application/sdp can contain a decimal session-error code instead of an SDP answer. Passing that string straight into aiortc produces an unrelated media-section parsing exception. The new parser accepts an SDP beginning with v=; maps known decimal values, including identity errors36/37, to ConnectionFailed; maps unknown numbers to SIGNALING_UNKNOWN_ERROR; and treats nonnumeric junk as SIGNALING_PARSING_FAILURE.

Tests fake responses36,37,9999 and junk. This is a focused improvement in failure meaning, not merely catching a wider exception. It deliberately loses the original unknown integer in the public error path. That choice differs from the LAN text parser, which preserves unknown numbers, and should be considered when a future protocol version adds errors.

Commit035 adds optional identity_signer to connect_http so it signs the offer before request_answer. The message links the omission to BDS error37. This adds no new test and reuses the operator-style signer; it does not prove that a self-signed operator token satisfies the application's real-player authorization requirements. The message says the LAN connect path already signs, but the final LAN connect signature and call path have no identity_signer parameter. The source discrepancy is retained rather than harmonized by assumption.

## Documentation and packaging boundaries {#documentation-and-packaging-boundaries}

The README warns that the PyPI name nethernet refers to an unrelated package and uses the intended Git repository installation route. Examples become command-line programs with explicit ports/identity flags and context-managed closure. The batching example is corrected: RakNet's Bedrock0xFE wrapper is not automatically part of a NetherNet application payload. The source reports that BDS ignores a prefixed batch and responds to the bare batch, but no raw exchange is supplied in this review corpus. Application batching, transport fragmentation and signaling are three separate layers.

## Reusable application {#reusable-application}

For an interoperable client, parse application-level error payloads before handing data to a lower library. Keep HTTP status, content framing, protocol rejection and authorization failure distinct. For identity features, document exactly what the signature proves and who supplies the trust anchor. Review examples as consumers of the public contract, but do not promote successful local roundtrips or self-signed test fixtures into real-service authentication claims.

Sources: dossiers030–031,033–035 and the final api.py/errors.py snapshots. Public implementation messages contain the explicit reasons; source discrepancies and unresolved trust/cleanup boundaries are static analysis. Runtime, service interoperability, production security and publication were not validated.

## Exact commit navigation {#exact-commit-navigation}

- [030 e98353be3b72: feat(http): HTTP signaling channel + SDP identity assertions](../dossiers/030-e98353be3b72.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/e98353be3b721be99ef95e3a83986573d93e5b8e)
- [031 d7d50c218b01: docs: align README and examples with raknet-python](../dossiers/031-d7d50c218b01.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/d7d50c218b0100f0371ed70dd2966e0b9d11a899)
- [033 a0e526ae5ee1: docs: NetherNet batches carry no RakNet 0xFE header](../dossiers/033-a0e526ae5ee1.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/a0e526ae5ee191c42745f8dce3425532947f4ec7)
- [034 ef3e80be5c25: fix(http): raise the host's session error from a numeric answer body](../dossiers/034-ef3e80be5c25.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/ef3e80be5c25064cec172f39b08e018e968ea1b7)
- [035 695095c7d853: feat(http): let connect_http sign its offer](../dossiers/035-695095c7d853.md) · [public source](https://github.com/EndstoneMC/nethernet-python/commit/695095c7d853e56fd60076bfe6db9fab6714e88b)
