<!-- retrieval: {"source_ids":[],"source_type":"public","date":"2026-10-30","topics":["testing","maintainability","complexity","google","llvm","go","cpython","linux","postgresql","sqlite"],"limitations":"Derived from linked official primary guidance; individual organizations have distinct contexts. Published SQLite size is from 2023. No tests executed."} -->
# Mature-project official testing guidance: reliable contracts at sustainable cost {#case}

## Google: useful tests and long-term maintenance {#google}

[Google code-review guidance](https://google.github.io/eng-practices/review/reviewer/looking-for.html) asks whether a test would actually fail on broken code, whether it would become brittle under change, and whether the assertions are simple and useful; it explicitly treats tests as maintainable code and rejects unnecessary complexity in them. [Software Engineering at Google, Testing Overview](https://abseil.io/resources/swe-book/html/ch11.html) distinguishes execution from verified behavior, warns against using a single coverage number as a quality target, and selects test size by runtime resources and determinism. **Transfer:** choose a cheap, discriminating test with a real oracle. **Limit:** the book's contextual organizational test mixes are not targets for other repositories.

## LLVM: keep each regression input small {#llvm}

[LLVM Testing Infrastructure Guide](https://llvm.org/docs/TestingGuide.html) explicitly recommends removing unnecessary instructions, attributes and metadata from tests, running minimal relevant passes, adding cases to existing test files and avoiding fragile unnamed identifiers. [Developer Policy](https://llvm.org/docs/DeveloperPolicy.html) rejects committing a whole failing program where a reduced case will do, because it imposes ongoing testing costs, and separates large integration suites. **Transfer:** reduce the fixture while retaining its bug-triggering semantics; do not write a new generic reduction framework for an ordinary one-off test.

## Go: consolidate repetitive examples, not unrelated semantics {#go}

[Go Wiki — TableDrivenTests](https://go.dev/wiki/TableDrivenTests) recommends noticing copy-pasted cases and considering a table of input/expected-output pairs or a shared helper. The advice is about reducing repeated test logic; a table itself must remain legible and produce useful failure messages. **Transfer:** replace many near-identical cases with data, not complex scenario DSLs.

## CPython: simple isolated tests and shared support helpers {#cpython}

[CPython Development Guide](https://devguide.python.org/testing/run-write-tests/) expects tests to be fast, repeatable, isolated and as simple as possible; contributors are encouraged to reuse `test.support` utilities for platform behavior, resources and cleanup. **Transfer:** use existing fixtures rather than adding platform-handling machinery in each test. **Limit:** interpreter-level platform support has broader obligations than a typical plugin.

## Linux kernel: select the layer that sees the real contract {#kernel}

[Kernel Testing Guide](https://docs.kernel.org/dev-tools/testing-overview.html) distinguishes internal, fine-grained KUnit from userspace interface and whole-feature kselftest. [Kselftest documentation](https://docs.kernel.org/dev-tools/kselftest.html) also describes selectively running relevant targets. **Transfer:** a mock-only unit test is not a substitute for the actual userspace ABI and vice versa. Use the existing testing layer that naturally witnesses the risk.

## PostgreSQL: distinguish real failures from unstable artifacts {#postgresql}

[PostgreSQL regression testing](https://www.postgresql.org/docs/current/regress.html) uses expected result comparisons; [Test Evaluation](https://www.postgresql.org/docs/current/regress-evaluation.html) documents output differences due to locale, time zone, floating point and unordered rows. It explicitly warns that forcing `ORDER BY` onto every query can make the test suite *less* useful by missing unordered-plan behavior. **Transfer:** make oracles robust to differences the contract allows, without sanitizing away the behavior being tested.

## SQLite: scale can be necessary, not a universal budget {#sqlite}

[How SQLite Is Tested](https://www.sqlite.org/testing.html) reports that as of SQLite 3.42.0 in May 2023 its test code/scripts were approximately **590 times** its core C source size, with fault injection, crash recovery and extensive independent checks. This is a domain-specific example of extremely high assurance investment, not a number to copy. The published snapshot is historical; do not label it the current 2026 ratio. **Transfer:** data loss and corruption merit heavier oracles and fault testing. **Limit:** high assurance requirements and available budget differ radically between systems.

## Cross-project synthesis and limitation {#interpretation}

None of these projects prescribes a universal test-code percentage or count. Different systems deliberately choose different verification costs according to failure consequences. Maintainers should ask: what can plausibly go wrong, what observable oracle would catch it, what existing facility can verify it, and what ongoing maintenance does the proposed fixture impose? These are review questions, not another required test-management bureaucracy. Official guides document recommendations, **not** proof that every historical change in those projects obeyed them. No external suite or tool was executed here.
