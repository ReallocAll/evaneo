<!-- retrieval: {"source_ids":["public:thread:seven332/EhViewer:60"],"source_type":"public","date":"2015-04-21","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->

Source: https://github.com/seven332/EhViewer/issues/60

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Quick-search shortcuts show homepage content instead of intended search results.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Maintainer asks the user to long-press/drag left to inspect saved settings. Another participant suspects creating a shortcut before actually searching and mistaking its name for search tags. Another user confirms the symptom, later asks deletion: drag right, confirmed solved. Maintainer eventually says it should be fixed in 0.9.0.

## Implementation and attribution {#implementation-and-attribution}
No patch or diagnostic data supplied. The deletion instruction is confirmed; the original search failure’s cause is not.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Closed with release-fix claim only. Do not conflate successful shortcut deletion with verification of search semantics.

## Reusable decision and costs {#reusable-decision-and-costs}
Differentiate shortcut labels from saved query state, and distinguish separate questions in one issue.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [seven332 · 2015-04-21T14:49:19Z](https://github.com/seven332/EhViewer/issues/60#issuecomment-94826532).
- [wu-vincent · 2015-04-22T09:46:11Z](https://github.com/seven332/EhViewer/issues/60#issuecomment-95102930).
- [seven332 · 2015-04-22T10:17:15Z](https://github.com/seven332/EhViewer/issues/60#issuecomment-95117390).
- [MofuMoca · 2015-04-27T15:30:41Z](https://github.com/seven332/EhViewer/issues/60#issuecomment-96709750).
- [74rbq · 2015-05-02T13:58:20Z](https://github.com/seven332/EhViewer/issues/60#issuecomment-98361741).
- [74rbq · 2015-07-11T07:33:36Z](https://github.com/seven332/EhViewer/issues/60#issuecomment-120592321).
- [seven332 · 2015-07-11T11:54:29Z](https://github.com/seven332/EhViewer/issues/60#issuecomment-120607697).
- [74rbq · 2015-07-11T14:09:36Z](https://github.com/seven332/EhViewer/issues/60#issuecomment-120624794).
- [seven332 · 2016-03-17T12:59:12Z](https://github.com/seven332/EhViewer/issues/60#issuecomment-197868431).
