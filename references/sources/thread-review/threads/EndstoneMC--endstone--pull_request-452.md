<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:452"],"source_type":"public","date":"2026-07-30","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-452-feat-event-add-player-sneak-and-sprint-events"></a>
# EndstoneMC/endstone #452: feat(event): add player sneak and sprint events {#endstonemc-endstone-452-feat-event-add-player-sneak-and-sprint-events}

Source: https://github.com/EndstoneMC/endstone/pull/452

## Evidence and attribution {#evidence-and-attribution}

Primary author: Packeting1. Created 2026-07-30T21:13:09Z; recorded state closed; merged True.

Replacement for #448 on develop. Packeting1 cherry-picks the sneak/sprint events after Wu's release-branch correction; merged. Compare the patches before treating the accepted version as semantically identical.

## Direct patch findings {#direct-patch-findings}

Same semantic additions as #448, rebased onto develop context; full patch read independently. Events are observational/noncancellable and state-gated; includes the unrelated Windows environment helper. No gameplay test added.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (8302 characters; SHA-256 4498d78749fb0aa1d8255d3fd138a4f321ede110059dc7ff710fc6199b440235), head c056ca648860a7d8760a53a7758435f56e621c75. This covers the supplied PR patch, not unrelated commits or historical intermediate revisions. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/452
- https://github.com/EndstoneMC/endstone/pull/452#issuecomment-5136358540
- https://github.com/EndstoneMC/endstone/pull/452#issuecomment-5137364671
