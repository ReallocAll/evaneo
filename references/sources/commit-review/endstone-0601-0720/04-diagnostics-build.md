<!-- retrieval: {"source_ids":["public:commit:0738832cbf5843678d9c5e06798b339aba28a06d","public:commit:0c53da2ff36edba1f6a8286c495932f8ae5853fc","public:commit:13a2d1d6329f1ec62259271b663bddc0b3b73c42","public:commit:15053d48a4ca9ec5b22f3f2896d95bcecb286b51","public:commit:2a69c9d289df638477182df97ef74f2dc2b8da3e","public:commit:4ad9e3883e42abb6ebbbbb0caecd09c65acc081c","public:commit:5cfc823324a8192b88da915dc96120ad1c7b7960","public:commit:60bbb2cf7fffd5239f16c7cf8328798a5646f3c7","public:commit:993057c734b6e9daebd9a99b11eca12a8add14ba","public:commit:c6b80cf19256bf2969ecf9dfc2d8774130a2ca00","public:commit:d58f3debe3df9c5a0ef7e195c06f789b0e51cbdb","public:commit:d649cd1bac987fb9d9a0160dd6330ca12069401a","public:commit:d90a2cf0e51ef02a55f9c5b9ef36ec3d401c2adf","public:commit:e1f2668bc3d21233efc1553e144082a443a74107","public:commit:f313a5bbbf4dacc61f1eef9109b3699aeb71aa6c","public:commit:f5be2894631f591135109f3dee9239121e06537b","public:commit:fab771cf18177c6c1f5b1e89cd9645ba9ffbb005"],"source_type":"public","date":"2024-04-10..2024-04-18","topics":["lifetime","concurrency","ffi","testing","build","performance","diagnosis","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Diagnostics and build evolution: usable symbols, fatal traces, targeted discovery {#diagnostics-and-build-evolution-usable-symbols-fatal-traces-targeted-discovery}

## Result and scope {#result-and-scope}

This sequence improves the ability to diagnose native failures and narrows symbol discovery while shipping optimized builds with debug information. It combines wheel/CI/Docker configuration, platform-specific lookup, cpptrace, fatal handlers and exception propagation. The explicit performance claim belongs to the Windows SymSearch replacement; no measured speedup is supplied. The LIEF→libelf replacement is observed, but its motive is not stated beyond the replacement title. [commit 653](https://github.com/EndstoneMC/endstone/commit/d649cd1bac987fb9d9a0160dd6330ca12069401a) [commit 659](https://github.com/EndstoneMC/endstone/commit/d58f3debe3df9c5a0ef7e195c06f789b0e51cbdb) [commit 669](https://github.com/EndstoneMC/endstone/commit/15053d48a4ca9ec5b22f3f2896d95bcecb286b51) [commit 671](https://github.com/EndstoneMC/endstone/commit/2a69c9d289df638477182df97ef74f2dc2b8da3e)

All source metadata here attributes author and committer to Vincent. Dependency authorship remains separate: adding cpptrace or libelf integration is not authorship of those libraries. Their external implementations were not independently inspected, downloaded or executed for this unit.

## 1. Debug information without widening hook selection {#1-debug-information-without-widening-hook-selection}

Wheel builds change from Release to RelWithDebInfo in Conan and scikit-build. Windows packages the runtime PDB. Docker is updated to the same Conan build type and Linux/Windows CI matrices add that mode. These adjacent repairs show build-mode alignment across delivery paths. They do not establish that any workflow ran successfully. [commit 653](https://github.com/EndstoneMC/endstone/commit/d649cd1bac987fb9d9a0160dd6330ca12069401a) [commit 656](https://github.com/EndstoneMC/endstone/commit/d90a2cf0e51ef02a55f9c5b9ef36ec3d401c2adf) [commit 657](https://github.com/EndstoneMC/endstone/commit/5cfc823324a8192b88da915dc96120ad1c7b7960)

The Windows hook scanner changes in the same first commit: runtime detours are explicitly selected from exported symbols with debug-symbol loading disabled, while executable targets still load their symbols. This is important when adding PDBs, because debug information should improve diagnostics without treating every debug symbol as a hook. Temporary info-level symbol/count logging is reduced immediately afterward. [commit 653](https://github.com/EndstoneMC/endstone/commit/d649cd1bac987fb9d9a0160dd6330ca12069401a) [commit 654](https://github.com/EndstoneMC/endstone/commit/e1f2668bc3d21233efc1553e144082a443a74107)

On UNIX, only the Python extension gets `--strip-debug --strip-unneeded` in RelWithDebInfo. The runtime retains its information, while Windows installs its PDB. That is selective packaging, not a universal preference for stripped binaries. The relative goals of artifact size versus runtime diagnostics are inferred from the target selection, not quoted as an explicit rationale. [commit 655](https://github.com/EndstoneMC/endstone/commit/c6b80cf19256bf2969ecf9dfc2d8774130a2ca00)

## 2. Logging repair: type/ownership boundary, exact crash cause unknown {#2-logging-repair-type-ownership-boundary-exact-crash-cause-unknown}

A commit explicitly reports a crash from `listd` and changes Bedrock log line splitting from string_view slices to owning std::string substrings. Full Logger context shows a virtual overload taking a string plus a fmt-format template overload. Selecting the literal-message path rather than a format conversion is a plausible mechanism; the actual crash stack and offending content are not supplied. It would be unjustified to declare a proven dangling-view failure merely because a view disappeared. [commit 658](https://github.com/EndstoneMC/endstone/commit/0738832cbf5843678d9c5e06798b339aba28a06d)

This matters methodologically: the claimed symptom is strong evidence of what motivated the repair, while the patch establishes the changed representation and overload boundary. Root-cause certainty requires more than those two facts. No test is added in the commit.

## 3. Stack traces and fatal handlers {#3-stack-traces-and-fatal-handlers}

cpptrace is added as a runtime dependency, and Windows bootstrap prepends runtime/plugin directories to the child process's symbol path while preserving existing entries. A noinline helper macro follows, but no use site changes in that commit. These prepare diagnostics before handlers are registered. [commit 659](https://github.com/EndstoneMC/endstone/commit/d58f3debe3df9c5a0ef7e195c06f789b0e51cbdb) [commit 660](https://github.com/EndstoneMC/endstone/commit/993057c734b6e9daebd9a99b11eca12a8add14ba)

Handlers are installed when the server thread starts, before PostWorld plugin enablement and server-load dispatch. Earlier bootstrap/runtime initialization is outside that registration point. Windows gets terminate, purecall and unhandled-exception handlers; the first two initially trace then abort, while the exception filter traces then continues normal exception search. Linux installs sigaction handlers for fatal/resource signals and traces before quick_exit(1). The source uses reset/deferral flags and reports sigaction setup failures; it does not preserve or restore earlier handlers. [commit 661](https://github.com/EndstoneMC/endstone/commit/0c53da2ff36edba1f6a8286c495932f8ae5853fc) [commit 662](https://github.com/EndstoneMC/endstone/commit/60bbb2cf7fffd5239f16c7cf8328798a5646f3c7)

Windows then adds SIGABRT and changes terminate/purecall to quick_exit(1). This prevents those handlers from routing their own abort through the newly added signal handler, an inference directly supported by control flow. It also makes clear that these paths are fatal diagnostics, not graceful plugin shutdown. The exception filter's continue-search policy remains different. Source-snippet trace output and exit handling are best-effort; no external cpptrace or platform signal-safety proof is present. [commit 663](https://github.com/EndstoneMC/endstone/commit/fab771cf18177c6c1f5b1e89cd9645ba9ffbb005)

The project also replaces several log-and-terminate sites with runtime_error: missing player identity, missing level association and missing original hook. This creates the possibility of propagation to an existing catch boundary; it does not demonstrate recoverability across every native ABI boundary. Uncaught exceptions can still reach the new terminate handler. In PyPlugin::getDescription, the catch logs and then `throw e` copies the caught std::exception expression rather than a bare rethrow; derived error identity can be lost. The surrounding onLoad/onEnable/onDisable methods still have their own log-and-suppress behavior. Avoid describing this as a uniform exception policy. [commit 664](https://github.com/EndstoneMC/endstone/commit/f313a5bbbf4dacc61f1eef9109b3699aeb71aa6c)

## 4. Linux symbol discovery becomes an explicit bounded scan {#4-linux-symbol-discovery-becomes-an-explicit-bounded-scan}

LIEF is replaced with libelf in CMake, Conan and runtime code; CI/Docker also install build-essential. The new scanner opens the file, starts ELF reading, finds a requested section type, iterates symbols and invokes a callback. Runtime detours come from defined global function entries in the dynamic table. Executable targets come from defined local functions in the static debug-symbol table, and only names present in the detour map are retained. Both platforms now return cached map references, using nonempty as the initialized sentinel. [commit 669](https://github.com/EndstoneMC/endstone/commit/15053d48a4ca9ec5b22f3f2896d95bcecb286b51)

The narrower scan makes the matching policy inspectable and avoids collecting unused target symbols. However, filtering changes are real semantics, not a library-only swap. The scanner stops after the first matching section, assumes table fields/data are usable, and cleans up ELF/file resources only at the success tail. Empty results cause a subsequent call to retry; a partial nonempty map after an exception could be treated as initialized later. These are bounded source consequences of this design, not an exhaustive malformed-ELF audit or a measured operational incident.

## 5. Windows lookup chooses public/global search {#5-windows-lookup-chooses-public-global-search}

Windows replaces SymEnumSymbols with SymSearch constrained to public/global symbols and adds elapsed-millisecond debug logging. Its message explicitly says this is to speed up lookup. It also replaces a random pseudo-handle with a duplicated current-process handle. Full endpoint context shows SymCleanup but no CloseHandle for that duplicated handle. No actual timings, benchmark workload or equivalence test establishes how much faster it is or whether every previous symbol remains discoverable. [commit 671](https://github.com/EndstoneMC/endstone/commit/2a69c9d289df638477182df97ef74f2dc2b8da3e)

This is a useful observed alternative: reduce the search population and cache results instead of repeatedly enumerating everything. It should not be generalized into a claim that all caches or narrower symbol filters are safe. Lifetime, empty/partial initialization and native version compatibility remain separate contracts.

## 6. Version semantics and validation evidence {#6-version-semantics-and-validation-evidence}

Conan development versions now bump the last version component before appending `.devN` whenever the tree is after a tag; exact-tag versions remain unchanged. That changes artifact identity and ordering, rather than only displaying a commit count. The implementation uses Version's internal item count; no new version test is included. [commit 673](https://github.com/EndstoneMC/endstone/commit/4ad9e3883e42abb6ebbbbb0caecd09c65acc081c)

The read CMake endpoint still uses recursive source/test globbing, so the extensive native source moves in the same range are picked up structurally without individual target-list edits. Existing tests target core/plugin loading, and changed Python tests cover imports. They do not establish crash-handler safety, symbol equivalence, native layout validity or ECS destruction behavior. No upstream code, build, test, container, bootstrap or host execution was performed during this research.

## Per-commit dispositions {#per-commit-dispositions}

<a id="commit-653"></a>
### 653. feat: build wheels with RelWithDebInfo {#commit-653}

Source: [d649cd1bac987fb9d9a0160dd6330ca12069401a](https://github.com/EndstoneMC/endstone/commit/d649cd1bac987fb9d9a0160dd6330ca12069401a); parent `9743cdccf357fa021c8ba2e4d18a41b6c74564d7`. Authored 2024-04-10T12:38:28Z. Disposition: meaningful.

Switches wheel Conan/scikit preset to RelWithDebInfo and installs Windows runtime PDB. Windows detour discovery explicitly restricts to export flags and disables PDB loading while targets still load symbols, preventing newly packaged debug symbols from broadening detour selection. Adds temporary info-level symbol logs removed654.

<a id="commit-654"></a>
### 654. fix: remove debug logs {#commit-654}

Source: [e1f2668bc3d21233efc1553e144082a443a74107](https://github.com/EndstoneMC/endstone/commit/e1f2668bc3d21233efc1553e144082a443a74107); parent `d649cd1bac987fb9d9a0160dd6330ca12069401a`. Authored 2024-04-10T13:04:24Z. Disposition: small-semantic.

Demotes per-detour logging from info to debug and removes count log. Small observability change only.

<a id="commit-655"></a>
### 655. feat: strip symbols for endstone_python on Linux {#commit-655}

Source: [c6b80cf19256bf2969ecf9dfc2d8774130a2ca00](https://github.com/EndstoneMC/endstone/commit/c6b80cf19256bf2969ecf9dfc2d8774130a2ca00); parent `e1f2668bc3d21233efc1553e144082a443a74107`. Authored 2024-04-10T13:04:41Z. Disposition: small-semantic.

For RelWithDebInfo UNIX builds strips debug/unneeded symbols only from Python extension, while preserving runtime debug information; keeps Windows runtime PDB install. Packaging has selective diagnostics/size tradeoff, not blanket stripping.

<a id="commit-656"></a>
### 656. fix: Dockerfile for building wheels with RelWithDebInfo {#commit-656}

Source: [d90a2cf0e51ef02a55f9c5b9ef36ec3d401c2adf](https://github.com/EndstoneMC/endstone/commit/d90a2cf0e51ef02a55f9c5b9ef36ec3d401c2adf); parent `c6b80cf19256bf2969ecf9dfc2d8774130a2ca00`. Authored 2024-04-10T13:05:36Z. Disposition: small-semantic.

Aligns Docker Conan build type with new RelWithDebInfo wheel preset; no container execution performed.

<a id="commit-657"></a>
### 657. ci: add RelWithDebInfo to build types for Linux and Windows {#commit-657}

Source: [5cfc823324a8192b88da915dc96120ad1c7b7960](https://github.com/EndstoneMC/endstone/commit/5cfc823324a8192b88da915dc96120ad1c7b7960); parent `d90a2cf0e51ef02a55f9c5b9ef36ec3d401c2adf`. Authored 2024-04-10T13:08:01Z. Disposition: small-semantic.

Adds RelWithDebInfo to Linux/Windows CI build matrix, broadening configured validation for newly shipped mode. This is workflow intent, not evidence jobs passed.

<a id="commit-658"></a>
### 658. fix: crash when executing `listd` command {#commit-658}

Source: [0738832cbf5843678d9c5e06798b339aba28a06d](https://github.com/EndstoneMC/endstone/commit/0738832cbf5843678d9c5e06798b339aba28a06d); parent `5cfc823324a8192b88da915dc96120ad1c7b7960`. Authored 2024-04-10T22:23:32Z. Disposition: meaningful.

Reported listd crash fix replaces string_view line slices with owning std::string substrings in Bedrock logging bridge. Difference is ownership/type across logger overload boundary; exact failing stack/root cause is not supplied in commit, so avoid attributing it to a proven dangling view. Full Logger context exposes a string-taking virtual overload and a fmt-format template; choosing the literal-message overload is a plausible mechanism, while the exact crash trace remains unknown.

<a id="commit-659"></a>
### 659. feat: add cpptrace for stacktrace {#commit-659}

Source: [d58f3debe3df9c5a0ef7e195c06f789b0e51cbdb](https://github.com/EndstoneMC/endstone/commit/d58f3debe3df9c5a0ef7e195c06f789b0e51cbdb); parent `0738832cbf5843678d9c5e06798b339aba28a06d`. Authored 2024-04-11T11:45:29Z. Disposition: meaningful.

Adds cpptrace0.5.2 runtime dependency and Windows child-process symbol lookup paths for runtime/plugins while preserving prior environment paths. Enables later diagnostics rather than installing crash handlers itself.

<a id="commit-660"></a>
### 660. feat: add ENDSTONE_NOINLINE macro {#commit-660}

Source: [993057c734b6e9daebd9a99b11eca12a8add14ba](https://github.com/EndstoneMC/endstone/commit/993057c734b6e9daebd9a99b11eca12a8add14ba); parent `d58f3debe3df9c5a0ef7e195c06f789b0e51cbdb`. Authored 2024-04-11T15:03:50Z. Disposition: small-semantic.

Defines cross-compiler ENDSTONE_NOINLINE macro with inline linkage semantics; no callsite changes in this commit.

<a id="commit-661"></a>
### 661. feat: implement crash handler for Windows {#commit-661}

Source: [0c53da2ff36edba1f6a8286c495932f8ae5853fc](https://github.com/EndstoneMC/endstone/commit/0c53da2ff36edba1f6a8286c495932f8ae5853fc); parent `993057c734b6e9daebd9a99b11eca12a8add14ba`. Authored 2024-04-11T15:07:07Z. Disposition: meaningful.

Registers Windows terminate/purecall/unhandled-exception handlers on server-thread-start, before PostWorld plugins. Generates source-snippet traces; terminate/purecall abort and exception filter continues search. Diagnostics do not recover corrupted execution; startup before registration remains outside this hook coverage.

<a id="commit-662"></a>
### 662. feat: implement crash handler for Linux {#commit-662}

Source: [60bbb2cf7fffd5239f16c7cf8328798a5646f3c7](https://github.com/EndstoneMC/endstone/commit/60bbb2cf7fffd5239f16c7cf8328798a5646f3c7); parent `0c53da2ff36edba1f6a8286c495932f8ae5853fc`. Authored 2024-04-11T15:35:49Z. Disposition: meaningful.

Adds Linux sigaction handlers for fatal/resource signals using SA_SIGINFO/NODEFER/RESETHAND, trace then quick_exit1. No saved-handler restoration or proven async-signal-safe trace path in source. Treat as best-effort fatal diagnostics, not reliable recovery or graceful plugin teardown.

<a id="commit-663"></a>
### 663. feat: add signal handler for SIGABRT on Windows {#commit-663}

Source: [fab771cf18177c6c1f5b1e89cd9645ba9ffbb005](https://github.com/EndstoneMC/endstone/commit/fab771cf18177c6c1f5b1e89cd9645ba9ffbb005); parent `60bbb2cf7fffd5239f16c7cf8328798a5646f3c7`. Authored 2024-04-11T15:36:10Z. Disposition: meaningful.

Adds Windows SIGABRT handler and changes terminate/purecall from abort to quick_exit1, preventing those paths from recursively routing through new abort handler. Prints purecall marker. Exception-filter continue-search policy unchanged.

<a id="commit-664"></a>
### 664. refactor: replace logging and termination with throwing exceptions {#commit-664}

Source: [f313a5bbbf4dacc61f1eef9109b3699aeb71aa6c](https://github.com/EndstoneMC/endstone/commit/f313a5bbbf4dacc61f1eef9109b3699aeb71aa6c); parent `fab771cf18177c6c1f5b1e89cd9645ba9ffbb005`. Authored 2024-04-11T15:50:35Z. Disposition: meaningful.

Replaces several critical-log/terminate paths with runtime_error for missing identity, missing level and missing hook original. PyPlugin::getDescription override logs caught exception then uses throw e, which copies/slices its std::exception static type rather than preserving a derived exception. Uncaught exceptions can still reach newly installed fatal handler; this does not prove recoverability.

<a id="commit-669"></a>
### 669. refactor(deps): replace LIEF with libelf {#commit-669}

Source: [15053d48a4ca9ec5b22f3f2896d95bcecb286b51](https://github.com/EndstoneMC/endstone/commit/15053d48a4ca9ec5b22f3f2896d95bcecb286b51); parent `155b58615e1f3ffba3ef3285889e68b0bf07f656`. Authored 2024-04-12T17:05:27Z. Disposition: meaningful.

Replaces Linux LIEF with libelf across Conan/CMake/CI/Docker and hand-writes ELF scan: dynamic global defined function detours; static local defined function targets filtered against detour names. Both platforms cache maps by nonempty sentinel and return const references. Reduces target collection, but empty results retry and ELF cleanup only occurs on success, not exceptions. No explicit rationale for library choice beyond replacement title.

<a id="commit-670"></a>
### 670. refactor: remove redundant pragma once in source file {#commit-670}

Source: [f5be2894631f591135109f3dee9239121e06537b](https://github.com/EndstoneMC/endstone/commit/f5be2894631f591135109f3dee9239121e06537b); parent `15053d48a4ca9ec5b22f3f2896d95bcecb286b51`. Authored 2024-04-12T17:08:34Z. Disposition: mechanical.

Removes redundant pragma once from Windows source file; no runtime change.

<a id="commit-671"></a>
### 671. feat: replace SymEnumSymbols with SymSearch to speed up symbol lookup on Windows {#commit-671}

Source: [2a69c9d289df638477182df97ef74f2dc2b8da3e](https://github.com/EndstoneMC/endstone/commit/2a69c9d289df638477182df97ef74f2dc2b8da3e); parent `f5be2894631f591135109f3dee9239121e06537b`. Authored 2024-04-12T23:35:38Z. Disposition: meaningful.

Explicit performance motive: SymEnumSymbols→SymSearch public/global symbol query with elapsed-time debug logging. Replaces random pseudo handle with duplicated process handle; source performs SymCleanup but no CloseHandle. No benchmark values or full symbol-equivalence proof supplied.

<a id="commit-673"></a>
### 673. fix(conan): bump version for dev builds {#commit-673}

Source: [4ad9e3883e42abb6ebbbbb0caecd09c65acc081c](https://github.com/EndstoneMC/endstone/commit/4ad9e3883e42abb6ebbbbb0caecd09c65acc081c); parent `23c6a56c43afaac621d52342f060c859a8fc10b4`. Authored 2024-04-13T01:38:47Z. Disposition: small-semantic.

Development Conan versions now bump last version component before appending .devN whenever commits follow tag; exact-tag versions unchanged. This changes version ordering/identity rather than simply incrementing a fixed release string. Uses Version internal _items length.

<a id="commit-707"></a>
### 707. refactor: clean up includes in event_coordinator.cpp {#commit-707}

Source: [13a2d1d6329f1ec62259271b663bddc0b3b73c42](https://github.com/EndstoneMC/endstone/commit/13a2d1d6329f1ec62259271b663bddc0b3b73c42); parent `776e1735e16ff0e6994dcfd71aefdf487e864315`. Authored 2024-04-18T15:53:24Z. Disposition: mechanical.

Removes unused cpptrace include after exploratory coordinator diagnostics remain commented; no active behavior change.
