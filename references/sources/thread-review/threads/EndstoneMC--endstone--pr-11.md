<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:11"],"source_type":"public","date":"2024-05-24","topics":["review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-11-added-more-struct-info"></a>
# EndstoneMC/endstone #11: Added More Struct Info {#endstonemc-endstone-11-added-more-struct-info}

Source: https://github.com/EndstoneMC/endstone/pull/11

## Review scope and state {#review-scope-and-state}

- Thread author: SaturnRoccat; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (88 additions, 12 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

SaturnRoccat, not wu, authored reconstructed type/member information. The merged diff names HashedString’s cached pointer mLastMatch; maps CommandOriginIdentity strings to mXuid/mPlatformOnlineId; documents observer subject pointers; and replaces Packet unknowns with priority, reliability, subclient, handled flag, timestamp, handler and compressibility. Offsets remain 8/12/16/17/24/32/40 with a 48-byte static assertion. NetworkPeer is deliberately a class to match name mangling. Wu offers appreciative acceptance, not the reverse-engineering derivation. Codecov reports covered modified lines and unchanged 12.99% total coverage, not binary-layout validation. Old explicit field initializers disappear, so equal layout alone does not prove identical default initialization.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/11
- https://github.com/EndstoneMC/endstone/pull/11#issuecomment-2129348930
- https://github.com/EndstoneMC/endstone/pull/11#issuecomment-2129349892
- https://github.com/EndstoneMC/endstone/pull/11#issuecomment-2129550155
