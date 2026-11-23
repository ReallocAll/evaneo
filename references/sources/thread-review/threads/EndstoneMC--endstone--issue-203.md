<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:203"],"source_type":"public","date":"2025-06-17","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-203-v0-9-0-changes-minecraft-server-version-to-1-21-90-beta28"></a>
# EndstoneMC/endstone #203: v0.9.0 changes minecraft server version to  1.21.90-beta28 {#endstonemc-endstone-203-v0-9-0-changes-minecraft-server-version-to-1-21-90-beta28}

Source: https://github.com/EndstoneMC/endstone/issues/203

## Review scope and state {#review-scope-and-state}

- Thread author: St0rmyMindbender; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

St0rmyMindbender expects stable BDS 1.21.90.4 from hosting auto-update but sees preview beta 28 and alleges world loss. Wu explains Endstone distribution through PyPI, recommends pinning versions or opting out, and justifies rapid preview-based support for updated clients. He denies Endstone deletes world files; neither allegation nor absolute denial is independently verified by this thread. The real engineering conflict is release-channel expectation and host auto-update control, not proof of data deletion. Follow-up 204 provides clarification and should be read together. This is retained as deployment/release engineering, not excluded as a personal disagreement.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/203
- https://github.com/EndstoneMC/endstone/issues/203#issuecomment-2981807958
- https://github.com/EndstoneMC/endstone/issues/203#issuecomment-2981818373
