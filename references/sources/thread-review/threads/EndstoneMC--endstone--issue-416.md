<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:416"],"source_type":"public","date":"2026-06-15","topics":["testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-416-custom-dimension-crashed-server"></a>
# EndstoneMC/endstone #416: Custom dimension crashed server {#endstonemc-endstone-416-custom-dimension-crashed-server}

Source: https://github.com/EndstoneMC/endstone/issues/416

## Evidence and attribution {#evidence-and-attribution}

Primary author: xie52a. Created 2026-06-15T05:25:51Z; recorded state closed; merged not applicable.

## Duplicate mechanism with independent reproduction {#duplicate-mechanism-with-independent-reproduction}

xie52a reproduced a Windows v0.11.4 crash using a custom-dimension behavior pack without plugins. The stack identifies the EndstoneLevel constructor lambda. Arduinonk links #406; wu-vincent confirms a fix for 0.11.5. The source's expected-behavior section mistakenly repeats the crash, so the intended successful startup is inferred from the report context.

The independently inspected #406 fix c7f7154a9 removes a dangling reference to a constructor-local lambda by extracting addDimension as a member. This record adds a plugin-free reproduction, not a separate root cause.

## Code and verification boundary {#code-and-verification-boundary}

Inspected full shared fix c7f7154a9e58eebf66672da00aedac122f1daab1 while reviewing #406; no additional patch in this thread. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/416
- https://github.com/EndstoneMC/endstone/issues/416#issuecomment-4736159633
- https://github.com/EndstoneMC/endstone/issues/416#issuecomment-4846290988
