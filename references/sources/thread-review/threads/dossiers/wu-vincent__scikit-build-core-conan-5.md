<!-- retrieval: {"source_ids":["public:thread:wu-vincent/scikit-build-core-conan:5"],"source_type":"public","date":"2024-12-13","topics":["concurrency","testing","build","performance","api","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="wu-vincent-scikit-build-core-conan-5-directly-call-conan-api-functions-instead-of-conan-cli"></a>
# wu-vincent/scikit-build-core-conan#5: Directly call conan-api functions instead of conan-cli {#wu-vincent-scikit-build-core-conan-5-directly-call-conan-api-functions-instead-of-conan-cli}

Source: https://github.com/wu-vincent/scikit-build-core-conan/pull/5

Thread state: closed; merged: True.

## Problem and constraints {#problem-and-constraints}
Replace invoking Conan’s CLI and parsing captured JSON stdout with direct Conan API calls during wheel builds.

## Reasoning, alternatives, and revision sequence {#reasoning-alternatives-and-revision-sequence}
mijoku authors the change; Vincent calls it cleaner and promises review, then merges. Contributor explains recreating the branch to remove unintended git-log information; those deleted branches are not sought. This change later regresses host/build profile semantics, explicitly corrected in #6.

## Implementation and attribution {#implementation-and-attribution}
Full two-file patch read. It replaces command argument construction, stdout redirection and JSON root-node extraction with remotes/lockfile/profile acquisition, graph loading and binary analysis, binary/consumer install, and lockfile update/save. Returns deps_graph.root and obtains generators_folder through root.conanfile. Profile detection switches to profiles.list/detect. README corrects output_folder to output-folder. The initial API version applies target build_type/settings/options/config equally to both host and build profiles, unlike prior CLI flags. It retains coupling to Conan’s install sequence despite removing serialization.

Diff evidence (patch inspected, not bundled): [pinned public three-dot comparison](https://github.com/wu-vincent/scikit-build-core-conan/compare/f0075aaa7cca0ee2d4ef48fcf4980b4633162f92...ac3be727dc359b280b2b49d74e7d7e921f5b6fd8). Declared changed files: 2.

## Verification, outcome, and remaining limits {#verification-outcome-and-remaining-limits}
Merged, no tests in patch. Review approval alone does not establish behavioral equivalence; #6 is a concrete counterexample. API result typing still says dict despite returning a node.

## Reusable decision and costs {#reusable-decision-and-costs}
Direct structured APIs remove fragile CLI output parsing but require faithfully reproducing semantic defaults and host/build separation; migration tests should compare dependency graphs, not merely successful invocation.

## Evidence coverage {#evidence-coverage}
No upstream source was executed.

Cited source links:
- [mijoku · 2024-12-13T21:39:14Z](https://github.com/wu-vincent/scikit-build-core-conan/pull/5#issuecomment-2542424166).
- [wu-vincent · 2024-12-14T16:13:01Z](https://github.com/wu-vincent/scikit-build-core-conan/pull/5#issuecomment-2543171002).
