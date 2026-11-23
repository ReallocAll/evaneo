<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:448"],"source_type":"public","date":"2026-07-30","topics":["testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-448-feat-event-add-player-sneak-and-sprint-events"></a>
# EndstoneMC/endstone #448: feat(event): add player sneak and sprint events {#endstonemc-endstone-448-feat-event-add-player-sneak-and-sprint-events}

Source: https://github.com/EndstoneMC/endstone/pull/448

## Evidence and attribution {#evidence-and-attribution}

Primary author: Packeting1. Created 2026-07-30T00:13:22Z; recorded state closed; merged False.

Packeting1 proposes sneak/sprint events and Windows environment handling. Wu asks for develop rather than main: main represents released API, and new event API belongs on the next-minor branch. Closed unmerged; #452 is the replacement, so do not count two independent accepted designs.

## Direct patch findings {#direct-patch-findings}

Adds noncancellable PlayerSneakEvent/PlayerSprintEvent with bool attempted state, C++umbrella/Python exports/stubs/bindings. PlayerAuthInput start/stop bits fire only when native current state differs, before existing block actions. Also replaces Windows getenv with _dupenv_s/free and false-on-error; Linux retains getenv. No tests added.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (8303 characters; SHA-256 b642492693cf4e68846e7f59504191688fd2415d94ddee36dfea0d0845f451bf), head 1893221236208d9061c5097096578c3f3a2829a2. This covers the supplied PR patch, not unrelated commits or historical intermediate revisions. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/448
- https://github.com/EndstoneMC/endstone/pull/448#issuecomment-5131695430
