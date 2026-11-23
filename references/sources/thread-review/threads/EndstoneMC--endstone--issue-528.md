<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:528"],"source_type":"public","date":"2026-09-06","topics":["testing","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-528-segfault-in-scriptitemgameplayhandler-handleevent2-identical-stack-trace-on-two-separate-crashes-different"></a>
# EndstoneMC/endstone #528: Segfault in ScriptItemGameplayHandler::handleEvent2 (identical stack trace on two separate crashes, different add-on configurations) {#endstonemc-endstone-528-segfault-in-scriptitemgameplayhandler-handleevent2-identical-stack-trace-on-two-separate-crashes-different}

Source: https://github.com/EndstoneMC/endstone/issues/528

## Evidence and attribution {#evidence-and-attribution}

Primary author: mccxsarix-afk. Created 2026-09-06T19:50:44Z; recorded state closed; merged not applicable.

Two identical item-use crash traces persist across add-on changes, with25–30 online players. Reporter infers vanilla interaction; identical addresses alone do not prove determinism. Wu resolves an empty-hand item-use path: script beforeEvents listeners request a copy of a nonexistent item. Any listening pack can trigger it, explaining why removing one pack did not solve it. a4965c0 reportedly skips the script step for empty item uses. The crash ZIP and all distinct technical log content were subsequently inspected; no independent reproduction.

## Additional source and attachment inspection {#additional-source-and-attachment-inspection}

The ZIP contains two 7,150-byte crash reports and two console logs of 3,357 and 3,590 lines. Both complete reports were read and have the same stack and Linux Endstone 0.11.10/API 0.11 SIGSEGV signature. The first symbolized gameplay frame is ScriptItemGameplayHandler::handleEvent2 at line 58, through variant visitation; the earlier Bedrock addresses are unnamed. Both logs identify BDS 1.26.45.1. The second pack list removes SUPER OP ENCHANTMENTS while retaining other scripting packs. They also show the container reporting `Out of memory: false` and Crashpad reporting `no ptrace`; these narrow the report but do not prove empty-hand causality.

All retained technical output is represented after classifying player lifecycle/chat/death/ordinary game-command spam and exact timestamp-normalized duplicates as noise. Player identifiers and incidental chat are not reproduced.

Full follow-up commit a4965c0761aba9e1c6078c308e91fe179d477de2 was inspected: after Endstone's own item-use event handling succeeds, a null item_instance returns NotifyListeners/Continue before invoking the original script handler. Cancelled plugin events still return BypassListeners/Cancel. The two-file patch adds a changelog statement but no test. This directly validates the guard's placement, while the supplied logs alone cannot prove which native copy failed.

## Code and verification boundary {#code-and-verification-boundary}

All distinct supplied diagnostic evidence and complete relevant follow-up commit patches/messages were inspected. Public sources are linked under Traceability; the original acquisition, hashes, and per-file inspection inventories are not distributed. No runtime reproduction. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Attachment coverage: Both complete crash reports and every retained technical log line were read. Player lifecycle/chat/death/ordinary game-command noise and normalized duplicates were explicitly classified, not individually analyzed; filter counts and command-name inventory were recorded but are not distributed.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/528
- https://github.com/EndstoneMC/endstone/issues/528#issuecomment-5703239013
- https://github.com/user-attachments/files/31888238/endstone_crash_reports.zip
- https://github.com/EndstoneMC/endstone/commit/a4965c0761aba9e1c6078c308e91fe179d477de2
