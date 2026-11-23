<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:372"],"source_type":"public","date":"2026-04-08","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-372-feat-add-restart-command"></a>
# EndstoneMC/endstone #372: feat: add /restart command {#endstonemc-endstone-372-feat-add-restart-command}

Source: https://github.com/EndstoneMC/endstone/pull/372

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-04-08T21:23:26Z; recorded state closed; merged True.

## Problem, design and limits {#problem-design-and-limits}

Restart is split across the native process and Python supervisor: operator-only endstone.command.restart writes an expirable Unix-timestamp .endstone_restart marker then calls shutdown; the wrapper relaunches only for a marker under 60 seconds old. The intended safeguards distinguish stop from restart and suppress stale restart intent. The checklist is unchecked and body discloses Claude Code generation. File/clock/error handling needs patch inspection before treating this as a durable protocol.

## Direct patch findings {#direct-patch-findings}

C++restart command checks permission(defaultConsole), writes system-clock seconds to current-directory marker then shuts down even if write fails. Python loops bootstrap.run; marker younger than60seconds triggers restart, invalid/old marker removed. It accepts negative elapsed (future timestamps), depends on shutdown finishing within60s and matching server cwd, and write closes only at command return. No tests. Explicit intent marker avoids interpreting every crash as restart but does not make every restart robust.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (6154 characters; SHA-256 83aecb344a882b7180d2ed395986f381506416a131cc629b3db56c5a57ecb85f), head 21ff17072c11bc7101cc89e9778a8c7b04bf0940. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/372
