<!-- retrieval: {"source_ids":["public:thread:PocketMine/PocketMine-MP:3576"],"source_type":"public","date":"2015-10-09","topics":["concurrency","testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="pocketmine-pocketmine-mp-3576-damned-git-desktop"></a>
# PocketMine/PocketMine-MP#3576: damned git desktop {#pocketmine-pocketmine-mp-3576-damned-git-desktop}

Source: https://github.com/PocketMine/PocketMine-MP/pull/3576

Thread state: closed; merged: False.

## Problem and constraints {#problem-and-constraints}
Apparently accidental broad branch PR, title “damned git desktop”, empty body.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Only discussion is Vincent saying XD; no engineering rationale, review, tests or ownership claims.

## Implementation and attribution {#implementation-and-attribution}
The initial visible hunks concern broad protocol/login/crafting/UUID branch history rather than one focused described change. The full patch was not reviewed, so no implementation claims are drawn from it.

Diff evidence: [public PR files-changed view](https://github.com/PocketMine/PocketMine-MP/pull/3576/files); this is the live upstream diff, not the captured immutable patch, and was not reviewed for full implementation behavior.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Closed unmerged. Implementation conclusions are limited to the branch and authorship checks below.

## Reusable decision and costs {#reusable-decision-and-costs}
Exclude accidental branch drift from reasoning synthesis while preserving source and unreviewed patch status.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2015-10-09T14:53:09Z](https://github.com/PocketMine/PocketMine-MP/pull/3576#issuecomment-146894354).

## PR author and branch provenance {#supplemental-verification-supersedes-earlier-acquisition-gaps}
The PR lists vvzar as its author, with base master `04fc062b2acdf61817698088f8eb3eebbe43d22e` and head mcpe-0.12 `a7e5e33db8a229992e4cc96d40be5dfc9897b061`. GitHub's commit list ends at that head and shows mostly Shoghi Cervantes protocol-0.12 history with a few collaborator merges; no vvzar-authored delta appears. This is canonical branch history accidentally proposed against master, not a new design from the PR opener. The initial MemoryManager UUID→md5 hunk is not isolated as an original contribution. Conclusions here are limited to branch provenance and attribution.
