<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:321"],"source_type":"public","date":"2026-01-08","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-321-inconsistent-sys-executable-path-in-virtual-environments"></a>
# EndstoneMC/endstone #321: Inconsistent sys.executable path in virtual environments {#endstonemc-endstone-321-inconsistent-sys-executable-path-in-virtual-environments}

Source: https://github.com/EndstoneMC/endstone/issues/321

## Evidence and attribution {#evidence-and-attribution}

Primary author: zl9545. Created 2026-01-08T23:46:22Z; recorded state closed; merged not applicable.

## Failure and actual fix {#failure-and-actual-fix}

zl9545 observed sys.executable randomly switching between a Windows virtual-environment Python and global Python despite launching Endstone inside the venv. killcerr supplied a temporary plugin-loader lookup link. wu-vincent confirmed commit 35f37f6e as the fix.

The inspected commit replaces paths=set(paths), which discards candidate priority, with Path.resolve() normalization and an order-preserving seen set plus ordered list. It returns the first existing Path, reports attempted paths in order on failure, and converts the result to str when assigning sys.executable and sys._base_executable. The function gains a Path return annotation.

## Reusable decision and limits {#reusable-decision-and-limits}

Deduplication and priority are independent requirements: do not let an unordered set choose an interpreter. Canonicalize paths while preserving configured preference order. No regression test is included in this commit, and deterministic lookup does not itself prove every embedding/venv issue is solved.

## Code and verification boundary {#code-and-verification-boundary}

Inspected complete mirror commit 35f37f6e09611e86389cb8bf049026ed30fd4e6e in endstone/plugin/plugin_loader.py. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/321
- https://github.com/EndstoneMC/endstone/issues/321#issuecomment-3734806285
- https://github.com/EndstoneMC/endstone/issues/321#issuecomment-3765687588
