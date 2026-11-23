<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:29"],"source_type":"public","date":"2024-07-30","topics":["concurrency","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-29-bug-the-command-register-seems-to-mask-the-reload-enum"></a>
# EndstoneMC/endstone #29: [bug] The command register seems to mask the "reload" enum {#endstonemc-endstone-29-bug-the-command-register-seems-to-mask-the-reload-enum}

Source: https://github.com/EndstoneMC/endstone/issues/29

## Review scope and state {#review-scope-and-state}

- Thread author: MengHanLOVE1027; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

The reload enum is absent from client suggestions although typing it works. Wu asks whether both client/console execute it; affirmative evidence isolates advertisement rather than parsing. smartcmd mentions knowing a fix but supplies none here. Wu links 46325a32420940cccb2dfe36bdde34f1929f1847, inspected in the mirror: updateCommands erases unregistered, unauthorized or above-GameDirectors commands instead of hiding them and assigning Internal permission; permission lookup also moves before lowercasing. Unauthorized reload metadata caused the client collision. Renaming the enum to reloading is the reporter’s diagnostic counterexample, not the selected solution.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/29
- https://github.com/EndstoneMC/endstone/issues/29#issuecomment-2258663753
- https://github.com/EndstoneMC/endstone/issues/29#issuecomment-2258666562
- https://github.com/EndstoneMC/endstone/issues/29#issuecomment-2258671959
- https://github.com/EndstoneMC/endstone/issues/29#issuecomment-2260679920
- https://github.com/EndstoneMC/endstone/commit/46325a32420940cccb2dfe36bdde34f1929f1847
