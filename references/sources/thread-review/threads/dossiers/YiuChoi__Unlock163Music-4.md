<!-- retrieval: {"source_ids":["public:thread:YiuChoi/Unlock163Music:4"],"source_type":"public","date":"2016-04-01","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->

Source: https://github.com/YiuChoi/Unlock163Music/issues/4

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Android6/CyanogenMod13 installation said app not installed.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Maintainer suspected same package with different signature and advised removing old app. Vincent recognized another differently named plugin could share package ID and ultimately confirmed signature conflict resolved. Another user added guest-profile installations as possible context.

## Implementation and attribution {#implementation-and-attribution}
No patch/system changes performed. Display name differs from package identity.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Reporter-confirmed diagnosis, exact remediation unspecified.

## Reusable decision and costs {#reusable-decision-and-costs}
Package ID and signing certificate govern upgrade compatibility, not visible app name.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [YiuChoi · 2016-04-01T11:11:58Z](https://github.com/YiuChoi/Unlock163Music/issues/4#issuecomment-204350898).
- [wu-vincent · 2016-04-01T11:13:22Z](https://github.com/YiuChoi/Unlock163Music/issues/4#issuecomment-204351103).
- [YiuChoi · 2016-04-01T11:14:41Z](https://github.com/YiuChoi/Unlock163Music/issues/4#issuecomment-204351300).
- [471448446 · 2016-08-19T03:28:24Z](https://github.com/YiuChoi/Unlock163Music/issues/4#issuecomment-240918746).
- [wu-vincent · 2016-08-19T04:15:22Z](https://github.com/YiuChoi/Unlock163Music/issues/4#issuecomment-240923708).
