<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:61"],"source_type":"public","date":"2024-09-26","topics":["concurrency","diagnosis","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-61-bug-using-addon-scriptapi-to-call-the-registered-command-causes-a-crash"></a>
# EndstoneMC/endstone #61: [bug]Using Addon ScriptAPI to call the registered command causes a crash {#endstonemc-endstone-61-bug-using-addon-scriptapi-to-call-the-registered-command-causes-a-crash}

Source: https://github.com/EndstoneMC/endstone/issues/61

## Review scope and state {#review-scope-and-state}

- Thread author: 1013011563; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

1013011563’s transfer command works from chat but crashes through ScriptAPI player.runCommand. Wu first requests RelWithDebInfo plus adjacent PDB to resolve an unknown plugin frame, then identifies unchecked sender.asPlayer(). ScriptAPI uses a privileged proxy origin, not a Player, so asPlayer returns null. A null guard avoids the crash but deliberately does not enable ScriptAPI/command-block transfers; wu plans ProxiedCommandSender to support that case. The reporter confirms resolution. The supplied corrected example still leaves argument-count, stoi and bool-return issues outside the focused diagnosis; it is not a validated complete command implementation. Distinguish crash prevention from feature parity and retain the security/identity reason for proxy semantics.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/61
- https://github.com/EndstoneMC/endstone/issues/61#issuecomment-2380604616
- https://github.com/EndstoneMC/endstone/issues/61#issuecomment-2380607083
- https://github.com/EndstoneMC/endstone/issues/61#issuecomment-2380610397
- https://github.com/EndstoneMC/endstone/issues/61#issuecomment-2380611769
