<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:170"],"source_type":"public","date":"2025-04-06","topics":["concurrency","review","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-170-bug-player-playsound-doesn-t-work"></a>
# EndstoneMC/endstone #170: [bug] Player.play_sound() doesn't work {#endstonemc-endstone-170-bug-player-playsound-doesn-t-work}

Source: https://github.com/EndstoneMC/endstone/issues/170

## Review scope and state {#review-scope-and-state}

- Thread author: Cdm2883; state at review: closed; merged: not applicable.
- Evidence: The public issue and code/reproduction described below were reviewed statically; no code execution or tests were performed.
- Limits: Source snapshot only; no independent runtime verification.

## Engineering reading and attribution {#engineering-reading-and-attribution}

Cdm2883 compares Player.play_sound with a working playsound command; Wu confirms a bug and a recent fix. The full matching mirror commit bd8354471e3fae29867415240af2bd5ed2b4d1e1 explicitly fixes 170: NetworkBlockPosition constructors multiply coordinates by eight, playSound casts location coordinates to int before assigning that network position, and Python bindings/stubs gain default volume/pitch 1.0. The implementation confirms a wire-coordinate representation issue; it does not implement sub-block precision (integer conversion happens first) or prove every negative/fractional coordinate behaves identically to the vanilla command. No reporter retest or executed validation appears.


## Source index {#source-index}

- https://github.com/EndstoneMC/endstone/issues/170
- https://github.com/EndstoneMC/endstone/issues/170#issuecomment-2781711448
