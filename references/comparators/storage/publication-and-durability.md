<!-- retrieval: {"source_type":"public","topics":["engineering","comparator"],"limitations":"Comparative design guidance from external implementations; no upstream or target-implementation runtime tests were independently executed for this comparison.","source_ids":["public:comparator-source:storage:RE-REVISION","public:comparator-source:storage:SQ-REVISION","public:comparator-source:storage:SQ-ATOMIC","public:comparator-source:storage:SQ-WAL","public:comparator-source:storage:SQ-SYNC","public:comparator-source:storage:SQ-BACKUP-GUIDE","public:comparator-source:storage:SQ-PAGER","public:comparator-source:storage:RE-DESIGN","public:comparator-source:storage:RE-LOCAL","public:comparator-source:storage:RE-LOCAL-UNIX","public:comparator-source:storage:RE-LOCAL-WINDOWS","public:comparator-source:storage:RE-ARCHIVER"]} -->
# Publication, visibility and durability are different boundaries {#case}

## Mechanism {#mechanism}
SQLite rollback journals preserve old pages until commit; WAL commits establish a reader-visible boundary before later checkpointing. A restic snapshot becomes reachable only after the referenced packs and indexes exist. Atomic file replacement, a published recovery root, and durable post-power-loss storage are different claims; synchronous settings and platforms matter.

## Applicability and validation {#applicability}
Publish blocks before the manifest or root. Accept temporary orphaned blocks rather than publishing dangling references. Test faults before and after publication; process-kill tests are not hardware power-loss proof. Do not assume a SQLite COMMIT also commits external block files.

**Verification boundary:** No upstream or target-implementation runtime tests were independently executed for this comparison.

## References {#references}

Case S1 in the [source inventory](sources.json) identifies the revisions and scope of these sources. The SQLite documentation links are live pages.

- [restic v0.18.0 revision (RE-REVISION)](https://github.com/restic/restic/commit/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2)
- [SQLite 3.51.3 release and source ID (SQ-REVISION)](https://sqlite.org/releaselog/3_51_3.html)
- [SQLite rollback journal and commit ordering (SQ-ATOMIC)](https://sqlite.org/atomiccommit.html)
- [SQLite WAL publication and checkpointing (SQ-WAL)](https://sqlite.org/wal.html)
- [SQLite synchronization settings (SQ-SYNC)](https://sqlite.org/pragma.html#pragma_synchronous)
- [SQLite online backup guide (SQ-BACKUP-GUIDE)](https://sqlite.org/backup.html)
- [SQLite rollback pager invariants (SQ-PAGER)](https://github.com/sqlite/sqlite/blob/a5333afb9ad1aa473f8963b92caeaa955f47dc74/src/pager.c)
- [restic repository ordering and reachability (RE-DESIGN)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/doc/design.rst)
- [restic local save sequence (RE-LOCAL)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/internal/backend/local/local.go)
- [Unix directory synchronization (RE-LOCAL-UNIX)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/internal/backend/local/local_unix.go)
- [Windows directory synchronization (RE-LOCAL-WINDOWS)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/internal/backend/local/local_windows.go)
- [restic snapshot publication (RE-ARCHIVER)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/internal/archiver/archiver.go)
