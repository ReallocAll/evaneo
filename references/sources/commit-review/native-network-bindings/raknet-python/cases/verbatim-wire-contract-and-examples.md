<!-- retrieval: {"source_ids":["public:commit:0894b496211c39dd29cd08275d15b776a78f2f80","public:commit:3c24fba1741a7d4b7a5bd66b382fd86898ec2219"],"source_type":"public","date":"2026-07-27","topics":["lifetime","ffi","testing","build","documentation","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="rp04-a-convenient-wrapper-header-can-break-protocol-composition"></a>
# A convenient wrapper header can break protocol composition {#rp04-a-convenient-wrapper-header-can-break-protocol-composition}

## Initial convenience and later correction {#initial-convenience-and-later-correction}

The first high-level Connection.send prepends ID_USER_PACKET_ENUM, and the router strips that byte before exposing a received payload. This makes simple application echo convenient because users need not know RakNet's distinction between control and user messages. It also means the wrapper, rather than the application protocol, owns the first wire byte.

Commit017 explicitly reverses that policy. The binding and high-level APIs now send and return application bytes verbatim. Router forwards messages whose first byte is in the user range, while built-in RakNet control IDs still drive connection and ping events. Existing tests change their payloads to include a user ID. Minecraft Bedrock's0xFE is cited as the motivating example.

The causal lesson is not that every transport wrapper must be raw. The tradeoff is composability with an existing application protocol. If the application already owns a message ID, an undocumented extra header changes the protocol. Conversely, a user sending arbitrary bytes below the user-ID range should not expect the high-level router to treat them as application payload. The final send method does not validate that leading byte or return the native send result, so the documented contract and the implementation's permissive argument path differ.

## Examples as consumers, not interoperability proof {#examples-as-consumers-not-interoperability-proof}

Five command-line examples replace the design document: synchronous and asynchronous echo clients/servers and an offline server-list ping. Echo data explicitly includes0xFE. These examples illustrate byte ownership and cleanup, but an echo response is not a Bedrock login or full game-protocol transaction.

The ping example's response fixture contains a big-endian16-bit MOTD length; its printing path decodes the raw pong data including that prefix. It is adequate as a transport demonstration, not a complete parser of the application payload. Tests and examples use local peers; no external Bedrock packet capture or remote interoperability result accompanies the framing reversal.

This also offers a useful cross-repository counterexample. NetherNet's README separately removes a RakNet-style0xFE prefix because its Bedrock application batching differs. The two transports must not share application framing by analogy alone. Keep the exact protocol contract at each adapter boundary and cite the relevant transport, rather than treating “Minecraft networking” as one interchangeable byte format.

## Documentation maturity and attribution {#documentation-maturity-and-attribution}

The project documents raw, synchronous and asyncio layers. Its build metadata and README describe an Alpha package despite a commit title using production-grade language. These labels are contextual claims, not evidence that local echo tests establish stability for all applications. The native transport comes from the Conan RakNet dependency; the local work here is facade semantics, byte ownership, examples and error delivery.

## Reuse guidance {#reuse-guidance}

Before adding framing in a convenience API, ask which layer owns the first byte, length prefix, compression and reliability semantics. Test exact bytes at the boundary, make a breaking wire expectation change explicit, and update examples as executable consumers of the new contract. Require an external peer only when claiming interoperability; local pairwise tests remain valuable for the narrower behavior they actually exercise.

Sources: dossiers006,017,019–020; final _peer.py and _router.py; NN04 for the independent NetherNet batching correction. No upstream test execution, external peer exchange or release verification was performed.

## Exact commit navigation {#exact-commit-navigation}

- [017 0894b496211c: change(peer): send and receive payloads verbatim without message-id framing](../dossiers/017-0894b496211c.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/0894b496211c39dd29cd08275d15b776a78f2f80)
- [019 3c24fba1741a: docs: replace design doc with runnable examples](../dossiers/019-3c24fba1741a.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/3c24fba1741a7d4b7a5bd66b382fd86898ec2219)
