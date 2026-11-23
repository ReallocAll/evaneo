<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:356"],"source_type":"public","date":"2026-04-04","topics":["lifetime","concurrency","ffi","testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-356-async-network-packet-processing-via-rewrittenbatchpeer-asio-strand"></a>
# EndstoneMC/endstone #356: Async network packet processing via RewrittenBatchPeer + asio strand {#endstonemc-endstone-356-async-network-packet-processing-via-rewrittenbatchpeer-asio-strand}

Source: https://github.com/EndstoneMC/endstone/issues/356

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-04-04T14:03:48Z; recorded state closed; merged not applicable.

## Bottleneck and native constraints {#bottleneck-and-native-constraints}

wu-vincent's proposal is based on reported disassembly of Windows BDS 1.26.10.4. Server receive performs decrypt/decompress/batch splitting plus deserialization and handler dispatch on the main thread. Outbound becomes async only after authorization, using one shared NETWORK worker. The connection constructor builds PacketTrace→Batch→Compressed→optional Encrypted→RakNet; onNewIncomingConnection is a later injection opportunity, not the chain constructor.

## Proposed architecture and alternatives {#proposed-architecture-and-alternatives}

Replace only BatchedNetworkPeer with an ABI-compatible subclass, retain tracing/compression/encryption peers and their weak pointers, and share a fixed asio io_context worker pool. A per-connection strand serializes both directions because cipher/counter/HMAC state requires packet order; connections may parallelize, packets within one connection may not. A second BufferedRakNetPeer leaf shim drains the native unsynchronized read buffer on the main thread into a raw SPSC queue. Workers perform codecs and batch splitting into a decoded SPSC queue; main-thread deserialization, events and handlers remain unchanged. Simply enabling existing native async send earlier is cheaper but leaves one-worker send and synchronous receive bottlenecks.

## Activation, lifetime and revision-sensitive hazards {#activation-lifetime-and-revision-sensitive-hazards}

Stay synchronous through handshake until native mAsyncEnabled flips after encryption configuration. On activation flush buffered base data once, then post receive work. A pointer-to-shared_ptr-slot walk supports both head and interior replacement without mutating intermediate ownership; lock the old peer, copy its inner shared pointer, and splice before worker activation. Posted tasks retain shared_from_this, and the proposal asserts inner-chain destructors are worker-safe for this binary. Unused base TaskGroup/SPSC allocation is an accepted ABI-compatibility cost. update() stays on main because it carries native receive-buffer drain; codec send/receive run on the strand. Flush callbacks are proposed to fire inline on main at enqueue, defining completion as handoff rather than actual network delivery.

## Claims, limitations and reusable knowledge {#claims-limitations-and-reusable-knowledge}

No performance measurement, code patch, load test or independent binary verification accompanies this issue; comments are encouragement only. The claimed 50+ player TPS gain is an expectation. Its assertion that a plain bool store/load on x86 is release/acquire must not be generalized into valid C++ cross-thread synchronization: hardware ordering does not erase C++ data-race rules. Likewise worker-safe destructor conclusions are explicitly version-specific. #412 is the implementation/revision source and should decide final ownership/gating details. The reusable decision is to draw exact thread-ownership boundaries and preserve native handshake/lifecycle constraints before offloading expensive codecs.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/356
- https://github.com/EndstoneMC/endstone/issues/356#issuecomment-4187280839
- https://github.com/EndstoneMC/endstone/issues/356#issuecomment-4187466671
