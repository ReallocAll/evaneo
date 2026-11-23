<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/scripting-nodejs-release:3"],"source_type":"public","date":"2026-08-09","topics":["lifetime","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-scripting-nodejs-release-3-reload-crashes-the-server-with-plugin"></a>
# EndstoneMC/scripting-nodejs-release #3: /reload crashes the server with plugin {#endstonemc-scripting-nodejs-release-3-reload-crashes-the-server-with-plugin}

Source: https://github.com/EndstoneMC/scripting-nodejs-release/issues/3

## Evidence and attribution {#evidence-and-attribution}

Primary author: AdemonG1tHub. Created 2026-08-09T00:55:55Z; recorded state closed; merged not applicable.

Windows reload disables scripting-nodejs then crashes through V8 StrongRootAllocator deallocation and runtime load entry points during Endstone reloadData. Wu reports fix for next release but supplies no ownership explanation or patch. Generic crashpad frames are not reliable root-cause symbols. The trace localizes reload lifetime involvement without proving exact teardown order defect; personal filesystem path omitted.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/scripting-nodejs-release/issues/3
- https://github.com/EndstoneMC/scripting-nodejs-release/issues/3#issuecomment-6169068144
