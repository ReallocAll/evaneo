<!-- retrieval: {"source_ids":["public:commit:0491e70852970bbec9d4e939543f3049d82c758f","public:commit:26ff36bef6f8da48139fc9af7685d3e1977826ef","public:commit:42d03e3a31df0068d667bcde52399c1a0baaed9d","public:commit:50895241707e6892eabd39b40473c2a8b906edf6","public:commit:56da33aa1e15156732ed0fe38dee543bfa5f24db","public:commit:581bc6a7d90cb2444e82ab5a3e39475b733db4c3","public:commit:589875d6f8af246f0c31e93795f4920a5802b281","public:commit:65d06714554d46888bcde1c2a4f2b9ecc81d85f5","public:commit:679a76d2481dbbade3bfc1f46e4b862ca4f69ecd","public:commit:6a534aa8cbf78df517fabcd1bc5783ab8666c2a4","public:commit:75b2d3c288fd562edf51c92ced98ebd41684c8d2","public:commit:9433096650310f3948b8b951ab72725d0084c3fd","public:commit:99bf036279c1b66edc48ed348d846284a781c1f0","public:commit:9df2ec94651621295999364396895e2adc676ebc","public:commit:a35a13cd89b0679568b14b2344c52a1495a7ea95","public:commit:a51e2bb6ed600233ebe0585505c3586d3c2ef99e","public:commit:a6e7f7e9e75e0dc3f3ac2078a9fb8918f9d5348d","public:commit:b0b8af6f2d176b5ca244c2ebb9394ef681706aa2","public:commit:b5743695e616a30da6b4a62ac3709d188c89804a","public:commit:bff79fb4614e57057498a5bc2133b8ad4b02dc7a","public:commit:cacc933daf9b794b08abaaf9efea8c0919a50210","public:commit:d4e2c8466cc3206c110599f199610f0c0ec13cb3","public:commit:f3dbf2db09db5c7a2ca3a696416a54ffc8a1c532"],"source_type":"public","date":"2024-02-21..2024-03-04","topics":["lifetime","concurrency","ffi","testing","performance","recovery","api","diagnosis","documentation","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Command API, registry consistency, adapters and usage lexing {#command-api-registry-consistency-adapters-and-usage-lexing}

## The API evolves through incomplete intermediate contracts {#the-api-evolves-through-incomplete-intermediate-contracts}

189 begins a shared-owner CommandMap with fallback-prefix collision semantics before all referenced headers exist.190/191 introduce executor, command, sender and plugin command contracts.192 removes broad noexcept;193 repairs a standard-library override whose base requires it.194 introduces a borrowed registration-map pointer with same-map guards.195 briefly tries typed arguments through RTTI names,196 replaces virtual metadata with stored strings/usages/aliases and removes that experiment, and197 removes its helpers. These are alternatives actually present in source, not rejected designs inferred from later code.

196 also constructs PluginCommand by copying a Command base. Its registration pointer is copied with metadata; copying an already registered object can propagate stale map state. A PluginCommand borrows its owner Plugin while optionally sharing a separate executor. It refuses execution for a disabled owner and catches std::exception from callbacks, but owner lifetime must already be valid before that check.215 makes server own command map before plugin manager, so reverse destruction destroys plugins/loaders first. No destructor dereference is shown, but external retained commands and future callbacks require a clear lifetime policy. Shared ownership of a command is not ownership of its borrowed plugin.

## Two registries must remain consistent {#two-registries-must-remain-consistent}

211 starts writing native command registrations without storing the corresponding Endstone command.213 adds a native placeholder adapter and aliases but hardcodes the overload name;216 fixes the name and introduces real shared-owner map bookkeeping.216 normalizes name/aliases, provides default usage text, prevents mutation after registration, locks registration and skips colliding aliases. Allocation-bearing metadata setters remain noexcept. A single-vector call to the variadic setters can select vector copy construction; it is not inherently an invalid nested initializer.

Primary-name collisions are rejected. A collision with an existing alias is allowed by the check, but emplace does not overwrite that existing map key. Thus native registration of a new primary name can coexist with an Endstone lookup still pointing at the previous alias target. The code also ignores registerTo failure and has no rollback if a native or allocation step fails after partial mutation. Lookup is unlocked while registration mutates the map; there is no stated single-thread-only contract in the inspected API. These are static consistency/concurrency concerns, not observed exploit or crash claims.

220 comments out clearCommands because the commit explicitly states BDS does not support command unregistration. This is an important capability-driven API retreat. It avoids advertising a local-only clear as full native unregistration and removes a nested-lock path introduced when default registration became locking. Command::unregisterFrom still only changes the local pointer. Neither that guard nor manager/plugin clearing removes native command records. A future lifecycle design must account for the host capability instead of assuming reversible registration.

## Execution, output and incomplete argument support {#execution-output-and-incomplete-argument-support}

219 replaces the printf-only native wrapper with CommandAdapter: find the Endstone command by native name, create a sender adapter borrowing server/origin/output, and execute with an empty argument map. Usage parsing, permission selection and flags remain TODO.225 routes messages through native CommandOutput and increments success count only on successful execution; missing commands produce an error.226 hooks addMessage rather than apparent wrapper symbols, gates output when mode None and retains the success count. Layout fields are reverse-engineered without complete size/offset checks in these changes.

No change in this unit proves a full command framework is ready. Public Server does not yet expose the concrete command map accessor218. Names, description, usages and aliases exist, but overload generation still ignores usage strings. Command output behavior is delegated partly to the host and partly reconstructed locally. The native bridge's hidden-return assumptions are covered in the ABI dossier, especially the199→228 self-move correction.

## Native commands are views, not re-registrations {#native-commands-are-views-not-re-registrations}

231 claims vanilla command support in its title but initially logs signatures and leaves object construction TODO.233 adds CommandView whose execute always returns false.235 then snapshots native command names, translated descriptions, host-described overload usages and alias metadata into views, marking them registered without invoking native registration again. That separation avoids trying to recreate host-owned commands.

However,235 removes the previous alias-key insertion loop and only stores primary signature names. Alias metadata is populated, but getCommand(alias) does not thereby find a view. View execution remains false, and there is no refresh path for later host registry changes. The snapshot occurs during command-map construction, before the original startServerThread call at the endpoint, so timing is another explicit host assumption. Title, metadata availability and executable dispatch must remain separate coverage claims.

## Lexer endpoint and negative tests {#lexer-endpoint-and-negative-tests}

240 is the first usage lexer, not an integrated parser. It borrows input as string_view and returns borrowed token views. It recognizes ASCII identifiers and integers, punctuation and selected whitespace; quotes are tokens, not string-literal parsing, and an embedded NUL stops scanning. Four source tests cover no arguments, required/optional typed parameters and enum alternatives.

The helper get() checks position before incrementing, then reads value_[++position_]. When consuming the final identifier/digit/space it can index at size(), outside string_view's valid range, even though callers ignore the returned character. A string literal may mask the physical-memory issue while an exact-length non-NUL buffer exposes it. This static finding warrants boundary/sanitizer tests; none were executed here. Input and token lifetime, unexpected bytes, integer boundaries and repeat-End behavior also remain untested. Disabling cognitive-complexity lint in the same commit records a local configuration decision, not evidence of measured performance or acceptable complexity.

## Use and limits {#use-and-limits}

Use this history to review ownership/state machines, coordinate native and wrapper registries, distinguish metadata views from dispatch, and design tests at input/lifetime/rollback boundaries. Package TestServer221 intentionally omits native registry integration; it cannot validate these paths. All conclusions are bounded to the historical endpoint4 March2024. PR comments, later repairs and current behavior are outside this unit unless separately cited.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-189"></a>
### 189. feat: add CommandMap {#commit-189}

[75b2d3c288fd562edf51c92ced98ebd41684c8d2](https://github.com/EndstoneMC/endstone/commit/75b2d3c288fd562edf51c92ced98ebd41684c8d2) · 2024-02-21T14:38:38Z · meaningful

Adds initial CommandMap API with shared command ownership, fallback-prefix collision semantics, clear and nullable get, all noexcept. It includes command.h before that file exists in this chain and initially sits outside endstone namespace. These are scaffolding/intermediate constraints, not an independently working map implementation.

Changed paths: `include/endstone/command/command_map.h`.

<a id="commit-190"></a>
### 190. feat: add CommandExecutor {#commit-190}

[42d03e3a31df0068d667bcde52399c1a0baaed9d](https://github.com/EndstoneMC/endstone/commit/42d03e3a31df0068d667bcde52399c1a0baaed9d) · 2024-02-21T15:25:14Z · meaningful

Adds CommandExecutor callback using sender/command references, label and named string-argument map. References command/sender headers not yet introduced;191 supplies them and removes label parameter. API shape is short-lived, with no implementation or test result here.

Changed paths: `include/endstone/command/command_executor.h`.

<a id="commit-191"></a>
### 191. feat: add command-related classes {#commit-191}

[cacc933daf9b794b08abaaf9efea8c0919a50210](https://github.com/EndstoneMC/endstone/commit/cacc933daf9b794b08abaaf9efea8c0919a50210) · 2024-02-21T16:56:34Z · meaningful

Adds abstract public Command, CommandSender and PluginCommand, makes Plugin implement CommandExecutor, and defaults executor callback false. PluginCommand refuses disabled owners, delegates to optional shared executor or owner, and logs caught std::exception. noexcept surrounding allocation/formatting can terminate; sender lacks explicit virtual destructor. Namespace/forward-declaration inconsistencies remain: global Command declaration and global CommandSender/Server conflict with new public namespace. Circular includes and header completeness need compilation validation, not title-based assumptions.

Changed paths: `include/endstone/command/command.h`, `include/endstone/command/command_executor.h`, `include/endstone/command/command_map.h`, `include/endstone/command/command_sender.h`, `include/endstone/command/plugin_command.h`, `include/endstone/plugin/plugin.h`.

<a id="commit-192"></a>
### 192. refactor: remove noexcept from code base {#commit-192}

[65d06714554d46888bcde1c2a4f2b9ecc81d85f5](https://github.com/EndstoneMC/endstone/commit/65d06714554d46888bcde1c2a4f2b9ecc81d85f5) · 2024-02-28T16:52:22Z · meaningful

Removes broad noexcept from plugin loading, command APIs/callbacks and hook error helpers, allowing exceptions from filesystem/formatting/allocation to propagate rather than automatically terminate. Also adds default empty command description/aliases. Mechanical removal wrongly relaxes std::error_category::name override, requiring noexcept restored193. Defaulted destructors may remain implicitly noexcept despite textual removal; do not infer all code can now throw.

Changed paths: `include/bedrock/command/command.h`, `include/endstone/command/command.h`, `include/endstone/command/command_executor.h`, `include/endstone/command/command_map.h`, `include/endstone/command/command_sender.h`, `include/endstone/command/plugin_command.h`, `include/endstone/detail/hook.h`, `include/endstone/detail/plugin/cpp_plugin_loader.h`, `include/endstone/detail/plugin/python_plugin_loader.h`, `include/endstone/plugin/plugin_loader.h`, `src/endstone_core/plugin/cpp_plugin_loader.cpp`, `src/endstone_python/plugin/plugin.cpp`, `src/endstone_python/plugin/plugin_loader.cpp`, `src/endstone_runtime/linux/hook.cpp`, `src/endstone_runtime/plugin/python_plugin_loader.cpp`, `src/endstone_runtime/windows/hook.cpp`.

<a id="commit-193"></a>
### 193. fix: compilation errors {#commit-193}

[99bf036279c1b66edc48ed348d846284a781c1f0](https://github.com/EndstoneMC/endstone/commit/99bf036279c1b66edc48ed348d846284a781c1f0) · 2024-02-28T16:59:44Z · meaningful

Restores required noexcept on error_category::name for both platforms and moves CommandMap reference from abstract Command into PluginCommand. Adds empty CommandUsage placeholder. Narrow compile repair plus ownership/API rearrangement; does not prove all remaining namespace/header defects resolved.

Changed paths: `include/endstone/command/command.h`, `include/endstone/command/command_usage.h`, `include/endstone/command/plugin_command.h`, `src/endstone_runtime/linux/hook.cpp`, `src/endstone_runtime/windows/hook.cpp`.

<a id="commit-194"></a>
### 194. feat: improve 'Command' and 'CommandMap' classes with registration methods {#commit-194}

[bff79fb4614e57057498a5bc2133b8ad4b02dc7a](https://github.com/EndstoneMC/endstone/commit/bff79fb4614e57057498a5bc2133b8ad4b02dc7a) · 2024-03-01T11:29:07Z · meaningful

Adds Command registration-state pointer and same-map-only register/unregister guard, and marks map noncopyable/movable. New guard methods are noexcept again, a counterexample to reading192 as permanent ban. Move-enabled map with commands borrowing its address needs explicit rebinding semantics; constructor declarations suppress implicit default constructor until later explicit addition. No state-machine tests accompany contract.

Changed paths: `include/endstone/command/command.h`, `include/endstone/command/command_map.h`.

<a id="commit-195"></a>
### 195. feat: add Command::Argument {#commit-195}

[a6e7f7e9e75e0dc3f3ac2078a9fb8918f9d5348d](https://github.com/EndstoneMC/endstone/commit/a6e7f7e9e75e0dc3f3ac2078a9fb8918f9d5348d) · 2024-03-01T12:12:48Z · meaningful

Experiments with typed Command::Argument using cleaned RTTI names plus GNU demangling/MSVC textual cleanup and a noinline portability macro. Constructor template type cannot be deduced from its only std::string argument as written. Helper removes pybind11 namespace text, suggesting adaptation but source authorship/provenance is not established. No serialization/type-stability guarantee; argument design disappears196 and helpers197.

Changed paths: `include/endstone/command/command.h`, `include/endstone/detail/typeid.h`, `include/endstone/endstone.h`.

<a id="commit-196"></a>
### 196. refactor: command registration and execution logic {#commit-196}

[9433096650310f3948b8b951ab72725d0084c3fd](https://github.com/EndstoneMC/endstone/commit/9433096650310f3948b8b951ab72725d0084c3fd) · 2024-03-02T19:18:26Z · meaningful

Moves Command metadata from virtual getters into stored name/description/usages/aliases, removes typed Argument and empty Usage, simplifies map registration to fail on name collision rather than fallback prefixes, and constructs PluginCommand by copying base Command. Copy includes registration pointer, so borrowed map state can unintentionally propagate. Execution remains abstract and usages are text strings, preparing later parser. This is a substantive API redesign with no behavior tests.

Changed paths: `include/endstone/command/command.h`, `include/endstone/command/command_map.h`, `include/endstone/command/command_usage.h`, `include/endstone/command/plugin_command.h`.

<a id="commit-197"></a>
### 197. refactor: code clean up {#commit-197}

[0491e70852970bbec9d4e939543f3049d82c758f](https://github.com/EndstoneMC/endstone/commit/0491e70852970bbec9d4e939543f3049d82c758f) · 2024-03-02T19:28:15Z · meaningful

Removes abandoned RTTI/noinline experiment, creates empty EndstoneCommandMap header/source, and renames internal server/plugin-manager/logging files/classes. Git heuristic pairs old endstone.h with new command_map.h because of shared license text; semantically it is removal plus new scaffolding, not preserved algorithm. All renamed changed hunks read; most logging behavior unchanged. Double-slash include persists until198.

Changed paths: `include/endstone/command/command.h`, `include/endstone/command/command_map.h`, `include/endstone/detail/command/command_map.h`, `include/endstone/detail/endstone_server.h`, `include/endstone/detail/plugin/endstone_plugin_manager.h`, `include/endstone/detail/plugin/plugin_manager.h`, `include/endstone/detail/server.h`, `include/endstone/detail/spdlog/bedrock_level_formatter.h`, `include/endstone/detail/spdlog/bedrock_log_sink.h`, `include/endstone/detail/spdlog/bedrock_text_formatter.h`, `include/endstone/detail/spdlog/level_formatter.h`, `include/endstone/detail/spdlog/log_sink.h`, `include/endstone/detail/spdlog/text_formatter.h`, `include/endstone/detail/typeid.h`, `include/endstone/endstone.h`, `src/endstone_core/command/command_map.cpp`, `src/endstone_core/endstone_server.cpp`, `src/endstone_core/logger_factory.cpp`, `src/endstone_core/plugin/cpp_plugin_loader.cpp`, `src/endstone_core/plugin/endstone_plugin_manager.cpp`, `src/endstone_core/plugin/plugin_manager.cpp`, `src/endstone_core/server.cpp`, `src/endstone_core/spdlog/bedrock_level_formatter.cpp`, `src/endstone_core/spdlog/bedrock_log_sink.cpp`, `src/endstone_core/spdlog/bedrock_text_formatter.cpp`, `src/endstone_core/spdlog/level_formatter.cpp`, `src/endstone_core/spdlog/log_sink.cpp`, `src/endstone_core/spdlog/text_formatter.cpp`, `src/endstone_runtime/bedrock/dedicated_server.cpp`, `src/endstone_runtime/bedrock/server_instance.cpp`, `src/endstone_runtime/main.cpp`, `test_package/src/test_server.cpp`, `tests/test_endstone_server.cpp`.

<a id="commit-211"></a>
### 211. feat: add Minecraft class {#commit-211}

[9df2ec94651621295999364396895e2adc676ebc](https://github.com/EndstoneMC/endstone/commit/9df2ec94651621295999364396895e2adc676ebc) · 2024-03-03T17:28:50Z · meaningful

Wires concrete command map to EndstoneServer and native MinecraftCommands; adds Minecraft virtual destructor and ServerInstance getMinecraft platform offsets16/21, initially with the same pointer-field/object confusion later repaired214. Registration starts writing native registry but still returns false and does not retain the command. Dummy package host returns objects whose owned registry pointers are empty, so this fixture cannot substantiate working registry integration.

Changed paths: `include/bedrock/minecraft.h`, `include/bedrock/server/server_instance.h`, `include/endstone/detail/command/command_map.h`, `include/endstone/detail/server.h`, `src/endstone_core/command/command_map.cpp`, `src/endstone_core/server.cpp`, `src/endstone_runtime/bedrock/server_instance.cpp`, `test_package/src/dummy_bedrock.cpp`.

<a id="commit-213"></a>
### 213. feat: add basic command registration {#commit-213}

[6a534aa8cbf78df517fabcd1bc5783ab8666c2a4](https://github.com/EndstoneMC/endstone/commit/6a534aa8cbf78df517fabcd1bc5783ab8666c2a4) · 2024-03-03T17:49:20Z · meaningful

Adds a native CommandWrapper whose execute only prints TODO, registers lowercase aliases, and reports success based on signature existence. Overload registration is mistakenly hardcoded to test instead of the actual command name;216 corrects it. Removes the deleted getCommand caller. This is incremental scaffolding, not completed command execution.

Changed paths: `src/endstone_core/command/command_map.cpp`.

<a id="commit-215"></a>
### 215. feat: add CommandMap to EndstoneServer {#commit-215}

[b0b8af6f2d176b5ca244c2ebb9394ef681706aa2](https://github.com/EndstoneMC/endstone/commit/b0b8af6f2d176b5ca244c2ebb9394ef681706aa2) · 2024-03-03T21:00:41Z · meaningful

EndstoneServer acquires unique ownership of EndstoneCommandMap and constructs it before the plugin manager. Header forward declaration reduces the include cycle. Member destruction is reversed: plugin manager dies before command map; any retained PluginCommand references to plugins therefore need an explicit lifetime policy, although no destructor dereference is demonstrated here.

Changed paths: `include/endstone/detail/command/command_map.h`, `include/endstone/detail/server.h`, `src/endstone_core/server.cpp`.

<a id="commit-216"></a>
### 216. feat: improve command registration {#commit-216}

[a51e2bb6ed600233ebe0585505c3586d3c2ef99e](https://github.com/EndstoneMC/endstone/commit/a51e2bb6ed600233ebe0585505c3586d3c2ef99e) · 2024-03-03T21:25:14Z · meaningful

Implements owned command metadata normalization and registration: name/aliases lowercase, empty usages default to /name, mutation blocked after registration. Variadic setters accept individual strings or a single vector through vector copy construction; allocation-bearing setters/constructor are noexcept. Command-map registration locks, rejects an existing primary name, emits host command/aliases/overload, stores shared owners and marks registration. Fixes213 hardcoded overload name. Existing-alias collision is allowed but emplace does not replace the prior map entry, risking disagreement with the native registry. registerTo failure is ignored; no rollback covers partially completed host/map changes. clearCommands holds the same mutex then calls default registration, now a self-deadlock path;220 removes this unsupported operation. Version command gains aliases ver/about.

Changed paths: `include/endstone/command/command.h`, `src/endstone_core/command/command_map.cpp`, `src/endstone_core/command/defaults/version_command.cpp`.

<a id="commit-218"></a>
### 218. feat: add getCommandMap function to EndstoneServer {#commit-218}

[26ff36bef6f8da48139fc9af7685d3e1977826ef](https://github.com/EndstoneMC/endstone/commit/26ff36bef6f8da48139fc9af7685d3e1977826ef) · 2024-03-03T22:25:33Z · meaningful

Exposes the concrete server command map by borrowed reference and moves the native commands accessor definition. It does not yet add command-map access to the public Server interface; concrete/core availability and plugin-facing API are distinct.

Changed paths: `include/endstone/detail/server.h`, `src/endstone_core/server.cpp`.

<a id="commit-219"></a>
### 219. feat: add adapters for Command and CommandSender {#commit-219}

[581bc6a7d90cb2444e82ab5a3e39475b733db4c3](https://github.com/EndstoneMC/endstone/commit/581bc6a7d90cb2444e82ab5a3e39475b733db4c3) · 2024-03-03T22:38:05Z · meaningful

Connects native execution to Endstone Command using a CommandAdapter lookup by native command name and a CommandSenderAdapter borrowing server/origin/output. Invokes execute with an empty argument map; usage parsing and permission/flags remain TODO. Sender output still prints to stdout plus sender name, not native output. Missing-command and false-result paths are silent TODOs until225. Adds origin virtual methods in ABI order, fixes CommandSender namespace and the stale output-sender include.

Changed paths: `include/bedrock/command/command_origin.h`, `include/bedrock/command/minecraft_commands.h`, `include/endstone/command/command_sender.h`, `include/endstone/detail/command/command_adapter.h`, `src/endstone_core/command/command_adapter.cpp`, `src/endstone_core/command/command_map.cpp`.

<a id="commit-220"></a>
### 220. refactor: comment out clearCommands as BDS does not support command unregistration {#commit-220}

[f3dbf2db09db5c7a2ca3a696416a54ffc8a1c532](https://github.com/EndstoneMC/endstone/commit/f3dbf2db09db5c7a2ca3a696416a54ffc8a1c532) · 2024-03-03T22:46:41Z · meaningful

Comments out clearCommands in public interface and implementation because the commit explicitly states Bedrock Dedicated Server does not support command unregistration. This removes an advertised operation that could clear only Endstone state and also removes216 nested-lock path. It does not implement native rollback or make Command::unregisterFrom remove native entries; capability limits should shape the exposed lifecycle contract.

Changed paths: `include/endstone/command/command_map.h`, `include/endstone/detail/command/command_map.h`, `src/endstone_core/command/command_map.cpp`.

<a id="commit-225"></a>
### 225. feat: add CommandOutput {#commit-225}

[50895241707e6892eabd39b40473c2a8b906edf6](https://github.com/EndstoneMC/endstone/commit/50895241707e6892eabd39b40473c2a8b906edf6) · 2024-03-04T01:48:40Z · meaningful

Models native CommandOutput message/type/parameter fields and success counter; sender now routes normal/error messages through host output instead of printf. Adapter increments success count only on true execution and emits a missing-command error. Initial forceOutput/error hooks are replaced by226 lower-level addMessage approach. Layout comments lack size/offset assertions here; unused local command-name result is still recomputed until228. Accidental executor comment says returning forceOutput instead of success, so documentation is not an independent behavioral guarantee.

Changed paths: `include/bedrock/command/command_output.h`, `include/endstone/command/command_executor.h`, `include/endstone/command/command_sender.h`, `include/endstone/detail/command/command_adapter.h`, `src/endstone_core/command/command_adapter.cpp`, `src/endstone_runtime/bedrock/command_output.cpp`.

<a id="commit-226"></a>
### 226. fix: hook command output methods {#commit-226}

[d4e2c8466cc3206c110599f199610f0c0ec13cb3](https://github.com/EndstoneMC/endstone/commit/d4e2c8466cc3206c110599f199610f0c0ec13cb3) · 2024-03-04T02:20:05Z · meaningful

Moves native interception to private addMessage, implements forceOutput/error wrappers locally and suppresses messages when output type is None, retaining explicit success counter increment. This changes which host symbol must resolve and locally reproduces output semantics rather than assuming all wrappers are exported. Runtime startup uses one EndstoneRuntime logger for both normal and exception messages; fatal initialization still terminates. No output-mode or ABI tests accompany it.

Changed paths: `include/bedrock/command/command_output.h`, `src/endstone_runtime/bedrock/command_output.cpp`, `src/endstone_runtime/main.cpp`.

<a id="commit-229"></a>
### 229. feat: update error message for unregistered commands {#commit-229}

[a35a13cd89b0679568b14b2344c52a1495a7ea95](https://github.com/EndstoneMC/endstone/commit/a35a13cd89b0679568b14b2344c52a1495a7ea95) · 2024-03-04T14:39:14Z · mechanical

Changes missing-command diagnostic from not registered to not found in command map. Behavior and error routing are unchanged;235 later revises the wording again.

Changed paths: `src/endstone_core/command/command_adapter.cpp`.

<a id="commit-231"></a>
### 231. feat: add vanilla commands to command map {#commit-231}

[b5743695e616a30da6b4a62ac3709d188c89804a](https://github.com/EndstoneMC/endstone/commit/b5743695e616a30da6b4a62ac3709d188c89804a) · 2024-03-04T14:46:35Z · meaningful

Starts importing vanilla commands before default registration, but only logs primary signatures and leaves construction TODO; aliases find no primary entries yet. Title overstates the implemented outcome until235. Also unifies native parameter-symbol padding at96 bytes, changing Linux layout from230 without a captured offset measurement or test.

Changed paths: `include/bedrock/command/command_registry.h`, `include/endstone/detail/command/command_map.h`, `src/endstone_core/command/command_map.cpp`.

<a id="commit-233"></a>
### 233. feat: add CommandView class for vanilla commands {#commit-233}

[679a76d2481dbbade3bfc1f46e4b862ca4f69ecd](https://github.com/EndstoneMC/endstone/commit/679a76d2481dbbade3bfc1f46e4b862ca4f69ecd) · 2024-03-04T17:04:38Z · meaningful

Introduces CommandView as metadata representation for commands not owned by Endstone. It inherits metadata constructors but execute returns false unconditionally. This is intentionally only a view at this point; presence in a map does not mean Endstone can dispatch it.

Changed paths: `include/endstone/detail/command/command_view.h`, `src/endstone_core/command/command_view.cpp`.

<a id="commit-235"></a>
### 235. feat: implement the registration of vanilla commands as command views {#commit-235}

[589875d6f8af246f0c31e93795f4920a5802b281](https://github.com/EndstoneMC/endstone/commit/589875d6f8af246f0c31e93795f4920a5802b281) · 2024-03-04T17:07:00Z · meaningful

Completes primary vanilla views: collects alias metadata, translates descriptions via I18n, asks native registry for each overload usage, builds CommandView and marks it registered without calling native registerCommand again. Stores under signature.name but does not insert alias keys into known_commands_, unlike the previous loop; aliases are now metadata only for lookup purposes. execute still returns false. Commands are a construction-time snapshot with no demonstrated refresh. Reverts the missing-command wording and clarifies existing primary names are not replaced; alias-shadow consistency issue in registration remains.

Changed paths: `src/endstone_core/command/command_adapter.cpp`, `src/endstone_core/command/command_map.cpp`.

<a id="commit-240"></a>
### 240. feat: add CommandLexer {#commit-240}

[56da33aa1e15156732ed0fe38dee543bfa5f24db](https://github.com/EndstoneMC/endstone/commit/56da33aa1e15156732ed0fe38dee543bfa5f24db) · 2024-03-04T22:03:47Z · meaningful

Adds a non-owning string_view CommandLexer for usage syntax: ASCII identifiers/integers, punctuation, whitespace skip, End and Unexpected tokens. Four GTests cover no arguments, required/optional typed arguments and enum alternatives; no parser or command-registration integration yet. get() preincrements position then reads value_[position_], so consuming a final identifier/digit/space can read at size(), outside string_view bounds even though the returned char is ignored. Borrowed input/tokens require storage lifetime; embedded NUL ends scanning and quoted strings are punctuation, not parsed literals. Tests omit exact-length non-NUL buffers, numeric boundaries, invalid bytes, dangling views and repeated End behavior. Disables cognitive-complexity lint globally, without supplying runtime performance or test outcomes.

Changed paths: `.clang-tidy`, `include/endstone/detail/command/command_lexer.h`, `src/endstone_core/command/command_lexer.cpp`, `tests/test_command_lexer.cpp`.
