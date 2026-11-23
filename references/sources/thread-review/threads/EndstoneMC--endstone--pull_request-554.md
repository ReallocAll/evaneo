<!-- retrieval: {"source_ids":["public:thread:EndstoneMC/endstone:554"],"source_type":"public","date":"2026-10-17","topics":["testing","review"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="endstonemc-endstone-554-fix-command-avoid-ambiguous-ban-and-ban-ip-command-grammar"></a>
# EndstoneMC/endstone #554: fix(command): avoid ambiguous ban and ban-ip command grammar {#endstonemc-endstone-554-fix-command-avoid-ambiguous-ban-and-ban-ip-command-grammar}

Source: https://github.com/EndstoneMC/endstone/pull/554

## Evidence and attribution {#evidence-and-attribution}

Primary author: FETXU. Created 2026-10-17T03:06:38Z; recorded state closed; merged True.

FETXU isolates a Windows development-client command-parser hang on clean LinuxEndstone: optional message grammar duplicates epsilon, and making only reasons required exposes a second string-versus-selector target ambiguity. Packet captures isolate changes; reverting only DLL restores assertion. Initial fix offers one string target and optional string reason, removing selectors and requiring quotes for multiword reasons.237C++ tests and console/live dev-client checks are reported; Python suites and retail-client qualification are not run.
Wu preserves single-target overload but keeps reason as message and globally registers message arguments as required, following vanilla /kick whose empty message still works. This avoids quotes while removing redundant optional grammar. Wu requests a dev-client rerun; no confirming reply is captured. Tests of Endstone usage parsing do not validate Minecraft client parsing. Separate allow-cheats=false tab behavior is explicitly outside this patch; #509's future API does not fix current built-ins by itself.

## Direct patch findings {#direct-patch-findings}

Final code globally sets message parameter is_optional=false after grammar symbol creation; ban/ban-ip each have one string target and keep optional message declaration. Python parameterized tests cover no/single/multiword reasons with finally cleanup, but no C++parser testcase remains in final captured diff. Live dev-client retest of maintainer revision absent.

## Code and verification boundary {#code-and-verification-boundary}

Inspected every hunk of captured PR diff (3536 characters; SHA-256 6480b40772e643d3abb0d5df5a174a622f65cd60f43494afa7f050fc1d701892), head 7aa4e81432830a13d2c9c4604871ffd9a80fbc08. This covers the supplied PR patch, not unrelated commits or historical intermediate revisions. No upstream code was executed and no tests were run in this review. Runtime assertions are source-reported unless explicitly identified as static code findings.

## Traceability {#traceability}


- https://github.com/EndstoneMC/endstone/pull/554
- https://github.com/EndstoneMC/endstone/pull/554#issuecomment-6243144964
