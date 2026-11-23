<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:334"],"source_type":"public","date":"2026-02-14","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-334-docs-add-link-to-register-event-listeners-tutorial-and-create-plugins-deep-dive-tutorial"></a>
# EndstoneMC/endstone #334: docs: add link to `register-event-listeners` tutorial and create `plugins-deep-dive` tutorial {#endstonemc-endstone-334-docs-add-link-to-register-event-listeners-tutorial-and-create-plugins-deep-dive-tutorial}

Source: https://github.com/EndstoneMC/endstone/pull/334

## Evidence and attribution {#evidence-and-attribution}

Primary author: Aevarkan. Created 2026-02-14T09:11:50Z; recorded state closed; merged False.

## Contribution and uncertainty {#contribution-and-uncertainty}

Aevarkan proposed a plugin-system tutorial covering server→manager→language-loader registration, plugin discovery/delegation, and event dispatch/cancellation, plus a link from the event tutorial to the API list. The patch clearly labels its snippets pseudo-source. The author independently warned that the deep-dive article might not be completely accurate or fit the docs.

wu-vincent initially planned to incorporate it into an ecosystem-wide docs redesign for Endstone, Endgate and Endweave, then closed the unmerged PR because the next docs version would cover it. No review certified the diagrams as exact implementation semantics. Preserve it as explanatory contribution and documentation transition evidence, not a merged architecture contract.

## Code and verification boundary {#code-and-verification-boundary}

Inspected the entire 5,122-character docs diff, including pseudo-source, diagrams, reference link and typo correction; no source execution or doc rendering. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/334
- https://github.com/EndstoneMC/endstone/pull/334#issuecomment-3903236547
- https://github.com/EndstoneMC/endstone/pull/334#issuecomment-4178575316
- https://github.com/EndstoneMC/endstone/pull/334#issuecomment-5387486371
