<!-- retrieval: {"source_ids":["public:thread:SeriousCache/UABE:102"],"source_type":"public","date":"2017-01-26","topics":["concurrency","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="seriouscache-uabe-102-feature-request-packing-files"></a>
# SeriousCache/UABE#102: Feature Request: Packing files {#seriouscache-uabe-102-feature-request-packing-files}

Source: https://github.com/SeriousCache/UABE/issues/102

Thread state: closed; merged: not applicable.

## Problem and constraints {#problem-and-constraints}
Requested Unity bundle packing/compression or format guidance.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
disunity recommendation failed InvalidSignature for reporter. 0x900x90 found unitypack: metadata-only compression loaded in Unity,128KiB data-block compression did not, while UABE could unpack identical originals. DerPopo acknowledged prior compression issues, later announced2.2 LZMA support plus assets metadata writing fix; LZ4 remained absent in earlier progress. Vincent asked status, not authored implementation.

## Implementation and attribution {#implementation-and-attribution}
No code patch. Named libraries are alternatives and format evidence only, not audited here.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Successful round-trip through same tool is weaker than consumer compatibility; release claim lacks reporter retest.

## Reusable decision and costs {#reusable-decision-and-costs}
Validate generated binary formats against independent consumers and separate compression, block framing and metadata correctness.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [0x900x90 · 2017-01-26T21:31:12Z](https://github.com/SeriousCache/UABE/issues/102#issuecomment-275520101).
- [ghost · 2017-01-27T16:13:21Z](https://github.com/SeriousCache/UABE/issues/102#issuecomment-275703920).
- [DerPopo · 2017-01-28T17:09:20Z](https://github.com/SeriousCache/UABE/issues/102#issuecomment-275860360).
- [0x900x90 · 2017-02-07T10:23:14Z](https://github.com/SeriousCache/UABE/issues/102#issuecomment-277957945).
- [DerPopo · 2017-04-22T15:22:31Z](https://github.com/SeriousCache/UABE/issues/102#issuecomment-296380411).
- [wu-vincent · 2017-08-14T12:25:22Z](https://github.com/SeriousCache/UABE/issues/102#issuecomment-322176530).
- [DerPopo · 2017-12-20T17:39:55Z](https://github.com/SeriousCache/UABE/issues/102#issuecomment-353131894).
