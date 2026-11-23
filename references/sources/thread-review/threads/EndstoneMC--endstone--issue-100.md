<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:100"],"source_type":"public","date":"2024-12-05","topics":["concurrency","build","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-100-crash-on-startup-with-latest-wheel"></a>
# EndstoneMC/endstone #100: Crash on startup with latest wheel {#endstonemc-endstone-100-crash-on-startup-with-latest-wheel}

Source: https://github.com/EndstoneMC/endstone/issues/100

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat’s startup trace reaches nlohmann JSON parse_error inside loadResourcePacks. Wu asks whether world_resource_packs.json is valid; the reporter confirms comments work in vanilla BDS but removing them fixes Endstone. Wu explains a new mixed folder/zipped-pack loader now parses that file with a library rejecting comments by default and proposes enabling comment tolerance. The compatibility bug is stricter parsing than the host’s accepted format, not simply user-malformed data. No fixing commit is linked; don’t conflate reporter workaround with verified final code.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/100
- https://github.com/EndstoneMC/endstone/issues/100#issuecomment-2520908778
- https://github.com/EndstoneMC/endstone/issues/100#issuecomment-2520927217
- https://github.com/EndstoneMC/endstone/issues/100#issuecomment-2520933158
- https://github.com/EndstoneMC/endstone/issues/100#issuecomment-2520941851
