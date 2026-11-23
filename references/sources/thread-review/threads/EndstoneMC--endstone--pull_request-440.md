<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:440"],"source_type":"public","date":"2026-07-17","topics":["testing","build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-440-include-the-endstone-package-in-the-sdist"></a>
# EndstoneMC/endstone #440: Include the endstone package in the sdist {#endstonemc-endstone-440-include-the-endstone-package-in-the-sdist}

Source: https://github.com/EndstoneMC/endstone/pull/440

## Evidence and attribution {#evidence-and-attribution}

Primary author: czoido. Created 2026-07-17T13:56:52Z; recorded state closed; merged True.

czoido identifies a packaging-layout mismatch: the backend's default sdist convention assumes src/package, while Endstone's package lives at the root. Explicitly include it in the sdist. Wheel success does not establish source-distribution completeness.

## Direct patch findings {#direct-patch-findings}

Adds tool.conan-py-build.sdist include=[endstone] while existing wheel packages stays unchanged. Narrow source-distribution repair.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (210 characters; SHA-256 95e65c0f7f01a0f9ae2fcc63d5666e175c8631da7443ffcb557ffae48bcb857b), head 0002dba3ebcf6d90a976ec1522e791e8feb757e2. This covers the supplied PR patch, not unrelated commits or historical intermediate revisions. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/440
- https://github.com/EndstoneMC/endstone/pull/440#issuecomment-5078715397
