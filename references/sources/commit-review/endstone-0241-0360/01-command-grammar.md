<!-- retrieval: {"source_ids":["public:commit:05136f1fcf32676d42a98befd42cb7ff914b8026","public:commit:06cb56abed48814971e66a706b2d3396b06816b6","public:commit:08de0a58e89c66290d6c122d5b9f974ff9afe547","public:commit:2489434eabc2723a8bb8c5dde37847dedd67487a","public:commit:26b25ed83abf76c8fdb6617f97c46901b45dbef1","public:commit:31fcd9ffbee28485d52dfc7aa124bbdf19d91c74","public:commit:38c371d34e0f52f0995009ca3844da4a022e2bf0","public:commit:4f26e158a136677d6e6db18859fea22119ed7c70","public:commit:53797269da12bdbc0e41160ccbe470eab4759ad3","public:commit:569122a81772798599c9b13e472282b8ef15fb08","public:commit:56e09bc9f5fb30540e08ba17df14804d5dee594e","public:commit:5fc7d2164dbfe0ef1a6d6c878dd7d940ff31a1a1","public:commit:5fe2eae7c42b01063e3277b64d892e652ba92451","public:commit:7af8eb265da90e87fed7c6b651df6a0ccfeeab08","public:commit:82375cfe0dcc57402e3661b395f3a18ca4137774","public:commit:865a06659b647e0ca4c0096d7fd139d8e623f6e6","public:commit:87431367cbc7bbdd08e2efcb566be105e105f2d3","public:commit:8b033bb9047ab23d6b77c7e892d12c26fdf05bc0","public:commit:8dacc12a7babdb77f07874b777f30976c21636f4","public:commit:9c42c2945248986867c65b534c8ad5fbbd45a2ad","public:commit:a3af52df4f82237ec36e7387828158f307e85bf4","public:commit:b33ea754a21fc5a5b4237a931940d04a3a30de96","public:commit:bafac45f5d51b6356be0d62e57c656ce80b573a4","public:commit:bb63eb54ae17ee6f8f98bb7538fb1d327ba24a2c","public:commit:c70a995956a9704faf6fe3c2f610b77ac54fb725","public:commit:cc74b0aa29d77e98a789b2f9739034739697382b","public:commit:d4a970b89ce02aca62aaf3704ab88c82fe194d11","public:commit:d8030556a275bdfcd4d6aa5c74fa9a5067a16e5e","public:commit:dbb759bf4384fc4a7d54ce8824ee3db56940ef8e","public:commit:dcc435ea2f05fe2b511a4088bcf255b02650acfb","public:commit:e4abf71a2b295880c77d7e03cc4249bd7a7759ea","public:commit:eb19b172b64308c9b0849f176794748e8467fc68","public:commit:f9aaa855a98e46d3d0e6910fbeb92457be9201bd","public:commit:fe09db8b5061bbc8879e6cab4fa17e61f8b8f174"],"source_type":"public","date":"2024-03-04..2024-03-12","topics":["lifetime","ffi","testing","recovery","api","diagnosis","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Usage grammar, native command parsing and ABI evolution {#usage-grammar-native-command-parsing-and-abi-evolution}

## Result and scope {#result-and-scope}

Between 4 and 13 March 2024, command metadata becomes an executable native-host adapter: usage strings describe overloads, native grammar validates parameter shapes, and a custom callback reconstructs positional strings for Endstone executors. The implementation repeatedly changes how it represents native parse callbacks and parameter layout. These alternatives and intermediate mismatches matter more than a single endpoint diagram. This dossier covers actual changes, not observed host execution or inferred personal preferences.

## Grammar grows independently of host support {#grammar-grows-independently-of-host-support}

241 immediately repairs the lexer boundary error introduced at the preceding unit's endpoint 240. The consumed character is returned before advancing the cursor. 242 introduces usage parsing with explicit required/optional delimiters, typed parameter names, enum syntax and exact-position diagnostics. Its twelve tests cover accepted forms and malformed delimiter/type/enum forms. The parser owns output names and values but borrows its input through the lexer. A syntax parser accepting a type name does not mean the native registry supports that type; integration later rejects unknown types.

The first enum form places alternatives in the type position, such as `<name:(a|b)>`. 322 changes the form to express enum type explicitly inside parameter brackets. 323 changes it again to `(a|b)<name:Type>`, preserving both parameter name and enum type. Empty alternatives allow a usage to reference an enum whose values are populated elsewhere. The final parser separates token, identifier, parameter and enum operations; helper exceptions become a false result and error text at the outer boundary. Tests change alongside the public syntax. This is deliberate grammar evolution, not equivalent refactoring.

The final parser resets its lexer but does not clear caller-owned output vectors or old error strings. Current registration creates fresh outputs per usage, so that call site avoids reuse contamination. Reusing the API elsewhere requires a defined reset/transaction contract. Invalid input can append partial parameters before failure. The outer noexcept function also writes an allocating error string in its catch path. These are bounded API observations rather than a claim of observed failures or an argument against using exceptions generally.

## Registration is a sequence of mutations {#registration-is-a-sequence-of-mutations}

245 begins constructing one native overload per usage. The command and aliases are already registered when a usage is parsed. Syntax failure logs and skips that usage; a name mismatch warns but still uses the actual registered command name. Later unsupported-type or enum-registration failures return false after earlier mutations. Thus a false result, or even success with no valid usages, cannot be assumed to mean no native/local state changed. The patch supplies no rollback protocol or integration test for partial failure.

The initial parameter adapter in 251 only prints and reports success. 253 then walks the native token tree to reconstruct arguments; 257 skips the command-name node and actually forwards the stored vector. Public execution moves from named maps to positional vectors across 255–267. The tree walker climbs to the root, traverses each argument subtree, joins text fragments with spaces and returns strings. Host grammar may validate a position, selector or JSON fragment, but this interface does not deliver typed positions, selected entities or parsed JSON objects. Reconstructed spacing is not the original lexical byte sequence. Host tree validity, token ownership and cycle freedom remain assumptions.

## Native representation alternatives and the Linux repair chain {#native-representation-alternatives-and-the-linux-repair-chain}

247 reinstates captured native parameter templates keyed by host type ID, returning empty data if no captured template exists. 252 abandons this approach for explicit grammar symbols and custom parsing. This removes dependence on capturing a matching parameter template first, but trades it for version-sensitive symbols and layouts. The source explicitly asks whether symbol mappings can be populated automatically; it does not show such discovery being implemented.

247 also changes ParseRule from a member-function pointer to a free-function pointer receiving the registry explicitly. 260 reports Linux registration crashes and introduces an extra eight-byte Linux field after that pointer, alongside revised overload fields and descriptor defaults. 319 restores a member-function pointer and removes the extra padding. The sequence supports a narrower explanation: parse-pointer representation was part of the layout mismatch. It does not establish a measured ABI specification, prove every changed field correct or identify one cause for every crash. Inline offset comments remain reverse-engineering annotations.

320 further changes the callback to a `CommandRegistry::parse<CommandAdapter>` specialization that receives the entire adapter at offset zero. Optional-presence offset becomes minus one, removing the old member-pointer offset trick and temporary flag. Friendship makes access to stored arguments explicit. 321 makes the member callback const and forwards native enum registration. These changes reduce guessed member offsets but retain host callback ABI dependence, versioned symbols and token-tree assumptions.

264 and 325–327 expand and centralize grammar symbols. Float's numeric symbol changes; position aliases distinguish integer block positions from floating coordinates. Equipment-slot gets a constant but no public usage-type map entry in this unit, so its commit title overstates usable support. 317–318 similarly revise enum value representation from strings to pairs of 64-bit values without supplying a meaning for those fields. Equal vector size would not prove element-level compatibility.

## Enum completion and origin dispatch {#enum-completion-and-origin-dispatch}

324 connects enum registration to parsed usages and populates PluginName from loaded plugins, lowercased for version-command completion. Enum-name pointers come from a map key rather than a temporary parameter string. The host owns the semantics of repeated enum registration and shared namespaces. A missing plugins directory still takes the create-directory path without loading entry points or populating names on that call. This is inherited server flow, not evidence that enum support itself discovers packages.

350 expands CommandOrigin's virtual interface through the methods needed to obtain permission level and origin type. Slots and signatures are part of the host ABI contract; source declarations alone are not compatibility tests. Later sender dispatch distinguishes a persistent server sender from temporary generic adapters. The concrete authorization work is in the permissions dossier.

## Evidence limits and application {#evidence-limits-and-application}

The parser test changes are real regression-test source. They do not exercise native registration, token layouts, partial rollback, optional-presence ABI or host version compatibility. No tests/build/server were run. Useful application is to separate grammar validation, registration mutation, native storage layout and callback output contracts, then choose tests at each boundary. Preserve the chronology when comparing alternatives; neither captured templates nor hardcoded symbols is a timeless demonstrated preference.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-241"></a>
### 241. fix: increment position correctly {#commit-241}

[87431367cbc7bbdd08e2efcb566be105e105f2d3](https://github.com/EndstoneMC/endstone/commit/87431367cbc7bbdd08e2efcb566be105e105f2d3) · 2024-03-04T22:12:45Z · meaningful

Author: Vincent. Actual parent: `56da33aa1e15156732ed0fe38dee543bfa5f24db`. Full individual diff read; static evidence only.

Changes lexer get from preincrement to postincrement, immediately repairing 240's final-character string_view boundary access while returning the character actually consumed. No new regression test is added; preserve this adjacent repair rather than treating the prior endpoint defect as lasting.

Changed paths: `include/endstone/detail/command/command_lexer.h`.

<a id="commit-242"></a>
### 242. fix: add CommandUsageParser {#commit-242}

[cc74b0aa29d77e98a789b2f9739034739697382b](https://github.com/EndstoneMC/endstone/commit/cc74b0aa29d77e98a789b2f9739034739697382b) · 2024-03-04T23:44:15Z · meaningful

Author: Vincent. Actual parent: `87431367cbc7bbdd08e2efcb566be105e105f2d3`. Full individual diff read; static evidence only.

Adds a usage parser for slash/name followed by required angle or optional square parameters, colon types and parenthesized enum alternatives. Lexer exposes reset/cursor/helpers publicly to support positional diagnostics. Parameters are owned strings even though lexer input remains borrowed. Twelve tests cover successful forms and missing slash/type/colon, unfinished enums, mismatched brackets and unexpected tokens with exact diagnostics. parse resets lexer but not output vectors/errors, so reuse/partial-failure state is not transactional. Syntax acceptance is separate from native type support; optional ordering, duplicate names and trailing NUL behavior are not validated here.

Changed paths: `include/endstone/detail/command/command_lexer.h`, `include/endstone/detail/command/command_usage_parser.h`, `src/endstone_core/command/command_lexer.cpp`, `src/endstone_core/command/command_usage_parser.cpp`, `tests/test_command_lexer.cpp`, `tests/test_command_usage_parser.cpp`.

<a id="commit-244"></a>
### 244. feat: add /plugins command {#commit-244}

[05136f1fcf32676d42a98befd42cb7ff914b8026](https://github.com/EndstoneMC/endstone/commit/05136f1fcf32676d42a98befd42cb7ff914b8026) · 2024-03-05T00:44:19Z · meaningful

Author: Vincent. Actual parent: `3330217dc8cd1a8d177b692fafea5ab7024b16dd`. Full individual diff read; static evidence only.

Adds built-in /plugins command and default registration, listing count/names with enabled green or disabled red coloring. Uses singleton manager snapshot and returns success even for an empty list. Version command namespace cleanup and parser test rename are incidental. This is operational visibility into lifecycle state, not permission-restricted administration yet.

Changed paths: `include/endstone/detail/command/defaults/plugins_command.h`, `src/endstone_core/command/command_map.cpp`, `src/endstone_core/command/defaults/plugins_command.cpp`, `src/endstone_core/command/defaults/version_command.cpp`, `tests/test_command_usage_parser.cpp`.

<a id="commit-245"></a>
### 245. feat: use command usage parser for command overload registration {#commit-245}

[d8030556a275bdfcd4d6aa5c74fa9a5067a16e5e](https://github.com/EndstoneMC/endstone/commit/d8030556a275bdfcd4d6aa5c74fa9a5067a16e5e) · 2024-03-05T00:54:55Z · meaningful

Author: Vincent. Actual parent: `05136f1fcf32676d42a98befd42cb7ff914b8026`. Full individual diff read; static evidence only.

Uses each usage string to create a native overload. Syntax failure logs and skips that usage; a mismatched parsed command name only warns while registration still uses the actual command name. Parameters remain TODO. Native command/map/aliases have already been registered, so invalid usages can leave a registered command with no usable overload while registration still succeeds. No rollback or parser-to-host integration test is added.

Changed paths: `src/endstone_core/command/command_map.cpp`.

<a id="commit-246"></a>
### 246. refactor: improve error logging messages in command map {#commit-246}

[08de0a58e89c66290d6c122d5b9f974ff9afe547](https://github.com/EndstoneMC/endstone/commit/08de0a58e89c66290d6c122d5b9f974ff9afe547) · 2024-03-05T01:02:43Z · small-semantic

Author: Vincent. Actual parent: `d8030556a275bdfcd4d6aa5c74fa9a5067a16e5e`. Full individual diff read; static evidence only.

Diagnostics now include the offending usage and expected command name rather than incorrectly calling the command name a usage. Control flow is unchanged; this improves actionable error context without establishing that malformed registrations are rejected atomically.

Changed paths: `src/endstone_core/command/command_map.cpp`.

<a id="commit-247"></a>
### 247. feat: add CommandParameterData::create {#commit-247}

[e4abf71a2b295880c77d7e03cc4249bd7a7759ea](https://github.com/EndstoneMC/endstone/commit/e4abf71a2b295880c77d7e03cc4249bd7a7759ea) · 2024-03-05T01:49:43Z · meaningful

Author: Vincent. Actual parent: `08de0a58e89c66290d6c122d5b9f974ff9afe547`. Full individual diff read; static evidence only.

Reintroduces captured CommandParameterData templates keyed by native type ID and adds create cloning a template with name/offset/optional fields. Missing templates return value-initialized empty data instead of prior fatal behavior. ParseRule changes from member-function pointer to explicit-registry free-function pointer, changing ABI representation; the later Linux padding workaround 260 and member-pointer restoration 319 matter to this experiment. Captured templates depend on observing host registration first.

Changed paths: `include/bedrock/command/command_registry.h`, `src/endstone_runtime/bedrock/command_registry.cpp`.

<a id="commit-248"></a>
### 248. fix: Bedrock type_id definitions {#commit-248}

[8dacc12a7babdb77f07874b777f30976c21636f4](https://github.com/EndstoneMC/endstone/commit/8dacc12a7babdb77f07874b777f30976c21636f4) · 2024-03-05T02:30:37Z · meaningful

Author: Vincent. Actual parent: `e4abf71a2b295880c77d7e03cc4249bd7a7759ea`. Full individual diff read; static evidence only.

Moves CommandRegistry forward declaration to global scope and wraps only specializations in Bedrock namespace, repairing 202's elaborated-name lookup problem. This is a concrete namespace/type identity correction, not simply cosmetic macro formatting.

Changed paths: `include/bedrock/type_id.h`.

<a id="commit-249"></a>
### 249. feat: CommandParameterData::create accepts std::string instead of const char* {#commit-249}

[c70a995956a9704faf6fe3c2f610b77ac54fb725](https://github.com/EndstoneMC/endstone/commit/c70a995956a9704faf6fe3c2f610b77ac54fb725) · 2024-03-05T02:31:27Z · meaningful

Author: Vincent. Actual parent: `8dacc12a7babdb77f07874b777f30976c21636f4`. Full individual diff read; static evidence only.

Accepts owned string names in parameter creation and moves them into metadata. Replaces variadic overload parameters with a vector, fitting runtime-parsed usage data rather than compile-time packs. Existing overload still copies into signature then passes a local object to native registration; no retention guarantee is added.

Changed paths: `include/bedrock/command/command_registry.h`, `src/endstone_runtime/bedrock/command_registry.cpp`.

<a id="commit-250"></a>
### 250. feat: add optional parameter `plugin_name` to version command {#commit-250}

[d4a970b89ce02aca62aaf3704ab88c82fe194d11](https://github.com/EndstoneMC/endstone/commit/d4a970b89ce02aca62aaf3704ab88c82fe194d11) · 2024-03-05T02:49:45Z · small-semantic

Author: Vincent. Actual parent: `c70a995956a9704faf6fe3c2f610b77ac54fb725`. Full individual diff read; static evidence only.

Advertises optional plugin_name:string in /version usage and broadens its description. Execution does not yet inspect arguments;256 and 257 complete that path. Metadata alone is not feature completion.

Changed paths: `src/endstone_core/command/defaults/version_command.cpp`.

<a id="commit-251"></a>
### 251. feat: register parameters {#commit-251}

[b33ea754a21fc5a5b4237a931940d04a3a30de96](https://github.com/EndstoneMC/endstone/commit/b33ea754a21fc5a5b4237a931940d04a3a30de96) · 2024-03-05T02:50:07Z · meaningful

Author: Vincent. Actual parent: `d4a970b89ce02aca62aaf3704ab88c82fe194d11`. Full individual diff read; static evidence only.

Builds native parameter descriptors from parsed usages and type-ID literals, with member offsets into CommandAdapter args/temp fields. Validates unsupported types/template sentinel and installs a custom parser, but that parser only prints and returns true. Descriptor construction can fail after command/alias state is already stored. All parameters share a temporary optional-presence field; source is still an incremental adapter experiment, not tested parsing.

Changed paths: `include/endstone/detail/command/command_adapter.h`, `src/endstone_core/command/command_adapter.cpp`, `src/endstone_core/command/command_map.cpp`.

<a id="commit-252"></a>
### 252. feat: improve register command with parameters {#commit-252}

[bafac45f5d51b6356be0d62e57c656ce80b573a4](https://github.com/EndstoneMC/endstone/commit/bafac45f5d51b6356be0d62e57c656ce80b573a4) · 2024-03-05T03:47:19Z · meaningful

Author: Vincent. Actual parent: `b33ea754a21fc5a5b4237a931940d04a3a30de96`. Full individual diff read; static evidence only.

Abandons captured templates/hardcoded type IDs in favor of native grammar symbols and custom parse rule; initially supports only string/str. Removes template cache and create helper introduced 247 and renames descriptor type/symbol fields. Runtime vector parameters are moved into overload. Direct construction leaves several fields unset until 260 supplies explicit defaults/constructor. TODO explicitly asks whether symbol table can be populated automatically; motive beyond observed simplification is unknown.

Changed paths: `include/bedrock/command/command_registry.h`, `include/bedrock/type_id.h`, `src/endstone_core/command/command_map.cpp`, `src/endstone_runtime/bedrock/command_registry.cpp`.

<a id="commit-253"></a>
### 253. feat: implement parseRuleAdapter {#commit-253}

[dbb759bf4384fc4a7d54ce8824ee3db56940ef8e](https://github.com/EndstoneMC/endstone/commit/dbb759bf4384fc4a7d54ce8824ee3db56940ef8e) · 2024-03-05T04:19:18Z · meaningful

Author: Vincent. Actual parent: `bafac45f5d51b6356be0d62e57c656ce80b573a4`. Full individual diff read; static evidence only.

Implements argument reconstruction by climbing ParseToken parents to root and walking each child subtree with a stack, concatenating text fragments with spaces. Stores ordered strings rather than a name map and avoids repeat reconstruction when nonempty. Initially includes command-name child;257 skips it. Assumes valid acyclic host links/text, preserves semantic text rather than exact original whitespace, and temporarily raises parse-tree logging to info. No tree-shape integration tests supplied.

Changed paths: `include/endstone/detail/command/command_adapter.h`, `src/endstone_core/command/command_adapter.cpp`, `src/endstone_runtime/bedrock/command_registry.cpp`.

<a id="commit-254"></a>
### 254. refactor: rename `parseRuleAdapter` function to `customParseRule` {#commit-254}

[865a06659b647e0ca4c0096d7fd139d8e623f6e6](https://github.com/EndstoneMC/endstone/commit/865a06659b647e0ca4c0096d7fd139d8e623f6e6) · 2024-03-05T04:58:54Z · mechanical

Author: Vincent. Actual parent: `dbb759bf4384fc4a7d54ce8824ee3db56940ef8e`. Full individual diff read; static evidence only.

Renames parser declaration and registration reference to customParseRule, but definition remains parseRuleAdapter until 257. Preserve the short-lived linkage mismatch; no independent behavior change intended.

Changed paths: `include/endstone/detail/command/command_adapter.h`, `src/endstone_core/command/command_map.cpp`.

<a id="commit-255"></a>
### 255. refactor: replace execute method args map with a vector {#commit-255}

[5fc7d2164dbfe0ef1a6d6c878dd7d940ff31a1a1](https://github.com/EndstoneMC/endstone/commit/5fc7d2164dbfe0ef1a6d6c878dd7d940ff31a1a1) · 2024-03-05T04:59:27Z · meaningful

Author: Vincent. Actual parent: `865a06659b647e0ca4c0096d7fd139d8e623f6e6`. Full individual diff read; static evidence only.

Changes public Command execution arguments from named map to ordered vector and updates views/plugins built-in command. Remaining version/executor/plugin signatures are completed in later commits. This changes public callback semantics and ABI; it aligns reconstruction with positional native arguments rather than retaining parameter names.

Changed paths: `include/endstone/command/command.h`, `include/endstone/detail/command/command_view.h`, `include/endstone/detail/command/defaults/plugins_command.h`, `src/endstone_core/command/command_view.cpp`, `src/endstone_core/command/defaults/plugins_command.cpp`.

<a id="commit-256"></a>
### 256. feat: include plugin in VersionCommand {#commit-256}

[38c371d34e0f52f0995009ca3844da4a022e2bf0](https://github.com/EndstoneMC/endstone/commit/38c371d34e0f52f0995009ca3844da4a022e2bf0) · 2024-03-05T05:00:19Z · meaningful

Author: Vincent. Actual parent: `5fc7d2164dbfe0ef1a6d6c878dd7d940ff31a1a1`. Full individual diff read; static evidence only.

/version now handles no arguments or case-insensitive plugin-name lookup, prints plugin version or useful failure guidance, and adopts vector arguments. Calls Plugin::getName before 258 introduces it. At this point adapter still sends no arguments until 257; feature is distributed across consecutive commits.

Changed paths: `include/endstone/detail/command/defaults/version_command.h`, `src/endstone_core/command/defaults/version_command.cpp`.

<a id="commit-257"></a>
### 257. feat: update command execution and parsing in command_adapter {#commit-257}

[53797269da12bdbc0e41160ccbe470eab4759ad3](https://github.com/EndstoneMC/endstone/commit/53797269da12bdbc0e41160ccbe470eab4759ad3) · 2024-03-05T05:00:42Z · meaningful

Author: Vincent. Actual parent: `38c371d34e0f52f0995009ca3844da4a022e2bf0`. Full individual diff read; static evidence only.

Passes reconstructed args_ into command execution, completes 254 parser rename, skips root's command-name child and accepts zero arguments. Restores parse-tree logging to debug. This connects prior descriptor/parser/API work; actual host parsing correctness remains unexecuted evidence.

Changed paths: `src/endstone_core/command/command_adapter.cpp`, `src/endstone_runtime/bedrock/command_registry.cpp`.

<a id="commit-260"></a>
### 260. fix: command registration crashes on Linux {#commit-260}

[31fcd9ffbee28485d52dfc7aa124bbdf19d91c74](https://github.com/EndstoneMC/endstone/commit/31fcd9ffbee28485d52dfc7aa124bbdf19d91c74) · 2024-03-05T12:58:39Z · meaningful

Author: Vincent. Actual parent: `bb51b7e2d690402e53af8965e8657f3391849597`. Full individual diff read; static evidence only.

Title reports Linux command-registration crashes. Patch revises native Overload unknown-field widths/defaults and gives parameter descriptors an explicit constructor, invalid symbols, zero option and Linux-only 8-byte unknown slot after free-function parse pointer. This attempts layout/default correctness, without a trace or passed host test. The later 319 restoration to member-function pointer removes the mysterious padding, providing a stronger evolving ABI explanation than the inline uncertainty comment alone.

Changed paths: `include/bedrock/command/command_registry.h`, `src/endstone_core/command/command_map.cpp`.

<a id="commit-262"></a>
### 262. feat: improve `/version` command to print plugin details {#commit-262}

[a3af52df4f82237ec36e7387828158f307e85bf4](https://github.com/EndstoneMC/endstone/commit/a3af52df4f82237ec36e7387828158f307e85bf4) · 2024-03-05T13:17:20Z · meaningful

Author: Vincent. Actual parent: `04284b19d39d2d3bca9557db58bce7fa7fbb23a6`. Full individual diff read; static evidence only.

/version describes a matched plugin with optional description and singular/plural author list joined with commas/and and colors. Website/contributor output and plugin-name completion remain TODO. Operational output is richer, but metadata validity follows loader/description contracts, and no sender-output tests are added.

Changed paths: `include/endstone/detail/command/defaults/version_command.h`, `src/endstone_core/command/defaults/version_command.cpp`.

<a id="commit-264"></a>
### 264. feat: refine command registry structure {#commit-264}

[8b033bb9047ab23d6b77c7e892d12c26fdf05bc0](https://github.com/EndstoneMC/endstone/commit/8b033bb9047ab23d6b77c7e892d12c26fdf05bc0) · 2024-03-05T16:48:20Z · meaningful

Author: Vincent. Actual parent: `c65af029b3a0b8fb16858a89e286d6d9377b140e`. Full individual diff read; static evidence only.

Refines native Registry unknown containers into literals/enums/symbols/soft enums and sets SemanticConstraint uint 8 representation. Adds int/float grammar-symbol literals to string support. Some substitutions change element types/ABI assumptions, not just labels. Static offset comments remain unverified against host; TODO about automatic symbol discovery persists.

Changed paths: `include/bedrock/command/command_registry.h`, `src/endstone_core/command/command_map.cpp`.

<a id="commit-265"></a>
### 265. feat: add version command usage without parameter {#commit-265}

[9c42c2945248986867c65b534c8ad5fbbd45a2ad](https://github.com/EndstoneMC/endstone/commit/9c42c2945248986867c65b534c8ad5fbbd45a2ad) · 2024-03-05T16:52:20Z · small-semantic

Author: Vincent. Actual parent: `8b033bb9047ab23d6b77c7e892d12c26fdf05bc0`. Full individual diff read; static evidence only.

Adds explicit /version no-parameter usage alongside optional plugin-name usage, creating an additional native overload. It documents/encodes the no-argument path rather than relying solely on optional parsing; no reason for redundancy or native result supplied.

Changed paths: `src/endstone_core/command/defaults/version_command.cpp`.

<a id="commit-266"></a>
### 266. chore: improve error messages while parsing command usages {#commit-266}

[f9aaa855a98e46d3d0e6910fbeb92457be9201bd](https://github.com/EndstoneMC/endstone/commit/f9aaa855a98e46d3d0e6910fbeb92457be9201bd) · 2024-03-05T16:54:41Z · mechanical

Author: Vincent. Actual parent: `9c42c2945248986867c65b534c8ad5fbbd45a2ad`. Full individual diff read; static evidence only.

Punctuation-only changes to unsupported-type and usage-parse diagnostics. Full diff read; no new control flow or general engineering principle.

Changed paths: `src/endstone_core/command/command_map.cpp`.

<a id="commit-271"></a>
### 271. feat: add default implementation to Plugin's execute method {#commit-271}

[56e09bc9f5fb30540e08ba17df14804d5dee594e](https://github.com/EndstoneMC/endstone/commit/56e09bc9f5fb30540e08ba17df14804d5dee594e) · 2024-03-05T22:45:56Z · meaningful

Author: Vincent. Actual parent: `ea95d2f7b78d0ceaec60daa7b6463f4558e11271`. Full individual diff read; static evidence only.

Makes Command::execute default false rather than pure, enabling metadata-only command values. Title incorrectly refers to Plugin execute. CommandView now reports explicitly that the view is not executable; clarifies distinction between host metadata and dispatch.

Changed paths: `include/endstone/command/command.h`, `src/endstone_core/command/command_view.cpp`.

<a id="commit-317"></a>
### 317. feat: add struct for CommandRegistry::Enum {#commit-317}

[4f26e158a136677d6e6db18859fea22119ed7c70](https://github.com/EndstoneMC/endstone/commit/4f26e158a136677d6e6db18859fea22119ed7c70) · 2024-03-08T18:28:34Z · meaningful

Author: Vincent. Actual parent: `b1c188d2c2903d9464dec2760299c28a31deec46`. Full individual diff read; static evidence only.

Models native Registry Enum with name, type ID, parse rule and initially vector<string> values. This is reverse-engineered data access, revised immediately 318; offsets alone are not host validation.

Changed paths: `include/bedrock/command/command_registry.h`.

<a id="commit-318"></a>
### 318. fix: type of `values` in `Enum` class {#commit-318}

[2489434eabc2723a8bb8c5dde37847dedd67487a](https://github.com/EndstoneMC/endstone/commit/2489434eabc2723a8bb8c5dde37847dedd67487a) · 2024-03-09T01:49:04Z · small-semantic

Author: Vincent. Actual parent: `4f26e158a136677d6e6db18859fea22119ed7c70`. Full individual diff read; static evidence only.

Corrects native Enum values from strings to pairs of 64-bit fields. Same vector footprint does not imply equivalent element interpretation; preserves uncertain native data semantics rather than inventing meanings.

Changed paths: `include/bedrock/command/command_registry.h`.

<a id="commit-319"></a>
### 319. fix: type of `CommandRegistry::ParseRule` and refactor function customParseRule {#commit-319}

[eb19b172b64308c9b0849f176794748e8467fc68](https://github.com/EndstoneMC/endstone/commit/eb19b172b64308c9b0849f176794748e8467fc68) · 2024-03-09T02:05:18Z · meaningful

Author: Vincent. Actual parent: `2489434eabc2723a8bb8c5dde37847dedd67487a`. Full individual diff read; static evidence only.

Restores ParseRule as a member-function pointer, moves custom parser into Registry with an explicit Endstone-only note, and removes Linux unknown padding introduced 260. This supports the interpretation that pointer representation, not a mysterious host field, explains the earlier Linux layout gap. Source now expresses the appropriate type; no host trace or offset measurement is supplied. Stale free-function declaration remains at 360;353 removes a different unused server method.

Changed paths: `include/bedrock/command/command_registry.h`, `src/endstone_core/command/command_adapter.cpp`, `src/endstone_core/command/command_map.cpp`.

<a id="commit-320"></a>
### 320. refactor: command adapter and parse rule {#commit-320}

[569122a81772798599c9b13e472282b8ef15fb08](https://github.com/EndstoneMC/endstone/commit/569122a81772798599c9b13e472282b8ef15fb08) · 2024-03-10T15:35:39Z · meaningful

Author: Vincent. Actual parent: `eb19b172b64308c9b0849f176794748e8467fc68`. Full individual diff read; static evidence only.

Turns parser into Registry::parse<CommandAdapter> specialization and passes whole adapter at offset 0 with optional presence offset-1. Removes pointer-to-member union offset helper and temporary-field dependence; accesses args_ through explicit friendship. This materially reduces hand-calculated member offsets while retaining host callback ABI and token-tree assumptions.

Changed paths: `include/bedrock/command/command_registry.h`, `include/endstone/detail/command/command_adapter.h`, `src/endstone_core/command/command_adapter.cpp`, `src/endstone_core/command/command_map.cpp`.

<a id="commit-321"></a>
### 321. feat: add CommandRegistry::addEnumValues method {#commit-321}

[fe09db8b5061bbc8879e6cab4fa17e61f8b8f174](https://github.com/EndstoneMC/endstone/commit/fe09db8b5061bbc8879e6cab4fa17e61f8b8f174) · 2024-03-11T11:41:27Z · meaningful

Author: Vincent. Actual parent: `569122a81772798599c9b13e472282b8ef15fb08`. Full individual diff read; static evidence only.

Makes parse member pointer/implementation const, adds native addEnumValues forwarding and enum parameter kind. Aligns native signature and creates registration capability used 324; declaring symbols alone does not yet connect usage enums.

Changed paths: `include/bedrock/command/command_registry.h`, `src/endstone_core/command/command_adapter.cpp`, `src/endstone_runtime/bedrock/command_registry.cpp`.

<a id="commit-322"></a>
### 322. feat: improve enum parsing in CommandUsageParser {#commit-322}

[82375cfe0dcc57402e3661b395f3a18ca4137774](https://github.com/EndstoneMC/endstone/commit/82375cfe0dcc57402e3661b395f3a18ca4137774) · 2024-03-11T12:40:27Z · meaningful

Author: Vincent. Actual parent: `fe09db8b5061bbc8879e6cab4fa17e61f8b8f174`. Full individual diff read; static evidence only.

Reworks enum usage syntax from name:(values) into (values):EnumType inside parameter brackets, adds is_enum and empty/single-value support, and makes lexer cursor private with accessor. Updates tests to assert enum/type/optionality and malformed trailing separators. This is a breaking grammar revision with explicit tests, not equivalent parser cleanup;323 changes syntax again to retain both parameter name and enum type.

Changed paths: `include/endstone/detail/command/command_lexer.h`, `include/endstone/detail/command/command_usage_parser.h`, `src/endstone_core/command/command_lexer.cpp`, `src/endstone_core/command/command_usage_parser.cpp`, `tests/test_command_usage_parser.cpp`.

<a id="commit-323"></a>
### 323. refactor: parsing in CommandUsageParser {#commit-323}

[bb63eb54ae17ee6f8f98bb7538fb1d327ba24a2c](https://github.com/EndstoneMC/endstone/commit/bb63eb54ae17ee6f8f98bb7538fb1d327ba24a2c) · 2024-03-11T14:39:55Z · meaningful

Author: Vincent. Actual parent: `82375cfe0dcc57402e3661b395f3a18ca4137774`. Full individual diff read; static evidence only.

Splits parser into token/identifier/parameter/enum helpers with exception-based internals caught by noexcept bool parse. Adds peek preserving cursor and defaults all Parameter fields. Final syntax places enum values before named parameter, e.g. (a|b)<name:Type>, allowing empty values for existing enum reuse. Tests update successful/error forms and expect fresh empty error strings. Output parameters/errors are still not cleared on repeated parse; assigning error in catch can allocate despite noexcept. Main lesson is simpler grammar decomposition plus changed public syntax, not a general endorsement of exceptions.

Changed paths: `include/bedrock/command/command_registry.h`, `include/endstone/detail/command/command_lexer.h`, `include/endstone/detail/command/command_usage_parser.h`, `src/endstone_core/command/command_lexer.cpp`, `src/endstone_core/command/command_usage_parser.cpp`, `tests/test_command_usage_parser.cpp`.

<a id="commit-324"></a>
### 324. feat: register plugin names to enum PluginName for auto-completion {#commit-324}

[06cb56abed48814971e66a706b2d3396b06816b6](https://github.com/EndstoneMC/endstone/commit/06cb56abed48814971e66a706b2d3396b06816b6) · 2024-03-11T15:19:54Z · meaningful

Author: Vincent. Actual parent: `bb63eb54ae17ee6f8f98bb7538fb1d327ba24a2c`. Full individual diff read; static evidence only.

Registers usage enums through native registry, borrows stable map-key c_str for enum metadata, and populates lowercase PluginName values after plugin loading for /version completion. Removes unused temp flag. Empty enum usage first establishes/reuses enum then later adds names. Shared enum namespace, repeated values and partial registration failures are delegated to host without tests; no independent completion runtime result observed.

Changed paths: `include/endstone/detail/command/command_adapter.h`, `include/endstone/detail/command/command_map.h`, `src/endstone_core/command/command_map.cpp`, `src/endstone_core/command/defaults/version_command.cpp`, `src/endstone_core/server.cpp`.

<a id="commit-325"></a>
### 325. feat: add more supported type {#commit-325}

[26b25ed83abf76c8fdb6617f97c46901b45dbef1](https://github.com/EndstoneMC/endstone/commit/26b25ed83abf76c8fdb6617f97c46901b45dbef1) · 2024-03-11T16:49:38Z · meaningful

Author: Vincent. Actual parent: `06cb56abed48814971e66a706b2d3396b06816b6`. Full individual diff read; static evidence only.

Centralizes native grammar symbol constants and adds selectors, integer/floating positions, messages and JSON aliases. FLOAT constant changes from prior 0x100002 to 0x100003. Arguments remain reconstructed strings even when host grammar validates richer types; this is parsing support, not typed object delivery. Constants still version-sensitive.

Changed paths: `include/bedrock/command/command_registry.h`, `src/endstone_core/command/command_map.cpp`, `src/endstone_runtime/bedrock/command_registry.cpp`.

<a id="commit-326"></a>
### 326. fix: type symbol look up {#commit-326}

[dcc435ea2f05fe2b511a4088bcf255b02650acfb](https://github.com/EndstoneMC/endstone/commit/dcc435ea2f05fe2b511a4088bcf255b02650acfb) · 2024-03-11T16:50:14Z · small-semantic

Author: Vincent. Actual parent: `26b25ed83abf76c8fdb6617f97c46901b45dbef1`. Full individual diff read; static evidence only.

Maps pos to floating-position grammar instead of block/integer position and adds vec 3f alias. Concrete semantic alias correction; block_pos/vec 3i retain integer behavior.

Changed paths: `src/endstone_core/command/command_map.cpp`.

<a id="commit-327"></a>
### 327. feat(command): add equipment_slot to supported type {#commit-327}

[5fe2eae7c42b01063e3277b64d892e652ba92451](https://github.com/EndstoneMC/endstone/commit/5fe2eae7c42b01063e3277b64d892e652ba92451) · 2024-03-11T16:54:45Z · small-semantic

Author: Vincent. Actual parent: `dcc435ea2f05fe2b511a4088bcf255b02650acfb`. Full individual diff read; static evidence only.

Adds EQUIPMENT_SLOT native symbol declaration/definition only. No equipment_slot entry is added to gTypeSymbols, so title does not establish usable public usage-type support in this commit.

Changed paths: `include/bedrock/command/command_registry.h`, `src/endstone_runtime/bedrock/command_registry.cpp`.

<a id="commit-350"></a>
### 350. feat: add virtual functions to CommandOrigin {#commit-350}

[7af8eb265da90e87fed7c6b651df6a0ccfeeab08](https://github.com/EndstoneMC/endstone/commit/7af8eb265da90e87fed7c6b651df6a0ccfeeab08) · 2024-03-12T18:15:16Z · meaningful

Author: Vincent. Actual parent: `09ac946f5d2bbd45f91b00263e51f48e5acaefeb`. Full individual diff read; static evidence only.

Expands CommandOrigin virtual declarations through slot 31, exposing permission level and origin type used by sender dispatch. Adds forward host types and moves permission-level enum to its own header with char underlying type rather than uint 8_t. Vtable ordering is an ABI assumption represented in comments, not measured here; merely adding callable signatures does not prove every host version matches.

Changed paths: `include/bedrock/command/command_origin.h`, `include/bedrock/command/command_permission_level.h`, `include/bedrock/command/command_registry.h`.
