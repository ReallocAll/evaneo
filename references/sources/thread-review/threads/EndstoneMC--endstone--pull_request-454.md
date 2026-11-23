<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:454"],"source_type":"public","date":"2026-08-01","topics":["testing","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-454-fix-stubgen-annotate-server-getplayer-as-player-none"></a>
# EndstoneMC/endstone #454: fix(stubgen): annotate Server.get_player as Player | None {#endstonemc-endstone-454-fix-stubgen-annotate-server-getplayer-as-player-none}

Source: https://github.com/EndstoneMC/endstone/pull/454

## Evidence and attribution {#evidence-and-attribution}

Primary author: Rezn1r. Created 2026-08-01T19:27:44Z; recorded state closed; merged False.

Rezn1r's narrow stubgen workaround marks Server.get_player optional. Wu prefers fixing nullability at its binding origin with NotNull/Nullable annotations (524f52a70), which also applies to plugin-command and scoreboard returns rather than accumulating signature substitutions. An empty approval by niko is review state, not additional reasoning. The change anticipates removal of the older griffe rewrite obstacle; #413 provides the problem history.

## Direct patch findings {#direct-patch-findings}

Final captured PR patch still rewrites two exact stub signatures by string replacement and checks in Player|None stubs; it does NOT contain the preferred NotNull/Nullable source-level alternative. Do not confuse review recommendation with this diff.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (1316 characters; SHA-256 42498c157c13e2958b9efe0f5637c01dde3f737b676c2d36b9a151cf8244af94), head 887a5a816e8f18d024d8719171b9bcc406185012. This covers the supplied PR patch, not unrelated commits or historical intermediate revisions. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/454
- https://github.com/EndstoneMC/endstone/pull/454#issuecomment-5231412320
- https://github.com/EndstoneMC/endstone/pull/454#pullrequestreview-4877048093
