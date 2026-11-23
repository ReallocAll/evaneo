<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:94"],"source_type":"public","date":"2024-11-27","topics":["concurrency","testing","build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-94-bug-can-t-start-the-endstone-undefined-symbol-pypropertytype"></a>
# EndstoneMC/endstone #94: [bug] Can't start the endstone, undefined symbol: PyProperty_Type {#endstonemc-endstone-94-bug-can-t-start-the-endstone-undefined-symbol-pypropertytype}

Source: https://github.com/EndstoneMC/endstone/issues/94

## Review scope and state {#review-scope-and-state}

- Thread author: Monarchdos; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Monarchdos reports PyProperty_Type unresolved on Ubuntu in local and CI builds while Windows works. smartcmd asks Python version; several versions and clean installs fail, contradicting FTS427’s environment-cleanup suggestions. Wu confirms a recent build-pipeline regression and later says fixed in latest commits. No exact commit or linker mechanism is supplied. Preserve the confirmed pipeline attribution and counterevidence to repeated reinstall advice without inventing a libpython link-flag fix.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/94
- https://github.com/EndstoneMC/endstone/issues/94#issuecomment-2503535932
- https://github.com/EndstoneMC/endstone/issues/94#issuecomment-2503573451
- https://github.com/EndstoneMC/endstone/issues/94#issuecomment-2503974825
- https://github.com/EndstoneMC/endstone/issues/94#issuecomment-2503986030
- https://github.com/EndstoneMC/endstone/issues/94#issuecomment-2504144546
- https://github.com/EndstoneMC/endstone/issues/94#issuecomment-2504177772
- https://github.com/EndstoneMC/endstone/issues/94#issuecomment-2506198280
- https://github.com/EndstoneMC/endstone/issues/94#issuecomment-2506725480
- https://github.com/EndstoneMC/endstone/issues/94#issuecomment-2512034239
