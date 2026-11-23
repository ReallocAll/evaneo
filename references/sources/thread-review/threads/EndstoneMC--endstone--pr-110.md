<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:110"],"source_type":"public","date":"2024-12-17","topics":["review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-110-adjust-plugin-loading-logic-fix-98"></a>
# EndstoneMC/endstone #110: Adjust plugin loading logic, fix #98 {#endstonemc-endstone-110-adjust-plugin-loading-logic-fix-98}

Source: https://github.com/EndstoneMC/endstone/pull/110

## Review scope and state {#review-scope-and-state}

- Thread author: engsr6982; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (9 additions, 5 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

engsr6982’s body claims index/while traversal plus #98 fixes, but the captured final patch does not contain that traversal change. It adds per-loader regex filters before loadPlugin and changes an inner plugin binding from const reference to pointer. The outer loader range loop remains. wu thanks the author; Codecov reports 0% patch coverage. The follow-on snapshot fix in #98 (6ed7faf) must be treated separately, not retroactively credited to this patch. The nested break leaves the outer loader loop running, so single-loader exclusivity is not proven by the apparent intent. Complete 9-add/5-delete patch read.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/110
- https://github.com/EndstoneMC/endstone/pull/110#issuecomment-2552367712
- https://github.com/EndstoneMC/endstone/pull/110#issuecomment-2552367962
