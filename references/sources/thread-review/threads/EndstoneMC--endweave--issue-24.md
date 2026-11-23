<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endweave:24"],"source_type":"public","date":"2026-05-07","topics":["ffi","testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endweave-24-food-bug"></a>
# EndstoneMC/endweave #24: food bug {#endstonemc-endweave-24-food-bug}

Source: https://github.com/EndstoneMC/endweave/issues/24

Primary text and available images were inspected; the case describes attachment coverage and has no runtime reproduction.

## Evidence and attribution {#evidence-and-attribution}

Primary author: MipaSenpai. Created 2026-05-07T11:10:04Z; recorded state closed; merged not applicable.

Windows 0.11.3 / Endweave 0.4.1 food defect is documented in the linked video. The expanded visual review is described below. Wu claims a 0.4.2 fix without a mechanism or subsequent retest; that fix remains unverified.

## Attachment inspection {#attachment-inspection}

The captured 12.766667-second, 60 fps video was reviewed in 52 quarter-second full-frame samples, plus every frame 195–270 (3.25–4.50 seconds) in terminal/gameplay regions and selected native-resolution images. It shows Endstone 0.11.3 / Endweave 0.4.1 and an apple-use-like animation. Disconnect log lines appear at frame 230 (3.833333 seconds), followed by a black client viewport at frame 241 (4.016667 seconds). This establishes screen-recording order only. The terminal remains visible; server-process liveness was not established by a subsequent command response or independent check. No server-exit/crash message is visible in the reviewed frames, but the capture does not rule out server failure or diagnose a client crash. The video supports an apple-use-associated disconnect/black-viewport sequence, without establishing an exact packet cause. The entire available audio stream decodes to exact digital silence; this numerical result is not a listening claim. Most other intermediate frames remain unreviewed. Wu’s 0.4.2 fix remains unverified by a subsequent retest.

## Code and verification boundary {#code-and-verification-boundary}

No implementation fix independently verified. Original attachment-download status and unavailable-source records are not distributed; the public video is linked below. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Attachment coverage: The original acquisition and frame-inspection logs are not distributed. The supplementary inspection recorded 52 quarter-second full-frame samples, 76 consecutive region-reviewed frames (195–270), and selected native-resolution checks: 122 unique frames with some review, of which 55 have full-frame review and 67 additional frames have region-only review; 644 frames have no visual review in the supplement. All available decoded audio samples are exactly zero. This is not whole-video semantic review.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endweave/issues/24
- https://github.com/EndstoneMC/endweave/issues/24#issuecomment-4401829380
- https://github.com/user-attachments/assets/3c36aa2e-972e-4b4d-8cbd-1e0677896fc2
