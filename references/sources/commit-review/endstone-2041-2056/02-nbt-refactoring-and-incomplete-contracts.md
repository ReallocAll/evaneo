<!-- retrieval: {"source_ids":["public:commit:4d873d03cfdbea24e532922368b856dae13e2e98","public:commit:87418c7f701680da46a0c9148717470c7cecc40c"],"source_type":"public","date":"2024-12-24","topics":["lifetime","testing","api","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# NBT cleanup preserves and exposes incomplete contracts {#nbt-cleanup-preserves-and-exposes-incomplete-contracts}

## What changes {#what-changes}

2052 extracts CompoundTagVariant into a dedicated header with typed emplace, mutable/const access and dereference operators; normalizes Tag::Type to uint8 and hash signatures to size_t; relocates CompoundTag iteration; and renames ListTag's storage.2053 moves ListTag bodies into a source file and expands its interface with bounds-checked get/erase, typed getters, compound iteration and cloning. Most scalar tag changes are formatting/signature consistency, but the variant access surface and list bounds behavior are substantive.

CompoundTag's new header declares many typed getters and mutation helpers. The full endpoint implementation contains only a subset: the existing put operations, string/compound access, contains, isEmpty, copy, iterators and size. New declarations must not be counted as implemented features. CompoundTag::load still throws “Not implemented”. Its equals checks that every left-hand key matches the right-hand object but does not compare sizes, so a strict subset can compare equal in one direction. deepCopy clears this before iterating other, so self-copy empties the object. These residuals are visible context, not claimed introductions by2053.

## Parser and semantic risks that the cleanup does not fix {#parser-and-semantic-risks-that-the-cleanup-does-not-fix}

ListTag::load reads a signed count and reserves without a nonnegative/size-budget guard, then discards each child's Result and returns success after pushing the child. The default type field remains uninitialized until load/add, and add overwrites the list-wide type without enforcing homogeneous children. Equality compares vectors of unique_ptr, hence pointer identity rather than deep Tag equality; hash similarly uses pointer-based elements. Cloning creates independent elements, so a clone is not established equal under that implementation. get and erase gain index checks at2053, but popBack remains unchecked on an empty list. These are source-visible properties; malformed-input execution was neither needed nor performed.

ByteArrayTag's count handling and the native IDataInput semantics were not comprehensively validated. No parser hardening claim is justified by the title “clean up”. The extra APIs and safer typed getters should be credited separately from unresolved loader behavior.

## JSON conversion introduces an empty-container representation change {#json-conversion-introduces-an-empty-container-representation-change}

2053 moves NbtIo::toJson into a devtools nlohmann ADL serializer. The prior function explicitly initialized arrays/objects before looping. The new serializer appends entries to a default JSON value without explicit array/object initialization. Nonempty values may construct the expected shape, but an empty list, array or compound remains null. That changes output representation despite broadly similar switch branches. Conversion also belongs to the devtools translation unit rather than a reusable runtime function. No GUI rendering or JSON round-trip test was run.

## Practical use and endpoint {#practical-use-and-endpoint}

When reviewing a large structural cleanup, separately track behavior-preserving moves, signature/visibility changes, new implemented APIs, declarations-only APIs and semantic changes hidden inside serialization rewrites. Proposed verification includes clone equality, subset symmetry, self-copy, zero/negative/oversized counts, child read errors, empty-container JSON, empty popBack, homogeneous lists and linkability of advertised methods. These are proposed checks, not passing test results.

2052/2053 are ancestors of2056 by verified parent chain and remain part of this2024endpoint even though the hotfix notes only mention cancellation/logging. This owner stops at5310484c580f9077b436a58c8f90905f3ddff2c4. No later source ownership or current-release vulnerability claim follows from these historical observations.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-2052"></a>
### Commit 2052 {#commit-2052}

4d873d03cfdbea24e532922368b856dae13e2e98 · 2024-12-24T00:26:30Z

[refactor: clean up nbt-related codes](https://github.com/EndstoneMC/endstone/commit/4d873d03cfdbea24e532922368b856dae13e2e98)


Splits CompoundTagVariant into header with typed emplace/get operators, changes tag enum to uint8 and hashes to size_t, renames ListTag storage and relocates Compound iterators. Preserves existing ListTag child-load-result discard, pointer-based unique_ptr equality/hash, unchecked list length reserve and heterogeneous-add permissiveness. Refactor is not parser hardening.

Static review only; no upstream execution.

<a id="commit-2053"></a>
### Commit 2053 {#commit-2053}

87418c7f701680da46a0c9148717470c7cecc40c · 2024-12-24T01:15:20Z

[refactor: clean up CompoundTag class](https://github.com/EndstoneMC/endstone/commit/87418c7f701680da46a0c9148717470c7cecc40c)


Moves ListTag implementation to source; adds bounds-checked get/erase and type-checked scalar/compound getters plus callback iteration. Many new CompoundTag typed APIs are declarations without definitions at endpoint. Moves NBTJSON conversion into devtools ADL serializer, losing explicit empty array/object initialization: empty containers become null. ListTag popBack remains unchecked and load still ignores child Result; deepCopy self-alias clears source. No compile or malformed-input tests run.

Static review only; no upstream execution.
