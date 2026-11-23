<!-- retrieval: {"source_ids":["public:commit:3d12059418e224ead0c39783429f3f5b0e9c5a87","public:commit:4dd0773b386e001cdcbc69911f267db6419217f6","public:commit:ac5ed41b3ae13aa787ea429c58546f983c6d31a4","public:commit:b28e5bdd4d875d04c17787951fd755fe5dd5d098","public:commit:bdd604587ad6403068f1864680e18e87e665b88a","public:commit:df37128241d06418c1c4471d890ff7563c77fa13"],"source_type":"public","date":"2023-11-19..2025-10-16","topics":["testing","build","diagnosis","documentation","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="lanelet2x-upstream-integration-and-release-evidence-boundaries"></a>
# Lanelet2x: upstream integration and release evidence boundaries {#lanelet2x-upstream-integration-and-release-evidence-boundaries}

## Geocentric fix belongs upstream {#geocentric-fix-belongs-upstream}

bdd6045, titled “merge from upstream,” introduces a GeocentricProjector constructor with a non-default origin and a tutorial write/load test. The constructor avoids the generic IO handler's rejection of a default projector. It is tempting to attribute this numerical-looking change to the merge author because GitHub lists that author on the commit. That would be incorrect.

The relevant DAG side commit is `a41d75b4332eb74920ffd9b5a4c49b7160ff413c`, authored by Michał Antkiewicz, with message “Fix #324: exception thrown when using GeocentricProjector (#325).” Its patch can be inspected at the linked public commit. Both the Geocentric header and tutorial blobs in bdd6045 are exactly equal to that upstream commit. The blob comparison establishes source identity rather than independent authorship. Upstream public provenance is [the original commit](https://github.com/fzi-forschungszentrum-informatik/Lanelet2/commit/a41d75b4332eb74920ffd9b5a4c49b7160ff413c).

The contribution in this commit is integration into the standalone fork. Copying the complete upstream tutorial also reverses prior local formatting and explicit imports. This explains why the merge diff is larger than the original upstream fix. It does not imply the merge author designed the origin convention, numerical value, or test.

## Three different merge shapes {#three-different-merge-shapes}

- `3d12059418e224ead0c39783429f3f5b0e9c5a87` combines fork RPATH/staging work with a description correction. Both parent deltas and the merge base were examined.
- `df37128241d06418c1c4471d890ff7563c77fa13` has the same tree as its first parent bdd6045. Its second-parent diff is a 277748-byte cumulative presentation of already reviewed fork work against upstream. Tree equality and exact upstream-path identity establish that the merge introduces ancestry, not an independently authored implementation. The cumulative patch was extracted but was not falsely reported as a fresh literal read.
- `4dd0773b386e001cdcbc69911f267db6419217f6` combines Docker and upstream branches. Its first-parent raw patch SHA256 exactly matches bdd6045's already read patch; its second-parent patch matches ac5ed41's already read Docker patch. Those matching hashes support reusing prior reviews rather than attributing a new implementation to the merge.

This is efficient deduplication of proven content, not using “merge” as a reason to skip examination.

## Moved and generated material {#moved-and-generated-material}

The two debugger scripts relocated by b28e5bd retain their exact Git blob IDs. Their move is structurally verified; their contents do not become newly authored merely because a no-renames diff displays deletion plus addition. Later actual edits to the scripts were read as local deltas.

The ROS metapackage removal deletes a generated 808-line clang-tidy fixes file containing 88 diagnostic names/91 replacements and a 22-record CodeClimate JSON report. Schema/count/hash/deletion verification is recorded, without pretending each obsolete diagnostic was semantically studied. Removing stale tool output is a different contribution from fixing every underlying diagnostic. These reports have no independent originality credit for the fork.

## What a release commit establishes {#what-a-release-commit-establishes}

The release-labelled commits change metadata, workflow upload names, caching and classifiers. Cibuildwheel and OIDC publishing configuration demonstrate an intended release route. The README's availability statement and Docker quick-import command are author-reported usage, not observed success in this review. No package was installed, no tag pushed, no release published and no Docker image built.

The Docker rewrite shrinks a multi-stage ROS setup into Python3.11-slim, build-essential, pip/Conan installation and a shell command. It drops the old explicit non-root runtime-user setup and uses floating dependencies. Those are observable configuration changes, with tradeoffs in convenience, reproducibility and privilege. One deleted old Docker line is credential-guarded and remains opaque; its duplicated appearance in the later merge is not “recovered.”

## Reuse {#reuse}

For “what did this fork's maintainer actually contribute,” combine linked author identity, actual patch, upstream source, parent trees and blob equality. Use source authorship for algorithm credit and merge activity for integration credit. For “can I rely on this package on another platform,” demand installation/runtime evidence in addition to workflow text and badges. Do not substitute commit counts, added-line counts, paper citations or release labels for validated behavior.
