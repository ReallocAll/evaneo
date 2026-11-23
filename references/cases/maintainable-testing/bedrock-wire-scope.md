<!-- retrieval: {"source_ids":["public:commit:b7b436a12cfa53df1c0784163a8dd26132408dc0"],"source_type":"public","date":"2026-10-30..2026-11-10","topics":["maintainability","complexity","refactoring","networking","api","dependencies","review"],"limitations":"Static inspection of PR #2, source commits and merged-tree documentation; upstream tests and runtime behavior were not independently reproduced. Commit messages are author explanations, not measured outcomes."} -->
# Bedrock wire codecs: remove a shared-looking layer without a shared contract {#case}

## Observed change {#change}

[EndstoneMC/bedrock-protocol PR #2](https://github.com/EndstoneMC/bedrock-protocol/pull/2) began with a reusable wire library: batch framing, DEFLATE/Snappy, encryption, directional state, prepared packets and packet-level recovery. The later [b7b436a12cfa](https://github.com/EndstoneMC/bedrock-protocol/commit/b7b436a12cfa53df1c0784163a8dd26132408dc0) **deleted** the wire library and its Python wrappers. This was a scope reversal within the same PR, not evidence of an upstream release of those features.

The commit explains the consumer mismatch. Packet-body serialization is protocol-schema work, but transport negotiation, batching and encryption depend on connection role and lifecycle: a client, proxy and server do not necessarily frame or recover identically. The named downstream client already performed its own framing. Retaining the library would pull OpenSSL, zlib and Snappy into native runtime wheels even for packet-only consumers. Once `BatchCodec` was removed, `prepare_packet`, `EncodedPacket` and batch-specific recoverable errors had no remaining consumer; they were removed too. Packet-body tests were redirected to the remaining packet codec.

## Transferable decision {#judgment}

When evaluating a proposed shared layer, ask **which concrete consumers need the same operation, state owner and error contract**. A common protocol format does not, by itself, prove that compression, encryption or connection state should be shared. Prefer the narrow packet codec here; leave transport/session policy with the actual transport user until demand establishes a stable common contract. If the only consumer of an auxiliary abstraction disappears, reevaluate the auxiliary abstraction as well.

This does **not** say batch/framing libraries are intrinsically wrong. They are justified when multiple actual consumers agree on the interface, state lifetime, security requirements and deployment dependency costs. Removing a required integrity check or misplacing an encryption boundary would be a regression, not simplification.

## Evidence and limits {#limits}

Primary evidence: [b7b436a12cfa](https://github.com/EndstoneMC/bedrock-protocol/commit/b7b436a12cfa53df1c0784163a8dd26132408dc0) (commit message and deletion diff). The initial [b7b436a12cfa](https://github.com/EndstoneMC/bedrock-protocol/commit/b7b436a12cfa53df1c0784163a8dd26132408dc0) parent tree had a wire library; merged PR documentation and `CMakeLists.txt` no longer expose its build target. Dependency reduction is grounded in removed declarations, not a measured package-size or performance benchmark. No live RakNet/NetherNet connection testing was performed here.

Related earlier decision: [Bedrock: protocol compiler](bedrock-protocol-compiler.md) narrowed an *initial compiler scaffold*, whereas this case removes a *transport-level extension*. These are distinct changes, not duplicate counts.
