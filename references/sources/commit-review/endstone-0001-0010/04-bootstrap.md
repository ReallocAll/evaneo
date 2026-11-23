<!-- retrieval: {"source_ids":["public:commit:196e39ef1f2d442cee659f393302da75758a5304","public:commit:1c6fefa3b8bd63f60fced477ea1b920c97789911","public:commit:43d7dc2ddbc5cbc43d97406a66571075f4529f4a","public:commit:4c41e2557f6328b937078446b0701b1c7486c5ee","public:commit:8ef820192d8d65f62039981ea59050fd7ccb1b6f","public:commit:a7a70a5b0c605f0e93b83be2878ab7aa16f3db26","public:commit:acaa1bd7325904babf34e750d5423ca30857fbc9","public:commit:bb9219d4989fc8720099cd08205eb405d9d0096e"],"source_type":"public","date":"2023-12-31..2024-01-05","topics":["concurrency","ffi","testing","recovery","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
# Bootstrap installation, process launch and recovery {#bootstrap-installation-process-launch-and-recovery}

## Intended workflow and observed revisions {#intended-workflow-and-observed-revisions}

61 replaces the CLI placeholder with OS-specific installation: choose version, fetch a remote JSON index, stream a temporary ZIP while hashing, compare SHA256, extract to a version directory and create the plugins directory. Launch is still TODO.66 creates platform classes and asynchronous process lifecycle;67 fixes an inverted download-confirmation condition introduced during that refactor.71 passes inherited stdin/stdout and leaves old forwarding code unused.74 removes the asynchronous layer, uses synchronous Popen plus wait, and assigns cwd to the child rather than changing the parent's process-wide working directory.

This chain supports a bounded simplification: direct inherited stdio is sufficient for the implemented foreground-server lifecycle. It does not establish that synchronous process APIs are always better, or that asynchronous forwarding was measured slower. The interim dead helpers and delayed dependency cleanup at79 show why refactor verification should include both behavior and packaging.

## Integrity and recovery boundaries {#integrity-and-recovery-boundaries}

The initial checksum is an assert. Optimized Python can remove it.74 makes a mismatch an explicit ValueError, materially strengthening that check. Other validation still asserts constructed exception objects, so failures are AssertionError rather than the exception classes promised by comments. An existing executable bypasses download/checksum verification. Network calls have no explicit timeout, and the source does not show signature validation or a comprehensive archive policy. A checksum downloaded alongside its index establishes consistency with that chosen source, not independent source authenticity.

The code makes installation paths absolute, creates version/plugin directories and restores executable mode on Linux. It does not demonstrate a complete transactional install/rollback or repair of a partially extracted directory. Missing permissions, interrupted download/extraction, corrupt existing executable and optimized-Python validation need distinct tests. No such test changes or operational results were supplied in this batch.

## Platform launch mechanisms {#platform-launch-mechanisms}

78 locates the packaged runtime before launch. Linux sets LD_PRELOAD so the runtime is loaded into the child server. Windows creates a suspended child, allocates/writes a DLL pathname into it, starts a remote loader thread and resumes enumerated threads. This review inspects the mechanism without executing it. The implementation exposes resource and failure-path questions: several handle-returning ctypes APIs lack full signatures, pathname allocation uses a fixed MAX_PATH budget, loader thread results are not fully checked, remote allocations/handles are not comprehensively released, and a failure can leave a suspended child without cleanup.

81 discovers loaded libpython through dladdr(Py_GetVersion), crediting tkf's linked gist, then sets child environment so native embedding can find Python and package modules. This is more grounded than guessing an install directory, but static embedding and missing libdl paths are not tested. Copying an environment and then overwriting PYTHONPATH, LD_LIBRARY_PATH, PATH or LD_PRELOAD can discard caller-provided configuration; each key's composition policy needs to be intentional. Runtime startup also depends on the [native hook](05-native-hooks.md) and [Python interpreter](03-python-boundary.md) lifetime chains.

## Costs, evidence and application {#costs-evidence-and-application}

The source contains user-facing installation/launch UX, but a prompt's presence is not proof that all cancellation, retry and failure paths work.67 specifically repairs a branch that did the opposite of the user's affirmative choice. Process return-code propagation and traceback logging improve diagnosability, while incomplete handle cleanup remains a separate issue.

Use this history for CLI launch refactors, install integrity, subprocess isolation, environment construction, error taxonomy and recovery reviews. Preserve explicit exceptions for checks that must survive optimized execution, scope cwd/env changes to the child, and audit every acquired process/library resource against success, failure and cancellation paths. These are proposed applications of observed mechanisms; they are not attributed statements of the author's universal preferences. There are no measured startup times, successful downloads, launch traces or platform integration test results in this workunit.

## Individual commit evidence {#individual-commit-evidence}



<a id="commit-61"></a>
### 61. feat: add basic cli {#commit-61}

- Source: [1c6fefa3b8bd63f60fced477ea1b920c97789911](https://github.com/EndstoneMC/endstone/commit/1c6fefa3b8bd63f60fced477ea1b920c97789911)
- Authored: 2023-12-31T02:32:59Z; parent: `3a6e1a118c75a532bc03b41db700542dcff43e2c`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces CLI placeholder with version-specific installation workflow: OS selection, prompt/install flag, remote JSON index, streamed temp ZIP, incremental SHA256 and extraction, then plugin directory creation. Launch remains TODO. Hash/schema checks use assert and requests have no timeout; optimized Python disables integrity assertions. Existing executable skips download/hash verification. Trust rests in the chosen index and archive, with no signature or archive-content validation shown.

Changed-path evidence: [.gitignore](https://github.com/EndstoneMC/endstone/blob/1c6fefa3b8bd63f60fced477ea1b920c97789911/.gitignore) (+1/−0); [endstone_python/python/endstone/_internal/bootstrap.py](https://github.com/EndstoneMC/endstone/blob/3a6e1a118c75a532bc03b41db700542dcff43e2c/endstone_python/python/endstone/_internal/bootstrap.py) (+0/−2); [endstone_python/python/endstone/_internal/bootstrap/__init__.py](https://github.com/EndstoneMC/endstone/blob/1c6fefa3b8bd63f60fced477ea1b920c97789911/endstone_python/python/endstone/_internal/bootstrap/__init__.py) (+147/−0); [endstone_python/python/endstone/_internal/bootstrap/windows.py](https://github.com/EndstoneMC/endstone/blob/1c6fefa3b8bd63f60fced477ea1b920c97789911/endstone_python/python/endstone/_internal/bootstrap/windows.py) (+0/−0)



<a id="commit-66"></a>
### 66. feat: add bootstrap {#commit-66}

- Source: [4c41e2557f6328b937078446b0701b1c7486c5ee](https://github.com/EndstoneMC/endstone/commit/4c41e2557f6328b937078446b0701b1c7486c5ee)
- Authored: 2024-01-02T15:54:24Z; parent: `e752bc3ced6dae3607d71b08fdcf9b76ea304b46`
- Disposition: meaningful; full actual diff statically reviewed.

Extracts base/Windows/Linux bootstraps, separates installation/validation/process lifecycle and adds async input/output forwarding, returning child exit code. Introduces inverted download conditional (raises when user chooses download), fixed next. Base class documents extension points, but async loop suppresses gathered exceptions and reads lines with no explicit encoding fallback. Changes exception logging to full traceback and exit -1; no bootstrap tests accompany refactor.

Changed-path evidence: [endstone_python/python/endstone/_internal/bootstrap/__init__.py](https://github.com/EndstoneMC/endstone/blob/4c41e2557f6328b937078446b0701b1c7486c5ee/endstone_python/python/endstone/_internal/bootstrap/__init__.py) (+27/−68); [endstone_python/python/endstone/_internal/bootstrap/base.py](https://github.com/EndstoneMC/endstone/blob/4c41e2557f6328b937078446b0701b1c7486c5ee/endstone_python/python/endstone/_internal/bootstrap/base.py) (+284/−0); [endstone_python/python/endstone/_internal/bootstrap/linux.py](https://github.com/EndstoneMC/endstone/blob/4c41e2557f6328b937078446b0701b1c7486c5ee/endstone_python/python/endstone/_internal/bootstrap/linux.py) (+15/−0); [endstone_python/python/endstone/_internal/bootstrap/windows.py](https://github.com/EndstoneMC/endstone/blob/4c41e2557f6328b937078446b0701b1c7486c5ee/endstone_python/python/endstone/_internal/bootstrap/windows.py) (+19/−0); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/4c41e2557f6328b937078446b0701b1c7486c5ee/pyproject.toml) (+1/−1)



<a id="commit-67"></a>
### 67. fix: permission and working directory is not correctly set on Linux {#commit-67}

- Source: [bb9219d4989fc8720099cd08205eb405d9d0096e](https://github.com/EndstoneMC/endstone/commit/bb9219d4989fc8720099cd08205eb405d9d0096e)
- Authored: 2024-01-02T17:16:48Z; parent: `4c41e2557f6328b937078446b0701b1c7486c5ee`
- Disposition: meaningful; full actual diff statically reviewed.

Fixes inverted download decision, makes install base absolute before changing global cwd to server directory, and adds executable permission after Linux extraction. Addresses path resolution and Unix archive mode separately. Global cwd mutation remains until later subprocess cwd refactor.

Changed-path evidence: [endstone_python/python/endstone/_internal/bootstrap/__init__.py](https://github.com/EndstoneMC/endstone/blob/bb9219d4989fc8720099cd08205eb405d9d0096e/endstone_python/python/endstone/_internal/bootstrap/__init__.py) (+1/−1); [endstone_python/python/endstone/_internal/bootstrap/base.py](https://github.com/EndstoneMC/endstone/blob/bb9219d4989fc8720099cd08205eb405d9d0096e/endstone_python/python/endstone/_internal/bootstrap/base.py) (+2/−1); [endstone_python/python/endstone/_internal/bootstrap/linux.py](https://github.com/EndstoneMC/endstone/blob/bb9219d4989fc8720099cd08205eb405d9d0096e/endstone_python/python/endstone/_internal/bootstrap/linux.py) (+9/−0)



<a id="commit-71"></a>
### 71. refactor: use sys.stdin and sys.stdout instead of pipes {#commit-71}

- Source: [acaa1bd7325904babf34e750d5423ca30857fbc9](https://github.com/EndstoneMC/endstone/commit/acaa1bd7325904babf34e750d5423ca30857fbc9)
- Authored: 2024-01-02T23:51:26Z; parent: `156c6f0b3f8a2c3ef26137cdd79ee870a7c6343c`
- Disposition: meaningful; full actual diff statically reviewed.

Passes sys.stdin/sys.stdout directly to subprocess instead of asyncio pipes and bypasses forwarding loop, retaining PTY TODO and unused helper. Simplifies terminal interaction at this stage without evidence of throughput improvement; asynchronous wrapper remains until commit 74.

Changed-path evidence: [endstone_python/python/endstone/_internal/bootstrap/base.py](https://github.com/EndstoneMC/endstone/blob/acaa1bd7325904babf34e750d5423ca30857fbc9/endstone_python/python/endstone/_internal/bootstrap/base.py) (+8/−9)



<a id="commit-74"></a>
### 74. refactor: simplify bootstrap and improve docstrings {#commit-74}

- Source: [a7a70a5b0c605f0e93b83be2878ab7aa16f3db26](https://github.com/EndstoneMC/endstone/commit/a7a70a5b0c605f0e93b83be2878ab7aa16f3db26)
- Authored: 2024-01-03T10:18:53Z; parent: `2c7f306515233b4ab6ca798a63ba3297fc135b79`
- Disposition: meaningful; full actual diff statically reviewed.

Replaces asyncio/aioconsole orchestration with synchronous Popen+wait and inherited stdio, passes cwd to child rather than mutating parent cwd, and removes lifecycle hooks/forwarder. Changes SHA256 mismatch from assert to explicit ValueError and runs download-finished validation; other validation still uses assert(exception-object), which raises AssertionError rather than documented exception types. Clear behavior-preserving intent coexists with stronger integrity-check semantics.

Changed-path evidence: [endstone_python/python/endstone/_internal/bootstrap/__init__.py](https://github.com/EndstoneMC/endstone/blob/2c7f306515233b4ab6ca798a63ba3297fc135b79/endstone_python/python/endstone/_internal/bootstrap/__init__.py) (+0/−1); [endstone_python/python/endstone/_internal/bootstrap/base.py](https://github.com/EndstoneMC/endstone/blob/a7a70a5b0c605f0e93b83be2878ab7aa16f3db26/endstone_python/python/endstone/_internal/bootstrap/base.py) (+57/−90); [endstone_python/python/endstone/_internal/bootstrap/linux.py](https://github.com/EndstoneMC/endstone/blob/a7a70a5b0c605f0e93b83be2878ab7aa16f3db26/endstone_python/python/endstone/_internal/bootstrap/linux.py) (+2/−3)



<a id="commit-78"></a>
### 78. feat: complete windows and linux bootstraps {#commit-78}

- Source: [43d7dc2ddbc5cbc43d97406a66571075f4529f4a](https://github.com/EndstoneMC/endstone/commit/43d7dc2ddbc5cbc43d97406a66571075f4529f4a)
- Authored: 2024-01-03T18:03:43Z; parent: `2fc2daa771366ffe012847b64d6f6233e0bd6568`
- Disposition: meaningful; full actual diff statically reviewed.

Adds runtime file validation, Linux LD_PRELOAD and Windows suspended-process DLL loading through explicit ctypes prototypes plus thread enumeration/resume. Risks include incomplete prototypes for several handle-returning APIs, fixed MAX_PATH allocation versus variable path length, missing remote-thread result check, unreleased remote memory/handles and no failure cleanup for suspended child. Existing environment LD_PRELOAD is overwritten. CLI text accidentally says executable is found in missing-executable branch. Review explains mechanism without executing injection.

Changed-path evidence: [endstone_python/python/endstone/_internal/bootstrap/__init__.py](https://github.com/EndstoneMC/endstone/blob/43d7dc2ddbc5cbc43d97406a66571075f4529f4a/endstone_python/python/endstone/_internal/bootstrap/__init__.py) (+2/−1); [endstone_python/python/endstone/_internal/bootstrap/base.py](https://github.com/EndstoneMC/endstone/blob/43d7dc2ddbc5cbc43d97406a66571075f4529f4a/endstone_python/python/endstone/_internal/bootstrap/base.py) (+13/−1); [endstone_python/python/endstone/_internal/bootstrap/linux.py](https://github.com/EndstoneMC/endstone/blob/43d7dc2ddbc5cbc43d97406a66571075f4529f4a/endstone_python/python/endstone/_internal/bootstrap/linux.py) (+9/−0); [endstone_python/python/endstone/_internal/bootstrap/windows.py](https://github.com/EndstoneMC/endstone/blob/43d7dc2ddbc5cbc43d97406a66571075f4529f4a/endstone_python/python/endstone/_internal/bootstrap/windows.py) (+134/−3)



<a id="commit-79"></a>
### 79. refactor: comments and docs, remove unused dependencies {#commit-79}

- Source: [196e39ef1f2d442cee659f393302da75758a5304](https://github.com/EndstoneMC/endstone/commit/196e39ef1f2d442cee659f393302da75758a5304)
- Authored: 2024-01-03T23:02:04Z; parent: `43d7dc2ddbc5cbc43d97406a66571075f4529f4a`
- Disposition: small-semantic; full actual diff statically reviewed.

Removes now-unused asyncio/aioconsole dependencies and improves validation/thread-resume comments. Docs claim NotImplementedError/FileNotFoundError while code still asserts exception objects; this mismatch remains. No new launch behavior.

Changed-path evidence: [endstone_python/python/endstone/_internal/bootstrap/base.py](https://github.com/EndstoneMC/endstone/blob/196e39ef1f2d442cee659f393302da75758a5304/endstone_python/python/endstone/_internal/bootstrap/base.py) (+8/−1); [endstone_python/python/endstone/_internal/bootstrap/windows.py](https://github.com/EndstoneMC/endstone/blob/196e39ef1f2d442cee659f393302da75758a5304/endstone_python/python/endstone/_internal/bootstrap/windows.py) (+2/−1); [pyproject.toml](https://github.com/EndstoneMC/endstone/blob/196e39ef1f2d442cee659f393302da75758a5304/pyproject.toml) (+1/−1)



<a id="commit-81"></a>
### 81. fix: set PYTHONPATH and LD_LIBRARY_PATH in bootstraps {#commit-81}

- Source: [8ef820192d8d65f62039981ea59050fd7ccb1b6f](https://github.com/EndstoneMC/endstone/commit/8ef820192d8d65f62039981ea59050fd7ccb1b6f)
- Authored: 2024-01-05T01:07:00Z; parent: `d72bc80e8a61350212e09fc40e8c22f99e464df0`
- Disposition: meaningful; full actual diff statically reviewed.

Sets child PYTHONPATH and Linux LD_LIBRARY_PATH from actual loaded libpython found via dladdr(Py_GetVersion), crediting tkf's linked gist. Uses copied environment but overwrites PATH/PYTHONPATH/LD_LIBRARY_PATH rather than composing existing values. dladdr validation remains an assertion. Runtime interpreter discovery is more specific than guessing installation layout, but static embedding/missing libdl cases are untested.

Changed-path evidence: [endstone_python/python/endstone/_internal/bootstrap/base.py](https://github.com/EndstoneMC/endstone/blob/8ef820192d8d65f62039981ea59050fd7ccb1b6f/endstone_python/python/endstone/_internal/bootstrap/base.py) (+1/−0); [endstone_python/python/endstone/_internal/bootstrap/linux.py](https://github.com/EndstoneMC/endstone/blob/8ef820192d8d65f62039981ea59050fd7ccb1b6f/endstone_python/python/endstone/_internal/bootstrap/linux.py) (+35/−0)
