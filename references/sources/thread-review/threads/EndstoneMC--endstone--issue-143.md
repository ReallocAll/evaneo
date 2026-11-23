<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:143"],"source_type":"public","date":"2025-02-24","topics":["concurrency","performance","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-143-feature-optional-hidden-commands"></a>
# EndstoneMC/endstone #143: [feature] Optional Hidden Commands {#endstonemc-endstone-143-feature-optional-hidden-commands}

Source: https://github.com/EndstoneMC/endstone/issues/143

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat asks for commands hidden from general slash suggestions but shown once their prefix is typed, motivated by clutter and a possible unmeasured performance concern. Wu explains that suggestion display is controlled by the client after the server advertises its command registry, so the server cannot selectively control that timing through the present API. His workaround uses a chat prefix such as ! and PlayerChatEvent with custom parsing. That meets a different interaction model and sacrifices native command parsing/completion; it is not implementation of the requested hidden-command flag. No patch or performance measurement appears.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/143
- https://github.com/EndstoneMC/endstone/issues/143#issuecomment-2745273955
