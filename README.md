# Evaneo

Evaneo is an [Agent Skill](https://agentskills.io/) for grounded engineering decisions. It helps coding agents reuse existing mechanisms, weigh safeguard and test costs, distinguish evidence from assumptions, and favor maintainable solutions. It uses plain Markdown; no MCP server, CLI, or case index is required.

## Installation

Clone the repository and place the `evaneo` directory in the Skill location supported by your agent, or use your agent's Skill installer:

```sh
git clone https://github.com/ReallocAll/evaneo.git
```

Keep `SKILL.md`, `references/`, and `scripts/` together. Installation paths and invocation syntax depend on the agent.

## Usage

Ask your agent to apply Evaneo when designing, implementing, debugging, or reviewing a consequential software change. For example:

> Use Evaneo to review this diff for observable regressions, unnecessary safeguards, and unsupported claims. Recommend no change if the existing behavior is sound.

The guidance lives in [SKILL.md](SKILL.md). Consult [reference cases](references/) only when relevant. For optional offline case lookup, use [`scripts/retrieve.py`](scripts/retrieve.py) (Python 3.9+); reading the Markdown cases directly requires no script.

## Contributing

Propose improvements to [SKILL.md](SKILL.md) or add concrete counterexamples under [references/](references/). Issues and focused pull requests are welcome.

## License

Original material is licensed under [MIT](LICENSE). Third-party attribution remains with its sources, including the bundled [Endstone Test MIT notice](references/sources/commit-review/endstone-test-all/NOTICE-endstone-test.txt).
