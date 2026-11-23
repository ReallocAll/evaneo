<!-- retrieval: {"source_ids":["public:commit:046ac50bffa0ea09c821190a95a22ddb8f689417","public:commit:067950ee00855a64a420edc4e0d5c7f0704a3f95","public:commit:08fb7b37cf3d890d5d8be269f8c64b8de6f6dab7","public:commit:0d1b30ccd92592ce5d0ad3763a02d7a6e25ef5fa","public:commit:0fd56515195055e401d4f48521293d359821169f","public:commit:15fe809e9df981262e931776fdc6a14ed8b99734","public:commit:181c6f7f85f49b208e68a6064747089c1d04fd6d","public:commit:1eafb1f25c39682a01601842a23d2163bd1dbfd5","public:commit:1f2d470734c71a217c531e96bbe3a46b237c7b86","public:commit:20cea31e6dc990f678ba227b163f3fd972a61f9b","public:commit:46dd28d15b7350a2333bf1987f7de2e6c6dabe3a","public:commit:4d353fc40d6d42acef342da456660a450f05c0ef","public:commit:5e2844de64ef1a7845793a9c66e8e96b5b10d464","public:commit:5f7ad3b55de02b9ce7e071c73dc37d917a984bf0","public:commit:71ccecac6ca809679b085f4515e7fb66025c16f2","public:commit:7e12102d3723e5538005184f7fb5bdacec73ede5","public:commit:812ab167e0b97edf22a8dd496e4ff9912616f6d3","public:commit:88b94c54b29e7ddda82042d2feb1a1f105412d8a","public:commit:90aaa172fd3f4bb17d52d555d34d0efa3fb403ca","public:commit:abb1a2f8211fdfb4444b31421307ce08adedeb7d","public:commit:b1da10564832b078e4442aa11165199c85dd1075","public:commit:b926e752fc66361d678dc2552b0af622c28d7887","public:commit:bc6aa9f78d9c18c25bad043bc1eb8275e80a36b4","public:commit:c80b4608079536ec56538a576daf5f593c02dfa9","public:commit:cb301918dabe259ab3e67cf3d735d2d2b5631bb1","public:commit:cd2b9fd8cd7048921d4fae327e2f252d5118b53d","public:commit:e12f39c7cd46a86e6260ba3c3a94ab24fefce76e","public:commit:e489af1f4f93cff468398b793cb29e1c0bb97369","public:commit:e8701263fe6ce3a352ce6da717819f4073bb0a6a","public:commit:ec37ef85f8b2c3258463046c117457f90f52539d","public:commit:f379cf857ecdc7b7e29067e5fad24950b175fabf","public:commit:f50eb8fcad975aa0e1431558e6f37252d72bd3ca","public:commit:fbd4a5068ace7c76b16bc58258cd56452b7422b2"],"source_type":"public","date":"2024-01-27..2024-03-04","topics":["lifetime","ffi","testing","build","api","diagnosis","documentation","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Native ABI, hook forwarding and reverse-engineered command structures {#native-abi-hook-forwarding-and-reverse-engineered-command-structures}

## Result and constraints {#result-and-constraints}

This unit builds a Bedrock command bridge against native host structures and symbols. C++ STL types, vtables, member-function pointers, hidden return parameters and platform offsets are part of the contract. Exported entry-point names or sizeof assertions alone cannot prove compatibility. The history contains immediate compile repairs, Linux/Windows divergence and changed assumptions that should remain visible rather than flattened into a polished final design.

## Hidden return and function-pointer evolution {#hidden-return-and-function-pointer-evolution}

142 adds const-member casts and removes macro semicolons;144 repairs call sites.151 routes RVO calls to a dedicated return-buffer adapter and caches host-generated type IDs.153 replaces that discovery with hardcoded uint16 IDs and explicitly notes they must be updated with the game.155 replaces std::function target extraction with union overlays. This reduces machinery but does not make member pointers equivalent to void pointers under the C++ language model, especially for larger representations, virtual functions or multiple inheritance.

156, titled as a Linux RVO crash fix, distinguishes Windows member-call argument order (this then return buffer) from Linux (return buffer then this), with a uniform C++ wrapper. No crash trace or passing runtime result accompanies the source.199 move-assigns the result from the returned pointer, supporting move-only values but potentially self-moving the same supplied storage.228 removes that assignment so host writes into the provided object. Although228 names Linux, its macro is shared. The endpoint still assumes the host uses the expected hidden-return convention and returned pointer, and that supplied result storage satisfies construction/lifetime requirements. Those are ABI constraints requiring host/compiler-specific tests, not portable C++ guarantees.

## Command layout and parser metadata {#command-layout-and-parser-metadata}

146 introduces Command, Registry, Signature and Overload models.149 renames fields but also removes the virtual destructor;150 restores it. That transient vtable change is not cosmetic even if total object size appears unchanged.152 models parameter layout and parse-member pointers.153 observes host registerOverloadInternal calls to capture templates, then uses hardcoded type IDs and terminates if a template is absent. This introduces registration-order dependence as well as game-version dependence.160 calculates parameter storage offsets via member-pointer representation and assumes std::optional engagement follows sizeof(T), citing particular library implementations. Those comments establish the basis of an assumption, not a portable layout contract.

The runtime test command added147 is an experiment embedded in the shipped runtime, not an asserted test suite.154 enables more overloads even though its title mentions README.160 supplies member storage and prints values.168 removes the demonstration before release. Therefore the narrative is exploration → layout/parameter experiments → removal, not evidence that a production general-purpose parser had been validated.

188 supplies ParseToken child/next/parent/data fields and sizeof40.201 adds parse-tree diagnostics and native createCommand forwarding, removes prior parameter builders and makes fields public. Acyclic structure and valid borrowed text are assumed by the traversal.202 moves remaining hardcoded type IDs into header specializations; include-order/name lookup and removed-source comments deserve care.230 expands Registry with command/alias maps, callback fields and unknown placeholders.231 revises Linux padding immediately. Offset comments and placeholder arrays are reverse-engineering notes, not measured verification in this review.

## Pointer fields and cross-platform repairs {#pointer-fields-and-cross-platform-repairs}

207 and211 add Minecraft/ServerInstance access through platform-specific word offsets. Initially they treat the address of a stored pointer as the target object.214 repairs both by loading the pointer and dereferencing it. The corrected indirection is concrete and important; it still assumes object existence, exact offset, pointer width and host version. No null/bounds/version gate is introduced. MinecraftCommands size24 checks only one aggregate size, not the validity of every member offset or subsystem startup timing.

The rename chains also show platform omissions:156 moves hook namespace but Linux definition follows157;187 moves public/private namespaces but Linux os definition follows208.217 combines command-output headers while219 fixes a stale include.203 removes a redundant qualified declaration from201. These changes should be retained as separate source identities with intermediate-state limitations, not silently treated as one all-at-once working patch.

## Host registration and output symbols {#host-registration-and-output-symbols}

Native registerOverload appends a copy into the signature but calls the native routine with a local overload object; if the host retains or mutates that object, lifetime/consistency needs verification. Pointers returned into a vector also invalidate on growth.212 adds alias forwarding,217 native command-name lookup,232 translation and234 overload-description forwarding with explicit typed member-function pointers to disambiguate overloads. Unknown trailing native arguments remain unexplained parameters. These wrappers add access, not evidence of complete semantics.

225/226 output work, discussed in the command dossier, changes from hooking apparent public forceOutput/error wrappers to hooking private addMessage and reproducing simple gating locally. This illustrates symbol-availability and inline-wrapper constraints in native interop. Calling a host function by a signature-shaped cast is only correct under the matching platform ABI; a static wrapper or successful compile would not alone settle it.

## How to use this evidence {#how-to-use-this-evidence}

Use these commits to audit native boundaries, determine which values are measured versus guessed, track per-platform fixes and design version-specific regression matrices. Useful tests would exercise hidden returns for strings and move-only objects, const and nonconst members, parser absence/ordering, optional presence, multiple overload growth and pointer offsets against real supported hosts. This unit supplies source reasoning and counterexamples, not those test outcomes. Distinguish inferred host reconstruction from Endstone-owned API design, and preserve unknown fields/causes instead of inventing rationale.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-142"></a>
### 142. feat: add fp_cast for const class method {#commit-142}

[f50eb8fcad975aa0e1431558e6f37252d72bd3ca](https://github.com/EndstoneMC/endstone/commit/f50eb8fcad975aa0e1431558e6f37252d72bd3ca) · 2024-01-27T03:00:37Z · meaningful

Adds const-member fp_cast and removes trailing semicolons from invocation macros. Uses std::function target storage and reinterpretation as before, retaining member-pointer representation assumptions; const overload uses Class* in callable signature although member itself is const. Macro call sites need semicolons, repaired144. RVO macro still points to ordinary forwarding until151.

Changed paths: `endstone_runtime/include/endstone_runtime/hook.h`.

<a id="commit-144"></a>
### 144. refactor: code cleanup {#commit-144}

[08fb7b37cf3d890d5d8be269f8c64b8de6f6dab7](https://github.com/EndstoneMC/endstone/commit/08fb7b37cf3d890d5d8be269f8c64b8de6f6dab7) · 2024-01-27T03:46:40Z · small-semantic

Moves dedicated/server-instance headers to bedrock/server with exact content reuse, updates includes and adds required semicolons after142's macro change. Constructor preprocessor test changes from GNU-or-Clang definition check to numeric __GNUC__. This is path/compile coordination, not a wholly cosmetic rename.

Changed paths: `endstone_api/include/bedrock/dedicated_server.h`, `endstone_api/include/bedrock/server/dedicated_server.h`, `endstone_api/include/bedrock/server/server_instance.h`, `endstone_api/include/bedrock/server_instance.h`, `endstone_runtime/src/bedrock/dedicated_server.cpp`, `endstone_runtime/src/bedrock/server_instance.cpp`, `endstone_runtime/src/endstone_runtime/main.cpp`.

<a id="commit-146"></a>
### 146. feat: add headers for command-related classes {#commit-146}

[71ccecac6ca809679b085f4515e7fb66025c16f2](https://github.com/EndstoneMC/endstone/commit/71ccecac6ca809679b085f4515e7fb66025c16f2) · 2024-01-27T03:47:33Z · meaningful

Introduces reverse-engineered Command/Registry/Signature/Overload layouts, permission/flag/version structures and forwarding hooks. Command has sizeof32 assertion, but most host offsets/unknown fields lack runtime verification. registerOverload const_casts signature, pushes an overload copy then passes the local object to host registration; returned vector element and registered local may diverge if mutated. Parameter packs are explicitly ignored initially. Raw pointers to vector entries can invalidate on growth. No native integration test supplied.

Changed paths: `endstone_api/include/bedrock/command/command.h`, `endstone_api/include/bedrock/command/command_parameter_data.h`, `endstone_api/include/bedrock/command/command_registry.h`, `endstone_api/include/bedrock/command/command_version.h`, `endstone_runtime/src/bedrock/command_registry.cpp`.

<a id="commit-147"></a>
### 147. feat: hook StopCommand::setup to registrate a custom test command {#commit-147}

[0d1b30ccd92592ce5d0ad3763a02d7a6e25ef5fa](https://github.com/EndstoneMC/endstone/commit/0d1b30ccd92592ce5d0ad3763a02d7a6e25ef5fa) · 2024-01-27T03:47:55Z · meaningful

Hooks StopCommand::setup after original registration to add an unrestricted test command whose execute prints to stdout. Demonstration is embedded in runtime, not a test harness or asserted test. Header includes redundant StopCommand:: qualification, fixed148. Host registry behavior remains inferred from code rather than observed.

Changed paths: `endstone_api/include/bedrock/command/stop_command.h`, `endstone_runtime/src/bedrock/stop_command.cpp`.

<a id="commit-148"></a>
### 148. fix: remove duplicate qualification on function `setup` {#commit-148}

[5f7ad3b55de02b9ce7e071c73dc37d917a984bf0](https://github.com/EndstoneMC/endstone/commit/5f7ad3b55de02b9ce7e071c73dc37d917a984bf0) · 2024-01-27T11:03:20Z · small-semantic

Removes redundant class qualification on in-class static setup declaration. Exact compile fix for147, not a behavior feature.

Changed paths: `endstone_api/include/bedrock/command/stop_command.h`.

<a id="commit-149"></a>
### 149. refactor: rename members of class Command {#commit-149}

[88b94c54b29e7ddda82042d2feb1a1f105412d8a](https://github.com/EndstoneMC/endstone/commit/88b94c54b29e7ddda82042d2feb1a1f105412d8a) · 2024-01-27T11:41:24Z · meaningful

Names previously unknown Command fields as registry pointer, signed symbol, permission and flags; changes flag initialization and removes virtual destructor while introducing header/forward-declaration changes. Title says rename, but vtable shape and polymorphic destruction change materially.150 immediately restores virtual destructor. Layout size alone cannot establish correct host vtable ABI.

Changed paths: `endstone_api/include/bedrock/command/command.h`, `endstone_api/include/bedrock/command/command_registry.h`.

<a id="commit-150"></a>
### 150. feat: add CommandOrigin {#commit-150}

[46dd28d15b7350a2333bf1987f7de2e6c6dabe3a](https://github.com/EndstoneMC/endstone/commit/46dd28d15b7350a2333bf1987f7de2e6c6dabe3a) · 2024-01-27T11:48:09Z · meaningful

Adds minimal CommandOrigin with virtual destructor and UUID field plus four-int UUID representation; restores Command's virtual destructor removed149. New class is skeletal host layout, not a complete command-origin interface or verified reconstruction.

Changed paths: `endstone_api/include/bedrock/command/command.h`, `endstone_api/include/bedrock/command/command_origin.h`, `endstone_api/include/bedrock/uuid.h`.

<a id="commit-151"></a>
### 151. feat: add Bedrock::type_id support {#commit-151}

[e489af1f4f93cff468398b793cb29e1c0bb97369](https://github.com/EndstoneMC/endstone/commit/e489af1f4f93cff468398b793cb29e1c0bb97369) · 2024-01-27T14:07:09Z · meaningful

Adds Bedrock type-id wrapper/template specializations that call original functions through cached RVO results, with comment that per-specialization lambda ensures distinct instantiations. Finally routes RVO macro to get_original_rvo and adds free-function return-buffer adapter. Runtime demo prints repeated IDs for several types. No assertions validate IDs or cross-platform return conventions;153 replaces this approach.

Changed paths: `endstone_api/include/bedrock/command/command_registry.h`, `endstone_api/include/bedrock/type_id.h`, `endstone_runtime/include/endstone_runtime/hook.h`, `endstone_runtime/src/bedrock/stop_command.cpp`, `endstone_runtime/src/bedrock/type_id.cpp`.

<a id="commit-152"></a>
### 152. feat: add CommandParameterData {#commit-152}

[90aaa172fd3f4bb17d52d555d34d0efa3fb403ca](https://github.com/EndstoneMC/endstone/commit/90aaa172fd3f4bb17d52d555d34d0efa3fb403ca) · 2024-01-28T17:08:33Z · meaningful

Replaces placeholder parameter struct with detailed CommandParameterData fields, member-function ParseRule, constructor and default-invalid Symbol. Offset comments expose expected host layout, but member-pointer/std::string sizes vary by ABI and no size/offset tests accompany it. Some enum/option state remains uninitialized. This is foundation for capturing host parser metadata, not full parameter support yet.

Changed paths: `endstone_api/include/bedrock/command/command.h`, `endstone_api/include/bedrock/command/command_parameter_data.h`, `endstone_api/include/bedrock/command/command_registry.h`.

<a id="commit-153"></a>
### 153. feat: fix type_id on Linux, add param support {#commit-153}

[0fd56515195055e401d4f48521293d359821169f](https://github.com/EndstoneMC/endstone/commit/0fd56515195055e401d4f48521293d359821169f) · 2024-01-29T17:16:56Z · meaningful

Changes type ID to uint16 and replaces original-function lookup with hardcoded IDs for string/bool/int/float/unique command, explicitly requiring updates after game updates. Captures type/parser templates from host registerOverloadInternal and creates new parameter data from them; absent template terminates process. Overload parameter packs become active. Adds describe RVO forwarding and a sample text argument, but offsets are initially zero. This trades dynamic lookup for version-sensitive constants and registration-order dependence; no actual-host run is demonstrated.

Changed paths: `endstone_api/include/bedrock/command/command_registry.h`, `endstone_api/include/bedrock/type_id.h`, `endstone_runtime/src/bedrock/command_registry.cpp`, `endstone_runtime/src/bedrock/stop_command.cpp`, `endstone_runtime/src/bedrock/type_id.cpp`.

<a id="commit-154"></a>
### 154. feat: update README.md {#commit-154}

[abb1a2f8211fdfb4444b31421307ce08adedeb7d](https://github.com/EndstoneMC/endstone/commit/abb1a2f8211fdfb4444b31421307ce08adedeb7d) · 2024-01-29T17:32:15Z · meaningful

Despite README title, enables float optional and integer required overload experiments and removes registry printf diagnostics. Documentation gains UDP forwarding for DockerHub example; GHCR example remains incomplete until159. Parameter demo still lacks storage offsets until160, so title must not replace diff review.

Changed paths: `README.md`, `endstone_runtime/src/bedrock/command_registry.cpp`, `endstone_runtime/src/bedrock/stop_command.cpp`.

<a id="commit-155"></a>
### 155. refactor: fp_cast function {#commit-155}

[bc6aa9f78d9c18c25bad043bc1eb8275e80a36b4](https://github.com/EndstoneMC/endstone/commit/bc6aa9f78d9c18c25bad043bc1eb8275e80a36b4) · 2024-01-29T22:42:05Z · meaningful

Replaces std::function-target extraction in function/member-pointer casts with unions overlaying pointer representation and void*. Simplifies implementation but retains platform-specific/nonportable assumptions, including larger member-function pointers and inactive-union-member access. No tests prove general virtual/multiple-inheritance applicability.

Changed paths: `endstone_runtime/include/endstone_runtime/hook.h`.

<a id="commit-156"></a>
### 156. fix: crash when calling rvo functions on linux {#commit-156}

[1f2d470734c71a217c531e96bbe3a46b237c7b86](https://github.com/EndstoneMC/endstone/commit/1f2d470734c71a217c531e96bbe3a46b237c7b86) · 2024-01-29T23:11:08Z · meaningful

Title reports Linux RVO crash. Implementation distinguishes Windows member-call order (this then return-buffer) from Linux (return-buffer then this), gives adapters uniform caller signature and updates describe. Renames internals namespace to detail and documents helpers; Linux implementation namespace is missed until157. This is concrete ABI-sensitive repair, not evidence that generic C++ return semantics permit arbitrary casts. No crash trace or passing regression supplied.

Changed paths: `endstone_runtime/include/endstone_runtime/hook.h`, `endstone_runtime/src/bedrock/command_registry.cpp`, `endstone_runtime/src/endstone_runtime/windows/hook.cpp`.

<a id="commit-157"></a>
### 157. fix: namespace in linux-specific code {#commit-157}

[7e12102d3723e5538005184f7fb5bdacec73ede5](https://github.com/EndstoneMC/endstone/commit/7e12102d3723e5538005184f7fb5bdacec73ede5) · 2024-01-29T23:18:37Z · small-semantic

Updates Linux get_original namespace to detail after156 changed declarations/Windows, repairing cross-platform linkage mismatch. No broader behavior change.

Changed paths: `endstone_runtime/src/endstone_runtime/linux/hook.cpp`.

<a id="commit-160"></a>
### 160. feat: add support for optional parameters {#commit-160}

[181c6f7f85f49b208e68a6064747089c1d04fd6d](https://github.com/EndstoneMC/endstone/commit/181c6f7f85f49b208e68a6064747089c1d04fd6d) · 2024-01-30T03:17:00Z · meaningful

Builds parameter metadata from command member pointers and storage offsets, with a separate std::optional overload assuming engagement flag immediately after sizeof(Type). Inline links cite particular LLVM/Microsoft implementations, but this is an explicit layout assumption, not portable std::optional guarantee. Pointer-to-member is overlaid with uint32, imposing representation/offset constraints. Runtime demo gains string/int/optional-float fields and logs values; unselected scalar int can remain uninitialized. Host parsing writes into command storage; no layout/absence/type matrix test is added.

Changed paths: `endstone_api/include/bedrock/command/command_registry.h`, `endstone_runtime/src/bedrock/command_registry.cpp`, `endstone_runtime/src/bedrock/stop_command.cpp`.

<a id="commit-168"></a>
### 168. chore: prepare for release {#commit-168}

[e12f39c7cd46a86e6260ba3c3a94ab24fefce76e](https://github.com/EndstoneMC/endstone/commit/e12f39c7cd46a86e6260ba3c3a94ab24fefce76e) · 2024-01-30T11:36:30Z · meaningful

Removes StopCommand shim and embedded test/testo command implementation before release. Retains command scaffolding elsewhere while eliminating demonstration commands from shipped runtime. Exact known code deletion, not a new test suite; absence of production command API remains distinct.

Changed paths: `include/bedrock/command/stop_command.h`, `src/endstone_runtime/bedrock/stop_command.cpp`.

<a id="commit-188"></a>
### 188. feat: add CommandRegistry::ParseToken {#commit-188}

[4d353fc40d6d42acef342da456660a450f05c0ef](https://github.com/EndstoneMC/endstone/commit/4d353fc40d6d42acef342da456660a450f05c0ef) · 2024-02-09T00:52:12Z · meaningful

Defines host ParseToken tree/list links, borrowed parent/data, size and Symbol with sizeof40 assertion; annotates overload offsets. Clarifies parse representation for later command adapters. Size assertion checks one dimension only; pointer lifetime, offsets and live-host parsing remain untested.

Changed paths: `include/bedrock/command/command_registry.h`.

<a id="commit-198"></a>
### 198. refactor: corrected a typo in the include path {#commit-198}

[812ab167e0b97edf22a8dd496e4ff9912616f6d3](https://github.com/EndstoneMC/endstone/commit/812ab167e0b97edf22a8dd496e4ff9912616f6d3) · 2024-03-02T19:30:04Z · mechanical

Corrects a doubled slash in the relocated detail/bedrock.h include. One-path spelling cleanup; no independent architectural conclusion.

Changed paths: `src/endstone_core/spdlog/text_formatter.cpp`.

<a id="commit-199"></a>
### 199. fix: apply std::move to return value in ENDSTONE_HOOK_CALL_ORIGINAL_RVO macro {#commit-199}

[15fe809e9df981262e931776fdc6a14ed8b99734](https://github.com/EndstoneMC/endstone/commit/15fe809e9df981262e931776fdc6a14ed8b99734) · 2024-03-03T01:13:19Z · meaningful

Changes the RVO call macro to move-assign from the returned pointer, allowing move-only return values such as unique_ptr. If the native function returns the supplied result-storage pointer, this becomes self-move assignment; 228 later removes the assignment. A compile-enabling change is not itself evidence of correct hidden-return ABI semantics.

Changed paths: `include/endstone/detail/hook.h`.

<a id="commit-200"></a>
### 200. refactor: rename variable in class Command {#commit-200}

[1eafb1f25c39682a01601842a23d2163bd1dbfd5](https://github.com/EndstoneMC/endstone/commit/1eafb1f25c39682a01601842a23d2163bd1dbfd5) · 2024-03-03T01:13:59Z · mechanical

Renames the unknown int32_t field in the native Command layout to int version_, retaining zero initialization and the existing size assertion. This records inferred field meaning; int width still relies on supported platform ABI.

Changed paths: `include/bedrock/command/command.h`.

<a id="commit-201"></a>
### 201. refactor: clean up codes {#commit-201}

[20cea31e6dc990f678ba227b163f3fd972a61f9b](https://github.com/EndstoneMC/endstone/commit/20cea31e6dc990f678ba227b163f3fd972a61f9b) · 2024-03-03T11:36:15Z · meaningful

Despite the cleanup title, removes CommandParameterData factories/accessors and exposes its layout fields directly; adds hooked createCommand returning unique_ptr through the RVO bridge. Diagnostic traversal prints ParseToken child/next trees and parameter descriptions to help update IDs. Traversal assumes trusted acyclic host structures and valid text lengths. Adds a formatter after code that uses it and a redundant qualified declaration repaired at203; no compilation or host parsing outcome is supplied.

Changed paths: `.clang-format`, `include/bedrock/command/command_registry.h`, `src/endstone_runtime/bedrock/command_registry.cpp`.

<a id="commit-202"></a>
### 202. refactor: move type_id definitions to header and remove type_id.cpp {#commit-202}

[b1da10564832b078e4442aa11165199c85dd1075](https://github.com/EndstoneMC/endstone/commit/b1da10564832b078e4442aa11165199c85dd1075) · 2024-03-03T12:13:32Z · meaningful

Moves hardcoded native type IDs into inline header specializations, removes BEDROCK_API exports and drops unique_ptr<Command> ID7, retaining string1/bool2/int5/float6. The header relies on transitive string declaration and an elaborated CommandRegistry name inside namespace Bedrock; standalone/include-order lookup merits checking rather than assuming this is purely linkage-neutral. The update-guidance comment elsewhere still points to the deleted source file.

Changed paths: `include/bedrock/type_id.h`, `src/endstone_runtime/bedrock/command_registry.cpp`, `src/endstone_runtime/bedrock/type_id.cpp`.

<a id="commit-203"></a>
### 203. fix: remove redundant scope from createCommand function {#commit-203}

[fbd4a5068ace7c76b16bc58258cd56452b7422b2](https://github.com/EndstoneMC/endstone/commit/fbd4a5068ace7c76b16bc58258cd56452b7422b2) · 2024-03-03T12:14:34Z · mechanical

Removes redundant CommandRegistry:: qualification from createCommand inside its own class declaration, repairing the immediately preceding declaration. No behavioral feature or test is added.

Changed paths: `include/bedrock/command/command_registry.h`.

<a id="commit-207"></a>
### 207. feat: add MinecraftCommands class {#commit-207}

[c80b4608079536ec56538a576daf5f593c02dfa9](https://github.com/EndstoneMC/endstone/commit/c80b4608079536ec56538a576daf5f593c02dfa9) · 2024-03-03T16:45:46Z · meaningful

Adds MinecraftCommands with virtual destructor, owned output-sender/registry pointers, getters and size24 assertion, plus Minecraft and ServerInstance access. getCommands uses platform-specific word offsets22/23 but initially interprets the pointer-field address as a MinecraftCommands object; 214 adds the missing dereference. Reverse-engineered offsets remain version/compiler/architecture assumptions.

Changed paths: `include/bedrock/command/command_output_sender.h`, `include/bedrock/command/minecraft_commands.h`, `include/bedrock/minecraft.h`, `include/bedrock/server/dedicated_server.h`, `src/endstone_runtime/bedrock/minecraft.cpp`.

<a id="commit-208"></a>
### 208. fix: 'endstone::os' namespace to 'endstone::detail::os' {#commit-208}

[ec37ef85f8b2c3258463046c117457f90f52539d](https://github.com/EndstoneMC/endstone/commit/ec37ef85f8b2c3258463046c117457f90f52539d) · 2024-03-03T17:09:52Z · mechanical

Corrects Linux OS helper namespace to endstone::detail::os after187 namespace migration. This is a concrete missed platform branch, not proof the original relocation was behavior-neutral or fully built.

Changed paths: `src/endstone_runtime/linux/os.cpp`.

<a id="commit-210"></a>
### 210. feat: add `getCommand` to expose private `findCommand` method {#commit-210}

[5e2844de64ef1a7845793a9c66e8e96b5b10d464](https://github.com/EndstoneMC/endstone/commit/5e2844de64ef1a7845793a9c66e8e96b5b10d464) · 2024-03-03T17:28:21Z · meaningful

Adds a public CommandRegistry getCommand wrapper over private findCommand. It temporarily exposes signature lookup for core registration, then is removed at212; short-lived API step rather than a durable design preference.

Changed paths: `include/bedrock/command/command_registry.h`.

<a id="commit-212"></a>
### 212. feat: add registerAlias method to CommandRegistry {#commit-212}

[046ac50bffa0ea09c821190a95a22ddb8f689417](https://github.com/EndstoneMC/endstone/commit/046ac50bffa0ea09c821190a95a22ddb8f689417) · 2024-03-03T17:46:01Z · meaningful

Adds hooked registerAlias forwarding with moved string arguments and removes the short-lived getCommand wrapper. Core call sites are repaired in213, making this an intermediate mismatch. Existing overload registration still appends a copy to the signature then passes the local overload to native registration; retention assumptions remain untested.

Changed paths: `include/bedrock/command/command_registry.h`, `src/endstone_runtime/bedrock/command_registry.cpp`.

<a id="commit-214"></a>
### 214. fix: getMinecraft and getCommands {#commit-214}

[b926e752fc66361d678dc2552b0af622c28d7887](https://github.com/EndstoneMC/endstone/commit/b926e752fc66361d678dc2552b0af622c28d7887) · 2024-03-03T21:00:08Z · meaningful

Repairs both ServerInstance::getMinecraft and Minecraft::getCommands by reading a pointer from the selected word slot and dereferencing it, rather than treating the pointer field storage as the object. Applies to Linux and Windows. This is a specific indirection correction, with no runtime bounds/null/version validation added.

Changed paths: `include/bedrock/command/minecraft_commands.h`, `src/endstone_runtime/bedrock/minecraft.cpp`, `src/endstone_runtime/bedrock/server_instance.cpp`.

<a id="commit-217"></a>
### 217. feat: add getCommandName function {#commit-217}

[cd2b9fd8cd7048921d4fae327e2f252d5118b53d](https://github.com/EndstoneMC/endstone/commit/cd2b9fd8cd7048921d4fae327e2f252d5118b53d) · 2024-03-03T22:24:25Z · meaningful

Adds getCommandName through the hidden-return hook bridge and creates combined CommandOutput/CommandOutputSender skeletons. MinecraftCommands still includes the removed separate sender header until219 repairs it. This introduces API dependencies before implementation rather than a tested output path.

Changed paths: `include/bedrock/command/command.h`, `include/bedrock/command/command_output.h`, `include/bedrock/command/command_output_sender.h`, `src/endstone_runtime/bedrock/command.cpp`.

<a id="commit-228"></a>
### 228. fix: ENDSTONE_HOOK_CALL_ORIGINAL_RVO macro for Linux {#commit-228}

[067950ee00855a64a420edc4e0d5c7f0704a3f95](https://github.com/EndstoneMC/endstone/commit/067950ee00855a64a420edc4e0d5c7f0704a3f95) · 2024-03-04T11:25:55Z · meaningful

Removes move assignment from the RVO macro so the native function writes directly into supplied storage, avoiding199 self-move of that storage. Title identifies Linux, but the macro definition is shared across supported platforms. Adapter reuses fetched command name; command-map constructor notes planned vanilla views. Hidden-return argument order, object construction and returned-pointer assumptions still need native ABI tests; no run result is present.

Changed paths: `include/endstone/detail/hook.h`, `src/endstone_core/command/command_adapter.cpp`, `src/endstone_core/command/command_map.cpp`.

<a id="commit-230"></a>
### 230. feat: add `CommandRegistry` data members {#commit-230}

[cb301918dabe259ab3e67cf3d735d2d2b5631bb1](https://github.com/EndstoneMC/endstone/commit/cb301918dabe259ab3e67cf3d735d2d2b5631bb1) · 2024-03-04T14:41:14Z · meaningful

Expands native CommandRegistry to many reverse-engineered callback/container fields, commands and aliases maps, unknown placeholders and platform-dependent parameter-symbol padding. These declarations expose STL layout directly; comments are not offset assertions. Incomplete ParseTable/Enum declarations and differing standard-library container sizes require compiler/host validation. The next commit removes the Linux-only120-byte padding in favor of96, showing this layout remains provisional.

Changed paths: `include/bedrock/command/command_registry.h`.

<a id="commit-232"></a>
### 232. feat: add `I18n::get` for translation {#commit-232}

[e8701263fe6ce3a352ce6da717819f4073bb0a6a](https://github.com/EndstoneMC/endstone/commit/e8701263fe6ce3a352ce6da717819f4073bb0a6a) · 2024-03-04T17:01:54Z · meaningful

Adds static I18n::get native symbol forwarding through RVO with message ID, string parameters and borrowed Localization pointer. Enables later translation of host description IDs; no locale fallback or unknown-key behavior is established beyond delegation to host.

Changed paths: `include/bedrock/i18n.h`, `src/endstone_runtime/bedrock/i18n.cpp`.

<a id="commit-234"></a>
### 234. feat: expose describe function in CommandRegistry {#commit-234}

[f379cf857ecdc7b7e29067e5fad24950b175fabf](https://github.com/EndstoneMC/endstone/commit/f379cf857ecdc7b7e29067e5fad24950b175fabf) · 2024-03-04T17:06:37Z · meaningful

Exposes a convenience describe(signature,overload) wrapper with native defaults and hooks the overloaded native description function. Uses explicitly typed member-function pointers to disambiguate overload resolution, including the existing parameter overload. Unknown trailing native arguments remain names a4/a5/a6, with no documented semantics or runtime verification.

Changed paths: `include/bedrock/command/command_registry.h`, `src/endstone_runtime/bedrock/command_registry.cpp`.
