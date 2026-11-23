<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:332"],"source_type":"public","date":"2026-02-13","topics":["lifetime","ffi","testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-332-fix-add-serverlistpingevent-back"></a>
# EndstoneMC/endstone #332: fix: add `ServerListPingEvent` back {#endstonemc-endstone-332-fix-add-serverlistpingevent-back}

Source: https://github.com/EndstoneMC/endstone/pull/332

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-02-13T20:06:10Z; recorded state closed; merged True.

## Discussion disposition {#discussion-disposition}

ServerListPingEvent restoration. Only Codecov bot commentary is captured: it says all coverable modified lines are covered while reporting 0.00% project coverage and a report one commit behind head. This is not proof of comprehensive tests.

The acquired patch is fully inspected below; no test-success claim is independently made.

## Direct patch findings {#direct-patch-findings}

Implementation moves from rewriting outgoing socket pongs to a gameplay peer's incoming datagram callback. It parses the native offline advertisement into mutable event fields, fires an explicitly asynchronous cancellable event, and constructs/sends an unconnected pong directly; returning false suppresses native processing, so cancellation now really suppresses a response. Remote host/port become SocketAddress, and Event acquires move operations to return the event by value. Network protocol is read-only, while other advertised values remain mutable. Native ABI declarations reorder Send/Ping virtuals, add adapter methods and socket Send; a new RakNet BitStream implements endian conversion, bit reads/writes and stack→heap growth. Direct risks: data[0] is inspected before a nonzero byte count guard; magic bytes are skipped without validation; minimum request length omits optional/read GUID and read results are ignored; advertisement stoi can throw without the old catch; signed-char length decode is retained; 400-byte MAX_OFFLINE_DATA_LENGTH is declared but unenforced and response length is narrowed to16bit. BitStream has allocating/reallocating paths but no destructor in its complete added declaration, leaking heap-backed responses beyond256 bytes. A global gameplay peer pointer and asynchronous callback introduce lifetime/thread-context assumptions not tested here. No tests are added; Codecov's bot claim is not a substitute for malformed-datagram, cancellation, long-advertisement or shutdown tests.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (50002 characters; SHA-256 49299197591cc75c082a929f318d5329d35dc6f9a4b49b6a68a8de27bc5e97a6), head bd756b1ebeb8ef2a1c23d068b1d0985b931604f6. For40 also verified exact-head src/endstone/core/registry.h cache ownership. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/332
- https://github.com/EndstoneMC/endstone/pull/332#issuecomment-3899662859
