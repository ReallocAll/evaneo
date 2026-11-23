<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:335"],"source_type":"public","date":"2026-02-15","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-335-log-files-are-automatically-archived-is-this-the-intended-behavior"></a>
# EndstoneMC/endstone #335: Log files are automatically archived. Is this the intended behavior? {#endstonemc-endstone-335-log-files-are-automatically-archived-is-this-the-intended-behavior}

Source: https://github.com/EndstoneMC/endstone/issues/335

## Evidence and attribution {#evidence-and-attribution}

Primary author: Arduinonk. Created 2026-02-15T06:29:09Z; recorded state closed; merged not applicable.

## Clarification and decision {#clarification-and-decision}

Arduinonk wanted a switch for gzip log archives and confused them with a changelog entry suppressing verbose BDS logs. wu-vincent separated content filtering from retention/storage: active logs/latest.log rotates daily or on restart into dated YYYY-MM-DD-N.log.gz, preserving history while reducing disk use. He cited Java/Paper/Spigot Log4j2 behavior as the precedent, kept compression as the default without an existing disable switch, and invited a separate retention/compression feature request.

This is an explicit default choice and boundary explanation, not evidence that log filtering causes compression. External Java-server behavior is cited by the maintainer, not independently audited in this review.

## Additional source and attachment inspection {#additional-source-and-attachment-inspection}

The file-list image contains large dated uncompressed .log files alongside small .log.gz archives with numbered suffixes. It verifies coexistence and naming, not that every old file was compressed or a particular retention duration.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Source and available attachment links are listed under Traceability; the separate acquisition and inspection ledger is not included in this distribution. A screenshot corroborates only visible content, not runtime causality.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/335
- https://github.com/EndstoneMC/endstone/issues/335#issuecomment-3903459313
- https://github.com/EndstoneMC/endstone/issues/335#issuecomment-4017604954
- https://github.com/EndstoneMC/endstone/issues/335#issuecomment-4604917667
- https://github.com/user-attachments/assets/7b7dd1ec-d70e-4f88-a47d-77ff029b54b8
