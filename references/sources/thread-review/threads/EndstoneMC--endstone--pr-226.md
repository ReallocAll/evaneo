<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:226"],"source_type":"public","date":"2025-07-23","topics":["review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-226-changed-venvdir-to-home-virtualenvs-endstone-to-avoid-polluting-users-home-directory"></a>
# EndstoneMC/endstone #226: Changed VENV_DIR to "$HOME/.virtualenvs/endstone" to avoid polluting users home directory {#endstonemc-endstone-226-changed-venvdir-to-home-virtualenvs-endstone-to-avoid-polluting-users-home-directory}

Source: https://github.com/EndstoneMC/endstone/pull/226

## Review scope and state {#review-scope-and-state}

- Thread author: GyanPrakash2483; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (2 additions, 2 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

GyanPrakash2483 changes installer and launcher venv paths together from generic $HOME/venv to $HOME/.virtualenvs/endstone, citing namespace collision and virtualenvwrapper convention. Full 2-file patch read; Wu approves without additional rationale. This isolates the application's environment name, but the patch contains no migration of an existing environment and no claim that hidden directories alone provide security isolation.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/226
- https://github.com/EndstoneMC/endstone/pull/226#issuecomment-3113094038
