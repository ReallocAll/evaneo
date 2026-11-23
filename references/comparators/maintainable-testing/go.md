<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2026-10-30","topics":["maintainability","complexity","refactor","historical-review","compiler"],"limitations":"Linked commit patches and rationale were inspected; upstream builds/tests were not rerun. Cases are illustrative, not statistically representative or proof of production impact."} -->
# Go: historical complexity-removal patches {#overview}

These **2** entries summarize selected historical commits about implementation complexity and maintenance. Source summaries paraphrase the linked diffs; inspect those commits before applying a lesson to another project. The design takeaways are conditional, not universally applicable rules or independently verified runtime outcomes.

## Remove unused HTTP2 Transport dialing path {#go-a33c32004dcc}

**Evidence:** [GO-a33c32004dcc — exact historical commit](https://github.com/golang/go/commit/a33c32004dcc) (commit date: 2026-09-11).

**Observed prior design:** net/http internal HTTP2 inherited standalone x/net dialing path. **Why it mattered:** Original alternate x/net client path no longer relevant.

**Observed decision:** Dial code deleted. **Conditional design inference:** Remove superseded internal paths only after checking real supported versions and contracts.

**Boundary:** Preserve public behavior needed by current HTTP2 integration. The linked patch and rationale were inspected, not rebuilt or executed; the change alone does not establish production impact or a universal preference.

## Remove unused SSA poset unsigned machinery {#go-0c0dacdf0b84}

**Evidence:** [GO-0c0dacdf0b84 — exact historical commit](https://github.com/golang/go/commit/0c0dacdf0b84) (commit date: 2026-07-20).

**Observed prior design:** SSA proof poset once tracked signed vs unsigned mode. **Why it mattered:** No reader after CL 599795; writes and calls persisted.

**Observed decision:** Dead code deleted. **Conditional design inference:** Delete dead state and derive available information instead of storing another copy.

**Boundary:** If mode affects future proofs, use evidence before reintroducing. The linked patch and rationale were inspected, not rebuilt or executed; the change alone does not establish production impact or a universal preference.
