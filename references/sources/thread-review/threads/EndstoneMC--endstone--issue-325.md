<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:325"],"source_type":"public","date":"2026-01-20","topics":["lifetime","ffi","testing","performance","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-325-attachment-changes-do-not-take-effect-immediately"></a>
# EndstoneMC/endstone #325: Attachment changes do not take effect immediately {#endstonemc-endstone-325-attachment-changes-do-not-take-effect-immediately}

Source: https://github.com/EndstoneMC/endstone/issues/325

## Evidence and attribution {#evidence-and-attribution}

Primary author: zl9545. Created 2026-01-20T19:19:06Z; recorded state closed; merged not applicable.

## Two separate issues {#two-separate-issues}

zl9545's reproduction adds/removes a hidden.command permission after login. Execution checks changed but the client's command catalog did not refresh until reload; join-time attachment behaved differently. wu-vincent explained that permissions are intentionally decoupled from available-command packets because rebuilding/sending that catalog is expensive and plugins may batch updates. Call player.update_commands() once after all changes. allow-cheats permits execution but does not visually refresh the catalog.

## Escalation and ownership boundary {#escalation-and-ownership-boundary}

The reporter then supplied a different reproduction: invoke reload from a jump handler, then iterate effective_permissions and remove an attachment. Addition was rejected because the original plugin was disabled; removal reached a stale PermissionAttachment and crashed in getPermissions. wu-vincent first promised investigation, then split this genuine use-after-free into #421 because replacing the attachment/info ownership model with shared ownership breaks ABI and belongs in the next API version.

## Reuse and limits {#reuse-and-limits}

Do not dismiss a memory-safety report as expected behavior merely because its original UI symptom was intentional. Separate server authorization, client presentation, and object lifetime. A performance-motivated explicit sync point is compatible with immediate server permission checks, but it requires clear API guidance. The raw reproduction and stack were read; the ownership fix is not present in this thread.

## Additional source and attachment inspection {#additional-source-and-attachment-inspection}

Earlier inspection included the original PNG and 36 one-second samples. Supplementary review inspected 142 quarter-second full-frame samples (source frames 0, 15, …, 2115) spanning 0–35.25 seconds of the 35.5-second clip, with nine of those images also read individually at native resolution. The samples show attachment-add and permission-test messages while hidden is absent from completion and execution displays the cheats-disabled warning; after reload, hidden is offered and execution displays its success message. Removing the attachment leaves the completion visible while execution displays the unknown-command/permission warning; another reload removes the completion and the cheats-disabled warning returns. This corroborates the narrow separation between visible command completion and displayed permission/command responses; implementation mechanics and the separate later lifetime defect are not verified by this video. The clip has quiet, nonzero audio. The available audio-output helper returned “audio content omitted because you do not support audio input”; no listening or transcription occurred. Intermediate frames and all audio content remain unreviewed. No exact timing/latency or audio-only claim is made.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Attachment coverage: The original acquisition and frame-inspection logs are not distributed. The supplementary inspection recorded 142 quarter-second full-frame samples of the 2,130-frame clip, including nine selected native-resolution checks; 1,988 frames were not visually reviewed in this supplement. Nonzero audio exists but none was listened to or transcribed because audio input was unsupported. A screenshot corroborates visible content, not runtime causality.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/325
- https://github.com/EndstoneMC/endstone/issues/325#issuecomment-3774602332
- https://github.com/EndstoneMC/endstone/issues/325#issuecomment-3774710185
- https://github.com/EndstoneMC/endstone/issues/325#issuecomment-3774718404
- https://github.com/EndstoneMC/endstone/issues/325#issuecomment-4848991963
- https://github.com/user-attachments/assets/7c9ab594-de22-4dbc-8302-5e63e25aa20a
- https://github.com/user-attachments/assets/80c773b8-8967-4510-8381-1b99ba81bee5
