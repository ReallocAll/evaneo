<!-- retrieval: {"source_ids":["public:external:nukkit-site"],"source_type":"public","topics":["api"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="external-nukkit-site"></a>

# external:nukkit-site {#external-nukkit-site}

Source: [Nukkit website](https://nukkit.org/).

The public page pairs Java Nukkit and Python Endstone plugin examples with FAQ content. It calls Endstone the creator's successor and distinguishes the community-maintained Cloudburst fork. Those comparative feature and maintenance claims are project marketing and were not independently audited here.

The examples map lifecycle methods, commands and event registration across Java Nukkit and Python Endstone. This is an API-familiarity demonstration, not proof that either is a drop-in migration. The Python example includes a `break` inside a `match` arm with no enclosing loop. A syntax-only compile of the example extracted from the linked public page reports `'break' outside loop` on example line 28. No imports or example code were executed. It is a concrete counterexample to trusting presentation snippets as executable recipes. Current installed API/version requirements still need checking before reuse.

No benchmark, plugin migration run, or third-party comparison was performed.
