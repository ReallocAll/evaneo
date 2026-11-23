<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:330"],"source_type":"public","date":"2026-02-13","topics":["testing","build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-330-docker-latest-image-is-still-0-10-x-needs-0-11-0"></a>
# EndstoneMC/endstone #330: Docker  latest  image is still 0.10.x (needs 0.11.0) {#endstonemc-endstone-330-docker-latest-image-is-still-0-10-x-needs-0-11-0}

Source: https://github.com/EndstoneMC/endstone/issues/330

## Evidence and attribution {#evidence-and-attribution}

Primary author: Bear3853. Created 2026-02-13T13:48:13Z; recorded state closed; merged not applicable.

## Disposition {#disposition}

Bear3853 found Docker latest still on 0.10 despite GitHub 0.11.0. wu-vincent identified failed image CI, said the fix would be available with 0.11.1, and offered ghcr.io/endstonemc/endstone:latest as the interim distribution channel. Distinguish source release, package release and registry-tag publication; the issue contains no underlying CI patch or verification of the workaround.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/330
- https://github.com/EndstoneMC/endstone/issues/330#issuecomment-3897411328
