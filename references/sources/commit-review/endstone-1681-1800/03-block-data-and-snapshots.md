<!-- retrieval: {"source_ids":["public:commit:0251488008ce909837de1dd902a9edf5bb556438","public:commit:1003a73c5e3beaf05b94bd674f7530ce7e5dde7d","public:commit:15b315bf0938a424175677c369c364c92ecaa7fb","public:commit:200f7bcba1fac108617728fc7da8cb59b37a7594","public:commit:3930176fffc3482a501d5dbf6cb5ac379a9cab92","public:commit:4198c783e0323bb574eedf1d999e287f21b0aa30","public:commit:5db94cbc29c6eb3e1952bf1ac93f139c58cfcc9b","public:commit:62ffad29ad04f154bf6f486ba7321ab7bf1b94a0","public:commit:6864ca9faadcb56148bfc18eda92d921769d70d0","public:commit:89e5d3689eee83d9c030aed45b22a2ad56398aba","public:commit:a125d74fc167fbff7a9367a8d27f47ce305ece55","public:commit:a80b6b3df90e7a8179778f62b4870a689e730622","public:commit:aac41a6098f1e825576a23907b86f96888a50678","public:commit:ae215557b970812a4ef949eeb39e9fdc0f2f7b0f","public:commit:b16893dc8789e3ba187f9c72c0c43f5ff8f1e972","public:commit:bf0d0440aac347fd9cce20fb644a2420e6446143","public:commit:d66a66e5c70a4b13494a95f5b46b8d2dbd881d0a","public:commit:e5c631ce99f147f7ff3b2c853ae911e6ee0c0bfb","public:commit:ede16744ed9cdd50bc4b7b7aa8b9507e6f176803","public:commit:efb1fcb23916cb5856695c68afcc9c8d593b9b8f","public:commit:f0de75ac84c018ab165fd936d6eb2ca6f9154eda","public:commit:fc432355a57d687547a7e416f9546e3681da5968"],"source_type":"public","date":"2024-09-01..2024-09-11","topics":["lifetime","ffi","testing","api","documentation","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Block data, typed state boundaries and snapshots {#block-data-typed-state-boundaries-and-snapshots}


Endstone commits 1681–1800, dated August 29–September 14, 2024.

## From a placeholder to a typed native adapter {#from-a-placeholder-to-a-typed-native-adapter}

BlockData returns after its earlier removal, first as a placeholder, then as JSON/command-like state text, then as a typed map. This is a dated evolution rather than a stable initial design. The Python string-rewrite parser exists only briefly; the final typed bool/string/int public map is converted into the native int/string/bool variant order before reusing ScriptBlockUtils. That conversion is significant even though the alternative types look identical. Native validation is delegated rather than reimplemented, and the source's null/exception behavior remains part of the boundary contract.

Shared ownership applies to Endstone wrapper objects, not automatically to native engine objects. BlockData holds a borrowed native permutation reference. BlockState similarly holds native source/dimension references and a permutation pointer. Its snapshot is not a copy of a block entity's complete persistent state. Retaining those distinctions prevents the misleading conclusion that shared_ptr alone solved chunk, level or engine-object lifetime.

Moving validity checks into Block changes lookup semantics: a wrapper can exist for an invalid location, and later operations recheck world height and chunk activity. This is better suited to wrappers that outlive a lookup, but it is not a lock or lifetime pin. Some consumers, including formatting and capture, still bypass the null/validity behavior implied by guarded getData. The checks and their callers were read together.

## Snapshot contract and counterexamples {#snapshot-contract-and-counterexamples}

The snapshot API separates editing an object from applying it to the world. However, update's actual comparison is against the snapshot's currently edited type, not a separately remembered original type, and it returns true after a void setter even if the native operation did not happen. This bounds the documented success semantics. Placement events own a proposed BlockState, but the hook forwards the original placement permutation and only consumes cancellation. Editing that object is therefore not an implemented transactional replacement of the native placement.

These cases are useful when designing APIs that distinguish live handles, immutable palette values, snapshots and world mutations. Test implications follow directly: empty-container round trips, typed variant conversion, invalid locations, snapshot type edits, failed native writes and Python overload dispatch all deserve explicit behavior checks. The observed test changes in this chain only keep mocks compiling; none adds those assertions, and none was executed. The complete endpoint block, BlockData, BlockState, server factory and placement hook contexts anchor these limits locally.

## Individual commit dispositions {#individual-commit-dispositions}

<a id="commit-1706"></a>
### Commit 1706 {#commit-1706}

2024-09-01T14:53:19Z · `ae215557b970812a4ef949eeb39e9fdc0f2f7b0f` · feat: add BlockData

Reintroduces BlockData after its removal in ordinal 1594. The initial class and server factory are placeholders, with a throwing factory and mock interface updates. This demonstrates a temporary removal followed by renewed implementation, not a permanent rejection of the abstraction. Later commits supply representation, bindings and native lookup.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/ae215557b970812a4ef949eeb39e9fdc0f2f7b0f). Classification: api_reintroduction.

<a id="commit-1707"></a>
### Commit 1707 {#commit-1707}

2024-09-01T14:55:16Z · `aac41a6098f1e825576a23907b86f96888a50678` · feat(block): add Block::setType and Block::setData

Moves block-coordinate, loaded-chunk and ticking-chunk checks from dimension lookup into the Block wrapper constructor and individual operations. Dimension lookup can now return a wrapper for an invalid location; isValid reports its state, while guarded reads return air/null and writes do nothing. Rechecking improves stale-wrapper handling but does not pin chunk lifetime or provide synchronization. Constructor logging is not rejection.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/aac41a6098f1e825576a23907b86f96888a50678). Classification: validation_boundary_change.

