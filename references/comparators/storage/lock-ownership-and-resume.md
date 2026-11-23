<!-- retrieval: {"source_type":"public","topics":["engineering","comparator"],"limitations":"Comparative design guidance from external implementations; no upstream or target-implementation runtime tests were independently executed for this comparison.","source_ids":["public:comparator-source:storage:RE-REVISION","public:comparator-source:storage:RE-DESIGN","public:comparator-source:storage:RE-LOCK-HISTORY","public:comparator-source:storage:RE-LOCK-PRIORITY-HISTORY","public:comparator-source:storage:RE-LOCK","public:comparator-source:storage:RE-LOCK-MANAGER","public:comparator-source:storage:RE-SEMA"]} -->
# Recovery requires proven ownership after lock loss {#case}

## Mechanism {#mechanism}
A timeout or stale lock marker does not by itself establish exclusive ownership. A repository protocol must distinguish locking, renewal, freeze behavior, in-flight operations, and safe resumption. Rate limiting ordinary data traffic must not starve lock-renewal traffic.

## Applicability and validation {#applicability}
For a single local writer, prefer a simple local ownership model. For truly shared writers, test lost renewal, concurrent maintenance, and re-acquisition before any destructive recovery. Resume from an already published recovery point rather than treating it as a new login.

**Verification boundary:** No upstream or target-implementation runtime tests were independently executed for this comparison.

## References {#references}

Case S2 in the [source inventory](sources.json) identifies the revisions and scope of these sources.

- [restic v0.18.0 revision (RE-REVISION)](https://github.com/restic/restic/commit/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2)
- [restic repository ordering and reachability (RE-DESIGN)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/doc/design.rst)
- [Lock expiry after standby (RE-LOCK-HISTORY)](https://github.com/restic/restic/commit/d92957dd78ca01dc16a7998ca6a9e339fe23044b)
- [Lock refresh during slow uploads (RE-LOCK-PRIORITY-HISTORY)](https://github.com/restic/restic/commit/d05f6211d151783cb2f1a26d05e5965ad78a89db)
- [Lock acquisition and stale renewal (RE-LOCK)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/internal/restic/lock.go)
- [Expiry monitoring and conditional recovery (RE-LOCK-MANAGER)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/internal/repository/lock.go)
- [Lock traffic priority and freeze behavior (RE-SEMA)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/internal/backend/sema/backend.go)
