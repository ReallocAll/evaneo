<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:312"],"source_type":"public","date":"2025-12-11","topics":["ffi","testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-312-unknown-crash"></a>
# EndstoneMC/endstone #312: Unknown Crash {#endstonemc-endstone-312-unknown-crash}

Source: https://github.com/EndstoneMC/endstone/issues/312

## Evidence and attribution {#evidence-and-attribution}

Primary author: pgrd1. Created 2025-12-11T17:21:22Z; recorded state closed; merged not applicable.

## Failure and evidence {#failure-and-evidence}

pgrd1 suspected a new-item-related Windows v0.10.16 crash but could not give a precise reproduction. The access-violation stack crosses ItemStackBase::deserializeComponents(IDataInput&) and the Item::readUserData hook before native frames. wu-vincent confirmed a bug and said he was working on a fix; the only follow-up is thanks.

## Limits {#limits}

The stack identifies a useful serialization boundary, but neither root cause nor patch nor successful retest appears. Do not combine this with the contemporaneous nautilus/dehydration issue merely because both follow a version update. Recorded closed status is not enough to claim resolution.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/312
- https://github.com/EndstoneMC/endstone/issues/312#issuecomment-3643404580
- https://github.com/EndstoneMC/endstone/issues/312#issuecomment-3643412655
