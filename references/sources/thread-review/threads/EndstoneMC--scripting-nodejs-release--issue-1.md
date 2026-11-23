<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/scripting-nodejs-release:1"],"source_type":"public","date":"2026-08-09","topics":["testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-scripting-nodejs-release-1-npm-package-resolution-from-inside-a-pack-causes-a-hard-crash"></a>
# EndstoneMC/scripting-nodejs-release #1: npm package resolution from inside a pack causes a hard crash {#endstonemc-scripting-nodejs-release-1-npm-package-resolution-from-inside-a-pack-causes-a-hard-crash}

Source: https://github.com/EndstoneMC/scripting-nodejs-release/issues/1

Primary text and available images were inspected; the case describes attachment coverage and has no runtime reproduction.

## Evidence and attribution {#evidence-and-attribution}

Primary author: AdemonG1tHub. Created 2026-08-09T00:52:58Z; recorded state closed; merged not applicable.

npm imports inside packs cause a reported Windows runtime crash. Primary evidence is a screenshot; Wu later claims fixed for next release without patch or mechanism. No reproducible stack is available in captured text.

## Attachment inspection {#attachment-inspection}

PNG is a prose diagnosis screenshot, not stack trace: it reports import("mongodb") from a behavior pack causes scripting-nodejs v0.1.0 std::_Xout_of_range crash, while bridge backend avoids npm resolution at boot and reaches Server started. This is reporter-supplied diagnosis, not independent exception inspection or proof every package.json pack reproduces. Wu's next-release assertion remains unverified.

## Code and verification boundary {#code-and-verification-boundary}

No implementation fix independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Source and available attachment links are listed under Traceability; the separate acquisition and inspection ledger is not included in this distribution. A screenshot corroborates only visible content, not runtime causality.

## Traceability {#traceability}


- https://github.com/EndstoneMC/scripting-nodejs-release/issues/1
- https://github.com/EndstoneMC/scripting-nodejs-release/issues/1#issuecomment-6169066607
- https://github.com/user-attachments/assets/741ff64a-5530-4bbd-a1c0-84140680ebf7
