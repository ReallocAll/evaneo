<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:401"],"source_type":"public","date":"2026-05-21","topics":["testing","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-401-chore-deps-bump-sentry-crashpad-from-0-7-17-1-to-0-14-0"></a>
# EndstoneMC/endstone #401: chore(deps): bump sentry-crashpad from 0.7.17.1 to 0.14.0 {#endstonemc-endstone-401-chore-deps-bump-sentry-crashpad-from-0-7-17-1-to-0-14-0}

Source: https://github.com/EndstoneMC/endstone/pull/401

## Evidence and attribution {#evidence-and-attribution}

Primary author: dependabot[bot]. Created 2026-05-21T16:24:25Z; recorded state closed; merged False.

## Superseded dependency change {#superseded-dependency-change}

Dependabot proposed sentry-crashpad 0.7.17.1→0.14.0. wu-vincent closed it because commit 0cd66a536 removes the pip dependency entirely and bundles the handler using Conan sentry-native. The captured patch only changes the old pin, so it is obsolete rather than an accepted upgrade. Related #429 shows why bundle-relative runtime resolution matters. No claims about the upstream release's internals are supported.

## Code and verification boundary {#code-and-verification-boundary}

Inspected the entire 190-character pin diff; replacement commit cited by discussion but not inspected in this record. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/401
- https://github.com/EndstoneMC/endstone/pull/401#issuecomment-4549735550
- https://github.com/EndstoneMC/endstone/pull/401#issuecomment-4549736038
