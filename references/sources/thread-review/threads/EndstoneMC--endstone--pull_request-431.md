<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:431"],"source_type":"public","date":"2026-07-12","topics":["testing","build","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-431-add-setuptools-scm-to-build-system-requires"></a>
# EndstoneMC/endstone #431: Add "setuptools-scm" to `build-system.requires`. {#endstonemc-endstone-431-add-setuptools-scm-to-build-system-requires}

Source: https://github.com/EndstoneMC/endstone/pull/431

## Evidence and attribution {#evidence-and-attribution}

Primary author: micich. Created 2026-07-12T03:57:59Z; recorded state closed; merged True.

## Build-isolation fix {#build-isolation-fix}

micich reports uv sync fails importing setuptools_scm. The complete patch adds setuptools-scm to build-system.requires, making a build-time import available in the isolated backend environment. wu-vincent thanks the contributor. No test logs accompany the fix; the dependency declaration is the only change.

## Code and verification boundary {#code-and-verification-boundary}

Inspected complete 200-character pyproject.toml patch. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/431
- https://github.com/EndstoneMC/endstone/pull/431#issuecomment-4961899244
