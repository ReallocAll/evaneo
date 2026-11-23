<!-- retrieval: {"source_ids":["public:thread:scikit-build/scikit-build-core:739"],"source_type":"public","date":"2024-05-09","topics":["concurrency","testing","build","documentation","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="scikit-build-scikit-build-core-739-docs-fix-example-of-configuration-overrides-in-configuration-md"></a>
# scikit-build/scikit-build-core#739: docs: fix example of configuration overrides in configuration.md {#scikit-build-scikit-build-core-739-docs-fix-example-of-configuration-overrides-in-configuration-md}

Source: https://github.com/scikit-build/scikit-build-core/pull/739

Thread state: closed; merged: True.

## Problem and constraints {#problem-and-constraints}
The documented scikit-build configuration-override example was reported to error with the current parser.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent proposed a minimal documentation-only correction. henryiii approved with thanks; the PR merged. No alternate parser or broader configuration redesign was proposed.

## Implementation and attribution {#implementation-and-attribution}
The patch at head 7406a9a46e79dc4c8d36ef47681b6512d7febe65 replaces `if.sys-platform = "darwin"` with `if.platform-system = "darwin"` in the [[tool.scikit-build.overrides]] example. The cmake.version >=3.18 condition and matching-order explanation are unchanged. This is Vincent’s narrow documentation correction.

Diff evidence (patch inspected, not bundled): [pinned public three-dot comparison](https://github.com/scikit-build/scikit-build-core/compare/2994db5d993f0cb252dbeebfac7d66677b670ed8...7406a9a46e79dc4c8d36ef47681b6512d7febe65). Declared changed files: 1.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
The codecov bot reports overall coverage increasing from 81.40% to 81.97% with unchanged 3,888 coverable lines. A Markdown-only changed line is not an executed configuration test; the report does not prove the example was run. No direct execution or added test is present in the diff. Exact mirror patch, base and head are retained.

## Reusable decision and costs {#reusable-decision-and-costs}
Configuration examples are executable interfaces to users: repair obsolete keys minimally and validate examples against the schema rather than treating project-wide coverage as example coverage.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [henryiii · 2024-05-09T16:03:51Z](https://github.com/scikit-build/scikit-build-core/pull/739#pullrequestreview-2048306495).
- [codecov[bot] · 2024-05-09T16:18:16Z](https://github.com/scikit-build/scikit-build-core/pull/739#issuecomment-2102986020).

## Parser-context verification {#parser-context-verification}
The exact PR-head override_match signature accepts platform_system, not sys_platform. Its matching branch compares against sys.platform, so lowercase darwin is consistent with the implementation. Only the relevant declaration/matching context at the cited PR head was read. No example was executed.
