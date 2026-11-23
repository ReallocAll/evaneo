<!-- retrieval: {"source_ids":["public:commit:236a462f1b6e81bf6ea37e222d7fe89bb112de82","public:commit:546aeaaea7c28ac5d1bc9bb00ace337f85f4ccf9","public:commit:6080f124a1fde58a3d5b1ec53bada60d1a49edfe","public:commit:8e11672a8ceecdd05db3aae6fb8fda28836f98d4","public:commit:a63b0fdf750351c244807ebc9e6ac5f211aacc8f","public:commit:abda651ac614e8a94d33f47cbeb0dad172b69a40","public:commit:afd48808425d6c4dd60aa4cd4a9c429b6fb2f02a","public:commit:be74c7115bacfe26accde4526ddab84bf9678eac","public:commit:d70fa6f8e10365be0d35330e228eb92fb7e8eb08","public:commit:e271a906ee2ae79c0aacc3ba2f71d9ad6088a88b"],"source_type":"public","date":"2024-05-23..2024-06-03","topics":["concurrency","ffi","build","recovery","api","documentation","review","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Plugin persistence and distribution: preserve user files, narrow helper promises and revise packaging {#plugin-persistence-and-distribution-preserve-user-files-narrow-helper-promises-and-revise-packaging}

## Storage location is distinct from storage lifecycle {#storage-location-is-distinct-from-storage-lifecycle}

1037 gives every plugin a data_folder path based on its loader directory and plugin name. It explicitly need not exist.1038 adds Python TOML helpers: configuration is lazy, reload opens the file, save does nothing when no configuration is cached, default save preserves an existing file, and resource copy can opt into replacement. The API uses tomlkit and importlib_resources; it does not implement atomic writes, schema validation, automatic defaults merge or failure recovery. Event registration skips the config attribute because reflection would otherwise invoke the lazy property while examining listeners.

1039 fixes resource lookup to use the plugin class's module.1066 chooses importlib_metadata and Optional syntax explicitly for backwards compatibility, citing issue14. The project declares Python>=3.9 and versions through3.12, so this is an observable compatibility goal. The issue conversation and a version matrix were not executed or read here. Resource copy still uses os.pathsep for normalization and mkdir without parents=True; nested directories and arbitrary paths deserve separate validation before generalizing the helper. No path exploit or live failure is asserted.

1042 tries snake_case data directories in both loaders;1058 restores plugin-name directories. The C++ and Python loader blobs match1037 exactly after the reversal, while a helper header retains an include. No migration accompanies the trial, and no message explains the reversal. This is a concrete reason to preserve decisions as dated choices rather than infer a settled personal preference for directory naming. Existing on-disk data is a compatibility boundary even when a patch is only a few lines.

## Bootstrap preservation and seed exposure are coupled {#bootstrap-preservation-and-seed-exposure-are-coupled}

The previous bootstrap skipped existing protected files during extraction but still rewrote server.properties afterward.1052 guards that post-processing and, for fresh defaults, also disables client-side chunk generation.1051's outgoing StartGamePacket hook zeros the packet seed only when that feature is disabled. The two changes therefore form a deployment precondition and a runtime serialization behavior, rather than unrelated configuration and network edits.

The guard is broader than its name: skipping any existing allowlist.json, permissions.json or server.properties disables default property modification. If an allowlist exists but properties are newly extracted, default seed-related modification can be skipped. This is a precise source-level limit, not a claim that every installation leaks a seed. The hook changes the packet's mutable settings before native writing and does not restore that packet field. It does not modify the world seed on disk, nor prove that the seed cannot be learned through any other channel. Hash validation of the downloaded server remains part of the inspected bootstrap, but no download/bootstrap was run.

## Portable Windows packaging is another attempt, not a permanent one-way decision {#portable-windows-packaging-is-another-attempt-not-a-permanent-one-way-decision}

After an earlier portable package was introduced and removed in932/951,1027 starts a WinPython-based workflow with a pinned download hash.1028 builds/installs using the bundled interpreter itself, packages its environment under bin/python and uses start.cmd. This addresses a concrete environment-consistency boundary: the interpreter used to install is the one shipped to run. The source does not claim a comparative evaluation of every embedded-Python distribution.

The workflow creates and uploads a ZIP with license/changelog. A release job is tag-conditioned, while ordinary triggers are main pushes and manual dispatch. A normal tag push does not automatically launch this workflow as written; manual dispatch on a tag is a separate possibility. The launcher looks for a relative bin/python path and reports a missing interpreter. No portable artifact, signing, startup or Windows runtime was tested here. Treat workflow source as intended automation, not evidence an actual release succeeded.

## Useful review questions {#useful-review-questions}

This family supports checking whether a configuration helper merely locates data or also creates/saves it, whether reflection triggers properties, whether a naming refactor migrates persisted state, whether privacy hooks have configuration prerequisites, and whether CI release conditions are reachable from their triggers. No general preference for one packaging backend, TOML library, installer or automatic migration policy follows. Full final plugin, bootstrap, loader, pyproject, launcher and portable-workflow context was read; detailed per-commit entries retain all revisions below.


## Individual commit dispositions {#individual-commit-dispositions}


<a id="commit-1027"></a>
### 1027: ci: add windows-portable.yml {#commit-1027}

Source: [be74c7115bacfe26accde4526ddab84bf9678eac](https://github.com/EndstoneMC/endstone/commit/be74c7115bacfe26accde4526ddab84bf9678eac). Authored 2024-05-23T03:51:36Z; Git author Vincent. Disposition: build_distribution.

Introduces Windows portable packaging around hash-pinned WinPython3.12.3. The initial workflow builds a wheel with a setup Python and installs via --find-links, which can still consult an index. It is a new portable distribution attempt after the prior932/951 create/remove sequence, not the same unchanged CPython bundle.


<a id="commit-1028"></a>
### 1028: ci: update windows-portable.yml {#commit-1028}

Source: [8e11672a8ceecdd05db3aae6fb8fda28836f98d4](https://github.com/EndstoneMC/endstone/commit/8e11672a8ceecdd05db3aae6fb8fda28836f98d4). Authored 2024-05-23T05:01:06Z; Git author Vincent. Disposition: build_revision.

Builds/installs Endstone using the bundled interpreter itself, cleans caches, assembles bin/python plus start.cmd/license/changelog and uploads a ZIP. Removes the PowerShell launcher and moves release work out of wheel.yml. The portable workflow has main-push/manual triggers but a tag-conditioned release job; ordinary tag pushes do not trigger it as written. Manual tag dispatch remains distinct. No artifact was built here.


<a id="commit-1037"></a>
### 1037: feat: add Plugin::getDataFolder {#commit-1037}

Source: [a63b0fdf750351c244807ebc9e6ac5f211aacc8f](https://github.com/EndstoneMC/endstone/commit/a63b0fdf750351c244807ebc9e6ac5f211aacc8f). Authored 2024-05-24T06:14:22Z; Git author Vincent. Disposition: public_storage_api.

Adds Plugin data_folder as a filesystem path initialized by both loaders from plugin directory/name, without promising the directory exists. Python gains logger-prefix support and initially a method binding for data_folder. This establishes a storage location, not automatic persistence or configuration migration.


<a id="commit-1038"></a>
### 1038: feat: add config helper functions for python plugins {#commit-1038}

Source: [d70fa6f8e10365be0d35330e228eb92fb7e8eb08](https://github.com/EndstoneMC/endstone/commit/d70fa6f8e10365be0d35330e228eb92fb7e8eb08). Authored 2024-05-24T07:23:18Z; Git author Vincent. Disposition: configuration_api.

Makes data_folder a property and adds lazy TOML config/reload/save/default/resource-copy helpers using tomlkit/importlib_resources. Event reflection skips config to avoid opening it during listener enumeration. Default save preserves existing files; reload still requires a file, mkdir lacks parents=True, and path normalization uses os.pathsep. These are bounded helper semantics, not a complete transactional configuration layer.


<a id="commit-1039"></a>
### 1039: fix: config.toml look up in wrong directory {#commit-1039}

Source: [236a462f1b6e81bf6ea37e222d7fe89bb112de82](https://github.com/EndstoneMC/endstone/commit/236a462f1b6e81bf6ea37e222d7fe89bb112de82). Authored 2024-05-24T14:24:44Z; Git author Vincent. Disposition: corrective_revision.

Uses the plugin class’s module as the resource anchor, fixing the wrong module lookup in1038. The later merge1040 imports this independent main-line fix into Duckos-Mods’ native-structure branch; its second-parent patch is exactly this change.


<a id="commit-1042"></a>
### 1042: refactor: use snake_case instead of CamelCase for plugin data folder {#commit-1042}

Source: [afd48808425d6c4dd60aa4cd4a9c429b6fb2f02a](https://github.com/EndstoneMC/endstone/commit/afd48808425d6c4dd60aa4cd4a9c429b6fb2f02a). Authored 2024-05-24T14:58:13Z; Git author Vincent. Disposition: storage_naming_trial.

Changes both loaders’ data-folder names from plugin names to underscore-separated lowercase names, inserting a separator before each uppercase character. No migration is implemented, so a name change can select a different directory.1058 removes this rule and restores name-based folders; neither transition states a rationale.


<a id="commit-1051"></a>
### 1051: feat: hide seed from client when `client-side-chunk-generation-enabled` is set to `false` in `server.properties` {#commit-1051}

Source: [6080f124a1fde58a3d5b1ec53bada60d1a49edfe](https://github.com/EndstoneMC/endstone/commit/6080f124a1fde58a3d5b1ec53bada60d1a49edfe). Authored 2024-05-26T13:54:03Z; Git author Vincent. Disposition: privacy_hook.

Hooks StartGamePacket::write to set the packet’s mutable LevelSettings seed to zero when client-side generation is disabled, then calls the native writer with platform-specific hook names. This is explicit seed-hiding intent with a configuration precondition. It mutates the outgoing packet and does not restore its seed; it does not alter the stored world seed or establish cryptographic secrecy against all other channels.


<a id="commit-1052"></a>
### 1052: fix: do not modify server.properties during update {#commit-1052}

Source: [e271a906ee2ae79c0aacc3ba2f71d9ad6088a88b](https://github.com/EndstoneMC/endstone/commit/e271a906ee2ae79c0aacc3ba2f71d9ad6088a88b). Authored 2024-05-26T14:01:23Z; Git author Vincent. Disposition: configuration_preservation.

Guards default server.properties rewriting with a flag that becomes false when any existing allowlist/permissions/properties file is skipped during extraction. Fresh defaults rename the server and disable client-side generation, enabling1051’s precondition. Existing user files are preserved, but the broad flag can also suppress defaults for a newly extracted properties file if another protected file already exists. This repairs940’s unconditional post-extraction rewrite without providing an atomic migration.


<a id="commit-1058"></a>
### 1058: refactor: remove toSnake function {#commit-1058}

Source: [abda651ac614e8a94d33f47cbeb0dad172b69a40](https://github.com/EndstoneMC/endstone/commit/abda651ac614e8a94d33f47cbeb0dad172b69a40). Authored 2024-05-27T03:22:46Z; Git author Vincent. Disposition: storage_naming_reversal.

Removes snake-case folder conversion and restores plugin-name folders in both loaders. Their implementation blobs match1037 exactly; the shared helper header is not an exact full-file restoration because an include remains. Preserve the trial and reversal together; no reason or migration strategy is documented.


<a id="commit-1066"></a>
### 1066: fix: use importlib_metadata for backwards compatibility, fix #14 {#commit-1066}

Source: [546aeaaea7c28ac5d1bc9bb00ace337f85f4ccf9](https://github.com/EndstoneMC/endstone/commit/546aeaaea7c28ac5d1bc9bb00ace337f85f4ccf9). Authored 2024-06-03T04:29:43Z; Git author Vincent. Disposition: compatibility_fix.

Explicitly addresses issue14 backwards compatibility by using importlib_metadata, adding its dependency and replacing union syntax with typing.Optional; tidies resource imports and public Command imports. Also repairs1065’s nonexistent MapDataManager include via a forward declaration. The issue thread is not read in this unit, and no supported-Python matrix is executed.
