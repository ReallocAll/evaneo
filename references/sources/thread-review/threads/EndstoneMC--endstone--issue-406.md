<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:406"],"source_type":"public","date":"2026-05-28","topics":["lifetime","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-406-server-crashes-if-1-specific-add-on-exists-add-on-works-on-vanilla-bds"></a>
# EndstoneMC/endstone #406: Server crashes if 1 specific add-on exists.Add-on works on vanilla BDS {#endstonemc-endstone-406-server-crashes-if-1-specific-add-on-exists-add-on-works-on-vanilla-bds}

Source: https://github.com/EndstoneMC/endstone/issues/406

## Evidence and attribution {#evidence-and-attribution}

Primary author: Arduinonk. Created 2026-05-28T09:08:19Z; recorded state closed; merged not applicable.

## Two independent failures and evidence refinement {#two-independent-failures-and-evidence-refinement}

Arduinonk initially blamed a large addon/custom dimensions for a startup crash. Narrowing showed Turkish letters in a command name triggered the first failure; changing to English letters worked around it. A second failure occurred when world.getDimension first instantiated a registered custom dimension, with an EndstoneLevel constructor-lambda stack. wu-vincent later reports reproducing both against BDS 1.26.32.

## Actual fixes {#actual-fixes}

Commit a5a6ee6d1 changes four command-name lowercasing sites to pass unsigned char to std::tolower, removing negative-char undefined behavior, and guards/logs a missing command before registering permissions. This is byte safety, not a complete Unicode case-folding implementation. Commit c7f7154a9 replaces constructor-local add_dimension captured by reference in a persistent callback with EndstoneLevel::addDimension. Vanilla dimensions were created synchronously while the local existed; lazy custom dimensions exposed the dangling capture later.

## Reusable decisions and limits {#reusable-decisions-and-limits}

Use minimal environmental distinctions to separate correlated failures. Fix both invalid character conversion and downstream null dereference, and audit callback captures against invocation lifetime. No automated tests are added in these two commits; runtime verification is the maintainer's report.

## Code and verification boundary {#code-and-verification-boundary}

Inspected complete commits a5a6ee6d15e4f18226ca191c9d243951995b1b2a and c7f7154a9e58eebf66672da00aedac122f1daab1. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/406
- https://github.com/EndstoneMC/endstone/issues/406#issuecomment-4642935632
- https://github.com/EndstoneMC/endstone/issues/406#issuecomment-4642952849
- https://github.com/EndstoneMC/endstone/issues/406#issuecomment-4848758185
