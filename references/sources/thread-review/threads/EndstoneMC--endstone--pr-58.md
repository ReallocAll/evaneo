<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:58"],"source_type":"public","date":"2024-09-19","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-58-feat-devtool-add-biome-export-add-exportall-button"></a>
# EndstoneMC/endstone #58: feat[devtool]: add biome export, add exportAll Button {#endstonemc-endstone-58-feat-devtool-add-biome-export-add-exportall-button}

Source: https://github.com/EndstoneMC/endstone/pull/58

## Review scope and state {#review-scope-and-state}

- Thread author: CoolLoong; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (112 additions, 3 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

CoolLoong authors biome extraction/display and Export All; wu praises the code without detailed reasoning. The complete merged patch adds identifier→ID biome data, UI menu/window and JSON/NBT exports. Review observations matter: exportAll builds creative_items but passes block_palette to creative_items.nbt, a concrete mismatch visible in the patch; static lambdas capture base_path by reference, which may outlive the first call’s argument; Export All is not guarded by data!=nullptr although the JSON submenu is. These are static observations/risks in the historical submitted code, not proof of current defects. The right lesson is to inspect accepted code rather than infer correctness from praise, merge or Codecov’s report (7.46%, stale by four commits). Neither screenshot UI behavior nor tests were independently verified.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/58
- https://github.com/EndstoneMC/endstone/pull/58#issuecomment-2360743341
- https://github.com/EndstoneMC/endstone/pull/58#issuecomment-2360756791
- https://github.com/EndstoneMC/endstone/pull/58#issuecomment-2360767102
- https://github.com/EndstoneMC/endstone/pull/58#issuecomment-2362491629
- https://github.com/EndstoneMC/endstone/pull/58#issuecomment-2362497711
