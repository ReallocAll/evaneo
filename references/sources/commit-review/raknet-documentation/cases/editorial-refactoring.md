<!-- retrieval: {"source_ids":["public:commit:01518f1d77f9a06a76042d4760ddbe977c773089","public:commit:076213f71493e840dc71ce87ef7662b8e1e36b5a","public:commit:08a3147faba92f823da810f33925cd60e4a93a37","public:commit:1b4af017155a9393226c0a314f7e51fa8b0ba3b9","public:commit:25e275ddc5ff67914b2ae3a9e84efa73e28addd0","public:commit:4704e4a97c10b776756ba0d746b9f49e44a63bb9","public:commit:4e7570cfd193c0192c9bd073e9592308a1680a1c","public:commit:81af283838a548411193960fc216e765e8adaa07","public:commit:9fb1c02bb570f8ad57ef177dd11f045f8d606712","public:commit:aa5646684c90d901327baec06a6812e2870a8916"],"source_type":"public","date":"2026-02-24..2026-02-27","topics":["testing","build","api","documentation","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="rd02-separate-presentation-refactoring-from-semantic-api-edits"></a>
# Separate presentation refactoring from semantic/API edits {#rd02-separate-presentation-refactoring-from-semantic-api-edits}

## Evidence chain {#evidence-chain}

Commit 015 removes redundant sidebar separators. Commit 029 shortens branding and registers shared Steps/Tabs/Accordions/TypeTable components. Commit 030 restructures79 pages with descriptions, tables, callouts, steps/tabs and FAQ accordions, removes TypeTable and changes the GitHub source target. Commit 031 describes code-name typography but also repairs sample syntax in70 files. Commit 032 changes two theme colors. Read the corresponding per-SHA dossiers for source identities and complete exceptions.

## Mechanism {#mechanism}

The documentation moves page titles into frontmatter and uses component structure to express procedures, alternatives, warnings and FAQ entries. This is a concrete authoring system rather than a list of arbitrary wording preferences. New descriptions improve page labeling and search/metadata inputs. Markdown tables replace the briefly registered TypeTable component, showing a local revision rather than evidence of a permanent component preference.

Formatting and semantic changes are mixed. Changes to display wrappers or code fences are often mechanical. However, fixing16 bytes to16 bits, API identifier spellings, a missing parenthesis or a wrong example class can alter readers' understanding or whether copied code compiles. Deleting authentication scope caveats and API counterpart names changes the material available to a reader. Those residuals were reviewed instead of being hidden behind a docs/formatting classification.

## Concrete API/example boundary {#concrete-api-example-boundary}

The Startup example is a useful counterexample to assuming that syntax cleanup modernizes a sample. Commit 031 closes its conditional and normalizes formatting, but the final snippet still passes an integer30 where the current signature expects SocketDescriptor*. It passes an array address in the next slot and uses a truthy success test although RAKNET_STARTED is enum zero. The displayed maxConnections type also differs from the native declaration. These are static source-contract mismatches; no compiler output was produced.

Other030 example fixes include Write call punctuation, Soldier/GetNetworkID spelling/syntax, Rackspace XML fragments, NatTypeDetectionClient, RakVoice outbuffer and ReplicaManager3's participation-method spelling. SWIG directions repair paths/placeholders/spellings but retain legacy build assumptions. The compiler guide adds static-library/source-build alternatives yet still names paths and old tools absent from the modernized layout.

The TwoWayAuthentication omission deserves special care: the old prose explicitly separated password verification from enabling/disabling features or blocking other messages during a challenge. Its removal does not establish that access-control behavior changed. Documentation reviewers should retain the boundary or verify the implementation independently. The examined documentation commits do not themselves implement a new authentication policy.

## Proven reduction without losing meaningful work {#proven-reduction-without-losing-meaningful-work}

At 030,55/79 fenced-body byte strings are unchanged and61/79 are equal under the stated lexer normalization. At 031,30/70 and56/70 are unchanged respectively. Fourteen031 and eighteen 030 non-equal lexical streams were read. A stricter core proof identifies15 entire031 pages differing only in backticks/whitespace. This allows mechanical credit where justified without treating every file as a distinct technical insight.

The seven-line sidebar deletion and eight-line color addition were read fully and receive concise dispositions. Neither requires an invented philosophical principle. No rendered color contrast, UX improvement, compilation, full API-table accuracy or security outcome was tested.

## Attribution and applicability {#attribution-and-applicability}

Claude Opus 4.6 trailers are present on 030/031, absent on 015/029/032 with assistance otherwise unknown. Inherited tutorial logic and old performance claims remain upstream material. Explicit commit messages support the listed authoring intentions; stronger claims about the author's universal style or validation habits would exceed the evidence.

Use for documentation-heavy refactors, API reference tables, example consistency, agent-assisted code review, or requests to distinguish mechanical diffs from meaningful semantic edits. A good review unit is the coherent transformation plus all residual exceptions, not one generic rule per changed file.
