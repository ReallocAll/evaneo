<!-- retrieval: {"source_ids":["public:context-commit:f14d05ee5a77e0deb7f23e7376330a3bbcac6d65"],"source_type":"public","topics":["build","performance","api"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="contributor-context-pr-5"></a>
# Contributor context: PR #5 {#contributor-context-pr-5}

Source: https://github.com/wu-vincent/scikit-build-core-conan/commit/f14d05ee5a77e0deb7f23e7376330a3bbcac6d65

Author: mijoku. Integrated SHA: f14d05ee5a77e0deb7f23e7376330a3bbcac6d65. PR head: ac3be727dc359b280b2b49d74e7d7e921f5b6fd8. Identical parent and complete tree verified locally; not counted as a second independent implementation.

Replaces CLI install/JSON decoding with explicit Conan API remotes, lockfile, profiles, graph analysis, binary installation, consumer generation and lockfile update. Returns root node and accesses root.conanfile.generators_folder. Both profiles receive host settings/options/config; profile.detect no longer persists by itself. Vincent called the API approach cleaner; neither that acknowledgement nor merge proves CLI semantic equivalence. Later 99994 fixes persistence and PR #6 fixes context separation. README corrects output_folder to output-folder.

[Captured discussion analysis](../../../thread-review/threads/dossiers/wu-vincent__scikit-build-core-conan-5.md). Full guarded diff. Full message and all 104 diff lines read. No tests/runtime execution or measured success. These are collaborator changes, not wu-vincent authorship; acceptance/release decisions are separate evidence.
