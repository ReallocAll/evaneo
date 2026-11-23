<!-- retrieval: {"source_ids":["public:thread:adamfisk/LittleProxy:313"],"source_type":"public","date":"2016-07-18","topics":["lifetime","concurrency","testing","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="adamfisk-littleproxy-313-leak-bytebuf-release-was-not-called-before-it-s-garbage-collected"></a>
# adamfisk/LittleProxy#313: LEAK: ByteBuf.release() was not called before it's garbage-collected {#adamfisk-littleproxy-313-leak-bytebuf-release-was-not-called-before-it-s-garbage-collected}

Source: https://github.com/adamfisk/LittleProxy/issues/313

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Enabling 10 MiB request/response aggregation triggered Netty ByteBuf leak warnings; setting buffer limits to zero avoided them. Multiple users confirmed aggregation correlation, one also reported connection exhaustion. Vincent only confirmed encountering the issue.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
jekh requested versions, target URL and configuration, initially could not reproduce, and suggested LP 1.1.1 plus later Netty leak-detector fixes. igor-dmitriev tested 1.1.1 and still saw warnings, correctly showing that one release call in SimpleChannelInboundHandler does not establish balanced ownership. The access histories contain copy, multiple retain calls and releases across deferred connection setup. The issue later closes in favor of #348 with fix #351. Full linked #351 body, patch and three comments were also read. Its explanation separates plain header-only HttpRequest from reference-counted aggregated FullHttpRequest; initial HTTP is queued then forwarded, while CONNECT is consumed locally.

## Implementation and attribution {#implementation-and-attribution}
jekh’s merged #351 adds one ReferenceCounted release at the end of connectionSucceeded, after either forwarding or dropping initialRequest. HTTP initial writes retain twice (before connection and after success) but network output releases once; HTTPS CONNECT retains once yet never reaches output. The additional release balances the initial queued ownership in both success paths.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
mjallday explicitly verified #348 resolution. This is stronger than the earlier upgrade speculation, but does not prove every warning in #313 had that cause. A 2020 comment observes the failed-connection path also needs release; a 2022 follow-up links a separate newer-repository PR #141, not inspected here and not claimed fixed. No upstream execution performed.

## Reusable decision and costs {#reusable-decision-and-costs}
Track retain/release ownership across queue, success, failure and locally consumed messages. A finally release is insufficient when a deferred write adds another retain; detector false positives and real lifecycle leaks can coexist.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [jekh · 2016-07-19T15:18:21Z](https://github.com/adamfisk/LittleProxy/issues/313#issuecomment-233666545).
- [adamjson · 2016-10-19T16:36:45Z](https://github.com/adamfisk/LittleProxy/issues/313#issuecomment-254868858).
- [phstudy · 2016-10-21T04:18:21Z](https://github.com/adamfisk/LittleProxy/issues/313#issuecomment-255290018).
- [wu-vincent · 2016-12-11T14:45:29Z](https://github.com/adamfisk/LittleProxy/issues/313#issuecomment-266286199).
- [jekh · 2016-12-27T01:12:44Z](https://github.com/adamfisk/LittleProxy/issues/313#issuecomment-269254033).
- [igor-dmitriev · 2016-12-30T15:08:40Z](https://github.com/adamfisk/LittleProxy/issues/313#issuecomment-269781875).
- [jekh · 2016-12-30T17:51:33Z](https://github.com/adamfisk/LittleProxy/issues/313#issuecomment-269801069).
- [igor-dmitriev · 2016-12-30T18:02:44Z](https://github.com/adamfisk/LittleProxy/issues/313#issuecomment-269802396).
- [igor-dmitriev · 2017-01-03T16:09:08Z](https://github.com/adamfisk/LittleProxy/issues/313#issuecomment-270150430).
- [jekh · 2017-01-31T07:55:13Z](https://github.com/adamfisk/LittleProxy/issues/313#issuecomment-276297373).
- [igor-dmitriev · 2017-01-31T10:03:39Z](https://github.com/adamfisk/LittleProxy/issues/313#issuecomment-276322550).
- [jekh · 2017-01-31T17:00:27Z](https://github.com/adamfisk/LittleProxy/issues/313#issuecomment-276423829).
- [jekh · 2017-02-27T01:10:51Z](https://github.com/adamfisk/LittleProxy/issues/313#issuecomment-282605348).
