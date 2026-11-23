<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:426"],"source_type":"public","date":"2026-07-08","topics":["testing","diagnosis","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-426-custom-map-renderers-are-not-called-when-the-map-has-no-decorations"></a>
# EndstoneMC/endstone #426: Custom map renderers are not called when the map has no decorations {#endstonemc-endstone-426-custom-map-renderers-are-not-called-when-the-map-has-no-decorations}

Source: https://github.com/EndstoneMC/endstone/issues/426

## Evidence and attribution {#evidence-and-attribution}

Primary author: MoriyamaDiamond. Created 2026-07-08T16:17:25Z; recorded state closed; merged not applicable.

## Diagnosis and corrected generalization {#diagnosis-and-corrected-generalization}

MoriyamaDiamond found send_map creates a texture packet with 128×128 pixels but no native decorations, and patchPacket returned on pixels.empty() OR decorations.empty(). The reporter disclosed AI-assisted diagnosis and personally verified removing the decorations test made custom rendering work.

wu-vincent's final commit uses AND instead, so it skips only when both payload categories are absent. Rendering occurs before branching; pixel bounds checks/copying occur only when pixels exist, preserving decoration-only processing as well. This is broader and more correct than merely ignoring every packet without pixels.

Static code confirms the split; no regression tests are in the commit. Reusable rule: optional orthogonal packet sections must not be treated as jointly required. Test texture-only, decoration-only, both and neither, with bounds checks scoped to the section they protect.

## Code and verification boundary {#code-and-verification-boundary}

Inspected full f8b13b1a30b63653a39ccaf503ea5fb6bcfeaa05, including the unrelated crash-handler-location fix carried in the same commit. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/426
- https://github.com/EndstoneMC/endstone/issues/426#issuecomment-4936348134
