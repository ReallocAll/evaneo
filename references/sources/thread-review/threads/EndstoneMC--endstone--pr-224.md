<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:224"],"source_type":"public","date":"2025-07-22","topics":["lifetime","concurrency","ffi","testing","api","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-224-feat-1-21-100-support"></a>
# EndstoneMC/endstone #224: [feat] 1.21.100 support {#endstonemc-endstone-224-feat-1-21-100-support}

Source: https://github.com/EndstoneMC/endstone/pull/224

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (1448 additions, 856 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu authored and merged this version port. The primary body reports Windows and Linux tested. The only review text is Wu's own concern that part of the symbol table looks wrong, with an empty COMMENTED review body; there is no detailed rationale, test transcript or external reviewer approval to infer.

### Complete patch inspection {#complete-patch-inspection}

The complete 113-file diff moves the targeted package and symbols from 1.21.95 to 1.21.100-preview.25 and protocol 819 to 827. This is an ABI/protocol migration, not a cosmetic version bump. Windows and Linux symbol tables, native class layouts, virtual interfaces, authentication, packet serialization and resource ownership all change.

Authentication now obtains trusted AuthenticationInfo from the game-server token, with verified request/token checks replacing the old certificate-validity path. Ban checks derive authenticated UUID/XUID and use the third-party client name only when XUID is empty. The patch therefore changes the provenance of identity fields; it does not establish that arbitrary client-supplied names are authenticated. NetworkSystem gains reflection context and packet override settings; outbound hooks call writeWithSerializationMode instead of the old manual write. New packet payload wrappers and SideBySide_LogOnMismatch defaults change where title, form, death, transfer, action and game-mode fields live. Existing callers are migrated to payload fields. Many serializer functions remain declarations delegated to native implementations, so reading headers does not prove byte-for-byte compatibility. Transfer port narrows to uint16_t while the public caller still accepts int.

BlockLegacy is renamed to BlockType across block/item descriptors, stacks, state access and vanilla-data dumping. The registry changes from a static enumerator to an instance obtained from Level, and native calls now pass this. A new isChestBlock virtual slot and the changed Level/Container interfaces make this more than a textual rename. BlockActor shrinks from 240/216 to 160/144 bytes (Windows/Linux assertions), moves its type to uint8_t and packs flags into EnumSet. Container open/close uses Actor rather than Player; Level adds entity insertion, tick-death settings and mutable serialization context. Biome names are explicitly full names. Assertions constrain declared sizes, not native offsets or runtime validity.

Resource-pack storage becomes shared, asynchronously queried and lockbox-protected. _getPacks copies shared pointers under a shared lock before invoking callbacks, separating callback lifetime from storage lifetime. However _setPacks and _setReport also take lockShared while mutating storage; concurrent readers/writers are not excluded by a shared mutex. The rvalue arguments are copied rather than moved. PackManifest layout expands substantially and is explicitly partial; unused callback maps are commented out. The new SharedLockbox also permits mutable callback access under shared locking. These are static concerns, not reproduced crashes.

The final Windows table still assigns the same address to Mob::knockback and Mob::_hurt, while Linux has distinct addresses. Wu's terse inline concern is attached to a broad symbol hunk; its exact intended target is unspecified. It cannot be reported as a corrected duplicate-address issue. The final hunk does correct other entries, including an instance-method BlockTypeRegistry signature and Campfire address relative to the inline snapshot. FireBlock::checkBurn, Weather::isRainingAt and BeehiveBlockActor::evictAll implementations are commented out; their old implementations must not be presented as active support in this revision. New TypeWrapper(const T&) has an empty body and does not initialize its stored value from the argument. ClipParameters adds a bool without a default member initializer. New bitset helpers perform unchecked positions and default storage is not explicitly initialized; correct callers/initialization remain prerequisites.

Reusable lesson: a server-version port must trace each ABI change through callers, identity provenance and serializer choice, and retain explicit gaps even when smoke testing is reported. No test changes are supplied here; the author's two-platform testing statement is evidence of reported testing, not an independently reproduced compatibility result.

Exact inspected base/head: b33dde81adcdc684744cc057a8f519f788c9ff7a…8e0de84fe0283f3489d55691a423ccaf2c64c842. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/224
- https://github.com/EndstoneMC/endstone/pull/224#discussion_r2252635031
- https://github.com/EndstoneMC/endstone/pull/224#pullrequestreview-3085839011
