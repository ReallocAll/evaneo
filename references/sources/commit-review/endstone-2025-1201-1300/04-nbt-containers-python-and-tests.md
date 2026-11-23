<!-- retrieval: {"source_ids":["public:commit:0cb247e1baf8276a7023a8a919f7ea1c9744b23f","public:commit:0d7c5c6f255ecff9d4c2a768281b3e591f58d009","public:commit:2302b470479b3e604238f3e1193af2885e7e5977","public:commit:2a406208eaeccc99526d690ea67b1cf860f64ad5","public:commit:2cc889fbf5ebbd3f67699c5ce013eabe72c585e4","public:commit:39a03c89017a6c848af5c5ca2d7aa851110cbfe0","public:commit:539f8ffdfbd6ae254aebddb9f51d54bd2867a394","public:commit:53b062473dd6c9328a8c4d373df89c712662a7ed","public:commit:7884921fd904c85b6a040bde9fc34e4f25f490f2","public:commit:893c752b624d6338bd7b80d3a2ba94b3315b73cb","public:commit:91a888c4f558c060147f74a7ebeccca29c839fd2","public:commit:95e44f7e17a073872144e4a33aaef9fea458ddf5","public:commit:aeca73f5450556a46df433c0fd8cb085cc0f305b","public:commit:b2b64a1a2e90719fe70791898475c4389cf5a638","public:commit:bc30ae0d047d61ac7b9eee1a54928e4f47e0371b","public:commit:cf4234a9fe6608f5635e210480c8f3b3221c09dd","public:commit:d9559c2f5c5e428dd2a6748bdb2472a60614a57a","public:commit:dea3eee91dd8340af35bd7e93bdad3954afc8796","public:commit:ebbcbca329a8e5fde66b77b11fad7e0f3cbd3a2d","public:commit:fbb83d7d1a9ea7e65489dae35975d620524299eb"],"source_type":"public","date":"2025-11-11..2025-11-14","topics":["ffi","testing","build","api","documentation","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# NBT containers, Python bindings and tests {#nbt-containers-python-bindings-and-tests}

## Implementation and revisions {#implementation-and-revisions}

1264–1268 begin with type IDs, scalar/string and array wrappers, then an owning recursive variant with ListTag and CompoundTag. Primitive values must be explicitly wrapped rather than guessed from C++ arithmetic types. Lists enforce homogeneous non-End elements on constructors/emplace; compounds use an ordered map, giving deterministic formatting. Common TagBase becomes the Python inheritance base while the variant remains the C++ transport type. This avoids exposing the variant as the bound object itself.

1270–1272 complete access, self-shaping insertion, iteration, equality and merging. The first C++ tests reveal staged API differences: implicit wrapper conversion and emplace helpers arrive next, and expectations distinguish the root compound from its list child. Python bindings add normal negative indices, list/compound pop and dict-like operations, with1281 correcting negative-pop indexing and returning the removed compound payload instead of erase count.

1276 initially copies an outbound Tag and discards return policy/parent.1283 takes const Tag& and forwards both to py::cast, so nested reference_internal results can retain their parent relationship rather than silently becoming detached copies. Incoming conversion accepts exact bound wrapper types and copies values. This is a concrete evolution in cross-language ownership, not a blanket claim that every container reference survives subsequent mutation.

1281–1282 add SNBT-style str and Python-oriented repr, numeric suffixes and float .0 handling. String quoting chooses a quote style and escapes slashes/quotes. The full authored293-line C++ test addition and529-line Python test addition were read, including defaults, equality, array mutation/bytes, homogeneous lists, bounds/negative indices, compounds, nested values and exact str/repr expectations. Later correction hunks were read too. No test was run, and generator output is not treated as an executed build result.

## Boundary counterexamples {#boundary-counterexamples}

At1300, numeric arrays expose numeric value_type, so Tag::size takes the scalar branch and returns1 even for empty/multi-element arrays. ByteArray str dereferences begin before checking emptiness. The escape formatter doubles braces before passing its string as data to fmt, altering brace-containing data. The Python byte-buffer constructor memcpy ignores strides after checking only dimension and item size; vector-mutating methods coexist with exported buffers and have no local lease/resize guard. C++ list element references can replace a value with a different tag kind after insertion checks, and ListTag::push_back declarations have no found definitions in this slice. These are bounded static observations, not measured failures or proof that all APIs are broken.

The added tests do not cover empty ByteArray string conversion, strided byte buffers or resize during an exported buffer. Additional testing would target these contracts rather than merely expanding ordinary examples. Changes to the stub generator handle empty classes, module aliases, qualified NBT names and generic variable placement; source was read without importing the package or running stub generation.

## Per-commit decisions and revisions {#per-commit-decisions-and-revisions}

<a id="commit-1264"></a>
### Commit 1264 {#commit-1264}

[2cc889fbf5eb](https://github.com/EndstoneMC/endstone/commit/2cc889fbf5ebbd3f67699c5ce013eabe72c585e4) · 2025-11-11T21:48:28Z · feat(nbt): add Tag types

Introduces NBTType values 0–11, initial Tag binding/stub and build registration. This is type scaffolding, not yet payload conversion.

<a id="commit-1265"></a>
### Commit 1265 {#commit-1265}

[539f8ffdfbd6](https://github.com/EndstoneMC/endstone/commit/539f8ffdfbd6ae254aebddb9f51d54bd2867a394) · 2025-11-11T22:13:08Z · feat(nbt): add primitive tag types

ValueTag<T> supplies explicit scalar/string wrappers, payload comparisons and read-only value access. Python numeric protocols/repr/str and stubs are added. Default-construction semantics differ between default initialization and value initialization; no runtime result claimed.

<a id="commit-1266"></a>
### Commit 1266 {#commit-1266}

[dea3eee91dd8](https://github.com/EndstoneMC/endstone/commit/dea3eee91dd8340af35bd7e93bdad3954afc8796) · 2025-11-11T22:42:00Z · feat(nbt): add `ByteArrayTag` and `IntArrayTag` types

ArrayTag vector wrapper adds bounds-checked at, unchecked indexing, iteration and mutation. Python negative indexing and iterator keepalive are supplied. Byte buffer input checks one dimension/item size but memcpy ignores strides; exported buffer can be invalidated by vector mutation. These edge cases are outside added tests.

<a id="commit-1267"></a>
### Commit 1267 {#commit-1267}

[91a888c4f558](https://github.com/EndstoneMC/endstone/commit/91a888c4f558c060147f74a7ebeccca29c839fd2) · 2025-11-11T23:21:28Z · feat(nbt): add `ListTag` and `CompoundTag`

Recursive variant Tag, ListTag and CompoundTag scaffolds own values rather than borrowing native NBT. Separate type header; list initializer homogeneity still incomplete and repaired1270. Python Tag enum removed during transition.

<a id="commit-1268"></a>
### Commit 1268 {#commit-1268}

[7884921fd904](https://github.com/EndstoneMC/endstone/commit/7884921fd904c85b6a040bde9fc34e4f25f490f2) · 2025-11-11T23:25:29Z · docs: update documentation

Adds NBT documentation navigation and lazy exports for scalar/array wrappers; removes obsolete enum binding/stub. The docs-labelled commit changes runtime import surface too.

<a id="commit-1270"></a>
### Commit 1270 {#commit-1270}

[39a03c89017a](https://github.com/EndstoneMC/endstone/commit/39a03c89017a6c848af5c5ca2d7aa851110cbfe0) · 2025-11-12T14:55:20Z · feat(nbt): implement `ListTag` and `CompoundTag`

Implements variant type/size/empty/access/visit, homogeneous non-End lists and ordered compounds. Array value_type enters numeric branch before container size, so numeric-array Tag::size reports1. C++ mutable element references can bypass list homogeneity. Empty Tag[index] shapes an empty list then uses unchecked indexing without growth. Python negative list pop uses unnormalized index until1281; compound rvalue merge iterates const and copies.

<a id="commit-1271"></a>
### Commit 1271 {#commit-1271}

[95e44f7e17a0](https://github.com/EndstoneMC/endstone/commit/95e44f7e17a073872144e4a33aaef9fea458ddf5) · 2025-11-12T15:21:46Z · test(nbt): add unit tests for NBT tag types and operations

Adds full C++ NBT tests covering wrapper equality, arrays, list homogeneity, compound merge, self-shaping/nesting and get_if. Test/source staging inconsistencies (root-vs-child type, explicit conversions and missing emplace) are corrected1272. Tests were read, not run.

<a id="commit-1272"></a>
### Commit 1272 {#commit-1272}

[bc30ae0d047d](https://github.com/EndstoneMC/endstone/commit/bc30ae0d047d61ac7b9eee1a54928e4f47e0371b) · 2025-11-12T16:23:54Z · feat: finish NBT classes and tests

Wrapper-to-Tag constructors become implicit const-reference/rvalue overloads; adds self-shaping emplace and typed get references, fixes test expectations and invalid_argument cases. Primitive guessing remains intentionally rejected. No runtime validation. ListTag::push_back declarations remain without found definitions in this slice; emplace_back is the implemented mutation route.

<a id="commit-1273"></a>
### Commit 1273 {#commit-1273}

[ebbcbca329a8](https://github.com/EndstoneMC/endstone/commit/ebbcbca329a8e5fde66b77b11fad7e0f3cbd3a2d) · 2025-11-12T16:53:18Z · feat: handle empty class templates by adding placeholder 'pass'

Stub generator first inserts pass for empty classes; placement is revised1275 to an indented ellipsis in the docstring filter.

<a id="commit-1274"></a>
### Commit 1274 {#commit-1274}

[0cb247e1baf8](https://github.com/EndstoneMC/endstone/commit/0cb247e1baf8276a7023a8a919f7ea1c9744b23f) · 2025-11-12T16:55:24Z · feat(nbt): refactor NBT tags to inherit from new base `Tag` class

Stubs introduce common Tag base and richer ListTag interface ahead of the C++ base/binding implementation. Staging change, not a tested generated result.

<a id="commit-1275"></a>
### Commit 1275 {#commit-1275}

[0d7c5c6f255e](https://github.com/EndstoneMC/endstone/commit/0d7c5c6f255ecff9d4c2a768281b3e591f58d009) · 2025-11-12T16:55:35Z · feat(nbt): add dummy base type

Introduces empty TagBase inherited by scalar/array/list/compound wrappers; Python Tag binds this base rather than owning variant. Empty-class ellipsis is emitted only for undocumented empty classes.

<a id="commit-1276"></a>
### Commit 1276 {#commit-1276}

[893c752b624d](https://github.com/EndstoneMC/endstone/commit/893c752b624d6338bd7b80d3a2ba94b3315b73cb) · 2025-11-12T17:26:53Z · feat(nbt): add type caster for tags

Custom Python Tag caster accepts eleven exact wrapper types and copies to variant. Outbound cast initially takes Tag by value and ignores policy/parent, so nested return references become copies until1283. Adds list export and initial empty compound binding/stub.

<a id="commit-1277"></a>
### Commit 1277 {#commit-1277}

[2a406208eaec](https://github.com/EndstoneMC/endstone/commit/2a406208eaeccc99526d690ea67b1cf860f64ad5) · 2025-11-12T18:34:44Z · refactor: update stubs

Repairs Server.get_registry generic _T signature and generator placement, adds CompoundTag lazy export. Generated stubs are source evidence only.

<a id="commit-1278"></a>
### Commit 1278 {#commit-1278}

[aeca73f54505](https://github.com/EndstoneMC/endstone/commit/aeca73f5450556a46df433c0fd8cb085cc0f305b) · 2025-11-12T19:43:22Z · fix(stubgen): skip alias modules during rendering

Stub generator skips module aliases; custom caster advertises qualified endstone.nbt.Tag instead of unqualified name.

<a id="commit-1279"></a>
### Commit 1279 {#commit-1279}

[53b062473dd6](https://github.com/EndstoneMC/endstone/commit/53b062473dd6c9328a8c4d373df89c712662a7ed) · 2025-11-12T19:43:29Z · fix(stubgen): update import handling for specific `__init__.pyi` files

Stub postprocessing limits relative version import to root module and strips endstone.nbt prefixes inside NBT stub; module-specific name resolution repair.

<a id="commit-1280"></a>
### Commit 1280 {#commit-1280}

[b2b64a1a2e90](https://github.com/EndstoneMC/endstone/commit/b2b64a1a2e90719fe70791898475c4389cf5a638) · 2025-11-12T21:45:48Z · feat: add python binding for `CompoundTag`

Completes CompoundTag Python mapping constructor and dict-like methods, reference policies/iterators and array bool. Constructor argument is spelled mapping with trailing space; initial pop returns erase count, repaired1281. getitem uses C++ at and has no explicit Python KeyError conversion.

<a id="commit-1281"></a>
### Commit 1281 {#commit-1281}

[fbb83d7d1a9e](https://github.com/EndstoneMC/endstone/commit/fbb83d7d1a9ea7e65489dae35975d620524299eb) · 2025-11-13T12:17:24Z · feat(nbt): add `fmt` formatters for NBT tag types and escape handling

Adds SNBT-style formatters and fixes list negative-pop normalization plus compound-pop payload. Empty ByteArray formatter dereferences begin unconditionally; string escape doubles braces even though result is passed as format data. Ordered compound map makes output deterministic. No tests run.

<a id="commit-1282"></a>
### Commit 1282 {#commit-1282}

[d9559c2f5c5e](https://github.com/EndstoneMC/endstone/commit/d9559c2f5c5e428dd2a6748bdb2472a60614a57a) · 2025-11-13T13:09:43Z · test(nbt): add comprehensive tests for NBT tag types and improve Python bindings

Improves floating suffix formatting and Python repr using actual Python scalar/list/dict repr. Full529-line Python NBT tests cover defaults, equality, mutation, bounds, list type errors, compound operations/nesting and exact string/repr output. They do not cover empty ByteArray str, strided input buffers or vector resize while a buffer is exported.

<a id="commit-1283"></a>
### Commit 1283 {#commit-1283}

[2302b470479b](https://github.com/EndstoneMC/endstone/commit/2302b470479b3e604238f3e1193af2885e7e5977) · 2025-11-13T13:22:40Z · fix(nbt): update type caster to use references

Outbound Tag caster now takes const Tag& and forwards return policy plus parent to py::cast, enabling reference_internal nested mutations instead of unconditional copy. Incoming Python→variant still copies.

<a id="commit-1285"></a>
### Commit 1285 {#commit-1285}

[cf4234a9fe66](https://github.com/EndstoneMC/endstone/commit/cf4234a9fe6608f5635e210480c8f3b3221c09dd) · 2025-11-14T14:35:51Z · feat(nbt): add NBT conversion functions

Adds bidirectional recursive native/public NBT conversion for all tag types, with unknown native types mapped to End. Initial header marks functions static across separate implementation TU;1286 removes static. Native list conversion skips null children; public-to-native list calls native add.
