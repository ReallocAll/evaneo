<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:28"],"source_type":"public","date":"2024-07-29","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-28-bug-endstone-is-unable-to-find-python-executable-when-use-endstone-in-venv"></a>
# EndstoneMC/endstone #28: [bug] Endstone is unable to find Python executable when use endstone in venv {#endstonemc-endstone-28-bug-endstone-is-unable-to-find-python-executable-when-use-endstone-in-venv}

Source: https://github.com/EndstoneMC/endstone/issues/28

## Review scope and state {#review-scope-and-state}

- Thread author: killcerr; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

killcerr’s Windows venv cannot locate Python. Wu initially cannot reproduce and requests sys.prefix, sys.exec_prefix and sys.base_prefix. After the reporter identifies the Scripts location, wu suggests the base interpreter. Substitution exposes a missing endstone.form error. Cryotap and wu distinguish that as an unreleased API, so the changed error supports executable-lookup recovery rather than another lookup failure. Screenshot-only details are unverified; existing JWT redaction remains preserved. This is a two-failure diagnostic sequence, not one unresolved exception.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/28
- https://github.com/EndstoneMC/endstone/issues/28#issuecomment-2255704221
- https://github.com/EndstoneMC/endstone/issues/28#issuecomment-2255712887
- https://github.com/EndstoneMC/endstone/issues/28#issuecomment-2255716867
- https://github.com/EndstoneMC/endstone/issues/28#issuecomment-2255867525
- https://github.com/EndstoneMC/endstone/issues/28#issuecomment-2255890400
- https://github.com/EndstoneMC/endstone/issues/28#issuecomment-2255918353
- https://github.com/EndstoneMC/endstone/issues/28#issuecomment-2255921532
