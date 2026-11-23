<!-- retrieval: {"source_ids":["public:thread:kkHAIKE/fake115:13"],"source_type":"public","date":"2016-09-15","topics":["concurrency","testing","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->

Source: https://github.com/kkHAIKE/fake115/pull/13

Thread state: closed; merged: False.

## Problem and constraints {#problem-and-constraints}
Enable the fake115 userscript on HTTPS and send its login POST over HTTPS.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
CoffeeScript PR #12 reviewer asks when HTTPS is needed, suggests matching both schemes, and asks how submission should detect the current scheme. JavaScript #13 has no discussion. Neither merged.

## Implementation and attribution {#implementation-and-attribution}
Both complete two-hunk patches replace the userscript @match HTTP scheme with HTTPS only and replace the passport login endpoint HTTP scheme with HTTPS. One is CoffeeScript source and the other its JavaScript counterpart; they make the same narrow change but are different artifacts. No adaptive scheme detection or both-scheme matcher is implemented.

Diff evidence (patch inspected, not bundled): [public PR files-changed view](https://github.com/kkHAIKE/fake115/pull/13/files) (live upstream diff, not the captured immutable patch). Declared changed files: 1.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
No tests or accepted result. The patch improves transport choice for matching HTTPS pages while dropping the old HTTP match; no claim that login integration remained compatible.

## Reusable decision and costs {#reusable-decision-and-costs}
Review execution-scope metadata together with network endpoints; switching a transport is not automatically the same as supporting both deployment contexts.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
