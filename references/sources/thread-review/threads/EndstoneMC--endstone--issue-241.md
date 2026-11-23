<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:241"],"source_type":"public","date":"2025-08-08","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-241-bug-server-crashed-when-using-addon-which-has-monsters-jump-scare-attack"></a>
# EndstoneMC/endstone #241: [bug]Server crashed when using addon which has monsters jump scare attack {#endstonemc-endstone-241-bug-server-crashed-when-using-addon-which-has-monsters-jump-scare-attack}

Source: https://github.com/EndstoneMC/endstone/issues/241

## Review scope and state {#review-scope-and-state}

- Thread author: DEVILENMO; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

DEVILENMO initially correlates three addon monster attacks with crashes. Wu first suspects235, then cannot reproduce and asks for a minimal example; the stack instead shows a scheduled Python task reading offhand inventory and EndstoneItemStack::getType. Reporter performs the requested no-plugin test and the crash disappears, then supplies a 0.10.4 stack with the same inventory path. This is strong isolation evidence of a plugin/addon interaction, not proof that attacks themselves or all addons cause the defect. No particular plugin or final fix is identified; the external addon video/download was not executed or independently analyzed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/241
- https://github.com/EndstoneMC/endstone/issues/241#issuecomment-3169023209
- https://github.com/EndstoneMC/endstone/issues/241#issuecomment-3172584632
- https://github.com/EndstoneMC/endstone/issues/241#issuecomment-3172615263
- https://github.com/EndstoneMC/endstone/issues/241#issuecomment-3172637372
- https://github.com/EndstoneMC/endstone/issues/241#issuecomment-3173038337
- https://github.com/EndstoneMC/endstone/issues/241#issuecomment-3181916255
- https://github.com/EndstoneMC/endstone/issues/241#issuecomment-3181916350
