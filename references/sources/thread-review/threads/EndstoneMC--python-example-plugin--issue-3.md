<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/python-example-plugin:3"],"source_type":"public","date":"2025-11-17","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-python-example-plugin-3-method-does-not-exist"></a>
# EndstoneMC/python-example-plugin #3: method does not exist {#endstonemc-python-example-plugin-3-method-does-not-exist}

Source: https://github.com/EndstoneMC/python-example-plugin/issues/3

## Evidence and attribution {#evidence-and-attribution}

Primary author: MipaSenpai. Created 2025-11-17T07:52:40Z; recorded state closed; merged not applicable.

Example plugin's as_player call is obsolete. Wu recommends isinstance(sender, Player) or ConsoleCommandSender rather than checking names, and promises example update. Type identity is the useful decision; no linked update verified.

## Additional source and attachment inspection {#additional-source-and-attachment-inspection}

The supplied search image shows as_player yielding “No matching documents.” This corroborates missing documentation, but the obsolete API conclusion rests on the maintainer reply rather than search absence alone.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Source and available attachment links are listed under Traceability; the separate acquisition and inspection ledger is not included in this distribution. A screenshot corroborates only visible content, not runtime causality.

## Traceability {#traceability}


- https://github.com/EndstoneMC/python-example-plugin/issues/3
- https://github.com/EndstoneMC/python-example-plugin/issues/3#issuecomment-3540693639
- https://github.com/user-attachments/assets/3a2594c5-1090-4b8f-a0df-921dede0379f
