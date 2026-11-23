<!-- retrieval: {"source_type":"judgment_synthesis","topics":["engineering-judgment","documentation","technical-writing","clarity","maintainability"],"limitations":"A synthesis of public writing guidance. Illustrative examples are anonymous, not allegations about any project; apply with judgment."} -->
# Write only what the reader needs {#overview}

## Decision rule {#rule}

Write for the reader's concrete task: explain the current behavior, interface, procedure, or decision. Keep a sentence only when removing it would cause a meaningful loss of information or a plausible reader mistake. Delete settled exclusions, repeated conclusions, filler introductions, and decorative summaries rather than rewriting them.

Prefer precise, familiar words and direct verbs. Remove empty modifiers, vague claims, and multiword phrases with simpler equivalents. Use one term consistently for one concept. Replace promotional claims with verifiable behavior or omit them.

For README, installation, and API documentation, put prerequisites, commands, inputs, outputs, and necessary failure conditions where the reader needs them. Keep examples runnable and placeholders explicit. Separate historical rationale from the current user path. Follow project conventions rather than forcing a universal template.

Conciseness is not the goal by itself: retain explanations required for correctness, ownership, security, compatibility, and meaningful tradeoffs. Do not delete a real warning merely to shorten the document.

## Anonymous examples {#examples}

- **Unrelated qualification:** “No additional isolation is currently required, so this is not listed as a problem.” → Delete when the reader requested only actual problems.
- **Filler:** “In order to successfully begin the installation process, first install the necessary dependencies.” → “Install the dependencies.”
- **Unsupported promotion:** “This cutting-edge architecture guarantees enterprise-grade reliability.” → State the verified guarantee and its conditions, or delete.
- **Template residue:** `git clone https://github.com/OWNER/REPO.git` → Substitute the actual repository URL before publishing.

## Reference guidance {#references}

- [GitHub Docs — Content guidelines](https://github.com/github/docs/blob/main/.github/instructions/content-guidelines.instructions.md): remove nonessential content and keep each article focused on the reader's purpose.
- [Google — Documentation Best Practices](https://google.github.io/styleguide/docguide/best_practices.html): maintain small, accurate documents; trim duplication and outdated material.
- [GitLab — Documentation language](https://docs.gitlab.com/development/documentation/styleguide/language/): use concise, direct, reader-oriented technical language.
- [Microsoft — Use simple words, concise sentences](https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences): choose clear verbs, avoid unnecessary modifiers and wordiness, and use terminology consistently.

## Applicability and limits {#limits}

Apply to substantive technical documentation, README, installation instructions, API references, and documentation review. These are editorial judgments, not a mandatory checklist or permission to remove required contract details.
