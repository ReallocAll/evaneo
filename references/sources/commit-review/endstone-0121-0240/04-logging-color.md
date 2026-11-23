<!-- retrieval: {"source_ids":["public:commit:0317e13ceeecc935f17d952d60b22c8cf094a1e0","public:commit:0ed724a154a795d0eadc8a03991789096028b936","public:commit:13b625097e1febe6930b1e5a23f330dcecf21706","public:commit:52bf438871652b3b75e3394ef9c70b1c5d05b209","public:commit:62ed16e75ccd027d089eebd7f022a18c6761f05e","public:commit:6a9bd69fe1f0ee21c01c1b6731f3bb0ee45fd875","public:commit:71140fee624d9ef606a84c5e1480a11e4f538241","public:commit:7e9e713bf0f764e19f1d9e052d013ddae43f9f2a","public:commit:8655cee249ad30b0ca14628b8a644322bc0f01b1","public:commit:b9958706f215cff55e27207260c9a6af2273c1f9","public:commit:bec1cf0f83aeb3f574b4ce63362186fe28c28238","public:commit:ce4b22269991ced80fbc5a822890c09160a5ce94","public:commit:e5212a03a35bf85b92bd77fcb82ea8ae3ef008d6"],"source_type":"public","date":"2024-01-31..2024-03-04","topics":["ffi","testing","performance","api","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Logging, Unicode and color formatting {#logging-unicode-and-color-formatting}

## Mechanism and revision sequence {#mechanism-and-revision-sequence}

174 sets Windows console input/output code pages to UTF-8 before runtime initialization.175 separates spdlog adapter/level formatting and introduces a custom terminal-aware sink.176 adds a payload formatter that scans UTF-8 section-sign formatting codes and translates them to ANSI or strips them when colors are disabled.179 creates public ColorFormat constants and Python static properties;180 actually registers those bindings;183 adds facade/stubs and constant-value tests.184 aligns translation keys with those constants and corrects emerald RGB.227 applies GOLD to version-command output.

These steps establish separate layers: public symbolic codes, language bindings, payload translation, terminal capability/color-mode selection and host/command output routing. A constant string test is not a rendering test. A property-binding function that is never called does not expose its class until integration is completed. The history is useful precisely because those distinctions are visible.

## Failure behavior and observability {#failure-behavior-and-observability}

176 initially uses unordered_map::at for a code suffix, so an unknown code throws.178, whose title reports an illegal-color crash, replaces that with find. The fallback emits the unknown code character when colors are enabled after consuming the prefix; color-disabled parsing consumes both. This is a specific asymmetric behavior, not an inferred promise of preserving malformed text. Trailing prefixes, malformed UTF-8 and embedded invalid codes need tests. No crash trace or demonstrated passing regression is retained in this commit-only unit.

The formatter captures a color-enabled bool at construction while the sink has a later mode setter. A changed sink mode can therefore diverge from the payload formatter's captured setting unless it is rebuilt. OBFUSCATED maps to terminal conceal rather than Minecraft-style changing characters; naming the same format does not establish identical visual semantics. RGB correction184 is functional despite its refactor title.

175 formats, writes and flushes per message. The sink's lock protects one instance; LoggerFactory creates separate sinks for separate loggers. It does not demonstrate whole-message serialization across those separate locks. There are no measured throughput or flush-cost results. This is an audit question about stdout sharing, not a claimed reproduced interleaving defect or blanket recommendation to eliminate flushing.

177 trims trailing host whitespace and splits captured host messages on newlines. Internal empty lines still produce log events, final empty tail does not, and CRLF normalization is not explicit. It also changes the payload forwarding expression from a literal format string to string_view. Braces and overload selection at that formatting boundary deserve a focused test; the commit alone is insufficient to claim a format-injection or compile failure.226 later unifies startup/error reporting on an EndstoneRuntime named logger while retaining fatal termination.

## Tests, style and attribution {#tests-style-and-attribution}

183 asserts every exported constant value. It does not cover terminal colors, invalid code parsing, setter behavior, level-color range interaction, cross-sink ordering or command output.185 removes several threshold assertions during lint cleanup, so test volume cannot be assumed preserved.181 is verified formatting/configuration work, while182 also changes Python type-registration order beyond an exact header move. Keep these distinctions when using style commits as evidence.

Source comments point to Minecraft formatting documentation and earlier project code. This workunit read the changed code and comments, not those external pages or all spdlog implementation internals. Similarity to upstream sink patterns is not enough to assign independent invention; individual commit attribution means this integration/change is attributed, not every mechanism's origin.

## Application {#application}

Use this material when reviewing a multi-runtime logging API, Unicode/ANSI conversion, failure-safe diagnostics, payload versus format-string boundaries and test completeness. Verify desired behavior for invalid input before choosing preservation or stripping. Treat no-run source findings as hypotheses for targeted validation and avoid translating a short implementation experiment into an enduring personal style preference.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-174"></a>
### 174. feat: set UTF-8 as default encoding for console on Windows {#commit-174}

[52bf438871652b3b75e3394ef9c70b1c5d05b209](https://github.com/EndstoneMC/endstone/commit/52bf438871652b3b75e3394ef9c70b1c5d05b209) · 2024-01-31T23:00:55Z · small-semantic

Sets Windows console input and output code pages to UTF-8 during DLL attach before runtime startup. Aligns Unicode/color output expectations; applies process-console state, with no failure checks or console-mode tests.

Changed paths: `src/endstone_runtime/main.cpp`.

<a id="commit-175"></a>
### 175. feat: add spdlog sink for bedrock log integration {#commit-175}

[62ed16e75ccd027d089eebd7f022a18c6761f05e](https://github.com/EndstoneMC/endstone/commit/62ed16e75ccd027d089eebd7f022a18c6761f05e) · 2024-02-01T01:59:02Z · meaningful

Splits logger adapter/level formatter into named files and introduces custom spdlog sink with terminal-aware ANSI level colors, formatted color ranges, fwrite and flush per message. LoggerFactory still creates a separate sink per logger; cross-sink stdout serialization is not demonstrated. Public color-mode setter and formatting setup are separated. This is a customization foundation, not a measured logging-performance improvement; upstream-style sink mechanics should not be assumed independently invented.

Changed paths: `.clang-tidy`, `include/endstone_core/logger_factory.h`, `include/endstone_core/spdlog/bedrock_level_formatter.h`, `include/endstone_core/spdlog/bedrock_log_sink.h`, `include/endstone_core/spdlog/spdlog_adapter.h`, `src/endstone_core/logger_factory.cpp`, `src/endstone_core/spdlog/bedrock_level_formatter.cpp`, `src/endstone_core/spdlog/bedrock_log_sink.cpp`, `src/endstone_core/spdlog/spdlog_adapter.cpp`.

<a id="commit-176"></a>
### 176. feat: add coloured text formatter {#commit-176}

[8655cee249ad30b0ca14628b8a644322bc0f01b1](https://github.com/EndstoneMC/endstone/commit/8655cee249ad30b0ca14628b8a644322bc0f01b1) · 2024-02-01T02:39:43Z · meaningful

Adds UTF-8 section-sign color-code parser and ANSI translations, strips codes when colors disabled, and installs custom payload formatter. Invalid code uses unordered_map::at and can throw, fixed178. Formatter captures color-mode bool at construction while sink setter can later change its own bool, risking inconsistent mode changes. RGB table maps emerald to gold initially, fixed184. Comments cite Minecraft formatting documentation and legacy project code; neither external source was read here. No formatter tests yet.

Changed paths: `.clang-tidy`, `include/endstone_core/spdlog/bedrock_text_formatter.h`, `src/endstone_core/spdlog/bedrock_level_formatter.cpp`, `src/endstone_core/spdlog/bedrock_log_sink.cpp`, `src/endstone_core/spdlog/bedrock_text_formatter.cpp`.

<a id="commit-177"></a>
### 177. feat: improve logging by handling line breaks {#commit-177}

[b9958706f215cff55e27207260c9a6af2273c1f9](https://github.com/EndstoneMC/endstone/commit/b9958706f215cff55e27207260c9a6af2273c1f9) · 2024-02-01T03:00:14Z · meaningful

Splits captured host log messages by newline after trailing-whitespace trimming, logging each line separately and omitting final empty tail. Replaces literal '{}' logging with string_view payload calls; Logger overloads include fmt format_string and std::string, so braces/overload behavior merits a focused boundary test. Empty lines inside message still produce entries; CRLF normalization is not explicit. No tests added.

Changed paths: `src/endstone_runtime/bedrock/bedrock_log.cpp`.

<a id="commit-178"></a>
### 178. fix: crash due to illegal color code {#commit-178}

[13b625097e1febe6930b1e5a23f330dcecf21706](https://github.com/EndstoneMC/endstone/commit/13b625097e1febe6930b1e5a23f330dcecf21706) · 2024-02-01T08:28:32Z · meaningful

Title reports illegal-color crash; replaces throwing .at with find and falls back to emitting code character when colors enabled. Section-sign prefix is still consumed; in color-disabled mode unknown code character is discarded too. This avoids the lookup exception but defines asymmetric invalid-input behavior. No malformed UTF-8/trailing-prefix/unknown-code regression tests supplied.

Changed paths: `src/endstone_core/spdlog/bedrock_text_formatter.cpp`.

<a id="commit-179"></a>
### 179. feat(api): add ColorFormat {#commit-179}

[0ed724a154a795d0eadc8a03991789096028b936](https://github.com/EndstoneMC/endstone/commit/0ed724a154a795d0eadc8a03991789096028b936) · 2024-02-01T16:22:44Z · meaningful

Adds public ColorFormat strings for standard/material colors and formatting plus readonly Python static properties. Uses inline static std::string values and a macro to expose them; binding function is not called until180. OBFUSCATED maps to terminal conceal in separate formatter rather than game-style random text. No full semantic equivalence claimed.

Changed paths: `include/endstone/color_format.h`, `src/endstone_python/color_format.cpp`.

<a id="commit-180"></a>
### 180. feat(python): add bindings for ColorFormat {#commit-180}

[bec1cf0f83aeb3f574b4ce63362186fe28c28238](https://github.com/EndstoneMC/endstone/commit/bec1cf0f83aeb3f574b4ce63362186fe28c28238) · 2024-02-01T16:23:53Z · small-semantic

Declares and invokes def_color_format in module initialization, making179's bindings reachable. Two-line integration completion, not redundant evidence that179 already exposed the class.

Changed paths: `include/endstone_python/endstone_python.h`, `src/endstone_python/endstone_python.cpp`.

<a id="commit-181"></a>
### 181. style: code reformat {#commit-181}

[e5212a03a35bf85b92bd77fcb82ea8ae3ef008d6](https://github.com/EndstoneMC/endstone/commit/e5212a03a35bf85b92bd77fcb82ea8ae3ef008d6) · 2024-02-01T16:24:11Z · mechanical_scope

Changes clang-format/tidy naming and inline-lambda preferences, reformats equivalent logger/manager lambdas and fixes namespace comment. Actual executable expressions remain unchanged. Configuration choices are dated local style, not universal quality rules.

Changed paths: `.clang-format`, `.clang-tidy`, `src/endstone_core/plugin/endstone_plugin_manager.cpp`, `src/endstone_python/logger.cpp`, `src/endstone_runtime/windows/hook.cpp`.

<a id="commit-182"></a>
### 182. refactor: move color_format.h to util/color_format.h {#commit-182}

[ce4b22269991ced80fbc5a822890c09160a5ce94](https://github.com/EndstoneMC/endstone/commit/ce4b22269991ced80fbc5a822890c09160a5ce94) · 2024-02-01T16:29:17Z · small-semantic

Moves ColorFormat header exactly into util, aligns include, and reorders Python Server registration after plugin types. Header content unchanged; module initialization order is real beyond path cleanup, though no stated reason or runtime result establishes necessity.

Changed paths: `include/endstone/color_format.h`, `include/endstone/util/color_format.h`, `src/endstone_python/color_format.cpp`, `src/endstone_python/endstone_python.cpp`.

<a id="commit-183"></a>
### 183. test: python binding for ColorFormat {#commit-183}

[6a9bd69fe1f0ee21c01c1b6731f3bb0ee45fd875](https://github.com/EndstoneMC/endstone/commit/6a9bd69fe1f0ee21c01c1b6731f3bb0ee45fd875) · 2024-02-01T16:36:20Z · meaningful

Adds Python util facade/stub and explicit assertions for every exported ColorFormat string. Tests cover name/value mapping, not ANSI rendering, invalid codes, color-mode changes or sink behavior. Source assertions read but not executed.

Changed paths: `python/src/endstone/util.py`, `python/src/endstone/util.pyi`, `python/tests/test_color_format.py`.

<a id="commit-184"></a>
### 184. refactor(core): use ChatColor constants when populating the ansi code map {#commit-184}

[71140fee624d9ef606a84c5e1480a11e4f538241](https://github.com/EndstoneMC/endstone/commit/71140fee624d9ef606a84c5e1480a11e4f538241) · 2024-02-01T17:02:08Z · meaningful

Replaces literal character keys with ColorFormat constant suffixes and renames translation map. Also corrects emerald RGB from gold to green, so not pure refactor. Title refers to ChatColor while actual type is ColorFormat; preserve actual code identity.

Changed paths: `include/endstone_core/spdlog/bedrock_text_formatter.h`, `src/endstone_core/spdlog/bedrock_text_formatter.cpp`.

<a id="commit-185"></a>
### 185. style: lint codes {#commit-185}

[0317e13ceeecc935f17d952d60b22c8cf094a1e0](https://github.com/EndstoneMC/endstone/commit/0317e13ceeecc935f17d952d60b22c8cf094a1e0) · 2024-02-01T17:27:37Z · meaningful

Broad lint cleanup includes public ValidName→VALID_NAME and sink-method renames, Python CLI return annotation, unused parameter cleanup and macro trailing declaration. Logger threshold test removes many assertions, narrowing coverage rather than preserving all tests. Manager's old regex symbol reference is missed until186. No general conclusion that lint-only commits are semantics-free.

Changed paths: `.clang-tidy`, `include/endstone/plugin/plugin.h`, `include/endstone/plugin/plugin_description.h`, `include/endstone_core/spdlog/bedrock_log_sink.h`, `python/src/endstone/_internal/bootstrap/__init__.py`, `python/src/endstone/_internal/bootstrap/linux.py`, `python/tests/test_imports.py`, `src/endstone_core/spdlog/bedrock_log_sink.cpp`, `src/endstone_python/endstone_python.cpp`, `src/endstone_runtime/bedrock/bedrock_log.cpp`, `src/endstone_runtime/bedrock/type_id.cpp`, `src/endstone_runtime/windows/hook.cpp`, `tests/test_logger.cpp`.

<a id="commit-227"></a>
### 227. feat: add colour for version command output {#commit-227}

[7e9e713bf0f764e19f1d9e052d013ddae43f9f2a](https://github.com/EndstoneMC/endstone/commit/7e9e713bf0f764e19f1d9e052d013ddae43f9f2a) · 2024-03-04T02:20:22Z · meaningful

Prefixes version-command text with the public GOLD color code. This connects earlier color constants to command output, but does not establish renderer support across console/client outputs or reset behavior.

Changed paths: `src/endstone_core/command/defaults/version_command.cpp`.
