<!-- retrieval: {"source_ids":["public:commit:044cb128d138e3d51422c128e1e3b1b64384e202","public:commit:070be6ee8ebc960c52361a981e556a17088c883a","public:commit:0cbb0b4b6b0e5963ea1f1179936a78cd489aa022","public:commit:0fdd2497e61ccfcffe67bf1292ef946fd659ce28","public:commit:1d45e10bfa5266ba0799130a9daa2c815a6c13e6","public:commit:488c9688300fc47890b747711c93d3a70cd3d56f","public:commit:4b978694f00dc5e50d97ca4eebda6cbfea8cc8bf","public:commit:68f566436258abecc75db3f0521cdbef6909f79b","public:commit:70fe10660887abc218fc7166a66956e566747e8a","public:commit:a018919d80f8fe0849e8c78bb85f232ab193b482","public:commit:a18015c4df2ad9c3e8edfb91ae59c66b67c6e121","public:commit:c3a4289ea1d09e5eb57d8424d175e1767d3c5259","public:commit:dae929b39bcf4c544cbe6e5e1d972e06fc80092c","public:commit:de0aa81266af0d11032c87b4b50bf1c3703dfbae","public:commit:fd3aad5c9f814513bed63d93c6561c011f81cdd9"],"source_type":"public","date":"2025-03-14..2025-03-18","topics":["lifetime","ffi","testing","build","api","documentation","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="papi02-api-migrations-must-close-every-binding-callback-and-command-path"></a>
# API migrations must close every binding, callback and command path {#papi02-api-migrations-must-close-every-binding-callback-and-command-path}

## Causal context and collaborators {#causal-context-and-collaborators}

Vincent supplies the service shell; daoge_cmd's `82c584a2` supplies the substantive Python scanner and registry, query functions, callback registration, and an attempted list overload. The overload is initially expressed as two Python methods with the same name, which does not provide runtime overload dispatch. `4cdee542` fixes C++ pybind overload selection, but `85bb72c3` removes the list overload, explicitly describing it as not making much sense. This removal is the collaborator's choice, not evidence of the commit author’s preference.

The collaborator also adds default processors (`189f493a`), command metadata/execution (`8428eba9`), renames modules (`b2199996`, `a12a2f5c`), and fixes permissions/usages and documentation later. Their 17 ancestral context commits are separately represented. All meaningful deltas were read; the clean merge carries already-read changes rather than a new independent implementation.

## The migration sequence {#the-migration-sequence}

`c3a4289e` reformats the now-populated implementation. Four changed Python ASTs compare equal; C++ layouts were inspected as whitespace-only. Large diff size is therefore not evidence Vincent invented the parser/default registry.

`4b978694` changes the translation API to plural `setPlaceholders` / `set_placeholders` and introduces `Processor = function<string(Player const&, string)>`, replacing the earlier optional-reference signature. It changes the C++ header, trampoline, Python concrete method, stub and native example together. Python example and command paths remain old until `a18015c4` and `de0aa812`; this chain is evidence that finding a symbol in one binding file is insufficient to close an API rename.

`dae929b3` separates compiled `_papi` from concrete `papi.py` and updates CMake/import paths. The macro-generated initialization symbol still says `pypapi` until `68f56643`, which also adds `pybind11/functional.h` needed for callback conversion and expands type stubs. A commit described as updating stubs therefore contains functional repairs. `de0aa812` also passes the owning plugin into the concrete service constructor, which needs it to register default providers and obtain server data.

`044cb128` implements the pattern accessor as a C++ string rather than a Python regex object. Python-facing properties route through underscored virtual hook names. This keeps the boundary representable in both languages while preserving Python property syntax. It does not prove the scanner and regex recognize precisely the same language.

## Nullable inputs and output contracts: unresolved edges {#nullable-inputs-and-output-contracts-unresolved-edges}

`a018919d` deliberately makes `Player` nullable: C++ changes references to pointers; Python signatures permit `None`; header explicitly permits `nullptr`. The final C++ trampoline still forwards `*player`. Reading the final source confirms the contradiction, not merely an intermediate diff. A C++ call with null therefore has an unsafe dereference path before reaching a Python override. This is static code reasoning, not a crash reproduced here.

Python defaults such as coordinates/name/ping access player fields directly. A null player can reasonably serve server/date-only placeholders, but player-specific placeholders do not have an explicit null fallback. Several default callbacks return numbers or UUID-like objects while the scanner ends with `''.join(builder)` and does not normalize non-string replacements. Sidebar independently centralizes `str` conversion; this PAPI path does not. A robust integration needs tests for null on each processor class and non-string return values, rather than accepting the annotation as enforcement.

Registration first tries the supplied identifier, then `plugin.name:identifier`, and rejects a second collision with a warning. This fallback is visible in the implementation; Vincent adds explicit namespace commentary. The registry retains only the callable keyed by the eventual name, without an unregister-by-plugin API. An owner-disposal policy and clear returned registered identifier would need separate design. Do not claim this history solved them.

## Parser preservation and review/merge behavior {#parser-preservation-and-review-merge-behavior}

The scanner consumes brace-delimited identifiers, optional pipe-separated parameters, and preserves unknown or failed (`None`) replacements. Initially it reconstructs pipe input with underscores on failure. Vincent's `070be6ee` explicitly questions delimiter consistency. daoge_cmd's `90754bcc` changes all three reconstruction branches to pipe. Merge `0cbb0b4b` imports this fix while resolving a papi.py conflict in favor of the nullable signature and retained docstring. Parent diffs and remerge output establish that exact resolution. Later collaborator docs correct the remaining colon-based description.

The other target merge, `fd3aad5c`, brings in `usage`→`usages` and has no independent conflict-resolution delta. The permission key/list repair is in collaborator `e977ec10`. These identities matter: a merge title cannot transfer the authorship of parser or command fixes.

## Command parsing {#command-parsing}

`70fe1066` corrects the text argument type to message. `0fdd2497` simplifies literal-subcommand declaration. `488c9688` moves player before the greedy message argument, adds `me`, `--null`, and named-player handling, and returns true for handled user errors. This ordering is a concrete parser-integration change. It asserts exactly three parsed arguments rather than gracefully rejecting wrong arity. Because metadata still declares a player-typed target, whether `me`/`--null` are accepted by the exact Endstone parser must be validated; no execution proves it here.

## Outcomes and task use {#outcomes-and-task-use}

Observed repairs: actual trampoline arguments, initialization symbol, constructor context, symbol-name call sites, delimiter preservation, metadata keys and message ordering. Outstanding static risks: nullable bridge dereference, non-string callbacks, player-specific null handling, callback-owner lifecycle, unchecked service lookup and command special-target acceptance. This case is useful for ABI/binding reviews and “rename is complete” checks, not as an unqualified finished PAPI recipe.

Suggested acceptance matrix, not tests performed: native→Python and Python→native calls; present/missing provider; ordinary/null player; empty/malformed/unknown placeholders; duplicate identifiers and owner unload; callback exception/non-string output; every documented command path; compiled wheel import and stubs matching runtime symbols.

## Sources {#sources}

[Per-commit source index](../repositories/papi-source-index.md) links the 46 selected revisions. The collaborator and merge-resolution analysis above is based on historical source review; local patch and remerge exports are not bundled. The [nullable bridge commit](https://github.com/EndstoneMC/papi/commit/a018919d80f8fe0849e8c78bb85f232ab193b482) is public.
