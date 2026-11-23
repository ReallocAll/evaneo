<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2026-10-30","topics":["maintainability","complexity","refactor","historical-review","linux","kernel"],"limitations":"Linked commit patches and rationale were inspected; upstream builds/tests were not rerun. Cases are illustrative, not statistically representative or proof of production impact."} -->
# Linux kernel: historical complexity-removal patches {#overview}

These **6** entries summarize selected historical commits about implementation complexity and maintenance. Source summaries paraphrase the linked diffs; inspect those commits before applying a lesson to another project. The design takeaways are conditional, not universally applicable rules or independently verified runtime outcomes.

## Eliminate dead enum hal_status abstraction {#lin-f56356ba219d}

**Evidence:** [LIN-f56356ba219d — exact historical commit](https://github.com/torvalds/linux/commit/f56356ba219d) (commit date: 2026-10-13).

**Observed prior design:** The vendor-config driver functions always returned HAL_STATUS_SUCCESS. **Why it mattered:** A return value which never conveys failure is a phantom interface.

**Observed decision:** Removed three always-success paths, the ghost prototype and status type. **Conditional design inference:** Call the underlying existing function directly when the layer adds no invariant or policy.

**Boundary:** Internal driver-only contract; not an exported failure-reporting ABI. The linked patch and rationale were inspected, not rebuilt or executed; the change alone does not establish production impact or a universal preference.

## Remove temp_mm_state_t abstraction {#lin-f5afa2e8efda}

**Evidence:** [LIN-f5afa2e8efda — exact historical commit](https://github.com/torvalds/linux/commit/f5afa2e8efda) (commit date: 2025-04-11).

**Observed prior design:** x86 text patching temporarily changes page tables. **Why it mattered:** Type name incorrectly communicates that it stores temporary MM rather than previous MM.

**Observed decision:** Abstraction removed in alternative.c. **Conditional design inference:** Keep a direct implementation or reuse an existing local primitive until an actual variant requires shared structure.

**Boundary:** Does not forbid meaningful strong types with invariants. The linked patch and rationale were inspected, not rebuilt or executed; the change alone does not establish production impact or a universal preference.

## Remove early_panic indirection {#lin-d214484f50f4}

**Evidence:** [LIN-d214484f50f4 — exact historical commit](https://github.com/torvalds/linux/commit/d214484f50f4) (commit date: 2025-12-14).

**Observed prior design:** Early boot error handling must report panic. **Why it mattered:** Both routines print; duplicated output and extra helper.

**Observed decision:** Wrapper removed. **Conditional design inference:** Call the underlying existing function directly when the layer adds no invariant or policy.

**Boundary:** A wrapper may remain if it changes behaviour or enforces a stable boundary. The linked patch and rationale were inspected, not rebuilt or executed; the change alone does not establish production impact or a universal preference.

## Remove AppArmor af_select macro {#lin-9045aa25d17c}

**Evidence:** [LIN-9045aa25d17c — exact historical commit](https://github.com/torvalds/linux/commit/9045aa25d17c) (commit date: 2025-01-18).

**Observed prior design:** AppArmor selected network address family. **Why it mattered:** Macro hid the actual selection and did not simplify reading.

**Observed decision:** Macro removed. **Conditional design inference:** Call the underlying existing function directly when the layer adds no invariant or policy.

**Boundary:** Security mechanism itself is not removed. The linked patch and rationale were inspected, not rebuilt or executed; the change alone does not establish production impact or a universal preference.

## Remove unnecessary dma-fence callbacks {#lin-2ce07fea3cc8}

**Evidence:** [LIN-2ce07fea3cc8 — exact historical commit](https://github.com/torvalds/linux/commit/2ce07fea3cc8) (commit date: 2025-03-06).

**Observed prior design:** SW sync printed fence-related values. **Why it mattered:** Caller already knew the concrete timeline fence.

**Observed decision:** Callbacks removed from SW sync, virtgpu and vgem. **Conditional design inference:** Keep a direct implementation or reuse an existing local primitive until an actual variant requires shared structure.

**Boundary:** Keep callbacks if multiple real fence implementations differ. The linked patch and rationale were inspected, not rebuilt or executed; the change alone does not establish production impact or a universal preference.

## Remove needless MIPS ISA abstraction {#lin-33679a50370d}

**Evidence:** [LIN-33679a50370d — exact historical commit](https://github.com/torvalds/linux/commit/33679a50370d) (commit date: 2017-04-12).

**Observed prior design:** MIPS assembly utilities support alternative ISA modes. **Why it mattered:** Build includes exactly one of two concrete implementations.

**Observed decision:** ISA macro layer removed. **Conditional design inference:** Implement current known usage; defer hypothetical branches.

**Boundary:** Build-time alternatives still exist; do not remove actual architecture selection. The linked patch and rationale were inspected, not rebuilt or executed; the change alone does not establish production impact or a universal preference.
