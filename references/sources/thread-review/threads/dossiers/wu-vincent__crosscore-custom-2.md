<!-- retrieval: {"source_ids":["public:thread:wu-vincent/crosscore-custom:2"],"source_type":"public","date":"2024-02-12","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->

Source: https://github.com/wu-vincent/crosscore-custom/issues/2

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Release consumer requests SHA256 checksums to verify downloaded ZIP integrity, while acknowledging that checksums do not themselves ensure the Actions build input was uncorrupted.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
Vincent states the latest release now includes checksum.txt for post-download verification.

## Implementation and attribution {#implementation-and-attribution}
No code patch is linked in the thread. The claim concerns generated distribution artifacts, not authentication or signatures.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Release claim not yet independently inspected; no checksum value or download test supplied.

## Reusable decision and costs {#reusable-decision-and-costs}
Pair published artifacts with checksums for transfer integrity, while distinguishing same-channel checksums from authenticity guarantees.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [wu-vincent · 2024-02-12T23:11:20Z](https://github.com/wu-vincent/crosscore-custom/issues/2#issuecomment-1939761715).

## Supplemental verification (supersedes earlier acquisition gaps) {#supplemental-verification-supersedes-earlier-acquisition-gaps}
Full Vincent commit df80a9f1cea508d36bd08ac490131f5b09ddfcac read. The release action previously used checksum.txt as release body text; it now attaches checksum.txt alongside custom-*.zip in a multiline files input and removes body_path. This verifies the publication mechanism behind the issue response. Artifact contents themselves were not downloaded/rehashed.
