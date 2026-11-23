<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:371"],"source_type":"public","date":"2026-04-08","topics":["ffi","testing","api","review","refactoring"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-371-refactor-replace-dimension-type-enum-with-dimensionid-identifier"></a>
# EndstoneMC/endstone #371: refactor: replace Dimension::Type enum with DimensionId identifier {#endstonemc-endstone-371-refactor-replace-dimension-type-enum-with-dimensionid-identifier}

Source: https://github.com/EndstoneMC/endstone/pull/371

## Evidence and attribution {#evidence-and-attribution}

Primary author: wu-vincent. Created 2026-04-08T20:43:33Z; recorded state closed; merged True.

## Problem, design and limits {#problem-design-and-limits}

A fixed Overworld/Nether/TheEnd/Custom enum cannot identify arbitrary addon dimensions. Replace it with namespaced DimensionId=Identifier<Dimension>, change Level::getDimension's parameter and update bindings/stubs/callers. Preserve predefined constants and expose id/translation_key. Windows/Linux build and compatibility checks are an unchecked plan, not test results.

## Direct patch findings {#direct-patch-findings}

Patch removes Dimension::Type/name in favor of typed namespaced ID and translation key, replaces case-insensitive/TheEnd-special name lookup with exact ID matching, and migrates actor/location/map/particle/event callers to native DimensionType where appropriate. Vanilla runtime0/1/2 map to constants; custom fallback still constructs ID from native name with explicit TODO for1.26.20, so arbitrary addon support is preparation rather than completed runtime mapping. getLocalizationKey formats dimension.dimensionName{runtime_id}. Python tests cover constants, lookup/unknownNone, IDs/nonemptytranslation, level identity and list membership; they do not cover custom dimensions, case migration, map dimension writes or cross-dimension actions. Existing stub still annotates get_dimension as nonnullable despite actual None. Much actor-header churn is formatting only.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (25391 characters; SHA-256 850bcdbb650926104d2d8313e94c1c43cf8c6ab66be60ebbb314df3ee9d18722), head 0b47207f779a678b38b61ce5cff9812222726b0a. Scope is this supplied patch, not all linked implementation history. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/371
