<!-- retrieval: {"source_type":"public","topics":["engineering","comparator"],"limitations":"Comparative design guidance from external implementations; no upstream or target-implementation runtime tests were independently executed for this comparison.","source_ids":["public:comparator-source:storage:RE-REVISION","public:comparator-source:storage:RE-DESIGN","public:comparator-source:storage:RE-PRUNE-DOC","public:comparator-source:storage:RE-PRUNE-CODE"]} -->
# Defer cleanup rather than destroy recoverable data {#case}

## Mechanism {#mechanism}
Shared objects and incremental snapshots make deletion a reachability problem. Publishing a replacement set before removing older content can leave harmless temporary garbage; deleting live dependencies breaks recovery. Repacking may cost more I/O than its output size suggests, and running out of disk does not justify publishing incomplete references.

## Applicability and validation {#applicability}
Keep old recovery points until the replacement is provably reachable. Bound maintenance work and allow safe refusal when storage is exhausted. Do not import a complex pack protocol into a simple immutable single-file backup.

**Verification boundary:** No upstream or target-implementation runtime tests were independently executed for this comparison.

## References {#references}

Case S4 in the [source inventory](sources.json) identifies the revisions and scope of these sources.

- [restic v0.18.0 revision (RE-REVISION)](https://github.com/restic/restic/commit/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2)
- [restic repository ordering and reachability (RE-DESIGN)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/doc/design.rst)
- [restic retention and prune budgets (RE-PRUNE-DOC)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/doc/060_forget.rst)
- [restic prune planning and deletion order (RE-PRUNE-CODE)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/internal/repository/prune.go)
