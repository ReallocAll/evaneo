<!-- retrieval: {"source_ids":["public:commit:109fb9f8a4e8df9273f6c91a8984606516e910ff","public:commit:12c2167ed9f6d0eb47c8a63dbeb340632e0c864e","public:commit:183c78a6c49506eb99dca6d1ac06ae01d6c51433","public:commit:25ca284b39d17686a426a93e7fb512815e74b3c7","public:commit:270bbbfa5418afa65c094f613ae601b0dc6cf2f7","public:commit:2e789bef8044aba3f823aefdd15765208b106557","public:commit:2ffbdca9f744558dbd35a4dd16f640504e509539","public:commit:3717f8657993aae939f93ba06eeb7d461895e9cd","public:commit:39bf998ba940791717590df8deb2b354720cbc05","public:commit:463aa5efe07831513c9adf605ed191a6af2866c3","public:commit:4b8c006b1da53de5fc84ebe6925036344eee6a16","public:commit:4c128b019854c2682548c58eecee15d80996786d","public:commit:4f38753b4d7c2e7298e17aae59a0bacada891060","public:commit:5ba15c4597021ce1de108b6dc518b273b6bd7267","public:commit:5c7cf0026c426090f31ebb8215eaa73df85a9e0a","public:commit:613b1d40b5ced495ff203858807a1c61e94f3ab8","public:commit:64e657979fc8bbd565fce9f93d3568c5b0dae15a","public:commit:6624931b6a6757a5be1bec8a611a0e84145b7778","public:commit:673b1afc3711b42a8836084a64969f3f979b5746","public:commit:6dd837b2c362ab4195ed9f3c428f277a4c2cb0df","public:commit:74b0d52c77889dc54e17dd0633391287f943c460","public:commit:776e2a63d6696f4744b7f3c22bc8ada35c7c30b4","public:commit:7e5c1a3cc3d4805edfff869995a73c51a192faa9","public:commit:89b9bfd49ad91a9a3a8e461e7ac8dabcb718cb6d","public:commit:9059e722bf103ea8e0ed7c5527430ab8c167c8b5","public:commit:906e488af8e5577f95992e93a75b4703e919072c","public:commit:943603843b8a200806fb1d08c31ee507db578eb6","public:commit:96bcd5294d1b14dc376f9797f9d34a601abed51e","public:commit:9d2b8b4ecb121cf034217fbda3174fedaa4da2be","public:commit:9d43ade25990a2a10e8526d003026e4d042cfefb","public:commit:9f1cca68c37cb2f47781526d45fd5d236021a7ad","public:commit:a05605e264fcabb4079842d178005f1c2225c742","public:commit:a49cc83d42b4373c04e0541f872525705a37100a","public:commit:a717a4fd6863f669751ce1ebee2062c6d01c0028","public:commit:af5c9d13b15d9b842fe0634c1aff92cc91847777","public:commit:b1be6ec957d07446d20636d8cef3aabafe03efcc","public:commit:b24e20e64b1bbca426add0e4a83381aa38e9e4c4","public:commit:c4c90eb31bafb4919cf09d81f8ceec2a1dea3a0b","public:commit:c61121e7033e3270112d760b02440f58bdbf617b","public:commit:c6e354cc2fc645bebb2e2a833e09140edb420a5e","public:commit:cb96d7df2cea4d5ec3281aa7f6b565fd0febfdb4","public:commit:cc04cfd121302b82616570df393adcb264967bc9","public:commit:d184ab251698630ea011efaf1ba6abf8ee7b4526","public:commit:d83eb6c52b26eb1f52ff40af02d907eab7c7846b","public:commit:d951b0dd7d2a346177a35316e93097d0a99a52d9","public:commit:e16b95da9659b41973d437d9f638965e9dc38390","public:commit:e3026684c5a7742d9705743c8934c6a24f23b457","public:commit:ee9f40319bb6c6680139eb9d338165e2a45714a4","public:commit:f01efea98fce30996467949c3c8a48eb7c67bd92","public:commit:f387e3ab14d836366bcca76cfbe8b8997fdcc44c"],"source_type":"public","date":"2024-04-19..2024-05-01","topics":["concurrency","ffi","testing","build","performance","recovery","api","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Packaging, durable diagnostics and documentation as a product surface {#packaging-durable-diagnostics-and-documentation-as-a-product-surface}

## Useful conclusion {#useful-conclusion}

This interval does substantial integration work beyond runtime features: selects the correct repaired wheels, narrows plugin-consumer dependencies, adds rotating file logs, builds bilingual-language plugin tutorials, generates Python/C++ references and iterates documentation deployment. The useful record includes revisions and reversals: Conda is tried and immediately removed; a manual MkDoxy build workaround is replaced with a minimum package version; global Linux ABI flags move from a reusable module to the consumer example. None of those configuration changes is itself a successful build or published-site observation.

Documentation titles can hide executable changes.809 exports Player from the Python root package;817 changes compiler/build behavior as well as tutorial prose. Conversely, broad header comment pass828 is verified non-executable and receives a brief disposition. Palette tweaks839–840 are not counted as independent engineering beliefs.

## Artifact selection and compatibility boundaries {#artifact-selection-and-compatibility-boundaries}

725 narrows pip installation to repaired manylinux_2_31_x86_64 wheels in CI and both Docker stages.726 applies analogous win_amd64 filtering and platform-specific artifact uploads while bumping API0.4.0. This avoids indiscriminately installing/uploading original plus repaired outputs. The local diff configures those paths; no CI log or container run demonstrates success.

726's Python loader accepts0.2/0.3/0.4, whereas the native loader still compares exact major.minor API strings. Endpoint source confirms both checks occur only after loading module code or entry point, not as a pre-execution safety boundary. The native mismatch path still returns before wrapping the raw plugin pointer; this earlier resource/lifecycle limitation is not repaired by release labeling. Patch versions0.4.1/0.4.2 keep API0.4. Public virtual additions/reordering within the interval mean a SemVer declaration alone is not a binary compatibility proof.

728 removes obsolete LIEF build options after the earlier libelf replacement and drops the core's exported smart-holder default macro.752 relocates EnTT from headers to core and adds GSL, narrowing the normal plugin-facing target to fmt.788 adds the scheduler's concurrentqueue dependency to core. These are packaging surfaces for different consumers, not just build-system spelling.

## Consumer mode: small public API target rather than full runtime build {#consumer-mode-small-public-api-target-rather-than-full-runtime-build}

815 introduces a dependency-mode branch before runtime package discovery and an EndstoneHeaders.cmake module.816 supplies the initially omitted include. A plugin using FetchContent can obtain endstone::headers and fmt10.2.1 without configuring the whole native runtime, Python extension or tests. The module enforces MSVC on Windows and Clang on UNIX, and sets Windows iterator-debug compatibility. Its initial global Linux libc++/PIC/static-library flags are removed817 and shown explicitly in the plugin's CMake tutorial instead.

817's tutorial explicitly identifies those flags as necessary for BDS ABI compatibility and warns that main tracks development, suggesting a release tag. That is stronger evidence of intent than a generic inference about liking pinned dependencies. Yet the example still defaults to main, so the actual snippet is not fully reproducible by default. Compiler-family validation alone is not a complete standard-library/CRT/build-mode match. The UNIX condition is broader than the 'Linux' error text, and no platform matrix was executed here.

The tutorial adds setuptools build metadata, an endstone entry point, a Plugin subclass, lifecycle callbacks and ENDSTONE_PLUGIN metadata. It retains TODO prose and C++ class examples lacking semicolons. Treat it as improving onboarding, not a fully verified copy-and-build artifact. The research does not run these examples or fetch their dependencies.

## File logging: persistence policy has specific bounds {#file-logging-persistence-policy-has-specific-bounds}

780 renames the existing sink to ConsoleLogSink.781 shares one console and one file sink across named loggers, writes logs/latest.log and rotates on startup or after the next local midnight. The file sink uses a mutex, a date-and-index filename pattern, a one-time100ms retry on failed rename and an exception if retry fails. It formats full timestamps/logger names and removes color decoration from payload.

The configuration uses max_files1000. That bound applies to numbered archives generated using the current date; it does not scan and expire all historical dates. Rotation at midnight names the just-finished file with the date at rotation time, not necessarily the date of every record it contains. The next deadline is computed as local midnight plus24hours, not a separately validated daylight-saving calendar operation. These are useful operational constraints to document rather than silently summarizing 'bounded log retention.'

782 starts periodic five-second spdlog flushing. This narrows ordinary buffering delay, but flush is not an fsync/power-loss guarantee, and fatal quick_exit behavior from the previous unit is not converted into graceful shutdown. No file-system failure, log rotation, restart, retention or DST tests are added. The spdlog internals were not independently read; no attribution of its helper behavior beyond the in-repository calls is made.

## Release narrative is evidence of claims, not independent validation {#release-narrative-is-evidence-of-claims-not-independent-validation}

802 creates a changelog back through0.2.0 using added/changed/fixed sections. It reports UUID correction, Linux weather and earlier listd fixes, sync-only scheduler and public API additions.818 moves the authoritative text to root CHANGELOG.md and includes it in the documentation, reducing duplicated maintenance. It declares Keep a Changelog and Semantic Versioning adherence. Those statements are retained as explicit intent, not proof that all releases obey compatibility guarantees.

831 dates0.4.2 and moves the unreleased block under it. Its game-version line says1.20.82 while827/830 use1.20.81. The historical discrepancy remains explicit. Similarly,822 manually rewrites a console example's development version to0.4.1; the guide's displayed output is illustrative source content, not a newly observed runtime success. It cannot be counted as an independent test run.

## Documentation architecture and revisions {#documentation-architecture-and-revisions}

804 adds Giscus comments gated by page metadata, with pathname mapping and theme synchronization.823 enables them specifically on installation/start/first-plugin pages.805–807 add Python references sourced from module metadata, configure source paths and move them under a Python section.809 additionally exports Player at root, so documentation work closes a real API discoverability gap.810 adds git committer/revision metadata and edit/view links; these display provenance but do not imply blanket authorship endorsement.

813 establishes tutorial navigation for creating/installing/publishing plugins, commands, events and scheduling. Most pages remain TODO.814 replaces the stock homepage and positions Python as quick/flexible and C++ as performance-oriented. This is explicit qualitative user guidance, not comparative benchmark evidence.817 replaces custom homepage palette JavaScript with separate light/dark image variants, a concrete simplification of one visual integration. No universal rejection of JavaScript follows: the Giscus theme script remains.

819's installation guide recommends an isolated virtual environment because it can be deleted/recreated, gives pip and Docker paths, persists the server directory via bind mount and documents the official-server download confirmation. It then instructs the user to check version. This is a real recovery/isolation rationale, although Windows shell distinctions and illustrative logs are not execution-verified by this review.821 repairs copied MkDocs wording, showing template adaptation is imperfect rather than fully original prose.

## C++ reference deployment: record the reversal, not an invented failure story {#c-reference-deployment-record-the-reversal-not-an-invented-failure-story}

824 changes Read the Docs from Python requirements to Mambaforge/Conda, including Doxygen.825 restores the previous RTD file exactly and deletes the environment file while adding MkDoxy generation over include/endstone, excluding detail. This is an observed reversal without an explicit failure explanation.826 adds manual pip install/mkdocs commands with a comment pointing to MkDoxy issue75.832 removes them and sets mkdoxy>=1.2.3. The local evidence supports replacement of a workaround by a dependency minimum; the issue body and release fix were not independently read, so exact upstream defect and collaborator credit remain unknown.

833 removes the hardcoded /usr/bin/doxygen path and adds a docs version manifest.834 splits stable into its own version and adds Python's object inventory. These are configured navigation/dependency states, not verified deployed URLs or generated output. No mkdocs, Doxygen, Python import or upstream tool was executed.

## Visual iteration receives proportionate treatment {#visual-iteration-receives-proportionate-treatment}

835 fixes a doubled URL scheme and adds a300×300 pixel-art cube logo/favicon. Its actual PNG was materialized, hashed and visually inspected, rather than marking an unseen binary reviewed.836–840 introduce light/dark semantic tokens, map Material components to them, refine search/header/footer/link styling, separate wide-screen header behavior and adjust height. Full CSS values were read. No screenshot of the rendered site, accessibility/contrast measurement or browser test was performed, so this is source-level visual intent only. Possible generated palette origin is unknown; it is not labeled generated merely from appearance.

## Attribution and applicability {#attribution-and-applicability}

Vincent authors/commits all sources in this assignment. Referenced tools/frameworks and copied stock-template conventions retain their own provenance; no old Nukkit or duplicate Cloudburst evidence is used. Useful application areas are packaging artifact selection, separating plugin consumers from runtime builds, operational logging policies, reproducible examples, source-generated reference maintenance and tracking temporary deployment workarounds. Do not infer broad personal taste from a version bump, social link or color-token adjustment.

Prior reviewed context: [RelWithDebInfo, fatal diagnostics and symbol loading](../endstone-0601-0720/04-diagnostics-build.md), [Python API-surface reorganization](../endstone-0601-0720/03-python-surface.md).

## Individual source dispositions {#individual-source-dispositions}

<a id="commit-725"></a>
### 725 · ci: fix test wheels {#commit-725}

[270bbbfa5418afa65c094f613ae601b0dc6cf2f7](https://github.com/EndstoneMC/endstone/commit/270bbbfa5418afa65c094f613ae601b0dc6cf2f7) · 2024-04-19T20:38:20Z · Vincent (author and committer).

Narrows wheel installation globs to repaired manylinux_2_31_x86_64 artifacts in CI/build/runtime Docker steps, preventing selection of all original/repaired wheels. Configured correction, no CI execution here.


<a id="commit-726"></a>
### 726 · release: version v0.4.0 {#commit-726}

[3717f8657993aae939f93ba06eeb7d461895e9cd](https://github.com/EndstoneMC/endstone/commit/3717f8657993aae939f93ba06eeb7d461895e9cd) · 2024-04-20T00:34:25Z · Vincent (author and committer).

Releases API0.4.0, expands Python supported API0.2/0.3/0.4 and restricts Windows install/upload to win_amd64 plus Linux upload to repaired platform. Native exact-version compatibility and Python allowlist remain different policies.


<a id="commit-728"></a>
### 728 · refactor: clean up conanfile.py {#commit-728}

[463aa5efe07831513c9adf605ed191a6af2866c3](https://github.com/EndstoneMC/endstone/commit/463aa5efe07831513c9adf605ed191a6af2866c3) · 2024-04-21T22:47:50Z · Vincent (author and committer).

Removes obsolete LIEF options after libelf migration669 and exported PYBIND11_USE_SMART_HOLDER_AS_DEFAULT core define. Build-consumer contract cleanup rather than runtime feature; no evidence establishes effect on unrelated consumer holders.


<a id="commit-730"></a>
### 730 · docs: update README.md {#commit-730}

[d184ab251698630ea011efaf1ba6abf8ee7b4526](https://github.com/EndstoneMC/endstone/commit/d184ab251698630ea011efaf1ba6abf8ee7b4526) · 2024-04-23T08:06:59Z · Vincent (author and committer).

README marks event system completed atv0.4.0. This is release roadmap assertion, not validation of all events.


<a id="commit-737"></a>
### 737 · docs: update README.md {#commit-737}

[e16b95da9659b41973d437d9f638965e9dc38390](https://github.com/EndstoneMC/endstone/commit/e16b95da9659b41973d437d9f638965e9dc38390) · 2024-04-23T16:28:14Z · Vincent (author and committer).

README replaces alternate GHCR run example with Compose build/up/attach production-oriented guidance. Instructions reviewed as documentation, not executed or proof of production readiness.


<a id="commit-751"></a>
### 751 · chore: update game version v1.20.80 {#commit-751}

[96bcd5294d1b14dc376f9797f9d34a601abed51e](https://github.com/EndstoneMC/endstone/commit/96bcd5294d1b14dc376f9797f9d34a601abed51e) · 2024-04-24T11:25:33Z · Vincent (author and committer).

Updates advertised/loader game version1.20.73→1.20.80. Marker change alone is not proof of ABI compatibility; following753–758 repair native interfaces.


<a id="commit-752"></a>
### 752 · chore(deps): add microsoft's GSL {#commit-752}

[af5c9d13b15d9b842fe0634c1aff92cc91847777](https://github.com/EndstoneMC/endstone/commit/af5c9d13b15d9b842fe0634c1aff92cc91847777) · 2024-04-24T11:25:51Z · Vincent (author and committer).

Adds Microsoft GSL4.0.0 and moves EnTT dependency from public headers target to core in CMake/Conan, aligns magic_enum/core transitive dependencies. GSL used by753 native I18n signatures; public API dependency narrowing observed, no explicit selection rationale.


<a id="commit-760"></a>
### 760 · release: version 0.4.1 {#commit-760}

[9059e722bf103ea8e0ed7c5527430ab8c167c8b5](https://github.com/EndstoneMC/endstone/commit/9059e722bf103ea8e0ed7c5527430ab8c167c8b5) · 2024-04-24T16:15:01Z · Vincent (author and committer).

Patch release0.4.1 marker only; APImajor.minor remains0.4.


<a id="commit-761"></a>
### 761 · refactor: CppPluginLoader::getPluginFileFilters {#commit-761}

[25ca284b39d17686a426a93e7fb512815e74b3c7](https://github.com/EndstoneMC/endstone/commit/25ca284b39d17686a426a93e7fb512815e74b3c7) · 2024-04-25T09:20:53Z · Vincent (author and committer).

Expands platform macro into explicit Windows.dll/Linux.so preprocessor branches, equivalent on supported targets. No other platform return supplied.


<a id="commit-780"></a>
### 780 · refactor: rename log_sink to console_log_sink {#commit-780}

[a05605e264fcabb4079842d178005f1c2225c742](https://github.com/EndstoneMC/endstone/commit/a05605e264fcabb4079842d178005f1c2225c742) · 2024-04-26T10:44:31Z · Vincent (author and committer).

Renames LogSink class/files/references to ConsoleLogSink with all methods unchanged, preparing separate file sink.


<a id="commit-781"></a>
### 781 · feat: add FileLogSink to write logging to files {#commit-781}

[c4c90eb31bafb4919cf09d81f8ceec2a1dea3a0b](https://github.com/EndstoneMC/endstone/commit/c4c90eb31bafb4919cf09d81f8ceec2a1dea3a0b) · 2024-04-26T13:38:57Z · Vincent (author and committer).

Adds shared mutex-protected file sink for all loggers at logs/latest.log, rotates on startup and next local midnight using dated numeric filenames, retries rename once after100ms then throws, strips color formatting. max_files1000 bounds numbered files for current date, not a global cross-date retention policy; startup/midnight archive name uses current date. No file rotation tests.


<a id="commit-782"></a>
### 782 · feat: flush sinks with interval of 5 seconds {#commit-782}

[9d2b8b4ecb121cf034217fbda3174fedaa4da2be](https://github.com/EndstoneMC/endstone/commit/9d2b8b4ecb121cf034217fbda3174fedaa4da2be) · 2024-04-26T13:55:32Z · Vincent (author and committer).

Starts spdlog periodic5-second sink flushing before runtime initialization. Improves periodic durability but is neither fsync guarantee nor crash-loss elimination; external worker shutdown not inspected.


<a id="commit-802"></a>
### 802 · docs: add changelog/index.md {#commit-802}

[183c78a6c49506eb99dca6d1ac06ae01d6c51433](https://github.com/EndstoneMC/endstone/commit/183c78a6c49506eb99dca6d1ac06ae01d6c51433) · 2024-04-29T16:10:43Z · Vincent (author and committer).

Introduces release-oriented changelog with added/changed/fixed sections and compare links back to0.2.0. Reports weather/listd fixes and basic sync-only scheduler. Changelog summarizes earlier commits but is not independent reproduction; broadcast all-players shorthand is broader than permission-filtered implementation.


<a id="commit-803"></a>
### 803 · docs: fix grammar {#commit-803}

[b24e20e64b1bbca426add0e4a83381aa38e9e4c4](https://github.com/EndstoneMC/endstone/commit/b24e20e64b1bbca426add0e4a83381aa38e9e4c4) · 2024-04-29T16:20:11Z · Vincent (author and committer).

Grammar-only changelog edit, no claim change.


<a id="commit-804"></a>
### 804 · docs: add overrides for comments partial {#commit-804}

[f01efea98fce30996467949c3c8a48eb7c67bd92](https://github.com/EndstoneMC/endstone/commit/f01efea98fce30996467949c3c8a48eb7c67bd92) · 2024-04-29T16:47:13Z · Vincent (author and committer).

Adds opt-in per-page Giscus comments tied to repository/pathname and theme synchronization via palette listener. Read script as data, not executed. Public repository/category identifiers are not credentials; no proof comment hosting configured successfully.


<a id="commit-805"></a>
### 805 · docs: add api references {#commit-805}

[5c7cf0026c426090f31ebb8215eaa73df85a9e0a](https://github.com/EndstoneMC/endstone/commit/5c7cf0026c426090f31ebb8215eaa73df85a9e0a) · 2024-04-29T17:18:43Z · Vincent (author and committer).

Adds Python API reference pages sourced by mkdocstrings and signatures/crossrefs configuration. Generated API display makes docstrings/stubs part of user contract; no documentation build run.


<a id="commit-806"></a>
### 806 · docs: add the 'paths' configuration to the mkdocs.yml {#commit-806}

[776e2a63d6696f4744b7f3c22bc8ada35c7c30b4](https://github.com/EndstoneMC/endstone/commit/776e2a63d6696f4744b7f3c22bc8ada35c7c30b4) · 2024-04-29T20:50:45Z · Vincent (author and committer).

Adds python/src search path for mkdocstrings source discovery.


<a id="commit-807"></a>
### 807 · docs: move python docstrings from reference to reference/python {#commit-807}

[4f38753b4d7c2e7298e17aae59a0bacada891060](https://github.com/EndstoneMC/endstone/commit/4f38753b4d7c2e7298e17aae59a0bacada891060) · 2024-04-29T22:35:26Z · Vincent (author and committer).

Seven exact reference-page relocations under reference/python and matching navigation nesting; contents unchanged.


<a id="commit-808"></a>
### 808 · docs: add getting-started.md {#commit-808}

[4c128b019854c2682548c58eecee15d80996786d](https://github.com/EndstoneMC/endstone/commit/4c128b019854c2682548c58eecee15d80996786d) · 2024-04-29T22:37:32Z · Vincent (author and committer).

Adds placeholder installation page/nav and reorders reference/changelog. Three-line scaffold is not a finished getting-started guide.


<a id="commit-809"></a>
### 809 · docs: update mkdocstrings options {#commit-809}

[89b9bfd49ad91a9a3a8e461e7ac8dabcb718cb6d](https://github.com/EndstoneMC/endstone/commit/89b9bfd49ad91a9a3a8e461e7ac8dabcb718cb6d) · 2024-04-29T22:48:23Z · Vincent (author and committer).

Documentation title also hides runtime facade repair: exports Player from root endstone package, previously only internal binding. mkdocstrings removes private-name filter, hides source and shows root headings.


<a id="commit-810"></a>
### 810 · docs: add git committer plugin and revision plugin {#commit-810}

[d83eb6c52b26eb1f52ff40af02d907eab7c7846b](https://github.com/EndstoneMC/endstone/commit/d83eb6c52b26eb1f52ff40af02d907eab7c7846b) · 2024-04-29T23:10:32Z · Vincent (author and committer).

Adds git revision/committer provenance plugins and edit/view/navigation links; sets author/copyright metadata. Introduces duplicated https scheme in site_url, repaired835. These are documentation provenance features, not evidence all displayed Git committers authored every passage.


<a id="commit-812"></a>
### 812 · docs: add Twitter link {#commit-812}

[7e5c1a3cc3d4805edfff869995a73c51a192faa9](https://github.com/EndstoneMC/endstone/commit/7e5c1a3cc3d4805edfff869995a73c51a192faa9) · 2024-04-29T23:30:44Z · Vincent (author and committer).

Adds official project Twitter social link to docs navigation; no technical behavior or personal preference inference.


<a id="commit-813"></a>
### 813 · docs: add blank tutorials {#commit-813}

[b1be6ec957d07446d20636d8cef3aabafe03efcc](https://github.com/EndstoneMC/endstone/commit/b1be6ec957d07446d20636d8cef3aabafe03efcc) · 2024-04-29T23:49:39Z · Vincent (author and committer).

Scaffolds Python/C++ tutorial paths for create/install/commands/events/scheduling/publish, with mostly TODO bodies and initial lifecycle examples. Adds linked tabs and broad Markdown extensions. Template-derived magiclink repository settings remain squidfunk/mkdocs-material; do not mistake copied scaffold for independently chosen architecture.


<a id="commit-814"></a>
### 814 · docs: improve index.md {#commit-814}

[d951b0dd7d2a346177a35316e93097d0a99a52d9](https://github.com/EndstoneMC/endstone/commit/d951b0dd7d2a346177a35316e93097d0a99a52d9) · 2024-04-30T08:42:04Z · Vincent (author and committer).

Replaces stock MkDocs homepage with Endstone entry cards and theme-responsive Socialify image script, removes empty tutorial index. Reference page explicitly positions Python for quick/flexible start and C++ for optimized performance; qualitative guidance, not a benchmark.


<a id="commit-815"></a>
### 815 · feat: update CMakeLists.txt and add EndstoneHeaders.cmake {#commit-815}

[5ba15c4597021ce1de108b6dc518b273b6bd7267](https://github.com/EndstoneMC/endstone/commit/5ba15c4597021ce1de108b6dc518b273b6bd7267) · 2024-04-30T09:35:22Z · Vincent (author and committer).

Adds dependency-mode early return and EndstoneHeaders module so plugin consumers can avoid runtime/Python/native dependencies. Module enforces MSVC/Clang, pins fmt10.2.1 and creates interface target; initially early-return branch does not include module until816. Initial global Linux ABI flags later moved into tutorial817.


<a id="commit-816"></a>
### 816 · feat: update CMakeLists.txt {#commit-816}

[74b0d52c77889dc54e17dd0633391287f943c460](https://github.com/EndstoneMC/endstone/commit/74b0d52c77889dc54e17dd0633391287f943c460) · 2024-04-30T09:47:02Z · Vincent (author and committer).

Actually includes EndstoneHeaders before dependency-mode return, completing815 consumer target setup.


<a id="commit-817"></a>
### 817 · docs: update create-your-first-plugin.md {#commit-817}

[64e657979fc8bbd565fce9f93d3568c5b0dae15a](https://github.com/EndstoneMC/endstone/commit/64e657979fc8bbd565fce9f93d3568c5b0dae15a) · 2024-04-30T10:29:47Z · Vincent (author and committer).

Expands first-plugin tutorial with setuptools entry point, lifecycle/metadata and CMake FetchContent/shared library target. Explicitly warns main is development and suggests release tag; documents ABI flags. Moves Linux flags out of shared headers module into consumer example, leaving compiler gate. Replaces homepage palette JS with light/dark image variants. Tutorial still has TODO prose and missing C++ class semicolons.


<a id="commit-818"></a>
### 818 · docs: move changelog.md to project root dir {#commit-818}

[906e488af8e5577f95992e93a75b4703e919072c](https://github.com/EndstoneMC/endstone/commit/906e488af8e5577f95992e93a75b4703e919072c) · 2024-04-30T10:43:11Z · Vincent (author and committer).

Moves authoritative changelog to repository root and includes it in docs via snippet, avoiding duplicated content; declares Keep a Changelog/SemVer adherence and adds per-release links. Adds black docs dependency and fixes ABI spelling. Statement of versioning intent does not establish binary compatibility across0.4.x.


<a id="commit-819"></a>
### 819 · docs: update getting-started {#commit-819}

[cc04cfd121302b82616570df393adcb264967bc9](https://github.com/EndstoneMC/endstone/commit/cc04cfd121302b82616570df393adcb264967bc9) · 2024-04-30T11:25:21Z · Vincent (author and committer).

Builds installation/bootstrap guide with disposable virtual environment rationale, pip/Docker choices, persisted Docker bind mount/UDP port, official server-download prompt and diagnostic console examples. Docs recommend isolation and verify via version command. Instructions reviewed, never executed; embedded output is authored example, not this review runtime evidence.


<a id="commit-820"></a>
### 820 · docs: update installation.md {#commit-820}

[673b1afc3711b42a8836084a64969f3f979b5746](https://github.com/EndstoneMC/endstone/commit/673b1afc3711b42a8836084a64969f3f979b5746) · 2024-04-30T11:29:42Z · Vincent (author and committer).

Repairs virtual-environment reference to local section.


<a id="commit-821"></a>
### 821 · docs: rename start-the-server.md to start-your-server.md {#commit-821}

[c6e354cc2fc645bebb2e2a833e09140edb420a5e](https://github.com/EndstoneMC/endstone/commit/c6e354cc2fc645bebb2e2a833e09140edb420a5e) · 2024-04-30T11:31:53Z · Vincent (author and committer).

Renames start-the-server→start-your-server/nav and fixes copied Material for MkDocs wording to Endstone.


<a id="commit-822"></a>
### 822 · docs: fix console logs {#commit-822}

[c61121e7033e3270112d760b02440f58bdbf617b](https://github.com/EndstoneMC/endstone/commit/c61121e7033e3270112d760b02440f58bdbf617b) · 2024-04-30T11:34:12Z · Vincent (author and committer).

Replaces development version in example console output with0.4.1 to align guide; edited illustrative log is not a separate observed production run.


<a id="commit-823"></a>
### 823 · docs: enable comment system for specific pages {#commit-823}

[a49cc83d42b4373c04e0541f872525705a37100a](https://github.com/EndstoneMC/endstone/commit/a49cc83d42b4373c04e0541f872525705a37100a) · 2024-04-30T11:38:30Z · Vincent (author and committer).

Enables opt-in comments on installation/start/first-plugin pages using804 template, not all docs.


<a id="commit-824"></a>
### 824 · docs: use conda as the environment for readthedocs {#commit-824}

[109fb9f8a4e8df9273f6c91a8984606516e910ff](https://github.com/EndstoneMC/endstone/commit/109fb9f8a4e8df9273f6c91a8984606516e910ff) · 2024-04-30T13:24:03Z · Vincent (author and committer).

Switches RTD to Mambaforge/Conda with Python3.12,Doxygen and pip docs dependencies; deletes requirements file. Experiment immediately reversed825, no explicit reason/results.


<a id="commit-825"></a>
### 825 · docs: use doxygen for c++ api reference {#commit-825}

[943603843b8a200806fb1d08c31ee507db578eb6](https://github.com/EndstoneMC/endstone/commit/943603843b8a200806fb1d08c31ee507db578eb6) · 2024-04-30T15:35:28Z · Vincent (author and committer).

Restores ordinary RTD Python/requirements exactly, replaces Conda experiment with MkDoxy C++ reference generation from public include/endstone excluding detail. Adds navigation and Python submodule grouping, hardcoded doxygen path removed833. Generated output not committed/read here, only generator config; claim of successful site build not supported.


<a id="commit-826"></a>
### 826 · docs: add build.commands {#commit-826}

[cb96d7df2cea4d5ec3281aa7f6b565fd0febfdb4](https://github.com/EndstoneMC/endstone/commit/cb96d7df2cea4d5ec3281aa7f6b565fd0febfdb4) · 2024-04-30T16:01:52Z · Vincent (author and committer).

Adds manual RTD install/mkdocs build commands as explicitly linked workaround for MkDoxy issue75. Issue body not examined in this unit; preserve stated dependency rationale rather than inventing bug details. Replaced832 with minimum version.


<a id="commit-827"></a>
### 827 · chore: game update v1.20.81 {#commit-827}

[a717a4fd6863f669751ce1ebee2062c6d01c0028](https://github.com/EndstoneMC/endstone/commit/a717a4fd6863f669751ce1ebee2062c6d01c0028) · 2024-04-30T16:16:15Z · Vincent (author and committer).

Updates Python game-version marker1.20.80→1.20.81 only.


<a id="commit-828"></a>
### 828 · docs: improve doxygen documentations {#commit-828}

[6624931b6a6757a5be1bec8a611a0e84145b7778](https://github.com/EndstoneMC/endstone/commit/6624931b6a6757a5be1bec8a611a0e84145b7778) · 2024-04-30T16:35:16Z · Vincent (author and committer).

Full broad Doxygen comment pass adds @brief/class descriptions across public API; no executable changes. Existing ActorSpawn cancellation wording still overstates prevention relative post-add despawn. Commentary not an independent correctness fix.


<a id="commit-829"></a>
### 829 · docs: minor fix {#commit-829}

[9f1cca68c37cb2f47781526d45fd5d236021a7ad](https://github.com/EndstoneMC/endstone/commit/9f1cca68c37cb2f47781526d45fd5d236021a7ad) · 2024-04-30T16:39:28Z · Vincent (author and committer).

Corrects namespace-list typo/C++ reference destination and missing ActorEvent @brief.


<a id="commit-830"></a>
### 830 · docs: update README.md {#commit-830}

[4b8c006b1da53de5fc84ebe6925036344eee6a16](https://github.com/EndstoneMC/endstone/commit/4b8c006b1da53de5fc84ebe6925036344eee6a16) · 2024-04-30T16:39:39Z · Vincent (author and committer).

README badge catches up with game-version marker1.20.81.


<a id="commit-831"></a>
### 831 · release: version 0.4.2 {#commit-831}

[613b1d40b5ced495ff203858807a1c61e94f3ab8](https://github.com/EndstoneMC/endstone/commit/613b1d40b5ced495ff203858807a1c61e94f3ab8) · 2024-04-30T16:40:06Z · Vincent (author and committer).

Releases0.4.2 marker and moves unreleased notes under dated release; changelog mistakenly claims game1.20.82 while Python/badge say1.20.81. Keep historical inconsistency, no guessed intended host version.


<a id="commit-832"></a>
### 832 · docs: update requirements.txt for readthedocs {#commit-832}

[6dd837b2c362ab4195ed9f3c428f277a4c2cb0df](https://github.com/EndstoneMC/endstone/commit/6dd837b2c362ab4195ed9f3c428f277a4c2cb0df) · 2024-05-01T09:47:14Z · Vincent (author and committer).

Removes manual RTD build-command workaround826 and requires mkdoxy>=1.2.3; returns build config to prior ordinary Python flow. Observed dependency-minimum replacement, no external issue/fix verification.


<a id="commit-833"></a>
### 833 · docs: add versions.json {#commit-833}

[9d43ade25990a2a10e8526d003026e4d042cfefb](https://github.com/EndstoneMC/endstone/commit/9d43ade25990a2a10e8526d003026e4d042cfefb) · 2024-05-01T10:09:10Z · Vincent (author and committer).

Adds latest/v0.4.2/stable-alias docs version manifest and removes absolute Doxygen executable path, allowing plugin discovery. No deployment proof.


<a id="commit-834"></a>
### 834 · docs: update versions.json {#commit-834}

[e3026684c5a7742d9705743c8934c6a24f23b457](https://github.com/EndstoneMC/endstone/commit/e3026684c5a7742d9705743c8934c6a24f23b457) · 2024-05-01T10:26:50Z · Vincent (author and committer).

Makes stable separate docs version entry rather than alias ofv0.4.2 and adds Python intersphinx inventory import. Explicit docs navigation state, not actual published versions verified.


<a id="commit-835"></a>
### 835 · docs: add logo {#commit-835}

[2ffbdca9f744558dbd35a4dd16f640504e509539](https://github.com/EndstoneMC/endstone/commit/2ffbdca9f744558dbd35a4dd16f640504e509539) · 2024-05-01T11:59:13Z · Vincent (author and committer).

Adds300x300pixel end-stone cube logo/favicon, visually inspected binary; fixes duplicated https site_url introduced810. Visual asset does not support independent personal engineering-style inference.


<a id="commit-836"></a>
### 836 · docs: add custom theme {#commit-836}

[f387e3ab14d836366bcca76cfbe8b8997fdcc44c](https://github.com/EndstoneMC/endstone/commit/f387e3ab14d836366bcca76cfbe8b8997fdcc44c) · 2024-05-01T12:39:14Z · Vincent (author and committer).

Adds light/dark semantic color variables and connects custom CSS to Material theme; no functional product API change. Full palette read, source origin/generation not stated. No browser rendering/accessibility validation.


<a id="commit-837"></a>
### 837 · docs: improve extra.css {#commit-837}

[39bf998ba940791717590df8deb2b354720cbc05](https://github.com/EndstoneMC/endstone/commit/39bf998ba940791717590df8deb2b354720cbc05) · 2024-05-01T16:14:20Z · Vincent (author and committer).

Extends palette mapping across default/code/footer/link colors; revises header/tab surfaces and rounded desktop search with hover/icon styling. Grouped with836–840 as documentation visual iteration, not repeated independent preferences.


<a id="commit-838"></a>
### 838 · docs: fix incorrect theme-color {#commit-838}

[12c2167ed9f6d0eb47c8a63dbeb340632e0c864e](https://github.com/EndstoneMC/endstone/commit/12c2167ed9f6d0eb47c8a63dbeb340632e0c864e) · 2024-05-01T21:19:51Z · Vincent (author and committer).

Fixes theme-color/header background with distinct wide-screen tab breakpoint76.25em, keeps search breakpoint60em. Scoped responsive change; title reports incorrect theme color but no screenshot or measured contrast evidence.


<a id="commit-839"></a>
### 839 · docs: update --md-default-fg-color--lightest {#commit-839}

[ee9f40319bb6c6680139eb9d338165e2a45714a4](https://github.com/EndstoneMC/endstone/commit/ee9f40319bb6c6680139eb9d338165e2a45714a4) · 2024-05-01T21:27:53Z · Vincent (author and committer).

Changes lightest foreground token to surface-container-high in both palettes, two verified CSS edits.


<a id="commit-840"></a>
### 840 · docs: increase the size of the app header {#commit-840}

[2e789bef8044aba3f823aefdd15765208b106557](https://github.com/EndstoneMC/endstone/commit/2e789bef8044aba3f823aefdd15765208b106557) · 2024-05-01T21:49:08Z · Vincent (author and committer).

Sets inner app-header height3.2rem, single visual adjustment.
