<!-- retrieval: {"source_ids":["public:commit:ab19c2c1b411fa0beff180efca17f9362fbb5cf8","public:commit:7c81e47de73d350aceb29af5222dd002a81aae82"],"source_type":"public","date":"2024-07-09","topics":["testing","build","performance","api","review","selection"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="socialify-route-removal-is-not-complete-subsystem-removal"></a>
# Socialify: route removal is not complete subsystem removal {#socialify-route-removal-is-not-complete-subsystem-removal}

## Actual change and inherited context {#actual-change-and-inherited-context}

[ab19c2](42-ab19c2c1b411fa0beff180efca17f9362fbb5cf8.md) makes the image route always delegate to SVG by removing its bot/user-agent PNG branch and PNG import. The isBot import remains unused. [7c81e4](43-7c81e47de73d350aceb29af5222dd002a81aae82.md) then removes the entire PNG route. Both target messages were read in full; they give no reason beyond removal and no test or deployment claim.

The deleted PNG route parses query parameters, renders a PNG, returns image/png with CDN-cache headers, and serializes exceptions into JSON responses. Those preexisting operations were removed, not originally implemented by the target. Exact-tree contextual reads establish that the SVG route retains the analogous SVG response/error wrapper, and common/renderPNG.tsx still imports Resvg WASM and renders SVG into a 1280-wide PNG. Thus removing the route does not establish renderer/dependency elimination.

The targeted local mirror initially lacked these unchanged contextual blobs. Public raw-file retrieval succeeded, and both downloaded bytes were verified against the Git blob IDs recorded in the selected commit tree. These are inherited context reads; no algorithms are attributed to these commits. Deeper SVG rendering internals and package dependency reachability were not audited.

## Consequences and limits {#consequences-and-limits}

Static consequence: bot consumers that used the mixed image route now receive SVG instead of PNG, and the dedicated PNG route file is absent. The record does not explain whether this was for hosting compatibility, performance, dependency size or another reason. Do not invent a favorable optimization story, characterize it as behavior-preserving, or extrapolate a preference for deleting features. There is no captured associated review thread in the established corpus, so tradeoffs and user acceptance remain unknown.

For a similar task, inspect both selection routing and route existence, check unused imports, and separately determine whether renderers/assets/dependencies remain reachable. Review caller/media-format compatibility before claiming safe removal. Those are general reviewer questions, not tests executed here. No Next.js build, linter, screenshot/render comparison, crawler test or deployment was run. This case is most useful as a boundary audit and attribution guard rather than a recommended implementation pattern.
