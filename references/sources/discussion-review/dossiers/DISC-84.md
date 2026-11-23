<!-- retrieval: {"source_ids":["public:discussion:EndstoneMC:84"],"source_type":"public","date":"2024-10-26..2024-11-28","topics":["lifetime","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="disc-84-callback-value-versus-deferred-callable"></a>

# DISC-84 — Callback value versus deferred callable {#disc-84-callback-value-versus-deferred-callable}

Evidence is limited to the cited public discussion and attributed replies; later edits, deleted material and independent runtime behavior are not verified.

Both registration sites in the image execute a function immediately and pass its result as on_click. The reporter says wrapping with a lambda solved immediate execution, and another participant explains the callable-versus-result distinction; the reporter confirms understanding. A later reply suggests instance state for additional arguments. A lambda in a loop also requires attention to late-bound variables; the discussion supplies no final repaired source or Endstone runtime test.

## Provenance {#provenance}

- [umarurize · 2024-10-26T11:03:36Z](https://github.com/orgs/EndstoneMC/discussions/84#discussion-7371706).
- [umarurize · 2024-10-26T11:57:22Z](https://github.com/orgs/EndstoneMC/discussions/84#discussioncomment-11059996).
- [xXLarryTFVWXx · 2024-11-03T12:51:57Z](https://github.com/orgs/EndstoneMC/discussions/84#discussioncomment-11134199).
- [umarurize · 2024-11-03T15:54:43Z](https://github.com/orgs/EndstoneMC/discussions/84#discussioncomment-11135118).
- [ye111566 · 2024-11-28T15:55:36Z](https://github.com/orgs/EndstoneMC/discussions/84#discussioncomment-11408102).

The attached source image was visually inspected. The image is research evidence, not a portable code dependency or runtime test.
