<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:38"],"source_type":"public","date":"2024-08-27","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-38-bug---installing-a-plugin-under-linux-causes-requirement-conflicts"></a>
# EndstoneMC/endstone #38: [bug] - installing a plugin under linux causes requirement conflicts {#endstonemc-endstone-38-bug---installing-a-plugin-under-linux-causes-requirement-conflicts}

Source: https://github.com/EndstoneMC/endstone/issues/38

## Review scope and state {#review-scope-and-state}

- Thread author: legitbox; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

legitbox reports Linux Mint 22 plugin installation errors involving venv/--user, both inside and outside a virtual environment, and attaches a plugin archive. Wu points to two commits and asks for dev-build testing inside a venv. No confirmation follows. Thus the record has a proposed remediation and validation request, not a demonstrated fix; plugin archive and linked patches have not been reviewed in this dossier.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/38
- https://github.com/EndstoneMC/endstone/issues/38#issuecomment-2312683343
- https://github.com/EndstoneMC/endstone/issues/38#issuecomment-2313067168
