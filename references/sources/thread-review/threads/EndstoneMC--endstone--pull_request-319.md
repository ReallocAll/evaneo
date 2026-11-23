<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:319"],"source_type":"public","date":"2026-01-04","topics":["ffi","testing","api","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-319-feat-add-noclip-and-verticalflyspeed-to-the-player-api"></a>
# EndstoneMC/endstone #319: feat: Add noclip and verticalflyspeed to the Player API {#endstonemc-endstone-319-feat-add-noclip-and-verticalflyspeed-to-the-player-api}

Source: https://github.com/EndstoneMC/endstone/pull/319

## Evidence and attribution {#evidence-and-attribution}

Primary author: Nipitare. Created 2026-01-04T15:11:11Z; recorded state closed; merged False.

## Proposal and actual patch {#proposal-and-actual-patch}

Nipitare added explicit Player getter/setter pairs for vertical fly speed and noclip, backed by native AbilitiesIndex values and updateAbilities(), with Python properties. Static inspection finds the noclip property supplies Player::getNoClip as both getter and setter; it is not a correct setter binding in the proposed patch.

## Alternatives and decision sequence {#alternatives-and-decision-sequence}

wu-vincent first deferred changes to the next API version because released v0.10 public APIs should remain stable. Later he closed this unmerged PR in favor of #513: Bedrock has twenty abilities and #296 needs eight, so two pure virtual accessors per ability would yield forty methods. A keyed, type-carrying API requires three virtuals once and rejects mismatched C++ value types at compile time. He credited the feature choice: noclip and vertical speed are enforced by the move filter and flight-control system, not cosmetic client flags.

## Costs and reusable rule {#costs-and-reusable-rule}

Separate feature acceptance from API shape acceptance. Registry/key-based typed access can bound ABI surface growth while retaining compile-time correctness. Preserve contributor credit to Nipitare for the original abilities proposal; #513 is the replacement design, not evidence that this original accessor patch merged. No tests accompany this patch.

## Code and verification boundary {#code-and-verification-boundary}

Inspected the entire captured 3,450-character patch, including all four pure virtual additions, implementation, declarations and Python bindings. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/319
- https://github.com/EndstoneMC/endstone/pull/319#issuecomment-3772542968
- https://github.com/EndstoneMC/endstone/pull/319#issuecomment-5387916218
