<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:325"],"source_type":"public","date":"2026-01-20","topics":["ffi","testing","performance","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstone-325-supplementary-video-review"></a>
# Endstone #325: supplementary video review {#endstone-325-supplementary-video-review}

Issue: https://github.com/EndstoneMC/endstone/issues/325  
Attachment ID: `80c773b8-8967-4510-8381-1b99ba81bee5`  
Attachment: https://github.com/user-attachments/assets/80c773b8-8967-4510-8381-1b99ba81bee5  
SHA-256: `3695d318a15cf76ed89b8aa14b43e966a456dd7b796513591d6a74fb1ef21094`  
Original dossier: [associated source analysis](../threads/EndstoneMC--endstone--issue-325.md)

## Coverage {#coverage}

H.264, 1920×1080, 60 fps, 2,130 decoded frames indexed 0–2,129, 35.5 seconds. Visually inspected 142 full-frame samples at indices 0, 15, …, 2,115 (0–35.25 seconds). Individually inspected nine native-resolution samples at indices 150, 360, 495, 780, 1,035, 1,260, 1,440, 1,515, and 1,935; these are among the same 142 frames, not additional unique frames.

This is expanded temporal sampling, not continuous playback or inspection of all 2,130 frames. 1,988 frames were not visually reviewed in this supplement. The previous review remains a separate historical record and is not added to these counts.

## Visible sequence {#visible-sequence}

Times below locate inspected samples, not exact action-onset or response latency measurements.

1. At 2.50 seconds the chat shows `/att add` followed by an `add_attachment` message for `hidden.command`.
2. At 6.00 seconds `/att test` reports that the permission is present. In the 7–8 second sampled interval, typing `/hidden` lacks a matching completion. At 8.25 seconds the displayed result is the cheats-disabled warning.
3. At 13.00 seconds the first reload is reported complete. Samples around 14–17 seconds show the hidden command in completion; at 17.25 seconds execution displays “Hidden command!”
4. At 21.00 seconds the chat shows `/att remove` and a `remove_attachment` message. The 24.00-second sample still offers the hidden command in completion.
5. At 25.25 seconds execution instead shows the unknown-command/permission warning. After a second reload, sampled completion around 30.5–32 seconds no longer offers the hidden command; at 32.25 seconds the cheats-disabled warning is visible again.

The video supports a difference between client-visible command completion and the displayed permission/command responses across attachment changes and reloads. It does not independently prove the implementation of permission checks, the cost of command packet rebuilding, or the proposed API remedy. Those remain attributed to the discussion. Nothing in the reviewed video establishes the separate later attachment-lifetime/use-after-free report.

## Audio {#audio}

One AAC stereo 48 kHz stream exists, with metadata duration 35.434 seconds. All decoded audio was checked numerically as float PCM: 3,401,728 scalar samples; all were nonzero; peak absolute amplitude 0.03371225669980049; RMS 0.0011968386547684; no NaNs. ffmpeg's separate volume summary reports approximately −58.4 dB mean and −29.4 dB maximum. These measurements do not establish whether the content is speech, game sound, or noise.

The audio was not listened to or transcribed. No transcript was produced, and the audio content remains unreviewed.

## Bounded result {#bounded-result}

The denser samples and native-resolution checks strengthen the narrow visible UI sequence. There is no full-video-review claim, no audio-only finding, no exact latency claim, and no implementation/fix verification. Audio content requires direct listening or transcription before drawing auditory conclusions.
