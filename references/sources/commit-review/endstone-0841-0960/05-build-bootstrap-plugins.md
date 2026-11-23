<!-- retrieval: {"source_ids":["public:commit:156f1e78cefba672cad3763334719bffbabe643c","public:commit:15f67c00450c7b0e6e0c3f984f1bbdfd52cec47e","public:commit:1bdfd86452fcf00b9243a213602faed25094ec2d","public:commit:258a2b1ecc7b5e9eb7054a6cc3ff5a3c33bc838b","public:commit:299e2da5a0304cf855ed3a59293f1e0f7b624bb8","public:commit:376a0cd80061b1ed5f218d7b10e0742d4d6c870f","public:commit:38657d6f2cfa5af1ffed922b66ac467aa7024276","public:commit:44e8c679b9e1ce8fd7b3e3546079d28c3d677585","public:commit:4c237c74b684f8d6e37c02967d6bcce6b5a01deb","public:commit:503ac64026664aa1183270b7eac34f6e1e15ab25","public:commit:556c2c160d398466dd16c071bbaa840973f0c336","public:commit:55c7f785dd4161625ba9ed370587d2489e914129","public:commit:5988237298428340c9140574eb7a6ed0572878d2","public:commit:6ce1842ad18bf9823e7279c642e59e22eb4b30b8","public:commit:6e0a9ca943a02ab61c367e146ab6c196ddddd706","public:commit:712c80fcaf7248e803a7c36c39998f4566a9970a","public:commit:72fbc553ea700893c3e369fdd3e02705e62b1a70","public:commit:7c74f0c96fe7cbfee2d18228e4fab5b0e902a6b7","public:commit:7e4541c8817179be6d04c05db33ea93faf4701c6","public:commit:8c0e48928e116506a03cb4bebf79d3c7712c7382","public:commit:8fd0fd5c92f0f11e0c0fc43a15f424c14a45559a","public:commit:9cefce226c2ead60e57a36a20227c660559e3252","public:commit:9e84c3197bb2404685d1c15178972f58b0394943","public:commit:b7b01c01dff5abd03fd055e829454ae488ba7d6b","public:commit:cab2d56df96f4cf86c69a55d4310f17c914db2a6","public:commit:cf44942e1362caf9e8a6818f0a6f182a4e24e7bc","public:commit:cfde4e9d82adef4de7ad20fbdb8335134e2d3a32","public:commit:d4151a9b456c5075b7de7ce0506ea8eb1efb3421","public:commit:e3ed4b3d6fc36bebb82dd0338116f9d9e80bd127","public:commit:f64598c135ad7a2d20f2d931ed05ec3240b3584b"],"source_type":"public","date":"2024-05-06..2024-05-14","topics":["concurrency","ffi","testing","build","performance","recovery","api","diagnosis","documentation","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Build delegation, update preservation and plugin installation all revise quickly {#build-delegation-update-preservation-and-plugin-installation-all-revise-quickly}

## Build responsibility moves to one backend {#build-responsibility-moves-to-one-backend}

896 explicitly pins Conan2.2.3 because of a reported2.3.0 regression.897 reverses the pin about12minutes later and uses a persistent build directory. Exact file identities verify that CI/Docker return to the pre-pin versions.907 then removes the persistent-dir workaround as it adopts scikit-build-core-conan. Profiles, compiler executables and the local funchook recipe move into backend configuration, while repeated CI/Docker preparation commands disappear.908's output/install-path mismatch is repaired in911; version floors introduced during the transition are also removed.

The useful engineering pattern is centralizing setup responsibility and then adjusting callers to that new boundary. It is not a durable 'always pin' or 'never pin' preference. The external backend was not executed or independently audited here. README's simplified pip build instructions still rely on native toolchains and the backend's dependency work.

## Distribution experiments are not permanent commitments {#distribution-experiments-are-not-permanent-commitments}

932 builds a Windows embedded-Python bundle and removes the sdist job. The workflow encodes a SHA256 check for the interpreter download, wheel installation and a zipped distribution with launchers.934 repairs artifact placement.938 temporarily moves release creation into the bundle path.951, despite its release-only title, removes the bundle and separate release jobs, returns release creation to the wheel/PyPI path and restores the workflow name. The sdist job does not return; the launcher files remain. The reason for this short-lived experiment's removal is unknown. No claim about user demand, Windows reliability or release strategy should fill that gap.

933 separately narrows Docker Hub to tags while GHCR retains development builds. That is an explicit distribution policy. No unstated cost/rate-limit motive is asserted.

## Updating a server preserves selected data without becoming transactional {#updating-a-server-preserves-selected-data-without-becoming-transactional}

935 changes the CLI folder API.936 replaces version-separated folders with a flat default and compares a local version.txt marker to the packaged target. Matching installations skip updates; newer installations are refused and users are asked to upgrade Endstone; older/unknown installations prompt unless confirmation is disabled. The marker is metadata, not inspection of the installed executable.

The first updater stages extraction and removes three configuration files before copying into the installation.940 changes to direct per-file extraction, skipping existing allowlist.json, permissions.json and server.properties on both fresh-install and update paths. It moves marker writing to successful download/configuration. This broadens preservation to the shared path, but it is neither atomic replacement nor backup/rollback. The code still rewrites server.properties and may change its default server name, so 'preserve' is a semantic promise with a specific exception, not byte identity. Unrelated world/state files are not comprehensively classified by this patch. No interrupted-update or recovery test was run.

## Wheel loading crosses an embedded-runtime boundary {#wheel-loading-crosses-an-embedded-runtime-boundary}

941 installs wheel plugins into a common plugins/.local user base rebuilt at process start, with dependencies enabled. Its custom import-by-spec path breaks editable packages,942 adds ordinary entry-point loading first, and949 removes the custom loader once the user site is explicitly inserted into sys.path. This is a concrete simplification after a compatibility failure, not a preference against importlib in every setting.

944 replaces pip's internal API with a subprocess,946 removes LD_PRELOAD from that subprocess environment, and952 uses sys.prefix to locate Python rather than assuming sys.executable identifies an interpreter inside a native host. These changes are causally related integration repairs. The loader still does not check subprocess success directly; all plugins share one dependency environment, and deleting/recreating it each start is not per-plugin isolation or security containment. Bootstrap PATH rewriting also remains. These are bounded limits to the achieved installation model, not claims of demonstrated exploitation.

## Evidence and retrieval {#evidence-and-retrieval}

Final bootstrap base/platform implementations, plugin loader, CLI, pyproject and both workflows were fully read. All assigned authors/committers are Vincent. Release notes and workflow code are source claims, not recorded runs by this review. Use this family for build-backend migration, environment discovery in embedded Python, installation process boundaries, preserving configuration during updates and distinguishing abandoned distribution experiments from settled practice. No commands from the reviewed project were executed, no package was installed and no server files were modified.

## Per-commit source dispositions {#per-commit-source-dispositions}

<a id="commit-896"></a>
### 896 · fix(ci): freeze conan version to 2.2.3 due to a regression introduced in 2.3.0 {#commit-896}

[Full commit b7b01c01dff5abd03fd055e829454ae488ba7d6b](https://github.com/EndstoneMC/endstone/commit/b7b01c01dff5abd03fd055e829454ae488ba7d6b) · 2024-05-06T21:47:36Z · parent `a898b20559169a05f9e4ae1037272a6c524317ea` · temporary_workaround.

Pins Conan2.2.3 in CI and Docker, explicitly citing a regression introduced in2.3.0. This is a stated compatibility workaround, not a measured diagnosis in this workunit.897 reverses the pin roughly12minutes later, so it must not be extracted as a lasting preference for dependency freezing.

Changed paths: `.github/workflows/wheel.yml`, `Dockerfile`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-897"></a>
### 897 · fix(ci): build with conan 2.3.0 with a persistent build dir {#commit-897}

[Full commit 8fd0fd5c92f0f11e0c0fc43a15f424c14a45559a](https://github.com/EndstoneMC/endstone/commit/8fd0fd5c92f0f11e0c0fc43a15f424c14a45559a) · 2024-05-06T21:59:04Z · parent `b7b01c01dff5abd03fd055e829454ae488ba7d6b` · workaround_revision.

Restores the CI/Docker files to their pre-pin blobs and adds a persistent scikit-build build directory, explicitly claiming Conan2.3.0 compatibility. Exact restoration hashes distinguish the reversal from an approximate equivalent edit.907 later replaces this setup with a Conan-aware backend and removes the persistent-dir setting. The sequence supports evolving integration workarounds, not a settled claim that pinning or persistence is always preferable.

Changed paths: `.github/workflows/wheel.yml`, `Dockerfile`, `pyproject.toml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-907"></a>
### 907 · refactor(build system): use scikit-build-core-conan {#commit-907}

[Full commit cab2d56df96f4cf86c69a55d4310f17c914db2a6](https://github.com/EndstoneMC/endstone/commit/cab2d56df96f4cf86c69a55d4310f17c914db2a6) · 2024-05-08T15:46:31Z · parent `ac82785cff63c721feb6fcbdb7c269de9ac0cb90` · build_architecture.

Moves Python packaging to scikit-build-core-conan with Windows/Linux Conan profiles and RelWithDebInfo, removing hand-written conan install steps from CI/Docker. Also removes897's persistent build directory and the old CMake preset choice. Dependency setup now belongs to the build backend rather than every caller. The backend's external implementation is not reviewed here; the actual in-repository configuration and consumers were read.

Changed paths: `.github/workflows/wheel.yml`, `Dockerfile`, `pyproject.toml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-908"></a>
### 908 · ci: update Dockerfile and wheel.yml {#commit-908}

[Full commit 556c2c160d398466dd16c071bbaa840973f0c336](https://github.com/EndstoneMC/endstone/commit/556c2c160d398466dd16c071bbaa840973f0c336) · 2024-05-08T17:04:56Z · parent `cab2d56df96f4cf86c69a55d4310f17c914db2a6` · build_migration.

Removes remaining CI Conan-profile/export setup, moves wheel outputs to dist and temporarily adds Docker cc/c++ aliases to Clang. CI installation still points to wheelhouse until911, so the migration is not internally complete at this commit. This is a concrete caller/backend coordination issue, not evidence of a successfully passing pipeline.

Changed paths: `.github/workflows/wheel.yml`, `Dockerfile`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-909"></a>
### 909 · chore: update conan profile for Linux {#commit-909}

[Full commit 4c237c74b684f8d6e37c02967d6bcce6b5a01deb](https://github.com/EndstoneMC/endstone/commit/4c237c74b684f8d6e37c02967d6bcce6b5a01deb) · 2024-05-09T08:49:36Z · parent `556c2c160d398466dd16c071bbaa840973f0c336` · build_configuration.

Configures Linux compiler_executables explicitly as clang/clang++ and requires backend>=0.2.1. This makes compiler selection part of the Conan profile rather than relying solely on PATH aliases. No compiler benchmark or new cross-toolchain validation is supplied.

Changed paths: `.github/conan_profiles/linux`, `pyproject.toml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-910"></a>
### 910 · chore(deps): use scikit-build-core-conan >= 0.3.0 {#commit-910}

[Full commit 299e2da5a0304cf855ed3a59293f1e0f7b624bb8](https://github.com/EndstoneMC/endstone/commit/299e2da5a0304cf855ed3a59293f1e0f7b624bb8) · 2024-05-09T09:21:27Z · parent `4c237c74b684f8d6e37c02967d6bcce6b5a01deb` · build_architecture.

Requires backend>=0.3.0 and configures the local funchook recipe path/version through it, removing the Docker manual Conan setup and temporary cc/c++ aliases. The change completes more of the handoff to backend-managed dependency preparation. External backend behavior is assumed by configuration, not independently executed or audited here.

Changed paths: `Dockerfile`, `pyproject.toml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-911"></a>
### 911 · fix(ci): update wheel.yml {#commit-911}

[Full commit 15f67c00450c7b0e6e0c3f984f1bbdfd52cec47e](https://github.com/EndstoneMC/endstone/commit/15f67c00450c7b0e6e0c3f984f1bbdfd52cec47e) · 2024-05-09T09:36:32Z · parent `299e2da5a0304cf855ed3a59293f1e0f7b624bb8` · build_correction.

Repairs wheel installation paths to dist and quiets apt output, while removing the backend version floor entirely. The title hides a dependency-policy change alongside the CI repair. The final configuration is unpinned, so the earlier minimum versions are historical transition requirements rather than an enduring lock policy.

Changed paths: `.github/workflows/wheel.yml`, `Dockerfile`, `pyproject.toml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-929"></a>
### 929 · refactor: update command line options {#commit-929}

[Full commit 156f1e78cefba672cad3763334719bffbabe643c](https://github.com/EndstoneMC/endstone/commit/156f1e78cefba672cad3763334719bffbabe643c) · 2024-05-11T13:07:28Z · parent `2468f9752baec492cc05c017329fca9018b924d6` · cli_revision.

Replaces the install confirmation option with -y/--no-confirm/--yes and updates Compose to use it. The help text describes all prompts, while current use is installation/update confirmation. This is a breaking option rename and automation affordance, not consent to unrelated future actions.

Changed paths: `docker-compose.yml`, `python/src/endstone/_internal/bootstrap/__init__.py`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-930"></a>
### 930 · feat: add __main__.py {#commit-930}

[Full commit 5988237298428340c9140574eb7a6ed0572878d2](https://github.com/EndstoneMC/endstone/commit/5988237298428340c9140574eb7a6ed0572878d2) · 2024-05-11T14:21:55Z · parent `156f1e78cefba672cad3763334719bffbabe643c` · entrypoint.

Adds package-root __main__.py so python -m endstone launches the CLI and removes the nested bootstrap __main__.py. This changes the supported invocation surface without altering the bootstrap algorithm itself.

Changed paths: `python/src/endstone/__main__.py`, `python/src/endstone/_internal/bootstrap/__init__.py`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-931"></a>
### 931 · feat: add start.cmd and start.ps1 {#commit-931}

[Full commit 1bdfd86452fcf00b9243a213602faed25094ec2d](https://github.com/EndstoneMC/endstone/commit/1bdfd86452fcf00b9243a213602faed25094ec2d) · 2024-05-11T15:59:30Z · parent `5988237298428340c9140574eb7a6ed0572878d2` · launcher_scripts.

Adds Windows cmd and PowerShell launchers for an embedded bin/python interpreter, forwarding arguments and retaining an error pause. Interpreter lookup is relative to the working directory rather than robustly anchored to the script location; the cmd diagnostic mentions the script directory but does not make lookup use it. The scripts are source-read only and remain after951 removes the bundle workflow.

Changed paths: `scripts/start.cmd`, `scripts/start.ps1`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-932"></a>
### 932 · feat(ci): add build_bundle_windows to wheel.yml {#commit-932}

[Full commit cfde4e9d82adef4de7ad20fbdb8335134e2d3a32](https://github.com/EndstoneMC/endstone/commit/cfde4e9d82adef4de7ad20fbdb8335134e2d3a32) · 2024-05-13T09:53:17Z · parent `1bdfd86452fcf00b9243a213602faed25094ec2d` · distribution_experiment.

Replaces the sdist-building job with a Windows Python3.12.3 bundle job: download with a hardcoded SHA256 check, unpack interpreter, copy launchers, install the matching wheel and archive. Adds a separate release/bundle path while PyPI publication receives wheels. This is an explicitly encoded integrity check on the downloaded archive, not independent verification of the fetched runtime or a successful CI run.951 later removes the entire bundle experiment.

Changed paths: `.github/workflows/wheel.yml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-933"></a>
### 933 · refactor(ci): dev build of docker image will no longer be pushed to docker hub {#commit-933}

[Full commit 8c0e48928e116506a03cb4bebf79d3c7712c7382](https://github.com/EndstoneMC/endstone/commit/8c0e48928e116506a03cb4bebf79d3c7712c7382) · 2024-05-13T10:02:41Z · parent `cfde4e9d82adef4de7ad20fbdb8335134e2d3a32` · distribution_policy.

Splits Docker publication so development/daily builds stay on GHCR while Docker Hub publication is limited to tags, matching the explicit commit claim. Jobs and permissions differ accordingly. This is a repository-specific distribution policy change; no pricing, rate-limit or organizational motive is stated.

Changed paths: `.github/workflows/docker.yml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-934"></a>
### 934 · fix(ci): update artifact download path in CI workflow {#commit-934}

[Full commit d4151a9b456c5075b7de7ce0506ea8eb1efb3421](https://github.com/EndstoneMC/endstone/commit/d4151a9b456c5075b7de7ce0506ea8eb1efb3421) · 2024-05-13T10:22:57Z · parent `8c0e48928e116506a03cb4bebf79d3c7712c7382` · pipeline_correction.

Changes the bundle job's wheel artifact download location from build to dist and creates the destination directory. This keeps wheel artifacts out of the interpreter directory being archived and aligns later installation paths. That packaging consequence is visible in the workflow; no completed bundle artifact was independently inspected.

Changed paths: `.github/workflows/wheel.yml`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-935"></a>
### 935 · refactor: command-line option for server installation directory {#commit-935}

[Full commit 38657d6f2cfa5af1ffed922b66ac467aa7024276](https://github.com/EndstoneMC/endstone/commit/38657d6f2cfa5af1ffed922b66ac467aa7024276) · 2024-05-13T15:52:04Z · parent `d4151a9b456c5075b7de7ce0506ea8eb1efb3421` · cli_revision.

Renames --install-folder/-if to --server-folder/-s and makes the formatted absolute path a stored bootstrap property, initially defaulting to bedrock_server/{system}/{version}. The bootstrap no longer appends platform/version in the property accessor.936 immediately changes the default layout again, so migration advice must identify the exact revision.

Changed paths: `python/src/endstone/_internal/bootstrap/__init__.py`, `python/src/endstone/_internal/bootstrap/base.py`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-936"></a>
### 936 · feat: boostrap will update the bedrock server if necessary {#commit-936}

[Full commit f64598c135ad7a2d20f2d931ed05ec3240b3584b](https://github.com/EndstoneMC/endstone/commit/f64598c135ad7a2d20f2d931ed05ec3240b3584b) · 2024-05-13T17:10:12Z · parent `38657d6f2cfa5af1ffed922b66ac467aa7024276` · update_architecture.

Changes the default to one flat bedrock_server directory and adds version-aware updates using the package's target version and a local version.txt marker. Equal versions skip, newer installations are refused with an Endstone-upgrade instruction, and older/unknown installs require confirmation unless -y. Downloads are initially staged under the server directory and merged after removing the three configuration files from the staged tree. Prepare creates plugin state and writes the marker. This preserves selected configuration on the update path, but is not atomic rollback or binary-version inspection; fresh-install extraction remains different until940.

Changed paths: `python/src/endstone/_internal/bootstrap/__init__.py`, `python/src/endstone/_internal/bootstrap/base.py`, `python/src/endstone/_internal/bootstrap/linux.py`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-937"></a>
### 937 · release: version 0.4.3 {#commit-937}

[Full commit 503ac64026664aa1183270b7eac34f6e1e15ab25](https://github.com/EndstoneMC/endstone/commit/503ac64026664aa1183270b7eac34f6e1e15ab25) · 2024-05-13T17:17:18Z · parent `f64598c135ad7a2d20f2d931ed05ec3240b3584b` · release_metadata.

Sets the0.4.3 package marker and records the CLI/update changes in the changelog. The release text reports the newly implemented behavior; it is not an additional executed update scenario or an independent architecture decision.

Changed paths: `CHANGELOG.md`, `include/endstone/endstone.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-938"></a>
### 938 · ci: rename wheel.yml to cd.yml {#commit-938}

[Full commit 258a2b1ecc7b5e9eb7054a6cc3ff5a3c33bc838b](https://github.com/EndstoneMC/endstone/commit/258a2b1ecc7b5e9eb7054a6cc3ff5a3c33bc838b) · 2024-05-13T21:12:26Z · parent `503ac64026664aa1183270b7eac34f6e1e15ab25` · pipeline_revision.

Renames wheel.yml to cd.yml but also removes Create Release from the PyPI job while retaining the separate bundle release job. It is not a byte-identical workflow relocation. The release responsibility is temporarily concentrated in the bundle path and changes again in951.

Changed paths: `.github/workflows/cd.yml`, `README.md`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-939"></a>
### 939 · docs: update CHANGELOG.md {#commit-939}

[Full commit 44e8c679b9e1ce8fd7b3e3546079d28c3d677585](https://github.com/EndstoneMC/endstone/commit/44e8c679b9e1ce8fd7b3e3546079d28c3d677585) · 2024-05-13T21:14:02Z · parent `258a2b1ecc7b5e9eb7054a6cc3ff5a3c33bc838b` · release_metadata.

Updates the changelog's release section for0.4.3. Verified release text receives a brief disposition; no new implementation or test is present.

Changed paths: `CHANGELOG.md`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-940"></a>
### 940 · feat: bootstrap now check if specific files exist before installation {#commit-940}

[Full commit 6e0a9ca943a02ab61c367e146ab6c196ddddd706](https://github.com/EndstoneMC/endstone/commit/6e0a9ca943a02ab61c367e146ab6c196ddddd706) · 2024-05-13T21:18:41Z · parent `44e8c679b9e1ce8fd7b3e3546079d28c3d677585` · update_revision.

Replaces staged-update copying with per-file extraction that skips existing allowlist.json, permissions.json and server.properties for both installation and update. Writes version.txt after download/configuration rather than every prepare. The code still reads and rewrites server.properties and substitutes the default server name, so 'preserved' does not mean byte-identical. Direct in-place extraction simplifies the path but provides no transaction/rollback guarantee; the newer-version refusal remains.

Changed paths: `python/src/endstone/_internal/bootstrap/__init__.py`, `python/src/endstone/_internal/bootstrap/base.py`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-941"></a>
### 941 · feat: PythonPluginLoader will load all *.whl files under the plugins directory {#commit-941}

[Full commit 7e4541c8817179be6d04c05db33ea93faf4701c6](https://github.com/EndstoneMC/endstone/commit/7e4541c8817179be6d04c05db33ea93faf4701c6) · 2024-05-13T23:53:49Z · parent `6e0a9ca943a02ab61c367e146ab6c196ddddd706` · plugin_distribution.

Adds wheel plugins: bootstrap deletes plugins/.local each start, sets PYTHONUSERBASE and adjusts search paths; the loader installs all *.whl with dependencies via pip's internal API into that shared user base. A custom import-by-spec path targets site.USER_SITE, inserting modules into sys.modules before execution. This breaks editable-package loading, corrected in942. The directory separates plugin installation from the main environment operationally, but all plugins share it and it is not a security sandbox or per-plugin dependency isolation.

Changed paths: `python/src/endstone/_internal/bootstrap/base.py`, `python/src/endstone/_internal/plugin_loader.py`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-942"></a>
### 942 · fix: editable plugins can now be loaded again {#commit-942}

[Full commit cf44942e1362caf9e8a6818f0a6f182a4e24e7bc](https://github.com/EndstoneMC/endstone/commit/cf44942e1362caf9e8a6818f0a6f182a4e24e7bc) · 2024-05-14T00:08:18Z · parent `7e4541c8817179be6d04c05db33ea93faf4701c6` · corrective_followup.

Tries entry-point loading normally first and falls back to the manual module loader on ModuleNotFoundError, explicitly restoring editable plugins. The exception may also represent a missing dependency inside the plugin rather than a missing top-level module, so the fallback is broader than the title's single case.949 removes the custom loader altogether once the site path is established.

Changed paths: `python/src/endstone/_internal/plugin_loader.py`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-943"></a>
### 943 · refactor: fix warnings due to type hints {#commit-943}

[Full commit 72fbc553ea700893c3e369fdd3e02705e62b1a70](https://github.com/EndstoneMC/endstone/commit/72fbc553ea700893c3e369fdd3e02705e62b1a70) · 2024-05-14T08:33:33Z · parent `cf44942e1362caf9e8a6818f0a6f182a4e24e7bc` · semantic_cleanup.

Changes command/permission defaults from None-guarded handling to empty dictionaries followed by unconditional iteration. Absent attributes now produce empty lists instead of None, while an explicit None value would fail at .items(). Although described as type-hint warning cleanup, this is a behavioral input-contract change and should not be classified as pure formatting.

Changed paths: `python/src/endstone/_internal/plugin_loader.py`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-944"></a>
### 944 · fix: use subprocess.run for calling pip install {#commit-944}

[Full commit e3ed4b3d6fc36bebb82dd0338116f9d9e80bd127](https://github.com/EndstoneMC/endstone/commit/e3ed4b3d6fc36bebb82dd0338116f9d9e80bd127) · 2024-05-14T09:45:33Z · parent `72fbc553ea700893c3e369fdd3e02705e62b1a70` · process_boundary.

Replaces in-process pip internals with subprocess.run using a discovered Python executable. Linux initially uses sys.executable and Windows searches sys.path;952 later centralizes discovery under sys.prefix. The subprocess invocation does not request check=True or inspect the return code, so installation failure is not directly surfaced at this boundary. Moving pip out of the embedded interpreter is observed; a complete causal diagnosis is not stated in this commit.

Changed paths: `python/src/endstone/_internal/plugin_loader.py`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-945"></a>
### 945 · feat: add --no-warn-script-location to pip install command {#commit-945}

[Full commit 6ce1842ad18bf9823e7279c642e59e22eb4b30b8](https://github.com/EndstoneMC/endstone/commit/6ce1842ad18bf9823e7279c642e59e22eb4b30b8) · 2024-05-14T10:06:20Z · parent `e3ed4b3d6fc36bebb82dd0338116f9d9e80bd127` · minor_configuration.

Adds --no-warn-script-location to the pip command. This suppresses a specific installation warning and does not change dependency isolation, failure handling or interpreter selection.

Changed paths: `python/src/endstone/_internal/plugin_loader.py`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-946"></a>
### 946 · fix: remove "LD_PRELOAD" from environment when calling pip install from PluginLoader on Linux {#commit-946}

[Full commit 9cefce226c2ead60e57a36a20227c660559e3252](https://github.com/EndstoneMC/endstone/commit/9cefce226c2ead60e57a36a20227c660559e3252) · 2024-05-14T10:09:26Z · parent `6ce1842ad18bf9823e7279c642e59e22eb4b30b8` · process_environment_fix.

Removes LD_PRELOAD from the copied environment passed to pip's subprocess, preventing the Endstone preload setting from being inherited by that helper process. Other environment settings remain. This is a targeted native/Python process-boundary correction, not a general environment sanitization mechanism or a sandbox.

Changed paths: `python/src/endstone/_internal/plugin_loader.py`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-949"></a>
### 949 · refactor: remove unused `_load_module` method in `plugin_loader.py` {#commit-949}

[Full commit 712c80fcaf7248e803a7c36c39998f4566a9970a](https://github.com/EndstoneMC/endstone/commit/712c80fcaf7248e803a7c36c39998f4566a9970a) · 2024-05-14T14:48:17Z · parent `779affa8eb2e977221a540f00bd86d51aa16bb80` · import_architecture_revision.

Removes the manual _load_module fallback and the bootstrap's private site-path calculation. After installing wheels, the loader inserts site.getusersitepackages() into sys.path and uses ordinary entry-point loading. This simplifies941/942's discovery path and uses a public site API. The bootstrap still overwrites PATH from Python search paths, and the shared plugin installation directory/unchecked pip status are unchanged.

Changed paths: `python/src/endstone/_internal/bootstrap/base.py`, `python/src/endstone/_internal/plugin_loader.py`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-950"></a>
### 950 · docs: update CHANGELOG.md {#commit-950}

[Full commit 376a0cd80061b1ed5f218d7b10e0742d4d6c870f](https://github.com/EndstoneMC/endstone/commit/376a0cd80061b1ed5f218d7b10e0742d4d6c870f) · 2024-05-14T14:54:21Z · parent `712c80fcaf7248e803a7c36c39998f4566a9970a` · release_documentation.

Documents wheel plugins/dependencies, protected server files and the Linux scheduler fix. These entries summarize941/940/947 and are not new tests or separate evidence of successful execution.

Changed paths: `CHANGELOG.md`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-951"></a>
### 951 · release: version 0.4.5 {#commit-951}

[Full commit 7c74f0c96fe7cbfee2d18228e4fab5b0e902a6b7](https://github.com/EndstoneMC/endstone/commit/7c74f0c96fe7cbfee2d18228e4fab5b0e902a6b7) · 2024-05-14T16:23:52Z · parent `376a0cd80061b1ed5f218d7b10e0742d4d6c870f` · distribution_reversal.

The0.4.5 release commit removes the entire Windows bundle job and separate bundle-release job, renames cd.yml back to wheel.yml, and restores Create Release to the PyPI path without uploaded bundle files. This is a substantial reversal hidden under a release title. The earlier sdist job does not return and launcher scripts remain. No reason for abandoning the bundle or explanation of the absent0.4.4 release is supplied here.

Changed paths: `.github/workflows/wheel.yml`, `CHANGELOG.md`, `include/endstone/endstone.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-952"></a>
### 952 · feat: improve Python executable detection {#commit-952}

[Full commit 9e84c3197bb2404685d1c15178972f58b0394943](https://github.com/EndstoneMC/endstone/commit/9e84c3197bb2404685d1c15178972f58b0394943) · 2024-05-14T23:24:16Z · parent `7c74f0c96fe7cbfee2d18228e4fab5b0e902a6b7` · interpreter_discovery_fix.

Finds Python at sys.prefix/python.exe on Windows or sys.prefix/bin/python on Linux, checks existence and raises RuntimeError if absent. This replaces sys.executable/search-path discovery from944 and is consistent with execution inside a native host where sys.executable may not identify Python; that motivation is an inference, while improved detection is the stated claim. No interpreter process was launched in this review.

Changed paths: `python/src/endstone/_internal/plugin_loader.py`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.

<a id="commit-953"></a>
### 953 · release: 0.4.6 {#commit-953}

[Full commit 55c7f785dd4161625ba9ed370587d2489e914129](https://github.com/EndstoneMC/endstone/commit/55c7f785dd4161625ba9ed370587d2489e914129) · 2024-05-14T23:38:21Z · parent `9e84c3197bb2404685d1c15178972f58b0394943` · release_metadata.

Sets0.4.6 and records improved Python executable detection. The release note points back to952's implementation and supplies no independent runtime validation.

Changed paths: `CHANGELOG.md`, `include/endstone/endstone.h`. Whole changed content was read; exact move/header reuse and binary handling are recorded in the coverage artifacts.
