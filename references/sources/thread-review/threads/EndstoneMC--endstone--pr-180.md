<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:150","public:thread:EndstoneMC/endstone:180"],"source_type":"public","date":"2025-03-06..2025-05-16","topics":["ffi","testing","api","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-180-refactor-the-command-api"></a>
# EndstoneMC/endstone #180: Refactor the Command API {#endstonemc-endstone-180-refactor-the-command-api}

Source: https://github.com/EndstoneMC/endstone/pull/180

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (434 additions, 340 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

<a id="engineering-reading-and-attribution"></a>
## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu marks three goals complete: beta Script API custom-command compatibility, LeviStone LegacyScriptEngine compatibility, and explicit permissions allowing non-operators to run operator commands (related issue 150). The body describes supported native origins routing through Endstone CommandSender/CommandMap and back through native wrappers, with unsupported origins retaining native dispatch and a custom-command adapter. There are no comments or reviews. The complete 21-file patch was read; the observations below distinguish its implementation from the stated goals.

### Complete patch inspection {#complete-patch-inspection}

The implementation replaces a global snapshot/restore of native registry maps with targeted custom-command registration/unregistration. Native commands are looked up dynamically and wrapped on demand; only custom commands are retained in Endstone's map. Thus commands introduced later by Script API or another loader need not be frozen out by the startup snapshot. getCommand now returns shared_ptr, keeping a returned custom command alive through dispatch. Registry aliases and CommandName/CommandAliases enum entries are removed individually; custom enums are cleared and empty names can be reused. Removing associated enum constraints is explicitly still TODO.

Permission checking and execution are coordinated at two layers. A MinecraftCommandWrapper checks Endstone permissions, compiles the native command, then sets that command instance's native permission level to Any before running it. AvailableCommands packets are filtered per player, permitted entries are advertised as Any, and the relevant host/elevated semantic constraints are removed. This makes an explicit permission grant useful for a non-operator without granting global operator status. Cheat/other constraints are not indiscriminately removed. Unknown-command feedback replaces permission-denied feedback. A separate corrected ternary fixes setOp(true) to assign Admin rather than Any.

The old CommandOutput padding flag and CommandOutputWithSender subclass disappear. The native adapter obtains a sender from the origin, falling back to an initialized origin wrapper for unsupported types, then calls the custom command directly. Soft-enum replacement/addition now updates storage and broadcasts corresponding packets. Native permission registration is idempotent; familiar harmless commands receive default permissions.

Limits visible in this snapshot: findEnum constructs an enum-value symbol rather than fromEnumIndex (its current caller strips flags to an index, so that caller alone does not prove a defect). Custom enum exclusion compares a const-char pointer against string literals; content-based comparison would express the intended Boolean/Block exemption more reliably. Alias entries can cause repeated unregistration calls, mostly rendered harmless by missing-signature checks. Registry cleanup is not a complete reclamation of all parser structures. No new automated tests accompany the claimed cross-loader compatibility; it remains an author completion claim backed by the observed architecture, not independent integration validation.

Exact inspected base/head: d8acbb9489e1767e34245eaa592def6f6ee4749e…490aa8b5fa03286fdb6d52f062af52a2987816b5. The complete PR diff was inspected; no upstream code or tests were executed.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/180
