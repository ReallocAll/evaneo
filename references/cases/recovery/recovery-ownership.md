<!-- retrieval: {"source_type":"static_review","topics":["testing","recovery","filesystem","ownership","interruption","Python","integration"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="design-recovery-before-mutation"></a>

# Design recovery before mutation {#design-recovery-before-mutation}

## Context {#context}

An integration test may need to stage artifacts and temporarily modify an existing environment. Successful assertions do not make the test safe if an interruption can lose the original files or if cleanup overwrites changes someone made afterward.

## Inspected design {#inspected-design}

The examined script established a run lock, checked for an interrupted prior run, recorded which managed resources originally existed, moved originals into a backup, installed temporary contents and updated a restoration manifest.

Restoration compared the expected installed state with the current state. When that comparison suggested an unexpected change, it refused automatic restoration and left the backup for reconciliation. The script also used a fresh test data area, bounded process execution and attempted restoration in finalization.

This separates several concerns that are often collapsed into a single cleanup block:

- Preventing two cooperating test runs from sharing the environment
- Knowing which resources belong to the test
- Preserving originals
- Detecting later conflicting changes
- Recovering after interruption
- Reporting residual side effects

## What the implementation does not prove {#what-the-implementation-does-not-prove}

The inspected fingerprint used metadata rather than a content digest. Same-sized changes with preserved timestamps can evade such a check. A lock only coordinates actors that honor it; it does not stop a user or unrelated process from modifying files.

Recording state around filesystem operations is not automatically an atomic transaction. Crashes between mutation and manifest update, partial copies, filesystem semantics, symlinks, new files in managed directories and finalization failures deserve explicit tests. No crash injection or restoration test was run in this review.

The source also recognized side effects outside the managed restoration set. A claim that “everything is restored” would therefore be broader than the inspected design supports.

## Applying the lesson {#applying-the-lesson}

Prefer a disposable environment when it provides equivalent evidence. If reuse is necessary, inventory the mutation set and determine restoration ownership before changing anything.

Use a journal or manifest whose recovery semantics are clear at every interruption point. Retain backups until restoration is verified. Refuse destructive automatic recovery when ownership or later changes are ambiguous. Report what remains untouched by recovery.

Test the normal path, interruption during each phase, a conflicting external edit and a second recovery attempt. Recovery should be observable, repeatable where intended and conservative about user data.

These are design and review practices. They grant no permission to install software, replace files, stop a service or restore data in a user's environment.
