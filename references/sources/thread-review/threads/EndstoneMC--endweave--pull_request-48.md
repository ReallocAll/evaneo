<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endweave:48"],"source_type":"public","date":"2026-09-12","topics":["testing","build","api","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endweave-48-bump-endstone-from-0-11-2-to-0-11-10"></a>
# EndstoneMC/endweave #48: Bump endstone from 0.11.2 to 0.11.10 {#endstonemc-endweave-48-bump-endstone-from-0-11-2-to-0-11-10}

Source: https://github.com/EndstoneMC/endweave/pull/48

## Evidence and attribution {#evidence-and-attribution}

Primary author: dependabot[bot]. Created 2026-09-12T19:02:47Z; recorded state closed; merged False.

Dependabot proposes Endstone0.11.2→0.11.10, reproducing abbreviated upstream release notes and changelog. Wu explicitly tells bot to ignore this dependency; bot confirms and PR is unmerged. No reason for the policy is given. Upstream changes such as IPv6 default, registry imports and API/lifetime fixes are quoted bot context, not authored reasoning or audited implementation. Literal '(truncated)' denotes upstream excerpts, not proof the captured primary body itself was cut off.

## Direct patch findings {#direct-patch-findings}

Full lock patch changes only Endstone version/wheel records and removes transitive sentry-crashpad package; dependency was moved into native bundle (see #401), not dropped crash reporting by this translator. Ten platform/CPython wheel records replace older equivalents. No translator code change or compatibility test; unmerged ignore decision.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (10511 characters; SHA-256 1027c102d30a1018bb16700308dfc66dbb82fb1795c65e256d681d68ccfc251d), head 2db4db46664ee534b2fbfdcfcd98fc22c570047a. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endweave/pull/48
- https://github.com/EndstoneMC/endweave/pull/48#issuecomment-5653200672
- https://github.com/EndstoneMC/endweave/pull/48#issuecomment-5653201032
