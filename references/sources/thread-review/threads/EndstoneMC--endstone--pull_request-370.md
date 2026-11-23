<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:370"],"source_type":"public","date":"2026-04-07","topics":["lifetime","testing","review","selection","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-370-refactor-use-pip-uninstall-instead-of-folder-deletion-on-plugin-reload"></a>
# EndstoneMC/endstone #370: refactor: use pip uninstall instead of folder deletion on plugin reload {#endstonemc-endstone-370-refactor-use-pip-uninstall-instead-of-folder-deletion-on-plugin-reload}

Source: https://github.com/EndstoneMC/endstone/pull/370

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-04-07T19:01:09Z; recorded state closed; merged False.

## Problem, design and limits {#problem-design-and-limits}

Unmerged proposal replaces recursive deletion of the whole .local prefix during Python loader destruction with pip uninstall of tracked plugin distribution names. Motivation: Windows file locks and repeated reinstall of unchanged shared dependencies. Dependencies should survive reload, new wheels still install, and LD_PRELOAD stripping is removed as already handled by main.cpp. Body discloses Claude Code generation. No discussion explains why it closed unmerged; do not promote its intended behavior into a shipped design.

## Direct patch findings {#direct-patch-findings}

Uses global endstone entry-point distributions to run sys.executable -m pip uninstall at construction and __del__, without check=True or limiting to plugins/.local; removes directory-based deletion and removes LD_PRELOAD sanitization from install subprocess. Therefore distribution-aware cleanup preserves dependency packages, but global environment scope/destructor subprocess failure and inherited preload are risks, not guaranteed clean isolation. Docstring says destruction, code additionally uninstalls at startup. No tests.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (6959 characters; SHA-256 ca39b39429a53dc2626a14985af5bc1dac3a7cbbf3fa6eb893dd7625679ec3a4), head e5cb33ce478028021ca96e9c449bb94724a22390. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/370
