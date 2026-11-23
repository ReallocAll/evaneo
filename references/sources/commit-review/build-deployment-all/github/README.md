<!-- retrieval: {"source_ids":["public:commit:05a1876eb5f78af03832cb1a9a70a89995898ff8","public:commit:0d0622659f188c1094203d11646c8343f703a315","public:commit:1dc242796ba4923448324847dcdc7e4a5cd041d6","public:commit:24782c48f08444801c4a7b2f59b6f8848b377db0","public:commit:76391843bce8dccd90d18e1ba5a1c50d872a2a79","public:commit:84f84ab60188e9d6753b74c784570c4fffcd50bf","public:commit:926701651f06ece09a5bf41ca7e3fbb62c212ce4","public:commit:9567b40b3caf16d7e57ff93367a81a712d02490b","public:commit:99f9bf0529dbdbe601b21b35123260962a637f48","public:commit:a5d940e1fa1614bf322f901005e5e3034d222a5e","public:commit:b2e27cec108b9d36ebb6b8cb28a305b9a9a4f25c","public:commit:b4c7770934d8991a545993ef8fbf21cf8e49eb27","public:commit:bd0b205f8df476048543d7069074914831dfe1e5","public:commit:e88a2e58fa68c773f4700ab1400efd13def37f0b","public:commit:e91f2074ab8bf2b807876eb135954d5cec683c42","public:commit:fc09a9c332b0e7a17e550161a12c09f71ccd8c63"],"source_type":"public","date":"2024-03-21..2026-10-12","topics":["performance","documentation","review","refactoring","networking"],"limitations":"Static source analysis. Reported tests and outcomes are not independently executed; read the case-specific limits and dated revisions."} -->
<a id="organization-documentation-entry-points-governance-and-claim-boundaries"></a>
# Organization documentation: entry points, governance and claim boundaries {#organization-documentation-entry-points-governance-and-claim-boundaries}

## Evolving audience contract {#evolving-audience-contract}
The organization repository begins with a banner, then moves the unchanged blob to GitHub's profile path. A landing-page rewrite supplies distinct routes for server users and contributors: quick start, templates, deployment and developer tooling. The next useful behavioral edit makes uvx the primary start command while retaining an install-and-launch pip fallback. This is a specific onboarding hierarchy, not evidence that the author avoids pip generally.

The ecosystem map expands beyond the core plugin framework: version translation, proxy, Node scripting, profiler and a protocol toolchain. Reordering the three named pillars and shortening the introduction show product-positioning work. The maps are useful discovery indexes, but repository descriptions cannot replace independent review of those implementations. In-development Endgate remains explicitly marked as such. Removing a project from a table is not evidence of deletion or abandonment.

## Project decision and contribution boundaries {#project-decision-and-contribution-boundaries}
The governance documents expressly separate day-to-day maintainer PR decisions from significant new APIs, breaking changes, repository and licensing decisions requiring the BDFL final call. This is a source for escalation design and reviewer authority, not authorization for an agent to mutate a repository. Contribution guidance says follow local patterns and run configured linters, with repository-specific guides taking precedence. Original-work and licensing assertions are historical organizational terms, not a performed legal or contributor-rights audit.

The license strategy explains different goals for core/plugins, templates/tools and infrastructure, then adds a commercial alternative for endgate. Conduct text credits Contributor Covenant 2.1. Security policy requests private reports with reproduction and affected version, with acknowledgement/assessment targets and best-effort remediation. Those targets are commitments in a document, not measured incident-response performance.

## Negative evidence and applicability {#negative-evidence-and-applicability}
The final TPS statement is merely a profile claim: over twice vanilla BDS. This source contains no workload, hardware, run count, spread or comparison methodology. Keep it as reported documentation, and use independently examined benchmark evidence for any performance conclusion. Small banner, table, relocation and funding commits receive complete structural identity/disposition but no inflated independent engineering lesson. No links to individual projects were treated as automatic proof of their contents; no external publication, licensing acceptance or policy changes were made.

## Complete per-SHA navigation {#complete-per-sha-navigation}

- [01 e88a2e58fa68 — Initial commit](dossiers/01-e88a2e58fa68c773f4700ab1400efd13def37f0b.md)
- [02 99f9bf0529db — Update README.md](dossiers/02-99f9bf0529dbdbe601b21b35123260962a637f48.md)
- [03 926701651f06 — Rename README.md to profile/README.md](dossiers/03-926701651f06ece09a5bf41ca7e3fbb62c212ce4.md)
- [04 84f84ab60188 — Rewrite org profile as a landing page for users and contributors](dossiers/04-84f84ab60188e9d6753b74c784570c4fffcd50bf.md)
- [05 24782c48f084 — Remove empty column from ecosystem table](dossiers/05-24782c48f08444801c4a7b2f59b6f8848b377db0.md)
- [06 a5d940e1fa16 — Use uvx endstone as primary quick start, pip as fallback](dossiers/06-a5d940e1fa1614bf322f901005e5e3034d222a5e.md)
- [07 e91f2074ab8b — Add org-wide governance files for LTD preparation](dossiers/07-e91f2074ab8bf2b807876eb135954d5cec683c42.md)
- [08 b4c7770934d8 — Document endgate dual-licensing (AGPL-3.0 + commercial)](dossiers/08-b4c7770934d8991a545993ef8fbf21cf8e49eb27.md)
- [09 b2e27cec108b — Add GOVERNANCE.md establishing BDFL model](dossiers/09-b2e27cec108b9d36ebb6b8cb28a305b9a9a4f25c.md)
- [10 05a1876eb5f7 — docs: refresh the ecosystem tables on the profile README](dossiers/10-05a1876eb5f78af03832cb1a9a70a89995898ff8.md)
- [11 0d0622659f18 — docs: add bedrock-protocol to the contributor repos](dossiers/11-0d0622659f188c1094203d11646c8343f703a315.md)
- [12 76391843bce8 — docs: lead the ecosystem table with the three pillars](dossiers/12-76391843bce8dccd90d18e1ba5a1c50d872a2a79.md)
- [13 bd0b205f8df4 — docs: describe Endstone as an ecosystem, not just a plugin framework](dossiers/13-bd0b205f8df476048543d7069074914831dfe1e5.md)
- [14 1dc242796ba4 — docs: tighten the intro to two lines](dossiers/14-1dc242796ba4923448324847dcdc7e4a5cd041d6.md)
- [15 fc09a9c332b0 — chore: add org-level funding config](dossiers/15-fc09a9c332b0e7a17e550161a12c09f71ccd8c63.md)
- [16 9567b40b3caf — docs(profile): mention Endstone's performance](dossiers/16-9567b40b3caf16d7e57ff93367a81a712d02490b.md)
