<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:253"],"source_type":"public","date":"2025-08-25","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-253-feature-add-endstonepluginmanager-clearplugin-endstone-plugin-to-clear-specific-plugin"></a>
# EndstoneMC/endstone #253: [feature] Add `EndstonePluginManager::clearPlugin(endstone::Plugin *)` to clear specific plugin {#endstonemc-endstone-253-feature-add-endstonepluginmanager-clearplugin-endstone-plugin-to-clear-specific-plugin}

Source: https://github.com/EndstoneMC/endstone/issues/253

## Review scope and state {#review-scope-and-state}

- Thread author: GyanPrakash2483; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

GyanPrakash2483 proposes clearPlugin for third-party loaders. Wu declines selective unload because other loaded plugins may retain/use the departing plugin's API, creating undefined behavior; he keeps collective clearPlugins and suggests disable instead. Reporter accepts. The decision is about dependency and lifetime closure, not proof that disabling frees resources or that clearPlugins can ignore external references. Any future selective unload would require accounting for dependents and outstanding callbacks/services.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/253
- https://github.com/EndstoneMC/endstone/issues/253#issuecomment-3227661076
- https://github.com/EndstoneMC/endstone/issues/253#issuecomment-3227694412
