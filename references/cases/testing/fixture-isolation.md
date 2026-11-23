<!-- retrieval: {"source_type":"static_review","topics":["testing","parallelism","filesystem","fixtures","cleanup","process-state"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="isolate-the-external-resources-a-fixture-actually-uses"></a>

# Isolate the external resources a fixture actually uses {#isolate-the-external-resources-a-fixture-actually-uses}

## Failure mechanism {#failure-mechanism}

Separate test processes can still share an external resource. If each process initializes its local identifier counter the same way and derives a directory beneath the same working directory, their fixtures can create, overwrite or delete each other's files. Process separation alone is not filesystem isolation.

## Observed change {#observed-change}

Two inspected fixture patches saved the previous working directory, created a test-specific temporary root, ran the fixture within it, destroyed dependent runtime objects, restored the previous directory and then removed the temporary root.

This addressed the collision at the namespace actually used by the implementation. Merely changing a test label or a context identifier would not establish that every derived path had moved into an isolated root.

The teardown order matters. Objects may still refer to files or interpret relative paths during destruction. Cleanup must respect those dependencies, and restoring process state should happen before removing the directory that was used as the current location.

## Review checklist {#review-checklist}

- Enumerate resources outside the fixture object: directories, ports, caches, environment variables, registries and process-global state.
- Determine whether identity is unique across cases, workers, processes and simultaneous test runs.
- Keep ownership of the temporary root explicit; remove only resources owned by this run.
- Exercise setup failure and interrupted teardown, not only successful cleanup.
- Prefer APIs that accept an explicit root when changing the process working directory would race other activity.

## Important limits {#important-limits}

The inspected naming scheme was based on test information and a run seed. It was not proven globally unique across independent runs with matching inputs. A preemptive recursive cleanup could therefore be unsafe if ownership of the selected location is uncertain. This review does not endorse copying that naming or deletion procedure unchanged.

Changing the current directory is process-global. The patch can isolate separate processes while still being unsuitable for concurrently running threads in one process. A disposable directory created through a uniqueness-preserving operating-system API, explicit path injection, or a per-test subprocess may be preferable.

Evidence supports the diagnosed shared-root collision and the observed setup/teardown correction. No parallel execution or crash-recovery test was performed here.
