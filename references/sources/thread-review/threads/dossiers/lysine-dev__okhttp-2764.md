<!-- retrieval: {"source_ids":["public:thread:lysine-dev/okhttp:2764"],"source_type":"public","date":"2016-08-01","topics":["concurrency","testing","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="lysine-dev-okhttp-2764-bug-with-cookie-parsing"></a>
# lysine-dev/okhttp#2764: Bug with cookie parsing. {#lysine-dev-okhttp-2764-bug-with-cookie-parsing}

Source: https://github.com/lysine-dev/okhttp/issues/2764

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Vincent interpreted Set-Cookie path metadata as a missing second Cookie or missing cookie value. A second participant expected Path/Domain to reappear in outgoing Cookie headers.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
swankjesse first asks for a precise failing test. The later exchange establishes that request Cookie headers intentionally omit response-side Path/Domain attributes; the maintainer calls the behavior designed and browser-consistent. The reporter’s logging only prints name and value, so it cannot establish that stored cookie attributes were discarded.

## Implementation and attribution {#implementation-and-attribution}
Inline CookieJar clears all saved cookies on every response and returns the entire list for every request URL. That example is not a safe general jar: it neither merges by cookie identity nor filters stored cookies by destination. These are separate static concerns, not the diagnosed formatting bug. Credential values were redacted in preserved text. Screenshots repeat the described request/response attribute contrast and were not needed to infer the explicitly stated resolution; no image-derived secret values were inspected or copied.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Closed as intended behavior, no library fix. No full failing test provided.

## Reusable decision and costs {#reusable-decision-and-costs}
Separate response cookie metadata, storage selection policy and request serialization. A missing attribute in a name/value log is not proof the parser discarded it.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [swankjesse · 2016-08-01T12:44:38Z](https://github.com/lysine-dev/okhttp/issues/2764#issuecomment-236570376).
- [whichname · 2016-09-07T03:55:22Z](https://github.com/lysine-dev/okhttp/issues/2764#issuecomment-245168029).
- [swankjesse · 2016-09-07T04:14:57Z](https://github.com/lysine-dev/okhttp/issues/2764#issuecomment-245170245).
- [whichname · 2016-09-07T04:32:30Z](https://github.com/lysine-dev/okhttp/issues/2764#issuecomment-245172232).
- [whichname · 2016-09-07T04:43:34Z](https://github.com/lysine-dev/okhttp/issues/2764#issuecomment-245173632).
- [swankjesse · 2016-09-07T11:14:14Z](https://github.com/lysine-dev/okhttp/issues/2764#issuecomment-245249572).