<a id="commit-1708"></a>
### Commit 1708 {#commit-1708}

2024-09-01T16:01:29Z · `6864ca9faadcb56148bfc18eda92d921769d70d0` · feat(block): implement Block::setData and Block::getData

Implements getData as an owning C++ wrapper around a borrowed native Block and setData through BlockSource::setBlock. It rejects null input, assumes the concrete EndstoneBlockData subtype and ignores the native setter's boolean result. Physics flags are 3 versus 2|16|1024; the latter carries an explicit uncertainty comment. The concrete header arrives in 1709, so intermediate buildability is not assumed.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/6864ca9faadcb56148bfc18eda92d921769d70d0). Classification: block_data_implementation.

<a id="commit-1709"></a>
### Commit 1709 {#commit-1709}

2024-09-01T16:01:59Z · `1003a73c5e3beaf05b94bd674f7530ce7e5dde7d` · feat(block): add EndstoneBlockData

Adds EndstoneBlockData's concrete definition, holding a native Block reference rather than owning or copying an engine block. Interface versus implementation includes are adjusted accordingly. Owning the wrapper does not establish the native palette object's lifetime; later shared_ptr conversion retains that distinction.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/1003a73c5e3beaf05b94bd674f7530ce7e5dde7d). Classification: ownership_model.

<a id="commit-1710"></a>
### Commit 1710 {#commit-1710}

2024-09-01T16:02:22Z · `62ffad29ad04f154bf6f486ba7321ab7bf1b94a0` · feat(block): implement Server::createBlockData

Adds native block-name lookup and uses the default render block for the server factory. Unknown names log and return null. A states string is accepted but deliberately ignored as TODO, so the signature is ahead of its behavior. The required native lookup declaration and symbol entries follow at 1711.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/62ffad29ad04f154bf6f486ba7321ab7bf1b94a0). Classification: partial_factory.

<a id="commit-1711"></a>
### Commit 1711 {#commit-1711}

2024-09-01T16:15:42Z · `0251488008ce909837de1dd902a9edf5bb556438` · feat(block): add BlockTypeRegistry::lookupByName

Defines the BlockTypeRegistry lookup wrapper and adds Windows/Linux symbol entries. The call suppresses native not-found logging so the Endstone factory can issue its own message. This bridge is short-lived: 1720 replaces it with the engine's block-descriptor path to support typed states.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/0251488008ce909837de1dd902a9edf5bb556438). Classification: native_lookup_bridge.

<a id="commit-1712"></a>
### Commit 1712 {#commit-1712}

2024-09-01T16:48:37Z · `a125d74fc167fbff7a9367a8d27f47ce305ece55` · feat: show Block Palette in DevTools

Moves the NBT-to-JSON conversion from devtools into NbtIo and uses it for block-palette inspection as well as creative-item data. The complete function body is verified identical after whitespace/comment normalization. The new availability is meaningful, but the serializer algorithm is reused rather than invented here. Empty-container shape is corrected separately at 1715.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/a125d74fc167fbff7a9367a8d27f47ce305ece55). Classification: verified_move_with_reuse.

<a id="commit-1713"></a>
### Commit 1713 {#commit-1713}

2024-09-01T18:05:56Z · `f0de75ac84c018ab165fd936d6eb2ca6f9154eda` · feat(block): add BlockData::getType and BlockData::getBlockStates

Adds BlockData's virtual destructor, type and string-valued states accessors, initially serializing NBT states as JSON. The API documentation promises reconstruction, but the receiving factory still has its states TODO. Preserve the distinction between interface intent and implemented round-trip behavior.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/f0de75ac84c018ab165fd936d6eb2ca6f9154eda). Classification: api_representation_iteration.

