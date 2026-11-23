<!-- retrieval: {"source_ids":["public:commit:1700c54e1c881977cefa164edda0636e09a8ef33","public:commit:193e85836fccbf4c37238f8d396a443d8b0fe36a","public:commit:198e85f379712131a0b14ffeaf3ab91a77bff7e2","public:commit:2080396a772ce362a08d31a275cc20aca235fa16","public:commit:33b939ce48da6d7a539bdc8c833b0dee82c6d745","public:commit:468423a5dcf54f6a17138556e32694811430e824","public:commit:56b514781cb89a0a42fc17b51435dfdd61bc8cb3","public:commit:58f342b7f8badce2522ca4ff232c048a5f9c2f47","public:commit:632897f9c1248b548332a290a49d24a8e31e3e14","public:commit:988c0fe3c7010282f286501cf9672d9b46bd3693","public:commit:b59a30edc28743d3d874ff9987ce2495357c38bb","public:commit:b788daee0875bade173207c5ec874a8a5053b194","public:commit:cd9294a76f8ec3f822377bdcadde34eac0b06ff1","public:commit:dd37325b9febd68cce4c8d0d94aec5dd6197dbe6"],"source_type":"public","date":"2025-03-17..2025-03-23","topics":["lifetime","ffi","testing","build","api","diagnosis","review","selection","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Plugin resolution, parser contracts and bootstrap {#plugin-resolution-parser-contracts-and-bootstrap}

## Causal result {#causal-result}

The slice turns the previous candidate-staging work into a dependency-aware loader. [401](https://github.com/EndstoneMC/endstone/commit/988c0fe3c7010282f286501cf9672d9b46bd3693) deliberately delays manager admission until validation and onLoad succeed: dependency injection alone is not registration. The previous slice's failed-onLoad visibility no longer describes the main tip. Loader-owned objects can still exist outside the admitted manager list.

403 collects canonical names/provides, 404 sketches dependency traversal, and 405 finishes stalled-pass behavior. Hard dependencies must load successfully; missing soft edges are discarded; a stalled graph retries hard-ready plugins ignoring soft edges, then reports remaining candidates as circular. This is incremental implementation, not proof every intermediate commit builds:404 has unresolved graph references. Canonical names beat provides during candidate bookkeeping; duplicate candidate names log but the map retains the later candidate. Unordered traversal gives no stable ordering among otherwise independent plugins.

At500 the existing-soft-dependency branch of load_before appends the target name to its own dependency list instead of the declaring plugin. Also, batch loaded_plugins does not seed already registered plugins, and failed provider aliases can remain in provided-name bookkeeping. These are bounded source observations: diagnostics/order can differ from intended dependency behavior, but no dependency test or runtime failure was reproduced. The full resolver, disable and clear paths were reconciled in the endpoint snapshot. The prior service cleanup boundary persists: disable cancels tasks/unregisters event handlers; clear removes loaders and plugin maps, but neither invokes service unregister. No claim is made that an actual dangling service was observed.

## Syntax errors become values, then syntax expands {#syntax-errors-become-values-then-syntax-expands}

406 adopts expected<Result,string> for parser syntax errors and updates registration to log/continue. Its fourteen existing tests move with the contract.407 introduces literal, mandatory and optional anonymous enum syntax and generated names, with five successful cases and one malformed-input case. Removing the old '/command <text>' rejection test is correct for the newly valid one-value enum grammar, not evidence of casually reducing test quality. The function remains noexcept while allocation/formatting can still throw; the value-error contract concerns expected syntax failures. No test was executed.

## API experiments and delivery boundaries {#api-experiments-and-delivery-boundaries}

414 adds platform symbol lookup for a global server accessor;415 repairs Linux declaration;456 removes the entire public accessor/export. The removed cached raw Server pointer and fatal symbol-lookup paths therefore must not be reported as present at500. The message says refactor, without a broader authored reason. The plugin's added server-version log disappears with that API, not as a lost assertion.

420 changes cache selection to RelWithDebInfo keys, retaining generic fallback; no compiler flag change occurs in that patch.426 removes an obsolete Python network facade.427 passes the running interpreter path into native startup, but set-based candidate deduplication loses preferred ordering;428 supplies a browser User-Agent explicitly to avoid download timeouts, without proving a timeout improvement. Metadata request timeout and streaming-download timeout are different contracts.

Evidence: all per-commit records below, canonical parent patches, tip context manifest, and previous301–400 synthesis. Reasons above are explicit only where tied to messages/comments/contracts; other causal interpretation is reviewer inference.

<!-- PER-COMMIT RECORDS -->

## Individual commit records {#individual-commit-records}


<a id="commit-401"></a>
### 401. refactor: improve checks when loading plugins {#commit-401}

[988c0fe3c7010282f286501cf9672d9b46bd3693](https://github.com/EndstoneMC/endstone/commit/988c0fe3c7010282f286501cf9672d9b46bd3693) · 2025-03-17T16:39:04Z · author Vincent.

Parents: `9e1ac6a312bc2100fe6ab6fd9c3b7992b55dbee0`. Read displays: parent 1.

Moves name/restricted-name/duplicate/dependency checks into actual loadPlugin and registers plugin plus provides aliases only after onLoad succeeds. initPlugin becomes dependency injection only, reversing397's pre-registration visibility of failed onLoad candidates. Duplicate canonical names now reject; alias insertion uses emplace and does not overwrite existing lookup names. Bulk ordering is still unresolved until403–405. Loader ownership of rejected plugin objects is separate from manager admission.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-402"></a>
### 402. refactor: use ranges library for string transform {#commit-402}

[632897f9c1248b548332a290a49d24a8e31e3e14](https://github.com/EndstoneMC/endstone/commit/632897f9c1248b548332a290a49d24a8e31e3e14) · 2025-03-17T16:42:43Z · author Vincent.

Parents: `988c0fe3c7010282f286501cf9672d9b46bd3693`. Read displays: parent 1.

Replaces equivalent find/transform calls with ranges forms, const iterators and scoped if initializers across plugin/permission lookup. Lowercasing callback and behavior remain unchanged; no speed claim or independent algorithm change.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-403"></a>
### 403. feat: handle `provides` of plugins during loading {#commit-403}

[b788daee0875bade173207c5ec874a8a5053b194](https://github.com/EndstoneMC/endstone/commit/b788daee0875bade173207c5ec874a8a5053b194) · 2025-03-17T17:09:34Z · author Vincent.

Parents: `632897f9c1248b548332a290a49d24a8e31e3e14`. Read displays: parent 1.

Builds candidate-name/provided-alias maps and warns about collisions, but still loads each candidate during collection, so filesystem/input ordering remains effective. Duplicate names log then overwrite candidate map; canonical names take precedence over provides in bookkeeping. Duplicate-provides log has three placeholders but only two arguments, repaired405. Dependency maps are prepared but unused here.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-404"></a>
### 404. feat: add basic dependency resolution {#commit-404}

[193e85836fccbf4c37238f8d396a443d8b0fe36a](https://github.com/EndstoneMC/endstone/commit/193e85836fccbf4c37238f8d396a443d8b0fe36a) · 2025-03-17T18:12:01Z · author Vincent.

Parents: `b788daee0875bade173207c5ec874a8a5053b194`. Read displays: parent 1.

Stages iterative hard/soft dependency resolution and reverse soft edges for load_before, loading ready candidates and advertising their provided names after success. It references an undeclared dependency_graph and leaves stalled-pass handler empty, so this intermediate source is not a complete resolver. The existing-soft-dependency load_before branch appends the target's own name instead of current plugin, an ordering error retained405. No dependency-resolution tests added.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-405"></a>
### 405. feat: implement logics for depend, soft_depend, load_before and provides {#commit-405}

[2080396a772ce362a08d31a275cc20aca235fa16](https://github.com/EndstoneMC/endstone/commit/2080396a772ce362a08d31a275cc20aca235fa16) · 2025-03-17T20:55:28Z · author Vincent.

Parents: `193e85836fccbf4c37238f8d396a443d8b0fe36a`. Read displays: parent 1.

Completes stalled-pass handling: ignore soft edges to load a hard-ready candidate, otherwise report circular dependencies and terminate. Comments out unused graph calls and fixes ambiguous-provides log arguments. Hard lookup ultimately checks manager registration; missing/failed providers are not successful dependencies. However batch loaded_names excludes previously registered external plugins, and stale provided-name bookkeeping can produce circular rather than unknown diagnostics after a provider fails. unordered_map iteration leaves tie/soft-cycle order unspecified; no successful-run claim.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-406"></a>
### 406. refactor: use `expected` for error handling in `CommandUsageParser` {#commit-406}

[cd9294a76f8ec3f822377bdcadde34eac0b06ff1](https://github.com/EndstoneMC/endstone/commit/cd9294a76f8ec3f822377bdcadde34eac0b06ff1) · 2025-03-17T21:17:25Z · author Vincent.

Parents: `2080396a772ce362a08d31a275cc20aca235fa16`. Read displays: parent 1.

Replaces Boolean-plus-output-arguments and internal syntax exceptions with expected<Result,string> and explicit error propagation. Command registration logs an error and continues on parse failure, while successful result owns command/parameter strings. Fourteen existing parser tests migrate to the new result/error contract, preserving relevant syntax expectations. parse remains noexcept while allocations/formatting may throw, so expected syntax errors do not promise recovery from every exception. No tests executed.

All-parent changed-file occurrences: 4. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-407"></a>
### 407. feat: allow anonymous enums in command usages {#commit-407}

[56b514781cb89a0a42fc17b51435dfdd61bc8cb3](https://github.com/EndstoneMC/endstone/commit/56b514781cb89a0a42fc17b51435dfdd61bc8cb3) · 2025-03-17T22:57:02Z · author Vincent.

Parents: `cd9294a76f8ec3f822377bdcadde34eac0b06ff1`. Read displays: parent 1.

Adds literal/angle/square anonymous enum forms and deterministic generated parameter name/type, while keeping named enum syntax. Five positive shorthand cases and one unfinished-enum case are added; diagnostic positions/messages adapt to peek semantics. The old '/command <text>' error test is intentionally removed because this is now a valid one-value mandatory enum, not unexplained lost invalid-input coverage. Generated type names can collide and command registry's existing suffix logic handles name uniqueness; no property/fuzz test added.

All-parent changed-file occurrences: 3. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-414"></a>
### 414. feat: export 'endstone_getServer' to enable plugins to access the server singleton {#commit-414}

[198e85f379712131a0b14ffeaf3ab91a77bff7e2](https://github.com/EndstoneMC/endstone/commit/198e85f379712131a0b14ffeaf3ab91a77bff7e2) · 2025-03-18T21:29:02Z · author Vincent.

Parents: `e6de388bd977177480e67e65f525e523be116cce`. Read displays: parent 1.

Adds exported C endstone_getServer and inline dynamically resolved, cached public Server accessor; exits1 if symbol missing and excludes it from hook installation. Linux branch references undeclared get_server until415. Test plugin name/prefix expectation changes to test and logs server version. Cached raw server pointer lifetime across locator reset is not established by tests.

All-parent changed-file occurrences: 5. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-415"></a>
### 415. fix: compilation error on Linux {#commit-415}

[1700c54e1c881977cefa164edda0636e09a8ef33](https://github.com/EndstoneMC/endstone/commit/1700c54e1c881977cefa164edda0636e09a8ef33) · 2025-03-19T11:44:20Z · author Vincent.

Parents: `198e85f379712131a0b14ffeaf3ab91a77bff7e2`. Read displays: parent 1.

Declares Linux get_server variable and removes unused Boost include, repairing414's Linux source problem. No compile/run performed.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-420"></a>
### 420. ci: update cache key {#commit-420}

[b59a30edc28743d3d874ff9987ce2495357c38bb](https://github.com/EndstoneMC/endstone/commit/b59a30edc28743d3d874ff9987ce2495357c38bb) · 2025-03-21T13:31:20Z · author Vincent.

Parents: `fa33de07c476b06b9ad52a694b1b0545d246a931`. Read displays: parent 1.

Changes wheel and Windows portable Conan cache keys from Release to RelWithDebInfo, retaining generic fallback. This patch changes cache selection, not compiler flags.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-426"></a>
### 426. docs: remove obsolete module `endstone.network` {#commit-426}

[468423a5dcf54f6a17138556e32694811430e824](https://github.com/EndstoneMC/endstone/commit/468423a5dcf54f6a17138556e32694811430e824) · 2025-03-21T17:32:45Z · author Vincent.

Parents: `ce3437a9a15c992e8481a5de63dacdac5690a653`. Read displays: parent 1.

Deletes obsolete endstone.network facade and docs navigation, closing the prior slice's dangling facade for removed Packet types. Intentional public compatibility removal accompanying raw packet API.

All-parent changed-file occurrences: 3. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-427"></a>
### 427. feat: add `ENDSTONE_PYTHON_EXECUTABLE` environment variable {#commit-427}

[58f342b7f8badce2522ca4ff232c048a5f9c2f47](https://github.com/EndstoneMC/endstone/commit/58f342b7f8badce2522ca4ff232c048a5f9c2f47) · 2025-03-21T17:33:23Z · author Vincent.

Parents: `468423a5dcf54f6a17138556e32694811430e824`. Read displays: parent 1.

Bootstrap passes ENDSTONE_PYTHON_EXECUTABLE=sys.executable to loader, which adds it to candidates but deduplicates with set, losing priority. Candidate test only checks file existence, not executable/version. No process launched in this review.

All-parent changed-file occurrences: 2. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-428"></a>
### 428. chore: update user agent to avoid download timeout {#commit-428}

[33b939ce48da6d7a539bdc8c833b0dee82c6d745](https://github.com/EndstoneMC/endstone/commit/33b939ce48da6d7a539bdc8c833b0dee82c6d745) · 2025-03-21T17:45:19Z · author Vincent.

Parents: `58f342b7f8badce2522ca4ff232c048a5f9c2f47`. Read displays: parent 1.

Adds browser User-Agent with explicit download-timeout motivation and logs before download. Metadata request has10-second timeout; streaming download request still lacks timeout. No observed performance/success claim.

All-parent changed-file occurrences: 1. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.


<a id="commit-456"></a>
### 456. refactor: remove `endstone_getServer` {#commit-456}

[dd37325b9febd68cce4c8d0d94aec5dd6197dbe6](https://github.com/EndstoneMC/endstone/commit/dd37325b9febd68cce4c8d0d94aec5dd6197dbe6) · 2025-03-23T13:33:56Z · author Vincent.

Parents: `e277d632064fbb4dcdaa92607ca567e1be6b25ad`. Read displays: parent 1.

Removes public dynamic endstone::getServer plus exported endstone_getServer introduced414 and its test log. Hook enumeration no longer needs export exclusion/copy. Removes cached-pointer/API/process-exit surface; message gives refactor reason only.

All-parent changed-file occurrences: 4. Exact prior PR reuse: 0; exact reviewed-ancestry file reuse: 0.
