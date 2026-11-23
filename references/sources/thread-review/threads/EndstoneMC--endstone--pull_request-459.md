<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:459"],"source_type":"public","date":"2026-08-05","topics":["ffi","testing","api","diagnosis","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-459-fix-resolve-linux-packet-compatibility-issues-for-26-40"></a>
# EndstoneMC/endstone #459: fix: resolve Linux packet compatibility issues for 26.40 {#endstonemc-endstone-459-fix-resolve-linux-packet-compatibility-issues-for-26-40}

Source: https://github.com/EndstoneMC/endstone/pull/459

## Evidence and attribution {#evidence-and-attribution}

Primary author: ReallocAll. Created 2026-08-05T09:58:09Z; recorded state closed; merged False.

## Cross-platform layout review changed the diagnosis {#cross-platform-layout-review-changed-the-diagnosis}
ReallocAll proposes Linux packet fixes: pad soft-enum data to the expected offsets, reconstruct map decoration IDs, and guard non-finite rotation input. The author reports Clang20 Linux gameplay and 29/29 byte round trips.
Wu confirms real defects but rejects the flat-padding explanation. The native packet contains an 8-byte-aligned payload subobject at +48, while a flattened derived declaration reuses base tail padding at +44; Windows's unchanged total size masked this and Linux can write out of bounds. c41890cb4 is described as a payload-structure fix across 26.32/36/40, rather than a Linux-only patch. Map decorations and IDs are two independent length-prefixed lists; native INVALID_ID=-1 is legitimate, unlike requiring block positions for every cursor. #426 exposed the defect by allowing decoration-only updates. Wu points to 97071083e. NaN may be a bad-offset artifact and is left for investigation, not accepted as demonstrated malicious-client input. This is a useful case of valid symptoms plus partially wrong proposed mechanism.

## Direct patch findings {#direct-patch-findings}

Unmerged patch pads UpdateSoftEnum only on Linux, normalizes nonfinite event rotations without rewriting native packet, clears map unique_ids and appends INVALID_ID for each visible cursor. Review explains more structural alternative; source patch itself does not implement payload-subobject reconstruction.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (2306 characters; SHA-256 608cd970190fe2fabb0d108c897f4493e28857c5f4d77dbdc2ef09512b91cabf), head 531c95ebb30b8fb4644b0263f7dc43aa241d15dd. This covers the supplied PR patch, not unrelated commits or historical intermediate revisions. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/459
- https://github.com/EndstoneMC/endstone/pull/459#issuecomment-5197129104
