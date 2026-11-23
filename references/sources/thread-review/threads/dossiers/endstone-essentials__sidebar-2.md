<!-- retrieval: {"source_ids":["public:thread:endstone-essentials/sidebar:2"],"source_type":"public","date":"2025-02-05","topics":["concurrency","testing","api","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstone-essentials-sidebar-2-attributeerror-endstone-internal-endstonepython-server-object-has-no-attribute-getnewscoreboard"></a>
# endstone-essentials/sidebar#2: AttributeError: 'endstone._internal.endstone_python.Server' object has no attribute 'get_new_scoreboard' {#endstone-essentials-sidebar-2-attributeerror-endstone-internal-endstonepython-server-object-has-no-attribute-getnewscoreboard}

Source: https://github.com/endstone-essentials/sidebar/issues/2

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
sidebar v0.0.1 fails on PlayerJoinEvent because the Server binding no longer exposes get_new_scoreboard; the provided template config is not the failing call.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent points to release 0.2.0. A supplemental 0.0.1...0.2.0 comparison was acquired and all five changed-file patches read, separating the direct API fix from accompanying refactor/release work.

## Implementation and attribution {#implementation-and-attribution}
Exact comparison base 584f7f659057121ea0d7899ce3264ba0af96fdb1 to 3d3683683b12e3753b11a28d106097383d116b48 replaces get_new_scoreboard with create_scoreboard. Five Vincent commits cover API adaptation, lambda placeholders and releases. Placeholder providers become arbitrary values coerced to str centrally; coordinates change rounding (:0f) to truncation (int), time components become zero-padded strftime, and date/time/datetime plus game_mode alias are added while gamemode remains compatible. Workflow removes an obsolete template-repository gate and publishes both wheel release assets and PyPI distribution.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
The reported missing-method path is concretely repaired; no reporter retest in issue. Release comparison is fully inspected, but this does not claim the whole five-commit history individually reviewed. Formatting/refactor includes semantic differences worth separate tests.

## Reusable decision and costs {#reusable-decision-and-costs}
Plugin errors from removed methods require matching API versions, not configuration edits. Compare release content to the diagnosed path; short lambda refactors can change numeric/time formatting semantics.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2025-02-11T13:14:20Z](https://github.com/endstone-essentials/sidebar/issues/2#issuecomment-2650798836).
