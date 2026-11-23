<!-- retrieval: {"source_ids":["public:commit:11f671d5695400f24821bca207ee127916cca406","public:commit:1e9487bdd5551ddb3579452538b0f5645480ae48","public:commit:23a63739cba3be2627913e533016aa72c44726c0","public:commit:241afdedeacb706e8b849f38cf6f4a09c32c2a17","public:commit:26434314f6034eb0e3f6c2e7c5da84b02a5e7558","public:commit:2badc3f8622b2f44e76669573da640c9344e0216","public:commit:3ff6d42109819f34070ec43650df55bda44ed395","public:commit:45ec6a5901dabd57efbebfe328b9129ee7eed96d","public:commit:6504edd7e5d1e8ad3d5cd401b8247c398bd70e1a","public:commit:7951aa519e3e17a1cbebed1ccec6ddab2fabc033","public:commit:7c7ef218541560c7ae981460c68dc94d3178db69","public:commit:b4d9f0d46f945810dacce6aab92dbb0ec1e5e3ac","public:commit:bdf2cc0f58f9bff61ffe35795a8d6f1d074eba05","public:commit:c47818821717722cd16c3a6a7383bf376354a97d","public:commit:dfb501e8c45f9d36ed6ab0ab5839865af653394e","public:commit:fca4c7bd2df7542f0e83643af87a51801e25f839"],"source_type":"public","date":"2024-09-16..2024-10-14","topics":["lifetime","ffi","testing","api","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Command identity, parsing, dispatch and output {#command-identity-parsing-dispatch-and-output}

Scope: Endstone commits 1801–1920, September 14–October 22, 2024. These notes follow related implementation areas during this period.

## Causal reading and applicability {#causal-reading-and-applicability}

Three concerns evolve separately: accepting only valid registrations, choosing the correct authority/identity for native execution, and preserving the actual output recipient. Registration preflight in 1809 is repaired in 1811 so empty argument lists are valid and invalid prefixes do not become overloads, but enum side effects prevent calling it a transaction. The parser subtree correction in 1819 addresses chained native parse calls; it is carried into the later command adapter rather than credited again as a new algorithm.

The performCommand permission change in 1816 has unusually clear user-facing rationale in 1828: player execution now uses the player's permissions, with an explicit server-dispatch alternative for prior elevated behavior. Proxy caller/callee separation in 1836–1837 is real but native virtual-origin wiring remains incomplete. Do not infer that every proxy source is supported merely because the interface exists.

The October command redesign (1866 onward) provides the strongest revision chain. Base-class copying loses derived plugin behavior; retaining the original shared command repairs that. Reconstructing a sender from native identity loses a decorator's callbacks; carrying the original borrowed sender through command output repairs that. Eager server translation loses message structure; forwarding Translatable preserves downstream presentation. Each repair has a different invariant and cost. The output marker occupies modeled native padding, and the public Python wrapper has no explicit sender keep-alive, so identity preservation does not itself prove lifetime or ABI safety. Native compiled-command ownership is not specified by the examined local implementation.

The portable lesson is conditional: preserve the semantic object when wrappers carry behavior, authority or capture state, then separately audit ownership, construction and native representation. The record does not assert that all command paths are tested, that permission denial intentionally implements a security concealment policy, or that external PR/issue discussion endorses each mechanism. No new behavior assertions accompany this redesign in the assigned changes.

## Per-commit evidence {#per-commit-evidence}

<a id="commit-1809"></a>
### Commit 1809 · feat: improve command registration logic by preventing registration when all usages fail to parse {#commit-1809}

Source: [dfb501e8c45f9d36ed6ab0ab5839865af653394e](https://github.com/EndstoneMC/endstone/commit/dfb501e8c45f9d36ed6ab0ab5839865af653394e). Authored 2024-09-16T11:01:36Z; committed 2024-09-16T11:01:36Z. Git author: Vincent; committer: Vincent.


Command registration first parses candidate usages and only then registers the command name, aliases and accepted overloads, addressing commands whose usages all fail. However, enum registration still happens during this preflight, so the change is not transactionally atomic. Its first implementation also confuses an empty parameter list with a failed parse and can retain the valid prefix of an invalid usage. Both edge cases matter to the next repair, rather than being hidden by the title's high-level goal.

Changed-source navigation: `include/endstone/detail/command/command_lexer.h`, `src/endstone_core/command/command_map.cpp`.

<a id="commit-1811"></a>
### Commit 1811 · fix: command registration with no parameter {#commit-1811}

Source: [45ec6a5901dabd57efbebfe328b9129ee7eed96d](https://github.com/EndstoneMC/endstone/commit/45ec6a5901dabd57efbebfe328b9129ee7eed96d). Authored 2024-09-16T11:21:05Z; committed 2024-09-16T11:21:05Z. Git author: Vincent; committer: Vincent.


An explicit parse-success flag separates invalid usages from valid zero-argument commands. The default usage becomes the command name, and an invalid parameter no longer leaves a shortened accepted overload. This completes the narrow registration repair from 1809 while retaining its enum side effects during validation. Full command-map context was read; no new test assertions accompany the fix.

Changed-source navigation: `src/endstone_core/command/command_map.cpp`.

<a id="commit-1816"></a>
### Commit 1816 · fix: ensure Player::performCommand calls command with Player as sender (#53) {#commit-1816}

Source: [2badc3f8622b2f44e76669573da640c9344e0216](https://github.com/EndstoneMC/endstone/commit/2badc3f8622b2f44e76669573da640c9344e0216). Authored 2024-09-16T22:03:58Z; committed 2024-09-16T22:03:58Z. Git author: Vincent; committer: Vincent.


Player performCommand now constructs a native Player command origin with the real player ID instead of the prior virtual/game-director route. This changes command identity and effective permissions, not merely output formatting. The later 1828 release notes explicitly describe the breaking reduction from operator-like execution to the player's own permissions and give server dispatch with execute-as as an alternative. That documented migration is stronger evidence of intent than guessing a general security philosophy from this patch alone.

Changed-source navigation: `src/endstone_runtime/bedrock/server/commands/command_origin.cpp`.

<a id="commit-1819"></a>
### Commit 1819 · fix: improve and correct command parser logic for handling chained commands {#commit-1819}

Source: [c47818821717722cd16c3a6a7383bf376354a97d](https://github.com/EndstoneMC/endstone/commit/c47818821717722cd16c3a6a7383bf376354a97d). Authored 2024-09-17T22:47:46Z; committed 2024-09-17T22:47:46Z. Git author: Vincent; committer: Vincent.


Each native parse call now traverses its own subtree, excludes the root's next sibling, and contributes its own argument instead of climbing to the outer root or skipping once arguments exist. Quoted identifiers are unwrapped. This supports nested/chained commands without repeatedly collecting the wrong outer arguments. Temporary parse debugging is added; serialized-origin logging is removed, and virtual-origin mapping is withdrawn with an explicit proxy caller/callee TODO. The patch records an unresolved boundary rather than implementing the later proxy design in full.

Changed-source navigation: `include/bedrock/server/commands/command_registry.h`, `src/endstone_core/command/command_adapter.cpp`, `src/endstone_runtime/bedrock/server/commands/command_origin.cpp`, `src/endstone_runtime/bedrock/server/commands/command_registry.cpp`.

<a id="commit-1835"></a>
### Commit 1835 · feat(command): add automatic downcaster for CommandSender objects {#commit-1835}

Source: [11f671d5695400f24821bca207ee127916cca406](https://github.com/EndstoneMC/endstone/commit/11f671d5695400f24821bca207ee127916cca406). Authored 2024-09-25T16:33:42Z; committed 2024-09-25T16:33:42Z. Git author: Vincent; committer: Vincent.


Replaces manual Player/Console casts in Python command callbacks with a polymorphic_type_hook for CommandSender. This aims to centralize dynamic Python type selection and removes repeated callback-specific conversion, including in plugin.cpp. At this unit's endpoint the specialization remains in command.cpp, so cross-translation-unit visibility and instantiation behavior are not assumed solved merely by its existence. The observed alternative is centralized type adaptation, with its actual placement retained as a limit.

Changed-source navigation: `src/endstone_python/command.cpp`, `src/endstone_python/plugin.cpp`.

<a id="commit-1836"></a>
### Commit 1836 · feat(command): add ProxiedCommandSender {#commit-1836}

Source: [7c7ef218541560c7ae981460c68dc94d3178db69](https://github.com/EndstoneMC/endstone/commit/7c7ef218541560c7ae981460c68dc94d3178db69). Authored 2024-09-25T16:43:24Z; committed 2024-09-25T16:43:24Z. Git author: Vincent; committer: Vincent.


Introduces ProxiedCommandSender with caller/callee accessors and a concrete implementation skeleton. The API returns borrowed references despite documentation wording about shared pointers. The split creates room to distinguish authority/output origin from the entity represented by the command; actual delegation arrives in 1837, and native virtual-origin integration remains unfinished.

Changed-source navigation: `include/endstone/command/proxied_command_sender.h`, `include/endstone/detail/command/proxied_command_sender.h`, `src/endstone_core/command/proxied_command_sender.cpp`.

<a id="commit-1837"></a>
### Commit 1837 · feat(command): implement ProxiedCommandSender {#commit-1837}

Source: [fca4c7bd2df7542f0e83643af87a51801e25f839](https://github.com/EndstoneMC/endstone/commit/fca4c7bd2df7542f0e83643af87a51801e25f839). Authored 2024-09-25T17:31:29Z; committed 2024-09-25T17:31:29Z. Git author: Vincent; committer: Vincent.


Implements proxy permissions, operator status, attachments and messages through the caller, while name and server come from the callee. The object borrows both senders. It does not pretend to be the callee's Player/Console type, and it does not complete the native virtual-origin TODO from 1819. This is a specific authority-versus-identity composition, useful only where the borrowed lifetimes and downstream type queries are understood.

Changed-source navigation: `include/endstone/detail/command/proxied_command_sender.h`, `src/endstone_core/command/proxied_command_sender.cpp`.

<a id="commit-1866"></a>
### Commit 1866 · refactor: re-design the command system {#commit-1866}

Source: [26434314f6034eb0e3f6c2e7c5da84b02a5e7558](https://github.com/EndstoneMC/endstone/commit/26434314f6034eb0e3f6c2e7c5da84b02a5e7558). Authored 2024-10-03T20:49:43Z; committed 2024-10-03T20:49:43Z. Git author: Vincent; committer: Vincent.


Separates CommandWrapper, the native MinecraftCommandAdapter and the public command map. Server dispatch compiles/runs through the map without recursively reentering the native execute hook; the native hook emits editable/cancellable command events for supported senders and falls back to the original for unsupported origins. Initial plugin wrapping copies into a base Command and slices derived behavior; 1867 retains the original shared command. Native compilation initially lacks a null guard, repaired in 1869. Output is initially server-localized, changed to Translatable in 1871. Command version 42 becomes a named constant and the parser's previously reviewed subtree behavior is retained under a new adapter. Native compiled-pointer ownership is not established by these files, so a definite leak is not asserted. All 1,337 raw lines were read.

Changed-source navigation: `include/bedrock/core/utility/property_bag.h`, `include/bedrock/forward.h`, `include/bedrock/server/commands/command.h`, `include/bedrock/server/commands/command_origin.h`, `include/bedrock/server/commands/command_output.h`, `include/bedrock/server/commands/command_property_bag.h`, `include/bedrock/server/commands/command_version.h`; plus 29 paths not listed here.

<a id="commit-1867"></a>
### Commit 1867 · feat: add CommandSender::asActor {#commit-1867}

Source: [6504edd7e5d1e8ad3d5cd401b8247c398bd70e1a](https://github.com/EndstoneMC/endstone/commit/6504edd7e5d1e8ad3d5cd401b8247c398bd70e1a). Authored 2024-10-05T07:59:44Z; committed 2024-10-05T07:59:44Z. Git author: Vincent; committer: Vincent.


Keeps the original shared Command inside CommandWrapper rather than copying/slicing it, preserving derived execution and plugin identity. Adds asActor and an entity-origin path, initially using the Player origin enum incorrectly; 1871 corrects that. Metadata is still copied into the wrapper and may diverge from later mutations of the original object. Original-sender pass-through remains a TODO until 1870. This sequence shows that ownership preservation and identity preservation are related but separate responsibilities.

Changed-source navigation: `include/bedrock/server/commands/command_origin.h`, `include/endstone/actor/actor.h`, `include/endstone/command/command_sender.h`, `include/endstone/detail/command/command_wrapper.h`, `include/endstone/permissions/permissible.h`, `src/endstone_core/command/command_map.cpp`, `src/endstone_core/command/command_wrapper.cpp`.

<a id="commit-1869"></a>
### Commit 1869 · feat: improve CommandMap::dispatch {#commit-1869}

Source: [b4d9f0d46f945810dacce6aab92dbb0ec1e5e3ac](https://github.com/EndstoneMC/endstone/commit/b4d9f0d46f945810dacce6aab92dbb0ec1e5e3ac). Authored 2024-10-05T09:25:43Z; committed 2024-10-05T09:25:43Z. Git author: Vincent; committer: Vincent.


Unknown command dispatch emits the localized unknown-command error, and a null native compile result is rejected before execution. This closes a specific failure path introduced by the command redesign; it does not validate every compiler outcome or establish ownership of successful compiled commands.

Changed-source navigation: `src/endstone_core/command/command_map.cpp`, `src/endstone_core/command/command_wrapper.cpp`.

<a id="commit-1870"></a>
### Commit 1870 · feat: allow passing down command sender if possible {#commit-1870}

Source: [241afdedeacb706e8b849f38cf6f4a09c32c2a17](https://github.com/EndstoneMC/endstone/commit/241afdedeacb706e8b849f38cf6f4a09c32c2a17). Authored 2024-10-05T09:57:41Z; committed 2024-10-05T09:57:41Z. Git author: Vincent; committer: Vincent.


CommandOutputWithSender carries a borrowed reference to the original sender through native execution, distinguished by a boolean placed in modeled native padding at offset 4. The plugin adapter can recover that sender, preserving wrapper capture instead of reconstructing only an equivalent actor/console. This introduces an ABI assumption: native-created output must not spuriously present the marker. Its initialization contract was not independently verified. The change concerns routing identity, not ownership extension.

Changed-source navigation: `include/bedrock/server/commands/command_output.h`, `include/endstone/detail/command/command_output_with_sender.h`, `src/endstone_core/command/command_wrapper.cpp`, `src/endstone_core/command/minecraft_command_adapter.cpp`.

<a id="commit-1871"></a>
### Commit 1871 · fix: preserve raw command output messages {#commit-1871}

Source: [23a63739cba3be2627913e533016aa72c44726c0](https://github.com/EndstoneMC/endstone/commit/23a63739cba3be2627913e533016aa72c44726c0). Authored 2024-10-05T10:01:01Z; committed 2024-10-05T10:01:01Z. Git author: Vincent; committer: Vincent.


Forwards a Translatable key and parameters rather than eagerly localized server text, leaving downstream senders able to choose presentation. Corrects entity command origins from Player to Entity. This completes two different earlier gaps: locale preservation from 1866 and origin identity from 1867.

Changed-source navigation: `src/endstone_core/command/command_wrapper.cpp`.

<a id="commit-1872"></a>
### Commit 1872 · feat: add CommandSenderWrapper {#commit-1872}

Source: [3ff6d42109819f34070ec43650df55bda44ed395](https://github.com/EndstoneMC/endstone/commit/3ff6d42109819f34070ec43650df55bda44ed395). Authored 2024-10-05T16:11:11Z; committed 2024-10-05T16:11:11Z. Git author: Vincent; committer: Vincent.


Adds CommandSenderWrapper with separate normal/error callbacks and delegation of permissions, type queries and server access to a borrowed sender. Missing callbacks drop output rather than forwarding it. Python exposes constructor callbacks without an explicit keep_alive policy, so retained wrapper/sender lifetimes remain a caller obligation not proven safe here. The original-sender path from 1870 is necessary for this wrapper to observe native command output. An unrelated stack-frame display change from hash-prefixed to bracketed numbering is proportionate formatting maintenance.

Changed-source navigation: `include/endstone/command/command_sender_wrapper.h`, `include/endstone/detail/signal_handler.h`, `python/src/endstone/_internal/endstone_python.pyi`, `python/src/endstone/command.py`, `src/endstone_python/command.cpp`.

<a id="commit-1873"></a>
### Commit 1873 · refactor: localise command error message using Translatable {#commit-1873}

Source: [1e9487bdd5551ddb3579452538b0f5645480ae48](https://github.com/EndstoneMC/endstone/commit/1e9487bdd5551ddb3579452538b0f5645480ae48). Authored 2024-10-07T21:15:50Z; committed 2024-10-07T21:15:50Z. Git author: Vincent; committer: Vincent.


Permission denial now uses the localized generic unknown-command message, making the visible response match unknown commands. The patch does not explicitly state a security rationale, so concealment of command existence is only a possible effect, not an attributed motive. A const qualification on unregister is a smaller contract cleanup.

Changed-source navigation: `include/endstone/command/command.h`.

<a id="commit-1875"></a>
### Commit 1875 · feat: add std::string overloads for log methods {#commit-1875}

Source: [bdf2cc0f58f9bff61ffe35795a8d6f1d074eba05](https://github.com/EndstoneMC/endstone/commit/bdf2cc0f58f9bff61ffe35795a8d6f1d074eba05). Authored 2024-10-09T11:22:44Z; committed 2024-10-09T11:22:44Z. Git author: Vincent; committer: Vincent.


Adds std::string overloads for all six Logger levels so already formatted/runtime strings can be logged without passing through fmt's compile-time format-string route. These overloads forward literal message contents rather than interpreting them again as format patterns. This is a bounded usability contract, not evidence that all formatting errors or logging lifetimes elsewhere were resolved.

Changed-source navigation: `include/endstone/logger.h`.

<a id="commit-1879"></a>
### Commit 1879 · chore: remove unused symbols {#commit-1879}

Source: [7951aa519e3e17a1cbebed1ccec6ddab2fabc033](https://github.com/EndstoneMC/endstone/commit/7951aa519e3e17a1cbebed1ccec6ddab2fabc033). Authored 2024-10-14T17:45:54Z; committed 2024-10-14T17:45:54Z. Git author: Vincent; committer: Vincent.


Removes now-unused CommandOutput::addMessage RVAs for both platforms after the local command-output implementation. TOML structure and deletions are verified. This is cleanup of a retired hook dependency, not a new command-output behavior.

Changed-source navigation: `python/src/endstone/_internal/symbols.toml`.