<a id="commit-1714"></a>
### Commit 1714 {#commit-1714}

2024-09-01T22:17:00Z · `fc432355a57d687547a7e416f9546e3681da5968` · refactor(block): use shared_ptr for BlockData

Changes BlockData return and parameter ownership from unique_ptr to shared_ptr, adds enable_shared_from_this and makes getData const. This supports reusable API/Python handles, an inferred benefit, while the underlying native Block remains borrowed. Several make_unique expressions rely on conversion to shared_ptr; they are not proof of exclusive native ownership.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/fc432355a57d687547a7e416f9546e3681da5968). Classification: ownership_api_revision.

<a id="commit-1715"></a>
### Commit 1715 {#commit-1715}

2024-09-01T22:18:18Z · `a80b6b3df90e7a8179778f62b4870a689e730622` · refactor(nbt): use default values for json arrays and objects

Initializes JSON arrays and objects explicitly for NBT lists, compounds and numeric arrays. Empty containers now retain their container shape rather than becoming null. A clipped initial display was repeated in full. This is a semantic serializer correction despite its small size; no new round-trip assertion is added.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/a80b6b3df90e7a8179778f62b4870a689e730622). Classification: serialization_fix.

<a id="commit-1716"></a>
### Commit 1716 {#commit-1716}

2024-09-01T22:18:37Z · `200f7bcba1fac108617728fc7da8cb59b37a7594` · feat(nbt): add CompoundTag::size() and CompoundTag::empty()

Adds CompoundTag size and empty accessors that delegate directly to its map. The implementation is fully read and straightforward. It is supporting API work, with no separate architectural preference inferred.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/200f7bcba1fac108617728fc7da8cb59b37a7594). Classification: small_helper.

<a id="commit-1717"></a>
### Commit 1717 {#commit-1717}

2024-09-01T22:20:26Z · `3930176fffc3482a501d5dbf6cb5ac379a9cab92` · feat(block): add python bindings for Block and BlockData

Introduces BlockData Python bindings and initially converts formatted states to dict via string replacement plus json.loads. C++ formatting simultaneously switches to command-like key=value syntax, with byte/int/string handling. This creates a fragile conversion boundary, soon removed by 1718 and replaced by typed maps at 1719. Block formatting dereferences getData without handling an invalid block's null result.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/3930176fffc3482a501d5dbf6cb5ac379a9cab92). Classification: python_representation_experiment.

<a id="commit-1718"></a>
### Commit 1718 {#commit-1718}

2024-09-01T22:55:09Z · `d66a66e5c70a4b13494a95f5b46b8d2dbd881d0a` · feat(command): support block type and block states in command usages

Registers native block-type and block-state grammar for command arguments and updates the command tutorial. Python states become a string, removing the preceding parsing rewrite but only briefly. These changes reuse the engine's command grammar; they do not implement an independent block-state parser. The next commit chooses a typed public mapping instead.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/d66a66e5c70a4b13494a95f5b46b8d2dbd881d0a). Classification: command_and_binding_change.

<a id="commit-1719"></a>
### Commit 1719 {#commit-1719}

2024-09-02T11:25:02Z · `89e5d3689eee83d9c030aed45b22a2ad56398aba` · refactor(block): change type of `block_states` from string to map

Replaces string states with an unordered map whose values are bool, string or int. Native NBT conversion and Python STL casting become explicit typed boundaries, while fmt handles quoted string escaping. This removes the ad hoc Python text parser. The factory remains incomplete until 1720, and an unconditional static_assert in a generic visitor needs 1722's compatibility repair. Map iteration order is not promised stable.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/89e5d3689eee83d9c030aed45b22a2ad56398aba). Classification: typed_state_redesign.

<a id="commit-1720"></a>
### Commit 1720 {#commit-1720}

2024-09-02T12:50:41Z · `5db94cbc29c6eb3e1952bf1ac93f139c58cfcc9b` · feat(block): implement Server::createBlockData with block states

Routes creation through ScriptBlockUtils::createBlockDescriptor and tryGetBlockNoLogging, replacing the temporary registry lookup. The public variant order bool/string/int is converted by visiting into the native int/string/bool representation; this avoids treating equal alternatives as equal ABI indices. Unknown blocks return null after logging. The returned wrapper borrows the descriptor's block pointer, relying on engine palette lifetime, and native state-validation exceptions are not translated locally.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/5db94cbc29c6eb3e1952bf1ac93f139c58cfcc9b). Classification: engine_factory_reuse.

<a id="commit-1721"></a>
### Commit 1721 {#commit-1721}

