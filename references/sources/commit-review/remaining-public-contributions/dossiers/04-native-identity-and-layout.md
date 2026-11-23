<!-- retrieval: {"source_ids":["public:commit:2fdbcfffbe3cb675d11aa01b2397b25ec9a7171d","public:commit:d0ae611a283e23bf9b8b5d90104bf9a4965dc2cb"],"source_type":"public","date":"2024-05-08..2024-08-07","topics":["ffi","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="native-declarations-tiny-edits-with-semantic-meaning"></a>
# Native declarations: tiny edits with semantic meaning {#native-declarations-tiny-edits-with-semantic-meaning}

## Enum identity {#enum-identity}

[2fdbcfff](40-2fdbcfffbe3cb675d11aa01b2397b25ec9a7171d.md) inserts Shulker at numeric value 0x34 and shifts SurfaceTypeTotal/Any to 0x35/0x36. The commit explicitly says MaterialType is outdated and identifies StringFromMaterialType as the reference. A `chore` label does not make numeric interop identity mechanical. A missing enum member can also make later sentinel values wrong.

The [captured PR #1529](https://github.com/LiteLDev/LeviLamina/pull/1529) has a contributor checklist and approval. These are reported validation, not test logs or independent binary reconstruction. A local search of that exact target source tree did not find the named StringFromMaterialType definition. The native reference is therefore a source-author rationale that this review cannot independently confirm; no executable/disassembly was acquired or run. Do not claim exact ABI conformance from a merged header.

## Layout completeness without invented size changes {#layout-completeness-without-invented-size-changes}

[d0ae611a](41-d0ae611a283e23bf9b8b5d90104bf9a4965dc2cb.md) adds `bool chaining` to CommandRegistry::Overload. The surrounding declaration annotates versionOffset at 0x28, chaining at 0x2C, and paramsSymbol at 0x30; a native MCAPI constructor is declared below. The useful observation is a field inserted within a preexisting annotated gap. There is no source evidence that paramsSymbol moves, or that the whole structure grows. Describing every missing field as a total-size fix would overstate this patch.

The change contains no offset assertion, sizeof assertion, test, binary provenance or explanation beyond the missing-field title. No matching captured PR/issue context was found in the established thread inventory. This missing causal context is retained. The remaining 938-line header was not fully audited: the contextual read is exactly lines 175–244, in addition to the full target diff/message.

## Practical retrieval {#practical-retrieval}

Use for reverse-engineered/native-boundary declaration reviews: compare explicit ordinal values and sentinels, examine offsets and padding separately from size, identify the authoritative native reference, and require version-specific evidence before making ABI claims. These checks are reviewer-derived transfer questions from two bounded contributions, not a claim that the author always follows a complete ABI-validation process. The surrounding native framework and game types are upstream code; the target receives credit only for the two corrections. No compilation, runtime validation or native binary testing occurred.
