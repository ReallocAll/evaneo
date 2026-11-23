<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:187"],"source_type":"public","date":"2025-05-23","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-187-bug-install-error-code-5"></a>
# EndstoneMC/endstone #187: [bug] Install Error code 5 {#endstonemc-endstone-187-bug-install-error-code-5}

Source: https://github.com/EndstoneMC/endstone/issues/187

## Review scope and state {#review-scope-and-state}

- Thread author: xXLarryTFVWXx; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

xXLarryTFVWXx reports startup exit 5 on Windows 11 using a VSCode virtualenv. Wu interprets code 5 as likely permission denial, suggests Microsoft Store Python's restrictions as a possible cause, and recommends the portable release in an accessible directory or another Python distribution. No confirmation establishes that Store Python was actually installed or that this remedy worked. Preserve this as environment triage with alternative distribution paths, not a verified root cause or instruction to weaken security permissions.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/187
- https://github.com/EndstoneMC/endstone/issues/187#issuecomment-2908089172
