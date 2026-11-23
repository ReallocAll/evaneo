<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:146"],"source_type":"public","date":"2025-03-01","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-146-bug-actor-calls-produce-empty-strings"></a>
# EndstoneMC/endstone #146: [bug] Actor Calls Produce Empty Strings? {#endstonemc-endstone-146-bug-actor-calls-produce-empty-strings}

Source: https://github.com/EndstoneMC/endstone/issues/146

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat reports actor name_tag/score_tags reads returning empty strings despite setting a name tag. Wu attributes the failure to Mojang's changed internal actor-data representation and links 0b6684a726c5b8848af2c7f3bd5747910e777753. Full linked patch inspected: DataItem gains virtual ID/type/equality/clone methods with type/id storage moved to DataItem2, accesses use data, and hasData changes the incorrect id >= size predicate to id < size before indexing. Thus the fix includes both ABI shape correction and an independently visible bounds/presence predicate correction; it should not be summarized as merely a renamed field. Reporter thanks the fix but supplies no explicit retest. The commit specifically names name-tag operations; all Actor getters are not thereby proven correct.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/146
- https://github.com/EndstoneMC/endstone/issues/146#issuecomment-2692321157
- https://github.com/EndstoneMC/endstone/issues/146#issuecomment-2692322805
- https://github.com/EndstoneMC/endstone/commit/0b6684a726c5b8848af2c7f3bd5747910e777753
