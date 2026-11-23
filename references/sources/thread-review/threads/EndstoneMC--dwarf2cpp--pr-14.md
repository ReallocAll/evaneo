<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/dwarf2cpp:14"],"source_type":"public","date":"2026-05-16","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-dwarf2cpp-14-fix-visitor-ignore-dwatdeclfile-line-in-visitnamespace"></a>
# EndstoneMC/dwarf2cpp #14: fix(visitor): ignore DW_AT_decl_file/line in visit_namespace {#endstonemc-dwarf2cpp-14-fix-visitor-ignore-dwatdeclfile-line-in-visitnamespace}

Source: https://github.com/EndstoneMC/dwarf2cpp/pull/14

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (3 additions, 0 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu diagnoses namespace DIE crashes on DW_AT_decl_file and DW_AT_decl_line falling through an exhaustive match to ValueError. Other visitors already ignore these attributes. The merged three-line fix adds the same skip-set before namespace attribute matching. Rationale is namespace-specific: namespaces reopen across files and members have their own locations, so attaching a single declaration site to a namespace is unnecessary. The alternative of accepting all unknown attributes is not chosen; the allowlist remains narrow. The reproduction test in the PR remains unchecked, so merge and apparent local consistency do not establish that the supplied binary was retested.



## Source index {#source-index}

- https://github.com/EndstoneMC/dwarf2cpp/pull/14
