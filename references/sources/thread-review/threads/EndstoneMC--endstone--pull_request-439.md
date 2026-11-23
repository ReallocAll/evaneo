<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:439"],"source_type":"public","date":"2026-07-17","topics":["lifetime","testing","build","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-439-drop-the-private-export-pkg-cache-workaround-now-that-conan-py-build-0-6-cleans-up-natively"></a>
# EndstoneMC/endstone #439: Drop the private export-pkg cache workaround now that conan-py-build 0.6 cleans up natively {#endstonemc-endstone-439-drop-the-private-export-pkg-cache-workaround-now-that-conan-py-build-0-6-cleans-up-natively}

Source: https://github.com/EndstoneMC/endstone/pull/439

## Evidence and attribution {#evidence-and-attribution}

Primary author: czoido. Created 2026-07-17T11:02:25Z; recorded state closed; merged True.

## Backend ownership replaces a private workaround {#backend-ownership-replaces-a-private-workaround}
czoido explains that conan-py-build 0.6 now cleans its export-pkg cache after copying the wheel (upstream PR 53), with cleanup enabled by default. That makes Endstone's override of a private Conan implementation unnecessary and liable to break on future Conan changes. Wu welcomes the simplification. This is an explicit dependency-capability migration, not evidence that cache cleanup is universally safe before wheel extraction. Upstream internals were not independently audited.

## Direct patch findings {#direct-patch-findings}

Deletes the entire107-line custom export_pkg implementation, including private Conan graph/hook calls and disabled normal export call, and pins conan-py-build>=0.6.0. No replacement workaround remains in this patch.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (4920 characters; SHA-256 5a7feb795762b5355edffcd325a2d4ced117f2894beff1470da5cf60c958c542), head 2276e0bde07a1a4eec798e5b67482a5c99b086ed. This covers the supplied PR patch, not unrelated commits or historical intermediate revisions. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/439
- https://github.com/EndstoneMC/endstone/pull/439#issuecomment-5003514084
