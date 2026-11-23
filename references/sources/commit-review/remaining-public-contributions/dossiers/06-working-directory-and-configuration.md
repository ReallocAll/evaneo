<!-- retrieval: {"source_ids":["public:commit:95fa9a31e392787115a8a073256df44da0bff201","public:commit:ae6c063b7ece31c0e614426af546f5560b5bbbf0"],"source_type":"public","date":"2024-05-01..2024-05-11","topics":["concurrency","testing","build","api","diagnosis","documentation","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="diagnose-the-boundary-before-changing-executable-discovery-or-configuration"></a>
# Diagnose the boundary before changing executable discovery or configuration {#diagnose-the-boundary-before-changing-executable-discovery-or-configuration}

## MkDoxy: a failing cwd, not a new search algorithm {#mkdoxy-a-failing-cwd-not-a-new-search-algorithm}

The [completed issue #75 context](../../../thread-review/threads/JakubAndrysek--MkDoxy--issue-75.md) starts with speculation about missing Doxygen, container and Poetry differences. Vincent later isolates a differential reproduction: plain mkdocs build works, while explicitly specifying relative mkdocs.yml fails. The traceback’s empty filename and the configuration-derived working directory narrow the boundary. The maintainer invites a contribution; a reporter’s intention to retest is not a successful retest.

[Commit 95fa9a](44-95fa9a31e392787115a8a073256df44da0bff201.md) removes the runPath parameter and stored member, the Popen cwd argument, and the caller's dirname computation and argument. For a filename without a directory component, dirname yields an empty string. After the patch, Popen inherits the calling working directory. It does not add executable-search logic. Existing validation already uses shutil.which for doxygen and file/executable checks for explicit paths; this capability is not introduced by the reviewed commit.

Removing cwd wholesale also changes nonempty-directory cases. The record does not test nested/absolute configuration paths, relative source/output paths, custom executable paths or platform-specific behavior. The PR discussion does not mention a narrower alternative such as normalizing only an empty directory; do not attribute that unchosen proposal to participants. The reusable question is whether a minimal reproducer identifies the actual failing argument and whether the fix preserves other path contracts.

The final [PR #103](https://github.com/JakubAndrysek/MkDoxy/pull/103) has one extra removal: unused import os. Maintainer Kuba Andrýsek authored commit 92b8bd006c7510aa68cede43f93a7bc3f284d4eb, whose parent is the reviewed commit. This follow-up change belongs to the maintainer, not Vincent’s fix. Sourcery’s generic review praise is not a measured test result.

The unchanged Doxygen wrapper also contains externally attributed helpers. Its broader hashing, configuration and process behavior is outside this fix and is not assessed here.

## Scikit-build: an example is part of the user-facing contract {#scikit-build-an-example-is-part-of-the-user-facing-contract}

[ae6c063](45-ae6c063b7ece31c0e614426af546f5560b5bbbf0.md) changes one example key, if.sys-platform to if.platform-system. The message reports errors from the old example; no parser implementation changes. The exact PR-head parser context, already completed in the thread review and reread here, accepts platform_system and compares it with sys.platform. That explains why lowercase darwin remains valid despite the key’s wording. This is a concrete reason to read the implementation contract rather than substitute a similarly named platform API from memory.

[PR #739](https://github.com/scikit-build/scikit-build-core/pull/739) is approved and merged. Its Codecov report changes overall project coverage even though the patch is Markdown-only; that does not show the configuration example executed. No direct example test was added or run here. For future documentation repairs, validate schema keys, expected values and matching order independently, and avoid counting project-wide coverage as example coverage.

## Shared retrieval boundary {#shared-retrieval-boundary}

These are two narrow compatibility repairs with explicit problems and observable edits. Both reward differential diagnosis and close reading of call/configuration boundaries. Neither proves a universal author preference, broad regression freedom or current-version compatibility. No upstream process, package installation, test or build was executed.
