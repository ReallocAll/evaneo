<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:458"],"source_type":"public","date":"2026-08-04","topics":["lifetime","ffi","testing","api","documentation","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-458-feat-add-26-40-support"></a>
# EndstoneMC/endstone #458: feat: add 26.40 support {#endstonemc-endstone-458-feat-add-26-40-support}

Source: https://github.com/EndstoneMC/endstone/pull/458

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-08-04T17:22:47Z; recorded state closed; merged True.

Empty primary description and an empty approval. The merged 26.40 support patch is the engineering evidence; no authored rationale can be inferred from the title.

## Complete port and a verified signature failure {#complete-port-and-a-verified-signature-failure}

The full206628-character named diff was read; ordered added/deleted lines exactly match the190887-character captured patch. Protocol1001→2168 is a discontinuous renumbering, so successor-range heuristics are invalid. The guide explicitly retreats from positive/monotonic RVA deltas when linker order changes and documents a concrete singleton-accessor failure: wildcarded prologues matched18different functions, with a coincidentally correct lowest address in two releases. The replacement getI18n recipe anchors a caller's distinctive immediate-encoded localization string and verifies the callee's marker-string closure.

Yet this final patch retains another exact failure of its own documented rule. Windows ItemInstance::fromTag changes an E8 call-site pattern to a direct prologue beginning55 41 56 56 57, but keeps rip_relative=true and rip_offset=1. The scanner interprets those instruction bytes as a signed displacement. The generated table contains1494353894 for that function. Exact head784c920701d6f929a0600eb729d5a51846817143 confirms both configuration and table; this is a historical source-level defect, not a runtime reproduction or claim about current HEAD. The reusable rule is to validate transformation metadata and resolved target together, then enforce address-section/function-boundary checks automatically, rather than merely recording the warning in a guide.

find_signature now enumerates matches and distinct resolved addresses and logs an ambiguity warning, but still returns the first match. Multiple call sites can legitimately resolve to one target; multiple targets are not rejected. It also resolves all candidates without a new bounds/error guard, so a bad secondary match can fail decoding even if the first was usable. The source guide says to treat ambiguity as unresolved, but code does not implement that policy. Download tooling falls back to official current-version links only on metadata404, checks a filename version prefix, logs 'unverified' and reuses cached bytes without a trusted hash. This is an explicit integrity tradeoff; no scanner/download tests accompany it.

## ABI investigation knowledge and its limits {#abi-investigation-knowledge-and-its-limits}

The expanded guide triangulates raw-binary evidence from constructors/destructors, packet field access, unwind/function ranges, RTTI relocation addends, distinctive strings and old/new caller relationships. It distinguishes ownership-kind changes (unique_ptr→shared_ptr, unique_ptr→inline optional), platform-specific string/container sizes, base tail-padding reuse, whole-object size versus prefix declarations, and net size deltas hiding multiple changes. Unknown types/slots are marked TODO rather than given falsely verified semantic names. Size assertions only compare the modeled declaration to a literal; they do not query the native binary. A live accessor and independent constructor/serialization paths are stronger evidence than a successful startup alone.

Several categorical guide statements remain heuristics: an expanded zeroing store does not by itself prove a new member; equal outer vtable anchors cannot rule out interior net-zero insert/delete pairs; successful original-call return does not universally prove a valid this pointer; and function-size/constant/caller intersections are corroboration, not mathematical identity proof. The later#534 guide explicitly warns about net-zero vtable edits. Windows leaf accessors and thunks can lack unwind records, already acknowledged elsewhere in this patch despite 'authority' wording. Preserve these qualifications when turning the history into reusable guidance.

## Packet-layout corrections and behavior {#packet-layout-corrections-and-behavior}

PlayerAuthInput and UpdateSoftEnum now use aligned payload subobjects rather than flat derived members. Linux reused Packet tail padding in the old flat form: equal total sizes can conceal wrong early field offsets. This explains why checking only Windows or sizeof missed movement/rotation reads. All consumer paths move to payload fields. Soft enums use SideBySide_LogOnMismatch; player input read/write remain unimplemented locally and depend on native allocation/dispatch.

Map packets gain a standalone map_id, reordered payload, and serialization mode. The old getMapId read map_ids.front(), but that vector is empty on non-creation paths; code now reads the standalone ID. Renderer rewrites both decorations and unique_ids, inserting INVALID_ID per visible custom cursor, preserving the parallel-array length invariant. It still assumes native pixel storage agrees with width/height, and the early return for empty pixels/decorations leaves no opportunity to add cursors to that empty packet. The patch adds no packet fixture proving all creation/texture/decoration combinations or client rendering.

CraftingData becomes separate typed vectors of shaped/shapeless/multi/smithing payloads, with platform-aware sizes and optional unlocking requirements. prepareFromRecipes returns the full payload aggregate rather than unique_ptr packet, requiring correct hidden-return ABI; Windows mangled name changes while Linux name does not. DevTools dumps adapt to typed fields, resolve numeric item IDs through registry, and base64 the pre-serialized user-data buffer. This changes the NBT source from the old explicit big-endian named-tag writer; encoding compatibility is not demonstrated. Unlocking requirements and assume_symmetry are modeled but not added to dumped JSON. Missing/invalid registry IDs remain unguarded.

## Ownership, lifecycle, public headers and validation {#ownership-lifecycle-public-headers-and-validation}

Connection raw token changes to inline optional; authentication display-name storage moves. NetworkSystem, ServerInstance and Minecraft members change ownership kind and introduce new offsets. DedicatedServer drops a base. initializeServer now forwards a32-byte opaque aggregate instead of bool; opaque pointer pairs deliberately avoid releasing native-owned reference counts, but exact nontrivial-return ABI still needs runtime validation. New virtual placeholders and event alternatives preserve positions without pretending their names are known. Knockback damage changes int→float, bed sleep adds bool/float arguments, and hook forwarding follows them.

Public headers stop including Windows.h and hand-declare the two needed imported functions; CMake propagates NOMINMAX/WIN32_LEAN_AND_MEAN. This reduces transitive macro pollution while making declaration/SDK compatibility a maintained contract. Many packet size assertions are added and incomplete prefixes marked. There are no new automated tests in this patch for signature ambiguity, address validity, public-header include order, aggregate-return forwarding, movement payload offsets, map arrays or recipe dumps. Empty review approval supplies no additional test evidence.


## Code and verification boundary {#code-and-verification-boundary}

Inspected complete named base-to-head diff (206628 characters / 206634 bytes; SHA-256 5a78a46751bf236b2c4458fb58f34a44a771b27ad96b07b68ec8a0dd85c943e8), captured PR diff SHA-256 18784cc719ab0171f68d972c2e3ba62ce0e89f08e9aadc971604c11473d4992a, head 784c920701d6f929a0600eb729d5a51846817143. Exact identity evidence: port-code-identities.json; ItemInstance signature rechecked in exact head. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/458
- https://github.com/EndstoneMC/endstone/pull/458#pullrequestreview-4867464077
