<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:296"],"source_type":"public","date":"2025-11-12","topics":["testing","build","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-296-feature-access-to-the-unique-member-permissions-inside-of-the-escape-menu"></a>
# EndstoneMC/endstone #296: [feature] Access to the unique member permissions inside of the escape menu {#endstonemc-endstone-296-feature-access-to-the-unique-member-permissions-inside-of-the-escape-menu}

Source: https://github.com/EndstoneMC/endstone/issues/296

## Evidence and attribution {#evidence-and-attribution}

Primary author: PrimeStrat. Created 2025-11-12T02:34:36Z; recorded state closed; merged not applicable.

## Problem and constraints {#problem-and-constraints}

PrimeStrat wanted direct access to the escape-menu member abilities (build, place, containers, commands, teleport) to avoid repeated event interception and to fix a teleport operation that permission nodes did not enable. A command-preprocess override was considered less clean; these abilities were distinguished from attributes.

## Resolution and authored reasoning {#resolution-and-authored-reasoning}

wu-vincent later linked #513 and supplied typed Ability examples. All eight menu abilities are enforced by the server, not merely client presentation. Endstone lowers vanilla command permission levels so its own nodes decide access, but TeleportCommand separately reads the Teleport ability inside its body; permission-node bypass therefore cannot fix the underlying check. Effective reads can differ from set base values: spectator NO_CLIP stays true. Bedrock re-derives the eight abilities on join for server-managed permissions, so reapply in PlayerJoinEvent for persistence.

## Boundaries and reusable decision {#boundaries-and-reusable-decision}

Setting OPERATOR_COMMANDS is not making someone an operator: visitor/member/operator permission level is coupled bidirectionally to abilities and requires separate work. Use a server-enforced ability abstraction rather than per-event imitation, while distinguishing stored value, effective value, and login reset policy. This thread reports the #513 implementation; its full code review is recorded separately.

## Additional source and attachment inspection {#additional-source-and-attachment-inspection}

The attached menu image was inspected. It visibly separates Build (No), Mine, Use doors and switches, Open containers, Attack players, Attack mobs (Yes), Operator Commands and Use Teleport (No). This grounds the requested per-ability granularity; a screenshot alone does not show the server enforcement path.

## Code and verification boundary {#code-and-verification-boundary}

No code inspection required for the narrow discussion finding; no implementation claim independently verified. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

Source and available attachment links are listed under Traceability; the separate acquisition and inspection ledger is not included in this distribution. A screenshot corroborates only visible content, not runtime causality.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/296
- https://github.com/EndstoneMC/endstone/issues/296#issuecomment-3735828397
- https://github.com/EndstoneMC/endstone/issues/296#issuecomment-5387913902
- https://github.com/user-attachments/assets/77b588ed-a02d-430d-84b4-3e1d72796d5a
