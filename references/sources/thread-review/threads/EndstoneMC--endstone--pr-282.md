<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:282"],"source_type":"public","date":"2025-10-25","topics":["ffi","testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-282-feat-use-py-smartholder-for-passing-objects-between-c-and-python-safely"></a>
# EndstoneMC/endstone #282: feat: use `py::smart_holder` for passing objects between c++ and python safely {#endstonemc-endstone-282-feat-use-py-smartholder-for-passing-objects-between-c-and-python-safely}

Source: https://github.com/EndstoneMC/endstone/pull/282

## Review scope and state {#review-scope-and-state}

- Thread author: wu-vincent; state at review: closed; merged: True.
- Evidence: Public PR and patch reviewed statically (14 additions, 19 deletions, matching recorded metadata); no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Wu's merged 7-file smart_holder patch is fully read. Python trampoline classes for CommandExecutor, Plugin and MapRenderer gain trampoline_self_life_support and bindings replace shared_ptr holders with py::smart_holder. Several prior keep_alive policies on get_command, map retrieval/creation and add_renderer are removed; supported API list adds 0.11, Ruff addsF checks, and an inline native map-manager connector definition becomes a declaration. The title supplies the intent of safe cross-language object transfer, but no specific lifetime regression test or review discussion exists. This is targeted holder/trampoline adoption, not a universal fix for borrowed Player/ItemType wrappers or permission to drop all keep_alive policies elsewhere.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/pull/282
