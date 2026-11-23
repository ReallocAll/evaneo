<!-- retrieval: {"source_ids":["public:commit:061b35e9e7531f0ba435e8b45f8a384eccb1cea8","public:commit:0a8622b76d66617cfa1d2bcdf77204e8f3839512","public:commit:0b242b32405a62b69348620b4190bfef088bbe75","public:commit:0dd21f72ae0378256c30e4baa2f483299be04fca","public:commit:13306c4c1ccc01ff0664da6173e69ca93c1f63c6","public:commit:1bc60239c15cce04e70e4ace82e786fb670b45f4","public:commit:1f215e4f5285b9cd21eeba65e5d1952f923c1da9","public:commit:27781ad6823cdb5bfa49da54887efef40a30e6a8","public:commit:3f31a5464a599daf7154927b63f99f6f9bdc7dda","public:commit:3f68f70a51394d42a829537b42b606869bda54bd","public:commit:422da5db3f7b285a4ab58546480d6481e0a6c3c8","public:commit:5c79df3f7b83cd56b0d52ca1edd9ec2cd9646276","public:commit:5edcb2ea27dd86088d9cf67a816d673f095dfd93","public:commit:6b3b7433045020cf8e7016b9e0689e7917e3888d","public:commit:7216e5e5e321cf31ffb1dcd4900da4f26e377c31","public:commit:829e727ec09e3886326caba65741b1a6bf21608d","public:commit:9145c38b6f41a667c9560fc280d3615e029b0bf4","public:commit:94907f19427447f75b4e5549f3cc33d67facf057","public:commit:9e9a6b6adff77277083f88d4c4265de2a9ab8b81","public:commit:b4e6d8db528b2efad7d98b11a421b4d83717012f","public:commit:ba3a587816688696b34d8937f7f14b0210a2b4d1","public:commit:bc69947bbbc87f3d9e44a0dd20b7af2e70cfadb4","public:commit:c027ebd62529c4fc951ccd03cb64b4517b93814f","public:commit:de34d2f8549e1dc07dcaf9b03b2ff8a750b5f873","public:commit:e0046a7b07072aeff633a89ea0d332f50499a7d3","public:commit:f26275fcdfbb21786dd7193a4849ea953d879644","public:commit:fa148554ac1b4c2a98d68cee20f5b44f23438006"],"source_type":"public","date":"2024-06-04..2024-06-17","topics":["lifetime","ffi","testing","build","recovery","api","diagnosis","documentation","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Manifest-based hooks and the Minecraft 1.21 ABI port {#manifest-based-hooks-and-the-minecraft-1-21-abi-port}

## Runtime discovery is replaced with a maintained contract {#runtime-discovery-is-replaced-with-a-maintained-contract}

1101–1104 replace dependence on host debug-symbol files with a colocated TOML manifest of mangled function names and executable-relative offsets. Runtime module exports/dynamic symbols are still inspected to find Endstone's detours; the change is not elimination of every symbol table. The manifest has version/timestamp metadata, but the inspected lookup code reads only the platform integer table. Every target must have a detour because installation now iterates targets and fails when a required detour is absent. This is a meaningful inversion from the previous detour-first lookup. It makes missing implementation conspicuous but does not itself validate offsets, executable identity, table presence, duplicate names or recovery after partially installing hooks. These are bounded limitations of the exact implementation, not observed production incidents.

The changelog explicitly claims debug symbols are no longer needed at runtime. That supports a deployment motivation; a quantitative startup improvement is not measured. New dependency tomlplusplus first enters as 3.4.0 then changes to 3.3.0. No reason for that version reduction is given. The export macro becomes ENDSTONE_HOOK, aligning its name with its role; the audit proves all 25 changed files are token/whitespace-equivalent after replacement, so no fictitious new behavior is assigned to the broad rename.

The manifest permits efficient but precise review of repetitive address changes. The initial file contains 40 entries per platform. 1107 adds announcement hooks while preserving all old values; 1112 adds inventory hooks. 1125 changes representation to decimal and refreshes a timestamp but preserves all 42 addresses per platform. In contrast, 1130 changes all 84 addresses for Minecraft 1.21.0 while retaining the key sets. The death and attribute additions later add two and one functions per platform respectively, without changing older values. These parsed comparisons were recorded in the historical review; the mechanical-audit JSON is not distributed. Numeric equality is evidence for formatting equivalence, not proof that any offset is correct against a native binary.

## Porting requires both linkage and representations {#porting-requires-both-linkage-and-representations}

The 1.21 port is not merely a manifest/version bump. It removes/reorders virtual declarations in I18n, Actor, ILevel and Container, changes CommandRegistry fields/array sizes and actor offsets, and replaces complete-looking tail models/assertions with explicitly incomplete tails. This is an observed willingness to narrow what is represented instead of preserving unsupported total-layout claims. That interpretation is confined to these files, not a general philosophy of avoiding assertions. Windows component type-hash assertions remain and are added for OnGroundFlagComponent and AttributesComponent. They check compiler-generated identity, a different invariant from object size or behavior.

The EnTT change is pinned to an exact unreleased commit via CMake FetchContent, not a floating branch. Its nearby EntityRegistry offset change suggests ABI alignment as a reason, but the commit only explicitly states use of an unreleased version. Conan component dependencies are corrected next because EnTT moved providers. Endstone's local CMake still links EnTT::EnTT and sets sparse/packed page macros. No third-party EnTT source was executed or independently reviewed; no archive integrity hash or reproducible-build experiment is supplied by this patch.

Several corrective cases demonstrate why semantic resemblance is insufficient at the boundary. Ground state queries switch from a wrapped flag type to a standalone component with a distinct EnTT hash. Linux ping stops aggregate-initializing an AddressOrGUID with incomplete sentinel fields and uses constructors that explicitly establish the unused address/GUID. Ability enum widths are corrected in the companion inventory/abilities dossier. TextPacket gains an optional filtered-message field, moving subsequent members used for translation. These are native representation corrections, not cosmetic declarations.

## Seed hiding reduces layout dependence, with a narrower runtime assumption {#seed-hiding-reduces-layout-dependence-with-a-narrower-runtime-assumption}

Earlier 1051 conditionally zeroed the seed based on a late packet boolean, while 1052 adjusted the default property only for newly created configuration. 1140 removes the long modeled packet tail and LevelSettings padding/size assertion, keeping the leading seed access. It obtains client-side generation from a registered native level instead, caches that bool on first serialization and calls the original serializer after mutation. This avoids depending on a far-tail packet offset, but assumes a nonempty level list and a stable first-level setting. It does not establish per-world live configuration handling, universal secrecy or independence from native lifecycle. The previous opt-in/out configuration boundary remains relevant.

## Attribution, tests and reuse {#attribution-tests-and-reuse}

Git records Vincent as the author of this sequence. Native declarations and map offsets are project compatibility source, not proof of authorship of the underlying server mechanisms. Recurring headers and ability-header moves preserve existing declarations. No binaries were run, no hook was installed, and no performance/native compatibility result is independently measured. A declaration-only ABI change can still be substantive; 1120's Symbol::toIndex addition is one example of a substantive change with a style-oriented title.

## Commit-by-commit dispositions {#commit-by-commit-dispositions}

<a id="commit-1087"></a>
### 1087: feat: add GameSession {#commit-1087}

Source: [422da5db3f7b285a4ab58546480d6481e0a6c3c8](https://github.com/EndstoneMC/endstone/commit/422da5db3f7b285a4ab58546480d6481e0a6c3c8) · 2024-06-04T10:07:57Z · staging

Adds an empty GameSession declaration and models Minecraft ownership with unique_ptr<GameSession> at the documented offset. This establishes a place to recover server networking state, not a functioning accessor yet; includes are adjusted for the native game callbacks.

<a id="commit-1088"></a>
### 1088: feat: add Minecraft::getServerNetworkHandler {#commit-1088}

Source: [3f68f70a51394d42a829537b42b606869bda54bd](https://github.com/EndstoneMC/endstone/commit/3f68f70a51394d42a829537b42b606869bda54bd) · 2024-06-04T10:25:03Z · substantive

Models GameSession network-system/entity/handler/callback/loopback/subclient members and returns a copied NonOwnerPointer<ServerNetworkHandler>. Minecraft returns null when no session exists. NonOwnerPointer gains null/default construction and initialized shared_ptr storage; its reference constructor remains shared_ptr(&obj), so the name alone does not prove non-owning local construction. Native control-block behavior is unknown.

<a id="commit-1090"></a>
### 1090: feat: add ServerNetworkHandler::getMaxPlayers {#commit-1090}

Source: [e0046a7b07072aeff633a89ea0d332f50499a7d3](https://github.com/EndstoneMC/endstone/commit/e0046a7b07072aeff633a89ea0d332f50499a7d3) · 2024-06-04T12:29:38Z · substantive

Models max_players in ServerNetworkHandler at Windows offset 800 / Linux 664 using platform-specific padding and exposes a native getter. This is ABI groundwork; public API arrives at 1099 and friend-based access replaces the getter at 1107–1108.

<a id="commit-1101"></a>
### 1101: chore(deps): add toml++ {#commit-1101}

Source: [13306c4c1ccc01ff0664da6173e69ca93c1f63c6](https://github.com/EndstoneMC/endstone/commit/13306c4c1ccc01ff0664da6173e69ca93c1f63c6) · 2024-06-07T08:41:10Z · build_configuration

Adds tomlplusplus 3.4.0 through Conan and CMake/core linkage for the forthcoming hook manifest. It changes dependency integration, not hook lookup yet; version is reduced to 3.3.0 at 1103 without an explained reason.

<a id="commit-1102"></a>
### 1102: feat: add symbols.toml {#commit-1102}

Source: [94907f19427447f75b4e5549f3cc33d67facf057](https://github.com/EndstoneMC/endstone/commit/94907f19427447f75b4e5549f3cc33d67facf057) · 2024-06-07T10:59:58Z · substantive

Introduces a versioned/timestamped symbols.toml with 40 native function offsets for each of Windows and Linux on Minecraft 1.20.81. The entire mapping was read. These are relative addresses used by the following platform changes; accuracy against the proprietary server binary is not independently validated.

<a id="commit-1103"></a>
### 1103: feat: look up functions to hook from symbol.toml on Windows {#commit-1103}

Source: [9e9a6b6adff77277083f88d4c4265de2a9ab8b81](https://github.com/EndstoneMC/endstone/commit/9e9a6b6adff77277083f88d4c4265de2a9ab8b81) · 2024-06-07T16:29:00Z · substantive

Windows target lookup now parses the adjacent symbols.toml windows table, adds offsets to executable base and enumerates runtime exports only for names in that target map. It stops needing host executable debug-symbol enumeration. Also pins tomlplusplus to 3.3.0. The new code does not validate the manifest version/timestamp against the running binary.

<a id="commit-1104"></a>
### 1104: feat: look up functions to hook from symbol.toml on Linux {#commit-1104}

Source: [de34d2f8549e1dc07dcaf9b03b2ff8a750b5f873](https://github.com/EndstoneMC/endstone/commit/de34d2f8549e1dc07dcaf9b03b2ff8a750b5f873) · 2024-06-07T16:42:53Z · substantive

Linux similarly replaces host debug-symbol-file lookup with manifest offsets while still scanning the runtime dynamic-symbol table for matching detours. Installation now iterates required targets and throws for a missing detour, reversing the previous detour-driven target check. This makes the manifest the required hook contract; it does not prove addresses valid or provide rollback if a later installation fails.

<a id="commit-1105"></a>
### 1105: refactor: rename BEDROCK_API to ENDSTONE_HOOK {#commit-1105}

Source: [5c79df3f7b83cd56b0d52ca1edd9ec2cd9646276](https://github.com/EndstoneMC/endstone/commit/5c79df3f7b83cd56b0d52ca1edd9ec2cd9646276) · 2024-06-07T17:27:42Z · verified_mechanical

Renames BEDROCK_API to ENDSTONE_HOOK across 25 files while preserving Windows export/default-visibility behavior. Full actual patches were read and every changed file was separately verified equivalent after this token substitution plus whitespace normalization. Do not count the repeated declarations as 25 new hook decisions.

<a id="commit-1120"></a>
### 1120: style: code formatting {#commit-1120}

Source: [0dd21f72ae0378256c30e4baa2f483299be04fca](https://github.com/EndstoneMC/endstone/commit/0dd21f72ae0378256c30e4baa2f483299be04fca) · 2024-06-09T21:12:16Z · mixed_change

Although titled style, adds CommandRegistry::Symbol::toIndex, masking value_ with 0xE00FFFFF and returning uint64_t, amid alignment edits. This helper addition is retained as semantic source coverage; no use or reason beyond its implementation is inferred.

<a id="commit-1125"></a>
### 1125: chore: update symbols.toml {#commit-1125}

Source: [bc69947bbbc87f3d9e44a0dd20b7af2e70cfadb4](https://github.com/EndstoneMC/endstone/commit/bc69947bbbc87f3d9e44a0dd20b7af2e70cfadb4) · 2024-06-13T11:16:52Z · verified_mechanical

Rewrites hook offsets from hexadecimal to decimal, rearranges an entry and refreshes the timestamp. A parsed TOML comparison proves all 42 keys and numeric offsets on each platform identical and version unchanged; this is not a new ABI-address discovery.

<a id="commit-1130"></a>
### 1130: feat: update symbols.toml to support 1.21.0 {#commit-1130}

Source: [ba3a587816688696b34d8937f7f14b0210a2b4d1](https://github.com/EndstoneMC/endstone/commit/ba3a587816688696b34d8937f7f14b0210a2b4d1) · 2024-06-13T17:43:41Z · version_port

Changes manifest version to 1.21.0, timestamp and all 42 offsets on both platforms, with identical function-key sets. Complete patch and parsed-key/value audit distinguish an actual address port from 1125 formatting. Subsequent vtable/layout fixes show the manifest alone was not the complete port.

<a id="commit-1132"></a>
### 1132: feat: update CommandRegistry {#commit-1132}

Source: [f26275fcdfbb21786dd7193a4849ea953d879644](https://github.com/EndstoneMC/endstone/commit/f26275fcdfbb21786dd7193a4849ea953d879644) · 2024-06-13T17:50:18Z · version_port

Adds a CommandRegistry boolean at offset 128, shifts subsequent fields and enlarges the parameter-symbol array from 96 to 104. Removes the modeled CommandOverrideFunctor/tail size assertion in favor of an explicit incomplete tail. This narrows asserted ABI knowledge rather than proving a complete class layout.

<a id="commit-1133"></a>
### 1133: fix: I18n virtual table {#commit-1133}

Source: [b4e6d8db528b2efad7d98b11a421b4d83717012f](https://github.com/EndstoneMC/endstone/commit/b4e6d8db528b2efad7d98b11a421b4d83717012f) · 2024-06-13T17:55:08Z · version_port

Removes the Localization-reference chooseLanguage virtual overload from I18n while retaining the string overload. In a host ABI model, removing a virtual declaration changes subsequent slot interpretation; no host execution verifies the corrected table here.

<a id="commit-1135"></a>
### 1135: chore(deps): use the unreleased version of EnTT {#commit-1135}

Source: [3f31a5464a599daf7154927b63f99f6f9bdc7dda](https://github.com/EndstoneMC/endstone/commit/3f31a5464a599daf7154927b63f99f6f9bdc7dda) · 2024-06-13T23:43:34Z · version_port

Moves EnTT acquisition from Conan's released 3.13.0 to CMake FetchContent pinned to exact commit 41aab920b083aa424ac1d27666ce287eeaff6ceb and adjusts EntityRegistry id offset 336 to 352. The source explicitly seeks an unreleased EnTT revision; host-layout matching is a reasonable inference, not an explicit explanation. The URL is SHA-pinned but has no archive URLHASH.

<a id="commit-1136"></a>
### 1136: fix: conan errors {#commit-1136}

Source: [0a8622b76d66617cfa1d2bcdf77204e8f3839512](https://github.com/EndstoneMC/endstone/commit/0a8622b76d66617cfa1d2bcdf77204e8f3839512) · 2024-06-13T23:50:39Z · corrective

Comments EnTT out of Conan component requirements after 1135 moved its provider to CMake, addressing the stated Conan errors. The target still links EnTT::EnTT. No dependency build was executed; dependency implementation was not independently audited.

<a id="commit-1137"></a>
### 1137: feat: update Actor and ILevel class {#commit-1137}

Source: [27781ad6823cdb5bfa49da54887efef40a30e6a8](https://github.com/EndstoneMC/endstone/commit/27781ad6823cdb5bfa49da54887efef40a30e6a8) · 2024-06-14T00:41:06Z · version_port

Updates Actor virtual slots, armor texture accessor and data layout, shrinking an opaque region and shifting dimension/level/components by eight bytes. Removes a trailing modeled member in favor of an incomplete tail. ILevel also removes a virtual slot and renames internal virtuals. This is targeted ABI adaptation, not a general actor ownership redesign.

<a id="commit-1138"></a>
### 1138: feat: update Container class {#commit-1138}

Source: [829e727ec09e3886326caba65741b1a6bf21608d](https://github.com/EndstoneMC/endstone/commit/829e727ec09e3886326caba65741b1a6bf21608d) · 2024-06-14T00:47:12Z · version_port

Adds Container removed-listener registration/removal and containerRemoved virtuals. The previously implemented inventory getters depend on correct later vtable positions, so this is functional ABI work despite declaration-only changes.

<a id="commit-1139"></a>
### 1139: fix: Actor::isOnGround {#commit-1139}

Source: [1bc60239c15cce04e70e4ace82e786fb670b45f4](https://github.com/EndstoneMC/endstone/commit/1bc60239c15cce04e70e4ace82e786fb670b45f4) · 2024-06-14T15:02:39Z · corrective

Fixes isOnGround by querying the standalone OnGroundFlagComponent rather than FlagComponent<OnGroundFlag>, with a Windows EnTT type-hash assertion. Same-looking semantic names are not interchangeable component identities; the assert checks the compiler-derived type key, not live collision behavior.

<a id="commit-1140"></a>
### 1140: fix: hiding seeds from the client {#commit-1140}

Source: [c027ebd62529c4fc951ccd03cb64b4517b93814f](https://github.com/EndstoneMC/endstone/commit/c027ebd62529c4fc951ccd03cb64b4517b93814f) · 2024-06-14T15:37:07Z · corrective

Replaces a fragile late StartGamePacket client-generation field read with a one-time query of the first registered native level's isClientSideGenerationEnabled. Removes most packet/LevelSettings padding and size assumptions, preserving the leading mutable seed field. When cached false, serialization still zeroes the seed before calling original. It assumes a level exists and caches one setting for process lifetime, not arbitrary per-level dynamic policy.

<a id="commit-1141"></a>
### 1141: feat: update ActorType {#commit-1141}

Source: [1f215e4f5285b9cd21eeba65e5d1952f923c1da9](https://github.com/EndstoneMC/endstone/commit/1f215e4f5285b9cd21eeba65e5d1952f923c1da9) · 2024-06-14T16:03:51Z · version_port

Adds native ActorType::OminousItemSpawner value 145. A bounded enum update; no plugin behavior is implemented by this declaration alone.

<a id="commit-1142"></a>
### 1142: feat: update CommandRegistry::HardNonTerminal {#commit-1142}

Source: [7216e5e5e321cf31ffb1dcd4900da4f26e377c31](https://github.com/EndstoneMC/endstone/commit/7216e5e5e321cf31ffb1dcd4900da4f26e377c31) · 2024-06-14T16:06:35Z · version_port

Adds four CodeBuilder HardNonTerminal values 0x100058–0x10005b. Actual constants were read; no broader parser design conclusion.

<a id="commit-1143"></a>
### 1143: feat: update Connection::DisconnectFailReason {#commit-1143}

Source: [9145c38b6f41a667c9560fc280d3615e029b0bf4](https://github.com/EndstoneMC/endstone/commit/9145c38b6f41a667c9560fc280d3615e029b0bf4) · 2024-06-14T16:06:51Z · version_port

Renames disconnect reason 89 to RealmsSessionNotFound_DEPRECATED without changing its numeric value. Compatibility naming maintenance only.

<a id="commit-1144"></a>
### 1144: fix: Player::getPing now returns the correct value on Linux {#commit-1144}

Source: [0b242b32405a62b69348620b4190bfef088bbe75](https://github.com/EndstoneMC/endstone/commit/0b242b32405a62b69348620b4190bfef088bbe75) · 2024-06-14T17:30:48Z · corrective

Fixes the stated Linux ping=-1 behavior by constructing AddressOrGUID explicitly from the network GUID. Adds valid unassigned GUID/address initialization, address family/default system indices, missing SystemAddress system_index and conversion/assignment overloads. This replaces aggregate initialization with a complete tagged-by-sentinel host argument; no measured ping experiment was run.

<a id="commit-1145"></a>
### 1145: refactor: rename member in CommandRegistry {#commit-1145}

Source: [5edcb2ea27dd86088d9cf67a816d673f095dfd93](https://github.com/EndstoneMC/endstone/commit/5edcb2ea27dd86088d9cf67a816d673f095dfd93) · 2024-06-14T17:44:11Z · mechanical

Names CommandRegistry's previously unknown boolean edu_mode at the same offset. No layout/behavior change beyond improved native-model meaning.

<a id="commit-1146"></a>
### 1146: refactor: move abilities to world/actor/player {#commit-1146}

Source: [6b3b7433045020cf8e7016b9e0689e7917e3888d](https://github.com/EndstoneMC/endstone/commit/6b3b7433045020cf8e7016b9e0689e7917e3888d) · 2024-06-14T22:08:53Z · verified_mechanical

Moves ability headers one directory upward and fixes dependent include paths; four files are exact blob moves, layered_abilities only changes includes. Actual rename-aware diffs and blob identities retain every path without treating relocation as new algorithms.

<a id="commit-1169"></a>
### 1169: feat: update MinecraftPacketIds {#commit-1169}

Source: [061b35e9e7531f0ba435e8b45f8a384eccb1cea8](https://github.com/EndstoneMC/endstone/commit/061b35e9e7531f0ba435e8b45f8a384eccb1cea8) · 2024-06-16T23:36:43Z · substantive

Expands MinecraftPacketIds from Text only to a comprehensive explicit native ID table including UpdateAbilitiesPacket=187 and later IDs through 310. Entire table read; it enables typed packet construction but is declarative protocol data, not 210 independent architectural choices.

<a id="commit-1179"></a>
### 1179: feat: update TextPacket {#commit-1179}

Source: [fa148554ac1b4c2a98d68cee20f5b44f23438006](https://github.com/EndstoneMC/endstone/commit/fa148554ac1b4c2a98d68cee20f5b44f23438006) · 2024-06-17T12:53:14Z · version_port

Adds optional filtered_message to native TextPacket and shifts following parameters/localization/identity offsets. Translation packet use at 1186 depends on this representation; the old total-size assertion remains commented out.
