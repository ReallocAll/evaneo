<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:413"],"source_type":"public","date":"2026-06-07","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-413-getplayer-misleadingly-returns-player-when-it-returns-player-none"></a>
# EndstoneMC/endstone #413: `get_player` misleadingly returns `Player` when it returns `Player | None` {#endstonemc-endstone-413-getplayer-misleadingly-returns-player-when-it-returns-player-none}

Source: https://github.com/EndstoneMC/endstone/issues/413

## Evidence and attribution {#evidence-and-attribution}

Primary author: niko-at-chalupa. Created 2026-06-07T09:05:31Z; recorded state closed; merged not applicable.

## Problem and change of abstraction level {#problem-and-change-of-abstraction-level}

niko-at-chalupa showed get_player(name/UUID) actually returns None for absence, but generated stubs promise Player, so IDEs mark necessary guards unreachable and consumers might assume exceptions instead. The initial suggestion was patching two annotations.

wu-vincent later reports source-level NotNull<T>/Nullable<T> from commit 524f52a70, making Server::getPlayer return Nullable<Player> so generated stubs naturally yield Player|None. The same correction covers get_plugin_command and scoreboard. It targets develop/next release, not 0.11.x.

Reusable rule: model nullability where the API is defined rather than accumulating post-generation string patches. #454 records the rejected/intermediate stub-only route. This thread does not contain the type-wrapper implementation or test output.

## Additional source and attachment inspection {#additional-source-and-attachment-inspection}

The image shows an IDE greying the `if in_game_player is None: continue` guard after a value annotated Player is returned by get_player. This is the concrete tooling symptom; it is not itself a runtime proof of None-return behavior.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Source and available attachment links are listed under Traceability; the separate acquisition and inspection ledger is not included in this distribution. A screenshot corroborates only visible content, not runtime causality.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/413
- https://github.com/EndstoneMC/endstone/issues/413#issuecomment-4937216254
- https://github.com/EndstoneMC/endstone/issues/413#issuecomment-5231413053
- https://github.com/user-attachments/assets/84e93e7e-3aa1-4cb1-aed0-7f034d7e59fc
