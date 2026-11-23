<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:152"],"source_type":"public","date":"2025-03-09","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-152-bug-bossbar-progress-doesn-t-display-on-linux"></a>
# EndstoneMC/endstone #152: [bug] Bossbar progress doesn't display on linux {#endstonemc-endstone-152-bug-bossbar-progress-doesn-t-display-on-linux}

Source: https://github.com/EndstoneMC/endstone/issues/152

## Review scope and state {#review-scope-and-state}

- Thread author: PrimeStrat; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

PrimeStrat reports Linux bossbar progress remaining zero while Windows works. Wu points to b7a6338257fd0732b7a11c64c096f3b38f127e7d and promises a release; the reporter responds positively without a detailed retest. Full linked patch inspected: BossEventPacket.name changes from std::string to Bedrock::Safety::RedactableString, obsolete fixed-offset comments disappear, and RedactableString constructors/assignment update the unredacted string and reset cached redaction. A preceding field's actual native type changes the layout of health_percent and following fields, explaining why a progress symptom can require a packet-layout fix rather than a numerical workaround. That layout explanation is a static inference; no execution was performed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/152
- https://github.com/EndstoneMC/endstone/issues/152#issuecomment-2708898445
- https://github.com/EndstoneMC/endstone/issues/152#issuecomment-2709122508
- https://github.com/EndstoneMC/endstone/commit/b7a6338257fd0732b7a11c64c096f3b38f127e7d
