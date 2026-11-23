<!-- retrieval: {"source_ids":["public:commit:129ca3f2aa9021f6e819d7a917220fac17875e83","public:commit:29c3bc26c0722a7436b4d3df3eff250ca0e68892","public:commit:6dc6428eda81f3f523ab9bb29d6ed814a9b875ad","public:commit:6fd55a4fd2cd3710755fa3036a30d45ade43a699","public:commit:7c99923bc41dd26b181b7086c239fe4638dfc7a4","public:commit:c4b9f52d6965ce5429b29b8ed90b86a5858110b2","public:commit:d6ae2bb3b8039bc0a9822098640a93b24f714715","public:commit:d6de0c0110fdc43662e7498160626bc536e38501","public:commit:da6aa69bc930a20cbae69c6194b34a8d7263dadb","public:commit:e9c466a554ca7ed6885580a8e77f323a95d9f4db"],"source_type":"public","date":"2026-07-27","topics":["lifetime","concurrency","ffi","testing","api","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="rp03-make-asynchronous-ownership-explicit-across-a-native-receive-pump"></a>
# Make asynchronous ownership explicit across a native receive pump {#rp03-make-asynchronous-ownership-explicit-across-a-native-receive-pump}

## One engine, two waiting models {#one-engine-two-waiting-models}

The synchronous facade uses one daemon receive pump per Peer. A shared Router classifies native packet IDs and calls sink methods. Connection objects are indexed by GUID, pending connects/pings by endpoint, and accept results go to a queue. A Condition-protected mailbox retains messages until read. Closure is sticky: existing data drains before a clean or error exception is raised, and close wakes blocked readers.

The asyncio facade reuses the same native peer/router and replaces waiting primitives with loop events and queues. Pump callbacks enter the loop with call_soon_threadsafe. This avoids a second protocol implementation, while retaining a boundary between native-thread delivery and loop-owned scheduling. Async close offloads thread joining and native shutdown to to_thread. Factories eventually move startup off the event loop; direct construction remains synchronous and is documented as such.

## Three repairs address different races {#three-repairs-address-different-races}

First, a close-versus-register repair moves a second _closed check under the same lock used to insert pending work. That prevents registration after the close snapshot at that point. The native connect/ping call still occurs after the lock is released; the patch does not claim that all startup/close interleavings have disappeared.

Second, pending response identity is corrected. The initial fallback pops the only outstanding request even if its key does not match the response endpoint. DNS names exacerbate this because RakNet returns a numeric address. The revised code resolves the hostname first, prefers IPv4, and consistently uses numeric IP plus port in the native call and table. Concurrent connections to different servers become a meaningful regression test. The table still contains one pending slot per endpoint, so the tests do not establish support for concurrent pings to the same endpoint.

Third, timeout cleanup distinguishes which side owns the pending operation. _abandon_connect reports whether it removed the entry. A synchronous timeout that loses to the pump waits for the pump's event and closes any connection that was established during the race. The async version only closes a connection if pending.connection is already assigned when cancellation is caught. The pump pops the entry before assigning connection and setting the event; that leaves a static interval to examine. No reproduced failure or cancellation regression accompanies this path.

## Failure is an outcome, not a vanished background thread {#failure-is-an-outcome-not-a-vanished-background-thread}

The receive loop catches BaseException, begins close under the shared lock, shuts down the native peer, closes connection mailboxes with a traceback-bearing ConnectionClosedError and wakes pending connects, pings and accepts. It then reraises on the pump thread. A fault-injection test makes routing fail and checks that a waiter observes failure instead of hanging. This is direct evidence for propagating background work failure through the public waiting contract.

The normal close path remains distinct. Iterator termination suppresses only clean closure; unexpected disconnection remains visible. Per-connection serving closes its connection in finally. However, sync handlers are daemon threads and are not joined; async serve_forever retains tasks but does not cancel/gather them when the serving loop exits. A task set for bookkeeping is not automatically a structured shutdown guarantee.

## Backpressure is an opt-in message count {#backpressure-is-an-opt-in-message-count}

max_queue defaults to None. Sync mailboxes enforce capacity while holding their Condition. Async mailboxes use a soft count shared by pump and event-loop execution; the source explicitly tolerates a small race. Overflow removes the connection, requests native close and records ConnectionClosedError after queued messages drain. This bounds the number of retained application messages only, not their byte size or all global queues. Zero and negative limits are not validated in the inspected source.

The original overflow test read messages while waiting for overflow, accidentally relieving the pressure it intended to create. The final fix waits for connected to become false with a monotonic deadline, then drains and expects the overflow exception. This tests causal order rather than lengthening a sleep or weakening the assertion. It is a useful example of improving a focused regression without adding redundant broad stress tests.

## Cancellation boundaries still deserve separate review {#cancellation-boundaries-still-deserve-separate-review}

Async connect/ping await to_thread(start...) before entering their cancellation cleanup scopes. Async factories similarly await _create before the factory's try/finally owns the peer. Cancelling these awaits does not stop the underlying thread; a constructed peer or pending native operation can finish after the caller has lost its result. Async close sets _closed before its awaited joins/shutdown; if that close is cancelled, later close sees the flag and may not execute the remainder. These are source-level ownership concerns to investigate when extending the code, not demonstrated leaks or hangs.

## Application {#application}

Use this chain to review a wrapper's state transitions: who may remove pending work, who must publish completion, who reaps a late success, and who wakes every waiter on failure. Keep shutdown completion separate from a boolean closed state. Choose a small number of tests around those contracts and causal interleavings; do not infer that every legacy stress scenario must be retained. The right queue bound and handler shutdown policy depend on the caller's workload and ownership requirements.

Sources: dossiers006–008,012–016,018,027 and complete final _peer.py/asyncio.py/_router.py snapshots. Credential-guarded lines were not reconstructed. All concurrency observations are static; tests, thread scheduling and native behavior were not executed.

## Exact commit navigation {#exact-commit-navigation}

- [006 e9c466a554ca: feat: add pythonic sync API (Peer/Connection) on top of the raw binding](../dossiers/006-e9c466a554ca.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/e9c466a554ca7ed6885580a8e77f323a95d9f4db)
- [007 c4b9f52d6965: feat: add asyncio API mirroring the sync API](../dossiers/007-c4b9f52d6965.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/c4b9f52d6965ce5429b29b8ed90b86a5858110b2)
- [008 6fd55a4fd2cd: feat: add Peer.serve_forever(handler) to the sync and asyncio APIs](../dossiers/008-6fd55a4fd2cd.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/6fd55a4fd2cd3710755fa3036a30d45ade43a699)
- [012 7c99923bc41d: fix(peer): re-check closed state under the lock when registering connect/ping](../dossiers/012-7c99923bc41d.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/7c99923bc41dd26b181b7086c239fe4638dfc7a4)
- [013 129ca3f2aa90: fix(peer): tear the peer down if the receive pump crashes instead of hanging](../dossiers/013-129ca3f2aa90.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/129ca3f2aa9021f6e819d7a917220fac17875e83)
- [014 d6ae2bb3b803: fix(peer): resolve hostnames up front and match pending ops by exact address](../dossiers/014-d6ae2bb3b803.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/d6ae2bb3b8039bc0a9822098640a93b24f714715)
- [015 6dc6428eda81: feat(peer): add optional max_queue backpressure that closes on overflow](../dossiers/015-6dc6428eda81.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/6dc6428eda81f3f523ab9bb29d6ed814a9b875ad)
- [016 29c3bc26c072: fix(peer): close the orphaned connection when a connect times out mid-handshake](../dossiers/016-29c3bc26c072.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/29c3bc26c0722a7436b4d3df3eff250ca0e68892)
- [018 da6aa69bc930: perf(asyncio): construct peers off the event loop so startup does not block it](../dossiers/018-da6aa69bc930.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/da6aa69bc930a20cbae69c6194b34a8d7263dadb)
- [027 d6de0c0110fd: test: make max_queue overflow test deterministic](../dossiers/027-d6de0c0110fd.md) · [public source](https://github.com/EndstoneMC/raknet-python/commit/d6de0c0110fdc43662e7498160626bc536e38501)
