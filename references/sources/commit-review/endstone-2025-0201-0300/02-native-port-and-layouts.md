<!-- retrieval: {"source_ids":["public:commit:00f02fc9a1ab6d010e2b08482b2b03d19242bd68","public:commit:067e30a8ddecaf3cec21a52a5ce5df6665ebff5c","public:commit:071cb0966e93ae36bbe5d38edee9809994f3b8dc","public:commit:0b18d1e261f624c1888ca2ddb9cacd84406d1218","public:commit:0c06473d1719cfdb79a3395204ebc7c541a93699","public:commit:0e3f6516800aa8469fb1d635ca598f852c49b386","public:commit:12f6dc3401508d77f04ff4c2e882e6fedb0286b0","public:commit:14f36a9832c724869197a9fd719f746c71b4d1e3","public:commit:182e81aedf1e9d9aca042a1c7c28679f4a31453d","public:commit:1b584f984645099a2e54c4d328d9afcb0a678a73","public:commit:210776e94488cfc2c23b6e4bf0287a3293e0d665","public:commit:3bb01af0d23bfb3e08f3b915d2f6ef045625b658","public:commit:3d7192a770cb42699146dce5d0e7c904dc8c9aa3","public:commit:3ede82a7a4f76d294b6c67d99c3e4d372e3da9d4","public:commit:5b3513e04a4bbcbcbf66245da5e013eafa9869a9","public:commit:6f3a2e8c6ceb54a18ea482560b736b33ea2072ce","public:commit:76f8795bf40385f1a951136941392928f5f81a94","public:commit:834bad07377d76052940375898c3997a0239b231","public:commit:8f93bfc7850e21466d8ea5647bc64a15e2339400","public:commit:92bc5b750f93f0bf1e08db589c407fc7d288968b","public:commit:9a9c47346232e9d0fca2b9b6f8164347f7340663","public:commit:9eda28c67b6ed1c31fef01ad2293e1f9d7059adc","public:commit:9f085ec467b69e62e7e1fd993324249272fda421","public:commit:a0f9d1f02c3f09b76d28244f4de1e34560cb9c26","public:commit:a584e7f1a9235510bf31647ffb166283d0e9fc72","public:commit:abe8ff0304b0a63ca8aad4ddfc30d9d283ea27f8","public:commit:afbcf135f53f7dbaaf6dffddbb5a1de695fef122","public:commit:b0cf8458da86714cc0e2c6ec2f1d072eb58de60b","public:commit:b1abbc204b675c53225abb9abe4ba0fa649c25dc","public:commit:b3ffabfda8a0e379250e0f372a478f1c72699e6f","public:commit:b7a6338257fd0732b7a11c64c096f3b38f127e7d","public:commit:be5efa7689a3e93f2ee052e87d63fc01b6118b62","public:commit:c27509dd9e855dc509781bfbdc43d1202ba4e1ec","public:commit:c2cf0184fb873c1630ed41d5ace50256c4d9145e","public:commit:c7b48fa1637106027866d78255d7688904d5d08e","public:commit:e365d4ca42fa2f1ef5e349163ddfe81b22c0a4c7","public:commit:e6d4d09ce1bd5097d4b7b4e78797c5252a59487c","public:commit:e817978c293d767a35ef200b04761628ba0deeaa","public:commit:e9506d0f46e3485e342099f76ee959489ae1045a","public:commit:eba2307d13fa366a0a97303813f1dd04c67a416a"],"source_type":"public","date":"2025-02-13..2025-02-23","topics":["lifetime","concurrency","ffi","testing","build","api","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Bedrock 1.21.60 port and native layout reconstruction {#bedrock-1-21-60-port-and-native-layout-reconstruction}

## Windows-first migration, then Linux repair {#windows-first-migration-then-linux-repair}

223 begins a Windows-specific port: new offsets coexist with zero/unresolved entries and old Linux addresses. Direct Player name/inventory access expands Actor/Mob/Player and container declarations225–227. Incorrect assertions, opaque fields and duplicated storage are revised as the underlying native types become clearer.270 replacing Container's std::string with RedactableString supersedes earlier padding guesses;295 applies the same type insight to BossEventPacket. Comments and sizeof assertions are compatibility hypotheses until validated against the host.

The port also changes virtual ordering, actor flags/data IDs, vertical flight speed, biome containers and opaque categories, mutable-attribute callback context, Height/ClipParameters and BlockLegacy material/color fields. These are ABI contracts, not cosmetic header changes.243 updates item initialization version/context.248 separates mutable attribute access from its modification context so writes can notify the native dirty callback.250 and271 continue virtual-slot reconstruction. The separate native sendTo overload256 is supplied to the scoreboard sender as an explicitly unsupported throwing path, not a completed transport feature.

getI18n223 initially adds a byte offset to an I18n pointer;237 changes to byte-address arithmetic. Linux forwarding is only restored261. The Linux port also fixes dependent template syntax and constructor declarations, changes pack-key-provider parameter ownership shape and rewrites Linux symbols. The data audit verifies all literal offset changes and structural symbol additions/removals, with full non-literal code changes read.262 fixes the Windows decorated symbol for the changed pack signature.264 later restores function storage alignment after261 removed its prior alignment-bearing union. Platform success is reported in commit messages, not reproduced here.

## Networking prerequisites and validation gates {#networking-prerequisites-and-validation-gates}

257's request-layout refactor adds certificate validity checking before token data is exposed, a semantic gate beyond field reorder.282 expresses that through a GameServerToken wrapper owning a certificate. This does not implement or verify native cryptographic checks.276–280 reconstruct NetworkSystem fields, callback virtuals, variant-backed server/client references and borrowed binary stream views. Several types are declarations or placeholders, including the temporary int asynchronous completion alias; their presence must not be mistaken for complete async behavior.

279 installs pass-through native packet-filter hooks; the public event policy only arrives291/293.280 refreshes BinaryStream's stored view after append, but callers still receive borrowed storage.277 renames protocol enum entries/adds IDs without a transport fixture.284's cap200 becomes effective in285's callers.286 supplies the all-zero UUID sentinel after its initial use. These intermediate dependency gaps are retained rather than edited into a fictitious atomic port.

## Exact reuse and boundaries {#exact-reuse-and-boundaries}

The completed PR133 dossier already read its entire103-file Windows port.184 file occurrences in this unit exactly match its old/new blobs and complete hunks:81 individual-commit occurrences plus103 merge occurrences. Only those proven file changes reuse that reading; intermediate residual layouts, every message and integration consequences were read separately. This is duplication removal, not counting the same net patch as184 independent engineering ideas. Reuse proof retains base/head and hunk identity. No disassembler, symbol generator, compiler or native host was executed.


<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}


<a id="commit-223"></a>
### 223. feat: 1.21.60 support for BDS (Windows) {#commit-223}

[14f36a9832c724869197a9fd719f746c71b4d1e3](https://github.com/EndstoneMC/endstone/commit/14f36a9832c724869197a9fd719f746c71b4d1e3) · 2025-02-13T14:51:40Z · author Vincent.

Parents: `be599b38b6286c06c33138b5777cdba147251c84`. Full message and sources: parent 1.

Starts Windows 1.21.60 port: updates advertised version/Windows offsets, removes inlined symbols, leaves several entries zero and Linux offsets on old version. Command name resolves through registry symbolToString (exact verified PR133 reuse). getI18n temporarily adds byte offset to an I18n* rather than byte pointer;237 fixes pointer arithmetic. This intermediate port is incomplete, not cross-platform compatibility proof.

Coverage: 6 all-parent changed-file occurrences; 3 exact prior PR133 file-patch occurrences reused.


<a id="commit-224"></a>
### 224. feat: update enums for 1.21.60 {#commit-224}

[3ede82a7a4f76d294b6c67d99c3e4d372e3da9d4](https://github.com/EndstoneMC/endstone/commit/3ede82a7a4f76d294b6c67d99c3e4d372e3da9d4) · 2025-02-13T15:03:28Z · author Vincent.

Parents: `14f36a9832c724869197a9fd719f746c71b4d1e3`. Full message and sources: parent 1.

Updates actor flags/data enum definitions through exact PR133 patch reuse, and adds VerticalFlySpeed ability at19 with count20. Serialized abilities insert vertical float before walk speed, shifting wire/native layout. Existing constructor populates it;229 later moves constructor implementation. No ABI/wire fixture test was run.

Coverage: 4 all-parent changed-file occurrences; 2 exact prior PR133 file-patch occurrences reused.


<a id="commit-225"></a>
### 225. feat: add members to `Player` class {#commit-225}

[210776e94488cfc2c23b6e4bf0287a3293e0d665](https://github.com/EndstoneMC/endstone/commit/210776e94488cfc2c23b6e4bf0287a3293e0d665) · 2025-02-13T19:29:37Z · author Vincent.

Parents: `3ede82a7a4f76d294b6c67d99c3e4d372e3da9d4`. Full message and sources: parent 1.

Expands native Actor/Mob/Player/container/inventory layouts so inlined Player getters can read members directly; fills previously zero item-init and hurt offsets. Twenty-one file changes exactly reuse completed PR133 reading; all intermediate residual layouts were read. Initial getter assertions incorrectly give both inventory and name offset1480, removed226; several fields are repaired227. Raw placeholder arrays, opaque declarations and size assertions are compatibility hypotheses, not host verification.

Coverage: 33 all-parent changed-file occurrences; 21 exact prior PR133 file-patch occurrences reused.


<a id="commit-226"></a>
### 226. feat: add `FillingContainer` {#commit-226}

[eba2307d13fa366a0a97303813f1dd04c67a416a](https://github.com/EndstoneMC/endstone/commit/eba2307d13fa366a0a97303813f1dd04c67a416a) · 2025-02-13T19:53:14Z · author Vincent.

Parents: `210776e94488cfc2c23b6e4bf0287a3293e0d665`. Full message and sources: parent 1.

Adds FillingContainer hierarchy and PlayerInventory implementation via exact PR133 reuse, replaces empty Inventory shell, registers source in CMake and adds mutable getInventory. Removes225's contradictory getter offsetof assertions and records name offset3160 in comments. Changing comments/removing assertions is not evidence native layout was proven.

Coverage: 8 all-parent changed-file occurrences; 3 exact prior PR133 file-patch occurrences reused.


<a id="commit-227"></a>
### 227. fix: `Player` class members {#commit-227}

[182e81aedf1e9d9aca042a1c7c28679f4a31453d](https://github.com/EndstoneMC/endstone/commit/182e81aedf1e9d9aca042a1c7c28679f4a31453d) · 2025-02-13T21:12:42Z · author Vincent.

Parents: `eba2307d13fa366a0a97303813f1dd04c67a416a`. Full message and sources: parent 1.

Repairs intermediate225 layout: comments out Actor wall fields and filtered creative arrays, removes player bed-position field, renames member typos, adds opaque SimpleContainer integer and repeated PlayerUIContainer storage. Unknown field-name TODOs remain explicit. The sequence shows iterative reverse-engineering, not one stable complete class model.

Coverage: 6 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-229"></a>
### 229. refactor: move the implementation of `SerializedAbilitiesData` to a separate source file {#commit-229}

[afbcf135f53f7dbaaf6dffddbb5a1de695fef122](https://github.com/EndstoneMC/endstone/commit/afbcf135f53f7dbaaf6dffddbb5a1de695fef122) · 2025-02-14T00:09:40Z · author Vincent.

Parents: `0ce5261e6befb28adfdaeb60d13f53bc2ce23d64`. Full message and sources: parent 1.

Moves SerializedAbilitiesData constructor from header to source and adds it to Bedrock target; destination body exactly matches prior-read PR133. The layer/bitset and fly/walk/vertical-speed logic is retained. This is compilation-boundary relocation, not changed serialization semantics or measured compile-time improvement.

Coverage: 3 all-parent changed-file occurrences; 1 exact prior PR133 file-patch occurrences reused.


<a id="commit-230"></a>
### 230. fix: correct members and virtual functions {#commit-230}

[b1abbc204b675c53225abb9abe4ba0fa649c25dc](https://github.com/EndstoneMC/endstone/commit/b1abbc204b675c53225abb9abe4ba0fa649c25dc) · 2025-02-14T15:40:48Z · author Vincent.

Parents: `afbcf135f53f7dbaaf6dffddbb5a1de695fef122`. Full message and sources: parent 1.

Corrects native AppPlatformListener, Random, ILevel/Level and Minecraft layouts; five exact PR133 files reused. Adds Level virtual slots for unknown/armor-trim/player-sleep operations and forwards additional type declarations. Unknown slot and Linux-specific extension comments remain; public method names and layout assertions do not prove binary compatibility.

Coverage: 7 all-parent changed-file occurrences; 5 exact prior PR133 file-patch occurrences reused.


<a id="commit-235"></a>
### 235. feat: add copy constructor to `CommandRegistry::Symbol` {#commit-235}

[067e30a8ddecaf3cec21a52a5ce5df6665ebff5c](https://github.com/EndstoneMC/endstone/commit/067e30a8ddecaf3cec21a52a5ce5df6665ebff5c) · 2025-02-15T17:23:54Z · author Vincent.

Parents: `c0ac26ef101e52d3540f7f7922268b6f0e830def`. Full message and sources: parent 1.

Adds explicit Symbol copy constructor copying integer value_. Small full diff read; it preserves value semantics but changes trivial-copy properties relative to an implicit constructor. No author rationale or benchmark beyond title.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-236"></a>
### 236. fix: BlockLegacy members {#commit-236}

[1b584f984645099a2e54c4d328d9afcb0a678a73](https://github.com/EndstoneMC/endstone/commit/1b584f984645099a2e54c4d328d9afcb0a678a73) · 2025-02-15T17:24:15Z · author Vincent.

Parents: `067e30a8ddecaf3cec21a52a5ce5df6665ebff5c`. Full message and sources: parent 1.

Reconstructs BlockLegacy layout: removes brightness_gamma, switches Material pointer to const reference and mce::Color to Color, changes tint enum to byte width and reorders instrument/tint fields, exposes renamed event map. Corresponding implementation field access exactly reuses PR133. Stored offsets and TODO-era layout remain unvalidated against native server.

Coverage: 3 all-parent changed-file occurrences; 1 exact prior PR133 file-patch occurrences reused.


<a id="commit-237"></a>
### 237. fix: getI18n implementation {#commit-237}

[0c06473d1719cfdb79a3395204ebc7c541a93699](https://github.com/EndstoneMC/endstone/commit/0c06473d1719cfdb79a3395204ebc7c541a93699) · 2025-02-15T17:24:25Z · author Vincent.

Parents: `1b584f984645099a2e54c4d328d9afcb0a678a73`. Full message and sources: parent 1.

Fixes223 getI18n address scaling by adding offset to char* before casting to I18n*. Wraps it in _WIN32, leaving no return path for Linux until later port. Hardcoded address TODO remains; no discovery or relocation validation.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-240"></a>
### 240. fix: update the vftable of `BlockLegacy` {#commit-240}

[834bad07377d76052940375898c3997a0239b231](https://github.com/EndstoneMC/endstone/commit/834bad07377d76052940375898c3997a0239b231) · 2025-02-15T20:37:11Z · author Vincent.

Parents: `ce77169007a43b4fad6fad406f9903cec3089da3`. Full message and sources: parent 1.

Removes no-argument BlockLegacy::getRenderLayer virtual slot and retains contextual overload. This corrects downstream vtable ordering rather than changing a public Endstone rendering API. No running-native validation.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-241"></a>
### 241. fix: members in `BiomeRegistry` {#commit-241}

[5b3513e04a4bbcbcbf66245da5e013eafa9869a9](https://github.com/EndstoneMC/endstone/commit/5b3513e04a4bbcbcbf66245da5e013eafa9869a9) · 2025-02-15T21:12:15Z · author Vincent.

Parents: `834bad07377d76052940375898c3997a0239b231`. Full message and sources: parent 1.

All three files exactly match previously read PR133 patch: associative adapter/flat_set scaffolding and BiomeRegistry representation. Preserves port context and unresolved opaque native types; no independent collection algorithm preference inferred.

Coverage: 3 all-parent changed-file occurrences; 3 exact prior PR133 file-patch occurrences reused.


<a id="commit-242"></a>
### 242. fix: update the members of `Biome` {#commit-242}

[c2cf0184fb873c1630ed41d5ace50256c4d9145e](https://github.com/EndstoneMC/endstone/commit/c2cf0184fb873c1630ed41d5ace50256c4d9145e) · 2025-02-15T21:26:09Z · author Vincent.

Parents: `5b3513e04a4bbcbcbf66245da5e013eafa9869a9`. Full message and sources: parent 1.

Both file changes exactly reuse completed PR133: common type and Biome layout update, including opaque32-byte category entries with TODO. This is bounded native-layout reconstruction, not proved category behavior.

Coverage: 2 all-parent changed-file occurrences; 2 exact prior PR133 file-patch occurrences reused.


<a id="commit-243"></a>
### 243. fix: add missing member `item_parse_version` to `Item` class {#commit-243}

[3bb01af0d23bfb3e08f3b915d2f6ef045625b658](https://github.com/EndstoneMC/endstone/commit/3bb01af0d23bfb3e08f3b915d2f6ef045625b658) · 2025-02-15T21:54:43Z · author Vincent.

Parents: `c2cf0184fb873c1630ed41d5ace50256c4d9145e`. Full message and sources: parent 1.

Adds Item parse-version representation and related native item/recipe/registry/event adaptations, with seven file changes exactly reused from PR133. Residual actor include is read directly. Preserves the dependence on new compact semantic-version layout rather than treating the missing field as an isolated padding fix.

Coverage: 8 all-parent changed-file occurrences; 7 exact prior PR133 file-patch occurrences reused.


<a id="commit-245"></a>
### 245. fix: add missing members to `ServerNetworkHandler` {#commit-245}

[0e3f6516800aa8469fb1d635ca598f852c49b386](https://github.com/EndstoneMC/endstone/commit/0e3f6516800aa8469fb1d635ca598f852c49b386) · 2025-02-15T23:37:25Z · author Vincent.

Parents: `b188d49d0df5e76354ec04190f7d92a348267f0e`. Full message and sources: parent 1.

Adds missing ServerNetworkHandler fields via exact PR133 reading, plus forward declarations for classroom/controller/upload/filter/cache managers. Field existence and layout are known-source reconstruction; no networking behavior or ownership lifecycle is established by declarations alone.

Coverage: 2 all-parent changed-file occurrences; 1 exact prior PR133 file-patch occurrences reused.


<a id="commit-248"></a>
### 248. feat: add `AttributeModificationContext` for modifying attributes {#commit-248}

[12f6dc3401508d77f04ff4c2e882e6fedb0286b0](https://github.com/EndstoneMC/endstone/commit/12f6dc3401508d77f04ff4c2e882e6fedb0286b0) · 2025-02-16T14:36:05Z · author Vincent.

Parents: `d10ceb34829788095b48f018bdc29de1fee87ff7`. Full message and sources: parent 1.

Moves mutable attribute modification into a separate context carrying dirty-notification callback and returns MutableAttributeWithContext rather than mutable AttributeInstance reference. Eight exact PR133 file changes reused; public native declaration residual read. Preserves update/notification coupling, not just a type-name substitution; tests/runtime delivery not established.

Coverage: 9 all-parent changed-file occurrences; 8 exact prior PR133 file-patch occurrences reused.


<a id="commit-249"></a>
### 249. fix: update virtual table of `Actor` class {#commit-249}

[a0f9d1f02c3f09b76d28244f4de1e34560cb9c26](https://github.com/EndstoneMC/endstone/commit/a0f9d1f02c3f09b76d28244f4de1e34560cb9c26) · 2025-02-16T15:03:13Z · author Vincent.

Parents: `12f6dc3401508d77f04ff4c2e882e6fedb0286b0`. Full message and sources: parent 1.

Removes five Actor virtual slots (wall/render/step-related), adjusting vtable ordering. Full diff inspected. No change in public Endstone API and no reason beyond native-version correction is recorded.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-250"></a>
### 250. fix: update virtual table of `BlockSource` class {#commit-250}

[9eda28c67b6ed1c31fef01ad2293e1f9d7059adc](https://github.com/EndstoneMC/endstone/commit/9eda28c67b6ed1c31fef01ad2293e1f9d7059adc) · 2025-02-16T16:07:42Z · author Vincent.

Parents: `a0f9d1f02c3f09b76d28244f4de1e34560cb9c26`. Full message and sources: parent 1.

Three exact PR133 file changes align Height, BlockSource virtual methods and ClipParameters with the new native ABI. The interface declarations and layout assumptions were read through the verified PR dossier; no live host compatibility is established.

Coverage: 3 all-parent changed-file occurrences; 3 exact prior PR133 file-patch occurrences reused.


<a id="commit-255"></a>
### 255. fix: correct member orders in `Dimension` class {#commit-255}

[e365d4ca42fa2f1ef5e349163ddfe81b22c0a4c7](https://github.com/EndstoneMC/endstone/commit/e365d4ca42fa2f1ef5e349163ddfe81b22c0a4c7) · 2025-02-16T20:50:14Z · author Vincent.

Parents: `366bdb9f4fd2f1eae9095c217367f7e1f03190da`. Full message and sources: parent 1.

Moves Dimension has_weather into earlier native layout after block_source, revises the brightness offset and cleans comments. This is ABI repair rather than weather algorithm change; comments do not prove actual offsets.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-256"></a>
### 256. fix: update virtual table of `PacketSender` class {#commit-256}

[76f8795bf40385f1a951136941392928f5f81a94](https://github.com/EndstoneMC/endstone/commit/76f8795bf40385f1a951136941392928f5f81a94) · 2025-02-16T21:07:16Z · author Vincent.

Parents: `e365d4ca42fa2f1ef5e349163ddfe81b22c0a4c7`. Full message and sources: parent 1.

Adds PacketSender sendTo(NetworkIdentifier, SubClientId, Packet) virtual slot, Loopback override and a ScoreboardPacketSender override that throws Not supported. Completing an interface slot is not complete transport support.

Coverage: 4 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-257"></a>
### 257. fix: correct member order in `ConnectionRequest` class {#commit-257}

[e817978c293d767a35ef200b04761628ba0deeaa](https://github.com/EndstoneMC/endstone/commit/e817978c293d767a35ef200b04761628ba0deeaa) · 2025-02-17T01:11:13Z · author Vincent.

Parents: `76f8795bf40385f1a951136941392928f5f81a94`. Full message and sources: parent 1.

Reorders ConnectionRequest and SubClientConnectionRequest pointers and now requires certificate isValid as well as presence before reading raw token data. This adds a validation gate despite the structural-refactor title. Certificate verification itself remains native.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-258"></a>
### 258. chore: fix comments in `SubClientConnectionRequest` header {#commit-258}

[e6d4d09ce1bd5097d4b7b4e78797c5252a59487c](https://github.com/EndstoneMC/endstone/commit/e6d4d09ce1bd5097d4b7b4e78797c5252a59487c) · 2025-02-17T01:18:11Z · author Vincent.

Parents: `e817978c293d767a35ef200b04761628ba0deeaa`. Full message and sources: parent 1.

Corrects ConnectionRequest offset comments. No executable change and no independent lesson beyond keeping ABI annotations consistent; no native layout verification was performed.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-259"></a>
### 259. feat: add `CreativeGroupInfo` {#commit-259}

[a584e7f1a9235510bf31647ffb166283d0e9fc72](https://github.com/EndstoneMC/endstone/commit/a584e7f1a9235510bf31647ffb166283d0e9fc72) · 2025-02-18T18:18:25Z · author Vincent.

Parents: `e6d4d09ce1bd5097d4b7b4e78797c5252a59487c`. Full message and sources: parent 1.

Adds CreativeCategory values and CreativeGroupInfo native layout, stores creative groups in ItemRegistry. GameSession changes preserve reference/value conversion to the existing registry non-owner interface; no new lifetime ownership is supplied.

Coverage: 9 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-260"></a>
### 260. feat: add creative groups to DevTools {#commit-260}

[e9506d0f46e3485e342099f76ee959489ae1045a](https://github.com/EndstoneMC/endstone/commit/e9506d0f46e3485e342099f76ee959489ae1045a) · 2025-02-18T18:41:15Z · author Vincent.

Parents: `a584e7f1a9235510bf31647ffb166283d0e9fc72`. Full message and sources: parent 1.

Exposes creative-group getters, registers their source, and dumps group name/category/icon to devtools JSON. Also changes wheel CMake build type Release to RelWithDebInfo, unrelated to the feature title and reversed at265. Native category/icon correctness was not exercised.

Coverage: 9 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-261"></a>
### 261. feat: 1.21.60 support for Linux {#commit-261}

[3d7192a770cb42699146dce5d0e7c904dc8c9aa3](https://github.com/EndstoneMC/endstone/commit/3d7192a770cb42699146dce5d0e7c904dc8c9aa3) · 2025-02-19T14:20:05Z · author Vincent.

Parents: `e9506d0f46e3485e342099f76ee959489ae1045a`. Full message and sources: parent 1.

Linux 1.21.60 port restores Linux getI18n native forwarding, fixes dependent-template syntax and missing function assignment return, adds constructor declarations, and changes pack key provider to NonOwnerPointer by value. Exact TOML data comparison verifies 47 Linux offset changes, five additions and nine removals while 51 Windows entries stay unchanged; offset literal bulk receives proportional verification. Removes function storage's max-align union, followed by263–264 repairs; Windows decorated signature needs262.

Coverage: 12 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-262"></a>
### 262. fix: resolve compilation error on Windows {#commit-262}

[92bc5b750f93f0bf1e08db589c407fc7d288968b](https://github.com/EndstoneMC/endstone/commit/92bc5b750f93f0bf1e08db589c407fc7d288968b) · 2025-02-19T14:38:23Z · author Vincent.

Parents: `3d7192a770cb42699146dce5d0e7c904dc8c9aa3`. Full message and sources: parent 1.

Updates Windows decorated createPack symbol to the NonOwnerPointer value parameter introduced261, keeping its offset. Message says Windows compile fix; no compiler was executed here.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-267"></a>
### 267. refactor: update the typedef of `MobCategoryMap` {#commit-267}

[b3ffabfda8a0e379250e0f372a478f1c72699e6f](https://github.com/EndstoneMC/endstone/commit/b3ffabfda8a0e379250e0f372a478f1c72699e6f) · 2025-02-19T23:48:47Z · author Vincent.

Parents: `2b88490577173ea28fe00b8aabb1098b9b55d2af`. Full message and sources: parent 1.

Replaces opaque MobCategoryMap32-byte array with WeightedRandomList<shared_ptr<MobSpawnerData>>. Header arrives268, so the history contains an intentional/staged intermediate incomplete dependency, not a standalone validated state.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-268"></a>
### 268. refactor: update player events {#commit-268}

[abe8ff0304b0a63ca8aad4ddfc30d9d283ea27f8](https://github.com/EndstoneMC/endstone/commit/abe8ff0304b0a63ca8aad4ddfc30d9d283ea27f8) · 2025-02-19T23:49:04Z · author Vincent.

Parents: `b3ffabfda8a0e379250e0f372a478f1c72699e6f`. Full message and sources: parent 1.

Defines WeightedRandomList storage and identifies PlayerEvent26 as weak_ptr<ClientJoinedEventData>, adding detailed joined-client data fields. Constructor is declared, not implemented here. This repairs event ABI identification but does not yet change public PlayerJoinEvent timing.

Coverage: 3 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-270"></a>
### 270. fix: correct the members of `Container` class {#commit-270}

[071cb0966e93ae36bbe5d38edee9809994f3b8dc](https://github.com/EndstoneMC/endstone/commit/071cb0966e93ae36bbe5d38edee9809994f3b8dc) · 2025-02-20T01:05:28Z · author Vincent.

Parents: `2e55636f369cb4e2ff5f0ff7682b5d53e70325c4`. Full message and sources: parent 1.

Changes Container name from std::string to RedactableString and removes227's guessed SimpleContainer integer and duplicate PlayerUI storage. Correcting an underlying field type supersedes opaque padding fixes. Host ABI validity is still untested.

Coverage: 3 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-271"></a>
### 271. fix: correct virtual tables for `BlockSource` and `Level` {#commit-271}

[6f3a2e8c6ceb54a18ea482560b736b33ea2072ce](https://github.com/EndstoneMC/endstone/commit/6f3a2e8c6ceb54a18ea482560b736b33ea2072ce) · 2025-02-20T01:13:58Z · author Vincent.

Parents: `071cb0966e93ae36bbe5d38edee9809994f3b8dc`. Full message and sources: parent 1.

Names an unknown BlockSource virtual as isInWall(Vec3)->bool and moves the low-memory interface slot into ILevel while removing a Level unknown slot. Vtable ordering is semantically relevant despite no new public feature.

Coverage: 3 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-276"></a>
### 276. feat: add `NetworkSystem` class {#commit-276}

[0b18d1e261f624c1888ca2ddb9cacd84406d1218](https://github.com/EndstoneMC/endstone/commit/0b18d1e261f624c1888ca2ddb9cacd84406d1218) · 2025-02-20T13:57:40Z · author Vincent.

Parents: `58440c88206ed74b225a3ca1374375a89c278ed3`. Full message and sources: parent 1.

Introduces native NetworkSystem ownership fields, connection callbacks and packet-filter enums, including receive buffer/send stream and mutex/task members. IAsyncResultCompletionHandler is temporarily an int placeholder rather than its former std::function alias. Declaration expansion is not implemented asynchronous lifecycle behavior, and ServerNetworkSystem include is supplied278.

Coverage: 8 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-277"></a>
### 277. chore: update packet ids {#commit-277}

[be5efa7689a3e93f2ee052e87d63fc01b6118b62](https://github.com/EndstoneMC/endstone/commit/be5efa7689a3e93f2ee052e87d63fc01b6118b62) · 2025-02-20T14:13:01Z · author Vincent.

Parents: `0b18d1e261f624c1888ca2ddb9cacd84406d1218`. Full message and sources: parent 1.

Renames NetworkIdentifierWithSubId fields to public id/sub_client_id and updates packet enum ItemComponent to ItemRegistry plus321/322 and End323. This adjusts protocol/native naming and IDs without independently validating transport bytes.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-278"></a>
### 278. feat: add `ServerNetworkSystem` {#commit-278}

[9f085ec467b69e62e7e1fd993324249272fda421](https://github.com/EndstoneMC/endstone/commit/9f085ec467b69e62e7e1fd993324249272fda421) · 2025-02-20T14:27:16Z · author Vincent.

Parents: `be5efa7689a3e93f2ee052e87d63fc01b6118b62`. Full message and sources: parent 1.

Adds ClientOrServerNetworkSystemRef explicit constructors and std::get accessors plus ServerNetworkSystem inheritance/declarations. Accessing the wrong variant throws; this is typed native plumbing for279 rather than evidence both client and server paths were exercised.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-279"></a>
### 279. feat: add hooks for the upcoming `DataPacketReceiveEvent` and `DataPacketSendEvent` events {#commit-279}

[9a9c47346232e9d0fca2b9b6f8164347f7340663](https://github.com/EndstoneMC/endstone/commit/9a9c47346232e9d0fca2b9b6f8164347f7340663) · 2025-02-20T18:58:18Z · author Vincent.

Parents: `9f085ec467b69e62e7e1fd993324249272fda421`. Full message and sources: parent 1.

Adds native NetEventCallback virtual interface and Windows/Linux symbols for incoming/outgoing filters. Hooks simply delegate original at this stage and identify payload buffers in TODOs. No public packet event is fired until291/293; symbol addresses are unvalidated static inputs.

Coverage: 5 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-280"></a>
### 280. feat: add getters for binary streams {#commit-280}

[b0cf8458da86714cc0e2c6ec2f1d072eb58de60b](https://github.com/EndstoneMC/endstone/commit/b0cf8458da86714cc0e2c6ec2f1d072eb58de60b) · 2025-02-20T20:38:48Z · author Vincent.

Parents: `9a9c47346232e9d0fca2b9b6f8164347f7340663`. Full message and sources: parent 1.

Exposes read stream string_view and BinaryStream buffer reference, refreshes view_ after every append so buffer reallocation does not leave the stored view stale. Views still borrow storage. Packet-hook comments identify receive buffer and send stream as sources.

Coverage: 3 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-282"></a>
### 282. refactor: update various structures {#commit-282}

[00f02fc9a1ab6d010e2b08482b2b03d19242bd68](https://github.com/EndstoneMC/endstone/commit/00f02fc9a1ab6d010e2b08482b2b03d19242bd68) · 2025-02-21T09:51:27Z · author Vincent.

Parents: `fc8bace5e2f6f53e5f008841b284dabbb0fe3f97`. Full message and sources: parent 1.

Models GameServerToken as certificate-owning wrapper with validity conversion and uses it in both connection requests, retaining raw-token validity gate. Also changes command override callback argument order/permission parameter, resource-pack source naming and removes Mob hurt_duration, all native ABI-sensitive declarations.

Coverage: 6 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-283"></a>
### 283. refactor: change ActorUniqueID from class to struct {#commit-283}

[c27509dd9e855dc509781bfbdc43d1202ba4e1ec](https://github.com/EndstoneMC/endstone/commit/c27509dd9e855dc509781bfbdc43d1202ba4e1ec) · 2025-02-21T10:37:11Z · author Vincent.

Parents: `00f02fc9a1ab6d010e2b08482b2b03d19242bd68`. Full message and sources: parent 1.

Changes ActorUniqueID class with explicit public section to struct. Access and field semantics are preserved; no independent engineering preference inferred.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-284"></a>
### 284. feat: add NetworkDefaultMaxConnections constant with value 200 {#commit-284}

[c7b48fa1637106027866d78255d7688904d5d08e](https://github.com/EndstoneMC/endstone/commit/c7b48fa1637106027866d78255d7688904d5d08e) · 2025-02-21T10:44:29Z · author Vincent.

Parents: `c27509dd9e855dc509781bfbdc43d1202ba4e1ec`. Full message and sources: parent 1.

Defines NetworkDefaultMaxConnections200 with explicit Endstone40→200 comment. The declaration alone does not change live capacity until callers use it285.

Coverage: 1 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-286"></a>
### 286. feat: add `mce::UUID::EMPTY` {#commit-286}

[8f93bfc7850e21466d8ea5647bc64a15e2339400](https://github.com/EndstoneMC/endstone/commit/8f93bfc7850e21466d8ea5647bc64a15e2339400) · 2025-02-21T11:01:00Z · author Vincent.

Parents: `4a1a7210c17735a5fe740555f890fdec6be8081e`. Full message and sources: parent 1.

Adds zero-initialized UUID default storage and mutable static UUID::EMPTY used by preceding capacity code. No special identity/security guarantee beyond all-zero sentinel.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.


<a id="commit-295"></a>
### 295. fix: boss bar now works as expected again {#commit-295}

[b7a6338257fd0732b7a11c64c096f3b38f127e7d](https://github.com/EndstoneMC/endstone/commit/b7a6338257fd0732b7a11c64c096f3b38f127e7d) · 2025-02-23T14:19:12Z · author Vincent.

Parents: `a7d190dee36bdf122b699feeea97adedae21e725`. Full message and sources: parent 1.

Changes BossEventPacket name from std::string to RedactableString and supplies construction/assignment that clear cached redacted string. Message reports boss-bar behavior restored; static mechanism is native packet layout repair, not tested rendering.

Coverage: 2 all-parent changed-file occurrences; 0 exact prior PR133 file-patch occurrences reused.
