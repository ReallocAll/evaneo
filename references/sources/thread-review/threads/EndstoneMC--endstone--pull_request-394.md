<!-- retrieval: {"source_ids":["public:commit:682a0a2d5ad8f0faa7e7fc95618ad00a1bdf6d8d","public:thread:EndstoneMC/endstone:394"],"source_type":"public","date":"2026-05-16..2026-05-25","topics":["lifetime","concurrency","ffi","testing","build","performance","api","documentation","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-394-feat-add-support-for-bds-version-1-26-20"></a>
# EndstoneMC/endstone #394: feat: add support for BDS version 1.26.20 {#endstonemc-endstone-394-feat-add-support-for-bds-version-1-26-20}

Source: https://github.com/EndstoneMC/endstone/pull/394

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-05-16T20:27:39Z; recorded state closed; merged True.

## Disposition {#disposition}

Merged BDS 1.26.20 support PR. Primary body is empty; comments express excitement and request 26.21. No engineering reasoning or test report in discussion. The complete version-port patch was subsequently inspected below.

## Full port, toolchain and symbol workflow {#full-port-toolchain-and-symbol-workflow}

The complete named base-to-head diff was read, including all generated symbol entries. This port changes protocol944→975, moves Windows consumers to clang-cl/lld-link, requires Ninja and Windows CMake3.29, turns off C++ module scanning, and makes C++20 required without extensions. CI scopes the compiler override to the consumer while dependencies keep MSVC; the checked-in Windows profile does not itself carry that consumer scope. A repository-local Conan home/profile replaces repeated platform settings; backend minimum-version constraint is removed. Detours loses /WX and the rejected MSVC-only /Gm- flag, narrowing warning enforcement for third-party code rather than proving warning cleanliness.

The porting guide expands failure classification, foundational-type review and full-diff cross-validation. Useful lessons: a byte-pattern match is not a verified symbol name; prologue matching must remove call-site RIP-decoding flags; alias-to-concrete-type changes require real declarations, not only renamed keys; an optimized-away this argument changes calling convention; and an inlined hook must move to a surviving caller with its trigger reconstructed. The guide contradicts its own earlier 'unresolved hooks are disabled' statement with the later correct boundary that consumed missing consteval symbols fail compilation. Its positive/monotonic RVA-delta rule is a heuristic, not universal: the Windows table here itself contains major negative shifts. 'Both platforms failed implies signature change' is likewise a triage hypothesis, not proof. Statements about legal safety/private artifacts are source assertions, not a legal conclusion or permission to redistribute those artifacts.

PDB lookup now falls back per unresolved entry to scanning the adjacent executable or downloading the configured version. Missing .text raises; missing signatures log and retain zero. There is no validation that an adjacent binary matches the PDB/config version, so name-verified and pattern-verified entries can otherwise be mixed from different builds. No new scanner tests prove uniqueness, correct displacement or old/new binary identity.

## Structural ABI and behavioral changes {#structural-abi-and-behavioral-changes}

Certificate/legacy-token declarations and hooks disappear, BaseConnectionRequest gains the shared request fields/virtual interface, and both request kinds inherit it. Raw-token access still dereferences without a local null guard. The removed hook enforced a3MiB input limit, certificate-chain count<=10 and malformed-JSON rejection; its deletion follows removal of the modeled certificate type, but the patch supplies no equivalent-limit regression proving the new native path protects the same boundary. Authentication info gains account permissions. Player initialization uses reference_wrapper rather than nullable request pointers, and subclients report server target version because their request no longer exposes a game-version field.

Packet payload restructuring affects disconnect, inventory slot, equipment and sounds. Inventory slot gains optional full-container/storage fields; equipment drops redundant byte fields; disconnect becomes reason plus message/null variant and drops skip_message from the handler. Native packet allocation is retained. BinaryStream inserts writeSignedByte into its virtual sequence; this matters beyond the method's simple byte-write body. DimensionType becomes a concrete integer struct, with all ID access and signature keys changed. MaterialType narrows to uint8 and Material size12→7. Actor flags cross128 bits and use explicit64bit brstd::bitset words. Block component storage gains a weak subscriber, growing Block/BlockType offsets; event variant additions, account/nonces, callback-token and player string fields, virtual insertions/removals and the new knockback parameter aggregate all require exact native ABI matching.

Furnace lookup changes from scanning recipe keys to a tag-hash-indexed map: exact id/aux wins, then wildcard aux constructed through the native item method. This explicitly establishes precedence absent from the prior scan; hash truncation/layout correctness and wildcard/user-data cases need fixtures. ItemStackBase::init is copied locally and calls mapped _setItem: negative count becomes0, positive count narrows to uint8, aux narrows to int16 when positive, then zero count clears. Counts above255 therefore wrap rather than fail; constructor and public setter policies remain distinct.

Linux MapInitialize interception moves from an inlined loader to getMapSavedData. It records cache presence before native lookup and schedules an event only for previously absent successful loads; Windows retains direct loader hook. Both schedule onto the server thread because loads may occur elsewhere. The precheck is not a synchronization primitive, and captured map/server references still require lifetime guarantees through task execution. Repeated concurrent first loads and shutdown are not tested. Linux leaves randomTick becomes static to match optimized-away this while Windows keeps a const member; the symbol key and hook declaration change together. Command parameters now point to a stable specialized ParamParseRule and retain a separate parse_override slot.

## Validation and applicability {#validation-and-applicability}

Three existing binary-stream tests gain complete-consumption assertions. No new automated test covers signed-byte virtual dispatch, scanner fallback, ABI sizes against a running binary, count narrowing, furnace wildcard precedence, map-event deduplication/thread lifetime, removed authentication guards or client packet rendering. Treat this as a multi-layer porting checklist and a record of observed code changes, not a passing compatibility result. Empty discussion contains no extra rationale beyond the implementation and guide.


## Code and verification boundary {#code-and-verification-boundary}

Inspected complete named base-to-head diff (237774 characters / 237776 bytes; SHA-256 e3e879baea488fb05bb60209f76491e75a98c30d59b2f68c8eb77aa8b95576f0) and captured PR patch identity 4b696d2e8c42100e44c3ea37afc689d9179bfa1e2595254c290d3a79d43ddf23, head dded6882709967bcd7d421077b882dcb4b750bc4. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/394
- https://github.com/EndstoneMC/endstone/pull/394#issuecomment-4493923129
- https://github.com/EndstoneMC/endstone/pull/394#issuecomment-4499416602