2024-09-02T17:55:42Z · `15b315bf0938a424175677c369c364c92ecaa7fb` · feat: add endstone::overloaded

Adds the overloaded-lambda helper to the public Endstone header. It uses the usual variadic inheritance and deduction-guide pattern. This supports public formatters without exposing an EnTT helper dependency; no claim of a novel dispatch algorithm is warranted.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/15b315bf0938a424175677c369c364c92ecaa7fb). Classification: small_public_helper.

<a id="commit-1735"></a>
### Commit 1735 {#commit-1735}

2024-09-05T16:29:51Z · `4198c783e0323bb574eedf1d999e287f21b0aa30` · feat(block): add BlockState

Introduces the BlockState interface with captured type/data/location and update(force,apply_physics). It promises a non-live snapshot; the first concrete class is still empty. Some documentation describes Java-style exceptions or unique Block instances not implemented by the C++ wrappers. Treat those as contract text needing implementation scrutiny, not established runtime behavior.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/4198c783e0323bb574eedf1d999e287f21b0aa30). Classification: snapshot_interface.

<a id="commit-1736"></a>
### Commit 1736 {#commit-1736}

2024-09-05T17:04:08Z · `efb1fcb23916cb5856695c68afcc9c8d593b9b8f` · feat(block): implement BlockState

Stores borrowed dimension/source references and a native permutation pointer. Editing type/data changes the snapshot; update compares the live type to the currently stored snapshot type and delegates to a void block setter. It has no separately retained original type or propagated native success flag, so a true return does not prove a world write occurred. Foreign BlockData subclasses also are not safely handled after a failed dynamic cast. No tile-entity payload snapshot is implemented.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/efb1fcb23916cb5856695c68afcc9c8d593b9b8f). Classification: snapshot_implementation.

<a id="commit-1742"></a>
### Commit 1742 {#commit-1742}

2024-09-06T16:18:31Z · `e5c631ce99f147f7ff3b2c853ae911e6ee0c0bfb` · feat(block): add python bindings for BlockState

Exposes BlockState with a shared_ptr holder, readonly location/dimension coordinates, editable type/data and update defaults; adds formatting and API comments. Dimension remains a borrowed reference. The generic captureState factory is still absent until 1778, although placement events will expose snapshots at 1743. The binding does not add a lifetime pin for the native block/source.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/e5c631ce99f147f7ff3b2c853ae911e6ee0c0bfb). Classification: binding_completion.

<a id="commit-1743"></a>
### Commit 1743 {#commit-1743}

2024-09-06T16:53:36Z · `bf0d0440aac347fd9cce20fb644a2420e6446143` · feat(block): add block placed to BlockPlaceEvent

Adds an event-owned proposed BlockState to BlockPlaceEvent, constructed from the native placement permutation before the engine places the block. Python receives a borrowed reference to that event-owned snapshot. The hook still only consumes cancellation and forwards the original placement_block; changing the snapshot alone is not implemented as replacement of the placement operation. This distinguishes an inspection object from an automatic transactional edit.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/bf0d0440aac347fd9cce20fb644a2420e6446143). Classification: placement_snapshot.

<a id="commit-1764"></a>
### Commit 1764 {#commit-1764}

2024-09-09T19:45:43Z · `ede16744ed9cdd50bc4b7b7aa8b9507e6f176803` · fix(python): correct binding for overloaded `Dimension::getBlockAt` function

Registers the Location overload first and disallows implicit conversion for that argument, correcting ambiguous/undesired Python overload routing. Also exposes floored block_x/y/z properties from Position. The implementation and stub changes were read; no Python invocation or assertion verifies edge cases in this unit.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/ede16744ed9cdd50bc4b7b7aa8b9507e6f176803). Classification: python_overload_repair.

<a id="commit-1778"></a>
### Commit 1778 {#commit-1778}

2024-09-11T23:23:40Z · `b16893dc8789e3ba187f9c72c0c43f5ff8f1e972` · feat(block): introduce Block::captureState method for capturing the current block state

Adds shared Block::captureState and the Python capture_state method, completing a public way to obtain the snapshot independently of placement events. It creates EndstoneBlockState directly; it does not add a fresh validity check or copy tile-entity data. The documented never-updated object describes snapshot behavior, not ownership of the native dimension or block source.

Source: [individual commit](https://github.com/EndstoneMC/endstone/commit/b16893dc8789e3ba187f9c72c0c43f5ff8f1e972). Classification: snapshot_acquisition_completion.

## Coverage boundary {#coverage-boundary}

Findings rely on the linked public sources; external PR/issue discussions, dependencies, and native engine internals are outside the cited evidence. Runtime and current-release behavior were not tested.
