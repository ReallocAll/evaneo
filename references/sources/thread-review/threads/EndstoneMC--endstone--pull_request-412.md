<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:412"],"source_type":"public","date":"2026-06-02","topics":["lifetime","concurrency","ffi","testing","performance","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-412-feat-network-offload-packet-codec-to-an-async-strand-pool"></a>
# EndstoneMC/endstone #412: feat(network): offload packet codec to an async strand pool {#endstonemc-endstone-412-feat-network-offload-packet-codec-to-an-async-strand-pool}

Source: https://github.com/EndstoneMC/endstone/pull/412

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-06-02T22:53:22Z; recorded state closed; merged False.

## Implementation proposal and relation to #356 {#implementation-proposal-and-relation-to-356}

This unmerged PR implements the strand-pool design: ABI-compatible 344-byte BatchedNetworkPeer subclass with async gate at +0x150, post-auth codec offload, main-thread plugin events and packet patching, BufferedRakNetPeer raw SPSC queue plus decoded return queue, and RAII EventLoopGroup that joins workers. Native handshake stays synchronous. Per-connection serialization preserves cipher/HMAC order despite handlers hopping worker threads.

## Refined ownership and verification {#refined-ownership-and-verification}

The body explicitly assigns activated_ to main only (non-atomic), recv_scheduled_ to an atomic single-in-flight guard, send batch to main and decoding buffers to strand. This is more precise than #356's plain-bool cross-thread claim. Posted work holds shared_from_this across disconnect; worker-side native destruction is asserted safe based on 1.26.10.4 disassembly, even though reported gameplay testing used 1.26.20.5. That cross-version verification boundary must remain visible.

Windows build/link, layout assertion and basic connections/gameplay are reported successful. A configurable worker count (currently cpu−2) and 50+ connection ordering/teardown load test remain unchecked. No discussion explains closed-unmerged state. Do not equate this PR with the final shipped async design, or infer measured TPS improvement from the proposal.

## Direct patch findings {#direct-patch-findings}

The final code differs materially from the early strand-pool description: EventLoopGroup creates one dedicated thread per io_context and round-robins each connection onto a permanent executor. It is serialized and thread-affine, with several connections sharing a loop, as explicitly compared to Netty in the added comment. No general strand hopping remains. Main-thread batching/events/packet patching is preserved; the leaf's native receive buffer is drained only on main into an SPSC raw queue, codec output into a second queue. Async activation waits for native async_enabled_, flushes the synchronous batch once, then posts send/decode tasks holding shared_ptr self. Every update posts at most one recv task via atomic exchange. Decoded queue capacity is approximately1024; raw queue and outbound posted work have no explicit bound, so this is not global backpressure. Final async config defaults true in shipped template but false when missing from existing config, with CPU−2 threads (minimum1) and experimental warning. The pool destructor resets work guards, immediately calls stop, then joins: this can abandon queued tasks rather than drain all work. Async flush calls its callback when queued on main, not when sent. Worker decode stores only string, dropping original receive timestamp; non-HasData statuses are not forwarded to main. Reconstructed batch parser has an edge path where a length exceeds remaining buffer without advancing past data or marking BrokenData, potentially returning empty HasData repeatedly until bounded decoded queue fills; malformed input parity needs tests. ABI assertions cover344/320 bytes, but layout agreement alone does not validate destructor thread safety, native flags or all chain variants. Full patch includes no automated tests, stress harness or timing measurements; Windows gameplay claims and unchecked multi-client/Linux teardown limits remain source-reported.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (61543 characters; SHA-256 c97534b4cf07a02e656d21799d7ea7c7d4e3a6d64a6ae8aebdaa74852b62786b), head b749da2e09f7e81a046b72011d3624f53df67800. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/412
