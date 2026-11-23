<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:423"],"source_type":"public","date":"2026-07-05","topics":["testing","review","selection","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-423-cannot-join-dedicated-server-using-docker-image-endstone-0-11-5"></a>
# EndstoneMC/endstone #423: Cannot join dedicated server using docker image endstone:0.11.5 {#endstonemc-endstone-423-cannot-join-dedicated-server-using-docker-image-endstone-0-11-5}

Source: https://github.com/EndstoneMC/endstone/issues/423

## Evidence and attribution {#evidence-and-attribution}

Primary author: RWRmrfrog. Created 2026-07-05T22:42:35Z; recorded state closed; merged not applicable.

## Symptom and competing hypotheses {#symptom-and-competing-hypotheses}

RWRmrfrog could not join Docker 0.11.5, with no connection log and eventual main-menu return; portable worked. evc24004 reproduced on Linux/Pterodactyl, captured a 33-byte unconnected pong without MCPE advertisement, and blamed a removed RakNet virtual. Their posted patch synthesizes an advertisement from live state, keeping plugin overrides but using level name as MOTD and Survival as default; they reported success across thirteen servers, independently confirmed by the original reporter.

## Maintainer investigation and reversal {#maintainer-investigation-and-reversal}

wu-vincent varied enable-lan-visibility on the exact Docker/BDS setup, showing the getter still returned complete data when enabled. He first rejected unconditional synthesis because it overrode administrators' hiding intent and recommended enabling the property. That did not solve every report. evc24004 identified level.dat LANBroadcast; DEVILENMO supplied vanilla version comparisons and an unresolved same-process next-day failure; pgrd1 linked #465.

The later maintainer matrix uses BDS 1.26.40.8 Linux, raw pings and roughly twenty configurations. Vanilla and Endstone both produce 33-byte pongs if the property is false or LANBroadcast=0, even with property true/absent. LANBroadcastIntent did not track results; MultiplayerGame reset to 1 on save. Default/nondefault ports and a busy 19132 did not explain the symptom. OPEN_CONNECTION_REQUEST_1/2 still received replies: client refusal to continue after advertisement loss differs from server handshake unavailability. Some early world-field values were inferred from shared ancestry rather than measured per run, explicitly disclosed. Longest observation was 90 seconds, so spontaneous next-day failure remained unexplained.

## Final code, tradeoff and limits {#final-code-tradeoff-and-limits}

Commit 03c70ae5b does not use the contributor's synthetic packet. It waits until level setup, checks a network handler with an empty server name, sets the configured server-name (fallback Endstone Server), and invokes native updateServerAnnouncement. It leaves world flags untouched. This restores both peers' advertisements and may reopen LAN discovery ports; maintainer reports two-server coexistence works even if one owns 19132/19133.

The final decision explicitly reverses the earlier priority: hidden servers are advertised because reachability now outweighs hiding. Preserve that disclosure and the contributor credit for packet captures and LANBroadcast narrowing. The crashpad libc++ error is unrelated to joining. Measurements constrain hypotheses but do not establish all possible causes; no runtime test was repeated here.

## Code and verification boundary {#code-and-verification-boundary}

Read all fifteen comments, posted contributor diff and full configuration matrix. Inspected complete final commit 03c70ae5b12e5182c2883019e193a71570a23cb2; upstream binaries/packet captures were not independently rerun. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/issues/423
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-4888124107
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-4888188721
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-4888250833
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-4888270772
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-4888519778
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-4888846929
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-4936946717
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-4940834695
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-4942740279
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-4949455232
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-4949683132
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-4949686775
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-5217682049
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-5218157649
- https://github.com/EndstoneMC/endstone/issues/423#issuecomment-5218632989
