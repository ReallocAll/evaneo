<!-- retrieval: {"source_type":"public","topics":["engineering","comparator"],"limitations":"Comparative design guidance from external implementations; no upstream or target-implementation runtime tests were independently executed for this comparison.","source_ids":["public:comparator-source:storage:RE-REVISION","public:comparator-source:storage:SQ-BACKUP-API","public:comparator-source:storage:SQ-BACKUP-C","public:comparator-source:storage:RE-CHECK-DOC","public:comparator-source:storage:RE-CHECK-CODE","public:comparator-source:storage:RE-BACKUP-DOC"]} -->
# Report what each verification layer actually proved {#case}

## Mechanism {#mechanism}
Hash checks, repository structure checks, restore tests, and end-to-end backup completion prove different things. An optimization that avoids re-reading unchanged blocks does not prove the remote medium was checked. A producer may fail even when a consumer exits successfully; cleanup success alone is not backup success.

## Applicability and validation {#applicability}
Report which layers passed: source consistency, stored-object hashes, reachable snapshot, and actual restoration. Distinguish sampled checks from complete coverage. Verify the producer pipeline and stored recovery root before claiming success.

**Verification boundary:** No upstream or target-implementation runtime tests were independently executed for this comparison.

## References {#references}

Case S3 in the [source inventory](sources.json) identifies the revisions and scope of these sources. The SQLite documentation links are live pages.

- [restic v0.18.0 revision (RE-REVISION)](https://github.com/restic/restic/commit/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2)
- [SQLite backup completion contract (SQ-BACKUP-API)](https://sqlite.org/c3ref/backup_finish.html)
- [SQLite completion and cleanup paths (SQ-BACKUP-C)](https://github.com/sqlite/sqlite/blob/a5333afb9ad1aa473f8963b92caeaa955f47dc74/src/backup.c)
- [restic integrity checks and sampling (RE-CHECK-DOC)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/doc/045_working_with_repos.rst)
- [restic data selection for checks (RE-CHECK-CODE)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/cmd/restic/cmd_check.go)
- [restic change detection and backup exit status (RE-BACKUP-DOC)](https://github.com/restic/restic/blob/d401ad6c1ec93a8fbcfcd9f6855a7a4468878ec2/doc/040_backup.rst)
