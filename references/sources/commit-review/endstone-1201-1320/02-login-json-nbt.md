<!-- retrieval: {"source_ids":["public:commit:139ce9ba9c833f6d1bf3dddb440393d849d00b66","public:commit:2ac48b23bfcfc3fba0c9c483186ff028cf9057f3","public:commit:5a7f5153a8927e863afeef0a1e231fe5647acc8c","public:commit:63fb02a8d6e90ede604aabdb8a96ab54c1ddad6a","public:commit:6be768c507b4ed6fb051d9ce1b94729dcba63c39","public:commit:7d3082bab0652e37d69b2c67050179f85a564e8b","public:commit:8eff20e277291856d2f56a95d4a74749376abffa","public:commit:92b5cee68cf77d886004d3ba2f1d66d31bb179f6","public:commit:aa6a81dfc5da575906cfbd1b1ae475cb8e9954e8","public:commit:cc5ba135854fcd90dde9b33b91d755ec5efb10d6","public:commit:da46104e6a747a37ce1e7cd72c0ccb83b51696fa","public:commit:e166a94819b017931066d5cdd420f78498d43b8a","public:commit:edc121505f8a5002753b3c60cc3ea4ffb4d15108","public:commit:f05495c86e94bdc70117fa232b872b1a451e59e3","public:commit:f0bd94ba56d57684c9e46f152c792ff04518ebe0"],"source_type":"public","date":"2024-06-23..2024-07-01","topics":["lifetime","ffi","testing","build","recovery","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Login metadata and native JSON/NBT boundaries {#login-metadata-and-native-json-nbt-boundaries}

## Login context before exposing metadata {#login-context-before-exposing-metadata}

Primary login interception moves to trytLoadPlayer and a separate subclient creation hook at 1221. The name is the host's spelling. Both call the original first and dispatch the cancellable login event afterward. Request models (1222–1223) then make metadata accessible, followed by locale and device fields initialized before the events (1228–1229). The observable design is to prepare the wrapper's metadata before plugins inspect it. The native call graph is not reconstructed fully enough to guarantee that every host route dispatches exactly once.

Locale, DeviceOS and DeviceId come from the client's request payload. Defaults for absent language/OS and a UUID conversion do not authenticate that device. A nonempty malformed UUID has no local catch. The initialized data must be described as client metadata rather than a secure identity claim. Request and token structures are borrowed views of native state; their presence does not imply that Endstone performs signature verification here.

## Two different JSON roles {#two-different-json-roles}

Removing jsoncpp (1225) and constructing a 16-byte Json::Value view (1226–1227) addresses host representation. The correction from char* to char** is particularly concrete evidence that convenient ordinary library types cannot be substituted blindly at an ABI boundary. Full implementation context shows lookup, scalar conversion, a zero-backed null object and key allocation, but no complete owning Value lifecycle. This should not be reused as an endorsed general-purpose JSON library.

The nlohmann_json integration in [the build dossier](06-build-vendoring-release.md#commit-1254) serves a different purpose: convenient in-process data snapshots and export. That separation explains why both JSON names coexist without requiring them to share layout or ownership. A native-view-to-export projection can be appropriate while still requiring explicit conversion and trust boundaries.

## NBT implementation is incremental, not a blanket codec claim {#nbt-implementation-is-incremental-not-a-blanket-codec-claim}

Compound lookup/equality/hash move out of line at 1239, variant storage changes at 1240, named-tag writing arrives at 1241 and copy direction is repaired at 1242. These commits are causally adjacent and individually different. The first copy attempt is not silently replaced in the record by the corrected form. At the final boundary, CompoundTag::load still throws not implemented. Equality tests every source entry without a cardinality check; a strict subset can compare equal in one direction. deepCopy clears before reading and is unsafe for self-copy. These are bounded counterexamples to claiming full container correctness, not a request to audit every NBT method.

Public payload exposure and list iteration at 1260 make the generic converter possible at 1261. JSON intentionally carries values rather than NBT widths/tag identities; empty containers currently emerge as null. That is suitable evidence for an inspection projection, not lossless serialization or persistence recovery. Final ListTag context confirms that its pre-existing load/copy/equality details are independent of this new access surface and were not repaired by making get/size public. Typed string/compound access returns empty/null for absence or wrong type (1273 in the UI dossier and 1309 here).

## Applicability, attribution and verification {#applicability-attribution-and-verification}

Use these cases for native-versus-owned representations, initialization ordering before plugin callbacks, borrowed data access, and distinguishing convenient export from reversible storage. Do not turn missing-value fallbacks into malformed-input validation claims. No external login issue/review discussion, packet signatures, live native memory or NBT round-trip tests were examined. Full relevant source blobs and all changed code were read; methods remain host-version sensitive. Vincent's commit attribution covers the authored integration patches, while host format/type contracts remain externally derived.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1221"></a>
### 1221: refactor: replace ServerNetworkHandler::_loadNewPlayer with ServerNetworkHandler::trytLoadPlayer {#commit-1221}

Source: [f0bd94ba56d57684c9e46f152c792ff04518ebe0](https://github.com/EndstoneMC/endstone/commit/f0bd94ba56d57684c9e46f152c792ff04518ebe0), 2024-06-23T11:05:33Z; git author Vincent. Disposition: substantive.

Moves primary login interception from _loadNewPlayer to the host-spelled trytLoadPlayer, and adds _createNewPlayer handling for subclients. Each path calls original first, then dispatches login and kicks if cancelled. This broadens explicit login coverage to both request routes. A guarantee of exactly one event across the entire undocumented native call graph is not established by these two local hooks.

<a id="commit-1222"></a>
### 1222: feat: add ConnectionRequest and SubClientConnectionRequest {#commit-1222}

Source: [6be768c507b4ed6fb051d9ce1b94729dcba63c39](https://github.com/EndstoneMC/endstone/commit/6be768c507b4ed6fb051d9ce1b94729dcba63c39), 2024-06-23T15:40:20Z; git author Vincent. Disposition: staging.

Models ConnectionRequest, SubClientConnectionRequest and WebToken data, including JSON header/payload and signature storage. Initial getData guards raw-token/data-info state. These borrowed native structures prepare locale/device initialization; the patch is not an implementation of authentication or token-signature verification.

<a id="commit-1223"></a>
### 1223: fix: correct ConnectionRequest::getData {#commit-1223}

Source: [8eff20e277291856d2f56a95d4a74749376abffa](https://github.com/EndstoneMC/endstone/commit/8eff20e277291856d2f56a95d4a74749376abffa), 2024-06-24T08:52:15Z; git author Vincent. Disposition: corrective.

Corrects ConnectionRequest::getData to guard the certificate and raw token before dereference, and refines native offsets/comments. This is the local null-chain repair to 1222. It does not validate JSON contents, trustworthiness or the lifetime of the host request after login.

<a id="commit-1225"></a>
### 1225: chore(deps): remove jsoncpp from conanfile.py {#commit-1225}

Source: [edc121505f8a5002753b3c60cc3ea4ffb4d15108](https://github.com/EndstoneMC/endstone/commit/edc121505f8a5002753b3c60cc3ea4ffb4d15108), 2024-06-24T08:59:19Z; git author Vincent. Disposition: build_configuration.

Removes jsoncpp from Conan and CMake integration before introducing a minimal native-layout Value model. This avoids treating the package implementation as automatically ABI-compatible with the host's embedded JSON representation. That compatibility rationale is an inference from the adjacent changes, not an explicit design statement in the commit.

<a id="commit-1226"></a>
### 1226: feat: add Json::Value {#commit-1226}

Source: [cc5ba135854fcd90dde9b33b91d755ec5efb10d6](https://github.com/EndstoneMC/endstone/commit/cc5ba135854fcd90dde9b33b91d755ec5efb10d6), 2024-06-24T12:38:28Z; git author Vincent. Disposition: substantive.

Introduces a 16-byte Json::Value layout, scalar conversions, map/key lookup, zero-backed null sentinel and minimal allocation helpers. This serves native login-data inspection, not a complete replacement JSON library: copied Value instances are shallow, allocation is present without a general owning destructor, and initial string storage is incorrectly char*. The next commit changes that ABI representation.

<a id="commit-1227"></a>
### 1227: fix: change string type from char* to char** in ValueHolder {#commit-1227}

Source: [5a7f5153a8927e863afeef0a1e231fe5647acc8c](https://github.com/EndstoneMC/endstone/commit/5a7f5153a8927e863afeef0a1e231fe5647acc8c), 2024-06-24T13:00:47Z; git author Vincent. Disposition: corrective.

Changes native string storage to char** and dereferences it in asCString/asString, matching the observed host representation rather than normalizing it to a conventional owning string. asString guards the outer pointer only; the null singleton is also placed in the correct namespace. The patch demonstrates an ABI correction, with no general JSON ownership or malformed-value guarantee.

<a id="commit-1228"></a>
### 1228: feat: add Player::getLocale {#commit-1228}

Source: [92b5cee68cf77d886004d3ba2f1d66d31bb179f6](https://github.com/EndstoneMC/endstone/commit/92b5cee68cf77d886004d3ba2f1d66d31bb179f6), 2024-06-24T13:21:38Z; git author Vincent. Disposition: api_change.

Adds Player.locale with en-US fallback, copying a nonempty LanguageCode from primary connection data before the login event. Updates C++/Python surfaces. This exposes client-supplied locale metadata; it neither verifies that value against installed translations nor changes global server language. Subclient initialization is unified in 1229.

<a id="commit-1229"></a>
### 1229: feat: add Player::getDeviceOS and getDeviceId {#commit-1229}

Source: [da46104e6a747a37ce1e7cd72c0ccb83b51696fa](https://github.com/EndstoneMC/endstone/commit/da46104e6a747a37ce1e7cd72c0ccb83b51696fa), 2024-06-24T15:26:01Z; git author Vincent. Disposition: substantive.

Consolidates request initialization over primary/subclient variants before their login events. Reads DeviceOS with enum conversion and Unknown fallback, parses a nonempty DeviceId as UUID, and initializes locale. These are client metadata, not authenticated device identity. The nonempty UUID parse has no local exception guard; safe handling of arbitrary payloads is not proven by default fallbacks for missing values.

<a id="commit-1239"></a>
### 1239: feat: implement more methods for class CompoundTag {#commit-1239}

Source: [7d3082bab0652e37d69b2c67050179f85a564e8b](https://github.com/EndstoneMC/endstone/commit/7d3082bab0652e37d69b2c67050179f85a564e8b), 2024-06-25T14:29:59Z; git author Vincent. Disposition: substantive.

Moves CompoundTag operations out of line and adds heterogeneous string_view lookup, presence checks, child comparison and ordered hash combination. Equality only checks this object's entries against the other and omits a size test, so it is asymmetric for strict subsets. Write/load/copy still contain unfinished paths. Also removes obsolete CommandPosition serialization; this is not a completed NBT implementation.

<a id="commit-1240"></a>
### 1240: refactor: CompoundTagVariant {#commit-1240}

Source: [e166a94819b017931066d5cdd420f78498d43b8a](https://github.com/EndstoneMC/endstone/commit/e166a94819b017931066d5cdd420f78498d43b8a), 2024-06-25T15:51:23Z; git author Vincent. Disposition: staging.

Replaces inheritance from std::variant with an explicit CompoundTagVariant member and dispatches moved Tag objects by their type ID. Begins copy/deepCopy work, but copy initially transfers in the wrong direction and deepCopy is unfinished. These intermediate semantics are preserved rather than treating the following correction as if present from the start.

<a id="commit-1241"></a>
### 1241: feat: add NbtIo::writeNamedTag {#commit-1241}

Source: [2ac48b23bfcfc3fba0c9c483186ff028cf9057f3](https://github.com/EndstoneMC/endstone/commit/2ac48b23bfcfc3fba0c9c483186ff028cf9057f3), 2024-06-25T16:11:36Z; git author Vincent. Disposition: substantive.

Adds NbtIo::writeNamedTag: type ID, then name and payload except for End. CompoundTag writes its children and a terminating End byte. This fills the write path while load remains unimplemented. It is evidence for a native-format writer fragment, not successful read/write round trips or a complete standalone NBT codec.

<a id="commit-1242"></a>
### 1242: feat: add more put methods in CompoundTag {#commit-1242}

Source: [63fb02a8d6e90ede604aabdb8a96ab54c1ddad6a](https://github.com/EndstoneMC/endstone/commit/63fb02a8d6e90ede604aabdb8a96ab54c1ddad6a), 2024-06-25T16:33:59Z; git author Vincent. Disposition: corrective.

Corrects copy to deep-copy from the source into the newly allocated compound; deepCopy clears the destination and copies each child. Adds generic Tag/unique_ptr insertion and short/double helpers, with null unique_ptr handled. Self deepCopy still clears its own source, and list-level copy/type semantics remain separate. No blanket correctness conclusion follows from fixing the direction bug.

<a id="commit-1260"></a>
### 1260: refactor: make member data public in nbt tags {#commit-1260}

Source: [aa6a81dfc5da575906cfbd1b1ae475cb8e9954e8](https://github.com/EndstoneMC/endstone/commit/aa6a81dfc5da575906cfbd1b1ae475cb8e9954e8), 2024-06-27T11:04:50Z; git author Vincent. Disposition: api_change.

Makes scalar/array tag payload members public under data, removes CompoundTag friendship, and adds ListTag size/get plus compound aliases/annotations. This changes internal encapsulation and permits generic inspection. It does not repair existing ListTag load/copy/equality semantics; get remains unchecked indexed access. Keep exposure convenience separate from a claim of safe arbitrary NBT manipulation.

<a id="commit-1261"></a>
### 1261: feat: add a helper function that converts a nbt tag to json {#commit-1261}

Source: [f05495c86e94bdc70117fa232b872b1a451e59e3](https://github.com/EndstoneMC/endstone/commit/f05495c86e94bdc70117fa232b872b1a451e59e3), 2024-06-27T11:05:16Z; git author Vincent. Disposition: substantive.

Adds recursive NBT-to-JSON conversion for scalars, lists, compounds and integer/byte arrays. Numeric widths and NBT type distinctions collapse into JSON values; empty containers remain the default null because they are not initialized as array/object. This is an inspection/export projection, not a reversible format conversion. Later refactoring moves it into the data layer without adding round-trip guarantees.

<a id="commit-1309"></a>
### 1309: feat: add CompoundTag::getCompound {#commit-1309}

Source: [139ce9ba9c833f6d1bf3dddb440393d849d00b66](https://github.com/EndstoneMC/endstone/commit/139ce9ba9c833f6d1bf3dddb440393d849d00b66), 2024-07-01T08:42:26Z; git author Vincent. Disposition: substantive.

Adds typed CompoundTag::getCompound, returning a borrowed compound only when the key exists with the right tag type, otherwise nullptr. This supports nested custom item data inspection. It neither deep-copies nor repairs the broader NBT equality/load limitations preserved in this unit.
