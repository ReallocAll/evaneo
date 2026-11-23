<!-- retrieval: {"source_ids":["public:thread:JakubAndrysek/MkDoxy:103"],"source_type":"public","date":"2024-05-01","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="jakubandrysek-mkdoxy-103-fix-executable-not-found-when-the-current-working-directory-cwd-is-set-to-config-file-path"></a>
# JakubAndrysek/MkDoxy #103: Fix executable not found when the current working directory (cwd) is set to config file path {#jakubandrysek-mkdoxy-103-fix-executable-not-found-when-the-current-working-directory-cwd-is-set-to-config-file-path}

Source: https://github.com/JakubAndrysek/MkDoxy/pull/103

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2024-05-01T08:04:28Z; recorded state closed; merged True.

Wu fixes #75's config-file/cwd failure. Maintainer thanks; Sourcery's generic all-green claims provide no specific test evidence. Review actual path transformation before interpreting the title as an executable-search change.

## Direct patch findings {#direct-patch-findings}

Removes runPath parameter/member and all caller construction from dirname(config.config_file_path), and omits cwd in Popen. For relative mkdocs.yml dirname is empty string, so this avoids invalid cwd=""; it does not add executable-search logic. Also stops changing cwd for nonempty config directories, a relative-path behavioral boundary not tested in patch.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (1819 characters; SHA-256 9126a9189403cff4435b5a9239c2585dbf8d06c2163daa3f3f56a3eeebb267ad), head 92b8bd006c7510aa68cede43f93a7bc3f284d4eb. This covers the supplied PR patch, not unrelated commits or historical intermediate revisions. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/JakubAndrysek/MkDoxy/pull/103
- https://github.com/JakubAndrysek/MkDoxy/pull/103#issuecomment-2088197983
- https://github.com/JakubAndrysek/MkDoxy/pull/103#pullrequestreview-2033198391
