<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endweave:24"],"source_type":"public","date":"2026-05-07","topics":["ffi","diagnosis","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endweave-24-supplementary-video-review"></a>
# Endweave #24: supplementary video review {#endweave-24-supplementary-video-review}

Issue: https://github.com/EndstoneMC/endweave/issues/24  
Attachment ID: `3c36aa2e-972e-4b4d-8cbd-1e0677896fc2`  
Attachment: https://github.com/user-attachments/assets/3c36aa2e-972e-4b4d-8cbd-1e0677896fc2  
SHA-256: `32d6e8c2ac8a911a4e97e93bf44bcbb2f47d275c0f036a63d9b8bb96ecd27b0e`  
Original dossier: [associated source analysis](../threads/EndstoneMC--endweave--issue-24.md)

## Coverage {#coverage}

H.264, 1920×1080, 60 fps, 766 decoded frames indexed 0–765, 12.766667 seconds.

- Inspected 52 full-frame quarter-second samples at indices 0, 15, …, 765.
- Inspected all 76 consecutive frames 195–270 (3.25–4.50 seconds) in two selected regions: terminal `(240,630)–(960,770)` and gameplay `(1000,550)–(1920,1060)`, coordinates in the original 1920×1080 frame.
- Read native-resolution full frames at quarter-second indices 105, 135, 195, 240, 390, 690 and transition indices 229, 230, 240, 241. Frame 240 is a duplicate; there are nine distinct native-resolution frames.
- In total, 122 unique source frames had some visual inspection: 55 had full-frame inspection and 67 additional frames had only the stated region inspection. The remaining 644 frames were not visually inspected in this supplement. Outside the selected regions, the region-only frames remain unreviewed.

The consecutive transition review closes the sampling gap for the two selected regions over 3.25–4.50 seconds only. It is not a whole-video review. A separate mechanical luminance scan of all frames was used only to locate the black-viewport transition.

## Visible sequence and boundaries {#visible-sequence-and-boundaries}

The native-resolution images show Endstone 0.11.3 (Minecraft 26.12) and Endweave 0.4.1 in terminal output.

- The sampled opening shows OBS and then the terminal beside the game. The player holds an apple.
- Across the consecutive-frame interval the apple raises/moves in a use/eating-like animation. The capture does not directly reveal the user's physical input or the underlying packet.
- At frame 229 (3.816667 seconds), the terminal still ends with the player-join message.
- Frame 230 (3.833333 seconds) is the first frame within the consecutively inspected range displaying player-disconnect/left-game log lines. The game view still renders the apple and terrain.
- Frame 240 (4.000000 seconds) still shows the game image. Frame 241 (4.016667 seconds) shows a black client viewport with the window title and cursor visible.
- Later quarter-second samples through 11.50 seconds continue showing the black game viewport and unchanged terminal output. At 11.75 seconds onward OBS is foregrounded.

The disconnect-log display precedes the black viewport by 11 recorded frames, approximately 0.183333 seconds. This is presentation order in a screen recording. It is not a measurement of network latency, server/client clock synchronization, or causal delay.

The visible terminal persists, but no subsequent command response, heartbeat, or independent liveness check was observed. Therefore the original wording “server console remains alive” must be narrowed to “the terminal remains visible; server-process liveness was not established.” There is no visible server-exit/crash message in the reviewed frames, but that absence does not prove that no server failure occurred. The clip supports an apple-use-associated disconnect and black-viewport sequence, not a diagnosed client crash, exact packet defect, or verified fix.

## Audio {#audio}

One AAC stereo 48 kHz stream exists, with metadata duration 12.714 seconds. The entire available stream was decoded to original-rate stereo float PCM and checked: 1,220,608 scalar samples; zero nonzero samples; peak absolute amplitude 0; RMS 0; no NaNs. Every decoded audio sample is exactly zero.

Thus there is no audible speech or sound in the decoded captured audio to transcribe. This is a complete numerical silence check, not a claim of listening. Audio duration and video duration differ slightly; nothing is inferred beyond the available audio stream or outside the recorded asset.

## Bounded result {#bounded-result}

The important visual transition is now reviewed at source frame rate within the stated regions, and the audio-content gap is closed by whole-stream digital silence. Most other intermediate frames remain unreviewed. No upstream code was executed, runtime reproduction performed, root cause established, or version 0.4.2 retest verified. Preserve those boundaries in any derived dossier.
