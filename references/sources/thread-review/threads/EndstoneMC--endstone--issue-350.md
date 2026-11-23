<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:350"],"source_type":"public","date":"2026-03-11","topics":["testing","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-350-pip-latest-image-is-still-0-10-x-needs-0-11-x"></a>
# EndstoneMC/endstone #350: pip latest  image is still 0.10.x (needs 0.11.x) {#endstonemc-endstone-350-pip-latest-image-is-still-0-10-x-needs-0-11-x}

Source: https://github.com/EndstoneMC/endstone/issues/350

## Evidence and attribution {#evidence-and-attribution}

Primary author: Bear3853. Created 2026-03-11T14:43:38Z; recorded state closed; merged not applicable.

## Disposition {#disposition}

The reporter says in Chinese that the problem is no longer needed and self-resolved. wu-vincent states PyPI is current and suggests an unsupported Python version likely explains old package selection: v0.11 requires Python 3.10+, with uvx endstone suggested for easy setup. No environment evidence confirms that hypothesis. Concise package-resolution support, not a new engineering decision.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/350
- https://github.com/EndstoneMC/endstone/issues/350#issuecomment-4039804200
