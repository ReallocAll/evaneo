<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:278"],"source_type":"public","date":"2025-10-17","topics":["lifetime","concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-278-proposal-nbt-apis"></a>
# EndstoneMC/endstone #278: Proposal: NBT APIs {#endstonemc-endstone-278-proposal-nbt-apis}

Source: https://github.com/EndstoneMC/endstone/issues/278

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

## Draft status and purpose {#draft-status-and-purpose}

Wu's November 11, 2025 updated proposal defines an explicit-typed JSON-like DOM for Bedrock LE-NBT in C++/Python. The captured body is a complete substantial draft, not a merged implementation; only stale automation follows. It revises earlier NBT discussions 97 toward a typed standalone DOM with SNBT and binary I/O, without establishing that all earlier serialization promises shipped.

## Intended data/ownership contract {#intended-data-ownership-contract}

Tag stores a variant of End(monostate), unsigned Byte, signed Short/Int/Long, Float/Double, String, ByteArray/IntArray, List and Compound; LongArray is unsupported. Scalar ValueTag wrappers expose read-only payloads, replaced at parent keys; lists/compounds/typed arrays mutate in place. is_mutable_tag_v drives get/get_if constness. Python indexing returns node-bound wrapper/proxies with the same scalar/container distinction. Explicit construction avoids guessing numeric widths or interpreting programmatic empty braces as compounds; textual SNBT {} remains allowed. Compound entries use an ordered map and can change kind. Lists fix homogeneous element type on first non-End insertion and retrofill earlier End placeholders, with nonempty serialized lists prohibited from containing End. Equality is intended deep and cross-kind-sensitive.

## I/O, constraints and unresolved mechanics {#i-o-constraints-and-unresolved-mechanics}

SNBT exposes indentation, ASCII escaping, whitespace, key sorting, comments/trailing-comma/NaN options; binary I/O exposes endian, named-root, compression and zlib level. Parse depth and compressed-size limits/fail-closed decompression are requirements, but no concrete bounds or implementation appear. Numeric runtime range checks are explicitly excluded, shifting conversion responsibility to callers/bindings rather than establishing safe arbitrary integer coercion. Indexing can self-shape End into List/Compound; at() reports absent/wrong-kind/OOB errors.

Static draft inconsistencies to resolve before implementation: explicit Tag wrapper constructors conflict with shown copy-initialization/implicit assignment examples unless conversion/assignment operators are added; defaulted scalar constructors leave arithmetic payload initialization unspecified in the declaration shown; mutable Tag& list access/iterators can bypass homogeneous-type enforcement; ListTag equality compares elements but omits its fixed element_type, leaving empty typed-list semantics unspecified. Proxies need lifetime/invalidation rules when parent nodes are replaced or vectors resize. The draft declares C++ primitive/brace rejection as runtime errors but its shown overload set more naturally produces compile-time errors or default End assignment; enforcement is not supplied. These are reviewer observations, not disagreements raised by participants. They do not negate the useful explicit typing, immutable scalar, mutable container and bounded parsing design goals.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/278
- https://github.com/EndstoneMC/endstone/issues/278#issuecomment-3735828471
