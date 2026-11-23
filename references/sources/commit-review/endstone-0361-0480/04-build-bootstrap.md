<!-- retrieval: {"source_ids":["public:commit:1a3ca242e96404ae8448f514f392d294e6671237","public:commit:33d72b923df2da37ca56ae8b28c0a88f4127ff17","public:commit:3cb927c7ef9ce24dc082185d6966aa5c8ff79e32","public:commit:48d9572c7b7887044e763a351041f42bb6547b19","public:commit:4b41d9d19fdfeb6e50fcd32be82930a2378797dd","public:commit:56e278a054cfc1764f8a14100aeac961820aca40","public:commit:5dc491617359564fb932edcd83106331ef5f4149","public:commit:91b22581a2ad8a944a732dc57d42879ac404e2fb","public:commit:98cff100c4cf64d07d8d08a1b5a3ff233e76336f","public:commit:a1bfae25c3fe35e9d871a79b2c92c63ecbe65fc1","public:commit:ac2265206c578c7d3285c86ee01b983bb8e4c47e","public:commit:ad2ae11cf58726f09d8ec2de3fee718e12076228","public:commit:b55e3194a8816b27e7d9f2e933285cb281269e1b","public:commit:c22850004f2bbfa43e5218ad32d74f7efa4371fa","public:commit:d40d153a940eaf1cffa50a5a553ca0b7b60435a8","public:commit:d584f661dbb9f770563ec593af6959acca8458e0","public:commit:d788a0b730dbc5c896d1b8850b2924712392870a"],"source_type":"public","date":"2024-03-13..2024-03-21","topics":["concurrency","ffi","testing","build","performance","recovery","api","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Bootstrap validation, persistent deployment and release surfaces {#bootstrap-validation-persistent-deployment-and-release-surfaces}

## Result and proportionate scope {#result-and-proportionate-scope}

The build/deployment changes in this range are small compared with the plugin redesign, but several alter actual behavior and cannot be dismissed as version or formatting noise. The main mechanisms are preserving validation under optimized Python, retaining a required native wait, adding persistent Compose storage, updating the artifact topology for CI v4 actions and separating game-version selection from framework version. Pure formatting, roadmap status and generated-signature changes receive concise individual dispositions after full diff verification.

No bootstrap, native injection API, server, container, workflow or package build was executed. Statements below concern source behavior and declared configuration, not measured deployment success. Public documentation URLs embedded in source were not independently fetched in this unit.

## Assertions were doing more than checking programmer invariants {#assertions-were-doing-more-than-checking-programmer-invariants}

361 converts the Linux dladdr result assertion into an explicit ValueError. 362 does the same for installation and remote-version checks, using FileNotFoundError for a nonempty installation directory missing the executable. These failures are runtime/environment conditions rather than development-only invariants. An assert carrying an exception object still raises AssertionError when active; it does not raise that supplied object as its own type. Explicit raise establishes both unconditional evaluation and the intended exception class.

363 applies the change to Windows process/injection checks. The important case is WaitForSingleObject: previously the call itself appeared inside an assertion expression. With optimized Python, the entire expression could disappear, removing the wait before continuing the bootstrap. Moving it into an ordinary conditional preserves an operation as well as its error check. This mechanism is clear from the diff without executing Windows APIs.

The patch does not redesign cleanup for partially initialized process, memory and handle resources, and it should not be described as a complete resource-safety fix. Full endpoint platform context was read to understand the call sequence and verify that the checks remained in their intended positions. The review did not execute the code or seek wider injection changes.

362 also adds explicit shell=False to the common Popen call, and 364 removes it. Full Linux and Windows caller context shows that neither current caller supplies shell: Linux passes an environment and Windows passes suspended-creation flags. The removal therefore retains the default for these actual callers. It allows the generic kwargs entry point to accept a shell keyword without duplicate-keyword failure, but there is no such call shown. It would be incorrect to infer that 364 enables a shell merely from deleting an explicit false value.

365 removes an f prefix from a string containing no interpolation. The verified log text, integrity check and control flow remain unchanged. This is exactly the kind of mechanical patch that deserves identity preservation without an inflated design essay.

## Deployment storage becomes explicit {#deployment-storage-becomes-explicit}

367 adds Compose configuration with a local build, an image tag, UDP 19132, restart policy, interactive terminal and a writable bind mount for the server directory. The mount supplies an explicit host persistence path missing from the earlier bare Docker invocation examples. Build context and image tag are separate choices: naming an image latest does not prove it was pulled, built or updated successfully.

The Compose configuration declares lifecycle and storage behavior; it does not demonstrate that a server starts, that ownership/permissions of existing host files are correct or that backups exist. The source was read, not deployed. This preserves the useful operational change without inventing a successful environment test.

## CI dependency versions can change workflow topology {#ci-dependency-versions-can-change-workflow-topology}

384 updates Codecov's action version. Only in-repository configuration is reviewed; the action implementation and external release notes were not read here. The token is a secret reference, not a captured credential value. No coverage upload result is inferred.

385 updates upload/download artifact actions to v4 and also changes artifact naming and retrieval. Matrix outputs acquire OS/Python-specific names, the source distribution has its own name, and the downstream download uses a pattern with merge-multiple. The naming and collection changes are meaningful: the workflow no longer relies on all matrix jobs contributing to one identically named artifact. This is therefore more than a text-only dependency bump, even though its rationale can be understood from the local configuration. No CI run was executed or independently verified.

## Public API and release version dimensions remain distinct {#public-api-and-release-version-dimensions-remain-distinct}

408 introduces a selected Minecraft version literal separate from the framework package version. 451 advances that selection from 1.20.71 to 1.20.72 and updates a badge; the actual changed content is a bounded version selection, not evidence of a new compatibility suite. 452 exports both the generated framework version and the game version from the Python package root, then uses the game version in bootstrap construction and prompting. This centralizes the Python selection source without conflating it with the package's release identifier.

414 defines the public header version and stringification helpers. 463 is not classified as routine version noise because it also changes the Python accepted API list while native exact-major.minor compatibility stays in place. The compatibility mechanics and their limitations are in the plugin dossier. The framework version, native API version, Python declared API version and selected Minecraft version are different contracts; a single number cannot safely substitute for the others.

412 centralizes the export macro behind an override guard. That is a source/build integration surface, not a claim that every compiler/export configuration was tested. 413 temporarily disables a member-to-static lint rule, restored in 435 after API-version storage changes. This adjacent disable/restore chain should be retained rather than interpreted as a lasting preference against the rule.

## Roadmaps and attribution {#roadmaps-and-attribution}

370, 442 and 461 update permission milestone status. These are dated claims about project progress. The implementation still contains specific gaps, including unresolved dependency scheduling and the permission caveats described in the other dossiers. A checked roadmap item is not test evidence or a warrant to erase those counterexamples.

382 adjusts README presentation and records author Vincent (Zhengyu) Wu with GitHub as committer; the other commits in this sequence record Vincent as both author and committer. The GitHub committer identity does not imply separate human review or endorsement. No PR or issue discussion is included here, so collaborator objections or approvals are unknown.

## Applying this evidence {#applying-this-evidence}

Useful operational checks suggested by these changes are narrow and concrete: does optimization remove required side effects, do actual kwargs callers preserve a claimed default, where does persistent server state live, how are matrix artifacts named and collected, and which version dimension controls a compatibility decision? These questions arise from verified changes and reversals. No universal workflow preference or present-day platform recommendation is inferred.

## Individual commit evidence {#individual-commit-evidence}

<a id="commit-361"></a>
### 361. refactor: use raise instead of assert {#commit-361}

Source: [98cff100c4cf64d07d8d08a1b5a3ff233e76336f](https://github.com/EndstoneMC/endstone/commit/98cff100c4cf64d07d8d08a1b5a3ff233e76336f) · authored 2024-03-13T17:51:16Z · parent `fb62ba97b2851a070c0b78ae0647f7da63ca0f6e`.

Author: **Vincent**.

Replaces Linux dladdr assertion with explicit ValueError, preserving failure validation under optimized Python and raising the intended exception type rather than AssertionError carrying an exception object. Native library discovery itself is unchanged.

Changed paths: `python/src/endstone/_internal/bootstrap/linux.py`.

Coverage: 16 canonical patch lines; 1 changed paths.

<a id="commit-362"></a>
### 362. refactor: use raise instead of assert {#commit-362}

Source: [3cb927c7ef9ce24dc082185d6966aa5c8ff79e32](https://github.com/EndstoneMC/endstone/commit/3cb927c7ef9ce24dc082185d6966aa5c8ff79e32) · authored 2024-03-13T17:56:20Z · parent `98cff100c4cf64d07d8d08a1b5a3ff233e76336f`.

Author: **Vincent**.

Uses FileNotFoundError for a nonempty installation lacking its executable and ValueError for unavailable remote version, removing optimized-away assertions. Drops obsolete cross-platform-directory hint after earlier platform subdirectories. Adds explicit shell=False, removed in 364. Full platform caller context confirms neither current Linux nor Windows caller overrides shell, so that adjacent keyword addition/removal does not change these callers. No installation recovery or network tests added.

Changed paths: `python/src/endstone/_internal/bootstrap/base.py`.

Coverage: 36 canonical patch lines; 1 changed paths.

<a id="commit-363"></a>
### 363. refactor: use raise instead of assert {#commit-363}

Source: [33d72b923df2da37ca56ae8b28c0a88f4127ff17](https://github.com/EndstoneMC/endstone/commit/33d72b923df2da37ca56ae8b28c0a88f4127ff17) · authored 2024-03-13T18:00:44Z · parent `3cb927c7ef9ce24dc082185d6966aa5c8ff79e32`.

Author: **Vincent**.

Converts Windows allocation, memory-write, symbol lookup, remote-thread, snapshot and thread-opening assertions to explicit errors. This preserves checks under optimization and, crucially, preserves the WaitForSingleObject call formerly inside assert itself. Existing resource cleanup/partial-start behavior is not redesigned. Source-only review; no injection or host APIs executed.

Changed paths: `python/src/endstone/_internal/bootstrap/windows.py`.

Coverage: 71 canonical patch lines; 1 changed paths.

<a id="commit-364"></a>
### 364. fix: remove shell=False in subprocess.Popen {#commit-364}

Source: [ad2ae11cf58726f09d8ec2de3fee718e12076228](https://github.com/EndstoneMC/endstone/commit/ad2ae11cf58726f09d8ec2de3fee718e12076228) · authored 2024-03-13T18:01:29Z · parent `33d72b923df2da37ca56ae8b28c0a88f4127ff17`.

Author: **Vincent**.

Removes explicit shell=False added in 362 from common subprocess.Popen call. Full Linux and Windows caller context confirms neither passes shell; omission therefore retains the normal default for these callers. The generic kwargs entry point can now accept a shell keyword without duplicate-keyword failure, but no such call is shown. This is a bounded parameter reversal, not evidence that a shell was enabled.

Changed paths: `python/src/endstone/_internal/bootstrap/base.py`.

Coverage: 12 canonical patch lines; 1 changed paths.

<a id="commit-365"></a>
### 365. refactor: remove unnecessary f-string {#commit-365}

Source: [5dc491617359564fb932edcd83106331ef5f4149](https://github.com/EndstoneMC/endstone/commit/5dc491617359564fb932edcd83106331ef5f4149) · authored 2024-03-13T21:59:18Z · parent `ad2ae11cf58726f09d8ec2de3fee718e12076228`.

Author: **Vincent**.

Removes f prefix from a string with no interpolated expressions. Log content, hash verification and control flow unchanged.

Changed paths: `python/src/endstone/_internal/bootstrap/base.py`.

Coverage: 13 canonical patch lines; 1 changed paths.

<a id="commit-367"></a>
### 367. feat: add docker-compose.yml {#commit-367}

Source: [1a3ca242e96404ae8448f514f392d294e6671237](https://github.com/EndstoneMC/endstone/commit/1a3ca242e96404ae8448f514f392d294e6671237) · authored 2024-03-13T23:21:00Z · parent `d4faa50098c38757b02e91f2f256c3afbc38dd28`.

Author: **Vincent**.

Adds Compose configuration with local build/latest image, UDP19132, unless-stopped restart, interactive terminal and writable server-directory bind mount. This addresses persistent host storage missing from earlier bare docker-run examples. Image identity and local Dockerfile source selection remain separate; configuration was read, not built or deployed.

Changed paths: `docker-compose.yml`.

Coverage: 21 canonical patch lines; 1 changed paths.

<a id="commit-370"></a>
### 370. docs: update README.md {#commit-370}

Source: [b55e3194a8816b27e7d9f2e933285cb281269e1b](https://github.com/EndstoneMC/endstone/commit/b55e3194a8816b27e7d9f2e933285cb281269e1b) · authored 2024-03-14T16:03:31Z · parent `7fdb675775a24c1d43133290c160df9ce9549999`.

Author: **Vincent**.

Updates roadmap permission core to done and C++/Python APIs underway. Dated project-status claim, not evidence all invalidation and precedence issues are resolved.

Changed paths: `README.md`.

Coverage: 13 canonical patch lines; 1 changed paths.

<a id="commit-382"></a>
### 382. docs: update README.md {#commit-382}

Source: [91b22581a2ad8a944a732dc57d42879ac404e2fb](https://github.com/EndstoneMC/endstone/commit/91b22581a2ad8a944a732dc57d42879ac404e2fb) · authored 2024-03-15T00:20:31Z · parent `e88dfe406dcfa869f665c27a9dd8a666dae5d736`.

Author: **Vincent (Zhengyu) Wu**.

Moves HTML closing div so README badges join centered header. Git author is Vincent (Zhengyu) Wu and committer GitHub, preserved separately; no collaborator design attribution inferred from web commit.

Changed paths: `README.md`.

Coverage: 21 canonical patch lines; 1 changed paths.

<a id="commit-384"></a>
### 384. ci: update codecov-action to {#commit-384}

Source: [ac2265206c578c7d3285c86ee01b983bb8e4c47e](https://github.com/EndstoneMC/endstone/commit/ac2265206c578c7d3285c86ee01b983bb8e4c47e) · authored 2024-03-15T00:44:09Z · parent `c4bf5f89b658d8014f235346d96b2a31510fa489`.

Author: **Vincent**.

Updates Codecov action v3 to v4 without changing token reference. Dependency major-version bump verified from diff; action implementation/release behavior and actual upload result not independently reviewed.

Changed paths: `.github/workflows/coverage.yml`.

Coverage: 12 canonical patch lines; 1 changed paths.

<a id="commit-385"></a>
### 385. ci: update upload-artifact action to v4 {#commit-385}

Source: [56e278a054cfc1764f8a14100aeac961820aca40](https://github.com/EndstoneMC/endstone/commit/56e278a054cfc1764f8a14100aeac961820aca40) · authored 2024-03-15T00:49:00Z · parent `ac2265206c578c7d3285c86ee01b983bb8e4c47e`.

Author: **Vincent**.

Migrates upload/download artifact actions to v4 and assigns unique OS/Python wheel names plus separate sdist name, then downloads endstone-* and merges outputs. Separates concurrent producers instead of sharing one artifact name. This is workflow topology adaptation, not only version noise; no workflow run or artifact collision result observed.

Changed paths: `.github/workflows/wheel.yml`.

Coverage: 54 canonical patch lines; 1 changed paths.

<a id="commit-408"></a>
### 408. feat: separate minecraft server version from endstone version {#commit-408}

Source: [d788a0b730dbc5c896d1b8850b2924712392870a](https://github.com/EndstoneMC/endstone/commit/d788a0b730dbc5c896d1b8850b2924712392870a) · authored 2024-03-19T17:53:26Z · parent `4ec9854cc82a6aacaf4e3719b03c9e257094caea`.

Author: **Vincent**.

Stops deriving server game version from Endstone package version and selects1.20.71 explicitly. Separates release axes so API/framework semver need not encode game version. Later 451/452 centralize and update this value; no remote-download result observed.

Changed paths: `python/src/endstone/_internal/bootstrap/__init__.py`.

Coverage: 22 canonical patch lines; 1 changed paths.

<a id="commit-413"></a>
### 413. style: update "readability-convert-member-functions-to-static" rule to .clang-tidy {#commit-413}

Source: [a1bfae25c3fe35e9d871a79b2c92c63ecbe65fc1](https://github.com/EndstoneMC/endstone/commit/a1bfae25c3fe35e9d871a79b2c92c63ecbe65fc1) · authored 2024-03-19T23:57:46Z · parent `106d7e0571e115b740962dcb9c5c62c5ae6ecf37`.

Author: **Vincent**.

Disables clang-tidy conversion of member functions to static. Explicit lint-policy choice, with no stated motive or measured impact; do not generalize into a universal design preference.

Changed paths: `.clang-tidy`.

Coverage: 12 canonical patch lines; 1 changed paths.

<a id="commit-427"></a>
### 427. style: update clang-tidy config for protected member naming {#commit-427}

Source: [48d9572c7b7887044e763a351041f42bb6547b19](https://github.com/EndstoneMC/endstone/commit/48d9572c7b7887044e763a351041f42bb6547b19) · authored 2024-03-20T11:42:51Z · parent `323b64b3ee3e0d77fa72a4983c1579c22ff9c76c`.

Author: **Vincent**.

Changes protected-member naming rule from camelBack to lower_case while preserving underscore suffix. Explicit style configuration only; no semantic code rewrite.

Changed paths: `.clang-tidy`.

Coverage: 13 canonical patch lines; 1 changed paths.

<a id="commit-442"></a>
### 442. docs: update README.md {#commit-442}

Source: [c22850004f2bbfa43e5218ad32d74f7efa4371fa](https://github.com/EndstoneMC/endstone/commit/c22850004f2bbfa43e5218ad32d74f7efa4371fa) · authored 2024-03-20T16:11:47Z · parent `65d51747dc1dd3a91769c32baa94e6dd4fb49a2f`.

Author: **Vincent**.

README marks C++ permissions complete while manager comment explicitly lists dependency/provides/load-before handling as TODO. Preserve this distinction: phase-aware enable is implemented; dependency graph ordering is not. No behavior change beyond documentation.

Changed paths: `README.md`, `src/endstone_core/plugin/plugin_manager.cpp`.

Coverage: 25 canonical patch lines; 2 changed paths.

<a id="commit-451"></a>
### 451. chore(game): update to v1.20.72 {#commit-451}

Source: [d584f661dbb9f770563ec593af6959acca8458e0](https://github.com/EndstoneMC/endstone/commit/d584f661dbb9f770563ec593af6959acca8458e0) · authored 2024-03-21T00:30:31Z · parent `84b664a602510b74587ea0edf851644ca2d80a32`.

Author: **Vincent**.

Updates selected game version 1.20.71→1.20.72 and README badge. Actual diff verified as version selection only; no host compatibility or download test result inferred.

Changed paths: `README.md`, `python/src/endstone/_internal/bootstrap/__init__.py`.

Coverage: 25 canonical patch lines; 2 changed paths.

<a id="commit-452"></a>
### 452. refactor: move versions to main module's __init__.py {#commit-452}

Source: [d40d153a940eaf1cffa50a5a553ca0b7b60435a8](https://github.com/EndstoneMC/endstone/commit/d40d153a940eaf1cffa50a5a553ca0b7b60435a8) · authored 2024-03-21T00:40:49Z · parent `d584f661dbb9f770563ec593af6959acca8458e0`.

Author: **Vincent**.

Exports framework version and separate game version from package root and consumes game version in bootstrap construction/prompt. Establishes one Python game-version source while package version remains generated. Existing users relying on empty root module now import generated version; package build completeness is a separate concern.

Changed paths: `python/src/endstone/__init__.py`, `python/src/endstone/_internal/bootstrap/__init__.py`.

Coverage: 38 canonical patch lines; 2 changed paths.

<a id="commit-461"></a>
### 461. docs: update README.md {#commit-461}

Source: [4b41d9d19fdfeb6e50fcd32be82930a2378797dd](https://github.com/EndstoneMC/endstone/commit/4b41d9d19fdfeb6e50fcd32be82930a2378797dd) · authored 2024-03-21T02:21:36Z · parent `a8c971e280fc5dc2112b9eb1e7ff1959ae0f677d`.

Author: **Vincent**.

README marks Python permission API complete. Dated milestone claim only; no tests or implementation changes.

Changed paths: `README.md`.

Coverage: 13 canonical patch lines; 1 changed paths.
