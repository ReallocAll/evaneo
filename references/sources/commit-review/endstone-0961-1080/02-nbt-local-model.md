<!-- retrieval: {"source_ids":["public:commit:058be41be6bd56c626659f592f1ddb59b31af43f","public:commit:093895a7d5aa491e1d233fd29cd6e79ee1faeed5","public:commit:1f45ab8475f0e99e2863835d0abcb81c78eb9508","public:commit:2f0e906337af2d3ba8efd0efe80ae80811f56721","public:commit:346176cea5e6ce63d4d1b76878f48064890403ca","public:commit:41267c0edefd82bb0b0b776b9b50d08d9b82cffb","public:commit:4b83c64de29cf6f944eda6aab602790a60084766","public:commit:51a109fa88ba7c56ec7c4fcf2c6ba995fc1a9085","public:commit:58f60826574a4d6d51dba134466cade750712b2c","public:commit:71be5a39c8acc37a4ec3436f03031c3cd2214a1b","public:commit:7b65a2d2a87718de73b58ecdf5dbcd8c1f3710bf","public:commit:86b8aa80e8bbb5dbe588f740ddca1efffb35b4d7","public:commit:8c2e71991ea6fbea4ee049b91ec9bacb8ed21ea7","public:commit:9f2c54d141d9cbfa7b052f46c1574359aaf99312","public:commit:bb6a26eb084a933e63b7beff6bb0f630ecacc63d","public:commit:f267c5d6c6cc52fdd9473712f1ce0d0e4674b8be"],"source_type":"public","date":"2024-05-20..2024-06-03","topics":["lifetime","ffi","testing","recovery","api","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# NBT returns from host-only declarations to local values, with deliberately incomplete serialization {#nbt-returns-from-host-only-declarations-to-local-values-with-deliberately-incomplete-serialization}

## A reversal with a concrete consumer {#a-reversal-with-a-concrete-consumer}

The earlier history first experimented with local NBT methods and then moved toward host-only/nonconstructible representations at928. [980](#commit-980)–[992](#commit-992) reverse that direction: locally constructible scalar, string, array, list and compound values return. The immediate consumer is command-origin construction, not a public general-purpose storage API. Local CompoundTag put methods create the tree that CommandOriginLoader consumes. That dependency explains why usable insertion can precede a complete serializer without proving that every TODO was accidental or acceptable for all use cases.

The staging is important.982 reads a ByteTag successfully without storing its value and writes nothing.983 fixes byte output and adds Short,984 adds Int/Int64, and985 assigns read results across the earlier scalar types while adding Float/Double. Treating each intermediate commit as 'NBT implemented' would erase the corrective history. EndTag copy also changes from the earlier null result to a real owned value in981. Unknown Tag factory input first returns success-with-null in990;995 changes it to an unexpected bad_message. A caller's Result check and a pointer's non-null invariant are separate contracts.

## Ownership and error propagation differ by container {#ownership-and-error-propagation-differ-by-container}

Scalar copies return unique-owned values and equality compares payloads after type checks. String uses its content. ByteArray checks its declared size against remaining bytes before allocating and propagates the byte-read result. The interface's remaining-byte count is unsigned; the signed negative length converts to a large unsigned value and is rejected by that comparison. IntArray instead reserves the declared count and propagates each integer-read failure, with no equivalent explicit remaining-byte precheck. These are observed implementation differences, not evidence of a consistent validated hostile-input policy.

Final ListTag context retains several counterexamples: child load results are ignored, equality compares vectors of unique_ptr values rather than recursively comparing Tag payloads, hashing follows those elements, and copy populates children without copying type_. The default type is not explicitly initialized.991's recursive child cleanup addresses ownership but does not repair these semantic issues. They matter to anyone reusing the model as a general serializer. They do not establish that the actual command-origin path exercises list parsing or that an exploit occurred. This review stops at explaining the bounded mechanism rather than conducting an unrequested exhaustive parser audit.

## Compound is a population bridge, not a finished round-trip type {#compound-is-a-population-bridge-not-a-finished-round-trip-type}

989 explicitly leaves write/load/equals/copy/hash throwing Not implemented.992 provides map/variant-based putByte, Boolean, Float, Int, Int64 and Compound.995 adds missing Byte friend access;997 makes header definitions inline;1072 adds String and friendship for the console-origin fields. The variant's temporary duplicate Compound entry is corrected to Byte. These revisions make C++ construction and cross-translation-unit inclusion usable for the intended bridge. They do not silently implement the throwing virtual operations.

A useful distinction is operational completeness for a narrow construction path versus completeness of a type's advertised virtual interface. Both are visible in the same file. The new values must match the native representation because the loader consumes them directly, so size assertions and variant ordering are ABI assumptions, not merely an application serialization choice. No native layout probe or NBT round-trip/error-input test was run or added in this assigned sequence.

## How to use this evidence {#how-to-use-this-evidence}

Retrieve this family when diagnosing half-complete native value mirrors, Result-versus-null factory contracts, copy semantics for owned polymorphic children, header-inline integration or a targeted serialization bridge. The justified lesson is to trace the actual consumer and remaining operations, not to infer a lasting preference for hand-writing NBT or to declare the implementation production-complete. All authorship in this family is Vincent; library hash/expected/container implementations were not independently audited. Detailed source dispositions below preserve the intervening corrections rather than collapsing the series into its final file.


## Individual commit dispositions {#individual-commit-dispositions}


<a id="commit-979"></a>
### 979: refactor: move CompoundTagVariant into compound_tag.h {#commit-979}

Source: [346176cea5e6ce63d4d1b76878f48064890403ca](https://github.com/EndstoneMC/endstone/commit/346176cea5e6ce63d4d1b76878f48064890403ca). Authored 2024-05-20T14:27:04Z; Git author Vincent. Disposition: structural.

Moves CompoundTagVariant into compound_tag.h and removes the separate header. The variant model is retained; the structural consolidation prepares inline local compound insertion. No persistence format change is visible here.


<a id="commit-980"></a>
### 980: feat: implement Tag base class {#commit-980}

Source: [058be41be6bd56c626659f592f1ddb59b31af43f](https://github.com/EndstoneMC/endstone/commit/058be41be6bd56c626659f592f1ddb59b31af43f). Authored 2024-05-20T14:40:53Z; Git author Vincent. Disposition: ownership_reversal.

Reinstates a locally implementable Tag interface after928’s host-only deleted/default-stub direction: read/write/name/id/copy/hash become virtual requirements, type-based equals and print return, and deleteChildren is locally no-op by default. Construction remains constrained until981. This is a dated reversal, not evidence for a timeless preference for either host delegation or local reimplementation.


<a id="commit-981"></a>
### 981: feat(nbt): implement EndTag {#commit-981}

Source: [1f45ab8475f0e99e2863835d0abcb81c78eb9508](https://github.com/EndstoneMC/endstone/commit/1f45ab8475f0e99e2863835d0abcb81c78eb9508). Authored 2024-05-20T14:44:29Z; Git author Vincent. Disposition: implementation.

Enables local Tag construction and fully implements EndTag. Copy now allocates an EndTag instead of returning an empty unique_ptr as in the earlier920 implementation. End is a real zero-payload value, not a null sentinel for all failed factories.


<a id="commit-982"></a>
### 982: feat(nbt): implement ByteTag {#commit-982}

Source: [f267c5d6c6cc52fdd9473712f1ce0d0e4674b8be](https://github.com/EndstoneMC/endstone/commit/f267c5d6c6cc52fdd9473712f1ce0d0e4674b8be). Authored 2024-05-20T15:06:30Z; Git author Vincent. Disposition: incremental_implementation.

Implements ByteTag constructor/id/equality/copy/hash, but its write is empty and successful load does not store the read value. These are intermediate omissions, repaired by983 and985 respectively. The source supports staged implementation, not a complete round-trip claim at982.


<a id="commit-983"></a>
### 983: feat(nbt): implement ShortTag {#commit-983}

Source: [7b65a2d2a87718de73b58ecdf5dbcd8c1f3710bf](https://github.com/EndstoneMC/endstone/commit/7b65a2d2a87718de73b58ecdf5dbcd8c1f3710bf). Authored 2024-05-20T15:09:51Z; Git author Vincent. Disposition: incremental_implementation.

Implements ByteTag output and adds ShortTag read/write/copy/equality/hash; converts Tag::Type to scoped char enum and qualifies standard names. Successful scalar reads still omit storing values until985. The enum change is a type/API change amid formatting.


<a id="commit-984"></a>
### 984: feat(nbt): implement IntTag and Int64Tag {#commit-984}

Source: [8c2e71991ea6fbea4ee049b91ec9bacb8ed21ea7](https://github.com/EndstoneMC/endstone/commit/8c2e71991ea6fbea4ee049b91ec9bacb8ed21ea7). Authored 2024-05-20T15:16:51Z; Git author Vincent. Disposition: incremental_implementation.

Adds local IntTag/Int64Tag implementations following the scalar pattern, including output and copy/hash. Like the earlier scalar forms, successful load still fails to assign the value;985 supplies the missing assignment. No tests accompany the staging.


<a id="commit-985"></a>
### 985: feat(nbt): implement FloatTag and DoubleTag {#commit-985}

Source: [58f60826574a4d6d51dba134466cade750712b2c](https://github.com/EndstoneMC/endstone/commit/58f60826574a4d6d51dba134466cade750712b2c). Authored 2024-05-20T15:22:53Z; Git author Vincent. Disposition: corrective_completion.

Adds FloatTag/DoubleTag implementations and assigns successful read results for Byte, Short, Int and Int64. Floating comparison is exact and hashing uses std::hash. This is a concrete correction to actual persistence behavior, not just filling declarations; no tolerance policy or round-trip test is shown.


<a id="commit-986"></a>
### 986: feat(nbt): implement ByteArrayTag and StringTag {#commit-986}

Source: [71be5a39c8acc37a4ec3436f03031c3cd2214a1b](https://github.com/EndstoneMC/endstone/commit/71be5a39c8acc37a4ec3436f03031c3cd2214a1b). Authored 2024-05-20T15:52:13Z; Git author Vincent. Disposition: implementation.

Implements ByteArrayTag and StringTag. Byte arrays read a signed length, compare against unsigned remaining-byte count, resize and propagate readBytes errors; strings retain the read value and use content equality/hash. Negative byte-array lengths are rejected by the signed/unsigned comparison against available bytes in the inspected interface. This does not establish equivalent length/error handling for List or IntArray.


<a id="commit-987"></a>
### 987: feat(nbt): implement ListTag {#commit-987}

Source: [51a109fa88ba7c56ec7c4fcf2c6ba995fc1a9085](https://github.com/EndstoneMC/endstone/commit/51a109fa88ba7c56ec7c4fcf2c6ba995fc1a9085). Authored 2024-05-20T16:35:42Z; Git author Vincent. Disposition: implementation_with_limits.

Implements ListTag type/count parsing, element factory, output, copy/equality/hash/print, while the initial factory is still a throwing placeholder. The final unit retains ignored child-load errors, pointer-based vector equality/hash, and copy without copying type_. These bounded counterexamples prevent a claim of finished semantic NBT round-tripping. They do not show that the command-origin use exercises list parsing.


<a id="commit-988"></a>
### 988: feat(nbt): implement IntArrayTag {#commit-988}

Source: [9f2c54d141d9cbfa7b052f46c1574359aaf99312](https://github.com/EndstoneMC/endstone/commit/9f2c54d141d9cbfa7b052f46c1574359aaf99312). Authored 2024-05-20T16:39:32Z; Git author Vincent. Disposition: implementation.

Implements IntArrayTag serialization and content copy/equality/hash. It propagates individual integer-read failures, clears/reserves the declared count and appends values. Unlike ByteArray there is no explicit remaining-byte bound before reserve; no adversarial input test or allocation limit is established.


<a id="commit-989"></a>
### 989: feat(nbt): add CompoundTag (not implemented) {#commit-989}

Source: [41267c0edefd82bb0b0b776b9b50d08d9b82cffb](https://github.com/EndstoneMC/endstone/commit/41267c0edefd82bb0b0b776b9b50d08d9b82cffb). Authored 2024-05-20T16:46:21Z; Git author Vincent. Disposition: incremental_implementation.

Creates local CompoundTag construction/string/id/map storage but intentionally leaves write/load/equality/copy/hash throwing Not implemented. Removes host put hooks in preparation for local insertion. The variant temporarily contains CompoundTag twice instead of ByteTag;992 repairs that model. This is not a completed general NBT serializer.


<a id="commit-990"></a>
### 990: feat(nbt): implement Tag::newTag {#commit-990}

Source: [4b83c64de29cf6f944eda6aab602790a60084766](https://github.com/EndstoneMC/endstone/commit/4b83c64de29cf6f944eda6aab602790a60084766). Authored 2024-05-21T00:58:46Z; Git author Vincent. Disposition: factory_implementation.

Implements Tag::newTag for all twelve concrete NBT types and moves type-name mapping into a source file; adjusts list printing. Unknown types initially return a successful null pointer, not an expected error.995 corrects that distinction, which matters to callers that check only Result success.


<a id="commit-991"></a>
### 991: feat(nbt): implement ListTag::deleteChildren {#commit-991}

Source: [093895a7d5aa491e1d233fd29cd6e79ee1faeed5](https://github.com/EndstoneMC/endstone/commit/093895a7d5aa491e1d233fd29cd6e79ee1faeed5). Authored 2024-05-21T01:59:26Z; Git author Vincent. Disposition: ownership_cleanup.

ListTag::deleteChildren now recursively invokes child cleanup before popping each unique_ptr. It frees owned child objects through ordinary unique ownership; this change does not repair the separate list equality/copy/load concerns.


<a id="commit-992"></a>
### 992: feat(nbt): implement put functions in CompoundTag {#commit-992}

Source: [bb6a26eb084a933e63b7beff6bb0f630ecacc63d](https://github.com/EndstoneMC/endstone/commit/bb6a26eb084a933e63b7beff6bb0f630ecacc63d). Authored 2024-05-21T01:59:43Z; Git author Vincent. Disposition: local_population.

Adds local CompoundTag putByte/Boolean/Float/Int/Int64/Compound methods using variant values in the map, corrects ByteTag in the variant, inherits variant constructors and adds friend access. Definitions in the header initially lack inline and ByteTag friendship remains missing until995. The local population operations are the immediate command-origin enabler, while general compound serialization remains intentionally unsupported.


<a id="commit-995"></a>
### 995: refactor(nbt): improve unexpected result from Tag::newTag {#commit-995}

Source: [86b8aa80e8bbb5dbe588f740ddca1efffb35b4d7](https://github.com/EndstoneMC/endstone/commit/86b8aa80e8bbb5dbe588f740ddca1efffb35b4d7). Authored 2024-05-21T02:00:56Z; Git author Vincent. Disposition: corrective_revision.

Changes unknown NBT types from success-with-null to an unexpected bad_message error and grants CompoundTag access to ByteTag storage. This repairs two concrete integration problems from990/992. It still does not propagate each ListTag child’s load error or complete CompoundTag serialization.


<a id="commit-1072"></a>
### 1072: feat(nbt): add CompoundTag::putString {#commit-1072}

Source: [2f0e906337af2d3ba8efd0efe80ae80811f56721](https://github.com/EndstoneMC/endstone/commit/2f0e906337af2d3ba8efd0efe80ae80811f56721). Authored 2024-06-03T16:22:01Z; Git author Vincent. Disposition: local_population.

Adds local CompoundTag::putString and friend access in StringTag, enabling console origin request/dimension strings in1075. This is a targeted bridge operation; other compound serialization methods remain explicit throwing stubs.
